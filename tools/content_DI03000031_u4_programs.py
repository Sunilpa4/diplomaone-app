"""DI03000031 RDBMS Unit 4 – constraints, views, synonyms, sequences, indexes (practicals 11-13). Real output from OraSim2."""
from sql_content import QE
from sql_seed import SCOTT

P = []

# ------------------------------------------------------------------ 4.1 domain integrity
P.append(QE("q4_1", "NOT NULL constraint", """
CREATE TABLE customer (
  cid   NUMBER(4),
  cname VARCHAR2(20) NOT NULL,
  city  VARCHAR2(15)
        CONSTRAINT nn_city NOT NULL,
  phone VARCHAR2(10)
);

INSERT INTO customer
VALUES (1, 'Mehta Stores', 'Surat', NULL);

INSERT INTO customer
VALUES (2, NULL, 'Anand', '9876543210');

INSERT INTO customer (cid, cname)
VALUES (3, 'Shah Traders');

DESC customer
""", """
<ul><li><b>NOT NULL</b> means the column must always have a value. It can only be defined at <b>column level</b>.</li>
<li>CNAME has an unnamed NOT NULL (Oracle gives it a SYS_C name); CITY has a named constraint <code>nn_city</code>.</li>
<li>PHONE has no constraint, so NULL is accepted in the first insert.</li>
<li>The second and third inserts fail with <b>ORA-01400</b>, because CNAME and CITY are left NULL.</li>
<li>DESC shows NOT NULL in the Null? column.</li></ul>
""", setup=""))

P.append(QE("q4_2", "CHECK constraint (column and table level)", """
CREATE TABLE student4 (
  roll   NUMBER(3),
  name   VARCHAR2(15),
  gender CHAR(1)
         CHECK (gender IN ('M', 'F')),
  age    NUMBER(2)
         CONSTRAINT ck_age
         CHECK (age BETWEEN 15 AND 30),
  min_m  NUMBER(3),
  marks  NUMBER(3),
  CONSTRAINT ck_marks
    CHECK (marks >= 0 AND marks <= 100)
);

INSERT INTO student4
VALUES (1, 'Aarav', 'M', 18, 35, 82);

INSERT INTO student4
VALUES (2, 'Diya', 'X', 17, 35, 91);

INSERT INTO student4
VALUES (3, 'Karan', 'M', 12, 35, 67);

INSERT INTO student4
VALUES (4, 'Isha', 'F', 19, 35, 120);
""", """
<ul><li><b>CHECK</b> allows only values for which the condition is TRUE (or NULL).</li>
<li>Gender 'X' violates the unnamed check (SYS_C name), age 12 violates <code>ck_age</code>, and marks 120 violates the table-level check <code>ck_marks</code>. Each gives <b>ORA-02290</b>.</li>
<li>Naming constraints (ck_age, ck_marks) makes error messages easy to understand.</li>
<li>A CHECK condition cannot use SYSDATE, sub-queries or other rows.</li></ul>
""", setup=""))

# ------------------------------------------------------------------ entity integrity
P.append(QE("q4_3", "UNIQUE constraint", """
CREATE TABLE users4 (
  uid4  NUMBER(3),
  email VARCHAR2(25)
        CONSTRAINT uq_email UNIQUE,
  phone VARCHAR2(10),
  CONSTRAINT uq_phone UNIQUE (phone)
);

INSERT INTO users4
VALUES (1, 'a@mail.com', '9800000001');
INSERT INTO users4
VALUES (2, 'a@mail.com', '9800000002');
INSERT INTO users4
VALUES (3, NULL, '9800000003');
INSERT INTO users4
VALUES (4, NULL, NULL);

SELECT * FROM users4 ORDER BY uid4;
""", """
<ul><li><b>UNIQUE</b> does not allow duplicate values in the column: the repeated email gives <b>ORA-00001</b>.</li>
<li>UNIQUE <b>allows NULL</b>, and several rows may have NULL, because NULL is not equal to any value (rows 3 and 4).</li>
<li>A table may have <b>many</b> UNIQUE constraints (email and phone).</li></ul>
""", setup=""))

