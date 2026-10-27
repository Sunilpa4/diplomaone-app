"""Basics of Electronics (DI01000151) - Unit 3 extras: numericals, equations, viva, exam questions"""


def N(id_, q_en, q_gu, a_en, a_gu):
    return {"id": id_, "q": {"en": q_en, "gu": q_gu}, "a": {"en": a_en, "gu": a_gu}}


NUMERICALS = [
    N("u3n1",
      "A silicon diode has V_F = 0.70 V at I_F = 10 mA and V_F = 0.72 V at I_F = 20 mA. Find (i) static resistance at 10 mA and (ii) dynamic resistance.",
      "Silicon diode માં I_F = 10 mA પર V_F = 0.70 V અને I_F = 20 mA પર V_F = 0.72 V છે. (i) 10 mA પર static resistance અને (ii) dynamic resistance શોધો.",
      """<p>(i) Static resistance: R<sub>DC</sub> = V<sub>F</sub> / I<sub>F</sub> = 0.70 / (10 × 10⁻³) = <b>70 Ω</b></p>
<p>(ii) Dynamic resistance: r<sub>d</sub> = ΔV / ΔI = (0.72 − 0.70) / (20 − 10) × 10⁻³ = 0.02 / 0.01 = <b>2 Ω</b></p>
<p><i>Dynamic resistance is much smaller than static resistance above the knee.</i></p>""",
      """<p>(i) Static resistance: R<sub>DC</sub> = V<sub>F</sub> / I<sub>F</sub> = 0.70 / (10 × 10⁻³) = <b>70 Ω</b></p>
<p>(ii) Dynamic resistance: r<sub>d</sub> = ΔV / ΔI = (0.72 − 0.70) / (20 − 10) × 10⁻³ = 0.02 / 0.01 = <b>2 Ω</b></p>
<p><i>Knee થી ઉપર dynamic resistance, static resistance કરતાં ઘણો ઓછો હોય છે.</i></p>"""),
    N("u3n2",
      "A red LED (V_F = 2 V, I_F = 15 mA) is to be operated from a 5 V supply. Find the series resistance and its power rating.",
      "લાલ LED (V_F = 2 V, I_F = 15 mA) ને 5 V supply થી ચલાવવો છે. Series resistance અને તેનું power rating શોધો.",
      """<p>R = (V<sub>S</sub> − V<sub>F</sub>) / I<sub>F</sub> = (5 − 2) / (15 × 10⁻³) = 3 / 0.015 = <b>200 Ω</b></p>
<p>Nearest standard value: <b>220 Ω</b> (gives I = 3/220 ≈ 13.6 mA, safe).</p>
<p>Power in resistor: P = I²R = (0.015)² × 200 = <b>45 mW</b> → a <b>¼ W</b> resistor is sufficient.</p>""",
      """<p>R = (V<sub>S</sub> − V<sub>F</sub>) / I<sub>F</sub> = (5 − 2) / (15 × 10⁻³) = 3 / 0.015 = <b>200 Ω</b></p>
<p>નજીકનું standard મૂલ્ય: <b>220 Ω</b> (I = 3/220 ≈ 13.6 mA, સુરક્ષિત).</p>
<p>Resistor માં power: P = I²R = (0.015)² × 200 = <b>45 mW</b> → <b>¼ W</b> resistor પૂરતો છે.</p>"""),
    N("u3n3",
      "In a Zener regulator, V_in = 15 V, V_Z = 10 V, R_S = 250 Ω and R_L = 1 kΩ. Find (i) load current (ii) current through R_S (iii) Zener current (iv) power dissipated in the Zener.",
      "Zener regulator માં V_in = 15 V, V_Z = 10 V, R_S = 250 Ω અને R_L = 1 kΩ છે. (i) Load current (ii) R_S માંથી current (iii) Zener current (iv) Zener માં power dissipation શોધો.",
      """<p>V<sub>out</sub> = V<sub>Z</sub> = 10 V</p>
<p>(i) I<sub>L</sub> = V<sub>Z</sub> / R<sub>L</sub> = 10 / 1000 = <b>10 mA</b></p>
<p>(ii) I = (V<sub>in</sub> − V<sub>Z</sub>) / R<sub>S</sub> = (15 − 10) / 250 = <b>20 mA</b></p>
<p>(iii) I<sub>Z</sub> = I − I<sub>L</sub> = 20 − 10 = <b>10 mA</b></p>
<p>(iv) P<sub>Z</sub> = V<sub>Z</sub> × I<sub>Z</sub> = 10 × 10 × 10⁻³ = <b>100 mW</b></p>""",
      """<p>V<sub>out</sub> = V<sub>Z</sub> = 10 V</p>
<p>(i) I<sub>L</sub> = V<sub>Z</sub> / R<sub>L</sub> = 10 / 1000 = <b>10 mA</b></p>
<p>(ii) I = (V<sub>in</sub> − V<sub>Z</sub>) / R<sub>S</sub> = (15 − 10) / 250 = <b>20 mA</b></p>
<p>(iii) I<sub>Z</sub> = I − I<sub>L</sub> = 20 − 10 = <b>10 mA</b></p>
<p>(iv) P<sub>Z</sub> = V<sub>Z</sub> × I<sub>Z</sub> = 10 × 10 × 10⁻³ = <b>100 mW</b></p>"""),
    N("u3n4",
      "Design a Zener regulator to give 5.1 V output from a 12 V supply. Load current = 20 mA and minimum Zener current = 5 mA. Find R_S.",
      "12 V supply માંથી 5.1 V output આપવા Zener regulator ડિઝાઇન કરો. Load current = 20 mA અને ન્યૂનતમ Zener current = 5 mA. R_S શોધો.",
      """<p>R<sub>S</sub> = (V<sub>in</sub> − V<sub>Z</sub>) / (I<sub>Z</sub> + I<sub>L</sub>) = (12 − 5.1) / (5 + 20) × 10⁻³</p>
<p>= 6.9 / 0.025 = <b>276 Ω</b> → use standard <b>270 Ω</b>.</p>
<p>Check with 270 Ω: I = 6.9 / 270 = 25.6 mA → I<sub>Z</sub> = 25.6 − 20 = 5.6 mA (&gt; 5 mA ✓).</p>
<p>Power in R<sub>S</sub> = (6.9)² / 270 ≈ 0.18 W → use a <b>½ W</b> resistor.</p>""",
      """<p>R<sub>S</sub> = (V<sub>in</sub> − V<sub>Z</sub>) / (I<sub>Z</sub> + I<sub>L</sub>) = (12 − 5.1) / (5 + 20) × 10⁻³</p>
<p>= 6.9 / 0.025 = <b>276 Ω</b> → standard <b>270 Ω</b> વાપરો.</p>
<p>270 Ω સાથે ચકાસણી: I = 6.9 / 270 = 25.6 mA → I<sub>Z</sub> = 25.6 − 20 = 5.6 mA (&gt; 5 mA ✓).</p>
<p>R<sub>S</sub> માં power = (6.9)² / 270 ≈ 0.18 W → <b>½ W</b> resistor વાપરો.</p>"""),
    N("u3n5",
      "A 6.2 V Zener diode has a power rating of 0.5 W. Find the maximum Zener current.",
      "6.2 V Zener diode નું power rating 0.5 W છે. મહત્તમ Zener current શોધો.",
      """<p>P<sub>Z</sub> = V<sub>Z</sub> × I<sub>Z(max)</sub></p>
<p>I<sub>Z(max)</sub> = P<sub>Z</sub> / V<sub>Z</sub> = 0.5 / 6.2 = <b>80.6 mA</b></p>""",
      """<p>P<sub>Z</sub> = V<sub>Z</sub> × I<sub>Z(max)</sub></p>
<p>I<sub>Z(max)</sub> = P<sub>Z</sub> / V<sub>Z</sub> = 0.5 / 6.2 = <b>80.6 mA</b></p>"""),
    N("u3n6",
      "A half-wave rectifier is fed from 230 V, 50 Hz mains through a 10:1 step-down transformer. R_L = 1 kΩ. Assuming an ideal diode, find V_m, V_dc, I_dc, V_rms, PIV and output frequency.",
      "Half-wave rectifier ને 230 V, 50 Hz mains થી 10:1 step-down transformer દ્વારા supply મળે છે. R_L = 1 kΩ. Ideal diode માની V_m, V_dc, I_dc, V_rms, PIV અને output frequency શોધો.",
      """<p>Secondary RMS voltage V<sub>s</sub> = 230 / 10 = 23 V</p>
<p>V<sub>m</sub> = √2 × 23 = <b>32.53 V</b></p>
<p>V<sub>dc</sub> = V<sub>m</sub> / π = 32.53 / 3.1416 = <b>10.35 V</b></p>
<p>I<sub>dc</sub> = V<sub>dc</sub> / R<sub>L</sub> = 10.35 / 1000 = <b>10.35 mA</b></p>
<p>V<sub>rms</sub> = V<sub>m</sub> / 2 = <b>16.26 V</b></p>
<p>PIV = V<sub>m</sub> = <b>32.53 V</b></p>
<p>Output frequency = input frequency = <b>50 Hz</b></p>""",
      """<p>Secondary RMS voltage V<sub>s</sub> = 230 / 10 = 23 V</p>
<p>V<sub>m</sub> = √2 × 23 = <b>32.53 V</b></p>
<p>V<sub>dc</sub> = V<sub>m</sub> / π = 32.53 / 3.1416 = <b>10.35 V</b></p>
<p>I<sub>dc</sub> = V<sub>dc</sub> / R<sub>L</sub> = 10.35 / 1000 = <b>10.35 mA</b></p>
<p>V<sub>rms</sub> = V<sub>m</sub> / 2 = <b>16.26 V</b></p>
<p>PIV = V<sub>m</sub> = <b>32.53 V</b></p>
<p>Output frequency = input frequency = <b>50 Hz</b></p>"""),
    N("u3n7",
      "A centre-tapped full-wave rectifier uses a 12-0-12 V (RMS) transformer and R_L = 500 Ω. Assuming ideal diodes, find V_dc, I_dc, PIV and ripple frequency (mains 50 Hz).",
      "Centre-tapped full-wave rectifier માં 12-0-12 V (RMS) transformer અને R_L = 500 Ω છે. Ideal diodes માની V_dc, I_dc, PIV અને ripple frequency શોધો (mains 50 Hz).",
      """<p>Each half of the secondary = 12 V RMS → V<sub>m</sub> = √2 × 12 = <b>16.97 V</b></p>
<p>V<sub>dc</sub> = 2V<sub>m</sub> / π = 2 × 16.97 / 3.1416 = <b>10.80 V</b></p>
<p>I<sub>dc</sub> = 10.80 / 500 = <b>21.6 mA</b></p>
<p>PIV = 2V<sub>m</sub> = <b>33.94 V</b></p>
<p>Ripple frequency = 2f = <b>100 Hz</b></p>""",
      """<p>Secondary નો દરેક અડધો ભાગ = 12 V RMS → V<sub>m</sub> = √2 × 12 = <b>16.97 V</b></p>
<p>V<sub>dc</sub> = 2V<sub>m</sub> / π = 2 × 16.97 / 3.1416 = <b>10.80 V</b></p>
<p>I<sub>dc</sub> = 10.80 / 500 = <b>21.6 mA</b></p>
<p>PIV = 2V<sub>m</sub> = <b>33.94 V</b></p>
<p>Ripple frequency = 2f = <b>100 Hz</b></p>"""),
    N("u3n8",
      "A bridge rectifier is supplied with 12 V RMS from a transformer secondary. R_L = 1 kΩ. Find V_dc (i) with ideal diodes and (ii) with silicon diodes (0.7 V each). Also find PIV.",
      "Bridge rectifier ને transformer secondary થી 12 V RMS મળે છે. R_L = 1 kΩ. (i) Ideal diodes સાથે અને (ii) silicon diodes (દરેક 0.7 V) સાથે V_dc શોધો. PIV પણ શોધો.",
      """<p>V<sub>m</sub> = √2 × 12 = 16.97 V</p>
<p>(i) Ideal: V<sub>dc</sub> = 2V<sub>m</sub>/π = 0.636 × 16.97 = <b>10.80 V</b>, I<sub>dc</sub> = <b>10.8 mA</b></p>
<p>(ii) Two diodes conduct in series → drop = 1.4 V</p>
<p>V<sub>m(out)</sub> = 16.97 − 1.4 = 15.57 V → V<sub>dc</sub> = 0.636 × 15.57 = <b>9.91 V</b></p>
<p>PIV = V<sub>m</sub> ≈ <b>16.97 V</b> (practically V<sub>m</sub> − 0.7 ≈ 16.27 V)</p>""",
      """<p>V<sub>m</sub> = √2 × 12 = 16.97 V</p>
<p>(i) Ideal: V<sub>dc</sub> = 2V<sub>m</sub>/π = 0.636 × 16.97 = <b>10.80 V</b>, I<sub>dc</sub> = <b>10.8 mA</b></p>
<p>(ii) બે diodes series માં conduction કરે → drop = 1.4 V</p>
<p>V<sub>m(out)</sub> = 16.97 − 1.4 = 15.57 V → V<sub>dc</sub> = 0.636 × 15.57 = <b>9.91 V</b></p>
<p>PIV = V<sub>m</sub> ≈ <b>16.97 V</b> (વ્યવહારમાં V<sub>m</sub> − 0.7 ≈ 16.27 V)</p>"""),
    N("u3n9",
      "In a half-wave rectifier the peak load current is 50 mA. Find I_dc, I_rms and the ripple factor.",
      "Half-wave rectifier માં peak load current 50 mA છે. I_dc, I_rms અને ripple factor શોધો.",
      """<p>I<sub>dc</sub> = I<sub>m</sub> / π = 50 / 3.1416 = <b>15.92 mA</b></p>
<p>I<sub>rms</sub> = I<sub>m</sub> / 2 = <b>25 mA</b></p>
<p>r = √[(I<sub>rms</sub> / I<sub>dc</sub>)² − 1] = √[(25 / 15.92)² − 1] = √(2.467 − 1) = √1.467 = <b>1.21</b></p>
<p><i>This confirms the standard HWR ripple factor of 1.21.</i></p>""",
      """<p>I<sub>dc</sub> = I<sub>m</sub> / π = 50 / 3.1416 = <b>15.92 mA</b></p>
<p>I<sub>rms</sub> = I<sub>m</sub> / 2 = <b>25 mA</b></p>
<p>r = √[(I<sub>rms</sub> / I<sub>dc</sub>)² − 1] = √[(25 / 15.92)² − 1] = √(2.467 − 1) = √1.467 = <b>1.21</b></p>
<p><i>આ HWR ના standard ripple factor 1.21 ને ચકાસે છે.</i></p>"""),
]


