"""Digital Electronics Fundamentals (DI03000011) - Unit 4 extras: numericals (all computed and checked), equations, viva, exam."""
from content_DI03000011_u1_extras import N, E, V, X
from de_gates import tt_html, equiv, bh as B
from diagrams_DI03000011_u4 import HA, FA, HS, FS, rows

nand = lambda a, b: 1 - (a & b)
S1, S0 = B("!(S1)"), B("!(S0)")
NC = B("!(Cin)")


def both(s):
    return s, s


# ---------------------------------------------------------------- n1: half adder with NAND only
_r1 = []
for a in (0, 1):
    for b in (0, 1):
        x = nand(a, b); p = nand(a, x); q = nand(b, x); s = nand(p, q); c = nand(x, x)
        assert (s, c) == HA(a, b)
        _r1.append((a, b, x, p, q, s, c))
_t1 = tt_html(["A", "B", "X", "P", "Q", "S", "C"], _r1, 2)
_a1_en = (f"<p>Gate 1: X = {B('!(AB)')}</p><p>Gate 2: P = {B('!(A·X)')} &nbsp; Gate 3: Q = {B('!(B·X)')}</p>"
          f"<p>Gate 4: S = {B('!(P·Q)')} = A ⊕ B</p><p>Gate 5 (NAND as inverter): C = {B('!(X·X)')} = {B('!X')} = AB</p>"
          f"<p><b>Verification:</b></p>{_t1}<p>S and C match the half-adder truth table. <b>Total: 5 NAND gates</b> (two 7400 ICs, or one 7400 + one gate of another).</p>")
_a1_gu = (_a1_en.replace("<b>Verification:</b>", "<b>ચકાસણી:</b>")
          .replace("S and C match the half-adder truth table.", "S અને C half-adder truth table સાથે મેળ ખાય છે.")
          .replace("<b>Total: 5 NAND gates</b> (two 7400 ICs, or one 7400 + one gate of another).", "<b>કુલ: 5 NAND gates</b>."))

# ---------------------------------------------------------------- n2: full adder outputs
_cases2 = [(1, 1, 0), (1, 0, 1), (1, 1, 1), (0, 1, 0)]
_t2 = tt_html(["A", "B", "Cin", "A+B+Cin", "S", "Cout"], [(a, b, c, a + b + c, *FA(a, b, c)) for a, b, c in _cases2], 2)
assert FA(1, 1, 1) == (1, 1) and FA(1, 1, 0) == (0, 1)
_a2_en = (f"<p>S = A ⊕ B ⊕ Cin and Cout = AB + B·Cin + A·Cin. S is the LSB and Cout the MSB of the 2-bit sum.</p>{_t2}"
          "<p>For A = 1, B = 1, Cin = 1: 1 + 1 + 1 = 3 = 11<sub>2</sub> → S = 1, Cout = 1.</p>")
_a2_gu = (f"<p>S = A ⊕ B ⊕ Cin અને Cout = AB + B·Cin + A·Cin. S એ 2-bit sum નો LSB અને Cout MSB છે.</p>{_t2}"
          "<p>A = 1, B = 1, Cin = 1 માટે: 1 + 1 + 1 = 3 = 11<sub>2</sub> → S = 1, Cout = 1.</p>")

# ---------------------------------------------------------------- n3: S = A xor B xor Cin by algebra
assert equiv(lambda a, b, c: ((1 - a) & (1 - b) & c) | ((1 - a) & b & (1 - c)) | (a & (1 - b) & (1 - c)) | (a & b & c),
             lambda a, b, c: a ^ b ^ c, 3)
_a3 = (f"<p>S = {B('!A!B')}Cin + {B('!AB')}{NC} + {B('A!B')}{NC} + AB·Cin</p>"
       f"<p>= Cin({B('!A!B')} + AB) + {NC}({B('!AB')} + {B('A!B')})</p>"
       f"<p>Now {B('!AB')} + {B('A!B')} = A ⊕ B and {B('!A!B')} + AB = {B('!(A⊕B)')} (XNOR).</p>"
       f"<p>Let P = A ⊕ B: S = Cin·{B('!P')} + {NC}·P = P ⊕ Cin</p>"
       "<p><b>S = A ⊕ B ⊕ Cin</b> ✔ (also checked for all 8 rows)</p>")
_a3_gu = _a3.replace("Now", "હવે").replace("Let P = A ⊕ B:", "P = A ⊕ B લેતાં:").replace("(also checked for all 8 rows)", "(બધી 8 rows માટે પણ ચકાસેલ)")


