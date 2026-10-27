"""Basics of Electronics (DI01000151) - Unit 1: solved numericals, equations, viva, exam questions"""
from content_DI01000151_u1_notes_a import Q

SEC_NUMERICALS = {
    "title": {"en": "Solved Numericals", "gu": "ઉકેલેલા દાખલા"},
    "items": [
        Q("Find the value and range of a resistor with colour bands Red – Red – Brown – Gold.",
          "રંગીન પટ્ટા લાલ – લાલ – બદામી – સોનેરી ધરાવતા રેઝિસ્ટરનું મૂલ્ય અને રેન્જ શોધો.",
          """<p><b>Given:</b> Red = 2, Red = 2, Brown = × 10, Gold = ± 5%</p>
<p>R = 22 × 10 = <b>220 Ω ± 5%</b></p>
<p>Tolerance = 5% × 220 = 11 Ω</p>
<p>R<sub>min</sub> = 220 − 11 = <b>209 Ω</b>, R<sub>max</sub> = 220 + 11 = <b>231 Ω</b></p>""",
          """<p><b>આપેલ:</b> લાલ = 2, લાલ = 2, બદામી = × 10, સોનેરી = ± 5%</p>
<p>R = 22 × 10 = <b>220 Ω ± 5%</b></p>
<p>ટોલરન્સ = 220 ના 5% = 11 Ω</p>
<p>R<sub>min</sub> = 220 − 11 = <b>209 Ω</b>, R<sub>max</sub> = 220 + 11 = <b>231 Ω</b></p>"""),
        Q("Find the value of a resistor with colour bands Green – Blue – Yellow – Silver.",
          "લીલો – વાદળી – પીળો – રૂપેરી પટ્ટા ધરાવતા રેઝિસ્ટરનું મૂલ્ય શોધો.",
          """<p><b>Given:</b> Green = 5, Blue = 6, Yellow = × 10⁴, Silver = ± 10%</p>
<p>R = 56 × 10⁴ = 560000 Ω = <b>560 kΩ ± 10%</b></p>
<p>Tolerance = 10% × 560 kΩ = 56 kΩ → Range: <b>504 kΩ to 616 kΩ</b></p>""",
          """<p><b>આપેલ:</b> લીલો = 5, વાદળી = 6, પીળો = × 10⁴, રૂપેરી = ± 10%</p>
<p>R = 56 × 10⁴ = 560000 Ω = <b>560 kΩ ± 10%</b></p>
<p>ટોલરન્સ = 560 kΩ ના 10% = 56 kΩ → રેન્જ: <b>504 kΩ થી 616 kΩ</b></p>"""),
        Q("Write the colour bands for a 1 kΩ ± 5% resistor.",
          "1 kΩ ± 5% રેઝિસ્ટર માટે રંગીન પટ્ટા લખો.",
          """<p>1 kΩ = 1000 Ω = <b>10 × 10²</b></p>
<p>1 → Brown, 0 → Black, 10² → Red, ±5% → Gold</p>
<p>Colour bands: <b>Brown – Black – Red – Gold</b></p>""",
          """<p>1 kΩ = 1000 Ω = <b>10 × 10²</b></p>
<p>1 → બદામી, 0 → કાળો, 10² → લાલ, ±5% → સોનેરી</p>
<p>રંગીન પટ્ટા: <b>બદામી – કાળો – લાલ – સોનેરી</b></p>"""),
        Q("A 100 μF capacitor is charged to 12 V. Find the charge stored and the energy stored.",
          "100 μF કેપેસિટરને 12 V સુધી ચાર્જ કરેલ છે. સંગ્રહિત ચાર્જ અને ઊર્જા શોધો.",
          """<p><b>Given:</b> C = 100 μF = 100 × 10⁻⁶ F, V = 12 V</p>
<p>Charge Q = C × V = 100 × 10⁻⁶ × 12 = <b>1.2 × 10⁻³ C (1.2 mC)</b></p>
<p>Energy E = ½ C V² = ½ × 100 × 10⁻⁶ × 12² = ½ × 100 × 10⁻⁶ × 144 = <b>7.2 × 10⁻³ J (7.2 mJ)</b></p>""",
          """<p><b>આપેલ:</b> C = 100 μF = 100 × 10⁻⁶ F, V = 12 V</p>
<p>ચાર્જ Q = C × V = 100 × 10⁻⁶ × 12 = <b>1.2 × 10⁻³ C (1.2 mC)</b></p>
<p>ઊર્જા E = ½ C V² = ½ × 100 × 10⁻⁶ × 12² = ½ × 100 × 10⁻⁶ × 144 = <b>7.2 × 10⁻³ J (7.2 mJ)</b></p>"""),
        Q("Find the value of a ceramic capacitor marked 473.",
          "473 લખેલા સિરામિક કેપેસિટરનું મૂલ્ય શોધો.",
          """<p>473 → 47 × 10³ pF = 47000 pF</p>
<p>= 47 nF = <b>0.047 μF</b></p>""",
          """<p>473 → 47 × 10³ pF = 47000 pF</p>
<p>= 47 nF = <b>0.047 μF</b></p>"""),
        Q("The current in a 0.5 H coil changes from 0 to 2 A in 0.1 s. Find the induced EMF.",
          "0.5 H ની કોઇલમાં કરંટ 0.1 s માં 0 થી 2 A બદલાય છે. પ્રેરિત EMF શોધો.",
          """<p><b>Given:</b> L = 0.5 H, di = 2 − 0 = 2 A, dt = 0.1 s</p>
<p>|e| = L × (di / dt) = 0.5 × (2 / 0.1) = 0.5 × 20 = <b>10 V</b></p>
<p>(The negative sign in e = −L di/dt only shows that the EMF opposes the change in current.)</p>""",
          """<p><b>આપેલ:</b> L = 0.5 H, di = 2 − 0 = 2 A, dt = 0.1 s</p>
<p>|e| = L × (di / dt) = 0.5 × (2 / 0.1) = 0.5 × 20 = <b>10 V</b></p>
<p>(e = −L di/dt માં માઇનસ ચિહ્ન માત્ર એટલું દર્શાવે છે કે EMF કરંટના ફેરફારનો વિરોધ કરે છે.)</p>"""),
        Q("Two coils of 4 mH and 9 mH have a coefficient of coupling 0.5. Find the mutual inductance.",
          "4 mH અને 9 mH ની બે કોઇલનો કપલિંગ ગુણાંક 0.5 છે. મ્યુચ્યુઅલ ઇન્ડક્ટન્સ શોધો.",
          """<p><b>Given:</b> L₁ = 4 mH, L₂ = 9 mH, k = 0.5</p>
<p>M = k √(L₁ L₂) = 0.5 × √(4 × 9) = 0.5 × √36 = 0.5 × 6 = <b>3 mH</b></p>""",
          """<p><b>આપેલ:</b> L₁ = 4 mH, L₂ = 9 mH, k = 0.5</p>
<p>M = k √(L₁ L₂) = 0.5 × √(4 × 9) = 0.5 × √36 = 0.5 × 6 = <b>3 mH</b></p>"""),
        Q("Find the reactance of (i) a 10 μF capacitor and (ii) a 0.1 H inductor at 50 Hz.",
          "50 Hz પર (i) 10 μF કેપેસિટર અને (ii) 0.1 H ઇન્ડક્ટરનો રિએક્ટન્સ શોધો.",
          """<p><b>(i)</b> X<sub>C</sub> = 1 / (2πfC) = 1 / (2 × 3.1416 × 50 × 10 × 10⁻⁶) = 1 / 0.0031416 = <b>318.3 Ω</b></p>
<p><b>(ii)</b> X<sub>L</sub> = 2πfL = 2 × 3.1416 × 50 × 0.1 = <b>31.42 Ω</b></p>""",
          """<p><b>(i)</b> X<sub>C</sub> = 1 / (2πfC) = 1 / (2 × 3.1416 × 50 × 10 × 10⁻⁶) = 1 / 0.0031416 = <b>318.3 Ω</b></p>
<p><b>(ii)</b> X<sub>L</sub> = 2πfL = 2 × 3.1416 × 50 × 0.1 = <b>31.42 Ω</b></p>"""),
    ],
}


