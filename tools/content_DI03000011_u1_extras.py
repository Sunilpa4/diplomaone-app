"""Digital Electronics Fundamentals (DI03000011) - Unit 1 extras: numericals (computed by de_num), equations, viva, exam."""
from fractions import Fraction
import de_num as D

S = lambda n, b: f"({n})<sub>{b}</sub>"


def N(id_, q_en, q_gu, a_en, a_gu):
    return {"id": id_, "q": {"en": q_en, "gu": q_gu}, "a": {"en": a_en, "gu": a_gu}}


def to_dec(id_, s, b):
    v, expr, (ten, tgu) = D.to_decimal(s, b)
    ans = f"<p>{S(s, b)} = {expr}</p>"
    r = f"<p><b>{S(s, b)} = {S(D.fmt(v), 10)}</b></p>"
    return N(id_, f"Convert {S(s, b)} to decimal.", f"{S(s, b)} ને decimal માં ફેરવો.", ten + ans + r, tgu + ans + r), v


def dec_to(id_, n, b, frac=None, places=6, note_en="", note_gu=""):
    ip, (ten, tgu) = D.int_to_base(n, b)
    q = f"{n}" + (f"{str(float(frac))[1:]}" if frac is not None else "")
    en = f"<p><b>Integer part</b> ({n}): repeated division by {b}</p>" + ten + f"<p>Remainders read upward: {S(ip, b)}</p>"
    gu = f"<p><b>Integer ભાગ</b> ({n}): {b} વડે વારંવાર ભાગાકાર</p>" + tgu + f"<p>શેષ ઉપર તરફ વાંચતાં: {S(ip, b)}</p>"
    res = ip
    if frac is not None:
        fd, exact, (fen, fgu) = D.frac_to_base(frac, b, places)
        en += f"<p><b>Fraction part</b> ({str(float(frac))[1:]}): repeated multiplication by {b}</p>" + fen + f"<p>Integer parts read downward: .{fd}</p>"
        gu += f"<p><b>Fraction ભાગ</b> ({str(float(frac))[1:]}): {b} વડે વારંવાર ગુણાકાર</p>" + fgu + f"<p>Integer ભાગો નીચે તરફ વાંચતાં: .{fd}</p>"
        res = ip + "." + fd
    name = D.BASE_NAME[b][0]
    tail = f"<p><b>{S(q, 10)} = {S(res, b)}</b></p>"
    return N(id_, f"Convert {S(q, 10)} to {name}.", f"{S(q, 10)} ને {name} માં ફેરવો.", en + tail + note_en, gu + tail + note_gu), res


def bin_to_oh(id_, bits):
    o, gi, gf, (oen, ogu) = D.bin_group(bits, 3)
    h, hi, hf, (hen, hgu) = D.bin_group(bits, 4)
    assert (o, h) == ("326.54", "D6.B")
    en = (f"<p><b>Octal:</b> groups of 3 from the point: {' '.join(gi)} . {' '.join(gf)}</p>" + oen + f"<p>{S(bits, 2)} = <b>{S(o, 8)}</b></p>"
          f"<p><b>Hexadecimal:</b> groups of 4 from the point: {' '.join(hi)} . {' '.join(hf)}</p>" + hen + f"<p>{S(bits, 2)} = <b>{S(h, 16)}</b></p>")
    gu = (f"<p><b>Octal:</b> point થી 3 ના groups: {' '.join(gi)} . {' '.join(gf)}</p>" + ogu + f"<p>{S(bits, 2)} = <b>{S(o, 8)}</b></p>"
          f"<p><b>Hexadecimal:</b> point થી 4 ના groups: {' '.join(hi)} . {' '.join(hf)}</p>" + hgu + f"<p>{S(bits, 2)} = <b>{S(h, 16)}</b></p>")
    return N(id_, f"Convert {S(bits, 2)} to octal and hexadecimal.", f"{S(bits, 2)} ને octal અને hexadecimal માં ફેરવો.", en, gu)