# ---------------------------------------------------------------- n4 / n8: ripple add / subtract
def ripple(a, b, sub=False):
    n = len(a)
    carry, out, tr = 0, [], []
    for i in range(n - 1, -1, -1):
        x, y = int(a[i]), int(b[i])
        s, c = (FS if sub else FA)(x, y, carry)
        tr.append((f"bit {n - 1 - i}", x, y, carry, s, c))
        out.insert(0, s)
        carry = c
    return "".join(map(str, out)), carry, tr


_s4, _c4, _tr4 = ripple("1011", "0111")
assert int(str(_c4) + _s4, 2) == 11 + 7 == 18
_t4 = tt_html(["Stage", "A", "B", "Cin", "S", "Cout"], _tr4, 2)
_a4_en = (f"<p>Four full adders are connected in cascade (FA0 = LSB). Cin of FA0 = 0; each Cout goes to the next Cin.</p>{_t4}"
          f"<p>Result: Cout S3S2S1S0 = <b>{_c4} {_s4}</b> = 18<sub>10</sub>. Check: 11 + 7 = 18 ✔</p>")
_a4_gu = (f"<p>ચાર full adders cascade માં જોડાય છે (FA0 = LSB). FA0 નો Cin = 0; દરેક Cout પછીના Cin માં જાય.</p>{_t4}"
          f"<p>પરિણામ: Cout S3S2S1S0 = <b>{_c4} {_s4}</b> = 18<sub>10</sub>. ચકાસણી: 11 + 7 = 18 ✔</p>")

_d8, _b8, _tr8 = ripple("1010", "0111", sub=True)
assert int(_d8, 2) == 10 - 7 and _b8 == 0
_t8 = tt_html(["Stage", "A", "B", "Bin", "D", "Bout"], _tr8, 2)
_a8_en = (f"<p>Four full subtractors in cascade; Bin of the LSB stage = 0; each Bout goes to the next Bin.</p>{_t8}"
          f"<p>Result: D = <b>{_d8}</b> = 3<sub>10</sub>, final borrow = {_b8} (result positive). Check: 10 − 7 = 3 ✔</p>")
_a8_gu = (f"<p>ચાર full subtractors cascade માં; LSB stage નો Bin = 0; દરેક Bout પછીના Bin માં જાય.</p>{_t8}"
          f"<p>પરિણામ: D = <b>{_d8}</b> = 3<sub>10</sub>, છેલ્લો borrow = {_b8} (પરિણામ positive). ચકાસણી: 10 − 7 = 3 ✔</p>")

# ---------------------------------------------------------------- n5: Cout identity
_t5 = tt_html(["A", "B", "Cin", "AB + (A⊕B)Cin", "AB + BCin + ACin"],
              [(a, b, c, (a & b) | ((a ^ b) & c), FA(a, b, c)[1]) for a, b, c, *_ in rows(FA, 3)], 2)
_a5 = (f"<p>AB + (A ⊕ B)Cin = AB + {B('A!B')}Cin + {B('!AB')}Cin</p>"
       f"<p>= AB + ABCin + {B('A!B')}Cin + ABCin + {B('!AB')}Cin &nbsp; (AB = AB + ABCin + ABCin)</p>"
       f"<p>= AB + ACin(B + {B('!B')}) + BCin(A + {B('!A')})</p><p>= <b>AB + A·Cin + B·Cin</b> ✔</p>{_t5}")
_a5_gu = _a5

# ---------------------------------------------------------------- n6 / n7: subtractor outputs
_t6 = tt_html(["A", "B", "A − B", "D", "Bo"], [(a, b, a - b, *HS(a, b)) for a in (0, 1) for b in (0, 1)], 2)
assert HS(0, 1) == (1, 1)
_a6_en = (f"<p>D = A ⊕ B, Bo = {B('!AB')}.</p>{_t6}<p>For A = 0, B = 1: D = 0 ⊕ 1 = 1 and Bo = {B('!0')}·1 = 1 (borrow 1 from the next bit: 10 − 1 = 1).</p>")
_a6_gu = (f"<p>D = A ⊕ B, Bo = {B('!AB')}.</p>{_t6}<p>A = 0, B = 1 માટે: D = 0 ⊕ 1 = 1 અને Bo = {B('!0')}·1 = 1 (આગળના bit માંથી borrow 1: 10 − 1 = 1).</p>")

_cases7 = [(0, 1, 1), (1, 0, 1), (1, 1, 1), (0, 0, 1)]
_t7 = tt_html(["A", "B", "Bin", "D", "Bout"], [(a, b, c, *FS(a, b, c)) for a, b, c in _cases7], 2)
assert FS(0, 1, 1) == (0, 1) and FS(1, 1, 1) == (1, 1)
_a7_en = (f"<p>D = A ⊕ B ⊕ Bin, Bout = {B('!AB')} + {B('!A')}·Bin + B·Bin.</p>{_t7}"
          "<p>A = 0, B = 1, Bin = 1: D = 0 ⊕ 1 ⊕ 1 = 0; Bout = 1·1 + 1·1 + 1·1 = 1. (Borrow 2 from the next bit: 2 + 0 − 1 − 1 = 0.)</p>"
          "<p>A = 1, B = 1, Bin = 1: D = 1, Bout = 1 (2 + 1 − 1 − 1 = 1).</p>")
