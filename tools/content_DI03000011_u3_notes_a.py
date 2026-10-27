"""Digital Electronics Fundamentals (DI03000011) - Unit 3 notes, part A: 3.1 Need for simplification, 3.2 K-map method."""
from content_DI03000011_u1_notes_a import T
from content_DI03000011_u3_common import solve, B
from diagrams_DI03000011_u3 import EX3, EX4, EXPOS

E3_EN, E3_GU, _, A3 = solve(*EX3)
E4_EN, E4_GU, _, A4 = solve(*EX4)
EP_EN, EP_GU, _, AP = solve(*EXPOS, pos=True)
assert (A3, A4) == ("C + AB", "!C + !A!D + B!D")

SEC_3_1 = {
    "title": {"en": "3.1 Need for Simplification", "gu": "3.1 Simplification ની જરૂરિયાત"},
    "items": [
        T("3.1.1 Need for Simplification and Methods", "3.1.1 Simplification ની જરૂરિયાત અને Methods",
          f"""<p>A Boolean function obtained from a truth table (canonical SOP or POS) usually has many terms. Each term needs a gate, so the circuit becomes large. <b>Simplification</b> reduces the expression to the minimum number of terms and literals <b>without changing its truth table</b>.</p>
<h4>Advantages of a simplified circuit</h4>
<ul>
<li><b>Fewer gates and ICs</b>: lower cost</li>
<li><b>Less wiring</b>: smaller size, easier to build and troubleshoot</li>
<li><b>Less propagation delay</b>: higher speed</li>
<li><b>Less power</b> consumption and heat</li>
<li><b>Higher reliability</b> (fewer components can fail)</li>
</ul>
<h4>Methods of simplification</h4>
<ol>
<li><b>Algebraic method</b> (Boolean laws, Unit 2): no fixed procedure; depends on skill and it is hard to know whether the result is minimum.</li>
<li><b>Karnaugh map (K-map) method</b>: a graphical, systematic method; best for 2 to 4 (up to 6) variables.</li>
<li><b>Quine–McCluskey (tabular) method</b>: suitable for many variables and for computer programs.</li>
</ol>
<p><b>Example:</b> Y = {B('!A!BC')} + {B('!ABC')} + {B('A!BC')} + ABC needs 4 AND, 1 OR and 2 NOT gates. With a K-map it reduces to <b>Y = C</b>, which needs no gate at all.</p>""",
          f"""<p>Truth table પરથી મળતું Boolean function (canonical SOP કે POS) સામાન્ય રીતે ઘણા terms ધરાવે છે. દરેક term માટે gate જોઈએ, તેથી circuit મોટો બને છે. <b>Simplification</b> એટલે expression ને <b>truth table બદલ્યા વગર</b> ઓછામાં ઓછા terms અને literals માં લાવવું.</p>
<h4>Simplified circuit ના ફાયદા</h4>
<ul>
<li><b>ઓછા gates અને ICs</b>: ઓછી cost</li>
<li><b>ઓછું wiring</b>: નાનું size, બનાવવામાં અને troubleshoot કરવામાં સરળ</li>
<li><b>ઓછો propagation delay</b>: વધુ speed</li>
<li><b>ઓછો power</b> વપરાશ અને ગરમી</li>
<li><b>વધુ reliability</b> (ઓછા components ખરાબ થઈ શકે)</li>
</ul>
<h4>Simplification ની methods</h4>
<ol>
<li><b>Algebraic method</b> (Boolean laws, Unit 2): નિશ્ચિત પદ્ધતિ નથી; આવડત પર આધાર રાખે અને જવાબ minimum છે કે નહીં તે જાણવું અઘરું.</li>
<li><b>Karnaugh map (K-map) method</b>: graphical અને systematic method; 2 થી 4 (6 સુધી) variables માટે શ્રેષ્ઠ.</li>
<li><b>Quine–McCluskey (tabular) method</b>: ઘણા variables અને computer programs માટે યોગ્ય.</li>
</ol>
<p><b>ઉદાહરણ:</b> Y = {B('!A!BC')} + {B('!ABC')} + {B('A!BC')} + ABC માટે 4 AND, 1 OR અને 2 NOT gates જોઈએ. K-map વડે તે <b>Y = C</b> બને છે, જેમાં કોઈ gate જોઈતો નથી.</p>""",
          diagram="de3_need", key=True),
    ],
}

