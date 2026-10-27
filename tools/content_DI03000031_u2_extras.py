"""DI03000031 Unit 2 extras: syntax sheet, viva, exam questions."""
from sql_content import SXE, VE, XE, G
from content_DI03000031_u2_notes_a import SN as SNA
from content_DI03000031_u2_notes_b import SN as SNB

SN = {**SNA, **SNB}


def S(name, key, terms=""):
    return SXE(name, SN[key].strip("\n"), terms)


SYNTAX = [
    G("Operators", [
        S("Special operators", "s_special", "BETWEEN includes both limits. Use IS NULL, never = NULL."),
        SXE("LIKE wildcards", "'A%'   starts with A\n'%A'   ends with A\n'_A%'  2nd letter A\n'___'  exactly 3 chars",
            "% = zero or more characters, _ = exactly one character."),
    ]),
    G("Single-row Functions", [
        SXE("Numeric", "ABS(n)  POWER(m,n)  MOD(m,n)\nSQRT(n)  CEIL(n)  FLOOR(n)\nROUND(n[,d])  TRUNC(n[,d])",
            "ROUND(15.67,1) = 15.7, TRUNC(15.67,1) = 15.6"),
        SXE("Character", "LOWER(s) UPPER(s) INITCAP(s)\nLENGTH(s) CONCAT(a,b) a || b\nLTRIM(s[,set]) RTRIM(s[,set])\n"
                         "REPLACE(s,find[,new])\nSUBSTR(s,start[,len])\nINSTR(s,find[,start[,n]])\nLPAD(s,n[,c]) RPAD(s,n[,c])",
            "Positions start at 1. INSTR returns 0 if not found."),
        SXE("Date", "SYSDATE\nADD_MONTHS(d, n)\nMONTHS_BETWEEN(d1, d2)\nLAST_DAY(d)\nNEXT_DAY(d, 'DAY')\n"
                    "ROUND(d[, 'MONTH'|'YEAR'])\nTRUNC(d[, 'MONTH'|'YEAR'])",
            "date ± n = date; date − date = days."),
        SXE("Conversion", "TO_CHAR(date, 'DD-MM-YYYY')\nTO_CHAR(num, '99,999.99')\nTO_DATE('text', 'format')\nTO_NUMBER('text'[, 'fmt'])",
            "Format elements: DD MM MON MONTH YY YYYY DAY DY HH24 MI SS; 9 0 , . $"),
        SXE("General", "NVL(e, v)\nNVL2(e, if_not_null, if_null)\nDECODE(e, s1, r1, s2, r2, def)",
            "DECODE works like IF-THEN-ELSE for equality tests."),
        S("CASE expression", "s_case", "ANSI standard; can test any condition."),
    ]),
    G("Grouping and Sorting", [
        S("GROUP BY / HAVING", "s_group", "WHERE filters rows; HAVING filters groups."),
        S("ORDER BY", "s_order", "Default ASC. Can use alias or column position."),
        SXE("Aggregate functions", "COUNT(*)  COUNT(col)\nCOUNT(DISTINCT col)\nSUM(col)  AVG(col)\nMAX(col)  MIN(col)",
            "All ignore NULLs except COUNT(*)."),
    ]),
    G("Joins", [
        S("Inner / equi join", "s_join", "Only matching rows."),
        S("Natural join / USING", "s_natural", "Joins on columns with the same name."),
        S("Outer joins", "s_outer", "(+) goes on the side that may be missing."),
        S("Cross join", "s_cross", "Rows = m × n."),
        S("Self join", "s_self", "Same table with two aliases."),
    ]),
    G("Sub-queries and Set Operators", [
        S("Sub-query", "s_subq", "Single-row: = &gt; &lt;. Multiple-row: IN ANY ALL EXISTS."),
        S("Sub-query in UPDATE / FROM", "s_sub_other", "A sub-query in FROM is called an inline view."),
        S("Set operators", "s_set", "Same number and type of columns; ORDER BY only at the end."),
    ]),
]