_a7_gu = (f"<p>D = A ⊕ B ⊕ Bin, Bout = {B('!AB')} + {B('!A')}·Bin + B·Bin.</p>{_t7}"
          "<p>A = 0, B = 1, Bin = 1: D = 0 ⊕ 1 ⊕ 1 = 0; Bout = 1·1 + 1·1 + 1·1 = 1. (આગળના bit માંથી 2 નો borrow: 2 + 0 − 1 − 1 = 0.)</p>"
          "<p>A = 1, B = 1, Bin = 1: D = 1, Bout = 1 (2 + 1 − 1 − 1 = 1).</p>")

# ---------------------------------------------------------------- n9: encoder
enc = lambda d3, d2, d1, d0: (d2 | d3, d1 | d3)
assert enc(0, 1, 0, 0) == (1, 0) and enc(0, 1, 1, 0) == (1, 1)
_a9_en = ("<p>Y1 = D2 + D3, Y0 = D1 + D3.</p>"
          "<p>(a) D2 = 1, others 0: Y1 = 1 + 0 = 1, Y0 = 0 + 0 = 0 → <b>Y1Y0 = 10</b> (binary 2) ✔</p>"
          "<p>(b) D1 = D2 = 1: Y1 = 1, Y0 = 1 → <b>Y1Y0 = 11</b>, which is the code of D3. The output is <b>wrong</b>.</p>"
          "<p>So a simple encoder needs only one active input at a time. A <b>priority encoder</b> would give 10 here (D2 has higher priority than D1).</p>")
_a9_gu = ("<p>Y1 = D2 + D3, Y0 = D1 + D3.</p>"
          "<p>(a) D2 = 1, બાકી 0: Y1 = 1 + 0 = 1, Y0 = 0 + 0 = 0 → <b>Y1Y0 = 10</b> (binary 2) ✔</p>"
          "<p>(b) D1 = D2 = 1: Y1 = 1, Y0 = 1 → <b>Y1Y0 = 11</b>, જે D3 નો code છે. Output <b>ખોટો</b> છે.</p>"
          "<p>તેથી સાદા encoder માં એક સમયે એક જ input active હોવો જોઈએ. <b>Priority encoder</b> અહીં 10 આપે (D2 ની priority D1 કરતાં વધુ).</p>")

# ---------------------------------------------------------------- n10: functions with a decoder
_dec = lambda a, b: [int(2 * a + b == k) for k in range(4)]
assert equiv(lambda a, b: _dec(a, b)[1] | _dec(a, b)[2], lambda a, b: a ^ b, 2)
assert equiv(lambda a, b: _dec(a, b)[0] | _dec(a, b)[3], lambda a, b: 1 - (a ^ b), 2)
_t10 = tt_html(["A", "B", "Y0", "Y1", "Y2", "Y3", "F1 = Y1+Y2", "F2 = Y0+Y3"],
               [(a, b, *_dec(a, b), _dec(a, b)[1] | _dec(a, b)[2], _dec(a, b)[0] | _dec(a, b)[3]) for a in (0, 1) for b in (0, 1)], 2)
_a10_en = ("<p>A decoder gives every minterm, so a function = OR of its minterm outputs.</p>"
           "<p>F1 = A ⊕ B = Σm(1, 2) → connect <b>Y1 and Y2 to a 2-input OR gate</b>.</p>"
           "<p>F2 = A ⊙ B = Σm(0, 3) → connect <b>Y0 and Y3 to another OR gate</b>.</p>" + _t10)
_a10_gu = ("<p>Decoder દરેક minterm આપે છે, તેથી function = તેના minterm outputs નો OR.</p>"
           "<p>F1 = A ⊕ B = Σm(1, 2) → <b>Y1 અને Y2 ને 2-input OR gate</b> સાથે જોડો.</p>"
           "<p>F2 = A ⊙ B = Σm(0, 3) → <b>Y0 અને Y3 ને બીજા OR gate</b> સાથે જોડો.</p>" + _t10)

