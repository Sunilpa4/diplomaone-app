"""Digital Electronics Fundamentals (DI03000011) - Unit 3 notes, part B: 3.3 Don't-care conditions, 3.4 Implementation."""
from content_DI03000011_u1_notes_a import T
from content_DI03000011_u3_common import solve, B
from diagrams_DI03000011_u3 import EXDC, EXBCD, EX4
import de_kmap as K

D_EN, D_GU, _, AD = solve(*EXDC)
BC_EN, BC_GU, _, ABC_ = solve(*EXBCD)
assert (AD, ABC_) == ("!A!B + CD", "A + BD + BC")
G4 = K.minimise(*EX4)

SEC_3_3 = {
    "title": {"en": "3.3 K-map with Don't-Care Conditions", "gu": "3.3 Don't-Care Conditions સાથે K-map"},
    "items": [
        T("3.3.1 Don't-Care Conditions", "3.3.1 Don't-Care Conditions",
          f"""<p>In some circuits, certain input combinations <b>never occur</b>, or the output for them <b>does not matter</b>. These are called <b>don't-care conditions</b>. They are marked <b>X</b> (or d, or φ) in the truth table and K-map and written as <b>d(…)</b>.</p>
<p><i>Examples:</i> in BCD only 0000–1001 occur, so 1010–1111 are don't-cares; a lift cannot be at two floors at once.</p>
<h4>How to use X in a K-map</h4>
<ul>
<li>An X may be treated as <b>1 or 0</b>, whichever gives a <b>larger group</b> or fewer groups.</li>
<li>Use an X <b>only if it helps</b>. Never make a group of only X cells.</li>
<li>Xs not used in any group are treated as 0.</li>
</ul>
<p><b>Example:</b> Y = Σm(1, 3, 7, 11, 15) + d(0, 2, 5)</p>""" + D_EN
          + f"<p>Using X0 and X2 turns the pair {B('!A!B')}D into the quad {B('!A!B')}. X5 is not needed, so it is taken as 0. Without don't-cares the answer would be {B('!A!BD')} + CD (more literals).</p>",
          f"""<p>કેટલાક circuits માં અમુક input combinations <b>ક્યારેય આવતા નથી</b>, અથવા તેમના માટે output <b>મહત્વનું નથી</b>. તેમને <b>don't-care conditions</b> કહે છે. Truth table અને K-map માં તેમને <b>X</b> (અથવા d, φ) વડે દર્શાવાય છે અને <b>d(…)</b> તરીકે લખાય છે.</p>
<p><i>ઉદાહરણ:</i> BCD માં માત્ર 0000–1001 આવે છે, તેથી 1010–1111 don't-cares છે; lift એક સાથે બે માળ પર ન હોઈ શકે.</p>
<h4>K-map માં X નો ઉપયોગ</h4>
<ul>
<li>X ને <b>1 અથવા 0</b> ગણી શકાય, જેનાથી <b>મોટો group</b> કે ઓછા groups બને તે મુજબ.</li>
<li>X નો ઉપયોગ <b>ફાયદો થાય ત્યારે જ</b> કરો. માત્ર X cells નો group ક્યારેય ન બનાવો.</li>
<li>કોઈ group માં ન વપરાયેલા X ને 0 ગણાય.</li>
</ul>
<p><b>ઉદાહરણ:</b> Y = Σm(1, 3, 7, 11, 15) + d(0, 2, 5)</p>""" + D_GU
          + f"<p>X0 અને X2 વાપરવાથી pair {B('!A!B')}D, quad {B('!A!B')} બને છે. X5 ની જરૂર નથી, તેથી તેને 0 ગણાય. Don't-cares વગર જવાબ {B('!A!BD')} + CD આવે (વધુ literals).</p>",
          diagram="de3_dontcare", examples=["de3n9"], key=True),

        T("3.3.2 Application: BCD Circuits", "3.3.2 ઉપયોગ: BCD Circuits",
          """<p>For a circuit with a <b>BCD input</b> (ABCD, A = MSB), the inputs 10 to 15 never occur, so m10–m15 are don't-cares. This makes BCD circuits very simple.</p>
<p><b>Example:</b> design a circuit whose output is 1 when the BCD input is 5 or more (5, 6, 7, 8, 9).</p>""" + BC_EN
          + "<p>Using the six don't-cares, the answer needs only 2 AND gates and 1 OR gate. Without them, the result would be " + B("A!B!C") + " + " + B("!ABD") + " + " + B("!ABC") + ".</p>",
          """<p><b>BCD input</b> (ABCD, A = MSB) વાળા circuit માં inputs 10 થી 15 ક્યારેય આવતા નથી, તેથી m10–m15 don't-cares છે. આથી BCD circuits ખૂબ સાદા બને છે.</p>
<p><b>ઉદાહરણ:</b> BCD input 5 કે વધુ (5, 6, 7, 8, 9) હોય ત્યારે output 1 આપતો circuit design કરો.</p>""" + BC_GU
          + "<p>છ don't-cares વાપરવાથી જવાબ માટે માત્ર 2 AND અને 1 OR gate જોઈએ. તેમના વગર જવાબ " + B("A!B!C") + " + " + B("!ABD") + " + " + B("!ABC") + " આવે.</p>",
          diagram="de3_bcd", examples=["de3n10"]),
    ],
}
# claims in the text
assert set(K.sop_str(K.minimise(4, EXDC[1])).split(" + ")) == {"!A!BD", "CD"}
assert set(K.sop_str(K.minimise(4, EXBCD[1])).split(" + ")) == {"A!B!C", "!ABD", "!ABC"}

