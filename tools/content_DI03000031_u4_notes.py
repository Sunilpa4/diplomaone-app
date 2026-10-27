"""DI03000031 Unit 4 notes: 4.1 integrity constraints, 4.2 database objects (views, synonyms, sequences, indexes)."""
from sql_content import make_TS

SN = {
    "s_levels": """
-- column level
col datatype [CONSTRAINT name] type

-- table level (after all columns)
[CONSTRAINT name] type (col1, col2)
""",
    "s_notnull": """
CREATE TABLE customer (
  cid   NUMBER(4),
  cname VARCHAR2(20) NOT NULL,
  city  VARCHAR2(15)
        CONSTRAINT nn_city NOT NULL
);
""",
    "s_check": """
age   NUMBER(2)
      CONSTRAINT ck_age
      CHECK (age BETWEEN 15 AND 30),
gender CHAR(1)
      CHECK (gender IN ('M', 'F')),
CONSTRAINT ck_marks
  CHECK (marks >= 0 AND marks <= 100)
""",
    "s_unique": """
email VARCHAR2(25)
      CONSTRAINT uq_email UNIQUE,
CONSTRAINT uq_phone UNIQUE (phone)
""",
    "s_pk": """
book_id NUMBER(4)
        CONSTRAINT pk_book PRIMARY KEY

-- composite key: table level only
CONSTRAINT pk_enroll
  PRIMARY KEY (roll, cid)
""",
    "s_fk": """
-- column level
deptno NUMBER(2)
       CONSTRAINT fk_emp_dept
       REFERENCES dept (deptno)

-- table level
CONSTRAINT fk_emp_dept
  FOREIGN KEY (deptno)
  REFERENCES dept (deptno)
""",
    "s_cascade": """
deptno NUMBER(2)
       REFERENCES dept (deptno)
       ON DELETE CASCADE

deptno NUMBER(2)
       REFERENCES dept (deptno)
       ON DELETE SET NULL
""",
    "s_alter_con": """
ALTER TABLE item
ADD CONSTRAINT pk_item PRIMARY KEY (icode);

ALTER TABLE item
ADD CONSTRAINT ck_rate CHECK (rate > 0);

ALTER TABLE emp
ADD CONSTRAINT fk_dept FOREIGN KEY (deptno)
REFERENCES dept (deptno);

ALTER TABLE item MODIFY iname NOT NULL;
""",
    "s_drop_con": """
ALTER TABLE item DROP CONSTRAINT ck_rate;
ALTER TABLE dept DROP PRIMARY KEY CASCADE;

ALTER TABLE emp DISABLE CONSTRAINT fk_dept;
ALTER TABLE emp ENABLE CONSTRAINT fk_dept;
""",
    "s_dict": """
SELECT constraint_name, constraint_type,
       table_name, status
FROM user_constraints
WHERE table_name = 'EMP';
""",
    "s_view": """
CREATE [OR REPLACE] [FORCE] VIEW name
  [(alias1, alias2, ...)]
AS SELECT ...
[WITH CHECK OPTION]
[WITH READ ONLY];
""",
    "s_view_ex": """
CREATE VIEW emp20 AS
SELECT empno, ename, job, sal
FROM emp
WHERE deptno = 20;

SELECT * FROM emp20;
""",
    "s_complex": """
CREATE VIEW dept_summary AS
SELECT d.dname, COUNT(e.empno) total,
       SUM(e.sal) total_sal
FROM dept d JOIN emp e
ON d.deptno = e.deptno
GROUP BY d.dname;
""",
    "s_check_opt": """
CREATE VIEW emp30 AS
SELECT empno, ename, sal, deptno
FROM emp WHERE deptno = 30
WITH CHECK OPTION;

CREATE VIEW emp_public AS
SELECT empno, ename, job FROM emp
WITH READ ONLY;
""",
    "s_alter_view": """
CREATE OR REPLACE VIEW v_emp AS
SELECT empno, ename, sal FROM emp;

ALTER VIEW v_emp COMPILE;

DROP VIEW v_emp;
""",
    "s_synonym": """
CREATE [PUBLIC] SYNONYM syn_name
FOR [schema.]object_name;

DROP [PUBLIC] SYNONYM syn_name;

CREATE SYNONYM e FOR emp;
SELECT * FROM e;
""",
    "s_seq": """
CREATE SEQUENCE seq_name
  [START WITH n]
  [INCREMENT BY n]
  [MINVALUE n | NOMINVALUE]
  [MAXVALUE n | NOMAXVALUE]
  [CYCLE | NOCYCLE]
  [CACHE n | NOCACHE];
""",
    "s_seq_use": """
CREATE SEQUENCE seq_bill
START WITH 1001 INCREMENT BY 1;

INSERT INTO bill
VALUES (seq_bill.NEXTVAL, 'Aarav');

SELECT seq_bill.CURRVAL FROM dual;
""",
    "s_seq_alter": """
ALTER SEQUENCE seq_bill
  INCREMENT BY 10
  MAXVALUE 99999
  CYCLE;

DROP SEQUENCE seq_bill;
""",
    "s_index": """
CREATE [UNIQUE] INDEX index_name
ON table_name (col1 [, col2 ...]);

DROP INDEX index_name;
""",
    "s_index_ex": """
CREATE INDEX idx_ename ON emp (ename);

CREATE UNIQUE INDEX idx_dname
ON dept (dname);

CREATE INDEX idx_dept_job
ON emp (deptno, job);
""",
}