# ---------------------------------------------------------------- n11: MUX output
I = [1, 0, 1, 1]
mux = lambda s1, s0, d: d[2 * s1 + s0]
_t11 = tt_html(["S1", "S0", "Selected", "Y"], [(s1, s0, f"I{2 * s1 + s0}", mux(s1, s0, I)) for s1 in (0, 1) for s0 in (0, 1)], 1)
assert mux(0, 1, I) == 0
YM = f"Y = {S1}{S0}I0 + {S1}S0I1 + S1{S0}I2 + S1S0I3"
_a11_en = f"<p>{YM}</p><p>With S1S0 = 01 only the AND gate {S1}S0I1 is enabled, so <b>Y = I1 = 0</b>.</p>{_t11}"
_a11_gu = f"<p>{YM}</p><p>S1S0 = 01 હોય ત્યારે માત્ર {S1}S0I1 AND gate enable થાય, તેથી <b>Y = I1 = 0</b>.</p>{_t11}"

# ---------------------------------------------------------------- n12: 2-var function with 4:1 MUX
f12 = lambda a, b: a ^ b
_d12 = [f12(a, b) for a in (0, 1) for b in (0, 1)]
assert all(mux(a, b, _d12) == f12(a, b) for a in (0, 1) for b in (0, 1))
_t12 = tt_html(["A (S1)", "B (S0)", "F", "Data input"], [(a, b, f12(a, b), f"I{2 * a + b} = {f12(a, b)}") for a in (0, 1) for b in (0, 1)], 1)
_a12_en = (f"<p>Connect A → S1 and B → S0. Each data input gets the value of F for that row.</p>{_t12}"
           f"<p><b>I0 = 0, I1 = 1, I2 = 1, I3 = 0</b> (connect 1 to +5 V, 0 to ground). Output Y = F = A ⊕ B.</p>")
_a12_gu = (f"<p>A → S1 અને B → S0 જોડો. દરેક data input ને તે row ની F ની કિંમત આપો.</p>{_t12}"
           f"<p><b>I0 = 0, I1 = 1, I2 = 1, I3 = 0</b> (1 એટલે +5 V, 0 એટલે ground). Output Y = F = A ⊕ B.</p>")

# ---------------------------------------------------------------- n13: 3-var function with 4:1 MUX
ONES13 = [1, 3, 5, 6]
f13 = lambda a, b, c: int(4 * a + 2 * b + c in ONES13)
_res13 = []
for a in (0, 1):
    for b in (0, 1):
        v0, v1 = f13(a, b, 0), f13(a, b, 1)
        val = {(0, 0): "0", (1, 1): "1", (0, 1): "C", (1, 0): "!C"}[(v0, v1)]
        _res13.append((a, b, 4 * a + 2 * b, 4 * a + 2 * b + 1, v0, v1, val))
for a, b, m0, m1, v0, v1, val in _res13:
    for c in (0, 1):
        got = {"0": 0, "1": 1, "C": c, "!C": 1 - c}[val]
        assert got == f13(a, b, c)
_t13 = tt_html(["A", "B", "Rows", "F (C=0)", "F (C=1)", "Data input"],
               [(a, b, f"m{m0}, m{m1}", v0, v1, f"I{2 * a + b} = " + B(val)) for a, b, m0, m1, v0, v1, val in _res13], 1)
_a13_en = (f"<p>Use A → S1, B → S0. For each pair of rows (same A, B) compare F with C:</p>{_t13}"
           f"<p>Rule: F = 0, 0 → 0; F = 1, 1 → 1; F = C → C; F = {B('!C')} → {B('!C')}.</p>"
           f"<p><b>I0 = C, I1 = C, I2 = C, I3 = {B('!C')}</b> (one NOT gate for {B('!C')}).</p>")
_a13_gu = (f"<p>A → S1, B → S0 વાપરો. દરેક rows ની જોડી (સરખા A, B) માટે F ને C સાથે સરખાવો:</p>{_t13}"
           f"<p>નિયમ: F = 0, 0 → 0; F = 1, 1 → 1; F = C → C; F = {B('!C')} → {B('!C')}.</p>"
           f"<p><b>I0 = C, I1 = C, I2 = C, I3 = {B('!C')}</b> ({B('!C')} માટે એક NOT gate).</p>")
assert [r[6] for r in _res13] == ["C", "C", "C", "!C"]

# ---------------------------------------------------------------- n14: DEMUX
dmx = lambda d, s1, s0: [d if 2 * s1 + s0 == k else 0 for k in range(4)]
assert dmx(1, 1, 0) == [0, 0, 1, 0] and dmx(0, 1, 0) == [0, 0, 0, 0]
_a14_en = (f"<p>Y0 = D{S1}{S0}, Y1 = D{S1}S0, Y2 = DS1{S0}, Y3 = DS1S0.</p>"
           "<p>(a) D = 1, S1S0 = 10: only Y2 = 1·1·1 = 1 → <b>Y0Y1Y2Y3 = 0010</b>.</p>"
           "<p>(b) D = 0, S1S0 = 10: Y2 = D = 0 → <b>all outputs 0</b> (the selected output simply follows D).</p>"
           "<p>(c) To send D to Y3, make S1S0 = 11.</p>")
