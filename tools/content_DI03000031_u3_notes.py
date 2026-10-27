"""DI03000031 Unit 3 notes: 3.1 basics of normalization, 3.2 normal forms, 3.3 advantages / disadvantages."""
from sql_content import make_TS

SN = {
    "s_dept3": """
CREATE TABLE dept3 AS
SELECT DISTINCT deptno, dname, loc
FROM emp_flat;
""",
}

T = make_TS(SN)

SEC_3_1 = {
    "title": {"en": "3.1 Basics of Normalization"},
    "items": [
        T("Normalization: Definition and Importance", """
<p><b>Normalization</b> is the process of organizing the columns (attributes) and tables (relations) of a relational database to <b>reduce data redundancy</b> and <b>remove insertion, update and deletion anomalies</b>. A large table is broken into smaller, well-structured tables that are linked by primary key / foreign key relationships.</p>
<p>It was introduced by <b>E. F. Codd</b> (the father of the relational model), who defined 1NF, 2NF and 3NF. Normalization is done step by step using <b>functional dependencies</b> and <b>normal forms</b>.</p>
<h4>Objectives (goals)</h4>
<ul><li>Store each fact only <b>once</b> (minimum redundancy).</li>
<li>Remove insertion, update and deletion anomalies.</li>
<li>Keep the data <b>consistent</b> and maintain data integrity.</li>
<li>Make the design simple, flexible and easy to extend.</li>
<li>Make sure the decomposition is <b>lossless</b>: the original data can be rebuilt by joining the tables.</li></ul>
<h4>Importance of normalization</h4>
<ul><li><b>Saves storage space</b> because repeated data is removed.</li>
<li><b>Data consistency:</b> a value is changed in one place only, so different copies cannot disagree.</li>
<li><b>Easy maintenance:</b> insert, update and delete are simple and safe.</li>
<li><b>Better data integrity</b> through primary and foreign keys.</li>
<li><b>Clear structure:</b> each table describes one entity (student, course, department), which makes the design easier to understand.</li>
<li>It is a key step in the <b>logical design</b> of a database (after the E-R diagram is converted into tables).</li></ul>
"""),
        T("Data Redundancy and Anomalies", """
<p><b>Data redundancy</b> means the same data is stored repeatedly in a database. In the table STUD_COURSE(ROLL, NAME, CID, CNAME, FEES), the course name and fees are repeated for every student in that course. Redundancy wastes space and causes three kinds of problems called <b>anomalies</b>.</p>
<h4>1. Insertion anomaly</h4>
<p>We cannot insert some data without inserting other, unrelated data. For example, a new course C3 cannot be stored until at least one student joins it, because ROLL is part of the primary key and cannot be NULL.</p>
<h4>2. Update (modification) anomaly</h4>
<p>The same fact is stored in many rows, so a change must be made in every row. If even one row is missed, the data becomes <b>inconsistent</b>. For example, the DBMS fee is stored in 3 rows; updating only one row gives two different fees for the same course.</p>
<h4>3. Deletion anomaly</h4>
<p>Deleting some data unintentionally deletes other useful data. For example, if Isha is the only student of the Python course and her row is deleted, all information about the Python course is also lost.</p>
<p><b>Cause:</b> one table stores facts about more than one entity (students and courses). <b>Solution:</b> normalization: store students, courses and enrolments in separate tables.</p>
""", diagram="db3_anomalies", programs=["q3_1", "q3_2"]),
        T("Keys in a Relation", """
<p>Keys are used to identify rows uniquely and to define normal forms.</p>
<ul><li><b>Super key:</b> a set of one or more attributes that uniquely identifies each row. Example: {ROLL}, {ROLL, NAME}, {EMAIL, CITY}.</li>
<li><b>Candidate key:</b> a <b>minimal</b> super key: no attribute can be removed from it. Example: {ROLL}, {EMAIL}, {AADHAAR}.</li>
<li><b>Primary key:</b> the candidate key chosen by the designer to identify rows. It must be unique and NOT NULL. Example: ROLL.</li>
<li><b>Alternate key:</b> a candidate key that is not chosen as the primary key. Example: EMAIL, AADHAAR.</li>
<li><b>Composite key:</b> a key made of two or more attributes. Example: (ROLL, CID) in RESULT.</li>
<li><b>Foreign key:</b> an attribute that refers to the primary key of another (or the same) table. Example: DEPTNO in EMP refers to DEPT(DEPTNO).</li></ul>
<p><b>Prime attribute:</b> an attribute that is part of <b>any</b> candidate key. <b>Non-prime (non-key) attribute:</b> an attribute that is not part of any candidate key. These terms are used in the definitions of 2NF and 3NF.</p>
""", diagram="db3_keys"),
        T("Functional Dependency (FD)", """
<p>A <b>functional dependency</b> X → Y (read "X determines Y") holds on a relation R if, whenever two rows have the same value of X, they must also have the same value of Y. X is called the <b>determinant</b> and Y the <b>dependent</b>.</p>
<p>In other words, the value of X <b>uniquely decides</b> the value of Y.</p>
<p><b>Examples</b> (from EMP, DEPT and RESULT):</p>
<ul><li>EMPNO → ENAME, SAL, DEPTNO (one employee number gives exactly one name, salary and department).</li>
<li>DEPTNO → DNAME, LOC.</li>
<li>ROLL, CID → MARKS (a student gets one mark in one course).</li>
<li>ENAME → EMPNO does <b>not</b> hold if two employees can have the same name.</li></ul>
<p>FDs come from the <b>meaning</b> of the data (business rules), not from a few sample rows. A sample can only show that an FD does <b>not</b> hold.</p>
<p><b>Trivial FD:</b> X → Y where Y is a subset of X, e.g. {ROLL, NAME} → NAME. It always holds. <b>Non-trivial FD:</b> Y is not a subset of X, e.g. ROLL → NAME.</p>
""", diagram="db3_fd"),
        T("Armstrong's Axioms and Attribute Closure", """
<p><b>Armstrong's axioms</b> are rules for deriving new FDs from given FDs (F). They are sound and complete.</p>
<table><tr><th>Rule</th><th>Statement</th></tr>
<tr><td>Reflexivity</td><td>If Y ⊆ X, then X → Y</td></tr>
<tr><td>Augmentation</td><td>If X → Y, then XZ → YZ</td></tr>
<tr><td>Transitivity</td><td>If X → Y and Y → Z, then X → Z</td></tr>
<tr><td>Union (derived)</td><td>If X → Y and X → Z, then X → YZ</td></tr>
<tr><td>Decomposition (derived)</td><td>If X → YZ, then X → Y and X → Z</td></tr>
<tr><td>Pseudo-transitivity (derived)</td><td>If X → Y and WY → Z, then WX → Z</td></tr></table>
<h4>Attribute closure (X<sup>+</sup>)</h4>
<p>The closure X<sup>+</sup> is the set of all attributes that are functionally determined by X using F.</p>
<ol><li>Set result = X.</li>
<li>For each FD A → B in F: if A ⊆ result, add B to result.</li>
<li>Repeat step 2 until result does not change.</li></ol>
<p><b>Uses:</b> if X<sup>+</sup> contains all attributes of R, then X is a <b>super key</b>; if no proper subset of X is a super key, X is a <b>candidate key</b>. It also tests whether an FD X → Y holds (check whether Y ⊆ X<sup>+</sup>).</p>
<p><b>Tip:</b> an attribute that never appears on the right side of any FD must be part of every candidate key.</p>
""", examples=["n3_7"]),
        T("Types of Functional Dependency", """
<ul><li><b>Full functional dependency:</b> Y depends on the whole of X and not on any proper subset of X. Example: (ROLL, CID) → MARKS, since neither ROLL alone nor CID alone gives the marks.</li>
<li><b>Partial dependency:</b> a non-prime attribute depends on <b>part</b> of a composite candidate key. Example: in RESULT(ROLL, CID, NAME, MARKS), ROLL → NAME. Partial dependencies violate <b>2NF</b>.</li>
<li><b>Transitive dependency:</b> X → Y and Y → Z, where Y is not a key and Z is non-prime, so X → Z holds indirectly. Example: EMPNO → DEPTNO and DEPTNO → DNAME give EMPNO → DNAME. Transitive dependencies violate <b>3NF</b>.</li>
<li><b>Trivial / non-trivial dependency:</b> explained in the previous topic.</li>
<li><b>Multivalued dependency</b> (X →→ Y): one X value is associated with a set of Y values independent of other attributes; used in 4NF (beyond syllabus).</li></ul>
""", diagram="db3_fd_types"),
    ],
}