def oh_to_bin(id_):
    r1, (a_en, a_gu) = D.to_bin_from("3A7.C", 16)
    r2, (b_en, b_gu) = D.to_bin_from("527", 8)
    assert (r1, r2) == ("1110100111.11", "101010111")
    en = (f"<p><b>(i)</b> Write each hex digit as 4 bits:</p>" + a_en + f"<p>{S('3A7.C', 16)} = <b>{S(r1, 2)}</b> (leading and trailing zeros removed)</p>"
          f"<p><b>(ii)</b> Write each octal digit as 3 bits:</p>" + b_en + f"<p>{S('527', 8)} = <b>{S(r2, 2)}</b></p>")
    gu = (f"<p><b>(i)</b> દરેક hex digit ને 4 bits માં લખો:</p>" + a_gu + f"<p>{S('3A7.C', 16)} = <b>{S(r1, 2)}</b> (આગળ-પાછળના zeros દૂર કર્યા)</p>"
          f"<p><b>(ii)</b> દરેક octal digit ને 3 bits માં લખો:</p>" + b_gu + f"<p>{S('527', 8)} = <b>{S(r2, 2)}</b></p>")
    return N(id_, f"Convert (i) {S('3A7.C', 16)} and (ii) {S('527', 8)} to binary.",
             f"(i) {S('3A7.C', 16)} અને (ii) {S('527', 8)} ને binary માં ફેરવો.", en, gu)


def oct_hex(id_, s, frm):
    if frm == 8:
        b, _ = D.to_bin_from(s, 8)
        res, gi, gf, _ = D.bin_group(b, 4)
        g_from = " ".join(format(int(c), "03b") for c in s)
        to, k1, k2 = 16, 3, 4
    else:
        b, _ = D.to_bin_from(s, 16)
        res, gi, gf, _ = D.bin_group(b, 3)
        g_from = " ".join(format(int(c, 16), "04b") for c in s)
        to, k1, k2 = 8, 4, 3
    assert int(res, to) == int(s, frm)
    dv = int(s, frm)
    en = (f"<p>Step 1: each digit → {k1} bits: {g_from}</p><p>Binary = {b}</p>"
          f"<p>Step 2: regroup in {k2} bits from the right: {' '.join(gi)}</p><p>Step 3: write each group as a digit: <b>{S(res, to)}</b></p>"
          f"<p><i>Check:</i> both equal {S(dv, 10)}.</p>")
    gu = (f"<p>Step 1: દરેક digit → {k1} bits: {g_from}</p><p>Binary = {b}</p>"
          f"<p>Step 2: જમણી બાજુથી {k2} bits ના groups ફરી બનાવો: {' '.join(gi)}</p><p>Step 3: દરેક group ને digit તરીકે લખો: <b>{S(res, to)}</b></p>"
          f"<p><i>ચકાસણી:</i> બંને {S(dv, 10)} બરાબર છે.</p>")
    nm = {8: "octal", 16: "hexadecimal"}[to]
    return N(id_, f"Convert {S(s, frm)} to {nm}.", f"{S(s, frm)} ને {nm} માં ફેરવો.", en, gu), res


def add_q(id_):
    r1, p1 = D.add_work("101101", "11011")
    r2, p2 = D.add_work("1101.11", "1011.01") if False else (None, None)
    a, b = "110110", "101011"
    r3, p3 = D.add_work(a, b)
    assert (r1, r3) == ("1001000", "1100001")
    en = (f"<p><b>(i)</b> 101101 + 11011 (45 + 27):</p>{p1}<p>= <b>(1001000)<sub>2</sub></b> = 72 ✓</p>"
          f"<p><b>(ii)</b> 110110 + 101011 (54 + 43):</p>{p3}<p>= <b>(1100001)<sub>2</sub></b> = 97 ✓</p>")
    gu = (f"<p><b>(i)</b> 101101 + 11011 (45 + 27):</p>{p1}<p>= <b>(1001000)<sub>2</sub></b> = 72 ✓</p>"
          f"<p><b>(ii)</b> 110110 + 101011 (54 + 43):</p>{p3}<p>= <b>(1100001)<sub>2</sub></b> = 97 ✓</p>")
    return N(id_, "Add: (i) 101101 + 11011 (ii) 110110 + 101011", "સરવાળો કરો: (i) 101101 + 11011 (ii) 110110 + 101011", en, gu)


