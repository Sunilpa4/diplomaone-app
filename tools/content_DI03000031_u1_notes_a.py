"""DI03000031 Unit 1 notes part A: 1.1 data and information, 1.2 database concepts and architecture, 1.3 schema, 1.4 SQL data types."""
from sql_content import make_TS

SN = {
    "dict_q": """
SELECT table_name
FROM user_tables;

SELECT column_name, data_type
FROM user_tab_columns
WHERE table_name = 'STUDENT';
""",
    "types_eg": """
CREATE TABLE product (
  pid    NUMBER(5),
  pname  VARCHAR2(30),
  grade  CHAR(1),
  price  NUMBER(8,2),
  mfg_dt DATE,
  photo  BLOB
);
""",
}

T = make_TS(SN)

SEC_1_1 = {
    "title": {"en": "1.1 Data, Information and Metadata"},
    "items": [
        T("Data and Information", """
<p><b>Data</b> are raw, unorganised facts and figures (numbers, text, images, sound) that have no meaning by themselves. Example: <code>82, Aarav, Surat, CE</code>.</p>
<p><b>Information</b> is data that has been <b>processed</b> (organised, classified, calculated) so that it is meaningful and useful for decision making. Example: "Aarav of CE scored 82 marks and stood 2nd in the class."</p>
<p><b>Processing</b> steps: collecting → recording → classifying → sorting → calculating → summarising → reporting.</p>
<h4>Difference between data and information</h4>
<table><tr><th>Data</th><th>Information</th></tr>
<tr><td>Raw facts</td><td>Processed data</td></tr>
<tr><td>Unorganised</td><td>Organised and structured</td></tr>
<tr><td>No meaning alone</td><td>Meaningful in a context</td></tr>
<tr><td>Input to processing</td><td>Output of processing</td></tr>
<tr><td>Not useful for decisions</td><td>Helps in decision making</td></tr>
<tr><td>Example: 35, 42, 28</td><td>Average temperature = 35 °C</td></tr></table>
<p>The information produced by one process can become the data for another process (e.g. the marks of each subject → total → class rank).</p>
<p><b>Qualities of good information:</b> accurate, complete, timely, relevant, easy to understand and cost-effective.</p>
""", diagram="db1_data_info"),
        T("Data Item, Record, File and Database", """
<p>Data in a database are organised in a hierarchy, from the smallest unit to the largest:</p>
<ol><li><b>Data item (field / attribute / column):</b> the smallest named unit of data that has meaning. Example: <code>NAME = 'Diya Shah'</code>. A data item has a name, a type and a size.</li>
<li><b>Record (tuple / row):</b> a collection of related data items about one entity (one student, one employee). Example: <code>(2, 'Diya Shah', 'IT', 91)</code>.</li>
<li><b>File (table / relation):</b> a collection of records of the same type. Example: the STUDENT file holds the records of all students.</li>
<li><b>Database:</b> a collection of logically related files. Example: a college database has STUDENT, FACULTY, COURSE and RESULT files.</li></ol>
<p>Other terms:</p>
<ul><li><b>Entity:</b> a real-world object about which data is stored (student, book, account).</li>
<li><b>Key field:</b> a field whose value uniquely identifies each record (roll number, account number).</li>
<li>In relational terms: table = relation, row = tuple, column = attribute, number of columns = degree, number of rows = cardinality.</li></ul>
""", diagram="db1_hierarchy"),
        T("Metadata and Data Dictionary", """
<p><b>Metadata</b> means <b>"data about data"</b>. It describes the data instead of being the data itself: table names, column names, data types, sizes, constraints, indexes, owners, privileges, creation date, etc.</p>
<p>Example: "NAME is VARCHAR2(15) and NOT NULL" is metadata; "Diya Shah" is data.</p>
<p>The <b>data dictionary</b> (system catalog) is a set of special tables in which the DBMS stores all the metadata of the database. It is created and updated <b>automatically</b> by the DBMS whenever a DDL command (CREATE, ALTER, DROP) runs. Users can only read it.</p>
<h4>Contents of the data dictionary</h4>
<ul><li>Names and structure of all tables, views, indexes, sequences and synonyms</li>
<li>Column names, data types, sizes and default values</li>
<li>Integrity constraints (primary key, foreign key, check ...)</li>
<li>Users, roles and their privileges</li>
<li>Storage and audit information</li></ul>
<h4>Types</h4>
<ul><li><b>Active (integrated):</b> managed by the DBMS itself and updated automatically. Oracle's dictionary is active.</li>
<li><b>Passive (non-integrated):</b> kept separately (e.g. as documents) and updated manually.</li></ul>
<p>In Oracle the dictionary is read through views such as <code>USER_TABLES</code>, <code>USER_TAB_COLUMNS</code>, <code>USER_CONSTRAINTS</code>, <code>ALL_TABLES</code> and <code>DBA_USERS</code>. The <code>DESC</code> command also reads it.</p>
@@dict_q@@
<p><b>Uses:</b> the DBMS checks every query against it (does the table exist? does the user have the privilege?), and it documents the database for DBAs and developers.</p>
""", diagram="db1_dictionary"),
    ],
}

