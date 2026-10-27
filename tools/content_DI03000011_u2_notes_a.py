"""Digital Electronics Fundamentals (DI03000011) - Unit 2 notes, part A: 2.1 Binary logic, 2.2 Logic gates."""
from content_DI03000011_u1_notes_a import T
import de_gates as G

B = G.bh


def TT(kind, n=2):
    head = ["A", "B", "Y"] if n == 2 else ["A", "Y"]
    return G.tt_html(head, G.truth(G.OPS[kind], n))


TT3_AND = G.tt_html(["A", "B", "C", "Y"], G.truth(lambda a, b, c: a & b & c, 3))
TT3_OR = G.tt_html(["A", "B", "C", "Y"], G.truth(lambda a, b, c: a | b | c, 3))


def gate_body(lang, kind, expr, define, rule, ic, extra=""):
    """common layout for one gate card"""
    if lang == "en":
        return (f"<p>{define}</p>"
                f"<p><b>Boolean expression:</b> {B(expr)}</p>"
                f"<p><b>Truth table (2-input):</b></p>{TT(kind, 1 if kind == 'NOT' else 2)}"
                f"<p><b>Rule:</b> {rule}</p>{extra}<p><b>IC:</b> {ic}</p>")
    return (f"<p>{define}</p>"
            f"<p><b>Boolean expression:</b> {B(expr)}</p>"
            f"<p><b>Truth table (2-input):</b></p>{TT(kind, 1 if kind == 'NOT' else 2)}"
            f"<p><b>નિયમ:</b> {rule}</p>{extra}<p><b>IC:</b> {ic}</p>")