P.append(QE("q4_4", "PRIMARY KEY constraint", """
CREATE TABLE book (
  book_id NUMBER(4)
          CONSTRAINT pk_book PRIMARY KEY,
  title   VARCHAR2(25) NOT NULL,
  price   NUMBER(6, 2)
);

INSERT INTO book
VALUES (101, 'DBMS Concepts', 450);
INSERT INTO book
VALUES (101, 'Oracle SQL', 520);
INSERT INTO book
VALUES (NULL, 'PL/SQL Guide', 380);

DESC book
""", """
<ul><li><b>PRIMARY KEY = UNIQUE + NOT NULL</b>. It identifies every row uniquely.</li>
<li>The duplicate 101 gives <b>ORA-00001</b> (unique constraint PK_BOOK violated), and the NULL key gives <b>ORA-01400</b>.</li>
<li>A table can have only <b>one</b> primary key. DESC shows BOOK_ID as NOT NULL.</li></ul>
""", setup=""))

P.append(QE("q4_5", "Composite PRIMARY KEY (table level)", """
CREATE TABLE enroll4 (
  roll  NUMBER(3),
  cid   VARCHAR2(4),
  edate DATE DEFAULT SYSDATE,
  CONSTRAINT pk_enroll
    PRIMARY KEY (roll, cid)
);

INSERT INTO enroll4 (roll, cid)
VALUES (1, 'C1');
INSERT INTO enroll4 (roll, cid)
VALUES (1, 'C2');
INSERT INTO enroll4 (roll, cid)
VALUES (2, 'C1');
INSERT INTO enroll4 (roll, cid)
VALUES (1, 'C1');

SELECT * FROM enroll4 ORDER BY roll, cid;
""", """
<ul><li>A key on more than one column is a <b>composite key</b>; it must be defined at <b>table level</b>.</li>
<li>Roll 1 can join C1 and C2, and C1 can have rolls 1 and 2; only the <b>combination</b> (1, C1) must be unique, so the last insert fails.</li>
<li><code>DEFAULT SYSDATE</code> fills EDATE automatically when no value is given.</li></ul>
""", setup=""))

# ------------------------------------------------------------------ referential integrity
DEPT_SETUP = """
CREATE TABLE dept4 (
  deptno NUMBER(2) CONSTRAINT pk_dept4 PRIMARY KEY,
  dname  VARCHAR2(12)
);
INSERT INTO dept4 VALUES (10, 'ACCOUNTS');
INSERT INTO dept4 VALUES (20, 'RESEARCH');
INSERT INTO dept4 VALUES (30, 'SALES');
COMMIT;
"""

P.append(QE("q4_6", "FOREIGN KEY: parent and child tables", """
CREATE TABLE emp4 (
  empno  NUMBER(4) PRIMARY KEY,
  ename  VARCHAR2(10),
  deptno NUMBER(2)
         CONSTRAINT fk_emp4_dept
         REFERENCES dept4 (deptno)
);

INSERT INTO emp4 VALUES (1, 'AMIT', 20);
INSERT INTO emp4 VALUES (2, 'NEHA', 20);
INSERT INTO emp4 VALUES (3, 'RAVI', 50);
INSERT INTO emp4 VALUES (4, 'MEET', NULL);

DELETE FROM dept4 WHERE deptno = 20;
DELETE FROM dept4 WHERE deptno = 30;
DROP TABLE dept4;
""", """
<ul><li>DEPT4 is the <b>parent</b> (referenced) table and EMP4 is the <b>child</b> (referencing) table.</li>
<li>Department 50 does not exist, so the insert fails with <b>ORA-02291: parent key not found</b>. A NULL foreign key is allowed (MEET).</li>
<li>Department 20 has employees, so it cannot be deleted: <b>ORA-02292: child record found</b>. Department 30 has no employees, so it is deleted.</li>
<li>The parent table cannot be dropped while a foreign key refers to it (<b>ORA-02449</b>); use <code>DROP TABLE dept4 CASCADE CONSTRAINTS</code> or drop the child first.</li></ul>
""", setup=DEPT_SETUP))

