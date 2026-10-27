"""Basics of Electronics (DI01000151) - Unit 5: IC 555 Timer (part A: 5.1 - 5.3)"""
from content_DI01000151_u3_notes_a import T

# =====================================================================================
SEC_5_1 = {
    "title": {"en": "5.1 Introduction to IC 555", "gu": "5.1 IC 555 નો પરિચય"},
    "items": [
        T("5.1.1 What is IC 555?", "5.1.1 IC 555 એટલે શું?",
          """<p>The <b>IC 555</b> is a very popular, low-cost <b>integrated circuit</b> used to produce accurate <b>time delays</b> and <b>oscillations</b> (square / rectangular waves). It is commonly called the <b>555 timer</b>.</p>
<h4>History</h4>
<ul>
<li>Designed by <b>Hans R. Camenzind</b> and introduced by <b>Signetics Corporation</b> in <b>1971</b> (part number <b>NE555</b>).</li>
<li>The name "555" is usually explained by the <b>three 5 kΩ resistors</b> used inside the IC as a voltage divider.</li>
<li>It is one of the most widely produced ICs in the world – billions are made every year.</li>
</ul>
<h4>Versions of 555</h4>
<table>
<tr><th>Version</th><th>Description</th></tr>
<tr><td><b>NE555</b></td><td>Commercial grade, 0 °C to 70 °C</td></tr>
<tr><td><b>SE555</b></td><td>Military grade, −55 °C to +125 °C</td></tr>
<tr><td><b>556</b></td><td>Dual timer – two 555 timers in one 14-pin IC</td></tr>
<tr><td><b>558</b></td><td>Quad timer – four timers in one 16-pin IC</td></tr>
<tr><td><b>7555 / TLC555 / LMC555</b></td><td>CMOS versions – very low power, can work from about 2 V</td></tr>
</table>
<h4>Packages</h4>
<p>It is available as an <b>8-pin DIP</b> (Dual In-line Package), 8-pin metal can (TO-99) and 8-pin SMD (SOIC) package. The 8-pin DIP is used in the laboratory.</p>""",
          """<p><b>IC 555</b> એ ખૂબ જાણીતું અને સસ્તું <b>integrated circuit</b> છે, જે ચોક્કસ <b>time delay</b> અને <b>oscillations</b> (square / rectangular waves) ઉત્પન્ન કરવા વપરાય છે. તેને સામાન્ય રીતે <b>555 timer</b> કહે છે.</p>
<h4>ઇતિહાસ</h4>
<ul>
<li><b>Hans R. Camenzind</b> એ ડિઝાઇન કર્યું અને <b>Signetics Corporation</b> એ <b>1971</b> માં રજૂ કર્યું (part number <b>NE555</b>).</li>
<li>"555" નામ સામાન્ય રીતે IC ની અંદર voltage divider તરીકે વપરાતા <b>ત્રણ 5 kΩ resistors</b> પરથી સમજાવાય છે.</li>
<li>દુનિયામાં સૌથી વધુ બનતા ICs માંનું એક છે – દર વર્ષે અબજો બને છે.</li>
</ul>
<h4>555 ના પ્રકારો (Versions)</h4>
<table>
<tr><th>Version</th><th>વર્ણન</th></tr>
<tr><td><b>NE555</b></td><td>Commercial grade, 0 °C થી 70 °C</td></tr>
<tr><td><b>SE555</b></td><td>Military grade, −55 °C થી +125 °C</td></tr>
<tr><td><b>556</b></td><td>Dual timer – એક 14-pin IC માં બે 555 timers</td></tr>
<tr><td><b>558</b></td><td>Quad timer – એક 16-pin IC માં ચાર timers</td></tr>
<tr><td><b>7555 / TLC555 / LMC555</b></td><td>CMOS versions – ખૂબ ઓછો power, લગભગ 2 V થી પણ કામ કરે</td></tr>
</table>
<h4>Packages</h4>
<p>તે <b>8-pin DIP</b> (Dual In-line Package), 8-pin metal can (TO-99) અને 8-pin SMD (SOIC) package માં મળે છે. Laboratory માં 8-pin DIP વપરાય છે.</p>"""),

        T("5.1.2 Features of IC 555", "5.1.2 IC 555 ની વિશેષતાઓ (Features)",
          """<ul>
<li><b>Wide supply voltage:</b> +4.5 V to +15 V (maximum 16–18 V, depending on manufacturer).</li>
<li><b>Timing range:</b> from a few <b>microseconds to hours</b>, set by external R and C only.</li>
<li><b>High output current:</b> output can <b>source or sink up to 200 mA</b> – can drive LEDs, relays, buzzers and small lamps directly.</li>
<li><b>Output compatible with TTL</b> logic when operated from a 5 V supply.</li>
<li><b>Adjustable duty cycle</b> in astable mode.</li>
<li><b>High temperature stability:</b> about <b>0.005 % per °C</b>.</li>
<li>Timing is <b>independent of supply voltage</b> because the thresholds are fixed fractions (⅔ and ⅓) of V<sub>CC</sub>.</li>
<li>Works in <b>monostable</b>, <b>astable</b> and <b>bistable</b> modes.</li>
<li>Small size, low cost, easily available and needs very few external components.</li>
</ul>
<h4>Typical ratings (NE555)</h4>
<table>
<tr><th>Parameter</th><th>Value</th></tr>
<tr><td>Supply voltage (V<sub>CC</sub>)</td><td>4.5 V – 15 V</td></tr>
<tr><td>Supply current (V<sub>CC</sub> = 5 V)</td><td>3 – 6 mA</td></tr>
<tr><td>Maximum output current</td><td>200 mA</td></tr>
<tr><td>Maximum power dissipation</td><td>600 mW</td></tr>
<tr><td>Maximum operating frequency</td><td>about 500 kHz</td></tr>
<tr><td>Output HIGH level</td><td>≈ V<sub>CC</sub> − 1.7 V</td></tr>
<tr><td>Output LOW level</td><td>≈ 0.1 V</td></tr>
</table>""",
          """<ul>
<li><b>વિશાળ supply voltage:</b> +4.5 V થી +15 V (manufacturer પ્રમાણે મહત્તમ 16–18 V).</li>
<li><b>Timing range:</b> થોડા <b>microseconds થી કલાકો</b> સુધી, ફક્ત બહારના R અને C થી નક્કી થાય.</li>
<li><b>વધુ output current:</b> output <b>200 mA સુધી source અથવા sink</b> કરી શકે – LEDs, relays, buzzers અને નાના lamps સીધા ચલાવી શકે.</li>
<li>5 V supply પર output <b>TTL logic compatible</b> છે.</li>
<li>Astable mode માં <b>duty cycle બદલી શકાય</b>.</li>
<li><b>ઉચ્ચ temperature stability:</b> લગભગ <b>0.005 % પ્રતિ °C</b>.</li>
<li>Thresholds V<sub>CC</sub> ના નિશ્ચિત ભાગ (⅔ અને ⅓) હોવાથી timing <b>supply voltage થી સ્વતંત્ર</b> છે.</li>
<li><b>Monostable</b>, <b>astable</b> અને <b>bistable</b> modes માં કામ કરે.</li>
<li>નાનું કદ, ઓછી કિંમત, સહેલાઈથી મળે અને બહુ ઓછા external components જોઈએ.</li>
</ul>
<h4>સામાન્ય ratings (NE555)</h4>
<table>
<tr><th>Parameter</th><th>મૂલ્ય</th></tr>
<tr><td>Supply voltage (V<sub>CC</sub>)</td><td>4.5 V – 15 V</td></tr>
<tr><td>Supply current (V<sub>CC</sub> = 5 V)</td><td>3 – 6 mA</td></tr>
<tr><td>મહત્તમ output current</td><td>200 mA</td></tr>
<tr><td>મહત્તમ power dissipation</td><td>600 mW</td></tr>
<tr><td>મહત્તમ operating frequency</td><td>લગભગ 500 kHz</td></tr>
<tr><td>Output HIGH level</td><td>≈ V<sub>CC</sub> − 1.7 V</td></tr>
<tr><td>Output LOW level</td><td>≈ 0.1 V</td></tr>
</table>"""),

        T("5.1.3 Modes of Operation", "5.1.3 Operation ના Modes",
          """<p>The 555 timer can be operated in three basic modes:</p>
<table>
<tr><th>Mode</th><th>Other name</th><th>Stable states</th><th>Output</th><th>Uses</th></tr>
<tr><td><b>Monostable</b></td><td>One-shot multivibrator</td><td>One (LOW)</td><td>One pulse of fixed width T = 1.1RC for each trigger</td><td>Timers, delay circuits, pulse stretching, debouncing</td></tr>
<tr><td><b>Astable</b></td><td>Free-running multivibrator</td><td>None (both quasi-stable)</td><td>Continuous rectangular wave, no trigger needed</td><td>Oscillators, LED flashers, clock pulses, tone generators</td></tr>
<tr><td><b>Bistable</b></td><td>Flip-flop / Schmitt trigger</td><td>Two</td><td>Stays HIGH or LOW until changed by trigger / reset</td><td>ON-OFF switches, memory, debouncing</td></tr>
</table>
<p><b>Multivibrator:</b> a circuit that switches between two states (HIGH and LOW). The number of <b>stable states</b> gives its type: mono (1), a-stable (0), bi-stable (2).</p>""",
          """<p>555 timer ને ત્રણ મૂળભૂત modes માં ચલાવી શકાય છે:</p>
<table>
<tr><th>Mode</th><th>બીજું નામ</th><th>Stable states</th><th>Output</th><th>ઉપયોગ</th></tr>
<tr><td><b>Monostable</b></td><td>One-shot multivibrator</td><td>એક (LOW)</td><td>દરેક trigger માટે નિશ્ચિત પહોળાઈ T = 1.1RC નો એક pulse</td><td>Timers, delay circuits, pulse stretching, debouncing</td></tr>
<tr><td><b>Astable</b></td><td>Free-running multivibrator</td><td>એક પણ નહીં (બંને quasi-stable)</td><td>સતત rectangular wave, trigger ની જરૂર નથી</td><td>Oscillators, LED flashers, clock pulses, tone generators</td></tr>
<tr><td><b>Bistable</b></td><td>Flip-flop / Schmitt trigger</td><td>બે</td><td>Trigger / reset થી બદલાય ત્યાં સુધી HIGH અથવા LOW રહે</td><td>ON-OFF switches, memory, debouncing</td></tr>
</table>
<p><b>Multivibrator:</b> બે states (HIGH અને LOW) વચ્ચે બદલાતો circuit. <b>Stable states</b> ની સંખ્યા પરથી પ્રકાર નક્કી થાય: mono (1), a-stable (0), bi-stable (2).</p>"""),

        T("5.1.4 Advantages, Limitations and Applications", "5.1.4 ફાયદા, મર્યાદાઓ અને ઉપયોગો",
          """<h4>Advantages</h4>
<ul>
<li>Very cheap, easily available, simple to use.</li>
<li>Wide range of supply voltage and timing.</li>
<li>High output current (200 mA) – drives loads directly.</li>
<li>Timing does not depend on supply voltage; good temperature stability.</li>
</ul>
<h4>Limitations</h4>
<ul>
<li>The bipolar NE555 draws a large current spike during output switching; needs a decoupling capacitor across the supply.</li>
<li>Maximum frequency about 500 kHz – not suitable for very high frequencies.</li>
<li>For very long delays, large capacitors are needed; leakage of electrolytic capacitors reduces accuracy.</li>
<li>In the basic astable circuit the duty cycle is always more than 50 %.</li>
</ul>
<h4>Applications</h4>
<p>Pulse generator, square-wave oscillator, time-delay circuit, LED flasher, traffic-light timer, burglar alarm, missing-pulse detector, frequency divider, PWM (pulse width modulation), frequency counter (gate pulse), tone / siren generator, touch switch, water-level indicator, DC-DC converter, etc.</p>""",
          """<h4>ફાયદા</h4>
<ul>
<li>ખૂબ સસ્તું, સહેલાઈથી મળે, વાપરવામાં સરળ.</li>
<li>Supply voltage અને timing ની વિશાળ range.</li>
<li>વધુ output current (200 mA) – loads ને સીધા ચલાવે.</li>
<li>Timing supply voltage પર આધાર રાખતું નથી; સારી temperature stability.</li>
</ul>
<h4>મર્યાદાઓ</h4>
<ul>
<li>Bipolar NE555 output switching વખતે મોટો current spike લે છે; supply પર decoupling capacitor જોઈએ.</li>
<li>મહત્તમ frequency લગભગ 500 kHz – ખૂબ ઊંચી frequencies માટે યોગ્ય નથી.</li>
<li>ખૂબ લાંબા delay માટે મોટા capacitors જોઈએ; electrolytic capacitors નો leakage ચોકસાઈ ઘટાડે.</li>
<li>Basic astable circuit માં duty cycle હંમેશા 50 % થી વધુ હોય છે.</li>
</ul>
<h4>ઉપયોગો</h4>
<p>Pulse generator, square-wave oscillator, time-delay circuit, LED flasher, traffic-light timer, burglar alarm, missing-pulse detector, frequency divider, PWM (pulse width modulation), frequency counter (gate pulse), tone / siren generator, touch switch, water-level indicator, DC-DC converter વગેરે.</p>"""),

        T("Key Points – 5.1", "મુખ્ય મુદ્દા – 5.1",
          """<ul>
<li>IC 555 = timer IC by <b>Signetics, 1971</b> (designer <b>Hans Camenzind</b>); named after the <b>three 5 kΩ</b> resistors.</li>
<li>NE555 (commercial), SE555 (military), 556 (dual), 558 (quad), 7555 (CMOS).</li>
<li>Supply <b>4.5 – 15 V</b>; output current <b>200 mA</b>; timing µs to hours; f<sub>max</sub> ≈ 500 kHz.</li>
<li>Three modes: <b>monostable</b> (1 stable state), <b>astable</b> (0), <b>bistable</b> (2).</li>
<li>Timing is independent of V<sub>CC</sub> because thresholds are ⅔V<sub>CC</sub> and ⅓V<sub>CC</sub>.</li>
</ul>""",
          """<ul>
<li>IC 555 = <b>Signetics, 1971</b> નું timer IC (designer <b>Hans Camenzind</b>); નામ <b>ત્રણ 5 kΩ</b> resistors પરથી.</li>
<li>NE555 (commercial), SE555 (military), 556 (dual), 558 (quad), 7555 (CMOS).</li>
<li>Supply <b>4.5 – 15 V</b>; output current <b>200 mA</b>; timing µs થી કલાકો; f<sub>max</sub> ≈ 500 kHz.</li>
<li>ત્રણ modes: <b>monostable</b> (1 stable state), <b>astable</b> (0), <b>bistable</b> (2).</li>
<li>Thresholds ⅔V<sub>CC</sub> અને ⅓V<sub>CC</sub> હોવાથી timing V<sub>CC</sub> થી સ્વતંત્ર છે.</li>
</ul>""", key=True),
    ],
}

