"""Basics of Electronics (DI01000151) - Unit 4: Bipolar Junction Transistor (part A: 4.1 - 4.2)"""
from content_DI01000151_u3_notes_a import T

# =====================================================================================
SEC_4_1 = {
    "title": {"en": "4.1 Transistor – Construction and Types (PNP / NPN)", "gu": "4.1 Transistor – રચના અને પ્રકાર (PNP / NPN)"},
    "items": [
        T("4.1.1 Introduction to Transistor", "4.1.1 Transistor નો પરિચય",
          """<p>A <b>transistor</b> is a three-terminal semiconductor device used for <b>amplification</b> (making a weak signal stronger) and <b>switching</b> (ON/OFF).</p>
<ul>
<li>The word <b>transistor</b> comes from <b>"transfer + resistor"</b>: it transfers a signal from a low-resistance input circuit to a high-resistance output circuit.</li>
<li>It was invented in <b>1947</b> at <b>Bell Laboratories</b> (USA) by <b>John Bardeen, Walter Brattain and William Shockley</b>, who received the Nobel Prize in 1956.</li>
<li>It replaced the bulky <b>vacuum tube (triode)</b> and started the era of modern electronics, ICs and computers.</li>
</ul>
<h4>Bipolar Junction Transistor (BJT)</h4>
<ul>
<li><b>Bipolar:</b> current is carried by <b>both</b> types of carriers – electrons and holes.</li>
<li><b>Junction:</b> it has <b>two P-N junctions</b>.</li>
<li>Three terminals: <b>Emitter (E), Base (B), Collector (C)</b>.</li>
<li>A BJT is a <b>current-controlled device</b>: a small base current controls a large collector current.</li>
</ul>
<h4>Advantages over vacuum tubes</h4>
<p>Small size, light weight, no heater (instant start), low operating voltage, low power consumption, long life, rugged and cheap.</p>""",
          """<p><b>Transistor</b> એ ત્રણ terminal વાળું semiconductor device છે, જે <b>Amplification</b> (નબળા signal ને મજબૂત બનાવવું) અને <b>Switching</b> (ON/OFF) માટે વપરાય છે.</p>
<ul>
<li><b>Transistor</b> શબ્દ <b>"transfer + resistor"</b> પરથી આવ્યો છે: તે signal ને ઓછા resistance વાળા input circuit થી વધુ resistance વાળા output circuit માં transfer કરે છે.</li>
<li>તેની શોધ <b>1947</b> માં <b>Bell Laboratories</b> (USA) માં <b>John Bardeen, Walter Brattain અને William Shockley</b> એ કરી હતી; તેમને 1956 માં Nobel Prize મળ્યું.</li>
<li>તેણે મોટી <b>vacuum tube (triode)</b> નું સ્થાન લીધું અને આધુનિક electronics, ICs અને computers ના યુગની શરૂઆત કરી.</li>
</ul>
<h4>Bipolar Junction Transistor (BJT)</h4>
<ul>
<li><b>Bipolar:</b> current <b>બંને</b> પ્રકારના carriers – electrons અને holes – દ્વારા વહન થાય છે.</li>
<li><b>Junction:</b> તેમાં <b>બે P-N junctions</b> હોય છે.</li>
<li>ત્રણ terminals: <b>Emitter (E), Base (B), Collector (C)</b>.</li>
<li>BJT એ <b>current-controlled device</b> છે: નાનો base current મોટા collector current ને નિયંત્રિત કરે છે.</li>
</ul>
<h4>Vacuum tubes કરતાં ફાયદા</h4>
<p>નાનું કદ, ઓછું વજન, heater નહીં (તરત શરૂ), ઓછો operating voltage, ઓછો power વપરાશ, લાંબું આયુષ્ય, મજબૂત અને સસ્તું.</p>"""),

        T("4.1.2 Construction of Transistor", "4.1.2 Transistor ની રચના",
          """<p>A transistor is made by sandwiching a <b>thin layer</b> of one type of semiconductor between two layers of the opposite type. It has <b>three regions</b> and <b>two junctions</b>.</p>
<table>
<tr><th>Region</th><th>Doping</th><th>Size</th><th>Function</th></tr>
<tr><td><b>Emitter (E)</b></td><td>Heavily doped</td><td>Medium</td><td>Emits (supplies) a large number of majority carriers into the base</td></tr>
<tr><td><b>Base (B)</b></td><td>Lightly doped</td><td>Very thin (≈ 10⁻⁶ m)</td><td>Controls the flow of carriers from emitter to collector</td></tr>
<tr><td><b>Collector (C)</b></td><td>Moderately doped</td><td>Largest</td><td>Collects carriers; large size to dissipate heat</td></tr>
</table>
<h4>Two junctions</h4>
<ul>
<li><b>Emitter-Base junction (J<sub>E</sub>)</b> – between emitter and base.</li>
<li><b>Collector-Base junction (J<sub>C</sub>)</b> – between collector and base.</li>
</ul>
<p>So a transistor looks like <b>two diodes connected back to back</b>. But two separate diodes <b>cannot</b> work as a transistor, because the base must be very thin and lightly doped.</p>
<h4>Why these doping levels and sizes?</h4>
<ul>
<li><b>Emitter heavily doped</b> → it can inject a large number of carriers.</li>
<li><b>Base thin and lightly doped</b> → very few carriers recombine in the base; most (95–99%) pass on to the collector.</li>
<li><b>Collector largest</b> → most power is dissipated at the collector junction, so a large area is needed to remove heat.</li>
<li>Emitter and collector are the same type of material but <b>cannot be interchanged</b>, because their doping and size are different.</li>
</ul>""",
          """<p>Transistor એક પ્રકારના semiconductor ના <b>પાતળા સ્તર</b> ને વિરુદ્ધ પ્રકારના બે સ્તરો વચ્ચે sandwich કરીને બનાવાય છે. તેમાં <b>ત્રણ regions</b> અને <b>બે junctions</b> હોય છે.</p>
<table>
<tr><th>Region</th><th>Doping</th><th>કદ</th><th>કાર્ય</th></tr>
<tr><td><b>Emitter (E)</b></td><td>વધુ doped</td><td>મધ્યમ</td><td>Base માં મોટી સંખ્યામાં majority carriers મોકલે (emit કરે)</td></tr>
<tr><td><b>Base (B)</b></td><td>ઓછું doped</td><td>ખૂબ પાતળું (≈ 10⁻⁶ m)</td><td>Emitter થી collector તરફ carriers ના પ્રવાહને નિયંત્રિત કરે</td></tr>
<tr><td><b>Collector (C)</b></td><td>મધ્યમ doped</td><td>સૌથી મોટું</td><td>Carriers એકત્ર કરે; ઉષ્મા દૂર કરવા મોટું કદ</td></tr>
</table>
<h4>બે junctions</h4>
<ul>
<li><b>Emitter-Base junction (J<sub>E</sub>)</b> – emitter અને base વચ્ચે.</li>
<li><b>Collector-Base junction (J<sub>C</sub>)</b> – collector અને base વચ્ચે.</li>
</ul>
<p>તેથી transistor <b>પીઠ-પીઠ જોડેલા બે diodes</b> જેવો દેખાય છે. પરંતુ બે અલગ diodes transistor તરીકે કામ <b>કરી શકતા નથી</b>, કારણ કે base ખૂબ પાતળું અને ઓછું doped હોવું જોઈએ.</p>
<h4>આવું doping અને કદ કેમ?</h4>
<ul>
<li><b>Emitter વધુ doped</b> → તે મોટી સંખ્યામાં carriers મોકલી શકે.</li>
<li><b>Base પાતળું અને ઓછું doped</b> → base માં ખૂબ ઓછા carriers recombine થાય; મોટાભાગના (95–99%) collector સુધી પહોંચે.</li>
<li><b>Collector સૌથી મોટું</b> → મોટાભાગનો power collector junction પર dissipate થાય છે, તેથી ઉષ્મા દૂર કરવા મોટો વિસ્તાર જોઈએ.</li>
<li>Emitter અને collector સમાન પ્રકારના material છે પરંતુ doping અને કદ અલગ હોવાથી તેમને <b>અદલાબદલી કરી શકાતા નથી</b>.</li>
</ul>""",
          diagram="u4_structure"),

        T("4.1.3 Types: NPN and PNP Transistors", "4.1.3 પ્રકાર: NPN અને PNP Transistors",
          """<h4>1. NPN transistor</h4>
<p>A thin <b>P-type</b> layer (base) is placed between two <b>N-type</b> layers (emitter and collector). Majority carriers are <b>electrons</b>.</p>
<h4>2. PNP transistor</h4>
<p>A thin <b>N-type</b> layer (base) is placed between two <b>P-type</b> layers. Majority carriers are <b>holes</b>.</p>
<h4>Symbols</h4>
<ul>
<li>The <b>arrow is always on the emitter</b> and shows the direction of <b>conventional current</b>.</li>
<li><b>NPN:</b> arrow points <b>outward</b> (Not Pointing iN). Current flows into C and B and out of E.</li>
<li><b>PNP:</b> arrow points <b>inward</b> (Pointing iN Permanently). Current flows into E and out of B and C.</li>
<li>In both: <b>I<sub>E</sub> = I<sub>B</sub> + I<sub>C</sub></b>.</li>
</ul>
<h4>Comparison of NPN and PNP</h4>
<table>
<tr><th>Point</th><th>NPN</th><th>PNP</th></tr>
<tr><td>Structure</td><td>P-layer between two N-layers</td><td>N-layer between two P-layers</td></tr>
<tr><td>Majority carriers</td><td>Electrons</td><td>Holes</td></tr>
<tr><td>Arrow in symbol</td><td>Outward (on emitter)</td><td>Inward (on emitter)</td></tr>
<tr><td>Biasing (active)</td><td>Collector +ve, emitter −ve</td><td>Collector −ve, emitter +ve</td></tr>
<tr><td>Speed</td><td>Faster (electron mobility is higher)</td><td>Slower</td></tr>
<tr><td>Use</td><td>More popular</td><td>Less used; complementary circuits</td></tr>
<tr><td>Examples</td><td>BC547, 2N2222, 2N3055</td><td>BC557, 2N2907, 2N2955</td></tr>
</table>
<p><b>Why is NPN more popular?</b> Electrons have higher mobility than holes, so NPN transistors are faster and give better high-frequency performance; also most circuits use a positive supply.</p>""",
          """<h4>1. NPN transistor</h4>
<p>બે <b>N-type</b> સ્તરો (emitter અને collector) વચ્ચે પાતળું <b>P-type</b> સ્તર (base) મૂકાય છે. Majority carriers <b>electrons</b> છે.</p>
<h4>2. PNP transistor</h4>
<p>બે <b>P-type</b> સ્તરો વચ્ચે પાતળું <b>N-type</b> સ્તર (base) મૂકાય છે. Majority carriers <b>holes</b> છે.</p>
<h4>Symbols</h4>
<ul>
<li><b>Arrow હંમેશા emitter પર</b> હોય છે અને <b>conventional current</b> ની દિશા બતાવે છે.</li>
<li><b>NPN:</b> arrow <b>બહાર તરફ</b> (Not Pointing iN). Current C અને B માં અંદર જાય અને E માંથી બહાર આવે.</li>
<li><b>PNP:</b> arrow <b>અંદર તરફ</b> (Pointing iN Permanently). Current E માં અંદર જાય અને B અને C માંથી બહાર આવે.</li>
<li>બંનેમાં: <b>I<sub>E</sub> = I<sub>B</sub> + I<sub>C</sub></b>.</li>
</ul>
<h4>NPN અને PNP ની સરખામણી</h4>
<table>
<tr><th>મુદ્દો</th><th>NPN</th><th>PNP</th></tr>
<tr><td>રચના</td><td>બે N-સ્તરો વચ્ચે P-સ્તર</td><td>બે P-સ્તરો વચ્ચે N-સ્તર</td></tr>
<tr><td>Majority carriers</td><td>Electrons</td><td>Holes</td></tr>
<tr><td>Symbol માં arrow</td><td>બહાર તરફ (emitter પર)</td><td>અંદર તરફ (emitter પર)</td></tr>
<tr><td>Biasing (active)</td><td>Collector +ve, emitter −ve</td><td>Collector −ve, emitter +ve</td></tr>
<tr><td>ઝડપ</td><td>વધુ ઝડપી (electron mobility વધુ)</td><td>ધીમું</td></tr>
<tr><td>ઉપયોગ</td><td>વધુ લોકપ્રિય</td><td>ઓછો; complementary circuits</td></tr>
<tr><td>ઉદાહરણ</td><td>BC547, 2N2222, 2N3055</td><td>BC557, 2N2907, 2N2955</td></tr>
</table>
<p><b>NPN વધુ લોકપ્રિય કેમ?</b> Electrons ની mobility holes કરતાં વધુ છે, તેથી NPN transistors વધુ ઝડપી છે અને high frequency પર વધુ સારું કામ કરે છે; ઉપરાંત મોટાભાગના circuits positive supply વાપરે છે.</p>""",
          diagram="u4_symbols"),

        T("4.1.4 Transistor Identification and Ratings", "4.1.4 Transistor ની ઓળખ અને Ratings",
          """<h4>Packages</h4>
<ul>
<li><b>TO-92</b> (small plastic, e.g. BC547, 2N2222A) – low-power signal transistors.</li>
<li><b>TO-220</b> (with metal tab, e.g. TIP31, TIP122) – medium power; mounted on a heat sink.</li>
<li><b>TO-3</b> (metal can, e.g. 2N3055) – high power; case is the collector.</li>
</ul>
<h4>Pin identification</h4>
<ul>
<li><b>BC547/BC557:</b> hold the flat face towards you, leads down → pins are <b>C – B – E</b> from left to right.</li>
<li>Pin order differs between types, so always check the <b>datasheet</b>.</li>
<li><b>Multimeter test (diode mode):</b> base-emitter and base-collector junctions each show ≈ 0.6–0.7 V in one direction only. If the red probe on the base gives readings to both other pins → <b>NPN</b>; if the black probe on the base does → <b>PNP</b>. The B-E reading is slightly higher than B-C.</li>
</ul>
<h4>Important ratings</h4>
<table>
<tr><th>Rating</th><th>Meaning</th><th>BC547 (typical)</th></tr>
<tr><td>V<sub>CEO</sub></td><td>Max collector-emitter voltage (base open)</td><td>45 V</td></tr>
<tr><td>I<sub>C(max)</sub></td><td>Max collector current</td><td>100 mA</td></tr>
<tr><td>P<sub>D</sub></td><td>Max power dissipation = V<sub>CE</sub> × I<sub>C</sub></td><td>500 mW</td></tr>
<tr><td>h<sub>FE</sub> (β<sub>dc</sub>)</td><td>DC current gain</td><td>110 – 800</td></tr>
<tr><td>f<sub>T</sub></td><td>Transition frequency (gain = 1)</td><td>300 MHz</td></tr>
</table>""",
          """<h4>Packages</h4>
<ul>
<li><b>TO-92</b> (નાનું plastic, દા.ત. BC547, 2N2222A) – ઓછા power ના signal transistors.</li>
<li><b>TO-220</b> (metal tab સાથે, દા.ત. TIP31, TIP122) – મધ્યમ power; heat sink પર લગાવાય.</li>
<li><b>TO-3</b> (metal can, દા.ત. 2N3055) – વધુ power; case એ collector છે.</li>
</ul>
<h4>Pin ની ઓળખ</h4>
<ul>
<li><b>BC547/BC557:</b> સપાટ ભાગ તમારી તરફ અને leads નીચે રાખો → ડાબેથી જમણે pins <b>C – B – E</b>.</li>
<li>જુદા જુદા types માં pin ક્રમ અલગ હોય છે, તેથી હંમેશા <b>datasheet</b> જુઓ.</li>
<li><b>Multimeter test (diode mode):</b> base-emitter અને base-collector junctions દરેક ફક્ત એક જ દિશામાં ≈ 0.6–0.7 V બતાવે છે. જો base પર red probe રાખતાં બાકીના બંને pins પર reading આવે → <b>NPN</b>; જો black probe base પર રાખતાં આવે → <b>PNP</b>. B-E reading, B-C કરતાં થોડું વધુ હોય છે.</li>
</ul>
<h4>મહત્વના Ratings</h4>
<table>
<tr><th>Rating</th><th>અર્થ</th><th>BC547 (સામાન્ય)</th></tr>
<tr><td>V<sub>CEO</sub></td><td>મહત્તમ collector-emitter voltage (base open)</td><td>45 V</td></tr>
<tr><td>I<sub>C(max)</sub></td><td>મહત્તમ collector current</td><td>100 mA</td></tr>
<tr><td>P<sub>D</sub></td><td>મહત્તમ power dissipation = V<sub>CE</sub> × I<sub>C</sub></td><td>500 mW</td></tr>
<tr><td>h<sub>FE</sub> (β<sub>dc</sub>)</td><td>DC current gain</td><td>110 – 800</td></tr>
<tr><td>f<sub>T</sub></td><td>Transition frequency (gain = 1)</td><td>300 MHz</td></tr>
</table>"""),

        T("Key Points – 4.1", "મુખ્ય મુદ્દા – 4.1",
          """<ul>
<li>Transistor = <b>transfer + resistor</b>; invented in 1947 at Bell Labs; used for amplification and switching.</li>
<li>BJT: <b>bipolar</b> (electrons + holes), <b>two junctions</b> (J<sub>E</sub>, J<sub>C</sub>), three terminals E, B, C; current-controlled.</li>
<li>Emitter: heavily doped; Base: lightly doped and very thin; Collector: moderately doped and largest.</li>
<li>Emitter and collector cannot be interchanged.</li>
<li><b>NPN</b>: arrow out, electrons majority; <b>PNP</b>: arrow in, holes majority.</li>
<li><b>I<sub>E</sub> = I<sub>B</sub> + I<sub>C</sub></b>.</li>
<li>NPN is more popular (higher electron mobility → faster).</li>
</ul>""",
          """<ul>
<li>Transistor = <b>transfer + resistor</b>; 1947 માં Bell Labs માં શોધ; amplification અને switching માટે વપરાય.</li>
<li>BJT: <b>bipolar</b> (electrons + holes), <b>બે junctions</b> (J<sub>E</sub>, J<sub>C</sub>), ત્રણ terminals E, B, C; current-controlled.</li>
<li>Emitter: વધુ doped; Base: ઓછું doped અને ખૂબ પાતળું; Collector: મધ્યમ doped અને સૌથી મોટું.</li>
<li>Emitter અને collector અદલાબદલી કરી શકાતા નથી.</li>
<li><b>NPN</b>: arrow બહાર, electrons majority; <b>PNP</b>: arrow અંદર, holes majority.</li>
<li><b>I<sub>E</sub> = I<sub>B</sub> + I<sub>C</sub></b>.</li>
<li>NPN વધુ લોકપ્રિય (electron mobility વધુ → વધુ ઝડપી).</li>
</ul>""", key=True),
    ],
}

