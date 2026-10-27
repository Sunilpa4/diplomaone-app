"""Basics of Electronics (DI01000151) - Unit 1 notes, topics 1.3, 1.4, 1.5"""
from content_DI01000151_u1_notes_a import Q

SEC_1_3 = {
    "title": {"en": "1.3 Capacitors", "gu": "1.3 કેપેસિટર"},
    "items": [
        Q("What is a capacitor? Explain the concept of capacitance.",
          "કેપેસિટર એટલે શું? કેપેસિટન્સનો ખ્યાલ સમજાવો.",
          """<p>A <b>capacitor</b> is a passive, two-terminal component that <b>stores electrical energy in the form of an electric field</b>.</p>
<p><b>Construction:</b> It consists of <b>two conducting plates</b> separated by an insulating material called the <b>dielectric</b> (air, paper, mica, ceramic, plastic film, electrolyte, etc.).</p>
<p><b>Working:</b> When a DC voltage is applied, electrons collect on one plate (−Q) and leave the other plate (+Q). An electric field is set up in the dielectric and energy is stored. The capacitor charges until its voltage equals the supply voltage.</p>
<p><b>Capacitance:</b> The ability of a capacitor to store charge. It is the ratio of charge to voltage:</p>
<p class='eq'>C = Q / V</p>
<ul>
<li><b>Unit:</b> Farad (F). Practical units: μF = 10⁻⁶ F, nF = 10⁻⁹ F, pF = 10⁻¹² F.</li>
<li>For a parallel plate capacitor: <b>C = ε₀ εᵣ A / d</b> – capacitance increases with plate area (A) and dielectric constant (εᵣ), and decreases with distance between plates (d).</li>
<li>Energy stored: <b>E = ½ C V²</b> joules.</li>
<li>A capacitor <b>blocks DC</b> (after charging) and <b>passes AC</b>. Capacitive reactance X<sub>C</sub> = 1 / (2πfC).</li>
</ul>
<p><b>Applications:</b> filters in power supplies, coupling and bypass in amplifiers, timing circuits (555 timer), tuning circuits in radio, power factor correction, motor starting, camera flash.</p>""",
          """<p><b>કેપેસિટર</b> એ બે ટર્મિનલ ધરાવતો પેસિવ ઘટક છે, જે <b>વિદ્યુત ઊર્જાનો વિદ્યુત ક્ષેત્ર (ઇલેક્ટ્રિક ફિલ્ડ) સ્વરૂપે સંગ્રહ</b> કરે છે.</p>
<p><b>રચના:</b> તેમાં <b>બે વાહક પ્લેટ</b> હોય છે, જે <b>ડાઇઇલેક્ટ્રિક</b> નામના અવાહક પદાર્થ (હવા, કાગળ, માઇકા, સિરામિક, પ્લાસ્ટિક ફિલ્મ, ઇલેક્ટ્રોલાઇટ વગેરે) વડે અલગ કરેલી હોય છે.</p>
<p><b>કાર્ય:</b> DC વોલ્ટેજ આપતાં એક પ્લેટ પર ઇલેક્ટ્રોન એકઠા થાય છે (−Q) અને બીજી પ્લેટ પરથી ઇલેક્ટ્રોન જતા રહે છે (+Q). ડાઇઇલેક્ટ્રિકમાં વિદ્યુત ક્ષેત્ર રચાય છે અને ઊર્જાનો સંગ્રહ થાય છે. કેપેસિટરનો વોલ્ટેજ સપ્લાય વોલ્ટેજ જેટલો થાય ત્યાં સુધી તે ચાર્જ થાય છે.</p>
<p><b>કેપેસિટન્સ:</b> કેપેસિટરની ચાર્જ સંગ્રહ કરવાની ક્ષમતા. તે ચાર્જ અને વોલ્ટેજનો ગુણોત્તર છે:</p>
<p class='eq'>C = Q / V</p>
<ul>
<li><b>એકમ:</b> ફેરાડ (F). વ્યવહારુ એકમ: μF = 10⁻⁶ F, nF = 10⁻⁹ F, pF = 10⁻¹² F.</li>
<li>સમાંતર પ્લેટ કેપેસિટર માટે: <b>C = ε₀ εᵣ A / d</b> – પ્લેટનું ક્ષેત્રફળ (A) અને ડાઇઇલેક્ટ્રિક અચળાંક (εᵣ) વધે તો કેપેસિટન્સ વધે, અને પ્લેટો વચ્ચેનું અંતર (d) વધે તો ઘટે.</li>
<li>સંગ્રહિત ઊર્જા: <b>E = ½ C V²</b> જૂલ.</li>
<li>કેપેસિટર (ચાર્જ થયા પછી) <b>DC ને રોકે</b> છે અને <b>AC ને પસાર</b> થવા દે છે. કેપેસિટિવ રિએક્ટન્સ X<sub>C</sub> = 1 / (2πfC).</li>
</ul>
<p><b>ઉપયોગ:</b> પાવર સપ્લાયમાં ફિલ્ટર, એમ્પ્લિફાયરમાં કપલિંગ અને બાયપાસ, ટાઇમિંગ સર્કિટ (555 ટાઇમર), રેડિયોમાં ટ્યુનિંગ સર્કિટ, પાવર ફેક્ટર સુધારણા, મોટર સ્ટાર્ટિંગ, કેમેરા ફ્લેશ.</p>""",
          diagram="u1_parallel_plate"),

        Q("Give the classification of capacitors.",
          "કેપેસિટરનું વર્ગીકરણ આપો.",
          """<ol>
<li><b>Fixed capacitors</b> – capacitance value is constant.
<ul>
<li><b>Polarized</b> (have + and − terminals, used only in DC circuits):
<ul><li>Aluminium electrolytic capacitor</li><li>Tantalum electrolytic capacitor</li></ul></li>
<li><b>Non-polarized</b> (can be connected either way, used in AC/DC):
<ul><li>Ceramic capacitor</li><li>Mica capacitor</li><li>Paper capacitor</li><li>Plastic film capacitor (polyester, polypropylene, polystyrene)</li></ul></li>
</ul></li>
<li><b>Variable capacitors</b> – capacitance can be changed.
<ul><li>Gang capacitor (tuning capacitor)</li><li>Trimmer capacitor</li></ul></li>
</ol>""",
          """<ol>
<li><b>ફિક્સ્ડ કેપેસિટર</b> – કેપેસિટન્સ મૂલ્ય અચળ હોય છે.
<ul>
<li><b>પોલરાઇઝ્ડ</b> (+ અને − ટર્મિનલ હોય, માત્ર DC સર્કિટમાં વપરાય):
<ul><li>એલ્યુમિનિયમ ઇલેક્ટ્રોલિટિક કેપેસિટર</li><li>ટેન્ટેલમ ઇલેક્ટ્રોલિટિક કેપેસિટર</li></ul></li>
<li><b>નોન-પોલરાઇઝ્ડ</b> (કોઈપણ દિશામાં જોડી શકાય, AC/DC બંનેમાં વપરાય):
<ul><li>સિરામિક કેપેસિટર</li><li>માઇકા કેપેસિટર</li><li>પેપર કેપેસિટર</li><li>પ્લાસ્ટિક ફિલ્મ કેપેસિટર (પોલિએસ્ટર, પોલિપ્રોપિલીન, પોલિસ્ટાયરીન)</li></ul></li>
</ul></li>
<li><b>વેરિએબલ કેપેસિટર</b> – કેપેસિટન્સ બદલી શકાય છે.
<ul><li>ગેંગ કેપેસિટર (ટ્યુનિંગ કેપેસિટર)</li><li>ટ્રીમર કેપેસિટર</li></ul></li>
</ol>""",
          diagram="u1_capacitor_tree"),

        Q("Explain the specifications of a capacitor.",
          "કેપેસિટરના સ્પેસિફિકેશન્સ સમજાવો.",
          """<ol>
<li><b>Capacitance value:</b> Nominal capacitance in pF, nF or μF, e.g. 100 μF.</li>
<li><b>Working voltage (WVDC):</b> Maximum DC voltage that can be applied continuously without breakdown of the dielectric, e.g. 16 V, 25 V, 50 V. Always choose a capacitor with working voltage <b>higher</b> than the circuit voltage.</li>
<li><b>Tolerance:</b> Allowed variation from the nominal value, e.g. ±5%, ±10%, ±20%. Electrolytic capacitors have high tolerance (−20% to +80%).</li>
<li><b>Leakage current:</b> Small current that flows through the dielectric because it is not a perfect insulator. Should be as low as possible (high in electrolytic, very low in mica/film).</li>
<li><b>Polarity:</b> Electrolytic and tantalum capacitors are polarized; they get damaged (may burst) if connected in reverse.</li>
<li><b>Temperature coefficient &amp; operating temperature:</b> Change of capacitance with temperature and the safe temperature range, e.g. −40°C to +105°C.</li>
<li><b>Dielectric type:</b> Decides the stability, size, frequency range and cost.</li>
<li><b>ESR (Equivalent Series Resistance):</b> Internal resistance of the capacitor; low ESR is needed in power supplies (SMPS).</li>
</ol>""",
          """<ol>
<li><b>કેપેસિટન્સ મૂલ્ય:</b> pF, nF કે μF માં નામાંકિત કેપેસિટન્સ, દા.ત. 100 μF.</li>
<li><b>વર્કિંગ વોલ્ટેજ (WVDC):</b> ડાઇઇલેક્ટ્રિક તૂટ્યા (બ્રેકડાઉન) વગર સતત આપી શકાય તેવો મહત્તમ DC વોલ્ટેજ, દા.ત. 16 V, 25 V, 50 V. હંમેશા સર્કિટ વોલ્ટેજ કરતાં <b>વધુ</b> વર્કિંગ વોલ્ટેજવાળો કેપેસિટર પસંદ કરવો.</li>
<li><b>ટોલરન્સ:</b> નામાંકિત મૂલ્યથી માન્ય ફેરફાર, દા.ત. ±5%, ±10%, ±20%. ઇલેક્ટ્રોલિટિક કેપેસિટરમાં ટોલરન્સ વધુ હોય છે (−20% થી +80%).</li>
<li><b>લીકેજ કરંટ:</b> ડાઇઇલેક્ટ્રિક સંપૂર્ણ અવાહક ન હોવાથી તેમાંથી વહેતો નાનો કરંટ. શક્ય તેટલો ઓછો હોવો જોઈએ (ઇલેક્ટ્રોલિટિકમાં વધુ, માઇકા/ફિલ્મમાં ખૂબ ઓછો).</li>
<li><b>પોલારિટી:</b> ઇલેક્ટ્રોલિટિક અને ટેન્ટેલમ કેપેસિટર પોલરાઇઝ્ડ છે; ઊંધા જોડવાથી તે નુકસાન પામે (ફાટી પણ શકે) છે.</li>
<li><b>તાપમાન ગુણાંક અને ઓપરેટિંગ તાપમાન:</b> તાપમાન સાથે કેપેસિટન્સમાં ફેરફાર અને સલામત તાપમાન રેન્જ, દા.ત. −40°C થી +105°C.</li>
<li><b>ડાઇઇલેક્ટ્રિકનો પ્રકાર:</b> તે સ્થિરતા, કદ, ફ્રિક્વન્સી રેન્જ અને કિંમત નક્કી કરે છે.</li>
<li><b>ESR (ઇક્વિવેલન્ટ સિરીઝ રેઝિસ્ટન્સ):</b> કેપેસિટરનો આંતરિક અવરોધ; પાવર સપ્લાય (SMPS)માં ઓછો ESR જરૂરી છે.</li>
</ol>"""),

        Q("Compare the specifications of different types of capacitors.",
          "વિવિધ પ્રકારના કેપેસિટરના સ્પેસિફિકેશન્સની સરખામણી કરો.",
          """<table>
<tr><th>Type</th><th>Typical range</th><th>Voltage</th><th>Polarity</th><th>Applications</th></tr>
<tr><td>Ceramic</td><td>1 pF – 1 μF</td><td>50 V – few kV</td><td>Non-polar</td><td>High-frequency, bypass, decoupling</td></tr>
<tr><td>Mica</td><td>1 pF – 10 nF</td><td>Up to a few kV</td><td>Non-polar</td><td>RF circuits, oscillators (very stable)</td></tr>
<tr><td>Paper</td><td>1 nF – a few μF</td><td>Up to a few kV</td><td>Non-polar</td><td>High-voltage, motor starting, AC circuits</td></tr>
<tr><td>Plastic film (polyester)</td><td>1 nF – 10 μF</td><td>50 V – 1 kV</td><td>Non-polar</td><td>Coupling, timing, audio, filters</td></tr>
<tr><td>Aluminium electrolytic</td><td>0.1 μF – 100,000 μF</td><td>6.3 V – 450 V</td><td>Polarized</td><td>Power-supply filter, DC smoothing</td></tr>
<tr><td>Tantalum</td><td>0.1 μF – 1000 μF</td><td>Up to about 50 V</td><td>Polarized</td><td>Small-size filtering, mobiles, laptops</td></tr>
<tr><td>Variable (gang)</td><td>Few pF – 500 pF</td><td>Low</td><td>Non-polar</td><td>Radio tuning</td></tr>
</table>
<p><b>Key points:</b> Electrolytic capacitors give the <b>highest capacitance in small size</b> but have high leakage and are polarized. Mica capacitors are the <b>most stable</b>. Ceramic capacitors are best for <b>high frequency</b>.</p>""",
          """<table>
<tr><th>પ્રકાર</th><th>સામાન્ય રેન્જ</th><th>વોલ્ટેજ</th><th>પોલારિટી</th><th>ઉપયોગ</th></tr>
<tr><td>સિરામિક</td><td>1 pF – 1 μF</td><td>50 V – થોડા kV</td><td>નોન-પોલર</td><td>હાઇ-ફ્રિક્વન્સી, બાયપાસ, ડિકપલિંગ</td></tr>
<tr><td>માઇકા</td><td>1 pF – 10 nF</td><td>થોડા kV સુધી</td><td>નોન-પોલર</td><td>RF સર્કિટ, ઓસિલેટર (ખૂબ સ્થિર)</td></tr>
<tr><td>પેપર</td><td>1 nF – થોડા μF</td><td>થોડા kV સુધી</td><td>નોન-પોલર</td><td>હાઇ-વોલ્ટેજ, મોટર સ્ટાર્ટિંગ, AC સર્કિટ</td></tr>
<tr><td>પ્લાસ્ટિક ફિલ્મ (પોલિએસ્ટર)</td><td>1 nF – 10 μF</td><td>50 V – 1 kV</td><td>નોન-પોલર</td><td>કપલિંગ, ટાઇમિંગ, ઓડિયો, ફિલ્ટર</td></tr>
<tr><td>એલ્યુમિનિયમ ઇલેક્ટ્રોલિટિક</td><td>0.1 μF – 1,00,000 μF</td><td>6.3 V – 450 V</td><td>પોલરાઇઝ્ડ</td><td>પાવર-સપ્લાય ફિલ્ટર, DC સ્મૂધિંગ</td></tr>
<tr><td>ટેન્ટેલમ</td><td>0.1 μF – 1000 μF</td><td>આશરે 50 V સુધી</td><td>પોલરાઇઝ્ડ</td><td>નાના કદમાં ફિલ્ટરિંગ, મોબાઇલ, લેપટોપ</td></tr>
<tr><td>વેરિએબલ (ગેંગ)</td><td>થોડા pF – 500 pF</td><td>ઓછો</td><td>નોન-પોલર</td><td>રેડિયો ટ્યુનિંગ</td></tr>
</table>
<p><b>મુખ્ય મુદ્દા:</b> ઇલેક્ટ્રોલિટિક કેપેસિટર <b>નાના કદમાં સૌથી વધુ કેપેસિટન્સ</b> આપે છે, પરંતુ લીકેજ વધુ અને પોલરાઇઝ્ડ છે. માઇકા કેપેસિટર <b>સૌથી સ્થિર</b> છે. સિરામિક કેપેસિટર <b>હાઇ ફ્રિક્વન્સી</b> માટે શ્રેષ્ઠ છે.</p>"""),

        Q("Explain fixed and variable capacitors.",
          "ફિક્સ્ડ અને વેરિએબલ કેપેસિટર સમજાવો.",
          """<p><b>Fixed capacitors</b> have a constant capacitance value.</p>
<ul>
<li><b>Ceramic capacitor:</b> Ceramic material (e.g. barium titanate) is the dielectric with silver coating as plates. Disc shaped, small, cheap. Used in high-frequency and bypass circuits.</li>
<li><b>Mica capacitor:</b> Thin mica sheets act as the dielectric between metal foils. Very stable, low loss, used in RF circuits.</li>
<li><b>Paper capacitor:</b> Waxed/oil-impregnated paper is placed between two aluminium foils, rolled into a cylinder. Used in high-voltage and AC circuits.</li>
<li><b>Electrolytic capacitor:</b> An oxide layer formed on aluminium foil acts as the dielectric; an electrolyte-soaked paper forms the second plate. Very high capacitance, polarized. The <b>negative lead is marked by a stripe</b> and is usually shorter. Used for filtering in power supplies.</li>
</ul>
<p><b>Variable capacitors</b> have a capacitance that can be changed by changing the <b>overlapping area</b> of the plates.</p>
<ul>
<li><b>Gang capacitor:</b> Has a set of fixed plates (stator) and movable plates (rotor) on a shaft with air as dielectric. Rotating the shaft changes the overlapping area and so the capacitance. Two or more sections on one shaft are called a "gang". Used for <b>station tuning in radio receivers</b>.</li>
<li><b>Trimmer capacitor:</b> A small variable capacitor (mica/ceramic dielectric) adjusted with a screwdriver for fine tuning and calibration in oscillators and RF circuits.</li>
</ul>""",
          """<p><b>ફિક્સ્ડ કેપેસિટર</b>નું કેપેસિટન્સ અચળ હોય છે.</p>
<ul>
<li><b>સિરામિક કેપેસિટર:</b> સિરામિક પદાર્થ (દા.ત. બેરિયમ ટાઇટેનેટ) ડાઇઇલેક્ટ્રિક અને ચાંદીનું આવરણ પ્લેટ તરીકે. ડિસ્ક આકારનો, નાનો, સસ્તો. હાઇ-ફ્રિક્વન્સી અને બાયપાસ સર્કિટમાં વપરાય.</li>
<li><b>માઇકા કેપેસિટર:</b> ધાતુની પતરીઓ વચ્ચે માઇકાની પાતળી શીટ ડાઇઇલેક્ટ્રિક તરીકે. ખૂબ સ્થિર, ઓછો લોસ, RF સર્કિટમાં વપરાય.</li>
<li><b>પેપર કેપેસિટર:</b> બે એલ્યુમિનિયમ ફોઇલ વચ્ચે મીણ/તેલવાળો કાગળ મૂકીને નળાકારમાં વીંટાળાય છે. હાઇ-વોલ્ટેજ અને AC સર્કિટમાં વપરાય.</li>
<li><b>ઇલેક્ટ્રોલિટિક કેપેસિટર:</b> એલ્યુમિનિયમ ફોઇલ પર બનેલું ઓક્સાઇડનું સ્તર ડાઇઇલેક્ટ્રિક તરીકે; ઇલેક્ટ્રોલાઇટમાં પલાળેલો કાગળ બીજી પ્લેટ બનાવે છે. ખૂબ વધુ કેપેસિટન્સ, પોલરાઇઝ્ડ. <b>નેગેટિવ લીડ પટ્ટા (સ્ટ્રાઇપ) વડે દર્શાવાય</b> છે અને સામાન્ય રીતે ટૂંકી હોય છે. પાવર સપ્લાયમાં ફિલ્ટરિંગ માટે વપરાય.</li>
</ul>
<p><b>વેરિએબલ કેપેસિટર</b>માં પ્લેટોનું <b>એકબીજા પર આવતું (ઓવરલેપિંગ) ક્ષેત્રફળ</b> બદલીને કેપેસિટન્સ બદલી શકાય છે.</p>
<ul>
<li><b>ગેંગ કેપેસિટર:</b> તેમાં સ્થિર પ્લેટો (સ્ટેટર) અને શાફ્ટ પર ફરતી પ્લેટો (રોટર) હોય છે, હવા ડાઇઇલેક્ટ્રિક તરીકે. શાફ્ટ ફેરવતાં ઓવરલેપિંગ ક્ષેત્રફળ અને તેથી કેપેસિટન્સ બદલાય છે. એક શાફ્ટ પર બે કે વધુ સેક્શનને "ગેંગ" કહે છે. <b>રેડિયો રિસીવરમાં સ્ટેશન ટ્યુનિંગ</b> માટે વપરાય.</li>
<li><b>ટ્રીમર કેપેસિટર:</b> નાનો વેરિએબલ કેપેસિટર (માઇકા/સિરામિક ડાઇઇલેક્ટ્રિક), જેને ઓસિલેટર અને RF સર્કિટમાં ફાઇન ટ્યુનિંગ અને કેલિબ્રેશન માટે સ્ક્રૂડ્રાઇવરથી એડજસ્ટ કરાય છે.</li>
</ul>"""),

        Q("How is the value of a capacitor read from its code?",
          "કેપેસિટરનું મૂલ્ય તેના કોડ પરથી કેવી રીતે વાંચાય છે?",
          """<ul>
<li><b>Electrolytic capacitors</b> have the value and voltage printed directly, e.g. <b>470 μF, 25 V</b>.</li>
<li><b>Ceramic/film capacitors</b> use a <b>3-digit code in pF</b>: first two digits = value, third digit = number of zeros.</li>
</ul>
<table>
<tr><th>Code</th><th>Calculation</th><th>Value</th></tr>
<tr><td>104</td><td>10 × 10⁴ pF</td><td>100,000 pF = 100 nF = <b>0.1 μF</b></td></tr>
<tr><td>103</td><td>10 × 10³ pF</td><td>10,000 pF = 10 nF = <b>0.01 μF</b></td></tr>
<tr><td>222</td><td>22 × 10² pF</td><td>2200 pF = <b>2.2 nF</b></td></tr>
<tr><td>47</td><td>(only 2 digits)</td><td><b>47 pF</b></td></tr>
</table>
<p>A letter after the code shows tolerance: <b>J</b> = ±5%, <b>K</b> = ±10%, <b>M</b> = ±20%. e.g. <b>104K</b> = 0.1 μF ± 10%.</p>""",
          """<ul>
<li><b>ઇલેક્ટ્રોલિટિક કેપેસિટર</b> પર મૂલ્ય અને વોલ્ટેજ સીધા છાપેલા હોય છે, દા.ત. <b>470 μF, 25 V</b>.</li>
<li><b>સિરામિક/ફિલ્મ કેપેસિટર</b> પર <b>pF માં 3-અંક કોડ</b> હોય છે: પહેલા બે અંક = મૂલ્ય, ત્રીજો અંક = શૂન્યની સંખ્યા.</li>
</ul>
<table>
<tr><th>કોડ</th><th>ગણતરી</th><th>મૂલ્ય</th></tr>
<tr><td>104</td><td>10 × 10⁴ pF</td><td>1,00,000 pF = 100 nF = <b>0.1 μF</b></td></tr>
<tr><td>103</td><td>10 × 10³ pF</td><td>10,000 pF = 10 nF = <b>0.01 μF</b></td></tr>
<tr><td>222</td><td>22 × 10² pF</td><td>2200 pF = <b>2.2 nF</b></td></tr>
<tr><td>47</td><td>(માત્ર 2 અંક)</td><td><b>47 pF</b></td></tr>
</table>
<p>કોડ પછીનો અક્ષર ટોલરન્સ દર્શાવે છે: <b>J</b> = ±5%, <b>K</b> = ±10%, <b>M</b> = ±20%. દા.ત. <b>104K</b> = 0.1 μF ± 10%.</p>"""),
    ],
}

