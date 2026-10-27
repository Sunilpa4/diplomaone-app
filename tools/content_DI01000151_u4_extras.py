"""Basics of Electronics (DI01000151) - Unit 4 extras: numericals, equations, viva, exam questions"""
from content_DI01000151_u3_extras import N, E, V, X

NUMERICALS = [
    N("u4n1",
      "In a transistor, I_E = 10 mA and I_C = 9.8 mA. Find I_B, α and β.",
      "એક transistor માં I_E = 10 mA અને I_C = 9.8 mA છે. I_B, α અને β શોધો.",
      """<p>I<sub>B</sub> = I<sub>E</sub> − I<sub>C</sub> = 10 − 9.8 = <b>0.2 mA</b></p>
<p>α = I<sub>C</sub> / I<sub>E</sub> = 9.8 / 10 = <b>0.98</b></p>
<p>β = I<sub>C</sub> / I<sub>B</sub> = 9.8 / 0.2 = <b>49</b></p>
<p>Check: β = α/(1 − α) = 0.98/0.02 = 49 ✓</p>""",
      """<p>I<sub>B</sub> = I<sub>E</sub> − I<sub>C</sub> = 10 − 9.8 = <b>0.2 mA</b></p>
<p>α = I<sub>C</sub> / I<sub>E</sub> = 9.8 / 10 = <b>0.98</b></p>
<p>β = I<sub>C</sub> / I<sub>B</sub> = 9.8 / 0.2 = <b>49</b></p>
<p>ચકાસણી: β = α/(1 − α) = 0.98/0.02 = 49 ✓</p>"""),
    N("u4n2",
      "A transistor has β = 100 and base current I_B = 40 µA. Find I_C, I_E and α.",
      "Transistor માં β = 100 અને base current I_B = 40 µA છે. I_C, I_E અને α શોધો.",
      """<p>I<sub>C</sub> = β I<sub>B</sub> = 100 × 40 µA = 4000 µA = <b>4 mA</b></p>
<p>I<sub>E</sub> = I<sub>B</sub> + I<sub>C</sub> = 0.04 + 4 = <b>4.04 mA</b></p>
<p>α = β / (1 + β) = 100 / 101 = <b>0.990</b></p>""",
      """<p>I<sub>C</sub> = β I<sub>B</sub> = 100 × 40 µA = 4000 µA = <b>4 mA</b></p>
<p>I<sub>E</sub> = I<sub>B</sub> + I<sub>C</sub> = 0.04 + 4 = <b>4.04 mA</b></p>
<p>α = β / (1 + β) = 100 / 101 = <b>0.990</b></p>"""),
    N("u4n3",
      "(a) Find β if α = 0.995. (b) Find α if β = 150.",
      "(a) α = 0.995 હોય તો β શોધો. (b) β = 150 હોય તો α શોધો.",
      """<p>(a) β = α / (1 − α) = 0.995 / 0.005 = <b>199</b></p>
<p>(b) α = β / (1 + β) = 150 / 151 = <b>0.9934</b></p>
<p><i>A very small change in α (near 1) gives a large change in β.</i></p>""",
      """<p>(a) β = α / (1 − α) = 0.995 / 0.005 = <b>199</b></p>
<p>(b) α = β / (1 + β) = 150 / 151 = <b>0.9934</b></p>
<p><i>α (1 નજીક) માં ખૂબ નાનો ફેરફાર β માં મોટો ફેરફાર કરે છે.</i></p>"""),
    N("u4n4",
      "A CE amplifier has input resistance r_i = 1 kΩ, load resistance R_L = 2 kΩ and β = 100. Find the voltage gain and power gain (also in dB).",
      "CE amplifier માં input resistance r_i = 1 kΩ, load resistance R_L = 2 kΩ અને β = 100 છે. Voltage gain અને power gain (dB માં પણ) શોધો.",
      """<p>A<sub>v</sub> = β × R<sub>L</sub> / r<sub>i</sub> = 100 × 2000 / 1000 = <b>200</b> (output inverted, 180°)</p>
<p>A<sub>p</sub> = β × A<sub>v</sub> = 100 × 200 = <b>20,000</b></p>
<p>A<sub>p</sub>(dB) = 10 log<sub>10</sub>(20000) = <b>43 dB</b>; A<sub>v</sub>(dB) = 20 log<sub>10</sub>(200) = <b>46 dB</b></p>""",
      """<p>A<sub>v</sub> = β × R<sub>L</sub> / r<sub>i</sub> = 100 × 2000 / 1000 = <b>200</b> (output ઉલટો, 180°)</p>
<p>A<sub>p</sub> = β × A<sub>v</sub> = 100 × 200 = <b>20,000</b></p>
<p>A<sub>p</sub>(dB) = 10 log<sub>10</sub>(20000) = <b>43 dB</b>; A<sub>v</sub>(dB) = 20 log<sub>10</sub>(200) = <b>46 dB</b></p>"""),
    N("u4n5",
      "In a CB amplifier, α = 0.98, input resistance = 50 Ω and load resistance = 5 kΩ. Find voltage gain and power gain.",
      "CB amplifier માં α = 0.98, input resistance = 50 Ω અને load resistance = 5 kΩ છે. Voltage gain અને power gain શોધો.",
      """<p>A<sub>v</sub> = α × R<sub>L</sub> / r<sub>i</sub> = 0.98 × 5000 / 50 = <b>98</b></p>
<p>A<sub>p</sub> = α × A<sub>v</sub> = 0.98 × 98 = <b>96.04</b></p>
<p><i>Current gain &lt; 1, but voltage gain is high because R<sub>L</sub> ≫ r<sub>i</sub>.</i></p>""",
      """<p>A<sub>v</sub> = α × R<sub>L</sub> / r<sub>i</sub> = 0.98 × 5000 / 50 = <b>98</b></p>
<p>A<sub>p</sub> = α × A<sub>v</sub> = 0.98 × 98 = <b>96.04</b></p>
<p><i>Current gain &lt; 1 છે, પરંતુ R<sub>L</sub> ≫ r<sub>i</sub> હોવાથી voltage gain વધુ છે.</i></p>"""),
    N("u4n6",
      "A transistor has β = 99. Find γ and α. If I_B = 50 µA, find I_E and I_C.",
      "Transistor માં β = 99 છે. γ અને α શોધો. જો I_B = 50 µA હોય તો I_E અને I_C શોધો.",
      """<p>γ = 1 + β = <b>100</b>; α = β/(1 + β) = 99/100 = <b>0.99</b></p>
<p>I<sub>E</sub> = γ I<sub>B</sub> = 100 × 50 µA = <b>5 mA</b></p>
<p>I<sub>C</sub> = β I<sub>B</sub> = 99 × 50 µA = <b>4.95 mA</b></p>""",
      """<p>γ = 1 + β = <b>100</b>; α = β/(1 + β) = 99/100 = <b>0.99</b></p>
<p>I<sub>E</sub> = γ I<sub>B</sub> = 100 × 50 µA = <b>5 mA</b></p>
<p>I<sub>C</sub> = β I<sub>B</sub> = 99 × 50 µA = <b>4.95 mA</b></p>"""),
    N("u4n7",
      "Design a transistor switch to glow a red LED (V_F = 2 V, 15 mA) from V_CC = 5 V. The input is 5 V (HIGH), β = 100, V_CE(sat) = 0.2 V, V_BE = 0.7 V. Find R_C and R_B.",
      "V_CC = 5 V થી લાલ LED (V_F = 2 V, 15 mA) ચલાવવા transistor switch ડિઝાઇન કરો. Input 5 V (HIGH), β = 100, V_CE(sat) = 0.2 V, V_BE = 0.7 V. R_C અને R_B શોધો.",
      """<p><b>Collector resistor:</b> R<sub>C</sub> = (V<sub>CC</sub> − V<sub>F</sub> − V<sub>CE(sat)</sub>) / I<sub>C</sub> = (5 − 2 − 0.2) / 0.015 = <b>186.7 Ω</b> → use <b>180 Ω</b> (I<sub>C</sub> = 2.8/180 ≈ 15.6 mA).</p>
<p><b>Minimum base current:</b> I<sub>B(min)</sub> = I<sub>C</sub> / β = 15.6 mA / 100 = 0.156 mA</p>
<p>For hard saturation take I<sub>B</sub> ≈ 5 × I<sub>B(min)</sub> ≈ 0.78 mA</p>
<p><b>Base resistor:</b> R<sub>B</sub> = (V<sub>in</sub> − V<sub>BE</sub>) / I<sub>B</sub> = (5 − 0.7) / 0.78 mA ≈ 5.5 kΩ → use <b>4.7 kΩ</b> (I<sub>B</sub> ≈ 0.91 mA, transistor surely saturated).</p>""",
      """<p><b>Collector resistor:</b> R<sub>C</sub> = (V<sub>CC</sub> − V<sub>F</sub> − V<sub>CE(sat)</sub>) / I<sub>C</sub> = (5 − 2 − 0.2) / 0.015 = <b>186.7 Ω</b> → <b>180 Ω</b> વાપરો (I<sub>C</sub> = 2.8/180 ≈ 15.6 mA).</p>
<p><b>ન્યૂનતમ base current:</b> I<sub>B(min)</sub> = I<sub>C</sub> / β = 15.6 mA / 100 = 0.156 mA</p>
<p>Hard saturation માટે I<sub>B</sub> ≈ 5 × I<sub>B(min)</sub> ≈ 0.78 mA લો</p>
<p><b>Base resistor:</b> R<sub>B</sub> = (V<sub>in</sub> − V<sub>BE</sub>) / I<sub>B</sub> = (5 − 0.7) / 0.78 mA ≈ 5.5 kΩ → <b>4.7 kΩ</b> વાપરો (I<sub>B</sub> ≈ 0.91 mA, transistor ચોક્કસ saturate થાય).</p>"""),
    N("u4n8",
      "A transistor has I_CBO = 5 µA and β = 100. Find I_CEO. Also find I_C when I_B = 20 µA.",
      "Transistor માં I_CBO = 5 µA અને β = 100 છે. I_CEO શોધો. I_B = 20 µA હોય ત્યારે I_C પણ શોધો.",
      """<p>I<sub>CEO</sub> = (1 + β) I<sub>CBO</sub> = 101 × 5 µA = <b>505 µA ≈ 0.505 mA</b></p>
<p>I<sub>C</sub> = β I<sub>B</sub> + I<sub>CEO</sub> = 100 × 20 µA + 0.505 mA = 2 + 0.505 = <b>2.505 mA</b></p>
<p><i>Leakage in CE is (1 + β) times larger than in CB.</i></p>""",
      """<p>I<sub>CEO</sub> = (1 + β) I<sub>CBO</sub> = 101 × 5 µA = <b>505 µA ≈ 0.505 mA</b></p>
<p>I<sub>C</sub> = β I<sub>B</sub> + I<sub>CEO</sub> = 100 × 20 µA + 0.505 mA = 2 + 0.505 = <b>2.505 mA</b></p>
<p><i>CE માં leakage, CB કરતાં (1 + β) ગણો વધુ હોય છે.</i></p>"""),
    N("u4n9",
      "In a CE circuit, V_CC = 12 V and R_C = 2 kΩ. Find the end points of the DC load line. If I_B = 30 µA and β = 100, find the Q-point.",
      "CE circuit માં V_CC = 12 V અને R_C = 2 kΩ છે. DC load line ના છેડાના બિંદુઓ શોધો. જો I_B = 30 µA અને β = 100 હોય તો Q-point શોધો.",
      """<p><b>Cut-off point:</b> I<sub>C</sub> = 0 → V<sub>CE</sub> = V<sub>CC</sub> = <b>12 V</b></p>
<p><b>Saturation point:</b> V<sub>CE</sub> = 0 → I<sub>C(sat)</sub> = V<sub>CC</sub> / R<sub>C</sub> = 12 / 2000 = <b>6 mA</b></p>
<p><b>Q-point:</b> I<sub>C</sub> = β I<sub>B</sub> = 100 × 30 µA = <b>3 mA</b></p>
<p>V<sub>CE</sub> = V<sub>CC</sub> − I<sub>C</sub> R<sub>C</sub> = 12 − 3 × 2 = <b>6 V</b></p>
<p>Q-point = (6 V, 3 mA) – exactly in the middle of the load line → good for an amplifier.</p>""",
      """<p><b>Cut-off બિંદુ:</b> I<sub>C</sub> = 0 → V<sub>CE</sub> = V<sub>CC</sub> = <b>12 V</b></p>
<p><b>Saturation બિંદુ:</b> V<sub>CE</sub> = 0 → I<sub>C(sat)</sub> = V<sub>CC</sub> / R<sub>C</sub> = 12 / 2000 = <b>6 mA</b></p>
<p><b>Q-point:</b> I<sub>C</sub> = β I<sub>B</sub> = 100 × 30 µA = <b>3 mA</b></p>
<p>V<sub>CE</sub> = V<sub>CC</sub> − I<sub>C</sub> R<sub>C</sub> = 12 − 3 × 2 = <b>6 V</b></p>
<p>Q-point = (6 V, 3 mA) – load line ના બરાબર મધ્યમાં → amplifier માટે યોગ્ય.</p>"""),
]

