"""Shared sample tables for the RDBMS (DI03000031) query programs.

DEPT / EMP follow the classic Oracle SCOTT schema, using Indian names and Gujarat cities.
STUDENT is used for the simpler Unit 1 examples.
Each constant is plain Oracle SQL so the same text can also be shown to students.
"""

DEPT_DDL = """
CREATE TABLE dept (
  deptno NUMBER(2) CONSTRAINT pk_dept PRIMARY KEY,
  dname  VARCHAR2(12),
  loc    VARCHAR2(10)
);
"""

DEPT_ROWS = """
INSERT INTO dept VALUES (10, 'ACCOUNTS', 'SURAT');
INSERT INTO dept VALUES (20, 'RESEARCH', 'AHMEDABAD');
INSERT INTO dept VALUES (30, 'SALES', 'VADODARA');
INSERT INTO dept VALUES (40, 'OPERATIONS', 'RAJKOT');
"""

EMP_DDL = """
CREATE TABLE emp (
  empno    NUMBER(4) CONSTRAINT pk_emp PRIMARY KEY,
  ename    VARCHAR2(10),
  job      VARCHAR2(10),
  mgr      NUMBER(4),
  hiredate DATE,
  sal      NUMBER(7,2),
  comm     NUMBER(7,2),
  deptno   NUMBER(2) CONSTRAINT fk_dept
           REFERENCES dept(deptno)
);
"""

# (empno, ename, job, mgr, hiredate, sal, comm, deptno)
EMP_DATA = [
    (101, "RAJESH", "PRESIDENT", None, "2015-01-10", 90000, None, 10),
    (102, "AMIT", "MANAGER", 101, "2016-03-15", 60000, None, 20),
    (103, "PRIYA", "MANAGER", 101, "2016-07-01", 58000, None, 30),
    (104, "NEHA", "ANALYST", 102, "2018-05-20", 45000, None, 20),
    (105, "KIRAN", "CLERK", 102, "2020-11-11", 22000, None, 20),
    (106, "SUNIL", "SALESMAN", 103, "2019-02-25", 30000, 3000, 30),
    (107, "POOJA", "SALESMAN", 103, "2021-08-30", 28000, 5000, 30),
    (108, "VIJAY", "CLERK", 103, "2022-01-05", 20000, None, 30),
    (109, "HETAL", "ACCOUNTANT", 101, "2017-09-12", 40000, None, 10),
    (110, "MEHUL", "TRAINEE", 104, "2024-06-03", 15000, None, None),
]

MON = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]


def _q(v):
    return "NULL" if v is None else (f"'{v}'" if isinstance(v, str) else str(v))


def _date(s):
    y, m, d = s.split("-")
    return f"'{d}-{MON[int(m) - 1]}-{y}'"


def emp_rows():
    out = []
    for r in EMP_DATA:
        e, n, j, mg, hd, sal, cm, dn = r
        vals = ", ".join([str(e), _q(n), _q(j), _q(mg), f"TO_DATE({_date(hd)}, 'DD-MON-YYYY')", _q(sal), _q(cm), _q(dn)])
        out.append(f"INSERT INTO emp VALUES ({vals});")
    return "\n".join(out) + "\n"


EMP_ROWS = emp_rows()

STUDENT_DDL = """
CREATE TABLE student (
  rollno NUMBER(3) PRIMARY KEY,
  name   VARCHAR2(15) NOT NULL,
  branch VARCHAR2(5),
  city   VARCHAR2(10),
  marks  NUMBER(3)
);
"""

STUDENT_ROWS = """
INSERT INTO student VALUES (1, 'Aarav Patel', 'CE', 'Surat', 82);
INSERT INTO student VALUES (2, 'Diya Shah', 'IT', 'Vadodara', 91);
INSERT INTO student VALUES (3, 'Karan Mehta', 'CE', 'Rajkot', 67);
INSERT INTO student VALUES (4, 'Isha Desai', 'ME', 'Surat', 74);
INSERT INTO student VALUES (5, 'Rohan Joshi', 'CE', 'Bharuch', 58);
"""

SALGRADE = """
CREATE TABLE salgrade (
  grade NUMBER(1),
  losal NUMBER(7),
  hisal NUMBER(7)
);
INSERT INTO salgrade VALUES (1, 10000, 19999);
INSERT INTO salgrade VALUES (2, 20000, 29999);
INSERT INTO salgrade VALUES (3, 30000, 44999);
INSERT INTO salgrade VALUES (4, 45000, 59999);
INSERT INTO salgrade VALUES (5, 60000, 99999);
"""

SCOTT = DEPT_DDL + DEPT_ROWS + EMP_DDL + EMP_ROWS + SALGRADE + "COMMIT;\n"
STUDENT = STUDENT_DDL + STUDENT_ROWS + "COMMIT;\n"
ALL = SCOTT + STUDENT
