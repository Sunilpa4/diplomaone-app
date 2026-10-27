"""DI03000031 RDBMS Unit 1 – query programs (Oracle SQL) with real output from sql_runner."""
from sql_content import QE
from sql_seed import STUDENT, STUDENT_DDL

P = []

# ------------------------------------------------------------------ DDL
P.append(QE("q1_1", "Create a table and view its structure (CREATE, DESC)", """
CREATE TABLE student (
  rollno NUMBER(3) PRIMARY KEY,
  name   VARCHAR2(15) NOT NULL,
  branch VARCHAR2(5),
  city   VARCHAR2(10),
  marks  NUMBER(3)
);

DESC student
""", """
<p><b>CREATE TABLE</b> defines a new table: its name, each column's name and data type, and optional constraints.</p>
<ul><li><code>NUMBER(3)</code> holds whole numbers of up to 3 digits; <code>VARCHAR2(15)</code> holds text of up to 15 characters.</li>
<li><code>PRIMARY KEY</code> makes <code>rollno</code> unique and not null, so it shows <b>NOT NULL</b> in DESC.</li>
<li><b>DESC</b> (DESCRIBE) is a SQL*Plus command that shows column names, the Null? flag and the data types. It reads the data dictionary.</li></ul>
<p>DESC is not an SQL statement, so it does not need a semicolon.</p>
""", setup=""))

P.append(QE("q1_2", "Table using different Oracle data types", """
CREATE TABLE employee (
  emp_id   NUMBER(4),
  emp_name VARCHAR2(20),
  gender   CHAR(1),
  salary   NUMBER(8,2),
  join_dt  DATE,
  resume   CLOB
);

DESC employee
""", """
<ul><li><code>CHAR(1)</code>: fixed length. 'M' is stored as exactly 1 character (blank-padded if shorter).</li>
<li><code>NUMBER(8,2)</code>: precision 8 and scale 2, so 6 digits before the decimal point and 2 after (max 999999.99).</li>
<li><code>DATE</code>: stores the date and time (century, year, month, day, hour, minute, second).</li>
<li><code>CLOB</code>: a large text object (up to GBs), e.g. a resume or description.</li></ul>
<p>No constraints are given, so every column is nullable (the Null? column is empty).</p>
""", setup=""))

P.append(QE("q1_3", "ALTER TABLE: add new columns and modify a column", """
ALTER TABLE student ADD (
  email VARCHAR2(30),
  phone NUMBER(10)
);

ALTER TABLE student
  MODIFY (city VARCHAR2(20));

DESC student
""", """
<ul><li><b>ADD</b> appends new columns at the end of the table. Existing rows get NULL in the new columns.</li>
<li><b>MODIFY</b> changes a column's data type or size. Here <code>city</code> grows from VARCHAR2(10) to VARCHAR2(20).</li>
<li>Decreasing a size or changing a type is allowed only if the existing data fits (or the column is empty).</li></ul>
""", setup=STUDENT_DDL))

P.append(QE("q1_4", "ALTER TABLE: drop and rename a column, rename the table", """
ALTER TABLE student DROP COLUMN city;

ALTER TABLE student
  RENAME COLUMN marks TO total;

RENAME student TO stud;

DESC stud
""", """
<ul><li><code>DROP COLUMN</code> removes the column and all its data permanently.</li>
<li><code>RENAME COLUMN old TO new</code> changes only the column name; the data stays.</li>
<li><code>RENAME old TO new</code> renames the table itself. <code>ALTER TABLE student RENAME TO stud;</code> does the same.</li></ul>
""", setup=STUDENT_DDL))

P.append(QE("q1_5", "TRUNCATE vs DROP", """
SELECT COUNT(*) FROM student;

TRUNCATE TABLE student;

SELECT * FROM student;

DESC student

DROP TABLE student;

SELECT * FROM student;
""", """
<ul><li><b>TRUNCATE</b> deletes <b>all rows</b> but keeps the table structure, so DESC still works and SELECT says "no rows selected".</li>
<li><b>DROP</b> removes the rows <b>and</b> the structure. After that, the table does not exist: ORA-00942.</li>
<li>Both are DDL: they auto-commit and cannot be undone with ROLLBACK. (Oracle 10g+ keeps dropped tables in the Recycle Bin: <code>FLASHBACK TABLE student TO BEFORE DROP;</code>)</li></ul>
""", setup=STUDENT))

# ------------------------------------------------------------------ DML
P.append(QE("q1_6", "INSERT rows: all columns, selected columns, NULL", """
INSERT INTO student VALUES
(1, 'Aarav Patel', 'CE', 'Surat', 82);

INSERT INTO student (rollno, name, branch)
VALUES (2, 'Diya Shah', 'IT');

INSERT INTO student
VALUES (3, 'Karan Mehta', 'CE', NULL, 67);

SELECT * FROM student;
""", """
<ul><li>Form 1: values for <b>all</b> columns, in the same order as the table.</li>
<li>Form 2: a column list. The missing columns (<code>city</code>, <code>marks</code>) get NULL.</li>
<li>Form 3: <code>NULL</code> written explicitly.</li>
<li>Text and date values go in single quotes; numbers do not.</li></ul>
<p>NULL means "unknown / not given". It shows as a blank in the output.</p>
""", setup=STUDENT_DDL))