EQUATIONS = [
    {"title": {"en": "Transistor Currents", "gu": "Transistor Currents"}, "items": [
        E("Current relation (KCL)", "Current સંબંધ (KCL)", "I<sub>E</sub> = I<sub>B</sub> + I<sub>C</sub>",
          "I_B is very small, so I_C ≈ I_E", "I_B ખૂબ નાનો, તેથી I_C ≈ I_E"),
        E("CB current gain", "CB current gain", "α = I<sub>C</sub> / I<sub>E</sub>",
          "Always < 1 (0.95 – 0.995)", "હંમેશા < 1 (0.95 – 0.995)"),
        E("CE current gain", "CE current gain", "β = I<sub>C</sub> / I<sub>B</sub>  (= h<sub>FE</sub>)",
          "Typical 20 – 500", "સામાન્ય 20 – 500"),
        E("CC current gain", "CC current gain", "γ = I<sub>E</sub> / I<sub>B</sub> = 1 + β",
          "Highest current gain", "સૌથી વધુ current gain"),
        E("β from α", "α પરથી β", "β = α / (1 − α)", "", ""),
        E("α from β", "β પરથી α", "α = β / (1 + β)", "", ""),
        E("γ from α", "α પરથી γ", "γ = 1 / (1 − α)", "", ""),
        E("Collector current with leakage (CB)", "Leakage સાથે collector current (CB)", "I<sub>C</sub> = α I<sub>E</sub> + I<sub>CBO</sub>",
          "I_CBO = collector-base leakage (emitter open)", "I_CBO = collector-base leakage (emitter open)"),
        E("Collector current with leakage (CE)", "Leakage સાથે collector current (CE)", "I<sub>C</sub> = β I<sub>B</sub> + I<sub>CEO</sub>",
          "I_CEO = (1 + β) I_CBO", "I_CEO = (1 + β) I_CBO"),
    ]},
    {"title": {"en": "Characteristics and Gains", "gu": "Characteristics અને Gains"}, "items": [
        E("CE input resistance", "CE input resistance", "r<sub>i</sub> = ΔV<sub>BE</sub> / ΔI<sub>B</sub>  (V<sub>CE</sub> const.)",
          "≈ 1 kΩ", "≈ 1 kΩ"),
        E("CE output resistance", "CE output resistance", "r<sub>o</sub> = ΔV<sub>CE</sub> / ΔI<sub>C</sub>  (I<sub>B</sub> const.)",
          "≈ 10 – 50 kΩ", "≈ 10 – 50 kΩ"),
        E("CB input / output resistance", "CB input / output resistance", "r<sub>i</sub> = ΔV<sub>EB</sub>/ΔI<sub>E</sub>,  r<sub>o</sub> = ΔV<sub>CB</sub>/ΔI<sub>C</sub>",
          "r_i very low, r_o very high", "r_i ખૂબ ઓછો, r_o ખૂબ વધુ"),
        E("AC current gain", "AC current gain", "β<sub>ac</sub> = ΔI<sub>C</sub> / ΔI<sub>B</sub>  (V<sub>CE</sub> const.)", "h_fe", "h_fe"),
        E("Voltage gain – CB", "Voltage gain – CB", "A<sub>v</sub> = α R<sub>L</sub> / r<sub>i</sub>", "", ""),
        E("Voltage gain – CE", "Voltage gain – CE", "A<sub>v</sub> = β R<sub>L</sub> / r<sub>i</sub>", "Output 180° out of phase", "Output 180° phase માં ઉલટો"),
        E("Power gain", "Power gain", "A<sub>p</sub> = A<sub>i</sub> × A<sub>v</sub>", "CE: A_p = β² R_L / r_i (highest)", "CE: A_p = β² R_L / r_i (સૌથી વધુ)"),
        E("Gain in dB", "dB માં gain", "A<sub>p</sub>(dB) = 10 log A<sub>p</sub>;  A<sub>v</sub>(dB) = 20 log A<sub>v</sub>", "", ""),
    ]},
    {"title": {"en": "Transistor as a Switch", "gu": "Switch તરીકે Transistor"}, "items": [
        E("DC load line", "DC load line", "V<sub>CE</sub> = V<sub>CC</sub> − I<sub>C</sub> R<sub>C</sub>",
          "End points: (V_CC, 0) and (0, V_CC/R_C)", "છેડા: (V_CC, 0) અને (0, V_CC/R_C)"),
        E("Saturation current", "Saturation current", "I<sub>C(sat)</sub> = (V<sub>CC</sub> − V<sub>CE(sat)</sub>) / R<sub>C</sub> ≈ V<sub>CC</sub> / R<sub>C</sub>",
          "V_CE(sat) ≈ 0.2 V", "V_CE(sat) ≈ 0.2 V"),
        E("Condition for saturation", "Saturation માટેની શરત", "I<sub>B</sub> > I<sub>C(sat)</sub> / β",
          "Use 2–10 times for hard saturation", "Hard saturation માટે 2–10 ગણો લો"),
        E("Base resistor", "Base resistor", "R<sub>B</sub> = (V<sub>in</sub> − V<sub>BE</sub>) / I<sub>B</sub>",
          "V_BE ≈ 0.7 V (Si)", "V_BE ≈ 0.7 V (Si)"),
        E("Power dissipation", "Power dissipation", "P<sub>D</sub> = V<sub>CE</sub> × I<sub>C</sub>",
          "Very small in both ON and OFF states", "ON અને OFF બંને સ્થિતિમાં ખૂબ ઓછો"),
    ]},
]

