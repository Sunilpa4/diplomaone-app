"""DI01005021 Winter 2025 — Q1 and Q2 answer parts (Material Science and Technology)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from paperkit import frac, work, steps, result, table, bullets, numbered, h4, p, eq, figure
import matfigs as fig
import matfigs2 as fig2


def join(*chunks):
    return "\n".join(c for c in chunks if c)


# ---------------------------------------------------------------- Q1
Q1 = {
    'title_en': 'Q1 · Plastics, thermal conductivity, soda-lime glass and ceramics',
    'title_gu': 'પ્ર.1 · પ્લાસ્ટિક, થર્મલ કન્ડક્ટિવિટી, સોડા-લાઇમ ગ્લાસ અને સિરામિક',
    'cards': [],
}

Q1['cards'].append(dict(
    number='Q.1 (a)', marks=3, q='Classify plastic.',
    en=join(
        p('A <b>plastic</b> is a high polymer — a long-chain organic material that can be shaped by '
          'heat and pressure and then kept in that shape. Plastics are classified mainly by what '
          'happens when they are heated again, and secondarily by their source and by their use.'),
        figure(fig2.plastic_tree(),
               'Fig. 1.1 · Classification of plastics — thermoplastic and thermosetting, with the '
               'chain structure of each drawn below.'),
        h4('The two main classes'),
        table(['Basis', 'Class', 'Behaviour', 'Examples'], [
            ['<b>Effect of heat</b>', '<b>Thermoplastic</b>', 'softens every time it is heated and '
             'hardens on cooling; can be re-moulded and recycled', 'polythene (PE), PVC, polypropylene, '
             'polystyrene, nylon, acrylic (PMMA)'],
            ['<b>Effect of heat</b>', '<b>Thermosetting</b>', 'sets once, by a chemical cross-linking '
             'reaction; it cannot be softened again, and it chars on strong heating',
             'bakelite, epoxy, melamine, urea formaldehyde, polyester resin'],
            ['Source', 'Natural · synthetic', 'natural from plants and animals; synthetic from petroleum '
             'chemicals', 'natural: cellulose, casein, shellac / synthetic: PE, PVC, bakelite'],
            ['Use', 'General purpose · engineering', 'general purpose is cheap and common; engineering '
             'plastics carry load or heat', 'PE, PP, PVC / nylon, PTFE, polycarbonate, ABS'],
        ]),
        p('<b>Example:</b> a bucket is a <b>thermoplastic</b> (polythene) — it can be melted and '
          're-moulded. A tabletop electrical switch is <b>thermosetting</b> (bakelite) — it must not '
          'soften when the switch warms up, and it cannot be re-melted.'),
    ),
    gu=join(
        p('<b>Plastic</b> એ ઊંચું polymer છે — લાંબી સાંકળવાળું organic પદાર્થ, જેને ગરમી અને દબાણથી '
          'આકાર આપી શકાય અને પછી એ આકારમાં રહી જાય. Plasticsનું વર્ગીકરણ મુખ્યત્વે એના પરથી થાય કે ફરી '
          'ગરમ કરતાં શું થાય, અને ગૌણ રીતે source તથા ઉપયોગ પરથી.'),
        figure(fig2.plastic_tree(),
               'Fig. 1.1 · Plasticsનું વર્ગીકરણ — thermoplastic અને thermosetting, નીચે બંનેની '
               'chain structure.'),
        h4('બે મુખ્ય વર્ગ'),
        table(['આધાર', 'વર્ગ', 'વર્તન', 'ઉદાહરણ'], [
            ['<b>ગરમીની અસર</b>', '<b>Thermoplastic</b>', 'દર વખતે ગરમ કરતાં નરમ થાય અને ઠંડા પડતાં સખત; '
             'ફરી mould થઈ શકે અને recycle થાય', 'polythene (PE), PVC, polypropylene, polystyrene, nylon, '
             'acrylic'],
            ['<b>ગરમીની અસર</b>', '<b>Thermosetting</b>', 'એક જ વાર chemical cross-linkingથી સેટ થાય; ફરી '
             'નરમ થઈ શકે નહીં, અને વધુ ગરમ કરતાં બળીને કોલસો થાય', 'bakelite, epoxy, melamine, urea '
             'formaldehyde, polyester resin'],
            ['Source', 'Natural · synthetic', 'natural વનસ્પતિ-પ્રાણીથી; synthetic petroleum chemicalથી',
             'natural: cellulose, casein, shellac / synthetic: PE, PVC, bakelite'],
            ['ઉપયોગ', 'General purpose · engineering', 'general purpose સસ્તું અને સામાન્ય; engineering '
             'plastic ભાર કે ગરમી ઝીલે', 'PE, PP, PVC / nylon, PTFE, polycarbonate, ABS'],
        ]),
        p('<b>ઉદાહરણ:</b> બાલદી <b>thermoplastic</b> (polythene) છે — ઓગાળીને ફરી આકાર આપી શકાય. '
          'Switch boardનું tabletop <b>thermosetting</b> (bakelite) છે — switch ગરમ થાય ત્યારે નરમ ન પડવું '
          'જોઈએ, અને એ ફરી ઓગળે નહીં.'),
    ),
))

Q1['cards'].append(dict(
    number='Q.1 (b)', marks=4, q='List factors affecting thermal conductivity of insulators.',
    en=join(
        p('<b>Thermal conductivity</b> k is the rate at which heat passes through unit thickness of a '
          'material for unit area and unit temperature difference, in W/m·K. For an <b>insulator</b> we '
          'want k as small as possible, and k depends on the following factors.'),
        h4('The factors'),
        table(['Factor', 'How it affects k', 'Why'], [
            ['<b>Porosity and the gas trapped in the pores</b>', 'k falls as porosity rises; a foam with '
             '90 % air has k ≈ 0.03 W/m·K', 'still air is a poor conductor (k = 0.026), so trapped air '
             'does most of the insulating'],
            ['<b>Moisture content</b>', 'a wet insulator can have two to three times the k of a dry one',
             'water has k = 0.6 W/m·K, about 25 times that of air, and it fills the pores'],
            ['<b>Density</b>', 'k falls as density falls, down to an optimum; below that, radiation '
             'through the pores raises k again', 'fewer solid paths for heat, but too little solid means '
             'the pores are large and radiate'],
            ['<b>Temperature</b>', 'k rises slowly with temperature, and radiation across the pores rises '
             'as T<sup>4</sup>', 'the gas conducts better when hot and the radiation becomes important '
             'above about 200 °C'],
            ['<b>Structure: fibrous, cellular or granular</b>', 'a fine closed-cell structure gives the '
             'lowest k', 'fine cells stop convection and radiation; open cells let air circulate'],
            ['<b>Pressure of the gas in the pores</b>', 'k falls when the gas pressure is reduced',
             'a vacuum removes gas conduction altogether — vacuum insulation'],
            ['<b>Composition and crystal structure</b>', 'amorphous and complex solids conduct less than '
             'simple crystalline ones', 'heat is carried by lattice vibration and free electrons; '
             'ordered lattices carry it better'],
            ['<b>Ageing and compaction</b>', 'k rises as the material settles, cracks or absorbs water',
             'the pore structure collapses and moisture gets in'],
        ]),
        figure(fig.insulation_wall(),
               'Fig. 1.2 · An insulating layer on a hot wall — the pores hold still air, and heat flow q '
               'falls as k falls.'),
        h4('Worked example — the value of dry insulation'),
        p('A furnace wall is 200 mm of firebrick with k = 1.0 W/m·K. Adding 50 mm of insulation with '
          'k = 0.05 W/m·K reduces the heat loss. Compare the heat flow through the two layers if the '
          'inner surface is at 900 °C and the outer at 60 °C, per m<sup>2</sup>.'),
        work('Given: brick t<sub>1</sub> = 0.2 m, k<sub>1</sub> = 1.0 W/m·K · insulation '
             't<sub>2</sub> = 0.05 m, k<sub>2</sub> = 0.05 W/m·K · ΔT = 900 − 60 = 840 K · A = 1 m<sup>2</sup>',
             'Brick alone: q = ' + frac('k · A · ΔT', 't') + ' = ' + frac('1.0 × 1 × 840', '0.2'),
             'q = 4200 W/m<sup>2</sup>',
             'Resistance of brick R<sub>1</sub> = ' + frac('t<sub>1</sub>', 'k<sub>1</sub>') + ' = '
             + frac('0.2', '1.0') + ' = 0.2 m<sup>2</sup>·K/W',
             'Resistance of insulation R<sub>2</sub> = ' + frac('0.05', '0.05') + ' = 1.0 m<sup>2</sup>·K/W',
             'With both: q = ' + frac('ΔT', 'R<sub>1</sub> + R<sub>2</sub>') + ' = '
             + frac('840', '0.2 + 1.0') + ' = ' + frac('840', '1.2')),
        result('4200 W/m<sup>2</sup> without insulation, only 700 W/m<sup>2</sup> with it — a saving of '
               '83 %'),
        p('Sanity check: a 50 mm layer of k = 0.05 has five times the resistance of 200 mm of brick, so '
          'the insulation must dominate — and it does: 1.0 against 0.2. This is exactly why a low-k, dry, '
          'closed-cell material is chosen.'),
        h4('Limitation'),
        p('The whole benefit is lost if the insulation gets wet or is compressed: water raises k about '
          'twenty-five times, so the surface must be vapour-sealed and the material must be kept dry.'),
    ),
    gu=join(
        p('<b>Thermal conductivity</b> k એટલે એકમ જાડાઈ, એકમ area અને એકમ તાપમાન ફરક માટે પસાર થતી heatનો દર, '
          'W/m·Kમાં. <b>Insulator</b> માટે k જેટલો નાનો તેટલું સારું, અને k નીચેના પરિબળો પર આધારિત છે.'),
        h4('પરિબળો'),
        table(['પરિબળ', 'k પર અસર', 'કારણ'], [
            ['<b>Porosity અને છિદ્રમાં ફસાયેલો gas</b>', 'porosity વધે તેમ k ઘટે; 90 % હવા વાળા foamનો '
             'k ≈ 0.03 W/m·K', 'શાંત હવા ખરાબ conductor છે (k = 0.026), એટલે insulationનું મુખ્ય કામ '
             'ફસાયેલી હવા કરે'],
            ['<b>ભેજ</b>', 'ભીનું insulator સૂકા કરતાં બે-ત્રણ ગણું k આપે', 'પાણીનો k = 0.6 W/m·K, હવા '
             'કરતાં લગભગ 25 ગણો, અને એ છિદ્રો ભરી દે'],
            ['<b>Density</b>', 'density ઘટે તેમ k ઘટે, એક શ્રેષ્ઠ બિંદુ સુધી; એથી નીચે radiationથી k ફરી વધે',
             'heat માટે ઓછા ઘન રસ્તા, પણ બહુ ઓછો ઘન પદાર્થ એટલે મોટા છિદ્રો અને radiation'],
            ['<b>તાપમાન</b>', 'તાપમાન સાથે k ધીમે વધે, અને છિદ્રોમાં radiation T<sup>4</sup> જેટલું વધે',
             'ગરમ gas સારું conduct કરે અને 200 °Cથી ઉપર radiation મહત્ત્વનું બને'],
            ['<b>રચના: fibrous, cellular કે granular</b>', 'બારીક closed-cell રચના સૌથી નીચો k આપે',
             'બારીક cell convection અને radiation રોકે; ખુલ્લા cellમાં હવા ફરે'],
            ['<b>છિદ્રોમાં gasનું pressure</b>', 'gas pressure ઘટાડતાં k ઘટે', 'vacuum gas conduction જ '
             'કાઢી નાખે — vacuum insulation'],
            ['<b>Composition અને crystal structure</b>', 'સાદા crystalline પદાર્થ કરતાં amorphous અને '
             'જટિલ પદાર્થ ઓછું conduct કરે', 'heat lattice vibration અને free electron લઈ જાય; ગોઠવાયેલ '
             'lattice વધુ સારી રીતે લઈ જાય'],
            ['<b>Ageing અને compaction</b>', 'પદાર્થ બેસી જાય, ફાટે કે ભેજ લે ત્યારે k વધે',
             'pore structure તૂટે અને ભેજ અંદર આવે'],
        ]),
        figure(fig.insulation_wall(),
               'Fig. 1.2 · ગરમ દીવાલ પર insulation layer — છિદ્રોમાં શાંત હવા રહે, અને k ઘટે તેમ heat flow '
               'q ઘટે.'),
        h4('ઉકેલેલું ઉદાહરણ — સૂકા insulationની કિંમત'),
        p('Furnaceની દીવાલ 200 mm firebrickની છે જેનો k = 1.0 W/m·K છે. 50 mm insulation ઉમેરતાં જેનો '
          'k = 0.05 W/m·K છે, heat loss ઘટે છે. અંદરની સપાટી 900 °C અને બહારની 60 °C હોય તો પ્રતિ '
          'm<sup>2</sup> બંને સ્થિતિમાં heat flow સરખાવો.'),
        work('Given: brick t<sub>1</sub> = 0.2 m, k<sub>1</sub> = 1.0 W/m·K · insulation '
             't<sub>2</sub> = 0.05 m, k<sub>2</sub> = 0.05 W/m·K · ΔT = 900 − 60 = 840 K · A = 1 m<sup>2</sup>',
             'ફક્ત brick: q = ' + frac('k · A · ΔT', 't') + ' = ' + frac('1.0 × 1 × 840', '0.2'),
             'q = 4200 W/m<sup>2</sup>',
             'Brickનો resistance R<sub>1</sub> = ' + frac('t<sub>1</sub>', 'k<sub>1</sub>') + ' = '
             + frac('0.2', '1.0') + ' = 0.2 m<sup>2</sup>·K/W',
             'Insulationનો resistance R<sub>2</sub> = ' + frac('0.05', '0.05') + ' = 1.0 m<sup>2</sup>·K/W',
             'બંને સાથે: q = ' + frac('ΔT', 'R<sub>1</sub> + R<sub>2</sub>') + ' = '
             + frac('840', '0.2 + 1.0') + ' = ' + frac('840', '1.2')),
        result('Insulation વગર 4200 W/m<sup>2</sup>, સાથે ફક્ત 700 W/m<sup>2</sup> — 83 % બચત'),
        p('Sanity check: k = 0.05 વાળા 50 mm layerનો resistance 200 mm brick કરતાં પાંચ ગણો છે, એટલે '
          'insulation જ પ્રભુત્વ ધરાવે — અને એમ જ છે: 1.0 સામે 0.2. એટલે જ નીચા k વાળો, સૂકો, closed-cell '
          'પદાર્થ પસંદ કરાય.'),
        h4('મર્યાદા'),
        p('Insulation ભીનું થાય કે દબાઈ જાય તો આખો ફાયદો જતો રહે: પાણી k લગભગ પચ્ચીસ ગણો વધારે છે, એટલે '
          'સપાટી vapour-sealed રાખવી પડે અને પદાર્થ સૂકો રાખવો પડે.'),
    ),
))

Q1['cards'].append(dict(
    number='Q.1 (c)', marks=7, q='Describe composition, properties and uses of soda lime glass and glass wool.',
    en=join(
        h4('Soda-lime glass — composition'),
        p('<b>Soda-lime glass</b> is the commonest glass. It is made by melting a batch of silica with '
          'soda and lime: silica forms the network, soda lowers the melting point, and lime gives '
          'durability and stops the glass dissolving in water.'),
        table(['Ingredient', 'Approximate %', 'Function'], [
            ['Silica sand (SiO<sub>2</sub>)', '70–74', 'the glass former; gives the network and the '
             'hardness'],
            ['Soda ash (Na<sub>2</sub>CO<sub>3</sub>)', '12–16', 'flux; lowers the melting point from '
             'about 1700 °C to 1400 °C, so the batch melts easily'],
            ['Limestone / dolomite (CaCO<sub>3</sub>, MgCO<sub>3</sub>)', '10–13', 'stabiliser; makes the '
             'glass durable and chemically resistant'],
            ['Alumina (Al<sub>2</sub>O<sub>3</sub>)', '1–3', 'improves the resistance to devitrification '
             'and the strength'],
            ['Cullet (broken glass)', 'up to 30', 'reduces the melting energy and speeds up the melt'],
        ]),
        h4('Soda-lime glass — properties'),
        bullets('It is <b>transparent</b>, hard and smooth, with a bright finish and good electrical '
                'insulation.',
                '<b>Soft</b> for a glass: it softens at about 700 °C and has a working range that makes it '
                'easy to press, blow and draw, which is why it is the cheapest glass.',
                '<b>Moderate thermal shock resistance</b>, about 60–80 °C — a hot jar put in cold water '
                'cracks it, because the coefficient of expansion is fairly high (about 9 × 10<sup>−6</sup> '
                'per °C).',
                'Good resistance to water and to most chemicals, but hydrofluoric acid and hot strong '
                'alkali attack it.',
                'Density about 2500 kg/m<sup>3</sup>, refractive index about 1.52, tensile strength about '
                '40 MPa but compressive strength about 700 MPa.'),
        h4('Soda-lime glass — uses'),
        table(['Form', 'Use'], [
            ['Sheet and float glass', 'window panes, shop fronts, mirrors, vehicle glazing'],
            ['Hollow ware', 'bottles, jars, tumblers, food containers'],
            ['Pressed ware', 'plates, tumblers, cheap tableware'],
            ['Drawn tube', 'fluorescent lamp tubes, low-temperature thermometer tubes'],
            ['Fibre', 'glass wool for insulation (see below), and the base for cheaper glass-fibre mats'],
        ]),
        h4('Glass wool — composition and manufacture'),
        p('<b>Glass wool</b> is a fibrous form of glass, spun from the same soda-lime (or sometimes '
          'borosilicate) batch. The molten glass is poured onto a rapidly spinning disc or through a '
          'bushing, and the jets of glass are thrown out into fine fibres of 3–10 µm diameter, which are '
          'sprayed with a binder and collected as a mat or a blanket.'),
        figure(fig2.glass_wool(),
               'Fig. 1.3 · Glass wool mat on a hot wall — the crimped fibres trap air, which is what '
               'insulates.'),
        h4('Glass wool — properties'),
        table(['Property', 'Value / behaviour', 'Why it matters'], [
            ['Thermal conductivity', '0.03–0.045 W/m·K', 'the trapped air does the insulating, not the glass'],
            ['Density', '10–100 kg/m<sup>3</sup>', 'very light for the volume it fills'],
            ['Temperature limit', 'up to about 230 °C, and higher for a borosilicate wool',
             'it is for building and pipe insulation, not for a furnace lining'],
            ['Fire behaviour', 'non-combustible; it does not burn, smoke or drip',
             'a fire-safety advantage over foamed plastic'],
            ['Chemical and biological', 'does not rot, is not attacked by mould or insects, and resists '
             'most chemicals', 'long life in a wall or a duct'],
            ['Sound', 'good absorber of sound, because the fibres are fine', 'used in partitions and ducts '
             'for acoustic insulation'],
            ['Health', 'a skin and eye irritant, and a respiratory dust when cut', 'needs gloves, goggles '
             'and a mask while installing'],
        ]),
        h4('Glass wool — uses'),
        bullets('Building insulation: loft rolls, wall cavity batts and ceiling insulation.',
                'Pipe and duct insulation in a plant, often with an aluminium foil facing as the vapour '
                'barrier.',
                'Acoustic lining of partitions, ducts and machine enclosures.',
                'Fire-stop and fire-resistant packing, and the sound-absorbing lining of a generator room.'),
        h4('Worked example — heat loss through a glass-wool lagging'),
        p('A steam pipe of 100 mm outside diameter runs at 180 °C. It is lagged with 50 mm of glass wool '
          'of k = 0.04 W/m·K, and the outside surface is at 40 °C. Find the heat loss per metre and the '
          'saving if the bare pipe (surface coefficient 10 W/m<sup>2</sup>·K) would lose heat at a much '
          'higher rate.'),
        work('Given: d<sub>1</sub> = 0.10 m, d<sub>2</sub> = 0.10 + 2 × 0.05 = 0.20 m · '
             'k = 0.04 W/m·K · T<sub>1</sub> = 180 °C, T<sub>2</sub> = 40 °C · L = 1 m',
             'For a cylinder, q = ' + frac('2 π k L (T<sub>1</sub> − T<sub>2</sub>)',
                                           'ln(d<sub>2</sub>/d<sub>1</sub>)'),
             'Substitute: q = ' + frac('2 × 3.14 × 0.04 × 1 × 140', 'ln(0.20/0.10)'),
             'ln 2 = 0.693, so q = ' + frac('35.19', '0.693')),
        result('Heat loss ≈ 50.8 W per metre of pipe'),
        p('Sanity check: 50 W/m is a normal figure for a lagged 100 mm steam line — a bare pipe in still '
          'air would lose several hundred W/m, so the lagging is doing its job.'),
        h4('Limitation of soda-lime glass'),
        p('Soda-lime glass cannot be used where a large temperature difference occurs, as in an oven door '
          'or a laboratory flask: it cracks on thermal shock. For that duty a <b>borosilicate</b> glass '
          'is used, because the boron oxide in it lowers the expansion coefficient to about a third.'),
    ),
    gu=join(
        h4('Soda-lime glass — રચના'),
        p('<b>Soda-lime glass</b> સૌથી સામાન્ય glass છે. એ silica સાથે soda અને lime ઓગાળીને બનાવાય: '
          'silica network બનાવે, soda melting point ઘટાડે, અને lime મજબૂતાઈ આપે તથા glassને પાણીમાં '
          'ઓગળતું અટકાવે.'),
        table(['ઘટક', 'લગભગ %', 'કામ'], [
            ['Silica sand (SiO<sub>2</sub>)', '70–74', 'glass બનાવનાર; network અને hardness આપે'],
            ['Soda ash (Na<sub>2</sub>CO<sub>3</sub>)', '12–16', 'flux; melting point લગભગ 1700 °Cથી '
             '1400 °C કરે, જેથી batch સહેલાઈથી ઓગળે'],
            ['Limestone / dolomite (CaCO<sub>3</sub>, MgCO<sub>3</sub>)', '10–13', 'stabiliser; glassને '
             'ટકાઉ અને રાસાયણિક રીતે પ્રતિરોધક બનાવે'],
            ['Alumina (Al<sub>2</sub>O<sub>3</sub>)', '1–3', 'devitrification સામે પ્રતિરોધ અને મજબૂતાઈ વધારે'],
            ['Cullet (તૂટેલો કાચ)', '30 સુધી', 'ઓગાળવાની energy ઘટાડે અને ઓગળવાની ઝડપ વધારે'],
        ]),
        h4('Soda-lime glass — ગુણધર્મો'),
        bullets('<b>પારદર્શક</b>, સખત અને ચીકણી સપાટી, ચમકદાર ફિનિશ અને સારું electrical insulation.'),
        'Glassમાં <b>નરમ</b>: લગભગ 700 °C પર નરમ થાય અને working range એટલી પહોળી છે કે press, blow અને '
        'draw કરવું સહેલું — એટલે જ એ સૌથી સસ્તો કાચ.',
        '<b>થોડું thermal shock resistance</b>, લગભગ 60–80 °C — ગરમ બરણી ઠંડા પાણીમાં નાખો તો ફાટે, કારણ કે '
        'expansion coefficient ઊંચો (લગભગ 9 × 10<sup>−6</sup> પ્રતિ °C) છે.',
        'પાણી અને મોટા ભાગના chemical સામે સારો પ્રતિરોધ, પણ hydrofluoric acid અને ગરમ પ્રબળ alkali એના પર '
        'હુમલો કરે.',
        'Density લગભગ 2500 kg/m<sup>3</sup>, refractive index 1.52, tensile strength 40 MPa પણ compressive '
        'strength લગભગ 700 MPa.',
        h4('Soda-lime glass — ઉપયોગ'),
        table(['સ્વરૂપ', 'ઉપયોગ'], [
            ['Sheet અને float glass', 'બારીની પટ્ટી, દુકાનનો આગળનો ભાગ, અરીસો, વાહનનું કાચ'],
            ['Hollow ware', 'બોટલ, બરણી, ગ્લાસ, ખાદ્ય container'],
            ['Pressed ware', 'થાળી, ગ્લાસ, સસ્તું tableware'],
            ['Drawn tube', 'fluorescent lampની tube, નીચા તાપમાનનું thermometer'],
            ['Fibre', 'insulation માટે glass wool, અને સસ્તા glass-fibre matનો આધાર'],
        ]),
        h4('Glass wool — રચના અને બનાવટ'),
        p('<b>Glass wool</b> એ glassનું તંતુમય સ્વરૂપ છે, જે એ જ soda-lime (ક્યારેક borosilicate) batchમાંથી '
          'કતાય. ઓગળેલો કાચ ઝડપથી ફરતી disc પર કે bushingમાંથી પસાર થાય, અને કાચના ધારા 3–10 µm વ્યાસના '
          'બારીક તંતુમાં ફૂટે; એના પર binder છાંટીને mat કે blanket સ્વરૂપે એકઠા કરાય.'),
        figure(fig2.glass_wool(),
               'Fig. 1.3 · ગરમ દીવાલ પર glass wool mat — વળેલા તંતુ હવા ફસાવે, અને એ જ insulation કરે.'),
        h4('Glass wool — ગુણધર્મો'),
        table(['ગુણધર્મ', 'કિંમત / વર્તન', 'કેમ મહત્ત્વનું'], [
            ['Thermal conductivity', '0.03–0.045 W/m·K', 'insulation ફસાયેલી હવા કરે, કાચ નહીં'],
            ['Density', '10–100 kg/m<sup>3</sup>', 'ભરેલા volume માટે ખૂબ હલકું'],
            ['તાપમાન મર્યાદા', 'લગભગ 230 °C સુધી, borosilicate wool માટે વધુ', 'building અને pipe '
             'insulation માટે છે, furnace lining માટે નહીં'],
            ['આગમાં વર્તન', 'બળતું નથી; ધુમાડો કે ટીપું પણ નહીં', 'foamed plastic કરતાં fire-safetyનો ફાયદો'],
            ['રાસાયણિક અને જૈવિક', 'સડતું નથી, ઘાટ કે જીવાત લાગતાં નથી, મોટા ભાગના chemical સામે ટકે',
             'દીવાલ કે ductમાં લાંબું આયુ'],
            ['અવાજ', 'બારીક તંતુ હોવાથી સારું sound absorber', 'partition અને ductમાં acoustic insulation માટે'],
            ['આરોગ્ય', 'ચામડી-આંખમાં બળતરા, અને કાપતી વખતે ધૂળ', 'લગાવતી વખતે મોજાં, ચશ્માં અને માસ્ક જરૂરી'],
        ]),
        h4('Glass wool — ઉપયોગ'),
        bullets('Building insulation: છતનું roll, દીવાલના cavityનું batt અને ceiling insulation.',
                'Plantમાં pipe અને ductનું insulation, ઘણી વાર vapour barrier તરીકે aluminium foil સાથે.',
                'Partition, duct અને machine enclosureનું acoustic lining.',
                'Fire-stop અને fire-resistant packing, તથા generator roomનું sound-absorbing lining.'),
        h4('ઉકેલેલું ઉદાહરણ — glass-wool laggingથી heat loss'),
        p('100 mm બહારના વ્યાસની steam pipe 180 °C પર ચાલે છે. એના પર k = 0.04 W/m·K વાળો 50 mm glass '
          'woolનો lagging છે, અને બહારની સપાટી 40 °C છે. પ્રતિ મીટર heat loss શોધો.'),
        work('Given: d<sub>1</sub> = 0.10 m, d<sub>2</sub> = 0.10 + 2 × 0.05 = 0.20 m · '
             'k = 0.04 W/m·K · T<sub>1</sub> = 180 °C, T<sub>2</sub> = 40 °C · L = 1 m',
             'Cylinder માટે q = ' + frac('2 π k L (T<sub>1</sub> − T<sub>2</sub>)',
                                         'ln(d<sub>2</sub>/d<sub>1</sub>)'),
             'Substitution: q = ' + frac('2 × 3.14 × 0.04 × 1 × 140', 'ln(0.20/0.10)'),
             'ln 2 = 0.693, એટલે q = ' + frac('35.19', '0.693')),
        result('Heat loss ≈ 50.8 W પ્રતિ મીટર pipe'),
        p('Sanity check: lagged 100 mm steam line માટે 50 W/m સામાન્ય આંકડો છે — નીચે lagging વગરની pipe '
          'શાંત હવામાં ઘણા સેંકડો W/m ગુમાવે, એટલે lagging કામ કરે છે.'),
        h4('Soda-lime glassની મર્યાદા'),
        p('Soda-lime glass મોટા temperature ફરકવાળી જગ્યાએ વપરાય નહીં, જેમ કે ovenનું બારણું કે laboratory '
          'flask: thermal shockથી ફાટે. એ કામ માટે <b>borosilicate</b> glass વપરાય, કારણ કે એમાંના boron '
          'oxide expansion coefficient ત્રીજા ભાગનો કરે.'),
    ),
))

Q1['cards'].append(dict(
    number='Q.1 (c)', marks=7, tag='OR', q='Explain composition, properties and uses of ceramic materials.',
    en=join(
        h4('What a ceramic is'),
        p('<b>Ceramic materials</b> are inorganic, non-metallic solids made by shaping a powder or a clay '
          'and then firing it at a high temperature. The firing sinters the particles and forms strong '
          '<b>ionic and covalent bonds</b>, which is the reason for the whole family of properties: hard, '
          'brittle, heat-resistant and electrically insulating.'),
        figure(fig2.ceramic_tree(),
               'Fig. 1.4 · Ceramic materials — traditional, refractory and advanced, with one example of '
               'each.'),
        h4('Composition — by group'),
        table(['Group', 'Typical composition', 'Examples'], [
            ['<b>Traditional (clay based)</b>', 'clay (Al<sub>2</sub>O<sub>3</sub>·2SiO<sub>2</sub>·2H<sub>2</sub>O), '
             'feldspar as a flux, silica as a filler', 'brick, tile, porcelain, sanitaryware, earthenware'],
            ['<b>Refractory</b>', 'alumina, silica, magnesia, chromite, fireclay, silicon carbide',
             'firebrick, silica brick, magnesia brick, crucibles'],
            ['<b>Advanced / technical</b>', 'pure oxides, carbides, nitrides; often with a controlled '
             'microstructure', 'alumina (Al<sub>2</sub>O<sub>3</sub>), zirconia (ZrO<sub>2</sub>), silicon '
             'carbide (SiC), silicon nitride, PZT'],
            ['<b>Cement and concrete (chemically bonded)</b>', 'tricalcium silicate and dicalcium silicate '
             'with gypsum', 'portland cement, concrete, plaster'],
        ]),
        h4('Properties'),
        table(['Property', 'Behaviour', 'The reason'], [
            ['Hardness', 'very high — alumina and SiC are harder than hardened steel',
             'strong directional ionic and covalent bonds resist scratching'],
            ['Brittleness', 'very low toughness; it fails without any plastic deformation',
             'no free electrons and no slip system, so a crack cannot be blunted'],
            ['Strength in compression', 'high; compressive strength 5–10 times the tensile strength',
             'a crack grows only in tension, so a ceramic is used in compression'],
            ['Melting point and hot strength', 'very high — above 1500 °C for most refractories',
             'the bonds are strong, so the lattice does not break down until a high temperature'],
            ['Thermal expansion', 'low to moderate; already low for silica and SiC',
             'few and stiff bonds, so the lattice does not expand much'],
            ['Thermal conductivity', 'low for a porous firebrick, high for a dense SiC',
             'pores insulate; a dense covalent crystal conducts by lattice vibration'],
            ['Electrical behaviour', 'insulators, and some are semiconductors or ionic conductors',
             'no free electrons — the valence electrons are locked in the bonds'],
            ['Chemical resistance', 'excellent against acids and to oxidation at high temperature; '
             'attacked by HF and hot alkali', 'the oxide surface is already the stable phase'],
            ['Density and porosity', 'density 2000–4000 kg/m<sup>3</sup>; porosity from 0 % (dense) to '
             '70 % (insulating brick)', 'the firing temperature and the pore former set the porosity'],
        ]),
        h4('Uses'),
        table(['Application', 'Ceramic used', 'Why this ceramic'], [
            ['Furnace lining, kiln brick', 'fireclay, silica and high-alumina brick', 'refractory and a '
             'low thermal conductivity when porous'],
            ['Electrical insulators, spark plugs', 'porcelain, steatite, alumina', 'high resistivity and '
             'it does not track'],
            ['Cutting tools and abrasives', 'alumina, SiC, cubic boron nitride', 'hardness close to diamond'],
            ['Tiles, sanitaryware, tableware', 'clay-based whiteware, glazed', 'cheap, hard, and easy to '
             'clean'],
            ['Chemical plant', 'alumina, SiC, glass-lined and acid-proof brick', 'resistance to acid and '
             'to a high temperature'],
            ['Sensors and electronics', 'PZT (piezoelectric), zirconia (oxygen sensor), ferrites',
             'the electrical and magnetic property is designed into the ceramic'],
            ['Bio-medical', 'alumina and zirconia', 'inert in the body and wear resistant'],
        ]),
        h4('Worked example — a refractory wall must be thick enough'),
        p('A furnace wall of firebrick of k = 1.2 W/m·K must keep its outside surface below 80 °C when the '
          'inside is at 1100 °C and the outside air takes heat at h = 10 W/m<sup>2</sup>·K. Find the '
          'minimum wall thickness.'),
        work('Given: k = 1.2 W/m·K · T<sub>i</sub> = 1100 °C · T<sub>o</sub> = 80 °C · '
             'T<sub>air</sub> = 30 °C · h = 10 W/m<sup>2</sup>·K',
             'Heat leaving the outer surface = h (T<sub>o</sub> − T<sub>air</sub>) = 10 × (80 − 30)',
             'q = 500 W/m<sup>2</sup>',
             'Through the wall: q = ' + frac('k (T<sub>i</sub> − T<sub>o</sub>)', 't'),
             'So t = ' + frac('k (T<sub>i</sub> − T<sub>o</sub>)', 'q') + ' = '
             + frac('1.2 × (1100 − 80)', '500') + ' = ' + frac('1224', '500')),
        result('Minimum thickness ≈ 2.45 m — which is why a real furnace wall is built of a thin hot-face '
               'brick backed by a thick porous insulating brick'),
        p('Sanity check: 2.45 m of dense firebrick is absurd, so the answer shows that a single material '
          'cannot do the job; a composite wall of 230 mm firebrick plus 230 mm insulating brick is the '
          'practical answer, and this is the design lesson of the calculation.'),
        h4('Limitations'),
        bullets('Ceramics are <b>brittle</b>: they give no warning before they break, and they cannot be '
                'welded or repaired, so a crack means a replacement.',
                'They are difficult to shape and to machine after firing, and firing shrinkage must be '
                'allowed for in the mould.',
                'They have poor thermal shock resistance unless the expansion is low, and they are weak in '
                'tension, so a ceramic part must be loaded in compression.',
                'Porosity makes a ceramic absorb water, which ruins both the insulation and the strength — '
                'hence the glaze on a tile or a sanitaryware piece.'),
    ),
    gu=join(
        h4('Ceramic એટલે શું'),
        p('<b>Ceramic materials</b> એ inorganic, non-metallic ઘન પદાર્થ છે જે powder કે clayને આકાર આપીને '
          'ઊંચા તાપમાને પકાવીને બનાવાય. પકાવવાથી કણો sinter થાય અને મજબૂત <b>ionic તથા covalent bonds</b> '
          'બને — આખા જૂથના ગુણધર્મોનું કારણ એ જ છે: સખત, ભંગુર, ગરમી સહેનાર અને વીજ-અવાહક.'),
        figure(fig2.ceramic_tree(),
               'Fig. 1.4 · Ceramic materials — traditional, refractory અને advanced, દરેકનું એક ઉદાહરણ.'),
        h4('રચના — જૂથ પ્રમાણે'),
        table(['જૂથ', 'સામાન્ય રચના', 'ઉદાહરણ'], [
            ['<b>Traditional (clay આધારિત)</b>', 'clay (Al<sub>2</sub>O<sub>3</sub>·2SiO<sub>2</sub>·2H<sub>2</sub>O), '
             'flux તરીકે feldspar, filler તરીકે silica', 'ઈંટ, ટાઇલ, porcelain, sanitaryware, earthenware'],
            ['<b>Refractory</b>', 'alumina, silica, magnesia, chromite, fireclay, silicon carbide',
             'firebrick, silica brick, magnesia brick, crucible'],
            ['<b>Advanced / technical</b>', 'શુદ્ધ oxide, carbide, nitride; ઘણી વાર નિયંત્રિત '
             'microstructure સાથે', 'alumina, zirconia, silicon carbide, silicon nitride, PZT'],
            ['<b>Cement અને concrete (રાસાયણિક બંધન)</b>', 'tricalcium silicate અને dicalcium silicate સાથે '
             'gypsum', 'portland cement, concrete, plaster'],
        ]),
        h4('ગુણધર્મો'),
        table(['ગુણધર્મ', 'વર્તન', 'કારણ'], [
            ['Hardness', 'ખૂબ ઊંચી — alumina અને SiC hardened steel કરતાં સખત', 'મજબૂત દિશાવાળા ionic અને '
             'covalent bond scratching સામે ટકે'],
            ['Brittleness', 'toughness ખૂબ નીચી; કોઈ plastic deformation વગર તૂટે', 'free electron નહીં અને '
             'slip system નહીં, એટલે crack નરમ (blunt) થઈ શકે નહીં'],
            ['Compressionમાં strength', 'ઊંચી; compressive strength tensile કરતાં 5–10 ગણી', 'crack ફક્ત '
             'tensionમાં વધે, એટલે ceramic compressionમાં વપરાય'],
            ['Melting point અને ગરમીમાં strength', 'ખૂબ ઊંચા — મોટા ભાગના refractory 1500 °Cથી ઉપર',
             'bond મજબૂત હોવાથી lattice ઊંચા તાપમાન સુધી તૂટતું નથી'],
            ['Thermal expansion', 'નીચુંથી મધ્યમ; silica અને SiC માટે પહેલેથી નીચું', 'ઓછા અને સખત bond '
             'હોવાથી lattice વધુ ફેલાતું નથી'],
            ['Thermal conductivity', 'porous firebrick માટે નીચી, ઘન SiC માટે ઊંચી', 'છિદ્રો insulation કરે; '
             'ઘન covalent crystal lattice vibrationથી conduct કરે'],
            ['Electrical વર્તન', 'insulator, અને કેટલાક semiconductor કે ionic conductor', 'free electron '
             'નહીં — valence electron bondમાં બંધાયેલા'],
            ['રાસાયણિક પ્રતિરોધ', 'acid સામે અને ઊંચા તાપમાને oxidation સામે ઉત્તમ; HF અને ગરમ alkali '
             'હુમલો કરે', 'ઓક્સાઇડ સપાટી પહેલેથી સ્થિર phase છે'],
            ['Density અને porosity', 'density 2000–4000 kg/m<sup>3</sup>; porosity 0 % (ઘન)થી 70 % '
             '(insulating brick)', 'firing temperature અને pore former porosity નક્કી કરે'],
        ]),
        h4('ઉપયોગ'),
        table(['ઉપયોગ', 'વપરાતો ceramic', 'કેમ આ ceramic'], [
            ['Furnace lining, kiln ઈંટ', 'fireclay, silica અને high-alumina brick', 'refractory, અને porous '
             'હોય તો નીચી thermal conductivity'],
            ['Electrical insulator, spark plug', 'porcelain, steatite, alumina', 'ઊંચી resistivity અને '
             'track થતું નથી'],
            ['Cutting tool અને abrasive', 'alumina, SiC, cubic boron nitride', 'hardness લગભગ diamond જેટલી'],
            ['ટાઇલ, sanitaryware, tableware', 'clay આધારિત whiteware, glazed', 'સસ્તું, સખત અને સાફ કરવું '
             'સહેલું'],
            ['Chemical plant', 'alumina, SiC, glass-lined અને acid-proof ઈંટ', 'acid અને ઊંચા તાપમાન સામે '
             'પ્રતિરોધ'],
            ['Sensor અને electronics', 'PZT (piezoelectric), zirconia (oxygen sensor), ferrite',
             'ceramicમાં electrical અને magnetic ગુણધર્મ design કરાય'],
            ['Bio-medical', 'alumina અને zirconia', 'શરીરમાં inert અને ઘસારા સામે ટકાઉ'],
        ]),
        h4('ઉકેલેલું ઉદાહરણ — refractory દીવાલ પૂરતી જાડી હોવી જોઈએ'),
        p('k = 1.2 W/m·K વાળી firebrickની furnace દીવાલની બહારની સપાટી 80 °Cથી નીચે રાખવી છે, જ્યારે '
          'અંદર 1100 °C છે અને બહારની હવા h = 10 W/m<sup>2</sup>·Kએ heat લે છે. દીવાલની લઘુતમ જાડાઈ શોધો.'),
        work('Given: k = 1.2 W/m·K · T<sub>i</sub> = 1100 °C · T<sub>o</sub> = 80 °C · '
             'T<sub>air</sub> = 30 °C · h = 10 W/m<sup>2</sup>·K',
             'બહારની સપાટીથી નીકળતી heat = h (T<sub>o</sub> − T<sub>air</sub>) = 10 × (80 − 30)',
             'q = 500 W/m<sup>2</sup>',
             'દીવાલમાંથી: q = ' + frac('k (T<sub>i</sub> − T<sub>o</sub>)', 't'),
             'એટલે t = ' + frac('k (T<sub>i</sub> − T<sub>o</sub>)', 'q') + ' = '
             + frac('1.2 × (1100 − 80)', '500') + ' = ' + frac('1224', '500')),
        result('લઘુતમ જાડાઈ ≈ 2.45 m — એટલે જ ખરી furnace દીવાલ પાતળી hot-face ઈંટ પાછળ જાડી porous '
               'insulating ઈંટથી બનાવાય'),
        p('Sanity check: ઘન firebrickના 2.45 m એ અસંભવ છે, એટલે જવાબ દેખાડે છે કે એક જ પદાર્થ કામ ન કરે; '
          '230 mm firebrick અને 230 mm insulating brickની composite દીવાલ જ વ્યવહારુ જવાબ છે — આ ગણતરીનો '
          'design પાઠ એ જ છે.'),
        h4('મર્યાદાઓ'),
        bullets('Ceramic <b>ભંગુર</b> છે: તૂટતાં પહેલાં ચેતવણી આપતું નથી, અને weld કે repair થઈ શકતું નથી, '
                'એટલે crack એટલે બદલવું પડે.',
                'Firing પછી આકાર આપવો અને machine કરવું મુશ્કેલ, અને firing shrinkage માટે mouldમાં ગણતરી '
                'કરવી પડે.',
                'Expansion નીચું ન હોય તો thermal shock resistance નબળી, અને tensionમાં નબળું, એટલે ceramic '
                'ભાગ compressionમાં જ લોડ લે.',
                'Porosity હોય તો ceramic પાણી શોષે, જે insulation અને strength બંને બગાડે — એટલે ટાઇલ કે '
                'sanitaryware પર glaze કરાય.'),
    ),
))


# ---------------------------------------------------------------- Q2
Q2 = {
    'title_en': 'Q2 · Melting and boiling point, scope, rubber and fibre, stress and creep, varnishes',
    'title_gu': 'પ્ર.2 · ગલન અને ઉત્કલન બિંદુ, અવકાશ, રબર અને ફાઇબર, તણાવ અને ક્રીપ, વાર્નિશ',
    'cards': [],
}

Q2['cards'].append(dict(
    number='Q.2 (a)', marks=3, q='Define melting point and boiling point.',
    en=join(
        p('<b>Melting point</b> is the temperature at which a solid changes to a liquid at a given '
          'pressure — strictly, the temperature at which the solid and the liquid phases are in '
          'equilibrium. For a pure crystalline solid the change happens at a single sharp temperature, '
          'and that temperature is a fingerprint of the substance.'),
        p('<b>Boiling point</b> is the temperature at which the vapour pressure of a liquid equals the '
          'pressure on it, so that bubbles of vapour can form inside the liquid and it boils throughout. '
          'It is quoted at the standard pressure of 1 atm (101.325 kPa) and is then called the '
          '<b>normal boiling point</b>.'),
        table(['Point', 'What it marks', 'Energy involved', 'Example'], [
            ['Melting point', 'solid → liquid at equilibrium', 'latent heat of fusion, e.g. 334 kJ/kg for '
             'ice', 'ice 0 °C, iron 1538 °C, copper 1085 °C'],
            ['Boiling point', 'vapour pressure = external pressure', 'latent heat of vaporisation, e.g. '
             '2257 kJ/kg for water', 'water 100 °C, ammonia −33 °C, mercury 357 °C'],
        ]),
        p('<b>Why an engineer cares:</b> the melting point sets the working temperature of a material — a '
          'solder must melt below 250 °C while a furnace brick must not soften at 1400 °C; the boiling '
          'point sets the temperature at which a refrigerant evaporates or a coolant boils, which is the '
          'basis of a whole refrigeration or heat-transfer design.'),
        p('<b>Note on pressure:</b> the boiling point falls as the pressure falls — water boils at about '
          '45 °C on a mountain at 0.1 bar — which is why an evaporator works under vacuum, while a '
          'pressure cooker raises the boiling point to about 120 °C.'),
    ),
    gu=join(
        p('<b>Melting point</b> એટલે એ તાપમાન જ્યાં આપેલા pressure પર ઘન પ્રવાહીમાં ફેરવાય — ચોક્કસ રીતે, જ્યાં '
          'ઘન અને પ્રવાહી અવસ્થા સંતુલનમાં હોય. શુદ્ધ crystalline ઘન માટે આ ફેરફાર એક જ તીખા તાપમાને થાય, '
          'અને એ તાપમાન એ પદાર્થની ઓળખ છે.'),
        p('<b>Boiling point</b> એટલે એ તાપમાન જ્યાં પ્રવાહીનું vapour pressure એના પરના pressure જેટલું થાય, '
          'એટલે પ્રવાહીની અંદર વરાળના પરપોટા બની શકે અને એ આખું ઉકળે. એ 1 atm (101.325 kPa) પર આપવામાં '
          'આવે અને પછી <b>normal boiling point</b> કહેવાય.'),
        table(['બિંદુ', 'શું દર્શાવે', 'કેટલી energy', 'ઉદાહરણ'], [
            ['Melting point', 'સંતુલને ઘન → પ્રવાહી', 'fusionની latent heat, જેમ કે બરફ માટે 334 kJ/kg',
             'બરફ 0 °C, લોખંડ 1538 °C, તાંબું 1085 °C'],
            ['Boiling point', 'vapour pressure = બહારનું pressure', 'vaporisationની latent heat, જેમ કે પાણી '
             'માટે 2257 kJ/kg', 'પાણી 100 °C, ammonia −33 °C, પારો 357 °C'],
        ]),
        p('<b>Engineerને કેમ જરૂરી:</b> melting point પદાર્થનું કામનું તાપમાન નક્કી કરે — solder 250 °Cથી '
          'નીચે ઓગળવો જોઈએ જ્યારે furnaceની ઈંટ 1400 °C પર નરમ ન પડવી જોઈએ; boiling point એ તાપમાન નક્કી કરે '
          'જ્યાં refrigerant બાષ્પીભવન થાય કે coolant ઉકળે, જે આખા refrigeration કે heat-transfer designનો '
          'આધાર છે.'),
        p('<b>Pressureની નોંધ:</b> pressure ઘટે તેમ boiling point ઘટે — પર્વત પર 0.1 bar પર પાણી લગભગ '
          '45 °C પર ઉકળે — એટલે જ evaporator vacuumમાં ચાલે, જ્યારે pressure cooker boiling point લગભગ '
          '120 °C કરે.'),
    ),
))

Q2['cards'].append(dict(
    number='Q.2 (b)', marks=4, q='Explain scope of material science.',
    en=join(
        p('<b>Material science</b> is the study of the structure of materials and of how that structure '
          'controls their properties, so that a material can be selected, improved or designed for a '
          'given job. Its scope runs from the atom to the plant.'),
        figure(fig.materials_tree(),
               'Fig. 2.1 · The four families of engineering materials — metals, ceramics, polymers and '
               'composites — all studied within material science.'),
        h4('The scope, area by area'),
        table(['Area', 'What is studied', 'Where it is used'], [
            ['<b>Structure and bonding</b>', 'atomic bonding, crystal structure, grains, phases, '
             'defects', 'explains why copper is ductile and glass is brittle'],
            ['<b>Properties and testing</b>', 'mechanical, thermal, electrical, magnetic, chemical '
             'properties and the tests that measure them', 'decides the safe working stress of a part'],
            ['<b>Selection of materials</b>', 'comparing candidates on strength, cost, corrosion, '
             'availability', 'picking a material for a pump body or a pipe'],
            ['<b>Processing and forming</b>', 'casting, rolling, forging, welding, sintering, moulding',
             'a forged shaft is stronger than a cast one of the same steel'],
            ['<b>Heat treatment and improvement</b>', 'annealing, hardening, tempering, alloying',
             'a cutting tool is hardened and tempered to the right hardness'],
            ['<b>Corrosion and degradation</b>', 'rusting, oxidation, stress corrosion, polymer ageing',
             'the reason a pipe is lined, coated or made of stainless steel'],
            ['<b>Failure analysis</b>', 'fatigue, creep, fracture, wear', 'finding out why a shaft broke '
             'and preventing a repeat'],
            ['<b>New materials</b>', 'composites, nano-materials, smart materials, bio-materials',
             'a lighter FRP tank, a zirconia oxygen sensor'],
            ['<b>Economics and ecology</b>', 'cost per unit of property, recyclability, energy of '
             'production', 'choosing a material that is cheap and can be recycled'],
        ]),
        h4('Worked example — why selection matters'),
        p('A tie rod must carry 60 kN in tension. Compare the mass of a steel rod (σ<sub>y</sub> = 250 MPa, '
          'ρ = 7850 kg/m<sup>3</sup>) with an aluminium rod (σ<sub>y</sub> = 150 MPa, ρ = 2700 '
          'kg/m<sup>3</sup>) if the rod is 2 m long and the design stress is half the yield stress.'),
        work('Given: F = 60 × 10<sup>3</sup> N · L = 2 m · steel σ = 125 MPa, ρ = 7850 · '
             'aluminium σ = 75 MPa, ρ = 2700',
             'Steel area A = ' + frac('F', 'σ') + ' = ' + frac('60 × 10<sup>3</sup>', '125 × 10<sup>6</sup>')
             + ' = 4.8 × 10<sup>−4</sup> m<sup>2</sup>',
             'Mass of steel = A · L · ρ = 4.8 × 10<sup>−4</sup> × 2 × 7850 = 7.54 kg',
             'Aluminium area = ' + frac('60 × 10<sup>3</sup>', '75 × 10<sup>6</sup>')
             + ' = 8.0 × 10<sup>−4</sup> m<sup>2</sup>',
             'Mass of aluminium = 8.0 × 10<sup>−4</sup> × 2 × 2700 = 4.32 kg'),
        result('Steel rod 7.5 kg, aluminium rod 4.3 kg — the aluminium rod is 43 % lighter'),
        p('Sanity check: the aluminium needs twice the area but has a third of the density, so the mass is '
          'smaller — which is the whole reason for using aluminium in an aircraft. The engineer reads '
          'this as the property index σ/ρ, and material science is what supplies that number.'),
        h4('Limitation of the scope'),
        p('Material science gives the property data and the mechanism, but the final choice is also '
          'limited by cost, availability, weldability, and the code of the plant — a material with the '
          'best property index may still be rejected because it cannot be welded on site.'),
    ),
    gu=join(
        p('<b>Material science</b> એ પદાર્થોની રચના અને એ રચના એમના ગુણધર્મોને કેવી રીતે નિયંત્રિત કરે એનો '
          'અભ્યાસ છે, જેથી આપેલા કામ માટે પદાર્થ પસંદ કરી શકાય, સુધારી શકાય કે design કરી શકાય. એનો અવકાશ '
          'પરમાણુથી plant સુધી ફેલાય છે.'),
        figure(fig.materials_tree(),
               'Fig. 2.1 · Engineering materialsનાં ચાર કુળ — metals, ceramics, polymers અને composites — '
               'જે material scienceમાં અભ્યાસ થાય.'),
        h4('અવકાશ, ક્ષેત્ર પ્રમાણે'),
        table(['ક્ષેત્ર', 'શું અભ્યાસ થાય', 'ક્યાં વપરાય'], [
            ['<b>રચના અને bonding</b>', 'atomic bonding, crystal structure, grain, phase, defect',
             'તાંબું ductile કેમ અને કાચ brittle કેમ એ સમજાવે'],
            ['<b>ગુણધર્મો અને testing</b>', 'mechanical, thermal, electrical, magnetic, chemical '
             'ગુણધર્મો અને એ માપતી કસોટીઓ', 'ભાગનો સલામત working stress નક્કી કરે'],
            ['<b>પદાર્થની પસંદગી</b>', 'strength, ખર્ચ, corrosion, ઉપલબ્ધતા પર સરખામણી',
             'pump body કે pipe માટે પદાર્થ પસંદ કરવો'],
            ['<b>Processing અને forming</b>', 'casting, rolling, forging, welding, sintering, moulding',
             'એ જ steelમાંથી forged shaft cast કરતાં મજબૂત'],
            ['<b>Heat treatment અને સુધારો</b>', 'annealing, hardening, tempering, alloying',
             'cutting tool સાચી hardness સુધી harden અને temper કરાય'],
            ['<b>Corrosion અને degradation</b>', 'rusting, oxidation, stress corrosion, polymer ageing',
             'એટલે જ pipeને lining, coating કે stainless steelથી બનાવાય'],
            ['<b>Failure analysis</b>', 'fatigue, creep, fracture, wear', 'shaft કેમ તૂટ્યો એ શોધીને ફરી '
             'ન થાય એ ગોઠવવું'],
            ['<b>નવા પદાર્થો</b>', 'composite, nano-material, smart material, bio-material',
             'હલકું FRP ટેન્ક, zirconia oxygen sensor'],
            ['<b>અર્થશાસ્ત્ર અને પર્યાવરણ</b>', 'ગુણધર્મના એકમ દીઠ ખર્ચ, recyclability, ઉત્પાદનની energy',
             'સસ્તો અને recycle થઈ શકે એવો પદાર્થ પસંદ કરવો'],
        ]),
        h4('ઉકેલેલું ઉદાહરણ — પસંદગી કેમ મહત્ત્વની'),
        p('એક tie rodને tensionમાં 60 kN ઉપાડવાનું છે. Steel rod (σ<sub>y</sub> = 250 MPa, ρ = 7850 '
          'kg/m<sup>3</sup>) અને aluminium rod (σ<sub>y</sub> = 150 MPa, ρ = 2700 kg/m<sup>3</sup>)નું '
          'દળ સરખાવો, જ્યારે rod 2 m લાંબો છે અને design stress yieldના અડધા છે.'),
        work('Given: F = 60 × 10<sup>3</sup> N · L = 2 m · steel σ = 125 MPa, ρ = 7850 · '
             'aluminium σ = 75 MPa, ρ = 2700',
             'Steelનું area A = ' + frac('F', 'σ') + ' = ' + frac('60 × 10<sup>3</sup>', '125 × 10<sup>6</sup>')
             + ' = 4.8 × 10<sup>−4</sup> m<sup>2</sup>',
             'Steelનું દળ = A · L · ρ = 4.8 × 10<sup>−4</sup> × 2 × 7850 = 7.54 kg',
             'Aluminiumનું area = ' + frac('60 × 10<sup>3</sup>', '75 × 10<sup>6</sup>')
             + ' = 8.0 × 10<sup>−4</sup> m<sup>2</sup>',
             'Aluminiumનું દળ = 8.0 × 10<sup>−4</sup> × 2 × 2700 = 4.32 kg'),
        result('Steel rod 7.5 kg, aluminium rod 4.3 kg — aluminiumનો rod 43 % હલકો'),
        p('Sanity check: aluminiumને બમણું area જોઈએ પણ density ત્રીજા ભાગની, એટલે દળ ઓછું — એ જ કારણે '
          'વિમાનમાં aluminium વપરાય. Engineer આને σ/ρ property index તરીકે વાંચે, અને એ આંકડો material '
          'science આપે છે.'),
        h4('અવકાશની મર્યાદા'),
        p('Material science property data અને mechanism આપે, પણ અંતિમ પસંદગી ખર્ચ, ઉપલબ્ધતા, weldability અને '
          'plantના codeથી પણ મર્યાદિત હોય — સૌથી સારો property index વાળો પદાર્થ પણ site પર weld ન થાય '
          'તો નકારાય.'),
    ),
))

Q2['cards'].append(dict(
    number='Q.2 (c)', marks=7, q='Describe properties and uses of rubber and fiber.',
    en=join(
        h4('Rubber'),
        p('<b>Rubber</b> is an elastomer: a polymer that can be stretched to several times its length and '
          'returns to the original shape when the load is removed. <b>Natural rubber</b> is '
          '<i>cis</i>-polyisoprene from the latex of the rubber tree; <b>synthetic rubbers</b> such as '
          'SBR, nitrile, neoprene and silicone are made from petroleum. In use the rubber is '
          '<b>vulcanised</b> — heated with sulphur — so that the chains are cross-linked into a network.'),
        h4('Properties of rubber'),
        table(['Property', 'Behaviour', 'Consequence in use'], [
            ['<b>Elasticity</b>', 'it stretches 500–700 % and recovers fully', 'a gasket follows the '
             'movement of a joint, a tyre follows the road'],
            ['<b>Toughness and damping</b>', 'it absorbs energy and damps vibration',
             'engine mounts, anti-vibration pads, shock absorbers'],
            ['<b>Abrasion resistance</b>', 'good, especially for the vulcanised and carbon-black filled '
             'grades', 'tyre tread, conveyor belt, hose cover'],
            ['<b>Impermeability</b>', 'very low permeability to air and water',
             'inner tube, diaphragm, balloon, waterproof cloth'],
            ['<b>Electrical insulation</b>', 'high resistivity', 'cable insulation, gloves, mats'],
            ['<b>Chemical resistance</b>', 'natural rubber swells in oil and petrol; nitrile resists oil, '
             'neoprene resists weathering, silicone resists heat', 'the grade must be matched to the fluid'],
            ['<b>Temperature range</b>', 'about −50 °C to 120 °C for natural, more for silicone',
             'a steam hose needs a special compound'],
            ['<b>Friction</b>', 'high coefficient of friction on a dry surface', 'tyres, brake lining '
             'bonding, footwear'],
        ]),
        h4('Uses of rubber'),
        bullets('<b>Tyres and tubes</b> — the largest single use, with carbon black and sulphur.',
                '<b>Hoses, belts and conveyor belting</b> for water, air, slurry and power transmission.',
                '<b>Gaskets, O-rings, seals and diaphragms</b> — the standard way of sealing a joint in a '
                'chemical plant; the grade is chosen for the fluid.',
                '<b>Insulation and protective goods</b>: cable sheathing, gloves, mats, aprons, footwear.',
                '<b>Vibration and sound control</b>: engine mounts, bridge bearings, rail pads, rubber '
                'tiles.',
                '<b>Domestic and medical</b>: hot-water bottle, eraser, teats, surgical gloves.'),
        h4('Fibre'),
        p('A <b>fibre</b> is a long, thin, flexible thread with a length at least a hundred times its '
          'diameter, used as a textile or as reinforcement. Fibres are <b>natural</b> (cotton, jute, '
          'wool, silk, asbestos) or <b>synthetic</b> (nylon, polyester, acrylic, rayon, glass, carbon, '
          'aramid).'),
        figure(fig.fibre_tree(),
               'Fig. 2.2 · Classification of fibres — natural and synthetic, with two common examples of '
               'each.'),
        h4('Properties of fibre'),
        table(['Property', 'Meaning', 'Example'], [
            ['<b>Tenacity (specific strength)</b>', 'the strength per unit of mass, the key property for a '
             'fibre', 'nylon and aramid are far stronger than cotton for the same mass'],
            ['<b>Finenss and flexibility</b>', 'a fine fibre bends easily without breaking',
             'cotton and wool are fine and soft; glass fibre is fine but brittle'],
            ['<b>Elasticity and recovery</b>', 'how well the fibre returns after stretching',
             'wool and nylon recover well, cotton wrinkles'],
            ['<b>Moisture absorption</b>', 'cotton absorbs 8 %, polyester almost nothing',
             'a cotton shirt is comfortable in summer; polyester dries fast'],
            ['<b>Thermal behaviour</b>', 'most synthetics melt; aramids and glass do not burn easily',
             'a glass-fibre mat is used where a synthetic would melt'],
            ['<b>Chemical resistance</b>', 'polyester and glass resist acids; nylon is attacked by '
             'strong acid', 'a chemical filter cloth is chosen by the fluid'],
            ['<b>Electrical and optical</b>', 'some fibres are insulators, and an optical fibre carries '
             'light', 'optical fibre in communication'],
        ]),
        h4('Uses of fibre'),
        bullets('Clothing and household textiles — cotton, wool, silk, polyester, and their blends.',
                '<b>Industrial textiles</b>: conveyor belt fabric, filter cloth, tyre cord, rope, '
                'tarpaulin, geotextile.',
                '<b>Reinforcement</b>: glass fibre in FRP tanks and pipes, carbon fibre in aircraft and '
                'sports goods, aramid in bullet-proof vests.',
                '<b>Insulation and fire protection</b>: glass wool, asbestos (now restricted), aramid '
                'fire clothing.',
                '<b>Communication</b>: optical fibre in place of copper cable.'),
        h4('Worked example — a fibre rope against a steel wire'),
        p('A rope must carry 10 kN. Compare the mass per metre of a nylon rope (σ = 80 MPa, ρ = 1140 '
          'kg/m<sup>3</sup>) with a steel wire (σ = 400 MPa, ρ = 7850 kg/m<sup>3</sup>), both at a factor '
          'of safety of 2.'),
        work('Given: F = 10 × 10<sup>3</sup> N · nylon σ = 40 MPa, ρ = 1140 · steel σ = 200 MPa, '
             'ρ = 7850 · L = 1 m',
             'Nylon area = ' + frac('10 × 10<sup>3</sup>', '40 × 10<sup>6</sup>')
             + ' = 2.5 × 10<sup>−4</sup> m<sup>2</sup>, mass = 2.5 × 10<sup>−4</sup> × 1140 = 0.285 kg/m',
             'Steel area = ' + frac('10 × 10<sup>3</sup>', '200 × 10<sup>6</sup>')
             + ' = 0.5 × 10<sup>−4</sup> m<sup>2</sup>, mass = 0.5 × 10<sup>−4</sup> × 7850 = 0.393 kg/m'),
        result('Nylon 0.285 kg/m against steel 0.393 kg/m — the fibre rope is about 27 % lighter'),
        p('Sanity check: steel is five times stronger per unit area but nearly seven times denser, so the '
          'fibre wins on mass; this is why a climbing rope and a mooring line are fibre.'),
        h4('Limitations'),
        bullets('Rubber swells in the wrong fluid and degrades in ozone and sunlight unless it is '
                'protected; it also creeps under a steady load and it is flammable.',
                'A fibre loses strength when wet (cotton, aramid), creeps under a steady load (nylon), and '
                'melts or burns (polyester, nylon) — the reason a glass or aramid fibre is used near heat.'),
    ),
    gu=join(
        h4('Rubber'),
        p('<b>Rubber</b> એ elastomer છે: એવો polymer જે પોતાની લંબાઈ કરતાં ઘણી ગણો ખેંચાય અને ભાર કાઢતાં '
          'મૂળ આકારમાં પાછો આવે. <b>Natural rubber</b> રબરના ઝાડના latexમાંથી મળતું <i>cis</i>-polyisoprene '
          'છે; SBR, nitrile, neoprene અને silicone જેવા <b>synthetic rubber</b> petroleumમાંથી બને. વપરાશમાં '
          'રબરને <b>vulcanise</b> કરાય — sulphur સાથે ગરમ કરીને સાંકળો networkમાં cross-link કરાય.'),
        h4('Rubberનાં ગુણધર્મો'),
        table(['ગુણધર્મ', 'વર્તન', 'વપરાશમાં પરિણામ'], [
            ['<b>Elasticity</b>', '500–700 % ખેંચાય અને પૂરેપૂરું પાછું આવે', 'gasket jointની હિલચાલ સાથે '
             'ચાલે, ટાયર રસ્તા સાથે'],
            ['<b>Toughness અને damping</b>', 'energy શોષે અને vibration ઓછું કરે', 'engine mount, '
             'anti-vibration pad, shock absorber'],
            ['<b>Abrasion resistance</b>', 'સારું, ખાસ કરીને vulcanised અને carbon-black ભરેલા gradeમાં',
             'ટાયરની tread, conveyor belt, hoseનું cover'],
            ['<b>Impermeability</b>', 'હવા અને પાણી માટે ખૂબ ઓછી permeability', 'inner tube, diaphragm, '
             'balloon, waterproof કાપડ'],
            ['<b>Electrical insulation</b>', 'ઊંચી resistivity', 'cable insulation, મોજાં, મેટ'],
            ['<b>રાસાયણિક પ્રતિરોધ</b>', 'natural rubber oil-પેટ્રોલમાં ફૂલે; nitrile oil સામે, neoprene '
             'હવામાં, silicone ગરમી સામે ટકે', 'પ્રવાહી પ્રમાણે grade પસંદ કરવો પડે'],
            ['<b>તાપમાન રેન્જ</b>', 'natural માટે લગભગ −50 °C થી 120 °C, silicone માટે વધુ',
             'steam hose માટે ખાસ compound જોઈએ'],
            ['<b>Friction</b>', 'સૂકી સપાટી પર ઊંચો friction coefficient', 'ટાયર, brake liningનું bonding, '
             'બૂટ'],
        ]),
        h4('Rubberના ઉપયોગ'),
        bullets('<b>ટાયર અને tube</b> — સૌથી મોટો વપરાશ, carbon black અને sulphur સાથે.'),
        '<b>Hose, belt અને conveyor belting</b> — પાણી, હવા, slurry અને power transmission માટે.',
        '<b>Gasket, O-ring, seal અને diaphragm</b> — chemical plantમાં joint સીલ કરવાની માનક રીત; grade '
        'પ્રવાહી પ્રમાણે પસંદ કરાય.',
        '<b>Insulation અને રક્ષણાત્મક વસ્તુ</b>: cable sheathing, મોજાં, મેટ, એપ્રન, બૂટ.',
        '<b>Vibration અને અવાજ નિયંત્રણ</b>: engine mount, bridge bearing, rail pad, rubber ટાઇલ.',
        '<b>ઘરેલું અને તબીબી</b>: ગરમ પાણીની બોટલ, રબર, teat, surgical મોજાં.',
        h4('Fibre'),
        p('<b>Fibre</b> એ લાંબું, પાતળું, લચીલું તંતુ છે જેની લંબાઈ વ્યાસ કરતાં ઓછામાં ઓછી સો ગણી હોય, '
          'અને જે textile તરીકે કે reinforcement તરીકે વપરાય. Fibres <b>natural</b> (કપાસ, જ્યૂટ, ઊન, '
          'રેશમ, એસ્બેસ્ટોસ) કે <b>synthetic</b> (nylon, polyester, acrylic, rayon, glass, carbon, aramid) '
          'હોય.'),
        figure(fig.fibre_tree(),
               'Fig. 2.2 · Fibresનું વર્ગીકરણ — natural અને synthetic, દરેકનાં બે સામાન્ય ઉદાહરણ.'),
        h4('Fibreનાં ગુણધર્મો'),
        table(['ગુણધર્મ', 'અર્થ', 'ઉદાહરણ'], [
            ['<b>Tenacity (specific strength)</b>', 'એકમ દળ દીઠ strength, fibre માટે મુખ્ય ગુણધર્મ',
             'એ જ દળ માટે nylon અને aramid કપાસ કરતાં ઘણા મજબૂત'],
            ['<b>Finenss અને flexibility</b>', 'બારીક fibre તૂટ્યા વગર સહેલાઈથી વળે', 'કપાસ અને ઊન બારીક '
             'અને મુલાયમ; glass fibre બારીક પણ ભંગુર'],
            ['<b>Elasticity અને recovery</b>', 'ખેંચાયા પછી કેટલું પાછું આવે', 'ઊન અને nylon સારી રીતે પાછા '
             'આવે, કપાસના સળ ઊભરા પડે'],
            ['<b>ભેજ શોષણ</b>', 'કપાસ 8 % શોષે, polyester લગભગ કંઈ નહીં', 'ઉનાળામાં કપાસનો શર્ટ આરામદાયક; '
             'polyester જલદી સૂકાય'],
            ['<b>ઉષ્મીય વર્તન</b>', 'મોટા ભાગના synthetic ઓગળે; aramid અને glass સહેલાઈથી બળે નહીં',
             'synthetic ઓગળે ત્યાં glass-fibre mat વપરાય'],
            ['<b>રાસાયણિક પ્રતિરોધ</b>', 'polyester અને glass acid સામે ટકે; nylon પર પ્રબળ acid હુમલો કરે',
             'chemical filter cloth પ્રવાહી પ્રમાણે પસંદ કરાય'],
            ['<b>Electrical અને optical</b>', 'કેટલાક fibre insulator, અને optical fibre પ્રકાશ લઈ જાય',
             'communicationમાં optical fibre'],
        ]),
        h4('Fibreના ઉપયોગ'),
        bullets('કપડાં અને ઘરેલું textile — કપાસ, ઊન, રેશમ, polyester અને એમનાં blend.',
                '<b>ઔદ્યોગિક textile</b>: conveyor beltનું કાપડ, filter cloth, ટાયર cord, દોરડું, '
                'tarpaulin, geotextile.',
                '<b>Reinforcement</b>: FRP ટેન્ક અને pipeમાં glass fibre, વિમાન તથા રમતના સામાનમાં carbon '
                'fibre, bullet-proof vestમાં aramid.',
                '<b>Insulation અને આગ રક્ષા</b>: glass wool, એસ્બેસ્ટોસ (હવે મર્યાદિત), aramid fire clothing.',
                '<b>Communication</b>: તાંબાના cableને બદલે optical fibre.'),
        h4('ઉકેલેલું ઉદાહરણ — fibre દોરડું સામે steel wire'),
        p('એક દોરડાએ 10 kN ઉપાડવાનું છે. Nylon દોરડું (σ = 80 MPa, ρ = 1140 kg/m<sup>3</sup>) અને steel '
          'wire (σ = 400 MPa, ρ = 7850 kg/m<sup>3</sup>)નું mass per metre સરખાવો, બંનેમાં factor of safety 2.'),
        work('Given: F = 10 × 10<sup>3</sup> N · nylon σ = 40 MPa, ρ = 1140 · steel σ = 200 MPa, '
             'ρ = 7850 · L = 1 m',
             'Nylonનું area = ' + frac('10 × 10<sup>3</sup>', '40 × 10<sup>6</sup>')
             + ' = 2.5 × 10<sup>−4</sup> m<sup>2</sup>, દળ = 2.5 × 10<sup>−4</sup> × 1140 = 0.285 kg/m',
             'Steelનું area = ' + frac('10 × 10<sup>3</sup>', '200 × 10<sup>6</sup>')
             + ' = 0.5 × 10<sup>−4</sup> m<sup>2</sup>, દળ = 0.5 × 10<sup>−4</sup> × 7850 = 0.393 kg/m'),
        result('Nylon 0.285 kg/m સામે steel 0.393 kg/m — fibre દોરડું લગભગ 27 % હલકું'),
        p('Sanity check: steel એકમ area દીઠ પાંચ ગણું મજબૂત પણ લગભગ સાત ગણું ઘન છે, એટલે દળમાં fibre જીતે; '
          'એટલે જ ચઢવાનું દોરડું અને બંધાણની દોરી fibreની હોય.'),
        h4('મર્યાદાઓ'),
        bullets('રબર ખોટા પ્રવાહીમાં ફૂલે અને ozone તથા સૂર્યપ્રકાશમાં બગડે, જો રક્ષણ ન હોય; સ્થિર ભાર નીચે '
                'creep કરે અને જ્વલનશીલ છે.',
                'Fibre ભીનું થતાં strength ગુમાવે (કપાસ, aramid), સ્થિર ભાર નીચે creep કરે (nylon), અને '
                'ઓગળે કે બળે (polyester, nylon) — એટલે જ ગરમી પાસે glass કે aramid fibre વપરાય.'),
    ),
))

Q2['cards'].append(dict(
    number='Q.2 (a)', marks=3, tag='OR', q='Define stress and creep.',
    en=join(
        p('<b>Stress</b> is the internal resisting force set up in a material per unit area of its cross '
          'section, when it is subjected to an external load. It is measured in N/m<sup>2</sup> or Pa, and '
          'in practice in MPa.'),
        eq('<b>σ = ' + frac('F', 'A') + '</b> &nbsp; where F is the load in N and A the original cross-sectional area in m<sup>2</sup>'),
        p('The <b>strain</b> that goes with it is the change in length per unit original length, '
          'ε = ΔL / L, and it is dimensionless. Three forms are used in design: <b>tensile</b> stress '
          '(pulling), <b>compressive</b> stress (pushing) and <b>shear</b> stress (sliding).'),
        p('<b>Creep</b> is the slow, permanent deformation of a material under a <b>constant</b> load held '
          'for a long time, usually at a high temperature. It is a time-dependent deformation, so a part '
          'that is safe when the load is first applied can still fail months later by creep.'),
        figure(fig2.creep_curve(),
               'Fig. 2.3 · Creep curve — primary, secondary and tertiary stages, ending in fracture.'),
        h4('The three stages of creep'),
        table(['Stage', 'What happens', 'Rate'], [
            ['Primary (I)', 'the metal strain-hardens and the rate falls', 'decreasing'],
            ['Secondary (II)', 'strain-hardening and recovery balance; the rate is nearly constant',
             'steady — used to compare materials and to predict life'],
            ['Tertiary (III)', 'voids and cracks grow, the section thins, the rate rises', 'increasing, '
             'ending in fracture'],
        ]),
        h4('Worked example — stress in a tie rod'),
        p('A tie rod of 20 mm diameter carries a load of 50 kN. Find the stress, and state whether a steel '
          'of yield strength 250 MPa is safe with a factor of safety of 2.'),
        work('Given: d = 20 mm = 0.02 m · F = 50 × 10<sup>3</sup> N · σ<sub>y</sub> = 250 MPa · FOS = 2',
             'Area A = ' + frac('π d<sup>2</sup>', '4') + ' = ' + frac('3.14 × 0.02<sup>2</sup>', '4')
             + ' = 3.14 × 10<sup>−4</sup> m<sup>2</sup>',
             'Stress σ = ' + frac('F', 'A') + ' = ' + frac('50 × 10<sup>3</sup>', '3.14 × 10<sup>−4</sup>'),
             'Allowable stress = ' + frac('σ<sub>y</sub>', 'FOS') + ' = ' + frac('250', '2') + ' = 125 MPa'),
        result('σ = 159 MPa, which is above the allowable 125 MPa — so the rod is <b>not</b> safe; a '
               'larger diameter is needed'),
        p('Sanity check: 159/250 gives a factor of safety of only 1.57 against yield, below the required 2, '
          'so the answer is consistent. A 25 mm rod would give about 102 MPa and would pass.'),
        h4('Where creep matters'),
        p('Creep governs the design of steam turbine blades and pipes, boiler tubes, furnace parts and '
          'nuclear components — the <b>creep strength</b> is the stress that produces a stated small '
          'strain (say 0.1 %) in 100 000 hours at a given temperature, and it is the number a '
          'high-temperature designer uses.'),
    ),
    gu=join(
        p('<b>Stress</b> એટલે બહારનો ભાર પડતાં પદાર્થના cross sectionના એકમ area દીઠ અંદર ઊભો થતો પ્રતિકારક '
          'બળ. એનું એકમ N/m<sup>2</sup> કે Pa, અને વ્યવહારમાં MPa.'),
        eq('<b>σ = ' + frac('F', 'A') + '</b> &nbsp; જ્યાં F એ Nમાં ભાર અને A એ m<sup>2</sup>માં મૂળ cross-sectional area'),
        p('એની સાથેનું <b>strain</b> એટલે મૂળ લંબાઈના એકમ દીઠ લંબાઈમાં ફેરફાર, ε = ΔL / L, અને એ '
          'dimensionless છે. Designમાં ત્રણ સ્વરૂપ વપરાય: <b>tensile</b> stress (ખેંચવું), '
          '<b>compressive</b> stress (દબાવવું) અને <b>shear</b> stress (સરકાવવું).'),
        p('<b>Creep</b> એટલે <b>અચલ</b> ભાર લાંબા સમય સુધી રહેવાથી, સામાન્ય રીતે ઊંચા તાપમાને, પદાર્થનું ધીમું '
          'અને કાયમી વિકૃતિકરણ (deformation). એ સમય પર આધારિત deformation છે, એટલે ભાર પહેલી વાર પડે ત્યારે '
          'સલામત દેખાતો ભાગ પણ મહિનાઓ પછી creepથી તૂટી શકે.'),
        figure(fig2.creep_curve(),
               'Fig. 2.3 · Creep curve — primary, secondary અને tertiary stage, અંતે fracture.'),
        h4('Creepના ત્રણ તબક્કા'),
        table(['તબક્કો', 'શું થાય', 'દર'], [
            ['Primary (I)', 'ધાતુ strain-hardened થાય અને દર ઘટે', 'ઘટતો'],
            ['Secondary (II)', 'strain-hardening અને recovery સંતુલિત થાય; દર લગભગ અચલ',
             'સ્થિર — પદાર્થ સરખાવવા અને આયુ અનુમાન કરવા વપરાય'],
            ['Tertiary (III)', 'void અને crack વધે, section પાતળું થાય, દર વધે', 'વધતો, અંતે fracture'],
        ]),
        h4('ઉકેલેલું ઉદાહરણ — tie rodમાં stress'),
        p('20 mm વ્યાસના tie rod પર 50 kN ભાર છે. Stress શોધો, અને 250 MPa yield strength વાળું steel '
          'factor of safety 2 સાથે સલામત છે કે નહીં કહો.'),
        work('Given: d = 20 mm = 0.02 m · F = 50 × 10<sup>3</sup> N · σ<sub>y</sub> = 250 MPa · FOS = 2',
             'Area A = ' + frac('π d<sup>2</sup>', '4') + ' = ' + frac('3.14 × 0.02<sup>2</sup>', '4')
             + ' = 3.14 × 10<sup>−4</sup> m<sup>2</sup>',
             'Stress σ = ' + frac('F', 'A') + ' = ' + frac('50 × 10<sup>3</sup>', '3.14 × 10<sup>−4</sup>'),
             'Allowable stress = ' + frac('σ<sub>y</sub>', 'FOS') + ' = ' + frac('250', '2') + ' = 125 MPa'),
        result('σ = 159 MPa, જે allowable 125 MPaથી વધુ છે — એટલે rod <b>સલામત નથી</b>; મોટો વ્યાસ જોઈએ'),
        p('Sanity check: 159/250 એટલે yield સામે factor of safety ફક્ત 1.57, જરૂરી 2થી નીચે, એટલે જવાબ '
          'સુસંગત. 25 mm rod લગભગ 102 MPa આપે અને પાસ થાય.'),
        h4('Creep ક્યાં મહત્ત્વનું'),
        p('Creep steam turbine blade અને pipe, boiler tube, furnace part તથા nuclear componentનું design નક્કી '
          'કરે — <b>creep strength</b> એટલે એ stress જે આપેલા તાપમાને 100 000 કલાકમાં નિશ્ચિત નાનું strain '
          '(કહો 0.1 %) ઉપજાવે, અને એ જ આંકડો ઊંચા તાપમાનનો designer વાપરે.'),
    ),
))

Q2['cards'].append(dict(
    number='Q.2 (b)', marks=4, tag='OR', q='Explain factors affecting material properties.',
    en=join(
        p('The properties of a material are not fixed numbers: they are the result of its internal '
          'structure. Anything that changes that structure changes the properties, and that is why the '
          'same steel can be soft or hard, and the same plastic flexible or brittle.'),
        h4('The factors'),
        table(['Factor', 'Effect on properties', 'Example'], [
            ['<b>Composition and alloying elements</b>', 'a small addition changes strength, hardness and '
             'corrosion resistance', '0.8 % C makes steel hard; 18 % Cr and 8 % Ni make it stainless'],
            ['<b>Crystal structure and phase</b>', 'the same metal in a different crystal form has '
             'different properties', 'iron is BCC ferrite at room temperature and FCC austenite above '
             '910 °C, and it is far more ductile as austenite'],
            ['<b>Grain size</b>', 'a finer grain gives higher yield strength and better toughness',
             'the Hall–Petch relation: σ<sub>y</sub> rises as the grain size falls'],
            ['<b>Heat treatment</b>', 'controls the phases, the grain size and the residual stress',
             'quenching and tempering a tool steel; annealing softens it for machining'],
            ['<b>Cold work (strain hardening)</b>', 'raises strength and hardness, lowers ductility',
             'a wire drawn thin is strong but cannot be bent further without cracking'],
            ['<b>Defects: vacancies, dislocations, grain boundaries</b>', 'dislocations and boundaries '
             'strengthen; vacancies aid diffusion', 'a perfect crystal is actually weak'],
            ['<b>Porosity and impurities</b>', 'porosity lowers strength, toughness and conductivity; '
             'inclusions start cracks', 'a casting with gas porosity fails early in fatigue'],
            ['<b>Moisture and environment</b>', 'water lowers the strength of a polymer and the insulation '
             'of a ceramic; corrosion reduces the section', 'wet glass wool loses its insulation value'],
            ['<b>Temperature</b>', 'strength falls and ductility generally rises with temperature; above '
             'about 0.4 T<sub>m</sub> creep appears', 'a steel that is tough at 20 °C creeps at 550 °C'],
            ['<b>Rate of loading and time</b>', 'a fast load gives a brittle response, a slow load a '
             'ductile one; a long load gives creep', 'a plastic part breaks suddenly under impact'],
            ['<b>Specimen size and shape, surface finish</b>', 'a rough surface and a sharp corner raise '
             'the local stress and start a fatigue crack', 'a polished shaft outlasts a rough one'],
        ]),
        h4('Worked example — the effect of grain size'),
        p('The Hall–Petch constants for a low-carbon steel are σ<sub>0</sub> = 120 MPa and k = 0.74 '
          'MPa·m<sup>1/2</sup>. Find the yield strength for a grain size of 0.05 mm and of 0.01 mm, and '
          'state the effect.'),
        work('Given: σ<sub>0</sub> = 120 MPa · k = 0.74 MPa·m<sup>1/2</sup> · d<sub>1</sub> = 0.05 mm = '
             '5 × 10<sup>−5</sup> m · d<sub>2</sub> = 0.01 mm = 1 × 10<sup>−5</sup> m',
             'Formula: σ<sub>y</sub> = σ<sub>0</sub> + ' + frac('k', '√d'),
             'For d<sub>1</sub>: √d = 7.07 × 10<sup>−3</sup>, so ' + frac('0.74', '7.07 × 10<sup>−3</sup>')
             + ' = 104.6 MPa',
             'σ<sub>y1</sub> = 120 + 104.6 = 224.6 MPa',
             'For d<sub>2</sub>: √d = 3.16 × 10<sup>−3</sup>, so ' + frac('0.74', '3.16 × 10<sup>−3</sup>')
             + ' = 234.2 MPa',
             'σ<sub>y2</sub> = 120 + 234.2 = 354.2 MPa'),
        result('224.6 MPa at 0.05 mm against 354.2 MPa at 0.01 mm — a five-fold finer grain gives about '
               '58 % more yield strength'),
        p('Sanity check: k/√d rises as √5 = 2.24 when d falls five times, and 104.6 × 2.24 = 234, exactly '
          'the second value — the arithmetic is consistent, and the lesson is that grain refinement is a '
          'free strengthening method.'),
        h4('Limitations'),
        p('Grain refinement helps only down to a limit, after which the material becomes unstable at high '
          'temperature; and every strengthening method costs something — a stronger steel is less '
          'weldable, a harder surface is more brittle, and a finer grain is lost if the weld or the '
          'heat-affected zone grows the grains again.'),
    ),
    gu=join(
        p('પદાર્થના ગુણધર્મો નિશ્ચિત આંકડા નથી: એ એની અંદરની રચનાનું પરિણામ છે. એ રચના બદલે એવું કંઈ પણ '
          'ગુણધર્મો બદલે, અને એટલે જ એક જ steel નરમ કે સખત, અને એક જ plastic લચીલું કે ભંગુર હોઈ શકે.'),
        h4('પરિબળો'),
        table(['પરિબળ', 'ગુણધર્મો પર અસર', 'ઉદાહરણ'], [
            ['<b>Composition અને alloying element</b>', 'થોડો ઉમેરો strength, hardness અને corrosion '
             'પ્રતિરોધ બદલે', '0.8 % C steelને સખત કરે; 18 % Cr અને 8 % Ni એને stainless કરે'],
            ['<b>Crystal structure અને phase</b>', 'એ જ ધાતુનું બીજું crystal સ્વરૂપ બીજા ગુણધર્મ આપે',
             'લોખંડ રૂમ તાપમાને BCC ferrite અને 910 °Cથી ઉપર FCC austenite, જે ઘણું વધુ ductile'],
            ['<b>Grain size</b>', 'બારીક grain ઊંચી yield strength અને સારી toughness આપે',
             'Hall–Petch સંબંધ: grain size ઘટે તેમ σ<sub>y</sub> વધે'],
            ['<b>Heat treatment</b>', 'phase, grain size અને residual stress નિયંત્રિત કરે',
             'tool steelને quench અને temper કરવું; machining માટે anneal કરીને નરમ કરવું'],
            ['<b>Cold work (strain hardening)</b>', 'strength અને hardness વધારે, ductility ઘટાડે',
             'પાતળું ખેંચેલું wire મજબૂત પણ વધુ વાળી શકાય નહીં'],
            ['<b>Defect: vacancy, dislocation, grain boundary</b>', 'dislocation અને boundary મજબૂતાઈ '
             'આપે; vacancy diffusionમાં મદદ કરે', 'સંપૂર્ણ crystal ખરેખર નબળો હોય'],
            ['<b>Porosity અને impurity</b>', 'porosity strength, toughness અને conductivity ઘટાડે; '
             'inclusion crack શરૂ કરે', 'gas porosity વાળું casting fatigueમાં જલદી તૂટે'],
            ['<b>ભેજ અને પર્યાવરણ</b>', 'પાણી polymerની strength અને ceramicનું insulation ઘટાડે; '
             'corrosion section ઘટાડે', 'ભીનું glass wool insulationની કિંમત ગુમાવે'],
            ['<b>તાપમાન</b>', 'તાપમાન સાથે strength ઘટે અને ductility સામાન્ય રીતે વધે; લગભગ 0.4 '
             'T<sub>m</sub>થી ઉપર creep આવે', '20 °C પર tough steel 550 °C પર creep કરે'],
            ['<b>Loadingનો દર અને સમય</b>', 'ઝડપી ભાર brittle વર્તન, ધીમો ભાર ductile; લાંબો ભાર creep',
             'impactમાં plastic ભાગ અચાનક તૂટે'],
            ['<b>Specimenનું કદ, આકાર, સપાટી</b>', 'ખરબચડી સપાટી અને તીવ્ર ખૂણો local stress વધારીને '
             'fatigue crack શરૂ કરે', 'polished shaft ખરબચડા કરતાં વધુ ટકે'],
        ]),
        h4('ઉકેલેલું ઉદાહરણ — grain sizeની અસર'),
        p('Low-carbon steel માટે Hall–Petch અચલ σ<sub>0</sub> = 120 MPa અને k = 0.74 MPa·m<sup>1/2</sup> છે. '
          '0.05 mm અને 0.01 mm grain size માટે yield strength શોધો અને અસર કહો.'),
        work('Given: σ<sub>0</sub> = 120 MPa · k = 0.74 MPa·m<sup>1/2</sup> · d<sub>1</sub> = 0.05 mm = '
             '5 × 10<sup>−5</sup> m · d<sub>2</sub> = 0.01 mm = 1 × 10<sup>−5</sup> m',
             'Formula: σ<sub>y</sub> = σ<sub>0</sub> + ' + frac('k', '√d'),
             'd<sub>1</sub> માટે: √d = 7.07 × 10<sup>−3</sup>, એટલે ' + frac('0.74', '7.07 × 10<sup>−3</sup>')
             + ' = 104.6 MPa',
             'σ<sub>y1</sub> = 120 + 104.6 = 224.6 MPa',
             'd<sub>2</sub> માટે: √d = 3.16 × 10<sup>−3</sup>, એટલે ' + frac('0.74', '3.16 × 10<sup>−3</sup>')
             + ' = 234.2 MPa',
             'σ<sub>y2</sub> = 120 + 234.2 = 354.2 MPa'),
        result('0.05 mm પર 224.6 MPa સામે 0.01 mm પર 354.2 MPa — પાંચ ગણું બારીક grain લગભગ 58 % વધુ '
               'yield strength આપે'),
        p('Sanity check: d પાંચ ગણું ઘટે ત્યારે k/√d √5 = 2.24 ગણું વધે, અને 104.6 × 2.24 = 234, બરાબર '
          'બીજી કિંમત — ગણતરી સુસંગત છે, અને પાઠ એ કે grain refinement મફત મજબૂતાઈ આપે.'),
        h4('મર્યાદાઓ'),
        p('Grain refinement ફક્ત એક હદ સુધી મદદ કરે, એથી આગળ ઊંચા તાપમાને ધાતુ અસ્થિર બને; અને દરેક '
          'મજબૂતાઈની રીતની કિંમત હોય — વધુ મજબૂત steel ઓછું weldable, સખત સપાટી વધુ ભંગુર, અને weld કે '
          'heat-affected zone grain ફરી મોટું કરે તો બારીક grain જતું રહે.'),
    ),
))

Q2['cards'].append(dict(
    number='Q.2 (c)', marks=7, tag='OR', q='Explain properties, ingredients and uses of varnishes.',
    en=join(
        h4('Definition'),
        p('A <b>varnish</b> is a clear, transparent coating — a solution of a resin or a drying oil in a '
          'solvent — which dries to a hard, glossy, protective film on wood or metal. Unlike a paint it has '
          'no pigment, so the grain or the surface below shows through; its job is protection and finish, '
          'not colour or hiding.'),
        h4('Ingredients'),
        table(['Ingredient', 'Function', 'Typical material', 'If it is missing or wrong'], [
            ['<b>Resin</b> (film former)', 'forms the hard, glossy film and gives the resistance',
             'shellac, copal, rosin, alkyd, polyurethane, phenolic', 'too little resin gives a soft film'],
            ['<b>Oil</b> (in an oil varnish)', 'makes the film flexible and lets it flow out',
             'linseed oil, tung oil, dehydrated castor oil', 'too much oil gives a slow-drying, soft film'],
            ['<b>Solvent / thinner</b>', 'dissolves the resin so it can be brushed, then evaporates',
             'turpentine, white spirit, naphtha, alcohol, water', 'the wrong solvent makes the film '
             'blush or dry too fast'],
            ['<b>Drier (siccative)</b>', 'accelerates the oxidation and drying of the oil',
             'lead, cobalt, manganese and zirconium naphthenates (0.02–0.5 %)', 'too much drier makes '
             'the film brittle and wrinkled'],
            ['<b>Additives (optional)</b>', 'improve flow, UV resistance, matting or anti-skinning',
             'plasticiser, UV absorber, matting agent', 'no UV absorber means early yellowing'],
        ]),
        figure(fig2.varnish_system(),
               'Fig. 2.4 · A three-coat varnish system — the sealer bonds to the wood, the second coat '
               'fills the grain, the top coat gives gloss.'),
        h4('Properties of a good varnish film'),
        table(['Property', 'Why it matters'], [
            ['<b>Transparency and gloss</b>', 'the wood grain must show; the gloss is the finish the '
             'customer sees'],
            ['<b>Adhesion</b>', 'the film must grip the wood and not lift at an edge'],
            ['<b>Hardness with flexibility</b>', 'hard enough to resist a scratch, flexible enough to '
             'follow the movement of the wood without cracking'],
            ['<b>Water and water-vapour resistance</b>', 'the film must keep moisture out, or the wood '
             'swells and the film blisters'],
            ['<b>Chemical resistance</b>', 'resistance to alcohol, alkali and household chemicals — this '
             'is where a polyurethane beats a shellac'],
            ['<b>Weather and UV resistance</b>', 'an exterior varnish needs a UV absorber or it fails by '
             'chalking and peeling'],
            ['<b>Drying time and re-coat time</b>', 'sets the production rate and the number of coats per '
             'day'],
            ['<b>Non-toxic, low odour when dry</b>', 'essential for furniture and for a food area'],
        ]),
        h4('Types'),
        bullets('<b>Oil varnish</b> — resin plus a drying oil; long-oil is flexible (exterior), short-oil is '
                'hard (interior).',
                '<b>Spirit varnish (French polish)</b> — shellac in alcohol; dries fast, is soft, and '
                'whitens with water.',
                '<b>Spar / exterior varnish</b> — phenolic or alkyd with tung oil, plus UV absorbers, for '
                'boats and doors.',
                '<b>Polyurethane varnish</b> — hard, tough and chemical resistant; the standard for floors '
                'and furniture.',
                '<b>Alkyd and acrylic water-borne varnish</b> — a low-odour, low-solvent option.',
                '<b>Lacquer and insulating varnish</b> — nitrocellulose for a fast finish, and a baking '
                'varnish for motor windings and transformer cores.'),
        h4('Uses'),
        table(['Application', 'Why a varnish'], [
            ['Furniture, doors, panelling', 'protects the wood and shows the grain'],
            ['Wooden floors', 'a hard polyurethane film resists wear and is easy to re-coat'],
            ['Boats and exterior wood', 'spar varnish with UV absorbers keeps out water'],
            ['Electrical insulation', 'insulating varnish impregnates a winding and keeps out moisture'],
            ['Metal protection', 'a clear varnish on brass or copper keeps the polish without hiding it'],
            ['Printing and paper', 'a varnish overprint gives gloss and scuff resistance'],
        ]),
        h4('Working — application step and reason'),
        steps(('Step 1', 'Sand the surface and remove all dust. Reason: a varnish film is transparent, so '
                         'every scratch and every speck of dust stays visible, and the film cannot grip a '
                         'loose surface.'),
              ('Step 2', 'Apply a thinned sealer coat and let it soak in. Reason: the first coat must '
                         'penetrate the open grain and bond to the wood, and a thinned coat penetrates '
                         'better.'),
              ('Step 3', 'Sand lightly between coats and wipe off the dust. Reason: the flattening gives '
                         'the next coat a key, and without it the coats do not bond.'),
              ('Step 4', 'Brush on two or three full coats, each thin. Reason: a thin coat dries evenly '
                         'and does not wrinkle; a thick coat skins over and stays soft underneath.'),
              ('Step 5', 'Let the last coat harden fully before use. Reason: the film is still soft while '
                         'the solvent leaves, and handling it early leaves marks that cannot be repaired '
                         'locally.')),
        h4('Worked example — coverage of a varnish'),
        p('A tin holds 4 litres of varnish. One coat gives a wet film of 100 µm, and the varnish has 45 % '
          'solids by volume. Find the dry film thickness per coat and the area one tin covers for two '
          'coats, allowing 10 % loss.'),
        work('Given: volume = 4 L = 4 × 10<sup>−3</sup> m<sup>3</sup> · wet film = 100 µm = 1 × 10<sup>−4</sup> m · '
             'solids = 0.45 · coats = 2 · loss = 10 %',
             'Dry film per coat = 100 × 0.45 = 45 µm',
             'Useful volume = 4 × 0.90 = 3.6 L = 3.6 × 10<sup>−3</sup> m<sup>3</sup>',
             'Wet area for two coats = ' + frac('volume', 'coats × wet film') + ' = '
             + frac('3.6 × 10<sup>−3</sup>', '2 × 1 × 10<sup>−4</sup>')),
        result('Dry film 45 µm per coat; one tin covers about 18 m<sup>2</sup> with two coats'),
        p('Sanity check: 18 m<sup>2</sup> from 4 L is 4.5 m<sup>2</sup> per litre for two coats, which is '
          'the normal coverage quoted on a varnish tin — the answer is consistent.'),
        h4('Limitations'),
        bullets('A varnish film is thin, so it cannot hide a defect and it wears through at a corner; it '
                'needs re-coating every two to five years outdoors.',
                'An oil varnish dries slowly and yellows; a shellac film is soft and whitens with water.',
                'Solvent-borne varnishes release VOCs and are flammable, and they need good ventilation.',
                'The film is only as good as the surface under it — moisture in the wood blisters it, and a '
                'dirty surface makes it peel.'),
    ),
    gu=join(
        h4('વ્યાખ્યા'),
        p('<b>Varnish</b> એ સ્પષ્ટ, પારદર્શક coating છે — solventમાં resin કે drying oilનું દ્રાવણ — જે લાકડા '
          'કે ધાતુ પર સખત, ચમકદાર, રક્ષણાત્મક પાતળો પડ બનાવે. Paintથી વિપરીત એમાં pigment હોતું નથી, એટલે '
          'નીચેનું grain કે સપાટી દેખાય; એનું કામ રક્ષણ અને ફિનિશ છે, રંગ કે ઢાંકવું નહીં.'),
        h4('ઘટકો'),
        table(['ઘટક', 'કામ', 'સામાન્ય material', 'ખૂટે કે ખોટું હોય તો'], [
            ['<b>Resin</b> (film બનાવનાર)', 'સખત, ચમકદાર પડ બનાવે અને પ્રતિરોધ આપે',
             'shellac, copal, rosin, alkyd, polyurethane, phenolic', 'resin ઓછું હોય તો film નરમ'],
            ['<b>Oil</b> (oil varnishમાં)', 'film લચીલો કરે અને પ્રવાહી થવા દે', 'linseed oil, tung oil, '
             'dehydrated castor oil', 'oil વધુ હોય તો ધીમે સૂકાય અને નરમ રહે'],
            ['<b>Solvent / thinner</b>', 'resin ઓગાળે જેથી brush થઈ શકે, પછી ઊડી જાય',
             'turpentine, white spirit, naphtha, alcohol, પાણી', 'ખોટો solvent filmને ધૂંધળો કરે કે જલદી '
             'સૂકવે'],
            ['<b>Drier (siccative)</b>', 'oilનું oxidation અને સૂકવવું ઝડપી કરે', 'lead, cobalt, manganese '
             'અને zirconium naphthenate (0.02–0.5 %)', 'drier વધુ હોય તો film ભંગુર અને સળ ઊભરા પડે'],
            ['<b>Additive (વૈકલ્પિક)</b>', 'flow, UV પ્રતિરોધ, matting કે anti-skinning સુધારે',
             'plasticiser, UV absorber, matting agent', 'UV absorber ન હોય તો જલદી પીળું પડે'],
        ]),
        figure(fig2.varnish_system(),
               'Fig. 2.4 · ત્રણ coatની varnish પદ્ધતિ — sealer લાકડા સાથે જોડાય, બીજો coat grain ભરે, '
               'top coat ચમક આપે.'),
        h4('સારા varnish પડનાં ગુણધર્મો'),
        table(['ગુણધર્મ', 'કેમ મહત્ત્વનું'], [
            ['<b>પારદર્શકતા અને ચમક</b>', 'લાકડાનું grain દેખાવું જોઈએ; ચમક એ ગ્રાહક જોય એ ફિનિશ છે'],
            ['<b>Adhesion</b>', 'પડ લાકડાને પકડે અને કિનારે ઊપડે નહીં'],
            ['<b>Hardness સાથે flexibility</b>', 'ખોદાઈ સામે ટકે એટલું સખત, પણ લાકડાની હિલચાલ સાથે '
             'ચાલે એટલું લચીલું'],
            ['<b>પાણી અને water-vapour પ્રતિરોધ</b>', 'પડ ભેજ બહાર રાખે, નહીં તો લાકડું ફૂલે અને પડ ફુગ્ગા '
             'પડે'],
            ['<b>રાસાયણિક પ્રતિરોધ</b>', 'alcohol, alkali અને ઘરેલું chemical સામે પ્રતિરોધ — અહીં '
             'polyurethane shellacને હરાવે'],
            ['<b>હવામાન અને UV પ્રતિરોધ</b>', 'બહારના varnishને UV absorber જોઈએ, નહીં તો chalk થઈને '
             'ઊપડે'],
            ['<b>સૂકવાનો સમય અને re-coat સમય</b>', 'ઉત્પાદનનો દર અને દિવસના coatની સંખ્યા નક્કી કરે'],
            ['<b>ઝેરી નહીં, સૂકા પછી ઓછી ગંધ</b>', 'ફર્નિચર અને ખાદ્ય જગ્યા માટે જરૂરી'],
        ]),
        h4('પ્રકારો'),
        bullets('<b>Oil varnish</b> — resin અને drying oil; long-oil લચીલું (બહાર), short-oil સખત (અંદર).'),
        '<b>Spirit varnish (French polish)</b> — alcoholમાં shellac; ઝડપથી સૂકાય, નરમ, અને પાણીથી સફેદ પડે.',
        '<b>Spar / exterior varnish</b> — tung oil સાથે phenolic કે alkyd, UV absorber સાથે, હોડી અને '
        'બારણા માટે.',
        '<b>Polyurethane varnish</b> — સખત, ટકાઉ અને રાસાયણિક પ્રતિરોધક; ફર્શ અને ફર્નિચરનું માનક.',
        '<b>Alkyd અને acrylic water-borne varnish</b> — ઓછી ગંધ અને ઓછા solvent વાળો વિકલ્પ.',
        '<b>Lacquer અને insulating varnish</b> — ઝડપી ફિનિશ માટે nitrocellulose, અને motor winding તથા '
        'transformer core માટે baking varnish.',
        h4('ઉપયોગ'),
        table(['ઉપયોગ', 'varnish કેમ'], [
            ['ફર્નિચર, બારણું, panelling', 'લાકડું બચાવે અને grain દેખાડે'],
            ['લાકડાનો ફર્શ', 'સખત polyurethane પડ ઘસારો ઝીલે અને ફરી coat કરવું સહેલું'],
            ['હોડી અને બહારનું લાકડું', 'UV absorber વાળો spar varnish પાણી બહાર રાખે'],
            ['Electrical insulation', 'insulating varnish windingને impregnate કરે અને ભેજ બહાર રાખે'],
            ['ધાતુનું રક્ષણ', 'પિત્તળ કે તાંબા પર સ્પષ્ટ varnish ચમક ઢાંક્યા વગર ટકાવે'],
            ['Printing અને કાગળ', 'overprint varnish ચમક અને ઘસારા સામે રક્ષણ આપે'],
        ]),
        h4('કાર્ય — લગાવવાના સ્ટેપ અને કારણ'),
        steps(('Step 1', 'સપાટી ઘાસીને બધી ધૂળ કાઢો. કારણ: varnishનો પડ પારદર્શક હોય, એટલે દરેક ખરજ અને '
                         'દરેક ધૂળનો કણ દેખાય, અને ઢીલી સપાટીને પડ પકડી શકે નહીં.'),
              ('Step 2', 'પાતળો sealer coat લગાવીને શોષાવા દો. કારણ: પહેલા coatે ખુલ્લા grainમાં ઊતરીને '
                         'લાકડા સાથે જોડાવું પડે, અને પાતળો coat વધુ સારી રીતે ઊતરે.'),
              ('Step 3', 'Coat વચ્ચે હળવું ઘાસો અને ધૂળ લૂછો. કારણ: ઘાસવાથી આગલા coatને પકડ મળે, નહીં તો '
                         'coat એકબીજાને પકડે નહીં.'),
              ('Step 4', 'બે-ત્રણ પૂરા પણ પાતળા coat brush કરો. કારણ: પાતળો coat સરખો સૂકાય અને સળ ઊભરા ન '
                         'પડે; જાડો coat ઉપરથી સુકાઈને અંદર નરમ રહે.'),
              ('Step 5', 'વાપરતાં પહેલાં છેલ્લો coat પૂરો સખત થવા દો. કારણ: solvent નીકળતી વખતે પડ નરમ હોય, '
                         'અને વહેલું અડવાથી એવા ડાઘ પડે જે સ્થાનિક રીતે સુધરે નહીં.')),
        h4('ઉકેલેલું ઉદાહરણ — varnishનું coverage'),
        p('એક ટિનમાં 4 લિટર varnish છે. એક coat 100 µm જાડો wet film આપે છે, અને varnishમાં volume પ્રમાણે '
          '45 % solids છે. પ્રતિ coat dry film thickness અને 10 % loss ગણીને બે coatમાં એક ટિન કેટલું area '
          'ઢાંકે તે શોધો.'),
        work('Given: volume = 4 L = 4 × 10<sup>−3</sup> m<sup>3</sup> · wet film = 100 µm = 1 × 10<sup>−4</sup> m · '
             'solids = 0.45 · coats = 2 · loss = 10 %',
             'પ્રતિ coat dry film = 100 × 0.45 = 45 µm',
             'ઉપયોગી volume = 4 × 0.90 = 3.6 L = 3.6 × 10<sup>−3</sup> m<sup>3</sup>',
             'બે coat માટે wet area = ' + frac('volume', 'coats × wet film') + ' = '
             + frac('3.6 × 10<sup>−3</sup>', '2 × 1 × 10<sup>−4</sup>')),
        result('Dry film પ્રતિ coat 45 µm; એક ટિન બે coatમાં લગભગ 18 m<sup>2</sup> ઢાંકે'),
        p('Sanity check: 4 Lમાંથી 18 m<sup>2</sup> એટલે બે coat માટે પ્રતિ લિટર 4.5 m<sup>2</sup>, જે '
          'varnishની ટિન પર લખેલું સામાન્ય coverage છે — જવાબ સુસંગત.'),
        h4('મર્યાદાઓ'),
        bullets('Varnishનો પડ પાતળો હોય, એટલે ખામી ઢાંકી શકે નહીં અને ખૂણે ઘસાઈ જાય; બહાર દર બે-પાંચ વર્ષે '
                'ફરી coat કરવું પડે.',
                'Oil varnish ધીમે સૂકાય અને પીળું પડે; shellacનો પડ નરમ અને પાણીથી સફેદ પડે.',
                'Solvent વાળા varnish VOC છોડે અને જ્વલનશીલ હોય, એટલે સારી ventilation જોઈએ.',
                'પડ એટલો જ સારો જેટલી એની નીચેની સપાટી — લાકડામાં ભેજ હોય તો પડ ફુગ્ગા પડે, અને સપાટી '
                'ગંદી હોય તો ઊપડી જાય.'),
    ),
))
