"""DI03000031 Unit 3 – worked normalization examples (Numericals tab). Every key / normal form is VERIFIED with nf_tools."""
import html
from nf_tools import parse, closure, closure_steps, candidate_keys, partial_deps, highest_nf, is_bcnf, fmt


def tb(head, rows):
    e = lambda x: html.escape(str(x), quote=False)
    out = "<table><tr>" + "".join(f"<th>{e(h)}</th>" for h in head) + "</tr>"
    for r in rows:
        out += "<tr>" + "".join(f"<td>{e(c)}</td>" for c in r) + "</tr>"
    return out + "</table>"


def sch(name, attrs, key):
    return name + "(" + ", ".join(f"<b>{a}</b>" if a in key else a for a in attrs) + ")"


def N(id_, q, a):
    return {"id": id_, "q": {"en": q}, "a": {"en": a}}


def check(R, fds, keys, nf):
    F = parse(fds)
    got = sorted(fmt(k) for k in candidate_keys(R, F))
    assert got == sorted(keys), (R, got)
    assert highest_nf(R, F) == nf, (R, highest_nf(R, F))
    return F


def check_bcnf(parts, F):
    for attrs in parts:
        sub = [(l, r & set(attrs)) for l, r in F if l <= set(attrs) and r & set(attrs)]
        # dependencies implied inside the part (via closure) must all have a superkey on the left
        from nf_tools import project
        P = project(F, attrs)
        assert is_bcnf(attrs, P), attrs


def steps_html(attrs, F):
    s = sorted(attrs)
    out = [f"Start: {{{fmt(s)}}}"]
    for l, r, c in closure_steps(attrs, F):
        out.append(f"{fmt(l)} → {fmt(r)} gives {{{fmt(c)}}}")
    return "<br>".join(out)


NUMERICALS = []

# ------------------------------------------------------------------ N1  UNF -> 1NF
NUMERICALS.append(N("n3_1", "Convert the following unnormalized STUDENT table into 1NF.<br>" + tb(
    ["ROLL", "NAME", "CITY", "COURSES"],
    [["1", "Aarav", "Surat", "DBMS, OS"], ["2", "Diya", "Vadodara", "DBMS"], ["3", "Karan", "Rajkot", "OS, CN, Java"]]), f"""
<p><b>Why it is not in 1NF:</b> the COURSES column holds several values in one cell (a multi-valued / repeating group). 1NF requires every cell to hold a single <b>atomic</b> value.</p>
<p><b>Method 1 (flattening):</b> write one row for each course.</p>
{tb(["ROLL", "NAME", "CITY", "COURSE"], [["1", "Aarav", "Surat", "DBMS"], ["1", "Aarav", "Surat", "OS"], ["2", "Diya", "Vadodara", "DBMS"],
                                          ["3", "Karan", "Rajkot", "OS"], ["3", "Karan", "Rajkot", "CN"], ["3", "Karan", "Rajkot", "Java"]])}
<p>Primary key = <b>(ROLL, COURSE)</b>, because ROLL alone repeats. The table is now in 1NF, but NAME and CITY repeat (redundancy), so it needs 2NF.</p>
<p><b>Method 2 (decomposition):</b> move the repeating group to a separate table:</p>
<p>{sch("STUDENT", ["ROLL", "NAME", "CITY"], ["ROLL"])}<br>{sch("STUDENT_COURSE", ["ROLL", "COURSE"], ["ROLL", "COURSE"])}</p>
<p>Method 2 already removes the redundancy and gives tables in 3NF.</p>
"""))