SEC_2_1 = {
    "title": {"en": "2.1 Binary Logic", "gu": "2.1 Binary Logic"},
    "items": [
        T("2.1.1 Binary Logic and Logic Operations", "2.1.1 Binary Logic અને Logic Operations",
          f"""<p><b>Binary logic</b> deals with <b>binary variables</b> (A, B, C, X, Y …) that can take only two values, <b>0 and 1</b> (FALSE/TRUE, OFF/ON, LOW/HIGH), and with <b>logical operations</b> on them.</p>
<h4>Three basic logic operations</h4>
<table><tr><th>Operation</th><th>Symbol</th><th>Meaning</th></tr>
<tr><td>AND</td><td>A · B or AB</td><td>1 only if both are 1</td></tr>
<tr><td>OR</td><td>A + B</td><td>1 if any one is 1</td></tr>
<tr><td>NOT</td><td>{B('!A')} or A'</td><td>Complement (inverts the value)</td></tr></table>
<p><b>Note:</b> "+" here means logical OR, not arithmetic addition. In binary logic 1 + 1 = 1.</p>
<h4>Truth table</h4>
<p>A <b>truth table</b> lists the output for <b>every possible combination</b> of inputs. With n inputs there are <b>2<sup>n</sup> rows</b> (2 inputs → 4 rows, 3 inputs → 8 rows, 4 inputs → 16 rows). Inputs are written in binary counting order (000, 001, 010 …).</p>
<h4>Logic levels</h4>
<p>In TTL circuits (5 V supply), a voltage from <b>2 V to 5 V</b> is treated as HIGH and <b>0 V to 0.8 V</b> as LOW. The range in between is undefined.</p>""",
          f"""<p><b>Binary logic</b> એવા <b>binary variables</b> (A, B, C, X, Y …) સાથે કામ કરે છે જે માત્ર બે કિંમત, <b>0 અને 1</b> (FALSE/TRUE, OFF/ON, LOW/HIGH), લઈ શકે, અને તેમના પરના <b>logical operations</b> સાથે.</p>
<h4>ત્રણ મૂળભૂત logic operations</h4>
<table><tr><th>Operation</th><th>Symbol</th><th>અર્થ</th></tr>
<tr><td>AND</td><td>A · B અથવા AB</td><td>બંને 1 હોય તો જ 1</td></tr>
<tr><td>OR</td><td>A + B</td><td>કોઈ પણ એક 1 હોય તો 1</td></tr>
<tr><td>NOT</td><td>{B('!A')} અથવા A'</td><td>Complement (કિંમત ઉલટાવે)</td></tr></table>
<p><b>નોંધ:</b> અહીં "+" નો અર્થ logical OR છે, ગણિતનો સરવાળો નહીં. Binary logic માં 1 + 1 = 1.</p>
<h4>Truth table</h4>
<p><b>Truth table</b> માં inputs ના <b>દરેક શક્ય combination</b> માટે output લખાય છે. n inputs માટે <b>2<sup>n</sup> rows</b> હોય (2 inputs → 4 rows, 3 inputs → 8 rows, 4 inputs → 16 rows). Inputs binary ગણતરીના ક્રમમાં (000, 001, 010 …) લખાય છે.</p>
<h4>Logic levels</h4>
<p>TTL circuits (5 V supply) માં <b>2 V થી 5 V</b> ને HIGH અને <b>0 V થી 0.8 V</b> ને LOW ગણાય છે. વચ્ચેની range undefined છે.</p>""",
          key=True),

        T("2.1.2 Positive and Negative Logic", "2.1.2 Positive અને Negative Logic",
          """<p>The two voltage levels of a digital signal can be assigned to logic 1 and 0 in two ways:</p>
<h4>Positive logic</h4>
<p>The <b>higher voltage</b> represents logic <b>1</b> and the lower voltage represents logic <b>0</b>. E.g. +5 V = 1, 0 V = 0. Most digital systems use positive logic.</p>
<h4>Negative logic</h4>
<p>The <b>lower voltage</b> represents logic <b>1</b> and the higher voltage represents logic <b>0</b>. E.g. 0 V = 1, +5 V = 0 (or −5 V = 1, 0 V = 0).</p>
<table><tr><th>Voltage</th><th>Positive logic</th><th>Negative logic</th></tr>
<tr><td>HIGH (+5 V)</td><td>1</td><td>0</td></tr><tr><td>LOW (0 V)</td><td>0</td><td>1</td></tr></table>
<h4>Effect on gates</h4>
<p>The same circuit performs different logic functions depending on the convention. Changing from positive to negative logic converts:</p>
<ul><li>AND ↔ OR</li><li>NAND ↔ NOR</li><li>NOT remains NOT</li></ul>
<p><i>Example:</i> a gate whose output is HIGH only when both inputs are HIGH is an <b>AND</b> gate in positive logic; in negative logic the same gate gives logic 0 only when both inputs are 0, i.e. it works as an <b>OR</b> gate.</p>""",
          """<p>Digital signal ના બે voltage levels ને logic 1 અને 0 સાથે બે રીતે જોડી શકાય:</p>
<h4>Positive logic</h4>
<p><b>વધુ voltage</b> logic <b>1</b> અને ઓછું voltage logic <b>0</b> દર્શાવે છે. દા.ત. +5 V = 1, 0 V = 0. મોટા ભાગની digital systems positive logic વાપરે છે.</p>
<h4>Negative logic</h4>
<p><b>ઓછું voltage</b> logic <b>1</b> અને વધુ voltage logic <b>0</b> દર્શાવે છે. દા.ત. 0 V = 1, +5 V = 0 (અથવા −5 V = 1, 0 V = 0).</p>
<table><tr><th>Voltage</th><th>Positive logic</th><th>Negative logic</th></tr>
<tr><td>HIGH (+5 V)</td><td>1</td><td>0</td></tr><tr><td>LOW (0 V)</td><td>0</td><td>1</td></tr></table>
<h4>Gates પર અસર</h4>
<p>એક જ circuit convention પ્રમાણે જુદાં logic functions કરે છે. Positive માંથી negative logic માં બદલતાં:</p>
<ul><li>AND ↔ OR</li><li>NAND ↔ NOR</li><li>NOT એ NOT જ રહે</li></ul>
<p><i>ઉદાહરણ:</i> જે gate નું output બંને inputs HIGH હોય ત્યારે જ HIGH થાય તે positive logic માં <b>AND</b> gate છે; negative logic માં એ જ gate બંને inputs 0 હોય ત્યારે જ 0 આપે છે, એટલે કે તે <b>OR</b> gate તરીકે કામ કરે છે.</p>""",
          diagram="de2_pos_neg", examples=["de2n15"]),
    ],
}