_a14_gu = (f"<p>Y0 = D{S1}{S0}, Y1 = D{S1}S0, Y2 = DS1{S0}, Y3 = DS1S0.</p>"
           "<p>(a) D = 1, S1S0 = 10: માત્ર Y2 = 1·1·1 = 1 → <b>Y0Y1Y2Y3 = 0010</b>.</p>"
           "<p>(b) D = 0, S1S0 = 10: Y2 = D = 0 → <b>બધા outputs 0</b> (પસંદ થયેલો output D ને અનુસરે છે).</p>"
           "<p>(c) D ને Y3 પર મોકલવા S1S0 = 11 કરો.</p>")

# ---------------------------------------------------------------- n15: counting lines
import math
_rows15 = [("MUX 8 : 1", 8, 3), ("MUX 16 : 1", 16, 4), ("MUX 32 : 1", 32, 5), ("DEMUX 1 : 8", 8, 3), ("Decoder 3 : 8", 8, 3), ("Encoder 8 : 3", 8, 3)]
for _, m, n in _rows15:
    assert 2 ** n == m and int(math.log2(m)) == n
_a15_en = ("<p>For a MUX/DEMUX with m data lines, select lines n = log<sub>2</sub> m (2<sup>n</sup> = m).</p>"
           + tt_html(["Circuit", "Data lines", "Select / code bits"], _rows15, 1)
           + "<p>(a) 8:1 MUX → <b>3</b> select lines. (b) 16:1 MUX → <b>4</b>. (c) A 1:8 DEMUX → <b>3</b> select lines. A 3:8 decoder has 3 inputs and 8 outputs; an 8:3 encoder has 8 inputs and 3 outputs.</p>")
_a15_gu = ("<p>m data lines વાળા MUX/DEMUX માટે select lines n = log<sub>2</sub> m (2<sup>n</sup> = m).</p>"
           + tt_html(["Circuit", "Data lines", "Select / code bits"], _rows15, 1)
           + "<p>(a) 8:1 MUX → <b>3</b> select lines. (b) 16:1 MUX → <b>4</b>. (c) 1:8 DEMUX → <b>3</b> select lines. 3:8 decoder માં 3 inputs અને 8 outputs; 8:3 encoder માં 8 inputs અને 3 outputs.</p>")

NUMERICALS = [
    N("de4n1", "Implement a half adder using NAND gates only and verify it.", "માત્ર NAND gates વડે half adder બનાવો અને ચકાસો.", _a1_en, _a1_gu),
    N("de4n2", "Find S and Cout of a full adder for (A, B, Cin) = (1, 1, 0), (1, 0, 1), (1, 1, 1) and (0, 1, 0).",
      "(A, B, Cin) = (1, 1, 0), (1, 0, 1), (1, 1, 1) અને (0, 1, 0) માટે full adder ના S અને Cout શોધો.", _a2_en, _a2_gu),
    N("de4n3", "Show that the sum of a full adder is S = A ⊕ B ⊕ Cin.", "સાબિત કરો કે full adder નો sum S = A ⊕ B ⊕ Cin છે.", _a3, _a3_gu),
    N("de4n4", "Add 1011 and 0111 using a 4-bit ripple-carry adder (four full adders). Show the output of each stage.",
      "4-bit ripple-carry adder (ચાર full adders) વડે 1011 અને 0111 ઉમેરો. દરેક stage નો output બતાવો.", _a4_en, _a4_gu),
    N("de4n5", "Prove that AB + (A ⊕ B)Cin = AB + B·Cin + A·Cin (carry of a full adder made with two half adders).",
      "સાબિત કરો કે AB + (A ⊕ B)Cin = AB + B·Cin + A·Cin (બે half adders થી બનેલા full adder નો carry).", _a5, _a5_gu),
    N("de4n6", "Find the outputs of a half subtractor for all inputs. What are D and Bo for A = 0, B = 1?",
      "બધા inputs માટે half subtractor ના outputs શોધો. A = 0, B = 1 માટે D અને Bo શું છે?", _a6_en, _a6_gu),
    N("de4n7", "Find D and Bout of a full subtractor for (A, B, Bin) = (0, 1, 1), (1, 0, 1), (1, 1, 1) and (0, 0, 1).",
      "(A, B, Bin) = (0, 1, 1), (1, 0, 1), (1, 1, 1) અને (0, 0, 1) માટે full subtractor ના D અને Bout શોધો.", _a7_en, _a7_gu),
    N("de4n8", "Subtract 0111 from 1010 using four full subtractors. Show each stage.",
      "ચાર full subtractors વડે 1010 માંથી 0111 બાદ કરો. દરેક stage બતાવો.", _a8_en, _a8_gu),
    N("de4n9", "For a 4-to-2 encoder find the output when (a) only D2 = 1, (b) D1 = D2 = 1. Comment.",
      "4-to-2 encoder માટે output શોધો જ્યારે (a) માત્ર D2 = 1, (b) D1 = D2 = 1. ટિપ્પણી કરો.", _a9_en, _a9_gu),
    N("de4n10", "Implement F1 = A ⊕ B and F2 = A ⊙ B using a 2-to-4 decoder and OR gates.",
      "2-to-4 decoder અને OR gates વડે F1 = A ⊕ B અને F2 = A ⊙ B બનાવો.", _a10_en, _a10_gu),
    N("de4n11", "A 4-to-1 MUX has I0 = 1, I1 = 0, I2 = 1, I3 = 1. Find Y for S1S0 = 01 and for all select inputs.",
      "4-to-1 MUX માં I0 = 1, I1 = 0, I2 = 1, I3 = 1 છે. S1S0 = 01 અને બધા select inputs માટે Y શોધો.", _a11_en, _a11_gu),
    N("de4n12", "Implement F(A, B) = A ⊕ B using a 4-to-1 multiplexer.", "4-to-1 multiplexer વડે F(A, B) = A ⊕ B બનાવો.", _a12_en, _a12_gu),
    N("de4n13", "Implement F(A, B, C) = Σm(1, 3, 5, 6) using a 4-to-1 multiplexer.", "4-to-1 multiplexer વડે F(A, B, C) = Σm(1, 3, 5, 6) બનાવો.", _a13_en, _a13_gu),
    N("de4n14", "For a 1-to-4 DEMUX find all outputs when (a) D = 1, S1S0 = 10, (b) D = 0, S1S0 = 10. (c) How is D sent to Y3?",
      "1-to-4 DEMUX માટે બધા outputs શોધો જ્યારે (a) D = 1, S1S0 = 10, (b) D = 0, S1S0 = 10. (c) D ને Y3 પર કેવી રીતે મોકલાય?", _a14_en, _a14_gu),
    N("de4n15", "How many select lines are needed for (a) an 8:1 MUX, (b) a 16:1 MUX, (c) a 1:8 DEMUX?",
      "(a) 8:1 MUX, (b) 16:1 MUX, (c) 1:8 DEMUX માટે કેટલી select lines જોઈએ?", _a15_en, _a15_gu),
]

