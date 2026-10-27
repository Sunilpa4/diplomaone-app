"""Basics of Electronics (DI01000151) - Unit 2: Fundamentals of Semiconductors
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
SEC_2_1 = {
    "title": {"en": "2.1 Atomic Structure", "gu": "2.1 Atomic Structure (પરમાણુ રચના)"},
    "items": [
        T("2.1.1 Structure of an Atom", "2.1.1 Atom ની રચના",
          """<p>Every material is made of extremely small particles called <b>atoms</b>. According to <b>Bohr's atomic model</b>, an atom has two parts:</p>
<ol>
<li><b>Nucleus:</b> The central, heavy part of the atom. It contains <b>protons</b> (positive charge) and <b>neutrons</b> (no charge). Almost the whole mass of the atom is in the nucleus.</li>
<li><b>Electrons:</b> Very light, <b>negatively charged</b> particles that revolve around the nucleus in fixed circular paths called <b>orbits or shells</b>.</li>
</ol>
<table>
<tr><th>Particle</th><th>Charge</th><th>Mass</th><th>Location</th></tr>
<tr><td>Proton</td><td>+1.6 × 10⁻¹⁹ C</td><td>1.672 × 10⁻²⁷ kg</td><td>Nucleus</td></tr>
<tr><td>Neutron</td><td>0</td><td>1.675 × 10⁻²⁷ kg</td><td>Nucleus</td></tr>
<tr><td>Electron</td><td>−1.6 × 10⁻¹⁹ C</td><td>9.1 × 10⁻³¹ kg</td><td>Shells</td></tr>
</table>
<h4>Important terms</h4>
<ul>
<li><b>Atomic number (Z):</b> Number of protons in the nucleus. In a neutral atom, number of electrons = number of protons, so the atom is electrically <b>neutral</b>.</li>
<li><b>Mass number (A):</b> Number of protons + number of neutrons.</li>
<li><b>Shells:</b> Named <b>K, L, M, N…</b> (n = 1, 2, 3, 4…) starting from the nucleus.</li>
<li><b>Maximum electrons in a shell = 2n²</b> → K = 2, L = 8, M = 18, N = 32. The outermost shell cannot hold more than 8 electrons.</li>
</ul>
<h4>Example: Silicon (Z = 14)</h4>
<p>Electron arrangement = <b>2, 8, 4</b> → K shell 2, L shell 8, M shell 4. So silicon has <b>4 electrons in its outermost shell</b> (see diagram).</p>
<p><b>Germanium (Z = 32):</b> 2, 8, 18, 4 → also 4 electrons in the outermost shell.</p>""",
          """<p>દરેક પદાર્થ અત્યંત નાના કણોનો બનેલો છે જેને <b>Atom</b> (પરમાણુ) કહે છે. <b>Bohr's atomic model</b> મુજબ atom ના બે ભાગ છે:</p>
<ol>
<li><b>Nucleus</b> (કેન્દ્ર): atom નો મધ્યનો, ભારે ભાગ. તેમાં <b>Protons</b> (ધન ચાર્જ) અને <b>Neutrons</b> (ચાર્જ રહિત) હોય છે. atom નું લગભગ સંપૂર્ણ દળ nucleus માં હોય છે.</li>
<li><b>Electrons:</b> ખૂબ હલકા, <b>ઋણ ચાર્જ</b>વાળા કણો, જે nucleus ની આસપાસ નિશ્ચિત વર્તુળાકાર માર્ગમાં ફરે છે, જેને <b>Orbits અથવા Shells</b> (કક્ષા) કહે છે.</li>
</ol>
<table>
<tr><th>કણ</th><th>ચાર્જ</th><th>દળ</th><th>સ્થાન</th></tr>
<tr><td>Proton</td><td>+1.6 × 10⁻¹⁹ C</td><td>1.672 × 10⁻²⁷ kg</td><td>Nucleus</td></tr>
<tr><td>Neutron</td><td>0</td><td>1.675 × 10⁻²⁷ kg</td><td>Nucleus</td></tr>
<tr><td>Electron</td><td>−1.6 × 10⁻¹⁹ C</td><td>9.1 × 10⁻³¹ kg</td><td>Shells</td></tr>
</table>
<h4>મહત્વના શબ્દો</h4>
<ul>
<li><b>Atomic number (Z):</b> nucleus માં રહેલા protons ની સંખ્યા. તટસ્થ atom માં electrons ની સંખ્યા = protons ની સંખ્યા, તેથી atom વિદ્યુતીય રીતે <b>Neutral</b> (તટસ્થ) હોય છે.</li>
<li><b>Mass number (A):</b> protons ની સંખ્યા + neutrons ની સંખ્યા.</li>
<li><b>Shells:</b> nucleus થી શરૂ કરીને <b>K, L, M, N…</b> (n = 1, 2, 3, 4…) નામ અપાય છે.</li>
<li><b>Shell માં મહત્તમ electrons = 2n²</b> → K = 2, L = 8, M = 18, N = 32. સૌથી બહારના shell માં 8 થી વધુ electrons રહી શકતા નથી.</li>
</ul>
<h4>ઉદાહરણ: Silicon (Z = 14)</h4>
<p>Electron ગોઠવણી = <b>2, 8, 4</b> → K shell માં 2, L shell માં 8, M shell માં 4. તેથી silicon ના <b>સૌથી બહારના shell માં 4 electrons</b> છે (આકૃતિ જુઓ).</p>
<p><b>Germanium (Z = 32):</b> 2, 8, 18, 4 → તેમાં પણ સૌથી બહારના shell માં 4 electrons છે.</p>""",
          diagram="u2_bohr_silicon"),

        T("2.1.2 Valence Electrons and Free Electrons", "2.1.2 Valence Electrons અને Free Electrons",
          """<h4>Valence electrons</h4>
<p>The electrons present in the <b>outermost shell</b> of an atom are called <b>valence electrons</b>, and the outermost shell is called the <b>valence shell</b>.</p>
<ul>
<li>Valence electrons are <b>loosely bound</b> to the nucleus because they are farthest from it, and the inner electrons partly shield them from the nucleus's attraction.</li>
<li>They decide the <b>electrical and chemical properties</b> of a material (conductivity, bonding, etc.).</li>
<li>Number of valence electrons → <b>Valency</b>. e.g. Silicon has 4 valence electrons.</li>
</ul>
<h4>Free electrons</h4>
<p>When a valence electron gets enough energy (from heat, light or an electric field), it <b>breaks away</b> from its atom and moves freely inside the material. Such electrons are called <b>free electrons</b>.</p>
<ul>
<li>Free electrons are responsible for <b>electric current</b>. When a voltage is applied, they drift towards the positive terminal.</li>
<li><b>More free electrons → higher conductivity.</b></li>
<li><b>Conductors</b> (copper, silver, aluminium) have a very large number of free electrons (about 10²⁸ per m³) even at room temperature.</li>
<li><b>Insulators</b> have almost no free electrons.</li>
<li><b>Semiconductors</b> have very few free electrons at room temperature; the number increases with temperature.</li>
</ul>
<h4>Relation of valence electrons with conductivity</h4>
<table>
<tr><th>Valence electrons</th><th>Nature</th><th>Examples</th></tr>
<tr><td>Less than 4 (1, 2, 3)</td><td>Conductor (usually metals)</td><td>Cu, Ag, Al</td></tr>
<tr><td>Exactly 4</td><td>Semiconductor</td><td>Si, Ge</td></tr>
<tr><td>More than 4 (5 to 8)</td><td>Insulator (usually non-metals)</td><td>Neon, glass, rubber</td></tr>
</table>
<p><i>Note:</i> This is a general rule. The exact behaviour is explained by the <b>energy band theory</b> (topic 2.1.4).</p>""",
          """<h4>Valence electrons</h4>
<p>atom ના <b>સૌથી બહારના shell</b> માં રહેલા electrons ને <b>Valence electrons</b> કહે છે, અને સૌથી બહારના shell ને <b>Valence shell</b> કહે છે.</p>
<ul>
<li>Valence electrons nucleus થી સૌથી દૂર હોવાથી અને અંદરના electrons nucleus ના આકર્ષણને અંશતઃ રોકતા હોવાથી, તે nucleus સાથે <b>ઢીલા બંધાયેલા (Loosely bound)</b> હોય છે.</li>
<li>તે પદાર્થના <b>વિદ્યુતીય અને રાસાયણિક ગુણધર્મો</b> (conductivity, bonding વગેરે) નક્કી કરે છે.</li>
<li>Valence electrons ની સંખ્યા → <b>Valency</b> (સંયોજકતા). દા.ત. Silicon માં 4 valence electrons છે.</li>
</ul>
<h4>Free electrons</h4>
<p>જ્યારે valence electron ને પૂરતી ઊર્જા (ઉષ્મા, પ્રકાશ કે electric field માંથી) મળે, ત્યારે તે પોતાના atom થી <b>છૂટો પડી</b> પદાર્થમાં મુક્ત રીતે ફરે છે. આવા electrons ને <b>Free electrons</b> (મુક્ત ઇલેક્ટ્રોન) કહે છે.</p>
<ul>
<li>Free electrons <b>Electric current</b> માટે જવાબદાર છે. Voltage આપતાં તે positive terminal તરફ ગતિ (drift) કરે છે.</li>
<li><b>વધુ free electrons → વધુ conductivity.</b></li>
<li><b>Conductors</b> (copper, silver, aluminium) માં room temperature પર પણ ખૂબ વધુ free electrons (આશરે 10²⁸ પ્રતિ m³) હોય છે.</li>
<li><b>Insulators</b> માં લગભગ free electrons હોતા નથી.</li>
<li><b>Semiconductors</b> માં room temperature પર ખૂબ ઓછા free electrons હોય છે; તાપમાન વધે તેમ તેની સંખ્યા વધે છે.</li>
</ul>
<h4>Valence electrons અને conductivity નો સંબંધ</h4>
<table>
<tr><th>Valence electrons</th><th>પ્રકૃતિ</th><th>ઉદાહરણ</th></tr>
<tr><td>4 થી ઓછા (1, 2, 3)</td><td>Conductor (મોટે ભાગે ધાતુઓ)</td><td>Cu, Ag, Al</td></tr>
<tr><td>બરાબર 4</td><td>Semiconductor</td><td>Si, Ge</td></tr>
<tr><td>4 થી વધુ (5 થી 8)</td><td>Insulator (મોટે ભાગે અધાતુઓ)</td><td>Neon, કાચ, રબર</td></tr>
</table>
<p><i>નોંધ:</i> આ સામાન્ય નિયમ છે. ચોક્કસ વર્તન <b>Energy band theory</b> (topic 2.1.4) દ્વારા સમજાવાય છે.</p>"""),

        T("2.1.3 Trivalent, Tetravalent and Pentavalent Materials", "2.1.3 Trivalent, Tetravalent અને Pentavalent પદાર્થો",
          """<p>Materials are named according to the <b>number of valence electrons</b> in their atoms. These three groups are very important in semiconductor technology.</p>
