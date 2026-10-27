"""Basics of Electronics (DI01000151) - Unit 4: Bipolar Junction Transistor (part B: 4.3 - 4.5)"""
from content_DI01000151_u3_notes_a import T

# =====================================================================================
SEC_4_3 = {
    "title": {"en": "4.3 Transistor Configurations and Characteristics", "gu": "4.3 Transistor Configurations અને Characteristics"},
    "items": [
        T("4.3.1 Transistor Configurations – Introduction", "4.3.1 Transistor Configurations – પરિચય",
          """<p>A transistor has <b>three terminals</b>, but a circuit needs <b>four terminals</b> – two for input and two for output. So <b>one terminal is made common</b> to both the input and the output circuits.</p>
<p>Depending on which terminal is common, there are three configurations (connections):</p>
<table>
<tr><th>Configuration</th><th>Common terminal</th><th>Input between</th><th>Output between</th></tr>
<tr><td><b>Common Base (CB)</b></td><td>Base</td><td>Emitter – Base</td><td>Collector – Base</td></tr>
<tr><td><b>Common Emitter (CE)</b></td><td>Emitter</td><td>Base – Emitter</td><td>Collector – Emitter</td></tr>
<tr><td><b>Common Collector (CC)</b></td><td>Collector</td><td>Base – Collector</td><td>Emitter – Collector</td></tr>
</table>
<p>In every configuration, for amplifier operation, the <b>emitter-base junction is forward biased</b> and the <b>collector-base junction is reverse biased</b>.</p>
<h4>Characteristics</h4>
<p>Graphs that show the relation between currents and voltages of a transistor are called <b>characteristics</b>:</p>
<ul>
<li><b>Input characteristics:</b> input current vs input voltage, with output voltage constant.</li>
<li><b>Output characteristics:</b> output current vs output voltage, with input current constant.</li>
</ul>""",
          """<p>Transistor માં <b>ત્રણ terminals</b> છે, પરંતુ circuit ને <b>ચાર terminals</b> જોઈએ – બે input માટે અને બે output માટે. તેથી <b>એક terminal ને input અને output બંને circuits માટે common</b> બનાવાય છે.</p>
<p>કયો terminal common છે તેના આધારે ત્રણ configurations (જોડાણ) છે:</p>
<table>
<tr><th>Configuration</th><th>Common terminal</th><th>Input વચ્ચે</th><th>Output વચ્ચે</th></tr>
<tr><td><b>Common Base (CB)</b></td><td>Base</td><td>Emitter – Base</td><td>Collector – Base</td></tr>
<tr><td><b>Common Emitter (CE)</b></td><td>Emitter</td><td>Base – Emitter</td><td>Collector – Emitter</td></tr>
<tr><td><b>Common Collector (CC)</b></td><td>Collector</td><td>Base – Collector</td><td>Emitter – Collector</td></tr>
</table>
<p>દરેક configuration માં amplifier કાર્ય માટે <b>emitter-base junction forward biased</b> અને <b>collector-base junction reverse biased</b> હોય છે.</p>
<h4>Characteristics</h4>
<p>Transistor ના currents અને voltages વચ્ચેનો સંબંધ બતાવતા આલેખોને <b>Characteristics</b> કહે છે:</p>
<ul>
<li><b>Input characteristics:</b> output voltage અચળ રાખી input current વિરુદ્ધ input voltage.</li>
<li><b>Output characteristics:</b> input current અચળ રાખી output current વિરુદ્ધ output voltage.</li>
</ul>"""),

        T("4.3.2 Common Base (CB) Configuration", "4.3.2 Common Base (CB) Configuration",
          """<p>In CB configuration the <b>base is common</b> to input and output. Input is applied between <b>emitter and base</b>, and output is taken between <b>collector and base</b> (see diagram for NPN).</p>
<ul>
<li>V<sub>EE</sub> forward biases the emitter-base junction; V<sub>CC</sub> reverse biases the collector-base junction.</li>
<li>Input current = <b>I<sub>E</sub></b>; output current = <b>I<sub>C</sub></b>.</li>
</ul>
<h4>Current amplification factor (α)</h4>
<p><b>α = ΔI<sub>C</sub> / ΔI<sub>E</sub></b> (V<sub>CB</sub> constant) → <b>less than 1</b> (0.95–0.995). So CB gives <b>no current gain</b>.</p>
<h4>Features</h4>
<ul>
<li>Current gain: less than 1 (α)</li>
<li>Voltage gain: high (because output resistance ≫ input resistance)</li>
<li>Input resistance: very <b>low</b> (≈ 20 – 100 Ω)</li>
<li>Output resistance: very <b>high</b> (≈ 500 kΩ – 1 MΩ)</li>
<li>Phase shift between input and output: <b>0°</b> (in phase)</li>
<li>Application: <b>high-frequency (RF) amplifiers</b>, impedance matching from low to high impedance</li>
</ul>""",
          """<p>CB configuration માં <b>base input અને output માટે common</b> છે. Input <b>emitter અને base</b> વચ્ચે લગાવાય છે અને output <b>collector અને base</b> વચ્ચેથી લેવાય છે (NPN માટે આકૃતિ જુઓ).</p>
<ul>
<li>V<sub>EE</sub> emitter-base junction ને forward bias કરે; V<sub>CC</sub> collector-base junction ને reverse bias કરે.</li>
<li>Input current = <b>I<sub>E</sub></b>; output current = <b>I<sub>C</sub></b>.</li>
</ul>
<h4>Current amplification factor (α)</h4>
<p><b>α = ΔI<sub>C</sub> / ΔI<sub>E</sub></b> (V<sub>CB</sub> અચળ) → <b>1 થી ઓછો</b> (0.95–0.995). તેથી CB માં <b>current gain મળતો નથી</b>.</p>
<h4>લક્ષણો</h4>
<ul>
<li>Current gain: 1 થી ઓછો (α)</li>
<li>Voltage gain: વધુ (કારણ કે output resistance ≫ input resistance)</li>
<li>Input resistance: ખૂબ <b>ઓછો</b> (≈ 20 – 100 Ω)</li>
<li>Output resistance: ખૂબ <b>વધુ</b> (≈ 500 kΩ – 1 MΩ)</li>
<li>Input અને output વચ્ચે phase shift: <b>0°</b> (in phase)</li>
<li>ઉપયોગ: <b>High-frequency (RF) amplifiers</b>, ઓછા થી વધુ impedance સુધી impedance matching</li>
</ul>""",
          diagram="u4_cb"),

        T("4.3.3 CB Characteristics", "4.3.3 CB Characteristics",
          """<h4>Input characteristics (I<sub>E</sub> vs V<sub>EB</sub>, V<sub>CB</sub> constant)</h4>
<ul>
<li>The curve is like the <b>forward characteristic of a diode</b> (emitter-base junction is forward biased).</li>
<li>Emitter current is very small until V<sub>EB</sub> reaches the knee voltage (≈ 0.7 V for Si), then it rises rapidly.</li>
<li>When V<sub>CB</sub> is increased, the curve shifts slightly <b>left</b> (more I<sub>E</sub> for the same V<sub>EB</sub>) due to the <b>Early effect</b> (base-width modulation).</li>
<li><b>Input resistance r<sub>i</sub> = ΔV<sub>EB</sub> / ΔI<sub>E</sub></b> → very low (tens of ohms).</li>
</ul>
<h4>Output characteristics (I<sub>C</sub> vs V<sub>CB</sub>, I<sub>E</sub> constant)</h4>
<ul>
<li><b>Active region:</b> I<sub>C</sub> ≈ I<sub>E</sub> and is almost <b>independent of V<sub>CB</sub></b> → the curves are nearly flat (horizontal) lines.</li>
<li>Even at V<sub>CB</sub> = 0, I<sub>C</sub> flows. To reduce I<sub>C</sub> to zero, the collector-base junction must be slightly forward biased (negative V<sub>CB</sub>) → <b>saturation region</b>.</li>
<li><b>Cut-off region:</b> below the I<sub>E</sub> = 0 curve; only I<sub>CBO</sub> flows.</li>
<li><b>Output resistance r<sub>o</sub> = ΔV<sub>CB</sub> / ΔI<sub>C</sub></b> → very high (since the curves are almost flat).</li>
</ul>""",
          """<h4>Input characteristics (I<sub>E</sub> વિરુદ્ધ V<sub>EB</sub>, V<sub>CB</sub> અચળ)</h4>
<ul>
<li>Curve <b>diode ની forward characteristic</b> જેવો છે (emitter-base junction forward biased છે).</li>
<li>V<sub>EB</sub> knee voltage (Si માટે ≈ 0.7 V) સુધી પહોંચે ત્યાં સુધી emitter current ખૂબ નાનો રહે છે, પછી ઝડપથી વધે છે.</li>
<li>V<sub>CB</sub> વધારતાં <b>Early effect</b> (base-width modulation) ને કારણે curve થોડો <b>ડાબી</b> તરફ ખસે છે (સમાન V<sub>EB</sub> માટે વધુ I<sub>E</sub>).</li>
<li><b>Input resistance r<sub>i</sub> = ΔV<sub>EB</sub> / ΔI<sub>E</sub></b> → ખૂબ ઓછો (દસેક ohms).</li>
</ul>
<h4>Output characteristics (I<sub>C</sub> વિરુદ્ધ V<sub>CB</sub>, I<sub>E</sub> અચળ)</h4>
<ul>
<li><b>Active region:</b> I<sub>C</sub> ≈ I<sub>E</sub> અને લગભગ <b>V<sub>CB</sub> થી સ્વતંત્ર</b> → curves લગભગ સપાટ (આડી) રેખાઓ છે.</li>
<li>V<sub>CB</sub> = 0 પર પણ I<sub>C</sub> વહે છે. I<sub>C</sub> ને શૂન્ય કરવા collector-base junction ને થોડો forward bias (negative V<sub>CB</sub>) કરવો પડે → <b>Saturation region</b>.</li>
<li><b>Cut-off region:</b> I<sub>E</sub> = 0 curve ની નીચે; ફક્ત I<sub>CBO</sub> વહે.</li>
<li><b>Output resistance r<sub>o</sub> = ΔV<sub>CB</sub> / ΔI<sub>C</sub></b> → ખૂબ વધુ (curves લગભગ સપાટ હોવાથી).</li>
</ul>""",
          diagram="u4_cb_char"),

        T("4.3.4 Common Emitter (CE) Configuration", "4.3.4 Common Emitter (CE) Configuration",
          """<p>In CE configuration the <b>emitter is common</b> to input and output. Input is applied between <b>base and emitter</b>, and output is taken between <b>collector and emitter</b> (see diagram).</p>
<ul>
<li>V<sub>BB</sub> (through R<sub>B</sub>) forward biases the base-emitter junction; V<sub>CC</sub> (through R<sub>C</sub>) keeps the collector-base junction reverse biased (V<sub>CC</sub> &gt; V<sub>BB</sub>).</li>
<li>Input current = <b>I<sub>B</sub></b>; output current = <b>I<sub>C</sub></b>.</li>
</ul>
<h4>Current amplification factor (β)</h4>
<p><b>β = ΔI<sub>C</sub> / ΔI<sub>B</sub></b> (V<sub>CE</sub> constant) → large (20–500). So CE gives <b>high current gain</b>.</p>
<h4>Features</h4>
<ul>
<li>Current gain: <b>high</b> (β)</li>
<li>Voltage gain: <b>high</b> (≈ 100–500)</li>
<li>Power gain: <b>highest</b> of all three</li>
<li>Input resistance: <b>medium</b> (≈ 1 kΩ)</li>
<li>Output resistance: <b>medium</b> (≈ 10 – 50 kΩ)</li>
<li>Phase shift: <b>180°</b> (output is inverted)</li>
<li>Application: <b>audio amplifiers</b>, voltage amplifiers, <b>switching</b>; the most widely used configuration</li>
</ul>""",
          """<p>CE configuration માં <b>emitter input અને output માટે common</b> છે. Input <b>base અને emitter</b> વચ્ચે લગાવાય છે અને output <b>collector અને emitter</b> વચ્ચેથી લેવાય છે (આકૃતિ જુઓ).</p>
<ul>
<li>V<sub>BB</sub> (R<sub>B</sub> દ્વારા) base-emitter junction ને forward bias કરે; V<sub>CC</sub> (R<sub>C</sub> દ્વારા) collector-base junction ને reverse biased રાખે (V<sub>CC</sub> &gt; V<sub>BB</sub>).</li>
<li>Input current = <b>I<sub>B</sub></b>; output current = <b>I<sub>C</sub></b>.</li>
</ul>
<h4>Current amplification factor (β)</h4>
<p><b>β = ΔI<sub>C</sub> / ΔI<sub>B</sub></b> (V<sub>CE</sub> અચળ) → મોટો (20–500). તેથી CE માં <b>વધુ current gain</b> મળે છે.</p>
<h4>લક્ષણો</h4>
<ul>
<li>Current gain: <b>વધુ</b> (β)</li>
<li>Voltage gain: <b>વધુ</b> (≈ 100–500)</li>
<li>Power gain: ત્રણેયમાં <b>સૌથી વધુ</b></li>
<li>Input resistance: <b>મધ્યમ</b> (≈ 1 kΩ)</li>
<li>Output resistance: <b>મધ્યમ</b> (≈ 10 – 50 kΩ)</li>
<li>Phase shift: <b>180°</b> (output ઉલટો)</li>
<li>ઉપયોગ: <b>Audio amplifiers</b>, voltage amplifiers, <b>switching</b>; સૌથી વધુ વપરાતું configuration</li>
</ul>""",
          diagram="u4_ce"),

        T("4.3.5 Circuit for CE Characteristics", "4.3.5 CE Characteristics માટેનો Circuit",
          """<p>The characteristics of an NPN transistor in CE configuration are obtained with the circuit shown.</p>
<h4>Components</h4>
<ul>
<li><b>V<sub>BB</sub></b> – variable DC supply for the base circuit, with series resistor <b>R<sub>B</sub></b>.</li>
<li><b>Micro-ammeter (µA)</b> – measures base current I<sub>B</sub>.</li>
<li><b>Voltmeter</b> across B-E – measures V<sub>BE</sub>.</li>
<li><b>V<sub>CC</sub></b> – variable DC supply for the collector circuit.</li>
<li><b>Milli-ammeter (mA)</b> – measures collector current I<sub>C</sub>.</li>
<li><b>Voltmeter</b> across C-E – measures V<sub>CE</sub>.</li>
</ul>
<h4>Procedure</h4>
<ol>
<li><b>Input characteristics:</b> keep V<sub>CE</sub> constant (e.g. 1 V). Vary V<sub>BB</sub> in small steps and note V<sub>BE</sub> and I<sub>B</sub>. Repeat for V<sub>CE</sub> = 5 V. Plot I<sub>B</sub> vs V<sub>BE</sub>.</li>
<li><b>Output characteristics:</b> set I<sub>B</sub> to a fixed value (e.g. 20 µA) using V<sub>BB</sub>. Vary V<sub>CC</sub> and note V<sub>CE</sub> and I<sub>C</sub>. Repeat for I<sub>B</sub> = 40, 60, 80 µA. Plot I<sub>C</sub> vs V<sub>CE</sub>.</li>
</ol>""",
          """<p>CE configuration માં NPN transistor ની characteristics આકૃતિમાં બતાવેલ circuit થી મેળવાય છે.</p>
<h4>ઘટકો</h4>
<ul>
<li><b>V<sub>BB</sub></b> – base circuit માટે variable DC supply, series resistor <b>R<sub>B</sub></b> સાથે.</li>
<li><b>Micro-ammeter (µA)</b> – base current I<sub>B</sub> માપે.</li>
<li>B-E પર <b>Voltmeter</b> – V<sub>BE</sub> માપે.</li>
<li><b>V<sub>CC</sub></b> – collector circuit માટે variable DC supply.</li>
<li><b>Milli-ammeter (mA)</b> – collector current I<sub>C</sub> માપે.</li>
<li>C-E પર <b>Voltmeter</b> – V<sub>CE</sub> માપે.</li>
</ul>
<h4>પદ્ધતિ</h4>
<ol>
<li><b>Input characteristics:</b> V<sub>CE</sub> અચળ રાખો (દા.ત. 1 V). V<sub>BB</sub> નાના પગલાંમાં બદલો અને V<sub>BE</sub> અને I<sub>B</sub> નોંધો. V<sub>CE</sub> = 5 V માટે ફરી કરો. I<sub>B</sub> વિરુદ્ધ V<sub>BE</sub> નો આલેખ દોરો.</li>
<li><b>Output characteristics:</b> V<sub>BB</sub> થી I<sub>B</sub> ને નિશ્ચિત મૂલ્ય (દા.ત. 20 µA) પર રાખો. V<sub>CC</sub> બદલો અને V<sub>CE</sub> અને I<sub>C</sub> નોંધો. I<sub>B</sub> = 40, 60, 80 µA માટે ફરી કરો. I<sub>C</sub> વિરુદ્ધ V<sub>CE</sub> નો આલેખ દોરો.</li>
</ol>""",
          diagram="u4_ce_test"),

        T("4.3.6 CE Input Characteristics", "4.3.6 CE Input Characteristics",
          """<p><b>Definition:</b> The curve between <b>base current I<sub>B</sub></b> and <b>base-emitter voltage V<sub>BE</sub></b> at constant <b>V<sub>CE</sub></b>.</p>
<h4>Observations</h4>
<ol>
<li>The curve is similar to the <b>forward characteristic of a P-N diode</b>, because the base-emitter junction is forward biased.</li>
<li>I<sub>B</sub> is almost zero until V<sub>BE</sub> reaches the <b>knee voltage (≈ 0.7 V for Si, 0.3 V for Ge)</b>. After that I<sub>B</sub> rises rapidly.</li>
<li>I<sub>B</sub> is in <b>micro-amperes (µA)</b>.</li>
<li>When V<sub>CE</sub> is increased, the curve shifts slightly to the <b>right</b> (less I<sub>B</sub> for the same V<sub>BE</sub>). This is due to the <b>Early effect</b>: higher V<sub>CE</sub> widens the collector-base depletion layer, the effective base width decreases, fewer carriers recombine in the base, so I<sub>B</sub> decreases.</li>
</ol>
<h4>Input resistance</h4>
<p><b>r<sub>i</sub> = ΔV<sub>BE</sub> / ΔI<sub>B</sub></b> (V<sub>CE</sub> constant) → medium, about <b>1 kΩ</b> (higher than CB).</p>""",
          """<p><b>વ્યાખ્યા:</b> અચળ <b>V<sub>CE</sub></b> પર <b>base current I<sub>B</sub></b> અને <b>base-emitter voltage V<sub>BE</sub></b> વચ્ચેનો curve.</p>
<h4>અવલોકનો</h4>
<ol>
<li>Base-emitter junction forward biased હોવાથી curve <b>P-N diode ની forward characteristic</b> જેવો છે.</li>
<li>V<sub>BE</sub> એ <b>knee voltage (Si માટે ≈ 0.7 V, Ge માટે 0.3 V)</b> સુધી પહોંચે ત્યાં સુધી I<sub>B</sub> લગભગ શૂન્ય રહે છે. પછી I<sub>B</sub> ઝડપથી વધે છે.</li>
<li>I<sub>B</sub> <b>micro-amperes (µA)</b> માં હોય છે.</li>
<li>V<sub>CE</sub> વધારતાં curve થોડો <b>જમણી</b> તરફ ખસે છે (સમાન V<sub>BE</sub> માટે ઓછો I<sub>B</sub>). આ <b>Early effect</b> ને કારણે છે: વધુ V<sub>CE</sub> collector-base depletion layer ને પહોળું કરે છે, અસરકારક base width ઘટે છે, base માં ઓછા carriers recombine થાય છે, તેથી I<sub>B</sub> ઘટે છે.</li>
</ol>
<h4>Input resistance</h4>
<p><b>r<sub>i</sub> = ΔV<sub>BE</sub> / ΔI<sub>B</sub></b> (V<sub>CE</sub> અચળ) → મધ્યમ, આશરે <b>1 kΩ</b> (CB કરતાં વધુ).</p>""",
          diagram="u4_ce_input"),

        T("4.3.7 CE Output Characteristics and Regions", "4.3.7 CE Output Characteristics અને Regions",
          """<p><b>Definition:</b> The curves between <b>collector current I<sub>C</sub></b> and <b>collector-emitter voltage V<sub>CE</sub></b> for different constant values of <b>I<sub>B</sub></b>.</p>
<h4>Observations</h4>
<ol>
<li>For a fixed I<sub>B</sub>, as V<sub>CE</sub> increases from 0, I<sub>C</sub> rises <b>rapidly</b> at first (up to about 0.2–1 V).</li>
<li>After that, I<sub>C</sub> becomes almost <b>constant</b> and depends mainly on I<sub>B</sub> (I<sub>C</sub> ≈ β I<sub>B</sub>). The curve rises only slightly due to the Early effect.</li>
<li>Higher I<sub>B</sub> → higher curve. Equal steps of I<sub>B</sub> give nearly equal steps of I<sub>C</sub>.</li>
</ol>
<h4>Three regions</h4>
<table>
<tr><th>Region</th><th>Where on graph</th><th>Junctions</th><th>Use</th></tr>
<tr><td><b>Active</b></td><td>Flat middle part of curves</td><td>J<sub>E</sub> FB, J<sub>C</sub> RB</td><td>Amplifier (I<sub>C</sub> = β I<sub>B</sub>)</td></tr>
<tr><td><b>Saturation</b></td><td>Steep part near the I<sub>C</sub> axis (V<sub>CE</sub> &lt; ≈ 0.2 V)</td><td>Both FB</td><td>ON switch</td></tr>
<tr><td><b>Cut-off</b></td><td>Below the I<sub>B</sub> = 0 curve</td><td>Both RB</td><td>OFF switch (only I<sub>CEO</sub> flows)</td></tr>
</table>
<h4>Parameters</h4>
<ul>
<li><b>Output resistance r<sub>o</sub> = ΔV<sub>CE</sub> / ΔI<sub>C</sub></b> (I<sub>B</sub> constant) → medium (10–50 kΩ).</li>
<li><b>AC current gain β = ΔI<sub>C</sub> / ΔI<sub>B</sub></b> (V<sub>CE</sub> constant) – can be found from two curves.</li>
</ul>""",
          """<p><b>વ્યાખ્યા:</b> <b>I<sub>B</sub></b> ના જુદા જુદા અચળ મૂલ્યો માટે <b>collector current I<sub>C</sub></b> અને <b>collector-emitter voltage V<sub>CE</sub></b> વચ્ચેના curves.</p>
<h4>અવલોકનો</h4>
<ol>
<li>નિશ્ચિત I<sub>B</sub> માટે V<sub>CE</sub> ને 0 થી વધારતાં, શરૂઆતમાં (આશરે 0.2–1 V સુધી) I<sub>C</sub> <b>ઝડપથી</b> વધે છે.</li>
<li>પછી I<sub>C</sub> લગભગ <b>અચળ</b> બને છે અને મુખ્યત્વે I<sub>B</sub> પર આધાર રાખે છે (I<sub>C</sub> ≈ β I<sub>B</sub>). Early effect ને કારણે curve થોડો જ વધે છે.</li>
<li>વધુ I<sub>B</sub> → ઉંચો curve. I<sub>B</sub> ના સમાન પગલાં I<sub>C</sub> ના લગભગ સમાન પગલાં આપે.</li>
</ol>
<h4>ત્રણ regions</h4>
<table>
<tr><th>Region</th><th>આલેખ પર ક્યાં</th><th>Junctions</th><th>ઉપયોગ</th></tr>
<tr><td><b>Active</b></td><td>Curves નો સપાટ મધ્ય ભાગ</td><td>J<sub>E</sub> FB, J<sub>C</sub> RB</td><td>Amplifier (I<sub>C</sub> = β I<sub>B</sub>)</td></tr>
<tr><td><b>Saturation</b></td><td>I<sub>C</sub> axis નજીકનો ઊભો ભાગ (V<sub>CE</sub> &lt; ≈ 0.2 V)</td><td>બંને FB</td><td>ON switch</td></tr>
<tr><td><b>Cut-off</b></td><td>I<sub>B</sub> = 0 curve ની નીચે</td><td>બંને RB</td><td>OFF switch (ફક્ત I<sub>CEO</sub> વહે)</td></tr>
</table>
<h4>Parameters</h4>
<ul>
<li><b>Output resistance r<sub>o</sub> = ΔV<sub>CE</sub> / ΔI<sub>C</sub></b> (I<sub>B</sub> અચળ) → મધ્યમ (10–50 kΩ).</li>
<li><b>AC current gain β = ΔI<sub>C</sub> / ΔI<sub>B</sub></b> (V<sub>CE</sub> અચળ) – બે curves પરથી શોધી શકાય.</li>
</ul>""",
          diagram="u4_ce_output"),

        T("4.3.8 Common Collector (CC) Configuration", "4.3.8 Common Collector (CC) Configuration",
          """<p>In CC configuration the <b>collector is common</b> to input and output. Input is applied between <b>base and collector</b>, and output is taken across the emitter resistor, between <b>emitter and collector</b> (see diagram). The collector is common through V<sub>CC</sub> (AC ground).</p>
<ul>
<li>Input current = <b>I<sub>B</sub></b>; output current = <b>I<sub>E</sub></b>.</li>
<li>It is also called an <b>emitter follower</b>, because the output (emitter) voltage follows the input (base) voltage: V<sub>out</sub> ≈ V<sub>in</sub> − 0.7 V.</li>
</ul>
<h4>Current amplification factor (γ)</h4>
<p><b>γ = ΔI<sub>E</sub> / ΔI<sub>B</sub> = 1 + β</b> → highest current gain.</p>
<h4>Features</h4>
<ul>
<li>Current gain: <b>highest</b> (1 + β)</li>
<li>Voltage gain: <b>less than 1</b> (≈ 1)</li>
<li>Power gain: low (≈ γ)</li>
<li>Input resistance: very <b>high</b> (≈ 100 kΩ – 1 MΩ)</li>
<li>Output resistance: very <b>low</b> (≈ 10 – 100 Ω)</li>
<li>Phase shift: <b>0°</b></li>
<li>Application: <b>buffer amplifier</b>, <b>impedance matching</b> (high to low impedance), driving low-impedance loads such as speakers</li>
</ul>""",
          """<p>CC configuration માં <b>collector input અને output માટે common</b> છે. Input <b>base અને collector</b> વચ્ચે લગાવાય છે અને output emitter resistor પરથી, <b>emitter અને collector</b> વચ્ચેથી લેવાય છે (આકૃતિ જુઓ). Collector, V<sub>CC</sub> (AC ground) દ્વારા common છે.</p>
<ul>
<li>Input current = <b>I<sub>B</sub></b>; output current = <b>I<sub>E</sub></b>.</li>
<li>તેને <b>Emitter follower</b> પણ કહે છે, કારણ કે output (emitter) voltage input (base) voltage ને અનુસરે છે: V<sub>out</sub> ≈ V<sub>in</sub> − 0.7 V.</li>
</ul>
<h4>Current amplification factor (γ)</h4>
<p><b>γ = ΔI<sub>E</sub> / ΔI<sub>B</sub> = 1 + β</b> → સૌથી વધુ current gain.</p>
<h4>લક્ષણો</h4>
<ul>
<li>Current gain: <b>સૌથી વધુ</b> (1 + β)</li>
<li>Voltage gain: <b>1 થી ઓછો</b> (≈ 1)</li>
<li>Power gain: ઓછો (≈ γ)</li>
<li>Input resistance: ખૂબ <b>વધુ</b> (≈ 100 kΩ – 1 MΩ)</li>
<li>Output resistance: ખૂબ <b>ઓછો</b> (≈ 10 – 100 Ω)</li>
<li>Phase shift: <b>0°</b></li>
<li>ઉપયોગ: <b>Buffer amplifier</b>, <b>Impedance matching</b> (વધુ થી ઓછા impedance સુધી), speakers જેવા ઓછા impedance વાળા loads ચલાવવા</li>
</ul>""",
          diagram="u4_cc"),

        T("4.3.9 Comparison of CB, CE and CC Configurations", "4.3.9 CB, CE અને CC Configurations ની સરખામણી",
          """<table>
<tr><th>Parameter</th><th>CB</th><th>CE</th><th>CC</th></tr>
<tr><td>Common terminal</td><td>Base</td><td>Emitter</td><td>Collector</td></tr>
<tr><td>Input / Output</td><td>E-B / C-B</td><td>B-E / C-E</td><td>B-C / E-C</td></tr>
<tr><td>Input current / Output current</td><td>I<sub>E</sub> / I<sub>C</sub></td><td>I<sub>B</sub> / I<sub>C</sub></td><td>I<sub>B</sub> / I<sub>E</sub></td></tr>
<tr><td>Current gain</td><td>α &lt; 1</td><td>β (high, 20–500)</td><td>γ = 1 + β (highest)</td></tr>
<tr><td>Voltage gain</td><td>High</td><td>High</td><td>&lt; 1 (≈ 1)</td></tr>
<tr><td>Power gain</td><td>Medium</td><td>Highest</td><td>Low</td></tr>
<tr><td>Input resistance</td><td>Very low (20–100 Ω)</td><td>Medium (≈ 1 kΩ)</td><td>Very high (100 kΩ–1 MΩ)</td></tr>
<tr><td>Output resistance</td><td>Very high (≈ 1 MΩ)</td><td>Medium (10–50 kΩ)</td><td>Very low (10–100 Ω)</td></tr>
<tr><td>Phase shift</td><td>0°</td><td>180°</td><td>0°</td></tr>
<tr><td>Applications</td><td>High-frequency (RF) amplifier</td><td>Audio / voltage amplifier, switch</td><td>Buffer, impedance matching</td></tr>
</table>
<p><b>Why is CE the most popular?</b> It gives high current gain, high voltage gain and the <b>highest power gain</b>; its input and output resistances are moderate, so stages can be cascaded easily.</p>""",
          """<table>
<tr><th>Parameter</th><th>CB</th><th>CE</th><th>CC</th></tr>
<tr><td>Common terminal</td><td>Base</td><td>Emitter</td><td>Collector</td></tr>
<tr><td>Input / Output</td><td>E-B / C-B</td><td>B-E / C-E</td><td>B-C / E-C</td></tr>
<tr><td>Input current / Output current</td><td>I<sub>E</sub> / I<sub>C</sub></td><td>I<sub>B</sub> / I<sub>C</sub></td><td>I<sub>B</sub> / I<sub>E</sub></td></tr>
<tr><td>Current gain</td><td>α &lt; 1</td><td>β (વધુ, 20–500)</td><td>γ = 1 + β (સૌથી વધુ)</td></tr>
<tr><td>Voltage gain</td><td>વધુ</td><td>વધુ</td><td>&lt; 1 (≈ 1)</td></tr>
<tr><td>Power gain</td><td>મધ્યમ</td><td>સૌથી વધુ</td><td>ઓછો</td></tr>
<tr><td>Input resistance</td><td>ખૂબ ઓછો (20–100 Ω)</td><td>મધ્યમ (≈ 1 kΩ)</td><td>ખૂબ વધુ (100 kΩ–1 MΩ)</td></tr>
<tr><td>Output resistance</td><td>ખૂબ વધુ (≈ 1 MΩ)</td><td>મધ્યમ (10–50 kΩ)</td><td>ખૂબ ઓછો (10–100 Ω)</td></tr>
<tr><td>Phase shift</td><td>0°</td><td>180°</td><td>0°</td></tr>
<tr><td>ઉપયોગો</td><td>High-frequency (RF) amplifier</td><td>Audio / voltage amplifier, switch</td><td>Buffer, impedance matching</td></tr>
</table>
<p><b>CE સૌથી લોકપ્રિય કેમ?</b> તે વધુ current gain, વધુ voltage gain અને <b>સૌથી વધુ power gain</b> આપે છે; તેના input અને output resistances મધ્યમ છે, તેથી stages સહેલાઈથી cascade કરી શકાય.</p>"""),

        T("Key Points – 4.3", "મુખ્ય મુદ્દા – 4.3",
          """<ul>
<li>Three configurations: <b>CB, CE, CC</b> – named after the terminal common to input and output.</li>
<li>CB: α &lt; 1, low r<sub>i</sub>, very high r<sub>o</sub>, 0° phase → RF amplifier.</li>
<li>CE: β high, highest power gain, 180° phase → most popular (amplifier, switch).</li>
<li>CC (emitter follower): γ = 1 + β, A<sub>v</sub> ≈ 1, high r<sub>i</sub>, low r<sub>o</sub> → buffer.</li>
<li>CE input char.: I<sub>B</sub> vs V<sub>BE</sub> (like a diode; knee 0.7 V); shifts right with higher V<sub>CE</sub> (Early effect).</li>
<li>CE output char.: I<sub>C</sub> vs V<sub>CE</sub> for fixed I<sub>B</sub>; regions – active, saturation, cut-off.</li>
<li>r<sub>i</sub> = ΔV<sub>BE</sub>/ΔI<sub>B</sub>; r<sub>o</sub> = ΔV<sub>CE</sub>/ΔI<sub>C</sub>.</li>
</ul>""",
          """<ul>
<li>ત્રણ configurations: <b>CB, CE, CC</b> – input અને output માટે common terminal પરથી નામ.</li>
<li>CB: α &lt; 1, ઓછો r<sub>i</sub>, ખૂબ વધુ r<sub>o</sub>, 0° phase → RF amplifier.</li>
<li>CE: β વધુ, સૌથી વધુ power gain, 180° phase → સૌથી લોકપ્રિય (amplifier, switch).</li>
<li>CC (emitter follower): γ = 1 + β, A<sub>v</sub> ≈ 1, વધુ r<sub>i</sub>, ઓછો r<sub>o</sub> → buffer.</li>
<li>CE input char.: I<sub>B</sub> વિરુદ્ધ V<sub>BE</sub> (diode જેવો; knee 0.7 V); વધુ V<sub>CE</sub> સાથે જમણી તરફ ખસે (Early effect).</li>
<li>CE output char.: નિશ્ચિત I<sub>B</sub> માટે I<sub>C</sub> વિરુદ્ધ V<sub>CE</sub>; regions – active, saturation, cut-off.</li>
<li>r<sub>i</sub> = ΔV<sub>BE</sub>/ΔI<sub>B</sub>; r<sub>o</sub> = ΔV<sub>CE</sub>/ΔI<sub>C</sub>.</li>
</ul>""", key=True),
    ],
}

