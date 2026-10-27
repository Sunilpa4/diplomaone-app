"""Basics of Electronics (DI01000151) - Unit 3: Diodes and Rectifiers (part A: 3.1 - 3.3)
Real-notes format: each item = one sub-topic card {h, body, diagram?, examples?, key?}"""


def T(h_en, h_gu, b_en, b_gu, diagram=None, examples=None, key=False):
    d = {"h": {"en": h_en, "gu": h_gu}, "body": {"en": b_en, "gu": b_gu}}
    if diagram:
        d["diagram"] = diagram
    if examples:
        d["examples"] = examples
    if key:
        d["key"] = True
    return d


# =====================================================================================
SEC_3_1 = {
    "title": {"en": "3.1 P-N Junction", "gu": "3.1 P-N Junction"},
    "items": [
        T("3.1.1 Formation of P-N Junction", "3.1.1 P-N Junction ની રચના",
          """<p>When a <b>P-type</b> semiconductor and an <b>N-type</b> semiconductor are joined in a <b>single crystal</b>, the boundary between them is called a <b>P-N junction</b>. A P-N junction with two metal leads is called a <b>P-N junction diode</b>.</p>
<p><i>Note:</i> Simply pressing two separate pieces together does not make a junction. It is made in one crystal by processes such as <b>alloying, diffusion</b> or <b>epitaxial growth</b>.</p>
<h4>What happens at the junction (unbiased)</h4>
<ol>
<li>P-side has a large number of <b>holes</b> (majority) and N-side has a large number of <b>free electrons</b> (majority).</li>
<li>Because of the difference in concentration, <b>diffusion</b> takes place: free electrons move from N-side to P-side, and holes move from P-side to N-side.</li>
<li>Electrons crossing to the P-side <b>recombine</b> with holes near the junction, and holes crossing to the N-side recombine with electrons.</li>
<li>After recombination, <b>immobile ions</b> are left near the junction: <b>negative acceptor ions</b> on the P-side and <b>positive donor ions</b> on the N-side.</li>
<li>These ions produce an <b>electric field</b> (N → P) which opposes further diffusion. Very soon an <b>equilibrium</b> is reached and diffusion stops.</li>
</ol>
<p>The region near the junction that now has only immobile ions and <b>no free charge carriers</b> is called the <b>depletion layer</b> (see diagram).</p>""",
          """<p>જ્યારે <b>P-type</b> અને <b>N-type</b> semiconductor ને <b>એક જ crystal</b> માં જોડવામાં આવે ત્યારે તેમની વચ્ચેની સીમાને <b>P-N junction</b> કહે છે. બે metal leads વાળા P-N junction ને <b>P-N junction diode</b> કહે છે.</p>
<p><i>નોંધ:</i> બે અલગ ટુકડા ફક્ત દબાવીને જોડવાથી junction બનતું નથી. તે એક જ crystal માં <b>alloying, diffusion</b> અથવા <b>epitaxial growth</b> જેવી પ્રક્રિયાથી બને છે.</p>
<h4>Junction પર શું થાય છે (unbiased)</h4>
<ol>
<li>P-side માં ઘણા <b>holes</b> (majority) અને N-side માં ઘણા <b>free electrons</b> (majority) હોય છે.</li>
<li>Concentration ના તફાવતને કારણે <b>Diffusion</b> થાય છે: free electrons N-side થી P-side તરફ અને holes P-side થી N-side તરફ જાય છે.</li>
<li>P-side માં ગયેલા electrons junction નજીક holes સાથે <b>Recombine</b> થાય છે, અને N-side માં ગયેલા holes electrons સાથે recombine થાય છે.</li>
<li>Recombination પછી junction નજીક <b>Immobile ions</b> (સ્થિર આયન) રહી જાય છે: P-side પર <b>negative acceptor ions</b> અને N-side પર <b>positive donor ions</b>.</li>
<li>આ ions એક <b>Electric field</b> (N → P) બનાવે છે જે વધુ diffusion નો વિરોધ કરે છે. થોડા સમયમાં <b>Equilibrium</b> (સંતુલન) આવે છે અને diffusion અટકી જાય છે.</li>
</ol>
<p>Junction નજીકનો જે વિસ્તાર ફક્ત immobile ions ધરાવે છે અને જેમાં <b>કોઈ free charge carriers નથી</b>, તેને <b>Depletion layer</b> કહે છે (આકૃતિ જુઓ).</p>""",
          diagram="u3_pn_junction"),

        T("3.1.2 Depletion Layer", "3.1.2 Depletion Layer",
          """<p><b>Definition:</b> The thin region on both sides of a P-N junction which is <b>depleted (emptied) of free charge carriers</b> and contains only immobile ions is called the <b>depletion layer</b> (also called <b>depletion region, space-charge region</b> or <b>transition region</b>).</p>
<h4>Properties of depletion layer</h4>
<ul>
<li>It contains <b>no free electrons and no holes</b>, only fixed (immobile) positive and negative ions.</li>
<li>Because there are no carriers, it behaves like an <b>insulator</b> (very high resistance).</li>
<li>Its width is very small, about <b>0.5 µm to 1 µm</b> (1 µm = 10⁻⁶ m) in an unbiased diode.</li>
<li>It extends <b>more into the lightly doped side</b> and less into the heavily doped side, because equal amounts of charge must be uncovered on both sides.</li>
<li>Width <b>decreases</b> with forward bias and <b>increases</b> with reverse bias.</li>
<li>The two layers of opposite charge act like the plates of a capacitor → <b>junction (transition) capacitance</b>. This is used in the varactor diode.</li>
</ul>
<h4>Factors affecting width</h4>
<table>
<tr><th>Factor</th><th>Effect on width</th></tr>
<tr><td>Higher doping</td><td>Width decreases</td></tr>
<tr><td>Forward bias</td><td>Width decreases</td></tr>
<tr><td>Reverse bias</td><td>Width increases</td></tr>
</table>""",
          """<p><b>વ્યાખ્યા:</b> P-N junction ની બંને બાજુનો પાતળો વિસ્તાર, જે <b>free charge carriers થી ખાલી (depleted)</b> હોય છે અને જેમાં ફક્ત immobile ions હોય છે, તેને <b>Depletion layer</b> કહે છે (તેને <b>depletion region, space-charge region</b> અથવા <b>transition region</b> પણ કહે છે).</p>
<h4>Depletion layer ના ગુણધર્મો</h4>
<ul>
<li>તેમાં <b>કોઈ free electrons કે holes નથી</b>, ફક્ત સ્થિર (immobile) positive અને negative ions છે.</li>
<li>Carriers ન હોવાથી તે <b>Insulator</b> (ખૂબ વધુ resistance) જેવું વર્તે છે.</li>
<li>Unbiased diode માં તેની પહોળાઈ ખૂબ ઓછી, આશરે <b>0.5 µm થી 1 µm</b> (1 µm = 10⁻⁶ m) હોય છે.</li>
<li>તે <b>ઓછા doped બાજુમાં વધુ</b> અને વધુ doped બાજુમાં ઓછું ફેલાય છે, કારણ કે બંને બાજુ સમાન charge ખુલ્લો થવો જોઈએ.</li>
<li>Forward bias થી પહોળાઈ <b>ઘટે</b> છે અને reverse bias થી <b>વધે</b> છે.</li>
<li>વિરુદ્ધ charge ના બે સ્તર capacitor ની plates જેવું કામ કરે છે → <b>Junction (transition) capacitance</b>. Varactor diode માં તેનો ઉપયોગ થાય છે.</li>
</ul>
<h4>પહોળાઈ પર અસર કરતા પરિબળો</h4>
<table>
<tr><th>પરિબળ</th><th>પહોળાઈ પર અસર</th></tr>
<tr><td>વધુ Doping</td><td>પહોળાઈ ઘટે</td></tr>
<tr><td>Forward bias</td><td>પહોળાઈ ઘટે</td></tr>
<tr><td>Reverse bias</td><td>પહોળાઈ વધે</td></tr>
</table>"""),

        T("3.1.3 Barrier Potential and Knee Voltage", "3.1.3 Barrier Potential અને Knee Voltage",
          """<h4>Barrier potential (V₀)</h4>
<p>The immobile ions in the depletion layer create a <b>potential difference across the junction</b>. This potential acts as a <b>barrier</b> which stops further movement of majority carriers. It is called the <b>barrier potential</b> or <b>junction potential</b> or <b>potential barrier</b>.</p>
<ul>
<li>Silicon (Si): <b>V₀ ≈ 0.7 V</b></li>
<li>Germanium (Ge): <b>V₀ ≈ 0.3 V</b></li>
</ul>
<p>The barrier potential cannot be measured with a voltmeter, because contact potentials at the metal leads cancel it.</p>
<h4>Factors affecting barrier potential</h4>
<ul>
<li><b>Material:</b> Si has a higher value than Ge (larger energy gap).</li>
<li><b>Doping:</b> Higher doping → slightly higher barrier potential.</li>
<li><b>Temperature:</b> Barrier potential <b>decreases by about 2 mV for every 1 °C rise</b> in temperature.</li>
</ul>
<h4>Knee voltage (cut-in voltage, V<sub>K</sub>)</h4>
<p><b>Definition:</b> The forward voltage at which the current through the diode starts to <b>increase rapidly</b> is called the <b>knee voltage</b> or <b>cut-in voltage</b> or <b>threshold voltage</b>.</p>
<ul>
<li>Below the knee voltage, the barrier is not fully overcome and only a very small current flows.</li>
<li>Above the knee voltage, current rises sharply (the curve bends like a knee).</li>
<li>Knee voltage is approximately equal to the barrier potential: <b>Si ≈ 0.7 V, Ge ≈ 0.3 V</b>.</li>
</ul>""",
          """<h4>Barrier potential (V₀)</h4>
<p>Depletion layer માંના immobile ions <b>junction પર potential difference</b> બનાવે છે. આ potential એક <b>અવરોધ (barrier)</b> તરીકે કામ કરે છે જે majority carriers ની વધુ ગતિ અટકાવે છે. તેને <b>Barrier potential</b>, <b>junction potential</b> અથવા <b>potential barrier</b> કહે છે.</p>
<ul>
<li>Silicon (Si): <b>V₀ ≈ 0.7 V</b></li>
<li>Germanium (Ge): <b>V₀ ≈ 0.3 V</b></li>
</ul>
<p>Barrier potential voltmeter થી માપી શકાતો નથી, કારણ કે metal leads પરના contact potentials તેને રદ કરે છે.</p>
<h4>Barrier potential પર અસર કરતા પરિબળો</h4>
<ul>
<li><b>Material:</b> Si નું મૂલ્ય Ge કરતાં વધુ છે (વધુ energy gap).</li>
<li><b>Doping:</b> વધુ doping → થોડો વધુ barrier potential.</li>
<li><b>તાપમાન:</b> તાપમાનમાં <b>દર 1 °C વધારે barrier potential આશરે 2 mV ઘટે</b> છે.</li>
</ul>
<h4>Knee voltage (cut-in voltage, V<sub>K</sub>)</h4>
<p><b>વ્યાખ્યા:</b> જે forward voltage પર diode માંથી current <b>ઝડપથી વધવા</b> લાગે છે, તેને <b>Knee voltage</b>, <b>cut-in voltage</b> અથવા <b>threshold voltage</b> કહે છે.</p>
<ul>
<li>Knee voltage થી નીચે barrier સંપૂર્ણ પાર થતો નથી અને ફક્ત ખૂબ ઓછો current વહે છે.</li>
<li>Knee voltage થી ઉપર current ઝડપથી વધે છે (curve ઘૂંટણ (knee) જેવો વળે છે).</li>
<li>Knee voltage લગભગ barrier potential જેટલો હોય છે: <b>Si ≈ 0.7 V, Ge ≈ 0.3 V</b>.</li>
</ul>"""),

        T("3.1.4 Diode Symbol, Identification and Ratings", "3.1.4 Diode Symbol, ઓળખ અને Ratings",
          """<h4>Symbol</h4>
<ul>
<li>The <b>arrow (triangle)</b> represents the <b>P-side = Anode (A)</b>.</li>
<li>The <b>bar (line)</b> represents the <b>N-side = Cathode (K)</b>.</li>
<li>The arrow shows the direction of <b>conventional current</b> in forward bias (A → K).</li>
</ul>
<h4>Identification of terminals</h4>
<ul>
<li>A <b>silver/white band</b> printed on the diode body marks the <b>cathode</b>.</li>
<li>With a <b>multimeter</b> in diode-test mode: if the meter shows about 0.5–0.7 V, the red probe is on the anode. In the reverse direction it shows "OL" (open).</li>
</ul>
<h4>Important ratings (specifications)</h4>
<table>
<tr><th>Rating</th><th>Meaning</th></tr>
<tr><td>Maximum forward current (I<sub>F(max)</sub>)</td><td>Highest forward current the diode can carry without damage</td></tr>
<tr><td>Peak Inverse Voltage (PIV)</td><td>Maximum reverse voltage that can be applied without breakdown</td></tr>
<tr><td>Forward voltage drop (V<sub>F</sub>)</td><td>Voltage across the diode when conducting (Si ≈ 0.7 V)</td></tr>
<tr><td>Reverse saturation current (I<sub>0</sub>)</td><td>Small current in reverse bias (nA for Si, µA for Ge)</td></tr>
<tr><td>Maximum power dissipation (P<sub>D</sub>)</td><td>P<sub>D</sub> = V<sub>F</sub> × I<sub>F</sub></td></tr>
</table>
<p><b>Example:</b> 1N4007 → I<sub>F(max)</sub> = 1 A, PIV = 1000 V. (1N4001 = 50 V, 1N4004 = 400 V.) 1N4148 is a small-signal switching diode.</p>""",
          """<h4>Symbol</h4>
<ul>
<li><b>Arrow (ત્રિકોણ)</b> એ <b>P-side = Anode (A)</b> દર્શાવે છે.</li>
<li><b>Bar (રેખા)</b> એ <b>N-side = Cathode (K)</b> દર્શાવે છે.</li>
<li>Arrow forward bias માં <b>conventional current</b> ની દિશા (A → K) બતાવે છે.</li>
</ul>
<h4>Terminals ની ઓળખ</h4>
<ul>
<li>Diode ના body પર છાપેલો <b>silver/સફેદ band</b> <b>Cathode</b> દર્શાવે છે.</li>
<li><b>Multimeter</b> ના diode-test mode માં: જો meter આશરે 0.5–0.7 V બતાવે તો red probe anode પર છે. ઉલટી દિશામાં તે "OL" (open) બતાવે છે.</li>
</ul>
<h4>મહત્વના Ratings (specifications)</h4>
<table>
<tr><th>Rating</th><th>અર્થ</th></tr>
<tr><td>Maximum forward current (I<sub>F(max)</sub>)</td><td>નુકસાન વિના diode વહન કરી શકે તેટલો મહત્તમ forward current</td></tr>
<tr><td>Peak Inverse Voltage (PIV)</td><td>Breakdown વિના લગાવી શકાય તેટલો મહત્તમ reverse voltage</td></tr>
<tr><td>Forward voltage drop (V<sub>F</sub>)</td><td>Conduction વખતે diode પરનો voltage (Si ≈ 0.7 V)</td></tr>
<tr><td>Reverse saturation current (I<sub>0</sub>)</td><td>Reverse bias માં નાનો current (Si માટે nA, Ge માટે µA)</td></tr>
<tr><td>Maximum power dissipation (P<sub>D</sub>)</td><td>P<sub>D</sub> = V<sub>F</sub> × I<sub>F</sub></td></tr>
</table>
<p><b>ઉદાહરણ:</b> 1N4007 → I<sub>F(max)</sub> = 1 A, PIV = 1000 V. (1N4001 = 50 V, 1N4004 = 400 V.) 1N4148 એ small-signal switching diode છે.</p>""",
          diagram="u3_diode_symbol"),

        T("Key Points – 3.1", "મુખ્ય મુદ્દા – 3.1",
          """<ul>
<li>P-type + N-type in one crystal → <b>P-N junction</b>; with leads → <b>diode</b>.</li>
<li>Diffusion + recombination → immobile ions → <b>depletion layer</b> (no free carriers, ~1 µm).</li>
<li>Depletion layer extends more into the <b>lightly doped</b> side.</li>
<li><b>Barrier potential:</b> Si 0.7 V, Ge 0.3 V; decreases ≈ 2 mV/°C.</li>
<li><b>Knee voltage</b> = forward voltage at which current rises sharply (≈ barrier potential).</li>
<li>Symbol: arrow = Anode (P), bar = Cathode (N); band on body = cathode.</li>
<li>Main ratings: I<sub>F(max)</sub>, PIV, V<sub>F</sub>, I<sub>0</sub>, P<sub>D</sub>.</li>
</ul>""",
          """<ul>
<li>એક crystal માં P-type + N-type → <b>P-N junction</b>; leads સાથે → <b>Diode</b>.</li>
<li>Diffusion + recombination → immobile ions → <b>Depletion layer</b> (free carriers નથી, ~1 µm).</li>
<li>Depletion layer <b>ઓછા doped</b> બાજુમાં વધુ ફેલાય છે.</li>
<li><b>Barrier potential:</b> Si 0.7 V, Ge 0.3 V; ≈ 2 mV/°C ઘટે.</li>
<li><b>Knee voltage</b> = જે forward voltage પર current ઝડપથી વધે (≈ barrier potential).</li>
<li>Symbol: arrow = Anode (P), bar = Cathode (N); body પરનો band = cathode.</li>
<li>મુખ્ય ratings: I<sub>F(max)</sub>, PIV, V<sub>F</sub>, I<sub>0</sub>, P<sub>D</sub>.</li>
</ul>""", key=True),
    ],
}

