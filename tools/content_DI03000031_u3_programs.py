"""DI03000031 RDBMS Unit 3 – SQL programs for normalization (practical 19), real output from sql_runner."""
from sql_content import QE
from sql_seed import SCOTT

FLAT = """
CREATE TABLE stud_course (
  roll  NUMBER(3),
  name  VARCHAR2(10),
  cid   VARCHAR2(3),
  cname VARCHAR2(10),
  fees  NUMBER(5)
);
INSERT INTO stud_course VALUES (1, 'Aarav', 'C1', 'DBMS', 5000);
INSERT INTO stud_course VALUES (2, 'Diya', 'C1', 'DBMS', 5000);
INSERT INTO stud_course VALUES (3, 'Karan', 'C1', 'DBMS', 5000);
INSERT INTO stud_course VALUES (4, 'Isha', 'C2', 'Python', 4000);
INSERT INTO stud_course VALUES (1, 'Aarav', 'C2', 'Python', 4000);
COMMIT;
"""

NF3 = """
CREATE TABLE student (roll NUMBER(3) PRIMARY KEY, name VARCHAR2(10));
CREATE TABLE course (cid VARCHAR2(3) PRIMARY KEY, cname VARCHAR2(10), fees NUMBER(5));
CREATE TABLE enroll (roll NUMBER(3) REFERENCES student(roll), cid VARCHAR2(3) REFERENCES course(cid), PRIMARY KEY (roll, cid));
INSERT INTO student VALUES (1, 'Aarav');
INSERT INTO student VALUES (2, 'Diya');
INSERT INTO student VALUES (3, 'Karan');
INSERT INTO student VALUES (4, 'Isha');
INSERT INTO course VALUES ('C1', 'DBMS', 5000);
INSERT INTO course VALUES ('C2', 'Python', 4000);
INSERT INTO enroll VALUES (1, 'C1');
INSERT INTO enroll VALUES (2, 'C1');
INSERT INTO enroll VALUES (3, 'C1');
INSERT INTO enroll VALUES (4, 'C2');
INSERT INTO enroll VALUES (1, 'C2');
COMMIT;
"""

P = []

P.append(QE("q3_1", "Unnormalized table: redundancy and update anomaly", """
SELECT * FROM stud_course;

-- Fees of DBMS changed, but only one
-- row is updated by mistake
UPDATE stud_course SET fees = 5500
WHERE roll = 1 AND cid = 'C1';

SELECT DISTINCT cid, cname, fees
FROM stud_course
ORDER BY cid, fees;
""", """
<ul><li>The course details (CNAME, FEES) are repeated for every student who joins the course, and Aarav's name is repeated for each of his courses: this is <b>redundancy</b>.</li>
<li>The new DBMS fee was saved in only one of the three DBMS rows. Now the same course C1 shows <b>two different fees</b> (5000 and 5500): an <b>update anomaly</b>, which makes the data inconsistent.</li>
<li>Only the dependency CID → CNAME, FEES caused this. Normalization moves it into its own table.</li></ul>
""", setup=FLAT))

P.append(QE("q3_2", "Unnormalized table: insertion and deletion anomalies", """
-- New course C3 with no student yet
INSERT INTO stud_course
VALUES (NULL, NULL, 'C3', 'Java', 4500);

-- Both C2 (Python) students
-- leave the course
DELETE FROM stud_course
WHERE roll IN (4, 1) AND cid = 'C2';

SELECT DISTINCT cid, cname, fees
FROM stud_course
ORDER BY cid;
""", """
<ul><li><b>Insertion anomaly:</b> to store a new course we must insert a row with NULL roll and name. If (ROLL, CID) were the primary key, this insert would be rejected, because a key cannot be NULL.</li>
<li><b>Deletion anomaly:</b> deleting the only students of course C2 also deleted all information about C2 (its name and fees). The course has disappeared from the database.</li></ul>
""", setup=FLAT))