P.append(QE("q1_7", "Insert many rows with substitution variables (&)", """
INSERT INTO student VALUES
(&rollno, '&name', '&branch',
 '&city', &marks);
""", """
<p>In SQL*Plus, <code>&amp;name</code> is a <b>substitution variable</b>. SQL*Plus asks for each value at run time, so one INSERT can be reused for many rows.</p>
<ul><li>After the first row, type <code>/</code> and press Enter to run the same INSERT again for the next row.</li>
<li>Text variables are written inside quotes (<code>'&amp;name'</code>), so the user does not have to type the quotes.</li>
<li>The <code>old</code>/<code>new</code> lines show the statement before and after substitution (turn them off with <code>SET VERIFY OFF</code>).</li></ul>
""", out="""Enter value for rollno: 6
Enter value for name: Meera Iyer
Enter value for branch: IT
Enter value for city: Navsari
Enter value for marks: 88
old   2: (&rollno, '&name', '&branch',
new   2: (6, 'Meera Iyer', 'IT',
old   3:  '&city', &marks)
new   3:  'Navsari', 88)

1 row created.

SQL> /
Enter value for rollno: 7
Enter value for name: Jay Trivedi
Enter value for branch: CE
Enter value for city: Anand
Enter value for marks: 79
old   2: (&rollno, '&name', '&branch',
new   2: (7, 'Jay Trivedi', 'CE',
old   3:  '&city', &marks)
new   3:  'Anand', 79)

1 row created."""))

P.append(QE("q1_8", "UPDATE rows (with and without WHERE)", """
UPDATE student
SET marks = marks + 5
WHERE branch = 'CE';

UPDATE student
SET city = 'Ahmedabad', marks = 95
WHERE rollno = 2;

SELECT rollno, name, city, marks
FROM student;
""", """
<ul><li>UPDATE changes values in existing rows. <code>WHERE</code> chooses which rows are changed.</li>
<li>The first UPDATE adds 5 marks to every CE student (3 rows). An expression can use the old value (<code>marks + 5</code>).</li>
<li>Several columns can be set at once, separated by commas.</li>
<li><b>Without WHERE, all rows are updated.</b> Always check the WHERE clause first.</li></ul>
""", setup=STUDENT))

P.append(QE("q1_9", "DELETE rows", """
DELETE FROM student
WHERE marks < 60;

DELETE FROM student
WHERE city = 'Mumbai';

SELECT rollno, name, marks
FROM student;
""", """
<ul><li>DELETE removes whole rows that satisfy the WHERE condition (Rohan, 58 marks).</li>
<li>If no row matches, Oracle reports <b>0 rows deleted</b>. This is not an error.</li>
<li><code>DELETE FROM student;</code> without WHERE deletes every row, but unlike TRUNCATE it can be rolled back because DELETE is DML.</li></ul>
""", setup=STUDENT))

P.append(QE("q1_10", "Copy a table (CREATE TABLE ... AS SELECT, INSERT ... SELECT)", """
CREATE TABLE ce_student AS
SELECT rollno, name, marks
FROM student
WHERE branch = 'CE';

SELECT * FROM ce_student;

INSERT INTO ce_student
SELECT rollno, name, marks
FROM student
WHERE branch = 'IT';

SELECT * FROM ce_student;
""", """
<ul><li><b>CREATE TABLE ... AS SELECT</b> (CTAS) creates a new table with the columns of the query and copies the selected rows.</li>
<li><b>INSERT INTO ... SELECT</b> copies rows from a query into an existing table (no VALUES keyword).</li>
<li>To copy only the structure, use a condition that is always false: <code>CREATE TABLE t2 AS SELECT * FROM student WHERE 1 = 2;</code></li></ul>
""", setup=STUDENT))

# ------------------------------------------------------------------ DQL
P.append(QE("q1_11", "SELECT columns, column alias and expression", """
SELECT name, marks,
       marks * 100 / 150 AS percent,
       marks + 10 "New Marks"
FROM student;
""", """
<ul><li>SELECT picks columns; FROM names the table.</li>
<li>An <b>expression</b> such as <code>marks * 100 / 150</code> is calculated for every row. It does not change the table.</li>
<li><b>Column alias</b>: <code>AS percent</code> gives a heading (shown in capitals). With double quotes, <code>"New Marks"</code> keeps its case and spaces.</li></ul>
""", setup=STUDENT))

P.append(QE("q1_12", "WHERE clause with relational and logical operators", """
SELECT rollno, name, marks
FROM student
WHERE branch = 'CE' AND marks >= 60;

SELECT name, city
FROM student
WHERE city = 'Surat' OR marks > 90;

SELECT name FROM student
WHERE NOT branch = 'CE';
""", """
<ul><li>WHERE filters rows. Only rows where the condition is TRUE are shown.</li>
<li><code>AND</code>: both conditions must be true. <code>OR</code>: at least one must be true. <code>NOT</code>: reverses the condition.</li>
<li>Text comparison is <b>case-sensitive</b>: <code>'Surat'</code> and <code>'SURAT'</code> are different.</li></ul>
""", setup=STUDENT))