def sub_q(id_, a, b, meth):
    f = D.sub_ones if meth == 1 else D.sub_twos
    res, se, sg = f(a, b)
    va, vb = int(a, 2), int(b, 2)
    chk = f"<p><i>Check:</i> {va} − {vb} = {va - vb} ✓</p>".replace("= -", "= −")
    chk_g = f"<p><i>ચકાસણી:</i> {va} − {vb} = {va - vb} ✓</p>".replace("= -", "= −")
    m = "1's" if meth == 1 else "2's"
    return N(id_, f"Subtract {S(b, 2)} from {S(a, 2)} using {m} complement.",
             f"{m} complement વડે {S(a, 2)} માંથી {S(b, 2)} બાદ કરો.",
             D.steps_html(se) + f"<p><b>Answer = {res.replace('-', '−')}</b></p>" + chk, D.steps_html(sg) + f"<p><b>જવાબ = {res.replace('-', '−')}</b></p>" + chk_g), res


_n1, v1 = to_dec("de1n1", "10110.011", 2)
_n2, v2 = to_dec("de1n2", "2AF.8", 16)
_n3, v3 = to_dec("de1n3", "157.4", 8)
assert (v1, v2, v3) == (Fraction(179, 8), Fraction(1375, 2), Fraction(223, 2))
_n4, r4 = dec_to("de1n4", 156, 2)
_n5, r5 = dec_to("de1n5", 25, 2, Fraction(11, 16))
_n6, r6 = dec_to("de1n6", 12, 2, Fraction(3, 10), 5,
                 "<p><i>The fraction does not become 0 (0.6 → 0.2 → 0.4 → 0.8 → 0.6 repeats), so the answer is approximate (5 places).</i></p>",
                 "<p><i>Fraction 0 થતો નથી (0.6 → 0.2 → 0.4 → 0.8 → 0.6 પુનરાવર્તન), તેથી જવાબ અંદાજિત છે (5 places).</i></p>")
_n7, r7 = dec_to("de1n7", 359, 8, Fraction(1, 4))
_n8, r8 = dec_to("de1n8", 4823, 16)
assert (r4, r5, r6, r7, r8) == ("10011100", "11001.1011", "1100.01001", "547.2", "12D7")
_n11, r11 = oct_hex("de1n11", "725", 8)
_n12, r12 = oct_hex("de1n12", "B2F", 16)
assert (r11, r12) == ("1D5", "5457")

_sd, _pre = D.sub_direct("11010", "10011")
assert _sd == "00111"
_n14 = N("de1n14", "Subtract 10011 from 11010 using the direct (borrow) method.", "Direct (borrow) method થી 11010 માંથી 10011 બાદ કરો.",
         f"<p>Borrow rule: 0 − 1 = 1 with borrow 1 from the next column (a borrowed 1 = 2 in this column).</p>{_pre}<p><b>Answer = (00111)<sub>2</sub> = 7</b>. Check: 26 − 19 = 7 ✓</p>",
         f"<p>Borrow નિયમ: 0 − 1 = 1 અને આગળના column માંથી 1 borrow (ઉધાર લીધેલો 1 = આ column માં 2).</p>{_pre}<p><b>જવાબ = (00111)<sub>2</sub> = 7</b>. ચકાસણી: 26 − 19 = 7 ✓</p>")