EQUATIONS = [
    {"title": {"en": "Adders", "gu": "Adders"}, "items": [
        E("Half adder: Sum", "Half adder: Sum", "S = " + B("!AB") + " + " + B("A!B") + " = A ⊕ B", "1 when inputs differ", "Inputs જુદા હોય ત્યારે 1"),
        E("Half adder: Carry", "Half adder: Carry", "C = AB", "1 when both inputs are 1", "બંને inputs 1 હોય ત્યારે 1"),
        E("Full adder: Sum", "Full adder: Sum", "S = A ⊕ B ⊕ Cin = Σm(1, 2, 4, 7)", "1 when an odd number of inputs are 1", "Odd number of inputs 1 હોય ત્યારે 1"),
        E("Full adder: Carry", "Full adder: Carry", "Cout = AB + B·Cin + A·Cin = Σm(3, 5, 6, 7)", "Majority of A, B, Cin", "A, B, Cin નું majority"),
        E("FA from two HAs", "બે HAs થી FA", "Cout = AB + (A ⊕ B)·Cin", "C1 = AB from HA1, C2 = (A⊕B)Cin from HA2", "HA1 માંથી C1 = AB, HA2 માંથી C2 = (A⊕B)Cin"),
    ]},
    {"title": {"en": "Subtractors", "gu": "Subtractors"}, "items": [
        E("Half subtractor: Difference", "Half subtractor: Difference", "D = A ⊕ B", "Same as half-adder sum", "Half-adder sum જેવું"),
        E("Half subtractor: Borrow", "Half subtractor: Borrow", "Bo = " + B("!AB"), "Borrow only for 0 − 1", "માત્ર 0 − 1 માટે borrow"),
        E("Full subtractor: Difference", "Full subtractor: Difference", "D = A ⊕ B ⊕ Bin = Σm(1, 2, 4, 7)", "", ""),
        E("Full subtractor: Borrow", "Full subtractor: Borrow", "Bout = " + B("!AB") + " + " + B("!A") + "·Bin + B·Bin = Σm(1, 2, 3, 7)", "", ""),
    ]},
    {"title": {"en": "Data Transmission Circuits", "gu": "Data Transmission Circuits"}, "items": [
        E("4-to-2 encoder", "4-to-2 encoder", "Y1 = D2 + D3, &nbsp; Y0 = D1 + D3", "One input active at a time", "એક સમયે એક જ input active"),
        E("2-to-4 decoder", "2-to-4 decoder", f"Y0 = {B('!A!B')}, Y1 = {B('!AB')}, Y2 = {B('A!B')}, Y3 = AB", "Each output is a minterm", "દરેક output એક minterm"),
        E("4-to-1 MUX", "4-to-1 MUX", f"Y = {S1}{S0}I0 + {S1}S0I1 + S1{S0}I2 + S1S0I3", "S1S0 selects the input", "S1S0 input પસંદ કરે"),
        E("1-to-4 DEMUX", "1-to-4 DEMUX", f"Y0 = D{S1}{S0}, Y1 = D{S1}S0, Y2 = DS1{S0}, Y3 = DS1S0", "D goes to the selected output", "D પસંદ થયેલા output પર જાય"),
        E("Select lines", "Select lines", "n = log<sub>2</sub> m &nbsp; (2<sup>n</sup> = m)", "m = number of data lines", "m = data lines ની સંખ્યા"),
    ]},
]