# ------------------------------------------------------------------ N2  1NF -> 2NF
R2 = ["ROLL", "CID", "NAME", "CNAME", "CREDITS", "MARKS"]
F2 = check(R2, ["ROLL->NAME", "CID->CNAME,CREDITS", "ROLL,CID->MARKS"], ["CID, ROLL"], "1NF")
assert sorted((fmt(a), fmt(b)) for a, b in partial_deps(R2, F2)) == [("CID", "CNAME, CREDITS"), ("ROLL", "NAME")]
check_bcnf([["ROLL", "NAME"], ["CID", "CNAME", "CREDITS"], ["ROLL", "CID", "MARKS"]], F2)
NUMERICALS.append(N("n3_2", """RESULT(ROLL, CID, NAME, CNAME, CREDITS, MARKS) has the functional dependencies:<br>
ROLL → NAME<br>CID → CNAME, CREDITS<br>ROLL, CID → MARKS<br>Find the key and convert the relation into 2NF.""", f"""
<p><b>Step 1: Candidate key.</b> (ROLL, CID)<sup>+</sup> = {{ROLL, CID, NAME, CNAME, CREDITS, MARKS}} = all attributes, and neither ROLL nor CID alone determines everything. So the key is <b>(ROLL, CID)</b> (composite).</p>
<p><b>Step 2: Check 2NF.</b> Non-key attributes: NAME, CNAME, CREDITS, MARKS.</p>
<ul><li>ROLL → NAME: NAME depends on <b>part</b> of the key → partial dependency.</li>
<li>CID → CNAME, CREDITS: partial dependency.</li>
<li>ROLL, CID → MARKS: full dependency (OK).</li></ul>
<p>Because of the partial dependencies, RESULT is in <b>1NF only</b>.</p>
<p><b>Step 3: Decompose.</b> Put each partial dependency in a separate table with its determinant as the key, and keep the full dependency with the whole key:</p>
<p>{sch("STUDENT", ["ROLL", "NAME"], ["ROLL"])}<br>{sch("COURSE", ["CID", "CNAME", "CREDITS"], ["CID"])}<br>{sch("RESULT", ["ROLL", "CID", "MARKS"], ["ROLL", "CID"])}</p>
<p>ROLL and CID in RESULT are foreign keys. All three tables are in 2NF (in fact in 3NF, since no transitive dependency remains).</p>
"""))

# ------------------------------------------------------------------ N3  2NF -> 3NF
R3 = ["EMPNO", "ENAME", "SAL", "DEPTNO", "DNAME", "LOC"]
F3 = check(R3, ["EMPNO->ENAME,SAL,DEPTNO", "DEPTNO->DNAME,LOC"], ["EMPNO"], "2NF")
check_bcnf([["EMPNO", "ENAME", "SAL", "DEPTNO"], ["DEPTNO", "DNAME", "LOC"]], F3)
NUMERICALS.append(N("n3_3", """EMPLOYEE(EMPNO, ENAME, SAL, DEPTNO, DNAME, LOC) with FDs:<br>EMPNO → ENAME, SAL, DEPTNO<br>DEPTNO → DNAME, LOC<br>
Is it in 3NF? If not, normalize it to 3NF.""", f"""
<p><b>Key:</b> EMPNO<sup>+</sup> = {{EMPNO, ENAME, SAL, DEPTNO}} → using DEPTNO → DNAME, LOC → {{all six attributes}}. So EMPNO is the key.</p>
<p><b>2NF?</b> The key has only one attribute, so a partial dependency is impossible. EMPLOYEE is in <b>2NF</b>.</p>
<p><b>3NF?</b> DEPTNO → DNAME, LOC: a non-key attribute (DEPTNO) determines other non-key attributes. Since EMPNO → DEPTNO and DEPTNO → DNAME, we get EMPNO → DNAME <b>transitively</b>. So it is <b>not in 3NF</b>.</p>
<p>Problem: DNAME and LOC are repeated for every employee of the department (update anomaly), and a department without employees cannot be stored (insertion anomaly).</p>
<p><b>Decompose:</b></p>
<p>{sch("EMP", ["EMPNO", "ENAME", "SAL", "DEPTNO"], ["EMPNO"])} (DEPTNO is a foreign key)<br>{sch("DEPT", ["DEPTNO", "DNAME", "LOC"], ["DEPTNO"])}</p>
<p>Both tables are in 3NF. Joining EMP and DEPT on DEPTNO gives back the original table (lossless decomposition).</p>
"""))