VIVA = [
    G("Operators and Functions", [
        VE("What are the special operators in SQL?", "IN, BETWEEN, LIKE, IS NULL, ANY, ALL and EXISTS (and their NOT forms)."),
        VE("What is the difference between % and _ in LIKE?", "% matches zero or more characters; _ matches exactly one character."),
        VE("Does BETWEEN include the boundary values?", "Yes. BETWEEN 10 AND 20 includes 10 and 20."),
        VE("Why can't we write comm = NULL?", "NULL means unknown, so a comparison with it is never true. Use IS NULL."),
        VE("What is the result of 5000 + NULL?", "NULL. Any arithmetic with NULL gives NULL; use NVL to avoid it."),
        VE("What is the DUAL table?", "A one-row, one-column dummy table owned by SYS, used to evaluate expressions and functions."),
        VE("Difference between ROUND and TRUNC?", "ROUND rounds to the nearest value; TRUNC simply cuts off the digits. ROUND(4.56,1) = 4.6, TRUNC(4.56,1) = 4.5."),
        VE("Difference between CEIL and FLOOR?", "CEIL returns the smallest integer ≥ n; FLOOR returns the largest integer ≤ n."),
        VE("What does MOD(17, 5) return?", "2, the remainder of 17 divided by 5."),
        VE("What does INITCAP do?", "It converts the first letter of every word to capital and the rest to small letters."),
        VE("What is the difference between SUBSTR and INSTR?", "SUBSTR extracts part of a string; INSTR returns the position of a substring."),
        VE("What is the difference between CONCAT and ||?", "CONCAT joins exactly two strings; || can join any number of strings."),
        VE("What does LPAD('5', 3, '0') return?", "'005'."),
        VE("What does LAST_DAY return?", "The date of the last day of the month of the given date."),
        VE("What does NEXT_DAY(SYSDATE, 'FRIDAY') return?", "The date of the first Friday after today."),
        VE("What is the result of subtracting two dates?", "The number of days between them."),
        VE("Name the conversion functions.", "TO_CHAR, TO_DATE and TO_NUMBER."),
        VE("What is the use of NVL?", "It replaces NULL with a given value, e.g. NVL(comm, 0)."),
        VE("What is DECODE?", "Oracle's IF-THEN-ELSE function that compares an expression with search values and returns the matching result."),
    ]),
    G("Grouping, Joins and Sub-queries", [
        VE("Name the aggregate functions.", "COUNT, SUM, AVG, MAX and MIN."),
        VE("Difference between COUNT(*) and COUNT(column)?", "COUNT(*) counts all rows; COUNT(column) counts only non-NULL values of that column."),
        VE("Difference between WHERE and HAVING?", "WHERE filters rows before grouping; HAVING filters groups after grouping and can use aggregate functions."),
        VE("What is the default order of ORDER BY?", "Ascending (ASC)."),
        VE("Where do NULLs appear in ORDER BY ASC in Oracle?", "Last (NULLs are treated as the largest values)."),
        VE("What is a join?", "An operation that combines rows of two or more tables based on a related column."),
        VE("What is an equi join?", "A join that uses the = operator in the join condition."),
        VE("What is a non-equi join?", "A join that uses an operator other than =, such as BETWEEN or &gt;."),
        VE("What is an outer join?", "A join that returns matching rows plus the non-matching rows of one or both tables, with NULLs for the missing columns."),
        VE("What is a self join?", "A join of a table with itself using two aliases, e.g. to find each employee's manager."),
        VE("How many rows does a cross join of 5 and 4 rows give?", "20 (5 × 4)."),
        VE("What is a sub-query?", "A query written inside another SQL statement; its result is used by the outer query."),
        VE("What is a correlated sub-query?", "A sub-query that uses a column of the outer query and is executed once for each outer row."),
        VE("What error occurs when a single-row sub-query returns many rows?", "ORA-01427: single-row subquery returns more than one row."),
        VE("Difference between UNION and UNION ALL?", "UNION removes duplicates and sorts; UNION ALL keeps all rows, including duplicates."),
        VE("What does MINUS return?", "The rows of the first query that are not returned by the second query."),
        VE("What are the rules for set operators?", "Same number of columns, compatible data types; ORDER BY only at the end."),
    ]),
]

EXAM_QS = [
    XE("Explain arithmetic, comparison and logical operators with examples.", 4),
    XE("Explain the special operators IN, BETWEEN and LIKE with examples.", 4),
    XE("Explain ANY, ALL and EXISTS operators with examples.", 4),
    XE("What is the DUAL table? Explain any four numeric functions with examples.", 4),
    XE("Explain any seven character functions with examples.", 7),
    XE("Explain the date functions ADD_MONTHS, MONTHS_BETWEEN, LAST_DAY, NEXT_DAY, ROUND and TRUNC.", 7),
    XE("Explain the conversion functions TO_CHAR, TO_DATE and TO_NUMBER with examples.", 4),
    XE("Explain NVL and DECODE functions with examples.", 3),
    XE("Explain aggregate functions with examples.", 4),
    XE("Explain GROUP BY and HAVING clauses with examples. Differentiate WHERE and HAVING.", 7),
    XE("Explain the ORDER BY clause with an example.", 3),
    XE("What is a join? Explain the types of joins with examples.", 7),
    XE("Differentiate inner join and outer join.", 3),
    XE("Explain self join and cross join with examples.", 4),
    XE("What is a sub-query? Explain its types with examples.", 4),
    XE("Explain correlated sub-query with an example. Differentiate nested and correlated sub-queries.", 4),
    XE("Explain set operators UNION, UNION ALL, INTERSECT and MINUS with examples.", 7),
    XE("Write SQL queries: (i) display employees whose name starts with 'A' (ii) find the second highest salary (iii) count employees in each department.", 3),
]