VIVA = [
    {"title": {"en": "Construction and Working", "gu": "રચના અને કાર્ય"}, "items": [
        V("What is a transistor?", "Transistor એટલે શું?",
          "A three-terminal semiconductor device used for amplification and switching.",
          "Amplification અને switching માટે વપરાતું ત્રણ terminal વાળું semiconductor device."),
        V("Why is it called 'bipolar'?", "તેને 'bipolar' કેમ કહે છે?",
          "Because both electrons and holes take part in conduction.", "કારણ કે conduction માં electrons અને holes બંને ભાગ લે છે."),
        V("Name the three terminals of a BJT.", "BJT ના ત્રણ terminals ના નામ આપો.",
          "Emitter, Base and Collector.", "Emitter, Base અને Collector."),
        V("Which region is most heavily doped?", "કયો region સૌથી વધુ doped છે?",
          "Emitter.", "Emitter."),
        V("Why is the base made thin and lightly doped?", "Base ને પાતળો અને ઓછો doped કેમ બનાવાય છે?",
          "So that very few carriers recombine in the base and most reach the collector.",
          "જેથી base માં ખૂબ ઓછા carriers recombine થાય અને મોટાભાગના collector સુધી પહોંચે."),
        V("Why is the collector made largest?", "Collector ને સૌથી મોટો કેમ બનાવાય છે?",
          "To dissipate the heat produced at the collector junction.", "Collector junction પર ઉત્પન્ન થતી ઉષ્મા દૂર કરવા."),
        V("Can emitter and collector be interchanged?", "Emitter અને collector અદલાબદલી કરી શકાય?",
          "No, because their doping levels and sizes are different.", "ના, કારણ કે તેમના doping અને કદ અલગ છે."),
        V("How do you identify NPN and PNP from the symbol?", "Symbol પરથી NPN અને PNP કેવી રીતે ઓળખાય?",
          "NPN: emitter arrow points outward; PNP: arrow points inward.", "NPN: emitter arrow બહાર તરફ; PNP: arrow અંદર તરફ."),
        V("What biasing is needed for the active region?", "Active region માટે કયું biasing જરૂરી છે?",
          "Emitter-base junction forward biased and collector-base junction reverse biased.",
          "Emitter-base junction forward biased અને collector-base junction reverse biased."),
        V("What percentage of emitter current reaches the collector?", "Emitter current ના કેટલા ટકા collector સુધી પહોંચે છે?",
          "About 95–99%.", "આશરે 95–99%."),
        V("Why is NPN preferred over PNP?", "PNP કરતાં NPN કેમ વધુ પસંદ કરાય છે?",
          "Electrons have higher mobility than holes, so NPN is faster.", "Electrons ની mobility holes કરતાં વધુ છે, તેથી NPN વધુ ઝડપી છે."),
        V("Pin order of BC547 (flat face towards you)?", "BC547 નો pin ક્રમ (સપાટ ભાગ તમારી તરફ)?",
          "Collector – Base – Emitter (left to right).", "Collector – Base – Emitter (ડાબેથી જમણે)."),
    ]},
    {"title": {"en": "Configurations and Gains", "gu": "Configurations અને Gains"}, "items": [
        V("Name the three transistor configurations.", "Transistor ના ત્રણ configurations ના નામ આપો.",
          "Common Base (CB), Common Emitter (CE) and Common Collector (CC).", "Common Base (CB), Common Emitter (CE) અને Common Collector (CC)."),
        V("Which configuration is most widely used and why?", "કયું configuration સૌથી વધુ વપરાય છે અને કેમ?",
          "CE, because it gives the highest power gain with good current and voltage gain.",
          "CE, કારણ કે તે સારા current અને voltage gain સાથે સૌથી વધુ power gain આપે છે."),
        V("Define α.", "α ની વ્યાખ્યા આપો.",
          "Ratio of collector current to emitter current (I_C/I_E) in CB.", "CB માં collector current અને emitter current નો ગુણોત્તર (I_C/I_E)."),
        V("Define β.", "β ની વ્યાખ્યા આપો.",
          "Ratio of collector current to base current (I_C/I_B) in CE.", "CE માં collector current અને base current નો ગુણોત્તર (I_C/I_B)."),
        V("Relation between α and β?", "α અને β વચ્ચેનો સંબંધ?",
          "β = α/(1 − α) and α = β/(1 + β).", "β = α/(1 − α) અને α = β/(1 + β)."),
        V("What is γ?", "γ એટલે શું?",
          "Current gain of CC configuration: γ = I_E/I_B = 1 + β.", "CC configuration નો current gain: γ = I_E/I_B = 1 + β."),
        V("Which configuration has the highest input resistance?", "કયા configuration માં સૌથી વધુ input resistance છે?",
          "Common Collector (CC).", "Common Collector (CC)."),
        V("Which configuration has phase shift of 180°?", "કયા configuration માં 180° phase shift છે?",
          "Common Emitter (CE).", "Common Emitter (CE)."),
        V("Why is CC called an emitter follower?", "CC ને emitter follower કેમ કહે છે?",
          "Because the emitter (output) voltage follows the base (input) voltage; voltage gain ≈ 1.",
          "કારણ કે emitter (output) voltage base (input) voltage ને અનુસરે છે; voltage gain ≈ 1."),
        V("What is the Early effect?", "Early effect એટલે શું?",
          "Reduction of effective base width when collector voltage increases (base-width modulation).",
          "Collector voltage વધતાં અસરકારક base width ઘટવું (base-width modulation)."),
        V("What are the regions on CE output characteristics?", "CE output characteristics પર કયા regions છે?",
          "Active, saturation and cut-off regions.", "Active, saturation અને cut-off regions."),
        V("What is thermal runaway?", "Thermal runaway એટલે શું?",
          "Self-heating cycle: temperature ↑ → leakage ↑ → I_C ↑ → more heat, which can destroy the transistor.",
          "સ્વ-ગરમીનું ચક્ર: તાપમાન ↑ → leakage ↑ → I_C ↑ → વધુ ઉષ્મા, જે transistor ને નષ્ટ કરી શકે."),
    ]},
    {"title": {"en": "Transistor as a Switch", "gu": "Switch તરીકે Transistor"}, "items": [
        V("In which regions does a transistor work as a switch?", "Transistor switch તરીકે કયા regions માં કામ કરે છે?",
          "Cut-off (OFF) and saturation (ON).", "Cut-off (OFF) અને saturation (ON)."),
        V("What is V_CE when the transistor switch is ON?", "Transistor switch ON હોય ત્યારે V_CE કેટલો હોય?",
          "About 0.2 V (V_CE(sat)).", "આશરે 0.2 V (V_CE(sat))."),
        V("What is V_CE when the switch is OFF?", "Switch OFF હોય ત્યારે V_CE કેટલો હોય?",
          "Almost equal to V_CC.", "લગભગ V_CC જેટલો."),
        V("What is the condition for saturation?", "Saturation માટેની શરત શું છે?",
          "I_B > I_C(sat) / β.", "I_B > I_C(sat) / β."),
        V("What is a DC load line?", "DC load line એટલે શું?",
          "A straight line on output characteristics given by V_CE = V_CC − I_C R_C; the Q-point lies on it.",
          "Output characteristics પર V_CE = V_CC − I_C R_C થી મળતી સીધી રેખા; Q-point તેના પર હોય છે."),
        V("Which logic gate does a transistor switch act as?", "Transistor switch કયા logic gate તરીકે કામ કરે છે?",
          "NOT gate (inverter).", "NOT gate (inverter)."),
        V("Why is a diode connected across a relay coil?", "Relay coil પર diode કેમ જોડાય છે?",
          "To absorb the back EMF and protect the transistor (freewheeling diode).", "Back EMF શોષી transistor ને રક્ષણ આપવા (freewheeling diode)."),
    ]},
]

