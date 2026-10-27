"""Digital Electronics Fundamentals (DI03000011) - Unit 2 extras. Every simplification is verified by truth table."""
import de_gates as G
from content_DI03000011_u1_extras import N, E, V, X

B = G.bh
n_ = lambda x: 1 - x


def simp(id_, expr, steps, answer, f, g, nv, q_gu_extra=""):
    """steps: list of (expression, law_en, law_gu). Verifies f == g."""
    assert G.equiv(f, g, nv), id_
    def body(lang):
        h = "<table><tr><th>Step</th><th>{}</th></tr>".format("Law used" if lang == "en" else "વપરાયેલ નિયમ")
        h += f"<tr><td>Y = {B(expr)}</td><td>{'Given' if lang == 'en' else 'આપેલ'}</td></tr>"
        for e, len_, lgu in steps:
            h += f"<tr><td>= {B(e)}</td><td>{len_ if lang == 'en' else lgu}</td></tr>"
        h += "</table>"
        h += f"<p><b>{'Answer' if lang == 'en' else 'જવાબ'}: Y = {B(answer)}</b></p>"
        h += ("<p><i>Verified: both expressions give the same truth table.</i></p>" if lang == "en"
              else "<p><i>ચકાસણી: બંને expressions નું truth table સરખું છે.</i></p>")
        return h
    return N(id_, f"Simplify: Y = {B(expr)}", f"Simplify કરો: Y = {B(expr)}", body("en"), body("gu"))


NUMERICALS = [
    simp("de2n1", "AB + A!B", [("A(B + !B)", "Distributive", "Distributive"), ("A·1", "Complement: B + !B = 1", "Complement: B + !B = 1"),
                              ("A", "Identity", "Identity")], "A",
         lambda a, b: (a & b) | (a & n_(b)), lambda a, b: a, 2),
    simp("de2n2", "A + AB + A!C", [("A(1 + B + !C)", "Distributive (common A)", "Distributive (common A)"),
                                  ("A·1", "Null: 1 + X = 1", "Null: 1 + X = 1"), ("A", "Identity", "Identity")], "A",
         lambda a, b, c: a | (a & b) | (a & n_(c)), lambda a, b, c: a, 3),
    simp("de2n3", "!AB + A!B + AB", [("!AB + A(!B + B)", "Distributive", "Distributive"), ("!AB + A", "Complement, identity", "Complement, identity"),
                                    ("A + !AB", "Commutative", "Commutative"), ("A + B", "Absorption: A + !AB = A + B", "Absorption: A + !AB = A + B")],
         "A + B", lambda a, b: (n_(a) & b) | (a & n_(b)) | (a & b), lambda a, b: a | b, 2),
    simp("de2n4", "(A + B)(A + C)", [("AA + AC + AB + BC", "Distributive (multiply out)", "Distributive (ગુણાકાર)"),
                                    ("A + AC + AB + BC", "Idempotent: AA = A", "Idempotent: AA = A"),
                                    ("A(1 + C + B) + BC", "Distributive (common A)", "Distributive (common A)"),
                                    ("A + BC", "Null, identity", "Null, identity")], "A + BC",
         lambda a, b, c: (a | b) & (a | c), lambda a, b, c: a | (b & c), 3),
    simp("de2n5", "AB + !AC + BC", [("AB + !AC + BC(A + !A)", "Complement: A + !A = 1", "Complement: A + !A = 1"),
                                   ("AB + !AC + ABC + !ABC", "Distributive", "Distributive"),
                                   ("AB(1 + C) + !AC(1 + B)", "Grouping", "Grouping"), ("AB + !AC", "Null, identity", "Null, identity")],
         "AB + !AC", lambda a, b, c: (a & b) | (n_(a) & c) | (b & c), lambda a, b, c: (a & b) | (n_(a) & c), 3),
    simp("de2n6", "!A!BC + !ABC + A!BC + ABC", [("!AC(!B + B) + AC(!B + B)", "Distributive", "Distributive"),
                                              ("!AC + AC", "Complement, identity", "Complement, identity"),
                                              ("C(!A + A)", "Distributive", "Distributive"), ("C", "Complement, identity", "Complement, identity")],
         "C", lambda a, b, c: (n_(a) & n_(b) & c) | (n_(a) & b & c) | (a & n_(b) & c) | (a & b & c), lambda a, b, c: c, 3),
    simp("de2n7", "!(AB + C)", [("!(AB)·!C", "De Morgan: !(X+Y) = !X·!Y", "De Morgan: !(X+Y) = !X·!Y"),
                               ("(!A + !B)·!C", "De Morgan: !(XY) = !X + !Y", "De Morgan: !(XY) = !X + !Y"),
                               ("!A!C + !B!C", "Distributive", "Distributive")], "!A!C + !B!C",
         lambda a, b, c: n_((a & b) | c), lambda a, b, c: (n_(a) & n_(c)) | (n_(b) & n_(c)), 3),
    simp("de2n8", "!(!(A+B) + !AB)", [("!(!(A+B))·!(!AB)", "De Morgan", "De Morgan"), ("(A + B)·(A + !B)", "Involution; De Morgan", "Involution; De Morgan"),
                                     ("A + B!B", "Distributive: (A+B)(A+C) = A + BC", "Distributive: (A+B)(A+C) = A + BC"),
                                     ("A + 0", "Complement: B!B = 0", "Complement: B!B = 0"), ("A", "Identity", "Identity")], "A",
         lambda a, b: n_(n_(a | b) | (n_(a) & b)), lambda a, b: a, 2),
]

