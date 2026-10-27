"""Digital Electronics Fundamentals (DI03000011) - Unit 2 notes, part B: 2.3 Boolean algebra, 2.4 De Morgan's theorems and Boolean functions.
Every law is verified by truth table (de_gates.equiv) before it is written."""
from content_DI03000011_u1_notes_a import T
import de_gates as G

B = G.bh
n_ = lambda x: 1 - x

# (law name EN, law name GU, html of law, [(f, g, nvars), ...] for verification)
LAWS = [
    ("Commutative", "Commutative (ક્રમ)", "A + B = B + A<br>A·B = B·A",
     [(lambda a, b: a | b, lambda a, b: b | a, 2), (lambda a, b: a & b, lambda a, b: b & a, 2)]),
    ("Associative", "Associative (જૂથ)", "(A + B) + C = A + (B + C)<br>(AB)C = A(BC)",
     [(lambda a, b, c: (a | b) | c, lambda a, b, c: a | (b | c), 3), (lambda a, b, c: (a & b) & c, lambda a, b, c: a & (b & c), 3)]),
    ("Distributive", "Distributive (વિભાજન)", "A(B + C) = AB + AC<br>A + BC = (A + B)(A + C)",
     [(lambda a, b, c: a & (b | c), lambda a, b, c: (a & b) | (a & c), 3), (lambda a, b, c: a | (b & c), lambda a, b, c: (a | b) & (a | c), 3)]),
    ("Identity", "Identity", "A + 0 = A<br>A · 1 = A", [(lambda a: a | 0, lambda a: a, 1), (lambda a: a & 1, lambda a: a, 1)]),
    ("Null (dominance)", "Null (dominance)", "A + 1 = 1<br>A · 0 = 0", [(lambda a: a | 1, lambda a: 1, 1), (lambda a: a & 0, lambda a: 0, 1)]),
    ("Idempotent", "Idempotent", "A + A = A<br>A · A = A", [(lambda a: a | a, lambda a: a, 1), (lambda a: a & a, lambda a: a, 1)]),
    ("Complement", "Complement", f"A + {B('!A')} = 1<br>A · {B('!A')} = 0", [(lambda a: a | n_(a), lambda a: 1, 1), (lambda a: a & n_(a), lambda a: 0, 1)]),
    ("Involution (double complement)", "Involution (double complement)", f"({B('!A')})' = A", [(lambda a: n_(n_(a)), lambda a: a, 1)]),
    ("Absorption", "Absorption", f"A + AB = A<br>A(A + B) = A<br>A + {B('!A')}B = A + B",
     [(lambda a, b: a | (a & b), lambda a, b: a, 2), (lambda a, b: a & (a | b), lambda a, b: a, 2), (lambda a, b: a | (n_(a) & b), lambda a, b: a | b, 2)]),
    ("Consensus", "Consensus", f"AB + {B('!A')}C + BC = AB + {B('!A')}C",
     [(lambda a, b, c: (a & b) | (n_(a) & c) | (b & c), lambda a, b, c: (a & b) | (n_(a) & c), 3)]),
    ("De Morgan", "De Morgan", f"{B('!(A+B)')} = {B('!A')}·{B('!B')}<br>{B('!(AB)')} = {B('!A')} + {B('!B')}",
     [(lambda a, b: n_(a | b), lambda a, b: n_(a) & n_(b), 2), (lambda a, b: n_(a & b), lambda a, b: n_(a) | n_(b), 2)]),
]
for _l in LAWS:
    for f, g, n in _l[3]:
        assert G.equiv(f, g, n), _l[0]


def laws_table(lang):
    h = "<table><tr><th>{}</th><th>{}</th></tr>".format(*(("Law", "Statement") if lang == "en" else ("નિયમ", "વિધાન")))
    for en, gu, html, _ in LAWS:
        h += f"<tr><td>{en if lang == 'en' else gu}</td><td>{html}</td></tr>"
    return h + "</table>"


