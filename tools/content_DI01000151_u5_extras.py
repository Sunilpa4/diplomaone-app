"""Basics of Electronics (DI01000151) - Unit 5 extras: numericals, equations, viva, exam questions"""
from content_DI01000151_u3_extras import N, E, V, X

NUMERICALS = [
    N("u5n1",
      "A 555 monostable multivibrator uses R = 100 kΩ and C = 10 µF. Find the output pulse width.",
      "555 monostable multivibrator માં R = 100 kΩ અને C = 10 µF છે. Output pulse width શોધો.",
      """<p>T = 1.1 RC = 1.1 × 100 × 10³ × 10 × 10⁻⁶</p>
<p>= 1.1 × 1 = <b>1.1 s</b></p>""",
      """<p>T = 1.1 RC = 1.1 × 100 × 10³ × 10 × 10⁻⁶</p>
<p>= 1.1 × 1 = <b>1.1 s</b></p>"""),
    N("u5n2",
      "Design a 555 monostable to give a time delay of 5 s using C = 47 µF.",
      "C = 47 µF વાપરી 5 s નો time delay આપતો 555 monostable ડિઝાઇન કરો.",
      """<p>T = 1.1 RC → R = T / (1.1 C) = 5 / (1.1 × 47 × 10⁻⁶)</p>
<p>= 5 / (51.7 × 10⁻⁶) = <b>96.7 kΩ</b></p>
<p>Use standard <b>100 kΩ</b> (or a 100 kΩ potentiometer for fine adjustment).</p>
<p>Check: T = 1.1 × 100 × 10³ × 47 × 10⁻⁶ = <b>5.17 s</b> ≈ 5 s ✓</p>""",
      """<p>T = 1.1 RC → R = T / (1.1 C) = 5 / (1.1 × 47 × 10⁻⁶)</p>
<p>= 5 / (51.7 × 10⁻⁶) = <b>96.7 kΩ</b></p>
<p>Standard <b>100 kΩ</b> વાપરો (અથવા બારીક ગોઠવણ માટે 100 kΩ potentiometer).</p>
<p>ચકાસણી: T = 1.1 × 100 × 10³ × 47 × 10⁻⁶ = <b>5.17 s</b> ≈ 5 s ✓</p>"""),
    N("u5n3",
      "A 555 astable multivibrator has R_A = 1 kΩ, R_B = 10 kΩ and C = 0.1 µF. Find t_H, t_L, T, frequency and duty cycle.",
      "555 astable multivibrator માં R_A = 1 kΩ, R_B = 10 kΩ અને C = 0.1 µF છે. t_H, t_L, T, frequency અને duty cycle શોધો.",
      """<p>t<sub>H</sub> = 0.693 (R<sub>A</sub> + R<sub>B</sub>) C = 0.693 × 11 × 10³ × 0.1 × 10⁻⁶ = <b>0.762 ms</b></p>
<p>t<sub>L</sub> = 0.693 R<sub>B</sub> C = 0.693 × 10 × 10³ × 0.1 × 10⁻⁶ = <b>0.693 ms</b></p>
<p>T = t<sub>H</sub> + t<sub>L</sub> = <b>1.455 ms</b></p>
<p>f = 1/T = 1 / 1.455 × 10⁻³ = <b>687 Hz</b> (check: 1.44 / (21 × 10³ × 0.1 × 10⁻⁶) = 686 Hz ✓)</p>
<p>D = t<sub>H</sub>/T × 100 = 0.762/1.455 × 100 = <b>52.4 %</b></p>""",
      """<p>t<sub>H</sub> = 0.693 (R<sub>A</sub> + R<sub>B</sub>) C = 0.693 × 11 × 10³ × 0.1 × 10⁻⁶ = <b>0.762 ms</b></p>
<p>t<sub>L</sub> = 0.693 R<sub>B</sub> C = 0.693 × 10 × 10³ × 0.1 × 10⁻⁶ = <b>0.693 ms</b></p>
<p>T = t<sub>H</sub> + t<sub>L</sub> = <b>1.455 ms</b></p>
<p>f = 1/T = 1 / 1.455 × 10⁻³ = <b>687 Hz</b> (ચકાસણી: 1.44 / (21 × 10³ × 0.1 × 10⁻⁶) = 686 Hz ✓)</p>
<p>D = t<sub>H</sub>/T × 100 = 0.762/1.455 × 100 = <b>52.4 %</b></p>"""),
    N("u5n4",
      "Design a 555 astable multivibrator for a frequency of 1 kHz and duty cycle of 60 % using C = 0.01 µF.",
      "C = 0.01 µF વાપરી 1 kHz frequency અને 60 % duty cycle માટે 555 astable multivibrator ડિઝાઇન કરો.",
      """<p>Duty cycle: (R<sub>A</sub> + R<sub>B</sub>)/(R<sub>A</sub> + 2R<sub>B</sub>) = 0.6 → R<sub>A</sub> + R<sub>B</sub> = 0.6R<sub>A</sub> + 1.2R<sub>B</sub> → 0.4R<sub>A</sub> = 0.2R<sub>B</sub> → <b>R<sub>B</sub> = 2R<sub>A</sub></b></p>
<p>Frequency: f = 1.44 / [(R<sub>A</sub> + 2R<sub>B</sub>) C] → R<sub>A</sub> + 2R<sub>B</sub> = 1.44 / (1000 × 0.01 × 10⁻⁶) = 144 kΩ</p>
<p>R<sub>A</sub> + 4R<sub>A</sub> = 144 kΩ → <b>R<sub>A</sub> = 28.8 kΩ</b>, <b>R<sub>B</sub> = 57.6 kΩ</b></p>
<p>Standard values: R<sub>A</sub> = <b>27 kΩ</b>, R<sub>B</sub> = <b>56 kΩ</b></p>
<p>Check: f = 1.44 / (139 × 10³ × 0.01 × 10⁻⁶) = <b>1036 Hz</b>; D = 83/139 = <b>59.7 %</b> ✓</p>""",
      """<p>Duty cycle: (R<sub>A</sub> + R<sub>B</sub>)/(R<sub>A</sub> + 2R<sub>B</sub>) = 0.6 → R<sub>A</sub> + R<sub>B</sub> = 0.6R<sub>A</sub> + 1.2R<sub>B</sub> → 0.4R<sub>A</sub> = 0.2R<sub>B</sub> → <b>R<sub>B</sub> = 2R<sub>A</sub></b></p>
<p>Frequency: f = 1.44 / [(R<sub>A</sub> + 2R<sub>B</sub>) C] → R<sub>A</sub> + 2R<sub>B</sub> = 1.44 / (1000 × 0.01 × 10⁻⁶) = 144 kΩ</p>
<p>R<sub>A</sub> + 4R<sub>A</sub> = 144 kΩ → <b>R<sub>A</sub> = 28.8 kΩ</b>, <b>R<sub>B</sub> = 57.6 kΩ</b></p>
<p>Standard મૂલ્યો: R<sub>A</sub> = <b>27 kΩ</b>, R<sub>B</sub> = <b>56 kΩ</b></p>
<p>ચકાસણી: f = 1.44 / (139 × 10³ × 0.01 × 10⁻⁶) = <b>1036 Hz</b>; D = 83/139 = <b>59.7 %</b> ✓</p>"""),
    N("u5n5",
      "An LED flasher uses a 555 astable with R_A = 10 kΩ, R_B = 68 kΩ and C = 10 µF. Find the ON time, OFF time, flashing frequency and duty cycle.",
      "LED flasher માં R_A = 10 kΩ, R_B = 68 kΩ અને C = 10 µF સાથે 555 astable છે. ON time, OFF time, flashing frequency અને duty cycle શોધો.",
      """<p>t<sub>H</sub> = 0.693 (10 + 68) × 10³ × 10 × 10⁻⁶ = 0.693 × 0.78 = <b>0.541 s</b> (LED2 ON)</p>
<p>t<sub>L</sub> = 0.693 × 68 × 10³ × 10 × 10⁻⁶ = 0.693 × 0.68 = <b>0.471 s</b> (LED1 ON)</p>
<p>T = 0.541 + 0.471 = <b>1.012 s</b> → f = 1/T ≈ <b>0.99 Hz</b> (about 1 flash per second)</p>
<p>D = 0.541/1.012 × 100 = <b>53.4 %</b></p>""",
      """<p>t<sub>H</sub> = 0.693 (10 + 68) × 10³ × 10 × 10⁻⁶ = 0.693 × 0.78 = <b>0.541 s</b> (LED2 ON)</p>
<p>t<sub>L</sub> = 0.693 × 68 × 10³ × 10 × 10⁻⁶ = 0.693 × 0.68 = <b>0.471 s</b> (LED1 ON)</p>
<p>T = 0.541 + 0.471 = <b>1.012 s</b> → f = 1/T ≈ <b>0.99 Hz</b> (લગભગ દર સેકન્ડે એક flash)</p>
<p>D = 0.541/1.012 × 100 = <b>53.4 %</b></p>"""),
    N("u5n6",
      "In a frequency counter, the counter shows 2500 counts during a gate time of 1 s. Find the unknown frequency. Also find R of the 555 monostable gate generator if C = 10 µF.",
      "Frequency counter માં 1 s ના gate time દરમિયાન counter 2500 counts બતાવે છે. અજાણી frequency શોધો. C = 10 µF હોય તો 555 monostable gate generator નો R પણ શોધો.",
      """<p>f<sub>x</sub> = N / T<sub>gate</sub> = 2500 / 1 = <b>2500 Hz = 2.5 kHz</b></p>
<p>Gate pulse: T = 1.1 RC → R = 1 / (1.1 × 10 × 10⁻⁶) = <b>90.9 kΩ</b> → use <b>91 kΩ</b> (T = 1.001 s)</p>
<p><i>If the gate time were 0.1 s, the same signal would give 250 counts.</i></p>""",
      """<p>f<sub>x</sub> = N / T<sub>gate</sub> = 2500 / 1 = <b>2500 Hz = 2.5 kHz</b></p>
<p>Gate pulse: T = 1.1 RC → R = 1 / (1.1 × 10 × 10⁻⁶) = <b>90.9 kΩ</b> → <b>91 kΩ</b> વાપરો (T = 1.001 s)</p>
<p><i>Gate time 0.1 s હોત તો તે જ signal 250 counts આપત.</i></p>"""),
    N("u5n7",
      "A 555 timer is operated at V_CC = 9 V. Find the upper and lower threshold voltages. What are they if 5 V is applied at the control pin (pin 5)?",
      "555 timer V_CC = 9 V પર ચાલે છે. Upper અને lower threshold voltages શોધો. Control pin (pin 5) પર 5 V આપીએ તો તે કેટલા થાય?",
      """<p>Upper threshold = ⅔ V<sub>CC</sub> = ⅔ × 9 = <b>6 V</b></p>
<p>Lower (trigger) threshold = ⅓ V<sub>CC</sub> = ⅓ × 9 = <b>3 V</b></p>
<p>With V<sub>CON</sub> = 5 V at pin 5: upper = V<sub>CON</sub> = <b>5 V</b>, lower = V<sub>CON</sub>/2 = <b>2.5 V</b></p>
<p><i>Lower thresholds make the capacitor reach them sooner → timing becomes shorter.</i></p>""",
      """<p>Upper threshold = ⅔ V<sub>CC</sub> = ⅔ × 9 = <b>6 V</b></p>
<p>Lower (trigger) threshold = ⅓ V<sub>CC</sub> = ⅓ × 9 = <b>3 V</b></p>
<p>Pin 5 પર V<sub>CON</sub> = 5 V હોય તો: upper = V<sub>CON</sub> = <b>5 V</b>, lower = V<sub>CON</sub>/2 = <b>2.5 V</b></p>
<p><i>ઓછા thresholds પર capacitor વહેલો પહોંચે → timing ટૂંકું થાય.</i></p>"""),
]