# =====================================================================================
SEC_5_2 = {
    "title": {"en": "5.2 Pin Diagram and Pin Functions", "gu": "5.2 Pin Diagram અને Pin ના કાર્યો"},
    "items": [
        T("5.2.1 Pin Diagram of IC 555", "5.2.1 IC 555 નો Pin Diagram",
          """<p>IC 555 in an <b>8-pin DIP</b> package has four pins on each side. Looking from the <b>top</b>, with the notch upward, <b>pin 1</b> is at the top-left (near the dot / notch) and pins are numbered <b>anticlockwise</b>: 1 → 4 down the left side and 5 → 8 up the right side.</p>
<table>
<tr><th>Pin</th><th>Name</th><th>Pin</th><th>Name</th></tr>
<tr><td>1</td><td>Ground (GND)</td><td>8</td><td>+V<sub>CC</sub></td></tr>
<tr><td>2</td><td>Trigger</td><td>7</td><td>Discharge</td></tr>
<tr><td>3</td><td>Output</td><td>6</td><td>Threshold</td></tr>
<tr><td>4</td><td>Reset</td><td>5</td><td>Control Voltage</td></tr>
</table>
<p><i>Memory tip:</i> opposite pins add up to 9 → (1, 8) supply pins, (2, 7), (3, 6), (4, 5).</p>""",
          """<p><b>8-pin DIP</b> package વાળા IC 555 માં દરેક બાજુ ચાર pins છે. Notch ઉપર રાખી <b>ઉપરથી</b> જોતાં <b>pin 1</b> ઉપર-ડાબી બાજુ (dot / notch પાસે) હોય છે અને pins <b>anticlockwise</b> ગણાય છે: ડાબી બાજુ નીચે 1 → 4 અને જમણી બાજુ ઉપર 5 → 8.</p>
<table>
<tr><th>Pin</th><th>નામ</th><th>Pin</th><th>નામ</th></tr>
<tr><td>1</td><td>Ground (GND)</td><td>8</td><td>+V<sub>CC</sub></td></tr>
<tr><td>2</td><td>Trigger</td><td>7</td><td>Discharge</td></tr>
<tr><td>3</td><td>Output</td><td>6</td><td>Threshold</td></tr>
<tr><td>4</td><td>Reset</td><td>5</td><td>Control Voltage</td></tr>
</table>
<p><i>યાદ રાખવાની રીત:</i> સામ-સામેના pins નો સરવાળો 9 → (1, 8) supply pins, (2, 7), (3, 6), (4, 5).</p>""",
          diagram="u5_pin_diagram"),

        T("5.2.2 Functions of Pins 1 to 4", "5.2.2 Pin 1 થી 4 ના કાર્યો",
          """<h4>Pin 1 – Ground (GND)</h4>
<p>All voltages are measured with respect to this pin. It is connected to the <b>negative terminal</b> (0 V) of the supply.</p>
<h4>Pin 2 – Trigger</h4>
<ul>
<li>It is the <b>inverting (−) input of the lower comparator</b> (comparator 2). Its other input is fixed at <b>⅓V<sub>CC</sub></b>.</li>
<li>When the voltage at pin 2 falls <b>below ⅓V<sub>CC</sub></b>, the comparator output goes HIGH and <b>sets</b> the flip-flop → <b>output (pin 3) goes HIGH</b>.</li>
<li>In monostable mode, a <b>negative-going trigger pulse</b> is applied here to start the timing.</li>
<li>Normally kept above ⅓V<sub>CC</sub> using a pull-up resistor.</li>
</ul>
<h4>Pin 3 – Output</h4>
<ul>
<li>Output of the timer, taken from a <b>totem-pole output stage</b>.</li>
<li>HIGH ≈ V<sub>CC</sub> − 1.7 V and LOW ≈ 0 V.</li>
<li>Can <b>source</b> current (load between pin 3 and ground, ON when output HIGH) or <b>sink</b> current (load between V<sub>CC</sub> and pin 3, ON when output LOW), up to <b>200 mA</b>.</li>
</ul>
<h4>Pin 4 – Reset</h4>
<ul>
<li><b>Active-LOW</b> reset input. When a voltage <b>below about 0.7 V</b> is applied, the flip-flop is reset: <b>output goes LOW</b> and the discharge transistor turns ON, whatever the other inputs.</li>
<li>It has the highest priority over all other inputs.</li>
<li>When not used, it is <b>connected to +V<sub>CC</sub></b> to avoid false resetting by noise.</li>
</ul>""",
          """<h4>Pin 1 – Ground (GND)</h4>
<p>બધા voltages આ pin ના સંદર્ભમાં માપાય છે. તેને supply ના <b>negative terminal</b> (0 V) સાથે જોડાય છે.</p>
<h4>Pin 2 – Trigger</h4>
<ul>
<li>તે <b>નીચેના comparator (comparator 2) નો inverting (−) input</b> છે. તેનો બીજો input <b>⅓V<sub>CC</sub></b> પર નિશ્ચિત છે.</li>
<li>Pin 2 નો voltage <b>⅓V<sub>CC</sub> થી નીચે</b> જાય ત્યારે comparator output HIGH થાય અને flip-flop ને <b>set</b> કરે → <b>output (pin 3) HIGH</b> થાય.</li>
<li>Monostable mode માં timing શરૂ કરવા અહીં <b>negative-going trigger pulse</b> અપાય છે.</li>
<li>સામાન્ય રીતે pull-up resistor વડે ⅓V<sub>CC</sub> થી ઉપર રખાય છે.</li>
</ul>
<h4>Pin 3 – Output</h4>
<ul>
<li>Timer નો output, <b>totem-pole output stage</b> માંથી લેવાય છે.</li>
<li>HIGH ≈ V<sub>CC</sub> − 1.7 V અને LOW ≈ 0 V.</li>
<li><b>Source</b> current (load pin 3 અને ground વચ્ચે, output HIGH હોય ત્યારે ON) અથવા <b>sink</b> current (load V<sub>CC</sub> અને pin 3 વચ્ચે, output LOW હોય ત્યારે ON) <b>200 mA</b> સુધી આપી શકે.</li>
</ul>
<h4>Pin 4 – Reset</h4>
<ul>
<li><b>Active-LOW</b> reset input. <b>લગભગ 0.7 V થી ઓછો</b> voltage આપતાં flip-flop reset થાય: બીજા inputs ગમે તે હોય તો પણ <b>output LOW</b> થાય અને discharge transistor ON થાય.</li>
<li>બધા inputs કરતાં તેની priority સૌથી વધુ છે.</li>
<li>ઉપયોગ ન હોય ત્યારે noise થી ખોટું reset ન થાય તે માટે તેને <b>+V<sub>CC</sub> સાથે જોડાય</b> છે.</li>
</ul>"""),

        T("5.2.3 Functions of Pins 5 to 8", "5.2.3 Pin 5 થી 8 ના કાર્યો",
          """<h4>Pin 5 – Control Voltage (CV)</h4>
<ul>
<li>It is connected directly to the <b>⅔V<sub>CC</sub> point</b> of the internal voltage divider (inverting input of the upper comparator).</li>
<li>By applying an external voltage here, the threshold levels can be changed: upper = V<sub>CON</sub>, lower = V<sub>CON</sub>/2. This changes the timing / frequency → used for <b>PWM</b> and <b>voltage-controlled oscillators (VCO)</b>.</li>
<li>When not used, it is connected to ground through a <b>0.01 µF capacitor</b> to bypass noise and keep the thresholds stable.</li>
</ul>
<h4>Pin 6 – Threshold</h4>
<ul>
<li>It is the <b>non-inverting (+) input of the upper comparator</b> (comparator 1), compared with <b>⅔V<sub>CC</sub></b>.</li>
<li>When the voltage at pin 6 rises <b>above ⅔V<sub>CC</sub></b>, the comparator output goes HIGH and <b>resets</b> the flip-flop → <b>output goes LOW</b>.</li>
<li>Usually connected to the timing capacitor, which it monitors.</li>
</ul>
<h4>Pin 7 – Discharge</h4>
<ul>
<li>Connected to the <b>open collector of the internal discharge transistor</b> (Q<sub>d</sub>).</li>
<li>When output is LOW, Q<sub>d</sub> is ON (saturated) and gives a <b>discharge path</b> to the timing capacitor. When output is HIGH, Q<sub>d</sub> is OFF and the capacitor can charge.</li>
</ul>
<h4>Pin 8 – +V<sub>CC</sub></h4>
<p>Positive supply pin, <b>+4.5 V to +15 V</b> with respect to pin 1. A 0.1 µF decoupling capacitor between pins 8 and 1 is recommended.</p>""",
          """<h4>Pin 5 – Control Voltage (CV)</h4>
<ul>
<li>તે અંદરના voltage divider ના <b>⅔V<sub>CC</sub> બિંદુ</b> (ઉપરના comparator નો inverting input) સાથે સીધો જોડાયેલો છે.</li>
<li>અહીં બહારનો voltage આપીને threshold levels બદલી શકાય: upper = V<sub>CON</sub>, lower = V<sub>CON</sub>/2. તેથી timing / frequency બદલાય → <b>PWM</b> અને <b>voltage-controlled oscillator (VCO)</b> માટે વપરાય.</li>
<li>ઉપયોગ ન હોય ત્યારે noise bypass કરવા અને thresholds સ્થિર રાખવા તેને <b>0.01 µF capacitor</b> દ્વારા ground સાથે જોડાય છે.</li>
</ul>
<h4>Pin 6 – Threshold</h4>
<ul>
<li>તે <b>ઉપરના comparator (comparator 1) નો non-inverting (+) input</b> છે, જેની સરખામણી <b>⅔V<sub>CC</sub></b> સાથે થાય છે.</li>
<li>Pin 6 નો voltage <b>⅔V<sub>CC</sub> થી ઉપર</b> જાય ત્યારે comparator output HIGH થાય અને flip-flop ને <b>reset</b> કરે → <b>output LOW</b> થાય.</li>
<li>સામાન્ય રીતે timing capacitor સાથે જોડાય છે અને તેના voltage પર નજર રાખે છે.</li>
</ul>
<h4>Pin 7 – Discharge</h4>
<ul>
<li>અંદરના <b>discharge transistor</b> (Q<sub>d</sub>) ના <b>open collector</b> સાથે જોડાયેલો છે.</li>
<li>Output LOW હોય ત્યારે Q<sub>d</sub> ON (saturated) હોય અને timing capacitor ને <b>discharge path</b> આપે. Output HIGH હોય ત્યારે Q<sub>d</sub> OFF હોય અને capacitor charge થઈ શકે.</li>
</ul>
<h4>Pin 8 – +V<sub>CC</sub></h4>
<p>Positive supply pin, pin 1 ના સંદર્ભમાં <b>+4.5 V થી +15 V</b>. Pins 8 અને 1 વચ્ચે 0.1 µF decoupling capacitor રાખવાની ભલામણ છે.</p>"""),

        T("Key Points – 5.2", "મુખ્ય મુદ્દા – 5.2",
          """<ul>
<li>Pins: 1 GND, 2 Trigger, 3 Output, 4 Reset, 5 Control, 6 Threshold, 7 Discharge, 8 V<sub>CC</sub>.</li>
<li>Trigger (2) &lt; ⅓V<sub>CC</sub> → output HIGH; Threshold (6) &gt; ⅔V<sub>CC</sub> → output LOW.</li>
<li>Reset (4) is <b>active LOW</b> → tie to V<sub>CC</sub> when unused.</li>
<li>Control (5) → <b>0.01 µF</b> to ground when unused; external voltage changes the thresholds.</li>
<li>Discharge (7) → shorts the timing capacitor to ground when output is LOW.</li>
<li>Output (3) sources / sinks up to <b>200 mA</b>.</li>
</ul>""",
          """<ul>
<li>Pins: 1 GND, 2 Trigger, 3 Output, 4 Reset, 5 Control, 6 Threshold, 7 Discharge, 8 V<sub>CC</sub>.</li>
<li>Trigger (2) &lt; ⅓V<sub>CC</sub> → output HIGH; Threshold (6) &gt; ⅔V<sub>CC</sub> → output LOW.</li>
<li>Reset (4) <b>active LOW</b> છે → ઉપયોગ ન હોય ત્યારે V<sub>CC</sub> સાથે જોડો.</li>
<li>Control (5) → ઉપયોગ ન હોય ત્યારે <b>0.01 µF</b> દ્વારા ground; બહારનો voltage thresholds બદલે.</li>
<li>Discharge (7) → output LOW હોય ત્યારે timing capacitor ને ground સાથે short કરે.</li>
<li>Output (3) <b>200 mA</b> સુધી source / sink કરે.</li>
</ul>""", key=True),
    ],
}

