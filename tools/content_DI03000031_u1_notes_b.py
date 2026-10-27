"""DI03000031 Unit 1 notes part B: 1.5 DDL, DML, DQL, 1.6 DCL, 1.7 TCL and transactions."""
from sql_content import make_TS

SN = {
    "s_createdb": """
CREATE DATABASE college;   -- MySQL style

-- Oracle: a database is created once by
-- the DBA (DBCA tool); users then create
-- schemas (users) and tables in it.
CREATE USER college IDENTIFIED BY pwd;
""",
    "s_create": """
CREATE TABLE table_name (
  column1 datatype [constraint],
  column2 datatype [constraint],
  ...
  [table_constraints]
);
""",
    "s_alter": """
ALTER TABLE t ADD (col datatype, ...);
ALTER TABLE t MODIFY (col new_datatype);
ALTER TABLE t DROP COLUMN col;
ALTER TABLE t RENAME COLUMN old TO new;
ALTER TABLE t RENAME TO new_name;
RENAME old_name TO new_name;
""",
    "s_drop": """
DROP TABLE table_name;
DROP TABLE table_name PURGE;
TRUNCATE TABLE table_name;
""",
    "s_insert": """
INSERT INTO t VALUES (v1, v2, ...);

INSERT INTO t (col1, col2)
VALUES (v1, v2);

INSERT INTO t (col1, col2)
SELECT c1, c2 FROM other WHERE ...;
""",
    "s_update": """
UPDATE table_name
SET col1 = value1, col2 = value2
[WHERE condition];
""",
    "s_delete": """
DELETE FROM table_name
[WHERE condition];
""",
    "s_select": """
SELECT [DISTINCT] col1 [AS alias], ...
FROM table_name
[WHERE condition]
[GROUP BY columns]
[HAVING group_condition]
[ORDER BY columns [ASC|DESC]];
""",
    "s_user": """
CREATE USER username
  IDENTIFIED BY password;
ALTER USER username
  IDENTIFIED BY new_password;
DROP USER username CASCADE;
""",
    "s_grant": """
GRANT privilege_list
ON object_name
TO user | role | PUBLIC
[WITH GRANT OPTION];

GRANT system_privilege TO user;
""",
    "s_revoke": """
REVOKE privilege_list
ON object_name
FROM user | role | PUBLIC;
""",
    "s_role": """
CREATE ROLE role_name;
GRANT privileges ON table TO role_name;
GRANT role_name TO user1, user2;
REVOKE role_name FROM user1;
DROP ROLE role_name;
""",
    "s_tcl": """
COMMIT [WORK];
ROLLBACK [WORK];
SAVEPOINT savepoint_name;
ROLLBACK TO [SAVEPOINT] savepoint_name;
""",
    "s_bank": """
UPDATE account SET bal = bal - 500
WHERE acno = 'A';
UPDATE account SET bal = bal + 500
WHERE acno = 'B';
COMMIT;
""",
}

T = make_TS(SN)