def E(name_en, name_gu, f, terms_en, terms_gu):
    return {"name": {"en": name_en, "gu": name_gu}, "f": f, "terms": {"en": terms_en, "gu": terms_gu}}


EQUATIONS = [
    {"title": {"en": "Resistor", "gu": "રેઝિસ્ટર"}, "items": [
        E("Ohm's Law", "ઓહ્મનો નિયમ", "V = I × R",
          "V = voltage (V), I = current (A), R = resistance (Ω)",
          "V = વોલ્ટેજ (V), I = કરંટ (A), R = અવરોધ (Ω)"),
        E("Resistance of a conductor", "વાહકનો અવરોધ", "R = ρ L / A",
          "ρ = resistivity (Ω·m), L = length (m), A = area of cross-section (m²)",
          "ρ = અવરોધકતા (Ω·m), L = લંબાઈ (m), A = આડછેદનું ક્ષેત્રફળ (m²)"),
        E("Electrical power", "વિદ્યુત પાવર", "P = V × I = I² R = V² / R",
          "P = power (W). Use it to choose the wattage of a resistor.",
          "P = પાવર (W). રેઝિસ્ટરનું વોટેજ પસંદ કરવા વપરાય."),
        E("Resistors in series", "શ્રેણી જોડાણમાં રેઝિસ્ટર", "R<sub>eq</sub> = R<sub>1</sub> + R<sub>2</sub> + R<sub>3</sub> + …",
          "Same current flows through all; total resistance increases.",
          "બધામાંથી સમાન કરંટ વહે; કુલ અવરોધ વધે."),
        E("Resistors in parallel", "સમાંતર જોડાણમાં રેઝિસ્ટર", "1 / R<sub>eq</sub> = 1 / R<sub>1</sub> + 1 / R<sub>2</sub> + …",
          "Same voltage across all; total resistance is less than the smallest resistor. For two: R<sub>eq</sub> = R<sub>1</sub>R<sub>2</sub> / (R<sub>1</sub> + R<sub>2</sub>)",
          "બધા પર સમાન વોલ્ટેજ; કુલ અવરોધ સૌથી નાના રેઝિસ્ટર કરતાં ઓછો. બે માટે: R<sub>eq</sub> = R<sub>1</sub>R<sub>2</sub> / (R<sub>1</sub> + R<sub>2</sub>)"),
        E("Tolerance range", "ટોલરન્સ રેન્જ", "R<sub>min/max</sub> = R ∓ (Tol% × R)",
          "e.g. 1 kΩ ± 5% → 950 Ω to 1050 Ω",
          "દા.ત. 1 kΩ ± 5% → 950 Ω થી 1050 Ω"),
    ]},
    {"title": {"en": "Capacitor", "gu": "કેપેસિટર"}, "items": [
        E("Capacitance", "કેપેસિટન્સ", "C = Q / V",
          "C = capacitance (F), Q = charge (C), V = voltage (V)",
          "C = કેપેસિટન્સ (F), Q = ચાર્જ (C), V = વોલ્ટેજ (V)"),
        E("Parallel plate capacitor", "સમાંતર પ્લેટ કેપેસિટર", "C = ε<sub>0</sub> ε<sub>r</sub> A / d",
          "ε₀ = 8.854 × 10⁻¹² F/m, εᵣ = dielectric constant, A = plate area (m²), d = distance between plates (m)",
          "ε₀ = 8.854 × 10⁻¹² F/m, εᵣ = ડાઇઇલેક્ટ્રિક અચળાંક, A = પ્લેટનું ક્ષેત્રફળ (m²), d = પ્લેટો વચ્ચેનું અંતર (m)"),
        E("Energy stored in capacitor", "કેપેસિટરમાં સંગ્રહિત ઊર્જા", "E = ½ C V²",
          "E = energy (J)", "E = ઊર્જા (J)"),
        E("Capacitive reactance", "કેપેસિટિવ રિએક્ટન્સ", "X<sub>C</sub> = 1 / (2π f C)",
          "f = frequency (Hz). X<sub>C</sub> decreases as frequency increases; for DC (f = 0), X<sub>C</sub> = ∞.",
          "f = ફ્રિક્વન્સી (Hz). ફ્રિક્વન્સી વધે તેમ X<sub>C</sub> ઘટે; DC (f = 0) માટે X<sub>C</sub> = ∞."),
        E("Capacitors in parallel", "સમાંતર જોડાણમાં કેપેસિટર", "C<sub>eq</sub> = C<sub>1</sub> + C<sub>2</sub> + …",
          "Total capacitance increases (opposite of resistors).",
          "કુલ કેપેસિટન્સ વધે (રેઝિસ્ટરથી ઊલટું)."),
        E("Capacitors in series", "શ્રેણી જોડાણમાં કેપેસિટર", "1 / C<sub>eq</sub> = 1 / C<sub>1</sub> + 1 / C<sub>2</sub> + …",
          "Total capacitance decreases.", "કુલ કેપેસિટન્સ ઘટે."),
    ]},
    {"title": {"en": "Inductor", "gu": "ઇન્ડક્ટર"}, "items": [
        E("Inductance of a coil", "કોઇલનું ઇન્ડક્ટન્સ", "L = μ<sub>0</sub> μ<sub>r</sub> N² A / l",
          "μ₀ = 4π × 10⁻⁷ H/m, μᵣ = relative permeability, N = turns, A = core area (m²), l = length (m)",
          "μ₀ = 4π × 10⁻⁷ H/m, μᵣ = સાપેક્ષ પરમિએબિલિટી, N = આંટા, A = કોરનું ક્ષેત્રફળ (m²), l = લંબાઈ (m)"),
        E("Faraday's law", "ફેરાડેનો નિયમ", "e = − N dΦ / dt",
          "e = induced EMF (V), N = turns, dΦ/dt = rate of change of flux (Wb/s). Minus sign = Lenz's law.",
          "e = પ્રેરિત EMF (V), N = આંટા, dΦ/dt = ફ્લક્સ ફેરફારનો દર (Wb/s). માઇનસ ચિહ્ન = લેન્ઝનો નિયમ."),
        E("Self-induced EMF", "સ્વ-પ્રેરિત EMF", "e = − L di / dt",
          "L = self-inductance (H), di/dt = rate of change of current (A/s)",
          "L = સેલ્ફ-ઇન્ડક્ટન્સ (H), di/dt = કરંટ ફેરફારનો દર (A/s)"),
        E("Self-inductance", "સેલ્ફ-ઇન્ડક્ટન્સ", "L = N Φ / I",
          "Φ = flux (Wb), I = current (A)", "Φ = ફ્લક્સ (Wb), I = કરંટ (A)"),
        E("Mutually induced EMF", "પરસ્પર પ્રેરિત EMF", "e<sub>2</sub> = − M di<sub>1</sub> / dt",
          "M = mutual inductance (H), di₁/dt = rate of change of primary current",
          "M = મ્યુચ્યુઅલ ઇન્ડક્ટન્સ (H), di₁/dt = પ્રાઇમરી કરંટ ફેરફારનો દર"),
        E("Mutual inductance", "મ્યુચ્યુઅલ ઇન્ડક્ટન્સ", "M = k √(L<sub>1</sub> L<sub>2</sub>)",
          "k = coefficient of coupling (0 to 1)", "k = કપલિંગ ગુણાંક (0 થી 1)"),
        E("Energy stored in inductor", "ઇન્ડક્ટરમાં સંગ્રહિત ઊર્જા", "E = ½ L I²",
          "E = energy (J)", "E = ઊર્જા (J)"),
        E("Inductive reactance", "ઇન્ડક્ટિવ રિએક્ટન્સ", "X<sub>L</sub> = 2π f L",
          "X<sub>L</sub> increases with frequency; for DC (f = 0), X<sub>L</sub> = 0.",
          "ફ્રિક્વન્સી વધે તેમ X<sub>L</sub> વધે; DC (f = 0) માટે X<sub>L</sub> = 0."),
        E("Quality factor", "ક્વોલિટી ફેક્ટર", "Q = X<sub>L</sub> / R = 2π f L / R",
          "R = resistance of winding (Ω). Higher Q = lower losses.",
          "R = વાઇન્ડિંગનો અવરોધ (Ω). વધુ Q = ઓછા લોસ."),
    ]},
]