def E(name_en, name_gu, f, terms_en, terms_gu):
    return {"name": {"en": name_en, "gu": name_gu}, "f": f, "terms": {"en": terms_en, "gu": terms_gu}}


EQUATIONS = [
    {"title": {"en": "P-N Junction Diode", "gu": "P-N Junction Diode"}, "items": [
        E("Barrier potential / knee voltage", "Barrier potential / knee voltage", "V<sub>K</sub> ≈ 0.7 V (Si), 0.3 V (Ge)",
          "Decreases ≈ 2 mV per °C rise", "દર °C વધારે ≈ 2 mV ઘટે"),
        E("Diode current equation", "Diode current equation", "I = I₀ (e<sup>V/ηV<sub>T</sub></sup> − 1)",
          "I₀ = reverse saturation current, V_T ≈ 26 mV at 300 K, η = 1 (Ge), 2 (Si)",
          "I₀ = reverse saturation current, 300 K પર V_T ≈ 26 mV, η = 1 (Ge), 2 (Si)"),
        E("Static (DC) resistance", "Static (DC) resistance", "R<sub>DC</sub> = V<sub>F</sub> / I<sub>F</sub>",
          "At an operating point", "કોઈ operating point પર"),
        E("Dynamic (AC) resistance", "Dynamic (AC) resistance", "r<sub>d</sub> = ΔV<sub>F</sub> / ΔI<sub>F</sub> ≈ 26 mV / I<sub>F</sub>",
          "Above the knee; few ohms", "Knee થી ઉપર; થોડા ohms"),
        E("Diode power dissipation", "Diode power dissipation", "P<sub>D</sub> = V<sub>F</sub> × I<sub>F</sub>",
          "Must be below rated value", "Rated મૂલ્ય કરતાં ઓછું હોવું જોઈએ"),
    ]},
    {"title": {"en": "Zener and Special Diodes", "gu": "Zener અને Special Diodes"}, "items": [
        E("Zener power rating", "Zener power rating", "P<sub>Z</sub> = V<sub>Z</sub> × I<sub>Z(max)</sub>",
          "Gives maximum safe Zener current", "મહત્તમ સુરક્ષિત Zener current આપે"),
        E("Regulator currents", "Regulator currents", "I = I<sub>Z</sub> + I<sub>L</sub>",
          "I = current through R_S, I_L = V_Z / R_L", "I = R_S માંથી current, I_L = V_Z / R_L"),
        E("Series current", "Series current", "I = (V<sub>in</sub> − V<sub>Z</sub>) / R<sub>S</sub>",
          "Output V_out = V_Z", "Output V_out = V_Z"),
        E("Series resistor design", "Series resistor design", "R<sub>S</sub> = (V<sub>in</sub> − V<sub>Z</sub>) / (I<sub>Z</sub> + I<sub>L</sub>)",
          "Keep I_Z between I_Z(min) and I_Z(max)", "I_Z ને I_Z(min) અને I_Z(max) વચ્ચે રાખો"),
        E("Zener resistance", "Zener resistance", "r<sub>Z</sub> = ΔV<sub>Z</sub> / ΔI<sub>Z</sub>",
          "Very small (ideal = 0)", "ખૂબ ઓછો (ideal = 0)"),
        E("Varactor capacitance", "Varactor capacitance", "C<sub>T</sub> = εA / W,  C<sub>T</sub> ∝ 1 / √V<sub>R</sub>",
          "W = depletion width, increases with V_R", "W = depletion width, V_R સાથે વધે"),
        E("LED series resistor", "LED series resistor", "R = (V<sub>S</sub> − V<sub>F</sub>) / I<sub>F</sub>",
          "V_F = 1.8–3.3 V, I_F = 10–20 mA", "V_F = 1.8–3.3 V, I_F = 10–20 mA"),
    ]},
    {"title": {"en": "Rectifiers", "gu": "Rectifiers"}, "items": [
        E("Peak voltage from RMS", "RMS થી Peak voltage", "V<sub>m</sub> = √2 × V<sub>rms</sub>",
          "Secondary peak voltage", "Secondary નો peak voltage"),
        E("Peak load current", "Peak load current", "I<sub>m</sub> = V<sub>m</sub> / (r<sub>f</sub> + R<sub>L</sub>)",
          "r_f = diode forward resistance", "r_f = diode forward resistance"),
        E("Ripple factor (general)", "Ripple factor (સામાન્ય)", "r = √[(I<sub>rms</sub> / I<sub>dc</sub>)² − 1]",
          "Lower is better", "જેટલું ઓછું એટલું સારું"),
        E("Efficiency (general)", "Efficiency (સામાન્ય)", "η = P<sub>dc</sub> / P<sub>ac</sub> = I<sub>dc</sub>²R<sub>L</sub> / I<sub>rms</sub>²(r<sub>f</sub> + R<sub>L</sub>)",
          "Higher is better", "જેટલું વધુ એટલું સારું"),
        E("Half-wave: DC values", "Half-wave: DC મૂલ્યો", "V<sub>dc</sub> = V<sub>m</sub>/π,  I<sub>dc</sub> = I<sub>m</sub>/π",
          "0.318 × peak", "0.318 × peak"),
        E("Half-wave: RMS and figures", "Half-wave: RMS અને આંકડા", "I<sub>rms</sub> = I<sub>m</sub>/2;  r = 1.21;  η = 40.6%;  PIV = V<sub>m</sub>",
          "Output frequency = f; TUF = 0.287", "Output frequency = f; TUF = 0.287"),
        E("Full-wave: DC values", "Full-wave: DC મૂલ્યો", "V<sub>dc</sub> = 2V<sub>m</sub>/π,  I<sub>dc</sub> = 2I<sub>m</sub>/π",
          "0.636 × peak (CT and bridge)", "0.636 × peak (CT અને bridge)"),
        E("Full-wave: RMS and figures", "Full-wave: RMS અને આંકડા", "I<sub>rms</sub> = I<sub>m</sub>/√2;  r = 0.482;  η = 81.2%",
          "Output frequency = 2f", "Output frequency = 2f"),
        E("PIV: centre-tap vs bridge", "PIV: centre-tap અને bridge", "PIV<sub>CT</sub> = 2V<sub>m</sub>,  PIV<sub>bridge</sub> = V<sub>m</sub>",
          "TUF: CT 0.693, bridge 0.812", "TUF: CT 0.693, bridge 0.812"),
        E("Bridge with Si diodes", "Si diodes સાથે bridge", "V<sub>dc</sub> = 2(V<sub>m</sub> − 1.4)/π",
          "Two diodes conduct in series", "બે diodes series માં conduction કરે"),
    ]},
]


