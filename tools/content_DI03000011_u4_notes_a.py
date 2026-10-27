"""Digital Electronics Fundamentals (DI03000011) - Unit 4 notes, part A: 4.1 Introduction, 4.2 Arithmetic circuits."""
from content_DI03000011_u1_notes_a import T
from de_gates import tt_html, bh as B
from diagrams_DI03000011_u4 import rows, HA, FA, HS, FS

TT_HA = tt_html(["A", "B", "S", "C"], rows(HA, 2), 2)
TT_FA = tt_html(["A", "B", "Cin", "S", "Cout"], rows(FA, 3), 2)
TT_HS = tt_html(["A", "B", "D", "Bo"], rows(HS, 2), 2)
TT_FS = tt_html(["A", "B", "Bin", "D", "Bout"], rows(FS, 3), 2)
NC = B("!(Cin)")
NBI = B("!(Bin)")

SEC_4_1 = {
    "title": {"en": "4.1 Introduction to Combinational Circuits", "gu": "4.1 Combinational Circuits નો પરિચય"},
    "items": [
        T("4.1.1 Combinational Circuits", "4.1.1 Combinational Circuits",
          """<p>A <b>combinational circuit</b> is a logic circuit whose outputs at any instant depend <b>only on the present combination of inputs</b>. It is made of logic gates only.</p>
<p>It has <b>n input variables</b> and <b>m output variables</b>. For each of the 2<sup>n</sup> input combinations there is one fixed output combination, so it is fully described by a <b>truth table</b> or by m Boolean equations.</p>
<h4>Characteristics</h4>
<ul>
<li>Output depends only on present inputs (not on past inputs).</li>
<li>No memory element and no clock.</li>
<li>No feedback path from output to input.</li>
<li>Built with basic and universal gates.</li>
</ul>
<h4>Classification</h4>
<ul>
<li><b>Arithmetic and logical circuits:</b> perform arithmetic operations: half adder, full adder, half subtractor, full subtractor.</li>
<li><b>Data transmission circuits:</b> route or convert data: encoder, decoder, multiplexer, demultiplexer.</li>
</ul>
<p><i>Note:</i> A <b>sequential circuit</b> (Unit 5) also has memory, so its output depends on present inputs <b>and</b> past outputs.</p>""",
          """<p><b>Combinational circuit</b> એવો logic circuit છે જેના outputs કોઈ પણ ક્ષણે <b>માત્ર inputs ના હાલના combination</b> પર આધાર રાખે છે. તે માત્ર logic gates થી બને છે.</p>
<p>તેમાં <b>n input variables</b> અને <b>m output variables</b> હોય છે. દરેક 2<sup>n</sup> input combinations માટે એક નક્કી output combination હોય છે, તેથી તેને <b>truth table</b> અથવા m Boolean equations વડે પૂરેપૂરો વર્ણવી શકાય.</p>
<h4>લાક્ષણિકતાઓ</h4>
<ul>
<li>Output માત્ર હાલના inputs પર આધાર રાખે (અગાઉના inputs પર નહીં).</li>
<li>કોઈ memory element કે clock નથી.</li>
<li>Output થી input તરફ feedback path નથી.</li>
<li>Basic અને universal gates વડે બને છે.</li>
</ul>
<h4>વર્ગીકરણ</h4>
<ul>
<li><b>Arithmetic અને logical circuits:</b> arithmetic operations કરે: half adder, full adder, half subtractor, full subtractor.</li>
<li><b>Data transmission circuits:</b> data ને route કે convert કરે: encoder, decoder, multiplexer, demultiplexer.</li>
</ul>
<p><i>નોંધ:</i> <b>Sequential circuit</b> (Unit 5) માં memory પણ હોય છે, તેથી તેનો output હાલના inputs <b>અને</b> અગાઉના outputs પર આધાર રાખે છે.</p>""",
          diagram="de4_comb", key=True),

        T("4.1.2 Design Procedure of Combinational Circuits", "4.1.2 Combinational Circuits ની Design Procedure",
          """<p>Any combinational circuit is designed by the following steps:</p>
<ol>
<li><b>State the problem</b> (the specification of the circuit).</li>
<li>Find the <b>number of inputs and outputs</b> and assign a letter symbol to each.</li>
<li>Prepare the <b>truth table</b> showing the relation between inputs and outputs.</li>
<li>Write the <b>Boolean expression</b> (SOP / POS) for each output.</li>
<li><b>Simplify</b> each expression using a K-map or Boolean algebra.</li>
<li>Draw the <b>logic diagram</b> from the simplified expressions.</li>
<li><b>Verify</b> the design (truth table check, simulation or breadboard).</li>
</ol>
<p><b>Example:</b> For the half adder: 2 inputs (A, B), 2 outputs (Sum S, Carry C). From the truth table, S = Σm(1, 2) = A ⊕ B and C = Σm(3) = AB. So one XOR gate and one AND gate are needed.</p>""",
          """<p>કોઈ પણ combinational circuit નીચેના steps થી design થાય છે:</p>
<ol>
<li><b>Problem લખો</b> (circuit નું specification).</li>
<li><b>Inputs અને outputs ની સંખ્યા</b> નક્કી કરી દરેકને નામ (letter) આપો.</li>
<li>Inputs અને outputs વચ્ચેનો સંબંધ દર્શાવતું <b>truth table</b> બનાવો.</li>
<li>દરેક output નું <b>Boolean expression</b> (SOP / POS) લખો.</li>
<li>K-map અથવા Boolean algebra વડે દરેક expression <b>simplify</b> કરો.</li>
<li>Simplified expressions પરથી <b>logic diagram</b> દોરો.</li>
<li>Design <b>verify</b> કરો (truth table, simulation અથવા breadboard).</li>
</ol>
<p><b>ઉદાહરણ:</b> Half adder માટે: 2 inputs (A, B), 2 outputs (Sum S, Carry C). Truth table પરથી S = Σm(1, 2) = A ⊕ B અને C = Σm(3) = AB. તેથી એક XOR gate અને એક AND gate જોઈએ.</p>""",
          diagram="de4_design"),
    ],
}

