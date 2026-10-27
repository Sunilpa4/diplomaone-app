"""Basics of Electronics (DI01000151) - Unit 1 notes, topics 1.1 and 1.2"""


def Q(q_en, q_gu, a_en, a_gu, diagram=None, marks=None):
    d = {"q": {"en": q_en, "gu": q_gu}, "a": {"en": a_en, "gu": a_gu}}
    if diagram:
        d["diagram"] = diagram
    if marks:
        d["marks"] = marks
    return d


SEC_1_1 = {
    "title": {"en": "1.1 Introduction to Electronics", "gu": "1.1 ઇલેક્ટ્રોનિક્સનો પરિચય"},
    "items": [
        Q("What is electronics? Write its applications.",
          "ઇલેક્ટ્રોનિક્સ એટલે શું? તેના ઉપયોગો લખો.",
          """<p><b>Electronics</b> is the branch of engineering that deals with the <b>flow and control of electrons</b> through semiconductor devices, vacuum tubes and gases, and with circuits made from these devices.</p>
<p>Electrical engineering mainly deals with generation and transmission of power, while electronics deals with <b>controlling small currents and voltages</b> to process signals and information.</p>
<p><b>Applications of electronics:</b></p>
<ul>
<li><b>Communication:</b> mobile phones, radio, TV, satellite, internet, optical fibre.</li>
<li><b>Computers &amp; IT:</b> computers, laptops, servers, printers, storage devices.</li>
<li><b>Consumer electronics:</b> TV, washing machine, microwave oven, music systems, smart watches.</li>
<li><b>Medical:</b> ECG, X-ray, CT scan, MRI, pacemaker, BP monitor.</li>
<li><b>Industrial:</b> PLC, automation, robotics, motor speed control, CNC machines.</li>
<li><b>Defence:</b> RADAR, missiles guidance, night-vision devices.</li>
<li><b>Automobile:</b> engine control unit (ECU), ABS, airbags, GPS navigation.</li>
</ul>""",
          """<p><b>ઇલેક્ટ્રોનિક્સ</b> એ એન્જિનિયરિંગની એવી શાખા છે જેમાં સેમિકન્ડક્ટર ડિવાઇસ, વેક્યુમ ટ્યુબ અને વાયુઓ દ્વારા <b>ઇલેક્ટ્રોનના વહન અને તેના નિયંત્રણ</b>નો તથા આવા ડિવાઇસથી બનતી સર્કિટનો અભ્યાસ થાય છે.</p>
<p>ઇલેક્ટ્રિકલ એન્જિનિયરિંગ મુખ્યત્વે પાવરના ઉત્પાદન અને વહન સાથે સંકળાયેલું છે, જ્યારે ઇલેક્ટ્રોનિક્સ સિગ્નલ અને માહિતીની પ્રક્રિયા માટે <b>નાના કરંટ અને વોલ્ટેજના નિયંત્રણ</b> સાથે સંકળાયેલું છે.</p>
<p><b>ઇલેક્ટ્રોનિક્સના ઉપયોગો:</b></p>
<ul>
<li><b>કમ્યુનિકેશન:</b> મોબાઇલ ફોન, રેડિયો, ટીવી, સેટેલાઇટ, ઇન્ટરનેટ, ઓપ્ટિકલ ફાઇબર.</li>
<li><b>કમ્પ્યુટર અને IT:</b> કમ્પ્યુટર, લેપટોપ, સર્વર, પ્રિન્ટર, સ્ટોરેજ ડિવાઇસ.</li>
<li><b>ઘરવપરાશ:</b> ટીવી, વોશિંગ મશીન, માઇક્રોવેવ ઓવન, મ્યુઝિક સિસ્ટમ, સ્માર્ટ વોચ.</li>
<li><b>મેડિકલ:</b> ECG, X-ray, CT સ્કેન, MRI, પેસમેકર, BP મોનિટર.</li>
<li><b>ઔદ્યોગિક:</b> PLC, ઓટોમેશન, રોબોટિક્સ, મોટર સ્પીડ કંટ્રોલ, CNC મશીન.</li>
<li><b>સંરક્ષણ:</b> RADAR, મિસાઇલ ગાઇડન્સ, નાઇટ-વિઝન ડિવાઇસ.</li>
<li><b>ઓટોમોબાઇલ:</b> એન્જિન કંટ્રોલ યુનિટ (ECU), ABS, એરબેગ, GPS નેવિગેશન.</li>
</ul>"""),

        Q("Write a brief history of electronic components.",
          "ઇલેક્ટ્રોનિક ઘટકોનો સંક્ષિપ્ત ઇતિહાસ લખો.",
          """<table>
<tr><th>Year</th><th>Development</th></tr>
<tr><td>1897</td><td>J. J. Thomson discovered the <b>electron</b>.</td></tr>
<tr><td>1904</td><td>J. A. Fleming invented the <b>vacuum tube diode</b> (Fleming valve).</td></tr>
<tr><td>1906</td><td>Lee De Forest invented the <b>triode</b> vacuum tube, which could amplify signals.</td></tr>
<tr><td>1947</td><td>Bardeen, Brattain and Shockley invented the <b>transistor</b> at Bell Labs.</td></tr>
<tr><td>1958–59</td><td>Jack Kilby (Texas Instruments) and Robert Noyce (Fairchild) developed the <b>Integrated Circuit (IC)</b>.</td></tr>
<tr><td>1971</td><td>Intel introduced the first <b>microprocessor</b> (Intel 4004).</td></tr>
<tr><td>Today</td><td>SMD components, VLSI chips with billions of transistors, nano-electronics.</td></tr>
</table>
<p><b>Trend:</b> components have become <b>smaller, faster, cheaper, more reliable</b> and consume <b>less power</b>.</p>""",
          """<table>
<tr><th>વર્ષ</th><th>વિકાસ</th></tr>
<tr><td>1897</td><td>જે. જે. થોમસને <b>ઇલેક્ટ્રોન</b>ની શોધ કરી.</td></tr>
<tr><td>1904</td><td>જે. એ. ફ્લેમિંગે <b>વેક્યુમ ટ્યુબ ડાયોડ</b> (ફ્લેમિંગ વાલ્વ)ની શોધ કરી.</td></tr>
<tr><td>1906</td><td>લી ડી ફોરેસ્ટે <b>ટ્રાયોડ</b> વેક્યુમ ટ્યુબની શોધ કરી, જે સિગ્નલને એમ્પ્લિફાય કરી શકતી હતી.</td></tr>
<tr><td>1947</td><td>બાર્ડીન, બ્રેટન અને શોકલીએ બેલ લેબમાં <b>ટ્રાન્ઝિસ્ટર</b>ની શોધ કરી.</td></tr>
<tr><td>1958–59</td><td>જેક કિલ્બી (Texas Instruments) અને રોબર્ટ નોયસ (Fairchild)એ <b>ઇન્ટિગ્રેટેડ સર્કિટ (IC)</b> વિકસાવી.</td></tr>
<tr><td>1971</td><td>ઇન્ટેલે પહેલું <b>માઇક્રોપ્રોસેસર</b> (Intel 4004) રજૂ કર્યું.</td></tr>
<tr><td>આજે</td><td>SMD ઘટકો, અબજો ટ્રાન્ઝિસ્ટર ધરાવતી VLSI ચિપ, નેનો-ઇલેક્ટ્રોનિક્સ.</td></tr>
</table>
<p><b>વલણ:</b> ઘટકો સમય સાથે <b>નાના, ઝડપી, સસ્તા, વધુ વિશ્વસનીય</b> અને <b>ઓછો પાવર</b> વાપરતા બન્યા છે.</p>"""),

        Q("Define active and passive components with examples.",
          "એક્ટિવ અને પેસિવ ઘટકોની ઉદાહરણ સાથે વ્યાખ્યા આપો.",
          """<p><b>Active components:</b> Components that can <b>control the flow of current</b>, and can <b>amplify</b> a signal or produce power gain. They need an external power source (biasing) to work.</p>
<p><i>Examples:</i> Diode, Transistor (BJT, FET), SCR, Integrated Circuits (ICs), vacuum tubes, batteries/cells (energy sources).</p>
<p><b>Passive components:</b> Components that <b>cannot amplify</b> a signal or produce power gain. They can only <b>consume, store or release</b> energy. They do not need any external power source to work.</p>
<p><i>Examples:</i> Resistor (R), Capacitor (C), Inductor (L), Transformer.</p>""",
          """<p><b>એક્ટિવ ઘટકો:</b> જે ઘટકો <b>કરંટના વહનને નિયંત્રિત</b> કરી શકે અને સિગ્નલને <b>એમ્પ્લિફાય</b> કરી શકે (પાવર ગેઇન આપી શકે) તેને એક્ટિવ ઘટકો કહે છે. તેમને કાર્ય કરવા માટે બાહ્ય પાવર સ્રોત (બાયસિંગ)ની જરૂર પડે છે.</p>
<p><i>ઉદાહરણ:</i> ડાયોડ, ટ્રાન્ઝિસ્ટર (BJT, FET), SCR, ઇન્ટિગ્રેટેડ સર્કિટ (IC), વેક્યુમ ટ્યુબ, બેટરી/સેલ (ઊર્જા સ્રોત).</p>
<p><b>પેસિવ ઘટકો:</b> જે ઘટકો સિગ્નલને <b>એમ્પ્લિફાય કરી શકતા નથી</b>, પરંતુ માત્ર ઊર્જાનો <b>વપરાશ, સંગ્રહ અથવા મુક્ત</b> કરી શકે છે તેને પેસિવ ઘટકો કહે છે. તેમને કાર્ય કરવા બાહ્ય પાવર સ્રોતની જરૂર નથી.</p>
<p><i>ઉદાહરણ:</i> રેઝિસ્ટર (R), કેપેસિટર (C), ઇન્ડક્ટર (L), ટ્રાન્સફોર્મર.</p>"""),

        Q("Differentiate between active and passive components.",
          "એક્ટિવ અને પેસિવ ઘટકો વચ્ચેનો તફાવત લખો.",
          """<table>
<tr><th>Point</th><th>Active Components</th><th>Passive Components</th></tr>
<tr><td>Amplification</td><td>Can amplify signals (power gain &gt; 1)</td><td>Cannot amplify signals</td></tr>
<tr><td>Energy</td><td>Supply / control energy</td><td>Consume, store or release energy</td></tr>
<tr><td>External supply</td><td>Required for operation</td><td>Not required</td></tr>
<tr><td>Current control</td><td>Can control current flow (switching)</td><td>Cannot control current by another signal</td></tr>
<tr><td>Nature</td><td>Mostly non-linear</td><td>Mostly linear</td></tr>
<tr><td>Examples</td><td>Diode, transistor, IC, SCR</td><td>Resistor, capacitor, inductor, transformer</td></tr>
</table>""",
          """<table>
<tr><th>મુદ્દો</th><th>એક્ટિવ ઘટકો</th><th>પેસિવ ઘટકો</th></tr>
<tr><td>એમ્પ્લિફિકેશન</td><td>સિગ્નલ એમ્પ્લિફાય કરી શકે (પાવર ગેઇન &gt; 1)</td><td>સિગ્નલ એમ્પ્લિફાય ન કરી શકે</td></tr>
<tr><td>ઊર્જા</td><td>ઊર્જા આપે / નિયંત્રિત કરે</td><td>ઊર્જાનો વપરાશ, સંગ્રહ કે મુક્ત કરે</td></tr>
<tr><td>બાહ્ય સપ્લાય</td><td>કાર્ય માટે જરૂરી</td><td>જરૂરી નથી</td></tr>
<tr><td>કરંટ નિયંત્રણ</td><td>કરંટનું નિયંત્રણ કરી શકે (સ્વિચિંગ)</td><td>બીજા સિગ્નલ દ્વારા કરંટ નિયંત્રિત ન કરી શકે</td></tr>
<tr><td>પ્રકૃતિ</td><td>મોટે ભાગે નોન-લિનિયર</td><td>મોટે ભાગે લિનિયર</td></tr>
<tr><td>ઉદાહરણ</td><td>ડાયોડ, ટ્રાન્ઝિસ્ટર, IC, SCR</td><td>રેઝિસ્ટર, કેપેસિટર, ઇન્ડક્ટર, ટ્રાન્સફોર્મર</td></tr>
</table>"""),

        Q("Draw the symbols of resistor, capacitor and inductor (fixed and variable).",
          "રેઝિસ્ટર, કેપેસિટર અને ઇન્ડક્ટર (ફિક્સ્ડ અને વેરિએબલ)ની સંજ્ઞાઓ દોરો.",
          """<p>The standard circuit symbols of common passive components are shown in the diagram below.</p>
<ul><li>An <b>arrow across</b> the symbol means the value is <b>variable</b>.</li>
<li>The <b>"+" sign</b> on a capacitor shows it is <b>polarized</b> (electrolytic).</li>
<li><b>Parallel lines</b> above an inductor show an <b>iron core</b>.</li></ul>""",
          """<p>સામાન્ય પેસિવ ઘટકોની પ્રમાણભૂત સર્કિટ સંજ્ઞાઓ નીચેની આકૃતિમાં દર્શાવી છે.</p>
<ul><li>સંજ્ઞા પર <b>ત્રાંસો તીર</b> હોય તો તેનું મૂલ્ય <b>બદલી શકાય (વેરિએબલ)</b> છે.</li>
<li>કેપેસિટર પર <b>"+" ચિહ્ન</b> હોય તો તે <b>પોલરાઇઝ્ડ</b> (ઇલેક્ટ્રોલિટિક) છે.</li>
<li>ઇન્ડક્ટર ઉપર <b>સમાંતર રેખાઓ</b> હોય તો તેમાં <b>આયર્ન કોર</b> છે.</li></ul>""",
          diagram="u1_symbols"),
    ],
}