P.append(QE("q1_13", "DISTINCT – remove duplicate values", """
SELECT branch FROM student;

SELECT DISTINCT branch FROM student;

SELECT DISTINCT branch, city
FROM student;
""", """
<ul><li>Without DISTINCT, the value 'CE' appears once for every CE student.</li>
<li><b>DISTINCT</b> shows each value only once.</li>
<li>With more than one column, DISTINCT removes rows whose <b>combination</b> is repeated. Here every (branch, city) pair is different, so all 5 rows stay.</li></ul>
""", setup=STUDENT))

# ------------------------------------------------------------------ DCL
P.append(QE("q1_14", "DCL: create user and role, GRANT and REVOKE", """
CREATE USER ravi IDENTIFIED BY ravi123;

GRANT CREATE SESSION TO ravi;

GRANT SELECT, INSERT ON student
TO ravi;

CREATE ROLE clerk_role;

GRANT SELECT, UPDATE ON student
TO clerk_role;

GRANT clerk_role TO ravi;

REVOKE INSERT ON student FROM ravi;

GRANT SELECT ON student TO meena
WITH GRANT OPTION;
""", """
<ul><li><code>CREATE USER</code> makes a new account (run as DBA/SYSTEM). <code>CREATE SESSION</code> is the system privilege needed to log in.</li>
<li><b>Object privileges</b> (SELECT, INSERT, UPDATE, DELETE) are given on a particular table with <code>GRANT ... ON table TO user</code>.</li>
<li>A <b>role</b> is a named group of privileges. Granting the role gives all of them at once, which makes management easy.</li>
<li><code>REVOKE</code> takes a privilege back. Ravi can still SELECT and UPDATE (through the role) but can no longer INSERT.</li>
<li><code>WITH GRANT OPTION</code> lets Meena grant SELECT to other users.</li></ul>
<p>Ravi now uses the table as <code>SELECT * FROM scott.student;</code> (owner.table).</p>
""", setup=STUDENT))

# ------------------------------------------------------------------ TCL
P.append(QE("q1_15", "COMMIT and ROLLBACK", """
INSERT INTO student VALUES
(6, 'Meera Iyer', 'IT', 'Navsari', 88);

COMMIT;

DELETE FROM student
WHERE branch = 'CE';

SELECT COUNT(*) FROM student;

ROLLBACK;

SELECT COUNT(*) FROM student;
""", """
<ul><li>INSERT, UPDATE and DELETE are first kept in a <b>transaction</b> and are not yet permanent.</li>
<li><b>COMMIT</b> makes them permanent and ends the transaction. Meera's row is now saved.</li>
<li>The DELETE removes 3 CE rows (count becomes 3), but <b>ROLLBACK</b> undoes everything after the last COMMIT, so the count is 6 again.</li>
<li>A normal exit from SQL*Plus commits; a crash or abnormal exit rolls back.</li></ul>
""", setup=STUDENT))

P.append(QE("q1_16", "SAVEPOINT and ROLLBACK TO SAVEPOINT", """
INSERT INTO student VALUES
(6, 'Meera Iyer', 'IT', 'Navsari', 88);
SAVEPOINT a;

UPDATE student SET marks = marks + 5
WHERE branch = 'CE';
SAVEPOINT b;

DELETE FROM student WHERE rollno = 5;

ROLLBACK TO b;

SELECT rollno, marks FROM student;

ROLLBACK TO a;

SELECT rollno, marks FROM student;

COMMIT;
""", """
<ul><li>A <b>SAVEPOINT</b> marks a point inside a transaction.</li>
<li><code>ROLLBACK TO b</code> undoes only the work done after <code>b</code>: the DELETE. Roll no. 5 is back, and the +5 update stays.</li>
<li><code>ROLLBACK TO a</code> undoes the UPDATE too, so the marks return to their original values. The INSERT of roll no. 6 (before <code>a</code>) stays.</li>
<li><code>COMMIT</code> saves what remains (the new row 6) and erases all savepoints.</li></ul>
""", setup=STUDENT))

P.append(QE("q1_17", "DDL causes an automatic COMMIT", """
INSERT INTO student VALUES
(6, 'Meera Iyer', 'IT', 'Navsari', 88);

CREATE TABLE log_t (id NUMBER);

ROLLBACK;

SELECT COUNT(*) FROM student;
""", """
<p>In Oracle, every DDL statement (CREATE, ALTER, DROP, TRUNCATE, RENAME) and DCL statement (GRANT, REVOKE) <b>commits the current transaction automatically</b>, before and after it runs.</p>
<p>So the INSERT was committed by <code>CREATE TABLE</code>, and the later ROLLBACK has nothing to undo: the count is still 6.</p>
""", setup=STUDENT))

PROGRAMS = P