P.append(QE("q4_7", "ON DELETE CASCADE", """
CREATE TABLE emp4 (
  empno  NUMBER(4) PRIMARY KEY,
  ename  VARCHAR2(10),
  deptno NUMBER(2)
         REFERENCES dept4 (deptno)
         ON DELETE CASCADE
);

INSERT INTO emp4 VALUES (1, 'AMIT', 20);
INSERT INTO emp4 VALUES (2, 'HETAL', 10);
INSERT INTO emp4 VALUES (3, 'RAJESH', 10);

DELETE FROM dept4 WHERE deptno = 10;

SELECT * FROM emp4;
""", """
<ul><li>With <b>ON DELETE CASCADE</b>, deleting a parent row automatically deletes all its child rows.</li>
<li>Deleting department 10 also removed HETAL and RAJESH. Only "1 row deleted." is shown, because the child rows are deleted by Oracle, not by our statement.</li>
<li>Use it when child rows have no meaning without the parent, e.g. order items of an order.</li></ul>
""", setup=DEPT_SETUP))

P.append(QE("q4_8", "ON DELETE SET NULL", """
CREATE TABLE emp4 (
  empno  NUMBER(4) PRIMARY KEY,
  ename  VARCHAR2(10),
  deptno NUMBER(2)
         REFERENCES dept4 (deptno)
         ON DELETE SET NULL
);

INSERT INTO emp4 VALUES (1, 'AMIT', 20);
INSERT INTO emp4 VALUES (2, 'HETAL', 10);
INSERT INTO emp4 VALUES (3, 'RAJESH', 10);

DELETE FROM dept4 WHERE deptno = 10;

SELECT * FROM emp4 ORDER BY empno;
""", """
<ul><li>With <b>ON DELETE SET NULL</b>, the child rows are kept but their foreign key becomes NULL.</li>
<li>HETAL and RAJESH still exist, now without a department.</li>
<li>The foreign key column must allow NULL for this rule.</li></ul>
""", setup=DEPT_SETUP))

# ------------------------------------------------------------------ ALTER TABLE constraints
P.append(QE("q4_9", "Add constraints to an existing table (ALTER TABLE)", """
CREATE TABLE item (
  icode NUMBER(3),
  iname VARCHAR2(15),
  rate  NUMBER(6)
);
INSERT INTO item VALUES (1, 'Pen', 10);
INSERT INTO item VALUES (2, 'Book', -60);

ALTER TABLE item
ADD CONSTRAINT pk_item PRIMARY KEY (icode);

ALTER TABLE item
ADD CONSTRAINT ck_rate CHECK (rate > 0);

UPDATE item SET rate = 60 WHERE icode = 2;

ALTER TABLE item
ADD CONSTRAINT ck_rate CHECK (rate > 0);

ALTER TABLE item MODIFY iname NOT NULL;
""", """
<ul><li><code>ALTER TABLE ... ADD CONSTRAINT</code> adds PRIMARY KEY, UNIQUE, CHECK or FOREIGN KEY to an existing table. NOT NULL is added with <code>MODIFY</code>.</li>
<li>Oracle checks the existing rows first. The rate -60 breaks the new check, so it fails with <b>ORA-02293: cannot validate</b>.</li>
<li>After correcting the data, the same constraint is added successfully.</li></ul>
""", setup=""))