<h4>1. Trivalent materials (3 valence electrons)</h4>
<ul>
<li>Atoms have <b>3 electrons</b> in the outermost shell (Group III elements).</li>
<li>Examples: <b>Boron (B, Z = 5)</b>, <b>Aluminium (Al, Z = 13)</b>, <b>Gallium (Ga, Z = 31)</b>, <b>Indium (In, Z = 49)</b>.</li>
<li>Used as <b>acceptor impurity</b> to make <b>P-type</b> semiconductors.</li>
</ul>
<h4>2. Tetravalent materials (4 valence electrons)</h4>
<ul>
<li>Atoms have <b>4 electrons</b> in the outermost shell (Group IV elements).</li>
<li>Examples: <b>Silicon (Si, Z = 14)</b>, <b>Germanium (Ge, Z = 32)</b>, Carbon (C, Z = 6).</li>
<li>Si and Ge are the <b>basic semiconductor materials</b>.</li>
</ul>
<h4>3. Pentavalent materials (5 valence electrons)</h4>
<ul>
<li>Atoms have <b>5 electrons</b> in the outermost shell (Group V elements).</li>
<li>Examples: <b>Phosphorus (P, Z = 15)</b>, <b>Arsenic (As, Z = 33)</b>, <b>Antimony (Sb, Z = 51)</b>, Bismuth (Bi, Z = 83).</li>
<li>Used as <b>donor impurity</b> to make <b>N-type</b> semiconductors.</li>
</ul>
<table>
<tr><th>Type</th><th>Valence e⁻</th><th>Examples</th><th>Use</th></tr>
<tr><td>Trivalent</td><td>3</td><td>B, Al, Ga, In</td><td>Acceptor → P-type</td></tr>
<tr><td>Tetravalent</td><td>4</td><td>Si, Ge, C</td><td>Base semiconductor</td></tr>
<tr><td>Pentavalent</td><td>5</td><td>P, As, Sb, Bi</td><td>Donor → N-type</td></tr>
</table>""",
          """<p>પદાર્થોના atom માં રહેલા <b>valence electrons ની સંખ્યા</b> પ્રમાણે તેમને નામ અપાય છે. Semiconductor technology માં આ ત્રણ જૂથ ખૂબ મહત્વના છે.</p>
<h4>1. Trivalent પદાર્થો (3 valence electrons)</h4>
<ul>
<li>atom ના સૌથી બહારના shell માં <b>3 electrons</b> હોય છે (Group III તત્વો).</li>
<li>ઉદાહરણ: <b>Boron (B, Z = 5)</b>, <b>Aluminium (Al, Z = 13)</b>, <b>Gallium (Ga, Z = 31)</b>, <b>Indium (In, Z = 49)</b>.</li>
<li><b>P-type</b> semiconductor બનાવવા <b>Acceptor impurity</b> તરીકે વપરાય છે.</li>
</ul>
<h4>2. Tetravalent પદાર્થો (4 valence electrons)</h4>
<ul>
<li>atom ના સૌથી બહારના shell માં <b>4 electrons</b> હોય છે (Group IV તત્વો).</li>
<li>ઉદાહરણ: <b>Silicon (Si, Z = 14)</b>, <b>Germanium (Ge, Z = 32)</b>, Carbon (C, Z = 6).</li>
<li>Si અને Ge <b>મૂળભૂત semiconductor પદાર્થો</b> છે.</li>
</ul>
<h4>3. Pentavalent પદાર્થો (5 valence electrons)</h4>
<ul>
<li>atom ના સૌથી બહારના shell માં <b>5 electrons</b> હોય છે (Group V તત્વો).</li>
<li>ઉદાહરણ: <b>Phosphorus (P, Z = 15)</b>, <b>Arsenic (As, Z = 33)</b>, <b>Antimony (Sb, Z = 51)</b>, Bismuth (Bi, Z = 83).</li>
<li><b>N-type</b> semiconductor બનાવવા <b>Donor impurity</b> તરીકે વપરાય છે.</li>
</ul>
<table>
<tr><th>પ્રકાર</th><th>Valence e⁻</th><th>ઉદાહરણ</th><th>ઉપયોગ</th></tr>
<tr><td>Trivalent</td><td>3</td><td>B, Al, Ga, In</td><td>Acceptor → P-type</td></tr>
<tr><td>Tetravalent</td><td>4</td><td>Si, Ge, C</td><td>મૂળ semiconductor</td></tr>
<tr><td>Pentavalent</td><td>5</td><td>P, As, Sb, Bi</td><td>Donor → N-type</td></tr>
</table>""",
          diagram="u2_valence_atoms"),

        T("2.1.4 Energy Levels and Energy Bands", "2.1.4 Energy Levels અને Energy Bands",
          """<h4>Energy levels (in a single atom)</h4>
<ul>
<li>Each shell of an atom has a fixed amount of energy, called an <b>energy level</b>.</li>
<li>Electrons in inner shells are <b>tightly bound</b> (strong attraction of nucleus). Electrons in outer shells are <b>loosely bound</b>.</li>
<li>To remove an electron from an atom, energy must be given to it. The valence electron needs the <b>least energy</b> to become free.</li>
<li>Energy of electrons is measured in <b>electron-volt (eV)</b>. <b>1 eV = 1.6 × 10⁻¹⁹ J</b>.</li>
</ul>
<h4>Energy bands (in a solid)</h4>
<p>In a solid crystal, atoms are very close to each other, so their energy levels interact and split into a large number of closely spaced levels. These closely spaced levels form a continuous range called an <b>energy band</b>. Three bands are important:</p>
<ol>
<li><b>Valence Band (VB):</b> The band formed by the energy levels of <b>valence electrons</b>. It is the highest band that is filled (or partly filled) with electrons.</li>
<li><b>Conduction Band (CB):</b> The higher band where electrons are <b>free</b> to move and conduct current. Electrons in the conduction band are free electrons.</li>
<li><b>Forbidden Energy Gap (E<sub>g</sub>):</b> The energy gap between the top of the valence band and the bottom of the conduction band. <b>No electron can exist in this gap.</b> An electron must get energy at least equal to E<sub>g</sub> to jump from VB to CB.</li>
</ol>
<p><b>The size of E<sub>g</sub> decides whether a material is a conductor, semiconductor or insulator</b> (see next topic).</p>""",
          """<h4>Energy levels (એક atom માં)</h4>
<ul>
<li>atom ના દરેક shell ની નિશ્ચિત ઊર્જા હોય છે, જેને <b>Energy level</b> (ઊર્જા સ્તર) કહે છે.</li>
<li>અંદરના shells ના electrons <b>મજબૂત રીતે બંધાયેલા (Tightly bound)</b> હોય છે (nucleus નું વધુ આકર્ષણ). બહારના shells ના electrons <b>ઢીલા બંધાયેલા (Loosely bound)</b> હોય છે.</li>
<li>atom માંથી electron દૂર કરવા તેને ઊર્જા આપવી પડે છે. Valence electron ને મુક્ત થવા માટે <b>સૌથી ઓછી ઊર્જા</b> જોઈએ છે.</li>
<li>Electrons ની ઊર્જા <b>electron-volt (eV)</b> માં મપાય છે. <b>1 eV = 1.6 × 10⁻¹⁹ J</b>.</li>
</ul>
<h4>Energy bands (solid માં)</h4>
<p>Solid crystal માં atoms એકબીજાની ખૂબ નજીક હોય છે, તેથી તેમના energy levels એકબીજા પર અસર કરી ખૂબ નજીક-નજીકના અનેક levels માં વિભાજિત થાય છે. આ નજીકના levels ની સળંગ રેન્જને <b>Energy band</b> કહે છે. ત્રણ bands મહત્વના છે:</p>
<ol>
<li><b>Valence Band (VB):</b> <b>Valence electrons</b> ના energy levels થી બનતો band. તે electrons થી ભરેલો (કે અંશતઃ ભરેલો) સૌથી ઊંચો band છે.</li>
<li><b>Conduction Band (CB):</b> ઉપરનો band, જ્યાં electrons <b>મુક્ત</b> રીતે ફરી current વહન કરી શકે છે. Conduction band ના electrons free electrons છે.</li>
<li><b>Forbidden Energy Gap (E<sub>g</sub>):</b> Valence band ની ટોચ અને conduction band ના તળિયા વચ્ચેનો energy gap. <b>આ gap માં કોઈ electron રહી શકતો નથી.</b> VB થી CB માં જવા electron ને ઓછામાં ઓછી E<sub>g</sub> જેટલી ઊર્જા મળવી જોઈએ.</li>
</ol>
<p><b>E<sub>g</sub> નું મૂલ્ય નક્કી કરે છે કે પદાર્થ conductor, semiconductor કે insulator છે</b> (આગળનો topic જુઓ).</p>"""),

        T("2.1.5 Conductors, Semiconductors and Insulators (Conductivity)", "2.1.5 Conductors, Semiconductors અને Insulators (Conductivity)",
          """<p>On the basis of <b>conductivity</b> (ability to conduct current) and <b>energy band structure</b>, materials are classified into three types:</p>