P.append(QE("q3_3", "Normalized (3NF) tables: STUDENT, COURSE and ENROLL", """
CREATE TABLE student (
  roll NUMBER(3) PRIMARY KEY,
  name VARCHAR2(10)
);

CREATE TABLE course (
  cid   VARCHAR2(3) PRIMARY KEY,
  cname VARCHAR2(10),
  fees  NUMBER(5)
);

CREATE TABLE enroll (
  roll NUMBER(3)
       REFERENCES student(roll),
  cid  VARCHAR2(3)
       REFERENCES course(cid),
  PRIMARY KEY (roll, cid)
);

INSERT INTO course
VALUES ('C1', 'DBMS', 5000);
INSERT INTO course
VALUES ('C2', 'Python', 4000);

-- course with no student: allowed
INSERT INTO course
VALUES ('C3', 'Java', 4500);

-- fee changed in ONE row only
UPDATE course SET fees = 5500
WHERE cid = 'C1';

SELECT * FROM course ORDER BY cid;
""", """
<ul><li>Each fact is now stored in exactly <b>one</b> place: student details in STUDENT, course details in COURSE, and who joined which course in ENROLL.</li>
<li>ENROLL has a composite primary key (roll, cid); both columns are foreign keys.</li>
<li>A new course can be added without any student, so there is <b>no insertion anomaly</b>.</li>
<li>The DBMS fee is changed with a single-row update, so there is <b>no update anomaly</b>.</li>
<li>Deleting an enrolment from ENROLL never deletes course data, so there is <b>no deletion anomaly</b>.</li></ul>
""", setup=""))

P.append(QE("q3_4", "Join the 3NF tables to get the original data back", """
SELECT e.roll, s.name, e.cid,
       c.cname, c.fees
FROM enroll e
JOIN student s ON e.roll = s.roll
JOIN course c ON e.cid = c.cid
ORDER BY e.roll, e.cid;

SELECT c.cname, COUNT(e.roll) students
FROM course c LEFT JOIN enroll e
ON c.cid = e.cid
GROUP BY c.cname
ORDER BY c.cname;
""", """
<ul><li>Joining the three tables on their keys gives back exactly the rows of the original table: the decomposition is <b>lossless</b> (no information is lost and no extra rows appear).</li>
<li>The original view can be saved as a <b>view</b> (Unit 4) so users can still query it as one table.</li>
<li>The second query counts the students in each course. The LEFT JOIN keeps courses that have no students.</li></ul>
""", setup=NF3))

P.append(QE("q3_5", "Normalize an existing table using CREATE TABLE ... AS SELECT", """
-- emp_flat repeats dname and loc
CREATE TABLE emp_flat AS
SELECT e.empno, e.ename, e.deptno,
       d.dname, d.loc
FROM emp e JOIN dept d
ON e.deptno = d.deptno;

-- 3NF: move DEPTNO -> DNAME, LOC out
CREATE TABLE dept3 AS
SELECT DISTINCT deptno, dname, loc
FROM emp_flat;

CREATE TABLE emp3 AS
SELECT empno, ename, deptno
FROM emp_flat;

SELECT * FROM dept3 ORDER BY deptno;

SELECT COUNT(*) flat_rows,
       COUNT(DISTINCT deptno) depts
FROM emp_flat;
""", """
<ul><li><code>emp_flat</code> is a 2NF table with the transitive dependency EMPNO → DEPTNO → DNAME, LOC: the department name and location are repeated 9 times for 3 departments.</li>
<li><code>SELECT DISTINCT</code> takes each department once, so DEPT3 stores the department facts only once.</li>
<li>EMP3 keeps DEPTNO as the link (a foreign key) to DEPT3. A PRIMARY KEY and FOREIGN KEY can then be added using ALTER TABLE (Unit 4).</li></ul>
""", setup=SCOTT))

PROGRAMS = P