# n9: majority function truth table + logic diagram description
_f9 = lambda a, b, c: (a & b) | (b & c) | (c & a)
_m9 = G.minterms(_f9, 3)
assert _m9 == [3, 5, 6, 7]
_tt9 = G.tt_html(["A", "B", "C", "AB", "BC", "CA", "Y"],
                 [(a, b, c, a & b, b & c, c & a, _f9(a, b, c)) for a in (0, 1) for b in (0, 1) for c in (0, 1)])
NUMERICALS.append(N("de2n9", "Prepare the truth table of Y = AB + BC + CA and draw its logic diagram. What does the circuit do?",
                    "Y = AB + BC + CA નું truth table બનાવો અને logic diagram દોરો. Circuit શું કાર્ય કરે છે?",
                    _tt9 + f"<p>Y = 1 for minterms {', '.join(map(str, _m9))} → Y = Σm(3, 5, 6, 7).</p>"
                    "<p><b>Logic diagram:</b> three 2-input AND gates (AB, BC, CA) whose outputs go to one 3-input OR gate.</p>"
                    "<p>The output is 1 when <b>two or more inputs are 1</b>; it is a <b>majority circuit</b> (also the carry output of a full adder).</p>",
                    _tt9 + f"<p>Y = 1 minterms {', '.join(map(str, _m9))} માટે → Y = Σm(3, 5, 6, 7).</p>"
                    "<p><b>Logic diagram:</b> ત્રણ 2-input AND gates (AB, BC, CA) જેના outputs એક 3-input OR gate માં જાય છે.</p>"
                    "<p><b>બે કે વધુ inputs 1</b> હોય ત્યારે output 1 થાય છે; આ <b>majority circuit</b> છે (full adder નું carry output પણ).</p>"))

# n10: prove XOR = (A+B)(!A+!B)
assert G.equiv(lambda a, b: a ^ b, lambda a, b: (a | b) & (n_(a) | n_(b)), 2)
_p10 = (f"<p>RHS = (A + B)({B('!A')} + {B('!B')})</p><p>= A{B('!A')} + A{B('!B')} + B{B('!A')} + B{B('!B')} &nbsp; [distributive]</p>"
        f"<p>= 0 + A{B('!B')} + {B('!A')}B + 0 &nbsp; [A{B('!A')} = 0]</p><p>= A{B('!B')} + {B('!A')}B = A⊕B = LHS ✓</p>")
NUMERICALS.append(N("de2n10", f"Prove that A⊕B = (A + B)({B('!A')} + {B('!B')}).", f"સાબિત કરો કે A⊕B = (A + B)({B('!A')} + {B('!B')}).",
                    _p10 + "<p>Also, (A + B)(" + B("!A") + " + " + B("!B") + ") = (A + B)·" + B("!(AB)") + " by De Morgan: output is 1 when at least one input is 1 but not both.</p>",
                    _p10 + "<p>વળી, De Morgan મુજબ (A + B)(" + B("!A") + " + " + B("!B") + ") = (A + B)·" + B("!(AB)") + ": ઓછામાં ઓછો એક input 1 હોય પણ બંને નહીં ત્યારે output 1.</p>"))