VIVA = [
    {"title": {"en": "Combinational and Arithmetic Circuits", "gu": "Combinational અને Arithmetic Circuits"}, "items": [
        V("What is a combinational circuit?", "Combinational circuit શું છે?", "A circuit whose output depends only on the present inputs; it has no memory.", "જેનો output માત્ર હાલના inputs પર આધાર રાખે તેવો circuit; તેમાં memory નથી."),
        V("Give two examples of combinational circuits.", "Combinational circuits ના બે ઉદાહરણ આપો.", "Adder and multiplexer (also decoder, encoder, subtractor).", "Adder અને multiplexer (decoder, encoder, subtractor પણ)."),
        V("What is a half adder?", "Half adder શું છે?", "A circuit that adds two bits and gives Sum and Carry.", "બે bits ઉમેરી Sum અને Carry આપતો circuit."),
        V("Which gates make a half adder?", "Half adder કયા gates થી બને?", "One XOR gate (Sum) and one AND gate (Carry).", "એક XOR gate (Sum) અને એક AND gate (Carry)."),
        V("Why is it called a 'half' adder?", "તેને 'half' adder કેમ કહે છે?", "It cannot add a carry from the previous stage.", "તે અગાઉના stage નો carry ઉમેરી શકતો નથી."),
        V("What is a full adder?", "Full adder શું છે?", "A circuit that adds three bits A, B and Cin, giving Sum and Cout.", "ત્રણ bits A, B અને Cin ઉમેરી Sum અને Cout આપતો circuit."),
        V("Write the sum and carry of a full adder.", "Full adder ના sum અને carry લખો.", "S = A ⊕ B ⊕ Cin; Cout = AB + B·Cin + A·Cin.", "S = A ⊕ B ⊕ Cin; Cout = AB + B·Cin + A·Cin."),
        V("How many half adders make a full adder?", "Full adder માટે કેટલા half adders જોઈએ?", "Two half adders and one OR gate.", "બે half adders અને એક OR gate."),
        V("How many NAND gates make a half adder?", "Half adder માટે કેટલા NAND gates જોઈએ?", "Five.", "પાંચ."),
        V("What is a ripple-carry adder?", "Ripple-carry adder શું છે?", "Full adders in cascade where each carry goes to the next stage; IC 7483 is a 4-bit adder.", "Cascade માં full adders જેમાં દરેક carry પછીના stage માં જાય; IC 7483 4-bit adder છે."),
        V("Write the outputs of a half subtractor.", "Half subtractor ના outputs લખો.", "D = A ⊕ B, Bo = " + B("!AB") + ".", "D = A ⊕ B, Bo = " + B("!AB") + "."),
        V("Write the borrow of a full subtractor.", "Full subtractor નો borrow લખો.", "Bout = " + B("!AB") + " + " + B("!A") + "·Bin + B·Bin.", "Bout = " + B("!AB") + " + " + B("!A") + "·Bin + B·Bin."),
        V("Which output is the same in an adder and a subtractor?", "Adder અને subtractor માં કયો output સરખો છે?", "Sum and Difference: both are XOR of the inputs.", "Sum અને Difference: બંને inputs નો XOR છે."),
    ]},
    {"title": {"en": "Encoder, Decoder, MUX and DEMUX", "gu": "Encoder, Decoder, MUX અને DEMUX"}, "items": [
        V("What is an encoder?", "Encoder શું છે?", "A circuit that converts one active input out of 2ⁿ into an n-bit code.", "2ⁿ માંથી એક active input ને n-bit code માં ફેરવતો circuit."),
        V("Write the equations of a 4-to-2 encoder.", "4-to-2 encoder ના equations લખો.", "Y1 = D2 + D3, Y0 = D1 + D3.", "Y1 = D2 + D3, Y0 = D1 + D3."),
        V("What is a priority encoder?", "Priority encoder શું છે?", "An encoder that gives the code of the highest-priority input when several are active.", "ઘણા inputs active હોય ત્યારે સૌથી વધુ priority વાળા input નો code આપતો encoder."),
        V("What is a decoder?", "Decoder શું છે?", "A circuit that converts an n-bit code into 2ⁿ outputs, with only one active.", "n-bit code ને 2ⁿ outputs માં ફેરવતો circuit, જેમાં એક જ active."),
        V("Why is a decoder called a minterm generator?", "Decoder ને minterm generator કેમ કહે છે?", "Each of its outputs is one minterm of the inputs.", "તેનો દરેક output inputs નો એક minterm છે."),
        V("What is a multiplexer?", "Multiplexer શું છે?", "A data selector: it sends one of many inputs to a single output using select lines.", "Data selector: select lines વડે ઘણા inputs માંથી એકને એક output પર મોકલે."),
        V("How many select lines does a 4:1 MUX have?", "4:1 MUX માં કેટલી select lines હોય?", "Two.", "બે."),
        V("What is a demultiplexer?", "Demultiplexer શું છે?", "A data distributor: it sends one input to one of many outputs.", "Data distributor: એક input ને ઘણા outputs માંથી એક પર મોકલે."),
        V("How can a DEMUX be used as a decoder?", "DEMUX ને decoder તરીકે કેવી રીતે વપરાય?", "Keep the data input at 1 and use the select lines as decoder inputs.", "Data input ને 1 રાખી select lines ને decoder inputs તરીકે વાપરો."),
        V("Give one application each of MUX and DEMUX.", "MUX અને DEMUX નો એક-એક ઉપયોગ આપો.", "MUX: parallel-to-serial conversion; DEMUX: serial-to-parallel conversion.", "MUX: parallel-to-serial conversion; DEMUX: serial-to-parallel conversion."),
        V("Name ICs for a 4:1 MUX and a 2:4 decoder.", "4:1 MUX અને 2:4 decoder ના ICs જણાવો.", "74153 (dual 4:1 MUX); 74139 (dual 2:4 decoder).", "74153 (dual 4:1 MUX); 74139 (dual 2:4 decoder)."),
    ]},
]

