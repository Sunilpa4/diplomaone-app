"""Digital Electronics Fundamentals (DI03000011) - Unit 3 extras: numericals solved by de_kmap, equations, viva, exam."""
import de_kmap as K
import de_gates as G
from content_DI03000011_u1_extras import N, E, V, X
from content_DI03000011_u3_common import solve, B


def KQ(id_, n, ones, dc=(), pos=False, pre_en="", pre_gu="", post_en="", post_gu="", q_en=None, q_gu=None, expect=None):
    en, gu, g, ans = solve(n, ones, dc, pos)
    if expect:
        assert set(ans.split(" + ")) == set(expect.split(" + ")), (id_, ans)
    fx = "Σm(" + ", ".join(map(str, sorted(ones))) + ")" + (" + d(" + ", ".join(map(str, sorted(dc))) + ")" if dc else "")
    form = "POS" if pos else "SOP"
    qe = q_en or f"Simplify Y = {fx} using a K-map ({form} form)."
    qg = q_gu or f"K-map વડે Y = {fx} simplify કરો ({form} સ્વરૂપ)."
    return N(id_, qe, qg, pre_en + en + post_en, pre_gu + gu + post_gu), g


NUMERICALS = []
NUMERICALS.append(KQ("de3n1", 2, [0, 1, 3], expect="!A + B")[0])
NUMERICALS.append(KQ("de3n2", 3, [0, 2, 4, 6], expect="!C")[0])
NUMERICALS.append(KQ("de3n3", 3, [1, 2, 3, 5, 7], expect="C + !AB")[0])
NUMERICALS.append(KQ("de3n4", 3, [0, 2, 3, 4, 5, 7])[0])
NUMERICALS.append(KQ("de3n5", 4, [0, 2, 5, 7, 8, 10, 13, 15], expect="!B!D + BD",
                     post_en="<p>This is the EX-NOR of B and D: Y = B⊙D.</p>", post_gu="<p>આ B અને D નો EX-NOR છે: Y = B⊙D.</p>")[0])
NUMERICALS.append(KQ("de3n6", 4, [1, 3, 4, 5, 6, 7, 9, 11, 13, 15], expect="D + !AB")[0])
NUMERICALS.append(KQ("de3n7", 4, [0, 1, 2, 3, 5, 7, 8, 9, 10, 11, 13, 15])[0])

# n8: from an expression
_f8 = lambda a, b, c, d: ((1 - a) & (1 - b) & (1 - c)) | ((1 - b) & c & (1 - d)) | ((1 - a) & b & c & (1 - d)) | (a & (1 - b) & (1 - c))
_m8 = G.minterms(_f8, 4)
_pre8_en = (f"<p><b>Convert to minterms:</b> {B('!A!B!C')} → m0, m1; {B('!BC!D')} → m2, m10; {B('!ABC!D')} → m6; {B('A!B!C')} → m8, m9.</p>"
            f"<p>So Y = Σm({', '.join(map(str, _m8))}).</p>")
_pre8_gu = _pre8_en.replace("Convert to minterms:", "Minterms માં ફેરવો:").replace("So Y", "તેથી Y")
assert _m8 == [0, 1, 2, 6, 8, 9, 10]
NUMERICALS.append(KQ("de3n8", 4, _m8, pre_en=_pre8_en, pre_gu=_pre8_gu, expect="!B!C + !B!D + !AC!D",
                     q_en=f"Simplify Y = {B('!A!B!C')} + {B('!BC!D')} + {B('!ABC!D')} + {B('A!B!C')} using a K-map.",
                     q_gu=f"K-map વડે Y = {B('!A!B!C')} + {B('!BC!D')} + {B('!ABC!D')} + {B('A!B!C')} simplify કરો.")[0])
NUMERICALS.append(KQ("de3n9", 4, [0, 1, 2, 5, 8, 9], [10, 11, 14, 15])[0])
NUMERICALS.append(KQ("de3n10", 4, [1, 2, 5, 6, 9], [10, 11, 12, 13, 14, 15])[0])
NUMERICALS.append(KQ("de3n11", 4, [0, 1, 4, 5, 6, 8, 9, 12, 13, 14], pos=True)[0])