<h4>1. Conductors</h4>
<ul>
<li>The valence band and conduction band <b>overlap</b> – there is <b>no forbidden gap</b>.</li>
<li>A huge number of free electrons are always available, so current flows easily.</li>
<li>Very low resistivity (≈ 10⁻⁸ Ω·m). Examples: <b>Copper, Silver, Aluminium, Gold</b>.</li>
<li>Resistance <b>increases</b> with temperature (positive temperature coefficient).</li>
</ul>
<h4>2. Insulators</h4>
<ul>
<li>The forbidden gap is <b>very large (E<sub>g</sub> &gt; 5 eV)</b>, e.g. diamond ≈ 5.5 eV.</li>
<li>Normal heat or voltage cannot give this much energy, so there are practically <b>no free electrons</b>.</li>
<li>Very high resistivity (&gt; 10¹⁰ Ω·m). Examples: <b>Glass, Rubber, Mica, Wood, Plastic, Diamond</b>.</li>
</ul>
<h4>3. Semiconductors</h4>
<ul>
<li>The forbidden gap is <b>small (about 1 eV)</b>: <b>Si = 1.1 eV</b>, <b>Ge = 0.7 eV</b> (at room temperature).</li>
<li>At <b>0 K</b> (absolute zero), VB is full and CB is empty → semiconductor acts as an <b>insulator</b>.</li>
<li>At <b>room temperature</b>, some electrons get enough thermal energy to cross the gap → small conduction.</li>
<li>Resistivity lies between conductors and insulators (≈ 10⁻⁵ to 10⁴ Ω·m approx.).</li>
<li>Resistance <b>decreases</b> with temperature (<b>negative temperature coefficient</b>).</li>
</ul>
<table>
<tr><th>Property</th><th>Conductor</th><th>Semiconductor</th><th>Insulator</th></tr>
<tr><td>Forbidden gap E<sub>g</sub></td><td>Zero (bands overlap)</td><td>Small (≈ 1 eV)</td><td>Large (&gt; 5 eV)</td></tr>
<tr><td>Valence electrons</td><td>Usually &lt; 4</td><td>4</td><td>Usually &gt; 4</td></tr>
<tr><td>Free electrons</td><td>Very large</td><td>Few (increase with temperature)</td><td>Almost none</td></tr>
<tr><td>Conductivity</td><td>Very high</td><td>Medium</td><td>Very low</td></tr>
<tr><td>Temperature coefficient of resistance</td><td>Positive</td><td>Negative</td><td>Negative</td></tr>
<tr><td>Current carriers</td><td>Electrons</td><td>Electrons and holes</td><td>–</td></tr>
<tr><td>Examples</td><td>Cu, Ag, Al</td><td>Si, Ge, GaAs</td><td>Glass, mica, rubber</td></tr>
</table>""",
          """<p><b>Conductivity</b> (current વહન કરવાની ક્ષમતા) અને <b>Energy band structure</b> ના આધારે પદાર્થોને ત્રણ પ્રકારમાં વહેંચવામાં આવે છે:</p>
<h4>1. Conductors (વાહકો)</h4>
<ul>
<li>Valence band અને conduction band એકબીજા પર <b>Overlap</b> થાય છે – <b>કોઈ forbidden gap નથી</b>.</li>
<li>હંમેશા ખૂબ વધુ free electrons ઉપલબ્ધ હોય છે, તેથી current સરળતાથી વહે છે.</li>
<li>ખૂબ ઓછી resistivity (≈ 10⁻⁸ Ω·m). ઉદાહરણ: <b>Copper, Silver, Aluminium, Gold</b>.</li>
<li>તાપમાન વધે તેમ resistance <b>વધે</b> છે (positive temperature coefficient).</li>
</ul>
<h4>2. Insulators (અવાહકો)</h4>
<ul>
<li>Forbidden gap <b>ખૂબ મોટો (E<sub>g</sub> &gt; 5 eV)</b> હોય છે, દા.ત. diamond ≈ 5.5 eV.</li>
<li>સામાન્ય ઉષ્મા કે voltage આટલી ઊર્જા આપી શકતા નથી, તેથી વ્યવહારમાં <b>કોઈ free electrons હોતા નથી</b>.</li>
<li>ખૂબ વધુ resistivity (&gt; 10¹⁰ Ω·m). ઉદાહરણ: <b>કાચ, રબર, Mica, લાકડું, પ્લાસ્ટિક, Diamond</b>.</li>
</ul>
<h4>3. Semiconductors (અર્ધવાહકો)</h4>
<ul>
<li>Forbidden gap <b>નાનો (આશરે 1 eV)</b>: <b>Si = 1.1 eV</b>, <b>Ge = 0.7 eV</b> (room temperature પર).</li>
<li><b>0 K</b> (absolute zero) પર VB સંપૂર્ણ ભરેલો અને CB ખાલી હોય છે → semiconductor <b>Insulator</b> તરીકે વર્તે છે.</li>
<li><b>Room temperature</b> પર કેટલાક electrons ને gap પાર કરવા પૂરતી thermal energy મળે છે → થોડું conduction.</li>
<li>Resistivity conductors અને insulators ની વચ્ચે હોય છે (આશરે 10⁻⁵ થી 10⁴ Ω·m).</li>
<li>તાપમાન વધે તેમ resistance <b>ઘટે</b> છે (<b>Negative temperature coefficient</b>).</li>
</ul>
<table>
<tr><th>ગુણધર્મ</th><th>Conductor</th><th>Semiconductor</th><th>Insulator</th></tr>
<tr><td>Forbidden gap E<sub>g</sub></td><td>શૂન્ય (bands overlap)</td><td>નાનો (≈ 1 eV)</td><td>મોટો (&gt; 5 eV)</td></tr>
<tr><td>Valence electrons</td><td>સામાન્ય રીતે &lt; 4</td><td>4</td><td>સામાન્ય રીતે &gt; 4</td></tr>
<tr><td>Free electrons</td><td>ખૂબ વધુ</td><td>થોડા (તાપમાન સાથે વધે)</td><td>લગભગ નહીં</td></tr>
<tr><td>Conductivity</td><td>ખૂબ વધુ</td><td>મધ્યમ</td><td>ખૂબ ઓછી</td></tr>
<tr><td>Resistance નો temperature coefficient</td><td>Positive</td><td>Negative</td><td>Negative</td></tr>
<tr><td>Current carriers</td><td>Electrons</td><td>Electrons અને holes</td><td>–</td></tr>
<tr><td>ઉદાહરણ</td><td>Cu, Ag, Al</td><td>Si, Ge, GaAs</td><td>કાચ, mica, રબર</td></tr>
</table>""",
          diagram="u2_energy_bands"),

        T("Key Points – 2.1", "મુખ્ય મુદ્દા – 2.1",
          """<ul>
<li>Atom = nucleus (protons + neutrons) + electrons in shells K, L, M, N.</li>
<li>Maximum electrons in a shell = <b>2n²</b>; Si = 2, 8, 4; Ge = 2, 8, 18, 4.</li>
<li>Electrons in the outermost shell = <b>valence electrons</b>; they decide conductivity.</li>
<li>Electrons that leave the atom and move freely = <b>free electrons</b>; they carry current.</li>
<li>Trivalent (B, Al, Ga, In) → P-type; Tetravalent (Si, Ge); Pentavalent (P, As, Sb) → N-type.</li>
<li>Energy bands: <b>Valence band, Conduction band, Forbidden gap (E<sub>g</sub>)</b>.</li>
<li>E<sub>g</sub>: Conductor = 0 (overlap), Semiconductor ≈ 1 eV (Si 1.1, Ge 0.7), Insulator &gt; 5 eV.</li>
<li>Semiconductors have a <b>negative temperature coefficient</b> of resistance.</li>
</ul>""",
          """<ul>