# =====================================================================================
SEC_3_2 = {
    "title": {"en": "3.2 Biasing of P-N Junction Diode", "gu": "3.2 P-N Junction Diode નું Biasing"},
    "items": [
        T("3.2.1 What is Biasing?", "3.2.1 Biasing એટલે શું?",
          """<p><b>Biasing</b> means applying an external <b>DC voltage</b> across the terminals of a diode (or any electronic device) to set its operating condition.</p>
<p>A P-N junction diode can be biased in two ways:</p>
<ol>
<li><b>Forward bias:</b> P-side (anode) connected to the <b>positive</b> terminal and N-side (cathode) to the <b>negative</b> terminal of the battery.</li>
<li><b>Reverse bias:</b> P-side connected to the <b>negative</b> terminal and N-side to the <b>positive</b> terminal.</li>
</ol>
<p>A resistor <b>R</b> is always connected in series to <b>limit the current</b>, otherwise a large forward current may damage the diode.</p>""",
          """<p><b>Biasing</b> એટલે diode (અથવા કોઈપણ electronic device) ના terminals પર તેની કાર્ય સ્થિતિ નક્કી કરવા બાહ્ય <b>DC voltage</b> લગાવવો.</p>
<p>P-N junction diode ને બે રીતે bias કરી શકાય:</p>
<ol>
<li><b>Forward bias:</b> P-side (anode) battery ના <b>positive</b> terminal સાથે અને N-side (cathode) <b>negative</b> terminal સાથે જોડાય.</li>
<li><b>Reverse bias:</b> P-side <b>negative</b> terminal સાથે અને N-side <b>positive</b> terminal સાથે જોડાય.</li>
</ol>
<p><b>Current મર્યાદિત</b> કરવા હંમેશા series માં resistor <b>R</b> જોડાય છે, નહીં તો વધુ forward current diode ને નુકસાન કરી શકે.</p>"""),

        T("3.2.2 Forward Bias", "3.2.2 Forward Bias",
          """<p><b>Connection:</b> Positive terminal of battery → P-side; negative terminal → N-side.</p>
<h4>Working</h4>
<ol>
<li>The positive terminal <b>repels holes</b> in the P-region towards the junction, and the negative terminal <b>repels electrons</b> in the N-region towards the junction.</li>
<li>The applied voltage <b>opposes the barrier potential</b>, so the <b>depletion layer becomes narrow</b>.</li>
<li>When the applied voltage becomes more than the barrier potential (0.7 V for Si), the barrier is overcome.</li>
<li>Electrons cross from N to P and holes from P to N, and they recombine. The battery keeps supplying electrons, so a <b>large current (mA)</b> flows continuously.</li>
<li>The current is due to <b>majority carriers</b>.</li>
</ol>
<h4>Result</h4>
<ul>
<li>Depletion layer: <b>narrow</b></li>
<li>Junction resistance: <b>very low</b> (a few ohms)</li>
<li>Current: <b>large</b>, in <b>mA</b> (increases rapidly after knee voltage)</li>
<li>Diode acts like a <b>closed (ON) switch</b></li>
</ul>""",
          """<p><b>જોડાણ:</b> Battery નો positive terminal → P-side; negative terminal → N-side.</p>
<h4>કાર્ય</h4>
<ol>
<li>Positive terminal P-region ના <b>holes ને junction તરફ ધકેલે</b> છે અને negative terminal N-region ના <b>electrons ને junction તરફ ધકેલે</b> છે.</li>
<li>લગાવેલો voltage <b>barrier potential નો વિરોધ</b> કરે છે, તેથી <b>depletion layer સાંકડું</b> થાય છે.</li>
<li>જ્યારે લગાવેલો voltage barrier potential (Si માટે 0.7 V) કરતાં વધે ત્યારે barrier પાર થઈ જાય છે.</li>
<li>Electrons N થી P અને holes P થી N તરફ જાય છે અને recombine થાય છે. Battery સતત electrons પૂરા પાડે છે, તેથી સતત <b>મોટો current (mA)</b> વહે છે.</li>
<li>આ current <b>Majority carriers</b> ને કારણે છે.</li>
</ol>
<h4>પરિણામ</h4>
<ul>
<li>Depletion layer: <b>સાંકડું</b></li>
<li>Junction resistance: <b>ખૂબ ઓછો</b> (થોડા ohms)</li>
<li>Current: <b>મોટો</b>, <b>mA</b> માં (knee voltage પછી ઝડપથી વધે)</li>
<li>Diode <b>બંધ (ON) switch</b> જેવું વર્તે છે</li>
</ul>""",
          diagram="u3_forward_bias"),

        T("3.2.3 Reverse Bias", "3.2.3 Reverse Bias",
          """<p><b>Connection:</b> Negative terminal of battery → P-side; positive terminal → N-side.</p>
<h4>Working</h4>
<ol>
<li>The negative terminal <b>attracts holes</b> of the P-region away from the junction, and the positive terminal <b>attracts electrons</b> of the N-region away from the junction.</li>
<li>More immobile ions are uncovered, so the <b>depletion layer becomes wider</b> and the barrier increases.</li>
<li>Majority carriers cannot cross the junction, so practically <b>no majority current</b> flows.</li>
<li>However, the <b>minority carriers</b> (electrons in P, holes in N), produced by heat, are pushed across the junction by the applied voltage. This produces a very small current called the <b>reverse saturation current (I₀)</b> or <b>leakage current</b>.</li>
</ol>
<h4>Result</h4>
<ul>
<li>Depletion layer: <b>wide</b></li>
<li>Junction resistance: <b>very high</b> (MΩ)</li>
<li>Current: <b>very small</b> → <b>nA for Si</b>, <b>µA for Ge</b></li>
<li>I₀ depends on <b>temperature</b>, not on applied voltage (it roughly <b>doubles for every 10 °C rise</b>).</li>
<li>Diode acts like an <b>open (OFF) switch</b></li>
</ul>
<p>If the reverse voltage is increased too much, the diode reaches <b>breakdown</b> and the reverse current increases suddenly (see 3.3.3).</p>""",
          """<p><b>જોડાણ:</b> Battery નો negative terminal → P-side; positive terminal → N-side.</p>
<h4>કાર્ય</h4>
<ol>
<li>Negative terminal P-region ના <b>holes ને junction થી દૂર ખેંચે</b> છે અને positive terminal N-region ના <b>electrons ને junction થી દૂર ખેંચે</b> છે.</li>
<li>વધુ immobile ions ખુલ્લા થાય છે, તેથી <b>depletion layer પહોળું</b> થાય છે અને barrier વધે છે.</li>
<li>Majority carriers junction પાર કરી શકતા નથી, તેથી વ્યવહારમાં <b>કોઈ majority current</b> વહેતો નથી.</li>
<li>પરંતુ ઉષ્માથી બનેલા <b>Minority carriers</b> (P માં electrons, N માં holes) લગાવેલા voltage થી junction પાર ધકેલાય છે. તેથી ખૂબ નાનો current વહે છે જેને <b>Reverse saturation current (I₀)</b> અથવા <b>leakage current</b> કહે છે.</li>
</ol>
<h4>પરિણામ</h4>
<ul>
<li>Depletion layer: <b>પહોળું</b></li>
<li>Junction resistance: <b>ખૂબ વધુ</b> (MΩ)</li>
<li>Current: <b>ખૂબ નાનો</b> → <b>Si માટે nA</b>, <b>Ge માટે µA</b></li>
<li>I₀ લગાવેલા voltage પર નહીં પરંતુ <b>તાપમાન</b> પર આધાર રાખે છે (તે લગભગ <b>દર 10 °C વધારે બમણો</b> થાય છે).</li>
<li>Diode <b>ખુલ્લા (OFF) switch</b> જેવું વર્તે છે</li>
</ul>
<p>જો reverse voltage ખૂબ વધારવામાં આવે તો diode <b>Breakdown</b> માં જાય છે અને reverse current અચાનક વધે છે (3.3.3 જુઓ).</p>""",
          diagram="u3_reverse_bias"),

        T("3.2.4 Comparison: Forward Bias vs Reverse Bias", "3.2.4 સરખામણી: Forward Bias અને Reverse Bias",
          """<table>
<tr><th>Point</th><th>Forward Bias</th><th>Reverse Bias</th></tr>
<tr><td>Connection</td><td>P → +ve, N → −ve</td><td>P → −ve, N → +ve</td></tr>
<tr><td>Depletion layer</td><td>Becomes narrow</td><td>Becomes wide</td></tr>
<tr><td>Potential barrier</td><td>Reduced</td><td>Increased</td></tr>
<tr><td>Resistance</td><td>Very low (few Ω)</td><td>Very high (MΩ)</td></tr>
<tr><td>Current</td><td>Large (mA)</td><td>Very small (nA/µA)</td></tr>
<tr><td>Current due to</td><td>Majority carriers</td><td>Minority carriers</td></tr>
<tr><td>Voltage across diode</td><td>Small (≈ 0.7 V Si)</td><td>Almost full supply voltage</td></tr>
<tr><td>Diode acts as</td><td>Closed (ON) switch</td><td>Open (OFF) switch</td></tr>
</table>
<p>This property of conducting in one direction only is called <b>unidirectional conduction</b>, and it is the basis of <b>rectification</b>.</p>""",
          """<table>
<tr><th>મુદ્દો</th><th>Forward Bias</th><th>Reverse Bias</th></tr>
<tr><td>જોડાણ</td><td>P → +ve, N → −ve</td><td>P → −ve, N → +ve</td></tr>
<tr><td>Depletion layer</td><td>સાંકડું થાય</td><td>પહોળું થાય</td></tr>
<tr><td>Potential barrier</td><td>ઘટે</td><td>વધે</td></tr>
<tr><td>Resistance</td><td>ખૂબ ઓછો (થોડા Ω)</td><td>ખૂબ વધુ (MΩ)</td></tr>
<tr><td>Current</td><td>મોટો (mA)</td><td>ખૂબ નાનો (nA/µA)</td></tr>
<tr><td>Current નું કારણ</td><td>Majority carriers</td><td>Minority carriers</td></tr>
<tr><td>Diode પરનો voltage</td><td>ઓછો (Si ≈ 0.7 V)</td><td>લગભગ સંપૂર્ણ supply voltage</td></tr>
<tr><td>Diode નું વર્તન</td><td>બંધ (ON) switch</td><td>ખુલ્લું (OFF) switch</td></tr>
</table>
<p>ફક્ત એક જ દિશામાં conduction કરવાના આ ગુણધર્મને <b>Unidirectional conduction</b> કહે છે, અને તે <b>Rectification</b> નો આધાર છે.</p>"""),

        T("Key Points – 3.2", "મુખ્ય મુદ્દા – 3.2",
          """<ul>
<li><b>Biasing</b> = applying external DC voltage to a device.</li>
<li><b>Forward bias:</b> P to +ve → narrow depletion layer → large current (mA) by majority carriers → ON switch.</li>
<li><b>Reverse bias:</b> P to −ve → wide depletion layer → tiny current I₀ (nA/µA) by minority carriers → OFF switch.</li>
<li>Diode conducts only after V > knee voltage (0.7 V Si / 0.3 V Ge).</li>
<li>I₀ depends on temperature (doubles per 10 °C), not on reverse voltage.</li>
<li>Diode conducts in one direction only → used for <b>rectification</b>.</li>
</ul>""",
          """<ul>
<li><b>Biasing</b> = device પર બાહ્ય DC voltage લગાવવો.</li>
<li><b>Forward bias:</b> P ને +ve → સાંકડું depletion layer → majority carriers થી મોટો current (mA) → ON switch.</li>
<li><b>Reverse bias:</b> P ને −ve → પહોળું depletion layer → minority carriers થી નાનો current I₀ (nA/µA) → OFF switch.</li>
<li>Diode ફક્ત V > knee voltage (Si 0.7 V / Ge 0.3 V) પછી જ conduction કરે.</li>
<li>I₀ reverse voltage પર નહીં, તાપમાન પર આધાર રાખે (દર 10 °C એ બમણો).</li>
<li>Diode ફક્ત એક દિશામાં conduction કરે → <b>Rectification</b> માટે વપરાય.</li>
</ul>""", key=True),
    ],
}