# n11: canonical SOP / POS of Y = A + !BC
_f11 = lambda a, b, c: a | (n_(b) & c)
_m11 = G.minterms(_f11, 3)
_M11 = [i for i in range(8) if i not in _m11]
assert (_m11, _M11) == ([1, 4, 5, 6, 7], [0, 2, 3])
_tt11 = G.tt_html(["A", "B", "C", "Y"], G.truth(_f11, 3))
_s11 = (f"<p>Expand each term with the missing variables:</p><p>A = A(B + {B('!B')})(C + {B('!C')}) = ABC + AB{B('!C')} + A{B('!B')}C + A{B('!B')}{B('!C')} → m7, m6, m5, m4</p>"
        f"<p>{B('!B')}C = {B('!B')}C(A + {B('!A')}) = A{B('!B')}C + {B('!A')}{B('!B')}C → m5, m1</p>")
NUMERICALS.append(N("de2n11", f"Express Y = A + {B('!B')}C in canonical SOP and canonical POS form.",
                    f"Y = A + {B('!B')}C ને canonical SOP અને canonical POS સ્વરૂપમાં દર્શાવો.",
                    _s11 + "<p>Truth table:</p>" + _tt11 + f"<p><b>Canonical SOP:</b> Y = Σm(1, 4, 5, 6, 7) = {B('!A!BC')} + {B('A!B!C')} + {B('A!BC')} + {B('AB!C')} + ABC</p>"
                    f"<p><b>Canonical POS:</b> Y = ΠM(0, 2, 3) = (A + B + C)(A + {B('!B')} + C)(A + {B('!B')} + {B('!C')})</p>",
                    _s11.replace("Expand each term with the missing variables:", "દરેક term ને ખૂટતા variables સાથે વિસ્તારો:") + "<p>Truth table:</p>" + _tt11
                    + f"<p><b>Canonical SOP:</b> Y = Σm(1, 4, 5, 6, 7) = {B('!A!BC')} + {B('A!B!C')} + {B('A!BC')} + {B('AB!C')} + ABC</p>"
                    f"<p><b>Canonical POS:</b> Y = ΠM(0, 2, 3) = (A + B + C)(A + {B('!B')} + C)(A + {B('!B')} + {B('!C')})</p>"))
# check the written POS
assert G.equiv(_f11, lambda a, b, c: (a | b | c) & (a | n_(b) | c) & (a | n_(b) | n_(c)), 3)

# n12: complement and dual
assert G.equiv(lambda a, b, c: n_((a & n_(b)) | (n_(a) & c)), lambda a, b, c: (n_(a) | b) & (a | n_(c)), 3)
_b12 = lambda L: (f"<p><b>(i) Y = A{B('!B')} + {B('!A')}C</b></p>"
                  f"<p>{'Complement' if L == 'en' else 'Complement'}: {B('!Y')} = ({B('!A')} + B)(A + {B('!C')}) &nbsp; ({'interchange + and ·, complement each variable' if L == 'en' else '+ અને · ની અદલાબદલી, દરેક variable નો complement'})</p>"
                  f"<p>Dual: (A + {B('!B')})({B('!A')} + C) &nbsp; ({'interchange + and · only' if L == 'en' else 'માત્ર + અને · ની અદલાબદલી'})</p>"
                  f"<p><b>(ii) Y = (A + B)·C + 0</b></p><p>Complement: {B('!Y')} = ({B('!A')}·{B('!B')} + {B('!C')})·1 = {B('!A!B')} + {B('!C')}</p>"
                  f"<p>Dual: (A·B + C)·1 = AB + C</p>")
assert G.equiv(lambda a, b, c: n_((a | b) & c), lambda a, b, c: (n_(a) & n_(b)) | n_(c), 3)
NUMERICALS.append(N("de2n12", f"Find the complement and dual of (i) Y = A{B('!B')} + {B('!A')}C (ii) Y = (A + B)·C + 0.",
                    f"(i) Y = A{B('!B')} + {B('!A')}C (ii) Y = (A + B)·C + 0 નો complement અને dual શોધો.", _b12("en"), _b12("gu")))