SEC_1_2 = {
    "title": {"en": "1.2 Database Concepts, Environment and Architecture"},
    "items": [
        T("Database, DBMS and RDBMS", """
<p><b>Database:</b> a shared, integrated collection of logically related data, stored with minimum redundancy, that serves the needs of many users. Example: a bank database (customers, accounts, transactions).</p>
<p><b>DBMS (Database Management System):</b> software that is used to <b>create, store, retrieve, update and manage</b> a database. It acts as an interface between the users/application programs and the database. Examples: Oracle, MySQL, Microsoft SQL Server, PostgreSQL, IBM DB2, MS Access.</p>
<p><b>Database system</b> = database + DBMS software + application programs + users.</p>
<p><b>RDBMS (Relational DBMS):</b> a DBMS based on the <b>relational model</b> of E. F. Codd (1970). The data is stored in <b>tables</b> (relations) of rows and columns, and the tables are related through common columns (keys). SQL is used to work with the data. Oracle, MySQL, SQL Server and PostgreSQL are RDBMSs.</p>
<h4>Functions / characteristics of a DBMS</h4>
<ul><li>Data definition: creates the structure (tables) using DDL</li>
<li>Data manipulation: insert, update, delete and query data</li>
<li>Data storage management and the data dictionary</li>
<li>Security: users, passwords and privileges</li>
<li>Integrity: constraints keep the data correct</li>
<li>Concurrency control: many users at the same time</li>
<li>Backup and recovery after failures</li>
<li>Transaction management (ACID)</li></ul>
<h4>DBMS vs RDBMS</h4>
<table><tr><th>DBMS</th><th>RDBMS</th></tr>
<tr><td>Data may be stored as files, hierarchy or network</td><td>Data stored in related tables</td></tr>
<tr><td>Relationships are not enforced</td><td>Keys enforce relationships</td></tr>
<tr><td>Normalization not required</td><td>Normalization supported</td></tr>
<tr><td>Usually single user, small data</td><td>Multi-user, large data</td></tr>
<tr><td>Example: file systems, XML stores</td><td>Oracle, MySQL, SQL Server</td></tr></table>
"""),
        T("File Processing System vs Database System", """
<p>Before DBMSs, each department kept its own data files and wrote its own programs to process them (the <b>file processing system</b>). This approach has many problems.</p>
<h4>Disadvantages of the file processing system</h4>
<ol><li><b>Data redundancy:</b> the same data (student name, address) is stored in many files, wasting space.</li>
<li><b>Data inconsistency:</b> when one copy is updated and another is not, the copies disagree.</li>
<li><b>Difficult data access:</b> a new program must be written for every new query.</li>
<li><b>Data isolation:</b> data are scattered in files of different formats.</li>
<li><b>Integrity problems:</b> rules (e.g. marks ≤ 100) are hidden inside program code and are hard to change.</li>
<li><b>Atomicity problems:</b> after a crash in the middle of an update, the data is left half-changed.</li>
<li><b>Concurrent access anomalies:</b> two users updating together can corrupt the data.</li>
<li><b>Security problems:</b> it is hard to give each user access to only part of the data.</li></ol>
<h4>Advantages of a DBMS</h4>
<ul><li>Controlled redundancy and better consistency</li>
<li>Data sharing among many users and applications</li>
<li>Integrity constraints enforced centrally</li>
<li>Security through users, roles and privileges</li>
<li>Backup and recovery, and transaction support</li>
<li>Easy querying with SQL; data independence</li>
<li>Standards can be enforced</li></ul>
<h4>Disadvantages of a DBMS</h4>
<ul><li>High cost of software, hardware and trained staff</li>
<li>Complex to design and manage; needs a DBA</li>
<li>A failure of the central database affects all users</li>
<li>Extra overhead, so it is slower than files for very small, simple jobs</li></ul>
""", diagram="db1_file_vs_db"),
        T("Applications of Database Systems", """
<ul><li><b>Banking:</b> customer accounts, loans, ATM and UPI transactions</li>
<li><b>Railway and airline reservation:</b> IRCTC bookings, seat availability, schedules</li>
<li><b>Universities:</b> student registration, GTU exam results, fees</li>
<li><b>Telecom:</b> call records, prepaid balance, monthly bills</li>
<li><b>E-commerce:</b> products, orders and payments (Amazon, Flipkart)</li>
<li><b>Hospitals:</b> patient records, doctors, billing</li>
<li><b>Government:</b> Aadhaar, income tax, voter lists</li>
<li><b>HR and payroll:</b> employee details, attendance, salaries</li>
<li><b>Social media:</b> profiles, posts, messages</li></ul>
"""),
        T("Database System Environment", """
<p>A database system has five main <b>components</b>:</p>
<ol><li><b>Hardware:</b> computers, storage disks, servers and network devices on which the database runs.</li>
<li><b>Software:</b> the DBMS itself, the operating system, network software and application programs.</li>
<li><b>Data:</b> the stored database (user data) and the metadata in the data dictionary.</li>
<li><b>Procedures:</b> rules and instructions for using and managing the system (login, backup, recovery steps).</li>
<li><b>Users (people):</b> everyone who interacts with the database.</li></ol>
<h4>Main parts of the DBMS software</h4>
<ul><li><b>Query processor:</b> DDL interpreter, DML compiler and query optimiser. It checks a query, chooses the best plan and runs it.</li>
<li><b>Storage manager:</b> file manager, buffer manager, authorisation and integrity manager. It moves data between disk and memory.</li>
<li><b>Transaction manager:</b> ensures ACID properties, concurrency control (locking) and recovery.</li>
<li><b>Data dictionary:</b> stores the metadata used by all the other parts.</li></ul>
""", diagram="db1_environment"),
        T("Database Users and the DBA", """
<h4>Types of database users</h4>
<ol><li><b>Naive (end) users:</b> use ready-made application screens without knowing SQL. Example: a bank clerk or an ATM user.</li>
<li><b>Application programmers:</b> write programs (Java, Python, PHP) that use the database through SQL.</li>
<li><b>Sophisticated / casual users:</b> analysts who write their own SQL queries or use reporting tools.</li>
<li><b>Specialised users:</b> write special database applications (CAD, expert systems).</li>
<li><b>Database Administrator (DBA):</b> the person with central control over the database.</li></ol>
<h4>Responsibilities of the DBA</h4>
<ul><li>Schema definition: designs and creates the database structure</li>
<li>Storage structure and access method definition (tablespaces, indexes)</li>
<li>Creating users and granting/revoking privileges (security)</li>
<li>Defining integrity constraints</li>
<li>Regular backup and recovery after failures</li>
<li>Monitoring and tuning performance</li>
<li>Installing and upgrading the DBMS software</li></ul>
"""),
        T("Three-Level Architecture (ANSI/SPARC) and Data Independence", """
<p>The ANSI/SPARC architecture separates the user's view of the database from the way the data is physically stored. It has <b>three levels</b>:</p>
<ol><li><b>External level (view level):</b> the highest level. Each user or group sees only the part of the database they need (a <b>view</b>). Example: the exam cell sees roll no., name and marks but not fees. There can be many external views.</li>
<li><b>Conceptual level (logical level):</b> describes the <b>whole database</b> for the community of users: all tables, columns, data types, relationships and constraints, without storage details. There is only one conceptual schema. It is designed by the DBA.</li>
<li><b>Internal level (physical level):</b> the lowest level. It describes <b>how</b> the data is actually stored on disk: file organisation, record layout, indexes, compression and access paths.</li></ol>
<p><b>Mappings</b> connect the levels: external/conceptual mapping and conceptual/internal mapping. The DBMS uses them to convert a user's request into operations on the stored data.</p>
<h4>Data independence</h4>
<p>The ability to change the schema at one level <b>without changing</b> the schema at the next higher level.</p>
<ul><li><b>Logical data independence:</b> the conceptual schema can be changed (e.g. a new column or table is added) without changing the external views or application programs.</li>
<li><b>Physical data independence:</b> the internal schema can be changed (e.g. a new index, a different disk, a new file organisation) without changing the conceptual schema.</li></ul>
<p>Physical data independence is easier to achieve than logical data independence.</p>
<h4>Objectives of the three-level architecture</h4>
<ul><li>Each user can see the data in their own way.</li>
<li>Users need not know storage details.</li>
<li>The DBA can change storage without affecting users.</li>
<li>It provides data independence and security.</li></ul>
""", diagram="db1_three_level"),
        T("Client-Server Architecture: 1-tier, 2-tier and 3-tier", """
<ul><li><b>1-tier:</b> the user, the application and the database are all on the same machine. Example: a student using Oracle SQL*Plus on a laptop to practise.</li>
<li><b>2-tier (client-server):</b> the client machine runs the application (user interface and logic); it talks directly to the database server using ODBC/JDBC. Example: a desktop billing application in a shop connected to a database server. It is simple, but it is difficult to scale and less secure.</li>
<li><b>3-tier:</b> the client (browser) → the <b>application server</b> (business logic, e.g. Java, PHP, Node.js) → the <b>database server</b>. The client never accesses the database directly. Used by web applications such as IRCTC and online banking. It is scalable, secure and easier to maintain.</li></ul>
<table><tr><th>2-tier</th><th>3-tier</th></tr>
<tr><td>Client talks to the DB directly</td><td>Client → app server → DB</td></tr>
<tr><td>Business logic on the client</td><td>Business logic on the app server</td></tr>
<tr><td>Fewer users, less secure</td><td>Many users, more secure</td></tr>
<tr><td>Desktop LAN applications</td><td>Web applications</td></tr></table>
"""),
    ],
}