<li>Atom = nucleus (protons + neutrons) + shells K, L, M, N માં electrons.</li>
<li>Shell માં મહત્તમ electrons = <b>2n²</b>; Si = 2, 8, 4; Ge = 2, 8, 18, 4.</li>
<li>સૌથી બહારના shell ના electrons = <b>Valence electrons</b>; તે conductivity નક્કી કરે છે.</li>
<li>atom છોડીને મુક્ત રીતે ફરતા electrons = <b>Free electrons</b>; તે current વહન કરે છે.</li>
<li>Trivalent (B, Al, Ga, In) → P-type; Tetravalent (Si, Ge); Pentavalent (P, As, Sb) → N-type.</li>
<li>Energy bands: <b>Valence band, Conduction band, Forbidden gap (E<sub>g</sub>)</b>.</li>
<li>E<sub>g</sub>: Conductor = 0 (overlap), Semiconductor ≈ 1 eV (Si 1.1, Ge 0.7), Insulator &gt; 5 eV.</li>
<li>Semiconductors નો resistance નો <b>Negative temperature coefficient</b> હોય છે.</li>
</ul>""", key=True),
    ],
}

# =====================================================================================
SEC_2_2 = {
    "title": {"en": "2.2 Semiconductors and Doping", "gu": "2.2 Semiconductors અને Doping"},
    "items": [
        T("2.2.1 Semiconductor – Definition and Properties", "2.2.1 Semiconductor – વ્યાખ્યા અને ગુણધર્મો",
          """<p>A <b>semiconductor</b> is a material whose <b>electrical conductivity lies between that of conductors and insulators</b>. Its forbidden energy gap is small (about 1 eV).</p>
<p><b>Examples:</b> <b>Silicon (Si)</b>, <b>Germanium (Ge)</b> – elemental semiconductors; Gallium Arsenide (GaAs), Indium Phosphide (InP) – compound semiconductors.</p>
<h4>Properties of semiconductors</h4>
<ol>
<li>Conductivity is between conductors and insulators.</li>
<li><b>Negative temperature coefficient:</b> resistance decreases (conductivity increases) as temperature increases.</li>
<li>Conductivity increases greatly when a small amount of <b>impurity</b> is added (<b>doping</b>).</li>
<li>Conductivity increases when <b>light</b> falls on it (used in photodiodes, solar cells, LDR).</li>
<li>Current is carried by <b>two types of carriers: electrons and holes</b>.</li>
<li>Atoms are joined by <b>covalent bonds</b> in a crystal structure.</li>
</ol>
<h4>Why is silicon preferred over germanium?</h4>
<ul>
<li>Si has a larger energy gap (1.1 eV vs 0.7 eV) → <b>less leakage current</b> and can work at <b>higher temperature</b> (≈ 150–200 °C vs ≈ 75–100 °C for Ge).</li>
<li>Si is <b>abundant</b> (sand – SiO₂) and <b>cheaper</b>.</li>
<li>Si forms a good protective oxide layer (SiO₂), which is essential for making <b>ICs</b>.</li>
</ul>
<h4>Applications</h4>
<p>Diodes, transistors, ICs, microprocessors, solar cells, LEDs, sensors, memory chips.</p>""",
          """<p><b>Semiconductor</b> એવો પદાર્થ છે જેની <b>electrical conductivity, conductors અને insulators ની વચ્ચે</b> હોય છે. તેનો forbidden energy gap નાનો (આશરે 1 eV) હોય છે.</p>
<p><b>ઉદાહરણ:</b> <b>Silicon (Si)</b>, <b>Germanium (Ge)</b> – elemental semiconductors; Gallium Arsenide (GaAs), Indium Phosphide (InP) – compound semiconductors.</p>
<h4>Semiconductors ના ગુણધર્મો</h4>
<ol>
<li>Conductivity, conductors અને insulators ની વચ્ચે હોય છે.</li>
<li><b>Negative temperature coefficient:</b> તાપમાન વધે તેમ resistance ઘટે (conductivity વધે).</li>
<li>થોડી માત્રામાં <b>Impurity</b> ઉમેરવાથી (<b>Doping</b>) conductivity ખૂબ વધી જાય છે.</li>
<li>તેના પર <b>પ્રકાશ</b> પડે ત્યારે conductivity વધે છે (photodiode, solar cell, LDR માં ઉપયોગ).</li>
<li>Current <b>બે પ્રકારના carriers: electrons અને holes</b> દ્વારા વહે છે.</li>
<li>Crystal structure માં atoms <b>Covalent bonds</b> થી જોડાયેલા હોય છે.</li>
</ol>
<h4>Germanium કરતાં Silicon શા માટે વધુ પસંદ થાય છે?</h4>
<ul>
<li>Si નો energy gap મોટો (1.1 eV vs 0.7 eV) → <b>ઓછો leakage current</b> અને <b>વધુ તાપમાને</b> કામ કરી શકે (Si ≈ 150–200 °C, Ge ≈ 75–100 °C).</li>
<li>Si <b>વિપુલ પ્રમાણમાં</b> (રેતી – SiO₂) મળે છે અને <b>સસ્તું</b> છે.</li>
<li>Si સારું રક્ષણાત્મક oxide layer (SiO₂) બનાવે છે, જે <b>ICs</b> બનાવવા માટે જરૂરી છે.</li>
</ul>
<h4>ઉપયોગો</h4>
<p>Diodes, transistors, ICs, microprocessors, solar cells, LEDs, sensors, memory chips.</p>"""),

        T("2.2.2 Crystal Structure and Covalent Bonds", "2.2.2 Crystal Structure અને Covalent Bonds",
          """<p>Silicon and germanium atoms arrange themselves in a regular, repeating 3-D pattern called a <b>crystal lattice</b>.</p>
<ul>
<li>Each Si atom has <b>4 valence electrons</b> and is surrounded by <b>4 neighbouring Si atoms</b>.</li>
<li>Each atom <b>shares one valence electron</b> with each of its 4 neighbours, and each neighbour shares one electron back.</li>
<li>Such a bond, formed by <b>sharing a pair of electrons</b> between two atoms, is called a <b>covalent bond</b>.</li>
<li>So each atom effectively has <b>8 electrons</b> in its outer shell → a <b>stable</b> structure.</li>
</ul>
<p>In the diagram, each line between two atoms is a covalent bond, and the two dots on it are the shared electron pair.</p>
<p><b>Result:</b> At <b>0 K</b> all valence electrons are tightly held in covalent bonds and there are <b>no free electrons</b> – pure silicon behaves as a <b>perfect insulator</b>.</p>""",
          """<p>Silicon અને germanium ના atoms એક નિયમિત, પુનરાવર્તિત 3-D રચનામાં ગોઠવાય છે, જેને <b>Crystal lattice</b> કહે છે.</p>
<ul>
<li>દરેક Si atom માં <b>4 valence electrons</b> હોય છે અને તે <b>4 પડોશી Si atoms</b> થી ઘેરાયેલો હોય છે.</li>
<li>દરેક atom તેના 4 પડોશીઓ સાથે <b>એક-એક valence electron ની ભાગીદારી (Sharing)</b> કરે છે, અને દરેક પડોશી પણ એક electron ની ભાગીદારી કરે છે.</li>
<li>બે atoms વચ્ચે <b>electrons ની જોડીની ભાગીદારી</b> થી બનતા bond ને <b>Covalent bond</b> (સહસંયોજક બંધ) કહે છે.</li>
<li>આમ દરેક atom ના બહારના shell માં અસરકારક રીતે <b>8 electrons</b> થાય છે → <b>Stable</b> (સ્થિર) રચના.</li>
</ul>
<p>આકૃતિમાં બે atoms વચ્ચેની દરેક રેખા covalent bond છે, અને તેના પરના બે ટપકાં ભાગીદારીવાળી electron જોડી છે.</p>
<p><b>પરિણામ:</b> <b>0 K</b> પર બધા valence electrons covalent bonds માં મજબૂત રીતે બંધાયેલા હોય છે અને <b>કોઈ free electrons નથી</b> – શુદ્ધ silicon <b>સંપૂર્ણ Insulator</b> તરીકે વર્તે છે.</p>""",
          diagram="u2_covalent_si"),

        T("2.2.3 Intrinsic Semiconductor", "2.2.3 Intrinsic Semiconductor",
          """<p>A <b>pure</b> semiconductor, without any impurity, is called an <b>intrinsic semiconductor</b>. e.g. pure silicon, pure germanium.</p>
<h4>Working</h4>
<ul>
<li><b>At 0 K:</b> All electrons are held in covalent bonds. No free electrons → acts as an <b>insulator</b>.</li>
<li><b>At room temperature (≈ 300 K):</b> Some valence electrons get <b>thermal energy</b> greater than E<sub>g</sub>. They <b>break their covalent bonds</b> and become free electrons (they jump from VB to CB).</li>
<li>When an electron leaves a bond, it leaves behind a <b>vacancy</b> in the bond. This vacancy is called a <b>hole</b>. A hole acts as a <b>positive charge</b>.</li>
<li>Thus electrons and holes are always produced <b>in pairs</b> → called <b>electron–hole pairs</b> (thermal generation).</li>
<li>Sometimes a free electron falls back into a hole – this is called <b>recombination</b>.</li>
</ul>
<h4>Important features</h4>
<ul>
<li>Number of free electrons = number of holes: <b>n = p = n<sub>i</sub></b> (n<sub>i</sub> = intrinsic carrier concentration).</li>
<li>For Si at 300 K, n<sub>i</sub> ≈ 1.5 × 10¹⁰ per cm³ (very small compared to ≈ 5 × 10²² atoms per cm³).</li>
<li>Current is carried by both <b>electrons</b> (towards +ve terminal) and <b>holes</b> (towards −ve terminal). Total current I = I<sub>e</sub> + I<sub>h</sub>.</li>
<li>Conductivity is <b>very low</b> and depends strongly on <b>temperature</b>, so intrinsic semiconductors are rarely used directly.</li>
</ul>""",
          """<p>કોઈપણ impurity વગરના <b>શુદ્ધ</b> semiconductor ને <b>Intrinsic semiconductor</b> કહે છે. દા.ત. શુદ્ધ silicon, શુદ્ધ germanium.</p>