# =====================================================================================
SEC_4_4 = {
    "title": {"en": "4.4 Current Gain and Voltage Gain", "gu": "4.4 Current Gain અને Voltage Gain"},
    "items": [
        T("4.4.1 Current Gain (α, β, γ) and Their Relations", "4.4.1 Current Gain (α, β, γ) અને તેમના સંબંધો",
          """<p><b>Current gain</b> = output current / input current. It has <b>no unit</b>.</p>
<table>
<tr><th>Gain</th><th>Configuration</th><th>Formula</th><th>Typical value</th></tr>
<tr><td><b>α</b> (alpha)</td><td>CB</td><td>α = I<sub>C</sub> / I<sub>E</sub></td><td>0.95 – 0.995 (&lt; 1)</td></tr>
<tr><td><b>β</b> (beta, h<sub>FE</sub>)</td><td>CE</td><td>β = I<sub>C</sub> / I<sub>B</sub></td><td>20 – 500</td></tr>
<tr><td><b>γ</b> (gamma)</td><td>CC</td><td>γ = I<sub>E</sub> / I<sub>B</sub></td><td>21 – 501 (= 1 + β)</td></tr>
</table>
<p><b>DC gain</b> uses DC values (e.g. β<sub>dc</sub> = h<sub>FE</sub> = I<sub>C</sub>/I<sub>B</sub>); <b>AC gain</b> uses small changes (β<sub>ac</sub> = h<sub>fe</sub> = ΔI<sub>C</sub>/ΔI<sub>B</sub>). In basic problems they are taken as equal.</p>
<h4>Derivation of relations</h4>
<p>Start with I<sub>E</sub> = I<sub>B</sub> + I<sub>C</sub>.</p>
<p><b>(1) β in terms of α:</b> β = I<sub>C</sub>/I<sub>B</sub> = I<sub>C</sub>/(I<sub>E</sub> − I<sub>C</sub>). Divide numerator and denominator by I<sub>E</sub>:</p>
<p>β = (I<sub>C</sub>/I<sub>E</sub>) / (1 − I<sub>C</sub>/I<sub>E</sub>) → <b>β = α / (1 − α)</b></p>
<p><b>(2) α in terms of β:</b> α = I<sub>C</sub>/I<sub>E</sub> = I<sub>C</sub>/(I<sub>B</sub> + I<sub>C</sub>). Divide by I<sub>B</sub>:</p>
<p>α = β / (1 + β) → <b>α = β / (1 + β)</b></p>
<p><b>(3) γ in terms of β:</b> γ = I<sub>E</sub>/I<sub>B</sub> = (I<sub>B</sub> + I<sub>C</sub>)/I<sub>B</sub> → <b>γ = 1 + β</b></p>
<p><b>(4) γ in terms of α:</b> γ = 1 + α/(1 − α) → <b>γ = 1 / (1 − α)</b></p>
<p>As α → 1, β becomes very large: α = 0.99 → β = 99; α = 0.995 → β = 199.</p>""",
          """<p><b>Current gain</b> = output current / input current. તેનો <b>કોઈ એકમ નથી</b>.</p>
<table>
<tr><th>Gain</th><th>Configuration</th><th>સૂત્ર</th><th>સામાન્ય મૂલ્ય</th></tr>
<tr><td><b>α</b> (alpha)</td><td>CB</td><td>α = I<sub>C</sub> / I<sub>E</sub></td><td>0.95 – 0.995 (&lt; 1)</td></tr>
<tr><td><b>β</b> (beta, h<sub>FE</sub>)</td><td>CE</td><td>β = I<sub>C</sub> / I<sub>B</sub></td><td>20 – 500</td></tr>
<tr><td><b>γ</b> (gamma)</td><td>CC</td><td>γ = I<sub>E</sub> / I<sub>B</sub></td><td>21 – 501 (= 1 + β)</td></tr>
</table>
<p><b>DC gain</b> માં DC મૂલ્યો વપરાય (દા.ત. β<sub>dc</sub> = h<sub>FE</sub> = I<sub>C</sub>/I<sub>B</sub>); <b>AC gain</b> માં નાના ફેરફારો વપરાય (β<sub>ac</sub> = h<sub>fe</sub> = ΔI<sub>C</sub>/ΔI<sub>B</sub>). સામાન્ય દાખલાઓમાં બંને સમાન લેવાય છે.</p>
<h4>સંબંધોની સાબિતી (Derivation)</h4>
<p>I<sub>E</sub> = I<sub>B</sub> + I<sub>C</sub> થી શરૂ કરો.</p>
<p><b>(1) α ના રૂપમાં β:</b> β = I<sub>C</sub>/I<sub>B</sub> = I<sub>C</sub>/(I<sub>E</sub> − I<sub>C</sub>). અંશ અને છેદ ને I<sub>E</sub> વડે ભાગો:</p>
<p>β = (I<sub>C</sub>/I<sub>E</sub>) / (1 − I<sub>C</sub>/I<sub>E</sub>) → <b>β = α / (1 − α)</b></p>
<p><b>(2) β ના રૂપમાં α:</b> α = I<sub>C</sub>/I<sub>E</sub> = I<sub>C</sub>/(I<sub>B</sub> + I<sub>C</sub>). I<sub>B</sub> વડે ભાગો:</p>
<p>α = β / (1 + β) → <b>α = β / (1 + β)</b></p>
<p><b>(3) β ના રૂપમાં γ:</b> γ = I<sub>E</sub>/I<sub>B</sub> = (I<sub>B</sub> + I<sub>C</sub>)/I<sub>B</sub> → <b>γ = 1 + β</b></p>
<p><b>(4) α ના રૂપમાં γ:</b> γ = 1 + α/(1 − α) → <b>γ = 1 / (1 − α)</b></p>
<p>α → 1 થાય તેમ β ખૂબ મોટો બને: α = 0.99 → β = 99; α = 0.995 → β = 199.</p>""",
          examples=["u4n6"]),

        T("4.4.2 Voltage Gain and Power Gain", "4.4.2 Voltage Gain અને Power Gain",
          """<h4>Voltage gain (A<sub>v</sub>)</h4>
<p><b>A<sub>v</sub> = output voltage / input voltage = ΔV<sub>out</sub> / ΔV<sub>in</sub></b></p>
<p>Output voltage = output current × load resistance (R<sub>L</sub>); input voltage = input current × input resistance (r<sub>i</sub>).</p>
<table>
<tr><th>Configuration</th><th>Voltage gain</th><th>Remark</th></tr>
<tr><td>CB</td><td><b>A<sub>v</sub> = α × R<sub>L</sub> / r<sub>i</sub></b></td><td>High, because R<sub>L</sub> ≫ r<sub>i</sub></td></tr>
<tr><td>CE</td><td><b>A<sub>v</sub> = β × R<sub>L</sub> / r<sub>i</sub></b></td><td>High; output inverted (−)</td></tr>
<tr><td>CC</td><td><b>A<sub>v</sub> ≈ 1</b> (slightly less)</td><td>Output follows input</td></tr>
</table>
<p>Even though α &lt; 1 in CB, voltage gain is high because the output resistance (load) is much larger than the input resistance. That is why the device is called a <b>trans-resistor</b>.</p>
<h4>Power gain (A<sub>p</sub>)</h4>
<p><b>A<sub>p</sub> = output power / input power = current gain × voltage gain</b></p>
<ul>
<li>CB: A<sub>p</sub> = α × A<sub>v</sub> (medium)</li>
<li>CE: A<sub>p</sub> = β × A<sub>v</sub> = β² R<sub>L</sub> / r<sub>i</sub> (<b>highest</b>)</li>
<li>CC: A<sub>p</sub> ≈ γ (low)</li>
</ul>
<h4>Gain in decibels</h4>
<p>Power gain (dB) = 10 log<sub>10</sub> A<sub>p</sub>; voltage gain (dB) = 20 log<sub>10</sub> A<sub>v</sub>.</p>""",
          """<h4>Voltage gain (A<sub>v</sub>)</h4>
<p><b>A<sub>v</sub> = output voltage / input voltage = ΔV<sub>out</sub> / ΔV<sub>in</sub></b></p>
<p>Output voltage = output current × load resistance (R<sub>L</sub>); input voltage = input current × input resistance (r<sub>i</sub>).</p>
<table>
<tr><th>Configuration</th><th>Voltage gain</th><th>નોંધ</th></tr>
<tr><td>CB</td><td><b>A<sub>v</sub> = α × R<sub>L</sub> / r<sub>i</sub></b></td><td>વધુ, કારણ કે R<sub>L</sub> ≫ r<sub>i</sub></td></tr>
<tr><td>CE</td><td><b>A<sub>v</sub> = β × R<sub>L</sub> / r<sub>i</sub></b></td><td>વધુ; output ઉલટો (−)</td></tr>
<tr><td>CC</td><td><b>A<sub>v</sub> ≈ 1</b> (થોડો ઓછો)</td><td>Output input ને અનુસરે</td></tr>
</table>
<p>CB માં α &lt; 1 હોવા છતાં voltage gain વધુ છે, કારણ કે output resistance (load) input resistance કરતાં ઘણો વધુ છે. તેથી જ device ને <b>trans-resistor</b> કહે છે.</p>
<h4>Power gain (A<sub>p</sub>)</h4>
<p><b>A<sub>p</sub> = output power / input power = current gain × voltage gain</b></p>
<ul>
<li>CB: A<sub>p</sub> = α × A<sub>v</sub> (મધ્યમ)</li>
<li>CE: A<sub>p</sub> = β × A<sub>v</sub> = β² R<sub>L</sub> / r<sub>i</sub> (<b>સૌથી વધુ</b>)</li>
<li>CC: A<sub>p</sub> ≈ γ (ઓછો)</li>
</ul>
<h4>Decibels માં gain</h4>
<p>Power gain (dB) = 10 log<sub>10</sub> A<sub>p</sub>; voltage gain (dB) = 20 log<sub>10</sub> A<sub>v</sub>.</p>""",
          examples=["u4n4", "u4n5"]),

        T("4.4.3 Comparison of Gains", "4.4.3 Gains ની સરખામણી",
          """<table>
<tr><th>Gain</th><th>CB</th><th>CE</th><th>CC</th></tr>
<tr><td>Current gain</td><td>α (&lt; 1)</td><td>β (high)</td><td>1 + β (highest)</td></tr>
<tr><td>Voltage gain</td><td>High (α R<sub>L</sub>/r<sub>i</sub>)</td><td>High (β R<sub>L</sub>/r<sub>i</sub>)</td><td>≈ 1</td></tr>
<tr><td>Power gain</td><td>Medium</td><td>Highest</td><td>Low</td></tr>
</table>
<h4>Remember</h4>
<ul>
<li><b>CB</b> → voltage gain only (no current gain).</li>
<li><b>CC</b> → current gain only (no voltage gain).</li>
<li><b>CE</b> → both current and voltage gain → maximum power gain.</li>
</ul>""",
          """<table>
<tr><th>Gain</th><th>CB</th><th>CE</th><th>CC</th></tr>
<tr><td>Current gain</td><td>α (&lt; 1)</td><td>β (વધુ)</td><td>1 + β (સૌથી વધુ)</td></tr>
<tr><td>Voltage gain</td><td>વધુ (α R<sub>L</sub>/r<sub>i</sub>)</td><td>વધુ (β R<sub>L</sub>/r<sub>i</sub>)</td><td>≈ 1</td></tr>
<tr><td>Power gain</td><td>મધ્યમ</td><td>સૌથી વધુ</td><td>ઓછો</td></tr>
</table>
<h4>યાદ રાખો</h4>
<ul>
<li><b>CB</b> → ફક્ત voltage gain (current gain નહીં).</li>
<li><b>CC</b> → ફક્ત current gain (voltage gain નહીં).</li>
<li><b>CE</b> → current અને voltage બંને gain → મહત્તમ power gain.</li>
</ul>"""),

        T("Key Points – 4.4", "મુખ્ય મુદ્દા – 4.4",
          """<ul>
<li><b>α = I<sub>C</sub>/I<sub>E</sub></b>, <b>β = I<sub>C</sub>/I<sub>B</sub></b>, <b>γ = I<sub>E</sub>/I<sub>B</sub></b> (no units).</li>
<li><b>β = α/(1 − α)</b>, <b>α = β/(1 + β)</b>, <b>γ = 1 + β = 1/(1 − α)</b>.</li>
<li>Voltage gain: CB = α R<sub>L</sub>/r<sub>i</sub>, CE = β R<sub>L</sub>/r<sub>i</sub>, CC ≈ 1.</li>
<li>Power gain = current gain × voltage gain; highest in CE.</li>
<li>dB: A<sub>p</sub>(dB) = 10 log A<sub>p</sub>, A<sub>v</sub>(dB) = 20 log A<sub>v</sub>.</li>
</ul>""",
          """<ul>
<li><b>α = I<sub>C</sub>/I<sub>E</sub></b>, <b>β = I<sub>C</sub>/I<sub>B</sub></b>, <b>γ = I<sub>E</sub>/I<sub>B</sub></b> (એકમ નથી).</li>
<li><b>β = α/(1 − α)</b>, <b>α = β/(1 + β)</b>, <b>γ = 1 + β = 1/(1 − α)</b>.</li>
<li>Voltage gain: CB = α R<sub>L</sub>/r<sub>i</sub>, CE = β R<sub>L</sub>/r<sub>i</sub>, CC ≈ 1.</li>
<li>Power gain = current gain × voltage gain; CE માં સૌથી વધુ.</li>
<li>dB: A<sub>p</sub>(dB) = 10 log A<sub>p</sub>, A<sub>v</sub>(dB) = 20 log A<sub>v</sub>.</li>
</ul>""", key=True),
    ],
}