T = make_TS(SN)

SEC_4_1 = {
    "title": {"en": "4.1 Integrity Constraints"},
    "items": [
        T("Integrity Constraints: Introduction and Types", """
<p><b>Data integrity</b> means the data in a database is accurate, valid and consistent. <b>Integrity constraints</b> are rules defined on the columns of a table that the DBMS checks automatically on every INSERT, UPDATE and DELETE. A statement that breaks a rule is rejected with an error, so invalid data never enters the table.</p>
<h4>Types of integrity constraints</h4>
<table><tr><th>Type</th><th>Purpose</th><th>Constraints</th></tr>
<tr><td>Domain integrity</td><td>Each value is valid for its column (domain)</td><td>NOT NULL, CHECK (and data type, DEFAULT)</td></tr>
<tr><td>Entity integrity</td><td>Each row is unique and identifiable</td><td>UNIQUE, PRIMARY KEY</td></tr>
<tr><td>Referential integrity</td><td>Links between tables stay valid</td><td>FOREIGN KEY, REFERENCES, ON DELETE CASCADE / SET NULL</td></tr></table>
<h4>Column level and table level</h4>
<ul><li><b>Column-level</b> constraint: written with the column definition. It applies to that one column. NOT NULL can only be column level.</li>
<li><b>Table-level</b> constraint: written after all columns. It is required when the constraint uses <b>more than one column</b> (composite primary key, multi-column CHECK).</li></ul>
@@s_levels@@
<h4>Naming constraints</h4>
<p>A constraint can be given a name with <code>CONSTRAINT name</code> (e.g. pk_emp, fk_emp_dept, ck_sal). If no name is given, Oracle creates one like <b>SYS_C008401</b>. Named constraints give clear error messages and are easy to drop, disable or enable.</p>
<p>Constraints can be defined in CREATE TABLE or added later with ALTER TABLE.</p>
""", diagram="db4_constraints"),
        T("NOT NULL Constraint", """
<p>A <b>NOT NULL</b> constraint ensures that a column <b>cannot contain NULL</b>: a value must be given for it in every row. By default every column allows NULL.</p>
<ul><li>It is a <b>domain integrity</b> constraint.</li>
<li>It can be defined only at <b>column level</b>.</li>
<li>Inserting NULL gives <b>ORA-01400: cannot insert NULL into (...)</b>; updating to NULL gives <b>ORA-01407</b>.</li>
<li>DESC shows NOT NULL in the Null? column.</li>
<li>Add it to an existing column with <code>ALTER TABLE t MODIFY col NOT NULL;</code> (only if the column has no NULLs). Remove it with <code>MODIFY col NULL</code>.</li></ul>
@@s_notnull@@
<p>Use NOT NULL for mandatory data such as name, date of birth or price.</p>
""", programs=["q4_1"]),
        T("CHECK Constraint", """
<p>A <b>CHECK</b> constraint defines a condition that each row must satisfy. A value is accepted only if the condition is TRUE (or UNKNOWN because of NULL).</p>
<ul><li>It is a <b>domain integrity</b> constraint: it limits the range or list of valid values.</li>
<li>It can be column level or table level; a condition on two or more columns must be table level.</li>
<li>Violation gives <b>ORA-02290: check constraint (...) violated</b>.</li>
<li>A table can have many CHECK constraints; one column can have several.</li>
<li>The condition cannot use sub-queries, SYSDATE, USER, ROWNUM, sequences or values from other rows.</li></ul>
@@s_check@@
<p>Examples: marks between 0 and 100, salary &gt; 0, gender IN ('M', 'F'), city = UPPER(city).</p>
""", programs=["q4_2"]),
        T("UNIQUE Constraint", """
<p>A <b>UNIQUE</b> constraint ensures that no two rows have the same value in the column (or combination of columns).</p>
<ul><li>It is an <b>entity integrity</b> constraint.</li>
<li>It <b>allows NULL</b>, and many rows can have NULL, because NULL is not equal to anything.</li>
<li>A table can have <b>many</b> UNIQUE constraints.</li>
<li>Oracle automatically creates a <b>unique index</b> with the same name to enforce it.</li>
<li>A duplicate value gives <b>ORA-00001: unique constraint (...) violated</b>.</li>
<li>A column set with a UNIQUE constraint can be referenced by a foreign key.</li></ul>
@@s_unique@@
<p>Typical use: alternate keys such as email, mobile number, Aadhaar number or vehicle number.</p>
""", programs=["q4_3"]),
        T("PRIMARY KEY Constraint", """
<p>A <b>PRIMARY KEY</b> uniquely identifies each row of a table. <b>PRIMARY KEY = UNIQUE + NOT NULL.</b></p>
<ul><li>It is an <b>entity integrity</b> constraint: every row has an identity.</li>
<li>A table can have <b>only one</b> primary key (ORA-02260 if you try to add a second).</li>
<li>Duplicate values give ORA-00001; NULL gives ORA-01400.</li>
<li>Oracle automatically creates a unique index for it.</li>
<li>A primary key on two or more columns is a <b>composite primary key</b> and must be defined at <b>table level</b>.</li>
<li>It is referenced by foreign keys of child tables.</li></ul>
@@s_pk@@
<p>Choose a value that never changes and is short, e.g. roll number, employee number, product code.</p>
""", diagram="db4_pk_unique", programs=["q4_4", "q4_5"]),
        T("FOREIGN KEY (REFERENCES) Constraint", """
<p>A <b>FOREIGN KEY</b> is a column (or set of columns) in one table whose values must match the <b>primary key or unique key</b> of another table (or of the same table). It creates a <b>parent-child relationship</b> and enforces <b>referential integrity</b>.</p>
<ul><li><b>Parent (referenced / master) table:</b> the table containing the primary key, e.g. DEPT.</li>
<li><b>Child (referencing / detail) table:</b> the table containing the foreign key, e.g. EMP.</li>
<li>The keyword <b>REFERENCES</b> names the parent table and column. If the column is omitted, the parent's primary key is used.</li>
<li>At table level the keywords <code>FOREIGN KEY (col)</code> are written before REFERENCES.</li></ul>
@@s_fk@@
<h4>Rules enforced</h4>
<ul><li>A child row can only contain a value that exists in the parent, or NULL; otherwise <b>ORA-02291: parent key not found</b>.</li>
<li>A parent row that has child rows cannot be deleted (or its key updated): <b>ORA-02292: child record found</b>.</li>
<li>The parent table must be created first and cannot be dropped while it is referenced (ORA-02449); use <code>DROP TABLE dept CASCADE CONSTRAINTS</code>.</li>
<li>A <b>self-referencing</b> foreign key refers to the same table, e.g. EMP.MGR REFERENCES EMP(EMPNO).</li></ul>
""", diagram="db4_fk", programs=["q4_6"]),
        T("ON DELETE CASCADE and ON DELETE SET NULL", """
<p>By default Oracle does not allow a parent row to be deleted while child rows refer to it. A <b>delete rule</b> written with the foreign key changes this behaviour:</p>
<table><tr><th>Rule</th><th>When a parent row is deleted</th></tr>
<tr><td>(none) / NO ACTION</td><td>Delete is rejected with ORA-02292 while child rows exist</td></tr>
<tr><td>ON DELETE CASCADE</td><td>All matching child rows are deleted automatically</td></tr>
<tr><td>ON DELETE SET NULL</td><td>The foreign key of matching child rows is set to NULL</td></tr></table>
@@s_cascade@@
<ul><li>Use <b>CASCADE</b> when child rows have no meaning without the parent (order items of an order, marks of a student).</li>
<li>Use <b>SET NULL</b> when child rows should be kept (employees of a closed department).</li>
<li>The delete rule is shown in the DELETE_RULE column of USER_CONSTRAINTS.</li>
<li>Oracle has no ON UPDATE CASCADE; parent keys should not be changed.</li></ul>
""", diagram="db4_cascade", programs=["q4_7", "q4_8"]),
        T("Adding, Dropping, Enabling and Disabling Constraints", """
<p>Constraints can be managed on an existing table with <b>ALTER TABLE</b>.</p>
<h4>Adding constraints</h4>
@@s_alter_con@@
<p>When a constraint is added, Oracle first checks the <b>existing rows</b>. If any row breaks the rule, the constraint is not created, e.g. ORA-02293 (check), ORA-02437 (primary key), ORA-02299 (unique), ORA-02298 (foreign key) or ORA-02296 (NOT NULL).</p>
<h4>Dropping, disabling and enabling</h4>
@@s_drop_con@@
<ul><li><b>DROP CONSTRAINT</b> removes the rule permanently.</li>
<li>A primary/unique key referenced by a foreign key cannot be dropped (ORA-02273) unless CASCADE is used, which also drops the foreign keys.</li>
<li><b>DISABLE</b> turns a constraint off temporarily, e.g. to load large amounts of data quickly. <b>ENABLE</b> turns it on again and checks all rows.</li>
<li>Disabling a primary key also drops its index; enabling re-creates it.</li></ul>
""", programs=["q4_9", "q4_10"]),
        T("Viewing Constraints: USER_CONSTRAINTS", """
<p>Constraint definitions are stored in the <b>data dictionary</b>.</p>
<ul><li><b>USER_CONSTRAINTS</b>: one row per constraint. Important columns: CONSTRAINT_NAME, CONSTRAINT_TYPE, TABLE_NAME, SEARCH_CONDITION, R_CONSTRAINT_NAME, DELETE_RULE, STATUS.</li>
<li><b>USER_CONS_COLUMNS</b>: the columns used in each constraint.</li></ul>
<table><tr><th>CONSTRAINT_TYPE</th><th>Meaning</th></tr>
<tr><td>P</td><td>Primary key</td></tr><tr><td>U</td><td>Unique key</td></tr>
<tr><td>R</td><td>Referential (foreign key)</td></tr><tr><td>C</td><td>Check (NOT NULL is also stored as C)</td></tr></table>
@@s_dict@@
<p>Practical 11 (re-implementing the Practical 1 tables with constraints) uses all of these: create the parent tables first with primary keys, then the child tables with foreign keys, CHECK and NOT NULL, and then test valid and invalid rows.</p>
""", programs=["q4_11", "q4_12"]),
    ],
}