# =====================================================================================
SEC_4_2 = {
    "title": {"en": "4.2 Working of Transistor", "gu": "4.2 Transistor નું કાર્ય"},
    "items": [
        T("4.2.1 Biasing of Transistor and Regions of Operation", "4.2.1 Transistor નું Biasing અને Regions of Operation",
          """<p>To work as an <b>amplifier</b>, a transistor must be biased so that:</p>
<ul>
<li><b>Emitter-base junction (J<sub>E</sub>) → forward biased</b> (low resistance)</li>
<li><b>Collector-base junction (J<sub>C</sub>) → reverse biased</b> (high resistance)</li>
</ul>
<p>Depending on the bias of the two junctions, a transistor has four regions of operation:</p>
<table>
<tr><th>Region</th><th>J<sub>E</sub></th><th>J<sub>C</sub></th><th>Behaviour / Use</th></tr>
<tr><td><b>Active</b></td><td>Forward</td><td>Reverse</td><td>I<sub>C</sub> = β I<sub>B</sub>; used as an <b>amplifier</b></td></tr>
<tr><td><b>Saturation</b></td><td>Forward</td><td>Forward</td><td>Maximum I<sub>C</sub>, V<sub>CE</sub> ≈ 0.2 V; <b>ON switch</b></td></tr>
<tr><td><b>Cut-off</b></td><td>Reverse</td><td>Reverse</td><td>I<sub>C</sub> ≈ 0; <b>OFF switch</b></td></tr>
<tr><td>Inverse active</td><td>Reverse</td><td>Forward</td><td>E and C roles exchanged; very low gain; rarely used</td></tr>
</table>
<p>Typical values for a silicon transistor in the active region: <b>V<sub>BE</sub> ≈ 0.7 V</b> (0.3 V for Ge).</p>""",
          """<p><b>Amplifier</b> તરીકે કામ કરવા transistor ને આ રીતે bias કરવો પડે:</p>
<ul>
<li><b>Emitter-base junction (J<sub>E</sub>) → forward biased</b> (ઓછો resistance)</li>
<li><b>Collector-base junction (J<sub>C</sub>) → reverse biased</b> (વધુ resistance)</li>
</ul>
<p>બંને junctions ના bias પ્રમાણે transistor ના ચાર regions of operation છે:</p>
<table>
<tr><th>Region</th><th>J<sub>E</sub></th><th>J<sub>C</sub></th><th>વર્તન / ઉપયોગ</th></tr>
<tr><td><b>Active</b></td><td>Forward</td><td>Reverse</td><td>I<sub>C</sub> = β I<sub>B</sub>; <b>Amplifier</b> તરીકે વપરાય</td></tr>
<tr><td><b>Saturation</b></td><td>Forward</td><td>Forward</td><td>મહત્તમ I<sub>C</sub>, V<sub>CE</sub> ≈ 0.2 V; <b>ON switch</b></td></tr>
<tr><td><b>Cut-off</b></td><td>Reverse</td><td>Reverse</td><td>I<sub>C</sub> ≈ 0; <b>OFF switch</b></td></tr>
<tr><td>Inverse active</td><td>Reverse</td><td>Forward</td><td>E અને C ની ભૂમિકા બદલાય; ખૂબ ઓછો gain; ભાગ્યે જ વપરાય</td></tr>
</table>
<p>Active region માં silicon transistor માટે સામાન્ય મૂલ્ય: <b>V<sub>BE</sub> ≈ 0.7 V</b> (Ge માટે 0.3 V).</p>"""),

        T("4.2.2 Working of NPN Transistor", "4.2.2 NPN Transistor નું કાર્ય",
          """<p><b>Biasing:</b> V<sub>EE</sub> forward biases J<sub>E</sub> (emitter N to −ve, base P to +ve); V<sub>CC</sub> reverse biases J<sub>C</sub> (collector N to +ve).</p>
<h4>Working</h4>
<ol>
<li>Because J<sub>E</sub> is forward biased, the large number of <b>free electrons</b> in the heavily doped N-type emitter are pushed into the base. This forms the <b>emitter current I<sub>E</sub></b>.</li>
<li>The base is <b>very thin and lightly doped</b> (few holes). So only a very small number of electrons (about <b>1–5%</b>) recombine with holes in the base. These form the small <b>base current I<sub>B</sub></b>.</li>
<li>The remaining electrons (about <b>95–99%</b>) diffuse across the thin base and reach the collector-base junction.</li>
<li>J<sub>C</sub> is reverse biased, so its electric field <b>attracts (sweeps)</b> these electrons into the collector, where they are collected by the positive terminal of V<sub>CC</sub>. This forms the <b>collector current I<sub>C</sub></b>.</li>
</ol>
<p>Thus: <b>I<sub>E</sub> = I<sub>B</sub> + I<sub>C</sub></b>, and I<sub>C</sub> is almost equal to I<sub>E</sub>.</p>
<p>Inside the NPN transistor current is carried mainly by <b>electrons</b>. In the external circuit, conventional current flows <b>into</b> the collector and base and <b>out of</b> the emitter.</p>
<p><b>Key idea:</b> a small change in base current (or V<sub>BE</sub>) produces a large change in collector current – this is the basis of <b>amplification</b>.</p>""",
          """<p><b>Biasing:</b> V<sub>EE</sub> એ J<sub>E</sub> ને forward bias કરે છે (emitter N ને −ve, base P ને +ve); V<sub>CC</sub> એ J<sub>C</sub> ને reverse bias કરે છે (collector N ને +ve).</p>
<h4>કાર્ય</h4>
<ol>
<li>J<sub>E</sub> forward biased હોવાથી, વધુ doped N-type emitter ના મોટી સંખ્યાના <b>free electrons</b> base માં ધકેલાય છે. તેનાથી <b>Emitter current I<sub>E</sub></b> બને છે.</li>
<li>Base <b>ખૂબ પાતળું અને ઓછું doped</b> (ઓછા holes) છે. તેથી ફક્ત ખૂબ ઓછા electrons (આશરે <b>1–5%</b>) base માં holes સાથે recombine થાય છે. તેનાથી નાનો <b>Base current I<sub>B</sub></b> બને છે.</li>
<li>બાકીના electrons (આશરે <b>95–99%</b>) પાતળા base માંથી diffuse થઈ collector-base junction સુધી પહોંચે છે.</li>
<li>J<sub>C</sub> reverse biased છે, તેથી તેનું electric field આ electrons ને collector માં <b>ખેંચી લે</b> છે, જ્યાં V<sub>CC</sub> નો positive terminal તેમને એકત્ર કરે છે. તેનાથી <b>Collector current I<sub>C</sub></b> બને છે.</li>
</ol>
<p>આમ: <b>I<sub>E</sub> = I<sub>B</sub> + I<sub>C</sub></b>, અને I<sub>C</sub> લગભગ I<sub>E</sub> જેટલો હોય છે.</p>
<p>NPN transistor ની અંદર current મુખ્યત્વે <b>electrons</b> દ્વારા વહન થાય છે. બાહ્ય circuit માં conventional current collector અને base માં <b>અંદર</b> જાય છે અને emitter માંથી <b>બહાર</b> આવે છે.</p>
<p><b>મુખ્ય વિચાર:</b> base current (અથવા V<sub>BE</sub>) માં નાનો ફેરફાર collector current માં મોટો ફેરફાર કરે છે – આ જ <b>Amplification</b> નો આધાર છે.</p>""",
          diagram="u4_npn_working"),

        T("4.2.3 Working of PNP Transistor", "4.2.3 PNP Transistor નું કાર્ય",
          """<p><b>Biasing:</b> V<sub>EE</sub> forward biases J<sub>E</sub> (emitter P to +ve, base N to −ve); V<sub>CC</sub> reverse biases J<sub>C</sub> (collector P to −ve). All polarities are <b>opposite</b> to NPN.</p>
<h4>Working</h4>
<ol>
<li>J<sub>E</sub> is forward biased, so a large number of <b>holes</b> from the heavily doped P-type emitter are pushed into the N-type base → <b>emitter current I<sub>E</sub></b>.</li>
<li>The base is thin and lightly doped (few electrons), so only about <b>1–5%</b> of holes recombine with electrons in the base → small <b>base current I<sub>B</sub></b>.</li>
<li>The remaining <b>95–99%</b> of holes cross the base and reach J<sub>C</sub>.</li>
<li>The reverse-biased J<sub>C</sub> (collector connected to −ve) attracts these holes into the collector → <b>collector current I<sub>C</sub></b>.</li>
</ol>
<p>Again <b>I<sub>E</sub> = I<sub>B</sub> + I<sub>C</sub></b>. Inside the PNP transistor current is carried mainly by <b>holes</b>; in the external circuit, conventional current flows <b>into</b> the emitter and <b>out of</b> the base and collector.</p>
<h4>Difference in working (NPN vs PNP)</h4>
<ul>
<li>NPN: majority carriers = electrons, collector +ve.</li>
<li>PNP: majority carriers = holes, collector −ve.</li>
<li>Both have the same current relations and the same principle of operation.</li>
</ul>""",
          """<p><b>Biasing:</b> V<sub>EE</sub> એ J<sub>E</sub> ને forward bias કરે છે (emitter P ને +ve, base N ને −ve); V<sub>CC</sub> એ J<sub>C</sub> ને reverse bias કરે છે (collector P ને −ve). બધી polarities NPN થી <b>વિરુદ્ધ</b> છે.</p>
<h4>કાર્ય</h4>
<ol>
<li>J<sub>E</sub> forward biased છે, તેથી વધુ doped P-type emitter ના મોટી સંખ્યાના <b>holes</b> N-type base માં ધકેલાય છે → <b>Emitter current I<sub>E</sub></b>.</li>
<li>Base પાતળું અને ઓછું doped (ઓછા electrons) છે, તેથી ફક્ત આશરે <b>1–5%</b> holes base માં electrons સાથે recombine થાય છે → નાનો <b>Base current I<sub>B</sub></b>.</li>
<li>બાકીના <b>95–99%</b> holes base પાર કરી J<sub>C</sub> સુધી પહોંચે છે.</li>
<li>Reverse-biased J<sub>C</sub> (collector −ve સાથે) આ holes ને collector માં ખેંચે છે → <b>Collector current I<sub>C</sub></b>.</li>
</ol>
<p>ફરીથી <b>I<sub>E</sub> = I<sub>B</sub> + I<sub>C</sub></b>. PNP transistor ની અંદર current મુખ્યત્વે <b>holes</b> દ્વારા વહન થાય છે; બાહ્ય circuit માં conventional current emitter માં <b>અંદર</b> જાય છે અને base અને collector માંથી <b>બહાર</b> આવે છે.</p>
<h4>કાર્યમાં તફાવત (NPN અને PNP)</h4>
<ul>
<li>NPN: majority carriers = electrons, collector +ve.</li>
<li>PNP: majority carriers = holes, collector −ve.</li>
<li>બંનેમાં current સંબંધો અને કાર્ય સિદ્ધાંત સમાન છે.</li>
</ul>""",
          diagram="u4_pnp_working"),

        T("4.2.4 Transistor Currents and Their Relations", "4.2.4 Transistor Currents અને તેમના સંબંધો",
          """<h4>Basic current equation (KCL)</h4>
<p><b>I<sub>E</sub> = I<sub>B</sub> + I<sub>C</sub></b> &nbsp; (I<sub>B</sub> is very small, so I<sub>C</sub> ≈ I<sub>E</sub>)</p>
<h4>α (alpha) – common-base DC current gain</h4>
<p><b>α = I<sub>C</sub> / I<sub>E</sub></b> → always <b>less than 1</b>; typical 0.95 to 0.995.</p>
<h4>β (beta) – common-emitter DC current gain (h<sub>FE</sub>)</h4>
<p><b>β = I<sub>C</sub> / I<sub>B</sub></b> → large; typical <b>20 to 500</b>.</p>
<h4>Relation between α and β</h4>
<p>Dividing I<sub>E</sub> = I<sub>B</sub> + I<sub>C</sub> by I<sub>C</sub>: &nbsp; 1/α = 1/β + 1</p>
<p><b>β = α / (1 − α)</b> &nbsp;&nbsp; and &nbsp;&nbsp; <b>α = β / (1 + β)</b></p>
<p>Example: α = 0.98 → β = 0.98/0.02 = 49. A small change in α causes a large change in β.</p>
<h4>Leakage currents</h4>
<ul>
<li><b>I<sub>CBO</sub></b>: collector-base leakage current with emitter open (due to minority carriers in reverse-biased J<sub>C</sub>). nA for Si, µA for Ge. Doubles every 10 °C.</li>
<li>In CB: <b>I<sub>C</sub> = α I<sub>E</sub> + I<sub>CBO</sub></b></li>
<li><b>I<sub>CEO</sub></b>: collector-emitter leakage with base open: <b>I<sub>CEO</sub> = (1 + β) I<sub>CBO</sub></b> (much larger).</li>
<li>In CE: <b>I<sub>C</sub> = β I<sub>B</sub> + I<sub>CEO</sub></b></li>
</ul>
<p>Leakage current increases with temperature and can lead to <b>thermal runaway</b> if the circuit is not stabilised.</p>""",
          """<h4>મૂળભૂત current સમીકરણ (KCL)</h4>
<p><b>I<sub>E</sub> = I<sub>B</sub> + I<sub>C</sub></b> &nbsp; (I<sub>B</sub> ખૂબ નાનો છે, તેથી I<sub>C</sub> ≈ I<sub>E</sub>)</p>
<h4>α (alpha) – common-base DC current gain</h4>
<p><b>α = I<sub>C</sub> / I<sub>E</sub></b> → હંમેશા <b>1 થી ઓછો</b>; સામાન્ય 0.95 થી 0.995.</p>
<h4>β (beta) – common-emitter DC current gain (h<sub>FE</sub>)</h4>
<p><b>β = I<sub>C</sub> / I<sub>B</sub></b> → મોટો; સામાન્ય <b>20 થી 500</b>.</p>
<h4>α અને β વચ્ચેનો સંબંધ</h4>
<p>I<sub>E</sub> = I<sub>B</sub> + I<sub>C</sub> ને I<sub>C</sub> વડે ભાગતાં: &nbsp; 1/α = 1/β + 1</p>
<p><b>β = α / (1 − α)</b> &nbsp;&nbsp; અને &nbsp;&nbsp; <b>α = β / (1 + β)</b></p>
<p>ઉદાહરણ: α = 0.98 → β = 0.98/0.02 = 49. α માં નાનો ફેરફાર β માં મોટો ફેરફાર કરે છે.</p>
<h4>Leakage currents</h4>
<ul>
<li><b>I<sub>CBO</sub></b>: emitter open હોય ત્યારે collector-base leakage current (reverse-biased J<sub>C</sub> માં minority carriers ને કારણે). Si માટે nA, Ge માટે µA. દર 10 °C એ બમણો.</li>
<li>CB માં: <b>I<sub>C</sub> = α I<sub>E</sub> + I<sub>CBO</sub></b></li>
<li><b>I<sub>CEO</sub></b>: base open હોય ત્યારે collector-emitter leakage: <b>I<sub>CEO</sub> = (1 + β) I<sub>CBO</sub></b> (ઘણો મોટો).</li>
<li>CE માં: <b>I<sub>C</sub> = β I<sub>B</sub> + I<sub>CEO</sub></b></li>
</ul>
<p>Leakage current તાપમાન સાથે વધે છે અને circuit stabilise ન હોય તો <b>Thermal runaway</b> થઈ શકે છે.</p>""",
          examples=["u4n1", "u4n2", "u4n3", "u4n8"]),

        T("Key Points – 4.2", "મુખ્ય મુદ્દા – 4.2",
          """<ul>
<li>Active region (amplifier): <b>J<sub>E</sub> forward, J<sub>C</sub> reverse</b>.</li>
<li>Saturation: both forward (ON switch); Cut-off: both reverse (OFF switch).</li>
<li>Emitter injects carriers; only 1–5% recombine in thin base (I<sub>B</sub>); 95–99% reach collector (I<sub>C</sub>).</li>
<li>NPN: electrons; PNP: holes; supply polarities opposite.</li>
<li><b>I<sub>E</sub> = I<sub>B</sub> + I<sub>C</sub></b>; <b>α = I<sub>C</sub>/I<sub>E</sub></b> (&lt; 1); <b>β = I<sub>C</sub>/I<sub>B</sub></b> (20–500).</li>
<li><b>β = α/(1 − α)</b>, <b>α = β/(1 + β)</b>.</li>
<li><b>I<sub>CEO</sub> = (1 + β) I<sub>CBO</sub></b>; I<sub>C</sub> = β I<sub>B</sub> + I<sub>CEO</sub>.</li>
</ul>""",
          """<ul>
<li>Active region (amplifier): <b>J<sub>E</sub> forward, J<sub>C</sub> reverse</b>.</li>
<li>Saturation: બંને forward (ON switch); Cut-off: બંને reverse (OFF switch).</li>
<li>Emitter carriers મોકલે; પાતળા base માં ફક્ત 1–5% recombine (I<sub>B</sub>); 95–99% collector સુધી (I<sub>C</sub>).</li>
<li>NPN: electrons; PNP: holes; supply polarities વિરુદ્ધ.</li>
<li><b>I<sub>E</sub> = I<sub>B</sub> + I<sub>C</sub></b>; <b>α = I<sub>C</sub>/I<sub>E</sub></b> (&lt; 1); <b>β = I<sub>C</sub>/I<sub>B</sub></b> (20–500).</li>
<li><b>β = α/(1 − α)</b>, <b>α = β/(1 + β)</b>.</li>
<li><b>I<sub>CEO</sub> = (1 + β) I<sub>CBO</sub></b>; I<sub>C</sub> = β I<sub>B</sub> + I<sub>CEO</sub>.</li>
</ul>""", key=True),
    ],
}

NOTES_A = [SEC_4_1, SEC_4_2]
