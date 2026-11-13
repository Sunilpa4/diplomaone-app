"""DI01005021 Summer 2026 — Q3, Q4 and Q5 answer parts."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from paperkit import frac, work, steps, result, table, bullets, numbered, h4, p, eq, figure
import matfigs as fig


def join(*chunks):
    return "\n".join(c for c in chunks if c)


# ---------------------------------------------------------------- Q3
Q3 = {
    'title_en': 'Q3 · Forming, testing, rolling and forging',
    'title_gu': 'પ્ર.3 · Forming, testing, rolling અને forging',
    'cards': [],
}

Q3['cards'].append(dict(
    number='Q.3 (a)', marks=3,
    q='Define: Material forming and testing. Write the Importance of material testing.',
    en=join(
        h4('Definitions'),
        p('<b>Material forming</b> is the group of manufacturing processes in which a material is given its '
          'final shape by plastic deformation or by flow — rolling, forging, extrusion, drawing, pressing, '
          'casting and moulding — without removing chips.'),
        p('<b>Material testing</b> is the systematic measurement of the properties or the soundness of a '
          'material, either on a specimen cut from the lot (destructive) or on the finished part itself '
          '(non-destructive), so that its suitability for the intended duty can be judged.'),
        h4('Importance of material testing'),
        bullets('<b>Safety:</b> a pressure vessel or a crane hook must not fail in service; a tensile and an '
                'impact test prove the strength and toughness before use.',
                '<b>Correct selection:</b> comparing two candidate materials on measured values instead of '
                'guesswork — for example, choosing between 304 and 316L on a corrosion test.',
                '<b>Quality control:</b> confirming that each heat, casting or weld meets the specification, '
                'so a bad batch is rejected at the gate and not in the plant.',
                '<b>Design data:</b> handbooks and codes are built from test results; the engineer needs '
                'yield strength, elongation and creep data to size a part.'),
        p('<b>Example:</b> boiler plate is accepted only after a tensile test, a bend test and a Charpy '
          'impact test on a sample from the same plate, because a single brittle plate can burst a boiler.'),
    ),
    gu=join(
        h4('વ્યાખ્યાઓ'),
        p('<b>Material forming</b> એટલે એ ઉત્પાદન પ્રક્રિયાઓ જેમાં materialને plastic deformation કે flow દ્વારા '
          'આખરી આકાર આપાય — rolling, forging, extrusion, drawing, pressing, casting અને moulding — chip '
          'કાઢ્યા વગર.'),
        p('<b>Material testing</b> એટલે materialની properties કે એની soundnessનું પદ્ધતિસર માપન — lotમાંથી '
          'કાપેલા specimen પર (destructive) કે તૈયાર ભાગ પર જ (non-destructive) — જેથી એ કામ માટે યોગ્ય છે કે '
          'નહીં તે નક્કી થાય.'),
        h4('Material testingનું મહત્ત્વ'),
        bullets('<b>સલામતી:</b> pressure vessel કે crane hook સેવામાં તૂટવો ન જોઈએ; tensile અને impact test '
                'વાપરતાં પહેલાં strength અને toughness સાબિત કરે.',
                '<b>સાચી પસંદગી:</b> બે material અંદાજને બદલે માપેલા આંકડા પર સરખાવવા — દા.ત. corrosion test '
                'પરથી 304 કે 316L પસંદ કરવું.',
                '<b>Quality control:</b> દરેક heat, casting કે weld specification પૂરી કરે છે તે ચકાસવું, જેથી '
                'ખરાબ batch plantમાં નહીં પણ દરવાજે જ અટકે.',
                '<b>Design data:</b> handbook અને code testના પરિણામ પર બને; ભાગનું માપ ઠરાવવા yield strength, '
                'elongation અને creep data જોઈએ.'),
        p('<b>ઉદાહરણ:</b> Boiler plate ત્યારે જ સ્વીકારાય જ્યારે એ જ plateમાંથી કાપેલા sample પર tensile, '
          'bend અને Charpy impact test પાસ થાય — કારણ કે એક brittle plate આખું boiler ફાડી શકે.'),
    ),
))

Q3['cards'].append(dict(
    number='Q.3 (b)', marks=4, q='Explain destructive and non-destructive testing of materials.',
    en=join(
        h4('Definition'),
        p('<b>Destructive testing (DT)</b> loads the material until it yields or breaks, so the specimen is '
          'spoiled and cannot go into service. <b>Non-destructive testing (NDT)</b> inspects the part '
          'without damaging it, so every finished piece can be checked and still used.'),
        h4('Destructive tests'),
        table(['Test', 'What it measures', 'Method in one line'], [
            ['Tensile test', 'yield strength, ultimate strength, elongation, reduction in area',
             'a standard specimen is pulled in a universal testing machine until it breaks'],
            ['Hardness test', 'resistance to indentation (Brinell, Vickers, Rockwell)',
             'a ball, cone or diamond is pressed into the surface and the impression is measured'],
            ['Impact test', 'toughness and brittle-fracture tendency (Izod, Charpy)',
             'a notched bar is struck by a swinging hammer; the energy absorbed is read'],
            ['Bend test', 'ductility of plate and weld', 'the specimen is bent through a fixed angle; '
             'cracks on the outer face mean rejection'],
            ['Fatigue test', 'life under repeated stress', 'the specimen is loaded and unloaded millions of '
             'times until it fails'],
            ['Creep test', 'slow deformation at high temperature', 'a constant load is held at constant '
             'temperature and extension is plotted against time'],
        ]),
        h4('Non-destructive tests'),
        table(['Test', 'Finds', 'Method in one line'], [
            ['Visual inspection', 'surface cracks, undercut, corrosion, wrong assembly',
             'eye, magnifier, borescope and mirror'],
            ['Dye penetration (DPT)', 'surface-breaking cracks in non-porous material',
             'red dye enters the crack, developer draws it out as a bright line'],
            ['Magnetic particle (MPI)', 'surface and near-surface defects in ferromagnetic steel',
             'the part is magnetised and iron powder collects at the leakage flux'],
            ['Ultrasonic (UT)', 'internal flaws and thickness', 'a high-frequency pulse is sent in and the '
             'echo from a flaw or the back wall is timed'],
            ['Radiography (RT)', 'internal porosity, slag, incomplete penetration',
             'X-rays or gamma rays pass through and expose a film behind the part'],
            ['Hydrostatic / pneumatic', 'leaks and strength of a pressure part',
             'the part is pressurised with water or air and held; a drop in pressure or a weep fails it'],
        ]),
        figure(fig.testing_tree(),
               'Fig. 3.1 · The two families of material testing.'),
        h4('Comparison'),
        table(['Point', 'Destructive testing', 'Non-destructive testing'], [
            ['Sample', 'specimen cut from the lot, spoiled', 'the actual part, kept fit for use'],
            ['Coverage', 'sample only — the rest is assumed similar', '100 % of production is possible'],
            ['Defect found', 'properties of the material', 'discontinuities and flaws'],
            ['When used', 'acceptance of a heat, design data, research', 'in-process and final inspection, '
             'in-service checks'],
            ['Cost', 'cheap per test, but the sample is lost', 'equipment and skilled operator are costly'],
        ]),
        h4('Limitation'),
        p('Neither family is complete on its own. A tensile test proves the strength of a sample but says '
          'nothing about a crack in the particular vessel, and a dye-penetration test finds a crack but '
          'cannot measure strength. That is why a pressure vessel is released only after both a destructive '
          'test on test plates and full NDT of every weld.'),
    ),
    gu=join(
        h4('વ્યાખ્યા'),
        p('<b>Destructive testing (DT)</b>માં materialને yield કે ભંગ સુધી load કરાય, એટલે specimen બગડે અને '
          'કામમાં ન વપરાય. <b>Non-destructive testing (NDT)</b> ભાગને નુકસાન પહોંચાડ્યા વગર તપાસે, એટલે દરેક '
          'તૈયાર ભાગ ચકાસીને પણ વાપરી શકાય.'),
        h4('Destructive test'),
        table(['Test', 'શું માપે', 'એક લીટીમાં રીત'], [
            ['Tensile test', 'yield strength, ultimate strength, elongation, areaમાં ઘટાડો',
             'standard specimenને universal testing machineમાં તૂટે ત્યાં સુધી ખેંચાય'],
            ['Hardness test', 'indentation સામેનો resistance (Brinell, Vickers, Rockwell)',
             'ball, cone કે diamond સપાટીમાં દબાવીને impression મપાય'],
            ['Impact test', 'toughness અને brittle fractureની વૃત્તિ (Izod, Charpy)',
             'notched bar પર ઝૂલતો hammer પડે; શોષાયેલી energy વંચાય'],
            ['Bend test', 'plate અને weldની ductility', 'specimen ચોક્કસ કોણ સુધી વાળાય; બહારની સપાટી પર '
             'crack હોય તો reject'],
            ['Fatigue test', 'વારંવારના stress હેઠળ life', 'specimenને લાખો વખત load-unload કરાય ત્યાં સુધી '
             'તૂટે'],
            ['Creep test', 'ઊંચા તાપમાને ધીમું deformation', 'અચલ load અને તાપમાને extension સામે સમય '
             'નોંધાય'],
        ]),
        h4('Non-destructive test'),
        table(['Test', 'શું શોધે', 'એક લીટીમાં રીત'], [
            ['Visual inspection', 'સપાટીના crack, undercut, corrosion, ખોટી assembly',
             'આંખ, magnifier, borescope અને mirror'],
            ['Dye penetration (DPT)', 'non-porous materialમાં સપાટી સુધી આવતા crack',
             'લાલ dye crackમાં જાય, developer એને તેજ લીટી તરીકે બહાર લાવે'],
            ['Magnetic particle (MPI)', 'ferromagnetic steelમાં સપાટી અને સપાટી પાસેના defect',
             'ભાગને magnetise કરીને iron powder છાંટાય; leakage flux પર એકઠું થાય'],
            ['Ultrasonic (UT)', 'અંદરના flaw અને thickness', 'ઊંચી frequencyનો pulse અંદર મોકલાય અને flaw કે '
             'back wallનો echo સમય પરથી વંચાય'],
            ['Radiography (RT)', 'અંદરની porosity, slag, અધૂરી penetration',
             'X-ray કે gamma ray પસાર થઈને પાછળની film પર છાપ પાડે'],
            ['Hydrostatic / pneumatic', 'pressure ભાગમાં leak અને strength',
             'પાણી કે હવાથી pressure આપીને થોડા સમય રોકાય; pressure ઘટે કે weep થાય તો fail'],
        ]),
        figure(fig.testing_tree(),
               'Fig. 3.1 · Material testingનાં બે પરિવાર.'),
        h4('સરખામણી'),
        table(['મુદ્દો', 'Destructive testing', 'Non-destructive testing'], [
            ['Sample', 'lotમાંથી કાપેલો specimen બગડે', 'જે ભાગ તે જ, વાપરવા યોગ્ય રહે'],
            ['Coverage', 'ફક્ત sample — બાકીના સરખા ધારવા', '100 % production ચકાસી શકાય'],
            ['શું શોધે', 'materialની properties', 'discontinuity અને flaw'],
            ['ક્યારે વપરાય', 'heatની સ્વીકૃતિ, design data, સંશોધન', 'process દરમિયાન અને અંતિમ તપાસ, '
             'સેવામાં ચકાસણી'],
            ['ખર્ચ', 'test દીઠ સસ્તું, પણ sample જાય', 'machine અને નિષ્ણાત operator મોંઘા'],
        ]),
        h4('મર્યાદા'),
        p('એકલા એક પરિવારથી પૂરું ન થાય. Tensile test sampleની strength સાબિત કરે પણ એ ખાસ vesselમાંની '
          'crack વિશે કંઈ કહે નહીં, અને dye-penetration crack શોધે પણ strength માપી ન શકે. એટલે pressure '
          'vessel ત્યારે જ release થાય જ્યારે test plate પર destructive test અને દરેક weld પર NDT — બંને '
          'થઈ ગયા હોય.'),
    ),
))

Q3['cards'].append(dict(
    number='Q.3 (c)', marks=7, q='Difference between rolling and forging.',
    en=join(
        h4('Definitions'),
        p('<b>Rolling</b> is a hot or cold forming process in which the material is passed between two '
          'rotating rolls whose gap is smaller than the entering thickness, so it is reduced in section and '
          'elongated. <b>Forging</b> is a forming process in which the heated billet is squeezed between a '
          'hammer or press and an anvil (or dies), so it takes the required shape by local plastic flow.'),
        h4('Construction — the equipment, part by part'),
        table(['Part', 'Rolling mill', 'Purpose'], [
            ['Two or more rolls', 'hardened steel or chilled cast iron, rotating in opposite directions',
             'grip the slab and reduce its thickness'],
            ['Roll gap and screw-down', 'sets the exit thickness', 'fixes the reduction per pass'],
            ['Rolling stand and housing', 'carries the roll-load, which can be 1000 tonnes',
             'keeps the rolls parallel and rigid'],
            ['Reheat furnace and descaling', 'soaks the slab at 1100–1250 °C and blasts off scale',
             'keeps the load low and the surface clean'],
            ['Run-out table, cooling and coiler', 'cools and coils the strip', 'gives the final '
             'microstructure and handling shape'],
        ]),
        table(['Part', 'Forging unit', 'Purpose'], [
            ['Furnace', 'heats the billet to 1000–1200 °C', 'lowers the flow stress so it can be shaped'],
            ['Hammer (drop or power) or press', 'delivers the blow or squeeze', 'deforms the billet in one '
             'or more blows'],
            ['Upper and lower die', 'carry the impression of the part', 'give the shape and trap the flash'],
            ['Anvil and foundation', 'absorbs the blow energy', 'protects the shop floor and gives '
             'accuracy'],
            ['Trimming press', 'cuts away the flash', 'gives the finished outline'],
        ]),
        figure(fig.rolling_forging(),
               'Fig. 3.2 · Rolling through a pair of rolls compared with hammer forging on an anvil.'),
        h4('Working — step and reason'),
        steps(('Step 1 (rolling)', 'The slab is soaked in a reheat furnace. Reason: at 1200 °C the flow stress '
                                  'falls about ten times, so the rolls need far less power.'),
              ('Step 2 (rolling)', 'Scale is broken off by high-pressure water. Reason: rolled-in scale '
                                   'becomes a surface defect that cannot be removed later.'),
              ('Step 3 (rolling)', 'The slab enters the roll gap and is dragged in by friction. Reason: the '
                                   'roll surface speed exceeds the entry speed, so friction pulls the metal '
                                   'through and the section is reduced while the length grows.'),
              ('Step 4 (rolling)', 'Several passes in reversing or tandem stands bring the thickness down '
                                   'to the ordered size. Reason: one pass gives only a limited reduction '
                                   '(about 10–30 %) before the bite angle is exceeded.'),
              ('Step 1 (forging)', 'The billet is heated and placed on the lower die. Reason: hot metal '
                                   'flows without cracking and fills the impression.'),
              ('Step 2 (forging)', 'The hammer or press strikes repeatedly. Reason: each blow deforms the '
                                   'outer layer and the grain flows along the die contour, which is why a '
                                   'forged part has a continuous grain flow and is stronger across the '
                                   'section.'),
              ('Step 3 (forging)', 'The flash is trimmed and the part is heat treated. Reason: excess metal '
                                   'is needed to fill the die completely, and normalising removes the '
                                   'internal stress of the blows.')),
        h4('Difference between rolling and forging'),
        table(['Point', 'Rolling', 'Forging'], [
            ['Definition', 'metal is passed between rotating rolls to reduce section',
             'hot metal is squeezed by hammer or press between dies'],
            ['Nature of process', 'continuous, steady-state', 'discrete, blow by blow'],
            ['Product', 'long sections: plate, sheet, strip, bar, rail, rod',
             'individual parts: crankshaft, connecting rod, gear blank, lever'],
            ['Tooling cost', 'very high mill cost, no die per shape', 'die cost per part, but the die can '
             'make thousands of pieces'],
            ['Grain flow', 'grain elongated in the rolling direction, so properties are directional',
             'grain follows the shape of the part, so it is stronger in the direction of service load'],
            ['Surface and tolerance', 'excellent surface, tight thickness tolerance over the length',
             'good but needs machining allowance'],
            ['Strength obtained', 'improves strength along the rolling direction only',
             'best combination of strength and toughness, especially for fatigue'],
            ['Size range', 'from foil to 200 mm plate, tonnes of length', 'a few grams to a 300-tonne '
             'turbine-rotor forging'],
            ['Defect', 'laminations and rolled-in scale', 'flash, laps and die wear'],
            ['Typical use', 'structural plate, sheet for vessels and car bodies, rails',
             'highly stressed parts: shafts, crankshafts, hooks, landing gear'],
        ]),
        h4('Worked example — reduction in one rolling pass'),
        p('A 200 mm thick slab is rolled to 160 mm in one pass and the width stays constant at 1500 mm. Find '
          'the percentage reduction and the exit length if the entry length is taken as 1 m for a small '
          'element.'),
        work('Given: h<sub>1</sub> = 200 mm · h<sub>2</sub> = 160 mm · width constant (b<sub>1</sub> = '
             'b<sub>2</sub>) · L<sub>1</sub> = 1 m',
             'Percentage reduction = ' + frac('h<sub>1</sub> − h<sub>2</sub>', 'h<sub>1</sub>') + ' × 100',
             'Substitute: ' + frac('200 − 160', '200') + ' × 100 = ' + frac('40', '200') + ' × 100 = 20 %',
             'Volume constancy: h<sub>1</sub> · L<sub>1</sub> = h<sub>2</sub> · L<sub>2</sub>',
             'L<sub>2</sub> = ' + frac('h<sub>1</sub> · L<sub>1</sub>', 'h<sub>2</sub>') + ' = '
             + frac('200 × 1', '160') + ' = 1.25 m'),
        result('Reduction = 20 %; the material lengthens from 1.00 m to 1.25 m'),
        p('Sanity check: a 20 % reduction lengthens the strip by exactly 1/0.8 = 1.25, and no metal is lost '
          'because the width was kept constant — correct.'),
        h4('Limitations'),
        bullets('Rolling cannot make a part with a closed shape; it gives a uniform section only.',
                'Forging needs a die per component, so it is economical only in reasonable quantity.',
                'Both are hot processes: scale, decarburisation and grain growth can spoil the surface and '
                'the properties unless cooling is controlled.',
                'Rolled sheet is anisotropic, and forged parts carry residual stress, so heat treatment '
                'follows both processes.'),
    ),
    gu=join(
        h4('વ્યાખ્યાઓ'),
        p('<b>Rolling</b> એ ગરમ કે ઠંડી forming પ્રક્રિયા છે જેમાં materialને બે ફરતા roll વચ્ચે પસાર કરાય; rollનું '
          'અંતર આવતી થિકનેસ કરતાં ઓછું હોય, એટલે section ઘટે અને લંબાઈ વધે. <b>Forging</b>માં ગરમ billetને '
          'hammer કે press અને anvil (કે die) વચ્ચે દબાવાય, એટલે સ્થાનિક plastic flowથી જરૂરી આકાર મળે.'),
        h4('રચના — સાધનના ભાગ અને હેતુ'),
        table(['ભાગ', 'Rolling mill', 'હેતુ'], [
            ['બે કે વધુ rolls', 'hardened steel કે chilled cast iron, ઊલટી દિશામાં ફરે',
             'slab પકડે અને થિકનેસ ઘટાડે'],
            ['Roll gap અને screw-down', 'બહાર નીકળતી થિકનેસ ઠરાવે', 'એક passનું reduction નક્કી કરે'],
            ['Rolling stand અને housing', 'roll-load ઉપાડે, જે 1000 tonne સુધી હોય',
             'rolls સમાંતર અને rigid રાખે'],
            ['Reheat furnace અને descaling', 'slabને 1100–1250 °C પર soak કરે અને scale ઉડાડે',
             'load ઓછો અને સપાટી સાફ રાખે'],
            ['Run-out table, cooling અને coiler', 'strip ઠંડી કરે અને coil કરે', 'આખરી microstructure અને '
             'સંભાળવા યોગ્ય આકાર આપે'],
        ]),
        table(['ભાગ', 'Forging unit', 'હેતુ'], [
            ['Furnace', 'billetને 1000–1200 °C સુધી ગરમ કરે', 'flow stress ઘટાડે જેથી આકાર આપી શકાય'],
            ['Hammer (drop કે power) કે press', 'blow કે squeeze આપે', 'એક કે વધુ ફટકામાં billetને ઘડે'],
            ['Upper અને lower die', 'ભાગનું impression રાખે', 'આકાર આપે અને flash પકડે'],
            ['Anvil અને foundation', 'blowની energy શોષે', 'જમીન બચાવે અને accuracy આપે'],
            ['Trimming press', 'flash કાપે', 'આખરી outline આપે'],
        ]),
        figure(fig.rolling_forging(),
               'Fig. 3.2 · બે roll વચ્ચે rolling અને anvil પર hammer forgingની સરખામણી.'),
        h4('કાર્ય — સ્ટેપ અને કારણ'),
        steps(('Step 1 (rolling)', 'Slabને reheat furnaceમાં soak કરાય. કારણ: 1200 °C પર flow stress લગભગ '
                                    'દસ ગણું ઘટે, એટલે rollને ઘણું ઓછું power જોઈએ.'),
              ('Step 2 (rolling)', 'ઊંચા pressureના પાણીથી scale તોડી કાઢાય. કારણ: અંદર દબાયેલું scale પછી '
                                   'કાઢી ન શકાય એવો સપાટીનો defect બને.'),
              ('Step 3 (rolling)', 'Slab roll gapમાં દાખલ થાય અને friction એને અંદર ખેંચે. કારણ: rollની '
                                   'સપાટીની ઝડપ આવતા metal કરતાં વધુ હોય, એટલે friction metalને પસાર કરાવે '
                                   'અને section ઘટે, લંબાઈ વધે.'),
              ('Step 4 (rolling)', 'Reversing કે tandem standમાં ઘણા pass થિકનેસ ઓર્ડરના માપ સુધી લાવે. '
                                   'કારણ: એક passમાં બite angleની મર્યાદા સુધી લગભગ 10–30 % જ reduction '
                                   'શક્ય છે.'),
              ('Step 1 (forging)', 'Billet ગરમ કરીને lower die પર મુકાય. કારણ: ગરમ metal crack વગર વહે અને '
                                    'impression ભરે.'),
              ('Step 2 (forging)', 'Hammer કે press વારંવાર ફટકા મારે. કારણ: દરેક ફટકો બહારના સ્તરને ઘડે અને '
                                    'grain dieના આકાર પ્રમાણે વહે, એટલે forged ભાગનો grain flow સતત રહે અને '
                                    'section આખામાં strength વધે.'),
              ('Step 3 (forging)', 'Flash કાપાય અને ભાગ heat treat થાય. કારણ: die પૂરેપૂરી ભરાય એટલા માટે '
                                    'વધારાની ધાતુ જરૂરી છે, અને normalising ફટકાનો internal stress કાઢે.')),
        h4('Rolling અને forging વચ્ચેનો ફરક'),
        table(['મુદ્દો', 'Rolling', 'Forging'], [
            ['વ્યાખ્યા', 'ફરતા roll વચ્ચે metal પસાર કરીને section ઘટાડવું',
             'ગરમ metalને hammer કે press વડે die વચ્ચે દબાવવું'],
            ['પ્રક્રિયાનો પ્રકાર', 'સતત, steady-state', 'એક-એક ફટકે, discrete'],
            ['Product', 'લાંબા section: plate, sheet, strip, bar, rail, rod',
             'એક-એક ભાગ: crankshaft, connecting rod, gear blank, lever'],
            ['Tooling ખર્ચ', 'mill ખૂબ મોંઘું, દરેક આકાર માટે die નહીં', 'દરેક ભાગ માટે die, પણ હજારો '
             'ભાગ બને'],
            ['Grain flow', 'grain rollingની દિશામાં લાંબા, એટલે properties દિશા પ્રમાણે',
             'grain ભાગના આકાર પ્રમાણે, એટલે સેવાના loadની દિશામાં મજબૂત'],
            ['સપાટી અને tolerance', 'ઉત્તમ સપાટી, લંબાઈ આખી સમાન થિકનેસ', 'સારું પણ machining allowance '
             'જોઈએ'],
            ['મળતી strength', 'ફક્ત rollingની દિશામાં strength વધે',
             'strength અને toughnessનું શ્રેષ્ઠ સંતુલન, ખાસ fatigue માટે'],
            ['કદની રેન્જ', 'foilથી 200 mm plate સુધી, ટન લંબાઈ', 'થોડા ગ્રામથી 300 ટન turbine rotor forging સુધી'],
            ['Defect', 'lamination અને અંદર દબાયેલું scale', 'flash, lap અને die wear'],
            ['સામાન્ય ઉપયોગ', 'structural plate, vessel અને car bodyની sheet, rail',
             'ખૂબ ભારે load વાળા ભાગ: shaft, crankshaft, hook, landing gear'],
        ]),
        h4('ઉકેલેલું ઉદાહરણ — એક rolling passમાં reduction'),
        p('200 mm જાડું slab એક passમાં 160 mm થાય અને પહોળાઈ 1500 mm જેટલી અચલ રહે. ટકાવારી reduction '
          'અને નાના elementની લંબાઈ 1 m લઈને બહાર નીકળતી લંબાઈ શોધો.'),
        work('Given: h<sub>1</sub> = 200 mm · h<sub>2</sub> = 160 mm · પહોળાઈ અચલ (b<sub>1</sub> = '
             'b<sub>2</sub>) · L<sub>1</sub> = 1 m',
             'ટકાવારી reduction = ' + frac('h<sub>1</sub> − h<sub>2</sub>', 'h<sub>1</sub>') + ' × 100',
             'Substitution: ' + frac('200 − 160', '200') + ' × 100 = ' + frac('40', '200') + ' × 100 = 20 %',
             'Volume અચલ: h<sub>1</sub> · L<sub>1</sub> = h<sub>2</sub> · L<sub>2</sub>',
             'L<sub>2</sub> = ' + frac('h<sub>1</sub> · L<sub>1</sub>', 'h<sub>2</sub>') + ' = '
             + frac('200 × 1', '160') + ' = 1.25 m'),
        result('Reduction = 20 %; material 1.00 m થી 1.25 m સુધી લાંબું થાય'),
        p('Sanity check: 20 % reduction એટલે લંબાઈ બરાબર 1/0.8 = 1.25 ગણી થાય, અને પહોળાઈ અચલ હોવાથી '
          'ધાતુ ખોવાતી નથી — સાચું છે.'),
        h4('મર્યાદાઓ'),
        bullets('Rollingથી બંધ આકારનો ભાગ ન બને; એ ફક્ત સરખા section આપે.',
                'Forgingમાં દરેક ભાગ માટે die જોઈએ, એટલે પૂરતા જથ્થામાં જ આર્થિક બને.',
                'બંને ગરમ પ્રક્રિયા છે: scale, decarburisation અને grain growth સપાટી તથા properties બગાડે, '
                'જો cooling નિયંત્રિત ન હોય.',
                'Rolled sheet anisotropic હોય અને forged ભાગમાં residual stress રહે, એટલે બંને પછી heat '
                'treatment જરૂરી.'),
    ),
))

Q3['cards'].append(dict(
    number='Q.3 (a)', marks=3, tag='OR', q='Importance of material testing.',
    en=join(
        p('<b>Material testing</b> is the measurement of the properties and soundness of a material before '
          'or during service. Its importance can be stated in four points.'),
        bullets('<b>Safety and reliability:</b> the strength and toughness measured in a tensile and an '
                'impact test decide whether a pressure vessel, a lifting hook or a boiler drum can carry '
                'its load without brittle failure.',
                '<b>Right selection at lowest cost:</b> comparing measured properties allows the cheapest '
                'material that meets the duty to be chosen, instead of over-specifying stainless steel '
                'where mild steel with a coating will do.',
                '<b>Quality control and rejection of bad batches:</b> chemical analysis, tensile test and '
                'NDT of welds catch a wrong heat or a bad casting in the shop, before it becomes a '
                'failure in the plant.',
                '<b>Design data and standardisation:</b> codes and handbooks are written from test results, '
                'so a designer needs yield strength, elongation, creep and fatigue data to fix dimensions.'),
        p('<b>Example:</b> a boiler plate is released only after a tensile, a bend and a Charpy test on a '
          'sample from the same plate — one brittle plate can burst a whole boiler, so the test is a legal '
          'requirement, not a formality.'),
    ),
    gu=join(
        p('<b>Material testing</b> એટલે સેવામાં વાપરતાં પહેલાં કે દરમિયાન materialની properties અને soundnessનું '
          'માપન. એનું મહત્ત્વ ચાર મુદ્દામાં કહી શકાય.'),
        bullets('<b>સલામતી અને ભરોસાપાત્રતા:</b> tensile અને impact testમાં મપાયેલી strength તથા toughness નક્કી '
                'કરે કે pressure vessel, lifting hook કે boiler drum brittle રીતે તૂટ્યા વગર load ઉપાડી '
                'શકશે કે નહીં.',
                '<b>ઓછા ખર્ચે સાચી પસંદગી:</b> માપેલી properties સરખાવવાથી કામ પૂરું કરતો સૌથી સસ્તો material '
                'પસંદ કરી શકાય; જ્યાં coating વાળું mild steel ચાલે ત્યાં stainless steel ન લેવાય.',
                '<b>Quality control અને ખરાબ batchનો અસ્વીકાર:</b> chemical analysis, tensile test અને weldનું '
                'NDT ખોટો heat કે ખરાબ casting દુકાનમાં જ પકડે, પછી plantમાં failure ન થાય.',
                '<b>Design data અને standardisation:</b> code અને handbook testના પરિણામ પર લખાય છે, એટલે '
                'designerને માપ ઠરાવવા yield strength, elongation, creep અને fatigue data જોઈએ.'),
        p('<b>ઉદાહરણ:</b> Boiler plate ત્યારે જ છૂટે જ્યારે એ જ plateમાંથી કાપેલા sample પર tensile, bend અને '
          'Charpy test થાય — એક brittle plate આખું boiler ફાડી શકે, એટલે આ test કાયદેસરની જરૂરિયાત છે, '
          'ફોર્માલિટી નહીં.'),
    ),
))

Q3['cards'].append(dict(
    number='Q.3 (b)', marks=4,
    q='Explain principle, procedure and applications. Dye Penetration Testing.',
    en=join(
        h4('Principle'),
        p('The <b>dye penetration test (DPT)</b> works on <b>capillary action</b>. A coloured liquid of low '
          'surface tension and high wetting power is applied to a clean surface. If a crack reaches the '
          'surface, the dye is drawn into it by capillary force. After the excess dye is removed from the '
          'surface, a white powder called the <b>developer</b> is applied; it draws the trapped dye back out '
          'and the crack shows as a bright red line against the white background.'),
        figure(fig.dye_penetrant(),
               'Fig. 3.3 · Six steps of DPT and how the developer reveals a surface crack.'),
        h4('Procedure — step and reason'),
        steps(('Step 1 · Clean', 'The surface is degreased, dried and brushed. Reason: oil, paint or water '
                                 'blocks the mouth of the crack so the dye cannot enter.'),
              ('Step 2 · Apply penetrant', 'Red dye is sprayed or brushed on and left for the dwell time, '
                                           'usually 10–30 minutes. Reason: capillary action needs time to '
                                           'fill a narrow crack.'),
              ('Step 3 · Remove excess', 'The surface is wiped and washed with water or cleaner. Reason: '
                                         'only the dye outside the crack is removed, so the indication '
                                         'comes from the crack and not from the surface.'),
              ('Step 4 · Apply developer', 'A thin white powder layer is sprayed on. Reason: it acts as a '
                                           'blotter and pulls the dye out, and the white background gives '
                                           'contrast.'),
              ('Step 5 · Inspect and record', 'The surface is examined under good light within 10–30 '
                                              'minutes. Reason: an indication fades as the dye spreads, '
                                              'so it must be read at once.'),
              ('Step 6 · Clean and evaluate', 'The part is cleaned and the indication is judged against '
                                              'the acceptance standard. Reason: a long or branched line is '
                                              'a reject, a single small spot may be accepted.')),
        h4('Applications'),
        bullets('Welds in steel, stainless steel and aluminium — especially where MPI cannot be used, '
                'because DPT works on any non-porous material.',
                'Castings and forgings: surface cracks, laps, cold shuts and grinding cracks.',
                'Non-magnetic materials such as austenitic stainless steel, aluminium, titanium, ceramics '
                'and plastics.',
                'In-service inspection: turbine blades, compressor discs, aircraft parts, pressure-vessel '
                'nozzle welds.'),
        h4('Limitations'),
        p('DPT finds only defects that are <b>open to the surface</b> — it cannot see porosity or lack of '
          'fusion inside a weld. The surface must be smooth and non-porous, the dye and developer are '
          'consumables, and the test is slower than visual inspection. That is why ultrasonic or '
          'radiography is used for internal flaws and DPT for the surface.'),
    ),
    gu=join(
        h4('સિદ્ધાંત'),
        p('<b>Dye penetration test (DPT)</b> <b>capillary action</b> પર કામ કરે. ઓછું surface tension અને '
          'ઊંચી wetting power વાળું રંગીન પ્રવાહી સાફ સપાટી પર લગાડાય. Crack સપાટી સુધી આવતો હોય તો dye '
          'capillary forceથી એમાં ખેંચાય. વધારાનો dye સપાટી પરથી કાઢ્યા પછી સફેદ પાવડર '
          '<b>developer</b> લગાડાય; એ અંદર ફસાયેલો dye બહાર ખેંચે અને crack સફેદ પાર્શ્વભૂમિ પર તેજ લાલ '
          'લીટી તરીકે દેખાય.'),
        figure(fig.dye_penetrant(),
               'Fig. 3.3 · DPTનાં છ પગલાં અને developer કેવી રીતે સપાટીનો crack દેખાડે.'),
        h4('પ્રક્રિયા — સ્ટેપ અને કારણ'),
        steps(('Step 1 · સફાઈ', 'સપાટીને degrease, સૂકવી અને brush કરાય. કારણ: oil, paint કે પાણી crackનું '
                                'મુખ બંધ કરે, એટલે dye અંદર ન જાય.'),
              ('Step 2 · Penetrant લગાડવો', 'લાલ dye spray કે brush કરીને dwell time — સામાન્ય રીતે 10–30 '
                                            'મિનિટ — રોકાય. કારણ: capillary actionને પાતળો crack ભરતાં '
                                            'સમય જોઈએ.'),
              ('Step 3 · વધારાનો dye કાઢવો', 'સપાટી wipe કરીને પાણી કે cleanerથી ધોવાય. કારણ: ફક્ત બહારનો '
                                             'dye જાય, indication crackમાંથી આવે, સપાટી પરથી નહીં.'),
              ('Step 4 · Developer લગાડવો', 'પાતળો સફેદ પાવડર છાંટાય. કારણ: એ blotterની જેમ dye બહાર ખેંચે '
                                           'અને સફેદ પાર્શ્વભૂમિ contrast આપે.'),
              ('Step 5 · તપાસ અને નોંધ', 'સારા પ્રકાશમાં 10–30 મિનિટમાં સપાટી તપાસાય. કારણ: dye ફેલાતો જાય '
                                         'તો indication ઝાંખું પડે, એટલે તરત વાંચવું જોઈએ.'),
              ('Step 6 · સફાઈ અને નિર્ણય', 'ભાગ સાફ કરીને indication acceptance standard સામે તપાસાય. કારણ: '
                                            'લાંબી કે શાખા પડેલી લીટી reject, એક નાનું ટપકું સ્વીકાર્ય '
                                            'હોઈ શકે.')),
        h4('ઉપયોગો'),
        bullets('Steel, stainless steel અને aluminiumના weld — ખાસ કરીને જ્યાં MPI ન ચાલે, કારણ કે DPT કોઈ પણ '
                'non-porous material પર કામ કરે.',
                'Casting અને forging: સપાટીના crack, lap, cold shut અને grinding crack.',
                'Non-magnetic material જેવા કે austenitic stainless steel, aluminium, titanium, ceramic અને '
                'plastic.',
                'સેવામાં તપાસ: turbine blade, compressor disc, aircraft part, pressure-vessel nozzle weld.'),
        h4('મર્યાદાઓ'),
        p('DPT ફક્ત એ defect શોધે જે <b>સપાટી સુધી ખુલ્લા</b> હોય — weldની અંદરની porosity કે અધૂરી fusion '
          'એ જોઈ ન શકે. સપાટી સપાટ અને છિદ્ર રહિત હોવી જોઈએ, dye અને developer વપરાઈ જાય છે, અને visual '
          'inspection કરતાં ધીમું છે. એટલે અંદરના flaw માટે ultrasonic કે radiography અને સપાટી માટે DPT '
          'વપરાય.'),
    ),
))

Q3['cards'].append(dict(
    number='Q.3 (c)', marks=7,
    q='Explain principle, procedure and applications Hydrostatic Testing.',
    en=join(
        h4('Principle'),
        p('The <b>hydrostatic test</b> proves the strength and tightness of a pressure part by filling it '
          'with water and raising the pressure above the design pressure, usually to <b>1.5 times</b> the '
          'design pressure, holding it for a fixed time and looking for a leak, a permanent bulge or a '
          'pressure drop.'),
        p('Water is used rather than air because water is almost <b>incompressible</b>. The energy stored in '
          'a water-filled vessel at test pressure is very small, so if it bursts the release is a small '
          'splash; a compressed-air test at the same pressure stores enough energy to destroy the shop. '
          'This is why the hydro test is the standard strength test and the pneumatic test is done only '
          'when water cannot be used.'),
        figure(fig.hydrostatic(),
               'Fig. 3.4 · Hydrostatic test: water-filled vessel, pressure gauge and level glass.'),
        h4('Construction of the test set-up — part and purpose'),
        table(['Part', 'Purpose'], [
            ['Test vessel itself', 'the item to be proved; all openings blanked with proper blind flanges'],
            ['Filling line and vent', 'fill completely and let all air escape; air left inside makes the '
             'test unsafe and gives a false pressure drop'],
            ['Hydro-test pump (hand or motor)', 'raises the pressure slowly and steadily to the test value'],
            ['Calibrated pressure gauge', 'reads the test pressure; the gauge range is about 2 times the '
             'test pressure'],
            ['Level glass or gauge glass', 'shows that the vessel is full and that the pressure is held by '
             'water, not by trapped air'],
            ['Relief valve and drain', 'protects against over-pressure and empties the vessel after the '
             'test'],
            ['Safety barricade', 'keeps people away during the hold, since the test is a proof of strength'],
        ]),
        h4('Procedure — step and reason'),
        steps(('Step 1 · Prepare', 'All welds are finished and NDT is complete, the vessel is clean, and the '
                                  'safety valves are removed and their openings blanked. Reason: the test '
                                  'comes after fabrication, and a safety valve would open before the test '
                                  'pressure is reached.'),
              ('Step 2 · Fill and vent', 'Water is filled from the bottom while the highest vent stays open '
                                        'until water overflows. Reason: any trapped air would compress '
                                        'under pressure and store energy, and would also make the gauge '
                                        'reading misleading.'),
              ('Step 3 · Pressurise slowly', 'The pump raises the pressure in steps, up to 1.5 × design '
                                            'pressure. Reason: a slow, stepwise rise lets the metal yield '
                                            'gradually and lets the operator watch every joint.'),
              ('Step 4 · Hold', 'The pressure is held for 30 minutes (10 minutes is the usual minimum in '
                                'codes). Reason: a leak or a yielding part shows itself as a drop in '
                                'pressure or a visible weep during the hold.'),
              ('Step 5 · Inspect', 'Every welded joint, nozzle and flange is examined for weeping. Reason: '
                                   'a leak at the test pressure proves a defect that normal working '
                                   'pressure would not reveal.'),
              ('Step 6 · Reduce and check', 'The pressure is brought down to the design pressure and held '
                                            'while the permanent set is checked across a marked diameter. '
                                            'Reason: a permanent (non-recoverable) bulge means the metal '
                                            'yielded, so the vessel is rejected even without a leak.'),
              ('Step 7 · Drain, dry and record', 'Water is drained, the vessel is dried and a test '
                                                 'certificate is signed. Reason: wet carbon steel rusts, '
                                                 'and the certificate is the legal proof of the test.')),
        h4('Applications'),
        bullets('New pressure vessels, boilers, heat exchangers, reactors and storage tanks after '
                'fabrication — this is a code requirement before commissioning.',
                'Pipelines: cross-country and plant piping after laying, and after any hot work on the line.',
                'Gas cylinders and LPG cylinders, every cylinder at a fixed interval (typically 5 years).',
                'Valves, pumps and castings: body-pressure test before dispatch.',
                'After repair or alteration of any pressure part, and periodically in service as a '
                'proof test.'),
        h4('Worked example'),
        p('A reactor is designed for 10 bar working pressure. Find the hydro test pressure, and the '
          'additional water needed to pressurise it if the vessel volume is 5 m<sup>3</sup> and water '
          'compresses by 0.05 % per 10 bar.'),
        work('Given: design pressure P<sub>d</sub> = 10 bar · test factor = 1.5 · volume V = 5 m<sup>3</sup> '
             '· compressibility = 0.05 % per 10 bar',
             'Test pressure P<sub>t</sub> = 1.5 × P<sub>d</sub> = 1.5 × 10',
             'P<sub>t</sub> = 15 bar',
             'Fractional compression at 15 bar = 0.05 % × ' + frac('15', '10') + ' = 0.075 %',
             'Extra water = 0.00075 × 5 m<sup>3</sup> = 0.00375 m<sup>3</sup>'),
        result('Test pressure = 15 bar; extra water ≈ 3.75 litres'),
        p('Sanity check: 3.75 litres is a bucketful for a 5000 litre vessel — this is exactly why water is '
          'safe: almost no energy is stored, so a failure is a splash and not a blast.'),
        h4('Limitations'),
        bullets('The vessel must be dried after the test; residual water causes rust and, in stainless '
                'steel, chloride pitting.',
                'It cannot be used where water would damage the internals (catalyst, refractory lining, '
                'dry product) — a pneumatic test is used there with strict safety distance.',
                'It proves strength and tightness only; it does not replace NDT of the welds, because a '
                'defect may close up under pressure and leak only later in service.',
                'A very high proof pressure can itself damage the vessel by local yielding, so the factor '
                'is limited by code and the metal temperature must be above its transition temperature.'),
    ),
    gu=join(
        h4('સિદ્ધાંત'),
        p('<b>Hydrostatic test</b> pressure ભાગની strength અને tightness સાબિત કરે: ભાગને પાણીથી ભરીને '
          'design pressureથી ઉપર — સામાન્ય રીતે <b>1.5 ગણા</b> સુધી — pressure વધારાય, થોડા સમય રોકાય, અને '
          'leak, કાયમી bulge કે pressure ઘટવાનું જોવાય.'),
        p('હવાને બદલે પાણી વપરાય, કારણ કે પાણી લગભગ <b>incompressible</b> છે. Test pressure પર પાણીથી ભરેલા '
          'vesselમાં સંગ્રહાયેલી energy ખૂબ ઓછી હોય, એટલે ફાટે તો ફક્ત છાંટો ઊડે; એ જ pressure પર હવાથી '
          'કરેલો test આખી દુકાન ઉડાડી શકે. એટલે hydro test માનક strength test છે અને જ્યાં પાણી વાપરી ન '
          'શકાય ત્યાં જ pneumatic test થાય.'),
        figure(fig.hydrostatic(),
               'Fig. 3.4 · Hydrostatic test: પાણીથી ભરેલું vessel, pressure gauge અને level glass.'),
        h4('Test set-upની રચના — ભાગ અને હેતુ'),
        table(['ભાગ', 'હેતુ'], [
            ['Test vessel પોતે', 'જે ભાગ સાબિત કરવાનો છે; બધાં opening યોગ્ય blind flangeથી બંધ'],
            ['Filling line અને vent', 'પૂરેપૂરું ભરવા અને હવા બહાર જવા દેવા; અંદર રહેલી હવા test અસુરક્ષિત '
             'કરે અને ખોટો pressure drop આપે'],
            ['Hydro-test pump (hand કે motor)', 'pressure ધીમે અને સ્થિર રીતે test કિંમત સુધી લે'],
            ['Calibrated pressure gauge', 'test pressure વાંચે; gaugeની રેન્જ test pressureની લગભગ 2 ગણી'],
            ['Level glass', 'vessel ભરાયું છે અને pressure પાણીથી ટકે છે, અંદર ફસાયેલી હવાથી નહીં, એ '
             'દેખાડે'],
            ['Relief valve અને drain', 'over-pressure સામે બચાવે અને test પછી vessel ખાલી કરે'],
            ['Safety barricade', 'hold દરમિયાન લોકો દૂર રહે, કારણ કે આ strengthની કસોટી છે'],
        ]),
        h4('પ્રક્રિયા — સ્ટેપ અને કારણ'),
        steps(('Step 1 · તૈયારી', 'બધા weld પૂરા અને NDT પતી ગયું, vessel સાફ, અને safety valve કાઢીને '
                                 'એનાં opening blind કરાય. કારણ: test fabrication પછી થાય, અને safety '
                                 'valve test pressure પહેલાં ખૂલી જાય.'),
              ('Step 2 · ભરવું અને vent', 'નીચેથી પાણી ભરાય અને ઉપરનું vent ખુલ્લું રાખીને પાણી overflow થાય '
                                          'ત્યાં સુધી રાખાય. કારણ: ફસાયેલી હવા pressure પર compress થઈ energy '
                                          'સંઘરે અને gaugeનું વાંચન પણ ખોટું કરે.'),
              ('Step 3 · ધીમે pressure', 'Pump ધીમે ધીમે, પગથિયાંમાં 1.5 × design pressure સુધી વધારે. '
                                         'કારણ: ધીમા વધારાથી ધાતુ ધીરે yield થાય અને operator દરેક joint '
                                         'જોઈ શકે.'),
              ('Step 4 · Hold', 'Pressure 30 મિનિટ રોકાય (codeમાં સામાન્ય રીતે ઓછામાં ઓછી 10 મિનિટ). કારણ: '
                                'leak કે yield થતો ભાગ hold દરમિયાન pressure ઘટાડીને કે weep થઈને દેખાય.'),
              ('Step 5 · તપાસ', 'દરેક welded joint, nozzle અને flange weep માટે તપાસાય. કારણ: test pressure '
                                'પરનો leak એ defect સાબિત કરે જે સામાન્ય working pressure પર દેખાય નહીં.'),
              ('Step 6 · ઘટાડો અને ચકાસણી', 'Pressure design pressure સુધી ઘટાડીને રોકાય અને નિશાન કરેલા '
                                             'વ્યાસ પર permanent set તપાસાય. કારણ: કાયમી (પાછો ન આવે એવો) '
                                             'bulge એટલે ધાતુ yield થઈ — leak ન હોય તો પણ vessel reject.'),
              ('Step 7 · ખાલી કરો, સૂકવો, નોંધ', 'પાણી કાઢીને vessel સૂકવાય અને test certificate sign થાય. '
                                                 'કારણ: ભીનું carbon steel કાટ ખાય, અને certificate testનો '
                                                 'કાયદેસર પુરાવો છે.')),
        h4('ઉપયોગો'),
        bullets('નવાં pressure vessel, boiler, heat exchanger, reactor અને storage tank — fabrication પછી '
                'commissioning પહેલાં codeની જરૂરિયાત.',
                'Pipeline: laying પછી અને લાઇન પર કોઈ પણ hot work પછી.',
                'Gas cylinder અને LPG cylinder — દરેક cylinder નિશ્ચિત સમયે (સામાન્ય રીતે 5 વર્ષે).',
                'Valve, pump અને casting: dispatch પહેલાં body-pressure test.',
                'કોઈ પણ pressure ભાગની મરામત કે ફેરફાર પછી, અને સેવામાં સમય-સમય પર proof test.'),
        h4('ઉકેલેલું ઉદાહરણ'),
        p('Reactor 10 bar working pressure માટે design થયું છે. Hydro test pressure શોધો, અને vesselનું '
          'volume 5 m<sup>3</sup> તથા દર 10 bar પર પાણી 0.05 % compress થાય તો કેટલું વધારે પાણી જોઈએ?'),
        work('Given: design pressure P<sub>d</sub> = 10 bar · test factor = 1.5 · volume V = 5 m<sup>3</sup> '
             '· compressibility દર 10 bar પર 0.05 %',
             'Test pressure P<sub>t</sub> = 1.5 × P<sub>d</sub> = 1.5 × 10',
             'P<sub>t</sub> = 15 bar',
             '15 bar પર compression = 0.05 % × ' + frac('15', '10') + ' = 0.075 %',
             'વધારે પાણી = 0.00075 × 5 m<sup>3</sup> = 0.00375 m<sup>3</sup>'),
        result('Test pressure = 15 bar; વધારે પાણી ≈ 3.75 લિટર'),
        p('Sanity check: 5000 લિટરના vessel માટે 3.75 લિટર એટલે એક ડોલ જેટલું — એટલે જ પાણી સુરક્ષિત છે: '
          'લગભગ કોઈ energy સંગ્રહાતી નથી, ને ફાટે તો છાંટો ઊડે, બ્લાસ્ટ નહીં.'),
        h4('મર્યાદાઓ'),
        bullets('Test પછી vessel સૂકવવું પડે; રહી ગયેલું પાણી કાટ લગાડે અને stainless steelમાં chloride '
                'pitting કરે.',
                'જ્યાં પાણી અંદરની વસ્તુ બગાડે (catalyst, refractory lining, સૂકું product) ત્યાં આ test '
                'ન ચાલે — ત્યાં કડક સલામતી અંતર સાથે pneumatic test થાય.',
                'એ ફક્ત strength અને tightness સાબિત કરે; weldના NDTનો વિકલ્પ નથી, કારણ કે defect પressureમાં '
                'બંધ થઈ જાય અને પછી સેવામાં leak કરે.',
                'ખૂબ ઊંચો proof pressure પોતે જ vesselને સ્થાનિક yieldingથી નુકસાન કરે, એટલે factor codeમાં '
                'મર્યાદિત છે અને ધાતુનું તાપમાન એના transition temperatureથી ઉપર હોવું જોઈએ.'),
    ),
))


# ---------------------------------------------------------------- Q4
Q4 = {
    'title_en': 'Q4 · Thermal insulation, borosilicate and soda-lime glass, porcelain',
    'title_gu': 'પ્ર.4 · Thermal insulation, borosilicate અને soda-lime glass, porcelain',
    'cards': [],
}

Q4['cards'].append(dict(
    number='Q.4 (a)', marks=3,
    q='Explain Thermal Insulation and write properties and application of thermal insulation.',
    en=join(
        h4('Definition'),
        p('<b>Thermal insulation</b> is the use of a low-conductivity material — or a vacuum, or a '
          'reflective surface — to reduce the heat flow between a hot body and its surroundings. The '
          'insulating material itself is also called insulation. It does not stop heat; it only slows it '
          'down by trapping still air in small cells or fibres, because still air has a thermal '
          'conductivity of only about 0.026 W/m·K.'),
        h4('Properties required of a good insulator'),
        table(['Property', 'Typical requirement', 'Why'], [
            ['Thermal conductivity k', 'as low as possible, 0.03–0.06 W/m·K', 'directly sets the heat loss '
             'for a given thickness'],
            ['Density', 'low, 40–150 kg/m<sup>3</sup>', 'low weight and small structural load'],
            ['Temperature limit', 'up to the hot-face temperature without melting or shrinking',
             'rock wool 700 °C, glass wool 450 °C, calcium silicate 650 °C'],
            ['Fire resistance', 'non-combustible, no smoke', 'safety in a plant handling hot oil'],
            ['Moisture resistance', 'hydrophobic or with a vapour barrier', 'wet insulation loses all its '
             'value: water has k ≈ 0.6 W/m·K, 20 times air'],
            ['Mechanical strength', 'enough to bear cladding and foot traffic',
             'insulation must not crush and leave a bare patch'],
            ['Chemical inertness', 'no attack on the steel it covers', 'chloride-free insulation avoids '
             'stress-corrosion cracking of stainless steel'],
            ['Cost and availability', 'cheap in the required form', 'insulation is used in large area'],
        ]),
        figure(fig.insulation_wall(),
               'Fig. 4.1 · Insulation layer on a hot wall and the heat flow it reduces.'),
        h4('Applications'),
        bullets('Process equipment: reactors, distillation columns, heat exchangers, storage tanks and '
                'steam pipelines, where a bare surface wastes steam and creates a burn hazard.',
                'Furnaces, kilns and boilers: refractory brick inside, mineral wool and cladding outside, '
                'to cut fuel consumption.',
                'Buildings and cold stores: roof and wall insulation, and cold-room panels (PUF) that keep '
                'the refrigeration load down.',
                'Cryogenic service: perlite and vacuum-jacketed lines for liquid nitrogen and oxygen.',
                'Personnel protection: a surface above 60 °C must be lagged or guarded, so insulation is a '
                'safety requirement and not only an energy saving.'),
        p('<b>Example of the saving:</b> a bare 100 mm steam pipe at 180 °C loses about 1000 W per metre; '
          'with 50 mm of mineral wool the loss falls below 100 W per metre — a ten-fold saving that pays for '
          'the lagging in a few months.'),
    ),
    gu=join(
        h4('વ્યાખ્યા'),
        p('<b>Thermal insulation</b> એટલે ઓછી conductivity વાળો material — કે vacuum, કે પરાવર્તક સપાટી — '
          'વાપરીને ગરમ પદાર્થ અને આસપાસ વચ્ચેનો heat flow ઘટાડવો. Insulating materialને પણ insulation કહે. '
          'એ heat અટકાવતું નથી, ફક્ત ધીમું કરે — નાના cell કે fibreમાં સ્થિર હવા ફસાવીને, કારણ કે સ્થિર '
          'હવાની thermal conductivity ફક્ત લગભગ 0.026 W/m·K છે.'),
        h4('સારા insulatorમાં જરૂરી ગુણધર્મ'),
        table(['ગુણધર્મ', 'સામાન્ય જરૂરિયાત', 'કેમ'], [
            ['Thermal conductivity k', 'શક્ય તેટલી ઓછી, 0.03–0.06 W/m·K', 'ચોક્કસ થિકનેસ માટે heat loss સીધો '
             'એના પર'],
            ['Density', 'ઓછી, 40–150 kg/m<sup>3</sup>', 'ઓછું વજન અને ઓછો structural load'],
            ['Temperature limit', 'hot-face તાપમાન સુધી, ઓગળ્યા કે સંકોચાયા વગર',
             'rock wool 700 °C, glass wool 450 °C, calcium silicate 650 °C'],
            ['Fire resistance', 'non-combustible, ધુમાડો નહીં', 'ગરમ oil વાળા plantમાં સલામતી'],
            ['Moisture resistance', 'hydrophobic કે vapour barrier સાથે', 'ભીનું insulation બધી કિંમત ગુમાવે: '
             'પાણીની k ≈ 0.6 W/m·K, હવા કરતાં 20 ગણી'],
            ['Mechanical strength', 'cladding અને પગલાંનું વજન ખમે', 'insulation દબાઈને ખાલી જગ્યા ન રહે'],
            ['Chemical inertness', 'નીચેના steel પર હુમલો નહીં', 'chloride-free insulation stainless steelના '
             'stress-corrosion cracking ટાળે'],
            ['ખર્ચ અને ઉપલબ્ધતા', 'જરૂરી સ્વરૂપમાં સસ્તું', 'insulation મોટા ક્ષેત્રમાં વપરાય'],
        ]),
        figure(fig.insulation_wall(),
               'Fig. 4.1 · ગરમ દીવાલ પર insulationનું સ્તર અને એ ઘટાડેલો heat flow.'),
        h4('ઉપયોગો'),
        bullets('Process equipment: reactor, distillation column, heat exchanger, storage tank અને steam '
                'pipeline — જ્યાં ખુલ્લી સપાટી steam વેડફે અને દાઝવાનો ખતરો ઊભો કરે.',
                'Furnace, kiln અને boiler: અંદર refractory brick, બહાર mineral wool અને cladding, જેથી fuel '
                'બચે.',
                'મકાન અને cold store: છત તથા દીવાલનું insulation, અને cold-room panel (PUF) જે refrigeration '
                'load ઓછો રાખે.',
                'Cryogenic સેવા: liquid nitrogen અને oxygen માટે perlite અને vacuum-jacketed લાઇન.',
                'માણસોની સલામતી: 60 °Cથી ઉપરની સપાટી પર lagging કે guard જરૂરી, એટલે insulation ફક્ત energy '
                'બચત નહીં, સલામતીની જરૂરિયાત પણ છે.'),
        p('<b>બચતનું ઉદાહરણ:</b> 180 °C પરનો ખુલ્લો 100 mm steam pipe પ્રતિ મીટર લગભગ 1000 W વેડફે; 50 mm '
          'mineral wool લગાડતાં નુકસાન 100 W પ્રતિ મીટરથી નીચે આવે — દસ ગણી બચત, જે થોડા મહિનામાં laggingનો '
          'ખર્ચ પાછો કઢાવે.'),
    ),
))

Q4['cards'].append(dict(
    number='Q.4 (b)', marks=4,
    q='What is Insulation? List types of insulation and give examples of each type of insulation.',
    en=join(
        h4('Definition'),
        p('<b>Insulation</b> is any material or arrangement used to reduce the transfer of heat, sound or '
          'electricity between two regions. In thermal work it is a low-conductivity material that traps '
          'still air and so reduces the heat flow between a hot or cold surface and its surroundings.'),
        h4('Types of thermal insulation'),
        table(['Type', 'How it works', 'Examples'], [
            ['<b>Fibrous</b> (blanket, batt, board)', 'fine fibres trap air in millions of small pockets',
             'glass wool, rock (mineral) wool, ceramic fibre blanket, slag wool'],
            ['<b>Cellular</b> (foam)', 'closed cells of gas give low conductivity and low water pick-up',
             'polyurethane foam (PUF), polystyrene (thermocol), phenolic foam, foam glass'],
            ['<b>Granular / loose fill</b>', 'loose grains fill any shape and trap air between them',
             'vermiculite, perlite, expanded clay, sawdust, rice husk'],
            ['<b>Reflective</b> (metallic foil)', 'a low-emissivity surface reflects radiation back',
             'aluminium foil, aluminised sheet, foil-faced bubble wrap'],
            ['<b>Vacuum</b>', 'removes the gas, so conduction and convection almost stop',
             'vacuum-jacketed cryogenic line, vacuum flask, vacuum insulated panel'],
            ['<b>Refractory / block</b>', 'a dense, heat-resistant brick or castable slows the heat and '
             'takes the temperature', 'fireclay brick, high-alumina brick, calcium silicate block, '
             'castable refractory'],
            ['<b>DIY / natural</b>', 'cheap local material used in low-temperature work',
             'cork board, woollen felt, coir, straw, paper wool'],
        ]),
        h4('Choice of type'),
        bullets('<b>Temperature decides first:</b> up to 450 °C glass wool, up to 700 °C rock wool, above '
                '1000 °C ceramic fibre or refractory brick.',
                '<b>Shape decides second:</b> pipe work takes a preformed section, a tank takes a mattress or '
                'sprayed foam, a flat roof takes boards or loose fill.',
                '<b>Moisture decides third:</b> cold surfaces need a closed-cell foam with a vapour barrier, '
                'otherwise water condenses inside the insulation and the k value jumps.',
                '<b>Fire and chemical limits decide last:</b> no combustible foam near a furnace, and no '
                'chloride-bearing insulation on stainless steel.'),
        p('<b>Example:</b> a 300 mm steam main at 250 °C is lagged with preformed rock-wool sections, '
          'wire-mesh and aluminium cladding; a chilled-water line at 7 °C uses PUF with a vapour barrier; a '
          'boiler at 1000 °C has fireclay brick inside and mineral wool outside.'),
    ),
    gu=join(
        h4('વ્યાખ્યા'),
        p('<b>Insulation</b> એટલે બે વિસ્તાર વચ્ચે heat, sound કે electricityનું transfer ઘટાડવા વપરાતો '
          'કોઈ પણ material કે ગોઠવણ. Thermal કામમાં એ ઓછી conductivity વાળો material છે જે સ્થિર હવા ફસાવે '
          'અને એટલે ગરમ કે ઠંડી સપાટી અને આસપાસ વચ્ચેનો heat flow ઘટાડે.'),
        h4('Thermal insulationના પ્રકાર'),
        table(['પ્રકાર', 'કેવી રીતે કામ કરે', 'ઉદાહરણ'], [
            ['<b>Fibrous</b> (blanket, batt, board)', 'નાના fibre લાખો નાના ખિસ્સામાં હવા ફસાવે',
             'glass wool, rock (mineral) wool, ceramic fibre blanket, slag wool'],
            ['<b>Cellular</b> (foam)', 'બંધ cellમાં gas ભરાય, conductivity ઓછી અને પાણી ઓછું લે',
             'polyurethane foam (PUF), polystyrene (thermocol), phenolic foam, foam glass'],
            ['<b>Granular / loose fill</b>', 'છૂટા દાણા કોઈ પણ આકાર ભરે અને વચ્ચે હવા ફસાવે',
             'vermiculite, perlite, expanded clay, coir, ભૂસું'],
            ['<b>Reflective</b> (metallic foil)', 'ઓછી emissivityની સપાટી radiation પાછી ફેરવે',
             'aluminium foil, aluminised sheet, foil-faced bubble wrap'],
            ['<b>Vacuum</b>', 'gas કાઢી નાખે, એટલે conduction અને convection લગભગ બંધ',
             'vacuum-jacketed cryogenic line, vacuum flask, vacuum insulated panel'],
            ['<b>Refractory / block</b>', 'ગીચ, heat-resistant brick કે castable heat ધીમું કરે અને તાપમાન '
             'સહે', 'fireclay brick, high-alumina brick, calcium silicate block, castable refractory'],
            ['<b>સ્થાનિક / કુદરતી</b>', 'નીચા તાપમાનના કામમાં સસ્તો સ્થાનિક material',
             'cork board, ઊનનું felt, coir, પરાળ, paper wool'],
        ]),
        h4('પ્રકારની પસંદગી'),
        bullets('<b>પહેલાં તાપમાન નક્કી કરે:</b> 450 °C સુધી glass wool, 700 °C સુધી rock wool, 1000 °Cથી '
                'ઉપર ceramic fibre કે refractory brick.',
                '<b>પછી આકાર:</b> pipe માટે preformed section, tank માટે mattress કે sprayed foam, સપાટ છત માટે '
                'board કે loose fill.',
                '<b>પછી ભેજ:</b> ઠંડી સપાટી પર vapour barrier સાથે closed-cell foam જોઈએ, નહીં તો અંદર પાણી '
                'ઘન થાય અને k કિંમત ઊછળે.',
                '<b>આખરે fire અને chemical મર્યાદા:</b> furnace પાસે combustible foam નહીં, અને stainless '
                'steel પર chloride વાળું insulation નહીં.'),
        p('<b>ઉદાહરણ:</b> 250 °C પરની 300 mm steam main પર preformed rock-wool section, wire-mesh અને '
          'aluminium cladding; 7 °Cની chilled-water લાઇન પર vapour barrier સાથે PUF; અને 1000 °Cના boilerમાં '
          'અંદર fireclay brick, બહાર mineral wool.'),
    ),
))

Q4['cards'].append(dict(
    number='Q.4 (c)', marks=7, q='Give composition and uses of Borosilicate glass.',
    en=join(
        h4('What borosilicate glass is'),
        p('<b>Borosilicate glass</b> is a glass in which a large part of the silica is replaced by '
          '<b>boron trioxide B<sub>2</sub>O<sub>3</sub></b>. The boron enters the silica network as '
          'BO<sub>3</sub> and BO<sub>4</sub> groups, tightens the network, and reduces both the thermal '
          'expansion and the tendency of the glass to be attacked by water and chemicals. It is the '
          'familiar "Pyrex" type of glass.'),
        h4('Composition'),
        table(['Constituent', 'Percentage by mass', 'Function'], [
            ['SiO<sub>2</sub> (silica)', '70–81 %', 'glass former; gives chemical durability'],
            ['B<sub>2</sub>O<sub>3</sub> (boric oxide)', '10–13 %', 'the key oxide: lowers thermal expansion '
             'and raises resistance to water and acids'],
            ['Na<sub>2</sub>O (soda)', '4–8 %', 'flux; lowers the melting temperature'],
            ['Al<sub>2</sub>O<sub>3</sub> (alumina)', '2–7 %', 'increases chemical durability and prevents '
             'phase separation'],
            ['K<sub>2</sub>O (potash)', '0–1 %', 'co-flux, improves workability'],
            ['CaO, MgO', '0–1 %', 'stabilisers'],
            ['As<sub>2</sub>O<sub>3</sub> or Sb<sub>2</sub>O<sub>3</sub>', '0.1–0.5 %', 'fining agent: '
             'removes bubbles from the melt'],
        ]),
        h4('Properties'),
        table(['Property', 'Value', 'Engineering meaning'], [
            ['Coefficient of thermal expansion', '3.2–3.3 × 10<sup>−6</sup>/K (soda-lime glass is '
             '9 × 10<sup>−6</sup>/K)', 'resists thermal shock; can go from boiling water to ice without '
             'cracking'],
            ['Maximum working temperature', 'about 500 °C continuous', 'usable for hot plates and '
             'digestion vessels'],
            ['Thermal shock resistance', 'ΔT of about 150 °C', 'autoclave and steriliser duty'],
            ['Chemical resistance', 'excellent against water, acids and salt solutions; attacked by HF and '
             'hot concentrated alkali', 'laboratory and pharmaceutical ware'],
            ['Hydrolytic class', 'Class I (the best, USP Type I)', 'no leaching into the contents'],
            ['Refractive index', '1.47', 'optical and lamp work'],
            ['Electrical resistivity', 'high, 10<sup>10</sup> Ω·cm at 250 °C', 'insulator in lamp and '
             'electronic parts'],
            ['Density', '2.23 g/cm<sup>3</sup>', 'lighter than soda-lime glass'],
        ]),
        h4('Working — how the boron content gives these properties'),
        steps(('Step 1', 'B<sub>2</sub>O<sub>3</sub> replaces part of the Na<sub>2</sub>O–SiO<sub>2</sub> '
                         'network. Reason: fewer non-bridging oxygen atoms remain, so the network is more '
                         'tightly cross-linked.'),
              ('Step 2', 'A tighter network vibrates less on heating. Reason: the coefficient of expansion '
                         'falls to about one third of that of soda-lime glass.'),
              ('Step 3', 'A low expansion means low thermal stress on sudden cooling. Reason: stress is '
                         'proportional to E·α·ΔT, so borosilicate survives a ΔT of about 150 °C where '
                         'soda-lime glass cracks at about 60 °C.'),
              ('Step 4', 'The tight network also leaves little room for water or acid molecules to enter and '
                         'leach out alkali. Reason: the glass is chemically durable and gets hydrolytic '
                         'class I.')),
        h4('Worked example — thermal stress in a glass beaker'),
        p('Compare the thermal stress produced in a borosilicate beaker and a soda-lime beaker when both '
          'are cooled suddenly by ΔT = 100 °C. Take E = 70 GPa and α = 3.3 × 10<sup>−6</sup>/K for '
          'borosilicate, α = 9.0 × 10<sup>−6</sup>/K for soda-lime.'),
        work('Given: E = 70 GPa = 70 × 10<sup>3</sup> MPa · ΔT = 100 °C · α<sub>borosilicate</sub> = '
             '3.3 × 10<sup>−6</sup>/K · α<sub>soda-lime</sub> = 9.0 × 10<sup>−6</sup>/K',
             'Formula: σ = E · α · ΔT',
             'Borosilicate: σ = 70 × 10<sup>3</sup> × 3.3 × 10<sup>−6</sup> × 100',
             'σ = 23.1 MPa',
             'Soda-lime: σ = 70 × 10<sup>3</sup> × 9.0 × 10<sup>−6</sup> × 100',
             'σ = 63.0 MPa'),
        result('σ ≈ 23 MPa for borosilicate against ≈ 63 MPa for soda-lime'),
        p('Sanity check: the breaking strength of glass is about 50–70 MPa, so the soda-lime beaker is at '
          'its limit and cracks, while the borosilicate one is at one third — which is why laboratory ware '
          'is borosilicate.'),
        h4('Uses'),
        bullets('Laboratory and analytical glassware: beakers, flasks, burettes, pipettes, reagent bottles, '
                'Soxhlet and distillation assemblies.',
                'Pharmaceutical and medical: ampoules, vials, syringes, blood-collection tubes (Type I glass '
                'because it does not leach alkali into the drug).',
                'Chemical and process plant: sight glasses, gauge glasses, pipe sections for corrosive '
                'service, immersion heaters.',
                'Household: ovenware, coffee pots, baby bottles, microwave cookware.',
                'Technical: halogen lamp and sodium lamp envelopes, solar water-heater tubes (evacuated '
                'glass tubes), telescope mirrors and optical windows.'),
        h4('Limitations'),
        bullets('Borosilicate is attacked by <b>hydrofluoric acid</b> and by hot concentrated alkali; it is '
                'not suitable for caustic service above about 60 °C.',
                'It is brittle and has low tensile strength, so it is used in compression-prone shapes and '
                'with rubber or PTFE gaskets.',
                'B<sub>2</sub>O<sub>3</sub> is volatile in the melt, so the composition drifts in the '
                'furnace unless the melt is covered, and B<sub>2</sub>O<sub>3</sub> vapour attacks the '
                'refractory.',
                'It is 2–3 times the price of soda-lime glass, so it is used only where thermal shock or '
                'chemical inertness is essential.'),
    ),
    gu=join(
        h4('Borosilicate glass શું છે'),
        p('<b>Borosilicate glass</b> એ એવું કાચ છે જેમાં silicaનો મોટો ભાગ <b>B<sub>2</sub>O<sub>3</sub></b> '
          'થી બદલાય છે. Boron silica networkમાં BO<sub>3</sub> અને BO<sub>4</sub> જૂથ તરીકે દાખલ થાય, '
          'networkને ગાઢ બનાવે, અને thermal expansion તથા પાણી-રસાયણોથી થતો હુમલો બંને ઘટાડે. આ જ પરિચિત '
          '"Pyrex" પ્રકારનો કાચ છે.'),
        h4('રચના'),
        table(['ઘટક', 'વજનથી ટકા', 'કામ'], [
            ['SiO<sub>2</sub> (silica)', '70–81 %', 'glass former; chemical durability આપે'],
            ['B<sub>2</sub>O<sub>3</sub> (boric oxide)', '10–13 %', 'મુખ્ય oxide: thermal expansion ઘટાડે અને '
             'પાણી તથા acid સામેનો resistance વધારે'],
            ['Na<sub>2</sub>O (soda)', '4–8 %', 'flux; melting temperature ઘટાડે'],
            ['Al<sub>2</sub>O<sub>3</sub> (alumina)', '2–7 %', 'chemical durability વધારે અને phase separation '
             'અટકાવે'],
            ['K<sub>2</sub>O (potash)', '0–1 %', 'સહાયક flux, workability સુધારે'],
            ['CaO, MgO', '0–1 %', 'stabiliser'],
            ['As<sub>2</sub>O<sub>3</sub> કે Sb<sub>2</sub>O<sub>3</sub>', '0.1–0.5 %', 'fining agent: meltમાંથી '
             'પરપોટા કાઢે'],
        ]),
        h4('ગુણધર્મ'),
        table(['ગુણધર્મ', 'કિંમત', 'engineering અર્થ'], [
            ['Thermal expansion coefficient', '3.2–3.3 × 10<sup>−6</sup>/K (soda-lime glass 9 × '
             '10<sup>−6</sup>/K)', 'thermal shock ઝીલે; ઉકળતા પાણીથી બરફમાં જાય તો પણ તૂટે નહીં'],
            ['Maximum working temperature', 'લગભગ 500 °C સતત', 'hot plate અને digestion vessel માટે યોગ્ય'],
            ['Thermal shock resistance', 'ΔT લગભગ 150 °C', 'autoclave અને steriliserનું કામ'],
            ['Chemical resistance', 'પાણી, acid અને salt દ્રાવણ સામે ઉત્તમ; HF અને ગરમ ગાઢ alkaliથી હુમલો '
             'થાય', 'laboratory અને pharmaceutical ware'],
            ['Hydrolytic class', 'Class I (સૌથી સારો, USP Type I)', 'અંદરની વસ્તુમાં કંઈ લીક ન થાય'],
            ['Refractive index', '1.47', 'optical અને lamp કામ'],
            ['Electrical resistivity', 'ઊંચી, 250 °C પર 10<sup>10</sup> Ω·cm', 'lamp અને electronic partમાં '
             'insulator'],
            ['Density', '2.23 g/cm<sup>3</sup>', 'soda-lime glass કરતાં હલકું'],
        ]),
        h4('કાર્ય — boron કેવી રીતે આ ગુણધર્મ આપે'),
        steps(('Step 1', 'B<sub>2</sub>O<sub>3</sub> એ Na<sub>2</sub>O–SiO<sub>2</sub> networkનો ભાગ બદલે. '
                         'કારણ: non-bridging oxygen ઓછા રહે, એટલે network વધુ ગાઢ cross-link થાય.'),
              ('Step 2', 'ગાઢ network ગરમ કરવામાં ઓછું ફેલાય. કારણ: expansion coefficient soda-lime glassના '
                         'લગભગ ત્રીજા ભાગ સુધી ઘટે.'),
              ('Step 3', 'ઓછું expansion એટલે અચાનક ઠંડું કરવામાં ઓછો thermal stress. કારણ: stress ∝ E·α·ΔT, '
                         'એટલે borosilicate લગભગ 150 °Cનો ΔT ઝીલે જ્યાં soda-lime 60 °C પર તૂટે.'),
              ('Step 4', 'ગાઢ networkમાં પાણી કે acidના અણુ ઘૂસીને alkali ખેંચી કાઢવાની જગ્યા ઓછી રહે. '
                         'કારણ: કાચ chemical રીતે ટકાઉ બને અને hydrolytic class I મળે.')),
        h4('ઉકેલેલું ઉદાહરણ — કાચના beakerમાં thermal stress'),
        p('Borosilicate અને soda-lime બંને beaker અચાનક ΔT = 100 °C ઠંડા થાય ત્યારે થતો thermal stress '
          'સરખાવો. E = 70 GPa, borosilicate માટે α = 3.3 × 10<sup>−6</sup>/K અને soda-lime માટે α = '
          '9.0 × 10<sup>−6</sup>/K લો.'),
        work('Given: E = 70 GPa = 70 × 10<sup>3</sup> MPa · ΔT = 100 °C · α<sub>borosilicate</sub> = '
             '3.3 × 10<sup>−6</sup>/K · α<sub>soda-lime</sub> = 9.0 × 10<sup>−6</sup>/K',
             'Formula: σ = E · α · ΔT',
             'Borosilicate: σ = 70 × 10<sup>3</sup> × 3.3 × 10<sup>−6</sup> × 100',
             'σ = 23.1 MPa',
             'Soda-lime: σ = 70 × 10<sup>3</sup> × 9.0 × 10<sup>−6</sup> × 100',
             'σ = 63.0 MPa'),
        result('Borosilicate માટે σ ≈ 23 MPa, soda-lime માટે ≈ 63 MPa'),
        p('Sanity check: કાચની breaking strength લગભગ 50–70 MPa છે, એટલે soda-lime beaker મર્યાદા પર આવીને '
          'તૂટે જ્યારે borosilicate ત્રીજા ભાગે હોય — એટલે જ laboratory ware borosilicateનું હોય.'),
        h4('ઉપયોગો'),
        bullets('Laboratory અને analytical glassware: beaker, flask, burette, pipette, reagent bottle, '
                'Soxhlet અને distillation assembly.',
                'Pharmaceutical અને medical: ampoule, vial, syringe, blood-collection tube (Type I glass, કારણ '
                'કે દવામાં alkali લીક ન થાય).',
                'Chemical અને process plant: sight glass, gauge glass, corrosive સેવા માટે pipe section, '
                'immersion heater.',
                'ઘરેલું: ovenware, coffee pot, baby bottle, microwave cookware.',
                'Technical: halogen અને sodium lampનું envelope, solar water heaterની evacuated tube, '
                'telescope mirror અને optical window.'),
        h4('મર્યાદાઓ'),
        bullets('Borosilicate પર <b>hydrofluoric acid</b> અને ગરમ ગાઢ alkali હુમલો કરે; 60 °Cથી ઉપર '
                'caustic સેવા માટે યોગ્ય નથી.',
                'એ brittle છે અને tensile strength નીચી, એટલે compression ખમે એવા આકારમાં અને rubber કે '
                'PTFE gasket સાથે વપરાય.',
                'Meltમાં B<sub>2</sub>O<sub>3</sub> ઊડી જાય છે, એટલે melt ઢાંક્યા વગર રચના બદલાય, અને '
                'B<sub>2</sub>O<sub>3</sub>ની વરાળ refractory પર હુમલો કરે.',
                'Soda-lime glass કરતાં 2–3 ગણું મોંઘું, એટલે ફક્ત જ્યાં thermal shock કે chemical inertness '
                'જરૂરી હોય ત્યાં વપરાય.'),
    ),
))

Q4['cards'].append(dict(
    number='Q.4 (a)', marks=3, tag='OR', q='Factors affecting thermal conductivity of insulators',
    en=join(
        p('<b>Thermal conductivity k</b> of an insulator is the heat that crosses unit area of unit '
          'thickness per unit temperature difference. For an insulator k is low, 0.03–0.06 W/m·K, and it '
          'is affected by the following factors.'),
        bullets('<b>Porosity and trapped air:</b> the more still air is trapped in cells or fibres, the lower '
                'the k. Air itself has k ≈ 0.026 W/m·K, so a highly porous foam is a good insulator.',
                '<b>Moisture content:</b> this is the biggest factor in practice. Water has k ≈ 0.6 W/m·K, '
                'about 20 times that of air, so a wet insulator loses almost all its value — hence the '
                'vapour barrier on cold lines.',
                '<b>Density:</b> k falls as density falls, but only up to a point; below about 30 kg/m<sup>3'
                '></sup> radiation and convection through the open pores raise k again.',
                '<b>Temperature:</b> k rises with temperature because radiation across the pores grows as '
                'T<sup>4</sup>; that is why a furnace wall is designed in layers of different materials.',
                '<b>Structure of the material:</b> closed-cell foam has a lower k than open-cell foam, and '
                'a fibrous blanket conducts along the fibres, so its k is higher when the fibres run across '
                'the heat flow.',
                '<b>Ageing and compression:</b> foam cells collapse and blow-hole gas escapes, and a '
                'compressed blanket loses its air pockets, so k rises with age and with poor installation.'),
        p('<b>Example:</b> dry mineral wool at 100 kg/m<sup>3</sup> has k ≈ 0.04 W/m·K; the same wool '
          'soaked with water rises to about 0.5 W/m·K, which is why insulation that has been rained on '
          'before cladding is rejected.'),
    ),
    gu=join(
        p('Insulatorની <b>thermal conductivity k</b> એટલે એકમ ક્ષેત્રફળ, એકમ થિકનેસ અને એકમ તાપમાનના ફરક દીઠ '
          'પસાર થતી heat. Insulator માટે k નીચી હોય, 0.03–0.06 W/m·K, અને એના પર નીચેનાં પરિબળો અસર કરે.'),
        bullets('<b>Porosity અને ફસાયેલી હવા:</b> cell કે fibreમાં જેટલી વધુ સ્થિર હવા ફસાય, k એટલી ઓછી. હવાની '
                'k ≈ 0.026 W/m·K, એટલે ખૂબ છિદ્રાળુ foam સારો insulator છે.',
                '<b>ભેજ:</b> વ્યવહારમાં આ સૌથી મોટું પરિબળ. પાણીની k ≈ 0.6 W/m·K, હવા કરતાં લગભગ 20 ગણી, '
                'એટલે ભીનું insulation લગભગ બધી કિંમત ગુમાવે — એટલે ઠંડી લાઇન પર vapour barrier જરૂરી.',
                '<b>Density:</b> density ઘટે તો k ઘટે, પણ એક હદ સુધી; લગભગ 30 kg/m<sup>3</sup>થી નીચે ખુલ્લા '
                'છિદ્રોમાં radiation અને convection k ફરી વધારે.',
                '<b>તાપમાન:</b> તાપમાન વધે તો k વધે, કારણ કે છિદ્રોમાં radiation T<sup>4</sup> જેટલી વધે; '
                'એટલે furnace wall જુદા materialના સ્તરોમાં બનાવાય.',
                '<b>Materialનું structure:</b> closed-cell foamની k ખુલ્લા cell કરતાં ઓછી; fibrous blanketમાં '
                'fibre દ્વારા heat જાય, એટલે fibre heat flowને આડી હોય ત્યારે k વધે.',
                '<b>Ageing અને compression:</b> foamના cell દબાઈ જાય અને gas નીકળી જાય, અને દબાયેલા blanketમાં '
                'હવાના ખિસ્સા મરી જાય, એટલે ઉંમર સાથે અને ખરાબ installationથી k વધે.'),
        p('<b>ઉદાહરણ:</b> 100 kg/m<sup>3</sup>ની સૂકી mineral woolની k ≈ 0.04 W/m·K; એ જ ઊન પાણીથી ભીની '
          'થાય તો લગભગ 0.5 W/m·K સુધી જાય — એટલે cladding પહેલાં વરસાદમાં ભીનું થયેલું insulation reject '
          'થાય.'),
    ),
))

Q4['cards'].append(dict(
    number='Q.4 (b)', marks=4, q='Give composition and uses of Soda lime glass',
    en=join(
        h4('What it is'),
        p('<b>Soda-lime glass</b> is the ordinary, cheapest glass — the glass of windows, bottles and '
          'tumblers. It is a sodium calcium silicate: silica is the glass former, soda is the flux that '
          'makes it melt at a workable temperature, and lime stabilises the network so that the glass does '
          'not dissolve in water.'),
        h4('Composition'),
        table(['Constituent', 'Percentage by mass', 'Function'], [
            ['SiO<sub>2</sub> (sand)', '70–74 %', 'glass former; gives hardness and durability'],
            ['Na<sub>2</sub>O (soda ash)', '12–16 %', 'flux; lowers the melting point from about 1700 °C to '
             'about 1400 °C'],
            ['CaO (lime, from limestone)', '5–12 %', 'stabiliser; makes the glass insoluble in water and '
             'raises chemical durability'],
            ['MgO', '0–4 %', 'improves durability and lowers the working temperature'],
            ['Al<sub>2</sub>O<sub>3</sub>', '0–2 %', 'increases strength and resistance to devitrification'],
            ['K<sub>2</sub>O', '0–1 %', 'improves lustre and workability'],
            ['Fe<sub>2</sub>O<sub>3</sub>', 'less than 0.05 %', 'impurity; gives the green tint of thick '
             'bottle glass'],
            ['Colouring / decolourising oxides', '0.1–1 %', 'Cr<sub>2</sub>O<sub>3</sub> green, '
             'CoO blue, Se pink, MnO<sub>2</sub> decolouriser'],
        ]),
        h4('Properties'),
        table(['Property', 'Value', 'Meaning'], [
            ['Coefficient of thermal expansion', '9 × 10<sup>−6</sup>/K', 'cracks on sudden cooling beyond '
             'about 60 °C'],
            ['Softening temperature', 'about 700 °C', 'cannot take hot-plate duty'],
            ['Density', '2.5 g/cm<sup>3</sup>', 'ordinary weight'],
            ['Refractive index', '1.52', 'good optical clarity for windows'],
            ['Chemical resistance', 'good against water and neutral solutions; poor against hot alkali and '
             'HF', 'bottles are safe for food and drink'],
            ['Strength', 'compressive 700–1000 MPa, tensile only 30–70 MPa', 'use in compression; glass '
             'fails in tension'],
            ['Cost', 'cheapest of all glasses', 'mass production of bottles and window panes'],
            ['Electrical resistivity', 'high at room temperature', 'insulator, but not at high temperature'],
        ]),
        h4('Uses'),
        bullets('Flat glass: window panes, shop fronts, mirrors, toughened and laminated safety glass for '
                'vehicles and buildings.',
                'Containers: bottles for water, soft drinks, beer, milk and medicine (the largest single '
                'use), and jars for food.',
                'Domestic ware: tumblers, jugs, bowls, tableware.',
                'Lighting and electrical: lamp bulbs and tubes (outer envelope), insulators, switch covers.',
                'Other: glass blocks, decorative glassware, greenhouse glazing, solar panels.'),
        h4('Limitations'),
        p('Soda-lime glass cannot take <b>thermal shock</b>: with α = 9 × 10<sup>−6</sup>/K a sudden '
          'cooling of about 60 °C already develops a stress equal to its tensile strength, so a hot jar put '
          'into cold water cracks. It is also attacked by hot alkali and by hydrofluoric acid, and it '
          'leaches a little alkali into water over long storage — which is why pharmaceutical vials are '
          'made of borosilicate (Type I) and not of soda-lime glass.'),
    ),
    gu=join(
        h4('શું છે'),
        p('<b>Soda-lime glass</b> એ સામાન્ય, સૌથી સસ્તો કાચ — બારી, બોટલ અને ગ્લાસનો કાચ. એ sodium calcium '
          'silicate છે: silica glass former, soda એ flux જે એને કામ થાય એવા તાપમાને ઓગાળે, અને lime network '
          'stabilise કરે જેથી કાચ પાણીમાં ઓગળે નહીં.'),
        h4('રચના'),
        table(['ઘટક', 'વજનથી ટકા', 'કામ'], [
            ['SiO<sub>2</sub> (રેતી)', '70–74 %', 'glass former; hardness અને durability આપે'],
            ['Na<sub>2</sub>O (soda ash)', '12–16 %', 'flux; melting point લગભગ 1700 °C થી 1400 °C સુધી '
             'ઘટાડે'],
            ['CaO (lime, limestoneમાંથી)', '5–12 %', 'stabiliser; કાચ પાણીમાં અદ્રાવ્ય બનાવે અને chemical '
             'durability વધારે'],
            ['MgO', '0–4 %', 'durability સુધારે અને working temperature ઘટાડે'],
            ['Al<sub>2</sub>O<sub>3</sub>', '0–2 %', 'strength અને devitrification સામેનો resistance વધારે'],
            ['K<sub>2</sub>O', '0–1 %', 'lustre અને workability સુધારે'],
            ['Fe<sub>2</sub>O<sub>3</sub>', '0.05 %થી ઓછું', 'અશુદ્ધિ; જાડી બોટલને લીલી છાયા આપે'],
            ['રંગ અને decolourising oxide', '0.1–1 %', 'Cr<sub>2</sub>O<sub>3</sub> લીલો, CoO ભૂરો, Se ગુલાબી, '
             'MnO<sub>2</sub> decolouriser'],
        ]),
        h4('ગુણધર્મ'),
        table(['ગુણધર્મ', 'કિંમત', 'અર્થ'], [
            ['Thermal expansion coefficient', '9 × 10<sup>−6</sup>/K', 'લગભગ 60 °Cથી વધુ અચાનક ઠંડું થાય તો '
             'તૂટે'],
            ['Softening temperature', 'લગભગ 700 °C', 'hot plateનું કામ ન લઈ શકે'],
            ['Density', '2.5 g/cm<sup>3</sup>', 'સામાન્ય વજન'],
            ['Refractive index', '1.52', 'બારી માટે સારી optical clarity'],
            ['Chemical resistance', 'પાણી અને neutral દ્રાવણ સામે સારો; ગરમ alkali અને HF સામે નબળો',
             'બોટલમાં ખાવા-પીવાની વસ્તુ સુરક્ષિત'],
            ['Strength', 'compressive 700–1000 MPa, tensile ફક્ત 30–70 MPa', 'compressionમાં વાપરવું; કાચ '
             'tensionમાં તૂટે'],
            ['ખર્ચ', 'બધા કાચમાં સૌથી સસ્તું', 'બોટલ અને window paneનું મોટા પ્રમાણમાં ઉત્પાદન'],
            ['Electrical resistivity', 'ઓરડાના તાપમાને ઊંચી', 'insulator, પણ ઊંચા તાપમાને નહીં'],
        ]),
        h4('ઉપયોગો'),
        bullets('Flat glass: window pane, shop front, mirror, વાહન અને મકાન માટે toughened તથા laminated '
                'safety glass.',
                'Container: પાણી, soft drink, beer, દૂધ અને દવાની બોટલ (સૌથી મોટો ઉપયોગ) અને ખાવાના jar.',
                'ઘરેલું વાસણ: ગ્લાસ, jug, bowl, tableware.',
                'Lighting અને electrical: lamp bulb તથા tubeનું outer envelope, insulator, switch cover.',
                'બીજું: glass block, decorative glassware, greenhouseનું glazing, solar panel.'),
        h4('મર્યાદાઓ'),
        p('Soda-lime glass <b>thermal shock</b> ખમી શકતું નથી: α = 9 × 10<sup>−6</sup>/K હોવાથી લગભગ 60 °Cનું '
          'અચાનક ઠંડું થવું એ tensile strength જેટલો stress પેદા કરે, એટલે ગરમ jar ઠંડા પાણીમાં મુકાય તો '
          'તૂટે. ગરમ alkali અને hydrofluoric acid પણ એના પર હુમલો કરે, અને લાંબા સંગ્રહમાં પાણીમાં થોડું '
          'alkali લીક થાય — એટલે દવાની vial soda-limeને બદલે borosilicate (Type I)ની બનાવાય.'),
    ),
))

Q4['cards'].append(dict(
    number='Q.4 (c)', marks=7, q='Give Composition, properties and uses of porcelain',
    en=join(
        h4('What porcelain is'),
        p('<b>Porcelain</b> is a white, vitrified, non-porous ceramic made from a mixture of kaolin (china '
          'clay), feldspar and quartz, fired at 1250–1400 °C. During firing the feldspar melts and forms a '
          'glass that binds the clay and quartz particles, so the body becomes dense and impermeable — this '
          'is what separates porcelain from ordinary earthenware, which stays porous.'),
        h4('Composition'),
        table(['Constituent', 'Percentage', 'Function'], [
            ['Kaolin / china clay (Al<sub>2</sub>O<sub>3</sub>·2SiO<sub>2</sub>·2H<sub>2</sub>O)', '40–50 %',
             'gives plasticity for shaping and whiteness after firing'],
            ['Feldspar (K<sub>2</sub>O·Al<sub>2</sub>O<sub>3</sub>·6SiO<sub>2</sub>)', '25–35 %',
             'flux: melts at 1100–1200 °C and forms the glass that vitrifies the body'],
            ['Quartz / flint (SiO<sub>2</sub>)', '20–30 %', 'filler: reduces shrinkage and gives rigidity '
             'and thermal stability'],
            ['Glaze (feldspar + quartz + clay, with colouring oxides)', 'thin surface layer',
             'makes the surface smooth, non-absorbent and easy to clean'],
        ]),
        h4('Properties'),
        table(['Property', 'Value / behaviour', 'Engineering meaning'], [
            ['Porosity', 'zero after firing (vitrified)', 'does not absorb water, can hold liquids'],
            ['Density', '2.3–2.5 g/cm<sup>3</sup>', 'dense body'],
            ['Compressive strength', 'very high, 400–700 MPa', 'good in compression, as in insulators'],
            ['Tensile and impact strength', 'low; brittle', 'cannot be used in tension or shock'],
            ['Dielectric strength', 'excellent, and low dielectric loss', 'high-voltage insulators'],
            ['Dielectric loss and power factor', 'low and stable with frequency',
             'capacitors and RF insulators'],
            ['Thermal expansion', 'about 4–5 × 10<sup>−6</sup>/K', 'moderate thermal shock resistance'],
            ['Maximum service temperature', 'about 1000 °C for the body', 'refractory and kiln furniture'],
            ['Chemical resistance', 'excellent against water, acids and alkalis except HF and hot caustic',
             'chemical stoneware, laboratory ware'],
            ['Hardness', '6–7 on the Mohs scale', 'resists scratching and abrasion'],
            ['Colour and finish', 'white, translucent when thin, glossy glaze', 'tableware and sanitaryware'],
        ]),
        h4('Manufacturing — step and reason'),
        steps(('Step 1 · Blunging', 'Clay, feldspar and quartz are mixed with water into a slip. Reason: '
                                   'water separates the particles so the mix is uniform.'),
              ('Step 2 · Shaping', 'The body is shaped by throwing, jiggering, pressing, extrusion or slip '
                                   'casting. Reason: clay is plastic only when wet, so shaping comes before '
                                   'firing.'),
              ('Step 3 · Drying', 'The article is dried slowly to about 1 % moisture. Reason: fast drying '
                                  'shrinks the outside first and cracks the ware.'),
              ('Step 4 · Bisque firing', 'The first firing at about 900–1000 °C burns off organic matter '
                                         'and gives a strong but still porous body. Reason: the ware can now '
                                         'be handled while the glaze is applied.'),
              ('Step 5 · Glazing', 'The glaze slip is sprayed or dipped on. Reason: fusion of the glaze in '
                                   'the next firing gives the non-absorbent, easy-clean surface.'),
              ('Step 6 · Glost firing', 'The second firing at 1250–1400 °C vitrifies the body and matures '
                                        'the glaze. Reason: feldspar melts, the open pores close, and the '
                                        'body becomes non-porous — this is the step that makes it '
                                        'porcelain.'),
              ('Step 7 · Sorting and testing', 'The ware is checked for crazing, warpage and dielectric '
                                               'strength. Reason: a crazed glaze lets water into the body '
                                               'and destroys an insulator.')),
        h4('Uses'),
        bullets('Electrical: high-voltage and low-voltage insulators, bushings, capacitor dielectrics, '
                'switch bases — porcelain is the classic insulator because it is strong in compression and '
                'has a very low dielectric loss.',
                'Chemical plant: stoneware pipes, tower packings, valve parts, acid-proof tiles and '
                'labouratory ware for corrosive service.',
                'Domestic: tableware, cups and plates, sanitaryware (wash basins, WC pans), tiles.',
                'Industrial: kiln furniture, saggers, grinding media, wear-resistant linings, dental and '
                'artificial-teeth porcelain.',
                'Laboratory: crucibles, combustion boats, spark-plug insulators.'),
        h4('Worked example — why porcelain is used in compression'),
        p('A porcelain insulator carries a compressive stress of 2.5 MN/m<sup>2</sup> and a bending stress '
          'of 60 MN/m<sup>2</sup> at the same section. Its compressive strength is 500 MN/m<sup>2</sup> and '
          'tensile strength 40 MN/m<sup>2</sup>. Find the factor of safety in each case and comment.'),
        work('Given: σ<sub>comp</sub> = 2.5 MN/m<sup>2</sup> · σ<sub>bend</sub> = 60 MN/m<sup>2</sup> · '
             'strength in compression = 500 MN/m<sup>2</sup> · strength in tension = 40 MN/m<sup>2</sup>',
             'Formula: FoS = ' + frac('strength', 'applied stress'),
             'In compression: FoS = ' + frac('500', '2.5') + ' = 200',
             'In bending (tension side): FoS = ' + frac('40', '60') + ' = 0.67'),
        result('FoS = 200 in compression, but only 0.67 in bending — the part would already have failed'),
        p('Sanity check: a factor below 1 means failure, so the design must be changed to keep the porcelain '
          'in compression — which is exactly why an insulator is shaped as a stack of skirts in compression '
          'and is never used as a beam.'),
        h4('Limitations'),
        bullets('Porcelain is <b>brittle</b>: it has almost no ductility and fails without warning, so it '
                'cannot be used where impact or bending is expected.',
                'It cannot take sudden temperature change; repeated heating and cooling crazes the glaze and '
                'then cracks the body.',
                'It is attacked by hydrofluoric acid and by hot concentrated alkali, which dissolve the '
                'silica network.',
                'Firing shrinkage of 10–15 % must be allowed in the mould, and the firing is energy '
                'intensive, so large or thick pieces are difficult and costly.'),
    ),
    gu=join(
        h4('Porcelain શું છે'),
        p('<b>Porcelain</b> એ સફેદ, vitrified, છિદ્ર રહિત ceramic છે, જે kaolin (china clay), feldspar અને '
          'quartzના મિશ્રણમાંથી 1250–1400 °C પર firing કરીને બનાવાય. Firing દરમિયાન feldspar ઓગળીને glass '
          'બનાવે જે clay અને quartzના કણને જોડે, એટલે body ગીચ અને impermeable બને — આ જ porcelainને સામાન્ય '
          'earthenwareથી અલગ પાડે, જે છિદ્રાળુ રહે.'),
        h4('રચના'),
        table(['ઘટક', 'ટકા', 'કામ'], [
            ['Kaolin / china clay (Al<sub>2</sub>O<sub>3</sub>·2SiO<sub>2</sub>·2H<sub>2</sub>O)', '40–50 %',
             'આકાર આપવા plasticity અને firing પછી સફેદપણું આપે'],
            ['Feldspar (K<sub>2</sub>O·Al<sub>2</sub>O<sub>3</sub>·6SiO<sub>2</sub>)', '25–35 %',
             'flux: 1100–1200 °C પર ઓગળીને એ glass બનાવે જે bodyને vitrify કરે'],
            ['Quartz / flint (SiO<sub>2</sub>)', '20–30 %', 'filler: shrinkage ઘટાડે અને rigidity તથા '
             'thermal stability આપે'],
            ['Glaze (feldspar + quartz + clay, રંગ આપતા oxide સાથે)', 'પાતળો સપાટી સ્તર',
             'સપાટી સરળ, પાણી ન શોષે એવી અને સાફ કરવા સહેલી બનાવે'],
        ]),
        h4('ગુણધર્મ'),
        table(['ગુણધર્મ', 'કિંમત / વર્તન', 'engineering અર્થ'], [
            ['Porosity', 'firing પછી શૂન્ય (vitrified)', 'પાણી શોષે નહીં, પ્રવાહી રાખી શકે'],
            ['Density', '2.3–2.5 g/cm<sup>3</sup>', 'ગીચ body'],
            ['Compressive strength', 'ખૂબ ઊંચી, 400–700 MPa', 'compressionમાં સારું, insulatorની જેમ'],
            ['Tensile અને impact strength', 'નીચી; brittle', 'tension કે ઝાટકામાં ન વપરાય'],
            ['Dielectric strength', 'ઉત્તમ, અને dielectric loss ઓછું', 'ઊંચા વોલ્ટેજના insulator'],
            ['Dielectric loss અને power factor', 'ઓછા અને frequency સાથે સ્થિર', 'capacitor અને RF insulator'],
            ['Thermal expansion', 'લગભગ 4–5 × 10<sup>−6</sup>/K', 'મધ્યમ thermal shock resistance'],
            ['Maximum service temperature', 'body માટે લગભગ 1000 °C', 'refractory અને kiln furniture'],
            ['Chemical resistance', 'પાણી, acid અને alkali સામે ઉત્તમ, HF અને ગરમ caustic સિવાય',
             'chemical stoneware, laboratory ware'],
            ['Hardness', 'Mohs 6–7', 'ખૂટે નહીં, abrasion ઝીલે'],
            ['રંગ અને finish', 'સફેદ, પાતળું હોય તો અર્ધપારદર્શક, ચમકદાર glaze', 'tableware અને '
             'sanitaryware'],
        ]),
        h4('બનાવટ — સ્ટેપ અને કારણ'),
        steps(('Step 1 · Blunging', 'Clay, feldspar અને quartzને પાણી સાથે slip બનાવાય. કારણ: પાણી કણોને '
                                   'અલગ કરે જેથી mix સરખું થાય.'),
              ('Step 2 · આકાર', 'Throwing, jiggering, pressing, extrusion કે slip castingથી આકાર આપાય. કારણ: '
                                'clay ભીની હોય ત્યારે જ plastic હોય, એટલે firing પહેલાં આકાર આપવો પડે.'),
              ('Step 3 · સૂકવણી', 'વસ્તુને ધીમે ધીમે લગભગ 1 % ભેજ સુધી સૂકવાય. કારણ: ઝડપી સૂકવણીમાં બહારનો ભાગ '
                                 'પહેલાં સંકોચાય અને વસ્તુ ફાટે.'),
              ('Step 4 · Bisque firing', 'લગભગ 900–1000 °C પર પહેલું firing organic પદાર્થ બાળી નાખે અને મજબૂત '
                                         'પણ છિદ્રાળુ body આપે. કારણ: હવે glaze લગાડી શકાય એટલી વસ્તુ '
                                         'સંભાળી શકાય.'),
              ('Step 5 · Glazing', 'Glazeની slip spray કે dip કરાય. કારણ: આગળના firingમાં glaze ઓગળીને પાણી '
                                   'ન શોષે એવી, સાફ કરવા સહેલી સપાટી આપે.'),
              ('Step 6 · Glost firing', 'બીજું firing 1250–1400 °C પર bodyને vitrify કરે અને glaze પકવે. '
                                        'કારણ: feldspar ઓગળે, ખુલ્લા છિદ્ર બંધ થાય, અને body છિદ્ર રહિત બને — '
                                        'આ જ પગલું એને porcelain બનાવે.'),
              ('Step 7 · Sorting અને testing', 'Crazing, warpage અને dielectric strength તપાસાય. કારણ: crazed '
                                               'glaze પાણી અંદર જવા દે અને insulator નકામો થાય.')),
        h4('ઉપયોગો'),
        bullets('Electrical: ઊંચા અને નીચા વોલ્ટેજના insulator, bushing, capacitor dielectric, switch base — '
                'porcelain classic insulator છે, કારણ કે compressionમાં મજબૂત અને dielectric loss બહુ ઓછું.',
                'Chemical plant: stoneware pipe, tower packing, valve part, acid-proof tile અને corrosive '
                'સેવા માટે laboratory ware.',
                'ઘરેલું: tableware, કપ-પ્લેટ, sanitaryware (wash basin, WC pan), tile.',
                'Industrial: kiln furniture, sagger, grinding media, wear-resistant lining, dental અને '
                'artificial teeth porcelain.',
                'Laboratory: crucible, combustion boat, spark-plug insulator.'),
        h4('ઉકેલેલું ઉદાહરણ — porcelain compressionમાં કેમ વપરાય'),
        p('Porcelain insulator પર એક જ section પર 2.5 MN/m<sup>2</sup> compressive stress અને 60 MN/m<sup>2</sup> '
          'bending stress આવે છે. એની compressive strength 500 MN/m<sup>2</sup> અને tensile strength '
          '40 MN/m<sup>2</sup> છે. બંને માટે factor of safety શોધો અને ટિપ્પણી કરો.'),
        work('Given: σ<sub>comp</sub> = 2.5 MN/m<sup>2</sup> · σ<sub>bend</sub> = 60 MN/m<sup>2</sup> · '
             'compressionમાં strength = 500 MN/m<sup>2</sup> · tensionમાં strength = 40 MN/m<sup>2</sup>',
             'Formula: FoS = ' + frac('strength', 'applied stress'),
             'Compressionમાં: FoS = ' + frac('500', '2.5') + ' = 200',
             'Bendingમાં (tension બાજુ): FoS = ' + frac('40', '60') + ' = 0.67'),
        result('Compressionમાં FoS = 200, પણ bendingમાં ફક્ત 0.67 — ભાગ તો પહેલેથી તૂટી ગયો હોત'),
        p('Sanity check: 1થી નીચો factor એટલે failure, એટલે design બદલીને porcelainને compressionમાં રાખવું '
          'પડે — એટલે જ insulator compressionમાં ગોઠવાયેલી skirtની થપ્પી જેવો બને છે અને beam તરીકે કદી '
          'વપરાતો નથી.'),
        h4('મર્યાદાઓ'),
        bullets('Porcelain <b>brittle</b> છે: ductility લગભગ શૂન્ય અને ચેતવણી વગર તૂટે, એટલે જ્યાં ઝાટકો કે '
                'bending હોય ત્યાં ન વપરાય.',
                'અચાનક તાપમાનનો ફરક ન ખમે; વારંવાર ગરમ-ઠંડું થવાથી glaze crazed થાય અને પછી body ફાટે.',
                'Hydrofluoric acid અને ગરમ ગાઢ alkali એના પર હુમલો કરે, કારણ કે એ silica network ઓગાળે.',
                'Firing shrinkage 10–15 % હોય, એટલે mouldમાં એ ગણતરી રાખવી પડે, અને firing ઊર્જા માગે છે, '
                'એટલે મોટા કે જાડા ભાગ મુશ્કેલ અને મોંઘા પડે.'),
    ),
))