# n13: NAND-only implementation of AB + CD
assert G.equiv(lambda a, b, c, d: (a & b) | (c & d), lambda a, b, c, d: n_(n_(a & b) & n_(c & d)), 4)
_b13 = lambda L: (f"<p>Y = AB + CD = {B('!(!(AB + CD))')} &nbsp; [double complement]</p>"
                  f"<p>= {B('!(!(AB)·!(CD))')} &nbsp; [De Morgan]</p>"
                  + ("<p>So Y = NAND( NAND(A, B), NAND(C, D) ).</p><p><b>Circuit:</b> two NAND gates at level 1 (inputs A, B and C, D) and one NAND gate at level 2. "
                     "Total <b>3 NAND gates</b> (one 7400 IC).</p><p><b>Rule:</b> an AND-OR (SOP) circuit becomes NAND-NAND by simply replacing every gate with a NAND gate.</p>"
                     if L == "en" else
                     "<p>તેથી Y = NAND( NAND(A, B), NAND(C, D) ).</p><p><b>Circuit:</b> level 1 પર બે NAND gates (inputs A, B અને C, D) અને level 2 પર એક NAND gate. "
                     "કુલ <b>3 NAND gates</b> (એક 7400 IC).</p><p><b>નિયમ:</b> AND-OR (SOP) circuit માં દરેક gate ને NAND વડે બદલવાથી તે NAND-NAND બને છે.</p>"))
NUMERICALS.append(N("de2n13", "Implement Y = AB + CD using only NAND gates.", "માત્ર NAND gates વડે Y = AB + CD બનાવો.", _b13("en"), _b13("gu")))

# n14: prove distributive A + BC = (A+B)(A+C) by truth table
_r14 = [(a, b, c, b & c, a | (b & c), a | b, a | c, (a | b) & (a | c)) for a in (0, 1) for b in (0, 1) for c in (0, 1)]
assert all(r[4] == r[7] for r in _r14)
_t14 = G.tt_html(["A", "B", "C", "BC", "A+BC", "A+B", "A+C", "(A+B)(A+C)"], _r14)
NUMERICALS.append(N("de2n14", "Prove A + BC = (A + B)(A + C) using a truth table and algebraically.",
                    "Truth table વડે અને algebra વડે સાબિત કરો: A + BC = (A + B)(A + C).",
                    _t14 + "<p>Columns A+BC and (A+B)(A+C) are identical ✓</p><p><b>Algebra:</b> (A + B)(A + C) = A + AC + AB + BC = A(1 + C + B) + BC = A + BC ✓</p>",
                    _t14 + "<p>A+BC અને (A+B)(A+C) ના columns સરખા છે ✓</p><p><b>Algebra:</b> (A + B)(A + C) = A + AC + AB + BC = A(1 + C + B) + BC = A + BC ✓</p>"))

# n15: positive/negative logic
_v = "<table><tr><th>A</th><th>B</th><th>Y</th></tr><tr><td>0 V</td><td>0 V</td><td>0 V</td></tr><tr><td>0 V</td><td>5 V</td><td>5 V</td></tr><tr><td>5 V</td><td>0 V</td><td>5 V</td></tr><tr><td>5 V</td><td>5 V</td><td>5 V</td></tr></table>"
_pos = G.tt_html(["A", "B", "Y"], [(0, 0, 0), (0, 1, 1), (1, 0, 1), (1, 1, 1)])
_neg = G.tt_html(["A", "B", "Y"], [(1, 1, 1), (1, 0, 0), (0, 1, 0), (0, 0, 0)])
NUMERICALS.append(N("de2n15", "A gate gives the voltage table below. Identify the gate in positive logic and in negative logic.",
                    "એક gate નીચે મુજબ voltage table આપે છે. Positive logic અને negative logic માં gate ઓળખો.",
                    _v + "<p><b>Positive logic</b> (5 V = 1, 0 V = 0):</p>" + _pos + "<p>Output is 1 when any input is 1 → <b>OR gate</b>.</p>"
                    "<p><b>Negative logic</b> (0 V = 1, 5 V = 0):</p>" + _neg + "<p>Output is 1 only when both inputs are 1 → <b>AND gate</b>.</p>"
                    "<p>This confirms: positive-logic OR = negative-logic AND.</p>",
                    _v + "<p><b>Positive logic</b> (5 V = 1, 0 V = 0):</p>" + _pos + "<p>કોઈ પણ input 1 હોય ત્યારે output 1 → <b>OR gate</b>.</p>"
                    "<p><b>Negative logic</b> (0 V = 1, 5 V = 0):</p>" + _neg + "<p>બંને inputs 1 હોય ત્યારે જ output 1 → <b>AND gate</b>.</p>"
                    "<p>આથી સાબિત થાય છે: positive-logic OR = negative-logic AND.</p>"))