_c = [("10110", D.ones("10110"), D.twos("10110")), ("1101000", D.ones("1101000"), D.twos("1101000")), ("0111", D.ones("0111"), D.twos("0111"))]
assert _c[1][2] == "0011000"
_rows = "".join(f"<tr><td>{a}</td><td>{b}</td><td>{c}</td></tr>" for a, b, c in _c)
_n15 = N("de1n15", "Find the 1's and 2's complement of (i) 10110 (ii) 1101000 (iii) 0111.",
         "(i) 10110 (ii) 1101000 (iii) 0111 ના 1's અને 2's complement શોધો.",
         f"<table><tr><th>Number</th><th>1's complement</th><th>2's complement</th></tr>{_rows}</table>"
         "<p>1's complement: invert every bit. 2's complement: 1's complement + 1.</p><p>E.g. (ii) 0010111 + 1 = 0011000 (or shortcut: keep '1000', invert '110' → '001').</p>",
         f"<table><tr><th>Number</th><th>1's complement</th><th>2's complement</th></tr>{_rows}</table>"
         "<p>1's complement: દરેક bit invert કરો. 2's complement: 1's complement + 1.</p><p>દા.ત. (ii) 0010111 + 1 = 0011000 (અથવા shortcut: '1000' એમ જ, '110' invert → '001').</p>")

_n16, r16 = sub_q("de1n16", "11010", "10011", 1)
_n17, r17 = sub_q("de1n17", "10011", "11010", 1)
_n18, r18 = sub_q("de1n18", "11010", "10011", 2)
_n19, r19 = sub_q("de1n19", "10011", "11010", 2)
assert (r16, r17, r18, r19) == ("00111", "-00111", "00111", "-00111")

_r20, _se, _sg = D.sub_twos("101101", "011011")
assert _r20 == "010010"
_n20 = N("de1n20", "Perform (45)<sub>10</sub> − (27)<sub>10</sub> in binary using 2's complement.",
         "2's complement વડે binary માં (45)<sub>10</sub> − (27)<sub>10</sub> કરો.",
         "<p>(45)<sub>10</sub> = 101101, (27)<sub>10</sub> = 11011 → 011011 (6 bits)</p>" + D.steps_html(_se) + "<p><b>Answer = (010010)<sub>2</sub> = (18)<sub>10</sub></b> ✓</p>",
         "<p>(45)<sub>10</sub> = 101101, (27)<sub>10</sub> = 11011 → 011011 (6 bits)</p>" + D.steps_html(_sg) + "<p><b>જવાબ = (010010)<sub>2</sub> = (18)<sub>10</sub></b> ✓</p>")

_n21 = N("de1n21", "Represent (58)<sub>10</sub> and (309)<sub>10</sub> in (i) BCD (ii) Excess-3 code.",
         "(58)<sub>10</sub> અને (309)<sub>10</sub> ને (i) BCD (ii) Excess-3 code માં દર્શાવો.",
         "<table><tr><th>Number</th><th>BCD</th><th>Excess-3 (digit + 3)</th></tr>"
         f"<tr><td>58</td><td>0101 1000</td><td>1000 1011</td></tr><tr><td>309</td><td>0011 0000 1001</td><td>0110 0011 1100</td></tr></table>"
         "<p>Each decimal digit is coded separately in 4 bits. For XS-3, add 3 to each digit first (3→6, 0→3, 9→12).</p>",
         "<table><tr><th>Number</th><th>BCD</th><th>Excess-3 (digit + 3)</th></tr>"
         f"<tr><td>58</td><td>0101 1000</td><td>1000 1011</td></tr><tr><td>309</td><td>0011 0000 1001</td><td>0110 0011 1100</td></tr></table>"
         "<p>દરેક decimal digit ને અલગથી 4 bits માં code કરાય છે. XS-3 માટે પહેલાં દરેક digit માં 3 ઉમેરો (3→6, 0→3, 9→12).</p>")
assert " ".join(format(int(c) + 3, "04b") for c in "309") == "0110 0011 1100"


def gray(b):
    return b[0] + "".join(str(int(b[i - 1]) ^ int(b[i])) for i in range(1, len(b)))


def ungray(g):
    out = g[0]
    for i in range(1, len(g)):
        out += str(int(out[-1]) ^ int(g[i]))
    return out