# =====================================================================================
SEC_5_3 = {
    "title": {"en": "5.3 Functional Block Diagram of IC 555", "gu": "5.3 IC 555 નો Functional Block Diagram"},
    "items": [
        T("5.3.1 Internal Blocks of IC 555", "5.3.1 IC 555 ના અંદરના Blocks",
          """<p>The internal circuit of IC 555 contains about 25 transistors, 2 diodes and 15 resistors. Functionally it can be represented by the following blocks (see diagram):</p>
<h4>1. Voltage divider</h4>
<p>Three equal <b>5 kΩ resistors</b> connected in series between V<sub>CC</sub> (pin 8) and ground (pin 1). They produce two <b>reference voltages</b>:</p>
<ul>
<li><b>⅔V<sub>CC</sub></b> at the junction of the upper two resistors (also brought out at pin 5) → reference for the upper comparator.</li>
<li><b>⅓V<sub>CC</sub></b> at the junction of the lower two resistors → reference for the lower comparator.</li>
</ul>
<h4>2. Upper comparator (Comparator 1 – threshold comparator)</h4>
<p>(+) input = threshold (pin 6), (−) input = ⅔V<sub>CC</sub>. Its output goes <b>HIGH when V<sub>6</sub> &gt; ⅔V<sub>CC</sub></b>. It drives the <b>R (reset)</b> input of the flip-flop.</p>
<h4>3. Lower comparator (Comparator 2 – trigger comparator)</h4>
<p>(+) input = ⅓V<sub>CC</sub>, (−) input = trigger (pin 2). Its output goes <b>HIGH when V<sub>2</sub> &lt; ⅓V<sub>CC</sub></b>. It drives the <b>S (set)</b> input of the flip-flop.</p>
<h4>4. SR flip-flop (control flip-flop)</h4>
<p>Stores the state. S = 1 → Q = 1, Q̄ = 0; R = 1 → Q = 0, Q̄ = 1. The <b>Q̄</b> output controls both the output stage and the discharge transistor.</p>
<h4>5. Output stage (power amplifier / inverting buffer)</h4>
<p>An inverting <b>totem-pole</b> amplifier driven by Q̄. So the <b>output (pin 3) = Q</b>. It gives the high current capability (200 mA) and isolates the flip-flop from the load.</p>
<h4>6. Discharge transistor (Q<sub>d</sub>)</h4>
<p>An NPN transistor with its base driven by Q̄, emitter grounded, and collector at pin 7. When Q̄ = 1 (output LOW) it is <b>ON</b> and discharges the external capacitor; when Q̄ = 0 (output HIGH) it is <b>OFF</b>.</p>
<h4>7. Reset</h4>
<p>Pin 4 directly resets the flip-flop when taken LOW (active-LOW), overriding all other inputs.</p>""",
          """<p>IC 555 ના અંદરના circuit માં લગભગ 25 transistors, 2 diodes અને 15 resistors હોય છે. કાર્યની દૃષ્ટિએ તેને નીચેના blocks વડે દર્શાવી શકાય (આકૃતિ જુઓ):</p>
<h4>1. Voltage divider</h4>
<p>V<sub>CC</sub> (pin 8) અને ground (pin 1) વચ્ચે series માં જોડાયેલા ત્રણ સમાન <b>5 kΩ resistors</b>. તેઓ બે <b>reference voltages</b> બનાવે છે:</p>
<ul>
<li>ઉપરના બે resistors ના જોડાણ પર <b>⅔V<sub>CC</sub></b> (pin 5 પર પણ બહાર લાવેલ) → ઉપરના comparator માટે reference.</li>
<li>નીચેના બે resistors ના જોડાણ પર <b>⅓V<sub>CC</sub></b> → નીચેના comparator માટે reference.</li>
</ul>
<h4>2. ઉપરનો comparator (Comparator 1 – threshold comparator)</h4>
<p>(+) input = threshold (pin 6), (−) input = ⅔V<sub>CC</sub>. <b>V<sub>6</sub> &gt; ⅔V<sub>CC</sub> થાય ત્યારે</b> તેનો output <b>HIGH</b> થાય. તે flip-flop ના <b>R (reset)</b> input ને ચલાવે છે.</p>
<h4>3. નીચેનો comparator (Comparator 2 – trigger comparator)</h4>
<p>(+) input = ⅓V<sub>CC</sub>, (−) input = trigger (pin 2). <b>V<sub>2</sub> &lt; ⅓V<sub>CC</sub> થાય ત્યારે</b> તેનો output <b>HIGH</b> થાય. તે flip-flop ના <b>S (set)</b> input ને ચલાવે છે.</p>
<h4>4. SR flip-flop (control flip-flop)</h4>
<p>State ને સંગ્રહે છે. S = 1 → Q = 1, Q̄ = 0; R = 1 → Q = 0, Q̄ = 1. <b>Q̄</b> output, output stage અને discharge transistor બંનેને control કરે છે.</p>
<h4>5. Output stage (power amplifier / inverting buffer)</h4>
<p>Q̄ થી ચાલતો inverting <b>totem-pole</b> amplifier. તેથી <b>output (pin 3) = Q</b>. તે વધુ current ક્ષમતા (200 mA) આપે છે અને flip-flop ને load થી અલગ રાખે છે.</p>
<h4>6. Discharge transistor (Q<sub>d</sub>)</h4>
<p>NPN transistor જેનો base Q̄ થી ચાલે, emitter ground પર અને collector pin 7 પર છે. Q̄ = 1 (output LOW) હોય ત્યારે તે <b>ON</b> થઈ બહારના capacitor ને discharge કરે; Q̄ = 0 (output HIGH) હોય ત્યારે <b>OFF</b> રહે.</p>
<h4>7. Reset</h4>
<p>Pin 4 ને LOW કરતાં (active-LOW) તે બીજા બધા inputs ને અવગણી flip-flop ને સીધો reset કરે છે.</p>""",
          diagram="u5_block_diagram"),

        T("5.3.2 Working of IC 555 (Function Table)", "5.3.2 IC 555 નું કાર્ય (Function Table)",
          """<p>The working depends on the voltages at the <b>trigger (pin 2)</b> and <b>threshold (pin 6)</b> compared with ⅓V<sub>CC</sub> and ⅔V<sub>CC</sub>:</p>
<ol>
<li><b>Trigger &lt; ⅓V<sub>CC</sub>:</b> lower comparator output = 1 → S = 1 → flip-flop <b>set</b>, Q = 1, Q̄ = 0 → <b>output HIGH</b>, discharge transistor <b>OFF</b> → external capacitor can charge.</li>
<li><b>Threshold &gt; ⅔V<sub>CC</sub>:</b> upper comparator output = 1 → R = 1 → flip-flop <b>reset</b>, Q = 0, Q̄ = 1 → <b>output LOW</b>, discharge transistor <b>ON</b> → capacitor discharges through pin 7.</li>
<li><b>Trigger &gt; ⅓V<sub>CC</sub> and threshold &lt; ⅔V<sub>CC</sub>:</b> both comparator outputs = 0 → S = R = 0 → flip-flop keeps its <b>previous state</b> (no change).</li>
<li><b>Reset (pin 4) LOW:</b> output LOW, discharge ON, regardless of other inputs.</li>
</ol>
<h4>Function table</h4>
<table>
<tr><th>Reset (4)</th><th>Trigger (2)</th><th>Threshold (6)</th><th>Output (3)</th><th>Discharge (7)</th></tr>
<tr><td>LOW</td><td>X</td><td>X</td><td>LOW</td><td>ON (grounded)</td></tr>
<tr><td>HIGH</td><td>&lt; ⅓V<sub>CC</sub></td><td>X</td><td>HIGH</td><td>OFF (open)</td></tr>
<tr><td>HIGH</td><td>&gt; ⅓V<sub>CC</sub></td><td>&gt; ⅔V<sub>CC</sub></td><td>LOW</td><td>ON (grounded)</td></tr>
<tr><td>HIGH</td><td>&gt; ⅓V<sub>CC</sub></td><td>&lt; ⅔V<sub>CC</sub></td><td>No change</td><td>No change</td></tr>
</table>
<p>(X = don't care.) In short: <b>the trigger turns the output ON, the threshold turns it OFF</b>. The external R and C decide how long it takes the capacitor voltage to move between ⅓V<sub>CC</sub> and ⅔V<sub>CC</sub>; this sets the timing.</p>
<h4>Effect of control voltage</h4>
<p>If a voltage V<sub>CON</sub> is applied at pin 5, the upper threshold becomes V<sub>CON</sub> and the lower threshold becomes V<sub>CON</sub>/2.</p>""",
          """<p>કાર્ય <b>trigger (pin 2)</b> અને <b>threshold (pin 6)</b> ના voltages ની ⅓V<sub>CC</sub> અને ⅔V<sub>CC</sub> સાથેની સરખામણી પર આધાર રાખે છે:</p>
<ol>
<li><b>Trigger &lt; ⅓V<sub>CC</sub>:</b> નીચેના comparator નો output = 1 → S = 1 → flip-flop <b>set</b>, Q = 1, Q̄ = 0 → <b>output HIGH</b>, discharge transistor <b>OFF</b> → બહારનો capacitor charge થઈ શકે.</li>
<li><b>Threshold &gt; ⅔V<sub>CC</sub>:</b> ઉપરના comparator નો output = 1 → R = 1 → flip-flop <b>reset</b>, Q = 0, Q̄ = 1 → <b>output LOW</b>, discharge transistor <b>ON</b> → capacitor pin 7 દ્વારા discharge થાય.</li>
<li><b>Trigger &gt; ⅓V<sub>CC</sub> અને threshold &lt; ⅔V<sub>CC</sub>:</b> બંને comparator outputs = 0 → S = R = 0 → flip-flop <b>અગાઉની state</b> જાળવી રાખે (કોઈ ફેરફાર નહીં).</li>
<li><b>Reset (pin 4) LOW:</b> બીજા inputs ગમે તે હોય, output LOW અને discharge ON.</li>
</ol>
<h4>Function table</h4>
<table>
<tr><th>Reset (4)</th><th>Trigger (2)</th><th>Threshold (6)</th><th>Output (3)</th><th>Discharge (7)</th></tr>
<tr><td>LOW</td><td>X</td><td>X</td><td>LOW</td><td>ON (grounded)</td></tr>
<tr><td>HIGH</td><td>&lt; ⅓V<sub>CC</sub></td><td>X</td><td>HIGH</td><td>OFF (open)</td></tr>
<tr><td>HIGH</td><td>&gt; ⅓V<sub>CC</sub></td><td>&gt; ⅔V<sub>CC</sub></td><td>LOW</td><td>ON (grounded)</td></tr>
<tr><td>HIGH</td><td>&gt; ⅓V<sub>CC</sub></td><td>&lt; ⅔V<sub>CC</sub></td><td>ફેરફાર નહીં</td><td>ફેરફાર નહીં</td></tr>
</table>
<p>(X = don't care.) ટૂંકમાં: <b>trigger output ને ON કરે, threshold તેને OFF કરે</b>. બહારના R અને C નક્કી કરે છે કે capacitor voltage ને ⅓V<sub>CC</sub> અને ⅔V<sub>CC</sub> વચ્ચે જતાં કેટલો સમય લાગે; આનાથી timing નક્કી થાય છે.</p>
<h4>Control voltage ની અસર</h4>
<p>Pin 5 પર V<sub>CON</sub> voltage આપીએ તો upper threshold V<sub>CON</sub> અને lower threshold V<sub>CON</sub>/2 બને છે.</p>""",
          examples=["u5n7"]),

        T("Key Points – 5.3", "મુખ્ય મુદ્દા – 5.3",
          """<ul>
<li>Blocks: <b>3 × 5 kΩ divider, 2 comparators, SR flip-flop, output stage, discharge transistor, reset</b>.</li>
<li>Divider gives references <b>⅔V<sub>CC</sub></b> (upper comparator) and <b>⅓V<sub>CC</sub></b> (lower comparator).</li>
<li>Upper comparator → R input (threshold &gt; ⅔V<sub>CC</sub> → output LOW).</li>
<li>Lower comparator → S input (trigger &lt; ⅓V<sub>CC</sub> → output HIGH).</li>
<li>Output LOW ⇔ discharge transistor ON; output HIGH ⇔ discharge transistor OFF.</li>
<li>With pin 5 voltage V<sub>CON</sub>: thresholds = V<sub>CON</sub> and V<sub>CON</sub>/2.</li>
</ul>""",
          """<ul>
<li>Blocks: <b>3 × 5 kΩ divider, 2 comparators, SR flip-flop, output stage, discharge transistor, reset</b>.</li>
<li>Divider references આપે: <b>⅔V<sub>CC</sub></b> (ઉપરનો comparator) અને <b>⅓V<sub>CC</sub></b> (નીચેનો comparator).</li>
<li>ઉપરનો comparator → R input (threshold &gt; ⅔V<sub>CC</sub> → output LOW).</li>
<li>નીચેનો comparator → S input (trigger &lt; ⅓V<sub>CC</sub> → output HIGH).</li>
<li>Output LOW ⇔ discharge transistor ON; output HIGH ⇔ discharge transistor OFF.</li>
<li>Pin 5 પર V<sub>CON</sub> હોય તો: thresholds = V<sub>CON</sub> અને V<sub>CON</sub>/2.</li>
</ul>""", key=True),
    ],
}

NOTES_A = [SEC_5_1, SEC_5_2, SEC_5_3]
