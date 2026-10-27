"""DI03000031 Unit 4 extras: syntax sheet, viva, exam questions."""
from sql_content import SXE, VE, XE, G
from content_DI03000031_u4_notes import SN


def S(name, key, terms=""):
    return SXE(name, SN[key].strip("\n"), terms)


SYNTAX = [
    G("Integrity Constraints", [
        S("Column and table level", "s_levels", "NOT NULL is column level only; composite keys are table level only."),
        S("NOT NULL", "s_notnull", "Error: ORA-01400 cannot insert NULL."),
        S("CHECK", "s_check", "Error: ORA-02290 check constraint violated."),
        S("UNIQUE", "s_unique", "Allows NULLs. Error: ORA-00001."),
        S("PRIMARY KEY", "s_pk", "UNIQUE + NOT NULL; only one per table."),
        S("FOREIGN KEY", "s_fk", "ORA-02291 parent key not found; ORA-02292 child record found."),
        S("Delete rules", "s_cascade", "CASCADE deletes child rows; SET NULL keeps them with NULL."),
        S("Add constraints", "s_alter_con", "Existing rows are validated first."),
        S("Drop / disable / enable", "s_drop_con", "CASCADE also drops (or disables) dependent foreign keys."),
        S("Data dictionary", "s_dict", "Types: P primary, U unique, R foreign, C check / NOT NULL."),
    ]),
    G("Views", [
        S("CREATE VIEW", "s_view", "A view stores only the query, not data."),
        S("Simple view", "s_view_ex"),
        S("Complex view", "s_complex", "DML not allowed with GROUP BY / DISTINCT (ORA-01732)."),
        S("CHECK OPTION / READ ONLY", "s_check_opt", "ORA-01402 check option violation; ORA-42399 read-only view."),
        S("Change and drop", "s_alter_view", "Use CREATE OR REPLACE to change the query."),
    ]),
    G("Synonyms, Sequences, Indexes", [
        S("Synonym", "s_synonym", "PUBLIC synonyms are available to all users."),
        S("CREATE SEQUENCE", "s_seq", "Defaults: START WITH 1, INCREMENT BY 1, NOCYCLE, CACHE 20."),
        S("NEXTVAL / CURRVAL", "s_seq_use", "CURRVAL works only after NEXTVAL in the session."),
        S("ALTER / DROP SEQUENCE", "s_seq_alter", "START WITH cannot be altered."),
        S("CREATE / DROP INDEX", "s_index", "PRIMARY KEY and UNIQUE create a unique index automatically."),
        S("Index examples", "s_index_ex", "Composite index: leading column matters."),
    ]),
]

