"""Basics of Electronics (DI01000151) - Unit 3: Diodes and Rectifiers (part B: 3.4 - 3.6)"""
from content_DI01000151_u3_notes_a import T

# =====================================================================================
SEC_3_4 = {
    "title": {"en": "3.4 Zener Diode", "gu": "3.4 Zener Diode"},
    "items": [
        T("3.4.1 Zener Diode – Definition, Symbol and Construction", "3.4.1 Zener Diode – વ્યાખ્યા, Symbol અને રચના",
          """<p><b>Definition:</b> A Zener diode is a <b>heavily doped</b> silicon P-N junction diode that is specially designed to operate in the <b>reverse breakdown region</b> without getting damaged. It keeps the voltage across it almost <b>constant</b> in breakdown.</p>
<p>It is named after the American scientist <b>Clarence Zener</b>, who explained the Zener breakdown effect.</p>
<h4>Symbol</h4>
<p>Like a normal diode symbol, but the cathode bar has <b>bent ends</b> (like the letter "Z"). See the symbol in the Zener characteristic diagram.</p>
<h4>Construction / special features</h4>
<ul>
<li>Made of <b>silicon</b> (Si) because of its better temperature stability and higher current capability.</li>
<li><b>Heavily doped</b> P and N regions → very <b>thin depletion layer</b> → breakdown at a low, sharp and well-defined voltage.</li>
<li>The breakdown voltage (Zener voltage V<sub>Z</sub>) can be set from about <b>2.4 V to 200 V</b> by controlling the doping.</li>
<li>Designed with good heat dissipation so that it is <b>not damaged</b> in breakdown, as long as current stays below I<sub>Z(max)</sub>.</li>
<li>Always used in <b>reverse bias</b> with a <b>series resistor</b>.</li>
</ul>
<p><b>Examples:</b> 1N4733 (5.1 V, 1 W), 1N4742 (12 V, 1 W), BZX55C5V1 (5.1 V, 0.5 W).</p>""",
          """<p><b>વ્યાખ્યા:</b> Zener diode એ <b>વધુ doped (heavily doped)</b> silicon P-N junction diode છે, જે નુકસાન વિના <b>reverse breakdown region</b> માં કાર્ય કરવા ખાસ બનાવેલો છે. Breakdown માં તે પોતાના પરનો voltage લગભગ <b>અચળ (constant)</b> રાખે છે.</p>
<p>તેનું નામ અમેરિકન વૈજ્ઞાનિક <b>Clarence Zener</b> પરથી પડ્યું છે, જેમણે Zener breakdown અસર સમજાવી હતી.</p>
<h4>Symbol</h4>
<p>સામાન્ય diode symbol જેવો, પરંતુ cathode bar ના છેડા <b>વાળેલા</b> હોય છે ("Z" અક્ષર જેવા). Zener characteristic આકૃતિમાં symbol જુઓ.</p>
<h4>રચના / ખાસ લક્ષણો</h4>
<ul>
<li>વધુ સારી temperature stability અને વધુ current ક્ષમતાને કારણે <b>Silicon</b> (Si) માંથી બને છે.</li>
<li><b>વધુ doped</b> P અને N regions → ખૂબ <b>પાતળું depletion layer</b> → ઓછા, તીક્ષ્ણ અને ચોક્કસ voltage પર breakdown.</li>
<li>Doping નિયંત્રિત કરીને breakdown voltage (Zener voltage V<sub>Z</sub>) આશરે <b>2.4 V થી 200 V</b> સુધી રાખી શકાય.</li>
<li>સારી heat dissipation સાથે બનાવેલ હોવાથી current I<sub>Z(max)</sub> થી નીચે રહે ત્યાં સુધી breakdown માં <b>નુકસાન પામતો નથી</b>.</li>
<li>હંમેશા <b>series resistor</b> સાથે <b>reverse bias</b> માં વપરાય છે.</li>
</ul>
<p><b>ઉદાહરણ:</b> 1N4733 (5.1 V, 1 W), 1N4742 (12 V, 1 W), BZX55C5V1 (5.1 V, 0.5 W).</p>"""),

        T("3.4.2 Working – Zener and Avalanche Breakdown", "3.4.2 કાર્ય – Zener અને Avalanche Breakdown",
          """<h4>In forward bias</h4>
<p>A Zener diode works like an ordinary silicon diode: it conducts after about <b>0.7 V</b>.</p>
<h4>In reverse bias</h4>
<p>A small leakage current flows until the reverse voltage reaches <b>V<sub>Z</sub></b>. At V<sub>Z</sub>, breakdown occurs, the current increases sharply, and the voltage across the diode stays almost constant at V<sub>Z</sub>. Two mechanisms cause breakdown:</p>
<h4>1. Zener breakdown</h4>
<ul>
<li>Occurs in <b>heavily doped</b> diodes with a <b>very thin</b> depletion layer.</li>
<li>Even a small reverse voltage produces a <b>very strong electric field</b> (about 3 × 10⁷ V/m) across the thin layer.</li>
<li>This field directly <b>pulls electrons out of covalent bonds</b> (field ionisation), producing many carriers → large current.</li>
<li>Occurs at <b>low voltages (below ≈ 5 V)</b>; V<sub>Z</sub> decreases with temperature (<b>negative temperature coefficient</b>).</li>
</ul>
<h4>2. Avalanche breakdown</h4>
<ul>
<li>Occurs in <b>lightly/moderately doped</b> diodes with a <b>wider</b> depletion layer, at <b>higher voltages (above ≈ 6 V)</b>.</li>
<li>Minority carriers are accelerated by the field and gain high kinetic energy. They collide with atoms and knock out more electrons (<b>impact ionisation</b>).</li>
<li>The new carriers also collide and produce more carriers → <b>chain reaction (avalanche)</b> → large current.</li>
<li>V<sub>Z</sub> increases with temperature (<b>positive temperature coefficient</b>).</li>
</ul>
<table>
<tr><th>Point</th><th>Zener breakdown</th><th>Avalanche breakdown</th></tr>
<tr><td>Doping</td><td>Heavy</td><td>Light/moderate</td></tr>
<tr><td>Depletion layer</td><td>Very thin</td><td>Wide</td></tr>
<tr><td>Voltage</td><td>Low (&lt; 5 V)</td><td>High (&gt; 6 V)</td></tr>
<tr><td>Mechanism</td><td>Strong field breaks bonds</td><td>Collision (impact ionisation)</td></tr>
<tr><td>Temperature coefficient</td><td>Negative</td><td>Positive</td></tr>
<tr><td>Characteristic</td><td>Breakdown is sharp</td><td>Breakdown is sharp; carriers multiply</td></tr>
</table>
<p>Between about 5 V and 6 V both effects occur, so the temperature coefficient is nearly <b>zero</b>. A 5.6 V Zener is therefore very stable.</p>""",
          """<h4>Forward bias માં</h4>
<p>Zener diode સામાન્ય silicon diode જેવું કામ કરે છે: આશરે <b>0.7 V</b> પછી conduction કરે છે.</p>
<h4>Reverse bias માં</h4>
<p>Reverse voltage <b>V<sub>Z</sub></b> સુધી પહોંચે ત્યાં સુધી નાનો leakage current વહે છે. V<sub>Z</sub> પર breakdown થાય છે, current ઝડપથી વધે છે, અને diode પરનો voltage લગભગ V<sub>Z</sub> પર અચળ રહે છે. Breakdown બે રીતે થાય છે:</p>
<h4>1. Zener breakdown</h4>
<ul>
<li><b>વધુ doped</b> diodes માં, જેમાં <b>ખૂબ પાતળું</b> depletion layer હોય છે.</li>
<li>નાનો reverse voltage પણ પાતળા layer પર <b>ખૂબ તીવ્ર electric field</b> (આશરે 3 × 10⁷ V/m) બનાવે છે.</li>
<li>આ field સીધા <b>covalent bonds માંથી electrons ખેંચી કાઢે</b> છે (field ionisation), જેથી ઘણા carriers બને → મોટો current.</li>
<li><b>ઓછા voltage (≈ 5 V થી નીચે)</b> પર થાય છે; તાપમાન વધતાં V<sub>Z</sub> ઘટે (<b>negative temperature coefficient</b>).</li>
</ul>
<h4>2. Avalanche breakdown</h4>
<ul>
<li><b>ઓછા/મધ્યમ doped</b> diodes માં, જેમાં <b>પહોળું</b> depletion layer હોય, <b>વધુ voltage (≈ 6 V થી ઉપર)</b> પર થાય છે.</li>
<li>Minority carriers field થી પ્રવેગિત થઈ વધુ ગતિ ઊર્જા મેળવે છે. તેઓ atoms સાથે અથડાઈ વધુ electrons છૂટા પાડે છે (<b>impact ionisation</b>).</li>
<li>નવા carriers પણ અથડાઈ વધુ carriers બનાવે છે → <b>શૃંખલા પ્રક્રિયા (avalanche)</b> → મોટો current.</li>
<li>તાપમાન વધતાં V<sub>Z</sub> વધે (<b>positive temperature coefficient</b>).</li>
</ul>
<table>
<tr><th>મુદ્દો</th><th>Zener breakdown</th><th>Avalanche breakdown</th></tr>
<tr><td>Doping</td><td>વધુ</td><td>ઓછું/મધ્યમ</td></tr>
<tr><td>Depletion layer</td><td>ખૂબ પાતળું</td><td>પહોળું</td></tr>
<tr><td>Voltage</td><td>ઓછો (&lt; 5 V)</td><td>વધુ (&gt; 6 V)</td></tr>
<tr><td>પ્રક્રિયા</td><td>તીવ્ર field bonds તોડે</td><td>અથડામણ (impact ionisation)</td></tr>
<tr><td>Temperature coefficient</td><td>Negative</td><td>Positive</td></tr>
<tr><td>Characteristic</td><td>Breakdown તીક્ષ્ણ</td><td>Breakdown તીક્ષ્ણ; carriers ગુણાકારમાં વધે</td></tr>
</table>
<p>આશરે 5 V અને 6 V વચ્ચે બંને અસરો થાય છે, તેથી temperature coefficient લગભગ <b>શૂન્ય</b> હોય છે. તેથી 5.6 V Zener ખૂબ સ્થિર હોય છે.</p>"""),

        T("3.4.3 V-I Characteristics of Zener Diode", "3.4.3 Zener Diode ની V-I Characteristics",
          """<h4>Forward characteristics</h4>
<p>Same as an ordinary Si diode: current rises sharply after the knee voltage of about <b>0.7 V</b>.</p>
<h4>Reverse characteristics</h4>
<ol>
<li>From 0 to V<sub>Z</sub>, only a very small <b>reverse leakage current</b> flows.</li>
<li>At <b>V<sub>Z</sub></b> (Zener voltage), breakdown occurs and current increases suddenly. The curve becomes almost <b>vertical</b>.</li>
<li>In this breakdown region, the current can change from <b>I<sub>Z(min)</sub></b> to <b>I<sub>Z(max)</sub></b> while the voltage stays almost constant at V<sub>Z</sub>. <b>This is the property used for voltage regulation.</b></li>
</ol>
<h4>Important Zener parameters</h4>
<table>
<tr><th>Parameter</th><th>Meaning</th></tr>
<tr><td>Zener voltage V<sub>Z</sub></td><td>Reverse voltage at which breakdown occurs and voltage remains constant</td></tr>
<tr><td>Minimum Zener current I<sub>Z(min)</sub> (I<sub>ZK</sub>)</td><td>Minimum current needed to stay in breakdown (knee current); below it, regulation is lost</td></tr>
<tr><td>Maximum Zener current I<sub>Z(max)</sub> (I<sub>ZM</sub>)</td><td>Maximum current without damage</td></tr>
<tr><td>Power rating P<sub>Z</sub></td><td>Maximum power dissipation: <b>P<sub>Z</sub> = V<sub>Z</sub> × I<sub>Z(max)</sub></b></td></tr>
<tr><td>Zener resistance r<sub>Z</sub></td><td>r<sub>Z</sub> = ΔV<sub>Z</sub> / ΔI<sub>Z</sub>, very small (a few ohms); ideal = 0</td></tr>
<tr><td>Tolerance</td><td>Allowed variation in V<sub>Z</sub> (±5%, ±10%)</td></tr>
</table>""",
          """<h4>Forward characteristics</h4>
<p>સામાન્ય Si diode જેવી જ: આશરે <b>0.7 V</b> ના knee voltage પછી current ઝડપથી વધે છે.</p>
<h4>Reverse characteristics</h4>
<ol>
<li>0 થી V<sub>Z</sub> સુધી ફક્ત ખૂબ નાનો <b>reverse leakage current</b> વહે છે.</li>
<li><b>V<sub>Z</sub></b> (Zener voltage) પર breakdown થાય છે અને current અચાનક વધે છે. Curve લગભગ <b>ઊભો (vertical)</b> બને છે.</li>
<li>આ breakdown region માં current <b>I<sub>Z(min)</sub></b> થી <b>I<sub>Z(max)</sub></b> સુધી બદલાય છતાં voltage લગભગ V<sub>Z</sub> પર અચળ રહે છે. <b>Voltage regulation માટે આ જ ગુણધર્મ વપરાય છે.</b></li>
</ol>
<h4>મહત્વના Zener parameters</h4>
<table>
<tr><th>Parameter</th><th>અર્થ</th></tr>
<tr><td>Zener voltage V<sub>Z</sub></td><td>જે reverse voltage પર breakdown થાય અને voltage અચળ રહે</td></tr>
<tr><td>Minimum Zener current I<sub>Z(min)</sub> (I<sub>ZK</sub>)</td><td>Breakdown માં રહેવા જરૂરી ન્યૂનતમ current (knee current); તેનાથી નીચે regulation ગુમાવાય</td></tr>
<tr><td>Maximum Zener current I<sub>Z(max)</sub> (I<sub>ZM</sub>)</td><td>નુકસાન વિનાનો મહત્તમ current</td></tr>
<tr><td>Power rating P<sub>Z</sub></td><td>મહત્તમ power dissipation: <b>P<sub>Z</sub> = V<sub>Z</sub> × I<sub>Z(max)</sub></b></td></tr>
<tr><td>Zener resistance r<sub>Z</sub></td><td>r<sub>Z</sub> = ΔV<sub>Z</sub> / ΔI<sub>Z</sub>, ખૂબ ઓછો (થોડા ohms); ideal = 0</td></tr>
<tr><td>Tolerance</td><td>V<sub>Z</sub> માં માન્ય ફેરફાર (±5%, ±10%)</td></tr>
</table>""",
          diagram="u3_zener_char", examples=["u3n5"]),

        T("3.4.4 Zener Diode as Voltage Regulator", "3.4.4 Voltage Regulator તરીકે Zener Diode",
          """<p>A <b>voltage regulator</b> keeps the output (load) voltage <b>constant</b> even when the input voltage or the load current changes.</p>
<h4>Circuit</h4>
<ul>
<li>A series resistor <b>R<sub>S</sub></b> is connected between the unregulated input V<sub>in</sub> and the Zener.</li>
<li>The Zener diode is connected in <b>reverse bias</b>, in <b>parallel (shunt)</b> with the load R<sub>L</sub>.</li>
<li>Output voltage V<sub>out</sub> = V<sub>Z</sub> (condition: V<sub>in</sub> &gt; V<sub>Z</sub>).</li>
</ul>
<h4>Equations</h4>
<p><b>I = (V<sub>in</sub> − V<sub>Z</sub>) / R<sub>S</sub></b>, &nbsp; <b>I<sub>L</sub> = V<sub>Z</sub> / R<sub>L</sub></b>, &nbsp; <b>I = I<sub>Z</sub> + I<sub>L</sub></b></p>
<h4>Working</h4>
<p><b>Case 1 – Input voltage changes (line regulation):</b></p>
<ul>
<li>If V<sub>in</sub> <b>increases</b>, the total current I increases. The Zener absorbs the extra current (I<sub>Z</sub> increases), so the extra voltage drops across R<sub>S</sub>. V<sub>out</sub> stays at V<sub>Z</sub>.</li>
<li>If V<sub>in</sub> <b>decreases</b>, I<sub>Z</sub> decreases, but V<sub>out</sub> still remains at V<sub>Z</sub> (as long as I<sub>Z</sub> &gt; I<sub>Z(min)</sub>).</li>
</ul>
<p><b>Case 2 – Load current changes (load regulation):</b></p>
<ul>
<li>If I<sub>L</sub> <b>increases</b> (R<sub>L</sub> decreases), I<sub>Z</sub> decreases by the same amount. Total I stays the same, so the drop across R<sub>S</sub> and V<sub>out</sub> stay constant.</li>
<li>If I<sub>L</sub> <b>decreases</b>, I<sub>Z</sub> increases by the same amount, and V<sub>out</sub> stays constant.</li>
</ul>
<p>Thus the Zener acts like an automatic <b>"current adjuster"</b>, keeping V<sub>out</sub> = V<sub>Z</sub>.</p>
<h4>Design of series resistance</h4>
<p><b>R<sub>S</sub> = (V<sub>in</sub> − V<sub>Z</sub>) / (I<sub>Z</sub> + I<sub>L</sub>)</b></p>
<p><b>Limitations:</b> low efficiency (power wasted in R<sub>S</sub> and Zener), suitable only for small load currents.</p>""",
          """<p><b>Voltage regulator</b> એ input voltage અથવા load current બદલાય તો પણ output (load) voltage ને <b>અચળ</b> રાખે છે.</p>
<h4>Circuit</h4>
<ul>
<li>Unregulated input V<sub>in</sub> અને Zener વચ્ચે series resistor <b>R<sub>S</sub></b> જોડાય છે.</li>
<li>Zener diode ને <b>reverse bias</b> માં, load R<sub>L</sub> ની <b>parallel (shunt)</b> માં જોડાય છે.</li>
<li>Output voltage V<sub>out</sub> = V<sub>Z</sub> (શરત: V<sub>in</sub> &gt; V<sub>Z</sub>).</li>
</ul>
<h4>સમીકરણો</h4>
<p><b>I = (V<sub>in</sub> − V<sub>Z</sub>) / R<sub>S</sub></b>, &nbsp; <b>I<sub>L</sub> = V<sub>Z</sub> / R<sub>L</sub></b>, &nbsp; <b>I = I<sub>Z</sub> + I<sub>L</sub></b></p>
<h4>કાર્ય</h4>
<p><b>Case 1 – Input voltage બદલાય (line regulation):</b></p>
<ul>
<li>જો V<sub>in</sub> <b>વધે</b>, તો કુલ current I વધે છે. Zener વધારાનો current શોષી લે છે (I<sub>Z</sub> વધે), તેથી વધારાનો voltage R<sub>S</sub> પર drop થાય છે. V<sub>out</sub> = V<sub>Z</sub> જ રહે છે.</li>
<li>જો V<sub>in</sub> <b>ઘટે</b>, તો I<sub>Z</sub> ઘટે છે, પરંતુ V<sub>out</sub> હજી V<sub>Z</sub> જ રહે છે (જ્યાં સુધી I<sub>Z</sub> &gt; I<sub>Z(min)</sub>).</li>
</ul>
<p><b>Case 2 – Load current બદલાય (load regulation):</b></p>
<ul>
<li>જો I<sub>L</sub> <b>વધે</b> (R<sub>L</sub> ઘટે), તો I<sub>Z</sub> તેટલો જ ઘટે છે. કુલ I એ જ રહે છે, તેથી R<sub>S</sub> પરનો drop અને V<sub>out</sub> અચળ રહે છે.</li>
<li>જો I<sub>L</sub> <b>ઘટે</b>, તો I<sub>Z</sub> તેટલો જ વધે છે અને V<sub>out</sub> અચળ રહે છે.</li>
</ul>
<p>આમ Zener સ્વયંસંચાલિત <b>"current adjuster"</b> જેવું કામ કરી V<sub>out</sub> = V<sub>Z</sub> રાખે છે.</p>
<h4>Series resistance ની ડિઝાઇન</h4>
<p><b>R<sub>S</sub> = (V<sub>in</sub> − V<sub>Z</sub>) / (I<sub>Z</sub> + I<sub>L</sub>)</b></p>
<p><b>મર્યાદાઓ:</b> ઓછી efficiency (R<sub>S</sub> અને Zener માં power વેડફાય), ફક્ત નાના load current માટે યોગ્ય.</p>""",
          diagram="u3_zener_regulator", examples=["u3n3", "u3n4"]),

        T("3.4.5 Applications of Zener Diode; P-N Diode vs Zener Diode", "3.4.5 Zener Diode ના ઉપયોગો; P-N Diode અને Zener Diode",
          """<h4>Applications</h4>
<ul>
<li><b>Voltage regulator</b> in small DC power supplies.</li>
<li><b>Reference voltage source</b> in ADCs, comparators and power supplies.</li>
<li><b>Over-voltage protection</b> – conducts and protects the circuit when voltage exceeds V<sub>Z</sub>.</li>
<li><b>Wave shaping / clipping</b> circuits.</li>
<li><b>Meter protection</b> in multimeters.</li>
<li>Voltage shifting (level shifter) circuits.</li>
</ul>
<h4>Comparison</h4>
<table>
<tr><th>Point</th><th>P-N junction diode</th><th>Zener diode</th></tr>
<tr><td>Doping</td><td>Normal (light)</td><td>Heavy</td></tr>
<tr><td>Depletion layer</td><td>Wider</td><td>Very thin</td></tr>
<tr><td>Normal operation</td><td>Forward bias</td><td>Reverse bias (breakdown)</td></tr>
<tr><td>Breakdown</td><td>Damages the diode</td><td>Normal working region; not damaged</td></tr>
<tr><td>Breakdown voltage</td><td>High (50–1000 V)</td><td>Low and sharp (2.4–200 V)</td></tr>
<tr><td>Symbol</td><td>Straight bar</td><td>Bent ("Z") bar</td></tr>
<tr><td>Main use</td><td>Rectifier, switch</td><td>Voltage regulator, reference</td></tr>
</table>""",
          """<h4>ઉપયોગો</h4>
<ul>
<li>નાના DC power supply માં <b>Voltage regulator</b>.</li>
<li>ADC, comparator અને power supply માં <b>Reference voltage source</b>.</li>
<li><b>Over-voltage protection</b> – voltage V<sub>Z</sub> થી વધે ત્યારે conduction કરી circuit ને રક્ષણ આપે.</li>
<li><b>Wave shaping / clipping</b> circuits.</li>
<li>Multimeter માં <b>Meter protection</b>.</li>
<li>Voltage shifting (level shifter) circuits.</li>
</ul>
<h4>સરખામણી</h4>
<table>
<tr><th>મુદ્દો</th><th>P-N junction diode</th><th>Zener diode</th></tr>
<tr><td>Doping</td><td>સામાન્ય (ઓછું)</td><td>વધુ</td></tr>
<tr><td>Depletion layer</td><td>વધુ પહોળું</td><td>ખૂબ પાતળું</td></tr>
<tr><td>સામાન્ય કાર્ય</td><td>Forward bias</td><td>Reverse bias (breakdown)</td></tr>
<tr><td>Breakdown</td><td>Diode ને નુકસાન કરે</td><td>સામાન્ય કાર્ય region; નુકસાન નહીં</td></tr>
<tr><td>Breakdown voltage</td><td>વધુ (50–1000 V)</td><td>ઓછો અને તીક્ષ્ણ (2.4–200 V)</td></tr>
<tr><td>Symbol</td><td>સીધો bar</td><td>વાળેલો ("Z") bar</td></tr>
<tr><td>મુખ્ય ઉપયોગ</td><td>Rectifier, switch</td><td>Voltage regulator, reference</td></tr>
</table>"""),

        T("Key Points – 3.4", "મુખ્ય મુદ્દા – 3.4",
          """<ul>
<li>Zener = <b>heavily doped Si diode</b> designed to work in <b>reverse breakdown</b> without damage.</li>
<li>Zener breakdown (&lt; 5 V, field ionisation, −ve temp. coeff.) and Avalanche breakdown (&gt; 6 V, impact ionisation, +ve temp. coeff.).</li>
<li>In breakdown, V<sub>Z</sub> remains constant while I<sub>Z</sub> varies from I<sub>Z(min)</sub> to I<sub>Z(max)</sub>.</li>
<li><b>P<sub>Z</sub> = V<sub>Z</sub> × I<sub>Z(max)</sub></b>.</li>
<li>Regulator: R<sub>S</sub> in series, Zener in shunt with load, reverse biased; <b>I = I<sub>Z</sub> + I<sub>L</sub></b>, <b>R<sub>S</sub> = (V<sub>in</sub> − V<sub>Z</sub>)/(I<sub>Z</sub> + I<sub>L</sub>)</b>.</li>
<li>Uses: voltage regulator, reference, over-voltage protection, clipping.</li>
</ul>""",
          """<ul>
<li>Zener = નુકસાન વિના <b>reverse breakdown</b> માં કામ કરવા બનાવેલો <b>વધુ doped Si diode</b>.</li>
<li>Zener breakdown (&lt; 5 V, field ionisation, −ve temp. coeff.) અને Avalanche breakdown (&gt; 6 V, impact ionisation, +ve temp. coeff.).</li>
<li>Breakdown માં I<sub>Z</sub> એ I<sub>Z(min)</sub> થી I<sub>Z(max)</sub> સુધી બદલાય છતાં V<sub>Z</sub> અચળ રહે.</li>
<li><b>P<sub>Z</sub> = V<sub>Z</sub> × I<sub>Z(max)</sub></b>.</li>
<li>Regulator: R<sub>S</sub> series માં, Zener load ની shunt માં, reverse bias; <b>I = I<sub>Z</sub> + I<sub>L</sub></b>, <b>R<sub>S</sub> = (V<sub>in</sub> − V<sub>Z</sub>)/(I<sub>Z</sub> + I<sub>L</sub>)</b>.</li>
<li>ઉપયોગો: voltage regulator, reference, over-voltage protection, clipping.</li>
</ul>""", key=True),
    ],
}

