"""Digital Electronics Fundamentals (DI03000011) - Unit 1 notes, part B: 1.3 Conversions, 1.4 Binary arithmetic, 1.5 Binary codes.
All worked values are computed by de_num (exact, asserted)."""
from fractions import Fraction
from content_DI03000011_u1_notes_a import T
import de_num as D

# ---- inline worked examples (computed) ----
_v, _x, (HEX_EN, HEX_GU) = D.to_decimal("2AF", 16)
assert _v == 687
_r45, (DIV_EN, DIV_GU) = D.int_to_base(45, 2)
_f, _ex, (FR_EN, FR_GU) = D.frac_to_base(Fraction(5, 8), 2)
_o125, (O_EN, O_GU) = D.int_to_base(125, 8)
_h2748, (H_EN, H_GU) = D.int_to_base(2748, 16)
_add, ADD_PRE = D.add_work("1011", "1101")
_sd, SUB_PRE = D.sub_direct("1101", "0110")
_s1, S1_EN, S1_GU = D.sub_ones("1101", "0110")
_s2, S2_EN, S2_GU = D.sub_twos("1101", "0110")
assert (_r45, _f, _o125, _h2748, _add, _sd, _s1, _s2) == ("101101", "101", "175", "ABC", "11000", "0111", "0111", "0111")


def sigtable():
    rows = [(5, "0000 0101", "0000 0101", "0000 0101"), (-5, "1000 0101", "1111 1010", "1111 1011")]
    h = "<table><tr><th>{}</th><th>Sign-magnitude</th><th>1's comp</th><th>2's comp</th></tr>"
    body = "".join(f"<tr><td>{'+' if n > 0 else '−'}{abs(n)}</td><td>{a}</td><td>{b}</td><td>{c}</td></tr>" for n, a, b, c in rows)
    assert format(256 - 5, "08b") == "11111011"
    return h.format("Number") + body + "</table>", h.format("સંખ્યા") + body + "</table>"


SIG_EN, SIG_GU = sigtable()


def codes_table():
    gray = lambda n: n ^ (n >> 1)
    r = "".join(f"<tr><td>{i}</td><td>{i:04b}</td><td>{i + 3:04b}</td><td>{gray(i):04b}</td></tr>" for i in range(10))
    return "<table><tr><th>Decimal</th><th>BCD (8421)</th><th>Excess-3</th><th>Gray</th></tr>" + r + "</table>"


CODES = codes_table()

