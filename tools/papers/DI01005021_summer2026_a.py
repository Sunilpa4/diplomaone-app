"""DI01005021 Summer 2026 — Q1 and Q2 answer parts (Material Science and Technology)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from paperkit import frac, work, steps, result, table, bullets, numbered, h4, p, eq, figure
import matfigs as fig


def join(*chunks):
    return "\n".join(c for c in chunks if c)


# ---------------------------------------------------------------- Q1
Q1 = {
    'title_en': 'Q1 · Scope of material science, factors and crystalline solids',
    'title_gu': 'પ્ર.1 · Material scienceનો અવકાશ, અસર કરતાં પરિબળો અને સ્ફટિકીય ઘન',
    'cards': [],
}

Q1['cards'].append(dict(
    number='Q.1 (a)', marks=3, q='Explain Scope of material science.',
    en=join(
        h4('Definition'),
        p('<b>Material science</b> is the study of the <b>structure, properties, processing and '
          'performance</b> of materials — metals, ceramics, polymers and composites — and of how these '
          'four depend on one another. Its working rule is simple: <i>structure decides properties, '
          'properties decide performance, and processing decides structure.</i>'),
        h4('Scope'),
        bullets('<b>Selection of material:</b> choosing the cheapest material that survives the '
                'temperature, pressure, corrosion and load of a job — for example, choosing rubber-lined '
                'steel instead of stainless steel for dilute HCl storage.',
                '<b>Development of new materials:</b> alloys, superalloys, engineering plastics, '
                'composites and cermets for higher temperature and lower weight.',
                '<b>Processing control:</b> casting, rolling, forging, welding and heat treatment, where '
                'the same metal is made soft or hard by changing its structure.',
                '<b>Testing and failure analysis:</b> finding out why a part cracked or corroded, and '
                'then changing the material, the design or the process.'),
        h4('Example'),
        p('A chemical plant needs a tank for 20 % nitric acid at 60 °C. Mild steel corrodes in a month, '
          'ordinary stainless steel 304 gives a few years, and stabilised 316L gives long service. '
          'Material science tells the engineer <i>why</i> — the molybdenum in 316L builds a passive film '
          'that resists chloride and oxidising acid — and therefore which one to buy for this duty.'),
    ),
    gu=join(
        h4('વ્યાખ્યા'),
        p('<b>Material science</b> એટલે materialsની <b>structure, properties, processing અને performance</b>નો '
          'અભ્યાસ — ધાતુ, ceramic, polymer અને composite માટે — અને આ ચારે એકબીજા પર કેવી રીતે આધાર રાખે છે '
          'તેનો અભ્યાસ. એનો સીધો નિયમ છે: <i>structure properties નક્કી કરે, properties performance નક્કી કરે, '
          'અને processing structure નક્કી કરે.</i>'),
        h4('અવકાશ'),
        bullets('<b>Materialની પસંદગી:</b> કામનું temperature, pressure, corrosion અને load સહન કરે એવો સૌથી '
                'સસ્તો material પસંદ કરવો — દા.ત. ડિલ્યુટ HClના tank માટે stainless steelને બદલે rubber-lined '
                'mild steel પસંદ કરવું.',
                '<b>નવા materialનો વિકાસ:</b> ઊંચા temperature અને ઓછા weight માટે alloys, superalloys, '
                'engineering plastics, composites અને cermets.',
                '<b>Processingનું નિયંત્રણ:</b> casting, rolling, forging, welding અને heat treatment — એક જ ધાતુ '
                'structure બદલીને soft કે hard બનાવાય છે.',
                '<b>Testing અને failure analysis:</b> ભાગ કેમ તૂટ્યો કે કેમ કાટ ખાધો તે શોધવું, પછી material, '
                'design કે process બદલવો.'),
        h4('ઉદાહરણ'),
        p('Chemical plantમાં 60 °C પર 20 % nitric acid રાખવાનો tank જોઈએ. Mild steel એક મહિનામાં કાટ ખાય, '
          'સાદું stainless steel 304 થોડાં વર્ષ ટકે, અને stabilised 316L લાંબો સમય ટકે. Material science '
          'કારણ સમજાવે છે — 316Lમાંનું molybdenum chloride અને oxidising acid સામે passive film બનાવે છે — '
          'એટલે આ કામ માટે કયું લેવું તે સ્પષ્ટ થાય.'),
    ),
))

Q1['cards'].append(dict(
    number='Q.1 (b)', marks=4, q='Explain factor affecting of material properties.',
    en=join(
        h4('Definition'),
        p('<b>Material properties</b> are the measurable behaviour of a material under load, heat, '
          'electricity or a corrosive environment. They are not fixed by the name of the metal — the same '
          'steel can be soft or brittle — because they depend on the factors below.'),
        h4('Factors and how each one acts'),
        table(['Factor', 'Effect on properties', 'Example'], [
            ['<b>Composition</b>', 'alloying elements change strength, hardness, corrosion resistance',
             '0.8 % C steel is hard and brittle, 0.15 % C mild steel is soft and weldable'],
            ['<b>Bonding and crystal structure</b>', 'metallic bonding gives ductility, ionic and covalent '
             'bonding give hardness and brittleness', 'copper bends, glass shatters'],
            ['<b>Grain size</b>', 'small grains raise yield strength and toughness (Hall–Petch relation)',
             'fine-grained steel plate is tougher than coarse-grained'],
            ['<b>Defects</b>', 'vacancies and dislocations allow slip; too many make the metal brittle',
             'cold-worked wire is stronger but less ductile'],
            ['<b>Temperature</b>', 'strength falls and ductility rises on heating; metals turn brittle '
             'below the transition temperature', 'steel at 600 °C creeps under steady load'],
            ['<b>Processing and heat treatment</b>', 'quenching, annealing and cold work set the final '
             'structure', 'quenched and tempered gear is tough, annealed one is soft'],
            ['<b>Impurities</b>', 'sulphur and phosphorus make steel hot- and cold-short',
             '0.05 % S in steel causes cracking during welding'],
            ['<b>Environment</b>', 'moisture, chlorides and acids cause corrosion and hydrogen embrittlement',
             'stainless steel pits in warm chloride brine'],
        ]),
        h4('Limitation'),
        p('One factor can never be improved alone. Making a metal stronger by cold work or by adding '
          'carbon also makes it less ductile and harder to weld, so the engineer has to choose a balance '
          'for the actual duty and confirm it by a test — not by the data sheet alone.'),
    ),
    gu=join(
        h4('વ્યાખ્યા'),
        p('<b>Material properties</b> એટલે load, heat, electricity કે corrosive વાતાવરણમાં material કેવો '
          'વર્તે છે તેનું માપી શકાય એવું વર્તન. ધાતુના નામ પરથી properties નક્કી થતી નથી — એક જ steel soft કે '
          'brittle હોઈ શકે — કારણ કે નીચેનાં પરિબળો એના પર અસર કરે છે.'),
        h4('પરિબળો અને એની અસર'),
        table(['પરિબળ', 'અસર', 'ઉદાહરણ'], [
            ['<b>Composition</b>', 'alloying element strength, hardness અને corrosion resistance બદલે',
             '0.8 % C steel hard અને brittle, 0.15 % C mild steel soft અને weldable'],
            ['<b>Bonding અને crystal structure</b>', 'metallic bonding ductility આપે, ionic અને covalent '
             'bonding hardness તથા brittleness આપે', 'copper વળે, glass તૂટે'],
            ['<b>Grain size</b>', 'નાના grain yield strength અને toughness વધારે (Hall–Petch)',
             'fine-grain steel plate coarse કરતાં tough'],
            ['<b>Defects</b>', 'vacancy અને dislocation slip શક્ય બનાવે; બહુ વધે તો brittle',
             'cold-work કરેલો wire મજબૂત પણ ઓછો ductile'],
            ['<b>Temperature</b>', 'ગરમ કરવાથી strength ઘટે ને ductility વધે; ઠંડા થવાથી કેટલીક ધાતુ '
             'brittle થાય', '600 °C પર steel steady loadમાં creep કરે'],
            ['<b>Processing અને heat treatment</b>', 'quenching, annealing અને cold work final structure '
             'નક્કી કરે', 'quenched-tempered gear tough, annealed gear soft'],
            ['<b>Impurities</b>', 'sulphur અને phosphorus steelને hot-short, cold-short બનાવે',
             'steelમાં 0.05 % S welding વખતે crack કરે'],
            ['<b>Environment</b>', 'ભેજ, chloride અને acid corrosion તથા hydrogen embrittlement કરે',
             'ગરમ chloride brineમાં stainless steel pitting પામે'],
        ]),
        h4('મર્યાદા'),
        p('એક પરિબળ સુધારીને બીજું બગડે છે. Cold work કે carbon વધારીને ધાતુ મજબૂત કરીએ તો ductility ઘટે '
          'અને welding મુશ્કેલ બને. એટલે engineerએ કામ પ્રમાણે સંતુલન પસંદ કરીને testથી ખાતરી કરવી પડે — '
          'ફક્ત data sheet પર ભરોસો ન કરવો.'),
    ),
))

Q1['cards'].append(dict(
    number='Q.1 (c)', marks=7, q='Classified crystalline solid',
    en=join(
        h4('Definition and importance'),
        p('A <b>crystalline solid</b> is a solid in which the atoms, ions or molecules are arranged in a '
          'regular, repeating three-dimensional pattern called a <b>lattice</b>. Because the pattern is '
          'regular, a crystal has long-range order, a sharp melting point, flat cleavage planes and a '
          'characteristic X-ray diffraction pattern.'),
        p('Classification matters in engineering because the type of particle and the type of bond decide '
          'hardness, melting point, electrical and thermal behaviour, solubility and even the way the '
          'material can be shaped. The same classification explains why diamond cuts steel, why salt '
          'dissolves in water, and why a metal conducts while a ceramic does not.'),
        h4('Classification'),
        table(['Class', 'Particles held by', 'Typical properties', 'Examples'], [
            ['<b>Ionic</b>', 'electrostatic force between cations and anions',
             'hard and brittle, high melting point, poor conductor as solid, conducts when molten or '
             'dissolved, soluble in water', 'NaCl, CaF<sub>2</sub>, MgO, KBr'],
            ['<b>Covalent (network)</b>', 'shared electron pairs in a continuous 3-D network',
             'very hard, very high melting point, non-conducting, insoluble',
             'diamond, silicon carbide, quartz (SiO<sub>2</sub>)'],
            ['<b>Molecular</b>', 'weak van der Waals force between molecules',
             'soft, low melting point, non-conducting, volatile',
             'ice, solid CO<sub>2</sub>, iodine, sulphur'],
            ['<b>Metallic</b>', 'delocalised electron cloud (metallic bond)',
             'ductile and malleable, good conductor of heat and electricity, moderate to high melting '
             'point, lustrous', 'Cu, Fe, Al, W, Ag'],
        ]),
        figure(fig.crystal_solids(),
               'Fig. 1.1 · Four classes of crystalline solid with one example of each.'),
        h4('Working — how the classification is applied'),
        steps(('Step 1', 'Find the particles that occupy the lattice points — ions, atoms or molecules.'),
              ('Step 2', 'Find the force that holds them together: ionic, covalent, van der Waals or '
                         'metallic. This single point decides most of the properties.'),
              ('Step 3', 'From the force, predict melting point, hardness, conduction and solubility.'),
              ('Step 4', 'Check the prediction with the given data — melting point, conductivity in solid '
                         'and in melt, and solubility — and name the class.')),
        h4('Worked example'),
        p('A white solid <b>X</b> melts at 801 °C, is hard and brittle, does not conduct electricity when '
          'solid, conducts well when molten, and dissolves in water. Identify the class and the solid.'),
        work('Given: melting point 801 °C · hard and brittle · non-conductor as solid · conductor as melt · '
             'water soluble',
             'Step 1 — high melting point and brittleness suggest a strong ionic or covalent lattice.',
             'Step 2 — conduction in the melt but not in the solid is the signature of free ions: ionic.',
             'Step 3 — solubility in water confirms the ionic class, since a network covalent solid is '
             'insoluble.'),
        result('X is an <b>ionic crystalline solid</b>; the data match sodium chloride, NaCl.'),
        p('Sanity check: the accepted melting point of NaCl is 801 °C, and molten NaCl is used as an '
          'electrolyte — both agree.'),
        h4('Limitations and applications'),
        bullets('A few solids lie between the classes — graphite conducts like a metal but is covalent, so '
                'it is called a covalent solid with delocalised electrons.',
                'Real crystals are never perfect: vacancies and dislocations change the measured strength '
                'from the ideal value.',
                'The classification is still the first step in material selection — ionic and covalent '
                'ceramics for refractory and dielectric duty, metals for conduction and forming, '
                'molecular solids for low-temperature and pharmaceutical use.'),
    ),
    gu=join(
        h4('વ્યાખ્યા અને મહત્ત્વ'),
        p('<b>Crystalline solid</b> એટલે એવો ઘન જેમાં atoms, ions કે molecules <b>lattice</b> કહેવાતા નિયમિત, '
          'પુનરાવર્તિત ત્રિપરિમાણીય ગોઠવણીમાં ગોઠવાયેલા હોય. ગોઠવણી નિયમિત હોવાથી long-range order, ચોક્કસ '
          'melting point, સપાટ cleavage plane અને ખાસ X-ray diffraction pattern મળે.'),
        p('Engineeringમાં classification જરૂરી છે, કારણ કે કણનો પ્રકાર અને bondનો પ્રકાર hardness, melting point, '
          'electrical તથા thermal વર્તન, solubility અને materialને આકાર આપવાની રીત નક્કી કરે છે. એ જ '
          'classification સમજાવે છે કે diamond steel કાપે કેમ, salt પાણીમાં ઓગળે કેમ, અને metal વીજળી '
          'વહન કરે પણ ceramic ન કરે કેમ.'),
        h4('Classification'),
        table(['વર્ગ', 'કણ કઈ શક્તિથી બંધાય', 'સામાન્ય ગુણધર્મ', 'ઉદાહરણ'], [
            ['<b>Ionic</b>', 'cation અને anion વચ્ચે electrostatic force',
             'hard અને brittle, ઊંચું melting point, ઘન સ્વરૂપે નબળો conductor, ઓગળે કે દ્રાવણમાં હોય ત્યારે '
             'conductor, પાણીમાં દ્રાવ્ય', 'NaCl, CaF<sub>2</sub>, MgO, KBr'],
            ['<b>Covalent (network)</b>', 'સતત 3-D networkમાં share થયેલા electron pair',
             'ખૂબ hard, ખૂબ ઊંચું melting point, non-conducting, અદ્રાવ્ય',
             'diamond, silicon carbide, quartz (SiO<sub>2</sub>)'],
            ['<b>Molecular</b>', 'molecules વચ્ચે નબળું van der Waals force',
             'soft, નીચું melting point, non-conducting, ઝડપથી volatile',
             'ice, ઘન CO<sub>2</sub>, iodine, sulphur'],
            ['<b>Metallic</b>', 'delocalised electron cloud (metallic bond)',
             'ductile અને malleable, heat તથા electricityના સારા conductor, મધ્યમથી ઊંચું melting point, '
             'ચમકદાર', 'Cu, Fe, Al, W, Ag'],
        ]),
        figure(fig.crystal_solids(),
               'Fig. 1.1 · Crystalline solidના ચાર વર્ગ અને દરેકનું એક ઉદાહરણ.'),
        h4('કાર્ય — classification કેવી રીતે લગાડવું'),
        steps(('Step 1', 'Lattice point પર કયો કણ બેઠો છે તે જુઓ — ion, atom કે molecule.'),
              ('Step 2', 'એમને જોડતું બળ શોધો: ionic, covalent, van der Waals કે metallic. આ એક મુદ્દો મોટા '
                         'ભાગની properties નક્કી કરે.'),
              ('Step 3', 'બળ પરથી melting point, hardness, conduction અને solubility અનુમાન કરો.'),
              ('Step 4', 'આપેલા data સાથે ચકાસો — melting point, ઘન અને ઓગળેલી અવસ્થાની conductivity, '
                         'solubility — અને વર્ગનું નામ આપો.')),
        h4('ઉકેલેલું ઉદાહરણ'),
        p('સફેદ ઘન <b>X</b> 801 °C પર ઓગળે, hard અને brittle છે, ઘન સ્વરૂપે વીજળી વહન ન કરે, ઓગળે ત્યારે '
          'સારી રીતે કરે, અને પાણીમાં ઓગળે. વર્ગ અને પદાર્થ ઓળખો.'),
        work('Given: melting point 801 °C · hard અને brittle · ઘન સ્વરૂપે non-conductor · ઓગળે ત્યારે '
             'conductor · પાણીમાં દ્રાવ્ય',
             'Step 1 — ઊંચું melting point અને brittleness મજબૂત ionic કે covalent lattice દર્શાવે.',
             'Step 2 — ઓગળે ત્યારે conduction પણ ઘન સ્વરૂપે નહીં, એ મુક્ત ionsની નિશાની: ionic.',
             'Step 3 — પાણીમાં solubility ionic વર્ગની પુષ્ટિ કરે, કારણ કે network covalent ઘન અદ્રાવ્ય હોય.'),
        result('X <b>ionic crystalline solid</b> છે; data sodium chloride, NaCl સાથે મળે છે.'),
        p('Sanity check: NaClનું સ્વીકૃત melting point 801 °C છે અને ઓગળેલું NaCl electrolyte તરીકે '
          'વપરાય છે — બંને મળે છે.'),
        h4('મર્યાદાઓ અને ઉપયોગો'),
        bullets('થોડાક ઘન વર્ગો વચ્ચે રહે છે — graphite metalની જેમ વીજળી વહન કરે પણ covalent છે, એટલે એને '
                'delocalised electron વાળો covalent ઘન કહીએ.',
                'વાસ્તવિક crystal ક્યારેય પરફેક્ટ નથી: vacancy અને dislocationથી મળતી strength ideal '
                'કિંમત કરતાં બદલાય.',
                'તેમ છતાં material selectionમાં આ પહેલું પગલું છે — refractory અને dielectric કામ માટે ionic '
                'તથા covalent ceramic, conduction અને forming માટે metal, નીચા temperature અને દવા માટે '
                'molecular ઘન.'),
    ),
))

Q1['cards'].append(dict(
    number='Q.1 (c)', marks=7, tag='OR', q='Explain general characteristic of solid state.',
    en=join(
        h4('Definition'),
        p('The <b>solid state</b> is that state of matter in which the constituent particles are held so '
          'close together that they can only vibrate about fixed mean positions. A solid therefore has a '
          'definite shape and a definite volume of its own, and it does not flow to fill the container.'),
        h4('General characteristics'),
        table(['Characteristic', 'What is observed', 'Reason from structure'], [
            ['<b>Definite shape and volume</b>', 'a solid keeps its own shape; a liquid takes the shape of '
             'the vessel', 'particles are locked in position, only vibration is possible'],
            ['<b>Rigidity and mechanical strength</b>', 'a solid resists shear and can carry load',
             'strong interparticle forces hold the lattice together'],
            ['<b>High density</b>', 'solids are denser than their liquids in most cases',
             'particles are closely packed; only a small free volume'],
            ['<b>Very low compressibility</b>', 'a solid cannot be squeezed like a gas',
             'interparticle gap is already close to the particle size'],
            ['<b>Definite melting point</b>', 'crystalline solids melt sharply; amorphous solids soften '
             'over a range', 'the whole lattice breaks at one temperature'],
            ['<b>Diffusion is very slow</b>', 'two solids in contact mix only over years',
             'movement needs a vacancy and a lot of energy'],
            ['<b>Anisotropy</b>', 'refractive index, conductivity and strength differ along directions',
             'the lattice spacing differs from plane to plane'],
            ['<b>Cleavage and X-ray diffraction</b>', 'a crystal splits along flat planes and gives sharp '
             'diffraction spots', 'regular planes of atoms act as a grating for X-rays'],
        ]),
        figure(fig.solids_compare(),
               'Fig. 1.2 · Ordered crystalline lattice compared with the random amorphous arrangement.'),
        h4('Working — how the characteristics are explained'),
        steps(('Step 1', 'Start from the interparticle force: it is strong and short-range in a solid, so '
                         'each particle is trapped in a potential well.'),
              ('Step 2', 'Trapped particles can only vibrate with small amplitude, so the solid keeps its '
                         'shape and resists shear.'),
              ('Step 3', 'The amplitude of vibration grows with temperature; when it exceeds a certain '
                         'fraction of the interparticle distance the lattice collapses — that is melting.'),
              ('Step 4', 'Because the lattice is regular, the same solid behaves differently in different '
                         'directions (anisotropy) and gives a sharp diffraction pattern.')),
        h4('Worked example'),
        p('Ordinary salt has a face-centred cubic lattice with lattice constant '
          'a = 564 pm, and each unit cell holds Z = 4 NaCl formula units. Check the density from the '
          'lattice, taking M = 58.5 g/mol and N<sub>A</sub> = 6.022 × 10<sup>23</sup> mol<sup>−1</sup>.'),
        work('Given: a = 564 pm = 5.64 × 10<sup>−8</sup> cm · Z = 4 · M = 58.5 g/mol · '
             'N<sub>A</sub> = 6.022 × 10<sup>23</sup> mol<sup>−1</sup>',
             'Formula: ρ = ' + frac('Z · M', 'N<sub>A</sub> · a<sup>3</sup>'),
             'Volume of one cell: a<sup>3</sup> = (5.64 × 10<sup>−8</sup>)<sup>3</sup> = '
             '1.794 × 10<sup>−22</sup> cm<sup>3</sup>',
             'Substitute: ρ = ' + frac('4 × 58.5', '6.022 × 10<sup>23</sup> × 1.794 × 10<sup>−22</sup>'),
             'Numerator = 234 g/mol; denominator = 108.0 cm<sup>3</sup>/mol'),
        result('ρ = 2.17 g/cm<sup>3</sup> for NaCl'),
        p('Sanity check: the measured density of rock salt is 2.16 g/cm<sup>3</sup>, so the lattice model '
          'of the solid state is correct to about 0.5 %.'),
        h4('Limitations and applications'),
        bullets('The eight characteristics describe an ideal crystal; real solids contain vacancies, '
                'dislocations and grain boundaries, so measured strength is 10 to 100 times below the '
                'theoretical value.',
                'Anisotropy is strong in single crystals but averages out in a polycrystalline metal, so a '
                'cast or rolled part behaves almost the same in all directions.',
                'The solid-state picture is the basis of alloy design, semiconductor doping, ceramic '
                'refractories and the heat treatment of steel.'),
    ),
    gu=join(
        h4('વ્યાખ્યા'),
        p('<b>Solid state</b> એટલે પદાર્થની એ અવસ્થા જેમાં ઘટક કણો એટલા નજીક બંધાયેલા હોય કે તેઓ ફક્ત પોતાની '
          'નિશ્ચિત જગ્યા આસપાસ થોડું કંપન કરી શકે. એટલે ઘનને પોતાનો ચોક્કસ આકાર અને ચોક્કસ volume હોય, '
          'અને એ પાત્ર પ્રમાણે વહીને ફેલાતો નથી.'),
        h4('સામાન્ય લાક્ષણિકતાઓ'),
        table(['લાક્ષણિકતા', 'શું દેખાય છે', 'structure પરથી કારણ'], [
            ['<b>ચોક્કસ આકાર અને volume</b>', 'ઘન પોતાનો આકાર રાખે; પ્રવાહી પાત્રનો આકાર લે',
             'કણો જગ્યાએ જકડાયેલા, ફક્ત કંપન શક્ય'],
            ['<b>Rigidity અને mechanical strength</b>', 'ઘન shear સામે ટકે અને load ઉપાડે',
             'મજબૂત interparticle force latticeને જોડી રાખે'],
            ['<b>ઊંચી density</b>', 'મોટા ભાગે ઘન પોતાના પ્રવાહી કરતાં ઘનતાવાળો',
             'કણો ગીચ ગોઠવાયેલા; મુક્ત જગ્યા બહુ ઓછી'],
            ['<b>ખૂબ ઓછી compressibility</b>', 'ઘનને gasની જેમ દબાવી શકાય નહીં',
             'કણો વચ્ચેનું અંતર કણના કદ જેટલું જ છે'],
            ['<b>ચોક્કસ melting point</b>', 'crystalline ઘન ચોક્કસ તાપમાને ઓગળે; amorphous ઘન થોડી રેન્જમાં '
             'soft થાય', 'આખું lattice એક જ તાપમાને તૂટે'],
            ['<b>Diffusion ખૂબ ધીમું</b>', 'બે ઘન સ્પર્શમાં રાખો તો વર્ષોમાં ભળે',
             'ગતિ માટે vacancy અને ઘણી energy જોઈએ'],
            ['<b>Anisotropy</b>', 'refractive index, conductivity અને strength દિશા પ્રમાણે બદલાય',
             'દરેક planeમાં lattice spacing જુદું'],
            ['<b>Cleavage અને X-ray diffraction</b>', 'crystal સપાટ plane પર તૂટે અને તીવ્ર diffraction '
             'બિંદુ આપે', 'નિયમિત atom plane X-ray માટે grating જેવા કામ કરે'],
        ]),
        figure(fig.solids_compare(),
               'Fig. 1.2 · નિયમિત crystalline lattice અને અસ્તવ્યસ્ત amorphous ગોઠવણીની સરખામણી.'),
        h4('કાર્ય — લાક્ષણિકતાઓ કેવી રીતે સમજાય'),
        steps(('Step 1', 'Interparticle forceથી શરૂ કરો: ઘનમાં એ મજબૂત અને ટૂંકી રેન્જનું હોય, એટલે દરેક કણ '
                         'potential wellમાં ફસાય.'),
              ('Step 2', 'ફસાયેલો કણ ફક્ત નાની amplitudeથી કંપે, એટલે ઘન આકાર રાખે અને shear સામે ટકે.'),
              ('Step 3', 'તાપમાન વધે તો કંપનની amplitude વધે; કણો વચ્ચેના અંતરના ચોક્કસ ભાગ કરતાં વધે ત્યારે '
                         'lattice તૂટે — એ જ melting.'),
              ('Step 4', 'Lattice નિયમિત હોવાથી એક જ ઘન દિશા પ્રમાણે જુદું વર્તે (anisotropy) અને તીવ્ર '
                         'diffraction pattern આપે.')),
        h4('ઉકેલેલું ઉદાહરણ'),
        p('સાદા saltનું face-centred cubic lattice છે, lattice constant a = 564 pm, અને એક unit cellમાં '
          'Z = 4 NaCl formula unit બેસે. M = 58.5 g/mol અને N<sub>A</sub> = 6.022 × 10<sup>23</sup> '
          'mol<sup>−1</sup> લઈને latticeમાંથી density ચકાસો.'),
        work('Given: a = 564 pm = 5.64 × 10<sup>−8</sup> cm · Z = 4 · M = 58.5 g/mol · '
             'N<sub>A</sub> = 6.022 × 10<sup>23</sup> mol<sup>−1</sup>',
             'Formula: ρ = ' + frac('Z · M', 'N<sub>A</sub> · a<sup>3</sup>'),
             'એક cellનું volume: a<sup>3</sup> = (5.64 × 10<sup>−8</sup>)<sup>3</sup> = '
             '1.794 × 10<sup>−22</sup> cm<sup>3</sup>',
             'Substitution: ρ = ' + frac('4 × 58.5', '6.022 × 10<sup>23</sup> × 1.794 × 10<sup>−22</sup>'),
             'Numerator = 234 g/mol; denominator = 108.0 cm<sup>3</sup>/mol'),
        result('NaCl માટે ρ = 2.17 g/cm<sup>3</sup>'),
        p('Sanity check: rock saltની માપેલી density 2.16 g/cm<sup>3</sup> છે, એટલે solid stateનું lattice '
          'model લગભગ 0.5 % જેટલી ભૂલ સાથે સાચું છે.'),
        h4('મર્યાદાઓ અને ઉપયોગો'),
        bullets('આ આઠ લાક્ષણિકતાઓ આદર્શ crystalનું વર્ણન છે; વાસ્તવિક ઘનમાં vacancy, dislocation અને grain '
                'boundary હોય, એટલે માપેલી strength થિયરી કરતાં 10થી 100 ગણી ઓછી મળે.',
                'Anisotropy single crystalમાં સ્પષ્ટ દેખાય, પણ polycrystalline metalમાં દિશાઓની સરેરાશ થઈ '
                'જાય, એટલે cast કે rolled ભાગ બધી દિશામાં લગભગ સરખો વર્તે.',
                'આ જ ચિત્ર alloy design, semiconductor doping, ceramic refractory અને steelની heat treatmentનો '
                'પાયો છે.'),
    ),
))


# ---------------------------------------------------------------- Q2
Q2 = {
    'title_en': 'Q2 · Crystal solids, brass, lead and zinc, lattices and alloys',
    'title_gu': 'પ્ર.2 · સ્ફટિકીય ઘન, પિત્તળ, સીસું અને જસત, લેટિસ અને એલોય',
    'cards': [],
}

Q2['cards'].append(dict(
    number='Q.2 (a)', marks=3, q='Give Classification of Crystalline Solid.',
    en=join(
        p('A <b>crystalline solid</b> has its particles in a regular repeating lattice. Crystalline solids '
          'are classified into four types by the particle that sits on the lattice points and by the bond '
          'that holds it there.'),
        table(['Class', 'Bond', 'Example'], [
            ['Ionic', 'electrostatic attraction between ions', 'NaCl, CaF<sub>2</sub>'],
            ['Covalent (network)', 'shared electrons in a 3-D network', 'diamond, SiC'],
            ['Molecular', 'van der Waals force between molecules', 'ice, solid CO<sub>2</sub>'],
            ['Metallic', 'metallic bond through delocalised electrons', 'Cu, Fe, Al'],
        ]),
        p('<b>Example of use:</b> NaCl is ionic and conducts only when molten, so it is used as an '
          'electrolyte in the manufacture of caustic soda, never as a solid conductor.'),
    ),
    gu=join(
        p('<b>Crystalline solid</b>માં કણો નિયમિત પુનરાવર્તિત latticeમાં ગોઠવાયેલા હોય. Crystalline ઘનને ચાર '
          'વર્ગમાં વહેંચીએ — lattice point પર કયો કણ બેઠો છે અને એને જોડતું બળ કયું છે એના આધારે.'),
        table(['વર્ગ', 'Bond', 'ઉદાહરણ'], [
            ['Ionic', 'ions વચ્ચે electrostatic આકર્ષણ', 'NaCl, CaF<sub>2</sub>'],
            ['Covalent (network)', '3-D networkમાં share થયેલા electrons', 'diamond, SiC'],
            ['Molecular', 'molecules વચ્ચે van der Waals force', 'ice, ઘન CO<sub>2</sub>'],
            ['Metallic', 'delocalised electrons દ્વારા metallic bond', 'Cu, Fe, Al'],
        ]),
        p('<b>ઉપયોગનું ઉદાહરણ:</b> NaCl ionic છે અને ફક્ત ઓગળે ત્યારે વીજળી વહન કરે, એટલે caustic sodaની '
          'બનાવટમાં electrolyte તરીકે વપરાય, ઘન conductor તરીકે નહીં.'),
    ),
))

Q2['cards'].append(dict(
    number='Q.2 (b)', marks=4, q='Give the properties and uses of Brass.',
    en=join(
        h4('What brass is'),
        p('<b>Brass</b> is a copper–zinc alloy, normally with 60–70 % Cu and 30–40 % Zn (the 70/30 grade is '
          'called cartridge brass, the 60/40 grade is Muntz metal). Zinc makes it stronger and cheaper than '
          'pure copper and keeps most of copper\'s corrosion resistance.'),
        h4('Properties'),
        table(['Property', 'Value / behaviour', 'Why it matters'], [
            ['Colour', 'yellow to golden', 'decorative and plumbing fittings'],
            ['Density', '8.4–8.7 g/cm<sup>3</sup>', 'lighter than steel, heavier than aluminium'],
            ['Melting range', 'about 900–940 °C', 'easy to melt and cast'],
            ['Tensile strength', '300–500 MPa (cold worked)', 'strong enough for fittings and valves'],
            ['Ductility', 'excellent when cold; can be rolled to foil', 'deep drawing, bending, spinning'],
            ['Machinability', 'best of all copper alloys (free-cutting brass)', 'screws, nuts, instrument parts'],
            ['Electrical conductivity', 'about 28 % of pure copper', 'springs and current-carrying clips only'],
            ['Corrosion', 'good in fresh water and dry air; fails in ammonia and sea water',
             'not for marine or ammonia duty'],
        ]),
        h4('Uses'),
        bullets('Plumbing: taps, valves, couplings and water fittings (also because it resists bacteria).',
                'Electrical: plugs, socket pins, terminals, switch parts (easy to machine and solder).',
                'Marine and general: condenser tubes in the 70/30 + 1 % Sn grade (admiralty brass), '
                'propeller shafts, heat-exchanger tubes.',
                'Domestic and decorative: door handles, locks, musical instruments, brassware, cartridge '
                'cases and coins.'),
        h4('Limitation'),
        p('<b>Dezincification</b> is the weakness of brass. In warm, slightly acidic or chloride water the '
          'zinc is leached out and a weak, porous copper sponge is left, which then leaks. Adding about '
          '1 % tin or arsenic and avoiding stagnant warm water controls the problem — this is why the '
          'admiralty grade is specified for condenser tubes.'),
    ),
    gu=join(
        h4('Brass શું છે'),
        p('<b>Brass</b> એ copper–zinc alloy છે, સામાન્ય રીતે 60–70 % Cu અને 30–40 % Zn (70/30 ગ્રેડને '
          'cartridge brass, 60/40ને Muntz metal કહે). Zinc એને શુદ્ધ copper કરતાં મજબૂત અને સસ્તું બનાવે, '
          'અને copperની corrosion resistance મોટા ભાગે જાળવી રાખે.'),
        h4('ગુણધર્મ'),
        table(['ગુણધર્મ', 'કિંમત / વર્તન', 'કેમ જરૂરી'], [
            ['રંગ', 'પીળોથી સોનેરી', 'decorative અને plumbing fittings'],
            ['Density', '8.4–8.7 g/cm<sup>3</sup>', 'steel કરતાં હલકું, aluminium કરતાં ભારે'],
            ['Melting range', 'લગભગ 900–940 °C', 'સહેલાઈથી ઓગળે અને cast થાય'],
            ['Tensile strength', '300–500 MPa (cold work કરેલું)', 'fittings અને valve માટે પૂરતી'],
            ['Ductility', 'ઠંડું હોય ત્યારે ઉત્તમ; foil સુધી roll થાય', 'deep drawing, bending, spinning'],
            ['Machinability', 'બધા copper alloyમાં શ્રેષ્ઠ (free-cutting brass)', 'screw, nut, instrument part'],
            ['Electrical conductivity', 'શુદ્ધ copperના લગભગ 28 %', 'ફક્ત spring અને current-carrying clip'],
            ['Corrosion', 'તાજા પાણી અને સૂકી હવામાં સારું; ammonia અને sea waterમાં ફેલ',
             'marine કે ammonia કામ માટે નહીં'],
        ]),
        h4('ઉપયોગો'),
        bullets('Plumbing: નળ, valve, coupling અને પાણીના fitting (bacteria સામે ટકે એટલે પણ).',
                'Electrical: plug, socket pin, terminal, switch part (machine કરવું અને solder કરવું સહેલું).',
                'Marine અને સામાન્ય: 70/30 + 1 % Sn ગ્રેડ (admiralty brass)ના condenser tube, propeller '
                'shaft, heat-exchanger tube.',
                'ઘરેલું અને decorative: door handle, lock, musical instrument, brassware, cartridge case '
                'અને coin.'),
        h4('મર્યાદા'),
        p('<b>Dezincification</b> એ brassની મુખ્ય નબળાઈ છે. ગરમ, થોડું acidic કે chloride વાળા પાણીમાં zinc '
          'ઓગળી જાય અને નબળો, છિદ્રાળુ copper સ્પોન્જ રહી જાય, જે પછી leak થાય. લગભગ 1 % tin કે arsenic '
          'ઉમેરવાથી અને ગરમ પાણી stagnation ટાળવાથી આ થતું અટકે — એટલે condenser tube માટે admiralty ગ્રેડ '
          'લેવાય છે.'),
    ),
))

Q2['cards'].append(dict(
    number='Q.2 (c)', marks=7, q='List out the properties of lead and zinc.',
    en=join(
        h4('Why these two metals are studied together'),
        p('<b>Lead</b> (Pb) and <b>zinc</b> (Zn) are both non-ferrous, low-melting metals, but they behave '
          'almost oppositely: lead is soft, dense and highly corrosion resistant, while zinc is harder, '
          'lighter and sacrifices itself to protect steel. Both are used as protection for other metals '
          'rather than as structural metals.'),
        h4('Properties of lead'),
        table(['Property', 'Value / behaviour', 'Consequence'], [
            ['Atomic number and density', 'Z = 82, 11.34 g/cm<sup>3</sup>', 'very heavy, used for shielding'],
            ['Melting point', '327 °C', 'easy to melt and cast, but creeps in hot service'],
            ['Hardness', 'very soft, 1.5 on the Mohs scale, Vickers 4–5', 'scratches with a fingernail, '
             'cannot carry load'],
            ['Tensile strength', 'only 15–20 MPa, very low', 'never used as a structural member'],
            ['Ductility and malleability', 'excellent; rolled to sheet and extruded to pipe',
             'lead sheet, lead pipe, cable sheathing'],
            ['Corrosion resistance', 'excellent against sulphuric acid, sulphates and fresh water because '
             'an insoluble PbSO<sub>4</sub> film forms', 'chamber plant, roof flashing, acid tanks'],
            ['Electrical and thermal conductivity', 'low, about 8 % of copper', 'not a conductor; used for '
             'shielding instead'],
            ['Toxicity', 'cumulative poison; damages nerves and blood', 'banned in drinking-water pipe and '
             'in paint'],
            ['Radiation shielding', 'high atomic number and density absorb gamma rays', 'X-ray and nuclear '
             'shielding'],
        ]),
        h4('Properties of zinc'),
        table(['Property', 'Value / behaviour', 'Consequence'], [
            ['Atomic number and density', 'Z = 30, 7.14 g/cm<sup>3</sup>', 'lighter than steel'],
            ['Melting point', '420 °C', 'low, so it can be hot-dip coated on steel at 450 °C'],
            ['Hardness', '2.5 on the Mohs scale', 'harder than lead and tin, softer than copper'],
            ['Tensile strength', 'about 110–150 MPa (rolled)', 'usable for sheet and die casting'],
            ['Ductility', 'good above 100 °C; brittle when cold and in very pure form',
             'galvanising, rolled zinc sheet, dry cells'],
            ['Corrosion behaviour', 'amphoteric — dissolves in both acids and alkalis; forms a protective '
             'basic zinc carbonate film in air', 'zinc-coated steel resists rural and industrial air, not '
             'strong acids'],
            ['Electrochemical position', 'more negative than iron (E° = −0.76 V)', 'sacrificial anode; '
             'protects steel even where the coating is scratched'],
            ['Electrical conductivity', 'about 28 % of copper', 'dry cells, battery cans, roofing'],
            ['Toxicity', 'essential trace element but zinc fume causes metal-fume fever',
             'welding must be done with extraction'],
        ]),
        h4('Lead and zinc compared'),
        table(['Point', 'Lead (Pb)', 'Zinc (Zn)'], [
            ['Density', '11.34 g/cm<sup>3</sup>, very heavy', '7.14 g/cm<sup>3</sup>'],
            ['Melting point', '327 °C', '420 °C'],
            ['Hardness', 'very soft', 'moderately soft, harder than lead'],
            ['Strength', '15–20 MPa', '110–150 MPa'],
            ['Corrosion use', 'sulphuric acid and sulphate service', 'atmospheric protection of steel'],
            ['Main engineering use', 'radiation shielding, acid plant, cable sheath',
             'galvanising, die casting, dry cells, brass'],
            ['Health', 'toxic, use is restricted', 'fume toxic, safe as solid coating'],
        ]),
        h4('Working — how the properties are used in selection'),
        steps(('Step 1', 'Read the duty: is the metal carrying load, carrying current, or protecting '
                         'something else?'),
              ('Step 2', 'Lead is chosen where density and acid resistance matter and load does not — '
                         'shielding, acid-proof lining, cable sheath.'),
              ('Step 3', 'Zinc is chosen where the cheapest corrosion protection of steel is needed — hot-dip '
                         'galvanising, because zinc is anodic to iron and protects the bare edges.'),
              ('Step 4', 'Check the temperature: both metals creep and lose strength above about 100 °C, so '
                         'neither is used for pressure parts at high temperature.')),
        h4('Worked example — coating life of a galvanised sheet'),
        p('A galvanised roof sheet carries a zinc coating of 275 g/m<sup>2</sup> (that is 0.038 mm thick on '
          'each side together). The local corrosion rate of zinc is 5 g/m<sup>2</sup> per year. Estimate '
          'the coating life.'),
        work('Given: coating mass = 275 g/m<sup>2</sup> · corrosion rate = 5 g/m<sup>2</sup> per year',
             'Formula: life = ' + frac('coating mass per area', 'corrosion rate per area'),
             'Substitute: life = ' + frac('275', '5') + ' years'),
        result('Estimated coating life ≈ 55 years'),
        p('Sanity check: a rural site with 2–4 g/m<sup>2</sup> per year gives 70–130 years, and a coastal '
          'site with 10 g/m<sup>2</sup> per year gives about 27 years — matching the 20+ years normally '
          'quoted for galvanised roofing.'),
        h4('Limitations and applications'),
        bullets('Neither metal is a structural material: both creep, both have low strength, and both are '
                'attacked by strong acids (lead by nitric acid, zinc by hydrochloric acid).',
                'Lead is a cumulative poison and is now banned in drinking-water pipe, paint and petrol; '
                'zinc fume during welding gives metal-fume fever.',
                'Applications: lead in lead-acid battery plates, radiation shielding, sulphuric acid plant '
                'lining and cable sheathing; zinc in galvanising, die-cast carburettor and housing parts, '
                'dry-cell cans, rolled roofing and as the alloying element of brass and bronze.'),
    ),
    gu=join(
        h4('આ બે ધાતુ ભેગી કેમ ભણાય'),
        p('<b>Lead</b> (Pb) અને <b>zinc</b> (Zn) બંને non-ferrous, નીચા melting point વાળી ધાતુ છે, પણ '
          'લગભગ ઊલટું વર્તે: lead soft, ભારે અને ખૂબ corrosion-resistant છે, જ્યારે zinc વધુ hard, હલકું '
          'અને steelને બચાવવા માટે પોતાનું બલિદાન આપે છે. બંને બીજી ધાતુની સુરક્ષા માટે વપરાય, structural '
          'metal તરીકે નહીં.'),
        h4('Leadના ગુણધર્મ'),
        table(['ગુણધર્મ', 'કિંમત / વર્તન', 'પરિણામ'], [
            ['Atomic number અને density', 'Z = 82, 11.34 g/cm<sup>3</sup>', 'ખૂબ ભારે, shielding માટે વપરાય'],
            ['Melting point', '327 °C', 'સહેલાઈથી ઓગળે પણ ગરમીમાં creep કરે'],
            ['Hardness', 'ખૂબ soft, Mohs 1.5, Vickers 4–5', 'નાખરથી પણ ખૂટે, load ઉપાડી ન શકે'],
            ['Tensile strength', 'ફક્ત 15–20 MPa', 'structural member તરીકે કદી ન વપરાય'],
            ['Ductility અને malleability', 'ઉત્તમ; sheet સુધી roll, pipe સુધી extrude', 'lead sheet, lead '
             'pipe, cable sheathing'],
            ['Corrosion resistance', 'sulphuric acid, sulphate અને તાજા પાણી સામે ઉત્તમ, કારણ કે અદ્રાવ્ય '
             'PbSO<sub>4</sub>નો પડ થાય', 'chamber plant, roof flashing, acid tank'],
            ['Electrical અને thermal conductivity', 'નીચી, copperના લગભગ 8 %', 'conductor નહીં; shielding '
             'માટે વપરાય'],
            ['Toxicity', 'શરીરમાં જમા થતું ઝેર; નસ અને લોહીને નુકસાન', 'drinking-water pipe અને paintમાં '
             'પ્રતિબંધ'],
            ['Radiation shielding', 'ઊંચો atomic number અને density gamma ray રોકે', 'X-ray અને nuclear '
             'shielding'],
        ]),
        h4('Zincના ગુણધર્મ'),
        table(['ગુણધર્મ', 'કિંમત / વર્તન', 'પરિણામ'], [
            ['Atomic number અને density', 'Z = 30, 7.14 g/cm<sup>3</sup>', 'steel કરતાં હલકું'],
            ['Melting point', '420 °C', 'નીચું, એટલે 450 °C પર hot-dip coating થઈ શકે'],
            ['Hardness', 'Mohs 2.5', 'lead અને tin કરતાં hard, copper કરતાં soft'],
            ['Tensile strength', 'લગભગ 110–150 MPa (rolled)', 'sheet અને die casting માટે પૂરતી'],
            ['Ductility', '100 °Cથી ઉપર સારી; ઠંડું અને ખૂબ શુદ્ધ સ્વરૂપે brittle',
             'galvanising, rolled zinc sheet, dry cell'],
            ['Corrosion વર્તન', 'amphoteric — acid અને alkali બંનેમાં ઓગળે; હવામાં basic zinc carbonateનો '
             'રક્ષક પડ બને', 'zinc-coated steel શહેરી હવામાં ટકે, મજબૂત acidમાં નહીં'],
            ['Electrochemical સ્થાન', 'iron કરતાં વધુ negative (E° = −0.76 V)', 'sacrificial anode; coating '
             'ખૂટે ત્યાં પણ steelને બચાવે'],
            ['Electrical conductivity', 'copperના લગભગ 28 %', 'dry cell, battery can, roofing'],
            ['Toxicity', 'જરૂરી trace element પણ zinc fumeથી metal-fume fever થાય',
             'welding વખતે extraction જરૂરી'],
        ]),
        h4('Lead અને zincની સરખામણી'),
        table(['મુદ્દો', 'Lead (Pb)', 'Zinc (Zn)'], [
            ['Density', '11.34 g/cm<sup>3</sup>, ખૂબ ભારે', '7.14 g/cm<sup>3</sup>'],
            ['Melting point', '327 °C', '420 °C'],
            ['Hardness', 'ખૂબ soft', 'મધ્યમ soft, lead કરતાં hard'],
            ['Strength', '15–20 MPa', '110–150 MPa'],
            ['Corrosion ઉપયોગ', 'sulphuric acid અને sulphate સેવા', 'steelની atmospheric સુરક્ષા'],
            ['મુખ્ય engineering ઉપયોગ', 'radiation shielding, acid plant, cable sheath',
             'galvanising, die casting, dry cell, brass'],
            ['આરોગ્ય', 'ઝેરી, ઉપયોગ મર્યાદિત', 'fume ઝેરી, ઘન coating સુરક્ષિત'],
        ]),
        h4('કાર્ય — ગુણધર્મ પરથી પસંદગી કેવી રીતે'),
        steps(('Step 1', 'કામ વાંચો: ધાતુ load ઉપાડવાની છે, current વહન કરવાની છે, કે બીજા કંઈકને બચાવવાની '
                         'છે?'),
              ('Step 2', 'જ્યાં density અને acid resistance જરૂરી હોય પણ load નહીં — shielding, acid-proof '
                         'lining, cable sheath — ત્યાં lead પસંદ થાય.'),
              ('Step 3', 'જ્યાં steelનું સૌથી સસ્તું corrosion protection જોઈએ ત્યાં zinc પસંદ થાય — hot-dip '
                         'galvanising, કારણ કે zinc iron સામે anodic છે અને કટકાની કોર પણ બચાવે.'),
              ('Step 4', 'તાપમાન ચકાસો: 100 °Cથી ઉપર બંને creep કરે અને strength ગુમાવે, એટલે ઊંચા '
                         'તાપમાનના pressure part માટે બંને નહીં.')),
        h4('ઉકેલેલું ઉદાહરણ — galvanised sheetની coating life'),
        p('Galvanised roof sheet પર 275 g/m<sup>2</sup> zinc coating છે (બંને બાજુ મળીને 0.038 mm જાડાઈ). '
          'સ્થાનિક zinc corrosion rate 5 g/m<sup>2</sup> પ્રતિ વર્ષ છે. Coating life આંકો.'),
        work('Given: coating mass = 275 g/m<sup>2</sup> · corrosion rate = 5 g/m<sup>2</sup> પ્રતિ વર્ષ',
             'Formula: life = ' + frac('coating mass per area', 'corrosion rate per area'),
             'Substitution: life = ' + frac('275', '5') + ' વર્ષ'),
        result('અંદાજિત coating life ≈ 55 વર્ષ'),
        p('Sanity check: ગામડાના વિસ્તારમાં 2–4 g/m<sup>2</sup> પ્રતિ વર્ષ હોય તો 70–130 વર્ષ, અને દરિયા '
          'કિનારે 10 g/m<sup>2</sup> પ્રતિ વર્ષ હોય તો લગભગ 27 વર્ષ — galvanised roofing માટે સામાન્ય રીતે '
          'કહેવાતા 20+ વર્ષ સાથે મળે.'),
        h4('મર્યાદાઓ અને ઉપયોગો'),
        bullets('બંને structural material નથી: બંને creep કરે, બંનેની strength નીચી, અને મજબૂત acid સામે '
                'ટકે નહીં (lead nitric acidમાં, zinc hydrochloric acidમાં).',
                'Lead શરીરમાં જમા થતું ઝેર છે, એટલે drinking-water pipe, paint અને petrolમાં પ્રતિબંધ છે; '
                'welding વખતે zinc fumeથી metal-fume fever થાય.',
                'ઉપયોગ: lead — lead-acid battery plate, radiation shielding, sulphuric acid plantની lining '
                'અને cable sheathing; zinc — galvanising, die-cast carburettor તથા housing part, dry-cell can, '
                'rolled roofing, અને brass તથા bronzeનું alloying element.'),
    ),
))

Q2['cards'].append(dict(
    number='Q.2 (a)', marks=3, tag='OR', q='Define crystal lattice and unit cell',
    en=join(
        h4('Definitions'),
        p('<b>Crystal lattice</b> is the regular, infinite three-dimensional arrangement of points in space '
          'such that every point has exactly the same surroundings. Each point represents the position of '
          'one atom, ion or molecule of the crystal.'),
        p('<b>Unit cell</b> is the smallest repeating portion of the lattice which, when translated in the '
          'three directions by the lattice constants a, b and c, builds the whole crystal.'),
        h4('Key points'),
        bullets('The lattice is a set of <i>points</i>; the unit cell is a <i>volume</i> with edges a, b, c '
                'and angles α, β, γ.',
                'There are 14 Bravais lattices and 7 crystal systems, from which every crystal is built.',
                'The number of atoms per unit cell is 1 for simple cubic, 2 for BCC and 4 for FCC, because '
                'corner atoms are shared by 8 cells.',
                'Lattice constant is measured in picometres by X-ray diffraction; it fixes the density of '
                'the crystal.'),
        p('<b>Example:</b> sodium chloride has a face-centred cubic lattice with a = 564 pm and 4 formula '
          'units per unit cell; copper is also FCC with a = 361 pm but has 4 atoms per cell.'),
    ),
    gu=join(
        h4('વ્યાખ્યાઓ'),
        p('<b>Crystal lattice</b> એટલે અવકાશમાં બિંદુઓની એવી નિયમિત, અનંત ત્રિપરિમાણીય ગોઠવણી જેમાં દરેક '
          'બિંદુની આસપાસનું વાતાવરણ બરાબર સરખું હોય. દરેક બિંદુ crystalના એક atom, ion કે moleculeની જગ્યા '
          'દર્શાવે.'),
        p('<b>Unit cell</b> એટલે latticeનો સૌથી નાનો પુનરાવર્તિત ભાગ, જેને a, b, c lattice constantની ત્રણ '
          'દિશામાં ખસેડતાં આખું crystal બને છે.'),
        h4('મુખ્ય મુદ્દા'),
        bullets('Lattice એ <i>બિંદુઓ</i>નો સમૂહ છે; unit cell એ a, b, c કિનારા અને α, β, γ ખૂણા વાળું '
                '<i>ઘનફળ</i> છે.',
                '14 Bravais lattice અને 7 crystal system હોય છે, અને દરેક crystal એમાંથી બને છે.',
                'Unit cellમાં atomsની સંખ્યા simple cubicમાં 1, BCCમાં 2 અને FCCમાં 4, કારણ કે ખૂણાના atom '
                '8 cell વચ્ચે વહેંચાય.',
                'Lattice constant X-ray diffractionથી picometreમાં મપાય, અને એના પરથી crystalની density '
                'નક્કી થાય.'),
        p('<b>ઉદાહરણ:</b> sodium chlorideનું face-centred cubic lattice છે, a = 564 pm અને unit cell દીઠ 4 '
          'formula unit; copper પણ FCC છે, a = 361 pm, પણ cell દીઠ 4 atom.'),
    ),
))

Q2['cards'].append(dict(
    number='Q.2 (b)', marks=4, q='Write properties and uses of stainless steel.',
    en=join(
        h4('What it is'),
        p('<b>Stainless steel</b> is an iron–chromium alloy containing at least 10.5 % chromium, with '
          'nickel, molybdenum, titanium and carbon added for particular duties. The chromium forms a thin, '
          'self-healing <b>Cr<sub>2</sub>O<sub>3</sub> passive film</b>, about 2–3 nm thick, which is the '
          'whole reason the steel does not rust.'),
        h4('Properties'),
        table(['Property', 'Value / behaviour', 'Consequence'], [
            ['Corrosion resistance', 'excellent in oxidising media, water and food acids; pitting in warm '
             'chloride', 'chemical and dairy plant, no paint needed'],
            ['Strength', 'tensile 500–700 MPa; work-hardens rapidly', 'thin sheet can do the work of a '
             'thicker mild-steel sheet'],
            ['Ductility and formability', 'good in the annealed 304 grade', 'deep drawing of sinks and '
             'vessels'],
            ['Heat resistance', '316 and 310 grades scale only above 800–900 °C', 'furnace parts, '
             'heat-exchanger tubes'],
            ['Cryogenic toughness', 'austenitic grades stay tough down to −196 °C', 'LNG and liquid-oxygen '
             'service'],
            ['Hygiene', 'smooth, non-porous, easy to sterilise', 'hospital, dairy and brewery equipment'],
            ['Cost and machining', '4–8 times the price of mild steel; gummy to machine and it work-hardens',
             'used as thin cladding or only where needed'],
            ['Welding', 'weldable, but carbide precipitation in 304 causes weld decay',
             'use low-carbon 304L or stabilised 321'],
        ]),
        h4('Uses'),
        bullets('Chemical and petrochemical plant: reactors, storage tanks, pipelines, pumps, heat-exchanger '
                'tubes (316L where chlorides are present).',
                'Food, dairy and brewery: milk tanks, pasteurisers, vessels that must be cleaned in place.',
                'Household and architectural: sinks, cutlery, cookware, railings, roofing and cladding.',
                'Medical and pharmaceutical: surgical instruments, implants (316L), clean-room equipment.',
                'Power and transport: turbine blades, boiler parts, exhaust systems, railway coaches.'),
        h4('Limitation'),
        p('Stainless steel is not "corrosion proof". In warm chloride water it <b>pits</b> and in '
          'chloride plus tensile stress it fails by <b>stress-corrosion cracking</b>. The passive film also '
          'needs oxygen: in stagnant, de-aerated acid it breaks down. That is why 316L (2–3 % Mo) is '
          'specified for brine and sea-water duty instead of 304.'),
    ),
    gu=join(
        h4('શું છે'),
        p('<b>Stainless steel</b> એ iron–chromium alloy છે જેમાં ઓછામાં ઓછું 10.5 % chromium હોય, અને ખાસ '
          'કામ માટે nickel, molybdenum, titanium તથા carbon ઉમેરાય. Chromium પાતળો, જાતે રિપેર થતો '
          '<b>Cr<sub>2</sub>O<sub>3</sub> passive film</b> બનાવે — લગભગ 2–3 nm — અને steel કાટ ન ખાય એનું '
          'આખું કારણ એ જ છે.'),
        h4('ગુણધર્મ'),
        table(['ગુણધર્મ', 'કિંમત / વર્તન', 'પરિણામ'], [
            ['Corrosion resistance', 'oxidising medium, પાણી અને food acidમાં ઉત્તમ; ગરમ chlorideમાં pitting',
             'chemical અને dairy plant, paintની જરૂર નહીં'],
            ['Strength', 'tensile 500–700 MPa; ઝડપથી work-harden થાય', 'પાતળી sheet જાડી mild-steel sheetનું '
             'કામ કરે'],
            ['Ductility અને formability', 'annealed 304માં સારી', 'sink અને vesselનું deep drawing'],
            ['Heat resistance', '316 અને 310 ગ્રેડ 800–900 °Cથી ઉપર જ scale થાય', 'furnace part, '
             'heat-exchanger tube'],
            ['Cryogenic toughness', 'austenitic ગ્રેડ −196 °C સુધી tough રહે', 'LNG અને liquid oxygen સેવા'],
            ['Hygiene', 'સપાટ, છિદ્ર રહિત, sterilise કરવું સહેલું', 'hospital, dairy અને brewery equipment'],
            ['ખર્ચ અને machining', 'mild steel કરતાં 4–8 ગણું મોંઘું; machine કરવું અઘરું, work-hardens',
             'પાતળું cladding કે જ્યાં જરૂરી ત્યાં જ વપરાય'],
            ['Welding', 'weldable, પણ 304માં carbide precipitationથી weld decay',
             'low-carbon 304L કે stabilised 321 લેવાય'],
        ]),
        h4('ઉપયોગો'),
        bullets('Chemical અને petrochemical plant: reactor, storage tank, pipeline, pump, heat-exchanger '
                'tube (chloride હોય ત્યાં 316L).',
                'Food, dairy અને brewery: milk tank, pasteuriser, clean-in-place vessel.',
                'ઘરેલું અને architecture: sink, cutlery, cookware, railing, roofing અને cladding.',
                'Medical અને pharmaceutical: surgical instrument, implant (316L), clean-room equipment.',
                'Power અને transport: turbine blade, boiler part, exhaust system, railway coach.'),
        h4('મર્યાદા'),
        p('Stainless steel "corrosion proof" નથી. ગરમ chloride પાણીમાં એ <b>pitting</b> પામે અને chloride '
          'સાથે tensile stress હોય તો <b>stress-corrosion cracking</b> થાય. Passive filmને oxygen જોઈએ: '
          'stagnant, de-aerated acidમાં એ તૂટે. એટલે brine અને sea-water કામ માટે 304ને બદલે 316L '
          '(2–3 % Mo) લેવાય.'),
    ),
))

Q2['cards'].append(dict(
    number='Q.2 (c)', marks=7, q='Give the composition, property and application of Gun metal.',
    en=join(
        h4('Definition and composition'),
        p('<b>Gun metal</b> (also written gunmetal) is a copper–tin–zinc alloy — a modified bronze. It is '
          'called gun metal because it was used for cannon and gun barrels, where it had to be strong, '
          'corrosion resistant and castable.'),
        table(['Element', 'Percentage', 'Function in the alloy'], [
            ['Copper (Cu)', '86–88 %', 'base metal; gives conductivity, ductility and toughness'],
            ['Tin (Sn)', '8–10 %', 'raises strength and hardness and improves resistance to sea water'],
            ['Zinc (Zn)', '2–4 %', 'deoxidises the melt, improves fluidity and pressure tightness, and '
             'makes the alloy cheaper'],
            ['Lead (Pb)', '0–1.5 % (leaded gun metal)', 'improves machinability and bearing behaviour'],
            ['Impurities', '&lt; 1 % total (Fe, Sb, As, Ni)', 'iron above 0.2 % makes it brittle'],
        ]),
        h4('Properties'),
        table(['Property', 'Value / behaviour', 'Why it matters'], [
            ['Colour', 'reddish-golden', 'distinguishes it from yellow brass'],
            ['Density', '8.7–8.8 g/cm<sup>3</sup>', 'heavier than brass'],
            ['Melting range', 'about 900–1000 °C', 'cast in sand and permanent moulds'],
            ['Tensile strength', '220–300 MPa (sand cast)', 'adequate for valve bodies'],
            ['Hardness', '60–80 HB', 'harder than brass, resists wear'],
            ['Corrosion resistance', 'excellent in sea water, steam and dilute alkalis; superior to brass '
             'because tin stops dezincification', 'the standard marine valve alloy'],
            ['Wear resistance and bearing quality', 'low friction, good embeddability',
             'bushes and bearing shells'],
            ['Casting and pressure tightness', 'high fluidity, feeds shrinkage, no porosity',
             'sound pressure castings'],
            ['Machinability', 'good, especially the leaded grade', 'threaded fittings'],
        ]),
        h4('Applications'),
        bullets('Marine: sea-water valves, pumps, pipe fittings, propeller-shaft bearings, condenser '
                'water boxes.',
                'Steam and water services: boiler fittings, steam valves, gauge cocks, locomotive '
                'bearings (the classic use).',
                'General engineering: bearing bushes, worm wheels, gears for slow speeds, hydraulic '
                'valve bodies, statuary and medals.',
                'Electrical: switch and plug parts where corrosion matters more than conductivity.'),
        h4('Casting route — part and purpose'),
        table(['Part of the process', 'Purpose'], [
            ['Induction or crucible furnace', 'melts the charge under a cover to limit oxidation and zinc loss'],
            ['Degassing and deoxidation', 'removes hydrogen porosity so the casting is pressure tight'],
            ['Sand or permanent mould', 'gives the valve or bush shape; a metal mould gives a finer grain'],
            ['Chill or riser', 'feeds shrinkage so the thick section does not pipe'],
            ['Machining and pressure test', 'cuts the seat and thread and proves tightness at 1.5 × design '
             'pressure'],
        ]),
        h4('Worked example — charge for a 100 kg melt'),
        p('For the 87 Cu – 9 Sn – 4 Zn composition, and allowing 2 % melting loss of zinc only, find the '
          'charge.'),
        work('Given: product mass = 100 kg · Cu 87 %, Sn 9 %, Zn 4 % · zinc loss = 2 % of the zinc charged',
             'Copper needed = 0.87 × 100 = 87 kg',
             'Tin needed = 0.09 × 100 = 9 kg',
             'Zinc in the product = 0.04 × 100 = 4 kg',
             'Zinc charged = ' + frac('4', '0.98') + ' = 4.08 kg',
             'Total charge = 87 + 9 + 4.08 = 100.08 kg'),
        result('Charge per 100 kg of gun metal: Cu 87 kg, Sn 9 kg, Zn 4.08 kg'),
        p('Sanity check: the extra 0.08 kg is exactly the 2 % zinc that burns away, so the melt comes out at '
          'the required 4 % Zn.'),
        h4('Limitations'),
        bullets('Tin is expensive, so gun metal costs 2–3 times as much as brass; it is used only where its '
                'sea-water and wear resistance is essential.',
                'It cannot be used above about 250 °C because the strength falls sharply, and it is not '
                'suitable for strong acids or ammonia.',
                'Tin sweat and inverse segregation appear if the casting cools too slowly; lead above 1.5 % '
                'lowers strength and makes the alloy hot-short.'),
    ),
    gu=join(
        h4('વ્યાખ્યા અને રચના'),
        p('<b>Gun metal</b> એ copper–tin–zinc alloy છે — સુધારેલું bronze. નામ એટલે પડ્યું કે જૂના જમાનામાં '
          'તોપ અને બંદૂકની નળી માટે વપરાતું, જ્યાં મજબૂતાઈ, corrosion resistance અને casting જરૂરી હતાં.'),
        table(['ઘટક', 'ટકા', 'Alloyમાં કામ'], [
            ['Copper (Cu)', '86–88 %', 'પાયાની ધાતુ; conductivity, ductility અને toughness આપે'],
            ['Tin (Sn)', '8–10 %', 'strength અને hardness વધારે, sea water સામેની ટકાવારી સુધારે'],
            ['Zinc (Zn)', '2–4 %', 'meltને deoxidise કરે, fluidity અને pressure tightness સુધારે, અને alloy '
             'સસ્તું કરે'],
            ['Lead (Pb)', '0–1.5 % (leaded gun metal)', 'machinability અને bearing વર્તન સુધારે'],
            ['Impurities', 'કુલ &lt; 1 % (Fe, Sb, As, Ni)', 'એક ટકાથી વધુ iron એને brittle કરે'],
        ]),
        h4('ગુણધર્મ'),
        table(['ગુણધર્મ', 'કિંમત / વર્તન', 'કેમ જરૂરી'], [
            ['રંગ', 'લાલ-સોનેરી', 'પીળા brassથી અલગ પડે'],
            ['Density', '8.7–8.8 g/cm<sup>3</sup>', 'brass કરતાં ભારે'],
            ['Melting range', 'લગભગ 900–1000 °C', 'sand અને permanent mouldમાં cast થાય'],
            ['Tensile strength', '220–300 MPa (sand cast)', 'valve body માટે પૂરતી'],
            ['Hardness', '60–80 HB', 'brass કરતાં hard, ઘસારો ઝીલે'],
            ['Corrosion resistance', 'sea water, steam અને ડિલ્યુટ alkaliમાં ઉત્તમ; tin હોવાથી '
             'dezincification થતું નથી, એટલે brass કરતાં ચઢિયાતું', 'marine valveનું માનક alloy'],
            ['Wear resistance અને bearing ગુણ', 'ઓછું friction, સારી embeddability', 'bush અને bearing shell'],
            ['Casting અને pressure tightness', 'ઊંચી fluidity, shrinkage ભરે, porosity નહીં',
             'ચોક્કસ pressure casting'],
            ['Machinability', 'સારી, ખાસ કરીને leaded ગ્રેડ', 'threaded fitting'],
        ]),
        h4('ઉપયોગો'),
        bullets('Marine: sea-water valve, pump, pipe fitting, propeller-shaft bearing, condenser water box.',
                'Steam અને પાણીની સેવા: boiler fitting, steam valve, gauge cock, locomotive bearing '
                '(એનો ઉલ્લેખનીય ઉપયોગ).',
                'સામાન્ય engineering: bearing bush, worm wheel, ધીમી ઝડપનો gear, hydraulic valve body, '
                'પુતળું અને medal.',
                'Electrical: switch અને plugના ભાગ, જ્યાં conductivity કરતાં corrosion વધુ જરૂરી.'),
        h4('Castingનો ક્રમ — ભાગ અને હેતુ'),
        table(['પ્રક્રિયાનો ભાગ', 'હેતુ'], [
            ['Induction કે crucible furnace', 'charge ઓગાળે, ઓછા oxidation અને zinc loss માટે cover રાખે'],
            ['Degassing અને deoxidation', 'hydrogen porosity કાઢે જેથી casting pressure tight થાય'],
            ['Sand કે permanent mould', 'valve કે bushનો આકાર આપે; metal mould નાનું grain આપે'],
            ['Chill કે riser', 'shrinkage ભરે જેથી જાડા ભાગમાં pipe ન પડે'],
            ['Machining અને pressure test', 'seat અને thread કાપે અને 1.5 × design pressure પર tightness '
             'સાબિત કરે'],
        ]),
        h4('ઉકેલેલું ઉદાહરણ — 100 kg melt માટે charge'),
        p('87 Cu – 9 Sn – 4 Zn રચના માટે, અને ફક્ત zincમાં 2 % melting loss ધરીને, charge શોધો.'),
        work('Given: product mass = 100 kg · Cu 87 %, Sn 9 %, Zn 4 % · zinc loss = charge કરેલા zincના 2 %',
             'Copper જરૂરી = 0.87 × 100 = 87 kg',
             'Tin જરૂરી = 0.09 × 100 = 9 kg',
             'Productમાં zinc = 0.04 × 100 = 4 kg',
             'Charge કરવાનું zinc = ' + frac('4', '0.98') + ' = 4.08 kg',
             'કુલ charge = 87 + 9 + 4.08 = 100.08 kg'),
        result('100 kg gun metal માટે charge: Cu 87 kg, Sn 9 kg, Zn 4.08 kg'),
        p('Sanity check: વધારાનું 0.08 kg બરાબર એ 2 % zinc છે જે ઊડી જાય, એટલે meltમાં જરૂરી 4 % Zn '
          'રહે છે.'),
        h4('મર્યાદાઓ'),
        bullets('Tin મોંઘું છે, એટલે gun metal brass કરતાં 2–3 ગણું મોંઘું પડે; ફક્ત જ્યાં sea-water અને '
                'wear resistance જરૂરી હોય ત્યાં જ વપરાય.',
                'લગભગ 250 °Cથી ઉપર strength ઝડપથી ઘટે, એટલે ત્યાં ન વપરાય; મજબૂત acid કે ammonia માટે પણ '
                'યોગ્ય નથી.',
                'Casting ધીમે ઠંડું થાય તો tin sweat અને inverse segregation થાય; 1.5 %થી વધુ lead strength '
                'ઘટાડે અને alloyને hot-short બનાવે.'),
    ),
))