SEC_1_5 = {
    "title": {"en": "1.5 SQL Commands: DDL, DML and DQL"},
    "items": [
        T("Classification of SQL Commands", """
<p>SQL commands are divided into five groups according to their purpose:</p>
<table><tr><th>Group</th><th>Purpose</th><th>Commands</th></tr>
<tr><td><b>DDL</b> Data Definition Language</td><td>Create/change/remove the structure of objects</td><td>CREATE, ALTER, DROP, TRUNCATE, RENAME</td></tr>
<tr><td><b>DML</b> Data Manipulation Language</td><td>Add, change, remove rows</td><td>INSERT, UPDATE, DELETE</td></tr>
<tr><td><b>DQL</b> Data Query Language</td><td>Retrieve data</td><td>SELECT</td></tr>
<tr><td><b>DCL</b> Data Control Language</td><td>Give/take privileges</td><td>GRANT, REVOKE</td></tr>
<tr><td><b>TCL</b> Transaction Control Language</td><td>Manage transactions</td><td>COMMIT, ROLLBACK, SAVEPOINT</td></tr></table>
<p>Note: DDL and DCL commands are <b>auto-committed</b> in Oracle; DML changes stay temporary until COMMIT.</p>
""", diagram="db1_sql_cmds"),
        T("DDL: CREATE DATABASE and CREATE TABLE", """
<p><b>CREATE DATABASE</b> creates a new, empty database. In MySQL/SQL Server it is used often. In Oracle, the database is created once by the DBA (using the DBCA tool or the CREATE DATABASE statement), and each user works in their own <b>schema</b> inside it.</p>
@@s_createdb@@
<p><b>CREATE TABLE</b> creates a new table: its name, its columns with data types and sizes, and optional constraints.</p>
@@s_create@@
<ul><li>A table name must be unique in the schema and must not be a reserved word.</li>
<li>Each column needs a name and a data type; the size is given in brackets.</li>
<li>Constraints (PRIMARY KEY, NOT NULL ...) can be written with a column or at the end (studied in Unit 4).</li>
<li><code>DESC table_name</code> shows the structure of the table.</li>
<li>A table can also be created from another table: <code>CREATE TABLE new AS SELECT ...</code></li></ul>
""", programs=["q1_1", "q1_10"]),
        T("DDL: ALTER TABLE and RENAME", """
<p><b>ALTER TABLE</b> changes the structure of an existing table without losing its data.</p>
@@s_alter@@
<ul><li><b>ADD:</b> adds one or more new columns (at the end). Old rows get NULL in them.</li>
<li><b>MODIFY:</b> changes the data type or size of a column. Size can be decreased, or the type changed, only if the existing data fits.</li>
<li><b>DROP COLUMN:</b> removes a column and its data.</li>
<li><b>RENAME COLUMN:</b> changes a column name.</li>
<li><b>RENAME TO / RENAME:</b> changes the table name.</li>
<li>ALTER is also used to add or drop constraints: <code>ALTER TABLE t ADD CONSTRAINT ...</code></li></ul>
""", programs=["q1_3", "q1_4"]),
        T("DDL: DROP and TRUNCATE (and DELETE)", """
@@s_drop@@
<ul><li><b>DROP TABLE</b> removes the whole table: its structure, data, indexes and constraints. In Oracle 10g+ it goes to the recycle bin (<code>PURGE</code> removes it permanently).</li>
<li><b>TRUNCATE TABLE</b> removes <b>all rows</b> quickly but keeps the structure. Storage is released and it cannot be rolled back.</li></ul>
<h4>DELETE vs TRUNCATE vs DROP</h4>
<table><tr><th>DELETE</th><th>TRUNCATE</th><th>DROP</th></tr>
<tr><td>DML</td><td>DDL</td><td>DDL</td></tr>
<tr><td>Removes selected rows (WHERE allowed)</td><td>Removes all rows</td><td>Removes rows + structure</td></tr>
<tr><td>Can be rolled back</td><td>Cannot be rolled back</td><td>Cannot be rolled back (Flashback possible)</td></tr>
<tr><td>Slow: logs every row</td><td>Fast</td><td>Fast</td></tr>
<tr><td>Fires DELETE triggers</td><td>No triggers</td><td>No triggers</td></tr>
<tr><td>Structure stays</td><td>Structure stays</td><td>Table no longer exists</td></tr></table>
""", programs=["q1_5"]),
        T("DML: INSERT", """
<p><b>INSERT</b> adds new rows to a table.</p>
@@s_insert@@
<ul><li>Without a column list, values must be given for <b>all</b> columns in table order.</li>
<li>With a column list, unlisted columns get NULL (or their DEFAULT value).</li>
<li>Strings and dates are enclosed in single quotes. A date can be written as <code>'15-AUG-2024'</code> or with <code>TO_DATE('15-08-2024','DD-MM-YYYY')</code>.</li>
<li><b>Substitution variables</b> (<code>&amp;var</code>) make SQL*Plus ask for values, so many rows can be inserted with one statement (run again with <code>/</code>).</li>
<li><code>INSERT INTO ... SELECT</code> copies rows from another table.</li></ul>
""", programs=["q1_6", "q1_7"]),
        T("DML: UPDATE", """
<p><b>UPDATE</b> modifies the values of existing rows.</p>
@@s_update@@
<ul><li>SET gives the new values; more than one column can be changed at a time.</li>
<li>The new value can be an expression using the old value: <code>SET sal = sal * 1.10</code>.</li>
<li>WHERE selects the rows to change. <b>If WHERE is omitted, all rows are updated.</b></li>
<li>Oracle reports how many rows were updated.</li></ul>
""", programs=["q1_8"]),
        T("DML: DELETE", """
<p><b>DELETE</b> removes rows from a table.</p>
@@s_delete@@
<ul><li>Only the rows satisfying WHERE are removed; without WHERE <b>all rows</b> are deleted, but the table remains.</li>
<li>A whole row is deleted; to clear only one column, use <code>UPDATE ... SET col = NULL</code>.</li>
<li>DELETE can be undone by ROLLBACK until COMMIT.</li></ul>
""", programs=["q1_9"]),
        T("DQL: SELECT, WHERE and DISTINCT", """
<p><b>SELECT</b> retrieves data from one or more tables. It never changes data. Full form:</p>
@@s_select@@
<ul><li><code>SELECT *</code> shows all columns; otherwise list the required columns.</li>
<li><b>Expressions</b> (<code>sal * 12</code>) are calculated for each row in the output only.</li>
<li><b>Column alias</b>: <code>expr AS name</code> or <code>expr "Any Name"</code> sets the heading.</li>
<li><b>WHERE</b> filters rows using comparison operators (=, &lt;&gt; or !=, &gt;, &lt;, &gt;=, &lt;=) and logical operators (AND, OR, NOT).</li>
<li><b>DISTINCT</b> removes duplicate rows from the result.</li>
<li>The order of execution is: FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY.</li></ul>
<p>Operators, functions, ORDER BY, GROUP BY and joins are covered in Unit 2.</p>
""", programs=["q1_11", "q1_12", "q1_13"]),
    ],
}