EQUATIONS = [
    {"title": {"en": "Logic Gates", "gu": "Logic Gates"}, "items": [
        E("AND", "AND", "Y = A·B", "1 only if all inputs are 1", "બધા inputs 1 હોય તો જ 1"),
        E("OR", "OR", "Y = A + B", "1 if any input is 1", "કોઈ પણ input 1 હોય તો 1"),
        E("NOT", "NOT", f"Y = {B('!A')}", "Inverts the input", "Input ને ઉલટાવે"),
        E("NAND", "NAND", f"Y = {B('!(A·B)')}", "0 only if all inputs are 1", "બધા inputs 1 હોય તો જ 0"),
        E("NOR", "NOR", f"Y = {B('!(A+B)')}", "1 only if all inputs are 0", "બધા inputs 0 હોય તો જ 1"),
        E("EX-OR", "EX-OR", f"Y = A⊕B = A{B('!B')} + {B('!A')}B", "1 when inputs differ", "Inputs જુદા હોય ત્યારે 1"),
        E("EX-NOR", "EX-NOR", f"Y = A⊙B = AB + {B('!A')}{B('!B')}", "1 when inputs are equal", "Inputs સરખા હોય ત્યારે 1"),
        E("Truth table rows", "Truth table rows", "Rows = 2<sup>n</sup>", "n = number of inputs", "n = inputs ની સંખ્યા"),
    ]},
    {"title": {"en": "Laws of Boolean Algebra", "gu": "Boolean Algebra ના નિયમો"}, "items": [
        E("Identity / Null", "Identity / Null", "A + 0 = A, A·1 = A, A + 1 = 1, A·0 = 0", "", ""),
        E("Idempotent / Complement", "Idempotent / Complement", f"A + A = A, A·A = A, A + {B('!A')} = 1, A·{B('!A')} = 0", "", ""),
        E("Commutative / Associative", "Commutative / Associative", "A + B = B + A, AB = BA, (A+B)+C = A+(B+C)", "", ""),
        E("Distributive", "Distributive", "A(B + C) = AB + AC; A + BC = (A + B)(A + C)", "", ""),
        E("Absorption", "Absorption", f"A + AB = A; A(A + B) = A; A + {B('!A')}B = A + B", "", ""),
        E("Consensus", "Consensus", f"AB + {B('!A')}C + BC = AB + {B('!A')}C", "", ""),
        E("De Morgan 1", "De Morgan 1", f"{B('!(AB)')} = {B('!A')} + {B('!B')}", "NAND = bubbled OR", "NAND = bubbled OR"),
        E("De Morgan 2", "De Morgan 2", f"{B('!(A+B)')} = {B('!A')}·{B('!B')}", "NOR = bubbled AND", "NOR = bubbled AND"),
    ]},
    {"title": {"en": "Functions and Forms", "gu": "Functions અને Forms"}, "items": [
        E("Canonical SOP", "Canonical SOP", "Y = Σm(rows where Y = 1)", "Minterm: 0 → complemented variable", "Minterm: 0 → complemented variable"),
        E("Canonical POS", "Canonical POS", "Y = ΠM(rows where Y = 0)", "Maxterm: 1 → complemented variable", "Maxterm: 1 → complemented variable"),
        E("Minterm–maxterm relation", "Minterm–maxterm સંબંધ", f"M<sub>i</sub> = {B('!m')}<sub>i</sub>", "", ""),
        E("Universal gate counts", "Universal gate counts", "NAND: NOT 1, AND 2, OR 3; NOR: NOT 1, OR 2, AND 3", "", ""),
    ]},
]