SEC_3_2 = {
    "title": {"en": "3.2 Normal Forms"},
    "items": [
        T("Normal Forms: Overview", """
<p>A <b>normal form</b> is a condition (set of rules) that a relation must satisfy. Each higher normal form removes one more kind of bad dependency, and each includes all the lower ones:</p>
<p>UNF → 1NF → 2NF → 3NF → BCNF → 4NF → 5NF</p>
<table><tr><th>Normal form</th><th>Rule</th><th>Removes</th></tr>
<tr><td>1NF</td><td>All values atomic; no repeating groups</td><td>Multi-valued cells</td></tr>
<tr><td>2NF</td><td>1NF + no partial dependency</td><td>Partial dependency</td></tr>
<tr><td>3NF</td><td>2NF + no transitive dependency</td><td>Transitive dependency</td></tr>
<tr><td>BCNF</td><td>Every determinant is a candidate key</td><td>Remaining anomalies</td></tr></table>
<p>The method is <b>decomposition</b>: a relation that breaks a rule is split into two or more relations, each with its own key. In practice, most databases are designed up to <b>3NF</b>.</p>
<p>An <b>unnormalized form (UNF)</b> table contains repeating groups or multi-valued attributes, e.g. a COURSES column holding "DBMS, OS".</p>
""", diagram="db3_steps"),
        T("First Normal Form (1NF)", """
<p><b>Definition:</b> a relation is in 1NF if every attribute contains only <b>atomic (indivisible) values</b> and there are no repeating groups. Each cell holds a single value of the attribute's domain.</p>
<h4>Rules of 1NF</h4>
<ul><li>Each column holds a single value (no lists such as "DBMS, OS").</li>
<li>No repeating groups of columns (COURSE1, COURSE2, COURSE3).</li>
<li>All values in a column are of the same type (domain).</li>
<li>Each row is unique: a primary key is identified.</li>
<li>The order of rows and columns does not matter.</li></ul>
<h4>How to convert UNF to 1NF</h4>
<ol><li><b>Flattening:</b> create a separate row for each value of the multi-valued attribute and repeat the other values. The key becomes composite, e.g. (ROLL, COURSE).</li>
<li><b>Decomposition:</b> move the repeating group to a new table together with a copy of the primary key: STUDENT(ROLL, NAME) and STUDENT_COURSE(ROLL, COURSE).</li></ol>
<p>A table in 1NF can still have redundancy (NAME repeated for each course), which is removed by 2NF.</p>
<p>In Oracle every column of a normal table already holds one value of its data type, so tables created with CREATE TABLE are in 1NF as long as lists are not stored inside VARCHAR2 columns.</p>
""", diagram="db3_1nf", examples=["n3_1"]),
        T("Second Normal Form (2NF)", """
<p><b>Definition:</b> a relation is in 2NF if it is in <b>1NF</b> and every non-prime attribute is <b>fully functionally dependent</b> on every candidate key, i.e. there is <b>no partial dependency</b>.</p>
<p>A partial dependency is possible only when the key is <b>composite</b>. So a 1NF relation whose candidate keys all have a single attribute is automatically in 2NF.</p>
<h4>Steps to convert 1NF to 2NF</h4>
<ol><li>Find the candidate key(s) and the FDs.</li>
<li>Find each partial dependency (part of key → non-prime attributes).</li>
<li>Move each partial dependency into a new table; the part of the key becomes the primary key of the new table.</li>
<li>Keep the attributes that depend on the whole key in the original table with the full key.</li></ol>
<p><b>Example:</b> RESULT(ROLL, CID, NAME, CNAME, MARKS) with key (ROLL, CID). ROLL → NAME and CID → CNAME are partial. 2NF tables: STUDENT(ROLL, NAME), COURSE(CID, CNAME), RESULT(ROLL, CID, MARKS).</p>
<p>A 2NF table can still have transitive dependencies, which are removed by 3NF.</p>
""", diagram="db3_2nf", examples=["n3_2", "n3_5"]),
        T("Third Normal Form (3NF)", """
<p><b>Definition:</b> a relation is in 3NF if it is in <b>2NF</b> and <b>no non-prime attribute is transitively dependent</b> on a candidate key.</p>
<p><b>Formal definition:</b> for every non-trivial FD X → A, either X is a <b>super key</b> or A is a <b>prime attribute</b>.</p>
<p>In simple words: "every non-key attribute must depend on the key, the whole key, and nothing but the key."</p>
<h4>Steps to convert 2NF to 3NF</h4>
<ol><li>Find each transitive dependency: key → Y → Z, where Y is a non-key attribute.</li>
<li>Move Y and the attributes it determines (Z) into a new table with Y as the primary key.</li>
<li>Keep Y in the original table as a foreign key.</li></ol>
<p><b>Example:</b> EMPLOYEE(EMPNO, ENAME, SAL, DEPTNO, DNAME, LOC) has EMPNO → DEPTNO → DNAME, LOC. 3NF tables: EMP(EMPNO, ENAME, SAL, DEPTNO) and DEPT(DEPTNO, DNAME, LOC). This is exactly how the EMP and DEPT tables of the SCOTT schema are designed.</p>
<p>In SQL, an existing table can be split with CREATE TABLE ... AS SELECT DISTINCT:</p>
@@s_dept3@@
""", diagram="db3_3nf", examples=["n3_3", "n3_6"], programs=["q3_5"]),
        T("Boyce-Codd Normal Form (BCNF)", """
<p><b>BCNF</b> is a stronger version of 3NF. A relation is in BCNF if for every non-trivial FD X → Y, <b>X is a super key</b>. That is, every determinant must be a candidate key.</p>
<p>3NF allows X → A when A is a prime attribute; BCNF does not. So every BCNF relation is in 3NF, but a 3NF relation may not be in BCNF.</p>
<p><b>Example:</b> TEACH(STUDENT, SUBJECT, TEACHER), where each teacher teaches only one subject (TEACHER → SUBJECT) and (STUDENT, SUBJECT) → TEACHER. The candidate keys are (STUDENT, SUBJECT) and (STUDENT, TEACHER), so all attributes are prime and the relation is in 3NF. But TEACHER is not a super key, so it is <b>not in BCNF</b>. Decompose into (TEACHER, SUBJECT) and (STUDENT, TEACHER).</p>
<p>BCNF decomposition is always lossless but may not preserve all dependencies, which is why 3NF is often accepted in practice.</p>
"""),
        T("Normalization: Complete Example (UNF to 3NF)", """
<p>Normalization of a real table is done in a fixed order. Write down the FDs first, then apply each normal form in turn.</p>
<ol><li><b>UNF → 1NF:</b> remove repeating groups; make every value atomic; find the primary key.</li>
<li><b>1NF → 2NF:</b> remove partial dependencies (part of key → non-key).</li>
<li><b>2NF → 3NF:</b> remove transitive dependencies (non-key → non-key).</li>
<li><b>Check:</b> each final table has a primary key; foreign keys link the tables; a natural join of the tables gives back the original data (lossless).</li></ol>
<p>A student-course database, for example, ends with three tables: STUDENT(ROLL, NAME), COURSE(CID, CNAME, FEES) and ENROLL(ROLL, CID). A new course can be added without students, a fee is changed in one row, and deleting an enrolment never deletes course data.</p>
<p>The worked examples below show a complete order bill normalized to four tables, and an abstract relation normalized step by step.</p>
""", examples=["n3_4"], programs=["q3_3", "q3_4"]),
    ],
}