SEC_1_4 = {
    "title": {"en": "1.4 Inductors", "gu": "1.4 ઇન્ડક્ટર"},
    "items": [
        Q("What is an inductor? Explain inductance.",
          "ઇન્ડક્ટર એટલે શું? ઇન્ડક્ટન્સ સમજાવો.",
          """<p>An <b>inductor</b> (also called a coil or choke) is a passive, two-terminal component that <b>stores energy in the form of a magnetic field</b> when current flows through it. It is made by winding an insulated copper wire on a core (air, iron or ferrite).</p>
<p><b>Inductance (L)</b> is the property of a coil by which it <b>opposes any change in the current</b> flowing through it.</p>
<ul>
<li><b>Unit:</b> Henry (H). Practical units: mH = 10⁻³ H, μH = 10⁻⁶ H.</li>
<li>Inductance of a coil: <b>L = μ₀ μᵣ N² A / l</b>, where N = number of turns, A = area of core, l = length of coil, μᵣ = relative permeability of core.</li>
<li>So inductance <b>increases</b> with more turns (∝ N²), larger area and higher permeability core (iron/ferrite).</li>
<li>Energy stored: <b>E = ½ L I²</b> joules.</li>
<li>An inductor <b>passes DC</b> easily and <b>opposes AC</b>. Inductive reactance X<sub>L</sub> = 2πfL.</li>
</ul>
<p><b>Types by core:</b> air-core (high-frequency, RF circuits), iron-core (low frequency, chokes, transformers), ferrite-core (SMPS, RF, EMI filters).</p>
<p><b>Applications:</b> filter chokes in power supplies, tuned circuits (LC), transformers, relays, SMPS, EMI suppression, fluorescent tube chokes.</p>""",
          """<p><b>ઇન્ડક્ટર</b> (જેને કોઇલ કે ચોક પણ કહે છે) એ બે ટર્મિનલ ધરાવતો પેસિવ ઘટક છે, જે તેમાંથી કરંટ વહે ત્યારે <b>ઊર્જાનો ચુંબકીય ક્ષેત્ર (મેગ્નેટિક ફિલ્ડ) સ્વરૂપે સંગ્રહ</b> કરે છે. તે કોર (હવા, લોખંડ કે ફેરાઇટ) પર અવાહક આવરણવાળો તાંબાનો તાર વીંટાળીને બનાવાય છે.</p>
<p><b>ઇન્ડક્ટન્સ (L)</b> એ કોઇલનો એવો ગુણધર્મ છે જેના કારણે તે તેમાંથી વહેતા <b>કરંટમાં થતા કોઈપણ ફેરફારનો વિરોધ</b> કરે છે.</p>
<ul>
<li><b>એકમ:</b> હેનરી (H). વ્યવહારુ એકમ: mH = 10⁻³ H, μH = 10⁻⁶ H.</li>
<li>કોઇલનું ઇન્ડક્ટન્સ: <b>L = μ₀ μᵣ N² A / l</b>, જ્યાં N = આંટાની સંખ્યા, A = કોરનું ક્ષેત્રફળ, l = કોઇલની લંબાઈ, μᵣ = કોરની સાપેક્ષ પરમિએબિલિટી.</li>
<li>તેથી વધુ આંટા (∝ N²), મોટું ક્ષેત્રફળ અને વધુ પરમિએબિલિટીવાળો કોર (લોખંડ/ફેરાઇટ) હોય તો ઇન્ડક્ટન્સ <b>વધે</b>.</li>
<li>સંગ્રહિત ઊર્જા: <b>E = ½ L I²</b> જૂલ.</li>
<li>ઇન્ડક્ટર <b>DC ને સરળતાથી પસાર</b> થવા દે છે અને <b>AC નો વિરોધ</b> કરે છે. ઇન્ડક્ટિવ રિએક્ટન્સ X<sub>L</sub> = 2πfL.</li>
</ul>
<p><b>કોર પ્રમાણે પ્રકાર:</b> એર-કોર (હાઇ-ફ્રિક્વન્સી, RF સર્કિટ), આયર્ન-કોર (ઓછી ફ્રિક્વન્સી, ચોક, ટ્રાન્સફોર્મર), ફેરાઇટ-કોર (SMPS, RF, EMI ફિલ્ટર).</p>
<p><b>ઉપયોગ:</b> પાવર સપ્લાયમાં ફિલ્ટર ચોક, ટ્યુન્ડ સર્કિટ (LC), ટ્રાન્સફોર્મર, રિલે, SMPS, EMI સપ્રેશન, ટ્યુબલાઇટ ચોક.</p>"""),

        Q("State and explain Faraday's laws of electromagnetic induction.",
          "ફેરાડેના વિદ્યુતચુંબકીય પ્રેરણના નિયમો લખો અને સમજાવો.",
          """<p><b>Faraday's First Law:</b> Whenever the <b>magnetic flux linked with a coil (conductor) changes</b>, an <b>EMF is induced</b> in it. If the circuit is closed, an induced current flows.</p>
<p>The flux can change by: (i) moving a magnet towards/away from a coil, (ii) moving the coil in a magnetic field, (iii) changing the current in a nearby coil.</p>
<p><b>Faraday's Second Law:</b> The <b>magnitude of the induced EMF is equal to the rate of change of flux linkage</b> with the coil.</p>
<p class='eq'>e = − N (dΦ / dt)</p>
<p>where e = induced EMF (V), N = number of turns, dΦ/dt = rate of change of flux (Wb/s).</p>
<p><b>Lenz's Law</b> (the minus sign): The direction of the induced EMF is such that it <b>opposes the cause</b> (change of flux) that produces it.</p>
<p><b>Applications:</b> generators, transformers, inductors, induction motors, induction cooktops, electric guitar pickups.</p>""",
          """<p><b>ફેરાડેનો પહેલો નિયમ:</b> જ્યારે પણ <b>કોઇલ (વાહક) સાથે સંકળાયેલું ચુંબકીય ફ્લક્સ બદલાય</b> છે, ત્યારે તેમાં <b>EMF પ્રેરિત</b> થાય છે. જો સર્કિટ બંધ હોય તો પ્રેરિત કરંટ વહે છે.</p>
<p>ફ્લક્સ આ રીતે બદલાઈ શકે: (i) ચુંબકને કોઇલ તરફ/દૂર ખસેડીને, (ii) ચુંબકીય ક્ષેત્રમાં કોઇલ ખસેડીને, (iii) નજીકની કોઇલમાં કરંટ બદલીને.</p>
<p><b>ફેરાડેનો બીજો નિયમ:</b> <b>પ્રેરિત EMF નું મૂલ્ય કોઇલ સાથે સંકળાયેલા ફ્લક્સ લિંકેજના ફેરફારના દર જેટલું</b> હોય છે.</p>
<p class='eq'>e = − N (dΦ / dt)</p>
<p>જ્યાં e = પ્રેરિત EMF (V), N = આંટાની સંખ્યા, dΦ/dt = ફ્લક્સ ફેરફારનો દર (Wb/s).</p>
<p><b>લેન્ઝનો નિયમ</b> (માઇનસ ચિહ્ન): પ્રેરિત EMF ની દિશા એવી હોય છે કે તે તેને ઉત્પન્ન કરનાર <b>કારણ (ફ્લક્સના ફેરફાર)નો વિરોધ</b> કરે.</p>
<p><b>ઉપયોગ:</b> જનરેટર, ટ્રાન્સફોર્મર, ઇન્ડક્ટર, ઇન્ડક્શન મોટર, ઇન્ડક્શન કૂકટોપ, ઇલેક્ટ્રિક ગિટાર પિકઅપ.</p>"""),

        Q("Explain self-inductance.",
          "સેલ્ફ-ઇન્ડક્ટન્સ (સ્વ-પ્રેરણ) સમજાવો.",
          """<p>When the current through a coil changes, the magnetic flux produced by the coil also changes. This changing flux links with the <b>same coil</b> and induces an EMF in it. This phenomenon is called <b>self-induction</b>, and the property is called <b>self-inductance (L)</b>.</p>
<p>The induced EMF opposes the change in current (Lenz's law), so it is called <b>back EMF</b>.</p>
<p class='eq'>e = − L (di / dt)</p>
<p class='eq'>L = N Φ / I</p>
<p><b>Definition of 1 Henry:</b> A coil has a self-inductance of 1 H if an EMF of <b>1 V</b> is induced in it when the current changes at the rate of <b>1 A/s</b>.</p>
<p><b>Factors affecting L:</b> number of turns (N²), area of cross-section, length of coil, permeability of core.</p>
<p><b>Example:</b> Choke in a tube light produces a high back-EMF to start the tube.</p>""",
          """<p>જ્યારે કોઇલમાંથી વહેતો કરંટ બદલાય છે, ત્યારે કોઇલ દ્વારા ઉત્પન્ન થતું ચુંબકીય ફ્લક્સ પણ બદલાય છે. આ બદલાતું ફ્લક્સ <b>તે જ કોઇલ</b> સાથે સંકળાય છે અને તેમાં EMF પ્રેરિત કરે છે. આ ઘટનાને <b>સ્વ-પ્રેરણ (સેલ્ફ-ઇન્ડક્શન)</b> અને આ ગુણધર્મને <b>સેલ્ફ-ઇન્ડક્ટન્સ (L)</b> કહે છે.</p>
<p>પ્રેરિત EMF કરંટના ફેરફારનો વિરોધ કરે છે (લેન્ઝનો નિયમ), તેથી તેને <b>બેક EMF</b> કહે છે.</p>
<p class='eq'>e = − L (di / dt)</p>
<p class='eq'>L = N Φ / I</p>
<p><b>1 હેનરીની વ્યાખ્યા:</b> જ્યારે કોઇલમાં કરંટ <b>1 A/s</b> ના દરે બદલાય ત્યારે તેમાં <b>1 V</b> EMF પ્રેરિત થાય, તો તે કોઇલનું સેલ્ફ-ઇન્ડક્ટન્સ 1 H છે.</p>
<p><b>L ને અસર કરતા પરિબળો:</b> આંટાની સંખ્યા (N²), આડછેદનું ક્ષેત્રફળ, કોઇલની લંબાઈ, કોરની પરમિએબિલિટી.</p>
<p><b>ઉદાહરણ:</b> ટ્યુબલાઇટનો ચોક ટ્યુબ ચાલુ કરવા ઊંચો બેક-EMF ઉત્પન્ન કરે છે.</p>"""),

        Q("Explain mutual inductance.",
          "મ્યુચ્યુઅલ ઇન્ડક્ટન્સ (પરસ્પર પ્રેરણ) સમજાવો.",
          """<p>When two coils are placed close to each other, a change of current in the <b>first coil (primary)</b> produces a changing flux which links with the <b>second coil (secondary)</b> and induces an EMF in it. This phenomenon is called <b>mutual induction</b>, and the property is called <b>mutual inductance (M)</b>.</p>
<p class='eq'>e₂ = − M (di₁ / dt)</p>
<p class='eq'>M = k √(L₁ L₂)</p>
<ul>
<li>e₂ = EMF induced in secondary coil, di₁/dt = rate of change of current in primary.</li>
<li><b>k = coefficient of coupling</b> (0 to 1). k = 1 means all flux of coil 1 links coil 2 (tight coupling, iron core). k close to 0 means loose coupling.</li>
<li><b>Unit:</b> Henry (H). Two coils have M = 1 H if 1 A/s change in one coil induces 1 V in the other.</li>
</ul>
<p><b>Factors affecting M:</b> number of turns of both coils, distance between coils, their orientation (alignment), and core material.</p>
<p><b>Applications:</b> <b>transformer</b> (main application), induction coil, wireless/mobile chargers, current transformers.</p>""",
          """<p>જ્યારે બે કોઇલ એકબીજાની નજીક મૂકેલી હોય, ત્યારે <b>પહેલી કોઇલ (પ્રાઇમરી)</b>માં કરંટનો ફેરફાર બદલાતું ફ્લક્સ ઉત્પન્ન કરે છે, જે <b>બીજી કોઇલ (સેકન્ડરી)</b> સાથે સંકળાઈને તેમાં EMF પ્રેરિત કરે છે. આ ઘટનાને <b>પરસ્પર પ્રેરણ (મ્યુચ્યુઅલ ઇન્ડક્શન)</b> અને આ ગુણધર્મને <b>મ્યુચ્યુઅલ ઇન્ડક્ટન્સ (M)</b> કહે છે.</p>
<p class='eq'>e₂ = − M (di₁ / dt)</p>
<p class='eq'>M = k √(L₁ L₂)</p>
<ul>
<li>e₂ = સેકન્ડરી કોઇલમાં પ્રેરિત EMF, di₁/dt = પ્રાઇમરીમાં કરંટ ફેરફારનો દર.</li>
<li><b>k = કપલિંગ ગુણાંક</b> (0 થી 1). k = 1 એટલે કોઇલ 1 નું બધું ફ્લક્સ કોઇલ 2 સાથે સંકળાય (ટાઇટ કપલિંગ, આયર્ન કોર). k શૂન્યની નજીક એટલે લૂઝ કપલિંગ.</li>
<li><b>એકમ:</b> હેનરી (H). એક કોઇલમાં 1 A/s ફેરફારથી બીજીમાં 1 V પ્રેરિત થાય તો M = 1 H.</li>
</ul>
<p><b>M ને અસર કરતા પરિબળો:</b> બંને કોઇલના આંટાની સંખ્યા, કોઇલો વચ્ચેનું અંતર, તેમની ગોઠવણ (દિશા) અને કોરનો પદાર્થ.</p>
<p><b>ઉપયોગ:</b> <b>ટ્રાન્સફોર્મર</b> (મુખ્ય ઉપયોગ), ઇન્ડક્શન કોઇલ, વાયરલેસ/મોબાઇલ ચાર્જર, કરંટ ટ્રાન્સફોર્મર.</p>""",
          diagram="u1_mutual_induction"),

        Q("Explain the specifications of an inductor.",
          "ઇન્ડક્ટરના સ્પેસિફિકેશન્સ સમજાવો.",
          """<ol>
<li><b>Inductance value:</b> Nominal inductance in μH, mH or H, e.g. 100 μH.</li>
<li><b>Tolerance:</b> Allowed variation from nominal value, e.g. ±5%, ±10%, ±20%.</li>
<li><b>Current rating:</b> Maximum current the inductor can carry without overheating or <b>core saturation</b>.</li>
<li><b>DC resistance (DCR):</b> Resistance of the copper winding. Lower DCR means lower power loss.</li>
<li><b>Quality factor (Q):</b> Ratio of inductive reactance to resistance, <b>Q = X<sub>L</sub> / R = 2πfL / R</b>. Higher Q = better (lower loss) inductor.</li>
<li><b>Self-resonant frequency (SRF):</b> Frequency at which the inductor's own winding capacitance resonates with its inductance; above it the inductor stops behaving as an inductor.</li>
<li><b>Core material:</b> air, iron or ferrite – decides frequency range and inductance.</li>
<li><b>Operating temperature range.</b></li>
</ol>""",
          """<ol>
<li><b>ઇન્ડક્ટન્સ મૂલ્ય:</b> μH, mH કે H માં નામાંકિત ઇન્ડક્ટન્સ, દા.ત. 100 μH.</li>
<li><b>ટોલરન્સ:</b> નામાંકિત મૂલ્યથી માન્ય ફેરફાર, દા.ત. ±5%, ±10%, ±20%.</li>
<li><b>કરંટ રેટિંગ:</b> વધુ ગરમ થયા વગર કે <b>કોર સેચ્યુરેશન</b> વગર ઇન્ડક્ટર વહન કરી શકે તેવો મહત્તમ કરંટ.</li>
<li><b>DC રેઝિસ્ટન્સ (DCR):</b> તાંબાના વાઇન્ડિંગનો અવરોધ. ઓછો DCR એટલે ઓછો પાવર લોસ.</li>
<li><b>ક્વોલિટી ફેક્ટર (Q):</b> ઇન્ડક્ટિવ રિએક્ટન્સ અને અવરોધનો ગુણોત્તર, <b>Q = X<sub>L</sub> / R = 2πfL / R</b>. વધુ Q = વધુ સારો (ઓછા લોસવાળો) ઇન્ડક્ટર.</li>
<li><b>સેલ્ફ-રેઝોનન્ટ ફ્રિક્વન્સી (SRF):</b> જે ફ્રિક્વન્સીએ ઇન્ડક્ટરના વાઇન્ડિંગનું પોતાનું કેપેસિટન્સ તેના ઇન્ડક્ટન્સ સાથે રેઝોનન્સમાં આવે; તેથી વધુ ફ્રિક્વન્સીએ તે ઇન્ડક્ટર તરીકે વર્તતો નથી.</li>
<li><b>કોરનો પદાર્થ:</b> હવા, લોખંડ કે ફેરાઇટ – ફ્રિક્વન્સી રેન્જ અને ઇન્ડક્ટન્સ નક્કી કરે છે.</li>
<li><b>ઓપરેટિંગ તાપમાન રેન્જ.</b></li>
</ol>"""),

        Q("Differentiate between resistor, capacitor and inductor.",
          "રેઝિસ્ટર, કેપેસિટર અને ઇન્ડક્ટર વચ્ચેનો તફાવત લખો.",
          """<table>
<tr><th>Point</th><th>Resistor</th><th>Capacitor</th><th>Inductor</th></tr>
<tr><td>Function</td><td>Opposes flow of current</td><td>Stores energy in electric field</td><td>Stores energy in magnetic field</td></tr>
<tr><td>Symbol letter</td><td>R</td><td>C</td><td>L</td></tr>
<tr><td>Unit</td><td>Ohm (Ω)</td><td>Farad (F)</td><td>Henry (H)</td></tr>
<tr><td>Energy</td><td>Dissipated as heat (P = I²R)</td><td>Stored: ½CV²</td><td>Stored: ½LI²</td></tr>
<tr><td>Behaviour with DC</td><td>Opposes equally</td><td>Blocks DC (open circuit)</td><td>Passes DC (short circuit)</td></tr>
<tr><td>Behaviour with AC</td><td>Same opposition at all frequencies</td><td>Passes AC; X<sub>C</sub> = 1/(2πfC) decreases with f</td><td>Opposes AC; X<sub>L</sub> = 2πfL increases with f</td></tr>
<tr><td>Opposes change in</td><td>–</td><td>Voltage</td><td>Current</td></tr>
<tr><td>Phase (in AC)</td><td>V and I in phase</td><td>I leads V by 90°</td><td>I lags V by 90°</td></tr>
<tr><td>Applications</td><td>Current limiting, voltage divider, biasing</td><td>Filter, coupling, timing, tuning</td><td>Choke, transformer, filter, tuning</td></tr>
</table>""",
          """<table>
<tr><th>મુદ્દો</th><th>રેઝિસ્ટર</th><th>કેપેસિટર</th><th>ઇન્ડક્ટર</th></tr>
<tr><td>કાર્ય</td><td>કરંટના વહનનો વિરોધ</td><td>વિદ્યુત ક્ષેત્રમાં ઊર્જા સંગ્રહ</td><td>ચુંબકીય ક્ષેત્રમાં ઊર્જા સંગ્રહ</td></tr>
<tr><td>સંજ્ઞા અક્ષર</td><td>R</td><td>C</td><td>L</td></tr>
<tr><td>એકમ</td><td>ઓહ્મ (Ω)</td><td>ફેરાડ (F)</td><td>હેનરી (H)</td></tr>
<tr><td>ઊર્જા</td><td>ઉષ્મા રૂપે વપરાય (P = I²R)</td><td>સંગ્રહ: ½CV²</td><td>સંગ્રહ: ½LI²</td></tr>
<tr><td>DC સાથે વર્તન</td><td>સમાન વિરોધ</td><td>DC ને રોકે (ઓપન સર્કિટ)</td><td>DC પસાર કરે (શોર્ટ સર્કિટ)</td></tr>
<tr><td>AC સાથે વર્તન</td><td>બધી ફ્રિક્વન્સીએ સમાન વિરોધ</td><td>AC પસાર કરે; X<sub>C</sub> = 1/(2πfC), f વધે તેમ ઘટે</td><td>AC નો વિરોધ; X<sub>L</sub> = 2πfL, f વધે તેમ વધે</td></tr>
<tr><td>શેના ફેરફારનો વિરોધ</td><td>–</td><td>વોલ્ટેજ</td><td>કરંટ</td></tr>
<tr><td>ફેઝ (AC માં)</td><td>V અને I એક જ ફેઝમાં</td><td>I, V કરતાં 90° આગળ</td><td>I, V કરતાં 90° પાછળ</td></tr>
<tr><td>ઉપયોગ</td><td>કરંટ લિમિટિંગ, વોલ્ટેજ ડિવાઇડર, બાયસિંગ</td><td>ફિલ્ટર, કપલિંગ, ટાઇમિંગ, ટ્યુનિંગ</td><td>ચોક, ટ્રાન્સફોર્મર, ફિલ્ટર, ટ્યુનિંગ</td></tr>
</table>"""),
    ],
}