VIVA = [
    {"title": {"en": "Binary Logic and Gates", "gu": "Binary Logic અને Gates"}, "items": [
        V("What is a logic gate?", "Logic gate એટલે શું?", "An electronic circuit with one or more inputs and one output that performs a logic operation.", "એક કે વધુ inputs અને એક output વાળો electronic circuit જે logic operation કરે છે."),
        V("What is positive logic?", "Positive logic એટલે શું?", "Higher voltage = logic 1, lower voltage = logic 0.", "વધુ voltage = logic 1, ઓછું voltage = logic 0."),
        V("What is negative logic?", "Negative logic એટલે શું?", "Lower voltage = logic 1, higher voltage = logic 0.", "ઓછું voltage = logic 1, વધુ voltage = logic 0."),
        V("A positive-logic AND gate acts as which gate in negative logic?", "Positive-logic AND gate negative logic માં કયો gate બને?", "OR gate.", "OR gate."),
        V("Which are the basic gates?", "Basic gates કયા છે?", "AND, OR and NOT.", "AND, OR અને NOT."),
        V("Which are universal gates and why?", "Universal gates કયા છે અને કેમ?", "NAND and NOR, because any gate or circuit can be made using only them.", "NAND અને NOR, કારણ કે માત્ર તેમના વડે કોઈ પણ gate કે circuit બનાવી શકાય."),
        V("When is the output of an AND gate 1?", "AND gate નું output ક્યારે 1 થાય?", "Only when all inputs are 1.", "બધા inputs 1 હોય ત્યારે જ."),
        V("When is the output of a NOR gate 1?", "NOR gate નું output ક્યારે 1 થાય?", "Only when all inputs are 0.", "બધા inputs 0 હોય ત્યારે જ."),
        V("Why is EX-NOR called an equality detector?", "EX-NOR ને equality detector કેમ કહે છે?", "Its output is 1 only when both inputs are equal.", "બંને inputs સરખા હોય ત્યારે જ તેનું output 1 થાય છે."),
        V("Give two applications of EX-OR gate.", "EX-OR gate ના બે ઉપયોગ આપો.", "Half/full adder sum, parity generator/checker, comparator.", "Half/full adder sum, parity generator/checker, comparator."),
        V("How is a NOT gate made from a NAND gate?", "NAND gate માંથી NOT gate કેવી રીતે બને?", "By connecting both inputs together.", "બંને inputs ને જોડીને."),
        V("How many NAND gates make an OR gate?", "OR gate બનાવવા કેટલા NAND gates જોઈએ?", "Three.", "ત્રણ."),
        V("Name the ICs for AND, OR, NOT and NAND gates.", "AND, OR, NOT અને NAND gates ના ICs ના નામ આપો.", "7408, 7432, 7404 and 7400.", "7408, 7432, 7404 અને 7400."),
        V("What are VCC and GND pins of a 14-pin TTL IC?", "14-pin TTL IC ના VCC અને GND pins કયા છે?", "Pin 14 = VCC (+5 V), pin 7 = GND.", "Pin 14 = VCC (+5 V), pin 7 = GND."),
        V("How many rows are in the truth table of a 3-input gate?", "3-input gate ના truth table માં કેટલી rows હોય?", "2³ = 8.", "2³ = 8."),
    ]},
    {"title": {"en": "Boolean Algebra", "gu": "Boolean Algebra"}, "items": [
        V("Who introduced Boolean algebra?", "Boolean algebra કોણે રજૂ કર્યું?", "George Boole (1854).", "George Boole (1854)."),
        V("What is the principle of duality?", "Principle of duality શું છે?", "An identity remains true if + and · are interchanged and 0 and 1 are interchanged.", "+ અને · તથા 0 અને 1 ની અદલાબદલી કરવા છતાં identity સાચી રહે છે."),
        V("State De Morgan's theorems.", "De Morgan's theorems લખો.", "(AB)' = A' + B' and (A + B)' = A'B'.", "(AB)' = A' + B' અને (A + B)' = A'B'."),
        V("What is A + 1 and A·0?", "A + 1 અને A·0 કેટલા?", "A + 1 = 1 and A·0 = 0.", "A + 1 = 1 અને A·0 = 0."),
        V("Simplify A + AB.", "A + AB simplify કરો.", "A (absorption law).", "A (absorption law)."),
        V("Simplify A + A'B.", "A + A'B simplify કરો.", "A + B.", "A + B."),
        V("What is a minterm?", "Minterm શું છે?", "A product term containing all variables, true or complemented.", "બધા variables (true અથવા complemented) ધરાવતો product term."),
        V("What is a maxterm?", "Maxterm શું છે?", "A sum term containing all variables, true or complemented.", "બધા variables (true અથવા complemented) ધરાવતો sum term."),
        V("What is SOP? Which circuit implements it?", "SOP શું છે? કયો circuit તેને બનાવે?", "Sum of products; an AND-OR (or NAND-NAND) circuit.", "Sum of products; AND-OR (અથવા NAND-NAND) circuit."),
        V("What is the difference between complement and dual?", "Complement અને dual વચ્ચે શું તફાવત છે?", "Both interchange + and ·, 0 and 1; only the complement also complements the variables.", "બંને + અને ·, 0 અને 1 ની અદલાબદલી કરે છે; માત્ર complement માં variables નો complement પણ લેવાય."),
        V("Why do we simplify Boolean expressions?", "Boolean expressions નું simplification કેમ કરીએ છીએ?", "To reduce the number of gates, cost, size, delay and power.", "Gates ની સંખ્યા, cost, size, delay અને power ઘટાડવા."),
        V("What is a literal?", "Literal શું છે?", "A variable or its complement in an expression.", "Expression માં variable અથવા તેનો complement."),
    ]},
]