VIVA = [
    G("Integrity Constraints", [
        VE("What is an integrity constraint?", "A rule defined on a table column that the DBMS checks automatically to keep the data valid and consistent."),
        VE("Name the three types of integrity constraints.", "Domain integrity (NOT NULL, CHECK), entity integrity (UNIQUE, PRIMARY KEY) and referential integrity (FOREIGN KEY)."),
        VE("What is the difference between column-level and table-level constraints?", "A column-level constraint is written with the column and applies to it; a table-level constraint is written after all columns and can use several columns."),
        VE("Which constraint can only be defined at column level?", "NOT NULL."),
        VE("When must a constraint be defined at table level?", "When it uses more than one column, e.g. a composite primary key."),
        VE("What name does Oracle give to an unnamed constraint?", "A system name like SYS_C008401."),
        VE("What does a CHECK constraint do?", "It allows only values for which a given condition is true, e.g. CHECK (marks BETWEEN 0 AND 100)."),
        VE("Can a UNIQUE column contain NULL?", "Yes, and several rows can contain NULL."),
        VE("What is the difference between PRIMARY KEY and UNIQUE?", "A primary key does not allow NULL and there can be only one per table; UNIQUE allows NULLs and there can be many."),
        VE("What is a composite primary key?", "A primary key made of two or more columns, defined at table level, e.g. PRIMARY KEY (roll, cid)."),
        VE("What is a foreign key?", "A column whose values must match the primary or unique key of another (parent) table, or be NULL."),
        VE("Which table must be created first: parent or child?", "The parent (referenced) table."),
        VE("What does ON DELETE CASCADE do?", "When a parent row is deleted, all its child rows are deleted automatically."),
        VE("What does ON DELETE SET NULL do?", "When a parent row is deleted, the foreign key in its child rows is set to NULL."),
        VE("What is a self-referencing foreign key?", "A foreign key that refers to the primary key of the same table, e.g. EMP.MGR → EMP.EMPNO."),
        VE("What is ORA-02291?", "Integrity constraint violated – parent key not found (child value has no matching parent)."),
        VE("What is ORA-02292?", "Integrity constraint violated – child record found (parent row has children)."),
        VE("How do you add a primary key to an existing table?", "ALTER TABLE t ADD CONSTRAINT pk_t PRIMARY KEY (col);"),
        VE("Why disable a constraint?", "To load or change a large amount of data quickly; it is enabled again afterwards."),
        VE("Which dictionary view shows constraints?", "USER_CONSTRAINTS (and USER_CONS_COLUMNS for their columns)."),
    ]),
    G("Views and Synonyms", [
        VE("What is a view?", "A virtual table based on a stored SELECT query; it stores no data."),
        VE("Give two advantages of views.", "Security (hide columns and rows) and simplicity (hide complex joins)."),
        VE("What is the difference between a simple and a complex view?", "A simple view uses one table without functions or grouping and allows DML; a complex view uses joins, functions or GROUP BY and may not allow DML."),
        VE("Can we insert data through a view?", "Yes, through a simple view; the row is inserted into the base table."),
        VE("What is WITH CHECK OPTION?", "It allows only inserts and updates that produce rows visible through the view."),
        VE("What is WITH READ ONLY?", "It prevents any INSERT, UPDATE or DELETE through the view."),
        VE("How do you change the query of a view?", "With CREATE OR REPLACE VIEW."),
        VE("What happens to the table when a view is dropped?", "Nothing; only the view definition is removed."),
        VE("What is a synonym?", "An alternative name (alias) for a database object such as a table or view."),
        VE("What is a public synonym?", "A synonym available to all users, created with CREATE PUBLIC SYNONYM."),
    ]),
    G("Sequences and Indexes", [
        VE("What is a sequence?", "A database object that generates unique numbers automatically, mainly for primary keys."),
        VE("What is the difference between NEXTVAL and CURRVAL?", "NEXTVAL gives the next number and advances the sequence; CURRVAL gives the last number generated in the session."),
        VE("Can CURRVAL be used before NEXTVAL?", "No, it gives ORA-08002."),
        VE("What does CYCLE mean in a sequence?", "After reaching MAXVALUE the sequence starts again from MINVALUE."),
        VE("Which sequence option cannot be altered?", "START WITH."),
        VE("What is the use of CACHE in a sequence?", "Oracle pre-allocates numbers in memory for faster access (default 20)."),
        VE("What is an index?", "An object that stores sorted column values with ROWIDs to speed up searching."),
        VE("What is a composite index?", "An index on two or more columns."),
        VE("What is a unique index?", "An index that does not allow duplicate values; created automatically for PRIMARY KEY and UNIQUE."),
        VE("What is a disadvantage of too many indexes?", "They slow down INSERT, UPDATE and DELETE and use extra storage."),
        VE("Does DROP INDEX delete table data?", "No, only the index is removed."),
    ]),
]

EXAM_QS = [
    XE("What is an integrity constraint? List the types of integrity constraints.", 3),
    XE("Explain domain integrity constraints NOT NULL and CHECK with examples.", 4),
    XE("Explain entity integrity constraints UNIQUE and PRIMARY KEY with examples.", 4),
    XE("Differentiate between PRIMARY KEY and UNIQUE constraints.", 3),
    XE("Explain FOREIGN KEY constraint with ON DELETE CASCADE with an example.", 4),
    XE("Explain all integrity constraints with suitable examples.", 7),
    XE("Differentiate between column-level and table-level constraints.", 3),
    XE("Write SQL to add, drop, enable and disable a constraint on an existing table.", 4),
    XE("Create tables DEPT and EMP with appropriate primary key, foreign key, NOT NULL and CHECK constraints.", 4),
    XE("What is a view? Explain its advantages.", 3),
    XE("Explain CREATE VIEW, ALTER VIEW and DROP VIEW with examples.", 4),
    XE("Differentiate between a simple view and a complex view.", 3),
    XE("Explain WITH CHECK OPTION and WITH READ ONLY with examples.", 4),
    XE("What is a synonym? Explain CREATE SYNONYM and DROP SYNONYM.", 3),
    XE("What is a sequence? Explain CREATE SEQUENCE with all options and an example.", 4),
    XE("Explain NEXTVAL and CURRVAL. Write SQL to insert rows using a sequence.", 3),
    XE("What is an index? Explain unique and composite indexes with examples.", 4),
    XE("Explain views, synonyms, sequences and indexes with syntax and examples.", 7),
]