SEC_4_2 = {
    "title": {"en": "4.2 Arithmetic Circuits: Adders and Subtractors", "gu": "4.2 Arithmetic Circuits: Adders અને Subtractors"},
    "items": [
        T("4.2.1 Half Adder: Block Diagram and Truth Table", "4.2.1 Half Adder: Block Diagram અને Truth Table",
          f"""<p>A <b>half adder</b> is a combinational circuit that <b>adds two 1-bit binary numbers</b> A and B. It has <b>2 inputs</b> (A, B) and <b>2 outputs</b>: <b>Sum (S)</b> and <b>Carry (C)</b>.</p>
<p>Binary addition rules: 0 + 0 = 0, 0 + 1 = 1, 1 + 0 = 1, 1 + 1 = 10 (sum 0, carry 1).</p>
<h4>Truth table</h4>{TT_HA}
<h4>Boolean expressions</h4>
<p>S = {B('!AB')} + {B('A!B')} = <b>A ⊕ B</b> &nbsp;&nbsp; (1 when inputs are different)</p>
<p>C = <b>AB</b> &nbsp;&nbsp; (1 only when both inputs are 1)</p>
<p>It is called a <i>half</i> adder because it cannot add a carry coming from a previous (lower) bit.</p>""",
          f"""<p><b>Half adder</b> એવો combinational circuit છે જે <b>બે 1-bit binary numbers</b> A અને B નો <b>સરવાળો</b> કરે છે. તેમાં <b>2 inputs</b> (A, B) અને <b>2 outputs</b>: <b>Sum (S)</b> અને <b>Carry (C)</b> હોય છે.</p>
<p>Binary addition ના નિયમો: 0 + 0 = 0, 0 + 1 = 1, 1 + 0 = 1, 1 + 1 = 10 (sum 0, carry 1).</p>
<h4>Truth table</h4>{TT_HA}
<h4>Boolean expressions</h4>
<p>S = {B('!AB')} + {B('A!B')} = <b>A ⊕ B</b> &nbsp;&nbsp; (inputs જુદા હોય ત્યારે 1)</p>
<p>C = <b>AB</b> &nbsp;&nbsp; (બંને inputs 1 હોય ત્યારે જ 1)</p>
<p>તેને <i>half</i> adder કહે છે કારણ કે તે અગાઉના (નીચલા) bit માંથી આવતો carry ઉમેરી શકતો નથી.</p>""",
          diagram="de4_ha", key=True),

        T("4.2.2 Half Adder: Logic Diagram", "4.2.2 Half Adder: Logic Diagram",
          f"""<p>From S = A ⊕ B and C = AB, the half adder needs:</p>
<ul><li>one <b>XOR gate</b> for the Sum (IC 7486), and</li><li>one <b>AND gate</b> for the Carry (IC 7408).</li></ul>
<p>Inputs A and B are given to both gates in parallel.</p>
<h4>Using basic gates only</h4>
<p>Since S = {B('!AB')} + {B('A!B')}, the XOR can be replaced by 2 NOT, 2 AND and 1 OR gate.</p>
<h4>Using NAND gates only</h4>
<p>A half adder can be built with <b>5 NAND gates</b>: 4 for the XOR (Sum) and 1 extra NAND used as an inverter after the first NAND to give the Carry (see the solved example).</p>
<p><b>Limitation:</b> no carry input, so it is used only for the LSB or as a building block of a full adder.</p>""",
          f"""<p>S = A ⊕ B અને C = AB પરથી half adder માટે જોઈએ:</p>
<ul><li>Sum માટે એક <b>XOR gate</b> (IC 7486), અને</li><li>Carry માટે એક <b>AND gate</b> (IC 7408).</li></ul>
<p>Inputs A અને B બંને gates ને parallel માં અપાય છે.</p>
<h4>માત્ર basic gates વડે</h4>
<p>S = {B('!AB')} + {B('A!B')} હોવાથી XOR ને બદલે 2 NOT, 2 AND અને 1 OR gate વાપરી શકાય.</p>
<h4>માત્ર NAND gates વડે</h4>
<p>Half adder <b>5 NAND gates</b> થી બને છે: XOR (Sum) માટે 4 અને Carry મેળવવા પહેલા NAND પછી inverter તરીકે 1 વધારાનો NAND (solved example જુઓ).</p>
<p><b>મર્યાદા:</b> carry input નથી, તેથી તે માત્ર LSB માટે અથવા full adder ના building block તરીકે વપરાય છે.</p>""",
          diagram="de4_ha_logic", examples=["de4n1"]),

        T("4.2.3 Full Adder: Block Diagram and Truth Table", "4.2.3 Full Adder: Block Diagram અને Truth Table",
          f"""<p>A <b>full adder</b> adds <b>three bits</b>: two significant bits A and B and the <b>carry-in (Cin)</b> from the previous stage. It has <b>3 inputs</b> (A, B, Cin) and <b>2 outputs</b>: <b>Sum (S)</b> and <b>Carry-out (Cout)</b>.</p>
<h4>Truth table</h4>{TT_FA}
<p>From the table:</p>
<p>S = Σm(1, 2, 4, 7) = {B('!A!B')}Cin + {B('!AB')}{NC} + {B('A!B')}{NC} + AB·Cin</p>
<p>Cout = Σm(3, 5, 6, 7) = {B('!AB')}Cin + {B('A!B')}Cin + AB{NC} + AB·Cin</p>
<p>S is 1 when an <b>odd number</b> of inputs are 1; Cout is 1 when <b>two or more</b> inputs are 1.</p>""",
          f"""<p><b>Full adder</b> <b>ત્રણ bits</b> નો સરવાળો કરે છે: બે significant bits A અને B તથા અગાઉના stage માંથી આવતો <b>carry-in (Cin)</b>. તેમાં <b>3 inputs</b> (A, B, Cin) અને <b>2 outputs</b>: <b>Sum (S)</b> અને <b>Carry-out (Cout)</b> હોય છે.</p>
<h4>Truth table</h4>{TT_FA}
<p>Table પરથી:</p>
<p>S = Σm(1, 2, 4, 7) = {B('!A!B')}Cin + {B('!AB')}{NC} + {B('A!B')}{NC} + AB·Cin</p>
<p>Cout = Σm(3, 5, 6, 7) = {B('!AB')}Cin + {B('A!B')}Cin + AB{NC} + AB·Cin</p>
<p><b>Odd number</b> of inputs 1 હોય ત્યારે S = 1; <b>બે કે વધુ</b> inputs 1 હોય ત્યારે Cout = 1.</p>""",
          diagram="de4_fa", examples=["de4n2"], key=True),

        T("4.2.4 Full Adder: K-map Simplification", "4.2.4 Full Adder: K-map Simplification",
          f"""<p><b>Sum:</b> In the K-map of S, the four 1s (m1, m2, m4, m7) are in a checkerboard pattern; no two are adjacent, so no grouping is possible. By algebra:</p>
<p>S = Cin({B('!A!B')} + AB) + {NC}({B('!AB')} + {B('A!B')}) = Cin·{B('!(A⊕B)')} + {NC}(A ⊕ B) = <b>A ⊕ B ⊕ Cin</b></p>
<p><b>Carry:</b> In the K-map of Cout, three pairs are formed around m7:</p>
<ul><li>m3, m7 → B·Cin</li><li>m5, m7 → A·Cin</li><li>m6, m7 → AB</li></ul>
<p><b>Cout = AB + B·Cin + A·Cin</b></p>
<p>This is the <b>majority function</b> of A, B and Cin.</p>""",
          f"""<p><b>Sum:</b> S ના K-map માં ચાર 1s (m1, m2, m4, m7) checkerboard pattern માં છે; કોઈ બે adjacent નથી, તેથી grouping શક્ય નથી. Algebra વડે:</p>
<p>S = Cin({B('!A!B')} + AB) + {NC}({B('!AB')} + {B('A!B')}) = Cin·{B('!(A⊕B)')} + {NC}(A ⊕ B) = <b>A ⊕ B ⊕ Cin</b></p>
<p><b>Carry:</b> Cout ના K-map માં m7 ની આસપાસ ત્રણ pairs બને છે:</p>
<ul><li>m3, m7 → B·Cin</li><li>m5, m7 → A·Cin</li><li>m6, m7 → AB</li></ul>
<p><b>Cout = AB + B·Cin + A·Cin</b></p>
<p>આ A, B અને Cin નું <b>majority function</b> છે.</p>""",
          diagram="de4_fa_kmap", examples=["de4n3"]),

        T("4.2.5 Full Adder: Logic Diagram", "4.2.5 Full Adder: Logic Diagram",
          """<p>From S = A ⊕ B ⊕ Cin and Cout = AB + B·Cin + A·Cin:</p>
<ul>
<li><b>Sum:</b> two 2-input XOR gates in cascade: the first gives A ⊕ B, the second XORs it with Cin.</li>
<li><b>Carry:</b> three 2-input AND gates (AB, B·Cin, A·Cin) followed by one 3-input OR gate.</li>
</ul>
<p>Total: 2 XOR + 3 AND + 1 OR gates.</p>
<h4>Parallel (ripple-carry) adder</h4>
<p>To add two n-bit numbers, n full adders are connected in cascade: the Cout of each stage goes to the Cin of the next higher stage. The Cin of the LSB stage is 0 (or a half adder is used for it). The final Cout is the carry of the result. Because the carry "ripples" from stage to stage, it is called a <b>ripple-carry adder</b> (e.g. IC 7483, a 4-bit adder).</p>""",
          """<p>S = A ⊕ B ⊕ Cin અને Cout = AB + B·Cin + A·Cin પરથી:</p>
<ul>
<li><b>Sum:</b> cascade માં બે 2-input XOR gates: પહેલો A ⊕ B આપે, બીજો તેને Cin સાથે XOR કરે.</li>
<li><b>Carry:</b> ત્રણ 2-input AND gates (AB, B·Cin, A·Cin) અને પછી એક 3-input OR gate.</li>
</ul>
<p>કુલ: 2 XOR + 3 AND + 1 OR gates.</p>
<h4>Parallel (ripple-carry) adder</h4>
<p>બે n-bit numbers ઉમેરવા n full adders ને cascade માં જોડાય છે: દરેક stage નો Cout પછીના ઉપલા stage ના Cin માં જાય છે. LSB stage નો Cin = 0 (અથવા ત્યાં half adder વપરાય). છેલ્લો Cout પરિણામનો carry છે. Carry એક stage થી બીજા stage માં "ripple" થાય છે, તેથી તેને <b>ripple-carry adder</b> કહે છે (દા.ત. IC 7483, 4-bit adder).</p>""",
          diagram="de4_fa_logic", examples=["de4n4"]),

        T("4.2.6 Full Adder using Two Half Adders", "4.2.6 બે Half Adders વડે Full Adder",
          f"""<p>A full adder can be built from <b>two half adders and one OR gate</b>:</p>
<ol>
<li><b>HA1</b> adds A and B: S1 = A ⊕ B, C1 = AB.</li>
<li><b>HA2</b> adds S1 and Cin: S = S1 ⊕ Cin = A ⊕ B ⊕ Cin, C2 = (A ⊕ B)·Cin.</li>
<li>An <b>OR gate</b> combines the carries: Cout = C1 + C2 = AB + (A ⊕ B)·Cin.</li>
</ol>
<p><b>Proof that it equals AB + B·Cin + A·Cin:</b></p>
<p>AB + (A ⊕ B)Cin = AB + {B('A!B')}Cin + {B('!AB')}Cin = AB(1 + Cin) + {B('A!B')}Cin + {B('!AB')}Cin = AB + ABCin + {B('A!B')}Cin + ABCin + {B('!AB')}Cin = AB + ACin(B + {B('!B')}) + BCin(A + {B('!A')}) = <b>AB + A·Cin + B·Cin</b></p>""",
          f"""<p>Full adder <b>બે half adders અને એક OR gate</b> વડે બનાવી શકાય:</p>
<ol>
<li><b>HA1</b> A અને B ઉમેરે: S1 = A ⊕ B, C1 = AB.</li>
<li><b>HA2</b> S1 અને Cin ઉમેરે: S = S1 ⊕ Cin = A ⊕ B ⊕ Cin, C2 = (A ⊕ B)·Cin.</li>
<li><b>OR gate</b> બંને carries જોડે: Cout = C1 + C2 = AB + (A ⊕ B)·Cin.</li>
</ol>
<p><b>તે AB + B·Cin + A·Cin બરાબર છે તેની સાબિતી:</b></p>
<p>AB + (A ⊕ B)Cin = AB + {B('A!B')}Cin + {B('!AB')}Cin = AB(1 + Cin) + {B('A!B')}Cin + {B('!AB')}Cin = AB + ABCin + {B('A!B')}Cin + ABCin + {B('!AB')}Cin = AB + ACin(B + {B('!B')}) + BCin(A + {B('!A')}) = <b>AB + A·Cin + B·Cin</b></p>""",
          diagram="de4_fa_2ha", examples=["de4n5"]),

        T("4.2.7 Half Subtractor", "4.2.7 Half Subtractor",
          f"""<p>A <b>half subtractor</b> subtracts one bit from another (A − B). It has <b>2 inputs</b> (A = minuend, B = subtrahend) and <b>2 outputs</b>: <b>Difference (D)</b> and <b>Borrow (Bo)</b>.</p>
<p>Binary subtraction rules: 0 − 0 = 0, 1 − 0 = 1, 1 − 1 = 0, 0 − 1 = 1 with borrow 1.</p>
<h4>Truth table</h4>{TT_HS}
<h4>Boolean expressions</h4>
<p>D = {B('!AB')} + {B('A!B')} = <b>A ⊕ B</b> &nbsp;&nbsp; (same as the sum of a half adder)</p>
<p>Bo = <b>{B('!AB')}</b> &nbsp;&nbsp; (borrow only when A = 0 and B = 1)</p>
<h4>Logic diagram</h4>
<p>One XOR gate for D, and one NOT gate + one AND gate for Bo.</p>
<p><b>Difference from half adder:</b> only the second output changes: Carry = AB but Borrow = {B('!AB')}.</p>""",
          f"""<p><b>Half subtractor</b> એક bit માંથી બીજો bit બાદ કરે છે (A − B). તેમાં <b>2 inputs</b> (A = minuend, B = subtrahend) અને <b>2 outputs</b>: <b>Difference (D)</b> અને <b>Borrow (Bo)</b> હોય છે.</p>
<p>Binary subtraction ના નિયમો: 0 − 0 = 0, 1 − 0 = 1, 1 − 1 = 0, 0 − 1 = 1 અને borrow 1.</p>
<h4>Truth table</h4>{TT_HS}
<h4>Boolean expressions</h4>
<p>D = {B('!AB')} + {B('A!B')} = <b>A ⊕ B</b> &nbsp;&nbsp; (half adder ના sum જેવું જ)</p>
<p>Bo = <b>{B('!AB')}</b> &nbsp;&nbsp; (A = 0 અને B = 1 હોય ત્યારે જ borrow)</p>
<h4>Logic diagram</h4>
<p>D માટે એક XOR gate, અને Bo માટે એક NOT gate + એક AND gate.</p>
<p><b>Half adder થી તફાવત:</b> માત્ર બીજો output બદલાય છે: Carry = AB પણ Borrow = {B('!AB')}.</p>""",
          diagram="de4_hs", examples=["de4n6"], key=True),

        T("4.2.8 Full Subtractor: Block Diagram and Truth Table", "4.2.8 Full Subtractor: Block Diagram અને Truth Table",
          f"""<p>A <b>full subtractor</b> subtracts two bits while also taking the <b>borrow-in (Bin)</b> from the previous (lower) stage: it computes A − B − Bin. It has <b>3 inputs</b> (A, B, Bin) and <b>2 outputs</b>: <b>Difference (D)</b> and <b>Borrow-out (Bout)</b>.</p>
<h4>Truth table</h4>{TT_FS}
<p>Example row: A = 0, B = 1, Bin = 1 → 0 − 1 − 1: borrow 1 from the next bit (value 2), 2 − 1 − 1 = 0 → D = 0, Bout = 1.</p>
<p>D = Σm(1, 2, 4, 7) (same as full-adder sum)</p>
<p>Bout = Σm(1, 2, 3, 7)</p>""",
          f"""<p><b>Full subtractor</b> બે bits ની બાદબાકી કરે છે અને સાથે અગાઉના (નીચલા) stage નો <b>borrow-in (Bin)</b> પણ લે છે: તે A − B − Bin ગણે છે. તેમાં <b>3 inputs</b> (A, B, Bin) અને <b>2 outputs</b>: <b>Difference (D)</b> અને <b>Borrow-out (Bout)</b> હોય છે.</p>
<h4>Truth table</h4>{TT_FS}
<p>ઉદાહરણ row: A = 0, B = 1, Bin = 1 → 0 − 1 − 1: આગળના bit માંથી borrow 1 (કિંમત 2), 2 − 1 − 1 = 0 → D = 0, Bout = 1.</p>
<p>D = Σm(1, 2, 4, 7) (full-adder sum જેવું જ)</p>
<p>Bout = Σm(1, 2, 3, 7)</p>""",
          diagram="de4_fs", examples=["de4n7"], key=True),

        T("4.2.9 Full Subtractor: K-map and Logic Diagram", "4.2.9 Full Subtractor: K-map અને Logic Diagram",
          f"""<p><b>Difference:</b> the 1s of D are in a checkerboard pattern (like the full-adder sum), so <b>D = A ⊕ B ⊕ Bin</b>.</p>
<p><b>Borrow:</b> in the K-map of Bout three pairs are formed:</p>
<ul><li>m2, m3 → {B('!AB')}</li><li>m1, m3 → {B('!A')}·Bin</li><li>m3, m7 → B·Bin</li></ul>
<p><b>Bout = {B('!AB')} + {B('!A')}·Bin + B·Bin</b></p>
<h4>Logic diagram</h4>
<ul><li>D: two XOR gates in cascade.</li><li>Bout: one NOT gate (for {B('!A')}), three 2-input AND gates and one 3-input OR gate.</li></ul>
<p>A full subtractor can also be made from <b>two half subtractors and one OR gate</b>: Bout = Bo1 + Bo2.</p>""",
          f"""<p><b>Difference:</b> D ના 1s checkerboard pattern માં છે (full-adder sum જેવા), તેથી <b>D = A ⊕ B ⊕ Bin</b>.</p>
<p><b>Borrow:</b> Bout ના K-map માં ત્રણ pairs બને છે:</p>
<ul><li>m2, m3 → {B('!AB')}</li><li>m1, m3 → {B('!A')}·Bin</li><li>m3, m7 → B·Bin</li></ul>
<p><b>Bout = {B('!AB')} + {B('!A')}·Bin + B·Bin</b></p>
<h4>Logic diagram</h4>
<ul><li>D: cascade માં બે XOR gates.</li><li>Bout: એક NOT gate ({B('!A')} માટે), ત્રણ 2-input AND gates અને એક 3-input OR gate.</li></ul>
<p>Full subtractor <b>બે half subtractors અને એક OR gate</b> વડે પણ બને: Bout = Bo1 + Bo2.</p>""",
          diagram="de4_fs_logic", examples=["de4n8"]),

        T("4.2.10 Comparison of Adders and Subtractors", "4.2.10 Adders અને Subtractors ની સરખામણી",
          f"""<table><tr><th>Circuit</th><th>Inputs</th><th>Outputs</th><th>Equations</th></tr>
<tr><td>Half adder</td><td>A, B</td><td>S, C</td><td>S = A⊕B, C = AB</td></tr>
<tr><td>Full adder</td><td>A, B, Cin</td><td>S, Cout</td><td>S = A⊕B⊕Cin, Cout = AB + B·Cin + A·Cin</td></tr>
<tr><td>Half subtractor</td><td>A, B</td><td>D, Bo</td><td>D = A⊕B, Bo = {B('!AB')}</td></tr>
<tr><td>Full subtractor</td><td>A, B, Bin</td><td>D, Bout</td><td>D = A⊕B⊕Bin, Bout = {B('!AB')} + {B('!A')}·Bin + B·Bin</td></tr></table>
<ul>
<li>Sum and Difference have the <b>same</b> equation; only the carry/borrow differs.</li>
<li>Half circuits cannot accept a carry/borrow from a previous stage; full circuits can.</li>
<li>A full adder/subtractor = 2 half circuits + 1 OR gate.</li>
<li>In practice subtraction is often done by an adder using <b>2's complement</b> (A − B = A + 2's complement of B).</li>
</ul>""",
          f"""<table><tr><th>Circuit</th><th>Inputs</th><th>Outputs</th><th>Equations</th></tr>
<tr><td>Half adder</td><td>A, B</td><td>S, C</td><td>S = A⊕B, C = AB</td></tr>
<tr><td>Full adder</td><td>A, B, Cin</td><td>S, Cout</td><td>S = A⊕B⊕Cin, Cout = AB + B·Cin + A·Cin</td></tr>
<tr><td>Half subtractor</td><td>A, B</td><td>D, Bo</td><td>D = A⊕B, Bo = {B('!AB')}</td></tr>
<tr><td>Full subtractor</td><td>A, B, Bin</td><td>D, Bout</td><td>D = A⊕B⊕Bin, Bout = {B('!AB')} + {B('!A')}·Bin + B·Bin</td></tr></table>
<ul>
<li>Sum અને Difference નું equation <b>સરખું</b> છે; માત્ર carry/borrow અલગ છે.</li>
<li>Half circuits અગાઉના stage નો carry/borrow લઈ શકતા નથી; full circuits લઈ શકે છે.</li>
<li>Full adder/subtractor = 2 half circuits + 1 OR gate.</li>
<li>વ્યવહારમાં subtraction ઘણી વાર adder વડે <b>2's complement</b> થી થાય છે (A − B = A + B નો 2's complement).</li>
</ul>"""),
    ],
}

NOTES_A = [SEC_4_1, SEC_4_2]