# 3-variable minterm / maxterm table
def mm_table():
    rows = ""
    for i in range(8):
        a, b, c = (i >> 2) & 1, (i >> 1) & 1, i & 1
        mt = "".join(v if bit else "!" + v for v, bit in zip("ABC", (a, b, c)))
        Mt = "(" + " + ".join(v if not bit else "!" + v for v, bit in zip("ABC", (a, b, c))) + ")"
        rows += f"<tr><td>{a}{b}{c}</td><td>{B(mt)}</td><td>m<sub>{i}</sub></td><td>{B(Mt)}</td><td>M<sub>{i}</sub></td></tr>"
    return "<table><tr><th>ABC</th><th>Minterm</th><th></th><th>Maxterm</th><th></th></tr>" + rows + "</table>"


MM = mm_table()

# truth-table proof for De Morgan 2
_dm2 = [(a, b, a | b, n_(a | b), n_(a), n_(b), n_(a) & n_(b)) for a in (0, 1) for b in (0, 1)]
assert all(r[3] == r[6] for r in _dm2)
DM2 = G.tt_html(["A", "B", "A+B", B("!(A+B)"), B("!A"), B("!B"), B("!A·!B")], _dm2, out_cols=1)

SEC_2_3 = {
    "title": {"en": "2.3 Boolean Algebra", "gu": "2.3 Boolean Algebra"},
    "items": [
        T("2.3.1 Boolean Algebra, Postulates and Duality", "2.3.1 Boolean Algebra, Postulates અને Duality",
          f"""<p><b>Boolean algebra</b> is the algebra of binary variables and logic operations, introduced by <b>George Boole</b> (1854). Claude Shannon applied it to switching circuits. It is used to <b>analyse and simplify</b> logic circuits.</p>
<h4>Postulates (basic rules)</h4>
<table><tr><th>AND</th><th>OR</th><th>NOT</th></tr>
<tr><td>0 · 0 = 0</td><td>0 + 0 = 0</td><td>{B('!0')} = 1</td></tr>
<tr><td>0 · 1 = 0</td><td>0 + 1 = 1</td><td>{B('!1')} = 0</td></tr>
<tr><td>1 · 0 = 0</td><td>1 + 0 = 1</td><td></td></tr>
<tr><td>1 · 1 = 1</td><td>1 + 1 = 1</td><td></td></tr></table>
<p>Huntington's postulates: (1) closure under + and ·; (2) identity elements 0 for + and 1 for ·; (3) commutative laws; (4) distributive laws; (5) for every A there is a complement {B('!A')} with A + {B('!A')} = 1 and A·{B('!A')} = 0; (6) at least two distinct elements (0 and 1).</p>
<h4>Principle of duality</h4>
<p>Every Boolean identity remains true if we <b>interchange + and ·</b> and <b>interchange 0 and 1</b> (variables and complements are not changed). The new expression is called the <b>dual</b>.</p>
<p><i>Example:</i> A + 0 = A → dual: A · 1 = A. &nbsp; A(B + C) = AB + AC → dual: A + BC = (A + B)(A + C).</p>
<p>So each law of Boolean algebra comes in a pair; proving one proves the other.</p>""",
          f"""<p><b>Boolean algebra</b> એ binary variables અને logic operations નું algebra છે, જે <b>George Boole</b> (1854) એ રજૂ કર્યું. Claude Shannon એ તેને switching circuits માં વાપર્યું. તેનો ઉપયોગ logic circuits નું <b>analysis અને simplification</b> કરવા થાય છે.</p>
<h4>Postulates (મૂળભૂત નિયમો)</h4>
<table><tr><th>AND</th><th>OR</th><th>NOT</th></tr>
<tr><td>0 · 0 = 0</td><td>0 + 0 = 0</td><td>{B('!0')} = 1</td></tr>
<tr><td>0 · 1 = 0</td><td>0 + 1 = 1</td><td>{B('!1')} = 0</td></tr>
<tr><td>1 · 0 = 0</td><td>1 + 0 = 1</td><td></td></tr>
<tr><td>1 · 1 = 1</td><td>1 + 1 = 1</td><td></td></tr></table>
<p>Huntington's postulates: (1) + અને · હેઠળ closure; (2) identity elements: + માટે 0 અને · માટે 1; (3) commutative laws; (4) distributive laws; (5) દરેક A માટે complement {B('!A')} હોય જેથી A + {B('!A')} = 1 અને A·{B('!A')} = 0; (6) ઓછામાં ઓછા બે જુદા elements (0 અને 1).</p>
<h4>Principle of duality</h4>
<p>કોઈ પણ Boolean identity માં <b>+ અને · ની અદલાબદલી</b> તથા <b>0 અને 1 ની અદલાબદલી</b> કરવાથી પણ તે સાચી રહે છે (variables અને complements બદલાતા નથી). નવા expression ને <b>dual</b> કહે છે.</p>
<p><i>ઉદાહરણ:</i> A + 0 = A → dual: A · 1 = A. &nbsp; A(B + C) = AB + AC → dual: A + BC = (A + B)(A + C).</p>
<p>તેથી Boolean algebra નો દરેક નિયમ જોડીમાં હોય છે; એક સાબિત કરવાથી બીજો પણ સાબિત થાય છે.</p>""",
          key=True),

        T("2.3.2 Laws of Boolean Algebra", "2.3.2 Boolean Algebra ના નિયમો",
          "<p>The following laws are used to simplify Boolean expressions. Each can be proved by a truth table (perfect induction).</p>" + laws_table("en")
          + f"<p><b>Proof of A + {B('!A')}B = A + B:</b> A + {B('!A')}B = (A + {B('!A')})(A + B) [distributive] = 1·(A + B) = A + B.</p>"
            "<p><b>Proof of A + AB = A:</b> A + AB = A(1 + B) = A·1 = A.</p>"
            "<p><b>Caution:</b> Boolean algebra has no subtraction or division, and A + A = A (not 2A), A·A = A (not A²).</p>",
          "<p>Boolean expressions ના simplification માટે નીચેના નિયમો વપરાય છે. દરેકને truth table (perfect induction) વડે સાબિત કરી શકાય.</p>" + laws_table("gu")
          + f"<p><b>A + {B('!A')}B = A + B ની સાબિતી:</b> A + {B('!A')}B = (A + {B('!A')})(A + B) [distributive] = 1·(A + B) = A + B.</p>"
            "<p><b>A + AB = A ની સાબિતી:</b> A + AB = A(1 + B) = A·1 = A.</p>"
            "<p><b>ધ્યાન રાખો:</b> Boolean algebra માં બાદબાકી કે ભાગાકાર નથી, અને A + A = A (2A નહીં), A·A = A (A² નહીં).</p>",
          examples=["de2n14"], key=True),

        T("2.3.3 Simplification of Boolean Expressions", "2.3.3 Boolean Expressions નું Simplification",
          f"""<p><b>Simplification</b> means reducing a Boolean expression to an equivalent form with <b>fewer terms and fewer literals</b> (a literal is a variable or its complement). A simpler expression needs fewer gates, so the circuit is cheaper, faster, smaller and uses less power.</p>
<h4>Steps</h4>
<ol>
<li>Remove brackets by multiplying out (distributive law) or apply De Morgan to remove bars over groups.</li>
<li>Take common factors from terms.</li>
<li>Use A + {B('!A')} = 1, A + 1 = 1, A + AB = A, A + {B('!A')}B = A + B, etc.</li>
<li>Check the answer with a truth table if needed.</li>
</ol>
<p><b>Example:</b> Y = AB + A{B('!B')} + {B('!A')}B</p>
<p>= A(B + {B('!B')}) + {B('!A')}B = A·1 + {B('!A')}B = A + {B('!A')}B = <b>A + B</b></p>
<p>Original: 3 AND + 1 OR + 2 NOT gates. Simplified: just 1 OR gate.</p>""",
          f"""<p><b>Simplification</b> એટલે Boolean expression ને <b>ઓછા terms અને ઓછા literals</b> વાળા સમાન સ્વરૂપમાં લાવવું (literal એટલે variable અથવા તેનો complement). સાદા expression માટે ઓછા gates જોઈએ, તેથી circuit સસ્તો, ઝડપી, નાનો બને છે અને ઓછો power વાપરે છે.</p>
<h4>Steps</h4>
<ol>
<li>Distributive law વડે brackets ખોલો અથવા groups પરના bar દૂર કરવા De Morgan લગાવો.</li>
<li>Terms માંથી common factors લો.</li>
<li>A + {B('!A')} = 1, A + 1 = 1, A + AB = A, A + {B('!A')}B = A + B વગેરે વાપરો.</li>
<li>જરૂર હોય તો truth table વડે જવાબ ચકાસો.</li>
</ol>
<p><b>ઉદાહરણ:</b> Y = AB + A{B('!B')} + {B('!A')}B</p>
<p>= A(B + {B('!B')}) + {B('!A')}B = A·1 + {B('!A')}B = A + {B('!A')}B = <b>A + B</b></p>
<p>મૂળ: 3 AND + 1 OR + 2 NOT gates. Simplified: માત્ર 1 OR gate.</p>""",
          examples=["de2n1", "de2n2", "de2n3", "de2n4", "de2n5", "de2n6"], key=True),
    ],
}
assert G.equiv(lambda a, b: (a & b) | (a & n_(b)) | (n_(a) & b), lambda a, b: a | b, 2)