SEC_1_3 = {
    "title": {"en": "1.3 Schema, Sub-schema and Instance"},
    "items": [
        T("Schema, Sub-schema and Instance", """
<p><b>Schema:</b> the overall <b>logical structure (design)</b> of the database: table names, column names, data types, keys, relationships and constraints. It is defined with DDL during design and changes rarely. It is like the plan of a building or a class in programming.</p>
<p>Example schema: <code>STUDENT(rollno, name, branch, city, marks)</code></p>
<p>By level there are three schemas: the <b>external schema</b> (views), the <b>conceptual (logical) schema</b> and the <b>internal (physical) schema</b>.</p>
<p><b>Sub-schema:</b> a <b>subset of the schema</b> that is visible to a particular user or application. It hides the rest of the data and gives security and simplicity. In SQL a sub-schema is created using a <b>view</b>. Example: the exam cell's sub-schema <code>(rollno, name, marks)</code>; the accounts section's sub-schema <code>(rollno, name, fees)</code>.</p>
<p><b>Instance (database state / snapshot):</b> the actual data stored in the database at a <b>particular moment</b>. Every INSERT, UPDATE or DELETE creates a new instance. The schema stays the same.</p>
<h4>Schema vs Instance</h4>
<table><tr><th>Schema</th><th>Instance</th></tr>
<tr><td>Structure / design of the DB</td><td>Data in the DB at one moment</td></tr>
<tr><td>Defined using DDL</td><td>Changed using DML</td></tr>
<tr><td>Changes rarely</td><td>Changes frequently</td></tr>
<tr><td>Like a class / blueprint</td><td>Like objects / a snapshot</td></tr>
<tr><td>Called the intension</td><td>Called the extension</td></tr></table>
""", diagram="db1_schema_instance"),
    ],
}