assert gray("1011") == "1110" and ungray("1101") == "1001" and gray("10110") == "11101"
_n22 = N("de1n22", "(i) Convert binary 10110 to Gray code. (ii) Convert Gray code 1101 to binary.",
         "(i) Binary 10110 ને Gray code માં ફેરવો. (ii) Gray code 1101 ને binary માં ફેરવો.",
         "<p><b>(i)</b> MSB same = 1; then 1⊕0 = 1, 0⊕1 = 1, 1⊕1 = 0, 1⊕0 = 1 → Gray = <b>11101</b></p>"
         "<p><b>(ii)</b> MSB same = 1; then 1⊕1 = 0, 0⊕0 = 0, 0⊕1 = 1 (each new binary bit XOR next Gray bit) → Binary = <b>1001</b></p>",
         "<p><b>(i)</b> MSB એમ જ = 1; પછી 1⊕0 = 1, 0⊕1 = 1, 1⊕1 = 0, 1⊕0 = 1 → Gray = <b>11101</b></p>"
         "<p><b>(ii)</b> MSB એમ જ = 1; પછી 1⊕1 = 0, 0⊕0 = 0, 0⊕1 = 1 (દરેક નવો binary bit XOR પછીનો Gray bit) → Binary = <b>1001</b></p>")

NUMERICALS = [_n1, _n2, _n3, _n4, _n5, _n6, _n7, _n8, bin_to_oh("de1n9", "11010110.1011"), oh_to_bin("de1n10"), _n11, _n12,
              add_q("de1n13"), _n14, _n15, _n16, _n17, _n18, _n19, _n20, _n21, _n22]


def E(name_en, name_gu, f, terms_en, terms_gu):
    return {"name": {"en": name_en, "gu": name_gu}, "f": f, "terms": {"en": terms_en, "gu": terms_gu}}


EQUATIONS = [
    {"title": {"en": "Number Systems", "gu": "Number Systems"}, "items": [
        E("Value of a number in base r", "Base r માં સંખ્યાની કિંમત", "N = Σ d<sub>i</sub> × r<sup>i</sup>",
          "i = 0, 1, 2 … left of point; −1, −2 … right of point", "Point ની ડાબી બાજુ i = 0, 1, 2 …; જમણી બાજુ −1, −2 …"),
        E("Number of combinations", "Combinations ની સંખ્યા", "Combinations = 2<sup>n</sup>; range 0 to 2<sup>n</sup> − 1",
          "n = number of bits", "n = bits ની સંખ્યા"),
        E("Bits per digit", "દરેક digit ના bits", "Octal digit = 3 bits; Hex digit = 4 bits", "8 = 2³, 16 = 2⁴", "8 = 2³, 16 = 2⁴"),
        E("Binary weights", "Binary weights", "… 16, 8, 4, 2, 1 . 0.5, 0.25, 0.125 …", "2⁴ … 2⁰ . 2⁻¹ 2⁻² 2⁻³", "2⁴ … 2⁰ . 2⁻¹ 2⁻² 2⁻³"),
        E("Hex digits", "Hex digits", "A=10, B=11, C=12, D=13, E=14, F=15", "", ""),
    ]},
    {"title": {"en": "Conversion Rules", "gu": "Conversion ના નિયમો"}, "items": [
        E("Decimal integer → base r", "Decimal integer → base r", "Divide by r repeatedly; remainders bottom → top",
          "First remainder = LSB", "પહેલી શેષ = LSB"),
        E("Decimal fraction → base r", "Decimal fraction → base r", "Multiply by r repeatedly; integer parts top → bottom",
          "Stop at 0 or after 4–6 digits", "0 થાય અથવા 4–6 digits પછી અટકો"),
        E("Binary → octal / hex", "Binary → octal / hex", "Group 3 / 4 bits from the binary point",
          "Pad zeros at the outer ends", "બહારના છેડે zeros ઉમેરો"),
    ]},
    {"title": {"en": "Arithmetic and Complements", "gu": "Arithmetic અને Complements"}, "items": [
        E("Binary addition", "Binary addition", "0+0=0, 0+1=1, 1+1=10, 1+1+1=11", "Second bit of 10 / 11 is the sum, first is carry", "10 / 11 માં છેલ્લો bit sum, પહેલો carry"),
        E("Binary subtraction", "Binary subtraction", "0−0=0, 1−0=1, 1−1=0, 0−1=1 borrow 1", "", ""),
        E("1's complement", "1's complement", "Invert all bits (0↔1)", "", ""),
        E("2's complement", "2's complement", "2's comp = 1's comp + 1", "r's comp = (r−1)'s comp + 1", "r's comp = (r−1)'s comp + 1"),
        E("A − B by 1's complement", "1's complement વડે A − B", "A + 1's(B): carry → add to LSB (+ve); no carry → −1's(sum)",
          "End-around carry", "End-around carry"),
        E("A − B by 2's complement", "2's complement વડે A − B", "A + 2's(B): carry → discard (+ve); no carry → −2's(sum)", "", ""),
        E("Range of n-bit 2's complement", "n-bit 2's complement ની range", "−2<sup>n−1</sup> to +(2<sup>n−1</sup> − 1)", "8 bits: −128 to +127", "8 bits: −128 થી +127"),
    ]},
    {"title": {"en": "Codes", "gu": "Codes"}, "items": [
        E("Excess-3", "Excess-3", "XS-3 = BCD + 0011 (per digit)", "", ""),
        E("Binary → Gray", "Binary → Gray", "G<sub>MSB</sub> = B<sub>MSB</sub>; G<sub>i</sub> = B<sub>i+1</sub> ⊕ B<sub>i</sub>", "", ""),
        E("Gray → Binary", "Gray → Binary", "B<sub>MSB</sub> = G<sub>MSB</sub>; B<sub>i</sub> = B<sub>i+1</sub> ⊕ G<sub>i</sub>", "", ""),
    ]},
]