EQUATIONS = [
    {"title": {"en": "IC 555 Basics", "gu": "IC 555 મૂળભૂત"}, "items": [
        E("Upper threshold", "Upper threshold", "V<sub>UT</sub> = ⅔ V<sub>CC</sub>",
          "Threshold (pin 6) above this → output LOW", "Threshold (pin 6) આનાથી ઉપર → output LOW"),
        E("Lower (trigger) threshold", "Lower (trigger) threshold", "V<sub>LT</sub> = ⅓ V<sub>CC</sub>",
          "Trigger (pin 2) below this → output HIGH", "Trigger (pin 2) આનાથી નીચે → output HIGH"),
        E("With control voltage at pin 5", "Pin 5 પર control voltage સાથે", "V<sub>UT</sub> = V<sub>CON</sub>, V<sub>LT</sub> = V<sub>CON</sub> / 2",
          "Used for PWM / VCO", "PWM / VCO માટે વપરાય"),
        E("Supply range", "Supply range", "V<sub>CC</sub> = 4.5 V – 15 V; I<sub>out(max)</sub> = 200 mA",
          "", ""),
    ]},
    {"title": {"en": "Monostable Multivibrator", "gu": "Monostable Multivibrator"}, "items": [
        E("Capacitor charging", "Capacitor charging", "V<sub>C</sub> = V<sub>CC</sub> (1 − e<sup>−t/RC</sup>)",
          "Starts from 0 V", "0 V થી શરૂ"),
        E("Pulse width", "Pulse width", "T = 1.1 R C",
          "From T = RC ln 3; independent of V_CC", "T = RC ln 3 પરથી; V_CC થી સ્વતંત્ર"),
        E("Design: resistor", "Design: resistor", "R = T / (1.1 C)", "", ""),
    ]},
    {"title": {"en": "Astable Multivibrator", "gu": "Astable Multivibrator"}, "items": [
        E("HIGH time (charging)", "HIGH time (charging)", "t<sub>H</sub> = 0.693 (R<sub>A</sub> + R<sub>B</sub>) C",
          "C charges through R_A + R_B", "C, R_A + R_B દ્વારા charge થાય"),
        E("LOW time (discharging)", "LOW time (discharging)", "t<sub>L</sub> = 0.693 R<sub>B</sub> C",
          "C discharges through R_B into pin 7", "C, R_B દ્વારા pin 7 માં discharge થાય"),
        E("Time period", "Time period", "T = t<sub>H</sub> + t<sub>L</sub> = 0.693 (R<sub>A</sub> + 2R<sub>B</sub>) C", "", ""),
        E("Frequency", "Frequency", "f = 1.44 / [(R<sub>A</sub> + 2R<sub>B</sub>) C]", "", ""),
        E("Duty cycle", "Duty cycle", "D = (R<sub>A</sub> + R<sub>B</sub>) / (R<sub>A</sub> + 2R<sub>B</sub>) × 100 %",
          "Always > 50 % in basic circuit", "Basic circuit માં હંમેશા > 50 %"),
        E("LOW-to-HIGH ratio / space ratio", "LOW-to-HIGH ratio", "t<sub>L</sub> / t<sub>H</sub> = R<sub>B</sub> / (R<sub>A</sub> + R<sub>B</sub>)", "", ""),
        E("With diode across R_B", "R_B ની સમાંતર diode સાથે", "t<sub>H</sub> = 0.693 R<sub>A</sub>C, t<sub>L</sub> = 0.693 R<sub>B</sub>C",
          "R_A = R_B gives 50 % duty cycle", "R_A = R_B થી 50 % duty cycle"),
        E("First cycle (from 0 V)", "પહેલો cycle (0 V થી)", "t<sub>H1</sub> ≈ 1.1 (R<sub>A</sub> + R<sub>B</sub>) C", "", ""),
    ]},
    {"title": {"en": "Frequency Counter", "gu": "Frequency Counter"}, "items": [
        E("Unknown frequency", "અજાણી frequency", "f<sub>x</sub> = N / T<sub>gate</sub>",
          "N = count; T_gate = 1 s → N = f in Hz", "N = count; T_gate = 1 s → N = f Hz માં"),
    ]},
]