EXAM_QS = [
    X("Explain the construction of NPN and PNP transistors with symbols.", "Symbols સાથે NPN અને PNP transistors ની રચના સમજાવો.", 4),
    X("Why is the emitter heavily doped and the base lightly doped and thin?", "Emitter વધુ doped અને base ઓછો doped અને પાતળો કેમ હોય છે?", 3),
    X("Compare NPN and PNP transistors.", "NPN અને PNP transistors ની સરખામણી કરો.", 3),
    X("Explain the working of NPN transistor with a neat diagram.", "સ્વચ્છ આકૃતિ સાથે NPN transistor નું કાર્ય સમજાવો.", 4),
    X("Explain the working of PNP transistor.", "PNP transistor નું કાર્ય સમજાવો.", 4),
    X("State the regions of operation of a transistor with junction biasing.", "Junction biasing સાથે transistor ના regions of operation લખો.", 3),
    X("Define α and β. Derive the relation between them.", "α અને β ની વ્યાખ્યા આપો. તેમની વચ્ચેનો સંબંધ સાબિત કરો.", 4),
    X("Derive the relation γ = 1 + β = 1/(1 − α).", "સંબંધ γ = 1 + β = 1/(1 − α) સાબિત કરો.", 3),
    X("Explain CB configuration with circuit diagram and characteristics.", "Circuit diagram અને characteristics સાથે CB configuration સમજાવો.", 4),
    X("Draw the circuit for CE characteristics and explain input and output characteristics of NPN transistor.", "CE characteristics માટેનો circuit દોરો અને NPN transistor ની input અને output characteristics સમજાવો.", 7),
    X("Explain active, saturation and cut-off regions on CE output characteristics.", "CE output characteristics પર active, saturation અને cut-off regions સમજાવો.", 3),
    X("Explain CC configuration. Why is it called an emitter follower?", "CC configuration સમજાવો. તેને emitter follower કેમ કહે છે?", 3),
    X("Compare CB, CE and CC configurations.", "CB, CE અને CC configurations ની સરખામણી કરો.", 4),
    X("Explain current gain and voltage gain of a transistor amplifier.", "Transistor amplifier નો current gain અને voltage gain સમજાવો.", 3),
    X("Explain DC load line with a neat sketch.", "સ્વચ્છ આકૃતિ સાથે DC load line સમજાવો.", 3),
    X("Explain transistor as a switch with circuit diagram.", "Circuit diagram સાથે switch તરીકે transistor સમજાવો.", 4),
    X("Explain transistor as a switch with load line and state its applications.", "Load line સાથે switch તરીકે transistor સમજાવો અને તેના ઉપયોગો લખો.", 7),
]