SEC_1_6 = {
    "title": {"en": "1.6 DCL: Users, Roles, GRANT and REVOKE"},
    "items": [
        T("Creating and Managing Users", """
<p>Every person who connects to Oracle needs a <b>user account</b> (username + password). In Oracle, each user also owns a <b>schema</b>: the set of objects (tables, views ...) created by that user. Users are created by the DBA (SYS/SYSTEM).</p>
@@s_user@@
<ul><li>A new user cannot even log in until given the <code>CREATE SESSION</code> privilege.</li>
<li><code>DROP USER ... CASCADE</code> also drops all objects owned by the user.</li>
<li>A user accesses another user's table as <code>owner.table</code>, e.g. <code>scott.emp</code>.</li></ul>
"""),
        T("Privileges and Roles", """
<p>A <b>privilege</b> is the right to run a particular SQL statement or to access an object.</p>
<ul><li><b>System privileges:</b> the right to perform an action in the database: CREATE SESSION, CREATE TABLE, CREATE VIEW, CREATE USER, DROP ANY TABLE ...</li>
<li><b>Object privileges:</b> the right to perform an action on a specific object: SELECT, INSERT, UPDATE, DELETE, ALTER, INDEX, REFERENCES on a table; EXECUTE on a procedure.</li></ul>
<p>A <b>role</b> is a named group of related privileges that can be granted to users. When privileges change, only the role is changed and all its users get the change. Predefined roles: CONNECT, RESOURCE, DBA.</p>
@@s_role@@
<h4>Advantages of roles</h4>
<ul><li>Easy privilege management for many users</li>
<li>Dynamic: changing the role affects all its users</li>
<li>Can be enabled/disabled and protected with a password</li></ul>
""", diagram="db1_dcl"),
        T("GRANT and REVOKE", """
<p><b>GRANT</b> gives privileges to users or roles.</p>
@@s_grant@@
<ul><li><code>ALL</code> grants all object privileges; <code>PUBLIC</code> means every user.</li>
<li><b>WITH GRANT OPTION</b>: the receiver can grant the same privilege to others (for object privileges). For system privileges use <code>WITH ADMIN OPTION</code>.</li>
<li>UPDATE can be limited to columns: <code>GRANT UPDATE (marks) ON student TO ravi;</code></li></ul>
<p><b>REVOKE</b> takes back privileges that were granted.</p>
@@s_revoke@@
<ul><li>Only the grantor (or the DBA) can revoke.</li>
<li>Revoking an object privilege that was given WITH GRANT OPTION also removes it from the users to whom it was passed on (cascading).</li></ul>
""", programs=["q1_14"]),
    ],
}