# n12: design from a word problem (majority)
_tt12 = G.tt_html(["A", "B", "C", "Y"], G.truth(lambda a, b, c: int(a + b + c >= 2), 3))
NUMERICALS.append(KQ("de3n12", 3, [3, 5, 6, 7], expect="BC + AC + AB",
                     q_en="Design a 3-input majority circuit (output 1 when two or more inputs are 1) using a K-map.",
                     q_gu="K-map વડે 3-input majority circuit (બે કે વધુ inputs 1 હોય ત્યારે output 1) design કરો.",
                     pre_en="<p><b>Truth table:</b></p>" + _tt12, pre_gu="<p><b>Truth table:</b></p>" + _tt12,
                     post_en="<p><b>Circuit:</b> three 2-input AND gates (AB, BC, AC) and one 3-input OR gate. Used as the carry of a full adder.</p>",
                     post_gu="<p><b>Circuit:</b> ત્રણ 2-input AND gates (AB, BC, AC) અને એક 3-input OR gate. Full adder ના carry તરીકે વપરાય છે.</p>")[0])

# n13: simplify and implement with basic gates
_n13, _g13 = KQ("de3n13", 4, [2, 3, 6, 7, 8, 10, 12, 14])
_lits = [K.literals(c) for c in _g13]
_nots = sorted({i for c in _g13 for i in range(4) if c[i] == "0"})
_and = [c for c in _g13 if K.literals(c) > 1]
_imp_en = (f"<p><b>Implementation:</b> {len(_nots)} NOT gate(s) for " + ", ".join(B('!' + 'ABCD'[i]) for i in _nots)
           + f"; {len(_and)} two-input AND gates; 1 {len(_g13)}-input OR gate. Total {len(_nots) + len(_and) + 1} gates.</p>")
_imp_gu = (f"<p><b>Implementation:</b> " + ", ".join(B('!' + 'ABCD'[i]) for i in _nots) + f" માટે {len(_nots)} NOT gate(s); "
           f"{len(_and)} two-input AND gates; 1 {len(_g13)}-input OR gate. કુલ {len(_nots) + len(_and) + 1} gates.</p>")
_n13["q"] = {"en": "Simplify Y = Σm(2, 3, 6, 7, 8, 10, 12, 14) and implement it using basic gates.",
             "gu": "Y = Σm(2, 3, 6, 7, 8, 10, 12, 14) simplify કરી basic gates વડે બનાવો."}
_n13["a"]["en"] += _imp_en
_n13["a"]["gu"] += _imp_gu
NUMERICALS.append(_n13)

# n14: NAND-only implementation of a K-map result
_n14, _g14 = KQ("de3n14", 4, [1, 3, 7, 11, 15], [0, 2, 5], expect="!A!B + CD")
assert G.equiv(lambda a, b, c, d: ((1 - a) & (1 - b)) | (c & d), lambda a, b, c, d: 1 - ((1 - ((1 - a) & (1 - b))) & (1 - (c & d))), 4)
_n14["q"] = {"en": "Simplify Y = Σm(1, 3, 7, 11, 15) + d(0, 2, 5) and implement it using NAND gates only.",
             "gu": "Y = Σm(1, 3, 7, 11, 15) + d(0, 2, 5) simplify કરી માત્ર NAND gates વડે બનાવો."}
_n14["a"]["en"] += (f"<p><b>NAND-NAND form:</b> Y = {B('!A!B')} + CD = {B('!(!(!A!B)·!(CD))')}</p>"
                    "<p>Gates: 2 NAND-inverters (for " + B("!A") + ", " + B("!B") + "), 2 NAND gates at level 1, 1 NAND gate at level 2 = <b>5 NAND gates</b> (two 7400 ICs).</p>")
_n14["a"]["gu"] += (f"<p><b>NAND-NAND સ્વરૂપ:</b> Y = {B('!A!B')} + CD = {B('!(!(!A!B)·!(CD))')}</p>"
                    "<p>Gates: 2 NAND-inverters (" + B("!A") + ", " + B("!B") + " માટે), level 1 પર 2 NAND, level 2 પર 1 NAND = <b>5 NAND gates</b> (બે 7400 ICs).</p>")
NUMERICALS.append(_n14)