def V(q_en, q_gu, a_en, a_gu):
    return {"q": {"en": q_en, "gu": q_gu}, "a": {"en": a_en, "gu": a_gu}}


VIVA = [
    {"title": {"en": "Digital Systems", "gu": "Digital Systems"}, "items": [
        V("What is a digital signal?", "Digital signal એટલે શું?", "A discrete signal with only two levels, 0 (LOW) and 1 (HIGH).", "માત્ર બે levels, 0 (LOW) અને 1 (HIGH), વાળો discrete signal."),
        V("What is an analog signal?", "Analog signal એટલે શું?", "A continuous signal that can have any value in a range.", "Range માં કોઈ પણ કિંમત લઈ શકે તેવો continuous signal."),
        V("Give two advantages of digital systems.", "Digital systems ના બે ફાયદા આપો.", "Less affected by noise; easy to store data; high accuracy.", "Noise ની અસર ઓછી; data store કરવો સરળ; વધુ ચોકસાઈ."),
        V("What is the use of an ADC?", "ADC નો ઉપયોગ શું છે?", "It converts an analog signal into digital form.", "તે analog signal ને digital સ્વરૂપમાં ફેરવે છે."),
        V("What is a bit? What is a nibble and a byte?", "Bit શું છે? Nibble અને byte શું છે?", "Bit = one binary digit; nibble = 4 bits; byte = 8 bits.", "Bit = એક binary digit; nibble = 4 bits; byte = 8 bits."),
        V("What are MSB and LSB?", "MSB અને LSB શું છે?", "MSB is the left-most bit with highest weight; LSB is the right-most bit with lowest weight.", "MSB સૌથી ડાબો અને સૌથી વધુ weight વાળો bit; LSB સૌથી જમણો અને સૌથી ઓછા weight વાળો bit."),
    ]},
    {"title": {"en": "Number Systems and Conversion", "gu": "Number Systems અને Conversion"}, "items": [
        V("What is the base (radix) of a number system?", "Number system નો base (radix) શું છે?", "The number of different digits used in that system.", "તે system માં વપરાતા જુદા જુદા digits ની સંખ્યા."),
        V("What are the bases of binary, octal, decimal and hexadecimal?", "Binary, octal, decimal અને hexadecimal ના base કયા છે?", "2, 8, 10 and 16.", "2, 8, 10 અને 16."),
        V("Why is binary used in computers?", "Computers માં binary કેમ વપરાય છે?", "Electronic devices have two stable states (ON/OFF), so two-level circuits are simple and reliable.", "Electronic devices ની બે stable અવસ્થા (ON/OFF) હોય છે, તેથી બે-level circuits સરળ અને વિશ્વસનીય છે."),
        V("Why are octal and hexadecimal used?", "Octal અને hexadecimal કેમ વપરાય છે?", "As short, readable forms of long binary numbers.", "લાંબી binary સંખ્યાઓના ટૂંકા અને વાંચી શકાય તેવા સ્વરૂપ તરીકે."),
        V("How many bits represent one hex digit?", "એક hex digit માટે કેટલા bits જોઈએ?", "Four bits (one nibble).", "ચાર bits (એક nibble)."),
        V("What is the decimal value of F in hexadecimal?", "Hexadecimal માં F ની decimal કિંમત શું છે?", "15.", "15."),
        V("Which method converts decimal integers to binary?", "Decimal integer ને binary માં કઈ method થી ફેરવાય?", "Repeated division by 2; remainders read from bottom to top.", "2 વડે વારંવાર ભાગાકાર; શેષ નીચેથી ઉપર વાંચવી."),
        V("Which method converts a decimal fraction to binary?", "Decimal fraction ને binary માં કઈ method થી ફેરવાય?", "Repeated multiplication by 2; integer parts read from top to bottom.", "2 વડે વારંવાર ગુણાકાર; integer ભાગો ઉપરથી નીચે વાંચવા."),
        V("How is octal converted to hexadecimal?", "Octal ને hexadecimal માં કેવી રીતે ફેરવાય?", "Through binary: each octal digit to 3 bits, then regroup in 4 bits.", "Binary મારફતે: દરેક octal digit ના 3 bits, પછી 4 bits માં ફરી group."),
        V("What is (1111)₂ in decimal and hex?", "(1111)₂ ની decimal અને hex કિંમત શું છે?", "15 and F.", "15 અને F."),
    ]},
    {"title": {"en": "Arithmetic and Complements", "gu": "Arithmetic અને Complements"}, "items": [
        V("What is 1 + 1 in binary?", "Binary માં 1 + 1 કેટલા?", "10 (sum 0, carry 1).", "10 (sum 0, carry 1)."),
        V("What is 1's complement?", "1's complement શું છે?", "The number obtained by inverting every bit.", "દરેક bit invert કરવાથી મળતી સંખ્યા."),
        V("How is 2's complement obtained?", "2's complement કેવી રીતે મેળવાય?", "Add 1 to the 1's complement.", "1's complement માં 1 ઉમેરીને."),
        V("What is end-around carry?", "End-around carry શું છે?", "In 1's complement subtraction, the carry is added back to the LSB.", "1's complement subtraction માં carry ને પાછો LSB માં ઉમેરવો."),
        V("In 2's complement subtraction, what is done with the carry?", "2's complement subtraction માં carry નું શું થાય?", "It is discarded; the result is positive.", "તેને અવગણવામાં આવે છે; જવાબ positive છે."),
        V("What does 'no carry' mean in complement subtraction?", "Complement subtraction માં 'carry નહીં' નો અર્થ શું?", "The result is negative and in complement form; take its complement again.", "જવાબ negative છે અને complement સ્વરૂપમાં છે; ફરી complement લો."),
        V("Why is 2's complement preferred?", "2's complement કેમ પસંદ કરાય છે?", "Only one zero, no end-around carry, faster hardware.", "માત્ર એક zero, end-around carry નહીં, ઝડપી hardware."),
        V("What is the range of an 8-bit 2's complement number?", "8-bit 2's complement સંખ્યાની range શું છે?", "−128 to +127.", "−128 થી +127."),
        V("What is the sign bit?", "Sign bit શું છે?", "The MSB of a signed number: 0 = positive, 1 = negative.", "Signed સંખ્યાનો MSB: 0 = positive, 1 = negative."),
    ]},
    {"title": {"en": "Binary Codes", "gu": "Binary Codes"}, "items": [
        V("What is BCD?", "BCD શું છે?", "Binary Coded Decimal: each decimal digit is written as 4 bits (8421).", "Binary Coded Decimal: દરેક decimal digit ને 4 bits (8421) માં લખાય છે."),
        V("Which BCD codes are invalid?", "કયા BCD codes invalid છે?", "1010 to 1111 (10 to 15).", "1010 થી 1111 (10 થી 15)."),
        V("What is Excess-3 code?", "Excess-3 code શું છે?", "BCD + 3 for each digit; a self-complementing, non-weighted code.", "દરેક digit માટે BCD + 3; self-complementing, non-weighted code."),
        V("What is the special property of Gray code?", "Gray code ની વિશેષતા શું છે?", "Only one bit changes between successive numbers.", "ક્રમિક સંખ્યાઓ વચ્ચે માત્ર એક bit બદલાય છે."),
        V("What is ASCII?", "ASCII શું છે?", "A 7-bit alphanumeric code for 128 characters; 'A' = 65.", "128 characters માટેનો 7-bit alphanumeric code; 'A' = 65."),
    ]},
]