<h4>કાર્ય</h4>
<ul>
<li><b>0 K પર:</b> બધા electrons covalent bonds માં બંધાયેલા હોય છે. કોઈ free electrons નથી → <b>Insulator</b> તરીકે વર્તે છે.</li>
<li><b>Room temperature (≈ 300 K) પર:</b> કેટલાક valence electrons ને E<sub>g</sub> કરતાં વધુ <b>Thermal energy</b> મળે છે. તે પોતાના <b>covalent bond તોડીને</b> free electrons બને છે (VB થી CB માં જાય છે).</li>
<li>Electron bond છોડે ત્યારે bond માં એક <b>ખાલી જગ્યા (Vacancy)</b> છોડી જાય છે. આ ખાલી જગ્યાને <b>Hole</b> કહે છે. Hole <b>Positive charge</b> તરીકે વર્તે છે.</li>
<li>આમ electrons અને holes હંમેશા <b>જોડીમાં</b> ઉત્પન્ન થાય છે → <b>Electron–hole pairs</b> (thermal generation).</li>
<li>ક્યારેક free electron ફરી hole માં પડે છે – તેને <b>Recombination</b> કહે છે.</li>
</ul>
<h4>મહત્વની લાક્ષણિકતાઓ</h4>
<ul>
<li>Free electrons ની સંખ્યા = holes ની સંખ્યા: <b>n = p = n<sub>i</sub></b> (n<sub>i</sub> = intrinsic carrier concentration).</li>
<li>300 K પર Si માટે n<sub>i</sub> ≈ 1.5 × 10¹⁰ પ્રતિ cm³ (≈ 5 × 10²² atoms પ્રતિ cm³ ની સરખામણીમાં ખૂબ ઓછું).</li>
<li>Current <b>Electrons</b> (+ve terminal તરફ) અને <b>Holes</b> (−ve terminal તરફ) બંને દ્વારા વહે છે. કુલ current I = I<sub>e</sub> + I<sub>h</sub>.</li>
<li>Conductivity <b>ખૂબ ઓછી</b> છે અને <b>તાપમાન</b> પર ખૂબ આધાર રાખે છે, તેથી intrinsic semiconductors સીધા ભાગ્યે જ વપરાય છે.</li>
</ul>""",
          diagram="u2_intrinsic", examples=["u2n1"]),

        T("2.2.4 Concept of Hole and Hole Current", "2.2.4 Hole અને Hole Current નો ખ્યાલ",
          """<p>A <b>hole</b> is the <b>vacancy (absence of an electron)</b> in a covalent bond. Since the atom has lost a negative electron, the hole behaves like a <b>positive charge (+1.6 × 10⁻¹⁹ C)</b>.</p>
<h4>How does a hole move?</h4>
<ol>
<li>Suppose a hole is present in a bond at position A.</li>
<li>A valence electron from a nearby bond B jumps into the hole at A (it needs very little energy).</li>
<li>Now the hole appears at B. Then an electron from C fills B, and the hole moves to C, and so on.</li>
</ol>
<p>So when <b>valence electrons move in one direction</b> (towards +ve terminal), the <b>hole moves in the opposite direction</b> (towards −ve terminal). This movement of holes is called <b>hole current</b>.</p>
<h4>Difference between electron current and hole current</h4>
<table>
<tr><th>Electron current</th><th>Hole current</th></tr>
<tr><td>Due to free electrons in the <b>conduction band</b></td><td>Due to movement of valence electrons in the <b>valence band</b></td></tr>
<tr><td>Electrons move towards +ve terminal</td><td>Holes move towards −ve terminal</td></tr>
<tr><td>Higher mobility (moves faster)</td><td>Lower mobility (moves slower)</td></tr>
</table>
<p>Both currents are in the <b>same conventional direction</b>, so they add up: <b>I = I<sub>e</sub> + I<sub>h</sub></b>.</p>""",
          """<p><b>Hole</b> એટલે covalent bond માં <b>ખાલી જગ્યા (electron ની ગેરહાજરી)</b>. atom એ negative electron ગુમાવ્યો હોવાથી hole <b>Positive charge (+1.6 × 10⁻¹⁹ C)</b> તરીકે વર્તે છે.</p>
<h4>Hole કેવી રીતે ગતિ કરે છે?</h4>
<ol>
<li>ધારો કે સ્થાન A પરના bond માં hole છે.</li>
<li>નજીકના bond B માંથી એક valence electron A ના hole માં કૂદી જાય છે (તેને ખૂબ ઓછી ઊર્જા જોઈએ છે).</li>
<li>હવે hole B પર દેખાય છે. પછી C માંથી electron B ને ભરે છે, અને hole C પર જાય છે, એ રીતે આગળ.</li>
</ol>
<p>આમ જ્યારે <b>valence electrons એક દિશામાં</b> (+ve terminal તરફ) ગતિ કરે, ત્યારે <b>hole વિરુદ્ધ દિશામાં</b> (−ve terminal તરફ) ગતિ કરે છે. holes ની આ ગતિને <b>Hole current</b> કહે છે.</p>
<h4>Electron current અને Hole current વચ્ચે તફાવત</h4>
<table>
<tr><th>Electron current</th><th>Hole current</th></tr>
<tr><td><b>Conduction band</b> ના free electrons ને કારણે</td><td><b>Valence band</b> માં valence electrons ની ગતિને કારણે</td></tr>
<tr><td>Electrons +ve terminal તરફ જાય</td><td>Holes −ve terminal તરફ જાય</td></tr>
<tr><td>વધુ mobility (ઝડપી)</td><td>ઓછી mobility (ધીમું)</td></tr>
</table>
<p>બંને currents ની <b>Conventional દિશા સમાન</b> છે, તેથી તે ઉમેરાય છે: <b>I = I<sub>e</sub> + I<sub>h</sub></b>.</p>"""),

        T("2.2.5 Doping", "2.2.5 Doping",
          """<p>The process of <b>adding a very small, controlled amount of suitable impurity</b> to a pure (intrinsic) semiconductor to <b>increase its conductivity</b> is called <b>doping</b>.</p>
<ul>
<li>The impurity atoms added are called <b>dopants</b>.</li>
<li>Doping level is very small – typically <b>1 impurity atom for every 10⁶ to 10⁸ semiconductor atoms</b>.</li>
<li>Even this tiny amount increases the conductivity by a very large factor (thousands of times or more).</li>
</ul>
<h4>Types of dopants (impurities)</h4>
<table>
<tr><th>Point</th><th>Donor impurity</th><th>Acceptor impurity</th></tr>
<tr><td>Valency</td><td>Pentavalent (5)</td><td>Trivalent (3)</td></tr>
<tr><td>Examples</td><td>P, As, Sb, Bi</td><td>B, Al, Ga, In</td></tr>
<tr><td>Action</td><td><b>Donates</b> one free electron</td><td><b>Accepts</b> one electron (creates a hole)</td></tr>
<tr><td>Semiconductor formed</td><td>N-type</td><td>P-type</td></tr>
</table>
<h4>Methods of doping</h4>
<ol>
<li><b>Adding impurity in the molten state</b> during crystal growth.</li>
<li><b>Diffusion:</b> heating the semiconductor wafer in a gas containing impurity atoms; atoms diffuse into it.</li>
<li><b>Ion implantation:</b> bombarding the wafer with high-energy impurity ions.</li>
</ol>
<h4>Purpose of doping</h4>
<ul>
<li>To <b>increase conductivity</b> of the semiconductor.</li>
<li>To make the semiconductor carry current mainly by <b>one type of carrier</b> (electrons or holes).</li>
<li>To make <b>P-type and N-type</b> materials, which are needed to build diodes, transistors and ICs.</li>
</ul>""",
          """<p>શુદ્ધ (intrinsic) semiconductor ની <b>Conductivity વધારવા</b> માટે તેમાં <b>યોગ્ય impurity ની ખૂબ ઓછી, નિયંત્રિત માત્રા ઉમેરવાની</b> પ્રક્રિયાને <b>Doping</b> કહે છે.</p>
<ul>
<li>ઉમેરાતા impurity atoms ને <b>Dopants</b> કહે છે.</li>
<li>Doping નું પ્રમાણ ખૂબ ઓછું હોય છે – સામાન્ય રીતે <b>10⁶ થી 10⁸ semiconductor atoms દીઠ 1 impurity atom</b>.</li>
<li>આટલી નાની માત્રા પણ conductivity ને ખૂબ મોટા પ્રમાણમાં (હજારો ગણી કે વધુ) વધારી દે છે.</li>
</ul>
<h4>Dopants (impurities) ના પ્રકાર</h4>
<table>
<tr><th>મુદ્દો</th><th>Donor impurity</th><th>Acceptor impurity</th></tr>
<tr><td>Valency</td><td>Pentavalent (5)</td><td>Trivalent (3)</td></tr>
<tr><td>ઉદાહરણ</td><td>P, As, Sb, Bi</td><td>B, Al, Ga, In</td></tr>
<tr><td>કાર્ય</td><td>એક free electron <b>આપે (Donate)</b></td><td>એક electron <b>સ્વીકારે (Accept)</b> (hole બનાવે)</td></tr>
<tr><td>બનતો semiconductor</td><td>N-type</td><td>P-type</td></tr>
</table>
<h4>Doping ની પદ્ધતિઓ</h4>
<ol>
<li>Crystal growth દરમિયાન <b>પીગળેલી અવસ્થામાં impurity ઉમેરવી</b>.</li>
<li><b>Diffusion:</b> semiconductor wafer ને impurity atoms વાળા gas માં ગરમ કરવું; atoms તેમાં પ્રસરે છે.</li>
<li><b>Ion implantation:</b> wafer પર ઊંચી ઊર્જાવાળા impurity ions નો મારો કરવો.</li>
</ol>
<h4>Doping નો હેતુ</h4>
<ul>
<li>Semiconductor ની <b>Conductivity વધારવી</b>.</li>
<li>Semiconductor માં current મુખ્યત્વે <b>એક જ પ્રકારના carrier</b> (electrons કે holes) થી વહે તેમ કરવું.</li>
<li>Diodes, transistors અને ICs બનાવવા જરૂરી <b>P-type અને N-type</b> પદાર્થો બનાવવા.</li>
</ul>""",
          examples=["u2n3"]),

        T("2.2.6 Extrinsic Semiconductor", "2.2.6 Extrinsic Semiconductor",
          """<p>A semiconductor to which a suitable impurity has been added (i.e. a <b>doped semiconductor</b>) is called an <b>extrinsic semiconductor</b>.</p>