VIVA = [
    {"title": {"en": "IC 555 – Pins and Block Diagram", "gu": "IC 555 – Pins અને Block Diagram"}, "items": [
        V("What is IC 555?", "IC 555 એટલે શું?",
          "An 8-pin timer IC used to generate accurate time delays and rectangular waves (oscillations).",
          "ચોક્કસ time delays અને rectangular waves (oscillations) બનાવવા વપરાતું 8-pin timer IC."),
        V("Who introduced the 555 and when?", "555 કોણે અને ક્યારે રજૂ કર્યું?",
          "Signetics Corporation in 1971; designed by Hans Camenzind.", "Signetics Corporation એ 1971 માં; Hans Camenzind એ ડિઝાઇન કર્યું."),
        V("Why is it called '555'?", "તેને '555' કેમ કહે છે?",
          "Because of the three 5 kΩ resistors in its internal voltage divider.", "તેના અંદરના voltage divider ના ત્રણ 5 kΩ resistors ને કારણે."),
        V("What is the supply voltage range of NE555?", "NE555 ની supply voltage range કેટલી છે?",
          "4.5 V to 15 V (maximum about 16–18 V).", "4.5 V થી 15 V (મહત્તમ લગભગ 16–18 V)."),
        V("What is the maximum output current of 555?", "555 નો મહત્તમ output current કેટલો છે?",
          "About 200 mA (source or sink).", "લગભગ 200 mA (source અથવા sink)."),
        V("What is IC 556?", "IC 556 એટલે શું?",
          "A dual timer – two 555 timers in one 14-pin package.", "Dual timer – એક 14-pin package માં બે 555 timers."),
        V("Name the pins of IC 555.", "IC 555 ના pins ના નામ આપો.",
          "1 GND, 2 Trigger, 3 Output, 4 Reset, 5 Control voltage, 6 Threshold, 7 Discharge, 8 +V_CC.",
          "1 GND, 2 Trigger, 3 Output, 4 Reset, 5 Control voltage, 6 Threshold, 7 Discharge, 8 +V_CC."),
        V("Why is the reset pin connected to V_CC?", "Reset pin ને V_CC સાથે કેમ જોડાય છે?",
          "Reset is active LOW; tying it HIGH prevents accidental resetting by noise.",
          "Reset active LOW છે; તેને HIGH રાખવાથી noise થી અચાનક reset થતું અટકે."),
        V("Why is a 0.01 µF capacitor connected at pin 5?", "Pin 5 પર 0.01 µF capacitor કેમ જોડાય છે?",
          "To bypass noise and ripple so that the threshold voltages remain stable.",
          "Noise અને ripple bypass કરવા જેથી threshold voltages સ્થિર રહે."),
        V("What are the two reference voltages inside 555?", "555 ની અંદર બે reference voltages કયા છે?",
          "⅔V_CC for the upper (threshold) comparator and ⅓V_CC for the lower (trigger) comparator.",
          "ઉપરના (threshold) comparator માટે ⅔V_CC અને નીચેના (trigger) comparator માટે ⅓V_CC."),
        V("What is the function of the flip-flop in 555?", "555 માં flip-flop નું કાર્ય શું છે?",
          "It stores the output state; set by the trigger comparator and reset by the threshold comparator.",
          "Output state સંગ્રહે; trigger comparator થી set અને threshold comparator થી reset થાય."),
        V("What is the function of the discharge transistor?", "Discharge transistor નું કાર્ય શું છે?",
          "When output is LOW it turns ON and discharges the timing capacitor through pin 7.",
          "Output LOW હોય ત્યારે ON થઈ pin 7 દ્વારા timing capacitor ને discharge કરે."),
        V("What happens when trigger voltage falls below ⅓V_CC?", "Trigger voltage ⅓V_CC થી નીચે જાય ત્યારે શું થાય?",
          "Flip-flop is set and output goes HIGH; discharge transistor turns OFF.",
          "Flip-flop set થાય અને output HIGH થાય; discharge transistor OFF થાય."),
        V("What happens when threshold voltage exceeds ⅔V_CC?", "Threshold voltage ⅔V_CC થી વધે ત્યારે શું થાય?",
          "Flip-flop is reset and output goes LOW; discharge transistor turns ON.",
          "Flip-flop reset થાય અને output LOW થાય; discharge transistor ON થાય."),
    ]},
    {"title": {"en": "Monostable and Astable", "gu": "Monostable અને Astable"}, "items": [
        V("What is a multivibrator?", "Multivibrator એટલે શું?",
          "A circuit that switches between two states (HIGH and LOW); used to generate rectangular waves or pulses.",
          "બે states (HIGH અને LOW) વચ્ચે બદલાતો circuit; rectangular waves અથવા pulses બનાવવા વપરાય."),
        V("How many stable states does a monostable have?", "Monostable માં કેટલી stable states હોય?",
          "One stable state (output LOW) and one quasi-stable state.", "એક stable state (output LOW) અને એક quasi-stable state."),
        V("Why is monostable called a one-shot?", "Monostable ને one-shot કેમ કહે છે?",
          "Because it gives exactly one output pulse for each trigger.", "કારણ કે દરેક trigger માટે બરાબર એક output pulse આપે છે."),
        V("Give the pulse-width formula of a 555 monostable.", "555 monostable નું pulse-width formula આપો.",
          "T = 1.1RC.", "T = 1.1RC."),
        V("Does the pulse width depend on V_CC?", "Pulse width V_CC પર આધાર રાખે છે?",
          "No. V_CC cancels out in the derivation; T depends only on R and C.",
          "ના. Derivation માં V_CC cancel થાય છે; T ફક્ત R અને C પર આધાર રાખે."),
        V("What type of trigger pulse does a 555 monostable need?", "555 monostable ને કેવો trigger pulse જોઈએ?",
          "A negative-going pulse at pin 2 that goes below ⅓V_CC and is shorter than T.",
          "Pin 2 પર ⅓V_CC થી નીચે જતો અને T કરતાં ટૂંકો negative-going pulse."),
        V("How many stable states does an astable have?", "Astable માં કેટલી stable states હોય?",
          "None – both states are quasi-stable, so it oscillates continuously.",
          "એક પણ નહીં – બંને states quasi-stable છે, તેથી સતત oscillate કરે."),
        V("Why is astable called a free-running multivibrator?", "Astable ને free-running multivibrator કેમ કહે છે?",
          "Because it produces a continuous output without any external trigger.",
          "કારણ કે બહારના trigger વગર સતત output આપે છે."),
        V("Give the frequency formula of a 555 astable.", "555 astable નું frequency formula આપો.",
          "f = 1.44 / [(R_A + 2R_B) C].", "f = 1.44 / [(R_A + 2R_B) C]."),
        V("Between which voltages does the capacitor voltage swing in astable mode?", "Astable mode માં capacitor voltage કયા voltages વચ્ચે ઝૂલે છે?",
          "Between ⅓V_CC and ⅔V_CC.", "⅓V_CC અને ⅔V_CC વચ્ચે."),
        V("What is duty cycle?", "Duty cycle એટલે શું?",
          "The ratio of HIGH time to total time period, expressed in %: D = t_H/T × 100.",
          "HIGH સમય અને કુલ time period નો ગુણોત્તર, % માં: D = t_H/T × 100."),
        V("Why is the duty cycle of a basic 555 astable always above 50 %?", "Basic 555 astable નો duty cycle હંમેશા 50 % થી વધુ કેમ હોય?",
          "Because C charges through R_A + R_B but discharges only through R_B, so t_H > t_L.",
          "કારણ કે C, R_A + R_B દ્વારા charge થાય પણ ફક્ત R_B દ્વારા discharge થાય, તેથી t_H > t_L."),
        V("How can 50 % duty cycle be obtained?", "50 % duty cycle કેવી રીતે મળે?",
          "Connect a diode across R_B and make R_A = R_B.", "R_B ની સમાંતર diode જોડો અને R_A = R_B રાખો."),
        V("Which pins are joined in astable and in monostable mode?", "Astable અને monostable mode માં કયા pins જોડાય છે?",
          "Astable: pins 2 and 6. Monostable: pins 6 and 7.", "Astable: pins 2 અને 6. Monostable: pins 6 અને 7."),
    ]},
    {"title": {"en": "Applications", "gu": "ઉપયોગો"}, "items": [
        V("Which mode is used for an LED flasher?", "LED flasher માટે કયો mode વપરાય?",
          "Astable mode.", "Astable mode."),
        V("What is the difference between sourcing and sinking current at pin 3?", "Pin 3 પર sourcing અને sinking current માં શું તફાવત છે?",
          "Sourcing: load from pin 3 to ground, ON when output HIGH. Sinking: load from V_CC to pin 3, ON when output LOW.",
          "Sourcing: load pin 3 થી ground, output HIGH હોય ત્યારે ON. Sinking: load V_CC થી pin 3, output LOW હોય ત્યારે ON."),
        V("Which mode is used for a timer / time-delay circuit?", "Timer / time-delay circuit માટે કયો mode વપરાય?",
          "Monostable mode.", "Monostable mode."),
        V("What is the role of 555 in a frequency counter?", "Frequency counter માં 555 ની ભૂમિકા શું છે?",
          "It generates the accurate gate pulse (e.g. 1 s) during which input pulses are counted.",
          "તે ચોક્કસ gate pulse (દા.ત. 1 s) બનાવે છે જે દરમિયાન input pulses ગણાય છે."),
        V("How is frequency calculated in a frequency counter?", "Frequency counter માં frequency કેવી રીતે ગણાય?",
          "f = N / T_gate, where N is the number of pulses counted in the gate time.",
          "f = N / T_gate, જ્યાં N gate time માં ગણેલા pulses ની સંખ્યા છે."),
        V("Name some applications of 555.", "555 ના થોડા ઉપયોગો જણાવો.",
          "LED flasher, timer, pulse generator, frequency counter, PWM, missing-pulse detector, alarm, siren, VCO.",
          "LED flasher, timer, pulse generator, frequency counter, PWM, missing-pulse detector, alarm, siren, VCO."),
    ]},
]