def V(q_en, q_gu, a_en, a_gu):
    return {"q": {"en": q_en, "gu": q_gu}, "a": {"en": a_en, "gu": a_gu}}


VIVA = [
    {"title": {"en": "Components & Resistors", "gu": "ઘટકો અને રેઝિસ્ટર"}, "items": [
        V("What is an active component?", "એક્ટિવ ઘટક એટલે શું?",
          "A component that can amplify a signal or control current, e.g. transistor, diode, IC.",
          "જે ઘટક સિગ્નલ એમ્પ્લિફાય કરી શકે કે કરંટ નિયંત્રિત કરી શકે, દા.ત. ટ્રાન્ઝિસ્ટર, ડાયોડ, IC."),
        V("What is a passive component?", "પેસિવ ઘટક એટલે શું?",
          "A component that cannot amplify; it only consumes, stores or releases energy, e.g. R, L, C.",
          "જે ઘટક એમ્પ્લિફાય ન કરી શકે; માત્ર ઊર્જાનો વપરાશ, સંગ્રહ કે મુક્ત કરે, દા.ત. R, L, C."),
        V("Who invented the transistor and when?", "ટ્રાન્ઝિસ્ટરની શોધ કોણે અને ક્યારે કરી?",
          "Bardeen, Brattain and Shockley at Bell Labs in 1947.",
          "બાર્ડીન, બ્રેટન અને શોકલીએ 1947 માં બેલ લેબમાં."),
        V("What is the unit of resistance?", "અવરોધનો એકમ શું છે?", "Ohm (Ω).", "ઓહ્મ (Ω)."),
        V("What is the tolerance of gold and silver bands?", "સોનેરી અને રૂપેરી પટ્ટાનું ટોલરન્સ કેટલું?",
          "Gold = ±5%, Silver = ±10% (no band = ±20%).",
          "સોનેરી = ±5%, રૂપેરી = ±10% (પટ્ટો ન હોય તો ±20%)."),
        V("What does the power rating of a resistor mean?", "રેઝિસ્ટરના પાવર રેટિંગનો અર્થ શું?",
          "The maximum power (watts) it can dissipate as heat without getting damaged.",
          "નુકસાન વગર તે ઉષ્મા રૂપે વધુમાં વધુ કેટલો પાવર (વોટ) ડિસિપેટ કરી શકે તે."),
        V("Which resistor is used for high power?", "ઊંચા પાવર માટે કયો રેઝિસ્ટર વપરાય?",
          "Wire wound resistor.", "વાયર વાઉન્ડ રેઝિસ્ટર."),
        V("Difference between potentiometer and rheostat?", "પોટેન્શિઓમીટર અને રીઓસ્ટેટ વચ્ચે તફાવત?",
          "Potentiometer has 3 terminals and is used as a voltage divider; rheostat uses 2 terminals and controls current.",
          "પોટેન્શિઓમીટરમાં 3 ટર્મિનલ, વોલ્ટેજ ડિવાઇડર તરીકે વપરાય; રીઓસ્ટેટમાં 2 ટર્મિનલ, કરંટ નિયંત્રિત કરે."),
        V("What happens to LDR resistance in light?", "પ્રકાશમાં LDR નો અવરોધ શું થાય?",
          "It decreases.", "તે ઘટે છે."),
        V("What is an NTC thermistor?", "NTC થર્મિસ્ટર શું છે?",
          "A thermistor whose resistance decreases when temperature increases.",
          "એવો થર્મિસ્ટર જેનો અવરોધ તાપમાન વધે ત્યારે ઘટે છે."),
        V("What is the value of a resistor marked 103?", "103 લખેલા રેઝિસ્ટરનું મૂલ્ય?",
          "10 × 10³ = 10 kΩ.", "10 × 10³ = 10 kΩ."),
    ]},
    {"title": {"en": "Capacitors & Inductors", "gu": "કેપેસિટર અને ઇન્ડક્ટર"}, "items": [
        V("What is the unit of capacitance?", "કેપેસિટન્સનો એકમ?", "Farad (F).", "ફેરાડ (F)."),
        V("What is a dielectric?", "ડાઇઇલેક્ટ્રિક એટલે શું?",
          "The insulating material between the plates of a capacitor, e.g. air, mica, ceramic, paper.",
          "કેપેસિટરની પ્લેટો વચ્ચેનો અવાહક પદાર્થ, દા.ત. હવા, માઇકા, સિરામિક, કાગળ."),
        V("Does a capacitor pass DC?", "શું કેપેસિટર DC પસાર કરે છે?",
          "No. After charging it blocks DC; it passes AC.",
          "ના. ચાર્જ થયા પછી DC ને રોકે છે; AC ને પસાર કરે છે."),
        V("Which capacitor is polarized?", "કયો કેપેસિટર પોલરાઇઝ્ડ છે?",
          "Electrolytic (aluminium and tantalum) capacitors.",
          "ઇલેક્ટ્રોલિટિક (એલ્યુમિનિયમ અને ટેન્ટેલમ) કેપેસિટર."),
        V("What happens if an electrolytic capacitor is connected in reverse?", "ઇલેક્ટ્રોલિટિક કેપેસિટર ઊંધો જોડીએ તો શું થાય?",
          "It heats up, leaks and may burst.", "તે ગરમ થાય, લીક થાય અને ફાટી પણ શકે."),
        V("What is the value of capacitor code 104?", "કેપેસિટર કોડ 104 નું મૂલ્ય?",
          "10 × 10⁴ pF = 100 nF = 0.1 μF.", "10 × 10⁴ pF = 100 nF = 0.1 μF."),
        V("Which capacitor is used for radio tuning?", "રેડિયો ટ્યુનિંગ માટે કયો કેપેસિટર વપરાય?",
          "Gang (variable) capacitor.", "ગેંગ (વેરિએબલ) કેપેસિટર."),
        V("What is the unit of inductance?", "ઇન્ડક્ટન્સનો એકમ?", "Henry (H).", "હેનરી (H)."),
        V("What does an inductor oppose?", "ઇન્ડક્ટર શેનો વિરોધ કરે છે?",
          "Any change in current through it.", "તેમાંથી વહેતા કરંટમાં થતા કોઈપણ ફેરફારનો."),
        V("State Lenz's law.", "લેન્ઝનો નિયમ લખો.",
          "The induced EMF always opposes the cause (change of flux) that produces it.",
          "પ્રેરિત EMF હંમેશા તેને ઉત્પન્ન કરનાર કારણ (ફ્લક્સના ફેરફાર)નો વિરોધ કરે છે."),
        V("Which device works on mutual induction?", "કયું ડિવાઇસ પરસ્પર પ્રેરણના સિદ્ધાંત પર કામ કરે છે?",
          "Transformer.", "ટ્રાન્સફોર્મર."),
        V("What is the range of the coefficient of coupling k?", "કપલિંગ ગુણાંક k ની રેન્જ?",
          "0 to 1.", "0 થી 1."),
    ]},
    {"title": {"en": "Power Supply", "gu": "પાવર સપ્લાય"}, "items": [
        V("What is the mains supply in India?", "ભારતમાં મેઇન્સ સપ્લાય કેટલો છે?",
          "230 V, 50 Hz, single-phase AC.", "230 V, 50 Hz, સિંગલ-ફેઝ AC."),
        V("What is the frequency of DC?", "DC ની ફ્રિક્વન્સી કેટલી?", "Zero (0 Hz).", "શૂન્ય (0 Hz)."),
        V("Name the blocks of a regulated DC power supply.", "રેગ્યુલેટેડ DC પાવર સપ્લાયના બ્લોકના નામ આપો.",
          "Transformer → Rectifier → Filter → Regulator → Load.",
          "ટ્રાન્સફોર્મર → રેક્ટિફાયર → ફિલ્ટર → રેગ્યુલેટર → લોડ."),
        V("What is the function of a rectifier?", "રેક્ટિફાયરનું કાર્ય શું છે?",
          "To convert AC into pulsating DC.", "AC ને પલ્સેટિંગ DC માં ફેરવવાનું."),
        V("What is the function of a filter?", "ફિલ્ટરનું કાર્ય શું છે?",
          "To remove ripple (AC part) from pulsating DC.", "પલ્સેટિંગ DC માંથી રિપલ (AC ભાગ) દૂર કરવાનું."),
        V("Which IC gives a fixed +5 V output?", "કયો IC +5 V ફિક્સ્ડ આઉટપુટ આપે છે?",
          "IC 7805.", "IC 7805."),
    ]},
]