SEC_1_2 = {
    "title": {"en": "1.2 Resistors", "gu": "1.2 રેઝિસ્ટર"},
    "items": [
        Q("What is a resistor? Explain the concept of resistance.",
          "રેઝિસ્ટર એટલે શું? અવરોધ (રેઝિસ્ટન્સ)નો ખ્યાલ સમજાવો.",
          """<p>A <b>resistor</b> is a passive, two-terminal component that <b>opposes (resists) the flow of electric current</b> in a circuit. The property of opposing current is called <b>resistance</b>.</p>
<ul>
<li><b>Symbol:</b> R &nbsp;&nbsp; <b>Unit:</b> Ohm (Ω). Larger units: kΩ = 10<sup>3</sup> Ω, MΩ = 10<sup>6</sup> Ω.</li>
<li><b>Ohm's law:</b> V = I × R, so R = V / I.</li>
<li>Resistance of a conductor: <b>R = ρL / A</b>, where ρ = resistivity (Ω·m), L = length (m), A = cross-sectional area (m²).</li>
<li>So resistance <b>increases with length</b> and <b>decreases with area</b>.</li>
<li>Energy lost in a resistor is converted into <b>heat</b>: P = I²R watts.</li>
</ul>
<p><b>Functions of resistors:</b> limit current (e.g. LED series resistor), divide voltage (voltage divider), provide biasing to transistors, control gain, act as load, and produce heat (heaters).</p>""",
          """<p><b>રેઝિસ્ટર</b> એ બે ટર્મિનલ ધરાવતો પેસિવ ઘટક છે, જે સર્કિટમાં <b>વિદ્યુત પ્રવાહના વહનનો વિરોધ</b> કરે છે. કરંટનો વિરોધ કરવાના ગુણધર્મને <b>અવરોધ (રેઝિસ્ટન્સ)</b> કહે છે.</p>
<ul>
<li><b>સંજ્ઞા:</b> R &nbsp;&nbsp; <b>એકમ:</b> ઓહ્મ (Ω). મોટા એકમ: kΩ = 10<sup>3</sup> Ω, MΩ = 10<sup>6</sup> Ω.</li>
<li><b>ઓહ્મનો નિયમ:</b> V = I × R, તેથી R = V / I.</li>
<li>વાહકનો અવરોધ: <b>R = ρL / A</b>, જ્યાં ρ = અવરોધકતા (Ω·m), L = લંબાઈ (m), A = આડછેદનું ક્ષેત્રફળ (m²).</li>
<li>તેથી <b>લંબાઈ વધે તો અવરોધ વધે</b> અને <b>ક્ષેત્રફળ વધે તો અવરોધ ઘટે</b>.</li>
<li>રેઝિસ્ટરમાં વપરાતી ઊર્જા <b>ઉષ્મા</b>માં ફેરવાય છે: P = I²R વોટ.</li>
</ul>
<p><b>રેઝિસ્ટરના કાર્યો:</b> કરંટ મર્યાદિત કરવો (દા.ત. LED સાથે શ્રેણીમાં રેઝિસ્ટર), વોલ્ટેજ વિભાજન (વોલ્ટેજ ડિવાઇડર), ટ્રાન્ઝિસ્ટરનું બાયસિંગ, ગેઇન નિયંત્રણ, લોડ તરીકે અને ઉષ્મા ઉત્પન્ન કરવી (હીટર).</p>"""),

        Q("Explain the specifications of a resistor.",
          "રેઝિસ્ટરના સ્પેસિફિકેશન્સ સમજાવો.",
          """<ol>
<li><b>Resistance value (Ohmic value):</b> The nominal value of resistance in Ω, kΩ or MΩ, e.g. 4.7 kΩ. It is shown by colour code or printed code.</li>
<li><b>Tolerance:</b> The maximum allowed variation of actual value from nominal value, in %. e.g. ±5% (gold), ±10% (silver), ±1% (brown). Lower tolerance = more accurate resistor.</li>
<li><b>Power rating (wattage):</b> Maximum power a resistor can dissipate without damage, e.g. 1/8 W, 1/4 W, 1/2 W, 1 W, 2 W, 5 W. Bigger size = higher wattage.</li>
<li><b>Temperature coefficient (TCR):</b> Change in resistance per °C change in temperature, in ppm/°C. Lower TCR = more stable resistor.</li>
<li><b>Maximum (working) voltage:</b> Highest voltage that can be applied across the resistor safely.</li>
<li><b>Stability:</b> Ability to keep its value constant with time, temperature and humidity.</li>
<li><b>Noise:</b> Unwanted electrical signal generated inside the resistor. Metal film resistors have low noise.</li>
</ol>""",
          """<ol>
<li><b>અવરોધ મૂલ્ય (ઓહ્મિક વેલ્યુ):</b> Ω, kΩ કે MΩ માં નામાંકિત મૂલ્ય, દા.ત. 4.7 kΩ. તે કલર કોડ અથવા છાપેલા કોડથી દર્શાવાય છે.</li>
<li><b>ટોલરન્સ:</b> વાસ્તવિક મૂલ્યમાં નામાંકિત મૂલ્યથી માન્ય મહત્તમ ફેરફાર (% માં). દા.ત. ±5% (સોનેરી), ±10% (રૂપેરી), ±1% (બ્રાઉન). ઓછું ટોલરન્સ = વધુ ચોક્કસ રેઝિસ્ટર.</li>
<li><b>પાવર રેટિંગ (વોટેજ):</b> નુકસાન વગર રેઝિસ્ટર વધુમાં વધુ કેટલો પાવર સહન (ડિસિપેટ) કરી શકે તે, દા.ત. 1/8 W, 1/4 W, 1/2 W, 1 W, 2 W, 5 W. મોટું કદ = વધુ વોટેજ.</li>
<li><b>તાપમાન ગુણાંક (TCR):</b> તાપમાનમાં 1°C ફેરફારથી અવરોધમાં થતો ફેરફાર (ppm/°C). ઓછો TCR = વધુ સ્થિર રેઝિસ્ટર.</li>
<li><b>મહત્તમ (વર્કિંગ) વોલ્ટેજ:</b> રેઝિસ્ટર પર સલામત રીતે આપી શકાય તેવો મહત્તમ વોલ્ટેજ.</li>
<li><b>સ્થિરતા (સ્ટેબિલિટી):</b> સમય, તાપમાન અને ભેજ સાથે મૂલ્ય સ્થિર રાખવાની ક્ષમતા.</li>
<li><b>નોઇઝ:</b> રેઝિસ્ટરની અંદર ઉત્પન્ન થતો અનિચ્છનીય વિદ્યુત સિગ્નલ. મેટલ ફિલ્મ રેઝિસ્ટરમાં નોઇઝ ઓછો હોય છે.</li>
</ol>"""),

        Q("Give the classification of resistors.",
          "રેઝિસ્ટરનું વર્ગીકરણ આપો.",
          """<p>Resistors are mainly classified into three types (see diagram):</p>
<ol>
<li><b>Fixed resistors</b> – value cannot be changed.
<ul><li>Carbon composition</li><li>Carbon film</li><li>Metal film / metal oxide film</li><li>Wire wound</li></ul></li>
<li><b>Variable resistors</b> – value can be changed manually.
<ul><li>Potentiometer (POT)</li><li>Rheostat</li><li>Preset / Trimmer</li></ul></li>
<li><b>Special (non-linear / dependent) resistors</b> – value changes with a physical quantity.
<ul><li>LDR – depends on light</li><li>Thermistor – depends on temperature</li><li>Varistor (VDR) – depends on voltage</li></ul></li>
</ol>""",
          """<p>રેઝિસ્ટરને મુખ્યત્વે ત્રણ પ્રકારમાં વહેંચવામાં આવે છે (આકૃતિ જુઓ):</p>
<ol>
<li><b>ફિક્સ્ડ રેઝિસ્ટર</b> – મૂલ્ય બદલી શકાતું નથી.
<ul><li>કાર્બન કમ્પોઝિશન</li><li>કાર્બન ફિલ્મ</li><li>મેટલ ફિલ્મ / મેટલ ઓક્સાઇડ ફિલ્મ</li><li>વાયર વાઉન્ડ</li></ul></li>
<li><b>વેરિએબલ રેઝિસ્ટર</b> – મૂલ્ય હાથથી બદલી શકાય છે.
<ul><li>પોટેન્શિઓમીટર (POT)</li><li>રીઓસ્ટેટ</li><li>પ્રીસેટ / ટ્રીમર</li></ul></li>
<li><b>સ્પેશિયલ (નોન-લિનિયર / આધારિત) રેઝિસ્ટર</b> – મૂલ્ય કોઈ ભૌતિક રાશિ પ્રમાણે બદલાય છે.
<ul><li>LDR – પ્રકાશ પર આધારિત</li><li>થર્મિસ્ટર – તાપમાન પર આધારિત</li><li>વેરિસ્ટર (VDR) – વોલ્ટેજ પર આધારિત</li></ul></li>
</ol>""",
          diagram="u1_resistor_tree"),

        Q("Explain fixed resistors with their applications.",
          "ફિક્સ્ડ રેઝિસ્ટર તેના ઉપયોગો સાથે સમજાવો.",
          """<p>A <b>fixed resistor</b> has a constant resistance value that cannot be changed.</p>
<p><b>1. Carbon composition resistor:</b> Made of a mixture of <b>carbon powder and a binder (resin)</b> moulded into a cylinder with leads at both ends. Range: about 1 Ω to 22 MΩ, 1/8 W to 2 W, tolerance ±5% to ±20%.<br>
<i>Advantages:</i> cheap, small, can handle short high-energy pulses. <i>Disadvantages:</i> high noise, poor stability, high tolerance.<br>
<i>Applications:</i> general-purpose circuits, surge-current circuits, old radio/TV circuits.</p>
<p><b>2. Carbon film resistor:</b> A thin <b>carbon film is deposited on a ceramic rod</b>; a spiral groove is cut to get the required value. Better stability and lower noise than carbon composition.<br><i>Applications:</i> general electronics, consumer products.</p>
<p><b>3. Metal film resistor:</b> A thin <b>metal / metal-oxide film</b> (e.g. nickel-chromium) is deposited on a ceramic rod. Tolerance ±1% or better, low noise, low TCR.<br><i>Applications:</i> precision circuits, measuring instruments, amplifiers, audio equipment.</p>
<p><b>4. Wire wound resistor:</b> A resistance wire of <b>nichrome or manganin is wound on a ceramic core</b> and coated with enamel/cement. Low values (fraction of Ω to a few kΩ) with <b>high power rating</b> (up to hundreds of watts).<br><i>Disadvantage:</i> acts like an inductor at high frequency. <i>Applications:</i> power supplies, motor control, heaters, high-current circuits.</p>""",
          """<p><b>ફિક્સ્ડ રેઝિસ્ટર</b>નું અવરોધ મૂલ્ય અચળ હોય છે, તેને બદલી શકાતું નથી.</p>
<p><b>1. કાર્બન કમ્પોઝિશન રેઝિસ્ટર:</b> <b>કાર્બન પાવડર અને બાઇન્ડર (રેઝિન)</b>ના મિશ્રણને નળાકારમાં ઢાળીને બંને છેડે લીડ લગાવીને બનાવાય છે. રેન્જ: આશરે 1 Ω થી 22 MΩ, 1/8 W થી 2 W, ટોલરન્સ ±5% થી ±20%.<br>
<i>ફાયદા:</i> સસ્તું, નાનું, ટૂંકા સમયના ઊંચા પલ્સ સહન કરી શકે. <i>ગેરફાયદા:</i> વધુ નોઇઝ, ઓછી સ્થિરતા, વધુ ટોલરન્સ.<br>
<i>ઉપયોગ:</i> સામાન્ય સર્કિટ, સર્જ-કરંટ સર્કિટ, જૂના રેડિયો/ટીવી.</p>
<p><b>2. કાર્બન ફિલ્મ રેઝિસ્ટર:</b> <b>સિરામિક સળિયા પર કાર્બનની પાતળી ફિલ્મ</b> જમાવવામાં આવે છે અને જરૂરી મૂલ્ય મેળવવા સર્પાકાર (સ્પાઇરલ) ખાંચો કાપવામાં આવે છે. કાર્બન કમ્પોઝિશન કરતાં વધુ સ્થિર અને ઓછો નોઇઝ.<br><i>ઉપયોગ:</i> સામાન્ય ઇલેક્ટ્રોનિક્સ, ઘરવપરાશનાં સાધનો.</p>
<p><b>3. મેટલ ફિલ્મ રેઝિસ્ટર:</b> સિરામિક સળિયા પર <b>ધાતુ / ધાતુ-ઓક્સાઇડની પાતળી ફિલ્મ</b> (દા.ત. નિકલ-ક્રોમિયમ) જમાવવામાં આવે છે. ટોલરન્સ ±1% કે તેથી ઓછું, ઓછો નોઇઝ, ઓછો TCR.<br><i>ઉપયોગ:</i> ચોકસાઈવાળી સર્કિટ, માપન સાધનો, એમ્પ્લિફાયર, ઓડિયો સાધનો.</p>
<p><b>4. વાયર વાઉન્ડ રેઝિસ્ટર:</b> <b>નાઇક્રોમ કે મેંગેનિનનો તાર સિરામિક કોર પર વીંટાળી</b> તેના પર ઇનેમલ/સિમેન્ટનું આવરણ કરાય છે. ઓછું મૂલ્ય (Ω ના અપૂર્ણાંકથી થોડા kΩ) પરંતુ <b>ઊંચું પાવર રેટિંગ</b> (સેંકડો વોટ સુધી).<br><i>ગેરફાયદો:</i> ઊંચી ફ્રિક્વન્સી પર ઇન્ડક્ટરની જેમ વર્તે છે. <i>ઉપયોગ:</i> પાવર સપ્લાય, મોટર કંટ્રોલ, હીટર, વધુ કરંટવાળી સર્કિટ.</p>"""),

        Q("Explain variable resistors with their applications.",
          "વેરિએબલ રેઝિસ્ટર તેના ઉપયોગો સાથે સમજાવો.",
          """<p>A <b>variable resistor</b> is a resistor whose resistance <b>can be changed</b> by rotating a knob or sliding a contact (called the <b>wiper</b>).</p>
<p><b>1. Potentiometer (POT):</b> A <b>three-terminal</b> device. The two outer terminals are connected across a carbon track and the middle terminal is the wiper. Used as a <b>voltage divider</b>.<br>
Types: <i>linear taper</i> (resistance changes uniformly) and <i>log taper</i> (used in audio).<br>
<i>Applications:</i> volume control in radio/TV/amplifiers, brightness/contrast control, tuning circuits.</p>
<p><b>2. Rheostat:</b> A <b>two-terminal</b> variable resistor, normally wire-wound, used to <b>control current</b> in high-power circuits.<br>
<i>Applications:</i> motor speed control, lamp dimmers, battery charging, laboratory experiments.</p>
<p><b>3. Preset / Trimmer:</b> A small variable resistor mounted on a PCB, adjusted with a <b>screwdriver</b>. It is set once during calibration and then left alone.<br>
<i>Applications:</i> calibration of instruments, setting the bias of transistors, fine tuning in TV and power-supply circuits.</p>""",
          """<p><b>વેરિએબલ રેઝિસ્ટર</b> એવો રેઝિસ્ટર છે જેનો અવરોધ નોબ ફેરવીને અથવા સંપર્ક (જેને <b>વાઇપર</b> કહે છે) ખસેડીને <b>બદલી શકાય</b> છે.</p>
<p><b>1. પોટેન્શિઓમીટર (POT):</b> <b>ત્રણ ટર્મિનલ</b>વાળું ડિવાઇસ. બહારના બે ટર્મિનલ કાર્બન ટ્રેકના બે છેડે જોડાયેલા હોય છે અને વચ્ચેનું ટર્મિનલ વાઇપર છે. <b>વોલ્ટેજ ડિવાઇડર</b> તરીકે વપરાય છે.<br>
પ્રકાર: <i>લિનિયર ટેપર</i> (અવરોધ એકસરખો બદલાય) અને <i>લોગ ટેપર</i> (ઓડિયોમાં વપરાય).<br>
<i>ઉપયોગ:</i> રેડિયો/ટીવી/એમ્પ્લિફાયરમાં વોલ્યુમ કંટ્રોલ, બ્રાઇટનેસ/કોન્ટ્રાસ્ટ કંટ્રોલ, ટ્યુનિંગ સર્કિટ.</p>
<p><b>2. રીઓસ્ટેટ:</b> <b>બે ટર્મિનલ</b>વાળો વેરિએબલ રેઝિસ્ટર, સામાન્ય રીતે વાયર-વાઉન્ડ, જે ઊંચા પાવરવાળી સર્કિટમાં <b>કરંટ નિયંત્રિત</b> કરવા વપરાય છે.<br>
<i>ઉપયોગ:</i> મોટર સ્પીડ કંટ્રોલ, લેમ્પ ડિમર, બેટરી ચાર્જિંગ, લેબોરેટરી પ્રયોગો.</p>
<p><b>3. પ્રીસેટ / ટ્રીમર:</b> PCB પર લગાવેલો નાનો વેરિએબલ રેઝિસ્ટર, જેને <b>સ્ક્રૂડ્રાઇવર</b>થી એડજસ્ટ કરાય છે. કેલિબ્રેશન વખતે એક વાર સેટ કરીને પછી તેને છોડી દેવાય છે.<br>
<i>ઉપયોગ:</i> સાધનોનું કેલિબ્રેશન, ટ્રાન્ઝિસ્ટરનું બાયસ સેટ કરવું, ટીવી અને પાવર-સપ્લાય સર્કિટમાં ફાઇન ટ્યુનિંગ.</p>"""),

        Q("Explain special (non-linear) resistors: LDR, thermistor and varistor.",
          "સ્પેશિયલ (નોન-લિનિયર) રેઝિસ્ટર સમજાવો: LDR, થર્મિસ્ટર અને વેરિસ્ટર.",
          """<p><b>1. LDR (Light Dependent Resistor):</b> Made of cadmium sulphide (CdS). Its resistance <b>decreases when light intensity increases</b> (very high in darkness – MΩ, low in bright light – few hundred Ω).<br><i>Applications:</i> automatic street lights, burglar alarms, light meters, camera exposure control.</p>
<p><b>2. Thermistor (Thermal resistor):</b> Its resistance changes with <b>temperature</b>.
<ul><li><b>NTC</b> (Negative Temperature Coefficient): resistance <b>decreases</b> as temperature increases.</li>
<li><b>PTC</b> (Positive Temperature Coefficient): resistance <b>increases</b> as temperature increases.</li></ul>
<i>Applications:</i> temperature measurement and control, fire alarms, over-current protection, battery charger temperature sensing.</p>
<p><b>3. Varistor / VDR (Voltage Dependent Resistor):</b> Usually made of zinc oxide (MOV). Its resistance is <b>very high at normal voltage</b> and <b>falls sharply when voltage exceeds a limit</b>, so it bypasses the surge.<br><i>Applications:</i> surge/spike protection in power supplies, extension boards, TVs and computers.</p>""",
          """<p><b>1. LDR (લાઇટ ડિપેન્ડન્ટ રેઝિસ્ટર):</b> કેડમિયમ સલ્ફાઇડ (CdS)માંથી બને છે. <b>પ્રકાશની તીવ્રતા વધે ત્યારે તેનો અવરોધ ઘટે</b> છે (અંધારામાં ખૂબ વધુ – MΩ, તેજ પ્રકાશમાં ઓછો – થોડાક સો Ω).<br><i>ઉપયોગ:</i> ઓટોમેટિક સ્ટ્રીટ લાઇટ, ચોર એલાર્મ, લાઇટ મીટર, કેમેરા એક્સપોઝર કંટ્રોલ.</p>
<p><b>2. થર્મિસ્ટર (થર્મલ રેઝિસ્ટર):</b> તેનો અવરોધ <b>તાપમાન</b> સાથે બદલાય છે.
<ul><li><b>NTC</b> (નેગેટિવ ટેમ્પરેચર કોએફિશિયન્ટ): તાપમાન વધે તેમ અવરોધ <b>ઘટે</b>.</li>
<li><b>PTC</b> (પોઝિટિવ ટેમ્પરેચર કોએફિશિયન્ટ): તાપમાન વધે તેમ અવરોધ <b>વધે</b>.</li></ul>
<i>ઉપયોગ:</i> તાપમાન માપન અને નિયંત્રણ, ફાયર એલાર્મ, ઓવર-કરંટ પ્રોટેક્શન, બેટરી ચાર્જરમાં તાપમાન સેન્સિંગ.</p>
<p><b>3. વેરિસ્ટર / VDR (વોલ્ટેજ ડિપેન્ડન્ટ રેઝિસ્ટર):</b> સામાન્ય રીતે ઝિંક ઓક્સાઇડ (MOV)માંથી બને છે. <b>સામાન્ય વોલ્ટેજે તેનો અવરોધ ખૂબ વધુ</b> હોય છે અને <b>વોલ્ટેજ મર્યાદા કરતાં વધે ત્યારે અવરોધ ઝડપથી ઘટી</b> જાય છે, જેથી સર્જ બાયપાસ થઈ જાય છે.<br><i>ઉપયોગ:</i> પાવર સપ્લાય, એક્સ્ટેન્શન બોર્ડ, ટીવી અને કમ્પ્યુટરમાં સર્જ/સ્પાઇક પ્રોટેક્શન.</p>"""),

        Q("Explain the colour coding of resistors with examples.",
          "રેઝિસ્ટરનો કલર કોડ ઉદાહરણ સાથે સમજાવો.",
          """<p>Small resistors are too small to print values on them, so the value is shown by <b>coloured bands</b>. Read the bands starting from the end <b>nearest to a band</b> (the tolerance band, gold/silver, is on the right).</p>
<p><b>Memory trick:</b> <b>B B R O Y G B V G W</b> – "<b>B</b>B <b>ROY</b> of <b>G</b>reat <b>B</b>ritain has a <b>V</b>ery <b>G</b>ood <b>W</b>ife".</p>
<table>
<tr><th>Colour</th><th>Digit</th><th>Multiplier</th><th>Tolerance</th></tr>
<tr><td>Black</td><td>0</td><td>× 1</td><td>–</td></tr>
<tr><td>Brown</td><td>1</td><td>× 10</td><td>± 1%</td></tr>
<tr><td>Red</td><td>2</td><td>× 10²</td><td>± 2%</td></tr>
<tr><td>Orange</td><td>3</td><td>× 10³</td><td>–</td></tr>
<tr><td>Yellow</td><td>4</td><td>× 10⁴</td><td>–</td></tr>
<tr><td>Green</td><td>5</td><td>× 10⁵</td><td>± 0.5%</td></tr>
<tr><td>Blue</td><td>6</td><td>× 10⁶</td><td>± 0.25%</td></tr>
<tr><td>Violet</td><td>7</td><td>× 10⁷</td><td>± 0.1%</td></tr>
<tr><td>Grey</td><td>8</td><td>× 10⁸</td><td>± 0.05%</td></tr>
<tr><td>White</td><td>9</td><td>× 10⁹</td><td>–</td></tr>
<tr><td>Gold</td><td>–</td><td>× 0.1</td><td>± 5%</td></tr>
<tr><td>Silver</td><td>–</td><td>× 0.01</td><td>± 10%</td></tr>
<tr><td>No colour</td><td>–</td><td>–</td><td>± 20%</td></tr>
</table>
<p><b>4-band code:</b> Band 1 = 1st digit, Band 2 = 2nd digit, Band 3 = multiplier, Band 4 = tolerance.</p>
<p><b>Example 1:</b> Yellow – Violet – Red – Gold<br>= 4 7 × 10² ± 5% = 4700 Ω = <b>4.7 kΩ ± 5%</b><br>Tolerance = 5% of 4700 = 235 Ω → Range: <b>4465 Ω to 4935 Ω</b>.</p>
<p><b>Example 2:</b> Brown – Black – Orange – Silver<br>= 1 0 × 10³ ± 10% = <b>10 kΩ ± 10%</b> (Range 9 kΩ to 11 kΩ).</p>
<p><b>5-band code</b> (precision resistors): Band 1, 2, 3 = digits, Band 4 = multiplier, Band 5 = tolerance.<br>
<b>Example 3:</b> Brown – Black – Black – Red – Brown = 1 0 0 × 10² ± 1% = <b>10 kΩ ± 1%</b>.</p>""",
          """<p>નાના રેઝિસ્ટર પર મૂલ્ય છાપી શકાતું નથી, તેથી મૂલ્ય <b>રંગીન પટ્ટાઓ (બેન્ડ)</b> વડે દર્શાવાય છે. જે છેડા પાસે પટ્ટો <b>નજીક</b> હોય ત્યાંથી વાંચવાનું શરૂ કરો (ટોલરન્સ બેન્ડ – સોનેરી/રૂપેરી – જમણી બાજુ હોય છે).</p>
<p><b>યાદ રાખવાની ટ્રિક:</b> <b>B B R O Y G B V G W</b> – "<b>B</b>B <b>ROY</b> of <b>G</b>reat <b>B</b>ritain has a <b>V</b>ery <b>G</b>ood <b>W</b>ife".</p>
<table>
<tr><th>રંગ</th><th>અંક</th><th>ગુણક</th><th>ટોલરન્સ</th></tr>
<tr><td>કાળો (Black)</td><td>0</td><td>× 1</td><td>–</td></tr>
<tr><td>બદામી (Brown)</td><td>1</td><td>× 10</td><td>± 1%</td></tr>
<tr><td>લાલ (Red)</td><td>2</td><td>× 10²</td><td>± 2%</td></tr>
<tr><td>નારંગી (Orange)</td><td>3</td><td>× 10³</td><td>–</td></tr>
<tr><td>પીળો (Yellow)</td><td>4</td><td>× 10⁴</td><td>–</td></tr>
<tr><td>લીલો (Green)</td><td>5</td><td>× 10⁵</td><td>± 0.5%</td></tr>
<tr><td>વાદળી (Blue)</td><td>6</td><td>× 10⁶</td><td>± 0.25%</td></tr>
<tr><td>જાંબલી (Violet)</td><td>7</td><td>× 10⁷</td><td>± 0.1%</td></tr>
<tr><td>રાખોડી (Grey)</td><td>8</td><td>× 10⁸</td><td>± 0.05%</td></tr>
<tr><td>સફેદ (White)</td><td>9</td><td>× 10⁹</td><td>–</td></tr>
<tr><td>સોનેરી (Gold)</td><td>–</td><td>× 0.1</td><td>± 5%</td></tr>
<tr><td>રૂપેરી (Silver)</td><td>–</td><td>× 0.01</td><td>± 10%</td></tr>
<tr><td>રંગ નહીં</td><td>–</td><td>–</td><td>± 20%</td></tr>
</table>
<p><b>4-બેન્ડ કોડ:</b> બેન્ડ 1 = પહેલો અંક, બેન્ડ 2 = બીજો અંક, બેન્ડ 3 = ગુણક, બેન્ડ 4 = ટોલરન્સ.</p>
<p><b>ઉદાહરણ 1:</b> પીળો – જાંબલી – લાલ – સોનેરી<br>= 4 7 × 10² ± 5% = 4700 Ω = <b>4.7 kΩ ± 5%</b><br>ટોલરન્સ = 4700 ના 5% = 235 Ω → રેન્જ: <b>4465 Ω થી 4935 Ω</b>.</p>
<p><b>ઉદાહરણ 2:</b> બદામી – કાળો – નારંગી – રૂપેરી<br>= 1 0 × 10³ ± 10% = <b>10 kΩ ± 10%</b> (રેન્જ 9 kΩ થી 11 kΩ).</p>
<p><b>5-બેન્ડ કોડ</b> (ચોકસાઈવાળા રેઝિસ્ટર): બેન્ડ 1, 2, 3 = અંક, બેન્ડ 4 = ગુણક, બેન્ડ 5 = ટોલરન્સ.<br>
<b>ઉદાહરણ 3:</b> બદામી – કાળો – કાળો – લાલ – બદામી = 1 0 0 × 10² ± 1% = <b>10 kΩ ± 1%</b>.</p>""",
          diagram="u1_colour_code"),

        Q("Explain the numerical (printed) code of resistors.",
          "રેઝિસ્ટરનો ન્યુમેરિકલ (છાપેલો) કોડ સમજાવો.",
          """<p>Bigger resistors and SMD resistors use a <b>printed number code</b>.</p>
<ul>
<li><b>3-digit code:</b> first two digits are the value, third digit is the number of zeros (multiplier).<br>e.g. <b>103</b> = 10 × 10³ = 10 kΩ; <b>472</b> = 47 × 10² = 4.7 kΩ; <b>220</b> = 22 × 10⁰ = 22 Ω.</li>
<li><b>4-digit code</b> (precision): first three digits are the value, fourth is the multiplier.<br>e.g. <b>1002</b> = 100 × 10² = 10 kΩ.</li>
<li><b>Letter code (R, K, M as decimal point):</b> <b>4R7</b> = 4.7 Ω, <b>2K2</b> = 2.2 kΩ, <b>1M5</b> = 1.5 MΩ.</li>
<li>Tolerance letters: <b>F</b> = ±1%, <b>G</b> = ±2%, <b>J</b> = ±5%, <b>K</b> = ±10%, <b>M</b> = ±20%.</li>
</ul>""",
          """<p>મોટા રેઝિસ્ટર અને SMD રેઝિસ્ટર પર <b>છાપેલો અંક કોડ</b> વપરાય છે.</p>
<ul>
<li><b>3-અંક કોડ:</b> પહેલા બે અંક મૂલ્ય, ત્રીજો અંક શૂન્યની સંખ્યા (ગુણક).<br>દા.ત. <b>103</b> = 10 × 10³ = 10 kΩ; <b>472</b> = 47 × 10² = 4.7 kΩ; <b>220</b> = 22 × 10⁰ = 22 Ω.</li>
<li><b>4-અંક કોડ</b> (ચોકસાઈવાળા): પહેલા ત્રણ અંક મૂલ્ય, ચોથો ગુણક.<br>દા.ત. <b>1002</b> = 100 × 10² = 10 kΩ.</li>
<li><b>અક્ષર કોડ (R, K, M દશાંશ ચિહ્ન તરીકે):</b> <b>4R7</b> = 4.7 Ω, <b>2K2</b> = 2.2 kΩ, <b>1M5</b> = 1.5 MΩ.</li>
<li>ટોલરન્સ અક્ષર: <b>F</b> = ±1%, <b>G</b> = ±2%, <b>J</b> = ±5%, <b>K</b> = ±10%, <b>M</b> = ±20%.</li>
</ul>"""),
    ],
}