SEC_1_3 = {
    "title": {"en": "1.3 Conversion between Number Systems", "gu": "1.3 Number Systems વચ્ચે Conversion"},
    "items": [
        T("1.3.1 Binary, Octal and Hexadecimal to Decimal", "1.3.1 Binary, Octal અને Hexadecimal થી Decimal",
          f"""<p>Any number can be converted to decimal by the <b>positional weight method</b>:</p>
<ol>
<li>Write the weight (base<sup>position</sup>) under each digit. Positions are 0, 1, 2 … to the left of the point and −1, −2 … to the right.</li>
<li>Multiply each digit by its weight.</li>
<li>Add all the products. The sum is the decimal number.</li>
</ol>
<p><b>Example:</b> (2AF)<sub>16</sub> to decimal (A = 10, F = 15):</p>{HEX_EN}
<p>(2AF)<sub>16</sub> = 512 + 160 + 15 = <b>(687)<sub>10</sub></b></p>
<p><i>Quick rule for binary:</i> just add the weights (1, 2, 4, 8, 16 …) of the positions that contain 1. E.g. (101101)<sub>2</sub> = 32 + 8 + 4 + 1 = 45.</p>""",
          f"""<p>કોઈ પણ સંખ્યાને <b>positional weight method</b> થી decimal માં ફેરવી શકાય:</p>
<ol>
<li>દરેક digit નીચે તેનું weight (base<sup>position</sup>) લખો. Point ની ડાબી બાજુ positions 0, 1, 2 … અને જમણી બાજુ −1, −2 … છે.</li>
<li>દરેક digit ને તેના weight સાથે ગુણો.</li>
<li>બધા ગુણાકારનો સરવાળો કરો. સરવાળો એ decimal સંખ્યા છે.</li>
</ol>
<p><b>ઉદાહરણ:</b> (2AF)<sub>16</sub> ને decimal માં (A = 10, F = 15):</p>{HEX_GU}
<p>(2AF)<sub>16</sub> = 512 + 160 + 15 = <b>(687)<sub>10</sub></b></p>
<p><i>Binary માટે ઝડપી નિયમ:</i> જે positions માં 1 હોય તેમના weights (1, 2, 4, 8, 16 …) નો સરવાળો કરો. દા.ત. (101101)<sub>2</sub> = 32 + 8 + 4 + 1 = 45.</p>""",
          examples=["de1n1", "de1n2", "de1n3"], key=True),

        T("1.3.2 Decimal to Binary (Integer Part)", "1.3.2 Decimal થી Binary (Integer ભાગ)",
          f"""<p>The integer part is converted by the <b>repeated division method</b> (double-dabble method):</p>
<ol>
<li>Divide the decimal number by <b>2</b>. Write the quotient and the remainder (0 or 1).</li>
<li>Divide the quotient again by 2. Repeat until the quotient becomes <b>0</b>.</li>
<li>Write the remainders <b>from bottom to top</b>. The first remainder is the <b>LSB</b> and the last remainder is the <b>MSB</b>.</li>
</ol>
<p><b>Example:</b> (45)<sub>10</sub> to binary:</p>{DIV_EN}
<p>Reading the remainders upward: (45)<sub>10</sub> = <b>(101101)<sub>2</sub></b></p>
<p><i>Check:</i> 32 + 8 + 4 + 1 = 45 ✓</p>""",
          f"""<p>Integer ભાગને <b>repeated division method</b> (double-dabble method) થી ફેરવાય છે:</p>
<ol>
<li>Decimal સંખ્યાને <b>2</b> વડે ભાગો. ભાગફળ અને શેષ (0 અથવા 1) લખો.</li>
<li>ભાગફળને ફરીથી 2 વડે ભાગો. ભાગફળ <b>0</b> થાય ત્યાં સુધી આમ કરો.</li>
<li>શેષને <b>નીચેથી ઉપર</b> લખો. પહેલી શેષ <b>LSB</b> અને છેલ્લી શેષ <b>MSB</b> છે.</li>
</ol>
<p><b>ઉદાહરણ:</b> (45)<sub>10</sub> ને binary માં:</p>{DIV_GU}
<p>શેષ ઉપર તરફ વાંચતાં: (45)<sub>10</sub> = <b>(101101)<sub>2</sub></b></p>
<p><i>ચકાસણી:</i> 32 + 8 + 4 + 1 = 45 ✓</p>""",
          diagram="de1_division", examples=["de1n4"], key=True),

        T("1.3.3 Decimal Fraction to Binary", "1.3.3 Decimal Fraction થી Binary",
          f"""<p>The fraction part is converted by the <b>repeated multiplication method</b>:</p>
<ol>
<li>Multiply the fraction by <b>2</b>.</li>
<li>The <b>integer part</b> of the product (0 or 1) is the next binary digit.</li>
<li>Multiply the remaining fraction part by 2 again.</li>
<li>Stop when the fraction becomes <b>0</b>, or when the required number of bits (usually 4 to 6) is obtained.</li>
<li>Write the integer parts <b>from top to bottom</b> (first one is just after the point).</li>
</ol>
<p><b>Example:</b> (0.625)<sub>10</sub> to binary:</p>{FR_EN}
<p>(0.625)<sub>10</sub> = <b>(0.101)<sub>2</sub></b></p>
<p><b>Note:</b> Many fractions such as 0.1, 0.2 and 0.3 never become 0; the bits repeat. The answer is then <b>approximate</b>, e.g. (0.3)<sub>10</sub> ≈ (0.01001)<sub>2</sub>.</p>
<p>For a mixed number (e.g. 25.6875), convert the integer and fraction parts separately and join them with a point.</p>""",
          f"""<p>Fraction ભાગને <b>repeated multiplication method</b> થી ફેરવાય છે:</p>
<ol>
<li>Fraction ને <b>2</b> વડે ગુણો.</li>
<li>ગુણનફળનો <b>integer ભાગ</b> (0 અથવા 1) એ પછીનો binary digit છે.</li>
<li>બાકી રહેલા fraction ભાગને ફરીથી 2 વડે ગુણો.</li>
<li>Fraction <b>0</b> થાય, અથવા જરૂરી bits (સામાન્ય રીતે 4 થી 6) મળે ત્યારે અટકો.</li>
<li>Integer ભાગોને <b>ઉપરથી નીચે</b> લખો (પહેલો point ની તરત પછી આવે).</li>
</ol>
<p><b>ઉદાહરણ:</b> (0.625)<sub>10</sub> ને binary માં:</p>{FR_GU}
<p>(0.625)<sub>10</sub> = <b>(0.101)<sub>2</sub></b></p>
<p><b>નોંધ:</b> 0.1, 0.2, 0.3 જેવા ઘણા fractions ક્યારેય 0 થતા નથી; bits પુનરાવર્તિત થાય છે. ત્યારે જવાબ <b>અંદાજિત (approximate)</b> હોય છે, દા.ત. (0.3)<sub>10</sub> ≈ (0.01001)<sub>2</sub>.</p>
<p>Mixed સંખ્યા (દા.ત. 25.6875) માટે integer અને fraction ભાગને અલગ અલગ ફેરવી point વડે જોડો.</p>""",
          diagram="de1_fraction", examples=["de1n5", "de1n6"]),

        T("1.3.4 Decimal to Octal and Hexadecimal", "1.3.4 Decimal થી Octal અને Hexadecimal",
          f"""<p>The same methods are used, but with base 8 or 16:</p>
<ul>
<li><b>Integer part:</b> divide repeatedly by <b>8</b> (octal) or <b>16</b> (hex); read the remainders upward.</li>
<li><b>Fraction part:</b> multiply repeatedly by <b>8</b> or <b>16</b>; read the integer parts downward.</li>
<li>In hex, remainders 10 to 15 are written as <b>A to F</b>.</li>
</ul>
<p><b>Example 1:</b> (125)<sub>10</sub> to octal:</p>{O_EN}
<p>(125)<sub>10</sub> = <b>(175)<sub>8</sub></b>. Check: 1×64 + 7×8 + 5 = 125 ✓</p>
<p><b>Example 2:</b> (2748)<sub>10</sub> to hexadecimal:</p>{H_EN}
<p>(2748)<sub>10</sub> = <b>(ABC)<sub>16</sub></b>. Check: 10×256 + 11×16 + 12 = 2748 ✓</p>
<p><i>Alternative:</i> convert decimal → binary first, then binary → octal/hex by grouping.</p>""",
          f"""<p>આ જ methods વપરાય છે, પણ base 8 અથવા 16 સાથે:</p>
<ul>
<li><b>Integer ભાગ:</b> <b>8</b> (octal) અથવા <b>16</b> (hex) વડે વારંવાર ભાગો; શેષ ઉપર તરફ વાંચો.</li>
<li><b>Fraction ભાગ:</b> <b>8</b> અથવા <b>16</b> વડે વારંવાર ગુણો; integer ભાગો નીચે તરફ વાંચો.</li>
<li>Hex માં શેષ 10 થી 15 ને <b>A થી F</b> તરીકે લખાય છે.</li>
</ul>
<p><b>ઉદાહરણ 1:</b> (125)<sub>10</sub> ને octal માં:</p>{O_GU}
<p>(125)<sub>10</sub> = <b>(175)<sub>8</sub></b>. ચકાસણી: 1×64 + 7×8 + 5 = 125 ✓</p>
<p><b>ઉદાહરણ 2:</b> (2748)<sub>10</sub> ને hexadecimal માં:</p>{H_GU}
<p>(2748)<sub>10</sub> = <b>(ABC)<sub>16</sub></b>. ચકાસણી: 10×256 + 11×16 + 12 = 2748 ✓</p>
<p><i>બીજી રીત:</i> પહેલાં decimal → binary કરો, પછી grouping દ્વારા binary → octal/hex કરો.</p>""",
          examples=["de1n7", "de1n8"]),

        T("1.3.5 Binary to Octal / Hexadecimal and Back", "1.3.5 Binary થી Octal / Hexadecimal અને પાછું",
          """<h4>Binary → Octal (groups of 3)</h4>
<ol>
<li>Starting from the binary point, make <b>groups of 3 bits</b>: towards the <b>left</b> for the integer part and towards the <b>right</b> for the fraction part.</li>
<li>Add zeros at the <b>left end</b> of the integer part and the <b>right end</b> of the fraction part to complete the groups.</li>
<li>Replace each group by its octal digit (000=0 … 111=7).</li>
</ol>
<h4>Binary → Hexadecimal (groups of 4)</h4>
<p>Same method, but with <b>groups of 4 bits</b> (0000=0 … 1111=F).</p>
<p><b>Example:</b> (11010110.1011)<sub>2</sub></p>
<ul>
<li>Octal: 011 010 110 . 101 100 → <b>(326.54)<sub>8</sub></b></li>
<li>Hex: 1101 0110 . 1011 → <b>(D6.B)<sub>16</sub></b></li>
</ul>
<h4>Octal / Hex → Binary</h4>
<p>Replace <b>each octal digit by 3 bits</b> and <b>each hex digit by 4 bits</b>; then remove extra zeros at the ends.</p>
<p>E.g. (3A7.C)<sub>16</sub> = 0011 1010 0111 . 1100 = <b>(1110100111.11)<sub>2</sub></b></p>
<p>This method is fast because 8 = 2<sup>3</sup> and 16 = 2<sup>4</sup>; no division is needed.</p>""",
          """<h4>Binary → Octal (3 ના groups)</h4>
<ol>
<li>Binary point થી શરૂ કરીને <b>3 bits ના groups</b> બનાવો: integer ભાગ માટે <b>ડાબી</b> તરફ અને fraction ભાગ માટે <b>જમણી</b> તરફ.</li>
<li>Groups પૂરા કરવા integer ભાગની <b>ડાબી બાજુએ</b> અને fraction ભાગની <b>જમણી બાજુએ</b> zeros ઉમેરો.</li>
<li>દરેક group ની જગ્યાએ તેનો octal digit લખો (000=0 … 111=7).</li>
</ol>
<h4>Binary → Hexadecimal (4 ના groups)</h4>
<p>આ જ method, પણ <b>4 bits ના groups</b> સાથે (0000=0 … 1111=F).</p>
<p><b>ઉદાહરણ:</b> (11010110.1011)<sub>2</sub></p>
<ul>
<li>Octal: 011 010 110 . 101 100 → <b>(326.54)<sub>8</sub></b></li>
<li>Hex: 1101 0110 . 1011 → <b>(D6.B)<sub>16</sub></b></li>
</ul>
<h4>Octal / Hex → Binary</h4>
<p><b>દરેક octal digit ને 3 bits</b> અને <b>દરેક hex digit ને 4 bits</b> વડે બદલો; પછી છેડા પરના વધારાના zeros કાઢી નાખો.</p>
<p>દા.ત. (3A7.C)<sub>16</sub> = 0011 1010 0111 . 1100 = <b>(1110100111.11)<sub>2</sub></b></p>
<p>8 = 2<sup>3</sup> અને 16 = 2<sup>4</sup> હોવાથી આ method ઝડપી છે; ભાગાકારની જરૂર નથી.</p>""",
          diagram="de1_grouping", examples=["de1n9", "de1n10"], key=True),

        T("1.3.6 Octal ↔ Hexadecimal and Summary of Conversions", "1.3.6 Octal ↔ Hexadecimal અને Conversions નો સારાંશ",
          """<p>Octal and hexadecimal are converted <b>through binary</b>:</p>
<ul>
<li><b>Octal → Hex:</b> octal → binary (3 bits each) → regroup in 4 bits → hex.</li>
<li><b>Hex → Octal:</b> hex → binary (4 bits each) → regroup in 3 bits → octal.</li>
</ul>
<p><b>Example:</b> (725)<sub>8</sub> = 111 010 101 = 1 1101 0101 = <b>(1D5)<sub>16</sub></b></p>
<p>(Through decimal is also possible: 725<sub>8</sub> = 469<sub>10</sub> = 1D5<sub>16</sub>, but it is longer.)</p>
<h4>Summary</h4>
<table><tr><th>From → To</th><th>Method</th></tr>
<tr><td>Any base → Decimal</td><td>Multiply each digit by its weight and add</td></tr>
<tr><td>Decimal → any base (integer)</td><td>Repeated division by base, remainders upward</td></tr>
<tr><td>Decimal → any base (fraction)</td><td>Repeated multiplication by base, integers downward</td></tr>
<tr><td>Binary → Octal / Hex</td><td>Groups of 3 / 4 bits from the point</td></tr>
<tr><td>Octal / Hex → Binary</td><td>Each digit → 3 / 4 bits</td></tr>
<tr><td>Octal ↔ Hex</td><td>Through binary</td></tr></table>""",
          """<p>Octal અને hexadecimal ને <b>binary મારફતે</b> ફેરવાય છે:</p>
<ul>
<li><b>Octal → Hex:</b> octal → binary (દરેકના 3 bits) → 4 bits માં ફરી group → hex.</li>
<li><b>Hex → Octal:</b> hex → binary (દરેકના 4 bits) → 3 bits માં ફરી group → octal.</li>
</ul>
<p><b>ઉદાહરણ:</b> (725)<sub>8</sub> = 111 010 101 = 1 1101 0101 = <b>(1D5)<sub>16</sub></b></p>
<p>(Decimal મારફતે પણ થઈ શકે: 725<sub>8</sub> = 469<sub>10</sub> = 1D5<sub>16</sub>, પણ તે લાંબી રીત છે.)</p>
<h4>સારાંશ</h4>
<table><tr><th>From → To</th><th>Method</th></tr>
<tr><td>કોઈ પણ base → Decimal</td><td>દરેક digit ને તેના weight સાથે ગુણી સરવાળો કરો</td></tr>
<tr><td>Decimal → કોઈ base (integer)</td><td>Base વડે વારંવાર ભાગાકાર, શેષ ઉપર તરફ</td></tr>
<tr><td>Decimal → કોઈ base (fraction)</td><td>Base વડે વારંવાર ગુણાકાર, integers નીચે તરફ</td></tr>
<tr><td>Binary → Octal / Hex</td><td>Point થી 3 / 4 bits ના groups</td></tr>
<tr><td>Octal / Hex → Binary</td><td>દરેક digit → 3 / 4 bits</td></tr>
<tr><td>Octal ↔ Hex</td><td>Binary મારફતે</td></tr></table>""",
          diagram="de1_conv_map", examples=["de1n11", "de1n12"]),
    ],
}