# =====================================================================================
SEC_4_5 = {
    "title": {"en": "4.5 Transistor as a Switch", "gu": "4.5 Switch તરીકે Transistor"},
    "items": [
        T("4.5.1 DC Load Line and Regions for Switching", "4.5.1 DC Load Line અને Switching માટેના Regions",
          """<p>In a CE circuit, applying KVL to the collector loop:</p>
<p><b>V<sub>CE</sub> = V<sub>CC</sub> − I<sub>C</sub> R<sub>C</sub></b></p>
<p>This is the equation of a straight line called the <b>DC load line</b>. It is drawn on the output characteristics using two points:</p>
<ul>
<li><b>Cut-off point</b> (I<sub>C</sub> = 0): V<sub>CE</sub> = V<sub>CC</sub></li>
<li><b>Saturation point</b> (V<sub>CE</sub> ≈ 0): I<sub>C(sat)</sub> = V<sub>CC</sub> / R<sub>C</sub></li>
</ul>
<p>The operating point (Q-point) of the transistor always lies on this load line.</p>
<h4>Use of the regions</h4>
<ul>
<li><b>Amplifier:</b> Q-point in the middle of the load line (<b>active region</b>).</li>
<li><b>Switch:</b> the transistor is operated only at the two ends of the load line – <b>cut-off (OFF)</b> and <b>saturation (ON)</b>. It moves quickly between them and does not stay in the active region.</li>
</ul>""",
          """<p>CE circuit માં collector loop પર KVL લગાવતાં:</p>
<p><b>V<sub>CE</sub> = V<sub>CC</sub> − I<sub>C</sub> R<sub>C</sub></b></p>
<p>આ એક સીધી રેખાનું સમીકરણ છે જેને <b>DC load line</b> કહે છે. તે output characteristics પર બે બિંદુઓથી દોરાય છે:</p>
<ul>
<li><b>Cut-off બિંદુ</b> (I<sub>C</sub> = 0): V<sub>CE</sub> = V<sub>CC</sub></li>
<li><b>Saturation બિંદુ</b> (V<sub>CE</sub> ≈ 0): I<sub>C(sat)</sub> = V<sub>CC</sub> / R<sub>C</sub></li>
</ul>
<p>Transistor નું operating point (Q-point) હંમેશા આ load line પર જ હોય છે.</p>
<h4>Regions નો ઉપયોગ</h4>
<ul>
<li><b>Amplifier:</b> Q-point load line ના મધ્યમાં (<b>active region</b>).</li>
<li><b>Switch:</b> transistor ફક્ત load line ના બે છેડે ચલાવાય છે – <b>cut-off (OFF)</b> અને <b>saturation (ON)</b>. તે તેમની વચ્ચે ઝડપથી બદલાય છે અને active region માં રહેતો નથી.</li>
</ul>""",
          diagram="u4_load_line", examples=["u4n9"]),

        T("4.5.2 Working of Transistor as a Switch", "4.5.2 Switch તરીકે Transistor નું કાર્ય",
          """<p><b>Circuit:</b> An NPN transistor in CE configuration. The load (LED, lamp, relay) with R<sub>C</sub> is connected between +V<sub>CC</sub> and the collector; the emitter is grounded; the input V<sub>in</sub> is applied to the base through R<sub>B</sub> (see diagram).</p>
<h4>1. Switch OFF – Cut-off region (V<sub>in</sub> = 0 / LOW)</h4>
<ul>
<li>V<sub>BE</sub> &lt; 0.7 V → both junctions reverse biased.</li>
<li>I<sub>B</sub> = 0, so I<sub>C</sub> ≈ 0 (only tiny leakage).</li>
<li>No voltage drop across R<sub>C</sub>, so <b>V<sub>CE</sub> ≈ V<sub>CC</sub></b>.</li>
<li>The transistor behaves like an <b>open switch</b> between C and E → load (LED) is OFF.</li>
</ul>
<h4>2. Switch ON – Saturation region (V<sub>in</sub> = HIGH)</h4>
<ul>
<li>Large base current flows, both junctions become forward biased.</li>
<li>I<sub>C</sub> reaches its maximum: <b>I<sub>C(sat)</sub> = (V<sub>CC</sub> − V<sub>CE(sat)</sub>) / R<sub>C</sub> ≈ V<sub>CC</sub> / R<sub>C</sub></b>.</li>
<li><b>V<sub>CE(sat)</sub> ≈ 0.2 V</b> (almost zero).</li>
<li>The transistor behaves like a <b>closed switch</b> → load (LED) is ON.</li>
</ul>
<h4>Condition for saturation</h4>
<p><b>I<sub>B</sub> &gt; I<sub>C(sat)</sub> / β</b>. In practice I<sub>B</sub> is taken 2–10 times this value to make sure the transistor is fully ON (hard saturation).</p>
<p>Base resistor: <b>R<sub>B</sub> = (V<sub>in</sub> − V<sub>BE</sub>) / I<sub>B</sub></b></p>
<h4>Transistor switch as an inverter (NOT gate)</h4>
<p>Input LOW → output (V<sub>CE</sub>) HIGH; input HIGH → output LOW. So the transistor switch acts as a <b>NOT gate</b>.</p>
<table>
<tr><th>Point</th><th>OFF (cut-off)</th><th>ON (saturation)</th></tr>
<tr><td>V<sub>in</sub></td><td>0 (LOW)</td><td>HIGH</td></tr>
<tr><td>J<sub>E</sub>, J<sub>C</sub></td><td>Both reverse</td><td>Both forward</td></tr>
<tr><td>I<sub>C</sub></td><td>≈ 0</td><td>I<sub>C(sat)</sub> ≈ V<sub>CC</sub>/R<sub>C</sub></td></tr>
<tr><td>V<sub>CE</sub></td><td>≈ V<sub>CC</sub></td><td>≈ 0.2 V</td></tr>
<tr><td>Acts as</td><td>Open switch</td><td>Closed switch</td></tr>
</table>""",
          """<p><b>Circuit:</b> CE configuration માં NPN transistor. Load (LED, lamp, relay) R<sub>C</sub> સાથે +V<sub>CC</sub> અને collector વચ્ચે જોડાય છે; emitter ground થાય છે; input V<sub>in</sub> R<sub>B</sub> દ્વારા base પર લગાવાય છે (આકૃતિ જુઓ).</p>
<h4>1. Switch OFF – Cut-off region (V<sub>in</sub> = 0 / LOW)</h4>
<ul>
<li>V<sub>BE</sub> &lt; 0.7 V → બંને junctions reverse biased.</li>
<li>I<sub>B</sub> = 0, તેથી I<sub>C</sub> ≈ 0 (ફક્ત ખૂબ નાનો leakage).</li>
<li>R<sub>C</sub> પર કોઈ voltage drop નહીં, તેથી <b>V<sub>CE</sub> ≈ V<sub>CC</sub></b>.</li>
<li>Transistor C અને E વચ્ચે <b>ખુલ્લા switch</b> જેવું વર્તે છે → load (LED) OFF.</li>
</ul>
<h4>2. Switch ON – Saturation region (V<sub>in</sub> = HIGH)</h4>
<ul>
<li>મોટો base current વહે છે, બંને junctions forward biased થાય છે.</li>
<li>I<sub>C</sub> મહત્તમ થાય છે: <b>I<sub>C(sat)</sub> = (V<sub>CC</sub> − V<sub>CE(sat)</sub>) / R<sub>C</sub> ≈ V<sub>CC</sub> / R<sub>C</sub></b>.</li>
<li><b>V<sub>CE(sat)</sub> ≈ 0.2 V</b> (લગભગ શૂન્ય).</li>
<li>Transistor <b>બંધ switch</b> જેવું વર્તે છે → load (LED) ON.</li>
</ul>
<h4>Saturation માટેની શરત</h4>
<p><b>I<sub>B</sub> &gt; I<sub>C(sat)</sub> / β</b>. વ્યવહારમાં transistor સંપૂર્ણ ON (hard saturation) થાય તે માટે I<sub>B</sub> આ મૂલ્ય કરતાં 2–10 ગણો લેવાય છે.</p>
<p>Base resistor: <b>R<sub>B</sub> = (V<sub>in</sub> − V<sub>BE</sub>) / I<sub>B</sub></b></p>
<h4>Inverter (NOT gate) તરીકે transistor switch</h4>
<p>Input LOW → output (V<sub>CE</sub>) HIGH; input HIGH → output LOW. તેથી transistor switch <b>NOT gate</b> તરીકે કામ કરે છે.</p>
<table>
<tr><th>મુદ્દો</th><th>OFF (cut-off)</th><th>ON (saturation)</th></tr>
<tr><td>V<sub>in</sub></td><td>0 (LOW)</td><td>HIGH</td></tr>
<tr><td>J<sub>E</sub>, J<sub>C</sub></td><td>બંને reverse</td><td>બંને forward</td></tr>
<tr><td>I<sub>C</sub></td><td>≈ 0</td><td>I<sub>C(sat)</sub> ≈ V<sub>CC</sub>/R<sub>C</sub></td></tr>
<tr><td>V<sub>CE</sub></td><td>≈ V<sub>CC</sub></td><td>≈ 0.2 V</td></tr>
<tr><td>વર્તન</td><td>ખુલ્લું switch</td><td>બંધ switch</td></tr>
</table>""",
          diagram="u4_switch", examples=["u4n7"]),

        T("4.5.3 Applications and Advantages of Transistor Switch", "4.5.3 Transistor Switch ના ઉપયોગો અને ફાયદા",
          """<h4>Applications</h4>
<ul>
<li><b>LED / lamp driver</b> – microcontroller (Arduino) pins give small current; a transistor switches the larger load current.</li>
<li><b>Relay driver</b> – switches a relay coil to control AC appliances (with a freewheeling diode across the coil).</li>
<li><b>Motor and buzzer control</b>.</li>
<li><b>Digital logic circuits</b> – NOT, NAND, NOR gates (TTL logic).</li>
<li><b>Automatic street light</b> (with LDR), fire/water-level alarms, touch switches.</li>
<li>Switching power supplies (SMPS), inverters and PWM control.</li>
</ul>
<h4>Advantages over a mechanical switch</h4>
<table>
<tr><th>Point</th><th>Transistor switch</th><th>Mechanical switch</th></tr>
<tr><td>Moving parts</td><td>None</td><td>Yes (wear and tear)</td></tr>
<tr><td>Switching speed</td><td>Very fast (µs – ns)</td><td>Slow (ms)</td></tr>
<tr><td>Sparking / bouncing</td><td>No</td><td>Yes</td></tr>
<tr><td>Control</td><td>Electronic (small signal)</td><td>Manual</td></tr>
<tr><td>Life</td><td>Very long</td><td>Limited</td></tr>
<tr><td>Size</td><td>Very small</td><td>Larger</td></tr>
</table>
<p><b>Limitations:</b> small voltage drop when ON (V<sub>CE(sat)</sub>), small leakage when OFF, limited current/voltage rating; it is used for DC loads (AC loads via relay/TRIAC).</p>""",
          """<h4>ઉપયોગો</h4>
<ul>
<li><b>LED / lamp driver</b> – microcontroller (Arduino) pins નાનો current આપે છે; transistor મોટો load current switch કરે છે.</li>
<li><b>Relay driver</b> – AC appliances નિયંત્રિત કરવા relay coil ને switch કરે (coil પર freewheeling diode સાથે).</li>
<li><b>Motor અને buzzer નિયંત્રણ</b>.</li>
<li><b>Digital logic circuits</b> – NOT, NAND, NOR gates (TTL logic).</li>
<li><b>Automatic street light</b> (LDR સાથે), fire/water-level alarms, touch switches.</li>
<li>Switching power supplies (SMPS), inverters અને PWM control.</li>
</ul>
<h4>Mechanical switch કરતાં ફાયદા</h4>
<table>
<tr><th>મુદ્દો</th><th>Transistor switch</th><th>Mechanical switch</th></tr>
<tr><td>હલતા ભાગો</td><td>નથી</td><td>છે (ઘસારો)</td></tr>
<tr><td>Switching ઝડપ</td><td>ખૂબ ઝડપી (µs – ns)</td><td>ધીમું (ms)</td></tr>
<tr><td>Sparking / bouncing</td><td>નથી</td><td>છે</td></tr>
<tr><td>નિયંત્રણ</td><td>Electronic (નાનો signal)</td><td>હાથથી</td></tr>
<tr><td>આયુષ્ય</td><td>ખૂબ લાંબું</td><td>મર્યાદિત</td></tr>
<tr><td>કદ</td><td>ખૂબ નાનું</td><td>મોટું</td></tr>
</table>
<p><b>મર્યાદાઓ:</b> ON હોય ત્યારે નાનો voltage drop (V<sub>CE(sat)</sub>), OFF હોય ત્યારે નાનો leakage, મર્યાદિત current/voltage rating; DC loads માટે વપરાય (AC loads relay/TRIAC દ્વારા).</p>"""),

        T("Key Points – 4.5", "મુખ્ય મુદ્દા – 4.5",
          """<ul>
<li>DC load line: <b>V<sub>CE</sub> = V<sub>CC</sub> − I<sub>C</sub>R<sub>C</sub></b>; end points (V<sub>CC</sub>, 0) and (0, V<sub>CC</sub>/R<sub>C</sub>).</li>
<li>Amplifier → active region (middle); switch → cut-off and saturation (ends).</li>
<li><b>OFF:</b> V<sub>in</sub> LOW, I<sub>B</sub> = 0, I<sub>C</sub> ≈ 0, V<sub>CE</sub> ≈ V<sub>CC</sub> → open switch.</li>
<li><b>ON:</b> V<sub>in</sub> HIGH, I<sub>C</sub> = I<sub>C(sat)</sub>, V<sub>CE</sub> ≈ 0.2 V → closed switch.</li>
<li>Saturation condition: <b>I<sub>B</sub> &gt; I<sub>C(sat)</sub>/β</b>; R<sub>B</sub> = (V<sub>in</sub> − 0.7)/I<sub>B</sub>.</li>
<li>Transistor switch = <b>NOT gate</b>; used for LED/relay/motor drivers; faster and longer-lasting than mechanical switches.</li>
</ul>""",
          """<ul>
<li>DC load line: <b>V<sub>CE</sub> = V<sub>CC</sub> − I<sub>C</sub>R<sub>C</sub></b>; છેડાના બિંદુઓ (V<sub>CC</sub>, 0) અને (0, V<sub>CC</sub>/R<sub>C</sub>).</li>
<li>Amplifier → active region (મધ્ય); switch → cut-off અને saturation (છેડા).</li>
<li><b>OFF:</b> V<sub>in</sub> LOW, I<sub>B</sub> = 0, I<sub>C</sub> ≈ 0, V<sub>CE</sub> ≈ V<sub>CC</sub> → ખુલ્લું switch.</li>
<li><b>ON:</b> V<sub>in</sub> HIGH, I<sub>C</sub> = I<sub>C(sat)</sub>, V<sub>CE</sub> ≈ 0.2 V → બંધ switch.</li>
<li>Saturation શરત: <b>I<sub>B</sub> &gt; I<sub>C(sat)</sub>/β</b>; R<sub>B</sub> = (V<sub>in</sub> − 0.7)/I<sub>B</sub>.</li>
<li>Transistor switch = <b>NOT gate</b>; LED/relay/motor drivers માટે વપરાય; mechanical switches કરતાં ઝડપી અને લાંબું ટકે.</li>
</ul>""", key=True),
    ],
}

NOTES_B = [SEC_4_3, SEC_4_4, SEC_4_5]