<p>Depending on the type of impurity, extrinsic semiconductors are of two types:</p>
<ol>
<li><b>N-type semiconductor</b> – doped with <b>pentavalent (donor)</b> impurity. Majority carriers: electrons.</li>
<li><b>P-type semiconductor</b> – doped with <b>trivalent (acceptor)</b> impurity. Majority carriers: holes.</li>
</ol>
<h4>Intrinsic vs Extrinsic semiconductor</h4>
<table>
<tr><th>Point</th><th>Intrinsic</th><th>Extrinsic</th></tr>
<tr><td>Purity</td><td>Pure semiconductor</td><td>Doped (impurity added)</td></tr>
<tr><td>Carriers</td><td>n = p (equal)</td><td>n ≠ p (one type is majority)</td></tr>
<tr><td>Conductivity</td><td>Very low</td><td>High</td></tr>
<tr><td>Dependence on temperature</td><td>Conductivity depends strongly on temperature</td><td>Depends mainly on doping level</td></tr>
<tr><td>Types</td><td>No types</td><td>N-type and P-type</td></tr>
<tr><td>Practical use</td><td>Rarely used directly</td><td>Used in all devices (diode, transistor, IC)</td></tr>
</table>""",
          """<p>જે semiconductor માં યોગ્ય impurity ઉમેરવામાં આવી હોય (એટલે કે <b>Doped semiconductor</b>) તેને <b>Extrinsic semiconductor</b> કહે છે.</p>
<p>Impurity ના પ્રકાર પ્રમાણે extrinsic semiconductors બે પ્રકારના છે:</p>
<ol>
<li><b>N-type semiconductor</b> – <b>Pentavalent (donor)</b> impurity થી doped. Majority carriers: electrons.</li>
<li><b>P-type semiconductor</b> – <b>Trivalent (acceptor)</b> impurity થી doped. Majority carriers: holes.</li>
</ol>
<h4>Intrinsic vs Extrinsic semiconductor</h4>
<table>
<tr><th>મુદ્દો</th><th>Intrinsic</th><th>Extrinsic</th></tr>
<tr><td>શુદ્ધતા</td><td>શુદ્ધ semiconductor</td><td>Doped (impurity ઉમેરેલ)</td></tr>
<tr><td>Carriers</td><td>n = p (સમાન)</td><td>n ≠ p (એક પ્રકાર majority)</td></tr>
<tr><td>Conductivity</td><td>ખૂબ ઓછી</td><td>વધુ</td></tr>
<tr><td>તાપમાન પર આધાર</td><td>Conductivity તાપમાન પર ખૂબ આધાર રાખે</td><td>મુખ્યત્વે doping level પર આધાર</td></tr>
<tr><td>પ્રકાર</td><td>કોઈ પ્રકાર નથી</td><td>N-type અને P-type</td></tr>
<tr><td>વ્યવહારુ ઉપયોગ</td><td>સીધો ભાગ્યે જ ઉપયોગ</td><td>બધા devices માં ઉપયોગ (diode, transistor, IC)</td></tr>
</table>"""),

        T("Key Points – 2.2", "મુખ્ય મુદ્દા – 2.2",
          """<ul>
<li>Semiconductor: conductivity between conductor and insulator; E<sub>g</sub> ≈ 1 eV; negative temperature coefficient.</li>
<li>Si is preferred over Ge: larger E<sub>g</sub>, lower leakage, higher temperature operation, cheaper.</li>
<li>Atoms in Si crystal are joined by <b>covalent bonds</b> (sharing electron pairs).</li>
<li><b>Intrinsic</b> = pure; electron–hole pairs generated by heat; <b>n = p = n<sub>i</sub></b>.</li>
<li><b>Hole</b> = vacancy of electron in a bond; acts as positive charge; moves opposite to electrons.</li>
<li><b>Doping</b> = adding 1 impurity atom per 10⁶–10⁸ atoms to increase conductivity.</li>
<li>Donor (pentavalent) → N-type; Acceptor (trivalent) → P-type.</li>
<li><b>Extrinsic</b> = doped semiconductor; n ≠ p.</li>
</ul>""",
          """<ul>
<li>Semiconductor: conductivity conductor અને insulator ની વચ્ચે; E<sub>g</sub> ≈ 1 eV; negative temperature coefficient.</li>
<li>Ge કરતાં Si વધુ પસંદ: મોટો E<sub>g</sub>, ઓછો leakage, વધુ તાપમાને કાર્ય, સસ્તું.</li>
<li>Si crystal માં atoms <b>Covalent bonds</b> (electron જોડીની ભાગીદારી) થી જોડાયેલા છે.</li>
<li><b>Intrinsic</b> = શુદ્ધ; ઉષ્માથી electron–hole pairs બને; <b>n = p = n<sub>i</sub></b>.</li>
<li><b>Hole</b> = bond માં electron ની ખાલી જગ્યા; positive charge તરીકે વર્તે; electrons ની વિરુદ્ધ દિશામાં ગતિ.</li>
<li><b>Doping</b> = conductivity વધારવા 10⁶–10⁸ atoms દીઠ 1 impurity atom ઉમેરવો.</li>
<li>Donor (pentavalent) → N-type; Acceptor (trivalent) → P-type.</li>
<li><b>Extrinsic</b> = doped semiconductor; n ≠ p.</li>
</ul>""", key=True),
    ],
}

# =====================================================================================
SEC_2_3 = {
    "title": {"en": "2.3 P-type and N-type Semiconductors", "gu": "2.3 P-type અને N-type Semiconductors"},
    "items": [
        T("2.3.1 N-type Semiconductor", "2.3.1 N-type Semiconductor",
          """<p>When a small amount of <b>pentavalent impurity</b> (P, As, Sb) is added to pure silicon or germanium, the resulting extrinsic semiconductor is called an <b>N-type semiconductor</b> ("N" for <b>negative</b> – the majority carriers are negative electrons).</p>
<h4>Formation</h4>
<ol>
<li>The pentavalent impurity atom (e.g. phosphorus) has <b>5 valence electrons</b>.</li>
<li>It takes the place of one Si atom in the crystal. <b>Four</b> of its valence electrons form covalent bonds with the 4 neighbouring Si atoms.</li>
<li>The <b>fifth electron</b> has no partner, so it is very loosely bound to the impurity atom. Very little energy (≈ 0.05 eV in Si, ≈ 0.01 eV in Ge) is enough to make it <b>free</b>. At room temperature, almost every impurity atom gives one free electron.</li>
<li>Since each impurity atom <b>donates</b> one free electron, it is called a <b>donor impurity</b>.</li>
<li>After giving away its electron, the impurity atom becomes a <b>positive ion (donor ion)</b>. These ions are fixed in the crystal and <b>cannot move</b>, so they do not carry current.</li>
</ol>
<h4>Charge carriers</h4>
<ul>
<li><b>Majority carriers: electrons</b> (from donor atoms + thermally generated).</li>
<li><b>Minority carriers: holes</b> (only thermally generated).</li>
</ul>
<h4>Energy band</h4>
<p>The donor atoms create a <b>donor energy level</b> just <b>below the conduction band</b>. Electrons from this level easily jump into the conduction band.</p>
<p><b>Note:</b> An N-type semiconductor is <b>electrically neutral</b> as a whole – the number of free electrons is balanced by positive donor ions and holes.</p>""",
          """<p>શુદ્ધ silicon કે germanium માં થોડી માત્રામાં <b>Pentavalent impurity</b> (P, As, Sb) ઉમેરતાં બનતા extrinsic semiconductor ને <b>N-type semiconductor</b> કહે છે ("N" એટલે <b>Negative</b> – majority carriers ઋણ electrons છે).</p>