# =====================================================================================
SEC_3_5 = {
    "title": {"en": "3.5 Special Purpose Diodes", "gu": "3.5 Special Purpose Diodes"},
    "items": [
        T("3.5.1 Varactor Diode (Varicap)", "3.5.1 Varactor Diode (Varicap)",
          """<p><b>Definition:</b> A varactor diode is a specially designed P-N junction diode whose <b>junction capacitance changes with the applied reverse voltage</b>. It works as a <b>voltage-controlled variable capacitor</b>. Other names: <b>varicap, tuning diode, voltage-variable capacitor (VVC)</b>.</p>
<h4>Symbol</h4>
<p>A diode symbol with a <b>capacitor symbol</b> (two parallel plates) at the cathode side.</p>
<h4>Construction</h4>
<ul>
<li>P-N junction made of <b>silicon</b> (or GaAs) with a specially controlled doping profile so the capacitance changes widely with voltage.</li>
<li>The P and N regions act as the <b>two plates</b>, and the depletion layer acts as the <b>dielectric</b>.</li>
</ul>
<h4>Working (always in reverse bias)</h4>
<ul>
<li>Junction (transition) capacitance: <b>C<sub>T</sub> = ε A / W</b>, where A = junction area and W = depletion layer width.</li>
<li>When <b>reverse voltage increases</b>, depletion width W <b>increases</b> → plates move further apart → <b>capacitance decreases</b>.</li>
<li>When reverse voltage decreases, W decreases → capacitance increases.</li>
<li>For an abrupt junction: <b>C<sub>T</sub> ∝ 1 / √V<sub>R</sub></b> (more exactly 1/√(V₀ + V<sub>R</sub>)).</li>
<li>Typical range: a few pF to about 100 pF.</li>
</ul>
<h4>Characteristics</h4>
<p>A graph of C<sub>T</sub> against V<sub>R</sub>: capacitance is high at low reverse voltage and falls as the reverse voltage increases (see diagram).</p>
<h4>Applications</h4>
<ul>
<li><b>Electronic tuning</b> in radio and TV receivers (replacing the gang capacitor).</li>
<li><b>Voltage-controlled oscillators (VCO)</b> and PLL circuits.</li>
<li><b>Automatic frequency control (AFC)</b>.</li>
<li><b>FM modulators</b>, frequency multipliers, parametric amplifiers.</li>
</ul>""",
          """<p><b>વ્યાખ્યા:</b> Varactor diode એ ખાસ બનાવેલો P-N junction diode છે જેની <b>junction capacitance લગાવેલા reverse voltage સાથે બદલાય</b> છે. તે <b>voltage-controlled variable capacitor</b> તરીકે કામ કરે છે. બીજા નામ: <b>varicap, tuning diode, voltage-variable capacitor (VVC)</b>.</p>
<h4>Symbol</h4>
<p>Cathode બાજુએ <b>capacitor symbol</b> (બે સમાંતર plates) સાથેનો diode symbol.</p>
<h4>રચના</h4>
<ul>
<li><b>Silicon</b> (અથવા GaAs) નું P-N junction, ખાસ નિયંત્રિત doping સાથે જેથી voltage સાથે capacitance વધુ બદલાય.</li>
<li>P અને N regions <b>બે plates</b> તરીકે અને depletion layer <b>Dielectric</b> તરીકે કામ કરે છે.</li>
</ul>
<h4>કાર્ય (હંમેશા reverse bias માં)</h4>
<ul>
<li>Junction (transition) capacitance: <b>C<sub>T</sub> = ε A / W</b>, જ્યાં A = junction area અને W = depletion layer ની પહોળાઈ.</li>
<li>જ્યારે <b>reverse voltage વધે</b>, ત્યારે depletion width W <b>વધે</b> → plates વચ્ચેનું અંતર વધે → <b>capacitance ઘટે</b>.</li>
<li>Reverse voltage ઘટે ત્યારે W ઘટે → capacitance વધે.</li>
<li>Abrupt junction માટે: <b>C<sub>T</sub> ∝ 1 / √V<sub>R</sub></b> (વધુ ચોક્કસ રીતે 1/√(V₀ + V<sub>R</sub>)).</li>
<li>સામાન્ય range: થોડા pF થી આશરે 100 pF.</li>
</ul>
<h4>Characteristics</h4>
<p>C<sub>T</sub> વિરુદ્ધ V<sub>R</sub> નો આલેખ: ઓછા reverse voltage પર capacitance વધુ અને reverse voltage વધતાં ઘટે છે (આકૃતિ જુઓ).</p>
<h4>ઉપયોગો</h4>
<ul>
<li>Radio અને TV receivers માં <b>Electronic tuning</b> (gang capacitor ની જગ્યાએ).</li>
<li><b>Voltage-controlled oscillators (VCO)</b> અને PLL circuits.</li>
<li><b>Automatic frequency control (AFC)</b>.</li>
<li><b>FM modulators</b>, frequency multipliers, parametric amplifiers.</li>
</ul>""",
          diagram="u3_varactor"),

        T("3.5.2 Photodiode", "3.5.2 Photodiode",
          """<p><b>Definition:</b> A photodiode is a P-N junction diode that is operated in <b>reverse bias</b> and whose <b>reverse current increases with the intensity of light</b> falling on the junction. It converts <b>light energy into electrical current</b>.</p>
<h4>Symbol</h4>
<p>A diode symbol with <b>two arrows pointing towards</b> the diode (light coming in).</p>
<h4>Construction</h4>
<ul>
<li>P-N junction made of <b>silicon</b> (also Ge, InGaAs) enclosed in a plastic or metal case.</li>
<li>A <b>transparent window or lens</b> allows light to fall exactly on the junction.</li>
<li>The rest of the body is covered (painted black) so light reaches only the junction.</li>
</ul>
<h4>Working</h4>
<ol>
<li>The photodiode is <b>reverse biased</b>, so only a very small <b>dark current</b> (minority carrier current) flows when there is no light.</li>
<li>When light (photons) with enough energy falls on the junction, it breaks covalent bonds and generates <b>electron-hole pairs</b>.</li>
<li>These extra minority carriers are swept across the junction by the reverse voltage, so the <b>reverse current increases</b>.</li>
<li>Greater light intensity → more electron-hole pairs → <b>larger reverse current</b>. The current is almost proportional to the light intensity.</li>
</ol>
<h4>Characteristics</h4>
<p>Graph of reverse current I<sub>R</sub> against reverse voltage V<sub>R</sub> for different light intensities (L1 &lt; L2 &lt; L3). The current is almost independent of voltage and depends mainly on light intensity (see diagram).</p>
<h4>Applications</h4>
<ul>
<li>Light detectors, <b>automatic street-light</b> controls and light meters.</li>
<li><b>Optical fibre communication</b> receivers.</li>
<li><b>TV remote-control receivers</b>, smoke detectors, barcode scanners.</li>
<li>Object counters, burglar alarms, CD/DVD players.</li>
</ul>""",
          """<p><b>વ્યાખ્યા:</b> Photodiode એ <b>reverse bias</b> માં ચલાવાતો P-N junction diode છે, જેનો <b>reverse current junction પર પડતા પ્રકાશની તીવ્રતા સાથે વધે</b> છે. તે <b>પ્રકાશ ઊર્જાને વિદ્યુત current</b> માં ફેરવે છે.</p>
<h4>Symbol</h4>
<p>Diode તરફ <b>અંદર આવતા બે arrows</b> (પ્રકાશ અંદર આવે છે) સાથેનો diode symbol.</p>
<h4>રચના</h4>
<ul>
<li><b>Silicon</b> (Ge, InGaAs પણ) નું P-N junction, plastic અથવા metal case માં બંધ.</li>
<li><b>પારદર્શક window અથવા lens</b> થી પ્રકાશ બરાબર junction પર પડે છે.</li>
<li>બાકીનો body ઢાંકેલો (કાળો રંગ) હોય છે જેથી પ્રકાશ ફક્ત junction સુધી પહોંચે.</li>
</ul>
<h4>કાર્ય</h4>
<ol>
<li>Photodiode <b>reverse biased</b> હોય છે, તેથી પ્રકાશ ન હોય ત્યારે ફક્ત ખૂબ નાનો <b>Dark current</b> (minority carrier current) વહે છે.</li>
<li>જ્યારે પૂરતી ઊર્જાવાળો પ્રકાશ (photons) junction પર પડે, ત્યારે તે covalent bonds તોડી <b>electron-hole pairs</b> બનાવે છે.</li>
<li>આ વધારાના minority carriers reverse voltage થી junction પાર ધકેલાય છે, તેથી <b>reverse current વધે</b> છે.</li>
<li>વધુ પ્રકાશની તીવ્રતા → વધુ electron-hole pairs → <b>વધુ reverse current</b>. Current લગભગ પ્રકાશની તીવ્રતાના સમપ્રમાણમાં હોય છે.</li>
</ol>
<h4>Characteristics</h4>
<p>જુદી જુદી પ્રકાશ તીવ્રતા (L1 &lt; L2 &lt; L3) માટે reverse current I<sub>R</sub> વિરુદ્ધ reverse voltage V<sub>R</sub> નો આલેખ. Current લગભગ voltage થી સ્વતંત્ર છે અને મુખ્યત્વે પ્રકાશની તીવ્રતા પર આધાર રાખે છે (આકૃતિ જુઓ).</p>
<h4>ઉપયોગો</h4>
<ul>
<li>Light detectors, <b>automatic street-light</b> નિયંત્રણ અને light meters.</li>
<li><b>Optical fibre communication</b> receivers.</li>
<li><b>TV remote-control receivers</b>, smoke detectors, barcode scanners.</li>
<li>Object counters, burglar alarms, CD/DVD players.</li>
</ul>""",
          diagram="u3_photodiode"),

        T("3.5.3 Light Emitting Diode (LED)", "3.5.3 Light Emitting Diode (LED)",
          """<p><b>Definition:</b> An LED is a P-N junction diode that <b>emits light when it is forward biased</b>. It converts <b>electrical energy into light energy</b> (electroluminescence).</p>
<h4>Symbol</h4>
<p>A diode symbol with <b>two arrows pointing away</b> from the diode (light going out).</p>
<h4>Construction</h4>
<ul>
<li>Made from <b>compound semiconductors</b> (not Si or Ge) such as GaAs, GaAsP, GaP, InGaN.</li>
<li>The P-N junction is placed in a <b>transparent epoxy dome</b> which acts as a lens.</li>
<li>A <b>reflector cup</b> directs the light upward.</li>
<li><b>Anode = longer leg</b>; cathode = shorter leg and <b>flat edge</b> on the body.</li>
</ul>
<h4>Working</h4>
<ol>
<li>When forward biased, electrons from the N-side and holes from the P-side move towards the junction.</li>
<li>At the junction, free electrons (conduction band) <b>recombine</b> with holes (valence band).</li>
<li>During recombination the electron falls to a lower energy level and releases the energy difference as a <b>photon (light)</b>.</li>
<li>The <b>colour (wavelength)</b> of light depends on the <b>energy gap</b> of the material: λ = hc / E<sub>g</sub>.</li>
</ol>
<p><i>Why not Si/Ge?</i> In Si and Ge the energy is released mainly as <b>heat</b> (indirect band gap), not light.</p>
<h4>Materials and colours</h4>
<table>
<tr><th>Material</th><th>Colour</th><th>Typical V<sub>F</sub></th></tr>
<tr><td>GaAs (Gallium Arsenide)</td><td>Infrared (invisible)</td><td>≈ 1.2 V</td></tr>
<tr><td>GaAsP (Gallium Arsenide Phosphide)</td><td>Red, orange, yellow</td><td>1.8 – 2.1 V</td></tr>
<tr><td>GaP (Gallium Phosphide)</td><td>Green (also red)</td><td>≈ 2.2 V</td></tr>
<tr><td>InGaN (Indium Gallium Nitride)</td><td>Blue, green, white (with phosphor)</td><td>3.0 – 3.3 V</td></tr>
</table>
<h4>Characteristics</h4>
<ul>
<li>Forward voltage <b>1.8 V to 3.3 V</b> (higher than Si diode), current typically <b>10–20 mA</b>.</li>
<li>Light output (intensity) is almost <b>proportional to forward current</b>.</li>
<li>Low reverse breakdown voltage (about <b>5 V</b>) → never apply large reverse voltage.</li>
<li>A <b>series resistor</b> is required: <b>R = (V<sub>S</sub> − V<sub>F</sub>) / I<sub>F</sub></b>.</li>
</ul>
<h4>Advantages</h4>
<p>Low power, long life (≈ 50,000 hours), small size, fast switching, rugged, available in many colours, no warm-up time.</p>
<h4>Applications</h4>
<p>Indicator lamps, <b>7-segment displays</b>, LED TV backlight and screens, traffic signals, LED bulbs and lighting, <b>IR remote controls</b> (IR LED), optocouplers, optical fibre transmitters.</p>""",
          """<p><b>વ્યાખ્યા:</b> LED એ P-N junction diode છે જે <b>forward bias થતાં પ્રકાશ ઉત્સર્જિત</b> કરે છે. તે <b>વિદ્યુત ઊર્જાને પ્રકાશ ઊર્જા</b> માં ફેરવે છે (electroluminescence).</p>
<h4>Symbol</h4>
<p>Diode થી <b>બહાર જતા બે arrows</b> (પ્રકાશ બહાર જાય છે) સાથેનો diode symbol.</p>
<h4>રચના</h4>
<ul>
<li>Si કે Ge નહીં પરંતુ GaAs, GaAsP, GaP, InGaN જેવા <b>Compound semiconductors</b> માંથી બને છે.</li>
<li>P-N junction ને <b>પારદર્શક epoxy dome</b> માં મૂકાય છે, જે lens તરીકે કામ કરે છે.</li>
<li><b>Reflector cup</b> પ્રકાશને ઉપર તરફ મોકલે છે.</li>
<li><b>Anode = લાંબો પગ</b>; cathode = ટૂંકો પગ અને body પર <b>સપાટ ધાર (flat edge)</b>.</li>
</ul>
<h4>કાર્ય</h4>
<ol>
<li>Forward bias થતાં N-side ના electrons અને P-side ના holes junction તરફ જાય છે.</li>
<li>Junction પર free electrons (conduction band) holes (valence band) સાથે <b>Recombine</b> થાય છે.</li>
<li>Recombination વખતે electron નીચા energy level માં આવે છે અને ઊર્જાનો તફાવત <b>Photon (પ્રકાશ)</b> તરીકે છોડે છે.</li>
<li>પ્રકાશનો <b>રંગ (wavelength)</b> material ના <b>energy gap</b> પર આધાર રાખે છે: λ = hc / E<sub>g</sub>.</li>
</ol>
<p><i>Si/Ge કેમ નહીં?</i> Si અને Ge માં ઊર્જા મુખ્યત્વે પ્રકાશ નહીં પરંતુ <b>ઉષ્મા</b> તરીકે છૂટે છે (indirect band gap).</p>
<h4>Materials અને રંગો</h4>
<table>
<tr><th>Material</th><th>રંગ</th><th>સામાન્ય V<sub>F</sub></th></tr>
<tr><td>GaAs (Gallium Arsenide)</td><td>Infrared (અદ્રશ્ય)</td><td>≈ 1.2 V</td></tr>
<tr><td>GaAsP (Gallium Arsenide Phosphide)</td><td>લાલ, નારંગી, પીળો</td><td>1.8 – 2.1 V</td></tr>
<tr><td>GaP (Gallium Phosphide)</td><td>લીલો (લાલ પણ)</td><td>≈ 2.2 V</td></tr>
<tr><td>InGaN (Indium Gallium Nitride)</td><td>વાદળી, લીલો, સફેદ (phosphor સાથે)</td><td>3.0 – 3.3 V</td></tr>
</table>
<h4>Characteristics</h4>
<ul>
<li>Forward voltage <b>1.8 V થી 3.3 V</b> (Si diode કરતાં વધુ), current સામાન્ય રીતે <b>10–20 mA</b>.</li>
<li>પ્રકાશ (intensity) લગભગ <b>forward current ના સમપ્રમાણમાં</b> હોય છે.</li>
<li>ઓછો reverse breakdown voltage (આશરે <b>5 V</b>) → ક્યારેય વધુ reverse voltage ન લગાવો.</li>
<li><b>Series resistor</b> જરૂરી છે: <b>R = (V<sub>S</sub> − V<sub>F</sub>) / I<sub>F</sub></b>.</li>
</ul>
<h4>ફાયદા</h4>
<p>ઓછો power, લાંબું આયુષ્ય (≈ 50,000 કલાક), નાનું કદ, ઝડપી switching, મજબૂત, ઘણા રંગોમાં ઉપલબ્ધ, warm-up સમય નહીં.</p>
<h4>ઉપયોગો</h4>
<p>Indicator lamps, <b>7-segment displays</b>, LED TV backlight અને screens, traffic signals, LED bulbs અને lighting, <b>IR remote controls</b> (IR LED), optocouplers, optical fibre transmitters.</p>""",
          diagram="u3_led", examples=["u3n2"]),

        T("3.5.4 Multicolour LED", "3.5.4 Multicolour LED",
          """<p><b>Definition:</b> A multicolour LED contains <b>two or more LED chips of different colours in a single package</b>. By controlling which chip is ON (and its current), different colours can be obtained.</p>
<h4>1. Bi-colour LED (2 leads)</h4>
<ul>
<li>Two LEDs (usually <b>red and green</b>) connected in <b>inverse parallel (anti-parallel)</b> – anode of one to the cathode of the other.</li>
<li>Current A → B: the red LED glows. Current B → A: the green LED glows.</li>
<li>If the polarity is switched quickly (AC), both appear ON → <b>yellow/orange</b>.</li>
<li>Used for polarity indication, charging/charged status.</li>
</ul>
<h4>2. Tri-colour LED (3 leads)</h4>
<ul>
<li>Red and green chips with a <b>common cathode</b> (or common anode) and two separate leads.</li>
<li>Red alone, green alone, or both ON together → <b>third colour (yellow/amber)</b>.</li>
</ul>
<h4>3. RGB LED (4 leads)</h4>
<ul>
<li>Three chips: <b>Red, Green and Blue</b> with one common lead – <b>common cathode</b> (common −, longest leg) or <b>common anode</b>.</li>
<li>Primary colour mixing: R + G = Yellow, R + B = Magenta, G + B = Cyan, <b>R + G + B = White</b>.</li>
<li>By varying the current (brightness) of each chip using <b>PWM</b>, <b>millions of colours</b> can be produced.</li>
</ul>
<h4>Applications</h4>
<p>Status indicators (battery charging red → green), decorative and mood lighting, RGB strips, full-colour LED displays and video walls, gaming keyboards, stage lighting.</p>""",
          """<p><b>વ્યાખ્યા:</b> Multicolour LED માં <b>એક જ package માં જુદા જુદા રંગના બે કે વધુ LED chips</b> હોય છે. કયો chip ON છે (અને તેનો current) નિયંત્રિત કરીને જુદા જુદા રંગ મેળવી શકાય છે.</p>
<h4>1. Bi-colour LED (2 leads)</h4>
<ul>
<li>બે LEDs (સામાન્ય રીતે <b>લાલ અને લીલો</b>) <b>inverse parallel (anti-parallel)</b> માં જોડેલા – એકનો anode બીજાના cathode સાથે.</li>
<li>Current A → B: લાલ LED ચમકે. Current B → A: લીલો LED ચમકે.</li>
<li>Polarity ઝડપથી બદલાય (AC) તો બંને ON દેખાય → <b>પીળો/નારંગી</b>.</li>
<li>Polarity indication, charging/charged status માટે વપરાય.</li>
</ul>
<h4>2. Tri-colour LED (3 leads)</h4>
<ul>
<li>લાલ અને લીલા chips, <b>common cathode</b> (અથવા common anode) અને બે અલગ leads સાથે.</li>
<li>ફક્ત લાલ, ફક્ત લીલો, અથવા બંને એકસાથે ON → <b>ત્રીજો રંગ (પીળો/amber)</b>.</li>
</ul>
<h4>3. RGB LED (4 leads)</h4>
<ul>
<li>ત્રણ chips: <b>Red, Green અને Blue</b>, એક common lead સાથે – <b>common cathode</b> (common −, સૌથી લાંબો પગ) અથવા <b>common anode</b>.</li>
<li>પ્રાથમિક રંગોનું મિશ્રણ: R + G = પીળો (Yellow), R + B = Magenta, G + B = Cyan, <b>R + G + B = સફેદ (White)</b>.</li>
<li><b>PWM</b> થી દરેક chip નો current (તેજ) બદલીને <b>લાખો રંગો</b> મેળવી શકાય.</li>
</ul>
<h4>ઉપયોગો</h4>
<p>Status indicators (battery charging લાલ → લીલો), શણગાર અને mood lighting, RGB strips, full-colour LED displays અને video walls, gaming keyboards, stage lighting.</p>""",
          diagram="u3_multicolour_led"),

        T("3.5.5 Comparison of Special Diodes", "3.5.5 Special Diodes ની સરખામણી",
          """<table>
<tr><th>Point</th><th>Zener</th><th>Varactor</th><th>Photodiode</th><th>LED</th></tr>
<tr><td>Bias</td><td>Reverse (breakdown)</td><td>Reverse</td><td>Reverse</td><td>Forward</td></tr>
<tr><td>Principle</td><td>Constant V<sub>Z</sub> in breakdown</td><td>C<sub>T</sub> changes with V<sub>R</sub></td><td>Light → current</td><td>Current → light</td></tr>
<tr><td>Energy conversion</td><td>—</td><td>—</td><td>Light → electrical</td><td>Electrical → light</td></tr>
<tr><td>Material</td><td>Si (heavily doped)</td><td>Si, GaAs</td><td>Si, Ge, InGaAs</td><td>GaAs, GaAsP, GaP, InGaN</td></tr>
<tr><td>Symbol feature</td><td>Bent "Z" bar</td><td>Capacitor plates</td><td>Arrows inward</td><td>Arrows outward</td></tr>
<tr><td>Main use</td><td>Voltage regulator</td><td>Electronic tuning, VCO</td><td>Light detector, receiver</td><td>Indicator, display, lighting</td></tr>
</table>""",
          """<table>
<tr><th>મુદ્દો</th><th>Zener</th><th>Varactor</th><th>Photodiode</th><th>LED</th></tr>
<tr><td>Bias</td><td>Reverse (breakdown)</td><td>Reverse</td><td>Reverse</td><td>Forward</td></tr>
<tr><td>સિદ્ધાંત</td><td>Breakdown માં અચળ V<sub>Z</sub></td><td>V<sub>R</sub> સાથે C<sub>T</sub> બદલાય</td><td>પ્રકાશ → current</td><td>Current → પ્રકાશ</td></tr>
<tr><td>ઊર્જા રૂપાંતર</td><td>—</td><td>—</td><td>પ્રકાશ → વિદ્યુત</td><td>વિદ્યુત → પ્રકાશ</td></tr>
<tr><td>Material</td><td>Si (વધુ doped)</td><td>Si, GaAs</td><td>Si, Ge, InGaAs</td><td>GaAs, GaAsP, GaP, InGaN</td></tr>
<tr><td>Symbol લક્ષણ</td><td>વાળેલો "Z" bar</td><td>Capacitor plates</td><td>અંદર તરફ arrows</td><td>બહાર તરફ arrows</td></tr>
<tr><td>મુખ્ય ઉપયોગ</td><td>Voltage regulator</td><td>Electronic tuning, VCO</td><td>Light detector, receiver</td><td>Indicator, display, lighting</td></tr>
</table>"""),

        T("Key Points – 3.5", "મુખ્ય મુદ્દા – 3.5",
          """<ul>
<li><b>Varactor:</b> reverse biased; C<sub>T</sub> = εA/W; V<sub>R</sub> ↑ → W ↑ → C ↓; used for electronic tuning, VCO, AFC.</li>
<li><b>Photodiode:</b> reverse biased; light → electron-hole pairs → reverse current ∝ light intensity; dark current when no light.</li>
<li><b>LED:</b> forward biased; recombination releases photons; colour depends on energy gap; V<sub>F</sub> 1.8–3.3 V, I<sub>F</sub> 10–20 mA; series R = (V<sub>S</sub> − V<sub>F</sub>)/I<sub>F</sub>.</li>
<li>LED materials: GaAs (IR), GaAsP (red/yellow), GaP (green), InGaN (blue/white).</li>
<li><b>Multicolour LED:</b> bi-colour (2 leads, anti-parallel), tri-colour (3 leads), RGB (4 leads, common anode/cathode).</li>
<li>Photodiode symbol arrows point <b>in</b>; LED arrows point <b>out</b>.</li>
</ul>""",
          """<ul>
<li><b>Varactor:</b> reverse biased; C<sub>T</sub> = εA/W; V<sub>R</sub> ↑ → W ↑ → C ↓; electronic tuning, VCO, AFC માં વપરાય.</li>
<li><b>Photodiode:</b> reverse biased; પ્રકાશ → electron-hole pairs → reverse current ∝ પ્રકાશની તીવ્રતા; પ્રકાશ ન હોય ત્યારે dark current.</li>
<li><b>LED:</b> forward biased; recombination થી photons છૂટે; રંગ energy gap પર આધાર રાખે; V<sub>F</sub> 1.8–3.3 V, I<sub>F</sub> 10–20 mA; series R = (V<sub>S</sub> − V<sub>F</sub>)/I<sub>F</sub>.</li>
<li>LED materials: GaAs (IR), GaAsP (લાલ/પીળો), GaP (લીલો), InGaN (વાદળી/સફેદ).</li>
<li><b>Multicolour LED:</b> bi-colour (2 leads, anti-parallel), tri-colour (3 leads), RGB (4 leads, common anode/cathode).</li>
<li>Photodiode symbol ના arrows <b>અંદર</b>; LED ના arrows <b>બહાર</b>.</li>
</ul>""", key=True),
    ],
}