# ------------------------------------------------------------------ N4  full example
R4 = ["ONO", "ODATE", "CID", "CNAME", "CITY", "ICODE", "INAME", "RATE", "QTY"]
F4 = check(R4, ["ONO->ODATE,CID", "CID->CNAME,CITY", "ICODE->INAME,RATE", "ONO,ICODE->QTY"], ["ICODE, ONO"], "1NF")
check_bcnf([["ONO", "ICODE", "QTY"], ["ICODE", "INAME", "RATE"], ["ONO", "ODATE", "CID"], ["CID", "CNAME", "CITY"]], F4)
NUMERICALS.append(N("n3_4", "Normalize the following customer order (bill) data up to 3NF.<br>" + tb(
    ["ONO", "ODATE", "CID", "CNAME", "CITY", "ITEMS (ICODE, INAME, RATE, QTY)"],
    [["501", "05-OCT-26", "C1", "Mehta Stores", "Surat", "I1 Pen 10 x5; I2 Book 60 x2"],
     ["502", "06-OCT-26", "C2", "Shah Traders", "Anand", "I1 Pen 10 x3"]]), f"""
<p><b>UNF → 1NF.</b> The ITEMS column is a repeating group. Make one row per item (atomic values):</p>
{tb(["ONO", "ODATE", "CID", "CNAME", "CITY", "ICODE", "INAME", "RATE", "QTY"],
    [["501", "05-OCT-26", "C1", "Mehta Stores", "Surat", "I1", "Pen", "10", "5"], ["501", "05-OCT-26", "C1", "Mehta Stores", "Surat", "I2", "Book", "60", "2"],
     ["502", "06-OCT-26", "C2", "Shah Traders", "Anand", "I1", "Pen", "10", "3"]])}
<p>Functional dependencies:</p>
<ul><li>ONO → ODATE, CID</li><li>CID → CNAME, CITY</li><li>ICODE → INAME, RATE</li><li>ONO, ICODE → QTY</li></ul>
<p>Key = <b>(ONO, ICODE)</b>, since (ONO, ICODE)<sup>+</sup> gives all nine attributes.</p>
<p><b>1NF → 2NF.</b> Partial dependencies: ONO → ODATE, CID (and so CNAME, CITY) and ICODE → INAME, RATE. Remove them:</p>
<p>{sch("ORDER_ITEM", ["ONO", "ICODE", "QTY"], ["ONO", "ICODE"])}<br>{sch("ITEM", ["ICODE", "INAME", "RATE"], ["ICODE"])}<br>
{sch("ORDERS", ["ONO", "ODATE", "CID", "CNAME", "CITY"], ["ONO"])}</p>
<p><b>2NF → 3NF.</b> In ORDERS, ONO → CID → CNAME, CITY is a transitive dependency. Split ORDERS:</p>
<p>{sch("ORDERS", ["ONO", "ODATE", "CID"], ["ONO"])}<br>{sch("CUSTOMER", ["CID", "CNAME", "CITY"], ["CID"])}</p>
<p><b>Final 3NF design (4 tables):</b> CUSTOMER, ORDERS, ITEM and ORDER_ITEM. Customer and item details are now stored only once; the amount of a line is calculated as RATE × QTY when needed.</p>
"""))

# ------------------------------------------------------------------ N5  abstract R(A,B,C,D)
R5 = "ABCD"
F5 = check(R5, ["A,B->C", "C->D"], ["A, B"], "2NF")
check_bcnf(["ABC", "CD"], F5)
NUMERICALS.append(N("n3_5", "R(A, B, C, D) with F = { AB → C, C → D }. Find the candidate key and the highest normal form. Decompose into 3NF if needed.", f"""
<p><b>Closure of AB:</b><br>{steps_html("AB", F5)}<br>AB<sup>+</sup> contains all attributes, so AB is a super key. A<sup>+</sup> = {{A}} and B<sup>+</sup> = {{B}}, so AB is minimal: <b>candidate key = AB</b>.</p>
<p>Prime attributes: A, B. Non-prime: C, D.</p>
<p><b>2NF:</b> does any non-prime attribute depend on only A or only B? No (A<sup>+</sup> and B<sup>+</sup> contain nothing else). So R is in <b>2NF</b>.</p>
<p><b>3NF:</b> C → D: C is not a super key and D is non-prime. AB → C → D is a <b>transitive</b> dependency. So R is <b>not in 3NF</b>; the highest normal form is <b>2NF</b>.</p>
<p><b>Decomposition:</b> R1(<b>A</b>, <b>B</b>, C) and R2(<b>C</b>, D). In R1 the only FD is AB → C, and in R2 it is C → D; both left sides are keys, so both are in 3NF (and BCNF). The common attribute C is the key of R2, so the decomposition is lossless.</p>
"""))