SEC_2_4 = {
    "title": {"en": "2.4 De Morgan's Theorems and Boolean Functions", "gu": "2.4 De Morgan's Theorems અને Boolean Functions"},
    "items": [
        T("2.4.1 De Morgan's Theorems", "2.4.1 De Morgan's Theorems",
          f"""<h4>Theorem 1</h4>
<p>The <b>complement of a product</b> is equal to the <b>sum of the complements</b>:</p>
<p style="text-align:center"><b>{B('!(A·B)')} = {B('!A')} + {B('!B')}</b></p>
<p>So a <b>NAND gate = bubbled (negative-input) OR gate</b>.</p>
<h4>Theorem 2</h4>
<p>The <b>complement of a sum</b> is equal to the <b>product of the complements</b>:</p>
<p style="text-align:center"><b>{B('!(A+B)')} = {B('!A')} · {B('!B')}</b></p>
<p>So a <b>NOR gate = bubbled (negative-input) AND gate</b>.</p>
<p><b>Proof of theorem 2 by truth table</b> (theorem 1 is proved in the diagram):</p>{DM2}
<p>Columns {B('!(A+B)')} and {B('!A·!B')} are identical, hence proved.</p>
<h4>For more variables</h4>
<p>{B('!(ABC)')} = {B('!A')} + {B('!B')} + {B('!C')} &nbsp; and &nbsp; {B('!(A+B+C)')} = {B('!A')}·{B('!B')}·{B('!C')}</p>
<p><b>Rule to remember:</b> "break the bar, change the sign". Break the long bar into bars over each variable and change · to + (or + to ·).</p>
<p><b>Uses:</b> simplifying expressions with bars over groups, finding the complement of a function, and converting circuits to NAND-only or NOR-only form.</p>""",
          f"""<h4>Theorem 1</h4>
<p><b>Product નો complement</b> એ <b>complements ના સરવાળા</b> બરાબર છે:</p>
<p style="text-align:center"><b>{B('!(A·B)')} = {B('!A')} + {B('!B')}</b></p>
<p>તેથી <b>NAND gate = bubbled (negative-input) OR gate</b>.</p>
<h4>Theorem 2</h4>
<p><b>Sum નો complement</b> એ <b>complements ના ગુણાકાર</b> બરાબર છે:</p>
<p style="text-align:center"><b>{B('!(A+B)')} = {B('!A')} · {B('!B')}</b></p>
<p>તેથી <b>NOR gate = bubbled (negative-input) AND gate</b>.</p>
<p><b>Truth table વડે theorem 2 ની સાબિતી</b> (theorem 1 આકૃતિમાં સાબિત કર્યું છે):</p>{DM2}
<p>{B('!(A+B)')} અને {B('!A·!B')} ના columns સરખા છે, તેથી સાબિત.</p>
<h4>વધુ variables માટે</h4>
<p>{B('!(ABC)')} = {B('!A')} + {B('!B')} + {B('!C')} &nbsp; અને &nbsp; {B('!(A+B+C)')} = {B('!A')}·{B('!B')}·{B('!C')}</p>
<p><b>યાદ રાખવાનો નિયમ:</b> "bar તોડો, sign બદલો". લાંબા bar ને દરેક variable પરના bars માં તોડો અને · ને + (અથવા + ને ·) માં બદલો.</p>
<p><b>ઉપયોગ:</b> groups પર bar વાળા expressions નું simplification, function નો complement શોધવો અને circuits ને NAND-only અથવા NOR-only સ્વરૂપમાં ફેરવવા.</p>""",
          diagram="de2_demorgan", examples=["de2n7", "de2n8", "de2n10"], key=True),

        T("2.4.2 Boolean Functions and Logic Diagrams", "2.4.2 Boolean Functions અને Logic Diagrams",
          f"""<p>A <b>Boolean function</b> is an expression formed with binary variables, the operators AND, OR, NOT, brackets and an equal sign, e.g. Y = AB + {B('!A')}C. For each combination of input values the function is either 0 or 1.</p>
<p>A Boolean function can be represented in three ways:</p>
<ol>
<li><b>Algebraic expression</b>, e.g. Y = AB + {B('!A')}C</li>
<li><b>Truth table</b>: output listed for all 2<sup>n</sup> input combinations</li>
<li><b>Logic diagram</b>: interconnection of gates</li>
</ol>
<h4>Drawing the logic diagram from an expression</h4>
<ol>
<li>Use a <b>NOT gate</b> for each complemented variable.</li>
<li>Use an <b>AND gate</b> for each product term.</li>
<li>Use an <b>OR gate</b> to add the product terms.</li>
</ol>
<h4>Writing the expression from a logic diagram</h4>
<p>Write the output of each gate, from inputs to output, until the final output is reached.</p>
<h4>Writing the truth table from an expression</h4>
<p>List all input combinations and evaluate the expression for each row. For Y = AB + {B('!A')}C, Y = 1 when (A = 1 and B = 1) or (A = 0 and C = 1), giving rows 1, 3, 6, 7.</p>""",
          f"""<p><b>Boolean function</b> એ binary variables, AND, OR, NOT operators, brackets અને બરાબર ચિહ્ન વડે બનેલું expression છે, દા.ત. Y = AB + {B('!A')}C. Inputs ના દરેક combination માટે function ની કિંમત 0 અથવા 1 હોય છે.</p>
<p>Boolean function ને ત્રણ રીતે દર્શાવી શકાય:</p>
<ol>
<li><b>Algebraic expression</b>, દા.ત. Y = AB + {B('!A')}C</li>
<li><b>Truth table</b>: બધા 2<sup>n</sup> input combinations માટે output</li>
<li><b>Logic diagram</b>: gates ની જોડાણ રચના</li>
</ol>
<h4>Expression પરથી logic diagram દોરવો</h4>
<ol>
<li>દરેક complemented variable માટે <b>NOT gate</b> વાપરો.</li>
<li>દરેક product term માટે <b>AND gate</b> વાપરો.</li>
<li>Product terms નો સરવાળો કરવા <b>OR gate</b> વાપરો.</li>
</ol>
<h4>Logic diagram પરથી expression લખવું</h4>
<p>Inputs થી output તરફ દરેક gate નું output લખતા જાઓ, જ્યાં સુધી અંતિમ output ન મળે.</p>
<h4>Expression પરથી truth table લખવું</h4>
<p>બધા input combinations લખી દરેક row માટે expression ની કિંમત શોધો. Y = AB + {B('!A')}C માટે, (A = 1 અને B = 1) અથવા (A = 0 અને C = 1) હોય ત્યારે Y = 1, એટલે rows 1, 3, 6, 7.</p>""",
          diagram="de2_func_impl", examples=["de2n9"], key=True),

        T("2.4.3 SOP and POS Forms, Minterms and Maxterms", "2.4.3 SOP અને POS સ્વરૂપ, Minterms અને Maxterms",
          f"""<h4>SOP (Sum of Products)</h4>
<p>Product (AND) terms are ORed together, e.g. Y = AB + {B('!A')}C + B{B('!C')}. It is implemented by an <b>AND-OR</b> circuit.</p>
<h4>POS (Product of Sums)</h4>
<p>Sum (OR) terms are ANDed together, e.g. Y = (A + B)({B('!A')} + C). It is implemented by an <b>OR-AND</b> circuit.</p>
<h4>Minterm and maxterm</h4>
<ul>
<li><b>Minterm (m):</b> a product term containing <b>all variables</b>, each once (true or complemented). A variable is complemented if its value is 0. Each minterm is 1 for only one row of the truth table.</li>
<li><b>Maxterm (M):</b> a sum term containing all variables. A variable is complemented if its value is 1. Each maxterm is 0 for only one row.</li>
<li>M<sub>i</sub> = {B('!m')}<sub>i</sub> (a maxterm is the complement of the minterm with the same number).</li>
</ul>{MM}
<h4>Canonical (standard) forms</h4>
<ul>
<li><b>Canonical SOP</b> = sum of the minterms for which Y = 1: Y = Σm(…)</li>
<li><b>Canonical POS</b> = product of the maxterms for which Y = 0: Y = ΠM(…)</li>
</ul>
<p><i>Example:</i> if Y = 1 for rows 1, 3, 6, 7 then Y = Σm(1, 3, 6, 7) = ΠM(0, 2, 4, 5).</p>
<p><b>To expand a term to canonical form</b>, multiply a missing variable X by (X + {B('!X')}) = 1. E.g. A = A(B + {B('!B')}) = AB + A{B('!B')}.</p>""",
          f"""<h4>SOP (Sum of Products)</h4>
<p>Product (AND) terms ને OR કરાય છે, દા.ત. Y = AB + {B('!A')}C + B{B('!C')}. તે <b>AND-OR</b> circuit વડે બને છે.</p>
<h4>POS (Product of Sums)</h4>
<p>Sum (OR) terms ને AND કરાય છે, દા.ત. Y = (A + B)({B('!A')} + C). તે <b>OR-AND</b> circuit વડે બને છે.</p>
<h4>Minterm અને maxterm</h4>
<ul>
<li><b>Minterm (m):</b> <b>બધા variables</b> એક વાર (true અથવા complemented) ધરાવતો product term. Variable ની કિંમત 0 હોય તો તેનો complement લેવાય. દરેક minterm truth table ની માત્ર એક row માટે 1 હોય છે.</li>
<li><b>Maxterm (M):</b> બધા variables ધરાવતો sum term. Variable ની કિંમત 1 હોય તો તેનો complement લેવાય. દરેક maxterm માત્ર એક row માટે 0 હોય છે.</li>
<li>M<sub>i</sub> = {B('!m')}<sub>i</sub> (maxterm એ સમાન ક્રમના minterm નો complement છે).</li>
</ul>{MM}
<h4>Canonical (standard) સ્વરૂપ</h4>
<ul>
<li><b>Canonical SOP</b> = જ્યાં Y = 1 હોય તે minterms નો સરવાળો: Y = Σm(…)</li>
<li><b>Canonical POS</b> = જ્યાં Y = 0 હોય તે maxterms નો ગુણાકાર: Y = ΠM(…)</li>
</ul>
<p><i>ઉદાહરણ:</i> Y = 1 rows 1, 3, 6, 7 માટે હોય તો Y = Σm(1, 3, 6, 7) = ΠM(0, 2, 4, 5).</p>
<p><b>કોઈ term ને canonical સ્વરૂપમાં વિસ્તારવા</b>, ખૂટતા variable X માટે (X + {B('!X')}) = 1 વડે ગુણો. દા.ત. A = A(B + {B('!B')}) = AB + A{B('!B')}.</p>""",
          diagram="de2_sop_pos", examples=["de2n11"], key=True),

        T("2.4.4 Complement and Dual of a Function", "2.4.4 Function નો Complement અને Dual",
          f"""<h4>Complement of a function</h4>
<p>The complement {B('!Y')} is 1 where Y is 0. It is found using <b>De Morgan's theorem</b>: interchange + and ·, interchange 0 and 1, and <b>complement every variable</b>.</p>
<p><i>Example:</i> Y = A{B('!B')} + C → {B('!Y')} = ({B('!A')} + B)·{B('!C')}</p>
<h4>Dual of a function</h4>
<p>Interchange + and ·, interchange 0 and 1, but <b>do not complement the variables</b>.</p>
<p><i>Example:</i> Y = A{B('!B')} + C → dual = (A + {B('!B')})·C</p>
<table><tr><th>Step</th><th>Complement</th><th>Dual</th></tr>
<tr><td>+ ↔ ·</td><td>Yes</td><td>Yes</td></tr><tr><td>0 ↔ 1</td><td>Yes</td><td>Yes</td></tr>
<tr><td>Complement variables</td><td>Yes</td><td>No</td></tr></table>
<p><b>Tip:</b> keep the original grouping by adding brackets before changing the operators: AB + C → (A + B)·C, not A + B·C.</p>""",
          f"""<h4>Function નો complement</h4>
<p>Complement {B('!Y')} ત્યાં 1 હોય જ્યાં Y = 0 હોય. તે <b>De Morgan's theorem</b> વડે મળે: + અને · ની અદલાબદલી, 0 અને 1 ની અદલાબદલી, અને <b>દરેક variable નો complement</b>.</p>
<p><i>ઉદાહરણ:</i> Y = A{B('!B')} + C → {B('!Y')} = ({B('!A')} + B)·{B('!C')}</p>
<h4>Function નો dual</h4>
<p>+ અને · ની અદલાબદલી, 0 અને 1 ની અદલાબદલી, પરંતુ <b>variables નો complement લેવો નહીં</b>.</p>
<p><i>ઉદાહરણ:</i> Y = A{B('!B')} + C → dual = (A + {B('!B')})·C</p>
<table><tr><th>Step</th><th>Complement</th><th>Dual</th></tr>
<tr><td>+ ↔ ·</td><td>હા</td><td>હા</td></tr><tr><td>0 ↔ 1</td><td>હા</td><td>હા</td></tr>
<tr><td>Variables નો complement</td><td>હા</td><td>ના</td></tr></table>
<p><b>Tip:</b> operators બદલતાં પહેલાં brackets ઉમેરી મૂળ grouping જાળવો: AB + C → (A + B)·C, A + B·C નહીં.</p>""",
          examples=["de2n12"]),
    ],
}
assert G.equiv(lambda a, b, c: n_((a & n_(b)) | c), lambda a, b, c: (n_(a) | b) & n_(c), 3)

NOTES_B = [SEC_2_3, SEC_2_4]