SEC_4_2 = {
    "title": {"en": "4.2 Database Objects"},
    "items": [
        T("Database Objects: Overview", """
<p>A <b>database object</b> is any named structure stored in the database. Besides tables, Oracle provides:</p>
<table><tr><th>Object</th><th>Purpose</th></tr>
<tr><td>Table</td><td>Basic unit of storage: rows and columns</td></tr>
<tr><td>View</td><td>Logical (virtual) table based on a query</td></tr>
<tr><td>Synonym</td><td>Alternative name for an object</td></tr>
<tr><td>Sequence</td><td>Generates unique numeric values</td></tr>
<tr><td>Index</td><td>Improves the speed of data retrieval</td></tr></table>
<p>All objects are created with CREATE, changed with ALTER (where allowed) and removed with DROP. Their details are stored in the data dictionary views USER_TABLES, USER_VIEWS, USER_SYNONYMS, USER_SEQUENCES, USER_INDEXES and USER_OBJECTS.</p>
""", diagram="db4_objects"),
        T("Views: Concept and CREATE VIEW", """
<p>A <b>view</b> is a <b>virtual table</b> based on the result of a SELECT statement. It has rows and columns like a table but <b>stores no data</b> of its own; only its query is stored in the data dictionary. Each time the view is used, Oracle runs the query on the <b>base table(s)</b>, so the view always shows current data.</p>
@@s_view@@
<ul><li><b>OR REPLACE</b>: re-creates the view if it already exists.</li>
<li><b>FORCE</b>: creates the view even if the base table does not exist yet.</li>
<li><b>Aliases</b>: column names for the view.</li>
<li><b>WITH CHECK OPTION</b> / <b>WITH READ ONLY</b>: restrict DML through the view.</li></ul>
@@s_view_ex@@
<h4>Advantages of views</h4>
<ul><li><b>Security:</b> users see only selected columns and rows (e.g. no salary).</li>
<li><b>Simplicity:</b> a complex join or calculation is written once and used like a table.</li>
<li><b>Data independence:</b> applications use the view even if the base table structure changes.</li>
<li><b>Different views</b> of the same data for different users.</li>
<li>No extra storage is needed.</li></ul>
<p><b>Disadvantages:</b> a view on a complex query can be slow, and DML through complex views is restricted.</p>
""", diagram="db4_view", programs=["q4_13"]),
        T("Simple and Complex Views; DML through Views", """
<table><tr><th>Simple view</th><th>Complex view</th></tr>
<tr><td>Based on one table</td><td>Based on one or more tables (joins)</td></tr>
<tr><td>No functions, GROUP BY or DISTINCT</td><td>Can contain group functions, GROUP BY, DISTINCT, expressions</td></tr>
<tr><td>INSERT, UPDATE, DELETE allowed (usually)</td><td>DML not always allowed</td></tr></table>
@@s_complex@@
<h4>Rules for DML through a view</h4>
<ul><li>INSERT, UPDATE and DELETE on a simple view change the <b>base table</b>.</li>
<li>DML is <b>not allowed</b> if the view contains group functions, GROUP BY, DISTINCT or ROWNUM: <b>ORA-01732</b>.</li>
<li>A column defined by an expression (e.g. sal * 12) cannot be inserted or updated: <b>ORA-01733</b>.</li>
<li>INSERT through a view fails if a NOT NULL column of the base table is not in the view.</li>
<li>For a join view, only the <b>key-preserved</b> table can be modified.</li></ul>
""", diagram="db4_view_types", programs=["q4_14", "q4_15"]),
        T("WITH CHECK OPTION and WITH READ ONLY", """
<p><b>WITH CHECK OPTION</b> ensures that every row inserted or updated through the view satisfies the view's WHERE condition, so it remains visible through the view. Otherwise Oracle gives <b>ORA-01402: view WITH CHECK OPTION where-clause violation</b>.</p>
<p><b>WITH READ ONLY</b> prevents all DML operations through the view (<b>ORA-42399</b>). The view can only be queried.</p>
@@s_check_opt@@
<ul><li>Through EMP30 you cannot insert an employee of department 10 or move an employee to department 20.</li>
<li>Through EMP_PUBLIC users can see employee names and jobs but cannot change anything.</li>
<li>A name can be given: <code>WITH CHECK OPTION CONSTRAINT ck_emp30</code>.</li></ul>
""", programs=["q4_16", "q4_17"]),
        T("ALTER VIEW and DROP VIEW", """
@@s_alter_view@@
<ul><li><b>CREATE OR REPLACE VIEW</b> is the way to change a view's query. The view keeps its name and the privileges granted on it.</li>
<li><b>ALTER VIEW view_name COMPILE</b> recompiles a view that became invalid after a change to its base table. ALTER VIEW cannot change the query.</li>
<li><b>DROP VIEW</b> removes the view definition only; the base table data is not affected. Views built on the dropped view become invalid.</li>
<li>If the base table is dropped, the view becomes <b>invalid</b> and gives an error when used.</li>
<li>View definitions can be seen in <b>USER_VIEWS</b> (VIEW_NAME, TEXT).</li></ul>
""", programs=["q4_18"]),
        T("Synonyms: CREATE SYNONYM and DROP SYNONYM", """
<p>A <b>synonym</b> is an alternative name (alias) for a table, view, sequence, procedure or another synonym. It stores no data; it only points to the object.</p>
@@s_synonym@@
<h4>Types</h4>
<ul><li><b>Private synonym</b> (default): owned by a user and usable by that user (and others with privileges).</li>
<li><b>Public synonym</b>: created with PUBLIC by the DBA and usable by all users, e.g. <code>CREATE PUBLIC SYNONYM emp FOR scott.emp</code>.</li></ul>
<h4>Uses / advantages</h4>
<ul><li>Gives a short, simple name for a long object name such as scott.employee_details.</li>
<li>Hides the owner and real name of the object (location transparency and security).</li>
<li>If the object moves, only the synonym is changed; programs stay the same.</li></ul>
<p>SELECT and DML on a synonym work on the real object. DROP SYNONYM removes only the alias. Synonyms are listed in <b>USER_SYNONYMS</b>.</p>
""", programs=["q4_19"]),
        T("Sequences: CREATE SEQUENCE, NEXTVAL and CURRVAL", """
<p>A <b>sequence</b> is a database object that generates a series of unique integers automatically. It is mainly used to generate <b>primary key values</b> such as roll numbers, bill numbers or order numbers.</p>
@@s_seq@@
<table><tr><th>Option</th><th>Meaning (default)</th></tr>
<tr><td>START WITH</td><td>First number (1)</td></tr>
<tr><td>INCREMENT BY</td><td>Gap between numbers; negative for descending (1)</td></tr>
<tr><td>MINVALUE / MAXVALUE</td><td>Lowest and highest value</td></tr>
<tr><td>CYCLE / NOCYCLE</td><td>Restart after MAXVALUE or stop with an error (NOCYCLE)</td></tr>
<tr><td>CACHE n / NOCACHE</td><td>Pre-allocate n numbers in memory for speed (CACHE 20)</td></tr></table>
<h4>Pseudo columns</h4>
<ul><li><b>seq.NEXTVAL</b>: returns the next number and advances the sequence.</li>
<li><b>seq.CURRVAL</b>: returns the current (last generated) number in this session; it can be used only after NEXTVAL (else ORA-08002).</li></ul>
@@s_seq_use@@
<p>A sequence is independent of tables: one sequence can be used for many tables. Numbers are not rolled back, so gaps can appear after ROLLBACK or a crash.</p>
""", diagram="db4_sequence", programs=["q4_20"]),
        T("ALTER SEQUENCE and DROP SEQUENCE", """
@@s_seq_alter@@
<ul><li><b>ALTER SEQUENCE</b> can change INCREMENT BY, MINVALUE, MAXVALUE, CYCLE and CACHE. The change affects only future numbers.</li>
<li><b>START WITH cannot be altered</b> (ORA-02283); drop and re-create the sequence to restart it.</li>
<li>MAXVALUE cannot be set lower than the current value.</li>
<li>With NOCYCLE, NEXTVAL after MAXVALUE gives <b>ORA-08004</b>.</li>
<li><b>DROP SEQUENCE</b> removes the sequence; values already stored in tables stay.</li>
<li><b>USER_SEQUENCES</b> shows SEQUENCE_NAME, MIN_VALUE, MAX_VALUE, INCREMENT_BY, CYCLE_FLAG, CACHE_SIZE and LAST_NUMBER.</li></ul>
""", programs=["q4_21"]),
        T("Indexes: Concept, Unique and Composite Index", """
<p>An <b>index</b> is a database object that speeds up the retrieval of rows, just like the index at the back of a book. It stores the column values in <b>sorted order</b> together with the <b>ROWID</b> (address) of each row. Oracle uses an index automatically when a query searches on the indexed column; without an index, Oracle reads every row (<b>full table scan</b>).</p>
@@s_index@@
<h4>Types of indexes</h4>
<ul><li><b>Simple (single-column) index:</b> on one column.</li>
<li><b>Composite (concatenated) index:</b> on two or more columns, e.g. (deptno, job). It is used when the WHERE clause uses the leading column(s).</li>
<li><b>Unique index:</b> does not allow duplicate values. Oracle creates one automatically for every PRIMARY KEY and UNIQUE constraint.</li>
<li><b>Non-unique index:</b> allows duplicates (the default).</li></ul>
@@s_index_ex@@
<h4>When to create an index</h4>
<ul><li>The column is used often in WHERE, JOIN or ORDER BY.</li>
<li>The table is large and queries return a small part of its rows.</li>
<li>The column has many different values.</li></ul>
<h4>When not to</h4>
<ul><li>Small tables, or columns that are rarely searched.</li>
<li>Tables that are updated very often: every INSERT, UPDATE and DELETE must also update the indexes, and indexes take disk space.</li></ul>
""", diagram="db4_index", programs=["q4_22"]),
        T("DROP INDEX and Index Rules", """
<p><code>DROP INDEX index_name;</code> removes an index. The table and its data are not affected; queries still work but may be slower.</p>
<ul><li>A unique index cannot be created on a column that already contains duplicates: <b>ORA-01452</b>.</li>
<li>The same column list cannot be indexed twice: <b>ORA-01408</b> (e.g. a primary key column is already indexed).</li>
<li>An index used by a PRIMARY KEY or UNIQUE constraint cannot be dropped directly (<b>ORA-02429</b>); drop or disable the constraint.</li>
<li>When a table is dropped, all its indexes are dropped automatically.</li>
<li>Indexes are listed in <b>USER_INDEXES</b> and their columns in <b>USER_IND_COLUMNS</b>.</li>
<li><b>Practical 13</b> also compares query time with and without an index: in SQL*Plus, <code>SET TIMING ON</code> shows the time taken by each statement, and the difference appears clearly on a large table.</li></ul>
""", programs=["q4_23"]),
    ],
}

NOTES = [SEC_4_1, SEC_4_2]