EQUATIONS = [
    {"title": {"en": "K-map Size and Groups", "gu": "K-map Size અને Groups"}, "items": [
        E("Number of cells", "Cells ની સંખ્યા", "Cells = 2<sup>n</sup>", "n = number of variables (2 → 4, 3 → 8, 4 → 16)", "n = variables ની સંખ્યા (2 → 4, 3 → 8, 4 → 16)"),
        E("Group size", "Group size", "Group = 2<sup>k</sup> cells (1, 2, 4, 8, 16)", "k variables are eliminated", "k variables દૂર થાય"),
        E("Literals in a term", "Term માં literals", "Literals = n − k", "4-var: pair 3, quad 2, octet 1", "4-var: pair 3, quad 2, octet 1"),
        E("Gray code order", "Gray code ક્રમ", "00, 01, 11, 10", "Adjacent cells differ in one bit", "Adjacent cells માં એક જ bit બદલાય"),
        E("3-variable cell order", "3-variable cell ક્રમ", "0 1 3 2 / 4 5 7 6", "Rows A = 0, 1; columns BC", "Rows A = 0, 1; columns BC"),
        E("4-variable cell order", "4-variable cell ક્રમ", "0 1 3 2 / 4 5 7 6 / 12 13 15 14 / 8 9 11 10", "Rows AB, columns CD", "Rows AB, columns CD"),
    ]},
    {"title": {"en": "Writing Terms", "gu": "Terms લખવા"}, "items": [
        E("SOP (group 1s)", "SOP (1s નો group)", "Variable = 1 → A; = 0 → " + B("!A") + "; changes → dropped", "Terms are ORed", "Terms નો OR"),
        E("POS (group 0s)", "POS (0s નો group)", "Variable = 0 → A; = 1 → " + B("!A") + "; changes → dropped", "Sum terms are ANDed", "Sum terms નો AND"),
        E("Don't care", "Don't care", "X = 1 or 0, whichever gives larger groups", "Never group only Xs", "માત્ર Xs નો group નહીં"),
        E("Basis of grouping", "Grouping નો આધાર", "AB + A" + B("!B") + " = A(B + " + B("!B") + ") = A", "", ""),
    ]},
]

VIVA = [
    {"title": {"en": "K-map Basics", "gu": "K-map Basics"}, "items": [
        V("Why do we simplify Boolean functions?", "Boolean functions નું simplification કેમ કરીએ?", "To reduce gates, cost, size, delay and power.", "Gates, cost, size, delay અને power ઘટાડવા."),
        V("What is a K-map?", "K-map શું છે?", "A graphical method of simplifying Boolean functions using a map of 2ⁿ cells.", "2ⁿ cells ના map વડે Boolean functions simplify કરવાની graphical method."),
        V("Who introduced the K-map?", "K-map કોણે રજૂ કર્યો?", "Maurice Karnaugh in 1953.", "Maurice Karnaugh એ 1953 માં."),
        V("How many cells are in a 4-variable K-map?", "4-variable K-map માં કેટલા cells હોય?", "16.", "16."),
        V("Why is Gray code used in a K-map?", "K-map માં Gray code કેમ વપરાય છે?", "So that adjacent cells differ in only one variable.", "જેથી adjacent cells માં માત્ર એક variable બદલાય."),
        V("Which cells are adjacent in a 4-variable K-map besides neighbours?", "4-variable K-map માં પાડોશી સિવાય કયા cells adjacent છે?", "Cells on opposite edges and the four corners.", "સામસામેની ધારના cells અને ચાર ખૂણા."),
        V("What group sizes are allowed?", "કયા group sizes માન્ય છે?", "Powers of 2: 1, 2, 4, 8, 16.", "2 ની ઘાત: 1, 2, 4, 8, 16."),
        V("Can a cell be used in more than one group?", "એક cell એકથી વધુ groups માં વાપરી શકાય?", "Yes, overlapping is allowed.", "હા, overlapping ચાલે છે."),
        V("Can diagonal cells be grouped?", "ત્રાંસા cells નો group બનાવી શકાય?", "No.", "ના."),
        V("How many variables does a quad eliminate?", "Quad કેટલા variables દૂર કરે?", "Two.", "બે."),
        V("What is an octet?", "Octet શું છે?", "A group of 8 adjacent 1s; it eliminates 3 variables.", "8 adjacent 1s નો group; તે 3 variables દૂર કરે છે."),
    ]},
    {"title": {"en": "Implicants, Don't-Cares and Implementation", "gu": "Implicants, Don't-Cares અને Implementation"}, "items": [
        V("What is a prime implicant?", "Prime implicant શું છે?", "A group of 1s that cannot be enlarged further.", "1s નો એવો group જેને વધુ મોટો ન કરી શકાય."),
        V("What is an essential prime implicant?", "Essential prime implicant શું છે?", "A prime implicant that covers a 1 not covered by any other prime implicant.", "એવો prime implicant જે બીજા કોઈ PI ન આવરે તેવો 1 આવરે."),
        V("What is a redundant group?", "Redundant group શું છે?", "A group whose 1s are all covered by other groups; it must be removed.", "જેના બધા 1s બીજા groups વડે આવરાઈ ગયા હોય તેવો group; તેને દૂર કરવો."),
        V("What is a don't-care condition?", "Don't-care condition શું છે?", "An input combination that never occurs or whose output does not matter.", "એવું input combination જે ક્યારેય ન આવે અથવા જેનું output મહત્વનું ન હોય."),
        V("How is a don't-care shown?", "Don't-care કેવી રીતે દર્શાવાય?", "By X (or d, φ) in the map; d(…) in the expression.", "Map માં X (અથવા d, φ) વડે; expression માં d(…)."),
        V("Is it necessary to cover every X?", "દરેક X ને આવરવો જરૂરી છે?", "No. Use an X only if it makes a group larger.", "ના. Group મોટો થાય ત્યારે જ X વાપરો."),
        V("Which inputs are don't-cares for a BCD circuit?", "BCD circuit માટે કયા inputs don't-cares છે?", "1010 to 1111 (10 to 15).", "1010 થી 1111 (10 થી 15)."),
        V("How do you get a POS expression from a K-map?", "K-map પરથી POS expression કેવી રીતે મળે?", "Group the 0s and write complemented sum terms, then AND them.", "0s ના groups બનાવી sum terms લખો અને તેમનો AND કરો."),
        V("Which circuit implements an SOP expression?", "SOP expression કયા circuit થી બને?", "AND-OR (two-level), or NAND-NAND.", "AND-OR (two-level), અથવા NAND-NAND."),
        V("What is the main limitation of a K-map?", "K-map ની મુખ્ય મર્યાદા શું છે?", "It becomes difficult for more than 4 variables.", "4 થી વધુ variables માટે અઘરો બને છે."),
        V("Which method is used for many variables?", "ઘણા variables માટે કઈ method વપરાય?", "Quine–McCluskey (tabular) method.", "Quine–McCluskey (tabular) method."),
    ]},
]

