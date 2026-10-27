"""DI03000031 Unit 1 extras: syntax sheet, viva, exam questions."""
from sql_content import SXE, VE, XE, G
from content_DI03000031_u1_notes_b import SN


def S(name, key, terms=""):
    return SXE(name, SN[key].strip("\n"), terms)


SYNTAX = [
    G("DDL – Data Definition", [
        S("CREATE TABLE", "s_create", "Defines a new table. DESC table_name shows its structure."),
        SXE("CREATE TABLE ... AS SELECT", "CREATE TABLE new_t AS\nSELECT cols FROM old_t\n[WHERE condition];",
            "Copies structure and rows. WHERE 1 = 2 copies only the structure."),
        S("ALTER TABLE", "s_alter", "Changes structure: add, modify, drop or rename columns; rename the table."),
        S("DROP and TRUNCATE", "s_drop", "DROP removes table + data. TRUNCATE removes all rows, keeps structure."),
        SXE("DESCRIBE", "DESC table_name", "SQL*Plus command; shows Name, Null? and Type."),
    ]),
    G("DML and DQL", [
        S("INSERT", "s_insert", "Adds rows. Use &var for substitution variables and / to run again."),
        S("UPDATE", "s_update", "Changes values. Without WHERE all rows are updated."),
        S("DELETE", "s_delete", "Removes rows. Can be rolled back before COMMIT."),
        S("SELECT", "s_select", "Retrieves data. Execution order: FROM, WHERE, GROUP BY, HAVING, SELECT, ORDER BY."),
    ]),
    G("DCL – Data Control", [
        S("Users", "s_user", "Run as DBA. A new user needs CREATE SESSION to log in."),
        S("GRANT", "s_grant", "WITH GRANT OPTION allows the user to pass the privilege on."),
        S("REVOKE", "s_revoke", "Takes back a privilege; cascades for object privileges."),
        S("Roles", "s_role", "A role is a named group of privileges."),
    ]),
    G("TCL – Transaction Control", [
        S("COMMIT / ROLLBACK / SAVEPOINT", "s_tcl", "DDL and DCL commit automatically in Oracle."),
    ]),
]

