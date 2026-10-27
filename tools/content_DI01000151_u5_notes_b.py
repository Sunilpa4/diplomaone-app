"""Basics of Electronics (DI01000151) - Unit 5: IC 555 Timer (part B: 5.4 Applications)"""
from content_DI01000151_u3_notes_a import T

# =====================================================================================
SEC_5_4 = {
    "title": {"en": "5.4 Applications of IC 555", "gu": "5.4 IC 555 ના ઉપયોગો"},
    "items": [
        T("5.4.1 555 as Monostable Multivibrator – Circuit and Working", "5.4.1 Monostable Multivibrator તરીકે 555 – Circuit અને કાર્ય",
          """<p>A <b>monostable multivibrator</b> (one-shot) has <b>one stable state</b> (output LOW) and one <b>quasi-stable</b> (temporary) state (output HIGH). When triggered, the output goes HIGH for a fixed time <b>T = 1.1RC</b> and then returns to LOW by itself.</p>
<h4>Circuit (see diagram)</h4>
<ul>
<li>Pin 8 and pin 4 → +V<sub>CC</sub>; pin 1 → ground; pin 5 → 0.01 µF to ground.</li>
<li>Timing resistor <b>R</b> from V<sub>CC</sub> to pins 6 and 7 (joined together); timing capacitor <b>C</b> from pins 6/7 to ground.</li>
<li>Trigger input at pin 2, held HIGH by a <b>10 kΩ pull-up</b>; a push switch (or negative pulse) pulls it LOW.</li>
<li>Output at pin 3 (e.g. LED with series resistor).</li>
</ul>
<h4>Working</h4>
<ol>
<li><b>Stable state:</b> Trigger is HIGH (&gt; ⅓V<sub>CC</sub>). Flip-flop is reset, Q̄ = 1 → <b>output LOW</b>, discharge transistor <b>ON</b> → capacitor C is shorted, V<sub>C</sub> ≈ 0. The circuit stays like this indefinitely.</li>
<li><b>Triggering:</b> A <b>negative-going pulse</b> at pin 2 takes it below <b>⅓V<sub>CC</sub></b>. The lower comparator <b>sets</b> the flip-flop → Q̄ = 0 → <b>output HIGH</b>, discharge transistor <b>OFF</b>.</li>
<li><b>Timing (quasi-stable state):</b> C now <b>charges through R</b> towards V<sub>CC</sub> (exponentially, time constant RC).</li>
<li><b>End of pulse:</b> When V<sub>C</sub> reaches <b>⅔V<sub>CC</sub></b>, the upper comparator <b>resets</b> the flip-flop → <b>output LOW</b>, discharge transistor <b>ON</b> → C discharges quickly to 0 V.</li>
<li>The circuit is back in its stable state and waits for the next trigger.</li>
</ol>
<p><b>Pulse width:</b> <b>T = 1.1 RC</b> (seconds, with R in Ω and C in F).</p>
<h4>Important points</h4>
<ul>
<li>The trigger pulse must be <b>shorter than T</b>; otherwise the output stays HIGH as long as the trigger is LOW.</li>
<li>Further triggers during the timing period have no effect (<b>non-retriggerable</b>).</li>
<li>Applying LOW to reset (pin 4) during timing ends the pulse immediately.</li>
<li>Applications: time delay, timer, pulse stretching, switch debouncing, missing-pulse detector, frequency divider, gate pulse for frequency counter.</li>
</ul>""",
          """<p><b>Monostable multivibrator</b> (one-shot) માં <b>એક stable state</b> (output LOW) અને એક <b>quasi-stable</b> (કામચલાઉ) state (output HIGH) હોય છે. Trigger મળતાં output નિશ્ચિત સમય <b>T = 1.1RC</b> માટે HIGH થાય અને પછી આપોઆપ LOW થઈ જાય.</p>
<h4>Circuit (આકૃતિ જુઓ)</h4>
<ul>
<li>Pin 8 અને pin 4 → +V<sub>CC</sub>; pin 1 → ground; pin 5 → 0.01 µF દ્વારા ground.</li>
<li>Timing resistor <b>R</b> V<sub>CC</sub> થી pins 6 અને 7 (એકસાથે જોડેલા) સુધી; timing capacitor <b>C</b> pins 6/7 થી ground સુધી.</li>
<li>Pin 2 પર trigger input, <b>10 kΩ pull-up</b> વડે HIGH રાખેલ; push switch (અથવા negative pulse) તેને LOW કરે.</li>
<li>Pin 3 પર output (દા.ત. series resistor સાથે LED).</li>
</ul>
<h4>કાર્ય</h4>
<ol>
<li><b>Stable state:</b> Trigger HIGH (&gt; ⅓V<sub>CC</sub>) છે. Flip-flop reset, Q̄ = 1 → <b>output LOW</b>, discharge transistor <b>ON</b> → capacitor C short, V<sub>C</sub> ≈ 0. Circuit અનિશ્ચિત સમય સુધી આમ જ રહે.</li>
<li><b>Triggering:</b> Pin 2 પર <b>negative-going pulse</b> તેને <b>⅓V<sub>CC</sub></b> થી નીચે લઈ જાય. નીચેનો comparator flip-flop ને <b>set</b> કરે → Q̄ = 0 → <b>output HIGH</b>, discharge transistor <b>OFF</b>.</li>
<li><b>Timing (quasi-stable state):</b> હવે C, <b>R દ્વારા charge</b> થઈ V<sub>CC</sub> તરફ જાય (exponential, time constant RC).</li>
<li><b>Pulse નો અંત:</b> V<sub>C</sub> <b>⅔V<sub>CC</sub></b> પર પહોંચે ત્યારે ઉપરનો comparator flip-flop ને <b>reset</b> કરે → <b>output LOW</b>, discharge transistor <b>ON</b> → C ઝડપથી 0 V સુધી discharge થાય.</li>
<li>Circuit ફરી stable state માં આવે અને આગલા trigger ની રાહ જુએ.</li>
</ol>
<p><b>Pulse width:</b> <b>T = 1.1 RC</b> (seconds, R Ω માં અને C F માં).</p>
<h4>મહત્વના મુદ્દા</h4>
<ul>
<li>Trigger pulse <b>T કરતાં ટૂંકો</b> હોવો જોઈએ; નહીં તો trigger LOW રહે ત્યાં સુધી output HIGH રહે.</li>
<li>Timing દરમિયાન આવતા બીજા triggers ની કોઈ અસર નથી (<b>non-retriggerable</b>).</li>
<li>Timing દરમિયાન reset (pin 4) ને LOW કરતાં pulse તરત પૂરો થાય.</li>
<li>ઉપયોગો: time delay, timer, pulse stretching, switch debouncing, missing-pulse detector, frequency divider, frequency counter માટે gate pulse.</li>
</ul>""",
          diagram="u5_mono_circuit", examples=["u5n1", "u5n2"]),

        T("5.4.2 Monostable – Waveforms and Pulse Width (T = 1.1RC)", "5.4.2 Monostable – Waveforms અને Pulse Width (T = 1.1RC)",
          """<h4>Waveforms (see diagram)</h4>
<ul>
<li><b>Trigger (pin 2):</b> normally HIGH; a short negative pulse below ⅓V<sub>CC</sub> starts the cycle.</li>
<li><b>Output (pin 3):</b> goes HIGH at the trigger instant and stays HIGH for time T, then LOW.</li>
<li><b>Capacitor voltage V<sub>C</sub> (pins 6, 7):</b> rises exponentially from 0 to ⅔V<sub>CC</sub> during T, then falls suddenly to 0 when discharged.</li>
</ul>
<h4>Derivation of T = 1.1RC</h4>
<p>During the timing period C charges from 0 V towards V<sub>CC</sub> through R:</p>
<p style="text-align:center"><b>V<sub>C</sub> = V<sub>CC</sub> (1 − e<sup>−t/RC</sup>)</b></p>
<p>The pulse ends when V<sub>C</sub> = ⅔V<sub>CC</sub> at t = T:</p>
<p>⅔V<sub>CC</sub> = V<sub>CC</sub> (1 − e<sup>−T/RC</sup>) → e<sup>−T/RC</sup> = ⅓ → T/RC = ln 3 = 1.0986</p>
<p style="text-align:center"><b>T = 1.0986 RC ≈ 1.1 RC</b></p>
<p><b>Note:</b> V<sub>CC</sub> cancels out, so the pulse width does <b>not depend on the supply voltage</b>. It depends only on R and C.</p>
<h4>Choice of components</h4>
<ul>
<li>R: about 1 kΩ to 1 MΩ (higher values make leakage currents important).</li>
<li>C: about 470 pF to a few hundred µF; use low-leakage capacitors for long delays.</li>
<li>To vary T, use a potentiometer (with a series fixed resistor) in place of R.</li>
</ul>""",
          """<h4>Waveforms (આકૃતિ જુઓ)</h4>
<ul>
<li><b>Trigger (pin 2):</b> સામાન્ય રીતે HIGH; ⅓V<sub>CC</sub> થી નીચેનો ટૂંકો negative pulse cycle શરૂ કરે.</li>
<li><b>Output (pin 3):</b> trigger ની ક્ષણે HIGH થાય, T સમય સુધી HIGH રહે, પછી LOW.</li>
<li><b>Capacitor voltage V<sub>C</sub> (pins 6, 7):</b> T દરમિયાન 0 થી ⅔V<sub>CC</sub> સુધી exponential રીતે વધે, પછી discharge થતાં અચાનક 0 થાય.</li>
</ul>
<h4>T = 1.1RC ની સાબિતી (Derivation)</h4>
<p>Timing સમય દરમિયાન C, R દ્વારા 0 V થી V<sub>CC</sub> તરફ charge થાય છે:</p>
<p style="text-align:center"><b>V<sub>C</sub> = V<sub>CC</sub> (1 − e<sup>−t/RC</sup>)</b></p>
<p>t = T પર V<sub>C</sub> = ⅔V<sub>CC</sub> થાય ત્યારે pulse પૂરો થાય:</p>
<p>⅔V<sub>CC</sub> = V<sub>CC</sub> (1 − e<sup>−T/RC</sup>) → e<sup>−T/RC</sup> = ⅓ → T/RC = ln 3 = 1.0986</p>
<p style="text-align:center"><b>T = 1.0986 RC ≈ 1.1 RC</b></p>
<p><b>નોંધ:</b> V<sub>CC</sub> cancel થઈ જાય છે, તેથી pulse width <b>supply voltage પર આધાર રાખતી નથી</b>. તે ફક્ત R અને C પર આધાર રાખે છે.</p>
<h4>Components ની પસંદગી</h4>
<ul>
<li>R: લગભગ 1 kΩ થી 1 MΩ (વધુ મૂલ્યે leakage currents મહત્વના બને).</li>
<li>C: લગભગ 470 pF થી થોડા સો µF; લાંબા delay માટે low-leakage capacitors વાપરો.</li>
<li>T બદલવા R ની જગ્યાએ potentiometer (series fixed resistor સાથે) વાપરો.</li>
</ul>""",
          diagram="u5_mono_wave"),

        T("5.4.3 555 as Astable Multivibrator (Oscillator) – Circuit and Working", "5.4.3 Astable Multivibrator (Oscillator) તરીકે 555 – Circuit અને કાર્ય",
          """<p>An <b>astable multivibrator</b> has <b>no stable state</b>. Its output switches continuously between HIGH and LOW <b>without any external trigger</b>, producing a <b>rectangular (square) wave</b>. So it works as a <b>free-running oscillator</b> or clock generator.</p>
<h4>Circuit (see diagram)</h4>
<ul>
<li>Pin 8 and pin 4 → +V<sub>CC</sub>; pin 1 → ground; pin 5 → 0.01 µF to ground.</li>
<li><b>R<sub>A</sub></b> between V<sub>CC</sub> and pin 7; <b>R<sub>B</sub></b> between pin 7 and pins 6 + 2.</li>
<li>Timing capacitor <b>C</b> from pins 6 and 2 (joined together) to ground.</li>
<li>Output at pin 3.</li>
</ul>
<h4>Working</h4>
<ol>
<li><b>At switch-on:</b> V<sub>C</sub> = 0 &lt; ⅓V<sub>CC</sub> → trigger comparator sets the flip-flop → <b>output HIGH</b>, discharge transistor OFF.</li>
<li><b>Charging (t<sub>H</sub>):</b> C charges through <b>R<sub>A</sub> + R<sub>B</sub></b> towards V<sub>CC</sub>. Output stays HIGH.</li>
<li>When V<sub>C</sub> reaches <b>⅔V<sub>CC</sub></b>, the threshold comparator resets the flip-flop → <b>output LOW</b>, discharge transistor ON (pin 7 grounded).</li>
<li><b>Discharging (t<sub>L</sub>):</b> C discharges through <b>R<sub>B</sub> only</b> into pin 7. Output stays LOW.</li>
<li>When V<sub>C</sub> falls to <b>⅓V<sub>CC</sub></b>, the trigger comparator sets the flip-flop again → output HIGH, discharge OFF, and C starts charging again.</li>
<li>The cycle repeats: V<sub>C</sub> swings between <b>⅓V<sub>CC</sub> and ⅔V<sub>CC</sub></b> and the output is a continuous rectangular wave.</li>
</ol>
<p><i>Note:</i> the first HIGH period after switch-on is longer (C charges from 0 instead of ⅓V<sub>CC</sub>), about 1.1(R<sub>A</sub> + R<sub>B</sub>)C.</p>
<h4>Applications</h4>
<p>Square-wave / clock generator, LED flasher, tone and siren generators, metronome, traffic-light sequencer clock, PWM, voltage-controlled oscillator (using pin 5).</p>""",
          """<p><b>Astable multivibrator</b> માં <b>કોઈ stable state નથી</b>. તેનો output <b>બહારના trigger વગર</b> સતત HIGH અને LOW વચ્ચે બદલાતો રહે છે અને <b>rectangular (square) wave</b> બનાવે છે. તેથી તે <b>free-running oscillator</b> અથવા clock generator તરીકે કામ કરે છે.</p>
<h4>Circuit (આકૃતિ જુઓ)</h4>
<ul>
<li>Pin 8 અને pin 4 → +V<sub>CC</sub>; pin 1 → ground; pin 5 → 0.01 µF દ્વારા ground.</li>
<li><b>R<sub>A</sub></b> V<sub>CC</sub> અને pin 7 વચ્ચે; <b>R<sub>B</sub></b> pin 7 અને pins 6 + 2 વચ્ચે.</li>
<li>Timing capacitor <b>C</b> pins 6 અને 2 (એકસાથે જોડેલા) થી ground સુધી.</li>
<li>Pin 3 પર output.</li>
</ul>
<h4>કાર્ય</h4>
<ol>
<li><b>Switch-on વખતે:</b> V<sub>C</sub> = 0 &lt; ⅓V<sub>CC</sub> → trigger comparator flip-flop ને set કરે → <b>output HIGH</b>, discharge transistor OFF.</li>
<li><b>Charging (t<sub>H</sub>):</b> C, <b>R<sub>A</sub> + R<sub>B</sub></b> દ્વારા V<sub>CC</sub> તરફ charge થાય. Output HIGH રહે.</li>
<li>V<sub>C</sub> <b>⅔V<sub>CC</sub></b> પર પહોંચે ત્યારે threshold comparator flip-flop ને reset કરે → <b>output LOW</b>, discharge transistor ON (pin 7 grounded).</li>
<li><b>Discharging (t<sub>L</sub>):</b> C <b>ફક્ત R<sub>B</sub></b> દ્વારા pin 7 માં discharge થાય. Output LOW રહે.</li>
<li>V<sub>C</sub> ઘટીને <b>⅓V<sub>CC</sub></b> થાય ત્યારે trigger comparator ફરી flip-flop ને set કરે → output HIGH, discharge OFF, અને C ફરી charge થવા લાગે.</li>
<li>Cycle પુનરાવર્તિત થાય: V<sub>C</sub> <b>⅓V<sub>CC</sub> અને ⅔V<sub>CC</sub></b> વચ્ચે ઝૂલે અને output સતત rectangular wave બને.</li>
</ol>
<p><i>નોંધ:</i> Switch-on પછીનો પહેલો HIGH સમય લાંબો હોય છે (C, ⅓V<sub>CC</sub> ની જગ્યાએ 0 થી charge થાય), લગભગ 1.1(R<sub>A</sub> + R<sub>B</sub>)C.</p>
<h4>ઉપયોગો</h4>
<p>Square-wave / clock generator, LED flasher, tone અને siren generators, metronome, traffic-light sequencer clock, PWM, voltage-controlled oscillator (pin 5 વાપરીને).</p>""",
          diagram="u5_astable_circuit", examples=["u5n3"]),

        T("5.4.4 Astable – Waveforms, Frequency and Duty Cycle", "5.4.4 Astable – Waveforms, Frequency અને Duty Cycle",
          """<h4>Waveforms (see diagram)</h4>
<ul>
<li><b>V<sub>C</sub>:</b> after the first cycle, rises (charging) and falls (discharging) exponentially between ⅓V<sub>CC</sub> and ⅔V<sub>CC</sub>.</li>
<li><b>Output:</b> HIGH while C charges (t<sub>H</sub>), LOW while C discharges (t<sub>L</sub>).</li>
</ul>
<h4>Derivation of timing</h4>
<p><b>Charging</b> from ⅓V<sub>CC</sub> to ⅔V<sub>CC</sub> through (R<sub>A</sub> + R<sub>B</sub>):</p>
<p>V<sub>C</sub> = V<sub>CC</sub> − (V<sub>CC</sub> − ⅓V<sub>CC</sub>) e<sup>−t/τ</sup>; putting V<sub>C</sub> = ⅔V<sub>CC</sub> → ⅓ = ⅔ e<sup>−t/τ</sup> → t = τ ln 2 = 0.693τ</p>
<p style="text-align:center"><b>t<sub>H</sub> = 0.693 (R<sub>A</sub> + R<sub>B</sub>) C</b></p>
<p><b>Discharging</b> from ⅔V<sub>CC</sub> to ⅓V<sub>CC</sub> through R<sub>B</sub>: V<sub>C</sub> = ⅔V<sub>CC</sub> e<sup>−t/R<sub>B</sub>C</sup> = ⅓V<sub>CC</sub> → t = 0.693 R<sub>B</sub>C</p>
<p style="text-align:center"><b>t<sub>L</sub> = 0.693 R<sub>B</sub> C</b></p>
<h4>Total time period and frequency</h4>
<p style="text-align:center"><b>T = t<sub>H</sub> + t<sub>L</sub> = 0.693 (R<sub>A</sub> + 2R<sub>B</sub>) C</b></p>
<p style="text-align:center"><b>f = 1/T = 1.44 / [(R<sub>A</sub> + 2R<sub>B</sub>) C]</b></p>
<h4>Duty cycle</h4>
<p>Duty cycle = ratio of HIGH time to total time:</p>
<p style="text-align:center"><b>D = t<sub>H</sub> / T × 100 % = (R<sub>A</sub> + R<sub>B</sub>) / (R<sub>A</sub> + 2R<sub>B</sub>) × 100 %</b></p>
<ul>
<li>Since t<sub>H</sub> &gt; t<sub>L</sub> always, the duty cycle of the basic circuit is <b>always more than 50 %</b>.</li>
<li>If R<sub>B</sub> ≫ R<sub>A</sub>, D approaches 50 % (nearly square wave).</li>
<li><b>Exactly 50 % (or less):</b> connect a <b>diode across R<sub>B</sub></b> (anode at pin 7). C then charges through R<sub>A</sub> and the diode, and discharges through R<sub>B</sub>, so t<sub>H</sub> = 0.693R<sub>A</sub>C and t<sub>L</sub> = 0.693R<sub>B</sub>C. With R<sub>A</sub> = R<sub>B</sub>, D = 50 %.</li>
<li>R<sub>A</sub> must not be zero, otherwise pin 7 would short V<sub>CC</sub> when the discharge transistor turns ON (minimum about 1 kΩ).</li>
</ul>""",
          """<h4>Waveforms (આકૃતિ જુઓ)</h4>
<ul>
<li><b>V<sub>C</sub>:</b> પહેલા cycle પછી ⅓V<sub>CC</sub> અને ⅔V<sub>CC</sub> વચ્ચે exponential રીતે વધે (charging) અને ઘટે (discharging).</li>
<li><b>Output:</b> C charge થાય ત્યારે HIGH (t<sub>H</sub>), C discharge થાય ત્યારે LOW (t<sub>L</sub>).</li>
</ul>
<h4>Timing ની સાબિતી (Derivation)</h4>
<p>(R<sub>A</sub> + R<sub>B</sub>) દ્વારા ⅓V<sub>CC</sub> થી ⅔V<sub>CC</sub> સુધી <b>Charging</b>:</p>
<p>V<sub>C</sub> = V<sub>CC</sub> − (V<sub>CC</sub> − ⅓V<sub>CC</sub>) e<sup>−t/τ</sup>; V<sub>C</sub> = ⅔V<sub>CC</sub> મૂકતાં → ⅓ = ⅔ e<sup>−t/τ</sup> → t = τ ln 2 = 0.693τ</p>
<p style="text-align:center"><b>t<sub>H</sub> = 0.693 (R<sub>A</sub> + R<sub>B</sub>) C</b></p>
<p>R<sub>B</sub> દ્વારા ⅔V<sub>CC</sub> થી ⅓V<sub>CC</sub> સુધી <b>Discharging</b>: V<sub>C</sub> = ⅔V<sub>CC</sub> e<sup>−t/R<sub>B</sub>C</sup> = ⅓V<sub>CC</sub> → t = 0.693 R<sub>B</sub>C</p>
<p style="text-align:center"><b>t<sub>L</sub> = 0.693 R<sub>B</sub> C</b></p>
<h4>કુલ time period અને frequency</h4>
<p style="text-align:center"><b>T = t<sub>H</sub> + t<sub>L</sub> = 0.693 (R<sub>A</sub> + 2R<sub>B</sub>) C</b></p>
<p style="text-align:center"><b>f = 1/T = 1.44 / [(R<sub>A</sub> + 2R<sub>B</sub>) C]</b></p>
<h4>Duty cycle</h4>
<p>Duty cycle = HIGH સમય અને કુલ સમયનો ગુણોત્તર:</p>
<p style="text-align:center"><b>D = t<sub>H</sub> / T × 100 % = (R<sub>A</sub> + R<sub>B</sub>) / (R<sub>A</sub> + 2R<sub>B</sub>) × 100 %</b></p>
<ul>
<li>t<sub>H</sub> &gt; t<sub>L</sub> હંમેશા હોવાથી basic circuit નો duty cycle <b>હંમેશા 50 % થી વધુ</b> હોય છે.</li>
<li>R<sub>B</sub> ≫ R<sub>A</sub> હોય તો D લગભગ 50 % (લગભગ square wave).</li>
<li><b>બરાબર 50 % (અથવા ઓછો):</b> <b>R<sub>B</sub> ની સમાંતર diode</b> (anode pin 7 તરફ) જોડો. પછી C, R<sub>A</sub> અને diode દ્વારા charge થાય અને R<sub>B</sub> દ્વારા discharge થાય, તેથી t<sub>H</sub> = 0.693R<sub>A</sub>C અને t<sub>L</sub> = 0.693R<sub>B</sub>C. R<sub>A</sub> = R<sub>B</sub> રાખતાં D = 50 %.</li>
<li>R<sub>A</sub> શૂન્ય ન હોવો જોઈએ, નહીં તો discharge transistor ON થતાં pin 7 V<sub>CC</sub> ને short કરે (ન્યૂનતમ લગભગ 1 kΩ).</li>
</ul>""",
          diagram="u5_astable_wave", examples=["u5n4"]),

        T("5.4.5 555 as Pulse Generator (LED Flasher)", "5.4.5 Pulse Generator (LED Flasher) તરીકે 555",
          """<p>A <b>pulse generator</b> produces a continuous train of rectangular pulses of required frequency and width. The <b>astable 555</b> is the simplest pulse generator. A common laboratory example is the <b>LED flasher</b> (see diagram).</p>
<h4>Circuit</h4>
<ul>
<li>Basic astable circuit with R<sub>A</sub> = 10 kΩ, R<sub>B</sub> = 68 kΩ, C = 10 µF (frequency ≈ 1 Hz).</li>
<li><b>LED2</b> + 470 Ω from pin 3 to <b>ground</b> → current is <b>sourced</b> by the 555.</li>
<li><b>LED1</b> + 470 Ω from <b>+V<sub>CC</sub></b> to pin 3 → current is <b>sunk</b> by the 555.</li>
</ul>
<h4>Working</h4>
<ul>
<li>When <b>output is HIGH</b> (C charging), current flows from pin 3 through LED2 to ground → <b>LED2 ON</b>, LED1 OFF (no voltage across it).</li>
<li>When <b>output is LOW</b> (C discharging), current flows from V<sub>CC</sub> through LED1 into pin 3 → <b>LED1 ON</b>, LED2 OFF.</li>
<li>So the two LEDs flash <b>alternately</b> about once per second. For a single flasher, use only one LED.</li>
<li>Flash rate is changed by changing R<sub>B</sub> or C (a potentiometer can be used in place of R<sub>B</sub>).</li>
</ul>
<h4>Other pulse-generator uses</h4>
<ul>
<li><b>Clock pulses</b> for digital counters and logic circuits (output is TTL compatible at 5 V).</li>
<li><b>Tone / buzzer generator:</b> with small C (e.g. 0.01 µF) the frequency is in the audio range; a speaker gives a tone.</li>
<li><b>PWM generator:</b> varying the voltage at pin 5 changes the pulse width – used in motor speed and LED brightness control.</li>
<li>A <b>monostable</b> 555 is used as a <b>single-pulse generator</b> (one clean pulse of fixed width for each trigger).</li>
</ul>""",
          """<p><b>Pulse generator</b> જરૂરી frequency અને width વાળા rectangular pulses ની સતત હારમાળા બનાવે છે. <b>Astable 555</b> સૌથી સરળ pulse generator છે. Laboratory નું સામાન્ય ઉદાહરણ <b>LED flasher</b> છે (આકૃતિ જુઓ).</p>
<h4>Circuit</h4>
<ul>
<li>R<sub>A</sub> = 10 kΩ, R<sub>B</sub> = 68 kΩ, C = 10 µF સાથેનો basic astable circuit (frequency ≈ 1 Hz).</li>
<li><b>LED2</b> + 470 Ω pin 3 થી <b>ground</b> સુધી → 555 current <b>source</b> કરે.</li>
<li><b>LED1</b> + 470 Ω <b>+V<sub>CC</sub></b> થી pin 3 સુધી → 555 current <b>sink</b> કરે.</li>
</ul>
<h4>કાર્ય</h4>
<ul>
<li><b>Output HIGH</b> (C charging) હોય ત્યારે current pin 3 થી LED2 દ્વારા ground માં વહે → <b>LED2 ON</b>, LED1 OFF (તેના પર voltage નથી).</li>
<li><b>Output LOW</b> (C discharging) હોય ત્યારે current V<sub>CC</sub> થી LED1 દ્વારા pin 3 માં વહે → <b>LED1 ON</b>, LED2 OFF.</li>
<li>આમ બંને LEDs લગભગ દર સેકન્ડે <b>વારાફરતી</b> ઝબકે. એક જ flasher માટે ફક્ત એક LED વાપરો.</li>
<li>R<sub>B</sub> અથવા C બદલીને flash rate બદલાય (R<sub>B</sub> ની જગ્યાએ potentiometer વાપરી શકાય).</li>
</ul>
<h4>Pulse generator ના બીજા ઉપયોગો</h4>
<ul>
<li>Digital counters અને logic circuits માટે <b>clock pulses</b> (5 V પર output TTL compatible).</li>
<li><b>Tone / buzzer generator:</b> નાના C (દા.ત. 0.01 µF) સાથે frequency audio range માં આવે; speaker tone આપે.</li>
<li><b>PWM generator:</b> pin 5 નો voltage બદલતાં pulse width બદલાય – motor speed અને LED brightness control માં વપરાય.</li>
<li><b>Monostable</b> 555 <b>single-pulse generator</b> તરીકે વપરાય (દરેક trigger માટે નિશ્ચિત width નો એક સ્વચ્છ pulse).</li>
</ul>""",
          diagram="u5_led_flasher", examples=["u5n5"]),

        T("5.4.6 555 as Timer (Time-Delay Circuit)", "5.4.6 Timer (Time-Delay Circuit) તરીકે 555",
          """<p>The most direct use of the 555 is as a <b>timer</b>: it keeps a load ON (or OFF) for a fixed, adjustable time after a start signal. The <b>monostable</b> circuit is used for this (see the monostable circuit diagram).</p>
<h4>Circuit idea</h4>
<ul>
<li>Monostable 555 with timing components R and C (T = 1.1RC). R can be a potentiometer + fixed resistor for adjustable time.</li>
<li>A <b>START push button</b> at pin 2 (with 10 kΩ pull-up) triggers the timer.</li>
<li>An optional <b>STOP / RESET push button</b> at pin 4 (with pull-up) ends the timing early.</li>
<li>Pin 3 drives the load directly (LED, buzzer) or through a <b>relay</b> (with a freewheeling diode across the relay coil) for AC loads such as a lamp.</li>
</ul>
<h4>Working</h4>
<ol>
<li>Pressing START pulls pin 2 below ⅓V<sub>CC</sub> → output HIGH → relay energises → load ON.</li>
<li>C charges through R; after <b>T = 1.1RC</b>, V<sub>C</sub> = ⅔V<sub>CC</sub> → output LOW → relay de-energises → load OFF automatically.</li>
<li>Pressing RESET at any time makes the output LOW immediately.</li>
</ol>
<h4>Examples of timer applications</h4>
<ul>
<li>Staircase / corridor light timer (light ON for 1–2 minutes after pressing a button).</li>
<li>Delay timer for washing machines, photographic enlargers, battery chargers, microwave ovens.</li>
<li>Power-on delay (e.g. switch on speakers a few seconds after amplifier power-up).</li>
<li>Quiz buzzer / game timer, egg timer, auto switch-off for gadgets.</li>
<li>Very long delays (minutes to hours) are made by using a 555 astable with a counter IC.</li>
</ul>""",
          """<p>555 નો સૌથી સીધો ઉપયોગ <b>timer</b> તરીકે છે: start signal પછી તે load ને નિશ્ચિત, બદલી શકાય તેવા સમય માટે ON (અથવા OFF) રાખે છે. આ માટે <b>monostable</b> circuit વપરાય છે (monostable circuit આકૃતિ જુઓ).</p>
<h4>Circuit ની રચના</h4>
<ul>
<li>Timing components R અને C (T = 1.1RC) સાથે monostable 555. સમય બદલવા R ની જગ્યાએ potentiometer + fixed resistor રાખી શકાય.</li>
<li>Pin 2 પર <b>START push button</b> (10 kΩ pull-up સાથે) timer ને trigger કરે.</li>
<li>Pin 4 પર વૈકલ્પિક <b>STOP / RESET push button</b> (pull-up સાથે) timing ને વહેલું પૂરું કરે.</li>
<li>Pin 3 load ને સીધો (LED, buzzer) અથવા lamp જેવા AC loads માટે <b>relay</b> (relay coil ની સમાંતર freewheeling diode સાથે) દ્વારા ચલાવે.</li>
</ul>
<h4>કાર્ય</h4>
<ol>
<li>START દબાવતાં pin 2 ⅓V<sub>CC</sub> થી નીચે જાય → output HIGH → relay energise થાય → load ON.</li>
<li>C, R દ્વારા charge થાય; <b>T = 1.1RC</b> પછી V<sub>C</sub> = ⅔V<sub>CC</sub> → output LOW → relay de-energise થાય → load આપોઆપ OFF.</li>
<li>ગમે ત્યારે RESET દબાવતાં output તરત LOW થાય.</li>
</ol>
<h4>Timer ઉપયોગોના ઉદાહરણો</h4>
<ul>
<li>Staircase / corridor light timer (button દબાવ્યા પછી 1–2 મિનિટ light ON).</li>
<li>Washing machines, photographic enlargers, battery chargers, microwave ovens માટે delay timer.</li>
<li>Power-on delay (દા.ત. amplifier ચાલુ થયા પછી થોડી સેકન્ડે speakers ચાલુ કરવા).</li>
<li>Quiz buzzer / game timer, egg timer, gadgets માટે auto switch-off.</li>
<li>ખૂબ લાંબા delay (મિનિટો થી કલાકો) 555 astable અને counter IC વાપરીને બનાવાય.</li>
</ul>"""),

        T("5.4.7 555 in Frequency Counter", "5.4.7 Frequency Counter માં 555",
          """<p>A <b>frequency counter</b> measures the frequency of an unknown signal by <b>counting the number of cycles in a known time interval</b> (called the <b>gate time</b>). The 555 timer is used to produce this accurate <b>gate pulse</b> (see block diagram).</p>
<p style="text-align:center"><b>f<sub>x</sub> = N / T<sub>gate</sub></b> (N = number of pulses counted)</p>
<p>If T<sub>gate</sub> = 1 s, the count N directly equals the frequency in Hz.</p>
<h4>Blocks and working</h4>
<ol>
<li><b>Wave shaper (Schmitt trigger):</b> converts the unknown input signal (sine, triangular etc.) into clean rectangular pulses of the same frequency.</li>
<li><b>555 timer (gate generator):</b> a <b>monostable</b> 555 (or a 555 astable followed by a divider) produces a pulse of exactly known width, e.g. <b>1 s</b> (T = 1.1RC).</li>
<li><b>AND gate (main gate):</b> one input gets the shaped pulses and the other gets the gate pulse. Pulses pass through <b>only while the gate pulse is HIGH</b>.</li>
<li><b>Decade counter:</b> counts the pulses passing through the AND gate. It is reset before each measurement; at the end of the gate time the count is latched.</li>
<li><b>Decoder / driver and 7-segment display:</b> show the count, i.e. the frequency.</li>
</ol>
<h4>Gate time and range</h4>
<ul>
<li>Gate 1 s → reading in Hz; gate 0.1 s → reading × 10; gate 10 ms → reading × 100 (higher frequency, lower resolution).</li>
<li>Accuracy depends on the accuracy of the gate time, so stable, low-tolerance R and C are used (crystal-based time bases are used in precision counters).</li>
</ul>""",
          """<p><b>Frequency counter</b> અજાણ્યા signal ની frequency, <b>જાણીતા સમયગાળા (gate time) માં cycles ની સંખ્યા ગણીને</b> માપે છે. આ ચોક્કસ <b>gate pulse</b> બનાવવા 555 timer વપરાય છે (block diagram જુઓ).</p>
<p style="text-align:center"><b>f<sub>x</sub> = N / T<sub>gate</sub></b> (N = ગણેલા pulses ની સંખ્યા)</p>
<p>T<sub>gate</sub> = 1 s હોય તો count N સીધો Hz માં frequency બરાબર થાય.</p>
<h4>Blocks અને કાર્ય</h4>
<ol>
<li><b>Wave shaper (Schmitt trigger):</b> અજાણ્યા input signal (sine, triangular વગેરે) ને તે જ frequency ના સ્વચ્છ rectangular pulses માં ફેરવે.</li>
<li><b>555 timer (gate generator):</b> <b>monostable</b> 555 (અથવા divider સાથે 555 astable) બરાબર જાણીતી width નો pulse બનાવે, દા.ત. <b>1 s</b> (T = 1.1RC).</li>
<li><b>AND gate (main gate):</b> એક input પર shaped pulses અને બીજા પર gate pulse. <b>Gate pulse HIGH હોય ત્યારે જ</b> pulses પસાર થાય.</li>
<li><b>Decade counter:</b> AND gate માંથી પસાર થતા pulses ગણે. દરેક માપન પહેલાં reset થાય; gate time ના અંતે count latch થાય.</li>
<li><b>Decoder / driver અને 7-segment display:</b> count એટલે કે frequency દર્શાવે.</li>
</ol>
<h4>Gate time અને range</h4>
<ul>
<li>Gate 1 s → reading Hz માં; gate 0.1 s → reading × 10; gate 10 ms → reading × 100 (વધુ frequency, ઓછું resolution).</li>
<li>ચોકસાઈ gate time ની ચોકસાઈ પર આધાર રાખે, તેથી સ્થિર, ઓછા tolerance વાળા R અને C વપરાય (precision counters માં crystal-based time base વપરાય).</li>
</ul>""",
          diagram="u5_freq_counter", examples=["u5n6"]),

        T("5.4.8 Other Applications and Comparison of Modes", "5.4.8 બીજા ઉપયોગો અને Modes ની સરખામણી",
          """<h4>Bistable mode (flip-flop)</h4>
<p>Pins 6 and 7 are not used for timing (pin 6 grounded); pin 2 (with pull-up) acts as <b>SET</b> and pin 4 (with pull-up) acts as <b>RESET</b>. Pressing SET makes output HIGH and it stays HIGH; pressing RESET makes it LOW. Used as a <b>switch debouncer</b> and ON/OFF touch switch.</p>
<h4>Other applications</h4>
<ul>
<li><b>Missing-pulse detector</b> – detects a missing heartbeat / pulse in a pulse train (alarm systems).</li>
<li><b>Frequency divider</b> – monostable with T longer than the input period.</li>
<li><b>PWM and PPM</b> (pulse width / position modulation) – modulating signal at pin 5.</li>
<li><b>Voltage-controlled oscillator (VCO)</b> – frequency controlled by pin 5 voltage.</li>
<li><b>Schmitt trigger</b> – pins 2 and 6 joined as input; converts sine into square wave.</li>
<li><b>Burglar / fire alarm, siren, police-siren (two 555s), water-level indicator, traffic-light controller, touch switch, DC-DC voltage doubler</b>.</li>
</ul>
<h4>Comparison: monostable vs astable vs bistable</h4>
<table>
<tr><th>Point</th><th>Monostable</th><th>Astable</th><th>Bistable</th></tr>
<tr><td>Stable states</td><td>1</td><td>0</td><td>2</td></tr>
<tr><td>Trigger needed</td><td>Yes (one per pulse)</td><td>No</td><td>Yes (set and reset)</td></tr>
<tr><td>Output</td><td>Single pulse</td><td>Continuous rectangular wave</td><td>Stays HIGH or LOW</td></tr>
<tr><td>Timing formula</td><td>T = 1.1RC</td><td>f = 1.44/[(R<sub>A</sub>+2R<sub>B</sub>)C]</td><td>None</td></tr>
<tr><td>Timing components</td><td>R, C</td><td>R<sub>A</sub>, R<sub>B</sub>, C</td><td>None</td></tr>
<tr><td>Pins 2 and 6</td><td>Separate (2 = trigger in; 6, 7 joined)</td><td>Joined (2 and 6)</td><td>2 = SET, 4 = RESET</td></tr>
<tr><td>Other name</td><td>One-shot</td><td>Free-running oscillator</td><td>Flip-flop / latch</td></tr>
<tr><td>Uses</td><td>Timer, delay, gate pulse, debouncing</td><td>Flasher, clock, tone, PWM</td><td>ON/OFF switch, memory</td></tr>
</table>""",
          """<h4>Bistable mode (flip-flop)</h4>
<p>Pins 6 અને 7 timing માટે વપરાતા નથી (pin 6 grounded); pin 2 (pull-up સાથે) <b>SET</b> તરીકે અને pin 4 (pull-up સાથે) <b>RESET</b> તરીકે કામ કરે. SET દબાવતાં output HIGH થાય અને HIGH જ રહે; RESET દબાવતાં LOW થાય. <b>Switch debouncer</b> અને ON/OFF touch switch તરીકે વપરાય.</p>
<h4>બીજા ઉપયોગો</h4>
<ul>
<li><b>Missing-pulse detector</b> – pulse train માં ખૂટતો heartbeat / pulse શોધે (alarm systems).</li>
<li><b>Frequency divider</b> – input period કરતાં લાંબા T વાળો monostable.</li>
<li><b>PWM અને PPM</b> (pulse width / position modulation) – pin 5 પર modulating signal.</li>
<li><b>Voltage-controlled oscillator (VCO)</b> – pin 5 voltage થી frequency control.</li>
<li><b>Schmitt trigger</b> – pins 2 અને 6 જોડી input; sine ને square wave માં ફેરવે.</li>
<li><b>Burglar / fire alarm, siren, police-siren (બે 555), water-level indicator, traffic-light controller, touch switch, DC-DC voltage doubler</b>.</li>
</ul>
<h4>સરખામણી: monostable vs astable vs bistable</h4>
<table>
<tr><th>મુદ્દો</th><th>Monostable</th><th>Astable</th><th>Bistable</th></tr>
<tr><td>Stable states</td><td>1</td><td>0</td><td>2</td></tr>
<tr><td>Trigger જોઈએ?</td><td>હા (દરેક pulse માટે એક)</td><td>ના</td><td>હા (set અને reset)</td></tr>
<tr><td>Output</td><td>એક pulse</td><td>સતત rectangular wave</td><td>HIGH અથવા LOW રહે</td></tr>
<tr><td>Timing formula</td><td>T = 1.1RC</td><td>f = 1.44/[(R<sub>A</sub>+2R<sub>B</sub>)C]</td><td>નથી</td></tr>
<tr><td>Timing components</td><td>R, C</td><td>R<sub>A</sub>, R<sub>B</sub>, C</td><td>નથી</td></tr>
<tr><td>Pins 2 અને 6</td><td>અલગ (2 = trigger in; 6, 7 જોડેલા)</td><td>જોડેલા (2 અને 6)</td><td>2 = SET, 4 = RESET</td></tr>
<tr><td>બીજું નામ</td><td>One-shot</td><td>Free-running oscillator</td><td>Flip-flop / latch</td></tr>
<tr><td>ઉપયોગ</td><td>Timer, delay, gate pulse, debouncing</td><td>Flasher, clock, tone, PWM</td><td>ON/OFF switch, memory</td></tr>
</table>"""),

        T("Key Points – 5.4", "મુખ્ય મુદ્દા – 5.4",
          """<ul>
<li><b>Monostable:</b> one pulse per trigger, <b>T = 1.1RC</b>; C charges 0 → ⅔V<sub>CC</sub>; pins 6 + 7 joined.</li>
<li><b>Astable:</b> continuous wave, no trigger; C swings ⅓ ↔ ⅔V<sub>CC</sub>; pins 2 + 6 joined.</li>
<li>t<sub>H</sub> = 0.693(R<sub>A</sub>+R<sub>B</sub>)C, t<sub>L</sub> = 0.693R<sub>B</sub>C, <b>f = 1.44/[(R<sub>A</sub>+2R<sub>B</sub>)C]</b>.</li>
<li>Duty cycle D = (R<sub>A</sub>+R<sub>B</sub>)/(R<sub>A</sub>+2R<sub>B</sub>) &gt; 50 %; diode across R<sub>B</sub> gives 50 % with R<sub>A</sub> = R<sub>B</sub>.</li>
<li>Pulse generator / LED flasher = astable; output sources (load to ground) or sinks (load to V<sub>CC</sub>).</li>
<li>Timer = monostable with START at pin 2, RESET at pin 4, relay at pin 3.</li>
<li>Frequency counter: 555 gives the <b>gate pulse</b>; <b>f = N / T<sub>gate</sub></b>.</li>
</ul>""",
          """<ul>
<li><b>Monostable:</b> દરેક trigger પર એક pulse, <b>T = 1.1RC</b>; C 0 → ⅔V<sub>CC</sub> charge થાય; pins 6 + 7 જોડેલા.</li>
<li><b>Astable:</b> સતત wave, trigger નહીં; C ⅓ ↔ ⅔V<sub>CC</sub> વચ્ચે ઝૂલે; pins 2 + 6 જોડેલા.</li>
<li>t<sub>H</sub> = 0.693(R<sub>A</sub>+R<sub>B</sub>)C, t<sub>L</sub> = 0.693R<sub>B</sub>C, <b>f = 1.44/[(R<sub>A</sub>+2R<sub>B</sub>)C]</b>.</li>
<li>Duty cycle D = (R<sub>A</sub>+R<sub>B</sub>)/(R<sub>A</sub>+2R<sub>B</sub>) &gt; 50 %; R<sub>B</sub> ની સમાંતર diode અને R<sub>A</sub> = R<sub>B</sub> થી 50 %.</li>
<li>Pulse generator / LED flasher = astable; output source (load ground તરફ) અથવા sink (load V<sub>CC</sub> તરફ) કરે.</li>
<li>Timer = pin 2 પર START, pin 4 પર RESET, pin 3 પર relay સાથેનો monostable.</li>
<li>Frequency counter: 555 <b>gate pulse</b> આપે; <b>f = N / T<sub>gate</sub></b>.</li>
</ul>""", key=True),
    ],
}

NOTES_B = [SEC_5_4]
