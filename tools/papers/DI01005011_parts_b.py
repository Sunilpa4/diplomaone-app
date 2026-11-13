"""DI01005011 Winter 2025 — Q3, Q4 and Q5 answer parts."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from paperkit import frac, work, steps, result, table, bullets, numbered, h4, p, eq, figure
import chemfigs as fig


def join(*chunks):
    return "\n".join(c for c in chunks if c)


# ---------------------------------------------------------------- Q3
Q3 = {
    'title_en': 'Q3 · Refrigerants, steam and boilers',
    'title_gu': 'પ્ર.3 · રેફ્રિજરેન્ટ, સ્ટીમ અને બોઇલર',
    'cards': [],
}

Q3['cards'].append(dict(
    number='Q.3 (a)', marks=3, q='Explain various properties desirable in an ideal refrigerant.',
    en=join(
        h4('Desirable properties'),
        bullets('<b>Thermodynamic:</b> high latent heat of vaporisation, boiling point slightly below the required '
                'temperature, low specific volume of vapour, high critical temperature.',
                '<b>Safety:</b> non-toxic, non-flammable, non-explosive, no irritating odour, no harm if it leaks '
                'into the product area.',
                '<b>Chemical:</b> stable in the cycle, no reaction with lubricating oil or metals, no corrosion, '
                'no moisture absorption.',
                '<b>Physical:</b> leak easily detected, low viscosity, high thermal conductivity, low freezing point.',
                '<b>Economic and environmental:</b> cheap and easily available, low power consumption per tonne of '
                'refrigeration, small compressor for the duty, zero ozone-depletion and low global-warming potential.'),
        p('No single fluid has all of these properties. The refrigerant is chosen by weighing the properties that '
          'matter most for the job — for example R-134a in a domestic refrigerator, ammonia in an industrial cold '
          'store, R-600a where the charge must be very small.'),
    ),
    gu=join(
        h4('ઇચ્છનીય ગુણધર્મો'),
        bullets('<b>Thermodynamic:</b> latent heat of vaporisation વધુ, boiling point જરૂરી temperatureથી થોડું નીચે, '
                'vapourનું specific volume ઓછું, critical temperature ઊંચું.',
                '<b>Safety:</b> non-toxic, non-flammable, non-explosive, ચડતી ગંધ નહીં, leak થાય તો નુકસાન ન થાય.',
                '<b>Chemical:</b> cycleમાં stable, lubricating oil કે metal સાથે reaction નહીં, corrosion નહીં, '
                'ભેજ શોષે નહીં.',
                '<b>Physical:</b> leak સહેલાઈથી ખબર પડે, viscosity ઓછી, thermal conductivity વધુ, freezing point નીચું.',
                '<b>Economic–environmental:</b> સસ્તું અને સહેલાઈથી મળે, પ્રતિ tonne refrigeration power ઓછું, એ જ કામ '
                'માટે નાનું compressor, ozone-depletion શૂન્ય અને global-warming potential ઓછું.'),
        p('એક પણ fluidમાં બધા ગુણધર્મ નથી હોતા. કામ માટે જે ગુણધર્મ સૌથી જરૂરી હોય તે જોઈને પસંદગી થાય — દા.ત. '
          'ઘરેલું ફ્રિજમાં R-134a, ઔદ્યોગિક cold storeમાં ammonia, અને જ્યાં charge ખૂબ ઓછું જોઈએ ત્યાં R-600a.'),
    ),
))

Q3['cards'].append(dict(
    number='Q.3 (b)', marks=4, q='List use of Steam and Air.',
    en=join(
        h4('Uses of steam in a chemical plant'),
        bullets('<b>Heating:</b> jackets and coils of reactors, reboilers of distillation columns, evaporators, '
                'dryers and preheaters.',
                '<b>Direct injection:</b> live steam for heating, stripping and steam distillation.',
                '<b>Power:</b> steam turbines driving pumps, compressors and generators.',
                '<b>Tracing and atomising:</b> steam tracing of pipelines to stop freezing or solidification, and '
                'steam atomising of fuel oil.',
                '<b>Process and utility:</b> steam cracking, humidification, cleaning and sterilising.'),
        h4('Uses of air'),
        bullets('<b>Combustion air:</b> for boilers, furnaces and flare stacks, supplied by a forced-draught blower.',
                '<b>Compressed air:</b> pneumatic instruments and control valves, air motors, cleaning and sparging.',
                '<b>Oxidation air:</b> oxidation reactions, aerobic effluent treatment, aeration tanks.',
                '<b>Cooling and drying:</b> air-cooled heat exchangers, drying of equipment and powder conveying.',
                '<b>Safety:</b> air is used to purge lines where a flammable gas must not remain.'),
        h4('Which one where'),
        p('Steam is chosen where heat must be delivered with a high heat-transfer coefficient and easy control; '
          'air is chosen where the duty is combustion, oxidation, conveying or instrument actuation.'),
    ),
    gu=join(
        h4('કેમિકલ પ્લાન્ટમાં steamનો ઉપયોગ'),
        bullets('<b>Heating:</b> reactorના jacket અને coil, distillation columnના reboiler, evaporator, dryer, preheater.',
                '<b>Direct injection:</b> heating, stripping અને steam distillation માટે live steam.',
                '<b>Power:</b> pump, compressor અને generator ચલાવતી steam turbine.',
                '<b>Tracing અને atomising:</b> line ઠંડકથી જામે નહીં એ માટે steam tracing, અને fuel oilનું steam atomising.',
                '<b>Process–utility:</b> steam cracking, humidification, સફાઈ અને sterilising.'),
        h4('Airનો ઉપયોગ'),
        bullets('<b>Combustion air:</b> boiler, furnace અને flare stack માટે, forced-draught blowerથી.',
                '<b>Compressed air:</b> pneumatic instrument–control valve, air motor, સફાઈ અને sparging.',
                '<b>Oxidation air:</b> oxidation reaction, aerobic effluent treatment, aeration tank.',
                '<b>Cooling અને drying:</b> air-cooled heat exchanger, equipment સુકવવા અને powder conveying.',
                '<b>Safety:</b> flammable gas બાકી ન રહે એ માટે line purgingમાં air વપરાય.'),
        h4('ક્યાં કઈ'),
        p('જ્યાં ઊંચા heat-transfer coefficient સાથે સહેલા controlમાં ગરમી જોઈએ ત્યાં steam; જ્યાં combustion, '
          'oxidation, conveying કે instrument ચલાવવાનું હોય ત્યાં air.'),
    ),
))

Q3['cards'].append(dict(
    number='Q.3 (c)', marks=7, q='Explain construction and working of Locomotive boiler.',
    en=join(
        h4('What it is'),
        p('The <b>locomotive boiler</b> is a horizontal, multi-tubular <b>fire-tube</b> boiler of about 9,000 kg/h '
          'capacity at 14–16 bar. It was designed for steam locomotives, so it is compact, light and mounted on '
          'the frame of the vehicle.'),
        figure(fig.locomotive_boiler(), 'Fig. 3.1 · Locomotive boiler: fire box, fire tubes, smoke box, dome and chimney.'),
        h4('Construction — part and purpose'),
        table(['Part', 'Purpose'], [
            ['Shell', 'steel body holding the water and steam; bolted to the locomotive frame'],
            ['Fire box and grate', 'coal burns here; the hot gases begin their path from this point'],
            ['Combustion chamber', 'completes the burning of the gases before they enter the tubes'],
            ['Fire tubes (about 150–180)', 'carry hot gas through the water and provide a large heating surface'],
            ['Smoke box and chimney', 'collect the cooled gas and throw it out; the chimney also creates the draught'],
            ['Steam space and dome', 'collect dry steam; the dome keeps the outlet above the water line'],
            ['Regulator valve', 'controls the steam going to the cylinders'],
            ['Safety valve, pressure gauge, water gauge', 'protect the boiler and show its condition'],
            ['Feed-water inlet and blow-down cock', 'maintain the level and remove sludge'],
        ]),
        h4('Working — step and reason'),
        steps(('Step 1', 'Coal is fired on the grate and air enters through the ash pan, so combustion starts in the '
                         'fire box.'),
              ('Step 2', 'The hot gases pass through the combustion chamber and then through the fire tubes. The tubes '
                         'are surrounded by water, so heat passes into the water.'),
              ('Step 3', 'The gases reach the smoke box and leave through the chimney. The exhaust steam blower in the '
                         'chimney increases the draught, so more air is pulled through the fire.'),
              ('Step 4', 'The water absorbs heat, circulates by natural convection and turns into steam, which collects '
                         'in the steam space and the dome.'),
              ('Step 5', 'Steam leaves through the regulator to the cylinders, and the exhaust steam is used again to '
                         'create the draught.')),
        h4('Advantages and limitations'),
        bullets('Very high evaporation rate for its size, compact, light, and it moves with the vehicle.',
                'The fire box is inside the shell and the boiler has to follow the load, so skilled firing is needed.',
                'It is not suitable as a stationary plant, and the tubes are difficult to clean.'),
    ),
    gu=join(
        h4('એ શું છે'),
        p('<b>Locomotive boiler</b> એ આડો, multi-tubular <b>fire-tube</b> boiler છે; ક્ષમતા લગભગ 9,000 kg/h અને '
          'pressure 14–16 bar. Steam engine માટે બનેલો હોવાથી એ compact, હલકો અને વાહનના frame પર બેસે એવો છે.'),
        figure(fig.locomotive_boiler(), 'આકૃતિ 3.1 · Locomotive boiler: fire box, fire tubes, smoke box, dome અને chimney.'),
        h4('રચના — ભાગ અને કામ'),
        table(['ભાગ', 'કામ'], [
            ['Shell', 'પાણી અને steam રાખતું steel body; locomotive frame સાથે બોલ્ટ થાય'],
            ['Fire box અને grate', 'કોલસો બળે છે; ગરમ gasની શરૂઆત અહીંથી'],
            ['Combustion chamber', 'tubesમાં જતાં પહેલાં gasનું બળવું પૂરું કરે'],
            ['Fire tubes (લગભગ 150–180)', 'ગરમ gas પાણીમાંથી પસાર થાય અને મોટું heating surface આપે'],
            ['Smoke box અને chimney', 'ઠંડા gas એકઠા કરી બહાર ફેંકે; chimney draught પણ બનાવે'],
            ['Steam space અને dome', 'સૂકું steam એકઠું કરે; dome outletને water lineથી ઉપર રાખે'],
            ['Regulator valve', 'cylinderને જતું steam નિયંત્રિત કરે'],
            ['Safety valve, pressure gauge, water gauge', 'boilerને સાચવે અને તેની સ્થિતિ દેખાડે'],
            ['Feed-water inlet અને blow-down cock', 'water level જાળવે અને sludge કાઢે'],
        ]),
        h4('કાર્ય — સ્ટેપ અને કારણ'),
        steps(('Step 1', 'Grate પર કોલસો નાખાય અને ash panથી હવા આવે, એટલે fire boxમાં combustion શરૂ થાય.'),
              ('Step 2', 'ગરમ gas combustion chamber પછી fire tubesમાં જાય. Tubes ચારે બાજુ પાણીથી ઘેરાયેલા હોય, '
                         'એટલે heat પાણીમાં જાય.'),
              ('Step 3', 'Gas smoke boxમાં પહોંચીને chimneyથી બહાર જાય. Chimneyમાં exhaust steam blower draught વધારે '
                         'છે, એટલે fireમાં વધુ હવા ખેંચાય.'),
              ('Step 4', 'પાણી heat લઈને natural convectionથી ફરે અને steam બને, જે steam space અને domeમાં એકઠું થાય.'),
              ('Step 5', 'Steam regulator થઈને cylinderમાં જાય, અને exhaust steam ફરી draught બનાવવા વપરાય.')),
        h4('ફાયદા અને મર્યાદાઓ'),
        bullets('કદ પ્રમાણે evaporation rate ખૂબ વધુ, compact, હલકો અને વાહન સાથે ચાલે.',
                'Fire box shellની અંદર હોય અને boiler load સાથે ચાલતો હોય, એટલે firingમાં કુશળતા જોઈએ.',
                'Stationary plant તરીકે યોગ્ય નથી, અને tubes સાફ કરવા અઘરા છે.'),
    ),
))

Q3['cards'].append(dict(
    number='Q.3 (a)', marks=3, tag='OR', q='Explain evaporative refrigeration system.',
    en=join(
        h4('Principle'),
        p('In <b>evaporative refrigeration</b> the cooling comes from the evaporation of water itself. When '
          'water evaporates it takes its <b>latent heat</b> — about 2,450 kJ per kg at 25 °C — from the air '
          'around it, so that air becomes cooler and more humid. No compressor and no refrigerant are needed, '
          'only a fan and a water supply.'),
        h4('Working'),
        numbered('A fan pulls air through a wet pad, or through a spray of water.',
                 'Water evaporates into the air and absorbs latent heat from the air.',
                 'The dry-bulb temperature of the air falls and its humidity rises; the wet-bulb temperature stays '
                 'nearly the same.',
                 'The cooled air is supplied to the room. The same principle cools water in a cooling tower.'),
        h4('Use and limits'),
        p('Used in desert coolers, cooling towers and evaporative condensers. It works well in hot, dry air and '
          'poorly in humid weather, because humid air can absorb little more water. It cannot cool below the '
          'wet-bulb temperature and it adds moisture to the space.'),
    ),
    gu=join(
        h4('સિદ્ધાંત'),
        p('<b>Evaporative refrigeration</b>માં ઠંડક પાણીના evaporationથી જ મળે છે. પાણી બાષ્પ બનતાં આસપાસની હવામાંથી '
          '<b>latent heat</b> — 25 °C પર લગભગ 2,450 kJ પ્રતિ kg — લે છે, એટલે એ હવા ઠંડી અને ભેજવાળી બને. '
          'Compressor કે refrigerantની જરૂર નહીં, ફક્ત fan અને પાણી.'),
        h4('કાર્ય'),
        numbered('Fan હવાને ભીના padમાંથી કે પાણીના sprayમાંથી ખેંચે છે.',
                 'પાણી બાષ્પ બનીને હવામાંથી latent heat લે છે.',
                 'હવાનું dry-bulb temperature ઘટે અને humidity વધે; wet-bulb temperature લગભગ એ જ રહે.',
                 'ઠંડી હવા રૂમમાં જાય. એ જ સિદ્ધાંતથી cooling towerમાં પાણી ઠંડું થાય.'),
        h4('ઉપયોગ અને મર્યાદા'),
        p('Desert cooler, cooling tower અને evaporative condenserમાં વપરાય. ગરમ–સૂકી હવામાં સારું કામ કરે અને '
          'ભેજવાળા હવામાનમાં નબળું, કારણ કે ભીની હવા વધુ પાણી લઈ શકતી નથી. Wet-bulb temperatureથી નીચે ઠંડક '
          'મળતી નથી અને જગ્યામાં ભેજ વધે છે.'),
    ),
))

Q3['cards'].append(dict(
    number='Q.3 (b)', marks=4, tag='OR', q='List properties of steam with one example.',
    en=join(
        h4('Properties of steam'),
        table(['Property', 'Meaning', 'Value at 1 bar (example)'], [
            ['Sensible heat / enthalpy of liquid, h<sub>f</sub>', 'heat to bring 1 kg water from 0 °C to the boiling point',
             '417 kJ/kg'],
            ['Latent heat, h<sub>fg</sub>', 'heat to change 1 kg saturated water into dry saturated steam',
             '2,257 kJ/kg'],
            ['Enthalpy of dry saturated steam, h<sub>g</sub>', 'h<sub>f</sub> + h<sub>fg</sub>', '2,674 kJ/kg'],
            ['Dryness fraction, x', 'mass of dry steam ÷ total mass of the mixture', 'x = 0.95 means 5 % water by mass'],
            ['Specific volume, v<sub>g</sub>', 'volume of 1 kg of steam', '1.694 m³/kg'],
            ['Saturation temperature', 'boiling point at that pressure', '100 °C at 1.013 bar, 180 °C at 10 bar'],
            ['Superheat', 'heat added above saturation temperature', 'steam at 300 °C at 10 bar has about 120 °C superheat'],
        ]),
        h4('One example worked out'),
        p('At 1 bar, 1 kg of water at 0 °C is heated: 417 kJ of sensible heat brings it to 100 °C, then 2,257 kJ '
          'of latent heat turns it into steam. The enthalpy of dry saturated steam is therefore '
          '417 + 2,257 = <b>2,674 kJ/kg</b>.'),
        p('Check of magnitude: that latent heat alone could warm ' + frac('2257', '4.18') +
          ' ≈ 540 kg of water through 1 °C, which is why steam is the preferred heating medium in a plant.'),
    ),
    gu=join(
        h4('Steamનાં ગુણધર્મો'),
        table(['ગુણધર્મ', 'અર્થ', '1 bar પર મૂલ્ય (ઉદાહરણ)'], [
            ['Sensible heat / enthalpy of liquid, h<sub>f</sub>', '1 kg પાણી 0 °Cથી boiling point સુધી લઈ જવાની heat',
             '417 kJ/kg'],
            ['Latent heat, h<sub>fg</sub>', '1 kg સંતૃપ્ત પાણીને dry saturated steamમાં ફેરવવાની heat', '2,257 kJ/kg'],
            ['Enthalpy of dry saturated steam, h<sub>g</sub>', 'h<sub>f</sub> + h<sub>fg</sub>', '2,674 kJ/kg'],
            ['Dryness fraction, x', 'dry steamનું mass ÷ મિશ્રણનું કુલ mass', 'x = 0.95 એટલે mass પ્રમાણે 5 % પાણી'],
            ['Specific volume, v<sub>g</sub>', '1 kg steamનું volume', '1.694 m³/kg'],
            ['Saturation temperature', 'એ pressure પર boiling point', '1.013 bar પર 100 °C, 10 bar પર 180 °C'],
            ['Superheat', 'saturation temperatureથી ઉપર ઉમેરાયેલી heat', '10 bar પર 300 °C steamમાં લગભગ 120 °C superheat'],
        ]),
        h4('એક ઉદાહરણ ગણીને'),
        p('1 bar પર 0 °Cનું 1 kg પાણી ગરમ કરીએ: 417 kJ sensible heat પાણીને 100 °C સુધી લાવે, પછી 2,257 kJ latent '
          'heat એને steamમાં ફેરવે. એટલે dry saturated steamની enthalpy 417 + 2,257 = <b>2,674 kJ/kg</b>.'),
        p('Magnitudeની ચકાસણી: એટલી જ latent heatથી ' + frac('2257', '4.18') + ' ≈ 540 kg પાણી 1 °C ગરમ થાય, '
          'એટલે જ plantમાં heating માટે steam પસંદ કરાય છે.'),
    ),
))

Q3['cards'].append(dict(
    number='Q.3 (c)', marks=7, tag='OR', q='Explain construction and working of Lancashire boiler.',
    en=join(
        h4('What it is'),
        p('The <b>Lancashire boiler</b> is a horizontal, stationary <b>fire-tube</b> boiler with two large internal '
          'flues. It is built for capacities up to about 9,000 kg/h at 10–15 bar and is the standard boiler for '
          'steady process steam in small and medium plants.'),
        figure(fig.lancashire_boiler(), 'Fig. 3.2 · Lancashire boiler: fire box, two flues, brick baffle, smoke box and dome.'),
        h4('Construction — part and purpose'),
        table(['Part', 'Purpose'], [
            ['Cylindrical shell', 'holds water and steam; diameter about 2–3 m, length 7–9 m'],
            ['Fire box and grate at the front', 'burns the coal; the gases enter the first flue'],
            ['Two internal flues', 'carry hot gas through the water, giving a large heating surface, and also '
                                   'stiffen the shell'],
            ['Brick baffle setting', 'turns the gas for a third pass under the shell, so more heat is transferred'],
            ['Smoke box and chimney', 'collect the cooled gas and produce the draught'],
            ['Steam space, dome, safety valve, pressure gauge', 'dry steam collection, protection and monitoring'],
            ['Fusible plug, water gauge, feed inlet', 'guard against low water and show the level'],
            ['Blow-down cock', 'removes sludge and scale-forming salts'],
        ]),
        h4('Working — step and reason'),
        steps(('Step 1', 'Coal is fired on the grate and air comes through the ash pit, so combustion starts in the '
                         'fire box.'),
              ('Step 2', 'Hot gas travels along the first flue to the back, then turns and comes forward through the '
                         'second flue. The two passes give a long gas path and better heat transfer.'),
              ('Step 3', 'After the second flue the gas passes under the shell through the brick baffle setting and '
                         'leaves through the smoke box and chimney.'),
              ('Step 4', 'Water around the flues absorbs heat, circulates by natural convection, and steam forms in '
                         'the steam space above the water level.'),
              ('Step 5', 'Steam is drawn from the dome; the safety valve releases excess pressure and the water gauge '
                         'shows the level.')),
        h4('Advantages and limitations'),
        bullets('Simple and robust, large steam space, easy to repair, moderate cost and good efficiency for a '
                'fire-tube boiler.',
                'Large floor area and heavy brick setting, slow start-up, unsuitable above about 15 bar, and the '
                'flues are difficult to clean.'),
    ),
    gu=join(
        h4('એ શું છે'),
        p('<b>Lancashire boiler</b> એ આડો, stationary <b>fire-tube</b> boiler છે જેમાં બે મોટા અંદરના flues હોય છે. '
          'ક્ષમતા લગભગ 9,000 kg/h સુધી અને pressure 10–15 bar. નાના–મધ્યમ plantમાં steady process steam માટે '
          'સામાન્ય boiler છે.'),
        figure(fig.lancashire_boiler(), 'આકૃતિ 3.2 · Lancashire boiler: fire box, બે flues, brick baffle, smoke box અને dome.'),
        h4('રચના — ભાગ અને કામ'),
        table(['ભાગ', 'કામ'], [
            ['નળાકાર shell', 'પાણી અને steam રાખે; વ્યાસ લગભગ 2–3 m, લંબાઈ 7–9 m'],
            ['આગળનું fire box અને grate', 'કોલસો બળે; gas પહેલા flueમાં જાય'],
            ['બે અંદરના flues', 'ગરમ gas પાણીમાંથી પસાર કરાવે, મોટું heating surface આપે અને shellને મજબૂતાઈ પણ આપે'],
            ['Brick baffle setting', 'gasને ત્રીજી વાર shellની નીચે ફેરવે, જેથી વધુ heat transfer થાય'],
            ['Smoke box અને chimney', 'ઠંડા gas એકઠા કરે અને draught બનાવે'],
            ['Steam space, dome, safety valve, pressure gauge', 'સૂકું steam, સુરક્ષા અને monitoring'],
            ['Fusible plug, water gauge, feed inlet', 'પાણી ઓછું થવાથી રક્ષણ અને level દેખાય'],
            ['Blow-down cock', 'sludge અને scaleવાળા ક્ષાર કાઢે'],
        ]),
        h4('કાર્ય — સ્ટેપ અને કારણ'),
        steps(('Step 1', 'Grate પર કોલસો નાખાય અને ash pitથી હવા આવે, એટલે fire boxમાં combustion શરૂ થાય.'),
              ('Step 2', 'ગરમ gas પહેલા flueમાં પાછળ જાય, પછી ફરીને બીજા flueમાં આગળ આવે. બે passથી gasનો લાંબો '
                         'રસ્તો અને સારું heat transfer મળે.'),
              ('Step 3', 'બીજા flue પછી gas brick baffleમાં shellની નીચે થઈને smoke box અને chimneyમાંથી નીકળે.'),
              ('Step 4', 'Fluesની આસપાસનું પાણી heat લે, natural convectionથી ફરે અને water level ઉપરના steam spaceમાં '
                         'steam બને.'),
              ('Step 5', 'Steam domeમાંથી ખેંચાય; safety valve વધુ pressure કાઢે અને water gauge level દેખાડે.')),
        h4('ફાયદા અને મર્યાદાઓ'),
        bullets('સાદું અને મજબૂત, મોટું steam space, સહેલાઈથી રિપેર થાય, fire-tube boiler માટે ખર્ચ વાજબી અને efficiency સારી.',
                'જગ્યા વધુ અને ભારે brick setting, ધીમું start-up, લગભગ 15 barથી ઉપર યોગ્ય નહીં, અને flues સાફ કરવા અઘરા.'),
    ),
))

# ---------------------------------------------------------------- Q4
Q4 = {
    'title_en': 'Q4 · Air as a utility, boiler selection and air compressors',
    'title_gu': 'પ્ર.4 · હવા utility તરીકે, boilerની પસંદગી અને air compressor',
    'cards': [],
}

Q4['cards'].append(dict(
    number='Q.4 (a)', marks=3, q='Explain blower air and compressed air as utility of air.',
    en=join(
        h4('Blower air'),
        p('<b>Blower air</b> is air moved in large volume at low pressure rise, typically 0.05 to 1 bar. It is '
          'produced by a centrifugal or roots blower and is used where the <b>quantity matters more than the '
          'pressure</b>: combustion air for boilers and furnaces, ventilation, pneumatic conveying of light '
          'material, and aeration in effluent treatment.'),
        h4('Compressed air'),
        p('<b>Compressed air</b> is air stored at high pressure, usually 6 to 10 bar, in a receiver. It is made by '
          'a reciprocating, rotary or centrifugal compressor and is used as a <b>power and control medium</b>: '
          'pneumatic instruments and control valves, air motors and tools, cleaning and sparging, and oxidation air.'),
        h4('Difference in one look'),
        table(['Point', 'Blower air', 'Compressed air'], [
            ['Pressure', 'low, 0.05–1 bar', 'high, 6–10 bar'],
            ['Volume handled', 'large', 'small'],
            ['Produced by', 'blower or fan', 'compressor with receiver'],
            ['Main use', 'combustion, aeration, conveying', 'instruments, tools, cleaning'],
        ]),
        p('Instrument air must be dry and oil-free, so a compressed-air line has an aftercooler, a dryer and a '
          'filter before the instrument header.'),
    ),
    gu=join(
        h4('Blower air'),
        p('<b>Blower air</b> એ ઓછા pressure (સામાન્ય રીતે 0.05–1 bar) પર મોટા volumeમાં વહેતી હવા છે. Centrifugal કે '
          'roots blowerથી બને છે અને જ્યાં <b>pressure કરતાં quantity મહત્ત્વની</b> હોય ત્યાં વપરાય: boiler–furnaceનું '
          'combustion air, ventilation, હલકા materialનું pneumatic conveying અને effluent treatmentમાં aeration.'),
        h4('Compressed air'),
        p('<b>Compressed air</b> એ ઊંચા pressure (સામાન્ય રીતે 6–10 bar) પર receiverમાં સંગ્રહાયેલી હવા છે. Reciprocating, '
          'rotary કે centrifugal compressorથી બને છે અને <b>power તથા control medium</b> તરીકે વપરાય: pneumatic '
          'instrument–control valve, air motor–tools, સફાઈ અને sparging, તથા oxidation air.'),
        h4('એક નજરમાં તફાવત'),
        table(['મુદ્દો', 'Blower air', 'Compressed air'], [
            ['Pressure', 'ઓછું, 0.05–1 bar', 'વધુ, 6–10 bar'],
            ['Volume', 'મોટું', 'નાનું'],
            ['કઈ રીતે બને', 'blower કે fan', 'compressor અને receiver'],
            ['મુખ્ય ઉપયોગ', 'combustion, aeration, conveying', 'instrument, tools, સફાઈ'],
        ]),
        p('Instrument air સૂકી અને oil-free હોવી જોઈએ, એટલે compressed-air લાઇનમાં aftercooler, dryer અને filter '
          'પછી જ હવા instrument headerમાં જાય.'),
    ),
))

Q4['cards'].append(dict(
    number='Q.4 (b)', marks=4, q='List factors affecting selection of Boiler.',
    en=join(
        h4('Factors affecting boiler selection'),
        table(['Factor', 'What it decides'], [
            ['Steam demand (kg/h) and how much it varies', 'boiler size; a swinging demand needs more steam space or '
                                                           'a bank of boilers'],
            ['Working pressure and temperature', 'fire-tube up to about 15 bar, water-tube above; a superheater is '
                                                 'needed for high temperature'],
            ['Fuel available and its cost', 'coal, oil, gas or agro-waste decides the furnace and firing system'],
            ['Floor area, headroom and weight', 'a Lancashire boiler needs a large area, a packaged boiler very little'],
            ['Efficiency and running cost', 'economiser, air preheater and number of gas passes'],
            ['Water quality', 'hard water demands a water-tube boiler with good treatment or internal phosphate dosing'],
            ['Nature of the load', 'steady process load, or quick start-up and quick shutdown'],
            ['Initial cost, maintenance and life', 'packaged boilers are quick to install, shell boilers are cheaper '
                                                   'to repair'],
            ['Safety and statutory requirements', 'IBR approval, safety valves, drum size, operator skill'],
        ]),
        p('In practice the selection is a compromise: the boiler must meet the steam demand at the required pressure '
          'with the fuel that is available, inside the available floor area, at the lowest total cost over its life.'),
    ),
    gu=join(
        h4('Boilerની પસંદગી પર અસર કરતા પરિબળો'),
        table(['પરિબળ', 'શું નક્કી કરે'], [
            ['Steamની માંગ (kg/h) અને તેમાં ફેરફાર', 'boilerનું size; માંગ ઘટ-વધતી હોય તો વધુ steam space કે અલગ boilers'],
            ['Working pressure અને temperature', 'fire-tube લગભગ 15 bar સુધી, ઉપર water-tube; ઊંચા temperature માટે superheater'],
            ['ઉપલબ્ધ fuel અને તેની કિંમત', 'કોલસો, oil, gas કે agro-waste પ્રમાણે furnace અને firing system'],
            ['જગ્યા, ઊંચાઈ અને વજન', 'Lancashireને મોટી જગ્યા, packaged boilerને ખૂબ ઓછી'],
            ['Efficiency અને running cost', 'economiser, air preheater અને gas passની સંખ્યા'],
            ['પાણીની ગુણવત્તા', 'hard પાણી માટે સારી treatmentવાળું water-tube boiler કે internal phosphate dosing'],
            ['Loadનું સ્વરૂપ', 'steady process load, કે ઝડપી start-up–shutdown'],
            ['Initial cost, maintenance અને આયુષ્ય', 'packaged boiler જલદી લાગે, shell boiler સહેલાઈથી રિપેર થાય'],
            ['સુરક્ષા અને કાયદાકીય જરૂરિયાત', 'IBR approval, safety valve, drumનું size, operatorની કુશળતા'],
        ]),
        p('વ્યવહારમાં પસંદગી સમાધાન છે: ઉપલબ્ધ fuel અને જગ્યામાં, જરૂરી pressure પર steamની માંગ પૂરી કરે અને '
          'આખા આયુષ્યનો કુલ ખર્ચ સૌથી ઓછો રહે એ boiler પસંદ થાય.'),
    ),
))

Q4['cards'].append(dict(
    number='Q.4 (c)', marks=7, q='Explain Reciprocating Air compressors in detail.',
    en=join(
        h4('What it is'),
        p('A <b>reciprocating air compressor</b> is a positive-displacement machine. A piston moving in a cylinder '
          'draws in a fixed volume of air and then squeezes it into a smaller volume, raising its pressure. '
          'Single-stage machines give up to about 6 bar; two-stage machines with an intercooler give 6–15 bar or more.'),
        figure(fig.air_compressor_reciprocating(), 'Fig. 4.1 · Single-stage reciprocating compressor: cylinder, piston, suction and delivery valves.'),
        h4('Construction — part and purpose'),
        table(['Part', 'Purpose'], [
            ['Cylinder and piston with rings', 'the compression space; the rings stop air leaking past the piston'],
            ['Suction valve', 'opens only when the cylinder pressure falls below the inlet pressure'],
            ['Delivery valve', 'opens only when the cylinder pressure rises above the receiver pressure'],
            ['Connecting rod and crankshaft', 'turn the rotation of the motor into piston movement'],
            ['Flywheel', 'stores energy so the crank turns smoothly through the compression stroke'],
            ['Intercooler (multi-stage)', 'cools the air between stages so the next stage does less work'],
            ['Aftercooler, receiver, dryer, filter', 'cool, store and clean the air before use'],
            ['Clearance space', 'the small space left at the end of the stroke; kept minimum because it reduces '
                               'volumetric efficiency'],
        ]),
        h4('Working — step and reason'),
        steps(('Suction stroke', 'The piston moves down; the pressure falls below the inlet pressure, the suction '
                                 'valve opens and air at P<sub>1</sub> fills the cylinder.'),
              ('Compression', 'The piston moves up with both valves closed, so the trapped air is compressed and its '
                              'pressure rises towards P<sub>2</sub>.'),
              ('Delivery', 'When the pressure reaches P<sub>2</sub> the delivery valve opens and the air is pushed into '
                           'the receiver.'),
              ('Clearance effect', 'Air left in the clearance space must re-expand before the suction valve can open, so '
                                   'the volumetric efficiency is always below 100 %.'),
              ('Multi-stage', 'Two or three stages with intercooling keep the air temperature low, reduce the work per '
                              'stage and raise the overall efficiency.')),
        h4('Work and efficiencies'),
        work('Isothermal work per kg: W = P1 V1 × ln ' + frac('P2', 'P1'),
             'Volumetric efficiency = ' + frac('actual volume of air drawn in', 'swept volume of the piston') + ' × 100 %',
             'Isothermal efficiency = ' + frac('isothermal work', 'actual indicated work') + ' × 100 %'),
        h4('Advantages and limitations'),
        bullets('Very high pressure is possible, efficiency is good, and the machine is robust and simple to maintain.',
                'Delivery is pulsating and needs a receiver; the machine is bulky and heavy, has many moving parts, '
                'needs a strong foundation, and the air picks up oil — so an oil-free instrument-air system needs a '
                'filter or a non-lubricated compressor.'),
    ),
    gu=join(
        h4('એ શું છે'),
        p('<b>Reciprocating air compressor</b> એ positive-displacement machine છે. Cylinderમાં ફરતો piston ચોક્કસ volumeની '
          'હવા ખેંચે અને પછી તેને નાના volumeમાં દબાવીને pressure વધારે. Single-stage લગભગ 6 bar સુધી; intercooler '
          'સાથે two-stage 6–15 bar કે વધુ આપે.'),
        figure(fig.air_compressor_reciprocating(), 'આકૃતિ 4.1 · Single-stage reciprocating compressor.'),
        h4('રચના — ભાગ અને કામ'),
        table(['ભાગ', 'કામ'], [
            ['Cylinder અને piston (rings સાથે)', 'compressionની જગ્યા; rings piston પાસેથી હવા લીક થતી રોકે'],
            ['Suction valve', 'cylinderનું pressure inlet કરતાં ઓછું થાય ત્યારે ખૂલે'],
            ['Delivery valve', 'cylinderનું pressure receiver કરતાં વધે ત્યારે ખૂલે'],
            ['Connecting rod અને crankshaft', 'motorના rotationને pistonની હિલચાલમાં ફેરવે'],
            ['Flywheel', 'energy સંગ્રહીને crank સરખું ચાલે એ જાળવે'],
            ['Intercooler (multi-stage)', 'stage વચ્ચે હવા ઠંડી કરે, જેથી આગળના stageને ઓછું કામ પડે'],
            ['Aftercooler, receiver, dryer, filter', 'વપરાશ પહેલાં હવા ઠંડી, સંગ્રહિત અને સાફ કરે'],
            ['Clearance space', 'strokeના અંતે બાકી રહેતી થોડી જગ્યા; ઓછી રાખાય કારણ કે volumetric efficiency ઘટાડે'],
        ]),
        h4('કાર્ય — સ્ટેપ અને કારણ'),
        steps(('Suction stroke', 'Piston નીચે જાય; pressure inlet કરતાં ઓછું થતાં suction valve ખૂલે અને P<sub>1</sub> '
                                 'પરની હવા cylinder ભરે.'),
              ('Compression', 'Piston ઉપર જાય અને બંને valve બંધ હોય, એટલે હવા દબાય અને pressure P<sub>2</sub> તરફ વધે.'),
              ('Delivery', 'Pressure P<sub>2</sub> સુધી પહોંચે ત્યારે delivery valve ખૂલે અને હવા receiverમાં જાય.'),
              ('Clearanceની અસર', 'Clearance spaceમાં બાકી રહેલી હવા ફરી expand થાય ત્યારે જ suction valve ખૂલે, એટલે '
                                  'volumetric efficiency હંમેશા 100 %થી ઓછી રહે.'),
              ('Multi-stage', 'Intercooling સાથે બે–ત્રણ stage રાખવાથી હવાનું temperature ઓછું રહે, પ્રતિ stage કામ ઘટે '
                              'અને કુલ efficiency વધે.')),
        h4('કામ અને efficiency'),
        work('Isothermal work પ્રતિ kg: W = P1 V1 × ln ' + frac('P2', 'P1'),
             'Volumetric efficiency = ' + frac('ખરેખર ખેંચેલી હવાનું volume', 'pistonનું swept volume') + ' × 100 %',
             'Isothermal efficiency = ' + frac('isothermal work', 'actual indicated work') + ' × 100 %'),
        h4('ફાયદા અને મર્યાદાઓ'),
        bullets('ખૂબ ઊંચું pressure મળે, efficiency સારી, machine મજબૂત અને સહેલાઈથી maintain થાય.',
                'Delivery pulsating હોય અને receiver જોઈએ; machine ભારે–મોટી, ઘણા moving parts, મજબૂત foundation જોઈએ, '
                'અને હવામાં oil ભળે — એટલે oil-free instrument air માટે filter કે non-lubricated compressor જોઈએ.'),
    ),
))

Q4['cards'].append(dict(
    number='Q.4 (a)', marks=3, tag='OR', q='List application of Nitrogen as Inert gas.',
    en=join(
        h4('Nitrogen as an inert gas — applications'),
        bullets('<b>Tank blanketing:</b> a nitrogen pad over a flammable solvent keeps air out, so no explosive '
                'mixture can form.',
                '<b>Purging before start-up and before maintenance:</b> lines and vessels are displaced with nitrogen '
                'so no flammable vapour or oxygen remains.',
                '<b>Inert atmosphere in reactors:</b> for oxidation-sensitive products, polymerisation and grinding of '
                'powders.',
                '<b>Pressure transfer:</b> nitrogen pushes a liquid from one vessel to another where a pump could '
                'damage the product or leak.',
                '<b>Packaging:</b> food and pharmaceutical packs are flushed with nitrogen to extend shelf life.',
                '<b>Storage-tank blanketing</b> for oils, and protection of catalyst during loading.',
                '<b>Safety:</b> nitrogen keeps the oxygen level below the limiting oxygen concentration.'),
        p('It is used because it is chemically almost unreactive, cheap, and available on site from an air-separation '
          'unit or a nitrogen generator.'),
    ),
    gu=join(
        h4('Inert gas તરીકે nitrogenની એપ્લિકેશન'),
        bullets('<b>Tank blanketing:</b> flammable solvent ઉપર nitrogenનું પડ રહે, એટલે હવા અંદર આવતી નથી અને explosive '
                'mixture બનતું નથી.',
                '<b>Start-up અને maintenance પહેલાં purging:</b> line અને vesselમાંથી હવા કાઢીને nitrogen ભરાય, જેથી '
                'flammable vapour કે oxygen ન રહે.',
                '<b>Reactorમાં inert વાતાવરણ:</b> oxidation-sensitive product, polymerisation અને powder grinding માટે.',
                '<b>Pressure transfer:</b> pumpને બદલે nitrogenના pressureથી liquid એક vesselમાંથી બીજામાં ખસેડાય.',
                '<b>Packaging:</b> food અને pharma packમાં nitrogen ભરીને shelf life વધારાય.',
                '<b>Storage-tank blanketing</b> (oil) અને loading દરમિયાન catalystની સુરક્ષા.',
                '<b>સુરક્ષા:</b> oxygenનું પ્રમાણ limiting oxygen concentrationથી નીચે રાખવા nitrogen વપરાય.'),
        p('Nitrogen વપરાય કારણ કે એ chemical રીતે લગભગ નિષ્ક્રિય છે, સસ્તું છે અને air-separation unit કે nitrogen '
          'generatorથી જગ્યા પર જ મળે છે.'),
    ),
))

Q4['cards'].append(dict(
    number='Q.4 (b)', marks=4, tag='OR', q='Differentiate Reciprocating and Centrifugal type of Air compressor.',
    en=join(
        h4('Difference'),
        table(['Point', 'Reciprocating compressor', 'Centrifugal compressor'], [
            ['Principle', 'positive displacement — the piston squeezes a trapped volume',
             'dynamic — a rotating impeller gives velocity, the diffuser converts it into pressure'],
            ['Pressure', 'very high, 6–15 bar or more in multi-stage', 'low to medium, about 2–8 bar per stage'],
            ['Capacity', 'small to medium', 'very large'],
            ['Flow', 'pulsating, needs a receiver', 'continuous and steady'],
            ['Efficiency', 'high at high pressure', 'high only near the design point, falls at part load'],
            ['Size and weight', 'bulky and heavy, needs a strong foundation', 'compact and light for the same flow'],
            ['Air quality', 'oil is carried with the air', 'oil-free delivery is possible'],
            ['Maintenance', 'many moving parts, valves and rings to replace', 'few moving parts, smooth running, less maintenance'],
            ['Cost', 'cheaper for small capacity and high pressure', 'cheaper for large flow'],
            ['Typical use', 'instrument air, high-pressure process, workshops', 'plant air, ventilation, blowers, large process air'],
        ]),
        p('In short: for <b>high pressure with a small flow</b> choose reciprocating; for <b>large flow at moderate '
          'pressure</b> choose centrifugal.'),
    ),
    gu=join(
        h4('તફાવત'),
        table(['મુદ્દો', 'Reciprocating compressor', 'Centrifugal compressor'], [
            ['સિદ્ધાંત', 'positive displacement — piston ચોક્કસ volume દબાવે',
             'dynamic — ફરતું impeller velocity આપે, diffuser એને pressureમાં ફેરવે'],
            ['Pressure', 'ખૂબ ઊંચું, multi-stageમાં 6–15 bar કે વધુ', 'ઓછું–મધ્યમ, પ્રતિ stage લગભગ 2–8 bar'],
            ['ક્ષમતા', 'નાની–મધ્યમ', 'ખૂબ મોટી'],
            ['Flow', 'pulsating, receiver જોઈએ', 'સતત અને સરખો'],
            ['Efficiency', 'ઊંચા pressure પર ઊંચી', 'design point પાસે ઊંચી, part load પર ઘટે'],
            ['કદ અને વજન', 'મોટું–ભારે, મજબૂત foundation જોઈએ', 'એ જ flow માટે compact અને હલકું'],
            ['હવાની ગુણવત્તા', 'હવા સાથે oil જાય', 'oil-free delivery શક્ય'],
            ['Maintenance', 'ઘણા moving parts, valve–ring બદલવા પડે', 'ઓછા moving parts, સરળ ચાલે, ઓછું maintenance'],
            ['ખર્ચ', 'નાની ક્ષમતા–ઊંચા pressure માટે સસ્તું', 'મોટા flow માટે સસ્તું'],
            ['સામાન્ય ઉપયોગ', 'instrument air, ઊંચા pressureનું process, workshop', 'plant air, ventilation, blower, મોટા process air'],
        ]),
        p('ટૂંકમાં: <b>ઊંચું pressure અને ઓછો flow</b> હોય તો reciprocating; <b>મોટો flow અને મધ્યમ pressure</b> હોય તો centrifugal.'),
    ),
))

Q4['cards'].append(dict(
    number='Q.4 (c)', marks=7, tag='OR', q='Explain Rotary compressors in detail.',
    en=join(
        h4('What they are'),
        p('<b>Rotary compressors</b> are positive-displacement machines in which the compressing element rotates '
          'continuously instead of reciprocating. Because there is no reciprocating mass they run smooth and give '
          'a steady, pulsation-free flow at moderate pressure, about 1–10 bar.'),
        h4('Main types'),
        table(['Type', 'How the air is trapped and squeezed'], [
            ['Screw compressor (twin-screw)', 'two meshing rotors trap air between the lobes; as they turn the space '
                                              'shrinks and the air is pushed to the delivery end'],
            ['Sliding-vane compressor', 'a rotor with radial vanes runs eccentrically in the casing; the space between '
                                        'two vanes shrinks as the rotor turns'],
            ['Roots blower', 'two lobes rotate without touching; air is displaced from inlet to outlet at almost '
                             'constant volume, for large volume at low pressure'],
            ['Liquid-ring compressor', 'a rotating ring of water seals the spaces and acts as the compressing element; '
                                       'handles dirty or explosive gases'],
        ]),
        h4('Construction — screw compressor as the example'),
        table(['Part', 'Purpose'], [
            ['Male and female rotors in a casing', 'trap and squeeze the air; the rotors are the only main moving parts'],
            ['Inlet and outlet ports', 'placed at the ends, so air enters at the large-volume end and leaves at the '
                                       'small-volume end'],
            ['Synchronising gears', 'keep the two rotors in mesh without touching'],
            ['Oil injection (oil-flooded type)', 'seals the clearances, carries away the heat of compression and '
                                                 'lubricates the bearings'],
            ['Oil separator, cooler and filter', 'clean and cool the air before it reaches the receiver'],
            ['Unloading valve or capacity control', 'matches the air output to the demand'],
        ]),
        h4('Working — step and reason'),
        steps(('Step 1', 'The rotors turn; their lobes open at the inlet, so air is drawn into the space between them.'),
              ('Step 2', 'As the rotors mesh, the trapped space is closed off from the inlet.'),
              ('Step 3', 'Further rotation makes the space smaller, so the air is compressed.'),
              ('Step 4', 'When the outlet port is uncovered, the compressed air leaves into the receiver. The cycle is '
                         'continuous, so the delivery is steady.'),
              ('Step 5', 'In an oil-flooded machine the oil is separated, cooled and returned; the air is cooled and '
                         'dried before use.')),
        h4('Advantages and limitations'),
        bullets('Compact and light for the air delivered, steady delivery, few moving parts, low vibration, small '
                'foundation, and fully automatic control is possible.',
                'Pressure per stage is limited; the rotors need precision machining and sealing; the oil-flooded type '
                'needs an oil separator, or must be oil-free for instrument air; and efficiency falls at part load '
                'unless a variable-speed drive is used.'),
    ),
    gu=join(
        h4('એ શું છે'),
        p('<b>Rotary compressors</b>માં compressing element સતત ફરે છે, ઉપર–નીચે થતું નથી. Reciprocating mass ન હોવાથી '
          'એ સરળ ચાલે અને મધ્યમ pressure (લગભગ 1–10 bar) પર સતત, pulsation વગરનો flow આપે.'),
        h4('મુખ્ય પ્રકારો'),
        table(['પ્રકાર', 'હવા કેવી રીતે ફસાય અને દબાય'], [
            ['Screw compressor (twin-screw)', 'બે mesh થતા rotors lobe વચ્ચે હવા ફસાવે; ફરતાં જગ્યા ઘટે અને હવા delivery '
                                              'તરફ ધકેલાય'],
            ['Sliding-vane compressor', 'eccentric casingમાં radial vaneવાળો rotor ફરે; બે vane વચ્ચેની જગ્યા ઘટે'],
            ['Roots blower', 'બે lobes સ્પર્શ્યા વગર ફરે; લગભગ અચળ volume પર હવા inletથી outlet જાય'],
            ['Liquid-ring compressor', 'ફરતું પાણીનું ring જગ્યા સીલ કરે અને compress કરે; ગંદા કે explosive gas માટે યોગ્ય'],
        ]),
        h4('રચના — screw compressorનું ઉદાહરણ'),
        table(['ભાગ', 'કામ'], [
            ['Casingમાં male અને female rotor', 'હવા ફસાવે અને દબાવે; મુખ્ય moving parts ફક્ત આ બે'],
            ['Inlet અને outlet port', 'હવા મોટા volumeવાળા છેડેથી આવે અને નાના volumeવાળા છેડેથી નીકળે'],
            ['Synchronising gears', 'બંને rotor સ્પર્શ્યા વગર meshમાં રાખે'],
            ['Oil injection (oil-flooded પ્રકાર)', 'clearance સીલ કરે, compressionની heat કાઢે અને bearing lubricate કરે'],
            ['Oil separator, cooler અને filter', 'receiver પહેલાં હવા સાફ અને ઠંડી કરે'],
            ['Unloading valve કે capacity control', 'માંગ પ્રમાણે હવાનું output ગોઠવે'],
        ]),
        h4('કાર્ય — સ્ટેપ અને કારણ'),
        steps(('Step 1', 'Rotors ફરે છે અને inlet પાસે lobes ખૂલે, એટલે તેમની વચ્ચે હવા ભરાય.'),
              ('Step 2', 'Rotors mesh થતાં ફસાયેલી જગ્યા inletથી અલગ થઈ જાય.'),
              ('Step 3', 'વધુ ફરવાથી જગ્યા નાની થાય, એટલે હવા દબાય.'),
              ('Step 4', 'Outlet port ખૂલે ત્યારે compressed હવા receiverમાં જાય. Cycle સતત ચાલે એટલે delivery steady રહે.'),
              ('Step 5', 'Oil-flooded machineમાં oil અલગ કરી, ઠંડું કરી ફરી વપરાય; હવા ઠંડી અને સૂકી કરીને વપરાય.')),
        h4('ફાયદા અને મર્યાદાઓ'),
        bullets('આપેલી હવા માટે compact અને હલકું, steady delivery, ઓછા moving parts, ઓછું vibration, નાનું foundation '
                'અને સંપૂર્ણ automatic control શક્ય.',
                'પ્રતિ stage pressure મર્યાદિત; rotorને ચોક્કસ machining અને sealing જોઈએ; oil-flooded પ્રકારમાં oil '
                'separator જોઈએ, કે instrument air માટે oil-free હોવું જોઈએ; અને variable-speed drive વગર part load '
                'પર efficiency ઘટે.'),
    ),
))

# ---------------------------------------------------------------- Q5
Q5 = {
    'title_en': 'Q5 · Refrigeration performance, multistage compression and refrigerants',
    'title_gu': 'પ્ર.5 · રેફ્રિજરેશન પર્ફોર્મન્સ, મલ્ટીસ્ટેજ કોમ્પ્રેશન અને રેફ્રિજરેન્ટ',
    'cards': [],
}

Q5['cards'].append(dict(
    number='Q.5 (a)', marks=3, q='Explain COP and TOR in refrigeration.',
    en=join(
        h4('COP — coefficient of performance'),
        p('<b>COP</b> is the cooling effect obtained for each unit of work supplied to the compressor. It is the '
          'measure of how good a refrigerator is:'),
        work('COP = ' + frac('heat absorbed in the evaporator, QL', 'work input to the compressor, W')),
        work('COP = ' + frac('QL', 'W') + ' = ' + frac('QL', 'QH − QL')),
        p('<b>Example (illustrative):</b> a refrigerator removes 3 kW from the cold space with a 1 kW compressor, so '
          'COP = 3 / 1 = <b>3</b>. A domestic refrigerator runs at COP about 2–4, a well-designed plant 5–6. COP has '
          'no unit, and a higher COP means less electricity for the same cooling.'),
        h4('TOR — tonne of refrigeration'),
        p('<b>TOR</b> (or TON) is a unit of cooling <b>capacity</b>, not of efficiency. One tonne of refrigeration is '
          'the heat absorbed in melting one tonne (1,000 kg) of ice at 0 °C in 24 hours:'),
        work('1 TOR = ' + frac('1000 kg × 334 kJ/kg', '24 × 3600 s') + ' = 3.86 kJ/s ≈ <b>3.5 kW</b>'),
        p('So a 5-tonne plant means 5 × 3.5 = 17.5 kW of cooling. The same plant can have any COP — COP describes '
          'efficiency, TOR describes size.'),
    ),
    gu=join(
        h4('COP — coefficient of performance'),
        p('<b>COP</b> એટલે compressorને આપેલા એક unit work સામે મળતું cooling. એટલે refrigerator કેટલું સારું છે તેનું માપ:'),
        work('COP = ' + frac('evaporatorમાં શોષાયેલી heat, QL', 'compressorને આપેલું work, W')),
        work('COP = ' + frac('QL', 'W') + ' = ' + frac('QL', 'QH − QL')),
        p('<b>ઉદાહરણ (સમજવા માટે):</b> refrigerator cold spaceમાંથી 3 kW heat લે અને compressor 1 kW વાપરે, તો '
          'COP = 3 / 1 = <b>3</b>. ઘરેલું ફ્રિજનો COP લગભગ 2–4 અને સારા plantનો 5–6. COPને unit હોતું નથી; COP વધુ એટલે '
          'એ જ ઠંડક માટે ઓછી electricity.'),
        h4('TOR — tonne of refrigeration'),
        p('<b>TOR</b> (કે TON) એ cooling <b>capacity</b>નું unit છે, efficiencyનું નહીં. 1 tonne refrigeration એટલે 0 °C પર '
          '24 કલાકમાં 1 tonne (1,000 kg) બરફ પીગળવા માટે શોષાતી heat:'),
        work('1 TOR = ' + frac('1000 kg × 334 kJ/kg', '24 × 3600 s') + ' = 3.86 kJ/s ≈ <b>3.5 kW</b>'),
        p('એટલે 5 tonne plant એટલે 5 × 3.5 = 17.5 kW cooling. એ જ plantનો COP કોઈ પણ હોઈ શકે — COP efficiency બતાવે, '
          'TOR કદ બતાવે.'),
    ),
))

Q5['cards'].append(dict(
    number='Q.5 (b)', marks=4, q='Explain Energy efficient Multistage compressors.',
    en=join(
        h4('Why one stage is not enough'),
        p('If the whole pressure rise is done in one stage, the air becomes very hot, the delivery temperature limits '
          'the pressure ratio to about 5–6, and much of the work is wasted as heat. A <b>multistage compressor</b> '
          'divides the compression into two or three stages with an <b>intercooler</b> between them.'),
        h4('Why intercooling saves energy'),
        p('The air is cooled back to almost the inlet temperature between the stages. The volume to be compressed in '
          'the next stage is therefore smaller, so the work of that stage falls. With perfect intercooling the saving '
          'is large — two stages need less work than one stage for the same total pressure ratio.'),
        work('Optimum intermediate pressure, two stages: P2 = √(P1 × P3)',
             'Saving in work = area between the single-stage and the two-stage indicator diagram'),
        h4('Other energy-saving features'),
        bullets('Intercooler and aftercooler with a large, clean heat-transfer surface.',
                'Good valves and minimum clearance volume, so the volumetric efficiency stays high.',
                'Variable-speed drive or load–unload control, so the machine does not run fully loaded at part demand.',
                'Dry air filters and a leak-free distribution line: lowering the line pressure by 1 bar saves roughly '
                '6–8 % of the compressor power.'),
        p('Overall: multistage compression with intercooling lowers the delivery temperature, lowers the power per kg '
          'of air, improves the volumetric efficiency and gives cooler, drier air.'),
    ),
    gu=join(
        h4('એક stage કેમ પૂરતું નથી'),
        p('આખું pressure એક જ stageમાં વધારીએ તો હવા ખૂબ ગરમ થાય, delivery temperatureને કારણે pressure ratio લગભગ '
          '5–6 સુધી મર્યાદિત રહે અને ઘણું કામ heat તરીકે વેડફાય. <b>Multistage compressor</b>માં compression બે–ત્રણ '
          'stageમાં વહેંચાય અને વચ્ચે <b>intercooler</b> રાખાય.'),
        h4('Intercoolingથી energy કેમ બચે'),
        p('Stage વચ્ચે હવા લગભગ inlet temperature સુધી ઠંડી કરાય. એટલે પછીના stageમાં compress કરવાનું volume નાનું '
          'થાય અને એ stageનું કામ ઘટે. સારા intercooling સાથે બચત ઘણી થાય — એ જ કુલ pressure ratio માટે બે stageને '
          'એક stage કરતાં ઓછું કામ જોઈએ.'),
        work('બે stage માટે optimum intermediate pressure: P2 = √(P1 × P3)',
             'કામમાં બચત = single-stage અને two-stage indicator diagram વચ્ચેનું ક્ષેત્રફળ'),
        h4('બીજાં energy-saving પગલાં'),
        bullets('મોટા અને સાફ heat-transfer surfaceવાળા intercooler તથા aftercooler.',
                'સારા valve અને ઓછું clearance volume, જેથી volumetric efficiency ઊંચી રહે.',
                'Variable-speed drive કે load–unload control, જેથી ઓછી માંગમાં machine પૂરી load પર ન ચાલે.',
                'સૂકા air filter અને leak-free line: lineનું pressure 1 bar ઘટાડવાથી compressor powerમાં લગભગ '
                '6–8 % બચે.'),
        p('એટલે: intercoolingવાળું multistage compression delivery temperature ઘટાડે, પ્રતિ kg હવાનું power ઘટાડે, '
          'volumetric efficiency સુધારે અને ઠંડી–સૂકી હવા આપે.'),
    ),
))

Q5['cards'].append(dict(
    number='Q.5 (c)', marks=7, q='Explain Primary Refrigerants Halo Carbons & Hydrocarbons.',
    en=join(
        h4('Primary and secondary refrigerant'),
        p('A <b>primary refrigerant</b> is the fluid that actually changes phase in the cycle — it absorbs heat in '
          'the evaporator and rejects it in the condenser. A <b>secondary refrigerant</b> such as water or brine '
          'merely carries heat from the load to the primary refrigerant.'),
        h4('1 · Halocarbons'),
        p('These are derivatives of methane and ethane in which hydrogen atoms are replaced by chlorine and fluorine. '
          'The familiar Freons belong to this family. Their great advantage is that they are non-toxic and '
          'non-flammable.'),
        table(['Refrigerant', 'Chemical name', 'Use and note'], [
            ['R-11 (CFCl<sub>3</sub>)', 'trichlorofluoromethane', 'large centrifugal chillers; very high ozone depletion, phased out'],
            ['R-12 (CCl<sub>2</sub>F<sub>2</sub>)', 'dichlorodifluoromethane', 'old domestic refrigerators and car AC; phased out'],
            ['R-22 (CHClF<sub>2</sub>)', 'chlorodifluoromethane', 'window AC and cold storage; being phased out'],
            ['R-134a (CH<sub>2</sub>FCF<sub>3</sub>)', 'tetrafluoroethane', 'present-day domestic and car AC; zero ozone depletion'],
            ['R-410A (blend)', 'R-32 / R-125 mixture', 'modern split AC; higher pressure, zero ozone depletion'],
        ]),
        h4('Properties and behaviour of halocarbons'),
        bullets('Non-toxic, non-flammable, colourless and odourless, so they are safe to handle — that is why they '
                'replaced ammonia and SO<sub>2</sub> in domestic machines.',
                'Miscible with lubricating oil and stable in the machine; the latent heat per unit volume is lower than '
                'ammonia, so a larger compressor is needed for the same duty.',
                'Very low boiling point, so a small pressure difference gives deep cooling.',
                'CFC and HCFC halocarbons destroy stratospheric ozone and have a high global-warming potential; the '
                'Montreal Protocol and the Kigali Amendment schedule their phase-out. HFCs such as R-134a are '
                'ozone-safe but still warm the climate, so HFOs and natural refrigerants are replacing them.'),
        h4('2 · Hydrocarbons'),
        p('Hydrocarbons are simple organic compounds — methane, ethane, propane, butane, isobutane and their mixtures. '
          'They are excellent refrigerants thermodynamically, but they are flammable.'),
        table(['Refrigerant', 'Name', 'Typical use'], [
            ['R-290', 'propane', 'domestic and small commercial refrigerators, heat pumps'],
            ['R-600a', 'isobutane', 'domestic refrigerators, charge only about 50–150 g'],
            ['R-600', 'butane', 'low-temperature work and mixture components'],
            ['R-170 / R-50', 'ethane / methane', 'cryogenic and very low-temperature plants'],
            ['R-1270', 'propylene', 'industrial refrigeration and mixtures'],
        ]),
        h4('Properties of hydrocarbons as refrigerants'),
        bullets('High latent heat and a good heat-transfer coefficient, so the charge is small and efficiency high.',
                'Zero ozone-depletion potential and a very low global-warming potential — the reason they are returning '
                'as natural refrigerants.',
                'Cheap and easily available (the LPG family) and compatible with ordinary mineral oil.',
                'They are flammable and form an explosive mixture with air, so the charge is kept small, the circuit '
                'is sealed, electrical parts are spark-free and the room is ventilated. They have no smell, so a leak '
                'is not noticed by smell alone.'),
        h4('Comparing the two families'),
        table(['Point', 'Halocarbons', 'Hydrocarbons'], [
            ['Safety', 'non-flammable, low toxicity', 'flammable, explosive in air'],
            ['Ozone depletion', 'high for CFC/HCFC, zero for HFC', 'zero'],
            ['Global-warming potential', 'high for CFC and HFC', 'very low'],
            ['Efficiency', 'moderate', 'high with a small charge'],
            ['Cost and availability', 'costly and controlled', 'cheap and easily available'],
            ['Present status', 'being phased down', 'preferred as natural refrigerant'],
        ]),
        p('Selection: R-134a and R-410A remain common where the charge is large and fire risk must be avoided; R-600a '
          'and R-290 are standard in sealed domestic appliances because the charge is only a few tens of grams.'),
    ),
    gu=join(
        h4('Primary અને secondary refrigerant'),
        p('<b>Primary refrigerant</b> એ દ્રવ્ય છે જે cycleમાં ખરેખર phase change પામે — evaporatorમાં heat લે અને '
          'condenserમાં છોડે. <b>Secondary refrigerant</b> (પાણી કે brine) ફક્ત loadની heat primary refrigerant સુધી પહોંચાડે.'),
        h4('1 · Halocarbons'),
        p('આ methane અને ethaneના derivatives છે, જેમાં hydrogen atomsની જગ્યાએ chlorine અને fluorine આવે છે. Freon કહેવાતું '
          'આ જ કુટુંબ છે. એમનો મોટો ફાયદો — non-toxic અને non-flammable.'),
        table(['Refrigerant', 'રાસાયણિક નામ', 'ઉપયોગ અને નોંધ'], [
            ['R-11 (CFCl<sub>3</sub>)', 'trichlorofluoromethane', 'મોટા centrifugal chiller; ozone depletion ખૂબ વધુ, બંધ'],
            ['R-12 (CCl<sub>2</sub>F<sub>2</sub>)', 'dichlorodifluoromethane', 'જૂનું ફ્રિજ અને car AC; બંધ'],
            ['R-22 (CHClF<sub>2</sub>)', 'chlorodifluoromethane', 'window AC અને cold storage; ધીમે ધીમે બંધ'],
            ['R-134a (CH<sub>2</sub>FCF<sub>3</sub>)', 'tetrafluoroethane', 'આજનું ફ્રિજ અને car AC; ozone depletion શૂન્ય'],
            ['R-410A (blend)', 'R-32 / R-125 મિશ્રણ', 'આધુનિક split AC; pressure વધુ, ozone depletion શૂન્ય'],
        ]),
        h4('Halocarbonનાં ગુણધર્મો'),
        bullets('Non-toxic, non-flammable, રંગ–ગંધ વગરનાં, એટલે વાપરવામાં સુરક્ષિત — એટલે જ ઘરેલું machineમાં ammonia '
                'અને SO<sub>2</sub>ની જગ્યાએ આવ્યાં.',
                'Lubricating oilમાં ભળે અને machineમાં stable રહે; ammonia કરતાં પ્રતિ volume latent heat ઓછી, એટલે એ જ '
                'કામ માટે મોટું compressor જોઈએ.',
                'Boiling point ખૂબ નીચું, એટલે નાના pressure તફાવતથી ઊંડી ઠંડક મળે.',
                'CFC–HCFC stratospheric ozone બગાડે અને global-warming potential ઊંચું હોય; Montreal Protocol અને Kigali '
                'Amendment એમનો phase-out નક્કી કરે. HFC (R-134a) ozone માટે સુરક્ષિત છે પણ climate માટે હાનિકારક, એટલે '
                'HFO અને natural refrigerants આવી રહ્યા છે.'),
        h4('2 · Hydrocarbons'),
        p('Hydrocarbons સાદા organic સંયોજનો છે — methane, ethane, propane, butane, isobutane અને તેમનાં મિશ્રણ. '
          'Thermodynamically ઉત્તમ refrigerant છે, પણ flammable છે.'),
        table(['Refrigerant', 'નામ', 'સામાન્ય ઉપયોગ'], [
            ['R-290', 'propane', 'ઘરેલું અને નાનું commercial ફ્રિજ, heat pump'],
            ['R-600a', 'isobutane', 'ઘરેલું ફ્રિજ, charge ફક્ત 50–150 g'],
            ['R-600', 'butane', 'નીચા temperatureનું કામ અને mixtureમાં'],
            ['R-170 / R-50', 'ethane / methane', 'cryogenic અને ખૂબ નીચા temperatureનાં plant'],
            ['R-1270', 'propylene', 'industrial refrigeration અને mixtures'],
        ]),
        h4('Hydrocarbonનાં ગુણધર્મો'),
        bullets('Latent heat વધુ અને heat-transfer coefficient સારો, એટલે charge ઓછું અને efficiency ઊંચી.',
                'Ozone-depletion શૂન્ય અને global-warming potential ખૂબ ઓછું — એટલે natural refrigerant તરીકે પાછાં આવે છે.',
                'સસ્તાં, સહેલાઈથી મળે (LPG કુટુંબ) અને સામાન્ય mineral oil સાથે compatible.',
                'Flammable હોય અને હવા સાથે explosive મિશ્રણ બનાવે, એટલે charge ઓછું રાખાય, circuit sealed રાખાય, '
                'electrical parts spark-free હોય અને જગ્યા ventilated હોય. ગંધ ન હોવાથી leak ગંધથી ખબર ન પડે.'),
        h4('બંને કુટુંબની સરખામણી'),
        table(['મુદ્દો', 'Halocarbons', 'Hydrocarbons'], [
            ['સુરક્ષા', 'non-flammable, ઓછું toxicity', 'flammable, હવામાં explosive'],
            ['Ozone depletion', 'CFC–HCFC વધુ, HFC શૂન્ય', 'શૂન્ય'],
            ['Global-warming potential', 'CFC–HFC વધુ', 'ખૂબ ઓછું'],
            ['Efficiency', 'મધ્યમ', 'ઓછા charge સાથે ઊંચી'],
            ['ખર્ચ અને ઉપલબ્ધતા', 'મોંઘા અને નિયંત્રિત', 'સસ્તા અને સહેલાઈથી મળે'],
            ['હાલની સ્થિતિ', 'ધીમે ધીમે ઘટે છે', 'natural refrigerant તરીકે પસંદ'],
        ]),
        p('પસંદગી: charge મોટું હોય અને આગનું જોખમ ટાળવું હોય ત્યાં R-134a–R-410A; અને સીલબંધ ઘરેલું ઉપકરણમાં charge '
          'થોડા ગ્રામ જ હોવાથી R-600a–R-290 પ્રમાણભૂત પસંદગી છે.'),
    ),
))

Q5['cards'].append(dict(
    number='Q.5 (a)', marks=3, tag='OR', q="Explain secondary Refrigerant's water & brine.",
    en=join(
        h4('What a secondary refrigerant is'),
        p('A <b>secondary refrigerant</b> does not change phase in the cycle. It is cooled by the primary refrigerant '
          'in a central plant and then pumped around to pick up heat from the load. Water and brine are the two '
          'common ones.'),
        h4('Water'),
        bullets('Cheap, easily available, high specific heat (4.18 kJ/kg·K), non-flammable, non-toxic and not corrosive '
                'to clean steel.',
                'It cannot go below 0 °C, so it is used for air-conditioning and chilled-water coils at 5–12 °C.',
                'It needs a closed circuit with a small pump head, and treatment against algae and scale.'),
        h4('Brine'),
        p('A <b>brine</b> is a solution of calcium chloride or sodium chloride in water. The salt lowers the freezing '
          'point, so brine works below 0 °C: CaCl<sub>2</sub> brine down to about −40 °C and NaCl brine to about −18 °C.'),
        bullets('Used in ice plants, cold stores, dairy chilling and fisheries, where the coil is at −5 to −25 °C.',
                'Specific heat is lower and viscosity higher than water, so more pumping power is needed.',
                'It is corrosive to steel and cast iron, so inhibitors are added and leakage into food must be '
                'prevented. Strong brine absorbs moisture and becomes dilute, so its strength is checked with a hydrometer.'),
        h4('Comparison'),
        table(['Point', 'Water', 'Brine (CaCl<sub>2</sub>)'], [
            ['Temperature range', 'above 0 °C, typically 5–12 °C', 'down to about −40 °C'],
            ['Specific heat', '4.18 kJ/kg·K', 'about 2.7–3.0 kJ/kg·K'],
            ['Corrosion', 'low', 'high, needs an inhibitor'],
            ['Cost', 'almost free', 'chemical and maintenance cost'],
            ['Use', 'air-conditioning, chilled-water coils', 'ice plant, cold storage, dairy'],
        ]),
        p('The advantage of both is that a costly or hazardous primary refrigerant such as ammonia stays in the plant '
          'room, and only a harmless secondary fluid travels to the rooms.'),
    ),
    gu=join(
        h4('Secondary refrigerant એટલે શું'),
        p('<b>Secondary refrigerant</b> cycleમાં phase change પામતું નથી. કેન્દ્રીય plantમાં primary refrigerant એને ઠંડું '
          'કરે અને પછી એને pump કરીને load પાસે મોકલાય, જ્યાં એ heat લે. પાણી અને brine સૌથી સામાન્ય છે.'),
        h4('પાણી'),
        bullets('સસ્તું, સહેલાઈથી મળે, specific heat ઊંચી (4.18 kJ/kg·K), non-flammable, non-toxic અને સાફ steel પર corrosion નહીં.',
                '0 °Cથી નીચે જઈ શકે નહીં, એટલે air-conditioning અને chilled-water coilમાં 5–12 °C પર વપરાય.',
                'Closed circuit અને ઓછું pump head જોઈએ; algae અને scale સામે treatment જરૂરી.'),
        h4('Brine'),
        p('<b>Brine</b> એટલે પાણીમાં calcium chloride કે sodium chlorideનું દ્રાવણ. ક્ષાર freezing point નીચે લાવે, એટલે '
          'brine 0 °Cથી નીચે કામ કરે: CaCl<sub>2</sub> brine લગભગ −40 °C સુધી અને NaCl brine લગભગ −18 °C સુધી.'),
        bullets('Ice plant, cold store, dairy chilling અને fisheriesમાં વપરાય, જ્યાં coil −5 થી −25 °C હોય.',
                'પાણી કરતાં specific heat ઓછી અને viscosity વધુ, એટલે pumping power વધુ લાગે.',
                'Steel અને cast iron પર corrosive, એટલે inhibitor ઉમેરાય અને ખોરાકમાં leak ન થાય એ ધ્યાન રાખાય. મજબૂત '
                'brine ભેજ શોષીને dilute થાય, એટલે hydrometerથી strength ચેક કરાય.'),
        h4('સરખામણી'),
        table(['મુદ્દો', 'પાણી', 'Brine (CaCl<sub>2</sub>)'], [
            ['Temperature રેન્જ', '0 °Cથી ઉપર, સામાન્ય 5–12 °C', 'લગભગ −40 °C સુધી'],
            ['Specific heat', '4.18 kJ/kg·K', 'લગભગ 2.7–3.0 kJ/kg·K'],
            ['Corrosion', 'ઓછું', 'વધુ, inhibitor જોઈએ'],
            ['ખર્ચ', 'લગભગ મફત', 'chemical અને maintenance ખર્ચ'],
            ['ઉપયોગ', 'air-conditioning, chilled-water coil', 'ice plant, cold storage, dairy'],
        ]),
        p('બંનેનો ફાયદો એ છે કે મોંઘું કે જોખમી primary refrigerant (ammonia) plant roomમાં જ રહે અને નિરુપદ્રવી '
          'secondary fluid જ રૂમ સુધી જાય.'),
    ),
))

Q5['cards'].append(dict(
    number='Q.5 (b)', marks=4, tag='OR', q='List advantages of multistage compressor.',
    en=join(
        h4('Advantages of multistage compression'),
        bullets('<b>Lower work input:</b> intercooling shrinks the volume handled by the next stage, so the total power '
                'falls for the same pressure ratio.',
                '<b>Lower delivery temperature:</b> heat is removed between the stages, so the air leaves cooler and the '
                'oil, valves and rings last longer.',
                '<b>Better volumetric efficiency:</b> a smaller pressure ratio per stage means less clearance loss and '
                'more air actually delivered.',
                '<b>Higher pressure is reachable:</b> one stage is limited to a pressure ratio of about 5–6; three '
                'stages reach 100 bar and more.',
                '<b>Better mechanical balance:</b> the load is spread over several cylinders, so the flywheel and '
                'foundation can be lighter.',
                '<b>Smaller cylinders and less leakage:</b> each stage handles a smaller volume at a moderate '
                'temperature, which reduces wear and leakage past the piston.',
                '<b>Water and oil separation:</b> condensed moisture is drained at the intercooler and aftercooler, so '
                'the air is drier and cleaner.',
                '<b>Cheaper running and longer life:</b> lower temperature and lower load per stage reduce power and '
                'maintenance cost.'),
        p('Comparison of ideal work: compressing air from 1 bar to 9 bar in one stage needs much more work than two '
          'stages (1 → 3 → 9 bar) with perfect intercooling, because the area of the p–V diagram between the two '
          'paths is saved.'),
    ),
    gu=join(
        h4('Multistage compressionના ફાયદા'),
        bullets('<b>કામ ઓછું લાગે:</b> intercoolingથી આગળના stageમાં volume ઘટે, એટલે એ જ pressure ratio માટે કુલ power ઘટે.',
                '<b>Delivery temperature ઓછું:</b> heat stage વચ્ચે કાઢાય, એટલે હવા ઠંડી નીકળે અને oil, valve તથા ring લાંબું ટકે.',
                '<b>Volumetric efficiency સારી:</b> પ્રતિ stage નાનું pressure ratio એટલે clearance loss ઓછું અને ખરેખર '
                'મળતી હવા વધુ.',
                '<b>વધુ pressure મળે:</b> એક stage લગભગ 5–6 pressure ratio સુધી જ; ત્રણ stage 100 barથી વધુ સુધી પહોંચે.',
                '<b>Mechanical balance સારું:</b> load ઘણા cylinderમાં વહેંચાય, એટલે flywheel અને foundation હલકાં રાખી શકાય.',
                '<b>Cylinder નાનું અને leakage ઓછું:</b> દરેક stage નાનું volume મધ્યમ temperature પર સંભાળે, એટલે ઘસારો અને '
                'piston પાસેનું leakage ઘટે.',
                '<b>પાણી અને oil અલગ થાય:</b> intercooler–aftercoolerમાં ભેજ condense થઈને નીકળે, એટલે હવા સૂકી અને સાફ.',
                '<b>ચલાવવાનો ખર્ચ ઓછો, આયુષ્ય લાંબું:</b> ઓછું temperature અને પ્રતિ stage ઓછો load હોવાથી power તથા '
                'maintenance ખર્ચ ઘટે.'),
        p('Ideal કામની સરખામણી: 1 barથી 9 bar સુધી એક stage કરતાં સંપૂર્ણ intercoolingવાળા બે stage (1 → 3 → 9 bar) ઘણું '
          'ઓછું કામ લે, કારણ કે બંને રસ્તા વચ્ચેના p–V diagramનું ક્ષેત્રફળ બચે છે.'),
    ),
))

Q5['cards'].append(dict(
    number='Q.5 (c)', marks=7, tag='OR', q='Explain vapor compression refrigeration.',
    en=join(
        h4('Principle'),
        p('In <b>vapour-compression refrigeration</b> a volatile liquid — the refrigerant — is evaporated at low '
          'pressure and condensed at high pressure. Evaporation takes latent heat from the cold space, which is the '
          'cooling effect; condensation rejects that heat plus the compressor work to the surroundings.'),
        p('A compressor is necessary because the vapour must be raised in pressure before it can be condensed at '
          'ambient temperature.'),
        figure(fig.vapour_compression(), 'Fig. 5.1 · The four components and the four processes of the cycle.'),
        h4('Construction — part and purpose'),
        table(['Part', 'Purpose'], [
            ['Compressor', 'raises the vapour from evaporator pressure to condenser pressure; this is the work input'],
            ['Condenser', 'rejects heat to cooling water or air and liquefies the vapour'],
            ['Expansion valve or capillary', 'drops the pressure to the evaporator level and meters the flow, so the '
                                             'temperature falls'],
            ['Evaporator', 'absorbs heat from the space and evaporates the liquid refrigerant'],
            ['Receiver, drier and filter', 'store the liquid and remove moisture and dirt before the expansion valve'],
            ['Thermostat, HP/LP cut-out, sight glass', 'start and stop the compressor and protect the machine'],
        ]),
        h4('Working — four processes, step and reason'),
        steps(('1 → 2 Compression', 'Dry saturated vapour enters the compressor at low pressure and leaves at condenser '
                                    'pressure as superheated vapour. Work W is added, so its temperature rises above '
                                    'the ambient temperature.'),
              ('2 → 3 Condensation', 'In the condenser the vapour first gives up superheat and then condenses at '
                                     'constant pressure; heat Q<sub>H</sub> goes to the cooling medium.'),
              ('3 → 4 Expansion', 'Liquid at high pressure passes through the expansion valve; the pressure falls '
                                  'suddenly, part of the liquid flashes and the mixture cools to the evaporator '
                                  'temperature. No work is done in this step.'),
              ('4 → 1 Evaporation', 'The cold mixture enters the evaporator, absorbs heat Q<sub>L</sub> from the space '
                                    'and evaporates completely; the vapour returns to the compressor and the cycle '
                                    'repeats.')),
        h4('Performance'),
        work('COP = ' + frac('QL', 'W') + ' = ' + frac('h1 − h4', 'h2 − h1'),
             'Refrigerating effect per kg = h1 − h4',
             'Heat rejected at the condenser, QH = QL + W = h2 − h3'),
        h4('Advantages, limitations and use'),
        bullets('High COP, compact equipment, a wide choice of refrigerants, and it reaches −40 °C with a suitable '
                'refrigerant.',
                'It needs a compressor and electricity; the refrigerant can leak and is controlled by ozone and '
                'global-warming rules; moving parts need maintenance.',
                'Used in domestic refrigerators, water coolers, window and split AC, cold stores, dairy chilling and '
                'process cooling.'),
    ),
    gu=join(
        h4('સિદ્ધાંત'),
        p('<b>Vapour-compression refrigeration</b>માં એક volatile liquid (refrigerant) નીચા pressure પર બાષ્પ બને છે અને '
          'ઊંચા pressure પર condense થાય છે. Evaporation ઠંડી જગ્યામાંથી latent heat લે — એ જ cooling effect; '
          'condensation એ heat અને compressorનું work આસપાસને આપે છે.'),
        p('Compressor જરૂરી છે કારણ કે ambient temperature પર condense કરવા માટે vapourનું pressure પહેલાં વધારવું પડે.'),
        figure(fig.vapour_compression(), 'આકૃતિ 5.1 · ચાર ભાગ અને ચાર process.'),
        h4('રચના — ભાગ અને કામ'),
        table(['ભાગ', 'કામ'], [
            ['Compressor', 'vapourનું pressure evaporatorથી condenser સુધી વધારે; આ જ work input'],
            ['Condenser', 'cooling water કે હવાને heat આપી vapourને લિક્વિડ કરે'],
            ['Expansion valve કે capillary', 'pressure evaporator સુધી ઘટાડે અને flow માપે, જેથી temperature ઘટે'],
            ['Evaporator', 'જગ્યામાંથી heat લઈને liquid refrigerantને બાષ્પ બનાવે'],
            ['Receiver, drier અને filter', 'liquid સંગ્રહે અને expansion valve પહેલાં ભેજ તથા ગряж કાઢે'],
            ['Thermostat, HP/LP cut-out, sight glass', 'compressor on–off કરે અને machine સાચવે'],
        ]),
        h4('કાર્ય — ચાર process, સ્ટેપ અને કારણ'),
        steps(('1 → 2 Compression', 'Dry saturated vapour નીચા pressure પર compressorમાં જાય અને condenserના pressure પર '
                                    'superheated vapour તરીકે નીકળે. Work W ઉમેરાય, એટલે temperature ambientથી ઉપર જાય.'),
              ('2 → 3 Condensation', 'Condenserમાં vapour પહેલાં superheat છોડે અને પછી અચળ pressure પર condense થાય; '
                                     'heat Q<sub>H</sub> cooling mediumને જાય.'),
              ('3 → 4 Expansion', 'ઊંચા pressureનું liquid expansion valveમાંથી પસાર થાય; pressure અચાનક ઘટે, થોડું liquid '
                                  'flash થાય અને mixture evaporator temperature સુધી ઠંડું થાય. આ stepમાં કોઈ work થતું નથી.'),
              ('4 → 1 Evaporation', 'ઠં�डું mixture evaporatorમાં જાય, જગ્યામાંથી heat Q<sub>L</sub> લઈને પૂરું બાષ્પ બને; '
                                    'vapour ફરી compressorમાં જાય અને cycle ચાલુ રહે.')),
        h4('પર્ફોર્મન્સ'),
        work('COP = ' + frac('QL', 'W') + ' = ' + frac('h1 − h4', 'h2 − h1'),
             'Refrigerating effect પ્રતિ kg = h1 − h4',
             'Condenserમાં નીકળતી heat, QH = QL + W = h2 − h3'),
        h4('ફાયદા, મર્યાદાઓ અને ઉપયોગ'),
        bullets('COP ઊંચો, equipment compact, ઘણા refrigerants ઉપલબ્ધ, અને યોગ્ય refrigerant સાથે −40 °C સુધી જાય.',
                'Compressor અને electricity જોઈએ; refrigerant leak થઈ શકે અને તે ozone–global-warming નિયમો હેઠળ નિયંત્રિત '
                'છે; moving parts હોવાથી maintenance જોઈએ.',
                'ઉપયોગ: ઘરેલું ફ્રિજ, water cooler, window–split AC, cold store, dairy chilling અને process cooling.'),
    ),
))