SEC_3_4 = {
    "title": {"en": "3.4 Implementation using Logic Gates", "gu": "3.4 Logic Gates વડે Implementation"},
    "items": [
        T("3.4.1 Implementation using Basic Gates (AND, OR, NOT)", "3.4.1 Basic Gates (AND, OR, NOT) વડે Implementation",
          f"""<p>A minimal SOP expression is implemented as a <b>two-level AND-OR circuit</b>:</p>
<ol>
<li><b>NOT gates</b> produce the complemented inputs needed ({B('!A')}, {B('!C')}, {B('!D')} …).</li>
<li><b>Level 1:</b> one <b>AND gate</b> for each product term (number of inputs = literals in the term). A single-literal term needs no AND gate.</li>
<li><b>Level 2:</b> one <b>OR gate</b> whose inputs are the AND outputs (number of inputs = number of terms).</li>
</ol>
<p>A minimal POS expression is implemented as an <b>OR-AND circuit</b> in the same way.</p>
<p><b>Example:</b> Y = {B(K.sop_str(G4))} (from 3.2.7)</p>
<ul><li>NOT gates: 3 ({B('!A')}, {B('!C')}, {B('!D')}) &nbsp; ICs: 7404</li>
<li>AND gates: 2 two-input ({B('!A!D')}, {B('B!D')}) &nbsp; IC: 7408</li>
<li>OR gate: 1 three-input (or two 2-input OR gates) &nbsp; IC: 7432</li></ul>
<p><b>Gate count</b> = NOT + AND + OR gates. The number of gate inputs (literals) is also used to compare circuits.</p>""",
          f"""<p>Minimal SOP expression ને <b>two-level AND-OR circuit</b> તરીકે બનાવાય છે:</p>
<ol>
<li><b>NOT gates</b> જરૂરી complemented inputs ({B('!A')}, {B('!C')}, {B('!D')} …) બનાવે છે.</li>
<li><b>Level 1:</b> દરેક product term માટે એક <b>AND gate</b> (inputs ની સંખ્યા = term ના literals). એક literal વાળા term માટે AND gate ની જરૂર નથી.</li>
<li><b>Level 2:</b> એક <b>OR gate</b> જેના inputs AND outputs છે (inputs = terms ની સંખ્યા).</li>
</ol>
<p>Minimal POS expression ને એ જ રીતે <b>OR-AND circuit</b> તરીકે બનાવાય છે.</p>
<p><b>ઉદાહરણ:</b> Y = {B(K.sop_str(G4))} (3.2.7 માંથી)</p>
<ul><li>NOT gates: 3 ({B('!A')}, {B('!C')}, {B('!D')}) &nbsp; IC: 7404</li>
<li>AND gates: 2 two-input ({B('!A!D')}, {B('B!D')}) &nbsp; IC: 7408</li>
<li>OR gate: 1 three-input (અથવા બે 2-input OR gates) &nbsp; IC: 7432</li></ul>
<p><b>Gate count</b> = NOT + AND + OR gates. Circuits ની સરખામણી માટે gate inputs (literals) ની સંખ્યા પણ વપરાય છે.</p>""",
          diagram="de3_impl", examples=["de3n13"], key=True),

        T("3.4.2 NAND-NAND Implementation, Advantages and Limitations of K-map", "3.4.2 NAND-NAND Implementation, K-map ના ફાયદા અને મર્યાદાઓ",
          f"""<h4>NAND-NAND implementation</h4>
<p>An AND-OR (SOP) circuit can be converted to an all-NAND circuit by <b>replacing every AND and OR gate with a NAND gate</b> (inputs complemented with NAND-inverters). This follows from De Morgan's theorem:</p>
<p style="text-align:center">AB + CD = {B('!(!(AB)·!(CD))')}</p>
<p>Similarly, an OR-AND (POS) circuit becomes an all-NOR circuit.</p>
<h4>Advantages of the K-map method</h4>
<ul><li>Simple, graphical and systematic; gives the minimal result directly.</li>
<li>Fewer chances of error than algebra; easy to use don't-cares.</li></ul>
<h4>Limitations</h4>
<ul><li>Difficult for more than 4 variables (5 and 6-variable maps need two or four 4-variable maps); impractical beyond 6.</li>
<li>Depends on visual identification of groups, so it is not suitable for computers. The <b>Quine–McCluskey</b> method is used then.</li></ul>""",
          f"""<h4>NAND-NAND implementation</h4>
<p>AND-OR (SOP) circuit માં <b>દરેક AND અને OR gate ને NAND gate વડે બદલવાથી</b> (complemented inputs NAND-inverters વડે) તે all-NAND circuit બને છે. આ De Morgan's theorem પરથી મળે છે:</p>
<p style="text-align:center">AB + CD = {B('!(!(AB)·!(CD))')}</p>
<p>તે જ રીતે OR-AND (POS) circuit all-NOR circuit બને છે.</p>
<h4>K-map method ના ફાયદા</h4>
<ul><li>સરળ, graphical અને systematic; સીધો minimal જવાબ આપે.</li>
<li>Algebra કરતાં ભૂલની શક્યતા ઓછી; don't-cares વાપરવા સરળ.</li></ul>
<h4>મર્યાદાઓ</h4>
<ul><li>4 થી વધુ variables માટે અઘરું (5 અને 6-variable maps માટે બે કે ચાર 4-variable maps જોઈએ); 6 થી વધુ માટે અવ્યવહારુ.</li>
<li>Groups ની દૃષ્ટિથી ઓળખ પર આધાર, તેથી computers માટે યોગ્ય નથી. ત્યારે <b>Quine–McCluskey</b> method વપરાય છે.</li></ul>""",
          examples=["de3n14"]),
    ],
}

NOTES_B = [SEC_3_3, SEC_3_4]