SEC_1_4 = {
    "title": {"en": "1.4 Binary Arithmetic and Complements", "gu": "1.4 Binary Arithmetic અને Complements"},
    "items": [
        T("1.4.1 Binary Addition", "1.4.1 Binary Addition (સરવાળો)",
          f"""<p>Binary addition is done column by column from the <b>LSB (right)</b>, like decimal addition. When the sum in a column is 2 or more, a <b>carry</b> goes to the next column.</p>
<h4>Rules of binary addition</h4>
<table><tr><th>A</th><th>B</th><th>Sum</th><th>Carry</th></tr>
<tr><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>1</td><td>1</td><td>0</td></tr>
<tr><td>1</td><td>0</td><td>1</td><td>0</td></tr><tr><td>1</td><td>1</td><td>0</td><td>1</td></tr></table>
<p>Also 1 + 1 + 1 = 1 with carry 1 (i.e. 11<sub>2</sub> = 3).</p>
<p><b>Example:</b> 1011 + 1101 (11 + 13):</p>{ADD_PRE}
<p>Result = <b>(11000)<sub>2</sub></b> = 24 ✓</p>""",
          f"""<p>Binary સરવાળો decimal ની જેમ જ <b>LSB (જમણી બાજુ)</b> થી column-wise થાય છે. કોઈ column નો સરવાળો 2 કે વધુ થાય ત્યારે આગળના column માં <b>carry</b> જાય છે.</p>
<h4>Binary addition ના નિયમો</h4>
<table><tr><th>A</th><th>B</th><th>Sum</th><th>Carry</th></tr>
<tr><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>1</td><td>1</td><td>0</td></tr>
<tr><td>1</td><td>0</td><td>1</td><td>0</td></tr><tr><td>1</td><td>1</td><td>0</td><td>1</td></tr></table>
<p>તેમજ 1 + 1 + 1 = 1 અને carry 1 (એટલે કે 11<sub>2</sub> = 3).</p>
<p><b>ઉદાહરણ:</b> 1011 + 1101 (11 + 13):</p>{ADD_PRE}
<p>જવાબ = <b>(11000)<sub>2</sub></b> = 24 ✓</p>""",
          diagram="de1_binary_add", examples=["de1n13"], key=True),

        T("1.4.2 Binary Subtraction (Direct Method)", "1.4.2 Binary Subtraction (Direct Method)",
          f"""<p>In direct subtraction, when a smaller bit has a larger bit subtracted from it (0 − 1), we <b>borrow 1</b> from the next higher column. A borrowed 1 is worth <b>2</b> (10<sub>2</sub>) in the current column.</p>
<h4>Rules of binary subtraction</h4>
<table><tr><th>A</th><th>B</th><th>Difference</th><th>Borrow</th></tr>
<tr><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>1</td><td>1</td><td>1</td></tr>
<tr><td>1</td><td>0</td><td>1</td><td>0</td></tr><tr><td>1</td><td>1</td><td>0</td><td>0</td></tr></table>
<p><b>Example:</b> 1101 − 0110 (13 − 6):</p>{SUB_PRE}
<p>Result = <b>(0111)<sub>2</sub></b> = 7 ✓</p>
<p>Digital circuits do not subtract this way; it needs a separate subtractor. Using <b>complements</b>, subtraction is done with the <b>adder</b> itself, so the same hardware performs both addition and subtraction.</p>""",
          f"""<p>Direct subtraction માં જ્યારે નાના bit માંથી મોટો bit બાદ કરવાનો હોય (0 − 1), ત્યારે આગળના મોટા column માંથી <b>1 ઉધાર (borrow)</b> લેવાય છે. ઉધાર લીધેલા 1 ની કિંમત ચાલુ column માં <b>2</b> (10<sub>2</sub>) છે.</p>
<h4>Binary subtraction ના નિયમો</h4>
<table><tr><th>A</th><th>B</th><th>Difference</th><th>Borrow</th></tr>
<tr><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>1</td><td>1</td><td>1</td></tr>
<tr><td>1</td><td>0</td><td>1</td><td>0</td></tr><tr><td>1</td><td>1</td><td>0</td><td>0</td></tr></table>
<p><b>ઉદાહરણ:</b> 1101 − 0110 (13 − 6):</p>{SUB_PRE}
<p>જવાબ = <b>(0111)<sub>2</sub></b> = 7 ✓</p>
<p>Digital circuits આ રીતે બાદબાકી કરતા નથી; તે માટે અલગ subtractor જોઈએ. <b>Complements</b> વાપરીને બાદબાકી <b>adder</b> વડે જ થાય છે, તેથી એક જ hardware સરવાળો અને બાદબાકી બંને કરે છે.</p>""",
          examples=["de1n14"]),

        T("1.4.3 1's and 2's Complement", "1.4.3 1's અને 2's Complement",
          """<h4>1's complement</h4>
<p>The 1's complement of a binary number is obtained by <b>inverting every bit</b>: change each 0 to 1 and each 1 to 0.</p>
<p>E.g. 1's complement of 10110 = <b>01001</b>. (A NOT gate on each bit gives the 1's complement.)</p>
<h4>2's complement</h4>
<p>2's complement = <b>1's complement + 1</b> (add 1 at the LSB).</p>
<p>E.g. 10110 → 1's complement 01001 → + 1 → <b>01010</b>.</p>
<p><b>Shortcut:</b> start from the LSB, copy all bits up to and including the <b>first 1</b>, then invert all the remaining bits. 10110 → keep "10", invert "101" to "010" → 01010.</p>
<h4>General rule</h4>
<p>For base r there are two complements: the <b>(r−1)'s complement</b> and the <b>r's complement</b> = (r−1)'s complement + 1. For decimal these are the 9's and 10's complements; for binary they are the 1's and 2's complements.</p>
<p><b>Uses:</b> complements are used to represent <b>negative numbers</b> and to perform <b>subtraction using addition</b>.</p>""",
          """<h4>1's complement</h4>
<p>Binary સંખ્યાનો 1's complement મેળવવા <b>દરેક bit ને ઉલટાવો (invert)</b>: દરેક 0 ને 1 અને દરેક 1 ને 0 કરો.</p>
<p>દા.ત. 10110 નો 1's complement = <b>01001</b>. (દરેક bit પર NOT gate મૂકવાથી 1's complement મળે.)</p>
<h4>2's complement</h4>
<p>2's complement = <b>1's complement + 1</b> (LSB માં 1 ઉમેરો).</p>
<p>દા.ત. 10110 → 1's complement 01001 → + 1 → <b>01010</b>.</p>
<p><b>Shortcut:</b> LSB થી શરૂ કરી <b>પહેલો 1</b> આવે ત્યાં સુધીના (તે 1 સહિત) bits એમ જ લખો, પછી બાકીના બધા bits invert કરો. 10110 → "10" એમ જ, "101" ને "010" → 01010.</p>
<h4>સામાન્ય નિયમ</h4>
<p>Base r માટે બે complements હોય છે: <b>(r−1)'s complement</b> અને <b>r's complement</b> = (r−1)'s complement + 1. Decimal માટે 9's અને 10's complement; binary માટે 1's અને 2's complement.</p>
<p><b>ઉપયોગ:</b> complements નો ઉપયોગ <b>negative સંખ્યાઓ</b> દર્શાવવા અને <b>સરવાળા વડે બાદબાકી</b> કરવા થાય છે.</p>""",
          diagram="de1_complement", examples=["de1n15"], key=True),

        T("1.4.4 Subtraction using 1's Complement", "1.4.4 1's Complement વડે Subtraction",
          "<p>To find <b>A − B</b> using 1's complement:</p>\n<ol>\n"
          "<li>Make A and B the <b>same number of bits</b> (add leading zeros).</li>\n"
          "<li>Find the <b>1's complement of B</b> (the subtrahend).</li>\n"
          "<li><b>Add</b> A and the 1's complement of B.</li>\n"
          "<li>If a <b>carry</b> is generated: the result is <b>positive</b>. Remove the carry and <b>add it to the LSB</b> (this is called <b>end-around carry</b>).</li>\n"
          "<li>If <b>no carry</b>: the result is <b>negative</b>. Take the 1's complement of the sum and put a minus sign.</li>\n</ol>\n"
          "<p><b>Example:</b> 1101 − 0110 (13 − 6):</p>" + D.steps_html(S1_EN) + "<p>Answer = <b>(0111)<sub>2</sub></b> = 7 ✓</p>",
          "<p>1's complement વડે <b>A − B</b> શોધવા:</p>\n<ol>\n"
          "<li>A અને B ને <b>સરખા bits</b> ના બનાવો (આગળ zeros ઉમેરો).</li>\n"
          "<li><b>B (subtrahend) નો 1's complement</b> શોધો.</li>\n"
          "<li>A અને B ના 1's complement નો <b>સરવાળો</b> કરો.</li>\n"
          "<li>જો <b>carry</b> મળે: જવાબ <b>positive</b> છે. Carry ને કાઢીને <b>LSB માં ઉમેરો</b> (તેને <b>end-around carry</b> કહે છે).</li>\n"
          "<li>જો <b>carry ન મળે</b>: જવાબ <b>negative</b> છે. સરવાળાનો 1's complement લઈ minus નિશાની મૂકો.</li>\n</ol>\n"
          "<p><b>ઉદાહરણ:</b> 1101 − 0110 (13 − 6):</p>" + D.steps_html(S1_GU) + "<p>જવાબ = <b>(0111)<sub>2</sub></b> = 7 ✓</p>",
          examples=["de1n16", "de1n17"], key=True),

        T("1.4.5 Subtraction using 2's Complement", "1.4.5 2's Complement વડે Subtraction",
          "<p>To find <b>A − B</b> using 2's complement:</p>\n<ol>\n"
          "<li>Make A and B the <b>same number of bits</b>.</li>\n"
          "<li>Find the <b>2's complement of B</b>.</li>\n"
          "<li><b>Add</b> A and the 2's complement of B.</li>\n"
          "<li>If a <b>carry</b> is generated: <b>discard</b> it. The result is <b>positive</b>.</li>\n"
          "<li>If <b>no carry</b>: the result is <b>negative</b> and in 2's complement form. Take the 2's complement of the sum and put a minus sign.</li>\n</ol>\n"
          "<p><b>Example:</b> 1101 − 0110 (13 − 6):</p>" + D.steps_html(S2_EN) + "<p>Answer = <b>(0111)<sub>2</sub></b> = 7 ✓</p>\n"
          "<h4>1's vs 2's complement method</h4>\n<table><tr><th>1's complement</th><th>2's complement</th></tr>\n"
          "<tr><td>Carry is added back (end-around carry)</td><td>Carry is simply discarded</td></tr>\n"
          "<tr><td>Two zeros: +0 (0000) and −0 (1111)</td><td>Only one zero</td></tr>\n"
          "<tr><td>Slower (extra addition)</td><td>Faster; used in all computers</td></tr></table>",
          "<p>2's complement વડે <b>A − B</b> શોધવા:</p>\n<ol>\n"
          "<li>A અને B ને <b>સરખા bits</b> ના બનાવો.</li>\n"
          "<li><b>B નો 2's complement</b> શોધો.</li>\n"
          "<li>A અને B ના 2's complement નો <b>સરવાળો</b> કરો.</li>\n"
          "<li>જો <b>carry</b> મળે: તેને <b>અવગણો (discard)</b>. જવાબ <b>positive</b> છે.</li>\n"
          "<li>જો <b>carry ન મળે</b>: જવાબ <b>negative</b> છે અને 2's complement સ્વરૂપમાં છે. સરવાળાનો 2's complement લઈ minus નિશાની મૂકો.</li>\n</ol>\n"
          "<p><b>ઉદાહરણ:</b> 1101 − 0110 (13 − 6):</p>" + D.steps_html(S2_GU) + "<p>જવાબ = <b>(0111)<sub>2</sub></b> = 7 ✓</p>\n"
          "<h4>1's અને 2's complement method ની સરખામણી</h4>\n<table><tr><th>1's complement</th><th>2's complement</th></tr>\n"
          "<tr><td>Carry પાછો ઉમેરાય છે (end-around carry)</td><td>Carry ને અવગણવામાં આવે છે</td></tr>\n"
          "<tr><td>બે zero: +0 (0000) અને −0 (1111)</td><td>માત્ર એક zero</td></tr>\n"
          "<tr><td>ધીમું (વધારાનો સરવાળો)</td><td>ઝડપી; બધા computers માં વપરાય છે</td></tr></table>",
          diagram="de1_sub_flow", examples=["de1n18", "de1n19", "de1n20"], key=True),

        T("1.4.6 Signed Binary Numbers", "1.4.6 Signed Binary Numbers",
          f"""<p>In a <b>signed number</b>, the MSB is used as the <b>sign bit</b>: <b>0 = positive</b>, <b>1 = negative</b>. Negative numbers can be written in three ways:</p>
<ol>
<li><b>Sign-magnitude:</b> sign bit + magnitude in normal binary.</li>
<li><b>1's complement form:</b> negative number = 1's complement of the positive number.</li>
<li><b>2's complement form:</b> negative number = 2's complement of the positive number.</li>
</ol>
<p><b>Example (8 bits):</b></p>{SIG_EN}
<p>Positive numbers are the same in all three forms. Range with n bits in 2's complement: <b>−2<sup>n−1</sup> to +(2<sup>n−1</sup> − 1)</b>; for 8 bits, −128 to +127.</p>
<p>The 2's complement form is used in computers because it has only one zero and subtraction is done by simple addition.</p>""",
          f"""<p><b>Signed સંખ્યા</b> માં MSB ને <b>sign bit</b> તરીકે વપરાય છે: <b>0 = positive</b>, <b>1 = negative</b>. Negative સંખ્યાઓ ત્રણ રીતે લખી શકાય:</p>
<ol>
<li><b>Sign-magnitude:</b> sign bit + સામાન્ય binary માં magnitude.</li>
<li><b>1's complement form:</b> negative સંખ્યા = positive સંખ્યાનો 1's complement.</li>
<li><b>2's complement form:</b> negative સંખ્યા = positive સંખ્યાનો 2's complement.</li>
</ol>
<p><b>ઉદાહરણ (8 bits):</b></p>{SIG_GU}
<p>Positive સંખ્યાઓ ત્રણેય સ્વરૂપમાં સરખી હોય છે. n bits ના 2's complement માં range: <b>−2<sup>n−1</sup> થી +(2<sup>n−1</sup> − 1)</b>; 8 bits માટે −128 થી +127.</p>
<p>2's complement સ્વરૂપમાં માત્ર એક zero હોય છે અને બાદબાકી સાદા સરવાળાથી થાય છે, તેથી computers માં તે વપરાય છે.</p>"""),
    ],
}