EXAM_QS = [
    X("Explain positive and negative logic with an example.", "ઉદાહરણ સાથે positive અને negative logic સમજાવો.", 3),
    X("Draw the symbol, write the Boolean expression and truth table of AND, OR and NOT gates.", "AND, OR અને NOT gates નો symbol દોરો, Boolean expression અને truth table લખો.", 4),
    X("Explain NAND and NOR gates with symbol and truth table.", "Symbol અને truth table સાથે NAND અને NOR gates સમજાવો.", 3),
    X("Explain EX-OR gate. Implement it using basic gates.", "EX-OR gate સમજાવો. Basic gates વડે તેને બનાવો.", 4),
    X("Why are NAND and NOR called universal gates? Realise AND, OR and NOT using NAND gates only.", "NAND અને NOR ને universal gates કેમ કહે છે? માત્ર NAND gates વડે AND, OR અને NOT બનાવો.", 7),
    X("Realise AND, OR and NOT gates using NOR gates only.", "માત્ર NOR gates વડે AND, OR અને NOT gates બનાવો.", 4),
    X("State and prove De Morgan's theorems.", "De Morgan's theorems લખો અને સાબિત કરો.", 4),
    X("List the laws of Boolean algebra.", "Boolean algebra ના નિયમો લખો.", 3),
    X("State the principle of duality with examples.", "ઉદાહરણ સાથે principle of duality લખો.", 3),
    X("Simplify: (i) AB + AB' (ii) A'B + AB' + AB (iii) (A + B)(A + C).", "Simplify કરો: (i) AB + AB' (ii) A'B + AB' + AB (iii) (A + B)(A + C).", 3),
    X("Simplify Y = A'B'C + A'BC + AB'C + ABC and draw the logic diagram.", "Y = A'B'C + A'BC + AB'C + ABC simplify કરી logic diagram દોરો.", 4),
    X("Prove that AB + A'C + BC = AB + A'C.", "સાબિત કરો કે AB + A'C + BC = AB + A'C.", 3),
    X("Explain SOP and POS forms with minterms and maxterms.", "Minterms અને maxterms સાથે SOP અને POS forms સમજાવો.", 4),
    X("Express Y = A + B'C in canonical SOP and POS form.", "Y = A + B'C ને canonical SOP અને POS સ્વરૂપમાં દર્શાવો.", 4),
    X("Draw the logic diagram of Y = AB + A'C and prepare its truth table.", "Y = AB + A'C નો logic diagram દોરો અને truth table બનાવો.", 3),
    X("Implement Y = AB + CD using NAND gates only.", "માત્ર NAND gates વડે Y = AB + CD બનાવો.", 3),
    X("Write the pin diagram of IC 7400 and explain how to verify the truth table of a gate.", "IC 7400 નો pin diagram દોરો અને gate ના truth table ની ચકાસણી કેવી રીતે થાય તે સમજાવો.", 4),
]