def X(q_en, q_gu, marks):
    return {"q": {"en": q_en, "gu": q_gu}, "marks": marks}


EXAM_QS = [
    X("Compare analog and digital signals.", "Analog અને digital signals ની સરખામણી કરો.", 3),
    X("List advantages and disadvantages of digital systems.", "Digital systems ના ફાયદા અને ગેરફાયદા લખો.", 3),
    X("Draw the block diagram of a digital system and give its applications.", "Digital system નો block diagram દોરો અને તેના ઉપયોગો આપો.", 3),
    X("Define: bit, nibble, byte, MSB, LSB.", "વ્યાખ્યા આપો: bit, nibble, byte, MSB, LSB.", 3),
    X("Explain the binary, octal and hexadecimal number systems with examples.", "Binary, octal અને hexadecimal number systems ઉદાહરણ સાથે સમજાવો.", 4),
    X("Convert (10110.011)₂ and (2AF.8)₁₆ to decimal.", "(10110.011)₂ અને (2AF.8)₁₆ ને decimal માં ફેરવો.", 3),
    X("Convert (25.6875)₁₀ to binary, octal and hexadecimal.", "(25.6875)₁₀ ને binary, octal અને hexadecimal માં ફેરવો.", 4),
    X("Convert (4823)₁₀ to hexadecimal and (359.25)₁₀ to octal.", "(4823)₁₀ ને hexadecimal અને (359.25)₁₀ ને octal માં ફેરવો.", 4),
    X("Convert (11010110.1011)₂ to octal and hexadecimal.", "(11010110.1011)₂ ને octal અને hexadecimal માં ફેરવો.", 3),
    X("Convert (725)₈ to hexadecimal and (B2F)₁₆ to octal.", "(725)₈ ને hexadecimal અને (B2F)₁₆ ને octal માં ફેરવો.", 4),
    X("State the rules of binary addition and add 101101 + 11011.", "Binary addition ના નિયમો લખો અને 101101 + 11011 નો સરવાળો કરો.", 3),
    X("Find the 1's and 2's complement of 10110 and 1101000.", "10110 અને 1101000 ના 1's અને 2's complement શોધો.", 3),
    X("Subtract 10011 from 11010 using 1's complement and 2's complement methods.", "1's complement અને 2's complement methods થી 11010 માંથી 10011 બાદ કરો.", 4),
    X("Explain subtraction using 2's complement with a flowchart and example (including a negative result).", "Flowchart અને ઉદાહરણ (negative જવાબ સહિત) સાથે 2's complement વડે subtraction સમજાવો.", 7),
    X("Explain number system conversions (all bases) with one example each.", "દરેકનું એક ઉદાહરણ આપી number system conversions (બધા bases) સમજાવો.", 7),
    X("Explain signed number representation: sign-magnitude, 1's and 2's complement.", "Signed number representation સમજાવો: sign-magnitude, 1's અને 2's complement.", 4),
    X("Explain BCD, Excess-3 and Gray codes with examples.", "BCD, Excess-3 અને Gray codes ઉદાહરણ સાથે સમજાવો.", 4),
]