VIVA = [
    G("Data, Database and DBMS", [
        VE("What is the difference between data and information?", "Data is raw, unprocessed facts. Information is processed, meaningful data used for decision making."),
        VE("What is metadata?", "Data about data, e.g. table names, column names, data types and constraints."),
        VE("What is a data dictionary?", "A set of system tables (system catalog) where the DBMS stores all metadata. In Oracle it is read through views like USER_TABLES."),
        VE("Define field, record and file.", "Field: smallest named unit of data. Record: collection of related fields about one entity. File: collection of similar records."),
        VE("What is a DBMS? Give examples.", "Software to create, store, retrieve and manage a database. Examples: Oracle, MySQL, SQL Server, PostgreSQL."),
        VE("What is an RDBMS?", "A DBMS based on the relational model in which data is stored in related tables of rows and columns, e.g. Oracle."),
        VE("Who proposed the relational model?", "Dr. E. F. Codd of IBM, in 1970."),
        VE("Name two disadvantages of the file system.", "Data redundancy and data inconsistency (also difficult access, poor security, no concurrency)."),
        VE("Who is a DBA?", "The Database Administrator: the person with central control who designs the schema, manages users and privileges, and takes backups."),
        VE("What are the three levels of the ANSI/SPARC architecture?", "External (view) level, conceptual (logical) level and internal (physical) level."),
        VE("What is data independence?", "The ability to change the schema at one level without changing the next higher level. It has two types: logical and physical."),
        VE("What is the difference between a schema and an instance?", "A schema is the structure/design of the database (changes rarely); an instance is the data stored at a particular moment (changes often)."),
        VE("What is a sub-schema?", "A part of the schema visible to a particular user or application; created as a view in SQL."),
    ]),
    G("SQL Commands", [
        VE("What is SQL?", "Structured Query Language: the standard non-procedural language for relational databases."),
        VE("What is the difference between CHAR and VARCHAR2?", "CHAR is fixed length and padded with spaces (max 2000 bytes); VARCHAR2 is variable length (max 4000 bytes)."),
        VE("What does NUMBER(7,2) mean?", "7 total digits with 2 after the decimal point; maximum value 99999.99."),
        VE("Name the DDL commands.", "CREATE, ALTER, DROP, TRUNCATE and RENAME."),
        VE("Name the DML commands.", "INSERT, UPDATE and DELETE."),
        VE("What is the difference between DELETE and TRUNCATE?", "DELETE is DML, can use WHERE and can be rolled back. TRUNCATE is DDL, removes all rows and cannot be rolled back."),
        VE("What is the difference between DROP and TRUNCATE?", "DROP removes the table structure and data; TRUNCATE removes only the data and keeps the structure."),
        VE("What happens if WHERE is omitted in UPDATE?", "All rows of the table are updated."),
        VE("What is the use of DISTINCT?", "It removes duplicate rows from the result of a SELECT."),
        VE("How do you see the structure of a table?", "With the DESC (DESCRIBE) table_name command."),
        VE("What is a substitution variable?", "A variable written as &name in SQL*Plus; the user is asked to enter its value when the statement runs."),
    ]),
    G("DCL and TCL", [
        VE("What is the use of GRANT and REVOKE?", "GRANT gives privileges to users or roles; REVOKE takes them back."),
        VE("What is a role?", "A named group of privileges that can be granted to many users at once."),
        VE("Difference between system and object privileges?", "System privileges allow actions in the database (CREATE TABLE); object privileges allow actions on a specific object (SELECT on emp)."),
        VE("What is WITH GRANT OPTION?", "It allows the user who receives an object privilege to grant it to other users."),
        VE("What is a transaction?", "A logical unit of work made of one or more SQL statements that is completed entirely or not at all."),
        VE("Expand ACID.", "Atomicity, Consistency, Isolation and Durability."),
        VE("What does COMMIT do?", "It makes all changes of the current transaction permanent and ends the transaction."),
        VE("What does ROLLBACK do?", "It undoes all changes since the last COMMIT."),
        VE("What is a SAVEPOINT?", "A named marker inside a transaction; ROLLBACK TO savepoint undoes only the work after it."),
        VE("Can a DROP TABLE be rolled back?", "No. DDL commands commit automatically. (In Oracle 10g+ it can be restored with FLASHBACK TABLE ... TO BEFORE DROP.)"),
    ]),
]

EXAM_QS = [
    XE("Define: (i) Data (ii) Information (iii) Metadata.", 3),
    XE("Differentiate between data and information.", 3),
    XE("Explain data item, record and file with an example.", 3),
    XE("What is a data dictionary? List its contents.", 3),
    XE("Explain the disadvantages of the file processing system.", 4),
    XE("List the advantages and disadvantages of a DBMS.", 4),
    XE("Explain the database system environment with a diagram.", 4),
    XE("Explain the three-level architecture of a DBMS with a neat diagram.", 7),
    XE("What is data independence? Explain its types.", 4),
    XE("Define schema, sub-schema and instance. Differentiate schema and instance.", 4),
    XE("Explain any five data types of Oracle SQL. Differentiate CHAR and VARCHAR2.", 4),
    XE("Classify SQL commands and explain DDL commands with syntax and examples.", 7),
    XE("Explain INSERT, UPDATE and DELETE commands with examples.", 4),
    XE("Differentiate DELETE, TRUNCATE and DROP.", 3),
    XE("Explain GRANT and REVOKE commands with syntax and examples.", 4),
    XE("What is a transaction? Explain the ACID properties.", 4),
    XE("Explain the states of a transaction with a diagram.", 3),
    XE("Explain COMMIT, ROLLBACK and SAVEPOINT with examples.", 7),
]