EXAM_QS = [
    X("Define combinational circuit. Give its block diagram and examples.", "Combinational circuit ની વ્યાખ્યા આપો. તેનો block diagram અને ઉદાહરણો આપો.", 3),
    X("Explain the design procedure of combinational circuits.", "Combinational circuits ની design procedure સમજાવો.", 3),
    X("Explain the half adder with block diagram, truth table and logic diagram.", "Block diagram, truth table અને logic diagram સાથે half adder સમજાવો.", 4),
    X("Design a full adder using a truth table and K-maps; draw its logic diagram.", "Truth table અને K-maps વડે full adder design કરો; તેનો logic diagram દોરો.", 7),
    X("Implement a full adder using two half adders.", "બે half adders વડે full adder બનાવો.", 4),
    X("Explain the half subtractor with truth table and logic diagram.", "Truth table અને logic diagram સાથે half subtractor સમજાવો.", 4),
    X("Design a full subtractor and draw its logic diagram.", "Full subtractor design કરી તેનો logic diagram દોરો.", 7),
    X("Compare half adder and full adder.", "Half adder અને full adder ની સરખામણી કરો.", 3),
    X("Implement a half adder using NAND gates only.", "માત્ર NAND gates વડે half adder બનાવો.", 4),
    X("Explain the 4-to-2 encoder with block diagram and truth table.", "Block diagram અને truth table સાથે 4-to-2 encoder સમજાવો.", 3),
    X("Explain the 2-to-4 decoder with block diagram, truth table and logic diagram.", "Block diagram, truth table અને logic diagram સાથે 2-to-4 decoder સમજાવો.", 4),
    X("What is a multiplexer? Explain the 4-to-1 MUX with block diagram, truth table and logic diagram.", "Multiplexer શું છે? Block diagram, truth table અને logic diagram સાથે 4-to-1 MUX સમજાવો.", 7),
    X("Explain the 1-to-4 demultiplexer with block diagram, truth table and logic diagram.", "Block diagram, truth table અને logic diagram સાથે 1-to-4 demultiplexer સમજાવો.", 4),
    X("Differentiate between multiplexer and demultiplexer.", "Multiplexer અને demultiplexer વચ્ચે તફાવત આપો.", 3),
    X("Differentiate between encoder and decoder.", "Encoder અને decoder વચ્ચે તફાવત આપો.", 3),
    X("Implement F(A, B, C) = Σm(1, 3, 5, 6) using a 4-to-1 multiplexer.", "4-to-1 multiplexer વડે F(A, B, C) = Σm(1, 3, 5, 6) બનાવો.", 4),
]