SEC_1_5 = {
    "title": {"en": "1.5 Binary Codes", "gu": "1.5 Binary Codes"},
    "items": [
        T("1.5.1 BCD and Excess-3 Codes", "1.5.1 BCD અને Excess-3 Codes",
          """<p>A <b>binary code</b> is a group of bits used to represent numbers, letters or symbols.</p>
<h4>BCD (Binary Coded Decimal) / 8421 code</h4>
<ul>
<li>Each <b>decimal digit</b> is written separately as a <b>4-bit</b> binary number with weights 8-4-2-1.</li>
<li>Only 0000 to 1001 are used; 1010 to 1111 are <b>invalid</b> in BCD.</li>
<li>E.g. (58)<sub>10</sub> = 0101 1000 (BCD). Compare: (58)<sub>10</sub> = 111010 in pure binary.</li>
<li>Used in digital clocks, calculators and 7-segment displays.</li>
</ul>
<h4>Excess-3 (XS-3) code</h4>
<ul>
<li>Excess-3 code = <b>BCD + 3 (0011)</b> for each digit. It is a <b>non-weighted</b> code.</li>
<li>E.g. (58)<sub>10</sub>: 5+3 = 8 → 1000, 8+3 = 11 → 1011, so XS-3 = 1000 1011.</li>
<li>It is <b>self-complementing</b>: the 9's complement of a digit is obtained by inverting its bits.</li>
</ul>""" + CODES,
          """<p><b>Binary code</b> એ સંખ્યાઓ, અક્ષરો કે symbols દર્શાવવા માટે વપરાતા bits નો group છે.</p>
<h4>BCD (Binary Coded Decimal) / 8421 code</h4>
<ul>
<li>દરેક <b>decimal digit</b> ને અલગથી 8-4-2-1 weights વાળી <b>4-bit</b> binary સંખ્યા તરીકે લખાય છે.</li>
<li>માત્ર 0000 થી 1001 વપરાય છે; 1010 થી 1111 BCD માં <b>invalid</b> છે.</li>
<li>દા.ત. (58)<sub>10</sub> = 0101 1000 (BCD). સરખામણી: (58)<sub>10</sub> = 111010 (pure binary).</li>
<li>Digital ઘડિયાળ, calculators અને 7-segment displays માં વપરાય છે.</li>
</ul>
<h4>Excess-3 (XS-3) code</h4>
<ul>
<li>Excess-3 code = દરેક digit માટે <b>BCD + 3 (0011)</b>. તે <b>non-weighted</b> code છે.</li>
<li>દા.ત. (58)<sub>10</sub>: 5+3 = 8 → 1000, 8+3 = 11 → 1011, તેથી XS-3 = 1000 1011.</li>
<li>તે <b>self-complementing</b> છે: digit ના bits invert કરવાથી તેનો 9's complement મળે છે.</li>
</ul>""" + CODES,
          examples=["de1n21"]),

        T("1.5.2 Gray Code and ASCII Code", "1.5.2 Gray Code અને ASCII Code",
          """<h4>Gray code</h4>
<ul>
<li>In Gray code, <b>only one bit changes</b> between two successive numbers (unit-distance code). It is non-weighted.</li>
<li>Used in shaft-position encoders and K-maps (Unit 3) to avoid errors during transitions.</li>
</ul>
<p><b>Binary → Gray:</b> MSB stays the same; each next Gray bit = XOR of the current and previous binary bits.<br>E.g. 1011 → 1, 1⊕0=1, 0⊕1=1, 1⊕1=0 → <b>1110</b>.</p>
<p><b>Gray → Binary:</b> MSB stays the same; each next binary bit = XOR of the previous <i>binary</i> bit and the current Gray bit.<br>E.g. 1101 → 1, 1⊕1=0, 0⊕0=0, 0⊕1=1 → <b>1001</b>.</p>
<h4>ASCII code</h4>
<ul>
<li><b>ASCII</b> (American Standard Code for Information Interchange) is a <b>7-bit alphanumeric code</b> giving 128 characters: letters, digits, symbols and control characters.</li>
<li>'A' = 65 = 100 0001, 'a' = 97 = 110 0001, '0' = 48 = 011 0000, space = 32.</li>
<li>Used in keyboards, computers and text files. (Unicode extends ASCII for all languages, including Gujarati.)</li>
</ul>""",
          """<h4>Gray code</h4>
<ul>
<li>Gray code માં બે ક્રમિક સંખ્યાઓ વચ્ચે <b>માત્ર એક જ bit બદલાય</b> છે (unit-distance code). તે non-weighted છે.</li>
<li>Transition દરમિયાન errors ટાળવા shaft-position encoders અને K-maps (Unit 3) માં વપરાય છે.</li>
</ul>
<p><b>Binary → Gray:</b> MSB એમ જ રહે; પછીનો દરેક Gray bit = ચાલુ અને આગળના binary bits નો XOR.<br>દા.ત. 1011 → 1, 1⊕0=1, 0⊕1=1, 1⊕1=0 → <b>1110</b>.</p>
<p><b>Gray → Binary:</b> MSB એમ જ રહે; પછીનો દરેક binary bit = આગળના <i>binary</i> bit અને ચાલુ Gray bit નો XOR.<br>દા.ત. 1101 → 1, 1⊕1=0, 0⊕0=0, 0⊕1=1 → <b>1001</b>.</p>
<h4>ASCII code</h4>
<ul>
<li><b>ASCII</b> (American Standard Code for Information Interchange) એ <b>7-bit alphanumeric code</b> છે જે 128 characters આપે છે: અક્ષરો, digits, symbols અને control characters.</li>
<li>'A' = 65 = 100 0001, 'a' = 97 = 110 0001, '0' = 48 = 011 0000, space = 32.</li>
<li>Keyboards, computers અને text files માં વપરાય છે. (Unicode એ ASCII ને બધી ભાષાઓ, ગુજરાતી સહિત, માટે વિસ્તારે છે.)</li>
</ul>""",
          examples=["de1n22"]),
    ],
}

NOTES_B = [SEC_1_3, SEC_1_4, SEC_1_5]