<h4>રચના</h4>
<ol>
<li>Pentavalent impurity atom (દા.ત. phosphorus) માં <b>5 valence electrons</b> હોય છે.</li>
<li>તે crystal માં એક Si atom ની જગ્યા લે છે. તેના <b>ચાર</b> valence electrons 4 પડોશી Si atoms સાથે covalent bonds બનાવે છે.</li>
<li><b>પાંચમા electron</b> ને કોઈ જોડીદાર મળતો નથી, તેથી તે impurity atom સાથે ખૂબ ઢીલો બંધાયેલો રહે છે. ખૂબ ઓછી ઊર્જા (Si માં ≈ 0.05 eV, Ge માં ≈ 0.01 eV) તેને <b>Free</b> કરવા પૂરતી છે. Room temperature પર લગભગ દરેક impurity atom એક free electron આપે છે.</li>
<li>દરેક impurity atom એક free electron <b>આપતો (Donate)</b> હોવાથી તેને <b>Donor impurity</b> કહે છે.</li>
<li>Electron આપ્યા પછી impurity atom <b>Positive ion (Donor ion)</b> બને છે. આ ions crystal માં સ્થિર હોય છે અને <b>ગતિ કરી શકતા નથી</b>, તેથી current વહન કરતા નથી.</li>
</ol>
<h4>Charge carriers</h4>
<ul>
<li><b>Majority carriers: Electrons</b> (donor atoms માંથી + thermally generated).</li>
<li><b>Minority carriers: Holes</b> (માત્ર thermally generated).</li>
</ul>
<h4>Energy band</h4>
<p>Donor atoms <b>Conduction band ની તરત નીચે</b> એક <b>Donor energy level</b> બનાવે છે. આ level ના electrons સરળતાથી conduction band માં કૂદી જાય છે.</p>
<p><b>નોંધ:</b> N-type semiconductor સમગ્ર રીતે <b>વિદ્યુતીય રીતે Neutral</b> છે – free electrons ની સંખ્યા positive donor ions અને holes થી સંતુલિત રહે છે.</p>""",
          diagram="u2_ntype"),

        T("2.3.2 P-type Semiconductor", "2.3.2 P-type Semiconductor",
          """<p>When a small amount of <b>trivalent impurity</b> (B, Al, Ga, In) is added to pure silicon or germanium, the resulting extrinsic semiconductor is called a <b>P-type semiconductor</b> ("P" for <b>positive</b> – the majority carriers are positive holes).</p>
<h4>Formation</h4>
<ol>
<li>The trivalent impurity atom (e.g. boron) has only <b>3 valence electrons</b>.</li>
<li>It takes the place of one Si atom. Its 3 electrons form covalent bonds with 3 neighbouring Si atoms.</li>
<li>The <b>fourth bond is incomplete</b> – one electron is missing. This vacancy is a <b>hole</b>.</li>
<li>This hole can easily <b>accept</b> an electron from a neighbouring bond, so the impurity is called an <b>acceptor impurity</b>.</li>
<li>When the impurity atom accepts an electron, it becomes a <b>negative ion (acceptor ion)</b>, which is fixed and <b>cannot move</b>. The hole moves to the neighbouring bond.</li>
</ol>
<h4>Charge carriers</h4>
<ul>
<li><b>Majority carriers: holes</b> (from acceptor atoms + thermally generated).</li>
<li><b>Minority carriers: electrons</b> (only thermally generated).</li>
</ul>
<h4>Energy band</h4>
<p>The acceptor atoms create an <b>acceptor energy level</b> just <b>above the valence band</b>. Electrons from the valence band easily jump into this level, leaving holes in the valence band.</p>
<p><b>Note:</b> A P-type semiconductor is also <b>electrically neutral</b> as a whole.</p>""",
          """<p>શુદ્ધ silicon કે germanium માં થોડી માત્રામાં <b>Trivalent impurity</b> (B, Al, Ga, In) ઉમેરતાં બનતા extrinsic semiconductor ને <b>P-type semiconductor</b> કહે છે ("P" એટલે <b>Positive</b> – majority carriers ધન holes છે).</p>
<h4>રચના</h4>
<ol>
<li>Trivalent impurity atom (દા.ત. boron) માં માત્ર <b>3 valence electrons</b> હોય છે.</li>
<li>તે એક Si atom ની જગ્યા લે છે. તેના 3 electrons 3 પડોશી Si atoms સાથે covalent bonds બનાવે છે.</li>
<li><b>ચોથો bond અધૂરો</b> રહે છે – એક electron ખૂટે છે. આ ખાલી જગ્યા <b>Hole</b> છે.</li>
<li>આ hole પડોશી bond માંથી સરળતાથી electron <b>સ્વીકારી (Accept)</b> શકે છે, તેથી આ impurity ને <b>Acceptor impurity</b> કહે છે.</li>
<li>Impurity atom electron સ્વીકારે ત્યારે તે <b>Negative ion (Acceptor ion)</b> બને છે, જે સ્થિર છે અને <b>ગતિ કરી શકતો નથી</b>. Hole પડોશી bond માં ખસી જાય છે.</li>
</ol>
<h4>Charge carriers</h4>
<ul>
<li><b>Majority carriers: Holes</b> (acceptor atoms માંથી + thermally generated).</li>
<li><b>Minority carriers: Electrons</b> (માત્ર thermally generated).</li>
</ul>
<h4>Energy band</h4>
<p>Acceptor atoms <b>Valence band ની તરત ઉપર</b> એક <b>Acceptor energy level</b> બનાવે છે. Valence band ના electrons સરળતાથી આ level માં જાય છે અને valence band માં holes છોડે છે.</p>
<p><b>નોંધ:</b> P-type semiconductor પણ સમગ્ર રીતે <b>વિદ્યુતીય રીતે Neutral</b> છે.</p>""",
          diagram="u2_ptype"),

        T("2.3.3 Majority and Minority Charge Carriers", "2.3.3 Majority અને Minority Charge Carriers",
          """<p>In an extrinsic semiconductor, both electrons and holes are present, but in <b>unequal numbers</b>.</p>
<ul>
<li><b>Majority carriers:</b> The charge carriers that are present in <b>larger number</b>. They are produced mainly by <b>doping</b>.</li>
<li><b>Minority carriers:</b> The charge carriers that are present in <b>smaller number</b>. They are produced only by <b>thermal generation</b> (breaking of covalent bonds by heat).</li>
</ul>
<table>
<tr><th>Semiconductor</th><th>Majority carriers</th><th>Minority carriers</th><th>Immobile ions</th></tr>
<tr><td>N-type</td><td>Electrons</td><td>Holes</td><td>Positive donor ions</td></tr>
<tr><td>P-type</td><td>Holes</td><td>Electrons</td><td>Negative acceptor ions</td></tr>
</table>
<h4>Mass action law</h4>
<p>In a semiconductor at a fixed temperature, the product of electron and hole concentrations is constant:</p>
<p class='eq'>n × p = n<sub>i</sub>²</p>
<p>So when doping increases the majority carriers, the minority carriers <b>decrease</b> (due to more recombination).</p>
<h4>Effect of temperature</h4>
<ul>
<li>Majority carrier concentration depends mainly on <b>doping</b> (almost constant with temperature).</li>
<li>Minority carrier concentration depends on <b>temperature</b> – it increases as temperature rises. This is why <b>leakage current</b> (due to minority carriers) in diodes and transistors increases with temperature.</li>
</ul>""",
          """<p>Extrinsic semiconductor માં electrons અને holes બંને હોય છે, પરંતુ <b>અસમાન સંખ્યામાં</b>.</p>
<ul>
<li><b>Majority carriers:</b> જે charge carriers <b>વધુ સંખ્યામાં</b> હોય. તે મુખ્યત્વે <b>Doping</b> થી ઉત્પન્ન થાય છે.</li>
<li><b>Minority carriers:</b> જે charge carriers <b>ઓછી સંખ્યામાં</b> હોય. તે માત્ર <b>Thermal generation</b> (ઉષ્માથી covalent bonds તૂટવા) થી ઉત્પન્ન થાય છે.</li>
</ul>
<table>
<tr><th>Semiconductor</th><th>Majority carriers</th><th>Minority carriers</th><th>સ્થિર ions</th></tr>
<tr><td>N-type</td><td>Electrons</td><td>Holes</td><td>Positive donor ions</td></tr>
<tr><td>P-type</td><td>Holes</td><td>Electrons</td><td>Negative acceptor ions</td></tr>
</table>
<h4>Mass action law</h4>
<p>નિશ્ચિત તાપમાને semiconductor માં electron અને hole concentration નો ગુણાકાર અચળ રહે છે:</p>
<p class='eq'>n × p = n<sub>i</sub>²</p>
<p>તેથી doping થી majority carriers વધે ત્યારે minority carriers <b>ઘટે</b> છે (વધુ recombination ને કારણે).</p>
<h4>તાપમાનની અસર</h4>
<ul>
<li>Majority carrier concentration મુખ્યત્વે <b>Doping</b> પર આધાર રાખે છે (તાપમાન સાથે લગભગ અચળ).</li>
<li>Minority carrier concentration <b>તાપમાન</b> પર આધાર રાખે છે – તાપમાન વધે તેમ વધે છે. તેથી diodes અને transistors માં (minority carriers ને કારણે થતો) <b>Leakage current</b> તાપમાન સાથે વધે છે.</li>
</ul>""",
          examples=["u2n2"]),

        T("2.3.4 Conductivity of Semiconductors", "2.3.4 Semiconductors ની Conductivity",
          """<p><b>Conductivity (σ)</b> is the ability of a material to conduct electric current. It is the reciprocal of resistivity: <b>σ = 1 / ρ</b>. Unit: <b>siemens per metre (S/m)</b> or (Ω·m)⁻¹.</p>