# =====================================================================================
SEC_3_6 = {
    "title": {"en": "3.6 Rectifiers", "gu": "3.6 Rectifiers"},
    "items": [
        T("3.6.1 Need of Rectifier and Definition", "3.6.1 Rectifier ની જરૂરિયાત અને વ્યાખ્યા",
          """<h4>Need</h4>
<ul>
<li>The electricity supplied to homes is <b>AC</b> (230 V, 50 Hz in India).</li>
<li>Almost all electronic circuits – mobiles, computers, TVs, amplifiers, ICs – need a <b>steady DC</b> supply of low voltage (5 V, 9 V, 12 V…).</li>
<li>Batteries are costly and need replacement, so DC is obtained from the AC mains using a <b>DC power supply</b>.</li>
<li>The heart of a DC power supply is the <b>rectifier</b>.</li>
</ul>
<h4>Definition</h4>
<p>A <b>rectifier</b> is a circuit that converts <b>alternating current (AC) into pulsating direct current (DC)</b>. The process is called <b>rectification</b>. It uses the <b>unidirectional</b> property of the diode (conducts only in forward bias).</p>
<h4>Blocks of a regulated DC power supply</h4>
<p>AC mains → <b>Step-down transformer</b> → <b>Rectifier</b> → <b>Filter</b> → <b>Regulator</b> → DC output</p>
<ul>
<li><b>Transformer:</b> reduces 230 V AC to the required low AC voltage.</li>
<li><b>Rectifier:</b> converts AC to pulsating DC.</li>
<li><b>Filter (capacitor):</b> removes ripples (AC component) and smooths the DC.</li>
<li><b>Regulator (Zener / IC 78xx):</b> keeps output DC constant.</li>
</ul>""",
          """<h4>જરૂરિયાત</h4>
<ul>
<li>ઘરોમાં મળતી વીજળી <b>AC</b> છે (ભારતમાં 230 V, 50 Hz).</li>
<li>લગભગ બધા electronic circuits – mobiles, computers, TVs, amplifiers, ICs – ને ઓછા voltage (5 V, 9 V, 12 V…) ના <b>સ્થિર DC</b> supply ની જરૂર પડે છે.</li>
<li>Batteries મોંઘી છે અને બદલવી પડે છે, તેથી <b>DC power supply</b> દ્વારા AC mains માંથી DC મેળવાય છે.</li>
<li>DC power supply નું હૃદય <b>Rectifier</b> છે.</li>
</ul>
<h4>વ્યાખ્યા</h4>
<p><b>Rectifier</b> એ એવો circuit છે જે <b>alternating current (AC) ને pulsating direct current (DC)</b> માં ફેરવે છે. આ પ્રક્રિયાને <b>Rectification</b> કહે છે. તે diode ના <b>Unidirectional</b> ગુણધર્મ (ફક્ત forward bias માં conduction) નો ઉપયોગ કરે છે.</p>
<h4>Regulated DC power supply ના blocks</h4>
<p>AC mains → <b>Step-down transformer</b> → <b>Rectifier</b> → <b>Filter</b> → <b>Regulator</b> → DC output</p>
<ul>
<li><b>Transformer:</b> 230 V AC ને જરૂરી ઓછા AC voltage માં ઘટાડે.</li>
<li><b>Rectifier:</b> AC ને pulsating DC માં ફેરવે.</li>
<li><b>Filter (capacitor):</b> ripples (AC ઘટક) દૂર કરી DC ને સરળ (smooth) બનાવે.</li>
<li><b>Regulator (Zener / IC 78xx):</b> output DC ને અચળ રાખે.</li>
</ul>"""),

        T("3.6.2 Types of Rectifiers", "3.6.2 Rectifiers ના પ્રકાર",
          """<ol>
<li><b>Half-wave rectifier (HWR):</b> uses <b>one diode</b>; conducts only during one half-cycle (positive) of AC input.</li>
<li><b>Full-wave rectifier (FWR):</b> conducts during <b>both half-cycles</b>. Two types:
<ul>
<li><b>Centre-tapped full-wave rectifier</b> – uses <b>two diodes</b> and a <b>centre-tapped transformer</b>.</li>
<li><b>Bridge rectifier</b> – uses <b>four diodes</b> in a bridge; no centre tap needed.</li>
</ul></li>
</ol>
<p>Rectifiers can also be classified by phase (single-phase / three-phase) and by control (uncontrolled using diodes / controlled using SCRs). In this syllabus we study <b>single-phase uncontrolled</b> rectifiers.</p>""",
          """<ol>
<li><b>Half-wave rectifier (HWR):</b> <b>એક diode</b> વાપરે છે; AC input ના ફક્ત એક half-cycle (positive) દરમિયાન conduction કરે.</li>
<li><b>Full-wave rectifier (FWR):</b> <b>બંને half-cycles</b> દરમિયાન conduction કરે. બે પ્રકાર:
<ul>
<li><b>Centre-tapped full-wave rectifier</b> – <b>બે diodes</b> અને <b>centre-tapped transformer</b> વાપરે.</li>
<li><b>Bridge rectifier</b> – bridge માં <b>ચાર diodes</b> વાપરે; centre tap ની જરૂર નથી.</li>
</ul></li>
</ol>
<p>Rectifiers ને phase (single-phase / three-phase) અને control (diodes વાળા uncontrolled / SCRs વાળા controlled) પ્રમાણે પણ વર્ગીકૃત કરી શકાય. આ syllabus માં આપણે <b>single-phase uncontrolled</b> rectifiers ભણીએ છીએ.</p>"""),

        T("3.6.3 Performance Parameters of Rectifiers", "3.6.3 Rectifiers ના Performance Parameters",
          """<p>V<sub>m</sub> = peak secondary voltage, I<sub>m</sub> = peak load current = V<sub>m</sub> / (r<sub>f</sub> + R<sub>L</sub>), where r<sub>f</sub> = diode forward resistance.</p>
<h4>1. Average (DC) value – V<sub>dc</sub>, I<sub>dc</sub></h4>
<p>The average value of the pulsating output over one cycle. This is what a DC voltmeter reads.</p>
<h4>2. RMS value – V<sub>rms</sub>, I<sub>rms</sub></h4>
<p>Effective value of the output, which includes both DC and AC components.</p>
<h4>3. Ripple factor (r or γ)</h4>
<p>The ratio of the RMS value of the AC component (ripple) to the DC value of the output. It shows how pure the DC is. <b>Smaller is better</b>.</p>
<p><b>r = V<sub>ac(rms)</sub> / V<sub>dc</sub> = √[(I<sub>rms</sub> / I<sub>dc</sub>)² − 1]</b></p>
<h4>4. Rectification efficiency (η)</h4>
<p>The ratio of DC output power to AC input power. <b>Higher is better</b>.</p>
<p><b>η = P<sub>dc</sub> / P<sub>ac</sub> = I<sub>dc</sub>² R<sub>L</sub> / [I<sub>rms</sub>² (r<sub>f</sub> + R<sub>L</sub>)] × 100%</b></p>
<h4>5. Peak Inverse Voltage (PIV)</h4>
<p>The maximum reverse voltage that appears across a diode when it is <b>not conducting</b>. The diode's PIV rating must be <b>greater</b> than this value.</p>
<h4>6. Ripple frequency</h4>
<p>Frequency of the pulsating output (50 Hz for HWR, 100 Hz for FWR with 50 Hz mains).</p>
<h4>7. Transformer Utilisation Factor (TUF)</h4>
<p>TUF = DC power delivered to the load / AC VA rating of transformer secondary. Higher TUF means the transformer is used better.</p>
<h4>8. Form factor and peak factor</h4>
<p>Form factor = V<sub>rms</sub> / V<sub>dc</sub>; peak factor = V<sub>m</sub> / V<sub>rms</sub>.</p>""",
          """<p>V<sub>m</sub> = secondary નો peak voltage, I<sub>m</sub> = peak load current = V<sub>m</sub> / (r<sub>f</sub> + R<sub>L</sub>), જ્યાં r<sub>f</sub> = diode નો forward resistance.</p>
<h4>1. Average (DC) મૂલ્ય – V<sub>dc</sub>, I<sub>dc</sub></h4>
<p>એક cycle દરમિયાન pulsating output નું સરેરાશ મૂલ્ય. DC voltmeter આ જ મૂલ્ય બતાવે છે.</p>
<h4>2. RMS મૂલ્ય – V<sub>rms</sub>, I<sub>rms</sub></h4>
<p>Output નું અસરકારક મૂલ્ય, જેમાં DC અને AC બંને ઘટકો સામેલ છે.</p>
<h4>3. Ripple factor (r અથવા γ)</h4>
<p>Output ના AC ઘટક (ripple) ના RMS મૂલ્ય અને DC મૂલ્યનો ગુણોત્તર. તે DC કેટલું શુદ્ધ છે તે બતાવે છે. <b>જેટલું ઓછું એટલું સારું</b>.</p>
<p><b>r = V<sub>ac(rms)</sub> / V<sub>dc</sub> = √[(I<sub>rms</sub> / I<sub>dc</sub>)² − 1]</b></p>
<h4>4. Rectification efficiency (η)</h4>
<p>DC output power અને AC input power નો ગુણોત્તર. <b>જેટલું વધુ એટલું સારું</b>.</p>
<p><b>η = P<sub>dc</sub> / P<sub>ac</sub> = I<sub>dc</sub>² R<sub>L</sub> / [I<sub>rms</sub>² (r<sub>f</sub> + R<sub>L</sub>)] × 100%</b></p>
<h4>5. Peak Inverse Voltage (PIV)</h4>
<p>Diode <b>conduction ન કરતો હોય</b> ત્યારે તેના પર આવતો મહત્તમ reverse voltage. Diode નું PIV rating આ મૂલ્ય કરતાં <b>વધુ</b> હોવું જોઈએ.</p>
<h4>6. Ripple frequency</h4>
<p>Pulsating output ની frequency (50 Hz mains માટે HWR માં 50 Hz, FWR માં 100 Hz).</p>
<h4>7. Transformer Utilisation Factor (TUF)</h4>
<p>TUF = load ને મળતો DC power / transformer secondary નું AC VA rating. વધુ TUF એટલે transformer નો વધુ સારો ઉપયોગ.</p>
<h4>8. Form factor અને peak factor</h4>
<p>Form factor = V<sub>rms</sub> / V<sub>dc</sub>; peak factor = V<sub>m</sub> / V<sub>rms</sub>.</p>""",
          examples=["u3n9"]),

        T("3.6.4 Half-Wave Rectifier", "3.6.4 Half-Wave Rectifier",
          """<h4>Circuit</h4>
<p>It consists of a <b>step-down transformer</b>, <b>one diode D</b> and a <b>load resistor R<sub>L</sub></b> connected in series across the secondary (see diagram).</p>
<h4>Working</h4>
<ul>
<li><b>Positive half-cycle:</b> The top of the secondary is positive, so the diode is <b>forward biased</b> (ON). Current flows through R<sub>L</sub> and the output follows the input half-cycle.</li>
<li><b>Negative half-cycle:</b> The top of the secondary is negative, so the diode is <b>reverse biased</b> (OFF). No current flows; output = 0.</li>
<li>Thus only <b>one half</b> of each AC cycle appears across the load → <b>pulsating DC</b> in one direction.</li>
</ul>
<h4>Formulas</h4>
<table>
<tr><th>Parameter</th><th>Value</th></tr>
<tr><td>I<sub>dc</sub> (average)</td><td>I<sub>m</sub> / π = 0.318 I<sub>m</sub></td></tr>
<tr><td>V<sub>dc</sub></td><td>V<sub>m</sub> / π = 0.318 V<sub>m</sub> (ideal diode, r<sub>f</sub> = 0)</td></tr>
<tr><td>I<sub>rms</sub></td><td>I<sub>m</sub> / 2</td></tr>
<tr><td>V<sub>rms</sub></td><td>V<sub>m</sub> / 2</td></tr>
<tr><td>Ripple factor</td><td><b>1.21</b> (121%)</td></tr>
<tr><td>Max. efficiency</td><td><b>40.6%</b></td></tr>
<tr><td>PIV</td><td><b>V<sub>m</sub></b></td></tr>
<tr><td>Output (ripple) frequency</td><td><b>f</b> (50 Hz)</td></tr>
<tr><td>TUF</td><td>0.287</td></tr>
<tr><td>Form factor</td><td>1.57</td></tr>
</table>
<h4>Advantages</h4>
<ul><li>Simple, only one diode, low cost.</li><li>No centre-tapped transformer needed.</li></ul>
<h4>Disadvantages</h4>
<ul>
<li>Very high ripple (1.21) → difficult to filter.</li>
<li>Low efficiency (40.6%) and low DC output (0.318 V<sub>m</sub>).</li>
<li>Low TUF; DC current through the secondary may saturate the transformer core.</li>
</ul>
<p><b>Applications:</b> low-power, low-cost circuits such as battery chargers for small devices, signal detection.</p>""",
          """<h4>Circuit</h4>
<p>તેમાં <b>step-down transformer</b>, <b>એક diode D</b> અને secondary પર series માં જોડેલ <b>load resistor R<sub>L</sub></b> હોય છે (આકૃતિ જુઓ).</p>
<h4>કાર્ય</h4>
<ul>
<li><b>Positive half-cycle:</b> Secondary નો ઉપરનો છેડો positive છે, તેથી diode <b>forward biased</b> (ON) થાય છે. R<sub>L</sub> માંથી current વહે છે અને output input half-cycle ને અનુસરે છે.</li>
<li><b>Negative half-cycle:</b> Secondary નો ઉપરનો છેડો negative છે, તેથી diode <b>reverse biased</b> (OFF) થાય છે. Current વહેતો નથી; output = 0.</li>
<li>આમ દરેક AC cycle નો ફક્ત <b>અડધો ભાગ</b> load પર આવે છે → એક જ દિશામાં <b>pulsating DC</b>.</li>
</ul>
<h4>સૂત્રો</h4>
<table>
<tr><th>Parameter</th><th>મૂલ્ય</th></tr>
<tr><td>I<sub>dc</sub> (average)</td><td>I<sub>m</sub> / π = 0.318 I<sub>m</sub></td></tr>
<tr><td>V<sub>dc</sub></td><td>V<sub>m</sub> / π = 0.318 V<sub>m</sub> (ideal diode, r<sub>f</sub> = 0)</td></tr>
<tr><td>I<sub>rms</sub></td><td>I<sub>m</sub> / 2</td></tr>
<tr><td>V<sub>rms</sub></td><td>V<sub>m</sub> / 2</td></tr>
<tr><td>Ripple factor</td><td><b>1.21</b> (121%)</td></tr>
<tr><td>મહત્તમ efficiency</td><td><b>40.6%</b></td></tr>
<tr><td>PIV</td><td><b>V<sub>m</sub></b></td></tr>
<tr><td>Output (ripple) frequency</td><td><b>f</b> (50 Hz)</td></tr>
<tr><td>TUF</td><td>0.287</td></tr>
<tr><td>Form factor</td><td>1.57</td></tr>
</table>
<h4>ફાયદા</h4>
<ul><li>સરળ, ફક્ત એક diode, ઓછી કિંમત.</li><li>Centre-tapped transformer ની જરૂર નથી.</li></ul>
<h4>ગેરફાયદા</h4>
<ul>
<li>ખૂબ વધુ ripple (1.21) → filter કરવું મુશ્કેલ.</li>
<li>ઓછી efficiency (40.6%) અને ઓછો DC output (0.318 V<sub>m</sub>).</li>
<li>ઓછું TUF; secondary માંથી DC current વહેવાથી transformer core saturate થઈ શકે.</li>
</ul>
<p><b>ઉપયોગો:</b> ઓછા power, ઓછી કિંમતના circuits જેમ કે નાના devices ના battery chargers, signal detection.</p>""",
          diagram="u3_hwr", examples=["u3n6"]),

        T("3.6.5 Centre-Tapped Full-Wave Rectifier", "3.6.5 Centre-Tapped Full-Wave Rectifier",
          """<h4>Circuit</h4>
<p>It uses a <b>centre-tapped transformer</b> and <b>two diodes D1 and D2</b>. The anodes of D1 and D2 are connected to the two ends of the secondary; their cathodes are joined together and connected to one end of R<sub>L</sub>. The other end of R<sub>L</sub> goes to the <b>centre tap (CT)</b> (see diagram).</p>
<p>The centre tap divides the secondary into two equal halves; each half gives a peak voltage V<sub>m</sub>.</p>
<h4>Working</h4>
<ul>
<li><b>Positive half-cycle:</b> The top end is positive w.r.t. CT → <b>D1 forward biased (ON)</b>, D2 reverse biased (OFF). Current: top end → D1 → R<sub>L</sub> → CT.</li>
<li><b>Negative half-cycle:</b> The bottom end is positive w.r.t. CT → <b>D2 ON</b>, D1 OFF. Current: bottom end → D2 → R<sub>L</sub> → CT.</li>
<li>In both half-cycles, current flows through R<sub>L</sub> in the <b>same direction</b> → full-wave pulsating DC.</li>
</ul>
<h4>Formulas</h4>
<table>
<tr><th>Parameter</th><th>Value</th></tr>
<tr><td>I<sub>dc</sub></td><td>2I<sub>m</sub> / π = 0.636 I<sub>m</sub></td></tr>
<tr><td>V<sub>dc</sub></td><td>2V<sub>m</sub> / π = 0.636 V<sub>m</sub></td></tr>
<tr><td>I<sub>rms</sub></td><td>I<sub>m</sub> / √2</td></tr>
<tr><td>V<sub>rms</sub></td><td>V<sub>m</sub> / √2</td></tr>
<tr><td>Ripple factor</td><td><b>0.482</b> (48.2%)</td></tr>
<tr><td>Max. efficiency</td><td><b>81.2%</b></td></tr>
<tr><td>PIV</td><td><b>2V<sub>m</sub></b> (V<sub>m</sub> = peak of each half)</td></tr>
<tr><td>Output (ripple) frequency</td><td><b>2f</b> (100 Hz)</td></tr>
<tr><td>TUF</td><td>0.693</td></tr>
<tr><td>Form factor</td><td>1.11</td></tr>
</table>
<p><b>Why is PIV = 2V<sub>m</sub>?</b> When D1 conducts (drop ≈ 0), the cathode of D2 is at +V<sub>m</sub> and its anode is at −V<sub>m</sub>, so D2 sees 2V<sub>m</sub> in reverse.</p>
<h4>Advantages</h4>
<ul><li>Ripple factor and efficiency are much better than HWR.</li><li>DC output is double that of HWR.</li><li>Only two diodes; no DC saturation of the core.</li></ul>
<h4>Disadvantages</h4>
<ul><li>Needs a <b>centre-tapped transformer</b> – bulky and costly.</li><li>Each half of the secondary is used only for half the time.</li><li>Diodes must have a high PIV rating (2V<sub>m</sub>).</li></ul>""",
          """<h4>Circuit</h4>
<p>તે <b>centre-tapped transformer</b> અને <b>બે diodes D1 અને D2</b> વાપરે છે. D1 અને D2 ના anodes secondary ના બે છેડા સાથે જોડાય છે; તેમના cathodes ભેગા કરી R<sub>L</sub> ના એક છેડે જોડાય છે. R<sub>L</sub> નો બીજો છેડો <b>centre tap (CT)</b> સાથે જોડાય છે (આકૃતિ જુઓ).</p>
<p>Centre tap secondary ને બે સમાન ભાગમાં વહેંચે છે; દરેક ભાગ peak voltage V<sub>m</sub> આપે છે.</p>
<h4>કાર્ય</h4>
<ul>
<li><b>Positive half-cycle:</b> ઉપરનો છેડો CT ની સાપેક્ષે positive → <b>D1 forward biased (ON)</b>, D2 reverse biased (OFF). Current: ઉપરનો છેડો → D1 → R<sub>L</sub> → CT.</li>
<li><b>Negative half-cycle:</b> નીચેનો છેડો CT ની સાપેક્ષે positive → <b>D2 ON</b>, D1 OFF. Current: નીચેનો છેડો → D2 → R<sub>L</sub> → CT.</li>
<li>બંને half-cycles માં R<sub>L</sub> માંથી current <b>એક જ દિશામાં</b> વહે છે → full-wave pulsating DC.</li>
</ul>
<h4>સૂત્રો</h4>
<table>
<tr><th>Parameter</th><th>મૂલ્ય</th></tr>
<tr><td>I<sub>dc</sub></td><td>2I<sub>m</sub> / π = 0.636 I<sub>m</sub></td></tr>
<tr><td>V<sub>dc</sub></td><td>2V<sub>m</sub> / π = 0.636 V<sub>m</sub></td></tr>
<tr><td>I<sub>rms</sub></td><td>I<sub>m</sub> / √2</td></tr>
<tr><td>V<sub>rms</sub></td><td>V<sub>m</sub> / √2</td></tr>
<tr><td>Ripple factor</td><td><b>0.482</b> (48.2%)</td></tr>
<tr><td>મહત્તમ efficiency</td><td><b>81.2%</b></td></tr>
<tr><td>PIV</td><td><b>2V<sub>m</sub></b> (V<sub>m</sub> = દરેક અડધા ભાગનો peak)</td></tr>
<tr><td>Output (ripple) frequency</td><td><b>2f</b> (100 Hz)</td></tr>
<tr><td>TUF</td><td>0.693</td></tr>
<tr><td>Form factor</td><td>1.11</td></tr>
</table>
<p><b>PIV = 2V<sub>m</sub> કેમ?</b> જ્યારે D1 conduction કરે (drop ≈ 0), ત્યારે D2 નો cathode +V<sub>m</sub> પર અને anode −V<sub>m</sub> પર હોય છે, તેથી D2 પર reverse માં 2V<sub>m</sub> આવે છે.</p>
<h4>ફાયદા</h4>
<ul><li>Ripple factor અને efficiency HWR કરતાં ઘણા સારા.</li><li>DC output HWR કરતાં બમણો.</li><li>ફક્ત બે diodes; core નું DC saturation નહીં.</li></ul>
<h4>ગેરફાયદા</h4>
<ul><li><b>Centre-tapped transformer</b> જરૂરી – મોટું અને મોંઘું.</li><li>Secondary નો દરેક અડધો ભાગ ફક્ત અડધો સમય વપરાય.</li><li>Diodes નું PIV rating વધુ (2V<sub>m</sub>) હોવું જોઈએ.</li></ul>""",
          diagram="u3_fwr_ct", examples=["u3n7"]),

        T("3.6.6 Full-Wave Bridge Rectifier", "3.6.6 Full-Wave Bridge Rectifier",
          """<h4>Circuit</h4>
<p>Four diodes <b>D1, D2, D3, D4</b> are connected in the form of a <b>bridge</b>. The AC secondary is connected across one diagonal, and the load R<sub>L</sub> across the other diagonal. <b>No centre tap</b> is needed (see diagram).</p>
<h4>Working</h4>
<ul>
<li><b>Positive half-cycle:</b> The top of the secondary is positive → <b>D1 and D4 are forward biased</b> (ON); D2 and D3 are OFF. Current: top → D1 → R<sub>L</sub> (+ to −) → D4 → bottom.</li>
<li><b>Negative half-cycle:</b> The bottom of the secondary is positive → <b>D2 and D3 are ON</b>; D1 and D4 are OFF. Current: bottom → D2 → R<sub>L</sub> (+ to −) → D3 → top.</li>
<li>In both half-cycles, current through R<sub>L</sub> flows in the <b>same direction</b> → full-wave output.</li>
<li>In each half-cycle <b>two diodes conduct in series</b>, so the total drop is 2 × 0.7 = 1.4 V.</li>
</ul>
<h4>Formulas</h4>
<p>V<sub>dc</sub> = 2V<sub>m</sub>/π, I<sub>dc</sub> = 2I<sub>m</sub>/π, I<sub>rms</sub> = I<sub>m</sub>/√2, ripple factor = <b>0.482</b>, efficiency = <b>81.2%</b>, output frequency = <b>2f</b> (same as centre-tap).</p>
<p><b>PIV = V<sub>m</sub></b> (each reverse-biased diode sees only V<sub>m</sub>), <b>TUF = 0.812</b>.</p>
<p>Practical: V<sub>dc</sub> = 2(V<sub>m</sub> − 1.4)/π for Si diodes.</p>
<h4>Advantages</h4>
<ul>
<li><b>No centre-tapped transformer</b> needed → smaller and cheaper transformer.</li>
<li>PIV is only <b>V<sub>m</sub></b> (half that of centre-tap).</li>
<li>Highest TUF (0.812); output voltage double that of centre-tap for the same transformer.</li>
<li>Readily available as a single package (bridge IC, e.g. W10M, KBPC).</li>
</ul>
<h4>Disadvantages</h4>
<ul>
<li>Needs <b>four diodes</b>.</li>
<li>Two diodes conduct at a time → <b>1.4 V drop</b>, so not good for very low voltage supplies.</li>
</ul>
<p><b>Applications:</b> most DC power supplies, mobile chargers, adapters, battery chargers, SMPS input stage.</p>""",
          """<h4>Circuit</h4>
<p>ચાર diodes <b>D1, D2, D3, D4</b> ને <b>Bridge</b> સ્વરૂપમાં જોડાય છે. AC secondary એક diagonal પર અને load R<sub>L</sub> બીજા diagonal પર જોડાય છે. <b>Centre tap ની જરૂર નથી</b> (આકૃતિ જુઓ).</p>
<h4>કાર્ય</h4>
<ul>
<li><b>Positive half-cycle:</b> Secondary નો ઉપરનો છેડો positive → <b>D1 અને D4 forward biased</b> (ON); D2 અને D3 OFF. Current: ઉપર → D1 → R<sub>L</sub> (+ થી −) → D4 → નીચે.</li>
<li><b>Negative half-cycle:</b> Secondary નો નીચેનો છેડો positive → <b>D2 અને D3 ON</b>; D1 અને D4 OFF. Current: નીચે → D2 → R<sub>L</sub> (+ થી −) → D3 → ઉપર.</li>
<li>બંને half-cycles માં R<sub>L</sub> માંથી current <b>એક જ દિશામાં</b> વહે છે → full-wave output.</li>
<li>દરેક half-cycle માં <b>બે diodes series માં conduction</b> કરે છે, તેથી કુલ drop 2 × 0.7 = 1.4 V.</li>
</ul>
<h4>સૂત્રો</h4>
<p>V<sub>dc</sub> = 2V<sub>m</sub>/π, I<sub>dc</sub> = 2I<sub>m</sub>/π, I<sub>rms</sub> = I<sub>m</sub>/√2, ripple factor = <b>0.482</b>, efficiency = <b>81.2%</b>, output frequency = <b>2f</b> (centre-tap જેવું જ).</p>
<p><b>PIV = V<sub>m</sub></b> (દરેક reverse-biased diode પર ફક્ત V<sub>m</sub>), <b>TUF = 0.812</b>.</p>
<p>વ્યવહારમાં: Si diodes માટે V<sub>dc</sub> = 2(V<sub>m</sub> − 1.4)/π.</p>
<h4>ફાયદા</h4>
<ul>
<li><b>Centre-tapped transformer ની જરૂર નથી</b> → નાનું અને સસ્તું transformer.</li>
<li>PIV ફક્ત <b>V<sub>m</sub></b> (centre-tap કરતાં અડધો).</li>
<li>સૌથી વધુ TUF (0.812); સમાન transformer માટે output voltage centre-tap કરતાં બમણો.</li>
<li>એક જ package (bridge IC, દા.ત. W10M, KBPC) તરીકે સહેલાઈથી મળે.</li>
</ul>
<h4>ગેરફાયદા</h4>
<ul>
<li><b>ચાર diodes</b> જરૂરી.</li>
<li>એક સાથે બે diodes conduction કરે → <b>1.4 V drop</b>, તેથી ખૂબ ઓછા voltage ના supply માટે યોગ્ય નથી.</li>
</ul>
<p><b>ઉપયોગો:</b> મોટાભાગના DC power supplies, mobile chargers, adapters, battery chargers, SMPS નો input stage.</p>""",
          diagram="u3_bridge", examples=["u3n8"]),

        T("3.6.7 Comparison of Rectifiers", "3.6.7 Rectifiers ની સરખામણી",
          """<table>
<tr><th>Parameter</th><th>Half-wave</th><th>Centre-tap FW</th><th>Bridge FW</th></tr>
<tr><td>No. of diodes</td><td>1</td><td>2</td><td>4</td></tr>
<tr><td>Transformer</td><td>Ordinary (optional)</td><td>Centre-tapped</td><td>Ordinary (optional)</td></tr>
<tr><td>V<sub>dc</sub></td><td>V<sub>m</sub>/π = 0.318 V<sub>m</sub></td><td>2V<sub>m</sub>/π = 0.636 V<sub>m</sub></td><td>2V<sub>m</sub>/π = 0.636 V<sub>m</sub></td></tr>
<tr><td>I<sub>rms</sub></td><td>I<sub>m</sub>/2</td><td>I<sub>m</sub>/√2</td><td>I<sub>m</sub>/√2</td></tr>
<tr><td>Ripple factor</td><td>1.21</td><td>0.482</td><td>0.482</td></tr>
<tr><td>Max. efficiency</td><td>40.6%</td><td>81.2%</td><td>81.2%</td></tr>
<tr><td>PIV of diode</td><td>V<sub>m</sub></td><td>2V<sub>m</sub></td><td>V<sub>m</sub></td></tr>
<tr><td>Output frequency</td><td>f (50 Hz)</td><td>2f (100 Hz)</td><td>2f (100 Hz)</td></tr>
<tr><td>TUF</td><td>0.287</td><td>0.693</td><td>0.812</td></tr>
<tr><td>Diodes conducting per half-cycle</td><td>1 (only in +ve half)</td><td>1</td><td>2</td></tr>
<tr><td>Cost / size</td><td>Lowest</td><td>Highest (CT transformer)</td><td>Medium</td></tr>
</table>
<p><b>Conclusion:</b> The bridge rectifier is the most widely used because it needs no centre tap, has low PIV and the highest TUF.</p>""",
          """<table>
<tr><th>Parameter</th><th>Half-wave</th><th>Centre-tap FW</th><th>Bridge FW</th></tr>
<tr><td>Diodes ની સંખ્યા</td><td>1</td><td>2</td><td>4</td></tr>
<tr><td>Transformer</td><td>સામાન્ય (વૈકલ્પિક)</td><td>Centre-tapped</td><td>સામાન્ય (વૈકલ્પિક)</td></tr>
<tr><td>V<sub>dc</sub></td><td>V<sub>m</sub>/π = 0.318 V<sub>m</sub></td><td>2V<sub>m</sub>/π = 0.636 V<sub>m</sub></td><td>2V<sub>m</sub>/π = 0.636 V<sub>m</sub></td></tr>
<tr><td>I<sub>rms</sub></td><td>I<sub>m</sub>/2</td><td>I<sub>m</sub>/√2</td><td>I<sub>m</sub>/√2</td></tr>
<tr><td>Ripple factor</td><td>1.21</td><td>0.482</td><td>0.482</td></tr>
<tr><td>મહત્તમ efficiency</td><td>40.6%</td><td>81.2%</td><td>81.2%</td></tr>
<tr><td>Diode નો PIV</td><td>V<sub>m</sub></td><td>2V<sub>m</sub></td><td>V<sub>m</sub></td></tr>
<tr><td>Output frequency</td><td>f (50 Hz)</td><td>2f (100 Hz)</td><td>2f (100 Hz)</td></tr>
<tr><td>TUF</td><td>0.287</td><td>0.693</td><td>0.812</td></tr>
<tr><td>દરેક half-cycle માં conduction કરતા diodes</td><td>1 (ફક્ત +ve half માં)</td><td>1</td><td>2</td></tr>
<tr><td>કિંમત / કદ</td><td>સૌથી ઓછું</td><td>સૌથી વધુ (CT transformer)</td><td>મધ્યમ</td></tr>
</table>
<p><b>નિષ્કર્ષ:</b> Bridge rectifier સૌથી વધુ વપરાય છે કારણ કે તેમાં centre tap ની જરૂર નથી, PIV ઓછો છે અને TUF સૌથી વધુ છે.</p>"""),

        T("Key Points – 3.6", "મુખ્ય મુદ્દા – 3.6",
          """<ul>
<li><b>Rectifier</b> converts AC → pulsating DC using the unidirectional property of diodes.</li>
<li>DC power supply: Transformer → Rectifier → Filter → Regulator.</li>
<li><b>HWR:</b> 1 diode, V<sub>dc</sub> = V<sub>m</sub>/π, r = 1.21, η = 40.6%, PIV = V<sub>m</sub>, f<sub>out</sub> = f.</li>
<li><b>Centre-tap FWR:</b> 2 diodes + CT transformer, V<sub>dc</sub> = 2V<sub>m</sub>/π, r = 0.482, η = 81.2%, PIV = 2V<sub>m</sub>, f<sub>out</sub> = 2f.</li>
<li><b>Bridge:</b> 4 diodes, no CT, same V<sub>dc</sub>, r, η as CT; PIV = V<sub>m</sub>; TUF 0.812; 1.4 V drop.</li>
<li>Ripple factor r = √[(I<sub>rms</sub>/I<sub>dc</sub>)² − 1]; lower is better.</li>
<li>Efficiency η = P<sub>dc</sub>/P<sub>ac</sub>; higher is better.</li>
</ul>""",
          """<ul>
<li><b>Rectifier</b> diodes ના unidirectional ગુણધર્મથી AC → pulsating DC માં ફેરવે.</li>
<li>DC power supply: Transformer → Rectifier → Filter → Regulator.</li>
<li><b>HWR:</b> 1 diode, V<sub>dc</sub> = V<sub>m</sub>/π, r = 1.21, η = 40.6%, PIV = V<sub>m</sub>, f<sub>out</sub> = f.</li>
<li><b>Centre-tap FWR:</b> 2 diodes + CT transformer, V<sub>dc</sub> = 2V<sub>m</sub>/π, r = 0.482, η = 81.2%, PIV = 2V<sub>m</sub>, f<sub>out</sub> = 2f.</li>
<li><b>Bridge:</b> 4 diodes, CT નહીં, V<sub>dc</sub>, r, η CT જેવા જ; PIV = V<sub>m</sub>; TUF 0.812; 1.4 V drop.</li>
<li>Ripple factor r = √[(I<sub>rms</sub>/I<sub>dc</sub>)² − 1]; જેટલું ઓછું એટલું સારું.</li>
<li>Efficiency η = P<sub>dc</sub>/P<sub>ac</sub>; જેટલું વધુ એટલું સારું.</li>
</ul>""", key=True),
    ],
}

NOTES_B = [SEC_3_4, SEC_3_5, SEC_3_6]