P.append(QE("q4_10", "Drop, disable and enable constraints", """
ALTER TABLE emp DISABLE CONSTRAINT fk_dept;

INSERT INTO emp (empno, ename, deptno)
VALUES (120, 'RAVI', 50);

ALTER TABLE emp ENABLE CONSTRAINT fk_dept;

DELETE FROM emp WHERE empno = 120;

ALTER TABLE emp ENABLE CONSTRAINT fk_dept;

ALTER TABLE dept DROP PRIMARY KEY;

ALTER TABLE emp DROP CONSTRAINT fk_dept;

ALTER TABLE dept DROP PRIMARY KEY;
""", """
<ul><li><b>DISABLE</b> switches a constraint off temporarily (for example, during bulk data loading); <b>ENABLE</b> switches it on again.</li>
<li>Enabling fails with <b>ORA-02298</b> while a row (department 50) breaks the rule; after the bad row is removed it succeeds.</li>
<li>A primary key that is referenced by a foreign key cannot be dropped (<b>ORA-02273</b>). Drop the foreign key first, or use <code>DROP PRIMARY KEY CASCADE</code>.</li></ul>
""", setup=SCOTT))

P.append(QE("q4_11", "View constraints in the data dictionary", """
SELECT constraint_name, constraint_type,
       table_name, r_constraint_name
FROM user_constraints
WHERE table_name IN ('DEPT', 'EMP')
ORDER BY table_name, constraint_name;

SELECT constraint_name, column_name,
       position
FROM user_cons_columns
WHERE table_name = 'EMP'
ORDER BY constraint_name;
""", """
<ul><li><b>USER_CONSTRAINTS</b> lists every constraint you own. CONSTRAINT_TYPE: <b>P</b> = primary key, <b>U</b> = unique, <b>R</b> = foreign key (referential), <b>C</b> = check or NOT NULL.</li>
<li>R_CONSTRAINT_NAME shows the parent key that a foreign key refers to (FK_DEPT → PK_DEPT).</li>
<li><b>USER_CONS_COLUMNS</b> shows which columns belong to each constraint.</li></ul>
""", setup=SCOTT))

P.append(QE("q4_12", "Practical 11: college database with all constraints", """
CREATE TABLE branch (
  bcode CHAR(2) PRIMARY KEY,
  bname VARCHAR2(20) NOT NULL UNIQUE
);

CREATE TABLE stud (
  enrol NUMBER(4) PRIMARY KEY,
  sname VARCHAR2(20) NOT NULL,
  bcode CHAR(2) REFERENCES branch
        ON DELETE CASCADE,
  sem   NUMBER(1)
        CHECK (sem BETWEEN 1 AND 6),
  email VARCHAR2(25) UNIQUE
);

INSERT INTO branch
VALUES ('CE', 'Computer');
INSERT INTO branch
VALUES ('IT', 'Information Tech');
INSERT INTO stud
VALUES (101, 'Aarav', 'CE', 3, 'a@g.in');
INSERT INTO stud
VALUES (102, 'Diya', 'IT', 3, 'd@g.in');
INSERT INTO stud
VALUES (103, 'Karan', 'ME', 3, 'k@g.in');
INSERT INTO stud
VALUES (104, 'Isha', 'CE', 9, 'i@g.in');

SELECT table_name, constraint_type,
       COUNT(*) total
FROM user_constraints
GROUP BY table_name, constraint_type
ORDER BY table_name, constraint_type;
""", """
<ul><li>All three types of integrity are used: <b>domain</b> (NOT NULL, CHECK on sem), <b>entity</b> (PRIMARY KEY, UNIQUE) and <b>referential</b> (FOREIGN KEY with ON DELETE CASCADE).</li>
<li><code>REFERENCES branch</code> without a column refers to the parent's primary key.</li>
<li>Branch 'ME' does not exist (ORA-02291) and semester 9 is out of range (ORA-02290), so those rows are rejected.</li>
<li>The last query counts the constraints of each type in each table (C includes the NOT NULL constraints).</li></ul>
""", setup=""))