def V(q_en, q_gu, a_en, a_gu):
    return {"q": {"en": q_en, "gu": q_gu}, "a": {"en": a_en, "gu": a_gu}}


VIVA = [
    {"title": {"en": "P-N Junction and Biasing", "gu": "P-N Junction અને Biasing"}, "items": [
        V("What is a P-N junction?", "P-N junction એટલે શું?",
          "The boundary formed when P-type and N-type semiconductors are joined in a single crystal.",
          "એક જ crystal માં P-type અને N-type semiconductor જોડાય ત્યારે બનતી સીમા."),
        V("What is depletion layer?", "Depletion layer એટલે શું?",
          "The region near the junction that has no free charge carriers, only immobile ions.",
          "Junction નજીકનો વિસ્તાર જેમાં free charge carriers નથી, ફક્ત immobile ions છે."),
        V("What is the barrier potential of Si and Ge?", "Si અને Ge નો barrier potential કેટલો છે?",
          "Si ≈ 0.7 V and Ge ≈ 0.3 V.", "Si ≈ 0.7 V અને Ge ≈ 0.3 V."),
        V("What is knee voltage?", "Knee voltage એટલે શું?",
          "The forward voltage at which diode current starts increasing rapidly.",
          "જે forward voltage પર diode current ઝડપથી વધવા લાગે."),
        V("What is biasing?", "Biasing એટલે શું?",
          "Applying an external DC voltage to set the operating condition of a device.",
          "Device ની કાર્ય સ્થિતિ નક્કી કરવા બાહ્ય DC voltage લગાવવો."),
        V("What happens to the depletion layer in forward bias?", "Forward bias માં depletion layer નું શું થાય?",
          "It becomes narrow.", "તે સાંકડું થાય છે."),
        V("What happens to the depletion layer in reverse bias?", "Reverse bias માં depletion layer નું શું થાય?",
          "It becomes wide.", "તે પહોળું થાય છે."),
        V("Why does a small current flow in reverse bias?", "Reverse bias માં નાનો current કેમ વહે છે?",
          "Due to thermally generated minority carriers (reverse saturation current).",
          "ઉષ્માથી બનેલા minority carriers ને કારણે (reverse saturation current)."),
        V("How is the cathode of a diode identified?", "Diode નો cathode કેવી રીતે ઓળખાય?",
          "By the silver/white band printed on the body.", "Body પર છાપેલા silver/સફેદ band થી."),
        V("What is PIV?", "PIV એટલે શું?",
          "Peak Inverse Voltage – the maximum reverse voltage a diode can withstand without breakdown.",
          "Peak Inverse Voltage – breakdown વિના diode સહન કરી શકે તેવો મહત્તમ reverse voltage."),
        V("What is the effect of temperature on reverse saturation current?", "Reverse saturation current પર તાપમાનની અસર શું છે?",
          "It approximately doubles for every 10 °C rise.", "દર 10 °C વધારે તે લગભગ બમણો થાય છે."),
    ]},
    {"title": {"en": "Zener and Special Diodes", "gu": "Zener અને Special Diodes"}, "items": [
        V("What is a Zener diode?", "Zener diode એટલે શું?",
          "A heavily doped Si diode designed to operate in reverse breakdown, keeping voltage constant.",
          "Reverse breakdown માં કામ કરી voltage અચળ રાખવા બનાવેલો વધુ doped Si diode."),
        V("In which bias is a Zener used as a regulator?", "Regulator તરીકે Zener કયા bias માં વપરાય?",
          "Reverse bias.", "Reverse bias."),
        V("Difference between Zener and avalanche breakdown?", "Zener અને avalanche breakdown વચ્ચે તફાવત?",
          "Zener: heavy doping, below 5 V, field breaks bonds. Avalanche: light doping, above 6 V, collision (impact ionisation).",
          "Zener: વધુ doping, 5 V થી નીચે, field bonds તોડે. Avalanche: ઓછું doping, 6 V થી ઉપર, અથડામણ (impact ionisation)."),
        V("Why is a series resistor used with a Zener?", "Zener સાથે series resistor કેમ વપરાય?",
          "To limit the current below I_Z(max) and to drop the extra voltage.",
          "Current ને I_Z(max) થી નીચે રાખવા અને વધારાનો voltage drop કરવા."),
        V("What is a varactor diode?", "Varactor diode એટલે શું?",
          "A reverse-biased diode used as a voltage-controlled variable capacitor.",
          "Voltage-controlled variable capacitor તરીકે વપરાતો reverse-biased diode."),
        V("What happens to varactor capacitance when reverse voltage increases?", "Reverse voltage વધે ત્યારે varactor capacitance નું શું થાય?",
          "It decreases, because the depletion width increases.", "તે ઘટે છે, કારણ કે depletion width વધે છે."),
        V("In which bias is a photodiode operated?", "Photodiode કયા bias માં ચલાવાય?",
          "Reverse bias.", "Reverse bias."),
        V("What is dark current?", "Dark current એટલે શું?",
          "The small reverse current of a photodiode when no light falls on it.",
          "Photodiode પર પ્રકાશ ન પડે ત્યારે વહેતો નાનો reverse current."),
        V("Why is Si not used for LEDs?", "LED માટે Si કેમ વપરાતું નથી?",
          "Si has an indirect band gap; energy is released mostly as heat, not light.",
          "Si માં indirect band gap છે; ઊર્જા મુખ્યત્વે પ્રકાશ નહીં પરંતુ ઉષ્મા તરીકે છૂટે છે."),
        V("Which material gives a blue LED?", "વાદળી LED કયા material થી બને?",
          "InGaN (Indium Gallium Nitride).", "InGaN (Indium Gallium Nitride)."),
        V("How do you identify the anode of an LED?", "LED નો anode કેવી રીતે ઓળખાય?",
          "The longer leg is the anode; the flat edge marks the cathode.",
          "લાંબો પગ anode છે; સપાટ ધાર cathode દર્શાવે છે."),
        V("How many leads does an RGB LED have?", "RGB LED માં કેટલા leads હોય?",
          "Four – R, G, B and one common (anode or cathode).", "ચાર – R, G, B અને એક common (anode અથવા cathode)."),
    ]},
    {"title": {"en": "Rectifiers", "gu": "Rectifiers"}, "items": [
        V("What is a rectifier?", "Rectifier એટલે શું?",
          "A circuit that converts AC into pulsating DC.", "AC ને pulsating DC માં ફેરવતો circuit."),
        V("What is ripple factor?", "Ripple factor એટલે શું?",
          "Ratio of RMS value of AC component to DC value of the output.", "Output ના AC ઘટકના RMS મૂલ્ય અને DC મૂલ્યનો ગુણોત્તર."),
        V("Ripple factor of half-wave and full-wave rectifiers?", "Half-wave અને full-wave rectifier નો ripple factor?",
          "HWR = 1.21, FWR = 0.482.", "HWR = 1.21, FWR = 0.482."),
        V("Maximum efficiency of HWR and FWR?", "HWR અને FWR ની મહત્તમ efficiency?",
          "HWR = 40.6%, FWR = 81.2%.", "HWR = 40.6%, FWR = 81.2%."),
        V("PIV of a centre-tap rectifier diode?", "Centre-tap rectifier ના diode નો PIV?",
          "2V_m.", "2V_m."),
        V("PIV of a bridge rectifier diode?", "Bridge rectifier ના diode નો PIV?",
          "V_m.", "V_m."),
        V("Output frequency of a full-wave rectifier with 50 Hz input?", "50 Hz input સાથે full-wave rectifier ની output frequency?",
          "100 Hz.", "100 Hz."),
        V("Why is the bridge rectifier most popular?", "Bridge rectifier સૌથી લોકપ્રિય કેમ છે?",
          "No centre tap needed, low PIV (V_m), highest TUF (0.812).", "Centre tap જરૂરી નથી, ઓછો PIV (V_m), સૌથી વધુ TUF (0.812)."),
        V("How many diodes conduct at a time in a bridge rectifier?", "Bridge rectifier માં એક સમયે કેટલા diodes conduction કરે?",
          "Two (in series).", "બે (series માં)."),
        V("What is the purpose of a filter after a rectifier?", "Rectifier પછી filter નો હેતુ શું છે?",
          "To remove ripples and make the DC smooth.", "Ripples દૂર કરી DC ને સરળ બનાવવું."),
    ]},
]