SEC_1_7 = {
    "title": {"en": "1.7 TCL: Transactions, ACID, COMMIT, ROLLBACK, SAVEPOINT"},
    "items": [
        T("Transaction and ACID Properties", """
<p>A <b>transaction</b> is a logical unit of work that contains one or more SQL statements and must be completed <b>fully or not at all</b>. Example: transferring money is one transaction of two updates.</p>
@@s_bank@@
<p>If the system fails after the first UPDATE, Rs 500 would vanish. The DBMS prevents this by guaranteeing the <b>ACID</b> properties:</p>
<ol><li><b>Atomicity:</b> all operations of the transaction are done, or none are. If any part fails, everything is rolled back. (Handled by the transaction/recovery manager using undo logs.)</li>
<li><b>Consistency:</b> a transaction takes the database from one valid state to another valid state. All constraints remain true (the total of A + B stays the same).</li>
<li><b>Isolation:</b> concurrently running transactions do not see each other's uncommitted changes; the result is as if they ran one after another. (Handled by concurrency control/locking.)</li>
<li><b>Durability:</b> once a transaction is committed, its changes are permanent and survive power failures or crashes. (Handled by redo logs and backups.)</li></ol>
<p>In Oracle, a transaction starts with the first DML statement and ends with COMMIT, ROLLBACK, a DDL/DCL statement (auto-commit) or the end of the session.</p>
""", diagram="db1_acid"),
        T("States of a Transaction", """
<ol><li><b>Active:</b> the initial state; the statements are being executed.</li>
<li><b>Partially committed:</b> the last statement has been executed, but the changes are still in memory buffers.</li>
<li><b>Committed:</b> the changes are written permanently to the database after successful completion.</li>
<li><b>Failed:</b> normal execution cannot continue (error, constraint violation, system crash).</li>
<li><b>Aborted:</b> the transaction is rolled back and the database is restored to its state before the transaction. It may then be <b>restarted</b> or <b>killed</b>.</li></ol>
<p>Committed and aborted are the <b>terminated</b> states.</p>
""", diagram="db1_tx_states"),
        T("COMMIT and ROLLBACK", """
@@s_tcl@@
<ul><li><b>COMMIT:</b> ends the current transaction and makes all its changes <b>permanent</b> and visible to other users. Locks are released and savepoints are erased.</li>
<li><b>ROLLBACK:</b> ends the current transaction and <b>undoes</b> all changes made since the last COMMIT.</li>
<li><b>Implicit (automatic) COMMIT</b> happens when a DDL or DCL statement runs or on a normal exit from SQL*Plus. <code>SET AUTOCOMMIT ON</code> commits after every DML statement.</li>
<li><b>Implicit ROLLBACK</b> happens on an abnormal end of the session or a system failure.</li>
<li>Before COMMIT, other users still see the old data, and the changed rows are locked.</li></ul>
""", programs=["q1_15", "q1_17"]),
        T("SAVEPOINT and ROLLBACK TO SAVEPOINT", """
<p>A <b>SAVEPOINT</b> is a named marker inside a transaction. It divides a long transaction into smaller parts so that you can undo only a part of it.</p>
<ul><li><code>SAVEPOINT name;</code> creates the marker.</li>
<li><code>ROLLBACK TO name;</code> undoes only the changes made <b>after</b> that savepoint. The transaction is still active; earlier changes are kept (not yet committed).</li>
<li>Savepoints after the one rolled back to are erased; the named savepoint itself remains.</li>
<li>Creating a savepoint with an existing name moves it to the new position.</li>
<li><code>COMMIT</code> or a plain <code>ROLLBACK</code> erases all savepoints.</li></ul>
""", diagram="db1_savepoint", programs=["q1_16"]),
    ],
}

NOTES_B = [SEC_1_5, SEC_1_6, SEC_1_7]