# ------------------------------------------------------------------ 4.2 views
P.append(QE("q4_13", "Create a simple view and query it", """
CREATE VIEW emp20 AS
SELECT empno, ename, job, sal
FROM emp
WHERE deptno = 20;

SELECT * FROM emp20 ORDER BY empno;

SELECT ename, sal FROM emp20
WHERE sal > 30000
ORDER BY sal DESC;

DESC emp20
""", """
<ul><li>A <b>view</b> is a stored SELECT statement that behaves like a virtual table. No data is copied; each query on EMP20 reads EMP.</li>
<li>The view hides the other columns (MGR, COMM, DEPTNO...) and other departments' rows: a simple way of giving <b>security</b>.</li>
<li>A view can be queried, filtered and described just like a table.</li></ul>
""", setup=SCOTT))

P.append(QE("q4_14", "INSERT, UPDATE and DELETE through a simple view", """
CREATE VIEW emp20 AS
SELECT empno, ename, sal, deptno
FROM emp WHERE deptno = 20;

INSERT INTO emp20
VALUES (111, 'RAVI', 25000, 20);

UPDATE emp20 SET sal = sal + 2000
WHERE ename = 'KIRAN';

DELETE FROM emp20 WHERE empno = 111;

SELECT empno, ename, sal, deptno
FROM emp WHERE deptno = 20
ORDER BY empno;
""", """
<ul><li>DML on a <b>simple view</b> (one table, no group functions, DISTINCT or expressions) changes the <b>base table</b>.</li>
<li>RAVI was inserted into EMP and then deleted; KIRAN's salary in EMP became 24000.</li>
<li>Columns not in the view (JOB, MGR ...) are set to NULL or their default when a row is inserted through the view, so NOT NULL columns of the base table must be included in the view.</li></ul>
""", setup=SCOTT))

P.append(QE("q4_15", "Complex view (join and GROUP BY)", """
CREATE VIEW dept_summary AS
SELECT d.dname, COUNT(e.empno) total,
       SUM(e.sal) total_sal
FROM dept d JOIN emp e
ON d.deptno = e.deptno
GROUP BY d.dname;

SELECT * FROM dept_summary
ORDER BY dname;

UPDATE dept_summary SET total = 10
WHERE dname = 'SALES';

CREATE VIEW emp_annual (id, name, annual)
AS SELECT empno, ename, sal * 12
FROM emp;

UPDATE emp_annual SET annual = 0
WHERE id = 101;
""", """
<ul><li>A <b>complex view</b> uses joins, group functions, GROUP BY, DISTINCT or expressions. It is very useful for reports.</li>
<li>DML on a group view is not allowed: <b>ORA-01732</b>.</li>
<li>A column made from an expression (sal * 12) is a <b>virtual column</b>; it cannot be updated (<b>ORA-01733</b>), but the other columns of that view can be.</li>
<li>Column aliases can be given in the view header: <code>emp_annual (id, name, annual)</code>.</li></ul>
""", setup=SCOTT))

P.append(QE("q4_16", "WITH CHECK OPTION", """
CREATE VIEW emp30 AS
SELECT empno, ename, sal, deptno
FROM emp WHERE deptno = 30
WITH CHECK OPTION;

INSERT INTO emp30
VALUES (112, 'ZARA', 21000, 30);

INSERT INTO emp30
VALUES (113, 'TINA', 21000, 10);

UPDATE emp30 SET deptno = 20
WHERE ename = 'VIJAY';

UPDATE emp30 SET sal = 21000
WHERE ename = 'VIJAY';
""", """
<ul><li><b>WITH CHECK OPTION</b> allows only those inserts and updates whose resulting rows can still be seen through the view.</li>
<li>Inserting a department 10 row, or moving VIJAY to department 20, would make the row disappear from EMP30, so Oracle gives <b>ORA-01402: view WITH CHECK OPTION where-clause violation</b>.</li>
<li>Changes that keep deptno = 30 are allowed.</li></ul>
""", setup=SCOTT))

