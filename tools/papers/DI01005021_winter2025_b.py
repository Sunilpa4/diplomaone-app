"""DI01005021 Winter 2025 — Q3 and Q4 answer parts."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from paperkit import frac, work, steps, result, table, bullets, numbered, h4, p, eq, figure
import matfigs as fig
import matfigs2 as fig2


def join(*chunks):
    return "\n".join(c for c in chunks if c)


# ---------------------------------------------------------------- Q3
Q3 = {
    'title_en': 'Q3 · Ferrous metals, solid state, crystal lattices, cast iron and electrical properties',
    'title_gu': 'પ્ર.3 · ફેરસ ધાતુ, ઘન અવસ્થા, ક્રિસ્ટલ જાળી, કાસ્ટ આયર્ન અને વિદ્યુત ગુણધર્મો',
    'cards': [],
}

Q3['cards'].append(dict(
    number='Q.3 (a)', marks=3, q='Define ferrous and nonferrous metal.',
    en=join(
        p('<b>Ferrous metals</b> are those whose main constituent is <b>iron</b>. They are magnetic, '
          'strong and cheap, and they are the backbone of engineering — but they rust unless they are '
          'alloyed or coated. The group contains pig iron, cast iron, wrought iron and all the steels.'),
        p('<b>Non-ferrous metals</b> are metals and alloys that contain <b>no iron</b> (or only a trace). '
          'They are generally lighter, more expensive, non-magnetic, and much more resistant to '
          'corrosion; many are excellent conductors of heat and electricity.'),
        table(['Point', 'Ferrous metal', 'Non-ferrous metal'], [
            ['Base element', 'iron (Fe)', 'no iron — Cu, Al, Zn, Pb, Ni, Sn, Mg'],
            ['Examples', 'cast iron, mild steel, high-carbon steel, stainless steel, alloy steel',
             'copper, aluminium, zinc, lead, nickel, brass, bronze, duralumin'],
            ['Magnetic', 'yes', 'no (except nickel and cobalt)'],
            ['Corrosion', 'rusts readily; needs paint, oil, galvanising or alloying', 'generally far more '
             'resistant, and some form a protective oxide layer'],
            ['Strength and cost', 'high strength at low cost', 'lower strength per rupee, but a high '
             'strength-to-weight ratio for aluminium'],
            ['Typical use', 'structural steel, machine frames, shafts, rails', 'electrical conductors, '
             'roofing, bearings, aircraft parts, domestic fittings'],
        ]),
        p('<b>Example:</b> a rail is <b>ferrous</b> (steel) because it needs strength and wear resistance '
          'at low cost; an overhead power cable is <b>non-ferrous</b> (aluminium over a steel core) '
          'because it needs conductivity and low weight.'),
    ),
    gu=join(
        p('<b>Ferrous metals</b> એ એ ધાતુઓ છે જેનો મુખ્ય ઘટક <b>લોખંડ</b> છે. એ magnetic, મજબૂત અને સસ્તી હોય, '
          'અને એન્જિનિયરિંગનો આધાર છે — પણ alloy કે coating ન હોય તો કટાય. એ જૂથમાં pig iron, cast iron, '
          'wrought iron અને બધા steel આવે.'),
        p('<b>Non-ferrous metals</b> એ ધાતુ અને alloy છે જેમાં <b>લોખંડ નથી</b> (કે ફક્ત ટેસો છે). એ સામાન્ય '
          'રીતે હલકી, મોંઘી, non-magnetic, અને corrosion સામે ઘણી વધુ ટકાઉ હોય; ઘણી heat અને વીજળીની '
          'ઉત્તમ વાહક છે.'),
        table(['મુદ્દો', 'Ferrous metal', 'Non-ferrous metal'], [
            ['મૂળ ધાતુ', 'લોખંડ (Fe)', 'લોખંડ નહીં — Cu, Al, Zn, Pb, Ni, Sn, Mg'],
            ['ઉદાહરણ', 'cast iron, mild steel, high-carbon steel, stainless steel, alloy steel',
             'તાંબું, એલ્યુમિનિયમ, જસત, સીસું, નિકલ, પિત્તળ, bronze, duralumin'],
            ['Magnetic', 'હા', 'ના (નિકલ અને કોબાલ્ટ સિવાય)'],
            ['Corrosion', 'સહેલાઈથી કટાય; paint, oil, galvanising કે alloying જોઈએ', 'સામાન્ય રીતે ઘણું '
             'વધુ ટકે, અને કેટલીક રક્ષણાત્મક oxide સપાટી બનાવે'],
            ['Strength અને ખર્ચ', 'ઓછા ખર્ચે ઊંચી strength', 'રૂપિયા પ્રમાણે strength ઓછી, પણ '
             'એલ્યુમિનિયમનું strength-to-weight ratio સારું'],
            ['સામાન્ય ઉપયોગ', 'structural steel, machine frame, shaft, rail', 'electrical conductor, '
             'છત, bearing, વિમાનનો ભાગ, ઘરેલું fitting'],
        ]),
        p('<b>ઉદાહરણ:</b> રેલ <b>ferrous</b> (steel) છે કારણ કે ઓછા ખર્ચે strength અને ઘસારો ઝીલવા જોઈએ; '
          'ઉપરની power cable <b>non-ferrous</b> (steel core પર એલ્યુમિનિયમ) છે કારણ કે conductivity અને '
          'હલકું વજન જોઈએ.'),
    ),
))

Q3['cards'].append(dict(
    number='Q.3 (b)', marks=4, q='Explain general characteristics of solid state.',
    en=join(
        p('In the <b>solid state</b> the particles — atoms, ions or molecules — are held close together by '
          'strong forces, so a solid has a definite shape and a definite volume of its own. The general '
          'characteristics that follow from this are:'),
        table(['Characteristic', 'What it means', 'The reason'], [
            ['<b>Definite shape and volume</b>', 'a solid does not take the shape of its container',
             'the particles are locked in position, not free to slide'],
            ['<b>High density</b>', 'solids are far denser than their liquids and gases', 'the particles '
             'are packed close, with little empty space'],
            ['<b>Very low compressibility</b>', 'a solid cannot be squeezed to any useful extent',
             'there is almost no free space between the particles'],
            ['<b>Rigidity and mechanical strength</b>', 'a solid resists shear and carries load',
             'the strong inter-particle bonds resist deformation'],
            ['<b>Diffusion is extremely slow</b>', 'two solids pressed together hardly mix, even in years',
             'the particles vibrate about fixed positions and cannot travel'],
            ['<b>Definite melting point</b>', 'a crystalline solid melts at one sharp temperature',
             'the lattice breaks down at a single energy, unlike an amorphous solid'],
            ['<b>Ordered structure (crystalline) or disordered (amorphous)</b>', 'crystals show '
             'long-range order and cleavage planes; glass shows short-range order only',
             'the arrangement of the particles, and how the solid was cooled'],
            ['<b>Anisotropy in a crystal</b>', 'properties differ along different directions',
             'the lattice spacing and the atomic density differ with direction'],
        ]),
        figure(fig.crystal_solids(),
               'Fig. 3.1 · In a crystalline solid the particles sit on a fixed repeating lattice, which is '
               'the root of every characteristic listed.'),
        h4('Worked example — the particles really are close'),
        p('Copper has a density of 8960 kg/m<sup>3</sup> and an atomic mass of 63.5. Find the number of '
          'atoms per m<sup>3</sup> and the volume per atom, and compare it with the volume of one atom '
          '(radius 0.128 nm).'),
        work('Given: ρ = 8960 kg/m<sup>3</sup> · M = 63.5 kg/kmol · N<sub>A</sub> = 6.022 × 10<sup>26</sup> '
             'per kmol · r = 0.128 nm',
             'Atoms per m<sup>3</sup> = ' + frac('ρ · N<sub>A</sub>', 'M') + ' = '
             + frac('8960 × 6.022 × 10<sup>26</sup>', '63.5') + ' = 8.5 × 10<sup>28</sup>',
             'Volume per atom = ' + frac('1', '8.5 × 10<sup>28</sup>') + ' = 1.18 × 10<sup>−29</sup> m<sup>3</sup>',
             'Volume of one atom = ' + frac('4', '3') + ' π r<sup>3</sup> = 4.19 × (1.28 × 10<sup>−10</sup>)<sup>3</sup>'
             + ' = 8.8 × 10<sup>−30</sup> m<sup>3</sup>'),
        result('Packing fraction = ' + frac('8.8 × 10<sup>−30</sup>', '1.18 × 10<sup>−29</sup>')
               + ' = 0.75 — about 74 % of the space is filled by atoms'),
        p('Sanity check: 74 % is exactly the known packing fraction of an FCC metal, and copper is FCC — so '
          'the calculation agrees with the crystal structure, and it explains the high density and the '
          'near-incompressibility of the solid.'),
        h4('Limitation'),
        p('These characteristics describe an ideal solid. A real solid has vacancies, dislocations and '
          'grain boundaries, and it is those defects — not the perfect lattice — that decide its strength '
          'and its diffusion behaviour.'),
    ),
    gu=join(
        p('<b>ઘન અવસ્થા</b>માં કણો — પરમાણુ, ion કે અણુ — પ્રબળ બળથી નજીક બંધાયેલા હોય, એટલે ઘનને પોતાનો '
          'નિશ્ચિત આકાર અને નિશ્ચિત volume હોય. એમાંથી આવતી સામાન્ય લાક્ષણિકતાઓ:'),
        table(['લાક્ષણિકતા', 'અર્થ', 'કારણ'], [
            ['<b>નિશ્ચિત આકાર અને volume</b>', 'ઘન પાત્રનો આકાર લેતું નથી', 'કણો જગ્યાએ જડાયેલા, સરકવા '
             'મુક્ત નહીં'],
            ['<b>ઊંચી density</b>', 'ઘન પોતાના પ્રવાહી અને gas કરતાં ઘણું ઘન', 'કણો નજીક ભરેલા, થોડી જ '
             'ખાલી જગ્યા'],
            ['<b>ખૂબ ઓછી compressibility</b>', 'ઘનને દબાવી શકાય નહીં', 'કણો વચ્ચે લગભગ કોઈ મુક્ત જગ્યા '
             'નથી'],
            ['<b>Rigidity અને mechanical strength</b>', 'ઘન shear સામે ટકે અને ભાર ઉપાડે', 'કણો વચ્ચેના '
             'પ્રબળ bond deformation સામે ટકે'],
            ['<b>Diffusion ખૂબ ધીમું</b>', 'બે ઘન દબાવી રાખો તો વર્ષોમાં પણ ભળે નહીં', 'કણો નિશ્ચિત જગ્યા '
             'આસપાસ દોલન કરે, પ્રવાસ કરી શકે નહીં'],
            ['<b>નિશ્ચિત melting point</b>', 'crystalline ઘન એક જ તીખા તાપમાને ઓગળે', 'lattice એક જ energyએ '
             'તૂટે, amorphous ઘનથી વિપરીત'],
            ['<b>ગોઠવાયેલી રચના (crystalline) કે અવ્યવસ્થિત (amorphous)</b>', 'crystalમાં લાંબા અંતરની '
             'વ્યવસ્થા અને cleavage plane; કાચમાં ફક્ત નજીકની વ્યવસ્થા', 'કણોની ગોઠવણી અને ઘન કેવી રીતે '
             'ઠંડું થયું એ'],
            ['<b>Crystalમાં anisotropy</b>', 'અલગ દિશામાં ગુણધર્મ અલગ', 'lattice અંતર અને atomic density '
             'દિશા પ્રમાણે બદલાય'],
        ]),
        figure(fig.crystal_solids(),
               'Fig. 3.1 · Crystalline ઘનમાં કણો નિશ્ચિત પુનરાવર્તી lattice પર બેઠા હોય, જે ઉપરની બધી '
               'લાક્ષણિકતાઓનું મૂળ છે.'),
        h4('ઉકેલેલું ઉદાહરણ — કણો ખરેખર નજીક છે'),
        p('તાંબાની density 8960 kg/m<sup>3</sup> અને atomic mass 63.5 છે. પ્રતિ m<sup>3</sup> પરમાણુની '
          'સંખ્યા અને પ્રતિ પરમાણુ volume શોધો, અને એક પરમાણુના volume (ત્રિજ્યા 0.128 nm) સાથે સરખાવો.'),
        work('Given: ρ = 8960 kg/m<sup>3</sup> · M = 63.5 kg/kmol · N<sub>A</sub> = 6.022 × 10<sup>26</sup> '
             'પ્રતિ kmol · r = 0.128 nm',
             'પ્રતિ m<sup>3</sup> પરમાણુ = ' + frac('ρ · N<sub>A</sub>', 'M') + ' = '
             + frac('8960 × 6.022 × 10<sup>26</sup>', '63.5') + ' = 8.5 × 10<sup>28</sup>',
             'પ્રતિ પરમાણુ volume = ' + frac('1', '8.5 × 10<sup>28</sup>')
             + ' = 1.18 × 10<sup>−29</sup> m<sup>3</sup>',
             'એક પરમાણુનું volume = ' + frac('4', '3') + ' π r<sup>3</sup> = 4.19 × (1.28 × 10<sup>−10</sup>)<sup>3</sup>'
             + ' = 8.8 × 10<sup>−30</sup> m<sup>3</sup>'),
        result('Packing fraction = ' + frac('8.8 × 10<sup>−30</sup>', '1.18 × 10<sup>−29</sup>')
               + ' = 0.75 — લગભગ 74 % જગ્યા પરમાણુથી ભરેલી'),
        p('Sanity check: 74 % એ FCC ધાતુનું જાણીતું packing fraction છે, અને તાંબું FCC છે — એટલે ગણતરી '
          'crystal structure સાથે મળે, અને ઘનની ઊંચી density તથા ઓછી compressibility સમજાય.'),
        h4('મર્યાદા'),
        p('આ લાક્ષણિકતાઓ આદર્શ ઘનને વર્ણવે. ખરા ઘનમાં vacancy, dislocation અને grain boundary હોય, અને '
          'એ જ defects — સંપૂર્ણ lattice નહીં — એની strength અને diffusion વર્તન નક્કી કરે.'),
    ),
))

Q3['cards'].append(dict(
    number='Q.3 (c)', marks=7, q='Explain crystal lattices and unit cell.',
    en=join(
        h4('Definitions'),
        p('A <b>crystal lattice</b> is the regular, repeating three-dimensional arrangement of points in '
          'space at which the atoms, ions or molecules of a crystal sit. Every lattice point has the same '
          'surroundings, and the pattern repeats indefinitely. A lattice is described by its '
          '<b>lattice parameters</b>: three edge lengths a, b, c and three interaxial angles α, β, γ.'),
        p('A <b>unit cell</b> is the smallest portion of the lattice that, repeated in three directions, '
          'builds the whole crystal. It is the building block of the crystal, and the whole crystal is the '
          'unit cell repeated N times in each direction.'),
        figure(fig.unit_cells(),
               'Fig. 3.2 · Simple cubic, BCC and FCC unit cells, with the number of atoms per cell and the '
               'packing fraction.'),
        h4('Construction — the unit cell part by part'),
        table(['Element of the cell', 'Purpose'], [
            ['Three edges a, b, c', 'fix the size of the cell and the spacing of the lattice'],
            ['Three angles α, β, γ', 'fix the shape — a cubic cell has α = β = γ = 90°'],
            ['Corner (lattice) points', 'each corner atom is shared by 8 cells, so it contributes 1/8'],
            ['Face-centre points', 'each face atom is shared by 2 cells, so it contributes 1/2'],
            ['Body-centre point', 'wholly inside the cell, so it contributes 1'],
            ['The basis (atom or ion)', 'the actual atom placed at each lattice point — two lattices with '
             'the same points but different bases are different crystals'],
        ]),
        h4('Working — how the cell builds the crystal, step and reason'),
        steps(('Step 1', 'Count the atoms that belong to one cell, using the sharing rules. Reason: corner '
                         'atoms are shared by eight cells, so a simple cubic cell holds 8 × 1/8 = 1 atom, '
                         'BCC holds 2 and FCC holds 4 — the count fixes the density.'),
              ('Step 2', 'Relate the atomic radius to the cell edge. Reason: the atoms touch along a '
                         'particular direction, so a is fixed by r — for SC a = 2r, for BCC a = 4r/√3, for '
                         'FCC a = 2√2 r.'),
              ('Step 3', 'Compute the packing fraction from the count and the geometry. Reason: it tells '
                         'how efficiently the space is filled — 52 % for SC, 68 % for BCC, 74 % for FCC.'),
              ('Step 4', 'Repeat the cell along the three axes. Reason: the repetition generates the whole '
                         'lattice, so a single cell plus the symmetry describes a crystal of any size.')),
        h4('The seven crystal systems'),
        table(['System', 'Edge / angle condition', 'Example'], [
            ['Cubic', 'a = b = c, α = β = γ = 90°', 'NaCl, copper, diamond'],
            ['Tetragonal', 'a = b ≠ c, all 90°', 'white tin, TiO<sub>2</sub> (rutile)'],
            ['Orthorhombic', 'a ≠ b ≠ c, all 90°', 'sulphur, aragonite'],
            ['Hexagonal', 'a = b ≠ c, α = β = 90°, γ = 120°', 'zinc, magnesium, graphite'],
            ['Rhombohedral', 'a = b = c, α = β = γ ≠ 90°', 'calcite, bismuth'],
            ['Monoclinic', 'a ≠ b ≠ c, two angles 90°', 'gypsum, sugar'],
            ['Triclinic', 'a ≠ b ≠ c, no angle 90°', 'K<sub>2</sub>Cr<sub>2</sub>O<sub>7</sub>'],
        ]),
        h4('Worked example — the lattice constant of copper'),
        p('Copper is FCC with an atomic radius of 0.128 nm and an atomic mass of 63.5 kg/kmol. Find the '
          'lattice constant a, the number of atoms per cell, and the theoretical density.'),
        work('Given: FCC · r = 0.128 nm = 1.28 × 10<sup>−10</sup> m · M = 63.5 kg/kmol · '
             'N<sub>A</sub> = 6.022 × 10<sup>26</sup> per kmol · n = 4 atoms per FCC cell',
             'For FCC: a = 2 √2 r = 2 × 1.414 × 1.28 × 10<sup>−10</sup>',
             'a = 3.62 × 10<sup>−10</sup> m = 0.362 nm',
             'Cell volume V = a<sup>3</sup> = (3.62 × 10<sup>−10</sup>)<sup>3</sup> '
             '= 4.74 × 10<sup>−29</sup> m<sup>3</sup>',
             'ρ = ' + frac('n · M', 'N<sub>A</sub> · V') + ' = '
             + frac('4 × 63.5', '6.022 × 10<sup>26</sup> × 4.74 × 10<sup>−29</sup>')),
        result('a = 0.362 nm and ρ = 8895 kg/m<sup>3</sup>, against the handbook value of 8960 '
               'kg/m<sup>3</sup>'),
        p('Sanity check: the calculated density is within 0.8 % of the measured value, the small '
          'difference being the vacancies and the thermal expansion at room temperature — so the unit-cell '
          'model is sound.'),
        h4('Importance and limitations'),
        bullets('The unit cell predicts density, the slip systems and therefore the ductility, the '
                'diffusion path, and the X-ray diffraction pattern — which is how a lattice is measured.',
                'But a real crystal is not one perfect cell: it is a mosaic of grains, each with defects, '
                'and the properties of the metal depend on those defects more than on the ideal cell.',
                'Some materials have the same lattice but a different stacking sequence (FCC and HCP both '
                'have 74 % packing) and behave quite differently in forming, so the cell alone is not '
                'enough — the stacking matters too.'),
    ),
    gu=join(
        h4('વ્યાખ્યાઓ'),
        p('<b>Crystal lattice</b> એટલે અવકાશમાં નિયમિત, પુનરાવર્તી ત્રિ-પરિમાણીય ગોઠવણીના બિંદુઓ, જેના પર '
          'crystalના પરમાણુ, ion કે અણુ બેસે. દરેક lattice બિંદુની આસપાસ સરખું જ વાતાવરણ હોય, અને પેટર્ન '
          'અનંત સુધી પુનરાવર્તન પામે. Lattice એનાં <b>lattice parameters</b>થી વર્ણવાય: ત્રણ ધાર a, b, c '
          'અને ત્રણ કોણ α, β, γ.'),
        p('<b>Unit cell</b> એટલે latticeનો સૌથી નાનો ભાગ, જેને ત્રણ દિશામાં પુનરાવર્તિત કરતાં આખો crystal '
          'બને. એ crystalની ઈંટ છે, અને આખો crystal એ દરેક દિશામાં N વાર પુનરાવર્તિત unit cell છે.'),
        figure(fig.unit_cells(),
               'Fig. 3.2 · Simple cubic, BCC અને FCC unit cell, પ્રતિ cell પરમાણુની સંખ્યા અને packing '
               'fraction સાથે.'),
        h4('રચના — unit cell ભાગ પ્રમાણે'),
        table(['Cellનું અંગ', 'હેતુ'], [
            ['ત્રણ ધાર a, b, c', 'cellનું કદ અને latticeનું અંતર નક્કી કરે'],
            ['ત્રણ કોણ α, β, γ', 'આકાર નક્કી કરે — cubic cellમાં α = β = γ = 90°'],
            ['ખૂણાના (lattice) બિંદુ', 'દરેક ખૂણાનો પરમાણુ 8 cellમાં વહેંચાય, એટલે 1/8 આપે'],
            ['Face-centre બિંદુ', 'દરેક faceનો પરમાણુ 2 cellમાં વહેંચાય, એટલે 1/2 આપે'],
            ['Body-centre બિંદુ', 'આખો cellની અંદર, એટલે 1 આપે'],
            ['Basis (પરમાણુ કે ion)', 'દરેક lattice બિંદુ પર મુકાતો ખરો પરમાણુ — એ જ બિંદુ પણ જુદો basis '
             'હોય તો જુદો crystal'],
        ]),
        h4('કાર્ય — cell કેવી રીતે crystal બનાવે, સ્ટેપ અને કારણ'),
        steps(('Step 1', 'Sharingના નિયમથી એક cellમાં આવતા પરમાણુ ગણો. કારણ: ખૂણાના પરમાણુ આઠ cellમાં '
                         'વહેંચાય, એટલે simple cubic cellમાં 8 × 1/8 = 1, BCCમાં 2 અને FCCમાં 4 પરમાણુ — આ '
                         'ગણતરી density નક્કી કરે.'),
              ('Step 2', 'Atomic radiusને cellની ધાર સાથે જોડો. કારણ: પરમાણુ એક ચોક્કસ દિશામાં સ્પર્શે, એટલે '
                         'r થી a નક્કી થાય — SCમાં a = 2r, BCCમાં a = 4r/√3, FCCમાં a = 2√2 r.'),
              ('Step 3', 'ગણતરી અને ભૂમિતિથી packing fraction કાઢો. કારણ: જગ્યા કેટલી કાર્યક્ષમ ભરાય છે તે '
                         'દેખાય — SC 52 %, BCC 68 %, FCC 74 %.'),
              ('Step 4', 'Cellને ત્રણ અક્ષ પર પુનરાવર્તિત કરો. કારણ: એ પુનરાવર્તન આખું lattice બનાવે, એટલે એક '
                         'cell અને symmetry થી ગમે તે કદનો crystal વર્ણવાય.')),
        h4('સાત crystal system'),
        table(['System', 'ધાર / કોણની શરત', 'ઉદાહરણ'], [
            ['Cubic', 'a = b = c, α = β = γ = 90°', 'NaCl, તાંબું, diamond'],
            ['Tetragonal', 'a = b ≠ c, બધા 90°', 'સફેદ tin, TiO<sub>2</sub>'],
            ['Orthorhombic', 'a ≠ b ≠ c, બધા 90°', 'sulphur, aragonite'],
            ['Hexagonal', 'a = b ≠ c, α = β = 90°, γ = 120°', 'જસત, મેગ્નેશિયમ, graphite'],
            ['Rhombohedral', 'a = b = c, α = β = γ ≠ 90°', 'calcite, bismuth'],
            ['Monoclinic', 'a ≠ b ≠ c, બે કોણ 90°', 'gypsum, ખાંડ'],
            ['Triclinic', 'a ≠ b ≠ c, કોઈ કોણ 90° નહીં', 'K<sub>2</sub>Cr<sub>2</sub>O<sub>7</sub>'],
        ]),
        h4('ઉકેલેલું ઉદાહરણ — તાંબાનો lattice constant'),
        p('તાંબું FCC છે, atomic radius 0.128 nm અને atomic mass 63.5 kg/kmol. Lattice constant a, પ્રતિ '
          'cell પરમાણુની સંખ્યા અને સૈદ્ધાંતિક density શોધો.'),
        work('Given: FCC · r = 0.128 nm = 1.28 × 10<sup>−10</sup> m · M = 63.5 kg/kmol · '
             'N<sub>A</sub> = 6.022 × 10<sup>26</sup> પ્રતિ kmol · n = 4 પરમાણુ પ્રતિ FCC cell',
             'FCC માટે: a = 2 √2 r = 2 × 1.414 × 1.28 × 10<sup>−10</sup>',
             'a = 3.62 × 10<sup>−10</sup> m = 0.362 nm',
             'Cellનું volume V = a<sup>3</sup> = (3.62 × 10<sup>−10</sup>)<sup>3</sup> '
             '= 4.74 × 10<sup>−29</sup> m<sup>3</sup>',
             'ρ = ' + frac('n · M', 'N<sub>A</sub> · V') + ' = '
             + frac('4 × 63.5', '6.022 × 10<sup>26</sup> × 4.74 × 10<sup>−29</sup>')),
        result('a = 0.362 nm અને ρ = 8895 kg/m<sup>3</sup>, જ્યારે handbookમાં 8960 kg/m<sup>3</sup> છે'),
        p('Sanity check: ગણેલી density માપેલા મૂલ્યથી 0.8 % અંદર છે; નાનો ફરક vacancy અને રૂમ તાપમાનના '
          'thermal expansionનો છે — એટલે unit-cell model સાચું છે.'),
        h4('મહત્ત્વ અને મર્યાદાઓ'),
        bullets('Unit cell density, slip system અને એથી ductility, diffusionનો રસ્તો તથા X-ray diffractionની '
                'પેટર્ન આપે — જે રીતે lattice માપાય છે એ જ.',
                'પણ ખરો crystal એક સંપૂર્ણ cell નથી: એ ઘણા grainનો mosaic છે, દરેકમાં defect હોય, અને '
                'ધાતુના ગુણધર્મ આદર્શ cell કરતાં એ defects પર વધુ આધારિત છે.',
                'કેટલાક પદાર્થનું lattice એક જ પણ stacking જુદું હોય (FCC અને HCP બંનેમાં 74 % packing) અને '
                'formingમાં એ ઘણું જુદું વર્તે, એટલે ફક્ત cell પૂરતું નથી — stacking પણ જોવું પડે.'),
    ),
))

Q3['cards'].append(dict(
    number='Q.3 (a)', marks=3, tag='OR', q='List physical properties and application of cast iron.',
    en=join(
        p('<b>Cast iron</b> is an iron–carbon alloy with <b>2–4 % carbon</b> (and 1–3 % silicon), which is '
          'cast rather than rolled. The carbon is mostly present as graphite or as cementite, and which one '
          'it is decides the type of iron.'),
        h4('Physical properties'),
        table(['Property', 'Value / behaviour'], [
            ['Density', 'about 7200 kg/m<sup>3</sup> (graphite makes it lighter than steel)'],
            ['Melting range', '1150–1250 °C, so it is fluid and fills a mould well'],
            ['Strength', 'tensile 100–400 MPa; compressive strength 3–4 times the tensile strength'],
            ['Hardness', '150–250 HB for grey iron, up to 500 HB for white iron'],
            ['Ductility', 'almost nil — elongation below 1 %; it is brittle and cannot be forged or rolled'],
            ['Machinability', 'excellent, because the graphite flakes lubricate the chip'],
            ['Thermal conductivity', 'about 45–55 W/m·K, higher than steel'],
            ['Damping capacity', 'very high — it absorbs vibration'],
            ['Wear resistance', 'good, and white iron is used for the hardest wear surfaces'],
            ['Corrosion', 'rusts, but more slowly than steel; it forms a protective graphitic skin'],
        ]),
        h4('Applications'),
        table(['Where', 'Why cast iron'], [
            ['Machine tool beds, frames, bases', 'it damps vibration, is rigid and is cheap'],
            ['Engine blocks, cylinder liners, brake drums, flywheels', 'it casts to shape, wears well and '
             'absorbs heat and vibration'],
            ['Pipes, manhole covers, drainage fittings', 'cheap and corrosion resistant enough for soil'],
            ['Pump bodies, valve bodies, water fittings', 'casts to a complex shape and resists water'],
            ['Fireplace grates, stoves, cooking ranges', 'it will not soften at cooking temperature'],
            ['Rolls and dies for the mill, and wear plates', 'white iron gives a very hard surface'],
        ]),
        p('<b>Example:</b> the bed of a lathe is grey cast iron: it is cast to shape in one piece, it damps '
          'the vibration of the cut so the finish is good, and it is far cheaper than a steel fabrication.'),
        p('<b>One-line limitation:</b> cast iron must never be used in tension or in impact — it gives no '
          'warning and breaks suddenly.'),
    ),
    gu=join(
        p('<b>Cast iron</b> એ લોખંડ–કાર્બન alloy છે જેમાં <b>2–4 % કાર્બન</b> (અને 1–3 % silicon) હોય, અને '
          'એને roll નહીં પણ cast કરાય. કાર્બન મુખ્યત્વે graphite કે cementite સ્વરૂપે હોય, અને કયું સ્વરૂપ '
          'છે એ ironનો પ્રકાર નક્કી કરે.'),
        h4('ભૌતિક ગુણધર્મો'),
        table(['ગુણધર્મ', 'કિંમત / વર્તન'], [
            ['Density', 'લગભગ 7200 kg/m<sup>3</sup> (graphiteને કારણે steel કરતાં હલકું)'],
            ['Melting range', '1150–1250 °C, એટલે પ્રવાહી અને mould સારી રીતે ભરે'],
            ['Strength', 'tensile 100–400 MPa; compressive strength tensile કરતાં 3–4 ગણી'],
            ['Hardness', 'grey iron 150–250 HB, white iron 500 HB સુધી'],
            ['Ductility', 'લગભગ શૂન્ય — elongation 1 %થી ઓછું; ભંગુર, forge કે roll થઈ શકે નહીં'],
            ['Machinability', 'ઉત્તમ, કારણ કે graphiteની પતરી chipને lubricate કરે'],
            ['Thermal conductivity', 'લગભગ 45–55 W/m·K, steel કરતાં વધુ'],
            ['Damping capacity', 'ખૂબ ઊંચી — vibration શોષે'],
            ['Wear resistance', 'સારી, અને white iron સૌથી સખત ઘસાતી સપાટી માટે વપરાય'],
            ['Corrosion', 'કટાય, પણ steel કરતાં ધીમે; રક્ષણાત્મક graphitic સપાટી બનાવે'],
        ]),
        h4('ઉપયોગ'),
        table(['ક્યાં', 'cast iron કેમ'], [
            ['Machine toolનું bed, frame, base', 'vibration damp કરે, rigid અને સસ્તું'],
            ['Engine block, cylinder liner, brake drum, flywheel', 'આકારમાં cast થાય, ઘસારો ઝીલે અને '
             'ગરમી તથા vibration શોષે'],
            ['Pipe, manhole cover, drainage fitting', 'સસ્તું અને જમીન માટે પૂરતું corrosion-resistant'],
            ['Pump body, valve body, water fitting', 'જટિલ આકારમાં cast થાય અને પાણી ઝીલે'],
            ['ચૂલો, stove, રાંધણું range', 'રાંધવાના તાપમાને નરમ ન પડે'],
            ['Millનું roll અને die, wear plate', 'white iron ખૂબ સખત સપાટી આપે'],
        ]),
        p('<b>ઉદાહરણ:</b> લેથનું bed grey cast ironનું છે: એક જ ટુકડામાં આકારમાં cast થાય, કાપનું vibration '
          'damp કરે જેથી ફિનિશ સારું આવે, અને steel fabrication કરતાં ઘણું સસ્તું પડે.'),
        p('<b>એક લીટીની મર્યાદા:</b> cast iron tensionમાં કે impactમાં કદી વાપરવું ન જોઈએ — એ ચેતવણી '
          'વગર અચાનક તૂટે.'),
    ),
))

Q3['cards'].append(dict(
    number='Q.3 (b)', marks=4, tag='OR', q='Explain electrical properties of solids.',
    en=join(
        p('The electrical behaviour of a solid is decided by its <b>band structure</b>. The electrons of '
          'the atoms fill bands of allowed energy; a solid conducts only if an electron can move into an '
          'empty state just above it. On that basis solids are conductors, semiconductors or insulators.'),
        figure(fig2.band_gaps(),
               'Fig. 3.3 · Band structure of a conductor, a semiconductor and an insulator — the width of '
               'the forbidden gap sets the behaviour.'),
        h4('The properties'),
        table(['Property', 'Meaning', 'Values'], [
            ['<b>Resistivity and conductivity</b>', 'the resistance offered to current per unit length and '
             'area; σ = 1/ρ', 'conductor 10<sup>−8</sup> Ω·m; semiconductor 10<sup>−5</sup>–10<sup>3</sup> '
             'Ω·m; insulator 10<sup>10</sup>–10<sup>16</sup> Ω·m'],
            ['<b>Temperature coefficient of resistance</b>', 'how the resistance changes with temperature',
             'positive for a metal (resistance rises), negative for a semiconductor and for carbon'],
            ['<b>Band gap</b>', 'the energy needed to lift an electron into the conduction band',
             '0 for a metal, about 1.1 eV for Si, 5–9 eV for glass and mica'],
            ['<b>Dielectric strength and permittivity</b>', 'how well a solid stands off a voltage without '
             'breaking down, and how much charge it stores', 'glass 10–14 kV/mm; mica 20 kV/mm'],
            ['<b>Conduction by ions</b>', 'in some solids the current is carried by ions, not electrons',
             'zirconia conducts O<sup>2−</sup> above 600 °C — the oxygen sensor'],
            ['<b>Superconductivity</b>', 'below a critical temperature the resistance falls to zero',
             'niobium–titanium below 9 K, used in MRI magnets'],
            ['<b>Semiconductor and doping</b>', 'a small addition of a donor or acceptor raises the '
             'conductivity by orders of magnitude', 'phosphorus in silicon gives n-type, boron gives p-type'],
            ['<b>Photoconductivity and piezoelectricity</b>', 'light or a mechanical strain changes the '
             'electrical behaviour', 'selenium photocell, PZT sensor'],
        ]),
        h4('Working — why a metal and a semiconductor behave so differently'),
        steps(('Step 1', 'In a metal the valence band is only partly filled or overlaps the next band. '
                         'Reason: a field can give an electron a tiny energy and move it, so conduction is '
                         'easy and the resistivity is very low.'),
              ('Step 2', 'In a semiconductor the valence band is full and the gap is about 1 eV. Reason: '
                         'heat or light can lift a few electrons across, so the conductivity is small but '
                         'rises sharply with temperature — which is why the coefficient is negative.'),
              ('Step 3', 'In an insulator the full valence band is separated by more than 5 eV. Reason: no '
                         'electron can cross at ordinary temperature, so the solid is an insulator.'),
              ('Step 4', 'In a metal the lattice vibrates more as it heats, and the electrons collide with '
                         'the vibrations. Reason: the scattering shortens the mean free path, so the '
                         'resistance rises with temperature.')),
        h4('Worked example — resistivity and its temperature rise'),
        p('A copper busbar has a resistivity of 1.7 × 10<sup>−8</sup> Ω·m at 20 °C and a temperature '
          'coefficient of 0.0039 per °C. It carries 500 A and is 3 m long with a 50 mm × 10 mm section. '
          'Find the resistance, the voltage drop and the resistance at 80 °C.'),
        work('Given: ρ = 1.7 × 10<sup>−8</sup> Ω·m · L = 3 m · A = 50 × 10 = 500 mm<sup>2</sup> = '
             '5 × 10<sup>−4</sup> m<sup>2</sup> · I = 500 A · α = 0.0039 per °C · ΔT = 60 °C',
             'Resistance R = ' + frac('ρ L', 'A') + ' = '
             + frac('1.7 × 10<sup>−8</sup> × 3', '5 × 10<sup>−4</sup>') + ' = 1.02 × 10<sup>−4</sup> Ω',
             'Voltage drop V = I R = 500 × 1.02 × 10<sup>−4</sup> = 0.051 V',
             'R at 80 °C = R<sub>20</sub> (1 + α ΔT) = 1.02 × 10<sup>−4</sup> × (1 + 0.0039 × 60)',
             '= 1.02 × 10<sup>−4</sup> × 1.234'),
        result('R = 0.102 mΩ, drop = 51 mV, and R rises to 0.126 mΩ at 80 °C — a 23 % rise'),
        p('Sanity check: a 51 mV drop at 500 A is 25 W of loss in 3 m of busbar, which is small but real — '
          'and the 23 % rise with 60 °C explains why a busbar is rated at a stated ambient temperature.'),
        h4('Limitations and importance'),
        p('The band picture is a model: it does not by itself give the resistivity, which also depends on '
          'the defects, the grain boundaries and the impurities, and that is why two samples of the same '
          'metal can differ. In practice the property is what decides the choice — copper for a conductor, '
          'porcelain or epoxy for an insulator, silicon for a device and zirconia for a sensor at 700 °C.'),
    ),
    gu=join(
        p('ઘનનું electrical વર્તન એની <b>band structure</b>થી નક્કી થાય. પરમાણુના electron માન્ય energyના '
          'band ભરે છે; ઘન ત્યારે જ conduct કરે જ્યારે electron ઉપરના ખાલી stateમાં જઈ શકે. એ આધારે ઘન '
          'conductor, semiconductor કે insulator હોય.'),
        figure(fig2.band_gaps(),
               'Fig. 3.3 · Conductor, semiconductor અને insulatorની band structure — forbidden gapની પહોળાઈ જ '
               'વર્તન નક્કી કરે.'),
        h4('ગુણધર્મો'),
        table(['ગુણધર્મ', 'અર્થ', 'કિંમતો'], [
            ['<b>Resistivity અને conductivity</b>', 'એકમ લંબાઈ અને area દીઠ પ્રવાહનો પ્રતિરોધ; σ = 1/ρ',
             'conductor 10<sup>−8</sup> Ω·m; semiconductor 10<sup>−5</sup>–10<sup>3</sup> Ω·m; insulator '
             '10<sup>10</sup>–10<sup>16</sup> Ω·m'],
            ['<b>Temperature coefficient of resistance</b>', 'તાપમાન સાથે resistance કેવી રીતે બદલાય',
             'ધાતુમાં ધન (resistance વધે), semiconductor અને કાર્બનમાં ઋણ'],
            ['<b>Band gap</b>', 'electronને conduction bandમાં લઈ જવા જરૂરી energy', 'ધાતુમાં 0, Siમાં લગભગ '
             '1.1 eV, કાચ અને micaમાં 5–9 eV'],
            ['<b>Dielectric strength અને permittivity</b>', 'voltage ઝીલીને breakdown વગર ટકવાની ક્ષમતા '
             'અને charge સંઘરવાની ક્ષમતા', 'કાચ 10–14 kV/mm; mica 20 kV/mm'],
            ['<b>Ion દ્વારા conduction</b>', 'કેટલાક ઘનમાં પ્રવાહ ion લઈ જાય, electron નહીં',
             'zirconia 600 °Cથી ઉપર O<sup>2−</sup> conduct કરે — oxygen sensor'],
            ['<b>Superconductivity</b>', 'critical temperatureથી નીચે resistance શૂન્ય થાય',
             'niobium–titanium 9 Kથી નીચે, MRI magnetમાં'],
            ['<b>Semiconductor અને doping</b>', 'થોડો donor કે acceptor ઉમેરતાં conductivity ઘણા ક્રમ વધે',
             'siliconમાં phosphorus n-type, boron p-type'],
            ['<b>Photoconductivity અને piezoelectricity</b>', 'પ્રકાશ કે mechanical strain electrical વર્તન '
             'બદલે', 'selenium photocell, PZT sensor'],
        ]),
        h4('કાર્ય — ધાતુ અને semiconductor એટલા જુદા કેમ વર્તે'),
        steps(('Step 1', 'ધાતુમાં valence band અંશતઃ ભરેલો કે આગલા band સાથે overlap થાય. કારણ: field '
                         'electronને થોડી energy આપીને ખસેડી શકે, એટલે conduction સહેલું અને resistivity ખૂબ '
                         'નીચી.'),
              ('Step 2', 'Semiconductorમાં valence band પૂરો ભરેલો અને gap લગભગ 1 eV. કારણ: ગરમી કે પ્રકાશ '
                         'થોડા electron પાર કરે, એટલે conductivity નાની પણ તાપમાન સાથે તીવ્ર વધે — એટલે '
                         'coefficient ઋણ.'),
              ('Step 3', 'Insulatorમાં ભરેલો valence band 5 eVથી વધુના gapથી અલગ. કારણ: સામાન્ય તાપમાને '
                         'કોઈ electron પાર ન કરી શકે, એટલે ઘન insulator.'),
              ('Step 4', 'ધાતુ ગરમ થાય તેમ lattice વધુ દોલન કરે અને electron એ દોલન સાથે અથડાય. કારણ: '
                         'scattering mean free path ટૂંકાવે, એટલે resistance તાપમાન સાથે વધે.')),
        h4('ઉકેલેલું ઉદાહરણ — resistivity અને તાપમાન વધારો'),
        p('તાંબાના busbarની resistivity 20 °C પર 1.7 × 10<sup>−8</sup> Ω·m અને temperature coefficient '
          '0.0039 પ્રતિ °C છે. એ 500 A લે છે, લંબાઈ 3 m અને section 50 mm × 10 mm છે. Resistance, voltage '
          'drop અને 80 °C પર resistance શોધો.'),
        work('Given: ρ = 1.7 × 10<sup>−8</sup> Ω·m · L = 3 m · A = 50 × 10 = 500 mm<sup>2</sup> = '
             '5 × 10<sup>−4</sup> m<sup>2</sup> · I = 500 A · α = 0.0039 પ્રતિ °C · ΔT = 60 °C',
             'Resistance R = ' + frac('ρ L', 'A') + ' = '
             + frac('1.7 × 10<sup>−8</sup> × 3', '5 × 10<sup>−4</sup>') + ' = 1.02 × 10<sup>−4</sup> Ω',
             'Voltage drop V = I R = 500 × 1.02 × 10<sup>−4</sup> = 0.051 V',
             '80 °C પર R = R<sub>20</sub> (1 + α ΔT) = 1.02 × 10<sup>−4</sup> × (1 + 0.0039 × 60)',
             '= 1.02 × 10<sup>−4</sup> × 1.234'),
        result('R = 0.102 mΩ, drop = 51 mV, અને 80 °C પર R 0.126 mΩ થાય — 23 % વધારો'),
        p('Sanity check: 500 A પર 51 mV drop એટલે 3 m busbarમાં 25 W loss, જે નાનું પણ ખરું છે — અને '
          '60 °C પર 23 % વધારો સમજાવે છે કે busbarનું rating કોઈ આપેલા ambient temperature પર કેમ અપાય.'),
        h4('મર્યાદાઓ અને મહત્ત્વ'),
        p('Bandનું ચિત્ર એક model છે: એ એકલું resistivity આપતું નથી, જે defect, grain boundary અને impurity પર '
          'પણ આધારિત છે, એટલે એક જ ધાતુના બે નમૂના જુદા પડે. વ્યવહારમાં આ ગુણધર્મ જ પસંદગી નક્કી કરે — '
          'conductor માટે તાંબું, insulator માટે porcelain કે epoxy, device માટે silicon અને 700 °C પર '
          'sensor માટે zirconia.'),
    ),
))

Q3['cards'].append(dict(
    number='Q.3 (c)', marks=7, tag='OR', q='Explain amorphous and crystalline solids.',
    en=join(
        h4('Definitions'),
        p('A <b>crystalline solid</b> is one in which the atoms, ions or molecules are arranged in a '
          'regular, repeating three-dimensional pattern that extends over a long range. A crystal therefore '
          'has long-range order, a sharp melting point, and flat cleavage planes.'),
        p('An <b>amorphous solid</b> (or non-crystalline, glassy solid) is one in which the particles are '
          'frozen in a disordered arrangement, with order only over a few atomic distances. It has '
          'short-range order, no sharp melting point, and it breaks with a conchoidal, glassy fracture.'),
        figure(fig.solids_compare(),
               'Fig. 3.4 · Ordered lattice in a crystalline solid against the random arrangement in an '
               'amorphous solid.'),
        h4('Construction — what the structure is made of'),
        table(['Feature', 'Crystalline', 'Amorphous'], [
            ['Particle arrangement', 'a regular lattice, repeating in all three directions',
             'random, like a frozen liquid'],
            ['Range of order', 'long-range, micrometres across', 'short-range, only a few atom spacings'],
            ['Cooling from the melt', 'the atoms take their lattice positions at the freezing point',
             'the melt stiffens before it can order — the viscosity rises above 10<sup>12</sup> Pa·s'],
            ['Typical examples', 'NaCl, quartz, sugar, metals, diamond', 'glass, rubber, plastics, '
             'amorphous silica, wax'],
        ]),
        h4('Comparison — property by property'),
        table(['Property', 'Crystalline solid', 'Amorphous solid'], [
            ['Melting', 'sharp melting point — ice at 0 °C, iron at 1538 °C', 'softens gradually over a '
             'temperature range; glass has no melting point, only a softening range'],
            ['Cleavage', 'breaks along definite crystallographic planes', 'breaks with a curved, conchoidal '
             'fracture like glass'],
            ['X-ray diffraction', 'sharp, well defined spots and lines', 'broad diffuse halos'],
            ['Density and packing', 'dense and closely packed — up to 74 %', 'looser packing, so usually a '
             'little less dense than the crystalline form of the same material'],
            ['Optical behaviour', 'usually anisotropic; a crystal can be birefringent', 'isotropic — the '
             'same in all directions'],
            ['Mechanical behaviour', 'anisotropic; a crystal cleaves and slips on definite planes',
             'isotropic and brittle; glass has no slip plane, so it shatters'],
            ['Thermal behaviour', 'a definite latent heat of fusion at the melting point',
             'no sharp latent heat; the specific heat changes gradually'],
            ['On heating', 'melts at one temperature and then flows', 'softens, and a thermosetting glass '
             'or polymer may set hard before it can flow'],
            ['Stability', 'thermodynamically stable form of the solid', 'metastable — glass may slowly '
             'devitrify over years'],
        ]),
        h4('Working — why the difference exists, step and reason'),
        steps(('Step 1', 'A melt cooled slowly gives the atoms time to find their lattice positions. Reason: '
                         'diffusion is fast at a high temperature, so the ordered, low-energy crystal '
                         'forms and the solid is crystalline.'),
              ('Step 2', 'A melt cooled fast does not give that time. Reason: the viscosity rises so quickly '
                         'that the atoms are frozen where they are, and the disorder of the liquid is '
                         'retained — the solid is amorphous.'),
              ('Step 3', 'Because a crystal has a periodic lattice, all its bonds break at one energy. '
                         'Reason: that is why the melting point is sharp, and why the X-ray pattern has '
                         'sharp lines.'),
              ('Step 4', 'In a glass the bond energies vary from place to place. Reason: so it softens over '
                         'a range, and an X-ray gives a broad halo instead of lines.')),
        h4('Worked example — the density of the two forms of silica'),
        p('Crystalline quartz has a density of 2650 kg/m<sup>3</sup>. Silica glass has a density of 2200 '
          'kg/m<sup>3</sup>. Find the percentage of the volume that is free space in each, taking the true '
          'density of silica as 2650 kg/m<sup>3</sup> for quartz, and explain the difference.'),
        work('Given: ρ<sub>quartz</sub> = 2650 kg/m<sup>3</sup> · ρ<sub>glass</sub> = 2200 kg/m<sup>3</sup> '
             '· true density of silica = 2650 kg/m<sup>3</sup>',
             'Quartz: volume fraction of solid = ' + frac('2650', '2650') + ' = 1.00',
             'Silica glass: ' + frac('2200', '2650') + ' = 0.83',
             'Free space in glass = 1 − 0.83 = 0.17'),
        result('Silica glass has about 17 % more free volume than quartz, which is why it is 17 % less '
               'dense'),
        p('Sanity check: the disordered packing of glass cannot fill space as efficiently as a lattice, so a '
          'lower density is expected; 17 % is consistent with the difference in packing between a random '
          'and an ordered arrangement of the same tetrahedra.'),
        h4('Importance and limitations'),
        bullets('The difference is used, not just described: a crystal is chosen where strength, a sharp '
                'melting point or anisotropy is wanted (a turbine blade, a semiconductor wafer), and a glass '
                'where isotropy, transparency and easy forming matter (a window, a bottle, an optical '
                'fibre).',
                'Amorphous metals (metallic glasses) are a modern exception: cooled at 10<sup>6</sup> K/s, '
                'they are stronger and much more corrosion resistant than the same alloy in crystalline '
                'form.',
                'A glass is metastable: it can devitrify — crystallise slowly — and that is a real failure '
                'mode of a glass-ceramic seal at high temperature.',
                'A crystal is not perfect either: vacancies, dislocations and grain boundaries mean that '
                'the real strength is 10–100 times below the theoretical strength of a perfect lattice.'),
    ),
    gu=join(
        h4('વ્યાખ્યાઓ'),
        p('<b>Crystalline solid</b> એ એવો ઘન છે જેમાં પરમાણુ, ion કે અણુ નિયમિત, પુનરાવર્તી ત્રિ-પરિમાણીય '
          'પેટર્નમાં લાંબા અંતર સુધી ગોઠવાયેલા હોય. એટલે crystalમાં long-range order, તીખું melting point '
          'અને સપાટ cleavage plane હોય.'),
        p('<b>Amorphous solid</b> (non-crystalline, glassy) એ એવો ઘન છે જેમાં કણો અવ્યવસ્થિત ગોઠવણીમાં જડાઈ '
          'ગયા હોય, અને વ્યવસ્થા ફક્ત થોડા atomic અંતર સુધી હોય. એમાં short-range order, તીખું melting point '
          'નહીં, અને conchoidal કાચ જેવો ભંગ થાય.'),
        figure(fig.solids_compare(),
               'Fig. 3.4 · Crystalline ઘનમાં ગોઠવાયેલી જાળી સામે amorphous ઘનમાં અવ્યવસ્થિત ગોઠવણી.'),
        h4('રચના — structure શેનાથી બને'),
        table(['લક્ષણ', 'Crystalline', 'Amorphous'], [
            ['કણોની ગોઠવણી', 'નિયમિત lattice, ત્રણેય દિશામાં પુનરાવર્તી', 'અવ્યવસ્થિત, થિજેલા પ્રવાહી જેવી'],
            ['વ્યવસ્થાનો વ્યાપ', 'long-range, માઇક્રોમીટર સુધી', 'short-range, ફક્ત થોડા atom અંતર'],
            ['પીગળેલામાંથી ઠંડું કરતાં', 'freezing point પર પરમાણુ પોતાની lattice જગ્યા લે',
             'order થવા પહેલાં પીગળેલું જડાઈ જાય — viscosity 10<sup>12</sup> Pa·sથી ઉપર જાય'],
            ['સામાન્ય ઉદાહરણ', 'NaCl, quartz, ખાંડ, ધાતુ, diamond', 'કાચ, રબર, plastic, amorphous silica, wax'],
        ]),
        h4('સરખામણી — ગુણધર્મ પ્રમાણે'),
        table(['ગુણધર્મ', 'Crystalline ઘન', 'Amorphous ઘન'], [
            ['ગલન', 'તીખું melting point — બરફ 0 °C, લોખંડ 1538 °C', 'તાપમાનની રેન્જમાં ધીમે નરમ પડે; કાચનું '
             'melting point નહીં, ફક્ત softening range'],
            ['Cleavage', 'ચોક્કસ crystallographic plane પર તૂટે', 'વળેલી, conchoidal fracture — કાચ જેવું'],
            ['X-ray diffraction', 'તીખા, સ્પષ્ટ spot અને line', 'પહોળા ધૂંધળા halo'],
            ['Density અને packing', 'ઘન અને નજીક ભરેલું — 74 % સુધી', 'ઢીલું packing, એટલે એ જ પદાર્થના '
             'crystalline સ્વરૂપ કરતાં સામાન્ય રીતે ઓછી density'],
            ['Optical વર્તન', 'સામાન્ય રીતે anisotropic; crystal birefringent હોઈ શકે', 'isotropic — બધી '
             'દિશામાં સરખું'],
            ['Mechanical વર્તન', 'anisotropic; ચોક્કસ plane પર cleave અને slip થાય', 'isotropic અને ભંગુર; '
             'કાચમાં slip plane નહીં, એટલે ચકણાં થઈ જાય'],
            ['ઉષ્મીય વર્તન', 'melting point પર ચોક્કસ latent heat', 'તીખી latent heat નહીં; specific heat ધીમે '
             'બદલાય'],
            ['ગરમ કરતાં', 'એક તાપમાને ઓગળીને વહે', 'નરમ પડે, અને thermosetting કાચ કે polymer વહે તે પહેલાં '
             'સખત થઈ જાય'],
            ['સ્થિરતા', 'ઘનનું થર્મોડાયનેમિક સ્થિર સ્વરૂપ', 'metastable — કાચ વર્ષોમાં ધીમે devitrify થઈ '
             'શકે'],
        ]),
        h4('કાર્ય — ફરક કેમ છે, સ્ટેપ અને કારણ'),
        steps(('Step 1', 'ધીમે ઠંડું કરેલું પીગળેલું પરમાણુને પોતાની lattice જગ્યા શોધવા સમય આપે. કારણ: ઊંચા '
                         'તાપમાને diffusion ઝડપી, એટલે ઓછી energy વાળો ગોઠવાયેલો crystal બને અને ઘન '
                         'crystalline થાય.'),
              ('Step 2', 'ઝડપથી ઠંડું કરતાં એ સમય મળે નહીં. કારણ: viscosity એટલી ઝડપથી વધે કે પરમાણુ જ્યાં છે '
                         'ત્યાં જડાઈ જાય, અને પ્રવાહીની અવ્યવસ્થા ટકી રહે — ઘન amorphous બને.'),
              ('Step 3', 'Crystalમાં lattice સામયિક હોવાથી એના બધા bond એક જ energyએ તૂટે. કારણ: એટલે '
                         'melting point તીખું, અને X-ray પેટર્નમાં તીખી line.'),
              ('Step 4', 'કાચમાં bondની energy જગ્યાએ જગ્યાએ બદલાય. કારણ: એટલે એ રેન્જમાં નરમ પડે, અને X-ray '
                         'lineને બદલે પહોળો halo આપે.')),
        h4('ઉકેલેલું ઉદાહરણ — silicaનાં બે સ્વરૂપની density'),
        p('Crystalline quartzની density 2650 kg/m<sup>3</sup> અને silica glassની 2200 kg/m<sup>3</sup> છે. '
          'બંેમાં કેટલા ટકા volume ખાલી જગ્યા છે તે શોધો, અને ફરક સમજાવો.'),
        work('Given: ρ<sub>quartz</sub> = 2650 kg/m<sup>3</sup> · ρ<sub>glass</sub> = 2200 kg/m<sup>3</sup> '
             '· silicaની ખરી density 2650 kg/m<sup>3</sup>',
             'Quartz: ઘનનું volume fraction = ' + frac('2650', '2650') + ' = 1.00',
             'Silica glass: ' + frac('2200', '2650') + ' = 0.83',
             'કાચમાં ખાલી જગ્યા = 1 − 0.83 = 0.17'),
        result('Silica glassમાં quartz કરતાં લગભગ 17 % વધુ ખાલી volume છે, એટલે જ એ 17 % ઓછું ઘન'),
        p('Sanity check: કાચની અવ્યવસ્થિત ગોઠવણી lattice જેટલી કાર્યક્ષમ જગ્યા ભરી શકે નહીં, એટલે ઓછી '
          'density અપેક્ષિત; એ જ tetrahedraની અવ્યવસ્થિત અને ગોઠવાયેલી ગોઠવણી વચ્ચેના ફરક સાથે 17 % મળે.'),
        h4('મહત્ત્વ અને મર્યાદાઓ'),
        bullets('આ ફરક વર્ણવાય નહીં, વપરાય: જ્યાં strength, તીખું melting point કે anisotropy જોઈએ ત્યાં '
                'crystal (turbine blade, semiconductor wafer), અને જ્યાં isotropy, પારદર્શકતા તથી સહેલી '
                'forming જોઈએ ત્યાં કાચ (બારી, બોટલ, optical fibre).',
                'Amorphous metals (metallic glass) આધુનિક અપવાદ છે: 10<sup>6</sup> K/sએ ઠંડા કરતાં એ જ alloyના '
                'crystalline સ્વરૂપ કરતાં વધુ મજબૂત અને ઘણા વધુ corrosion-resistant બને.',
                'કાચ metastable છે: એ devitrify થઈ શકે — ધીમે crystallise થાય — અને ઊંચા તાપમાને glass-ceramic '
                'sealની એ ખરી નિષ્ફળતાની રીત છે.',
                'Crystal પણ સંપૂર્ણ નથી: vacancy, dislocation અને grain boundaryને કારણે ખરી strength સંપૂર્ણ '
                'ના સૈદ્ધાંતિક મૂલ્યથી 10–100 ગણી નીચે હોય.'),
    ),
))


# ---------------------------------------------------------------- Q4
Q4 = {
    'title_en': 'Q4 · Forging, material testing, visual inspection, monel, DPT and hydrostatic testing',
    'title_gu': 'પ્ર.4 · ફોજિંગ, મટીરિયલ ટેસ્ટિંગ, વિઝ્યુઅલ ઇન્સ્પેક્શન, મોનેલ, DPT અને હાઇડ્રોસ્ટેટિક ટેસ્ટ',
    'cards': [],
}

Q4['cards'].append(dict(
    number='Q.4 (a)', marks=3, q='Explain forging.',
    en=join(
        p('<b>Forging</b> is a metal forming process in which the metal is heated to a hot working '
          'temperature and shaped by <b>compressive force</b> — by hammer blows (drop forging) or by a '
          'slow squeeze (press forging). The metal flows plastically into the required shape, and the '
          'working closes the internal porosity and refines the grain.'),
        figure(fig.rolling_forging(),
               'Fig. 4.1 · Rolling is continuous and gives a long product; forging is discrete and shapes '
               'one part at a time.'),
        h4('Types'),
        table(['Type', 'How it works', 'Use'], [
            ['<b>Open-die (smith) forging</b>', 'the hot billet is hammered between flat dies, and the '
             'operator turns it', "a large shaft, a ship's anchor, a one-off part"],
            ['<b>Impression (closed-die) forging</b>', 'the dies carry the shape, and the metal fills the '
             'impression', 'connecting rods, crankshafts, gear blanks, spanners'],
            ['<b>Drop forging</b>', 'a heavy hammer falls on the die; a rapid blow', 'high production of a '
             'medium part'],
            ['<b>Press forging</b>', 'a slow squeeze; the deformation reaches the centre of the part',
             'a large part needing sound internal structure'],
            ['<b>Upset forging</b>', 'the bar end is heated and the length is shortened to swell the '
             'diameter', 'bolt heads, rivets, valve heads'],
            ['<b>Roll forging</b>', 'the bar passes between grooved rolls', 'a tapered lever or a '
             'spanner shank'],
        ]),
        h4('Properties it gives, and the reason'),
        bullets('<b>Strength</b> is higher than in a casting of the same steel, <b>because</b> the working '
                'closes the shrinkage porosity and welds the internal voids.',
                '<b>Toughness and fatigue life</b> are better, <b>because</b> the grain is refined and the '
                'fibre flow follows the shape of the part, so the grain does not run across a corner.',
                '<b>Weight saving</b>, <b>because</b> a forged part can be made with the metal exactly '
                'where the load is, and a casting needs a thicker section to be sound.',
                '<b>But</b> it needs expensive dies and a large press, and it is economical only in '
                'quantity; a thin section or a very intricate shape is better cast.'),
        h4('Worked example — forging force'),
        p('A billet of 0.02 m<sup>2</sup> cross section is forged at 1100 °C where the flow stress is '
          '120 MPa. Find the force needed for an open-die squeeze (neglecting friction), and the press '
          'capacity for a factor of 1.5.'),
        work('Given: A = 0.02 m<sup>2</sup> · σ<sub>f</sub> = 120 MPa = 120 × 10<sup>6</sup> N/m<sup>2</sup> '
             '· FOS = 1.5',
             'Force F = σ<sub>f</sub> · A = 120 × 10<sup>6</sup> × 0.02',
             'F = 2.4 × 10<sup>6</sup> N = 2.4 MN',
             'Press capacity = 1.5 × 2.4 = 3.6 MN'),
        result('Forging force 2.4 MN, so a press of at least 3.6 MN (about 360 tonne) is needed'),
        p('Sanity check: 360 tonne is a typical forging press size for a part of this section, so the '
          'answer is realistic. Forging with a fuller die would need 1.15–1.5 times more because of '
          'friction and the constraint of the die shape.'),
        h4('Limitation'),
        p('Forging gives only a rough shape: a machining allowance must be left, and a thin web or a sharp '
          'rib cannot be forged at all. A forging is also anisotropic — strongest along the fibre flow — '
          'so the designer must know the grain direction.'),
    ),
    gu=join(
        p('<b>Forging</b> એ metal forming પ્રક્રિયા છે જેમાં ધાતુને ગરમ કરીને <b>compressive force</b>થી આકાર '
          'અપાય — હથોડાના ઘા (drop forging) કે ધીમા દબાણ (press forging) થી. ધાતુ plastic રીતે વહીને જરૂરી '
          'આકાર લે, અને કામ કરવાથી અંદરની porosity બંધ થાય તથા grain બારીક બને.'),
        figure(fig.rolling_forging(),
               'Fig. 4.1 · Rolling સતત છે અને લાંબું ઉત્પાદન આપે; forging એક-એક ભાગને આકાર આપે છે.'),
        h4('પ્રકારો'),
        table(['પ્રકાર', 'કેવી રીતે કામ કરે', 'ઉપયોગ'], [
            ['<b>Open-die (smith) forging</b>', 'ગરમ billet સપાટ die વચ્ચે હથોડાથી ઠોકાય, ને operator એને '
             'ફેરવે', 'મોટો shaft, જહાજનું anchor, એક જ ભાગ'],
            ['<b>Impression (closed-die) forging</b>', 'dieમાં આકાર કોતરેલો હોય, ધાતુ એ impression ભરે',
             'connecting rod, crankshaft, gear blank, પાનું'],
            ['<b>Drop forging</b>', 'ભારે હથોડો die પર પડે; ઝડપી ઘા', 'મધ્યમ ભાગનું વધુ ઉત્પાદન'],
            ['<b>Press forging</b>', 'ધીમું દબાણ; deformation ભાગના મધ્ય સુધી પહોંચે', 'અંદરથી ઘન '
             'રચના જોઈએ એવો મોટો ભાગ'],
            ['<b>Upset forging</b>', 'દંડનો છેડો ગરમ કરીને લંબાઈ ઘટાડીને વ્યાસ ફુલાવાય', 'બોલ્ટનું માથું, '
             'rivet, valve head'],
            ['<b>Roll forging</b>', 'દંડ grooved roll વચ્ચે પસાર થાય', 'ટેપર લિવર કે પાનાનું દાંડું'],
        ]),
        h4('કયા ગુણધર્મ આપે, અને કારણ'),
        bullets('એ જ steelના casting કરતાં <b>strength વધુ</b>, <b>કારણ</b> કે કામ કરવાથી shrinkage porosity '
                'બંધ થાય અને અંદરના void weld થાય.',
                '<b>Toughness અને fatigue life સારી</b>, <b>કારણ</b> કે grain બારીક બને અને fibre flow ભાગના '
                'આકાર સાથે ચાલે, એટલે ખૂણે grain આડું ન જાય.',
                '<b>વજનમાં બચત</b>, <b>કારણ</b> કે forged ભાગમાં ધાતુ બરાબર જ્યાં ભાર છે ત્યાં રાખી શકાય, '
                'જ્યારે castingને ઘન રહેવા જાડો section જોઈએ.',
                '<b>પણ</b> મોંઘા die અને મોટું press જોઈએ, અને એ ફક્ત મોટા જથ્થામાં આર્થિક; પાતળો section કે '
                'બહુ જટિલ આકાર cast કરવો સારો.'),
        h4('ઉકેલેલું ઉદાહરણ — forging force'),
        p('0.02 m<sup>2</sup> cross section વાળું billet 1100 °C પર forge થાય છે જ્યાં flow stress 120 MPa છે. '
          'Open-die squeeze માટે જરૂરી force (friction ગણ્યા વગર) અને factor 1.5 સાથે pressની ક્ષમતા શોધો.'),
        work('Given: A = 0.02 m<sup>2</sup> · σ<sub>f</sub> = 120 MPa = 120 × 10<sup>6</sup> N/m<sup>2</sup> '
             '· FOS = 1.5',
             'Force F = σ<sub>f</sub> · A = 120 × 10<sup>6</sup> × 0.02',
             'F = 2.4 × 10<sup>6</sup> N = 2.4 MN',
             'Pressની ક્ષમતા = 1.5 × 2.4 = 3.6 MN'),
        result('Forging force 2.4 MN, એટલે ઓછામાં ઓછું 3.6 MN (લગભગ 360 ટન) press જોઈએ'),
        p('Sanity check: આ sectionના ભાગ માટે 360 ટન સામાન્ય forging pressનું માપ છે, એટલે જવાબ વાસ્તવિક '
          'છે. Fuller die સાથે friction અને dieના constraintને કારણે 1.15–1.5 ગણું વધુ જોઈએ.'),
        h4('મર્યાદા'),
        p('Forging ફક્ત ઢબૂલ આકાર આપે: machining allowance રાખવો પડે, અને પાતળી web કે તીવ્ર rib forge થઈ '
          'શકે જ નહીં. Forging anisotropic પણ હોય — fibre flowની દિશામાં સૌથી મજબૂત — એટલે designerને grainની '
          'દિશા ખબર હોવી જોઈએ.'),
    ),
))

Q4['cards'].append(dict(
    number='Q.4 (b)', marks=4, q='Describe importance of material testing.',
    en=join(
        p('<b>Material testing</b> is the measurement of the properties of a material — its strength, '
          'ductility, hardness, toughness, and its freedom from defects — so that the design can be based '
          'on measured numbers rather than on guesswork.'),
        figure(fig.testing_tree(),
               'Fig. 4.2 · The two families of tests: destructive tests spoil the sample, non-destructive '
               'tests keep the part fit for service.'),
        h4('Why it matters'),
        table(['Reason', 'What testing gives', 'Consequence if it is skipped'], [
            ['<b>Safe design</b>', 'yield strength, ultimate strength and elongation, for the design stress '
             'and the factor of safety', 'a vessel or a structure sized on assumed numbers can fail'],
            ['<b>Correct selection</b>', 'a comparison of candidate materials on measured properties',
             'the wrong grade is chosen and the part wears or corrodes early'],
            ['<b>Quality control of the product</b>', 'a check that the delivered material matches the '
             'specification (a mill test certificate is verified by a sample test)', 'a substandard heat '
             'of steel enters the plant'],
            ['<b>Control of the process</b>', 'hardness after heat treatment, strength after welding, '
             'density after casting', 'the heat treatment or the weld is wrong and nobody knows'],
            ['<b>Failure investigation</b>', 'the mechanism — fatigue, creep, brittle fracture, corrosion',
             'the same failure repeats'],
            ['<b>Legal and code requirement</b>', 'a test certificate for a pressure part, a lifting '
             'tackle or a boiler', 'the plant cannot be insured or commissioned'],
            ['<b>Development of new materials</b>', 'property data for a new alloy or a new composite',
             'a new material cannot be used with confidence'],
            ['<b>Economy</b>', 'the cheapest material that meets the measured requirement', 'an '
             'over-designed, over-cost part'],
        ]),
        h4('Working — how a test is used, step and reason'),
        steps(('Step 1', 'Take a sample from the lot, in the direction and from the place the code '
                         'specifies. Reason: the properties vary through a forging and across a weld, so a '
                         'sample from the wrong place tells nothing about the part.'),
              ('Step 2', 'Prepare the specimen to the standard size and finish. Reason: a rough or an '
                         'oversize specimen gives a different result, and the standard size is what makes '
                         'results comparable.'),
              ('Step 3', 'Run the test at the specified rate and temperature. Reason: a metal is stronger '
                         'at a high strain rate and weaker when hot, so the test condition must match the '
                         'service condition.'),
              ('Step 4', 'Compare the result with the specification and record it. Reason: the number is '
                         'only useful against the acceptance limit; a test without a limit proves nothing.')),
        h4('Worked example — reading a tensile test'),
        p('A 12.5 mm diameter specimen of steel with a 50 mm gauge length is pulled to failure at 78 kN. It '
          'yields at 45 kN and the gauge length at failure is 62 mm. Find the yield strength, the ultimate '
          'strength and the percentage elongation, and comment.'),
        work('Given: d = 12.5 mm = 0.0125 m · L<sub>0</sub> = 50 mm · F<sub>y</sub> = 45 kN · '
             'F<sub>max</sub> = 78 kN · L<sub>f</sub> = 62 mm',
             'Area A = ' + frac('π d<sup>2</sup>', '4') + ' = ' + frac('3.14 × 0.0125<sup>2</sup>', '4')
             + ' = 1.227 × 10<sup>−4</sup> m<sup>2</sup>',
             'Yield strength = ' + frac('45 × 10<sup>3</sup>', '1.227 × 10<sup>−4</sup>') + ' = 367 MPa',
             'Ultimate strength = ' + frac('78 × 10<sup>3</sup>', '1.227 × 10<sup>−4</sup>') + ' = 636 MPa',
             'Elongation = ' + frac('62 − 50', '50') + ' × 100 = 24 %'),
        result('σ<sub>y</sub> = 367 MPa, σ<sub>u</sub> = 636 MPa, elongation 24 % — a ductile, medium-carbon '
               'steel'),
        p('Sanity check: a 24 % elongation and a σ<sub>u</sub>/σ<sub>y</sub> ratio of 1.7 are typical of a '
          'ductile structural steel, and the part would "neck" before breaking — so the material is not '
          'brittle and the test result is credible.'),
        h4('Limitation'),
        p('A test measures a small specimen, not the whole part: it cannot prove that a casting is free '
          'from an internal void or that a weld has no crack, which is exactly why the non-destructive '
          'tests exist. And a single test at room temperature says nothing about creep at 550 °C or '
          'brittle fracture at −20 °C.'),
    ),
    gu=join(
        p('<b>Material testing</b> એટલે પદાર્થના ગુણધર્મો માપવા — strength, ductility, hardness, toughness, '
          'અને defectથી મુક્તિ — જેથી design અનુમાનને બદલે માપેલા આંકડા પર આધારિત હોય.'),
        figure(fig.testing_tree(),
               'Fig. 4.2 · બે કુળની કસોટી: destructive ટેસ્ટ નમૂનો બગાડે, non-destructive ટેસ્ટ ભાગને '
               'કામ માટે લાયક રાખે.'),
        h4('કેમ જરૂરી'),
        table(['કારણ', 'ટેસ્ટ શું આપે', 'ન કરો તો પરિણામ'], [
            ['<b>સલામત design</b>', 'yield strength, ultimate strength અને elongation, design stress તથા '
             'factor of safety માટે', 'અનુમાનિત આંકડા પર માપેલું vessel કે structure તૂટી શકે'],
            ['<b>સાચી પસંદગી</b>', 'ઉમેદવાર પદાર્થોની માપેલા ગુણધર્મો પર સરખામણી', 'ખોટો grade પસંદ થાય '
             'અને ભાગ વહેલો ઘસાય કે કટાય'],
            ['<b>ઉત્પાદનનું quality control</b>', 'આવેલો માલ specification સાથે મળે છે એની ચકાસણી (mill test '
             'certificate નમૂના ટેસ્ટથી ચકાસાય)', 'નબળી heatનું steel plantમાં આવી જાય'],
            ['<b>Processનું નિયંત્રણ</b>', 'heat treatment પછીની hardness, welding પછીની strength, casting '
             'પછીની density', 'heat treatment કે weld ખોટું થાય અને કોઈને ખબર ન પડે'],
            ['<b>Failureની તપાસ</b>', 'mechanism — fatigue, creep, brittle fracture, corrosion', 'એ જ નિષ્ફળતા '
             'ફરી ફરી થાય'],
            ['<b>કાયદેસર અને codeની જરૂરિયાત</b>', 'pressure part, lifting tackle કે boiler માટે test '
             'certificate', 'plantનું insurance કે commissioning ન થાય'],
            ['<b>નવા પદાર્થનો વિકાસ</b>', 'નવા alloy કે composite માટે property data', 'નવો પદાર્થ ભરોસા સાથે '
             'વપરાય નહીં'],
            ['<b>અર્થતંત્ર</b>', 'માપેલી જરૂરિયાત પૂરી કરતો સૌથી સસ્તો પદાર્થ', 'વધુ પડતો design અને વધુ ખર્ચ'],
        ]),
        h4('કાર્ય — ટેસ્ટ કેવી રીતે વપરાય, સ્ટેપ અને કારણ'),
        steps(('Step 1', 'Code કહે એ દિશામાં અને એ જગ્યાએથી લોટમાંથી નમૂનો લો. કારણ: forgingમાં અને weld આસપાસ '
                         'ગુણધર્મ બદલાય, એટલે ખોટી જગ્યાનો નમૂનો ભાગ વિશે કંઈ કહેતો નથી.'),
              ('Step 2', 'નમૂનો standard માપ અને ફિનિશમાં તૈયાર કરો. કારણ: ખરબચડો કે જુદા માપનો નમૂનો જુદું '
                         'પરિણામ આપે, અને standard માપ જ પરિણામોની સરખામણી શક્ય કરે.'),
              ('Step 3', 'ટેસ્ટ નિશ્ચિત દરે અને તાપમાને કરો. કારણ: ધાતુ ઝડપી strain rateએ મજબૂત અને ગરમ '
                         'હોય ત્યારે નબળી પડે, એટલે ટેસ્ટની શરત સેવાની શરત સાથે મળવી જોઈએ.'),
              ('Step 4', 'પરિણામ specification સાથે સરખાવીને નોંધો. કારણ: આંકડો acceptance limit સામે જ '
                         'અર્થપૂર્ણ; limit વગરનો ટેસ્ટ કંઈ સાબિત કરતો નથી.')),
        h4('ઉકેલેલું ઉદાહરણ — tensile ટેસ્ટ વાંચવો'),
        p('50 mm gauge length અને 12.5 mm વ્યાસના steelના નમૂનાને 78 kN પર તૂટે એટલું ખેંચાય છે. એ 45 kN પર '
          'yield થાય અને તૂટતી વખતે gauge length 62 mm છે. Yield strength, ultimate strength અને ટકાવારી '
          'elongation શોધો અને ટિપ્પણી કરો.'),
        work('Given: d = 12.5 mm = 0.0125 m · L<sub>0</sub> = 50 mm · F<sub>y</sub> = 45 kN · '
             'F<sub>max</sub> = 78 kN · L<sub>f</sub> = 62 mm',
             'Area A = ' + frac('π d<sup>2</sup>', '4') + ' = ' + frac('3.14 × 0.0125<sup>2</sup>', '4')
             + ' = 1.227 × 10<sup>−4</sup> m<sup>2</sup>',
             'Yield strength = ' + frac('45 × 10<sup>3</sup>', '1.227 × 10<sup>−4</sup>') + ' = 367 MPa',
             'Ultimate strength = ' + frac('78 × 10<sup>3</sup>', '1.227 × 10<sup>−4</sup>') + ' = 636 MPa',
             'Elongation = ' + frac('62 − 50', '50') + ' × 100 = 24 %'),
        result('σ<sub>y</sub> = 367 MPa, σ<sub>u</sub> = 636 MPa, elongation 24 % — ductile, medium-carbon '
               'steel'),
        p('Sanity check: 24 % elongation અને σ<sub>u</sub>/σ<sub>y</sub> = 1.7 એ ductile structural steel માટે '
          'સામાન્ય છે, અને ભાગ તૂટતાં પહેલાં neck બનાવે — એટલે પદાર્થ ભંગુર નથી અને પરિણામ ભરોસાપાત્ર છે.'),
        h4('મર્યાદા'),
        p('ટેસ્ટ નાનો નમૂનો માપે, આખો ભાગ નહીં: એ સાબિત કરી શકે નહીં કે castingમાં અંદર void નથી કે weldમાં '
          'crack નથી — એટલે જ non-destructive ટેસ્ટ હોય છે. અને રૂમ તાપમાનનો એક ટેસ્ટ 550 °C પરના creep કે '
          '−20 °C પરના brittle fracture વિશે કંઈ કહેતો નથી.'),
    ),
))

Q4['cards'].append(dict(
    number='Q.4 (c)', marks=7, q='Explain importance and tools used for visual Inspection for material.',
    en=join(
        h4('What visual inspection is'),
        p('<b>Visual inspection</b> is the examination of a material or a component with the unaided eye, '
          'or with a simple aid such as a magnifier, a boroscope or a light, to find surface defects. It is '
          'the oldest and the cheapest test, it is always the first test, and no other test replaces it.'),
        figure(fig2.visual_inspection(),
               'Fig. 4.3 · Visual inspection of a butt weld — good light, a clean surface and a magnifier '
               'find a surface crack that no gauge would catch.'),
        h4('Importance'),
        table(['Reason', 'What it finds'], [
            ['<b>It is the first filter</b>', 'a part with an obvious crack, a blowhole or a bad weld is '
             'rejected before a costly NDT is spent on it'],
            ['<b>It finds the surface defects that matter most in service</b>', 'cracks, laps, seams, '
             'corrosion pits, and a fatigue crack always starts at a surface'],
            ['<b>It is cheap and quick</b>', 'no consumable, no radiation, no skilled operator beyond a '
             'trained inspector, so 100 % inspection is practical'],
            ['<b>It records the general condition</b>', 'misalignment, undercut, spatter, poor finish, '
             'wrong marking, and a dimension check with a rule'],
            ['<b>It needs no power and no special environment</b>', 'it can be done on site, in a pit, on '
             'a scaffold, on a hot line'],
            ['<b>It is a legal and a code requirement</b>', 'a weld procedure and a pressure vessel both '
             'call for a visual examination before and after other NDT'],
            ['<b>It supports the other tests</b>', 'the area for a dye-penetrant or an ultrasonic test is '
             'chosen from what the eye has already found'],
        ]),
        h4('Tools used'),
        table(['Tool', 'Purpose'], [
            ['<b>Adequate lighting</b> — a torch, a flood lamp, or daylight', 'the eye cannot find a defect '
             'it cannot see; 500–1000 lux at the surface is the normal requirement'],
            ['<b>Magnifying glass or a loupe (2×–10×)</b>', 'resolves a fine crack, a pore or a lap'],
            ['<b>Boroscope / endoscope with a light</b>', 'inspects the inside of a pipe, a tube or a '
             'casting cavity that cannot be opened'],
            ['<b>Flexible fibre-optic and video boroscope</b>', 'reaches a bend or a long tube and records '
             'the image'],
            ['<b>Mirror and a light</b>', 'sees round a corner or into a hidden face'],
            ['<b>Weld gauge (fillet and butt weld gauge)</b>', 'measures the leg length, the throat, the '
             'reinforcement and the undercut'],
            ['<b>Vernier, micrometer, steel rule, feeler and taper gauge</b>', 'checks the dimension, the '
             'gap and the alignment'],
            ['<b>Surface comparator / replica tape</b>', 'judges the surface roughness against a standard'],
            ['<b>Cleaning tools — wire brush, solvent, emery</b>', 'the surface must be clean and dry, '
             'because scale and paint hide the defect'],
            ['<b>Camera and a report form</b>', 'records the finding and its location, so that the repair '
             'can be traced'],
            ['<b>Magnet and a dye-penetrant kit (as an extension)</b>', 'confirms a crack the eye has '
             'suspected — a visual finding often leads straight to an NDT'],
        ]),
        h4('Working — the inspection, step and reason'),
        steps(('Step 1', 'Clean the surface — wire brush, solvent, and dry it. Reason: scale, paint, oil and '
                         'water hide a crack, and a wet surface reflects light into the eye.'),
              ('Step 2', 'Light the surface at a low angle rather than straight on. Reason: a raking light '
                         'casts a shadow in a fine crack or a lap, which makes it visible.'),
              ('Step 3', 'Examine systematically — in a grid, or along the weld from toe to toe. Reason: a '
                         'random scan misses the one defect that matters, and a grid makes the coverage '
                         'provable.'),
              ('Step 4', 'Use the magnifier, the boroscope or the gauge on anything that looks doubtful. '
                         'Reason: the eye is poor at judging a size, and a weld gauge gives a number that '
                         'can be compared with the acceptance limit.'),
              ('Step 5', 'Record, mark and report every finding. Reason: a defect that is not recorded is not '
                         'repaired, and the report is the evidence for the next inspection.')),
        h4('Worked example — is the undercut acceptable?'),
        p('A fillet weld of 8 mm leg length shows an undercut of 0.6 mm along 40 mm of its length. The code '
          'allows an undercut of 0.5 mm, or up to 1.0 mm if the length is below 10 % of the weld length. '
          'Decide whether the weld is acceptable for a weld length of 500 mm.'),
        work('Given: leg = 8 mm · undercut = 0.6 mm · undercut length = 40 mm · weld length = 500 mm · '
             'allowance 0.5 mm, or 1.0 mm if the length is under 10 %',
             'Is 0.6 mm above the general 0.5 mm limit? Yes',
             'Is the length below 10 % of the weld? ' + frac('40', '500') + ' × 100 = 8 %',
             'Is 8 % below 10 %? Yes, so the relaxed 1.0 mm limit applies',
             'Is 0.6 mm below 1.0 mm? Yes'),
        result('The undercut is within the code, so the weld is acceptable — but it must be recorded'),
        p('Sanity check: 8 % is just inside the 10 % allowance, so the decision is sensitive to the '
          'measurement; a re-measure of the undercut length is the prudent step before accepting it.'),
        h4('Limitations'),
        bullets('It finds <b>surface</b> defects only — an internal void, a lack of fusion inside a weld or '
                'a mid-wall crack is completely invisible, which is why DPT, MPI, UT and RT exist.',
                'It depends on the inspector: eyesight, training and fatigue change the result, so a '
                'second inspector or a documented procedure is needed.',
                'It needs access and light: a closed vessel, an insulated pipe or a dark corner cannot be '
                'inspected without a boroscope or dismantling.',
                'A very fine crack, or one filled with dirt or paint, can be missed — and a small '
                'indication is easily dismissed as a scratch.'),
    ),
    gu=join(
        h4('Visual inspection એટલે શું'),
        p('<b>Visual inspection</b> એટલે પદાર્થ કે ભાગને નરી આંખે, કે magnifier, boroscope કે light જેવા '
          'સાદા સાધનથી જોઈને સપાટીની ખામી શોધવી. એ સૌથી જૂની અને સૌથી સસ્તી કસોટી છે, હંમેશા પહેલી કસોટી '
          'છે, અને બીજી કોઈ કસોટી એની જગ્યા લઈ શકતી નથી.'),
        figure(fig2.visual_inspection(),
               'Fig. 4.3 · Butt weldનું visual inspection — સારો પ્રકાશ, સાફ સપાટી અને magnifier એ સપાટીની '
               'crack શોધે જે કોઈ gauge ન પકડે.'),
        h4('મહત્ત્વ'),
        table(['કારણ', 'શું શોધે'], [
            ['<b>એ પહેલું filter છે</b>', 'સ્પષ્ટ crack, blowhole કે ખોટો weld વાળો ભાગ મોંઘા NDT પહેલાં જ '
             'નકારાય'],
            ['<b>સેવામાં સૌથી મહત્ત્વની સપાટીની ખામી એ જ શોધે</b>', 'crack, lap, seam, corrosion pit — અને '
             'fatigue crack હંમેશા સપાટીથી જ શરૂ થાય'],
            ['<b>સસ્તું અને ઝડપી</b>', 'કોઈ consumable નહીં, radiation નહીં, તાલીમબદ્ધ inspector સિવાય કોઈ '
             'નહીં, એટલે 100 % inspection શક્ય'],
            ['<b>સામાન્ય સ્થિતિની નોંધ</b>', 'misalignment, undercut, spatter, ખરાબ ફિનિશ, ખોટું marking, અને '
             'rule વડે માપ'],
            ['<b>વીજળી કે ખાસ વાતાવરણની જરૂર નહીં</b>', 'site પર, ખાડામાં, scaffold પર, ગરમ લાઇન પર થઈ '
             'શકે'],
            ['<b>કાયદેસર અને codeની જરૂરિયાત</b>', 'weld procedure અને pressure vessel બંને બીજા NDT પહેલાં '
             'અને પછી visual examination માગે'],
            ['<b>બીજી કસોટીને ટેકો</b>', 'આંખે જોયું એના આધારે dye-penetrant કે ultrasonic ટેસ્ટની જગ્યા '
             'પસંદ થાય'],
        ]),
        h4('વપરાતાં સાધનો'),
        table(['સાધન', 'હેતુ'], [
            ['<b>પૂરતો પ્રકાશ</b> — torch, flood lamp કે દિવસનો પ્રકાશ', 'આંખ જે ખામી જોઈ શકે નહીં એ શોધી '
             'શકે નહીં; સપાટી પર 500–1000 lux સામાન્ય જરૂરિયાત'],
            ['<b>Magnifying glass કે loupe (2×–10×)</b>', 'બારીક crack, pore કે lap જોઈ શકાય'],
            ['<b>Boroscope / endoscope, પ્રકાશ સાથે</b>', 'ખોલી ન શકાય એવી pipe, tube કે casting cavityની '
             'અંદરની તપાસ'],
            ['<b>Flexible fibre-optic અને video boroscope</b>', 'વળાંક કે લાંબી tube સુધી પહોંચીને ચિત્ર '
             'નોંધે'],
            ['<b>અરીસો અને પ્રકાશ</b>', 'ખૂણા પાછળ કે છુપાયેલી સપાટી જુએ'],
            ['<b>Weld gauge (fillet અને butt weld gauge)</b>', 'leg length, throat, reinforcement અને undercut '
             'માપે'],
            ['<b>Vernier, micrometer, steel rule, feeler અને taper gauge</b>', 'માપ, gap અને alignment ચકાસે'],
            ['<b>Surface comparator / replica tape</b>', 'સપાટીની roughness standard સામે આંકે'],
            ['<b>સફાઈનાં સાધન — wire brush, solvent, emery</b>', 'સપાટી સાફ અને સૂકી હોવી જોઈએ, કારણ કે '
             'scale અને paint ખામી ઢાંકે'],
            ['<b>કૅમેરો અને report form</b>', 'શું મળ્યું અને ક્યાં, એ નોંધે જેથી repair ટ્રેસ થાય'],
            ['<b>Magnet અને dye-penetrant kit (વિસ્તાર તરીકે)</b>', 'આંખે શંકા પડેલી crack ખાતરી કરે — visual '
             'finding ઘણી વાર સીધી NDT તરફ લઈ જાય'],
        ]),
        h4('કાર્ય — inspection, સ્ટેપ અને કારણ'),
        steps(('Step 1', 'સપાટી સાફ કરો — wire brush, solvent, અને સૂકવો. કારણ: scale, paint, oil અને પાણી '
                         'crack ઢાંકે, અને ભીની સપાટી પ્રકાશ આંખમાં પરાવર્તિત કરે.'),
              ('Step 2', 'પ્રકાશ સીધો નહીં પણ નીચા ખૂણેથી આપો. કારણ: રેતી જેવો પ્રકાશ બારીક crack કે lapમાં '
                         'પડછાયો પાડે, જેથી એ દેખાય.'),
              ('Step 3', 'વ્યવસ્થિત રીતે તપાસો — gridમાં, કે weldના toeથી toe સુધી. કારણ: અવ્યવસ્થિત સ્કેન '
                         'એ એક ખામી ચૂકી જાય જે મહત્ત્વની છે, અને grid coverage સાબિત કરી શકાય.'),
              ('Step 4', 'શંકાસ્પદ દેખાય એના પર magnifier, boroscope કે gauge વાપરો. કારણ: આંખ માપ આંકવામાં '
                         'નબળી છે, અને weld gauge એવો આંકડો આપે જે acceptance limit સાથે સરખાવી શકાય.'),
              ('Step 5', 'દરેક finding નોંધો, mark કરો અને report કરો. કારણ: ન નોંધાયેલી ખામી સુધરતી નથી, '
                         'અને report જ આગલી inspectionનો પુરાવો છે.')),
        h4('ઉકેલેલું ઉદાહરણ — undercut સ્વીકાર્ય છે?'),
        p('8 mm leg length વાળા fillet weldમાં 40 mm લંબાઈ સુધી 0.6 mm undercut દેખાય છે. Code 0.5 mm '
          'undercut સ્વીકારે, અથવા 1.0 mm સુધી જો લંબાઈ weldની લંબાઈના 10 %થી ઓછી હોય. Weldની લંબાઈ '
          '500 mm હોય તો weld સ્વીકાર્ય છે કે નહીં તે નક્કી કરો.'),
        work('Given: leg = 8 mm · undercut = 0.6 mm · undercutની લંબાઈ = 40 mm · weldની લંબાઈ = 500 mm · '
             'allowance 0.5 mm, અથવા લંબાઈ 10 %થી ઓછી હોય તો 1.0 mm',
             '0.6 mm સામાન્ય 0.5 mm મર્યાદાથી વધુ છે? હા',
             'લંબાઈ weldના 10 %થી ઓછી છે? ' + frac('40', '500') + ' × 100 = 8 %',
             '8 % એ 10 %થી ઓછું છે? હા, એટલે 1.0 mmની છૂટ લાગુ પડે',
             '0.6 mm એ 1.0 mmથી ઓછું છે? હા'),
        result('Undercut codeમાં છે, એટલે weld સ્વીકાર્ય — પણ એ નોંધવું ફરજિયાત છે'),
        p('Sanity check: 8 % એ 10 %ની છૂટની બરાબર અંદર છે, એટલે નિર્ણય માપ પર સંવેદનશીલ છે; સ્વીકારતાં '
          'પહેલાં undercutની લંબાઈ ફરી માપવી સમજદારી છે.'),
        h4('મર્યાદાઓ'),
        bullets('એ ફક્ત <b>સપાટીની</b> ખામી શોધે — અંદરનું void, weldની અંદર lack of fusion કે mid-wall crack '
                'સાવ અદૃશ્ય છે, એટલે જ DPT, MPI, UT અને RT છે.',
                'એ inspector પર આધારિત: દૃષ્ટિ, તાલીમ અને થાક પરિણામ બદલે, એટલે બીજો inspector કે લેખિત '
                'procedure જોઈએ.',
                'એને access અને પ્રકાશ જોઈએ: બંધ vessel, insulated pipe કે અંધારો ખૂણો boroscope કે '
                'dismantling વગર તપાસી શકાય નહીં.',
                'બહુ બારીક crack, કે ધૂળ-પેન્ટથી ભરેલી crack ચૂકાઈ શકે — અને નાની indicationને ખરજ ગણીને '
                'અવગણવામાં આવે.'),
    ),
))

Q4['cards'].append(dict(
    number='Q.4 (a)', marks=3, tag='OR', q='List properties and application of monel metal.',
    en=join(
        p('<b>Monel</b> is a nickel–copper alloy with roughly <b>67 % Ni, 30 % Cu, 1.5 % Fe and small '
          'amounts of Mn, Si and C</b>. It is a single-phase solid solution, which is why it is tough, and '
          'it is one of the standard alloys for sea water and for hydrofluoric acid service.'),
        table(['Property', 'Value / behaviour'], [
            ['Composition', '67 % Ni, 30 % Cu, 1.5 % Fe, 1 % Mn, small Si and C'],
            ['Strength', 'tensile 480–620 MPa, yield 170–350 MPa; it work-hardens strongly'],
            ['Hardness', 'about 125–250 HB, depending on the temper'],
            ['Ductility', 'elongation 20–35 %, so it can be rolled, drawn and deep-drawn'],
            ['Corrosion resistance', 'excellent in sea water, in neutral and alkaline solutions, in '
             'hydrofluoric acid and in sulphuric acid without air'],
            ['High-temperature behaviour', 'usable up to about 500 °C, with good oxidation resistance'],
            ['Electrical and thermal', 'low conductivity compared with copper, so it is not used as a '
             'conductor'],
            ['Magnetic', 'non-magnetic (unlike most nickel alloys), which matters for instruments'],
            ['Machinability', 'only fair, because it work-hardens; it needs a slow speed and a heavy feed'],
            ['Cost', 'expensive, because nickel is dear'],
        ]),
        h4('Applications'),
        bullets('Sea-water piping, pump shafts, valve trim, condenser tubes and marine propeller shafts.',
                'Chemical plant for <b>hydrofluoric acid</b> and for sulphuric acid, where no other '
                'common alloy survives.',
                'Petroleum refining equipment, and sour-gas and brine handling.',
                'Domestic and food equipment: a good-quality sink, a cooking pan, a milk-line fitting.',
                'Instrument parts and springs that must be non-magnetic and corrosion resistant.'),
        p('<b>Example:</b> a sea-water cooling line on a ship uses monel tube because copper–nickel and '
          'monel both resist sea water, but monel also resists the velocity and the erosion–corrosion at '
          'the tube inlet.'),
        p('<b>Limitation:</b> monel is expensive and its machinability is poor because it work-hardens — so '
          'it is used only where a cheaper stainless steel or cupronickel will not survive.'),
    ),
    gu=join(
        p('<b>Monel</b> એ નિકલ–તાંબાનું alloy છે જેમાં લગભગ <b>67 % Ni, 30 % Cu, 1.5 % Fe</b> અને થોડું '
          'Mn, Si તથા C હોય. એ single-phase solid solution છે, એટલે tough છે, અને sea water તથા '
          'hydrofluoric acid માટેનું માનક alloy છે.'),
        table(['ગુણધર્મ', 'કિંમત / વર્તન'], [
            ['રચના', '67 % Ni, 30 % Cu, 1.5 % Fe, 1 % Mn, થોડું Si અને C'],
            ['Strength', 'tensile 480–620 MPa, yield 170–350 MPa; ખૂબ work-harden થાય'],
            ['Hardness', 'temper પ્રમાણે લગભગ 125–250 HB'],
            ['Ductility', 'elongation 20–35 %, એટલે roll, draw અને deep-draw થઈ શકે'],
            ['Corrosion પ્રતિરોધ', 'sea waterમાં, neutral અને alkaline દ્રાવણમાં, hydrofluoric acidમાં અને '
             'હવા વગરના sulphuric acidમાં ઉત્તમ'],
            ['ઊંચા તાપમાનનું વર્તન', 'લગભગ 500 °C સુધી વપરાય, oxidation સામે સારો પ્રતિરોધ'],
            ['Electrical અને thermal', 'તાંબા કરતાં નીચી conductivity, એટલે conductor તરીકે વપરાય નહીં'],
            ['Magnetic', 'non-magnetic (મોટા ભાગના nickel alloyથી વિપરીત), જે instrument માટે મહત્ત્વનું'],
            ['Machinability', 'ફક્ત સાધારણ, કારણ કે work-harden થાય; ધીમી ઝડપ અને ભારે feed જોઈએ'],
            ['ખર્ચ', 'મોંઘું, કારણ કે નિકલ મોંઘું'],
        ]),
        h4('ઉપયોગ'),
        bullets('Sea-water pipe, pump shaft, valve trim, condenser tube અને જહાજનો propeller shaft.'),
        '<b>Hydrofluoric acid</b> અને sulphuric acid માટેનું chemical plant, જ્યાં બીજું સામાન્ય alloy ટકતું '
        'નથી.',
        'Petroleum refiningનાં સાધનો, અને sour gas તથા brine handling.',
        'ઘરેલું અને ખાદ્ય સાધન: સારી ગુણવત્તાનું sink, રાંધણું વાસણ, milk-line fitting.',
        'Non-magnetic અને corrosion-resistant હોવું જોઈએ એવા instrumentના ભાગ અને spring.',
        p('<b>ઉદાહરણ:</b> જહાજની sea-water cooling lineમાં monel tube વપરાય, કારણ કે copper–nickel અને '
          'monel બંને sea water ઝીલે, પણ monel tubeના મુખ પરના velocity અને erosion–corrosion સામે પણ ટકે.'),
        p('<b>મર્યાદા:</b> monel મોંઘું છે અને work-hardeningને કારણે machinability નબળી — એટલે જ્યાં સસ્તું '
          'stainless steel કે cupronickel ટકે નહીં ત્યાં જ વપરાય.'),
    ),
))

Q4['cards'].append(dict(
    number='Q.4 (b)', marks=4, tag='OR', q='Describe dye penetration testing.',
    en=join(
        h4('Principle'),
        p('<b>Dye penetrant testing (DPT)</b>, also called liquid penetrant inspection, is a '
          'non-destructive test that finds <b>surface-breaking</b> defects in a non-porous material. A '
          'coloured or fluorescent liquid is applied and it seeps into a crack by <b>capillary action</b>; '
          'the excess is cleaned off and a developer draws the trapped liquid back out, so the crack shows '
          'as a bright line.'),
        figure(fig.dye_penetrant(),
               'Fig. 4.4 · The five steps of DPT — clean, penetrate, remove the excess, develop, and '
               'inspect.'),
        h4('Working — step and reason'),
        steps(('Step 1 · Pre-clean', 'The surface is cleaned of oil, scale, paint and water and then dried. '
                                     'Reason: the penetrant can only enter a crack that is open and clean, '
                                     'and any dirt blocks the entry.'),
              ('Step 2 · Apply the penetrant', 'The part is flooded or dipped and left for a dwell time of '
                                               '5–30 minutes. Reason: the liquid needs time to be drawn '
                                               'into a fine crack by capillary pressure, and a fine crack '
                                               'takes longer.'),
              ('Step 3 · Remove the excess', 'The surface penetrant is wiped and washed off. Reason: only '
                                             'the liquid <b>inside</b> the defect should remain, or the '
                                             'whole surface would glow and hide the indication.'),
              ('Step 4 · Apply the developer', 'A thin white powder layer is sprayed on and left to dry. '
                                               'Reason: the powder draws the trapped penetrant out by '
                                               'absorption and gives a contrasting white background.'),
              ('Step 5 · Inspect and record', 'The part is examined under white light, or under UV for a '
                                              'fluorescent penetrant. Reason: a coloured indication stands '
                                              'out against the white developer, and the size is judged '
                                              'against the acceptance standard.')),
        h4('Methods and their properties'),
        table(['Method', 'Penetrant', 'Advantage', 'Limitation'], [
            ['Colour contrast (visible dye)', 'red dye in a solvent', 'no UV lamp needed; works in daylight',
             'less sensitive than fluorescent'],
            ['Fluorescent', 'fluorescent dye', 'the most sensitive; a fine crack glows brightly under UV',
             'needs a dark room and a UV lamp'],
            ['Water-washable', 'penetrant with an emulsifier in it', 'quick, one step to wash', 'easy to '
             'over-wash and lose the indication'],
            ['Post-emulsifiable', 'separate emulsifier', 'most sensitive water-wash method, good for a '
             'rough surface', 'one extra step'],
            ['Solvent-removable', 'penetrant wiped with solvent', 'portable, used on site for a weld',
             'less repeatable'],
        ]),
        h4('Worked example — how deep the penetrant must be'),
        p('The capillary rise in a crack of width 2w = 2 µm can be estimated from h = 2γ cos θ/(ρ g w). '
          'Take γ = 0.030 N/m, θ = 0°, ρ = 900 kg/m<sup>3</sup> and w = 1 µm. Find the rise and the time '
          'for it to be useful.'),
        work('Given: γ = 0.030 N/m · θ = 0° so cos θ = 1 · ρ = 900 kg/m<sup>3</sup> · '
             'w = 1 × 10<sup>−6</sup> m · g = 9.81 m/s<sup>2</sup>',
             'h = ' + frac('2 γ cos θ', 'ρ g w') + ' = '
             + frac('2 × 0.030 × 1', '900 × 9.81 × 1 × 10<sup>−6</sup>'),
             'h = ' + frac('0.060', '8.83 × 10<sup>−3</sup>') + ' = 6.8 m'),
        result('The capillary rise is far more than the wall thickness (6.8 m against a few mm), so the '
               'penetrant fills the crack quickly — the dwell time is set by viscosity, not by height'),
        p('Sanity check: a rise of metres in a micron-wide crack means gravity is negligible, so a 5–30 '
          'minute dwell is governed by the viscosity and by the fact that the crack may be only partly '
          'open — consistent with the standard practice.'),
        h4('Limitations'),
        bullets('It finds <b>surface-breaking</b> defects only — an internal void or a crack below a weld '
                'cap is invisible, so DPT complements rather than replaces UT or RT.',
                'The surface must be smooth and non-porous; a rough casting or a porous weld gives a '
                'background of false indications.',
                'It cannot be used on a painted or plated part, and it must be done before the coating.',
                'The penetrant and the developer are a health and a fire hazard, and the residues must be '
                'cleaned off afterwards — especially on a stainless steel that will be welded or on a '
                'titanium part, where a chloride residue causes later cracking.'),
    ),
    gu=join(
        h4('સિદ્ધાંત'),
        p('<b>Dye penetrant testing (DPT)</b>, જેને liquid penetrant inspection પણ કહે, એ non-destructive '
          'ટેસ્ટ છે જે non-porous પદાર્થમાં <b>સપાટી સુધી ખુલ્લી</b> ખામી શોધે. રંગીન કે fluorescent પ્રવાહી '
          'લગાવાય અને એ <b>capillary action</b>થી crackમાં ઊતરે; વધારાનું લૂછી નાખાય અને developer ફસાયેલું '
          'પ્રવાહી પાછું ખેંચે, જેથી crack તેજસ્વી લીટી તરીકે દેખાય.'),
        figure(fig.dye_penetrant(),
               'Fig. 4.4 · DPTના પાંચ સ્ટેપ — સફાઈ, penetrant, વધારાનું દૂર, developer, અને inspection.'),
        h4('કાર્ય — સ્ટેપ અને કારણ'),
        steps(('Step 1 · Pre-clean', 'સપાટી પરથી oil, scale, paint અને પાણી સાફ કરીને સૂકવાય. કારણ: penetrant '
                                     'ફક્ત ખુલ્લી અને સાફ crackમાં જ જઈ શકે, અને ધૂળ મુખ બંધ કરે.'),
              ('Step 2 · Penetrant લગાવો', 'ભાગ પર penetrant રેડાય કે ડુબાડાય અને 5–30 મિનિટ રહેવા દેવાય. '
                                           'કારણ: capillary pressureથી પ્રવાહી બારીક crackમાં ઊતરવા સમય જોઈએ, '
                                           'અને બારીક crackને વધુ સમય લાગે.'),
              ('Step 3 · વધારાનું દૂર કરો', 'સપાટીનું penetrant લૂછીને ધોવાય. કારણ: ફક્ત ખામીની <b>અંદરનું</b> '
                                          'પ્રવાહી રહેવું જોઈએ, નહીં તો આખી સપાટી ચમકે અને indication ઢંકાય.'),
              ('Step 4 · Developer લગાવો', 'પાતળો સફેદ પાવડર છાંટીને સૂકવાય. કારણ: પાવડર ફસાયેલું penetrant '
                                          'ખેંચી કાઢે અને વિરોધી સફેદ પાર્શ્વભૂમિ આપે.'),
              ('Step 5 · Inspection અને નોંધ', 'ભાગ સફેદ પ્રકાશમાં, કે fluorescent penetrant માટે UV નીચે '
                                             'જોવાય. કારણ: રંગીન indication સફેદ developer સામે ઊપસી આવે, '
                                             'અને એનું માપ acceptance standard સામે આંકાય.')),
        h4('પદ્ધતિઓ અને એમના ગુણધર્મો'),
        table(['પદ્ધતિ', 'Penetrant', 'ફાયદો', 'મર્યાદા'], [
            ['Colour contrast (દૃશ્ય dye)', 'solventમાં લાલ dye', 'UV lamp ન જોઈએ; દિવસના પ્રકાશમાં ચાલે',
             'fluorescent કરતાં ઓછી sensitivity'],
            ['Fluorescent', 'fluorescent dye', 'સૌથી વધુ sensitive; બારીક crack UV નીચે તેજસ્વી ચમકે',
             'અંધારું ઓરડું અને UV lamp જોઈએ'],
            ['Water-washable', 'અંદર emulsifier વાળો penetrant', 'ઝડપી, ધોવાનું એક જ સ્ટેપ', 'વધુ ધોવાય તો '
             'indication જતું રહે'],
            ['Post-emulsifiable', 'અલગ emulsifier', 'water-washમાં સૌથી sensitive, ખરબચડી સપાટી માટે સારી',
             'એક વધારાનું સ્ટેપ'],
            ['Solvent-removable', 'solventથી લૂછાતું penetrant', 'portable, site પર weld માટે વપરાય',
             'ઓછું repeatable'],
        ]),
        h4('ઉકેલેલું ઉદાહરણ — penetrant કેટલું ઊંડે જવું પડે'),
        p('2w = 2 µm પહોળાઈના crackમાં capillary rise h = 2γ cos θ/(ρ g w)થી આંકી શકાય. γ = 0.030 N/m, '
          'θ = 0°, ρ = 900 kg/m<sup>3</sup> અને w = 1 µm લઈને rise શોધો.'),
        work('Given: γ = 0.030 N/m · θ = 0° એટલે cos θ = 1 · ρ = 900 kg/m<sup>3</sup> · '
             'w = 1 × 10<sup>−6</sup> m · g = 9.81 m/s<sup>2</sup>',
             'h = ' + frac('2 γ cos θ', 'ρ g w') + ' = '
             + frac('2 × 0.030 × 1', '900 × 9.81 × 1 × 10<sup>−6</sup>'),
             'h = ' + frac('0.060', '8.83 × 10<sup>−3</sup>') + ' = 6.8 m'),
        result('Capillary rise દીવાલની જાડાઈ (થોડા mm) કરતાં ઘણું વધુ (6.8 m) છે, એટલે penetrant crack ઝડપથી '
               'ભરે — dwell time વiscosityથી નક્કી થાય, ઊંચાઈથી નહીં'),
        p('Sanity check: માઇક્રોન પહોળાઈના crackમાં મીટરો ઊંચું ચઢવું એટલે gravity નજીવી, એટલે 5–30 મિનિટનો '
          'dwell viscosity અને crack ફક્ત અંશતઃ ખુલ્લી હોવાથી નક્કી થાય — માનક પદ્ધતિ સાથે મળે.'),
        h4('મર્યાદાઓ'),
        bullets('એ ફક્ત <b>સપાટી સુધી ખુલ્લી</b> ખામી શોધે — અંદરનું void કે weld cap નીચેની crack અદૃશ્ય છે, '
                'એટલે DPT UT કે RTની જગ્યા લેતું નથી, પૂરક છે.',
                'સપાટી સપાટ અને non-porous હોવી જોઈએ; ખરબચડું casting કે porous weld ખોટા indicationની '
                'પાર્શ્વભૂમિ આપે.',
                'Painted કે plated ભાગ પર વપરાય નહીં, અને coating પહેલાં જ કરવું પડે.',
                'Penetrant અને developer આરોગ્ય તથા આગનું જોખમ છે, અને અવશેષ પછી સાફ કરવા પડે — ખાસ કરીને '
                'weld કરવાના stainless steel કે titanium પર, જ્યાં chloride અવશેષ પછી crack કરે.'),
    ),
))

Q4['cards'].append(dict(
    number='Q.4 (c)', marks=7, tag='OR', q='Explain hydrostatic testing and pneumatic testing.',
    en=join(
        h4('What the two tests are for'),
        p('A newly built or a repaired pressure vessel, a pipeline or a boiler must be proved <b>sound</b> '
          'and <b>tight</b> before it is put into service. Two tests do this: a <b>hydrostatic test</b>, in '
          'which the vessel is filled with water and pressurised, and a <b>pneumatic test</b>, in which it '
          'is filled with air or nitrogen and pressurised.'),
        figure(fig.hydrostatic(),
               'Fig. 4.5 · Hydrostatic test — the vessel is filled with water, a test pump raises the '
               'pressure, and a gauge and a relief valve protect the test.'),
        h4('Hydrostatic test'),
        table(['Part of the test', 'Purpose'], [
            ['Filling with water (with a vent open)', 'expels all the air, which is the point: water is '
             'almost incompressible, so the stored energy is small'],
            ['Test pump and a calibrated gauge', 'raises the pressure steadily to the test pressure and '
             'reads it'],
            ['Test pressure', 'usually 1.5 times the design pressure, or as the code requires'],
            ['Holding time', '30 minutes at the test pressure, then a check of the gauge and of every '
             'joint'],
            ['Relief valve on the test rig', 'protects the vessel against a pump surge or a thermal rise'],
            ['Inspection of all welds and joints', 'a leak shows as a drip or a damp patch; a permanent '
             'deformation shows on the gauge'],
        ]),
        h4('Working — hydrostatic, step and reason'),
        steps(('Step 1', 'Fill the vessel with water and vent all the air out. Reason: air is compressible, '
                         'so any air left stores energy that would be released violently if the vessel '
                         'failed.'),
              ('Step 2', 'Pressurise slowly to the test pressure with a hand or a motor pump. Reason: a '
                         'slow rise lets the metal yield locally and redistribute the stress instead of '
                         'shocking it.'),
              ('Step 3', 'Hold for 30 minutes and inspect every weld and joint. Reason: a leak needs time '
                         'to appear at a joint, and the hold also shows any creep or permanent set.'),
              ('Step 4', 'Reduce the pressure to the design value, inspect again, then drain and dry. '
                         'Reason: the test is read at a steady, safe pressure, and the water must be out '
                         'before the vessel is commissioned.')),
        h4('Pneumatic test'),
        table(['Point', 'Pneumatic test', 'Why it is used'], [
            ['Medium', 'dry air or nitrogen', 'a vessel that cannot be filled with water — a large gas '
             'holder, an air receiver on site, a pipeline in a cold climate, a vessel with a refractory '
             'lining that water would ruin'],
            ['Test pressure', 'usually 1.1–1.25 times the design pressure, lower than the hydrostatic value',
             'air stores far more energy, so the test pressure is reduced'],
            ['Stored energy', 'very high — a 1 m<sup>3</sup> vessel at 10 bar holds the energy of about '
             '1 kg of TNT', 'the reason for the strict precautions'],
            ['Method', 'a soap or a leak-detection solution on every joint, a pressure hold, and a check of '
             'the gauge', 'a leak shows as a bubble'],
            ['Precautions', 'a barricade, no personnel in line with a joint, remote gauges, and a staged '
             'pressure rise', 'a brittle failure of an air-filled vessel is an explosion'],
        ]),
        h4('Comparison'),
        table(['Point', 'Hydrostatic test', 'Pneumatic test'], [
            ['Medium', 'water (with a corrosion inhibitor)', 'air or nitrogen'],
            ['Stored energy', 'low — water is nearly incompressible', 'high — the gas is compressible'],
            ['Test pressure', '1.5 × design pressure', '1.1–1.25 × design pressure'],
            ['Sensitivity to a leak', 'good — a drip is seen', 'excellent for a small leak if a soap '
             'solution is used'],
            ['Safety of the test', 'safe: a failure leaks water', 'dangerous: a failure is an explosion'],
            ['After the test', 'drain and dry; the water must not be left in', 'no drying needed'],
            ['When it is preferred', 'the default for a new pressure vessel', 'only where water cannot be '
             'used, with the code permission'],
        ]),
        h4('Worked example — the energy stored in the two tests'),
        p('A vessel of 2 m<sup>3</sup> is tested at 15 bar. Estimate the energy released if it fails in a '
          'hydrostatic test and in a pneumatic test, taking the bulk modulus of water as 2.2 GPa and '
          'treating the air as isothermal.'),
        work('Given: V = 2 m<sup>3</sup> · P = 15 bar = 1.5 × 10<sup>6</sup> Pa · '
             'K<sub>water</sub> = 2.2 × 10<sup>9</sup> Pa',
             'Water: the stored energy ≈ ' + frac('P<sup>2</sup> V', '2 K') + ' = '
             + frac('(1.5 × 10<sup>6</sup>)<sup>2</sup> × 2', '2 × 2.2 × 10<sup>9</sup>')
             + ' = 1.0 × 10<sup>3</sup> J',
             'Air (isothermal): W = P V ln(P<sub>2</sub>/P<sub>1</sub>) = 1.5 × 10<sup>6</sup> × 2 × '
             'ln 15',
             '= 3.0 × 10<sup>6</sup> × 2.71'),
        result('About 1 kJ with water against 8.1 MJ with air — a ratio of roughly 8000 to 1'),
        p('Sanity check: 8 MJ is about the energy of 2 kg of TNT, which is exactly why a pneumatic test is '
          'barricaded while a hydrostatic test is not — the calculation justifies the rule.'),
        h4('Limitations'),
        bullets('A hydrostatic test leaves water in the vessel: it must be drained and dried, or it causes '
                'corrosion; and a vessel that cannot be dried, or one with a refractory lining, cannot be '
                'tested this way.',
                'A hydrostatic test may be impossible in freezing weather, and the water must be treated '
                'with an inhibitor for a stainless steel (chlorides cause stress corrosion).',
                'A pneumatic test is the only option for a gas holder or a large air receiver, but its '
                'stored energy makes it a hazardous operation, allowed only with a code permission, a '
                'barricade and a staged pressure rise.',
                'Neither test finds an internal lamination or a small slag inclusion unless it happens to '
                'leak — that is the job of UT and RT, so a pressure test is a proof of tightness, not a '
                'complete proof of soundness.'),
    ),
    gu=join(
        h4('બે ટેસ્ટ શેના માટે'),
        p('નવું બનેલું કે સુધારેલું pressure vessel, pipeline કે boiler સેવામાં મુકાય એ પહેલાં <b>ઘન</b> અને '
          '<b>ચુસ્ત</b> હોવું સાબિત કરવું પડે. બે ટેસ્ટ એ કરે: <b>hydrostatic test</b>, જેમાં vessel પાણીથી '
          'ભરીને pressure આપાય, અને <b>pneumatic test</b>, જેમાં હવા કે nitrogen ભરીને pressure આપાય.'),
        figure(fig.hydrostatic(),
               'Fig. 4.5 · Hydrostatic test — vessel પાણીથી ભરાય, test pump pressure વધારે, અને gauge તથા '
               'relief valve ટેસ્ટ બચાવે.'),
        h4('Hydrostatic test'),
        table(['ટેસ્ટનો ભાગ', 'હેતુ'], [
            ['પાણીથી ભરવું (vent ખુલ્લો રાખીને)', 'બધી હવા કાઢે, જે મુખ્ય મુદ્દો છે: પાણી લગભગ '
             'incompressible હોવાથી સંગ્રહાયેલી energy ઓછી'],
            ['Test pump અને calibrated gauge', 'pressure ધીમે test pressure સુધી લાવે અને વાંચે'],
            ['Test pressure', 'સામાન્ય રીતે design pressureના 1.5 ગણું, કે code કહે એ પ્રમાણે'],
            ['Holdનો સમય', 'test pressure પર 30 મિનિટ, પછી gauge અને દરેક jointની ચકાસણી'],
            ['Test rig પર relief valve', 'pump surge કે thermal rise સામે vessel બચાવે'],
            ['બધા weld અને jointની inspection', 'leak ટીપું કે ભીનો ડાઘ તરીકે દેખાય; કાયમી deformation '
             'gauge પર દેખાય'],
        ]),
        h4('કાર્ય — hydrostatic, સ્ટેપ અને કારણ'),
        steps(('Step 1', 'Vessel પાણીથી ભરો અને બધી હવા vent દ્વારા કાઢો. કારણ: હવા compressible છે, એટલે '
                         'બાકી રહેલી હવા energy સંઘરે જે vessel ફાટે તો જોરથી બહાર નીકળે.'),
              ('Step 2', 'Hand કે motor pumpથી ધીમે test pressure સુધી pressure વધારો. કારણ: ધીમો વધારો '
                         'ધાતુને સ્થાનિક રીતે yield થઈને stress ફરી વહેંચવા દે, આંચકો આપતું નથી.'),
              ('Step 3', '30 મિનિટ hold કરીને દરેક weld અને joint તપાસો. કારણ: leak દેખાવા સમય જોઈએ, અને '
                         'hold creep કે કાયમી set પણ દેખાડે.'),
              ('Step 4', 'Pressure ઘટાડીને design value પર લાવો, ફરી તપાસો, પછી પાણી કાઢીને સૂકવો. કારણ: '
                         'ટેસ્ટ સ્થિર અને સલામત pressure પર વંચાય, અને vessel commissioning પહેલાં પાણી નીકળવું '
                         'જોઈએ.')),
        h4('Pneumatic test'),
        table(['મુદ્દો', 'Pneumatic test', 'કેમ વપરાય'], [
            ['Medium', 'સૂકી હવા કે nitrogen', 'જે vessel પાણીથી ભરી શકાય નહીં — મોટું gas holder, site પરનું '
             'air receiver, ઠંડા હવામાનમાં pipeline, જેની refractory lining પાણીથી બગડે'],
            ['Test pressure', 'સામાન્ય રીતે design pressureના 1.1–1.25 ગણું, hydrostatic કરતાં નીચું',
             'હવા ઘણી વધુ energy સંઘરે, એટલે test pressure ઘટાડાય'],
            ['સંગ્રહાયેલી energy', 'ખૂબ ઊંચી — 10 bar પર 1 m<sup>3</sup> vessel લગભગ 1 kg TNT જેટલી energy '
             'રાખે', 'એટલે કડક સાવચેતી જરૂરી'],
            ['પદ્ધતિ', 'દરેક joint પર soap કે leak-detection દ્રાવણ, pressure hold, અને gaugeની ચકાસણી',
             'leak પરપોટા તરીકે દેખાય'],
            ['સાવચેતી', 'barricade, jointની સામે કોઈ માણસ નહીં, remote gauge, અને તબક્કાવાર pressure વધારો',
             'હવાથી ભરેલા vesselનું brittle fracture એ વિસ્ફોટ છે'],
        ]),
        h4('સરખામણી'),
        table(['મુદ્દો', 'Hydrostatic test', 'Pneumatic test'], [
            ['Medium', 'પાણી (corrosion inhibitor સાથે)', 'હવા કે nitrogen'],
            ['સંગ્રહાયેલી energy', 'નીચી — પાણી લગભગ incompressible', 'ઊંચી — gas compressible છે'],
            ['Test pressure', 'design pressureના 1.5 ગણું', 'design pressureના 1.1–1.25 ગણું'],
            ['Leak પ્રત્યે sensitivity', 'સારી — ટીપું દેખાય', 'soap solution વાપરો તો નાના leak માટે ઉત્તમ'],
            ['ટેસ્ટની સલામતી', 'સલામત: ફાટે તો પાણી લીક થાય', 'ખતરનાક: ફાટે તો વિસ્ફોટ'],
            ['ટેસ્ટ પછી', 'પાણી કાઢીને સૂકવવું પડે', 'સૂકવવાની જરૂર નહીં'],
            ['ક્યારે પસંદ', 'નવા pressure vessel માટે default', 'ફક્ત જ્યાં પાણી વપરાય ન શકે, codeની પરવાનગી '
             'સાથે'],
        ]),
        h4('ઉકેલેલું ઉદાહરણ — બે ટેસ્ટમાં સંગ્રહાયેલી energy'),
        p('2 m<sup>3</sup> vessel 15 bar પર ટેસ્ટ થાય છે. Hydrostatic અને pneumatic ટેસ્ટમાં ફાટે તો નીકળતી '
          'energy આંકો; પાણીનું bulk modulus 2.2 GPa લો અને હવાને isothermal ગણો.'),
        work('Given: V = 2 m<sup>3</sup> · P = 15 bar = 1.5 × 10<sup>6</sup> Pa · '
             'K<sub>water</sub> = 2.2 × 10<sup>9</sup> Pa',
             'પાણી: સંગ્રહાયેલી energy ≈ ' + frac('P<sup>2</sup> V', '2 K') + ' = '
             + frac('(1.5 × 10<sup>6</sup>)<sup>2</sup> × 2', '2 × 2.2 × 10<sup>9</sup>')
             + ' = 1.0 × 10<sup>3</sup> J',
             'હવા (isothermal): W = P V ln(P<sub>2</sub>/P<sub>1</sub>) = 1.5 × 10<sup>6</sup> × 2 × ln 15',
             '= 3.0 × 10<sup>6</sup> × 2.71'),
        result('પાણી સાથે લગભગ 1 kJ સામે હવા સાથે 8.1 MJ — લગભગ 8000 ગણો ફરક'),
        p('Sanity check: 8 MJ એટલે લગભગ 2 kg TNTની energy — એટલે જ pneumatic ટેસ્ટ barricade સાથે થાય અને '
          'hydrostatic નહીં; આ ગણતરી જ નિયમને ન્યાય આપે છે.'),
        h4('મર્યાદાઓ'),
        bullets('Hydrostatic ટેસ્ટ vesselમાં પાણી છોડે: કાઢીને સૂકવવું પડે, નહીં તો corrosion થાય; અને જે '
                'vessel સૂકવી શકાય નહીં કે જેની refractory lining હોય એ આ રીતે ટેસ્ટ થઈ શકે નહીં.',
                'થિજતા હવામાનમાં hydrostatic ટેસ્ટ અશક્ય બને, અને stainless steel માટે પાણીમાં inhibitor '
                'નાખવો પડે (chloride stress corrosion કરે).',
                'Gas holder કે મોટા air receiver માટે pneumatic જ એક વિકલ્પ છે, પણ એની સંગ્રહાયેલી energy '
                'એને જોખમી બનાવે — ફક્ત codeની પરવાનગી, barricade અને તબક્કાવાર pressure વધારા સાથે.',
                'બંને ટેસ્ટ અંદરની lamination કે નાનો slag inclusion ન શોધે જ્યાં સુધી એ leak ન કરે — એ UT '
                'અને RTનું કામ છે, એટલે pressure ટેસ્ટ ચુસ્તતાનો પુરાવો છે, સંપૂર્ણ ઘનતાનો નહીં.'),
    ),
))