EXAM_QS = [
    X("Explain the need for simplification of Boolean functions.", "Boolean functions ના simplification ની જરૂરિયાત સમજાવો.", 3),
    X("Draw 2, 3 and 4-variable K-maps showing minterm numbers.", "Minterm numbers સાથે 2, 3 અને 4-variable K-maps દોરો.", 3),
    X("State the rules for grouping 1s in a K-map.", "K-map માં 1s ના grouping ના નિયમો લખો.", 3),
    X("Define: prime implicant, essential prime implicant, don't-care condition.", "વ્યાખ્યા આપો: prime implicant, essential prime implicant, don't-care condition.", 3),
    X("Simplify Y = Σm(1, 3, 5, 6, 7) using a K-map.", "K-map વડે Y = Σm(1, 3, 5, 6, 7) simplify કરો.", 3),
    X("Simplify Y = Σm(0, 2, 3, 4, 5, 7) using a K-map.", "K-map વડે Y = Σm(0, 2, 3, 4, 5, 7) simplify કરો.", 3),
    X("Simplify Y = Σm(0, 1, 2, 4, 5, 6, 8, 9, 12, 13, 14) and draw the logic diagram.", "Y = Σm(0, 1, 2, 4, 5, 6, 8, 9, 12, 13, 14) simplify કરી logic diagram દોરો.", 4),
    X("Simplify Y = Σm(0, 2, 5, 7, 8, 10, 13, 15) using a K-map.", "K-map વડે Y = Σm(0, 2, 5, 7, 8, 10, 13, 15) simplify કરો.", 4),
    X("Explain don't-care conditions. Simplify Y = Σm(1, 3, 7, 11, 15) + d(0, 2, 5).", "Don't-care conditions સમજાવો. Y = Σm(1, 3, 7, 11, 15) + d(0, 2, 5) simplify કરો.", 4),
    X("Simplify Y = Σm(0, 1, 2, 5, 8, 9, 10) in SOP and POS forms.", "Y = Σm(0, 1, 2, 5, 8, 9, 10) ને SOP અને POS સ્વરૂપમાં simplify કરો.", 7),
    X("Simplify Y = A'B'C' + B'CD' + A'BCD' + AB'C' using a K-map and implement it with basic gates.", "K-map વડે Y = A'B'C' + B'CD' + A'BCD' + AB'C' simplify કરી basic gates વડે બનાવો.", 7),
    X("Design a circuit that gives output 1 when a BCD input is 5 or more.", "BCD input 5 કે વધુ હોય ત્યારે output 1 આપતો circuit design કરો.", 4),
    X("Design a 3-input majority circuit using a K-map.", "K-map વડે 3-input majority circuit design કરો.", 4),
    X("Simplify Y = Σm(1, 3, 7, 11, 15) + d(0, 2, 5) and implement using NAND gates only.", "Y = Σm(1, 3, 7, 11, 15) + d(0, 2, 5) simplify કરી માત્ર NAND gates વડે બનાવો.", 4),
    X("Give advantages and limitations of the K-map method.", "K-map method ના ફાયદા અને મર્યાદાઓ આપો.", 3),
]