P.append(QE("q4_17", "WITH READ ONLY view", """
CREATE VIEW emp_public AS
SELECT empno, ename, job
FROM emp
WITH READ ONLY;

SELECT * FROM emp_public
WHERE job = 'MANAGER'
ORDER BY empno;

UPDATE emp_public SET job = 'CEO'
WHERE empno = 101;

DELETE FROM emp_public;
""", """
<ul><li>A <b>READ ONLY</b> view can only be queried. Any INSERT, UPDATE or DELETE through it gives <b>ORA-42399</b>.</li>
<li>Use it to let users see data (without salary) but never change it.</li></ul>
""", setup=SCOTT))

P.append(QE("q4_18", "Alter, replace and drop a view", """
CREATE VIEW v_emp AS
SELECT empno, ename FROM emp;

CREATE OR REPLACE VIEW v_emp AS
SELECT empno, ename, sal FROM emp
WHERE sal > 50000;

ALTER VIEW v_emp COMPILE;

SELECT * FROM v_emp ORDER BY empno;

SELECT view_name, text
FROM user_views;

DROP VIEW v_emp;

SELECT * FROM v_emp;
""", """
<ul><li><b>CREATE OR REPLACE VIEW</b> changes the definition of an existing view without dropping it (privileges granted on it are kept).</li>
<li><b>ALTER VIEW ... COMPILE</b> recompiles a view, e.g. after its base table was changed. (ALTER VIEW cannot change the query.)</li>
<li><b>USER_VIEWS</b> stores the view's query text.</li>
<li><b>DROP VIEW</b> removes only the definition; the data in EMP is not affected. Afterwards the view no longer exists (ORA-00942).</li></ul>
""", setup=SCOTT))

# ------------------------------------------------------------------ synonyms
P.append(QE("q4_19", "Create, use and drop a synonym", """
CREATE SYNONYM e FOR emp;

SELECT ename, sal FROM e
WHERE deptno = 10
ORDER BY ename;

UPDATE e SET sal = 16000
WHERE empno = 110;

SELECT synonym_name, table_owner,
       table_name
FROM user_synonyms;

DROP SYNONYM e;

SELECT COUNT(*) FROM e;
""", """
<ul><li>A <b>synonym</b> is an alias (another name) for a table, view, sequence or other object. It stores no data.</li>
<li>All SELECT and DML statements on the synonym work on the real table EMP.</li>
<li>It hides the real owner and name, and gives a short name for a long one (e.g. <code>CREATE PUBLIC SYNONYM emp FOR scott.emp</code>, so other users need not write scott.emp).</li>
<li>After DROP SYNONYM the name no longer exists, but the table is unaffected.</li></ul>
""", setup=SCOTT))

# ------------------------------------------------------------------ sequences
P.append(QE("q4_20", "Sequence with NEXTVAL and CURRVAL", """
CREATE TABLE bill (
  bill_no NUMBER(5) PRIMARY KEY,
  cust    VARCHAR2(15)
);

CREATE SEQUENCE seq_bill
START WITH 1001
INCREMENT BY 1
NOCACHE;

INSERT INTO bill
VALUES (seq_bill.NEXTVAL, 'Aarav');
INSERT INTO bill
VALUES (seq_bill.NEXTVAL, 'Diya');
INSERT INTO bill
VALUES (seq_bill.NEXTVAL, 'Karan');

SELECT * FROM bill ORDER BY bill_no;

SELECT seq_bill.CURRVAL FROM dual;
""", """
<ul><li>A <b>sequence</b> generates unique numbers automatically; it is mostly used for primary key values such as bill numbers.</li>
<li><b>NEXTVAL</b> returns the next number and advances the sequence; <b>CURRVAL</b> returns the last number given by NEXTVAL in this session.</li>
<li>CURRVAL cannot be used before the first NEXTVAL in a session (ORA-08002).</li></ul>
""", setup=""))