def X(q_en, q_gu, marks):
    return {"q": {"en": q_en, "gu": q_gu}, "marks": marks}


EXAM_QS = [
    X("Explain the formation of depletion layer in a P-N junction.", "P-N junction માં depletion layer ની રચના સમજાવો.", 3),
    X("Define: (i) Barrier potential (ii) Knee voltage (iii) PIV.", "વ્યાખ્યા આપો: (i) Barrier potential (ii) Knee voltage (iii) PIV.", 3),
    X("Explain forward and reverse biasing of a P-N junction diode with neat diagrams.", "સ્વચ્છ આકૃતિ સાથે P-N junction diode નું forward અને reverse biasing સમજાવો.", 4),
    X("Draw and explain the V-I characteristics of a P-N junction diode.", "P-N junction diode ની V-I characteristics દોરો અને સમજાવો.", 4),
    X("Compare forward bias and reverse bias.", "Forward bias અને reverse bias ની સરખામણી કરો.", 3),
    X("Explain the working of Zener diode and draw its V-I characteristics.", "Zener diode નું કાર્ય સમજાવો અને તેની V-I characteristics દોરો.", 4),
    X("Differentiate between Zener breakdown and avalanche breakdown.", "Zener breakdown અને avalanche breakdown વચ્ચે તફાવત લખો.", 3),
    X("Explain Zener diode as a voltage regulator with circuit diagram.", "Circuit diagram સાથે voltage regulator તરીકે Zener diode સમજાવો.", 4),
    X("Compare P-N junction diode and Zener diode.", "P-N junction diode અને Zener diode ની સરખામણી કરો.", 3),
    X("Explain the construction and working of LED. List its applications.", "LED ની રચના અને કાર્ય સમજાવો. તેના ઉપયોગો લખો.", 4),
    X("Explain photodiode with symbol, working and characteristics.", "Symbol, કાર્ય અને characteristics સાથે photodiode સમજાવો.", 4),
    X("Explain varactor diode and state its applications.", "Varactor diode સમજાવો અને તેના ઉપયોગો લખો.", 3),
    X("Write a short note on multicolour LED.", "Multicolour LED પર ટૂંક નોંધ લખો.", 3),
    X("What is a rectifier? State its need and types.", "Rectifier એટલે શું? તેની જરૂરિયાત અને પ્રકારો લખો.", 3),
    X("Explain half-wave rectifier with circuit diagram and waveforms.", "Circuit diagram અને waveforms સાથે half-wave rectifier સમજાવો.", 4),
    X("Explain centre-tapped full-wave rectifier with circuit diagram and waveforms.", "Circuit diagram અને waveforms સાથે centre-tapped full-wave rectifier સમજાવો.", 4),
    X("Explain full-wave bridge rectifier with circuit diagram and waveforms. State its advantages.", "Circuit diagram અને waveforms સાથે full-wave bridge rectifier સમજાવો. તેના ફાયદા લખો.", 7),
    X("Compare half-wave, centre-tap and bridge rectifiers.", "Half-wave, centre-tap અને bridge rectifiers ની સરખામણી કરો.", 4),
    X("Explain Zener diode with its V-I characteristics and use as a voltage regulator.", "V-I characteristics અને voltage regulator તરીકે ઉપયોગ સાથે Zener diode સમજાવો.", 7),
]