SEC_1_5 = {
    "title": {"en": "1.5 DC & AC Power Supply", "gu": "1.5 DC અને AC પાવર સપ્લાય"},
    "items": [
        Q("What are AC and DC? Compare them.",
          "AC અને DC એટલે શું? તેમની સરખામણી કરો.",
          """<p><b>DC (Direct Current):</b> Current that flows in <b>one direction only</b> and its magnitude is (ideally) constant. Sources: batteries, cells, solar cells, DC generators, rectifier circuits.</p>
<p><b>AC (Alternating Current):</b> Current that <b>changes its direction periodically</b>, and its magnitude varies continuously (sinusoidally). Source: AC generators (alternators), mains supply. In India, mains supply is <b>230 V, 50 Hz</b> single-phase.</p>
<table>
<tr><th>Point</th><th>AC</th><th>DC</th></tr>
<tr><td>Direction</td><td>Changes periodically</td><td>Always the same</td></tr>
<tr><td>Frequency</td><td>50 Hz (India), 60 Hz (USA)</td><td>Zero</td></tr>
<tr><td>Waveform</td><td>Sinusoidal</td><td>Straight line</td></tr>
<tr><td>Voltage change</td><td>Easily stepped up/down using transformer</td><td>Cannot use a transformer directly</td></tr>
<tr><td>Transmission</td><td>Economical over long distance</td><td>Costly (except HVDC)</td></tr>
<tr><td>Storage</td><td>Cannot be stored</td><td>Can be stored in batteries</td></tr>
<tr><td>Source</td><td>Alternator, mains</td><td>Battery, cell, solar cell, rectifier</td></tr>
<tr><td>Used in</td><td>Homes, industries, motors, fans</td><td>Electronic circuits, computers, mobiles, electroplating</td></tr>
</table>""",
          """<p><b>DC (ડાયરેક્ટ કરંટ):</b> જે કરંટ <b>માત્ર એક જ દિશામાં</b> વહે છે અને તેનું મૂલ્ય (આદર્શ રીતે) અચળ હોય છે. સ્રોત: બેટરી, સેલ, સોલર સેલ, DC જનરેટર, રેક્ટિફાયર સર્કિટ.</p>
<p><b>AC (આલ્ટરનેટિંગ કરંટ):</b> જે કરંટ <b>નિયમિત સમયાંતરે પોતાની દિશા બદલે</b> છે અને તેનું મૂલ્ય સતત (સાઇન તરંગ પ્રમાણે) બદલાય છે. સ્રોત: AC જનરેટર (ઓલ્ટરનેટર), મેઇન્સ સપ્લાય. ભારતમાં મેઇન્સ સપ્લાય <b>230 V, 50 Hz</b> સિંગલ-ફેઝ છે.</p>
<table>
<tr><th>મુદ્દો</th><th>AC</th><th>DC</th></tr>
<tr><td>દિશા</td><td>નિયમિત બદલાય</td><td>હંમેશા એક જ</td></tr>
<tr><td>ફ્રિક્વન્સી</td><td>50 Hz (ભારત), 60 Hz (USA)</td><td>શૂન્ય</td></tr>
<tr><td>તરંગ</td><td>સાઇન તરંગ</td><td>સીધી રેખા</td></tr>
<tr><td>વોલ્ટેજ ફેરફાર</td><td>ટ્રાન્સફોર્મરથી સરળતાથી વધારી/ઘટાડી શકાય</td><td>સીધું ટ્રાન્સફોર્મર વાપરી ન શકાય</td></tr>
<tr><td>વહન (ટ્રાન્સમિશન)</td><td>લાંબા અંતર માટે કરકસરયુક્ત</td><td>ખર્ચાળ (HVDC સિવાય)</td></tr>
<tr><td>સંગ્રહ</td><td>સંગ્રહ ન થઈ શકે</td><td>બેટરીમાં સંગ્રહ થઈ શકે</td></tr>
<tr><td>સ્રોત</td><td>ઓલ્ટરનેટર, મેઇન્સ</td><td>બેટરી, સેલ, સોલર સેલ, રેક્ટિફાયર</td></tr>
<tr><td>ઉપયોગ</td><td>ઘર, ઉદ્યોગ, મોટર, પંખા</td><td>ઇલેક્ટ્રોનિક સર્કિટ, કમ્પ્યુટર, મોબાઇલ, ઇલેક્ટ્રોપ્લેટિંગ</td></tr>
</table>"""),

        Q("Draw and explain the block diagram of a regulated DC power supply.",
          "રેગ્યુલેટેડ DC પાવર સપ્લાયનો બ્લોક ડાયાગ્રામ દોરો અને સમજાવો.",
          """<p>Electronic circuits need a <b>steady, low-voltage DC</b> (e.g. 5 V, 12 V), but mains gives 230 V AC. A <b>DC power supply</b> converts AC mains into regulated DC. It has the following blocks:</p>
<ol>
<li><b>Step-down transformer:</b> Reduces 230 V AC mains to a <b>low AC voltage</b> (e.g. 12 V AC) as required. It also <b>isolates</b> the circuit from the mains for safety.</li>
<li><b>Rectifier:</b> Converts AC into <b>pulsating DC</b> (unidirectional but not steady) using diodes. Types: half-wave, full-wave centre-tap, and bridge rectifier.</li>
<li><b>Filter:</b> Removes the AC ripple from pulsating DC and gives <b>smooth DC with small ripple</b>. A large electrolytic capacitor is commonly used (capacitor filter); LC and π filters are also used.</li>
<li><b>Voltage regulator:</b> Keeps the output DC voltage <b>constant</b> even if the input mains voltage or the load current changes. e.g. Zener diode regulator, IC 7805 (+5 V), 7812 (+12 V), LM317 (adjustable).</li>
<li><b>Load:</b> The electronic circuit/device that uses the regulated DC output.</li>
</ol>
<p><b>Waveforms:</b> AC (230 V) → small AC → pulsating DC → DC with ripple → pure DC (see diagram).</p>
<p><b>Applications:</b> mobile chargers, computers (SMPS), TV, laboratory DC supplies, battery chargers.</p>""",
          """<p>ઇલેક્ટ્રોનિક સર્કિટને <b>સ્થિર, ઓછા વોલ્ટેજનો DC</b> (દા.ત. 5 V, 12 V) જોઈએ છે, પરંતુ મેઇન્સ 230 V AC આપે છે. <b>DC પાવર સપ્લાય</b> AC મેઇન્સને રેગ્યુલેટેડ DC માં ફેરવે છે. તેમાં નીચેના બ્લોક હોય છે:</p>
<ol>
<li><b>સ્ટેપ-ડાઉન ટ્રાન્સફોર્મર:</b> 230 V AC મેઇન્સને જરૂર મુજબ <b>ઓછા AC વોલ્ટેજ</b> (દા.ત. 12 V AC)માં ઘટાડે છે. સલામતી માટે સર્કિટને મેઇન્સથી <b>અલગ (આઇસોલેટ)</b> પણ કરે છે.</li>
<li><b>રેક્ટિફાયર:</b> ડાયોડની મદદથી AC ને <b>પલ્સેટિંગ DC</b> (એક દિશામાં પણ સ્થિર નહીં) માં ફેરવે છે. પ્રકાર: હાફ-વેવ, ફુલ-વેવ સેન્ટર-ટેપ અને બ્રિજ રેક્ટિફાયર.</li>
<li><b>ફિલ્ટર:</b> પલ્સેટિંગ DC માંથી AC રિપલ દૂર કરીને <b>ઓછા રિપલવાળો સ્મૂધ DC</b> આપે છે. સામાન્ય રીતે મોટો ઇલેક્ટ્રોલિટિક કેપેસિટર વપરાય છે (કેપેસિટર ફિલ્ટર); LC અને π ફિલ્ટર પણ વપરાય છે.</li>
<li><b>વોલ્ટેજ રેગ્યુલેટર:</b> ઇનપુટ મેઇન્સ વોલ્ટેજ કે લોડ કરંટ બદલાય તો પણ આઉટપુટ DC વોલ્ટેજ <b>અચળ</b> રાખે છે. દા.ત. ઝેનર ડાયોડ રેગ્યુલેટર, IC 7805 (+5 V), 7812 (+12 V), LM317 (એડજસ્ટેબલ).</li>
<li><b>લોડ:</b> રેગ્યુલેટેડ DC આઉટપુટ વાપરતી ઇલેક્ટ્રોનિક સર્કિટ/ડિવાઇસ.</li>
</ol>
<p><b>તરંગો:</b> AC (230 V) → નાનો AC → પલ્સેટિંગ DC → રિપલવાળો DC → શુદ્ધ DC (આકૃતિ જુઓ).</p>
<p><b>ઉપયોગ:</b> મોબાઇલ ચાર્જર, કમ્પ્યુટર (SMPS), ટીવી, લેબોરેટરી DC સપ્લાય, બેટરી ચાર્જર.</p>""",
          diagram="u1_dc_power_supply"),

        Q("Compare AC power supply and DC power supply.",
          "AC પાવર સપ્લાય અને DC પાવર સપ્લાયની સરખામણી કરો.",
          """<table>
<tr><th>Point</th><th>AC Power Supply</th><th>DC Power Supply</th></tr>
<tr><td>Output</td><td>Alternating voltage (sine wave)</td><td>Constant (unidirectional) voltage</td></tr>
<tr><td>Source</td><td>Power stations / alternators, mains socket (230 V, 50 Hz), inverter, UPS</td><td>Battery, cell, solar panel, adapter / rectifier-based supply</td></tr>
<tr><td>Polarity</td><td>No fixed polarity (phase, neutral)</td><td>Fixed polarity (+ and −)</td></tr>
<tr><td>Frequency</td><td>50 Hz / 60 Hz</td><td>0 Hz</td></tr>
<tr><td>Voltage conversion</td><td>Easy using transformer</td><td>Needs DC–DC converter</td></tr>
<tr><td>Components needed</td><td>Generator, transformer</td><td>Transformer + rectifier + filter + regulator</td></tr>
<tr><td>Storage</td><td>Not possible</td><td>Possible in batteries</td></tr>
<tr><td>Applications</td><td>Fans, motors, AC, refrigerators, lighting</td><td>Computers, mobiles, ICs, LEDs, electronic circuits</td></tr>
</table>
<p><b>Conclusion:</b> AC is best for <b>generation and transmission</b> of power, while DC is required for <b>operating electronic devices</b>. That is why every electronic device has a DC power supply (adapter/SMPS) inside or outside it.</p>""",
          """<table>
<tr><th>મુદ્દો</th><th>AC પાવર સપ્લાય</th><th>DC પાવર સપ્લાય</th></tr>
<tr><td>આઉટપુટ</td><td>બદલાતો વોલ્ટેજ (સાઇન તરંગ)</td><td>અચળ (એક દિશાનો) વોલ્ટેજ</td></tr>
<tr><td>સ્રોત</td><td>પાવર સ્ટેશન / ઓલ્ટરનેટર, મેઇન્સ સોકેટ (230 V, 50 Hz), ઇન્વર્ટર, UPS</td><td>બેટરી, સેલ, સોલર પેનલ, એડેપ્ટર / રેક્ટિફાયર આધારિત સપ્લાય</td></tr>
<tr><td>પોલારિટી</td><td>નિશ્ચિત પોલારિટી નથી (ફેઝ, ન્યુટ્રલ)</td><td>નિશ્ચિત પોલારિટી (+ અને −)</td></tr>
<tr><td>ફ્રિક્વન્સી</td><td>50 Hz / 60 Hz</td><td>0 Hz</td></tr>
<tr><td>વોલ્ટેજ રૂપાંતર</td><td>ટ્રાન્સફોર્મરથી સરળ</td><td>DC–DC કન્વર્ટર જોઈએ</td></tr>
<tr><td>જરૂરી ઘટકો</td><td>જનરેટર, ટ્રાન્સફોર્મર</td><td>ટ્રાન્સફોર્મર + રેક્ટિફાયર + ફિલ્ટર + રેગ્યુલેટર</td></tr>
<tr><td>સંગ્રહ</td><td>શક્ય નથી</td><td>બેટરીમાં શક્ય</td></tr>
<tr><td>ઉપયોગ</td><td>પંખા, મોટર, AC, ફ્રિજ, લાઇટિંગ</td><td>કમ્પ્યુટર, મોબાઇલ, IC, LED, ઇલેક્ટ્રોનિક સર્કિટ</td></tr>
</table>
<p><b>નિષ્કર્ષ:</b> પાવરના <b>ઉત્પાદન અને વહન</b> માટે AC શ્રેષ્ઠ છે, જ્યારે <b>ઇલેક્ટ્રોનિક ડિવાઇસ ચલાવવા</b> માટે DC જરૂરી છે. તેથી દરેક ઇલેક્ટ્રોનિક ડિવાઇસમાં અંદર કે બહાર DC પાવર સપ્લાય (એડેપ્ટર/SMPS) હોય છે.</p>"""),
    ],
}