P.append(QE("q4_21", "ALTER SEQUENCE, CYCLE and DROP SEQUENCE", """
CREATE SEQUENCE seq_tok
START WITH 1 INCREMENT BY 1
MAXVALUE 3 NOCYCLE NOCACHE;

SELECT seq_tok.NEXTVAL FROM dual;
SELECT seq_tok.NEXTVAL FROM dual;
SELECT seq_tok.NEXTVAL FROM dual;
SELECT seq_tok.NEXTVAL FROM dual;

ALTER SEQUENCE seq_tok
INCREMENT BY 10 MAXVALUE 100;

SELECT seq_tok.NEXTVAL FROM dual;

SELECT sequence_name, increment_by,
       max_value, last_number
FROM user_sequences;

DROP SEQUENCE seq_tok;
""", """
<ul><li>With <b>NOCYCLE</b>, the sequence stops at MAXVALUE: the 4th call gives <b>ORA-08004</b>. With <b>CYCLE</b> it would start again from MINVALUE.</li>
<li><b>ALTER SEQUENCE</b> can change INCREMENT BY, MAXVALUE, MINVALUE, CYCLE and CACHE, but <b>not START WITH</b> (drop and re-create the sequence for that).</li>
<li>After the change, the next number is 3 + 10 = 13. <b>USER_SEQUENCES</b> shows the settings; LAST_NUMBER is the next number to be given.</li></ul>
""", setup=""))

# ------------------------------------------------------------------ indexes
P.append(QE("q4_22", "Simple, composite and unique indexes", """
CREATE INDEX idx_ename ON emp (ename);

CREATE INDEX idx_dept_job
ON emp (deptno, job);

CREATE UNIQUE INDEX idx_dname
ON dept (dname);

SELECT index_name, table_name,
       uniqueness
FROM user_indexes
ORDER BY table_name, index_name;

SELECT index_name, column_name,
       column_position
FROM user_ind_columns
WHERE index_name = 'IDX_DEPT_JOB'
ORDER BY column_position;

SELECT ename, sal FROM emp
WHERE ename = 'NEHA';
""", """
<ul><li>An <b>index</b> speeds up searching (WHERE, JOIN, ORDER BY) on its columns, like the index of a book. Oracle uses it automatically; queries do not change.</li>
<li><b>Composite index</b>: on two or more columns (deptno, job); most useful when the WHERE clause uses the leading column.</li>
<li><b>Unique index</b>: also stops duplicate values. PK_DEPT and PK_EMP were created automatically by the primary keys.</li></ul>
""", setup=SCOTT))

P.append(QE("q4_23", "Index rules and DROP INDEX", """
CREATE UNIQUE INDEX idx_job ON emp (job);

CREATE INDEX idx_empno ON emp (empno);

CREATE INDEX idx_sal ON emp (sal);

DROP INDEX pk_emp;

DROP INDEX idx_sal;

INSERT INTO dept
VALUES (50, 'HR', 'SURAT');
CREATE UNIQUE INDEX idx_loc
ON dept (loc);
""", """
<ul><li>A unique index cannot be created on a column that already has duplicates (several CLERKs): <b>ORA-01452</b>.</li>
<li>EMPNO is already indexed by its primary key: <b>ORA-01408</b>.</li>
<li>An index that enforces a primary key / unique constraint cannot be dropped directly (<b>ORA-02429</b>); drop or disable the constraint instead.</li>
<li>After a second SURAT department is inserted, a unique index on LOC also fails with ORA-01452.</li>
<li><b>DROP INDEX</b> removes only the index, never the table data. Too many indexes slow down INSERT, UPDATE and DELETE, because every index must be updated as well.</li></ul>
""", setup=SCOTT))

PROGRAMS = P