# =====================================================================================
SEC_3_3 = {
    "title": {"en": "3.3 V-I Characteristics of P-N Junction Diode", "gu": "3.3 P-N Junction Diode ની V-I Characteristics"},
    "items": [
        T("3.3.1 Circuit for V-I Characteristics", "3.3.1 V-I Characteristics માટેનો Circuit",
          """<p>The graph of <b>diode current (I)</b> against <b>diode voltage (V)</b> is called the <b>V-I characteristic</b> of the diode.</p>
<h4>Circuit components</h4>
<ul>
<li><b>Variable DC power supply</b> (0–30 V) – to change the applied voltage</li>
<li><b>Current-limiting resistor R</b> – protects the diode</li>
<li><b>Milliammeter (mA)</b> in series – measures forward current</li>
<li><b>Voltmeter (V)</b> in parallel with the diode – measures diode voltage</li>
</ul>
<h4>Procedure</h4>
<ol>
<li>Connect the circuit in <b>forward bias</b> as shown in the diagram.</li>
<li>Increase the supply voltage in small steps (0.1 V) and note V<sub>F</sub> and I<sub>F</sub> each time.</li>
<li>For <b>reverse characteristics</b>, reverse the supply polarity, replace the mA meter with a <b>µA meter</b>, and increase the voltage in steps of 1–2 V. Note V<sub>R</sub> and I<sub>R</sub>.</li>
<li>Plot V on the X-axis and I on the Y-axis (forward in the first quadrant, reverse in the third quadrant).</li>
</ol>
<p><b>Precaution:</b> Do not exceed I<sub>F(max)</sub> in forward bias or PIV in reverse bias.</p>""",
          """<p><b>Diode current (I)</b> વિરુદ્ધ <b>diode voltage (V)</b> ના આલેખને diode ની <b>V-I characteristic</b> કહે છે.</p>
<h4>Circuit ના ઘટકો</h4>
<ul>
<li><b>Variable DC power supply</b> (0–30 V) – લગાવેલો voltage બદલવા</li>
<li><b>Current-limiting resistor R</b> – diode ને રક્ષણ આપે</li>
<li>Series માં <b>Milliammeter (mA)</b> – forward current માપે</li>
<li>Diode ની parallel માં <b>Voltmeter (V)</b> – diode voltage માપે</li>
</ul>
<h4>પદ્ધતિ</h4>
<ol>
<li>આકૃતિ પ્રમાણે circuit ને <b>forward bias</b> માં જોડો.</li>
<li>Supply voltage નાના પગલાં (0.1 V) માં વધારો અને દર વખતે V<sub>F</sub> અને I<sub>F</sub> નોંધો.</li>
<li><b>Reverse characteristics</b> માટે supply polarity ઉલટાવો, mA meter ની જગ્યાએ <b>µA meter</b> મૂકો અને voltage 1–2 V ના પગલામાં વધારો. V<sub>R</sub> અને I<sub>R</sub> નોંધો.</li>
<li>X-axis પર V અને Y-axis પર I લઈ આલેખ દોરો (forward પ્રથમ ચરણમાં, reverse ત્રીજા ચરણમાં).</li>
</ol>
<p><b>સાવચેતી:</b> Forward bias માં I<sub>F(max)</sub> અને reverse bias માં PIV થી વધુ ન જવું.</p>""",
          diagram="u3_vi_circuit"),

        T("3.3.2 Forward Characteristics", "3.3.2 Forward Characteristics",
          """<p>The forward characteristic is drawn in the <b>first quadrant</b> (see diagram).</p>
<ol>
<li><b>Region 0 to V<sub>K</sub>:</b> When the forward voltage is less than the knee voltage, the potential barrier is not overcome. Current is <b>very small</b> (almost zero).</li>
<li><b>At V<sub>K</sub> (knee):</b> At about <b>0.7 V (Si)</b> or <b>0.3 V (Ge)</b> the barrier is overcome and current begins to rise sharply. The curve bends like a knee.</li>
<li><b>Above V<sub>K</sub>:</b> Current increases <b>rapidly (exponentially)</b> for a very small increase in voltage. The diode offers very low resistance. The curve is almost a straight, steep line.</li>
</ol>
<p>If the forward current exceeds I<sub>F(max)</sub>, the diode overheats and gets damaged. So a series resistor is always used.</p>
<p><b>Diode current equation (Shockley):</b> I = I₀ (e<sup>V/ηV<sub>T</sub></sup> − 1), where V<sub>T</sub> ≈ 26 mV at room temperature, η = 1 (Ge) or 2 (Si).</p>""",
          """<p>Forward characteristic <b>પ્રથમ ચરણ (first quadrant)</b> માં દોરાય છે (આકૃતિ જુઓ).</p>
<ol>
<li><b>વિસ્તાર 0 થી V<sub>K</sub>:</b> જ્યારે forward voltage, knee voltage કરતાં ઓછો હોય ત્યારે potential barrier પાર થતો નથી. Current <b>ખૂબ નાનો</b> (લગભગ શૂન્ય) હોય છે.</li>
<li><b>V<sub>K</sub> (knee) પર:</b> આશરે <b>0.7 V (Si)</b> અથવા <b>0.3 V (Ge)</b> પર barrier પાર થાય છે અને current ઝડપથી વધવા લાગે છે. Curve ઘૂંટણ જેવો વળે છે.</li>
<li><b>V<sub>K</sub> થી ઉપર:</b> Voltage માં ખૂબ નાના વધારા સાથે current <b>ઝડપથી (exponentially)</b> વધે છે. Diode ખૂબ ઓછો resistance આપે છે. Curve લગભગ સીધી, ઊભી રેખા બને છે.</li>
</ol>
<p>જો forward current I<sub>F(max)</sub> થી વધે તો diode વધુ ગરમ થઈ નુકસાન પામે છે. તેથી હંમેશા series resistor વપરાય છે.</p>
<p><b>Diode current equation (Shockley):</b> I = I₀ (e<sup>V/ηV<sub>T</sub></sup> − 1), જ્યાં room temperature પર V<sub>T</sub> ≈ 26 mV, η = 1 (Ge) અથવા 2 (Si).</p>""",
          diagram="u3_vi_char"),

        T("3.3.3 Reverse Characteristics and Breakdown", "3.3.3 Reverse Characteristics અને Breakdown",
          """<p>The reverse characteristic is drawn in the <b>third quadrant</b>.</p>
<ol>
<li><b>Before breakdown:</b> A very small, almost constant <b>reverse saturation current I₀</b> flows (nA for Si, µA for Ge). It does not depend on reverse voltage. The diode offers very high resistance.</li>
<li><b>At breakdown voltage (V<sub>BR</sub>):</b> When reverse voltage reaches V<sub>BR</sub>, the reverse current <b>increases suddenly and sharply</b>. This is called <b>reverse breakdown</b>.</li>
<li>An ordinary diode is usually <b>damaged</b> at breakdown due to excessive heat, so it is always operated below V<sub>BR</sub> (i.e., below its PIV rating).</li>
</ol>
<h4>Types of breakdown</h4>
<ul>
<li><b>Avalanche breakdown:</b> In lightly doped diodes at high reverse voltage. Minority carriers gain high energy and knock out more electrons from covalent bonds (impact ionisation), creating a chain reaction.</li>
<li><b>Zener breakdown:</b> In heavily doped diodes at low reverse voltage (below ≈ 5 V). The strong electric field directly breaks covalent bonds. (Explained in 3.4.)</li>
</ul>
<p><i>Note:</i> Different scales are used for forward (mA, fractions of a volt) and reverse (µA, tens of volts) axes.</p>""",
          """<p>Reverse characteristic <b>ત્રીજા ચરણ (third quadrant)</b> માં દોરાય છે.</p>
<ol>
<li><b>Breakdown પહેલાં:</b> ખૂબ નાનો, લગભગ અચળ <b>Reverse saturation current I₀</b> વહે છે (Si માટે nA, Ge માટે µA). તે reverse voltage પર આધાર રાખતો નથી. Diode ખૂબ વધુ resistance આપે છે.</li>
<li><b>Breakdown voltage (V<sub>BR</sub>) પર:</b> જ્યારે reverse voltage V<sub>BR</sub> સુધી પહોંચે ત્યારે reverse current <b>અચાનક અને ઝડપથી વધે</b> છે. તેને <b>Reverse breakdown</b> કહે છે.</li>
<li>સામાન્ય diode વધુ ગરમીને કારણે breakdown પર સામાન્ય રીતે <b>નુકસાન પામે</b> છે, તેથી તેને હંમેશા V<sub>BR</sub> થી નીચે (એટલે કે PIV rating થી નીચે) ચલાવાય છે.</li>
</ol>
<h4>Breakdown ના પ્રકાર</h4>
<ul>
<li><b>Avalanche breakdown:</b> ઓછા doped diodes માં વધુ reverse voltage પર. Minority carriers વધુ ઊર્જા મેળવી covalent bonds માંથી વધુ electrons છૂટા પાડે છે (impact ionisation), જેથી શૃંખલા પ્રક્રિયા (chain reaction) થાય છે.</li>
<li><b>Zener breakdown:</b> વધુ doped diodes માં ઓછા reverse voltage (≈ 5 V થી નીચે) પર. તીવ્ર electric field સીધા covalent bonds તોડે છે. (3.4 માં સમજાવેલ છે.)</li>
</ul>
<p><i>નોંધ:</i> Forward (mA, volt નો અપૂર્ણાંક) અને reverse (µA, દસેક volts) axes માટે અલગ scale વપરાય છે.</p>"""),

        T("3.3.4 Diode Resistance, Ideal and Practical Diode", "3.3.4 Diode Resistance, Ideal અને Practical Diode",
          """<h4>1. Static (DC) resistance</h4>
<p>The ratio of DC voltage across the diode to the DC current through it at a point on the characteristic:</p>
<p><b>R<sub>DC</sub> = V<sub>F</sub> / I<sub>F</sub></b></p>
<h4>2. Dynamic (AC) resistance</h4>
<p>The ratio of a small change in voltage to the corresponding small change in current:</p>
<p><b>r<sub>d</sub> = ΔV<sub>F</sub> / ΔI<sub>F</sub></b></p>
<p>Above the knee, r<sub>d</sub> is very small (a few ohms). At room temperature, approximately r<sub>d</sub> ≈ 26 mV / I<sub>F</sub>.</p>
<h4>3. Reverse resistance</h4>
<p>R<sub>R</sub> = V<sub>R</sub> / I<sub>R</sub> → very high (MΩ).</p>
<h4>Ideal vs practical diode</h4>
<table>
<tr><th>Point</th><th>Ideal diode</th><th>Practical diode</th></tr>
<tr><td>Forward resistance</td><td>Zero</td><td>Small (few Ω)</td></tr>
<tr><td>Forward voltage drop</td><td>Zero</td><td>0.7 V (Si), 0.3 V (Ge)</td></tr>
<tr><td>Reverse resistance</td><td>Infinite</td><td>Very high (MΩ)</td></tr>
<tr><td>Reverse current</td><td>Zero</td><td>Small I₀ (nA/µA)</td></tr>
<tr><td>Behaviour</td><td>Perfect switch</td><td>Nearly a switch</td></tr>
</table>""",
          """<h4>1. Static (DC) resistance</h4>
<p>Characteristic ના કોઈ બિંદુ પર diode પરના DC voltage અને તેમાંથી વહેતા DC current નો ગુણોત્તર:</p>
<p><b>R<sub>DC</sub> = V<sub>F</sub> / I<sub>F</sub></b></p>
<h4>2. Dynamic (AC) resistance</h4>
<p>Voltage માં નાના ફેરફાર અને તેને અનુરૂપ current ના નાના ફેરફારનો ગુણોત્તર:</p>
<p><b>r<sub>d</sub> = ΔV<sub>F</sub> / ΔI<sub>F</sub></b></p>
<p>Knee થી ઉપર r<sub>d</sub> ખૂબ ઓછો (થોડા ohms) હોય છે. Room temperature પર આશરે r<sub>d</sub> ≈ 26 mV / I<sub>F</sub>.</p>
<h4>3. Reverse resistance</h4>
<p>R<sub>R</sub> = V<sub>R</sub> / I<sub>R</sub> → ખૂબ વધુ (MΩ).</p>
<h4>Ideal અને practical diode</h4>
<table>
<tr><th>મુદ્દો</th><th>Ideal diode</th><th>Practical diode</th></tr>
<tr><td>Forward resistance</td><td>શૂન્ય</td><td>ઓછો (થોડા Ω)</td></tr>
<tr><td>Forward voltage drop</td><td>શૂન્ય</td><td>0.7 V (Si), 0.3 V (Ge)</td></tr>
<tr><td>Reverse resistance</td><td>અનંત</td><td>ખૂબ વધુ (MΩ)</td></tr>
<tr><td>Reverse current</td><td>શૂન્ય</td><td>નાનો I₀ (nA/µA)</td></tr>
<tr><td>વર્તન</td><td>સંપૂર્ણ switch</td><td>લગભગ switch</td></tr>
</table>""",
          examples=["u3n1"]),

        T("3.3.5 Applications of P-N Junction Diode", "3.3.5 P-N Junction Diode ના ઉપયોગો",
          """<ul>
<li><b>Rectifiers</b> – convert AC to DC in power supplies and chargers (3.6).</li>
<li><b>Switching circuits</b> – diode as an electronic ON/OFF switch (1N4148).</li>
<li><b>Clipper circuits</b> – remove (clip) part of a waveform above or below a level.</li>
<li><b>Clamper circuits</b> – shift the DC level of a waveform.</li>
<li><b>Reverse-polarity protection</b> – prevents damage if the battery is connected the wrong way.</li>
<li><b>Freewheeling (flyback) diode</b> – across relay coils and motors to absorb back EMF.</li>
<li><b>Voltage multipliers</b> – doubler, tripler circuits.</li>
<li><b>Detector/demodulator</b> in radio receivers.</li>
<li><b>Logic gates</b> – diode AND / OR gates.</li>
</ul>""",
          """<ul>
<li><b>Rectifiers</b> – power supply અને chargers માં AC ને DC માં ફેરવે (3.6).</li>
<li><b>Switching circuits</b> – electronic ON/OFF switch તરીકે diode (1N4148).</li>
<li><b>Clipper circuits</b> – waveform નો કોઈ સ્તરથી ઉપર કે નીચેનો ભાગ કાપે (clip).</li>
<li><b>Clamper circuits</b> – waveform નું DC level ખસેડે.</li>
<li><b>Reverse-polarity protection</b> – battery ઉલટી જોડાય તો નુકસાન અટકાવે.</li>
<li><b>Freewheeling (flyback) diode</b> – relay coils અને motors પર back EMF શોષવા.</li>
<li><b>Voltage multipliers</b> – doubler, tripler circuits.</li>
<li>Radio receivers માં <b>Detector/demodulator</b>.</li>
<li><b>Logic gates</b> – diode AND / OR gates.</li>
</ul>"""),

        T("Key Points – 3.3", "મુખ્ય મુદ્દા – 3.3",
          """<ul>
<li>V-I characteristic = graph of diode current vs diode voltage.</li>
<li>Forward: almost zero current up to V<sub>K</sub>, then current rises sharply (mA).</li>
<li>Reverse: tiny constant I₀ (nA/µA) until <b>breakdown voltage V<sub>BR</sub></b>, then sharp rise.</li>
<li>Ordinary diode is damaged at breakdown → keep reverse voltage below PIV.</li>
<li>Static R = V/I; dynamic r<sub>d</sub> = ΔV/ΔI ≈ 26 mV/I<sub>F</sub>.</li>
<li>Ideal diode: zero forward resistance & drop, infinite reverse resistance.</li>
<li>Applications: rectifier, switch, clipper, clamper, protection, voltage multiplier.</li>
</ul>""",
          """<ul>
<li>V-I characteristic = diode current વિરુદ્ધ diode voltage નો આલેખ.</li>
<li>Forward: V<sub>K</sub> સુધી લગભગ શૂન્ય current, પછી current ઝડપથી વધે (mA).</li>
<li>Reverse: <b>Breakdown voltage V<sub>BR</sub></b> સુધી નાનો અચળ I₀ (nA/µA), પછી ઝડપી વધારો.</li>
<li>સામાન્ય diode breakdown પર નુકસાન પામે → reverse voltage PIV થી નીચે રાખો.</li>
<li>Static R = V/I; dynamic r<sub>d</sub> = ΔV/ΔI ≈ 26 mV/I<sub>F</sub>.</li>
<li>Ideal diode: શૂન્ય forward resistance અને drop, અનંત reverse resistance.</li>
<li>ઉપયોગો: rectifier, switch, clipper, clamper, protection, voltage multiplier.</li>
</ul>""", key=True),
    ],
}

NOTES_A = [SEC_3_1, SEC_3_2, SEC_3_3]