def X(q_en, q_gu, marks):
    return {"q": {"en": q_en, "gu": q_gu}, "marks": marks}


EXAM_QS = [
    X("Define active and passive components with two examples each.", "એક્ટિવ અને પેસિવ ઘટકોની બે-બે ઉદાહરણ સાથે વ્યાખ્યા આપો.", 3),
    X("Differentiate between active and passive components.", "એક્ટિવ અને પેસિવ ઘટકો વચ્ચે તફાવત લખો.", 3),
    X("Explain the colour coding of resistors with a suitable example.", "રેઝિસ્ટરનો કલર કોડ યોગ્ય ઉદાહરણ સાથે સમજાવો.", 4),
    X("Find the value of a resistor having bands Yellow, Violet, Orange, Gold.", "પીળો, જાંબલી, નારંગી, સોનેરી પટ્ટાવાળા રેઝિસ્ટરનું મૂલ્ય શોધો.", 3),
    X("Classify resistors and explain any one fixed resistor.", "રેઝિસ્ટરનું વર્ગીકરણ કરો અને કોઈ એક ફિક્સ્ડ રેઝિસ્ટર સમજાવો.", 4),
    X("List the specifications of a resistor and explain any three.", "રેઝિસ્ટરના સ્પેસિફિકેશન્સની યાદી આપો અને કોઈ ત્રણ સમજાવો.", 4),
    X("Classify capacitors and compare their specifications.", "કેપેસિટરનું વર્ગીકરણ કરો અને તેમના સ્પેસિફિકેશન્સની સરખામણી કરો.", 7),
    X("State Faraday's laws of electromagnetic induction.", "ફેરાડેના વિદ્યુતચુંબકીય પ્રેરણના નિયમો લખો.", 3),
    X("Explain self-inductance and mutual inductance.", "સેલ્ફ-ઇન્ડક્ટન્સ અને મ્યુચ્યુઅલ ઇન્ડક્ટન્સ સમજાવો.", 4),
    X("Differentiate between resistor, capacitor and inductor.", "રેઝિસ્ટર, કેપેસિટર અને ઇન્ડક્ટર વચ્ચે તફાવત લખો.", 4),
    X("Draw and explain the block diagram of a regulated DC power supply with waveforms.", "તરંગો સાથે રેગ્યુલેટેડ DC પાવર સપ્લાયનો બ્લોક ડાયાગ્રામ દોરો અને સમજાવો.", 7),
    X("Compare AC power supply and DC power supply.", "AC પાવર સપ્લાય અને DC પાવર સપ્લાયની સરખામણી કરો.", 3),
]