SEC_3_2 = {
    "title": {"en": "3.2 Karnaugh Map (K-map) Method", "gu": "3.2 Karnaugh Map (K-map) Method"},
    "items": [
        T("3.2.1 K-map and Two-Variable K-map", "3.2.1 K-map અને Two-Variable K-map",
          f"""<p>A <b>Karnaugh map</b> (introduced by Maurice Karnaugh, 1953) is a <b>diagram of squares (cells)</b>, one cell for each minterm of the function. For n variables it has <b>2<sup>n</sup> cells</b>.</p>
<p>The cells are arranged so that <b>adjacent cells differ in only one variable</b> (Gray code order). Grouping adjacent 1s therefore removes the variable that changes, using the law A + {B('!A')} = 1.</p>
<h4>Two-variable K-map</h4>
<ul>
<li>4 cells: rows for A (0, 1), columns for B (0, 1).</li>
<li>Cells: m0 = {B('!A!B')}, m1 = {B('!A')}B, m2 = A{B('!B')}, m3 = AB.</li>
</ul>
<p><b>Example:</b> Y = Σm(1, 2, 3). Plot 1s in cells 1, 2, 3. Group the right column (m1, m3): A changes, B = 1 → <b>B</b>. Group the bottom row (m2, m3): <b>A</b>. Cell m3 may be used twice.</p>
<p><b>Y = A + B</b> (an OR gate). Check: {B('!A')}B + A{B('!B')} + AB = A + B ✓</p>""",
          f"""<p><b>Karnaugh map</b> (Maurice Karnaugh, 1953) એ <b>ચોરસ (cells) ની આકૃતિ</b> છે, function ના દરેક minterm માટે એક cell. n variables માટે <b>2<sup>n</sup> cells</b> હોય છે.</p>
<p>Cells એવી રીતે ગોઠવાય છે કે <b>બાજુ-બાજુના cells માં માત્ર એક જ variable બદલાય</b> (Gray code ક્રમ). તેથી પાસ-પાસેના 1s નો group બનાવવાથી A + {B('!A')} = 1 નિયમ મુજબ બદલાતો variable દૂર થાય છે.</p>
<h4>Two-variable K-map</h4>
<ul>
<li>4 cells: A માટે rows (0, 1), B માટે columns (0, 1).</li>
<li>Cells: m0 = {B('!A!B')}, m1 = {B('!A')}B, m2 = A{B('!B')}, m3 = AB.</li>
</ul>
<p><b>ઉદાહરણ:</b> Y = Σm(1, 2, 3). Cells 1, 2, 3 માં 1 લખો. જમણો column (m1, m3) group કરો: A બદલાય, B = 1 → <b>B</b>. નીચેની row (m2, m3) group કરો: <b>A</b>. Cell m3 બે વાર વાપરી શકાય.</p>
<p><b>Y = A + B</b> (OR gate). ચકાસણી: {B('!A')}B + A{B('!B')} + AB = A + B ✓</p>""",
          diagram="de3_kmap2", examples=["de3n1"], key=True),

        T("3.2.2 Three-Variable K-map", "3.2.2 Three-Variable K-map",
          """<ul>
<li><b>8 cells</b> (2<sup>3</sup>). Usually A is written on the rows (0, 1) and BC on the columns.</li>
<li>Columns are in <b>Gray code order: 00, 01, 11, 10</b>. Hence the cell order in a row is m0, m1, m3, m2 and m4, m5, m7, m6.</li>
<li>The <b>left-most and right-most columns are adjacent</b> (the map is like a cylinder), e.g. m0 and m2, m4 and m6.</li>
</ul>
<h4>Groups in a 3-variable map</h4>
<table><tr><th>Group</th><th>Variables eliminated</th><th>Literals in term</th></tr>
<tr><td>1 cell</td><td>0</td><td>3</td></tr><tr><td>Pair (2)</td><td>1</td><td>2</td></tr>
<tr><td>Quad (4)</td><td>2</td><td>1</td></tr><tr><td>All 8</td><td>3</td><td>Y = 1</td></tr></table>
<p><b>Why Gray code?</b> In binary order (00, 01, 10, 11) the cells 01 and 10 would be neighbours but differ in two bits, so they could not be combined.</p>""",
          """<ul>
<li><b>8 cells</b> (2<sup>3</sup>). સામાન્ય રીતે A rows (0, 1) પર અને BC columns પર લખાય છે.</li>
<li>Columns <b>Gray code ક્રમમાં: 00, 01, 11, 10</b> હોય છે. તેથી row માં cells નો ક્રમ m0, m1, m3, m2 અને m4, m5, m7, m6 છે.</li>
<li><b>સૌથી ડાબો અને સૌથી જમણો column adjacent છે</b> (map cylinder જેવો છે), દા.ત. m0 અને m2, m4 અને m6.</li>
</ul>
<h4>3-variable map માં groups</h4>
<table><tr><th>Group</th><th>દૂર થતા variables</th><th>Term માં literals</th></tr>
<tr><td>1 cell</td><td>0</td><td>3</td></tr><tr><td>Pair (2)</td><td>1</td><td>2</td></tr>
<tr><td>Quad (4)</td><td>2</td><td>1</td></tr><tr><td>બધા 8</td><td>3</td><td>Y = 1</td></tr></table>
<p><b>Gray code કેમ?</b> Binary ક્રમ (00, 01, 10, 11) માં 01 અને 10 cells બાજુ-બાજુમાં આવે પણ બે bits માં જુદા પડે, તેથી તેમને જોડી ન શકાય.</p>""",
          diagram="de3_kmap3", examples=["de3n2", "de3n3"], key=True),

        T("3.2.3 Four-Variable K-map", "3.2.3 Four-Variable K-map",
          """<ul>
<li><b>16 cells</b> (2<sup>4</sup>). Rows: AB = 00, 01, 11, 10. Columns: CD = 00, 01, 11, 10 (both in Gray code).</li>
<li>Cell order by rows: 0 1 3 2 / 4 5 7 6 / 12 13 15 14 / 8 9 11 10.</li>
<li><b>Adjacency:</b> left and right edges are adjacent, top and bottom edges are adjacent, and the <b>four corners</b> (m0, m2, m8, m10) form one group.</li>
</ul>
<table><tr><th>Group</th><th>Variables eliminated</th><th>Literals in term</th></tr>
<tr><td>1 cell</td><td>0</td><td>4</td></tr><tr><td>Pair (2)</td><td>1</td><td>3</td></tr>
<tr><td>Quad (4)</td><td>2</td><td>2</td></tr><tr><td>Octet (8)</td><td>3</td><td>1</td></tr><tr><td>All 16</td><td>4</td><td>Y = 1</td></tr></table>
<p><b>Rule:</b> a group of 2<sup>k</sup> cells eliminates k variables.</p>""",
          """<ul>
<li><b>16 cells</b> (2<sup>4</sup>). Rows: AB = 00, 01, 11, 10. Columns: CD = 00, 01, 11, 10 (બંને Gray code માં).</li>
<li>Rows મુજબ cells નો ક્રમ: 0 1 3 2 / 4 5 7 6 / 12 13 15 14 / 8 9 11 10.</li>
<li><b>Adjacency:</b> ડાબી અને જમણી ધાર adjacent, ઉપરની અને નીચેની ધાર adjacent, અને <b>ચાર ખૂણા</b> (m0, m2, m8, m10) એક group બનાવે છે.</li>
</ul>
<table><tr><th>Group</th><th>દૂર થતા variables</th><th>Term માં literals</th></tr>
<tr><td>1 cell</td><td>0</td><td>4</td></tr><tr><td>Pair (2)</td><td>1</td><td>3</td></tr>
<tr><td>Quad (4)</td><td>2</td><td>2</td></tr><tr><td>Octet (8)</td><td>3</td><td>1</td></tr><tr><td>બધા 16</td><td>4</td><td>Y = 1</td></tr></table>
<p><b>નિયમ:</b> 2<sup>k</sup> cells નો group k variables દૂર કરે છે.</p>""",
          diagram="de3_kmap4", key=True),

        T("3.2.4 Rules for Grouping", "3.2.4 Grouping ના નિયમો",
          """<ol>
<li>Group only <b>adjacent</b> cells containing 1 (horizontally or vertically, <b>not diagonally</b>).</li>
<li>The number of cells in a group must be a <b>power of 2</b>: 1, 2, 4, 8, 16. A group of 3 or 6 is not allowed.</li>
<li>Groups must be <b>rectangles</b> (including wrap-around across edges and the four corners).</li>
<li>Make each group <b>as large as possible</b> (larger group → fewer literals).</li>
<li>Use the <b>fewest groups</b> that cover all 1s (fewer groups → fewer terms).</li>
<li>A 1 may be used in <b>more than one group</b> (overlapping is allowed) if it makes a group larger.</li>
<li>Every 1 must be in at least one group. Do not make a group whose 1s are all already covered (a <b>redundant group</b>).</li>
<li>Start with 1s that can be grouped in <b>only one way</b> (these give essential prime implicants).</li>
</ol>
<h4>Writing the term of a group</h4>
<p>Look at the row and column labels of the group. A variable that <b>changes</b> inside the group is dropped. A variable that stays <b>1</b> is written as it is; one that stays <b>0</b> is written complemented.</p>
<h4>Implicant terms</h4>
<ul>
<li><b>Implicant:</b> any group of 1s (a product term that implies the function).</li>
<li><b>Prime implicant (PI):</b> a group that cannot be made larger.</li>
<li><b>Essential prime implicant (EPI):</b> a PI that covers at least one 1 that no other PI covers. All EPIs must appear in the answer.</li>
</ul>""",
          """<ol>
<li>માત્ર <b>adjacent</b> (પાસ-પાસેના) 1 વાળા cells નો જ group બનાવો (આડા કે ઊભા, <b>ત્રાંસા નહીં</b>).</li>
<li>Group માં cells ની સંખ્યા <b>2 ની ઘાત</b> હોવી જોઈએ: 1, 2, 4, 8, 16. 3 કે 6 નો group ન ચાલે.</li>
<li>Groups <b>લંબચોરસ (rectangle)</b> હોવા જોઈએ (ધાર પારના wrap-around અને ચાર ખૂણા સહિત).</li>
<li>દરેક group <b>શક્ય તેટલો મોટો</b> બનાવો (મોટો group → ઓછા literals).</li>
<li>બધા 1s ને આવરી લેતા <b>ઓછામાં ઓછા groups</b> વાપરો (ઓછા groups → ઓછા terms).</li>
<li>Group મોટો થતો હોય તો એક 1 ને <b>એકથી વધુ groups</b> માં વાપરી શકાય (overlapping ચાલે).</li>
<li>દરેક 1 ઓછામાં ઓછા એક group માં હોવો જોઈએ. જેના બધા 1s પહેલેથી આવરાઈ ગયા હોય એવો group (<b>redundant group</b>) ન બનાવો.</li>
<li>જે 1s ને <b>માત્ર એક જ રીતે</b> group કરી શકાય ત્યાંથી શરૂઆત કરો (તે essential prime implicants આપે છે).</li>
</ol>
<h4>Group નો term લખવો</h4>
<p>Group ના row અને column labels જુઓ. Group માં જે variable <b>બદલાય</b> તે દૂર થાય. જે <b>1</b> રહે તે સીધો લખાય; જે <b>0</b> રહે તે complement સાથે લખાય.</p>
<h4>Implicant terms</h4>
<ul>
<li><b>Implicant:</b> 1s નો કોઈ પણ group (function ને imply કરતો product term).</li>
<li><b>Prime implicant (PI):</b> જેને વધુ મોટો ન કરી શકાય એવો group.</li>
<li><b>Essential prime implicant (EPI):</b> એવો PI જે ઓછામાં ઓછો એક એવો 1 આવરે જેને બીજો કોઈ PI ન આવરે. બધા EPIs જવાબમાં હોવા જ જોઈએ.</li>
</ul>""",
          diagram="de3_groups", key=True),

        T("3.2.5 Steps of K-map Simplification", "3.2.5 K-map Simplification ના Steps",
          """<ol>
<li>Draw a K-map with 2<sup>n</sup> cells and label rows and columns in Gray code.</li>
<li>Write <b>1</b> in the cells of the given minterms (and X for don't-cares); the other cells are 0 (may be left blank).</li>
<li>Look for <b>octets</b>, then <b>quads</b>, then <b>pairs</b>, then single 1s that cannot be combined.</li>
<li>Check that every 1 is covered with the minimum number of largest groups; remove redundant groups.</li>
<li>Write the product term for each group.</li>
<li>OR all terms to get the minimal SOP expression.</li>
<li>Draw the logic diagram (AND-OR or NAND-NAND).</li>
</ol>
<p><b>If the function is given as an expression</b> (not as minterms), first convert each term to minterms (or plot each term directly: e.g. in a 3-variable map the term A{} covers the whole A = 1 row).</p>""".replace("A{}", "A"),
          """<ol>
<li>2<sup>n</sup> cells વાળો K-map દોરો અને rows તથા columns ને Gray code માં label કરો.</li>
<li>આપેલા minterms ના cells માં <b>1</b> લખો (અને don't-cares માટે X); બાકીના cells 0 છે (ખાલી રાખી શકાય).</li>
<li>પહેલાં <b>octets</b>, પછી <b>quads</b>, પછી <b>pairs</b>, પછી જોડી ન શકાય તેવા એકલા 1s શોધો.</li>
<li>દરેક 1 ઓછામાં ઓછા અને મોટામાં મોટા groups વડે આવરાય છે તે ચકાસો; redundant groups દૂર કરો.</li>
<li>દરેક group નો product term લખો.</li>
<li>બધા terms નો OR કરી minimal SOP expression મેળવો.</li>
<li>Logic diagram દોરો (AND-OR અથવા NAND-NAND).</li>
</ol>
<p><b>Function expression તરીકે આપ્યું હોય</b> (minterms નહીં) તો પહેલાં દરેક term ને minterms માં ફેરવો (અથવા term સીધો plot કરો: દા.ત. 3-variable map માં term A આખી A = 1 row આવરે છે).</p>""",
          diagram="de3_steps", examples=["de3n12"]),

        T("3.2.6 Solved Example: Three-Variable K-map", "3.2.6 Solved Example: Three-Variable K-map",
          "<p><b>Simplify Y = Σm(1, 3, 5, 6, 7) using a K-map.</b></p>" + E3_EN
          + "<p>The quad (m1, m3, m5, m7) is the whole C = 1 area. The pair (m6, m7) shares m7 with the quad; overlapping is allowed.</p>",
          "<p><b>K-map વડે Y = Σm(1, 3, 5, 6, 7) simplify કરો.</b></p>" + E3_GU
          + "<p>Quad (m1, m3, m5, m7) આખો C = 1 વિસ્તાર છે. Pair (m6, m7) quad સાથે m7 વહેંચે છે; overlapping ચાલે છે.</p>",
          diagram="de3_ex3", examples=["de3n4"], key=True),

        T("3.2.7 Solved Example: Four-Variable K-map", "3.2.7 Solved Example: Four-Variable K-map",
          "<p><b>Simplify Y = Σm(0, 1, 2, 4, 5, 6, 8, 9, 12, 13, 14) using a K-map.</b></p>" + E4_EN
          + "<p>The octet uses the two left columns (C = 0). The quad " + B("!A!D") + " wraps from the left edge to the right edge.</p>"
            "<p>Original function: 11 minterms (11 four-input AND gates). Simplified: 2 AND + 1 OR + 3 NOT gates.</p>",
          "<p><b>K-map વડે Y = Σm(0, 1, 2, 4, 5, 6, 8, 9, 12, 13, 14) simplify કરો.</b></p>" + E4_GU
          + "<p>Octet ડાબા બે columns (C = 0) વાપરે છે. Quad " + B("!A!D") + " ડાબી ધારથી જમણી ધાર સુધી wrap થાય છે.</p>"
            "<p>મૂળ function: 11 minterms (11 four-input AND gates). Simplified: 2 AND + 1 OR + 3 NOT gates.</p>",
          diagram="de3_ex4", examples=["de3n5", "de3n6", "de3n7", "de3n8"], key=True),

        T("3.2.8 POS Simplification using K-map", "3.2.8 K-map વડે POS Simplification",
          f"""<p>To get the minimal <b>Product of Sums</b>:</p>
<ol>
<li>Plot the function; write <b>0</b> in the cells where Y = 0 (maxterms).</li>
<li><b>Group the 0s</b> using the same rules as for 1s.</li>
<li>For each group write a <b>sum term</b>: a variable that stays <b>0</b> is written as it is, one that stays <b>1</b> is written <b>complemented</b> (opposite of SOP).</li>
<li>AND all sum terms.</li>
</ol>
<p>(Grouping 0s gives {B('!Y')} in SOP form; applying De Morgan gives Y in POS form.)</p>
<p><b>Example:</b> Y = Σm(0, 1, 2, 5, 8, 9, 10) in POS form:</p>""" + EP_EN
          + f"<p>For comparison, the minimal SOP is Y = {B('!B!C')} + {B('!B!D')} + {B('!A!CD')}. Choose the form with fewer gates.</p>",
          f"""<p>Minimal <b>Product of Sums</b> મેળવવા:</p>
<ol>
<li>Function plot કરો; જ્યાં Y = 0 હોય ત્યાં (maxterms) <b>0</b> લખો.</li>
<li>1s ના જ નિયમો વડે <b>0s ના groups</b> બનાવો.</li>
<li>દરેક group માટે <b>sum term</b> લખો: જે variable <b>0</b> રહે તે સીધો, જે <b>1</b> રહે તે <b>complement</b> સાથે લખાય (SOP થી ઉલટું).</li>
<li>બધા sum terms નો AND કરો.</li>
</ol>
<p>(0s group કરવાથી {B('!Y')} SOP સ્વરૂપમાં મળે; De Morgan લગાવવાથી Y POS સ્વરૂપમાં મળે.)</p>
<p><b>ઉદાહરણ:</b> Y = Σm(0, 1, 2, 5, 8, 9, 10) POS સ્વરૂપમાં:</p>""" + EP_GU
          + f"<p>સરખામણી માટે, minimal SOP Y = {B('!B!C')} + {B('!B!D')} + {B('!A!CD')} છે. ઓછા gates વાળું સ્વરૂપ પસંદ કરો.</p>",
          diagram="de3_pos", examples=["de3n11"]),
    ],
}

NOTES_A = [SEC_3_1, SEC_3_2]