SEC_3_3 = {
    "title": {"en": "3.3 Advantages and Disadvantages of Normalization"},
    "items": [
        T("Advantages and Disadvantages of Normalization", """
<h4>Advantages</h4>
<ul><li><b>Less redundancy:</b> each fact is stored only once, which saves storage.</li>
<li><b>No anomalies:</b> insertion, update and deletion anomalies are removed.</li>
<li><b>Data consistency and integrity:</b> one copy of the data cannot disagree with itself; keys enforce relationships.</li>
<li><b>Easier maintenance:</b> changes are made in one place.</li>
<li><b>Better design:</b> each table represents one entity, so the database is easy to understand and extend.</li>
<li><b>Smaller tables:</b> indexes and searches on small tables are faster, and fewer NULL values are stored.</li>
<li><b>Flexible queries:</b> data can be combined in many ways using joins.</li></ul>
<h4>Disadvantages</h4>
<ul><li><b>More tables:</b> the number of tables increases, so the design looks complex.</li>
<li><b>More joins:</b> queries need joins to combine data, which can reduce performance for reports.</li>
<li><b>Harder to write queries</b> for beginners.</li>
<li><b>Requires skill:</b> correct FDs and keys must be identified; this takes time and a good understanding of the data.</li>
<li>Over-normalization (beyond 3NF / BCNF) may give little benefit for extra complexity.</li></ul>
"""),
        T("Decomposition: Lossless Join and Dependency Preservation", """
<p><b>Decomposition</b> means replacing a relation R by two or more relations R1, R2, ... such that every attribute of R appears in at least one of them. A good decomposition has two properties.</p>
<h4>1. Lossless-join decomposition</h4>
<p>Joining R1 and R2 gives back <b>exactly</b> the original R: no rows are lost and no extra (spurious) rows appear. <b>Test:</b> the decomposition of R into R1 and R2 is lossless if the common attributes R1 ∩ R2 form a key (super key) of R1 or of R2.</p>
<p>Example: EMP(EMPNO, ENAME, DEPTNO) and DEPT(DEPTNO, DNAME, LOC). The common attribute DEPTNO is the key of DEPT, so the decomposition is lossless. Splitting into (EMPNO, ENAME) and (DNAME, LOC) would be lossy, because there is no common attribute to join on.</p>
<h4>2. Dependency-preserving decomposition</h4>
<p>Every FD of the original relation can be checked within a single decomposed relation (or derived from the FDs of the decomposed relations), so constraints can be enforced without joins.</p>
<p>Decomposition into 3NF can always be done so that it is both lossless and dependency-preserving. BCNF is always lossless but may not preserve all dependencies.</p>
"""),
        T("Denormalization", """
<p><b>Denormalization</b> is the deliberate process of adding some redundancy back into a normalized database (for example, combining tables or storing calculated values) to <b>improve read (query) performance</b>.</p>
<p><b>When it is used:</b> reporting systems and data warehouses, where data is read far more often than it is updated, and joining many tables is slow.</p>
<p><b>Examples:</b></p>
<ul><li>Storing DNAME in an EMP report table to avoid joining DEPT.</li>
<li>Storing a TOTAL_AMOUNT column in ORDERS instead of summing ORDER_ITEM rows every time.</li></ul>
<table><tr><th>Normalization</th><th>Denormalization</th></tr>
<tr><td>Removes redundancy</td><td>Adds controlled redundancy</td></tr>
<tr><td>More tables, more joins</td><td>Fewer tables, fewer joins</td></tr>
<tr><td>Faster insert, update and delete</td><td>Faster SELECT (reports)</td></tr>
<tr><td>Better consistency</td><td>Risk of inconsistency</td></tr>
<tr><td>Used in OLTP (transaction) systems</td><td>Used in OLAP / data warehouses</td></tr></table>
<p>Denormalization is done <b>after</b> normalization, never instead of it.</p>
"""),
    ],
}

NOTES = [SEC_3_1, SEC_3_2, SEC_3_3]