SEC_2_2 = {
    "title": {"en": "2.2 Logic Gates", "gu": "2.2 Logic Gates"},
    "items": [
        T("2.2.1 AND Gate", "2.2.1 AND Gate",
          gate_body("en", "AND", "Y = A·B",
                    "A <b>logic gate</b> is an electronic circuit with one or more inputs and one output that performs a logic operation. The <b>AND gate</b> performs logical multiplication.",
                    "the output is <b>1 only when all inputs are 1</b>; if any input is 0, the output is 0.", "7408 (quad 2-input AND)",
                    "<p>It works like <b>switches in series</b>: the lamp glows only when both switches A and B are closed.</p>"
                    "<p><b>3-input AND:</b> Y = ABC</p>" + TT3_AND),
          gate_body("gu", "AND", "Y = A·B",
                    "<b>Logic gate</b> એ એક કે વધુ inputs અને એક output વાળો electronic circuit છે જે logic operation કરે છે. <b>AND gate</b> logical ગુણાકાર કરે છે.",
                    "<b>બધા inputs 1 હોય ત્યારે જ output 1</b>; કોઈ પણ input 0 હોય તો output 0.", "7408 (quad 2-input AND)",
                    "<p>તે <b>series માં જોડેલી switches</b> જેવું કામ કરે છે: switch A અને B બંને બંધ (ON) હોય ત્યારે જ lamp ચાલુ થાય.</p>"
                    "<p><b>3-input AND:</b> Y = ABC</p>" + TT3_AND),
          diagram="de2_and", key=True),

        T("2.2.2 OR Gate", "2.2.2 OR Gate",
          gate_body("en", "OR", "Y = A + B", "The <b>OR gate</b> performs logical addition.",
                    "the output is <b>1 when any one (or more) input is 1</b>; the output is 0 only when all inputs are 0.", "7432 (quad 2-input OR)",
                    "<p>It works like <b>switches in parallel</b>: the lamp glows when switch A or switch B (or both) is closed.</p>"
                    "<p><b>3-input OR:</b> Y = A + B + C</p>" + TT3_OR),
          gate_body("gu", "OR", "Y = A + B", "<b>OR gate</b> logical સરવાળો કરે છે.",
                    "<b>કોઈ પણ એક (કે વધુ) input 1 હોય ત્યારે output 1</b>; બધા inputs 0 હોય ત્યારે જ output 0.", "7432 (quad 2-input OR)",
                    "<p>તે <b>parallel માં જોડેલી switches</b> જેવું કામ કરે છે: switch A અથવા B (અથવા બંને) બંધ હોય ત્યારે lamp ચાલુ થાય.</p>"
                    "<p><b>3-input OR:</b> Y = A + B + C</p>" + TT3_OR),
          diagram="de2_or", key=True),

        T("2.2.3 NOT Gate (Inverter)", "2.2.3 NOT Gate (Inverter)",
          gate_body("en", "NOT", "Y = !A", "The <b>NOT gate</b> has <b>one input and one output</b>. It performs complementation (inversion).",
                    "the output is the <b>complement</b> of the input: 0 → 1 and 1 → 0. The small circle (bubble) at the output means inversion.",
                    "7404 (hex inverter, 6 NOT gates)",
                    "<p>Two NOT gates in series give back the original signal: double complement = A.</p>"),
          gate_body("gu", "NOT", "Y = !A", "<b>NOT gate</b> માં <b>એક input અને એક output</b> હોય છે. તે complement (inversion) કરે છે.",
                    "output એ input નો <b>complement</b> છે: 0 → 1 અને 1 → 0. Output પરનું નાનું વર્તુળ (bubble) inversion દર્શાવે છે.",
                    "7404 (hex inverter, 6 NOT gates)",
                    "<p>Series માં બે NOT gates મૂકવાથી મૂળ signal પાછો મળે: double complement = A.</p>"),
          diagram="de2_not", key=True),

        T("2.2.4 NAND Gate", "2.2.4 NAND Gate",
          gate_body("en", "NAND", "Y = !(A·B)", "The <b>NAND gate</b> (NOT-AND) is an <b>AND gate followed by a NOT gate</b>. Its output is the complement of the AND output.",
                    "the output is <b>0 only when all inputs are 1</b>; otherwise the output is 1.", "7400 (quad 2-input NAND)",
                    "<p>NAND is a <b>universal gate</b> (see 2.2.9).</p>"),
          gate_body("gu", "NAND", "Y = !(A·B)", "<b>NAND gate</b> (NOT-AND) એ <b>AND gate પછી NOT gate</b> છે. તેનું output AND output નો complement છે.",
                    "<b>બધા inputs 1 હોય ત્યારે જ output 0</b>; બાકી output 1.", "7400 (quad 2-input NAND)",
                    "<p>NAND એ <b>universal gate</b> છે (જુઓ 2.2.9).</p>"),
          diagram="de2_nand", key=True),

        T("2.2.5 NOR Gate", "2.2.5 NOR Gate",
          gate_body("en", "NOR", "Y = !(A+B)", "The <b>NOR gate</b> (NOT-OR) is an <b>OR gate followed by a NOT gate</b>.",
                    "the output is <b>1 only when all inputs are 0</b>; if any input is 1, the output is 0.", "7402 (quad 2-input NOR)",
                    "<p>NOR is also a <b>universal gate</b> (see 2.2.10).</p>"),
          gate_body("gu", "NOR", "Y = !(A+B)", "<b>NOR gate</b> (NOT-OR) એ <b>OR gate પછી NOT gate</b> છે.",
                    "<b>બધા inputs 0 હોય ત્યારે જ output 1</b>; કોઈ પણ input 1 હોય તો output 0.", "7402 (quad 2-input NOR)",
                    "<p>NOR પણ <b>universal gate</b> છે (જુઓ 2.2.10).</p>"),
          diagram="de2_nor", key=True),

        T("2.2.6 EX-OR Gate", "2.2.6 EX-OR Gate",
          gate_body("en", "XOR", f"Y = A⊕B = A!B + !AB", "The <b>Exclusive-OR (EX-OR / XOR)</b> gate gives output 1 when the inputs are <b>different</b>. Symbol of the operation: ⊕.",
                    "the output is <b>1 when an odd number of inputs are 1</b> (for 2 inputs: when A ≠ B).", "7486 (quad 2-input EX-OR)",
                    "<p><b>Applications:</b> half adder and full adder (sum bit), parity generator/checker, comparator, controlled inverter (A⊕1 = " + B("!A") + ", A⊕0 = A).</p>"
                    "<p>It can be built using 2 NOT, 2 AND and 1 OR gate (see diagram).</p>"),
          gate_body("gu", "XOR", f"Y = A⊕B = A!B + !AB", "<b>Exclusive-OR (EX-OR / XOR)</b> gate inputs <b>જુદા</b> હોય ત્યારે output 1 આપે છે. Operation નો symbol: ⊕.",
                    "<b>એકી (odd) સંખ્યામાં inputs 1 હોય ત્યારે output 1</b> (2 inputs માટે: A ≠ B હોય ત્યારે).", "7486 (quad 2-input EX-OR)",
                    "<p><b>ઉપયોગો:</b> half adder અને full adder (sum bit), parity generator/checker, comparator, controlled inverter (A⊕1 = " + B("!A") + ", A⊕0 = A).</p>"
                    "<p>તેને 2 NOT, 2 AND અને 1 OR gate વડે બનાવી શકાય (આકૃતિ જુઓ).</p>"),
          diagram="de2_xor", key=True),

        T("2.2.7 EX-NOR Gate", "2.2.7 EX-NOR Gate",
          gate_body("en", "XNOR", "Y = !(A⊕B) = AB + !A!B", "The <b>Exclusive-NOR (EX-NOR / XNOR)</b> gate is an EX-OR gate followed by a NOT gate. Symbol: ⊙.",
                    "the output is <b>1 when the inputs are equal</b> (both 0 or both 1).", "74266 (quad 2-input EX-NOR)",
                    "<p>It is also called the <b>equality</b> or <b>coincidence</b> gate and is used in digital <b>comparators</b> to check whether two bits are equal.</p>"),
          gate_body("gu", "XNOR", "Y = !(A⊕B) = AB + !A!B", "<b>Exclusive-NOR (EX-NOR / XNOR)</b> gate એ EX-OR gate પછી NOT gate છે. Symbol: ⊙.",
                    "<b>inputs સરખા હોય ત્યારે output 1</b> (બંને 0 અથવા બંને 1).", "74266 (quad 2-input EX-NOR)",
                    "<p>તેને <b>equality</b> અથવા <b>coincidence</b> gate પણ કહે છે અને બે bits સરખા છે કે નહીં તે ચકાસવા digital <b>comparators</b> માં વપરાય છે.</p>"),
          diagram="de2_xnor", key=True),

        T("2.2.8 Classification and Summary of Logic Gates", "2.2.8 Logic Gates નું વર્ગીકરણ અને સારાંશ",
          f"""<h4>Classification</h4>
<ol>
<li><b>Basic gates:</b> AND, OR, NOT. Every Boolean function can be built using these three.</li>
<li><b>Universal gates:</b> NAND, NOR. Any gate (and any circuit) can be built using only one type of universal gate.</li>
<li><b>Special (derived) gates:</b> EX-OR, EX-NOR.</li>
</ol>
<h4>Summary</h4>
<table><tr><th>Gate</th><th>Expression</th><th>Output is 1 when</th></tr>
<tr><td>AND</td><td>AB</td><td>all inputs are 1</td></tr>
<tr><td>OR</td><td>A + B</td><td>any input is 1</td></tr>
<tr><td>NOT</td><td>{B('!A')}</td><td>input is 0</td></tr>
<tr><td>NAND</td><td>{B('!(AB)')}</td><td>any input is 0</td></tr>
<tr><td>NOR</td><td>{B('!(A+B)')}</td><td>all inputs are 0</td></tr>
<tr><td>EX-OR</td><td>A⊕B</td><td>inputs are different</td></tr>
<tr><td>EX-NOR</td><td>{B('!(A⊕B)')}</td><td>inputs are equal</td></tr></table>""",
          f"""<h4>વર્ગીકરણ</h4>
<ol>
<li><b>Basic gates:</b> AND, OR, NOT. આ ત્રણ વડે દરેક Boolean function બનાવી શકાય.</li>
<li><b>Universal gates:</b> NAND, NOR. માત્ર એક પ્રકારના universal gate વડે કોઈ પણ gate (અને કોઈ પણ circuit) બનાવી શકાય.</li>
<li><b>Special (derived) gates:</b> EX-OR, EX-NOR.</li>
</ol>
<h4>સારાંશ</h4>
<table><tr><th>Gate</th><th>Expression</th><th>Output 1 ક્યારે</th></tr>
<tr><td>AND</td><td>AB</td><td>બધા inputs 1</td></tr>
<tr><td>OR</td><td>A + B</td><td>કોઈ પણ input 1</td></tr>
<tr><td>NOT</td><td>{B('!A')}</td><td>input 0</td></tr>
<tr><td>NAND</td><td>{B('!(AB)')}</td><td>કોઈ પણ input 0</td></tr>
<tr><td>NOR</td><td>{B('!(A+B)')}</td><td>બધા inputs 0</td></tr>
<tr><td>EX-OR</td><td>A⊕B</td><td>inputs જુદા</td></tr>
<tr><td>EX-NOR</td><td>{B('!(A⊕B)')}</td><td>inputs સરખા</td></tr></table>""",
          diagram="de2_summary"),

        T("2.2.9 NAND as a Universal Gate", "2.2.9 Universal Gate તરીકે NAND",
          f"""<p>A <b>universal gate</b> is a gate with which <b>all basic gates (NOT, AND, OR)</b> can be made, so any logic circuit can be built using it alone. NAND and NOR are universal gates. They are preferred because only one IC type is needed, which reduces cost and inventory.</p>
<h4>Basic gates using NAND</h4>
<ol>
<li><b>NOT:</b> join both inputs of a NAND gate: Y = {B('!(A·A)')} = {B('!A')}. (1 NAND)</li>
<li><b>AND:</b> NAND followed by a NAND-inverter: Y = {B('!(!(AB))')} = AB. (2 NAND)</li>
<li><b>OR:</b> invert both inputs using NAND-inverters, then NAND them: Y = {B('!(!A·!B)')} = A + B (by De Morgan's theorem). (3 NAND)</li>
</ol>
<p><b>NOR using NAND:</b> make OR with 3 NAND gates and add one more NAND-inverter (4 NAND).</p>""",
          f"""<p><b>Universal gate</b> એવો gate છે જેના વડે <b>બધા basic gates (NOT, AND, OR)</b> બનાવી શકાય, તેથી માત્ર તેના વડે કોઈ પણ logic circuit બનાવી શકાય. NAND અને NOR universal gates છે. માત્ર એક જ પ્રકારનું IC જોઈએ, તેથી cost અને inventory ઘટે છે; માટે તે પસંદ કરાય છે.</p>
<h4>NAND વડે basic gates</h4>
<ol>
<li><b>NOT:</b> NAND gate ના બંને inputs જોડી દો: Y = {B('!(A·A)')} = {B('!A')}. (1 NAND)</li>
<li><b>AND:</b> NAND પછી NAND-inverter: Y = {B('!(!(AB))')} = AB. (2 NAND)</li>
<li><b>OR:</b> NAND-inverters વડે બંને inputs invert કરી, પછી NAND કરો: Y = {B('!(!A·!B)')} = A + B (De Morgan's theorem મુજબ). (3 NAND)</li>
</ol>
<p><b>NAND વડે NOR:</b> 3 NAND વડે OR બનાવી એક વધુ NAND-inverter ઉમેરો (4 NAND).</p>""",
          diagram="de2_nand_universal", examples=["de2n13"], key=True),

        T("2.2.10 NOR as a Universal Gate", "2.2.10 Universal Gate તરીકે NOR",
          f"""<h4>Basic gates using NOR</h4>
<ol>
<li><b>NOT:</b> join both inputs of a NOR gate: Y = {B('!(A+A)')} = {B('!A')}. (1 NOR)</li>
<li><b>OR:</b> NOR followed by a NOR-inverter: Y = {B('!(!(A+B))')} = A + B. (2 NOR)</li>
<li><b>AND:</b> invert both inputs using NOR-inverters, then NOR them: Y = {B('!(!A+!B)')} = AB (by De Morgan's theorem). (3 NOR)</li>
</ol>
<p><b>NAND using NOR:</b> make AND with 3 NOR gates and add a NOR-inverter (4 NOR).</p>
<table><tr><th>Gate to make</th><th>NAND gates</th><th>NOR gates</th></tr>
<tr><td>NOT</td><td>1</td><td>1</td></tr><tr><td>AND</td><td>2</td><td>3</td></tr><tr><td>OR</td><td>3</td><td>2</td></tr>
<tr><td>NOR / NAND</td><td>4</td><td>4</td></tr></table>""",
          f"""<h4>NOR વડે basic gates</h4>
<ol>
<li><b>NOT:</b> NOR gate ના બંને inputs જોડી દો: Y = {B('!(A+A)')} = {B('!A')}. (1 NOR)</li>
<li><b>OR:</b> NOR પછી NOR-inverter: Y = {B('!(!(A+B))')} = A + B. (2 NOR)</li>
<li><b>AND:</b> NOR-inverters વડે બંને inputs invert કરી, પછી NOR કરો: Y = {B('!(!A+!B)')} = AB (De Morgan's theorem મુજબ). (3 NOR)</li>
</ol>
<p><b>NOR વડે NAND:</b> 3 NOR વડે AND બનાવી NOR-inverter ઉમેરો (4 NOR).</p>
<table><tr><th>બનાવવાનો gate</th><th>NAND gates</th><th>NOR gates</th></tr>
<tr><td>NOT</td><td>1</td><td>1</td></tr><tr><td>AND</td><td>2</td><td>3</td></tr><tr><td>OR</td><td>3</td><td>2</td></tr>
<tr><td>NOR / NAND</td><td>4</td><td>4</td></tr></table>""",
          diagram="de2_nor_universal", key=True),

        T("2.2.11 Logic Gate ICs (Practical)", "2.2.11 Logic Gate ICs (Practical)",
          """<p>Logic gates are available as <b>TTL 74-series ICs</b> in a 14-pin DIP package. Pin 14 is <b>VCC (+5 V)</b> and pin 7 is <b>GND</b>. Pins are counted anticlockwise from the notch (pin 1 at bottom-left when the notch is on the left).</p>
<table><tr><th>IC</th><th>Gate</th><th>Gates per IC</th></tr>
<tr><td>7408</td><td>2-input AND</td><td>4</td></tr><tr><td>7432</td><td>2-input OR</td><td>4</td></tr>
<tr><td>7404</td><td>NOT</td><td>6</td></tr><tr><td>7400</td><td>2-input NAND</td><td>4</td></tr>
<tr><td>7402</td><td>2-input NOR</td><td>4</td></tr><tr><td>7486</td><td>2-input EX-OR</td><td>4</td></tr>
<tr><td>74266</td><td>2-input EX-NOR</td><td>4</td></tr></table>
<h4>Verifying a truth table (Practical 3)</h4>
<ol>
<li>Place the IC on the breadboard; connect pin 14 to +5 V and pin 7 to ground.</li>
<li>Connect inputs (e.g. pins 1 and 2) to logic switches and the output (pin 3) to an LED with a 330 Ω resistor.</li>
<li>Apply all input combinations 00, 01, 10, 11 and note the LED: ON = 1, OFF = 0.</li>
<li>Compare with the theoretical truth table.</li>
</ol>
<p><b>Precautions:</b> do not exceed 5 V; never leave TTL inputs floating (they act as 1); switch off the supply while changing connections. <b>Note:</b> the 7402 NOR IC has a different pinout (outputs on pins 1, 4, 10, 13).</p>""",
          """<p>Logic gates <b>TTL 74-series ICs</b> તરીકે 14-pin DIP package માં મળે છે. Pin 14 <b>VCC (+5 V)</b> અને pin 7 <b>GND</b> છે. Notch થી શરૂ કરીને pins ઘડિયાળની વિરુદ્ધ દિશામાં ગણાય છે (notch ડાબી બાજુ હોય ત્યારે pin 1 નીચે ડાબે).</p>
<table><tr><th>IC</th><th>Gate</th><th>IC દીઠ gates</th></tr>
<tr><td>7408</td><td>2-input AND</td><td>4</td></tr><tr><td>7432</td><td>2-input OR</td><td>4</td></tr>
<tr><td>7404</td><td>NOT</td><td>6</td></tr><tr><td>7400</td><td>2-input NAND</td><td>4</td></tr>
<tr><td>7402</td><td>2-input NOR</td><td>4</td></tr><tr><td>7486</td><td>2-input EX-OR</td><td>4</td></tr>
<tr><td>74266</td><td>2-input EX-NOR</td><td>4</td></tr></table>
<h4>Truth table ની ચકાસણી (Practical 3)</h4>
<ol>
<li>IC ને breadboard પર મૂકો; pin 14 ને +5 V અને pin 7 ને ground સાથે જોડો.</li>
<li>Inputs (દા.ત. pins 1 અને 2) ને logic switches સાથે અને output (pin 3) ને 330 Ω resistor સાથે LED પર જોડો.</li>
<li>બધા input combinations 00, 01, 10, 11 આપો અને LED નોંધો: ON = 1, OFF = 0.</li>
<li>Theoretical truth table સાથે સરખાવો.</li>
</ol>
<p><b>સાવચેતી:</b> 5 V થી વધુ ન આપો; TTL inputs ખુલ્લા (floating) ન રાખો (તે 1 તરીકે વર્તે છે); connections બદલતી વખતે supply બંધ કરો. <b>નોંધ:</b> 7402 NOR IC ની pin રચના જુદી છે (outputs pins 1, 4, 10, 13 પર).</p>""",
          diagram="de2_ic7400"),
    ],
}

NOTES_A = [SEC_2_1, SEC_2_2]