SEC_1_4 = {
    "title": {"en": "1.4 SQL and SQL Data Types"},
    "items": [
        T("Introduction to SQL", """
<p><b>SQL (Structured Query Language)</b>, pronounced "sequel", is the standard language used to create, manage and query relational databases. It was developed by IBM in the 1970s (as SEQUEL for System R) and is standardised by ANSI and ISO.</p>
<h4>Features of SQL</h4>
<ul><li><b>Non-procedural:</b> you say <i>what</i> data you want, not <i>how</i> to get it.</li>
<li>English-like, easy to learn commands (SELECT, INSERT, UPDATE ...)</li>
<li>One language for defining, manipulating, querying and controlling data</li>
<li>Portable: works on Oracle, MySQL, SQL Server, PostgreSQL (with small differences)</li>
<li>Can be embedded in programs (Java, Python, C) and extended with PL/SQL</li></ul>
<h4>Rules for writing SQL statements</h4>
<ul><li>Keywords are not case-sensitive: <code>SELECT</code> = <code>select</code>. But data inside quotes is case-sensitive.</li>
<li>A statement can span many lines and ends with a semicolon <code>;</code> in SQL*Plus.</li>
<li>Text and date values are written in single quotes: <code>'Surat'</code>.</li>
<li>Names (tables, columns) start with a letter, can have up to 30 characters (128 in Oracle 12.2+), and may contain letters, digits, _, $ and #.</li>
<li>Comments: <code>-- single line</code> and <code>/* multi line */</code>.</li></ul>
<p><b>Oracle tools:</b> SQL*Plus (command line), SQL Developer (GUI) and Oracle Live SQL (online).</p>
"""),
        T("SQL Data Types in Oracle", """
<p>Every column must have a <b>data type</b>, which decides what kind of values it can hold and how much space they take.</p>
<h4>Character types</h4>
<ul><li><b>CHAR(n):</b> fixed-length text of n characters (max 2000 bytes). Shorter values are padded with spaces. Use for fixed codes: gender 'M'/'F', state code 'GJ'.</li>
<li><b>VARCHAR2(n):</b> variable-length text of up to n characters (max 4000 bytes; 32767 with extended size). It stores only the actual characters, so there is no wasted space. This is the most used text type.</li>
<li><b>VARCHAR(n):</b> currently the same as VARCHAR2, but reserved by Oracle for future use, so use VARCHAR2.</li>
<li><b>NCHAR / NVARCHAR2:</b> Unicode text (for Gujarati, Hindi and other languages).</li>
<li><b>LONG:</b> variable text up to 2 GB (old type; only one per table; use CLOB instead).</li></ul>
<h4>Number type</h4>
<ul><li><b>NUMBER(p, s):</b> p = precision (total digits, 1 to 38), s = scale (digits after the decimal point). <code>NUMBER(7,2)</code> stores up to 99999.99.</li>
<li><code>NUMBER(5)</code> = whole numbers up to 5 digits. <code>NUMBER</code> alone = any number (floating).</li>
<li>INTEGER, INT, SMALLINT, DECIMAL and FLOAT are accepted and mapped to NUMBER.</li></ul>
<h4>Date and time types</h4>
<ul><li><b>DATE:</b> stores the date and time (century, year, month, day, hour, minute, second). The default display is <code>DD-MON-YY</code>, e.g. 28-OCT-26.</li>
<li><b>TIMESTAMP:</b> date and time with fractions of a second.</li>
<li><b>INTERVAL YEAR TO MONTH / DAY TO SECOND:</b> a period of time.</li></ul>
<h4>Large object (LOB) and binary types</h4>
<ul><li><b>CLOB:</b> large text (up to 128 TB), e.g. articles and descriptions.</li>
<li><b>BLOB:</b> large binary data such as images, audio and video.</li>
<li><b>BFILE:</b> a pointer to a binary file stored outside the database.</li>
<li><b>RAW(n) / LONG RAW:</b> small/large binary data.</li></ul>
<p><b>Others:</b> ROWID (the physical address of a row) and BOOLEAN (only in PL/SQL before 23ai).</p>
@@types_eg@@
<h4>CHAR vs VARCHAR2</h4>
<table><tr><th>CHAR(n)</th><th>VARCHAR2(n)</th></tr>
<tr><td>Fixed length</td><td>Variable length</td></tr>
<tr><td>Pads with spaces</td><td>No padding</td></tr>
<tr><td>Max 2000 bytes</td><td>Max 4000 bytes</td></tr>
<tr><td>Wastes space for short values</td><td>Saves space</td></tr>
<tr><td>Slightly faster for fixed data</td><td>Best for names, addresses</td></tr>
<tr><td>'GJ' in CHAR(5) = 'GJ   '</td><td>'GJ' in VARCHAR2(5) = 'GJ'</td></tr></table>
""", programs=["q1_2"]),
    ],
}

NOTES_A = [SEC_1_1, SEC_1_2, SEC_1_3, SEC_1_4]