# ------------------------------------------------------------------ N6  abstract R(A,B,C,D,E)
R6 = "ABCDE"
F6 = check(R6, ["A->B", "A,C->D", "D->E"], ["A, C"], "1NF")
check_bcnf(["AB", "ACD", "DE"], F6)
NUMERICALS.append(N("n3_6", "R(A, B, C, D, E) with F = { A → B, AC → D, D → E }. Find the key, the normal form, and normalize R up to 3NF.", f"""
<p><b>Key:</b> A and C never appear on the right side of any FD, so both must be in every key.<br>{steps_html("AC", F6)}<br>
AC<sup>+</sup> = all attributes, so <b>AC</b> is the candidate key.</p>
<p><b>Check:</b></p>
<ul><li>A → B: B depends on part (A) of the key → <b>partial dependency</b>. So R is <b>only in 1NF</b>.</li>
<li>D → E: E depends on the non-key attribute D → transitive dependency.</li></ul>
<p><b>To 2NF:</b> remove the partial dependency: R1(<b>A</b>, B) and R2(<b>A</b>, <b>C</b>, D, E).</p>
<p><b>To 3NF:</b> in R2, AC → D → E is transitive. Split R2 into R21(<b>A</b>, <b>C</b>, D) and R22(<b>D</b>, E).</p>
<p><b>Final 3NF relations:</b> R1(<b>A</b>, B), R21(<b>A</b>, <b>C</b>, D), R22(<b>D</b>, E).</p>
"""))

# ------------------------------------------------------------------ N7  closure and candidate keys
R7 = "ABCDE"
F7 = parse(["A->B,C", "C,D->E", "B->D", "E->A"])
assert sorted(fmt(k) for k in candidate_keys(R7, F7)) == ["A", "B, C", "C, D", "E"]
assert closure("B", F7) == {"B", "D"} and closure("C", F7) == {"C"}
NUMERICALS.append(N("n3_7", "R(A, B, C, D, E) with F = { A → BC, CD → E, B → D, E → A }. Compute A<sup>+</sup>, E<sup>+</sup>, (BC)<sup>+</sup>, (CD)<sup>+</sup> and find all candidate keys.", f"""
<p><b>Attribute closure algorithm:</b> start with the given attributes; repeatedly, for every FD X → Y whose left side X is already in the result, add Y; stop when nothing changes.</p>
<p><b>A<sup>+</sup>:</b><br>{steps_html("A", F7)}<br>A<sup>+</sup> = ABCDE → A is a key.</p>
<p><b>E<sup>+</sup>:</b><br>{steps_html("E", F7)}<br>E<sup>+</sup> = ABCDE → E is a key.</p>
<p><b>(BC)<sup>+</sup>:</b><br>{steps_html("BC", F7)}<br>→ BC is a super key. B<sup>+</sup> = {{B, D}} and C<sup>+</sup> = {{C}}, so BC is minimal: candidate key.</p>
<p><b>(CD)<sup>+</sup>:</b><br>{steps_html("CD", F7)}<br>→ CD is a super key; C<sup>+</sup> = {{C}}, D<sup>+</sup> = {{D}}, so CD is a candidate key.</p>
<p><b>Candidate keys: A, E, BC and CD.</b> Prime attributes = A, B, C, D, E (all), so there are no non-prime attributes and R is in 3NF.</p>
"""))