<p>In a semiconductor, current is carried by both electrons and holes, so:</p>
<p class='eq'>σ = q (n μ<sub>n</sub> + p μ<sub>p</sub>)</p>
<ul>
<li>q = charge of electron = 1.6 × 10⁻¹⁹ C</li>
<li>n, p = concentration of electrons and holes</li>
<li>μ<sub>n</sub>, μ<sub>p</sub> = <b>mobility</b> of electrons and holes (how easily they move in an electric field). Electrons are more mobile than holes: for Si, μ<sub>n</sub> ≈ 1350 and μ<sub>p</sub> ≈ 480 cm²/V·s.</li>
</ul>
<h4>Special cases</h4>
<ul>
<li><b>Intrinsic:</b> n = p = n<sub>i</sub> → <b>σ<sub>i</sub> = q n<sub>i</sub> (μ<sub>n</sub> + μ<sub>p</sub>)</b></li>
<li><b>N-type:</b> n ≫ p → <b>σ ≈ q n μ<sub>n</sub></b> (n ≈ N<sub>D</sub>, donor concentration)</li>
<li><b>P-type:</b> p ≫ n → <b>σ ≈ q p μ<sub>p</sub></b> (p ≈ N<sub>A</sub>, acceptor concentration)</li>
</ul>
<h4>Factors affecting conductivity</h4>
<ol>
<li><b>Doping level:</b> More doping → more carriers → higher conductivity.</li>
<li><b>Temperature:</b> Higher temperature → more electron–hole pairs → higher conductivity (resistance decreases).</li>
<li><b>Light:</b> Light energy breaks covalent bonds → more carriers → higher conductivity.</li>
<li><b>Type of carrier:</b> For the same doping, N-type has higher conductivity than P-type because electrons have higher mobility than holes.</li>
</ol>""",
          """<p><b>Conductivity (σ)</b> એ પદાર્થની electric current વહન કરવાની ક્ષમતા છે. તે resistivity નો વ્યસ્ત છે: <b>σ = 1 / ρ</b>. એકમ: <b>siemens per metre (S/m)</b> અથવા (Ω·m)⁻¹.</p>
<p>Semiconductor માં current electrons અને holes બંને દ્વારા વહે છે, તેથી:</p>
<p class='eq'>σ = q (n μ<sub>n</sub> + p μ<sub>p</sub>)</p>
<ul>
<li>q = electron નો charge = 1.6 × 10⁻¹⁹ C</li>
<li>n, p = electrons અને holes નું concentration</li>
<li>μ<sub>n</sub>, μ<sub>p</sub> = electrons અને holes ની <b>Mobility</b> (electric field માં તે કેટલી સરળતાથી ગતિ કરે છે). Electrons ની mobility holes કરતાં વધુ છે: Si માટે μ<sub>n</sub> ≈ 1350 અને μ<sub>p</sub> ≈ 480 cm²/V·s.</li>
</ul>
<h4>ખાસ કિસ્સાઓ</h4>
<ul>
<li><b>Intrinsic:</b> n = p = n<sub>i</sub> → <b>σ<sub>i</sub> = q n<sub>i</sub> (μ<sub>n</sub> + μ<sub>p</sub>)</b></li>
<li><b>N-type:</b> n ≫ p → <b>σ ≈ q n μ<sub>n</sub></b> (n ≈ N<sub>D</sub>, donor concentration)</li>
<li><b>P-type:</b> p ≫ n → <b>σ ≈ q p μ<sub>p</sub></b> (p ≈ N<sub>A</sub>, acceptor concentration)</li>
</ul>
<h4>Conductivity ને અસર કરતા પરિબળો</h4>
<ol>
<li><b>Doping level:</b> વધુ doping → વધુ carriers → વધુ conductivity.</li>
<li><b>Temperature:</b> વધુ તાપમાન → વધુ electron–hole pairs → વધુ conductivity (resistance ઘટે).</li>
<li><b>Light:</b> પ્રકાશ ઊર્જા covalent bonds તોડે → વધુ carriers → વધુ conductivity.</li>
<li><b>Carrier નો પ્રકાર:</b> સમાન doping માટે N-type ની conductivity P-type કરતાં વધુ હોય છે, કારણ કે electrons ની mobility holes કરતાં વધુ છે.</li>
</ol>""",
          examples=["u2n1", "u2n4"]),

        T("2.3.5 Comparison of N-type and P-type Semiconductors", "2.3.5 N-type અને P-type Semiconductors ની સરખામણી",
          """<table>
<tr><th>Point</th><th>N-type</th><th>P-type</th></tr>
<tr><td>Impurity added</td><td>Pentavalent (5 valence e⁻)</td><td>Trivalent (3 valence e⁻)</td></tr>
<tr><td>Examples of impurity</td><td>P, As, Sb, Bi</td><td>B, Al, Ga, In</td></tr>
<tr><td>Name of impurity</td><td>Donor</td><td>Acceptor</td></tr>
<tr><td>Majority carriers</td><td>Electrons</td><td>Holes</td></tr>
<tr><td>Minority carriers</td><td>Holes</td><td>Electrons</td></tr>
<tr><td>Immobile ions</td><td>Positive donor ions</td><td>Negative acceptor ions</td></tr>
<tr><td>Extra energy level</td><td>Donor level just below conduction band</td><td>Acceptor level just above valence band</td></tr>
<tr><td>Carrier concentration</td><td>n ≫ p</td><td>p ≫ n</td></tr>
<tr><td>Conductivity</td><td>σ ≈ q n μ<sub>n</sub> (higher, as μ<sub>n</sub> &gt; μ<sub>p</sub>)</td><td>σ ≈ q p μ<sub>p</sub></td></tr>
<tr><td>Overall charge</td><td>Electrically neutral</td><td>Electrically neutral</td></tr>
</table>
<p><b>Remember:</b> When a P-type and an N-type region are joined together in one crystal, a <b>P-N junction</b> is formed. This is the basic building block of <b>diodes</b> (Unit 3) and <b>transistors</b> (Unit 4).</p>""",
          """<table>
<tr><th>મુદ્દો</th><th>N-type</th><th>P-type</th></tr>
<tr><td>ઉમેરાતી impurity</td><td>Pentavalent (5 valence e⁻)</td><td>Trivalent (3 valence e⁻)</td></tr>
<tr><td>Impurity ના ઉદાહરણ</td><td>P, As, Sb, Bi</td><td>B, Al, Ga, In</td></tr>
<tr><td>Impurity નું નામ</td><td>Donor</td><td>Acceptor</td></tr>
<tr><td>Majority carriers</td><td>Electrons</td><td>Holes</td></tr>
<tr><td>Minority carriers</td><td>Holes</td><td>Electrons</td></tr>
<tr><td>સ્થિર ions</td><td>Positive donor ions</td><td>Negative acceptor ions</td></tr>
<tr><td>વધારાનું energy level</td><td>Conduction band ની તરત નીચે donor level</td><td>Valence band ની તરત ઉપર acceptor level</td></tr>
<tr><td>Carrier concentration</td><td>n ≫ p</td><td>p ≫ n</td></tr>
<tr><td>Conductivity</td><td>σ ≈ q n μ<sub>n</sub> (વધુ, કારણ μ<sub>n</sub> &gt; μ<sub>p</sub>)</td><td>σ ≈ q p μ<sub>p</sub></td></tr>
<tr><td>કુલ charge</td><td>વિદ્યુતીય રીતે Neutral</td><td>વિદ્યુતીય રીતે Neutral</td></tr>
</table>
<p><b>યાદ રાખો:</b> એક જ crystal માં P-type અને N-type વિભાગ જોડાય ત્યારે <b>P-N junction</b> બને છે. તે <b>Diodes</b> (Unit 3) અને <b>Transistors</b> (Unit 4) નો મૂળભૂત ભાગ છે.</p>"""),

        T("Key Points – 2.3", "મુખ્ય મુદ્દા – 2.3",
          """<ul>
<li><b>N-type</b> = Si/Ge + pentavalent (donor) impurity → majority electrons, minority holes, positive donor ions.</li>
<li><b>P-type</b> = Si/Ge + trivalent (acceptor) impurity → majority holes, minority electrons, negative acceptor ions.</li>
<li>Majority carriers come from <b>doping</b>; minority carriers come from <b>heat</b> (thermal generation).</li>
<li>Mass action law: <b>n × p = n<sub>i</sub>²</b>.</li>
<li>Conductivity: <b>σ = q (n μ<sub>n</sub> + p μ<sub>p</sub>)</b>; increases with doping, temperature and light.</li>
<li>μ<sub>n</sub> &gt; μ<sub>p</sub> → N-type conducts better than P-type for equal doping.</li>
<li>Both N-type and P-type are electrically <b>neutral</b>.</li>
<li>P-type + N-type joined → <b>P-N junction</b> (basis of diode and transistor).</li>
</ul>""",
          """<ul>
<li><b>N-type</b> = Si/Ge + pentavalent (donor) impurity → majority electrons, minority holes, positive donor ions.</li>
<li><b>P-type</b> = Si/Ge + trivalent (acceptor) impurity → majority holes, minority electrons, negative acceptor ions.</li>
<li>Majority carriers <b>Doping</b> માંથી; minority carriers <b>ઉષ્મા</b> (thermal generation) માંથી આવે છે.</li>
<li>Mass action law: <b>n × p = n<sub>i</sub>²</b>.</li>
<li>Conductivity: <b>σ = q (n μ<sub>n</sub> + p μ<sub>p</sub>)</b>; doping, તાપમાન અને પ્રકાશ સાથે વધે.</li>
<li>μ<sub>n</sub> &gt; μ<sub>p</sub> → સમાન doping માટે N-type, P-type કરતાં વધુ સારું conduction કરે.</li>
<li>N-type અને P-type બંને વિદ્યુતીય રીતે <b>Neutral</b> છે.</li>
<li>P-type + N-type જોડાય → <b>P-N junction</b> (diode અને transistor નો આધાર).</li>
</ul>""", key=True),
    ],
}

NOTES = [SEC_2_1, SEC_2_2, SEC_2_3]
