"""DI01005021 Winter 2025 — Q5 answer parts."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from paperkit import frac, work, steps, result, table, bullets, numbered, h4, p, eq, figure
import matfigs as fig
import matfigs2 as fig2


def join(*chunks):
    return "\n".join(c for c in chunks if c)


Q5 = {
    'title_en': 'Q5 · Alloys, brass, copper and aluminium, duralumin, bronze, silver and nickel',
    'title_gu': 'પ્ર.5 · એલોય, પિત્તળ, તાંબું અને એલ્યુમિનિયમ, ડ્યુરાલ્યુમિન, બ્રોન્ઝ, ચાંદી અને નિકલ',
    'cards': [],
}

Q5['cards'].append(dict(
    number='Q.5 (a)', marks=3, q='Classify alloys.',
    en=join(
        p('An <b>alloy</b> is a metallic substance made by melting a base metal together with one or more '
          'other elements, so that the product has better properties than the base metal. Alloys are '
          'classified in three ways.'),
        figure(fig2.alloy_tree(),
               'Fig. 5.1 · Alloys classified by the base metal and by the phase that forms.'),
        table(['Basis', 'Classes', 'Examples'], [
            ['<b>By the base metal</b>', 'ferrous alloys · non-ferrous alloys', 'steel, cast iron, '
             'stainless steel / brass, bronze, duralumin, monel'],
            ['<b>By the number of elements</b>', 'binary (2) · ternary (3) · quaternary (4 or more)',
             'Cu–Zn / Cu–Zn–Sn / Al–Cu–Mg–Mn (duralumin)'],
            ['<b>By the phase formed</b>', '<b>solid solution</b> · <b>eutectic</b> · <b>intermetallic '
             'compound</b> · <b>mixture</b>', 'brass (substitutional solid solution) / solder (eutectic) / '
             'cementite Fe<sub>3</sub>C (intermetallic) / pearlite (mixture)'],
            ['<b>By the method of making</b>', 'cast alloy · wrought alloy', 'cast iron / mild steel sheet'],
        ]),
        p('<b>Example:</b> brass is a <b>non-ferrous, binary, substitutional solid solution</b> alloy of '
          'copper and zinc — the zinc atoms simply replace copper atoms in the lattice, which is why brass '
          'is tougher than pure copper but still ductile.'),
        p('<b>Note on the phases:</b> a solid solution is one homogeneous phase and is the most ductile; a '
          'eutectic is a fine lamellar mixture of two phases and has the lowest melting point of the system; '
          'an intermetallic compound is a definite chemical compound, hard and brittle — cementite in steel '
          'is the classic example.'),
    ),
    gu=join(
        p('<b>Alloy</b> એ ધાતુઓનો પદાર્થ છે જે મૂળ ધાતુને એક કે વધુ તત્વો સાથે ઓગાળીને બનાવાય, જેથી ઉત્પાદનના '
          'ગુણધર્મ મૂળ ધાતુ કરતાં સારા થાય. Alloysનું વર્ગીકરણ ત્રણ રીતે થાય.'),
        figure(fig2.alloy_tree(),
               'Fig. 5.1 · Alloysનું મૂળ ધાતુ અને બનતા phase પ્રમાણે વર્ગીકરણ.'),
        table(['આધાર', 'વર્ગ', 'ઉદાહરણ'], [
            ['<b>મૂળ ધાતુ પ્રમાણે</b>', 'ferrous alloy · non-ferrous alloy', 'steel, cast iron, stainless '
             'steel / પિત્તળ, bronze, duralumin, monel'],
            ['<b>તત્વોની સંખ્યા પ્રમાણે</b>', 'binary (2) · ternary (3) · quaternary (4 કે વધુ)',
             'Cu–Zn / Cu–Zn–Sn / Al–Cu–Mg–Mn (duralumin)'],
            ['<b>બનતા phase પ્રમાણે</b>', '<b>solid solution</b> · <b>eutectic</b> · <b>intermetallic '
             'compound</b> · <b>mixture</b>', 'પિત્તળ (substitutional solid solution) / solder (eutectic) / '
             'cementite Fe<sub>3</sub>C (intermetallic) / pearlite (mixture)'],
            ['<b>બનાવવાની રીત પ્રમાણે</b>', 'cast alloy · wrought alloy', 'cast iron / mild steel sheet'],
        ]),
        p('<b>ઉદાહરણ:</b> પિત્તળ એ <b>non-ferrous, binary, substitutional solid solution</b> alloy છે, જે '
          'તાંબું અને જસતનું બને — જસતના પરમાણુ સીધા તાંબાના પરમાણુની જગ્યા લે, એટલે પિત્તળ શુદ્ધ તાંબા કરતાં '
          'મજબૂત પણ હજી ductile રહે.'),
        p('<b>Phaseની નોંધ:</b> solid solution એક સમાન phase છે અને સૌથી ductile; eutectic બે phaseનું બારીક '
          'lamellar મિશ્રણ છે અને systemનું melting point સૌથી નીચું; intermetallic compound નિશ્ચિત રાસાયણિક '
          'સંયોજન છે, સખત અને ભંગુર — steelમાં cementite એનું classic ઉદાહરણ છે.'),
    ),
))

Q5['cards'].append(dict(
    number='Q.5 (b)', marks=4, q='Explain composition and application of brass.',
    en=join(
        h4('Composition'),
        p('<b>Brass</b> is an alloy of <b>copper and zinc</b>, with copper between 55 % and 90 %. The zinc '
          'makes it stronger and harder than pure copper while keeping it ductile and easy to machine, and '
          'the colour changes from red to gold as the zinc rises.'),
        table(['Type', 'Cu', 'Zn', 'Other', 'Character'], [
            ['<b>Commercial / yellow brass</b> (60/40)', '60 %', '40 %', '—', 'cheap, strong, workable cold'],
            ['<b>Alpha brass</b> (70/30, cartridge brass)', '70 %', '30 %', '—', 'the most ductile; deep '
             'drawn into cartridge cases'],
            ['<b>Admiralty brass</b>', '70 %', '29 %', '1 % Sn', 'resists dezincification in sea water'],
            ['<b>Naval brass</b>', '60 %', '39 %', '1 % Sn', 'for marine forgings and valve stems'],
            ['<b>Muntz metal</b>', '60 %', '40 %', '—', 'hot-worked sheet for ship sheathing'],
            ['<b>Free-cutting brass</b>', '62 %', '36 %', '2 % Pb', 'the lead lubricates the chip, so it '
             'machines fast'],
            ['<b>Aluminium brass</b>', '76 %', '22 %', '2 % Al', 'condenser tubes; a protective film forms'],
            ['<b>Silicon / phosphor bronze-type brass</b>', '75–80 %', 'rest', 'Si or P', 'higher strength '
             'and corrosion resistance'],
        ]),
        h4('Properties'),
        bullets('Good <b>strength and hardness</b> — tensile 300–500 MPa, harder than copper.',
                '<b>Excellent ductility and cold workability</b> in the alpha range, so it is rolled and deep '
                'drawn easily.',
                '<b>Very good machinability</b>, especially with 1–2 % lead — free-cutting brass is the '
                'standard material for a turned part.',
                '<b>Corrosion resistance</b> to fresh water and to a marine atmosphere; but it '
                '<b>dezincifies</b> in sea water unless it is inhibited with tin, arsenic or antimony.',
                '<b>High thermal and electrical conductivity</b> — about 28 % of copper\'s, which is enough '
                'for a heat exchanger but not for a conductor.',
                '<b>Non-magnetic and it does not spark</b>, which is why it is used for a tool in a '
                'flammable area.',
                'It <b>work-hardens</b>, so it must be annealed between cold drawing passes; and it '
                'season-cracks in an ammoniacal atmosphere unless it is stress-relieved.'),
        h4('Applications'),
        table(['Application', 'Which brass and why'], [
            ['Plumbing fittings, taps, valves, couplings', 'free-cutting or naval brass — it machines fast, '
             'resists water and takes a thread'],
            ['Cartridge and shell cases, radiator cores', '70/30 cartridge brass — it deep-draws without '
             'cracking'],
            ['Condenser and heat-exchanger tubes', 'admiralty or aluminium brass — the tin or aluminium '
             'stops dezincification'],
            ['Ship sheathing, propeller shaft sleeves', 'Muntz metal — it resists sea water and hot works'],
            ['Decorative hardware, door handles, musical instruments, locks', 'yellow brass — golden colour, '
             'polishes well and casts easily'],
            ['Electrical terminals, socket pins, switch parts', 'brass — conductive, machines well and does '
             'not corrode in a dry room'],
            ['Non-sparking tools (chisel, hammer) for an oil store', 'brass or aluminium bronze — it does '
             'not throw a spark'],
        ]),
        h4('Worked example — the density of a 70/30 brass'),
        p('A brass contains 70 % copper (ρ = 8960 kg/m<sup>3</sup>) and 30 % zinc (ρ = 7140 kg/m<sup>3</sup>) '
          'by mass. Estimate its density, and find the mass of a bush of 40 mm outside diameter, 25 mm bore '
          'and 30 mm length.'),
        work('Given: 70 % Cu, ρ<sub>Cu</sub> = 8960 · 30 % Zn, ρ<sub>Zn</sub> = 7140 · D = 0.040 m · '
             'd = 0.025 m · L = 0.030 m',
             'Rule of mixtures on volume: ' + frac('1', 'ρ') + ' = ' + frac('0.70', '8960') + ' + '
             + frac('0.30', '7140') + ' = 7.81 × 10<sup>−5</sup> + 4.20 × 10<sup>−5</sup> '
             '= 1.201 × 10<sup>−4</sup>',
             'ρ = ' + frac('1', '1.201 × 10<sup>−4</sup>') + ' = 8329 kg/m<sup>3</sup>',
             'Bush volume = ' + frac('π (D<sup>2</sup> − d<sup>2</sup>) L', '4') + ' = '
             + frac('3.14 × (0.0016 − 0.000625) × 0.030', '4') + ' = 2.29 × 10<sup>−5</sup> m<sup>3</sup>',
             'Mass = 8329 × 2.29 × 10<sup>−5</sup>'),
        result('Density 8330 kg/m<sup>3</sup>, mass of the bush ≈ 0.19 kg'),
        p('Sanity check: 8330 kg/m<sup>3</sup> lies between copper (8960) and zinc (7140) and near the '
          'handbook 8530 kg/m<sup>3</sup> for 70/30 brass, so the mixture rule is reasonable.'),
        h4('Limitation'),
        p('Brass <b>dezincifies</b>: in sea water or in a chloride environment the zinc is leached out and a '
          'porous copper plug is left, which then fails. That is why a marine brass must contain an '
          'inhibitor (tin, arsenic or antimony), and why a condenser tube is admiralty or aluminium brass '
          'and never plain 60/40.'),
    ),
    gu=join(
        h4('રચના'),
        p('<b>પિત્તળ (brass)</b> એ <b>તાંબું અને જસત</b>નું alloy છે, જેમાં તાંબું 55 %થી 90 % હોય. જસત એને '
          'શુદ્ધ તાંબા કરતાં મજબૂત અને સખત બનાવે પણ ductile અને machine કરવા સહેલું રાખે, અને જસત વધે તેમ '
          'રંગ લાલથી સોનેરી થાય.'),
        table(['પ્રકાર', 'Cu', 'Zn', 'બીજું', 'લક્ષણ'], [
            ['<b>Commercial / પીળું પિત્તળ</b> (60/40)', '60 %', '40 %', '—', 'સસ્તું, મજબૂત, ઠંડું કામ કરી '
             'શકાય'],
            ['<b>Alpha brass</b> (70/30)', '70 %', '30 %', '—', 'સૌથી ductile; cartridge caseમાં deep draw '
             'થાય'],
            ['<b>Admiralty brass</b>', '70 %', '29 %', '1 % Sn', 'sea waterમાં dezincification સામે ટકે'],
            ['<b>Naval brass</b>', '60 %', '39 %', '1 % Sn', 'marine forging અને valve stem માટે'],
            ['<b>Muntz metal</b>', '60 %', '40 %', '—', 'જહાજના sheathing માટે hot-worked sheet'],
            ['<b>Free-cutting brass</b>', '62 %', '36 %', '2 % Pb', 'લેડ chipને lubricate કરે, એટલે ઝડપી '
             'machining'],
            ['<b>Aluminium brass</b>', '76 %', '22 %', '2 % Al', 'condenser tube; રક્ષણાત્મક પડ બને'],
            ['<b>Silicon / phosphorus વાળું</b>', '75–80 %', 'બાકી', 'Si કે P', 'વધુ strength અને corrosion '
             'પ્રતિરોધ'],
        ]),
        h4('ગુણધર્મો'),
        bullets('સારી <b>strength અને hardness</b> — tensile 300–500 MPa, તાંબા કરતાં સખત.',
                'Alpha રેન્જમાં <b>ઉત્તમ ductility અને cold workability</b>, એટલે roll અને deep draw સહેલું.',
                '<b>ખૂબ સારી machinability</b>, ખાસ કરીને 1–2 % લેડ સાથે — free-cutting brass turned ભાગનું '
                'માનક material છે.',
                'તાજા પાણી અને marine વાતાવરણ સામે <b>corrosion પ્રતિરોધ</b>; પણ sea waterમાં tin, arsenic કે '
                'antimony વગર <b>dezincify</b> થાય.',
                '<b>ઊંચી thermal અને electrical conductivity</b> — તાંબાના લગભગ 28 %, જે heat exchanger માટે '
                'પૂરતી પણ conductor માટે નહીં.',
                '<b>Non-magnetic અને spark થતું નથી</b>, એટલે જ્વલનશીલ જગ્યામાં tool તરીકે વપરાય.',
                '<b>Work-harden</b> થાય, એટલે cold drawing વચ્ચે anneal કરવું પડે; અને ammonia વાળા વાતાવરણમાં '
                'stress-relief ન કરો તો season-crack થાય.'),
        h4('ઉપયોગ'),
        table(['ઉપયોગ', 'કયું પિત્તળ અને કેમ'], [
            ['Plumbing fitting, નળ, valve, coupling', 'free-cutting કે naval brass — ઝડપી machine થાય, પાણી '
             'ઝીલે અને thread લે'],
            ['Cartridge, shell case, radiator core', '70/30 cartridge brass — crack વગર deep draw થાય'],
            ['Condenser અને heat-exchanger tube', 'admiralty કે aluminium brass — tin કે એલ્યુમિનિયમ '
             'dezincification રોકે'],
            ['જહાજનું sheathing, propeller shaft sleeve', 'Muntz metal — sea water ઝીલે અને hot work થાય'],
            ['સજાવટનું hardware, દરવાજાનું handle, વાજિંત્ર, તાળું', 'પીળું પિત્તળ — સોનેરી રંગ, સરસ polish '
             'અને સહેલું casting'],
            ['Electrical terminal, socket pin, switchનો ભાગ', 'પિત્તળ — conductive, machine થાય અને સૂકા '
             'ઓરડામાં કટાય નહીં'],
            ['તેલના ભંડારમાં non-sparking tool (chisel, હથોડો)', 'પિત્તળ કે aluminium bronze — spark ઊડે નહીં'],
        ]),
        h4('ઉકેલેલું ઉદાહરણ — 70/30 પિત્તળની density'),
        p('પિત્તળમાં દળ પ્રમાણે 70 % તાંબું (ρ = 8960 kg/m<sup>3</sup>) અને 30 % જસત (ρ = 7140 '
          'kg/m<sup>3</sup>) છે. Density આંકો, અને 40 mm બહારનો વ્યાસ, 25 mm bore અને 30 mm લંબાઈવાળા bushનું '
          'દળ શોધો.'),
        work('Given: 70 % Cu, ρ<sub>Cu</sub> = 8960 · 30 % Zn, ρ<sub>Zn</sub> = 7140 · D = 0.040 m · '
             'd = 0.025 m · L = 0.030 m',
             'Volume પર mixture rule: ' + frac('1', 'ρ') + ' = ' + frac('0.70', '8960') + ' + '
             + frac('0.30', '7140') + ' = 7.81 × 10<sup>−5</sup> + 4.20 × 10<sup>−5</sup> '
             '= 1.201 × 10<sup>−4</sup>',
             'ρ = ' + frac('1', '1.201 × 10<sup>−4</sup>') + ' = 8329 kg/m<sup>3</sup>',
             'Bushનું volume = ' + frac('π (D<sup>2</sup> − d<sup>2</sup>) L', '4') + ' = '
             + frac('3.14 × (0.0016 − 0.000625) × 0.030', '4') + ' = 2.29 × 10<sup>−5</sup> m<sup>3</sup>',
             'દળ = 8329 × 2.29 × 10<sup>−5</sup>'),
        result('Density 8330 kg/m<sup>3</sup>, bushનું દળ ≈ 0.19 kg'),
        p('Sanity check: 8330 kg/m<sup>3</sup> તાંબા (8960) અને જસત (7140) વચ્ચે અને 70/30 પિત્તળના handbook '
          'મૂલ્ય 8530ની નજીક છે, એટલે mixture rule વાજબી.'),
        h4('મર્યાદા'),
        p('પિત્તળ <b>dezincify</b> થાય: sea water કે chloride વાતાવરણમાં જસત નીકળી જાય અને છિદ્રાળુ તાંબાનો '
          'ટુકડો રહે, જે પછી તૂટે. એટલે જ marine પિત્તળમાં inhibitor (tin, arsenic કે antimony) હોવો જોઈએ, '
          'અને condenser tube admiralty કે aluminium brassની હોય, સાદું 60/40 કદી નહીં.'),
    ),
))

Q5['cards'].append(dict(
    number='Q.5 (c)', marks=7, q='Explain physical properties and application of copper and aluminum.',
    en=join(
        h4('Copper'),
        p('<b>Copper</b> is a reddish, soft, very ductile metal with the second-highest electrical '
          'conductivity of any metal (after silver). It is used both as a conductor and as an alloy base, '
          'and it is one of the few metals that occurs native in nature.'),
        h4('Physical properties of copper'),
        table(['Property', 'Value', 'Engineering consequence'], [
            ['Colour and appearance', 'reddish brown, takes a bright polish',
             'architectural and decorative use, and a copper roof weathers to a green patina'],
            ['Density', '8960 kg/m<sup>3</sup>', 'heavy — 3.3 times that of aluminium'],
            ['Melting point', '1083 °C', 'it is easily melted and cast, but it softens above 200 °C'],
            ['Electrical conductivity', '58 × 10<sup>6</sup> S/m — 100 % IACS', 'the standard conductor: '
             'wires, busbars, windings, printed circuits'],
            ['Thermal conductivity', 'about 400 W/m·K', 'the standard heat-exchanger material: condenser and '
             'radiator tubes, cooking pans'],
            ['Strength', 'annealed 200 MPa, work-hardened 400 MPa', 'it work-hardens strongly, so it can be '
             'drawn to a fine wire'],
            ['Ductility', 'elongation up to 45 %; the finest wire is drawn from it', 'winding wire, cable, '
             'and the deep drawing of a vessel'],
            ['Corrosion resistance', 'excellent in fresh water, in the soil and in a marine atmosphere; it '
             'forms a protective patina', 'plumbing, roofing and a marine fitting'],
            ['Alloying behaviour', 'forms brass, bronze, cupronickel, monel and beryllium copper',
             'the base of a whole family of alloys'],
            ['Magnetic and biological', 'non-magnetic; copper surfaces are antimicrobial',
             'instrument parts, and hospital door handles and touch plates'],
        ]),
        h4('Applications of copper'),
        bullets('<b>Electrical</b> — house wiring, cable, motor and transformer windings, busbars, earthing '
                'and printed circuit boards; about 60 % of all copper goes into electrical use.',
                '<b>Heat transfer</b> — condenser and heat-exchanger tubes, solar panels, cooking pans and '
                'radiators.',
                '<b>Plumbing</b> — water and gas pipe, fittings and valves, where it resists corrosion and '
                'does not support bacteria.',
                '<b>Building</b> — roofing, flashing and cladding, which weather to a green patina.',
                '<b>Alloys</b> — brass, bronze, gunmetal, cupronickel and monel.',
                '<b>Coinage, artwork and antimicrobial surfaces</b>.'),
        h4('Aluminium'),
        p('<b>Aluminium</b> is a silvery, light, corrosion-resistant metal. It is the most abundant metal in '
          'the earth\'s crust, but it is extracted by electrolysis, which is why its cost depends on '
          'electricity. Its great advantage is its <b>strength-to-weight ratio</b>.'),
        h4('Physical properties of aluminium'),
        table(['Property', 'Value', 'Engineering consequence'], [
            ['Colour and appearance', 'silvery white, takes a matt or a bright anodised finish',
             'architectural and consumer use'],
            ['Density', '2700 kg/m<sup>3</sup> — a third of steel', 'the lightest of the common structural '
             'metals: aircraft, transport, portable structures'],
            ['Melting point', '660 °C', 'easy to melt and cast, but its strength falls quickly above 150 °C'],
            ['Electrical conductivity', 'about 62 % of copper, by volume', 'overhead transmission cable '
             '(with a steel core for strength), busbar and foil'],
            ['Thermal conductivity', 'about 205 W/m·K — half of copper', 'heat exchangers, cooking foil, '
             'engine radiators'],
            ['Strength', 'pure 70–100 MPa; alloyed and heat treated up to 600 MPa',
             'duralumin and the 7000 series give an aircraft-grade strength'],
            ['Ductility', 'excellent — foil of 6 µm is rolled', 'packaging foil, deep-drawn cans'],
            ['Corrosion resistance', 'excellent: a thin, self-healing oxide film forms at once',
             'it needs no paint in most atmospheres; it is attacked by alkali and by mercury'],
            ['Reflectivity', 'high for light and heat', 'reflectors, insulation foil, and low-emissivity '
             'roofing'],
            ['Non-magnetic and non-sparking', 'yes', 'instrument housings and a tool in a flammable area'],
        ]),
        h4('Applications of aluminium'),
        bullets('<b>Transport</b> — aircraft structure, vehicle body and engine block, railway coach, '
                'shipping.',
                '<b>Electrical</b> — overhead transmission conductor (ACSR), cable sheathing and busbar.',
                '<b>Packaging</b> — foil, beverage can, aerosol, food tray — where it is light, impermeable '
                'and recyclable.',
                '<b>Building</b> — window and door frame, curtain wall, roofing sheet and cladding.',
                '<b>Domestic and industrial</b> — cooking utensil, pressure cooker, heat exchanger, '
                'furniture.',
                '<b>Alloys</b> — duralumin, Al–Si casting alloy, Al–Mg for a marine part, Al–Li for an '
                'aircraft.'),
        h4('Worked example — the mass saving in a conductor'),
        p('A busbar must carry 800 A with a voltage drop below 40 mV over 4 m. Compare the mass of a copper '
          'bar (ρ<sub>e</sub> = 1.7 × 10<sup>−8</sup> Ω·m, density 8960) with an aluminium bar '
          '(ρ<sub>e</sub> = 2.8 × 10<sup>−8</sup> Ω·m, density 2700), each of 1000 mm<sup>2</sup> section.'),
        work('Given: I = 800 A · L = 4 m · V<sub>max</sub> = 0.040 V · A = 1000 mm<sup>2</sup> = '
             '1 × 10<sup>−3</sup> m<sup>2</sup>',
             'Allowed resistance R = ' + frac('V', 'I') + ' = ' + frac('0.040', '800')
             + ' = 5 × 10<sup>−5</sup> Ω',
             'Copper: R = ' + frac('ρ L', 'A') + ' = ' + frac('1.7 × 10<sup>−8</sup> × 4', '1 × 10<sup>−3</sup>')
             + ' = 6.8 × 10<sup>−5</sup> Ω — too high, so copper must be larger',
             'Aluminium: R = ' + frac('2.8 × 10<sup>−8</sup> × 4', '1 × 10<sup>−3</sup>')
             + ' = 1.12 × 10<sup>−4</sup> Ω — also too high',
             'Mass of copper at this section = 1 × 10<sup>−3</sup> × 4 × 8960 = 35.8 kg',
             'Mass of aluminium at this section = 1 × 10<sup>−3</sup> × 4 × 2700 = 10.8 kg'),
        result('At equal section, aluminium is 70 % lighter (10.8 kg against 35.8 kg), but it needs a '
               '1.65 times larger section to meet the same voltage drop — and even then it is still about '
               'half the mass'),
        p('Sanity check: aluminium carries 62 % of the current of copper for the same section, and it has '
          '30 % of the density, so for equal resistance the mass ratio is 0.30/0.62 = 0.48 — the aluminium '
          'bar is about half the mass, which is why an overhead line is aluminium.'),
        h4('Limitations'),
        bullets('Copper is heavy and expensive, and its price is volatile; it also work-hardens so much that '
                'it must be annealed between drawing passes.',
                'Aluminium has a low melting point and loses strength quickly when hot, so it cannot be used '
                'for a hot part; it is difficult to weld, and it cannot be used in contact with alkali or '
                'mercury.',
                'The two together are worse: a copper–aluminium joint in the presence of moisture makes a '
                'galvanic couple, and the aluminium is corroded away — which is why a bimetallic joint must '
                'use a transition plate.'),
    ),
    gu=join(
        h4('તાંબું'),
        p('<b>તાંબું (copper)</b> લાલાશ પડતી, નરમ અને ખૂબ ductile ધાતુ છે જેની electrical conductivity ચાંદી '
          'પછી બીજા ક્રમે છે. એ conductor તરીકે અને alloyની મૂળ ધાતુ તરીકે બંને રીતે વપરાય, અને એ થોડી ધાતુઓમાં '
          'એક છે જે પ્રકૃતિમાં શુદ્ધ સ્વરૂપે મળે.'),
        h4('તાંબાનાં ભૌતિક ગુણધર્મો'),
        table(['ગુણધર્મ', 'કિંમત', 'એન્જિનિયરિંગ પરિણામ'], [
            ['રંગ અને દેખાવ', 'લાલાશ પડતો બદામી, તેજસ્વી polish લે',
             'સ્થાપત્ય અને સજાવટમાં વપરાય, અને તાંબાની છત લીલી patina બનાવે'],
            ['Density', '8960 kg/m<sup>3</sup>', 'ભારે — એલ્યુમિનિયમ કરતાં 3.3 ગણું'],
            ['Melting point', '1083 °C', 'સહેલાઈથી ઓગળે અને cast થાય, પણ 200 °Cથી ઉપર નરમ પડે'],
            ['Electrical conductivity', '58 × 10<sup>6</sup> S/m — 100 % IACS', 'માનક conductor: wire, '
             'busbar, winding, printed circuit'],
            ['Thermal conductivity', 'લગભગ 400 W/m·K', 'માનક heat-exchanger material: condenser અને radiator '
             'tube, રાંધણું વાસણ'],
            ['Strength', 'annealed 200 MPa, work-hardened 400 MPa', 'ખૂબ work-harden થાય, એટલે બારીક wire '
             'ખેંચી શકાય'],
            ['Ductility', 'elongation 45 % સુધી; સૌથી બારીક wire એની બને', 'winding wire, cable, અને vesselનું '
             'deep drawing'],
            ['Corrosion પ્રતિરોધ', 'તાજા પાણીમાં, જમીનમાં અને marine વાતાવરણમાં ઉત્તમ; રક્ષણાત્મક patina બને',
             'plumbing, છત અને marine fitting'],
            ['Alloy બનાવવાનો ગુણધર્મ', 'પિત્તળ, bronze, cupronickel, monel અને beryllium copper બનાવે',
             'આખા alloy કુળની મૂળ ધાતુ'],
            ['Magnetic અને જૈવિક', 'non-magnetic; તાંબાની સપાટી antimicrobial',
             'instrumentના ભાગ, અને hospitalનાં દરવાજાના handle'],
        ]),
        h4('તાંબાના ઉપયોગ'),
        bullets('<b>Electrical</b> — ઘરની wiring, cable, motor અને transformerનું winding, busbar, earthing '
                'અને PCB; આખા તાંબાના લગભગ 60 % electrical કામમાં જાય.',
                '<b>Heat transfer</b> — condenser અને heat-exchanger tube, solar panel, રાંધણું વાસણ અને '
                'radiator.',
                '<b>Plumbing</b> — પાણી અને gasની pipe, fitting અને valve, જ્યાં એ કટાય નહીં અને bacteria '
                'ટકાવે.',
                '<b>Building</b> — છત, flashing અને cladding, જે લીલી patina બનાવે.',
                '<b>Alloys</b> — પિત્તળ, bronze, gunmetal, cupronickel અને monel.',
                '<b>Coinage, કલાકૃતિ અને antimicrobial સપાટી</b>.'),
        h4('એલ્યુમિનિયમ'),
        p('<b>એલ્યુમિનિયમ</b> ચાંદી જેવી, હલકી અને corrosion-resistant ધાતુ છે. એ ભૂસ્તળમાં સૌથી વધુ મળતી '
          'ધાતુ છે, પણ electrolysisથી નીકળે, એટલે એનો ખર્ચ વીજળી પર આધારિત. એનો મુખ્ય ફાયદો '
          '<b>strength-to-weight ratio</b> છે.'),
        h4('એલ્યુમિનિયમનાં ભૌતિક ગુણધર્મો'),
        table(['ગુણધર્મ', 'કિંમત', 'એન્જિનિયરિંગ પરિણામ'], [
            ['રંગ અને દેખાવ', 'ચાંદી જેવો સફેદ, matt કે તેજસ્વી anodised ફિનિશ લે',
             'સ્થાપત્ય અને ગ્રાહક વપરાશ'],
            ['Density', '2700 kg/m<sup>3</sup> — steelના ત્રીજા ભાગનું', 'સામાન્ય structural ધાતુઓમાં સૌથી '
             'હલકું: વિમાન, વાહન, ઊપાડી શકાય એવી રચના'],
            ['Melting point', '660 °C', 'ઓગાળવું અને cast કરવું સહેલું, પણ 150 °C પછી strength ઝડપથી ઘટે'],
            ['Electrical conductivity', 'તાંબાના લગભગ 62 % (volume પ્રમાણે)', 'ઓવરહેડ transmission cable '
             '(strength માટે steel core સાથે), busbar અને foil'],
            ['Thermal conductivity', 'લગભગ 205 W/m·K — તાંબાના અડધું', 'heat exchanger, રાંધણું foil, engineનું '
             'radiator'],
            ['Strength', 'શુદ્ધ 70–100 MPa; alloy અને heat-treated 600 MPa સુધી', 'duralumin અને 7000 series '
             'વિમાન જેવી strength આપે'],
            ['Ductility', 'ઉત્તમ — 6 µmનું foil roll થાય', 'packaging foil, deep-drawn કેન'],
            ['Corrosion પ્રતિરોધ', 'ઉત્તમ: તરત જ પાતળો, પોતે સુધરતો oxide પડ બને', 'મોટા ભાગના વાતાવરણમાં '
             'paint ન જોઈએ; alkali અને mercury એના પર હુમલો કરે'],
            ['Reflectivity', 'પ્રકાશ અને ગરમી માટે ઊંચી', 'reflector, insulation foil, અને low-emissivity છત'],
            ['Non-magnetic અને non-sparking', 'હા', 'instrument housing અને જ્વલનશીલ જગ્યામાં tool'],
        ]),
        h4('એલ્યુમિનિયમના ઉપયોગ'),
        bullets('<b>વાહન</b> — વિમાનની રચના, વાહનનું body અને engine block, રેલનો coach, જહાજ.'
                '<b>Electrical</b> — ઓવરહેડ transmission conductor (ACSR), cable sheathing અને busbar.',
                '<b>Packaging</b> — foil, પીણાનું કેન, aerosol, ખાદ્ય tray — જ્યાં હલકું, અભેદ્ય અને '
                'recyclable જોઈએ.',
                '<b>Building</b> — બારી-દરવાજાની frame, curtain wall, છતની sheet અને cladding.',
                '<b>ઘરેલું અને ઔદ્યોગિક</b> — રાંધણું વાસણ, pressure cooker, heat exchanger, ફર્નિચર.',
                '<b>Alloys</b> — duralumin, Al–Si casting alloy, marine ભાગ માટે Al–Mg, વિમાન માટે Al–Li.'),
        h4('ઉકેલેલું ઉદાહરણ — conductorમાં દળની બચત'),
        p('એક busbarે 4 m લંબાઈ પર 40 mVથી ઓછા voltage drop સાથે 800 A લેવાનું છે. 1000 mm<sup>2</sup> '
          'sectionવાળા તાંબાના bar (ρ<sub>e</sub> = 1.7 × 10<sup>−8</sup> Ω·m, density 8960) અને '
          'એલ્યુમિનિયમના bar (ρ<sub>e</sub> = 2.8 × 10<sup>−8</sup> Ω·m, density 2700)નું દળ સરખાવો.'),
        work('Given: I = 800 A · L = 4 m · V<sub>max</sub> = 0.040 V · A = 1000 mm<sup>2</sup> = '
             '1 × 10<sup>−3</sup> m<sup>2</sup>',
             'માન્ય resistance R = ' + frac('V', 'I') + ' = ' + frac('0.040', '800')
             + ' = 5 × 10<sup>−5</sup> Ω',
             'તાંબું: R = ' + frac('ρ L', 'A') + ' = ' + frac('1.7 × 10<sup>−8</sup> × 4', '1 × 10<sup>−3</sup>')
             + ' = 6.8 × 10<sup>−5</sup> Ω — વધુ, એટલે તાંબું મોટું લેવું પડે',
             'એલ્યુમિનિયમ: R = ' + frac('2.8 × 10<sup>−8</sup> × 4', '1 × 10<sup>−3</sup>')
             + ' = 1.12 × 10<sup>−4</sup> Ω — એ પણ વધુ',
             'આ section પર તાંબાનું દળ = 1 × 10<sup>−3</sup> × 4 × 8960 = 35.8 kg',
             'આ section પર એલ્યુમિનિયમનું દળ = 1 × 10<sup>−3</sup> × 4 × 2700 = 10.8 kg'),
        result('એ જ section પર એલ્યુમિનિયમ 70 % હલકું (35.8 kg સામે 10.8 kg), પણ એ જ voltage drop માટે '
               '1.65 ગણું section માગે — તો પણ દળ લગભગ અડધું જ રહે'),
        p('Sanity check: એ જ section પર એલ્યુમિનિયમ તાંબાના 62 % પ્રવાહ લે અને density 30 % છે, એટલે એ જ '
          'resistance માટે દળનું પ્રમાણ 0.30/0.62 = 0.48 — એલ્યુમિનિયમનો bar લગભગ અડધા દળનો, એટલે જ '
          'ઓવરહેડ લાઇન એલ્યુમિનિયમની હોય.'),
        h4('મર્યાદાઓ'),
        bullets('તાંબું ભારે અને મોંઘું છે, એનો ભાવ વધઘટ કરે; અને એ એટલું work-harden થાય કે drawing વચ્ચે '
                'anneal કરવું પડે.',
                'એલ્યુમિનિયમનું melting point નીચું અને ગરમ થતાં strength ઝડપથી ઘટે, એટલે ગરમ ભાગમાં ન વપરાય; '
                'weld કરવું મુશ્કેલ, અને alkali કે mercuryના સંપર્કમાં ન વપરાય.',
                'બંને ભેગા તો વધુ ખરાબ: ભેજમાં તાંબું–એલ્યુમિનિયમ joint galvanic couple બનાવે અને એલ્યુમિનિયમ '
                'કટી જાય — એટલે bimetallic jointમાં transition plate વાપરવો પડે.'),
    ),
))

Q5['cards'].append(dict(
    number='Q.5 (a)', marks=3, tag='OR', q='List composition and properties of duralumin.',
    en=join(
        h4('Composition'),
        p('<b>Duralumin</b> is a heat-treatable aluminium alloy of the Al–Cu–Mg family, and it was the '
          'first high-strength aluminium alloy, developed for airship and aircraft structures.'),
        table(['Element', 'Content', 'Job'], [
            ['Aluminium', 'about 94 %', 'the base metal — light and corrosion resistant'],
            ['Copper', '3.5–4.5 %', 'the main strengthener; it forms the precipitates on ageing'],
            ['Magnesium', '0.4–1.4 %', 'adds strength and helps the precipitation'],
            ['Manganese', '0.4–1.0 %', 'improves corrosion resistance and limits grain growth'],
            ['Silicon', 'up to 0.7 % (impurity)', 'kept low, because it forms coarse brittle particles'],
            ['Iron', 'up to 0.7 % (impurity)', 'kept low for the same reason'],
        ]),
        h4('Properties'),
        table(['Property', 'Value / behaviour'], [
            ['Density', '2780 kg/m<sup>3</sup> — only 35 % of steel'],
            ['Strength', 'solution treated and aged: tensile 350–450 MPa, yield 250–300 MPa'],
            ['Strength-to-weight ratio', 'as good as a mild steel and better than most, which is the whole '
             'reason for its use'],
            ['Hardness', 'about 100–120 HB in the aged condition'],
            ['Ductility', 'elongation 10–20 % in the aged condition — enough to form but not to deep draw'],
            ['Heat treatment', 'it responds to solution treatment at 500 °C, quenching in water, and '
             'ageing at room temperature for 4–5 days'],
            ['Corrosion resistance', 'poor in the bare condition — it needs cladding (Alclad) or painting, '
             'and it is attacked by sea water'],
            ['Machinability', 'good, but it must be machined in the aged condition'],
            ['Weldability', 'poor — it loses strength at the weld and cracks; it is riveted or bonded '
             'instead'],
            ['High-temperature limit', 'about 150 °C; above that it overages and softens'],
        ]),
        h4('Why the alloying works'),
        p('Copper and magnesium are soluble in aluminium at 500 °C but almost insoluble at room '
          'temperature. Solution treatment dissolves them, quenching traps them in a supersaturated solid '
          'solution, and ageing precipitates fine CuAl<sub>2</sub> and MgZn<sub>2</sub>-type particles that '
          'block dislocation movement — which is the <b>precipitation hardening</b> that gives the strength.'),
        h4('Applications'),
        bullets('Aircraft skin, rib, spar, former and rivet — the classic airframe material.',
                'Vehicle body panels, commercial vehicle frame and rail coach.',
                'Pressure vessel and a light structural member where weight matters.',
                'A light forging: a connecting rod, a wheel hub, a fastener.',
                'Not for a marine part or a hot part, and not for a welded structure.'),
        h4('Worked example — the weight saved in an airframe member'),
        p('A strut must carry 40 kN in tension with a design stress of one-third of the yield strength. '
          'Compare the mass of a duralumin strut (σ<sub>y</sub> = 280 MPa, ρ = 2780) with a mild-steel one '
          '(σ<sub>y</sub> = 250 MPa, ρ = 7850) of 1.5 m length.'),
        work('Given: F = 40 × 10<sup>3</sup> N · FOS = 3 · duralumin σ = 93.3 MPa, ρ = 2780 · '
             'steel σ = 83.3 MPa, ρ = 7850 · L = 1.5 m',
             'Duralumin area = ' + frac('40 × 10<sup>3</sup>', '93.3 × 10<sup>6</sup>')
             + ' = 4.29 × 10<sup>−4</sup> m<sup>2</sup>, mass = 4.29 × 10<sup>−4</sup> × 1.5 × 2780 '
             '= 1.79 kg',
             'Steel area = ' + frac('40 × 10<sup>3</sup>', '83.3 × 10<sup>6</sup>')
             + ' = 4.80 × 10<sup>−4</sup> m<sup>2</sup>, mass = 4.80 × 10<sup>−4</sup> × 1.5 × 7850 '
             '= 5.65 kg'),
        result('Duralumin 1.79 kg against steel 5.65 kg — a saving of 68 %'),
        p('Sanity check: duralumin is slightly stronger than the steel used here and less than half as '
          'dense, so a saving of about two-thirds is exactly what the property ratio predicts — and that is '
          'why the airframe is duralumin.'),
        h4('Limitations and safety'),
        p('Duralumin corrodes badly in sea water and in contact with steel, so it is clad with pure '
          'aluminium (Alclad) or painted; it cannot be welded; and its strength falls above 150 °C. Its '
          'fatigue behaviour is what limits an aircraft structure, which is why the design uses a safe-life '
          'or a damage-tolerance approach rather than a simple static factor.'),
    ),
    gu=join(
        h4('રચના'),
        p('<b>ડ્યુરાલ્યુમિન (duralumin)</b> એ Al–Cu–Mg કુળનું heat-treatable એલ્યુમિનિયમ alloy છે, અને એ '
          'પહેલું ઊંચી strength વાળું એલ્યુમિનિયમ alloy હતું, જે airship અને વિમાનની રચના માટે વિકસાવાયું.'),
        table(['તત્વ', 'પ્રમાણ', 'કામ'], [
            ['એલ્યુમિનિયમ', 'લગભગ 94 %', 'મૂળ ધાતુ — હલકી અને corrosion-resistant'],
            ['તાંબું', '3.5–4.5 %', 'મુખ્ય મજબૂતાઈ આપનાર; ageingમાં precipitate બનાવે'],
            ['મેગ્નેશિયમ', '0.4–1.4 %', 'strength વધારે અને precipitationમાં મદદ કરે'],
            ['મેંગેનીઝ', '0.4–1.0 %', 'corrosion પ્રતિરોધ સુધારે અને grain વૃદ્ધિ મર્યાદિત કરે'],
            ['Silicon', '0.7 % સુધી (impurity)', 'નીચું રાખાય, કારણ કે જાડા ભંગુર કણ બનાવે'],
            ['લોખંડ', '0.7 % સુધી (impurity)', 'એ જ કારણે નીચું રાખાય'],
        ]),
        h4('ગુણધર્મો'),
        table(['ગુણધર્મ', 'કિંમત / વર્તન'], [
            ['Density', '2780 kg/m<sup>3</sup> — steelના ફક્ત 35 %'],
            ['Strength', 'solution treated અને aged: tensile 350–450 MPa, yield 250–300 MPa'],
            ['Strength-to-weight ratio', 'mild steel જેટલું અને મોટા ભાગના કરતાં સારું — એ જ એના વપરાશનું '
             'કારણ'],
            ['Hardness', 'aged સ્થિતિમાં લગભગ 100–120 HB'],
            ['Ductility', 'aged સ્થિતિમાં elongation 10–20 % — form થાય પણ deep draw નહીં'],
            ['Heat treatment', '500 °C પર solution treatment, પાણીમાં quench, અને ઓરડાના તાપમાને 4–5 દિવસ '
             'ageing'],
            ['Corrosion પ્રતિરોધ', 'ખુલ્લી સ્થિતિમાં નબળો — cladding (Alclad) કે paint જોઈએ, અને sea water '
             'એના પર હુમલો કરે'],
            ['Machinability', 'સારી, પણ aged સ્થિતિમાં જ machine કરવું પડે'],
            ['Weldability', 'નબળી — weld પર strength જાય અને crack પડે; એટલે rivet કે bonding વપરાય'],
            ['ઊંચા તાપમાનની મર્યાદા', 'લગભગ 150 °C; એથી ઉપર overage થઈને નરમ પડે'],
        ]),
        h4('Alloying કેમ કામ કરે'),
        p('તાંબું અને મેગ્નેશિયમ 500 °C પર એલ્યુમિનિયમમાં ઓગળે પણ ઓરડાના તાપમાને લગભગ નહીં. Solution '
          'treatment એમને ઓગાળે, quench સુપરસેચ્યુરેટેડ solid solutionમાં ફસાવે, અને ageing બારીક '
          'CuAl<sub>2</sub> તથા MgZn<sub>2</sub> જેવા કણ precipitate કરે જે dislocationની હિલચાલ રોકે — એ જ '
          '<b>precipitation hardening</b> strength આપે.'),
        h4('ઉપયોગ'),
        bullets('વિમાનનું skin, rib, spar, former અને rivet — classic airframe material.',
                'વાહનનું body panel, commercial vehicleની frame અને rail coach.',
                'જ્યાં વજન મહત્ત્વનું હોય ત્યાં pressure vessel અને હલકો structural ભાગ.',
                'હલકું forging: connecting rod, wheel hub, fastener.',
                'Marine ભાગ કે ગરમ ભાગ માટે નહીં, અને welded structure માટે નહીં.'),
        h4('ઉકેલેલું ઉદાહરણ — airframe ભાગમાં વજનની બચત'),
        p('એક strutે yield strengthના ત્રીજા ભાગના design stress પર 40 kN tension ઉપાડવાનું છે. 1.5 m '
          'લંબાઈના duralumin strut (σ<sub>y</sub> = 280 MPa, ρ = 2780) અને mild steel strut '
          '(σ<sub>y</sub> = 250 MPa, ρ = 7850)નું દળ સરખાવો.'),
        work('Given: F = 40 × 10<sup>3</sup> N · FOS = 3 · duralumin σ = 93.3 MPa, ρ = 2780 · '
             'steel σ = 83.3 MPa, ρ = 7850 · L = 1.5 m',
             'Duraluminનું area = ' + frac('40 × 10<sup>3</sup>', '93.3 × 10<sup>6</sup>')
             + ' = 4.29 × 10<sup>−4</sup> m<sup>2</sup>, દળ = 4.29 × 10<sup>−4</sup> × 1.5 × 2780 = 1.79 kg',
             'Steelનું area = ' + frac('40 × 10<sup>3</sup>', '83.3 × 10<sup>6</sup>')
             + ' = 4.80 × 10<sup>−4</sup> m<sup>2</sup>, દળ = 4.80 × 10<sup>−4</sup> × 1.5 × 7850 = 5.65 kg'),
        result('Duralumin 1.79 kg સામે steel 5.65 kg — 68 % બચત'),
        p('Sanity check: duralumin આંકડામાં વપરાયેલા steel કરતાં થોડું મજબૂત અને અડધાથી પણ ઓછું ઘન છે, '
          'એટલે લગભગ બે-તૃતીયાંશ બચત property ratio જ કહે — અને એટલે જ airframe duraluminનું હોય.'),
        h4('મર્યાદાઓ અને સલામતી'),
        p('Duralumin sea waterમાં અને steelના સંપર્કમાં ખરાબ રીતે કટાય, એટલે એને શુદ્ધ એલ્યુમિનિયમથી clad '
          '(Alclad) કે paint કરાય; એ weld થઈ શકે નહીં; અને 150 °Cથી ઉપર strength ઘટે. વિમાનની રચના '
          'fatigueથી મર્યાદિત થાય, એટલે design સાદા static factorને બદલે safe-life કે damage-tolerance '
          'approach વાપરે.'),
    ),
))

Q5['cards'].append(dict(
    number='Q.5 (b)', marks=4, tag='OR', q='Explain properties and application of bronze.',
    en=join(
        p('<b>Bronze</b> is an alloy of <b>copper and tin</b>, usually with 5–12 % tin, and often with small '
          'additions of phosphorus, zinc, lead or aluminium. It is the oldest alloy known to man, and it is '
          'still the standard bearing and marine material.'),
        h4('Composition of the common bronzes'),
        table(['Type', 'Cu', 'Sn', 'Addition', 'Character'], [
            ['<b>Phosphor bronze</b>', '90–95 %', '5–10 %', '0.1–0.4 % P', 'the standard bearing and spring '
             'alloy; the phosphorus deoxidises and adds wear resistance'],
            ['<b>Gunmetal</b>', '85–88 %', '8–10 %', '2–5 % Zn, 1–2 % Pb', 'cast valve, pump body, a marine '
             'fitting'],
            ['<b>Bell bronze</b>', '78–80 %', '20–22 %', '—', 'hard and sonorous — a bell and a cymbal'],
            ['<b>Aluminium bronze</b>', '90 %', '—', '8–10 % Al, with Fe and Ni', 'the strongest bronze, '
             'resists sea water and does not spark'],
            ['<b>Silicon bronze</b>', '95 %', '—', '3 % Si, 1 % Mn', 'corrosion resistant, used for a '
             'marine fastener'],
            ['<b>Leaded bronze</b>', '85 %', '8 %', '5 % Pb', 'free-cutting bearing bronze'],
        ]),
        h4('Properties'),
        table(['Property', 'Behaviour'], [
            ['Strength', 'tensile 250–400 MPa (phosphor bronze), up to 700 MPa for aluminium bronze'],
            ['Hardness and wear resistance', 'good — better than brass, which is why it is a bearing material'],
            ['Friction and bearing behaviour', 'a low coefficient of friction and it conforms to the shaft, '
             'so it is the standard sleeve bearing and bush'],
            ['Corrosion resistance', 'excellent in sea water, in steam and in a marine atmosphere — better '
             'than brass, because it does not dezincify'],
            ['Ductility', 'good, and it can be rolled, drawn and cast easily; it casts very well, with a '
             'low shrinkage'],
            ['Electrical and thermal conductivity', 'lower than copper — about 10–15 % IACS, so it is a '
             'spring and a bearing material, not a conductor'],
            ['Fatigue and spring properties', 'phosphor bronze is the standard spring material for a '
             'diaphragm, a bellows and an electrical contact'],
            ['Non-sparking and non-magnetic', 'yes — a tool for an oil store and a non-magnetic instrument '
             'part'],
            ['Machinability', 'good, and the leaded grade is free-cutting'],
            ['Cost', 'expensive, because tin is dear — which is why a bronze is used only where it earns '
             'its cost'],
        ]),
        h4('Applications'),
        table(['Application', 'Which bronze and why'], [
            ['Sleeve bearing, bush, thrust washer, worm wheel', 'phosphor or leaded bronze — low friction, '
             'conforms to the shaft, and it survives a temporary oil failure'],
            ['Pump body, valve, impeller, a sea-water fitting', 'gunmetal — it casts to shape and resists '
             'sea water'],
            ['Ship propeller, a marine fastener, a pump shaft', 'aluminium or silicon bronze — the strongest '
             'corrosion resistance in sea water'],
            ['Bell, cymbal, gong and a statue', 'bell bronze — hard and sonorous'],
            ['Spring, diaphragm, bellows and an electrical contact', 'phosphor bronze — good fatigue and '
             'spring properties'],
            ['Non-sparking tool, and a part in a magnetic field', 'aluminium bronze — non-sparking and '
             'non-magnetic'],
        ]),
        h4('Worked example — a bearing pressure check'),
        p('A phosphor-bronze bush of 60 mm bore and 60 mm length carries a radial load of 18 kN at 300 rpm. '
          'Find the bearing pressure and the PV factor, and check them against the usual limits of 15 MPa '
          'and 1.8 MPa·m/s for a bronze bush.'),
        work('Given: d = 0.060 m · L = 0.060 m · W = 18 × 10<sup>3</sup> N · N = 300 rpm',
             'Projected area = d L = 0.060 × 0.060 = 3.6 × 10<sup>−3</sup> m<sup>2</sup>',
             'Bearing pressure p = ' + frac('W', 'd L') + ' = ' + frac('18 × 10<sup>3</sup>', '3.6 × 10<sup>−3</sup>')
             + ' = 5.0 × 10<sup>6</sup> Pa',
             'Surface speed v = ' + frac('π d N', '60') + ' = ' + frac('3.14 × 0.060 × 300', '60')
             + ' = 0.94 m/s',
             'PV = 5.0 × 0.94 = 4.7 MPa·m/s'),
        result('p = 5.0 MPa (within 15 MPa) but PV = 4.7 MPa·m/s, which is far above the 1.8 MPa·m/s limit '
               '— the bush would overheat'),
        p('Sanity check: the pressure alone passes but the PV product fails, which is the normal lesson of a '
          'bearing check: heat generation depends on PV, not on p, so a bush must be selected on both. A '
          'larger bush (80 mm × 80 mm) would bring PV to about 2.0 MPa·m/s and would still be marginal.'),
        h4('Limitations'),
        bullets('Bronze is expensive because tin is costly, so it is used for a bearing, a bush or a marine '
                'fitting and not for a general structural part.',
                'It has a lower conductivity than copper, so it cannot be used as an electrical conductor.',
                'Some bronzes (the high-tin and the aluminium grades) are hard and difficult to machine, and '
                'a bronze bearing must be run in and must be kept lubricated.',
                'A bronze in contact with steel in sea water can still set up a galvanic couple — the '
                'material is resistant, but the joint design must be right.'),
    ),
    gu=join(
        p('<b>બ્રોન્ઝ (bronze)</b> એ <b>તાંબું અને ટિન</b>નું alloy છે, સામાન્ય રીતે 5–12 % ટિન સાથે, અને '
          'ઘણી વાર થોડું phosphorus, જસત, લેડ કે એલ્યુમિનિયમ પણ હોય. એ માણસને જાણીતું સૌથી જૂનું alloy છે, '
          'અને આજે પણ bearing તથા marine materialનું માનક છે.'),
        h4('સામાન્ય બ્રોન્ઝની રચના'),
        table(['પ્રકાર', 'Cu', 'Sn', 'ઉમેરો', 'લક્ષણ'], [
            ['<b>Phosphor bronze</b>', '90–95 %', '5–10 %', '0.1–0.4 % P', 'માનક bearing અને spring alloy; '
             'phosphorus deoxidise કરે અને wear resistance આપે'],
            ['<b>Gunmetal</b>', '85–88 %', '8–10 %', '2–5 % Zn, 1–2 % Pb', 'cast valve, pump body, marine '
             'fitting'],
            ['<b>Bell bronze</b>', '78–80 %', '20–22 %', '—', 'સખત અને ગુંજન કરે — ઘંટડી અને cymbal'],
            ['<b>Aluminium bronze</b>', '90 %', '—', '8–10 % Al, Fe અને Ni સાથે', 'સૌથી મજબૂત bronze, sea '
             'water ઝીલે અને spark થાય નહીં'],
            ['<b>Silicon bronze</b>', '95 %', '—', '3 % Si, 1 % Mn', 'corrosion-resistant, marine fastener માટે'],
            ['<b>Leaded bronze</b>', '85 %', '8 %', '5 % Pb', 'free-cutting bearing bronze'],
        ]),
        h4('ગુણધર્મો'),
        table(['ગુણધર્મ', 'વર્તન'], [
            ['Strength', 'tensile 250–400 MPa (phosphor bronze), aluminium bronze 700 MPa સુધી'],
            ['Hardness અને wear resistance', 'સારી — પિત્તળ કરતાં વધુ, એટલે જ એ bearing material છે'],
            ['Friction અને bearing વર્તન', 'નીચો friction coefficient અને shaft સાથે બેસી જાય, એટલે માનક '
             'sleeve bearing અને bush'],
            ['Corrosion પ્રતિરોધ', 'sea water, steam અને marine વાતાવરણમાં ઉત્તમ — પિત્તળ કરતાં સારો, કારણ કે '
             'dezincification થતું નથી'],
            ['Ductility', 'સારી, અને roll, draw તથા cast સહેલું; ઓછા shrinkage સાથે સરસ cast થાય'],
            ['Electrical અને thermal conductivity', 'તાંબા કરતાં નીચી — લગભગ 10–15 % IACS, એટલે conductor નહીં '
             'પણ spring અને bearing material'],
            ['Fatigue અને spring ગુણધર્મ', 'phosphor bronze diaphragm, bellows અને electrical contact માટેનું '
             'માનક spring material'],
            ['Non-sparking અને non-magnetic', 'હા — તેલના ભંડારમાં tool, અને non-magnetic instrument ભાગ'],
            ['Machinability', 'સારી, અને leaded grade free-cutting'],
            ['ખર્ચ', 'મોંઘું, કારણ કે ટિન મોંઘું — એટલે જ્યાં કિંમત વસૂલ થાય ત્યાં જ વપરાય'],
        ]),
        h4('ઉપયોગ'),
        table(['ઉપયોગ', 'કયું bronze અને કેમ'], [
            ['Sleeve bearing, bush, thrust washer, worm wheel', 'phosphor કે leaded bronze — નીચો friction, shaft '
             'સાથે બેસે, અને oil ક્ષણિક બંધ થાય તો પણ ટકે'],
            ['Pump body, valve, impeller, sea-water fitting', 'gunmetal — આકારમાં cast થાય અને sea water ઝીલે'],
            ['જહાજનો propeller, marine fastener, pump shaft', 'aluminium કે silicon bronze — sea waterમાં સૌથી '
             'મજબૂત પ્રતિરોધ'],
            ['ઘંટડી, cymbal, gong અને મૂર્તિ', 'bell bronze — સખત અને ગુંજનકારી'],
            ['Spring, diaphragm, bellows અને electrical contact', 'phosphor bronze — સારા fatigue અને spring '
             'ગુણધર્મ'],
            ['Non-sparking tool, અને magnetic fieldમાં ભાગ', 'aluminium bronze — non-sparking અને non-magnetic'],
        ]),
        h4('ઉકેલેલું ઉદાહરણ — bearing pressureની ચકાસણી'),
        p('60 mm bore અને 60 mm લંબાઈનો phosphor-bronze bush 300 rpm પર 18 kN radial ભાર ઉપાડે છે. Bearing '
          'pressure અને PV factor શોધો, અને bronze bush માટેની સામાન્ય 15 MPa તથા 1.8 MPa·m/s મર્યાદા સામે '
          'ચકાસો.'),
        work('Given: d = 0.060 m · L = 0.060 m · W = 18 × 10<sup>3</sup> N · N = 300 rpm',
             'Projected area = d L = 0.060 × 0.060 = 3.6 × 10<sup>−3</sup> m<sup>2</sup>',
             'Bearing pressure p = ' + frac('W', 'd L') + ' = ' + frac('18 × 10<sup>3</sup>', '3.6 × 10<sup>−3</sup>')
             + ' = 5.0 × 10<sup>6</sup> Pa',
             'Surface speed v = ' + frac('π d N', '60') + ' = ' + frac('3.14 × 0.060 × 300', '60')
             + ' = 0.94 m/s',
             'PV = 5.0 × 0.94 = 4.7 MPa·m/s'),
        result('p = 5.0 MPa (15 MPa અંદર) પણ PV = 4.7 MPa·m/s, જે 1.8 MPa·m/s મર્યાદાથી ઘણું વધુ — bush ગરમ '
               'થઈ જાય'),
        p('Sanity check: ફક્ત pressure પાસ થાય પણ PV product ફેલ થાય, જે bearing ચકાસણીનો સામાન્ય પાઠ છે: '
          'ગરમી PV પર આધારિત છે, p પર નહીં, એટલે બંને પર bush પસંદ કરવો પડે. મોટો bush (80 mm × 80 mm) '
          'PV લગભગ 2.0 MPa·m/s કરે અને તો પણ સીમાંત રહે.'),
        h4('મર્યાદાઓ'),
        bullets('ટિન મોંઘું હોવાથી bronze મોંઘું છે, એટલે એ bearing, bush કે marine fitting માટે વપરાય, સામાન્ય '
                'structural ભાગ માટે નહીં.',
                'તાંબા કરતાં conductivity નીચી, એટલે electrical conductor તરીકે વપરાય નહીં.',
                'કેટલાક bronze (ઊંચા ટિનવાળા અને aluminium grade) સખત અને machine કરવા મુશ્કેલ, અને bronze '
                'bearing run-in કરવો પડે તથા lubricated રાખવો પડે.',
                'Sea waterમાં steelના સંપર્કમાં આવતું bronze પણ galvanic couple બનાવી શકે — material પ્રતિરોધક '
                'છે, પણ jointનું design સાચું હોવું જોઈએ.'),
    ),
))

Q5['cards'].append(dict(
    number='Q.5 (c)', marks=7, tag='OR', q='Describe physical properties and application of silver and nickel.',
    en=join(
        h4('Silver'),
        p('<b>Silver</b> is a white, lustrous, very soft metal and the <b>best electrical and thermal '
          'conductor of all metals</b>. It is also the standard against which the reflectivity of a '
          'surface is judged. Its use in engineering is limited by its cost and by its softness, but where '
          'the best conductivity or the best reflectivity is needed, silver is chosen.'),
        table(['Property', 'Value / behaviour'], [
            ['Density', '10 490 kg/m<sup>3</sup> — heavy, denser than copper'],
            ['Melting point', '961 °C'],
            ['Electrical conductivity', '63 × 10<sup>6</sup> S/m — 105 % IACS, the highest of any metal'],
            ['Thermal conductivity', '429 W/m·K — also the highest of any metal'],
            ['Reflectivity', 'the highest of any metal over the visible spectrum — about 95 %'],
            ['Strength', 'annealed only 140 MPa, hard drawn 300 MPa — soft and weak compared with copper'],
            ['Ductility', 'the most ductile and malleable metal: 1 g can be drawn into 2 km of wire'],
            ['Corrosion and tarnish', 'noble and it resists most chemicals, but it <b>tarnishes</b> black in '
             'sulphur compounds and in H<sub>2</sub>S'],
            ['Antibacterial', 'silver ions kill bacteria, which is why it is used in a medical dressing '
             'and a water filter'],
            ['Alloying', 'copper is added (7.5–12.5 %) to make sterling silver and to harden it for a '
             'contact and a bearing'],
        ]),
        h4('Applications of silver'),
        bullets('<b>Electrical contacts</b> — a relay, a contactor and a circuit breaker: a silver–cadmium '
                'oxide or a silver–nickel contact has the lowest contact resistance and does not weld shut.',
                '<b>Electronic and microwave</b> — a silver-plated conductor, a waveguide and a high-Q '
                'cavity, where the surface conductivity matters.',
                '<b>Brazing filler</b> — a silver solder (a Ag–Cu–Zn alloy) joins a copper pipe and a '
                'carbide tool tip at 600–700 °C.',
                '<b>Mirrors and reflectors</b> — a silvered mirror, a solar reflector.',
                '<b>Bearing</b> — a silver-lined aircraft bearing, a sterling-silver bush for a high-load '
                'application.',
                '<b>Coinage, jewellery, cutlery and photography</b> — the traditional and the photographic '
                'uses; a silver halide is still used in an X-ray film.'),
        h4('Nickel'),
        p('<b>Nickel</b> is a silvery, hard, tough and <b>magnetic</b> metal with excellent corrosion '
          'resistance. It is used in the pure state for a chemical plant and as an alloying element on a '
          'huge scale — stainless steel and the superalloys are built on it.'),
        table(['Property', 'Value / behaviour'], [
            ['Density', '8900 kg/m<sup>3</sup>'],
            ['Melting point', '1455 °C — high, so a nickel alloy keeps its strength when hot'],
            ['Electrical conductivity', 'about 14 × 10<sup>6</sup> S/m — 23 % IACS, low for a metal'],
            ['Thermal conductivity', 'about 90 W/m·K — low, which is why a nickel alloy is used for a '
             'heating element'],
            ['Strength', 'tensile 400–600 MPa, and it keeps much of it at 600 °C'],
            ['Hardness and toughness', 'hard and very tough; it work-hardens strongly'],
            ['Corrosion resistance', 'excellent against alkali, sea water and many acids; it resists '
             'oxidation at high temperature'],
            ['Magnetic', 'ferromagnetic up to its Curie point of 358 °C'],
            ['Catalytic', 'it catalyses hydrogenation and steam reforming, which is why a nickel catalyst '
             'is used in a hydrogenation plant'],
            ['Alloying', 'the base of stainless steel (8–20 % Ni), monel, inconel, nichrome, nimonic and '
             'the coinage alloys'],
            ['Toxicity', 'a nickel salt can cause contact dermatitis, so a nickel release is limited in a '
             'jewellery and a skin-contact item'],
        ]),
        h4('Applications of nickel'),
        bullets('<b>Alloying element</b> — stainless steel (18/8), monel, inconel, nichrome (a heating '
                'element), nimonic (a turbine blade) and maraging steel.',
                '<b>Chemical and food plant</b> — a nickel-lined vessel and a caustic soda handling line, '
                'where the alkali attacks steel.',
                '<b>Electroplating</b> — a nickel undercoat under chrome on a tap, a bicycle part and a '
                'plastic trim; it also gives a hard wearing surface.',
                '<b>Battery and electronics</b> — the nickel–cadmium and the nickel–metal-hydride cell, a '
                'nickel screen and a thermocouple (Ni–Cr/Ni–Al).',
                '<b>Coinage and a magnet</b> — an Alnico magnet contains nickel, and a cupronickel coin is '
                '25 % Ni.',
                '<b>Catalyst</b> — a Raney nickel catalyst for hydrogenation in a food and a pharmaceutical '
                'plant.'),
        h4('Worked example — a silver contact against a copper one'),
        p('A contact must carry 200 A, and the contact resistance must stay below 20 µΩ. Compare the '
          'resistance of a contact spot of 1 mm<sup>2</sup> area if it is copper '
          '(ρ = 1.7 × 10<sup>−8</sup> Ω·m) and if it is silver (ρ = 1.6 × 10<sup>−8</sup> Ω·m), taking the '
          'constriction resistance as R = ρ/(2a) with a the equivalent spot radius.'),
        work('Given: A = 1 mm<sup>2</sup> = 1 × 10<sup>−6</sup> m<sup>2</sup> · ρ<sub>Cu</sub> = '
             '1.7 × 10<sup>−8</sup> Ω·m · ρ<sub>Ag</sub> = 1.6 × 10<sup>−8</sup> Ω·m',
             'Radius a = √(A/π) = √(1 × 10<sup>−6</sup>/3.14) = 5.64 × 10<sup>−4</sup> m',
             'Copper: R = ' + frac('1.7 × 10<sup>−8</sup>', '2 × 5.64 × 10<sup>−4</sup>')
             + ' = 1.51 × 10<sup>−5</sup> Ω',
             'Silver: R = ' + frac('1.6 × 10<sup>−8</sup>', '2 × 5.64 × 10<sup>−4</sup>')
             + ' = 1.42 × 10<sup>−5</sup> Ω'),
        result('Copper 15.1 µΩ against silver 14.2 µΩ — both pass the 20 µΩ limit, but the silver contact '
               'runs about 6 % cooler and, more importantly, it does not oxidise'),
        p('Sanity check: the resistivities differ by only 6 %, so the reason for a silver contact is not its '
          'bulk conductivity but its <b>surface</b>: a silver oxide is conductive and a copper oxide is '
          'not, so a copper contact heats up and fails while a silver one does not.'),
        h4('Limitations'),
        bullets('Silver is expensive and soft: it wears, it tarnishes black in sulphur, and it must be '
                'alloyed or plated for a wearing application.',
                'Nickel is heavy and its conductivity is poor, so it is an alloy base and a corrosion '
                'barrier and not a conductor; its salt causes contact dermatitis.',
                'Both are strategic and price-volatile metals, and both are recovered from scrap rather '
                'than being used once.'),
    ),
    gu=join(
        h4('ચાંદી'),
        p('<b>ચાંદી (silver)</b> સફેદ, ચમકદાર અને ખૂબ નરમ ધાતુ છે, અને <b>બધી ધાતુઓમાં સૌથી સારી electrical '
          'તથા thermal conductor</b>. સપાટીની reflectivity પણ એના પર આંકાય. Engineeringમાં એનો વપરાશ ખર્ચ '
          'અને નરમાઈથી મર્યાદિત છે, પણ જ્યાં સૌથી સારી conductivity કે reflectivity જોઈએ ત્યાં ચાંદી પસંદ થાય.'),
        table(['ગુણધર્મ', 'કિંમત / વર્તન'], [
            ['Density', '10 490 kg/m<sup>3</sup> — ભારે, તાંબા કરતાં ઘન'],
            ['Melting point', '961 °C'],
            ['Electrical conductivity', '63 × 10<sup>6</sup> S/m — 105 % IACS, બધી ધાતુઓમાં સૌથી વધુ'],
            ['Thermal conductivity', '429 W/m·K — એ પણ સૌથી વધુ'],
            ['Reflectivity', 'દૃશ્ય સ્પેક્ટ્રમમાં સૌથી વધુ — લગભગ 95 %'],
            ['Strength', 'annealed ફક્ત 140 MPa, hard drawn 300 MPa — તાંબા કરતાં નરમ અને નબળી'],
            ['Ductility', 'સૌથી ductile અને malleable ધાતુ: 1 gમાંથી 2 km wire ખેંચાય'],
            ['Corrosion અને tarnish', 'noble અને મોટા ભાગના chemical સામે ટકે, પણ sulphur સંયોજન અને '
             'H<sub>2</sub>Sમાં <b>કાળી થઈ જાય</b>'],
            ['Antibacterial', 'ચાંદીના ion bacteria મારે, એટલે medical dressing અને water filterમાં વપરાય'],
            ['Alloying', 'તાંબું (7.5–12.5 %) ઉમેરીને sterling silver અને contact તથા bearing માટે harden કરાય'],
        ]),
        h4('ચાંદીના ઉપયોગ'),
        bullets('<b>Electrical contact</b> — relay, contactor અને circuit breaker: silver–cadmium oxide કે '
                'silver–nickel contactનો contact resistance સૌથી નીચો અને એ weld થઈને ચોંટી જતો નથી.',
                '<b>Electronic અને microwave</b> — silver-plated conductor, waveguide અને high-Q cavity, જ્યાં '
                'સપાટીની conductivity મહત્ત્વની.',
                '<b>Brazing filler</b> — silver solder (Ag–Cu–Zn) તાંબાની pipe અને carbide tool tipને 600–700 °C '
                'પર જોડે.',
                '<b>અરીસો અને reflector</b> — silvered અરીસો, solar reflector.',
                '<b>Bearing</b> — વિમાનનું silver-lined bearing, ઊંચા ભાર માટે sterling-silver bush.',
                '<b>Coinage, દાગીના, cutlery અને photography</b> — પરંપરાગત અને photographic વપરાશ; silver '
                'halide આજે પણ X-ray filmમાં વપરાય.'),
        h4('નિકલ'),
        p('<b>નિકલ</b> ચાંદી જેવી, સખત, tough અને <b>magnetic</b> ધાતુ છે જેનો corrosion પ્રતિરોધ ઉત્તમ છે. '
          'એ શુદ્ધ સ્વરૂપે chemical plantમાં અને alloying element તરીકે ખૂબ મોટા પ્રમાણમાં વપરાય — stainless '
          'steel અને superalloy નિકલ પર જ બન્યા છે.'),
        table(['ગુણધર્મ', 'કિંમત / વર્તન'], [
            ['Density', '8900 kg/m<sup>3</sup>'],
            ['Melting point', '1455 °C — ઊંચું, એટલે નિકલ alloy ગરમ હોય ત્યારે પણ strength રાખે'],
            ['Electrical conductivity', 'લગભગ 14 × 10<sup>6</sup> S/m — 23 % IACS, ધાતુ માટે નીચી'],
            ['Thermal conductivity', 'લગભગ 90 W/m·K — નીચી, એટલે heating element માટે નિકલ alloy વપરાય'],
            ['Strength', 'tensile 400–600 MPa, અને 600 °C પર પણ ઘણું રાખે'],
            ['Hardness અને toughness', 'સખત અને ખૂબ tough; જોરદાર work-harden થાય'],
            ['Corrosion પ્રતિરોધ', 'alkali, sea water અને ઘણા acid સામે ઉત્તમ; ઊંચા તાપમાને oxidation સામે ટકે'],
            ['Magnetic', '358 °Cના Curie point સુધી ferromagnetic'],
            ['Catalytic', 'hydrogenation અને steam reforming ઉપર catalyst, એટલે hydrogenation plantમાં નિકલ '
             'catalyst વપરાય'],
            ['Alloying', 'stainless steel (8–20 % Ni), monel, inconel, nichrome, nimonic અને coinage alloyનો '
             'આધાર'],
            ['ઝેરીપણું', 'નિકલના ક્ષારથી contact dermatitis થાય, એટલે દાગીના અને ચામડીના સંપર્કની વસ્તુમાં '
             'નિકલ release મર્યાદિત'],
        ]),
        h4('નિકલના ઉપયોગ'),
        bullets('<b>Alloying element</b> — stainless steel (18/8), monel, inconel, nichrome (heating element), '
                'nimonic (turbine blade) અને maraging steel.',
                '<b>Chemical અને food plant</b> — નિકલ-lined vessel અને caustic sodaની લાઇન, જ્યાં alkali '
                'steel પર હુમલો કરે.',
                '<b>Electroplating</b> — નળ, સાયકલના ભાગ અને plastic trim પર chrome નીચે નિકલનો undercoat; '
                'એ સખત ઘસાતી સપાટી પણ આપે.',
                '<b>Battery અને electronics</b> — nickel–cadmium અને nickel–metal-hydride cell, નિકલ screen અને '
                'thermocouple (Ni–Cr/Ni–Al).',
                '<b>Coinage અને magnet</b> — Alnico magnetમાં નિકલ, અને cupronickel સિક્કામાં 25 % Ni.',
                '<b>Catalyst</b> — food અને pharmaceutical plantમાં hydrogenation માટે Raney નિકલ catalyst.'),
        h4('ઉકેલેલું ઉદાહરણ — ચાંદીનો contact સામે તાંબાનો'),
        p('એક contactે 200 A લેવાનું છે અને contact resistance 20 µΩથી નીચે રહેવો જોઈએ. 1 mm<sup>2</sup> '
          'areaના contact spotનો resistance તાંબું (ρ = 1.7 × 10<sup>−8</sup> Ω·m) અને ચાંદી '
          '(ρ = 1.6 × 10<sup>−8</sup> Ω·m) માટે સરખાવો; constriction resistance R = ρ/(2a), જ્યાં a એ '
          'સમતુલ્ય spotની ત્રિજ્યા છે.'),
        work('Given: A = 1 mm<sup>2</sup> = 1 × 10<sup>−6</sup> m<sup>2</sup> · ρ<sub>Cu</sub> = '
             '1.7 × 10<sup>−8</sup> Ω·m · ρ<sub>Ag</sub> = 1.6 × 10<sup>−8</sup> Ω·m',
             'ત્રિજ્યા a = √(A/π) = √(1 × 10<sup>−6</sup>/3.14) = 5.64 × 10<sup>−4</sup> m',
             'તાંબું: R = ' + frac('1.7 × 10<sup>−8</sup>', '2 × 5.64 × 10<sup>−4</sup>')
             + ' = 1.51 × 10<sup>−5</sup> Ω',
             'ચાંદી: R = ' + frac('1.6 × 10<sup>−8</sup>', '2 × 5.64 × 10<sup>−4</sup>')
             + ' = 1.42 × 10<sup>−5</sup> Ω'),
        result('તાંબું 15.1 µΩ સામે ચાંદી 14.2 µΩ — બંને 20 µΩ મર્યાદામાં, પણ ચાંદીનો contact લગભગ 6 % ઠંડો '
               'ચાલે અને, વધુ મહત્ત્વનું, એ oxidise થતો નથી'),
        p('Sanity check: resistivitiesમાં ફક્ત 6 % ફરક છે, એટલે ચાંદીના contactનું કારણ bulk conductivity નહીં '
          'પણ <b>સપાટી</b> છે: ચાંદીનો oxide conductive છે અને તાંબાનો નહીં, એટલે તાંબાનો contact ગરમ થઈને '
          'ફેલ થાય જ્યારે ચાંદીનો નહીં.'),
        h4('મર્યાદાઓ'),
        bullets('ચાંદી મોંઘી અને નરમ છે: ઘસાય, sulphurમાં કાળી થાય, અને ઘસાતા કામ માટે alloy કે plating કરવી '
                'પડે.',
                'નિકલ ભારે છે અને conductivity નબળી, એટલે એ alloyનો આધાર અને corrosion barrier છે, conductor '
                'નહીં; એના ક્ષારથી contact dermatitis થાય.',
                'બંને strategic અને ભાવ વધઘટ કરતી ધાતુ છે, અને બંને એક વાર વાપરીને ફેંકવાને બદલે scrapમાંથી '
                'પાછી મેળવાય.'),
    ),
))