EXAM_QS = [
    X("State the features of IC 555.", "IC 555 ની વિશેષતાઓ (features) લખો.", 3),
    X("Draw the pin diagram of IC 555 and explain the function of each pin.", "IC 555 નો pin diagram દોરો અને દરેક pin નું કાર્ય સમજાવો.", 4),
    X("Explain the function of trigger, threshold, reset and control voltage pins of IC 555.", "IC 555 ના trigger, threshold, reset અને control voltage pins નું કાર્ય સમજાવો.", 3),
    X("Draw the functional block diagram of IC 555 and explain its working.", "IC 555 નો functional block diagram દોરો અને તેનું કાર્ય સમજાવો.", 7),
    X("Write the function table of IC 555.", "IC 555 નો function table લખો.", 3),
    X("Explain the working of 555 as a monostable multivibrator with circuit diagram and waveforms.", "Circuit diagram અને waveforms સાથે monostable multivibrator તરીકે 555 નું કાર્ય સમજાવો.", 7),
    X("Derive the expression T = 1.1RC for a 555 monostable multivibrator.", "555 monostable multivibrator માટે T = 1.1RC સૂત્ર સાબિત કરો.", 3),
    X("Explain the working of 555 as an astable multivibrator with circuit diagram and waveforms.", "Circuit diagram અને waveforms સાથે astable multivibrator તરીકે 555 નું કાર્ય સમજાવો.", 7),
    X("Derive the expressions for t_H, t_L, frequency and duty cycle of a 555 astable multivibrator.", "555 astable multivibrator માટે t_H, t_L, frequency અને duty cycle ના સૂત્રો સાબિત કરો.", 4),
    X("Why is the duty cycle of a 555 astable more than 50 %? How can it be made 50 %?", "555 astable નો duty cycle 50 % થી વધુ કેમ હોય છે? તેને 50 % કેવી રીતે કરી શકાય?", 3),
    X("Compare monostable, astable and bistable multivibrators.", "Monostable, astable અને bistable multivibrators ની સરખામણી કરો.", 4),
    X("Explain 555 as a pulse generator (LED flasher) with circuit diagram.", "Circuit diagram સાથે pulse generator (LED flasher) તરીકે 555 સમજાવો.", 4),
    X("Explain the use of 555 as a timer.", "Timer તરીકે 555 નો ઉપયોગ સમજાવો.", 3),
    X("Explain the use of 555 timer in a frequency counter with block diagram.", "Block diagram સાથે frequency counter માં 555 timer નો ઉપયોગ સમજાવો.", 4),
    X("List the applications of IC 555.", "IC 555 ના ઉપયોગો લખો.", 3),
    X("Calculate the pulse width of a 555 monostable with R = 100 kΩ and C = 10 µF.", "R = 100 kΩ અને C = 10 µF વાળા 555 monostable ની pulse width ગણો.", 3),
    X("Find the frequency and duty cycle of a 555 astable with R_A = 1 kΩ, R_B = 10 kΩ and C = 0.1 µF.", "R_A = 1 kΩ, R_B = 10 kΩ અને C = 0.1 µF વાળા 555 astable ની frequency અને duty cycle શોધો.", 4),
]
