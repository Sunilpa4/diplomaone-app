"""DI01005011 Summer 2026 — Q1 and Q2 answer parts (Plant Utilities)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from paperkit import frac, work, steps, result, table, bullets, numbered, h4, p, eq, figure
import chemfigs as fig
import utilfigs as ufig


def join(*chunks):
    return "\n".join(c for c in chunks if c)


# ---------------------------------------------------------------- Q1
Q1 = {
    'title_en': 'Q1 · Plant utilities, water disinfection and lime–soda softening',
    'title_gu': 'પ્ર.1 · પ્લાન્ટ યુટિલિટી, પાણીનું જંતુમુક્તીકરણ અને ચૂના-સોડા નરમ કરવું',
    'cards': [],
}

Q1['cards'].append(dict(
    number='Q.1 (a)', marks=3, q='List six utilities in chemical plant',
    en=join(
        p('<b>Utilities</b> are the services — not the product — that a chemical plant must supply for its '
          'process to run. Six of them, with what each one is used for:'),
        table(['No.', 'Utility', 'Use in the plant'], [
            ['1', '<b>Water</b> (raw, filtered, soft, demineralised, cooling)', 'boiler feed, cooling '
             'tower make-up, process water, washing'],
            ['2', '<b>Steam</b> (saturated and superheated, at several pressures)',
             'heating of reactors and reboilers, distillation, ejectors, tracing'],
            ['3', '<b>Electricity</b> (power and lighting)', 'pumps, compressors, agitators, '
             'instrumentation, lighting'],
            ['4', '<b>Compressed air</b> and instrument air', 'pneumatic valves and actuators, tools, '
             'packing and cleaning'],
            ['5', '<b>Fuel</b> (coal, fuel oil, natural gas)', 'fired heaters, boilers, furnaces, '
             'incinerators'],
            ['6', '<b>Inert gas</b> (nitrogen, CO<sub>2</sub>)', 'tank blanketing, purging before '
             'maintenance, inert atmosphere for flammable material'],
        ]),
        p('<b>Example:</b> a distillation column needs steam in the reboiler, cooling water in the '
          'condenser, electricity for the reflux pump, instrument air for the control valve, and nitrogen '
          'for blanketing the reflux drum — five utilities for one unit, which is why utilities are '
          'planned before the plant layout.'),
    ),
    gu=join(
        p('<b>Utilities</b> એટલે એ સેવાઓ — product નહીં — જે chemical plantે પોતાની process ચલાવવા પૂરી પાડવી '
          'પડે. એમાંથી છ, અને દરેક શેના માટે:'),
        table(['ક્રમ', 'Utility', 'Plantમાં ઉપયોગ'], [
            ['1', '<b>પાણી</b> (raw, filtered, soft, demineralised, cooling)', 'boiler feed, cooling tower '
             'make-up, process water, ધોવા માટે'],
            ['2', '<b>Steam</b> (saturated અને superheated, જુદા જુદા pressure પર)',
             'reactor અને reboiler ગરમ કરવા, distillation, ejector, tracing'],
            ['3', '<b>Electricity</b> (power અને lighting)', 'pump, compressor, agitator, instrumentation, '
             'lighting'],
            ['4', '<b>Compressed air</b> અને instrument air', 'pneumatic valve અને actuator, સાધનો, packing '
             'તથા સફાઈ'],
            ['5', '<b>Fuel</b> (કોલસો, fuel oil, natural gas)', 'fired heater, boiler, furnace, incinerator'],
            ['6', '<b>Inert gas</b> (nitrogen, CO<sub>2</sub>)', 'tank blanketing, maintenance પહેલાં '
             'purging, જ્વલનશીલ પદાર્થ માટે inert વાતાવરણ'],
        ]),
        p('<b>ઉદાહરણ:</b> એક distillation columnને reboilerમાં steam, condenserમાં cooling water, reflux '
          'pump માટે electricity, control valve માટે instrument air અને reflux drumનાં blanketing માટે '
          'nitrogen જોઈએ — એક જ unit માટે પાંચ utility, એટલે જ plant layout પહેલાં utilitiesનું planning થાય.'),
    ),
))

Q1['cards'].append(dict(
    number='Q.1 (b)', marks=4,
    q='Write down the conventional methods to remove bacteria and micro-organism from water. and Explain '
      'any one in detail',
    en=join(
        h4('Conventional methods'),
        table(['Method', 'How it kills or removes the organism', 'Typical use'], [
            ['<b>Boiling</b>', 'heat at 100 °C coagulates the cell protein — kills all bacteria and cysts '
             'in 5–10 minutes', 'household and small-scale drinking water'],
            ['<b>Chlorination</b>', 'free chlorine (HOCl) oxidises the cell wall and the enzymes',
             'municipal water, cooling water, plant water distribution'],
            ['<b>Bleaching powder / chloramine</b>', 'same as chlorine, but a cheaper and slower source',
             'rural supply, wells, swimming pools'],
            ['<b>Ozone treatment</b>', 'ozone is a stronger oxidiser than chlorine and breaks the cell '
             'wall', 'bottling plants and modern municipal plants'],
            ['<b>UV irradiation</b>', 'ultraviolet light at 254 nm damages the DNA so the cell cannot '
             'multiply', 'small and medium units, pharma and food plant'],
            ['<b>Membrane filtration</b>', 'a 0.2–0.45 µm membrane or an ultrafilter physically retains '
             'the organisms', 'pharmaceutical and laboratory water'],
            ['<b>Excess lime / high pH</b>', 'pH above 11 for 2–3 hours kills most bacteria during '
             'softening', 'part of the lime–soda plant'],
        ]),
        h4('One method in detail — chlorination'),
        p('<b>Chlorination</b> is the addition of chlorine gas, bleaching powder or sodium hypochlorite '
          'to water in a dose that leaves a small free-chlorine residual after the demand of the water is '
          'satisfied. The active species is <b>hypochlorous acid, HOCl</b>, formed as '
          'Cl<sub>2</sub> + H<sub>2</sub>O → HOCl + HCl. HOCl is a small neutral molecule, so it '
          'penetrates the cell wall and oxidises the enzyme system, and the cell dies.'),
        h4('Construction — part and purpose'),
        bullets('<b>Chlorine cylinder and weighing scale</b> — stores the gas and shows how much is being '
                'used, so the dose can be calculated.',
                '<b>Chlorinator (rotameter type)</b> — dissolves the gas in a small side stream of water and '
                'meters it, so a measured dose goes into the main.',
                '<b>Mixing chamber or static mixer</b> — gives the chlorine contact with the water, so a '
                'local high concentration does not occur.',
                '<b>Contact tank (baffled, 30 minutes)</b> — provides the contact time needed for the kill.',
                '<b>Residual chlorine test kit (DPD)</b> — proves the dose was right.'),
        h4('Working — step and reason'),
        steps(('Step 1', 'The chlorine demand of the water is found by a test (about 1–3 mg/L for clear '
                         'water). Reason: the organic matter and ammonia in the water consume chlorine '
                         'first, so the dose must cover the demand plus the residual.'),
              ('Step 2', 'A dose is set at demand + 0.2–0.5 mg/L residual and the chlorinator is adjusted. '
                         'Reason: a residual proves that the water is protected until it is used, and '
                         '0.2 mg/L is enough to keep the mains safe without a taste.'),
              ('Step 3', 'The chlorinated water is held in the contact tank for about 30 minutes. Reason: '
                         'the kill follows first-order kinetics, so contact time and concentration both '
                         'count; 30 minutes at pH below 8 gives over 99.9 % kill.'),
              ('Step 4', 'The residual is tested and recorded. Reason: a falling residual at the far end of '
                         'the mains shows a re-contamination or a dosing fault.')),
        h4('Worked example — dose of bleaching powder'),
        p('A tank of 50 m<sup>3</sup> of water needs a dose of 2 mg/L of available chlorine. The bleaching '
          'powder available contains 30 % available chlorine. Find the quantity to be added.'),
        work('Given: volume = 50 m<sup>3</sup> = 50 × 1000 = 50 000 litre · dose = 2 mg/L · '
             'bleaching powder strength = 30 %',
             'Chlorine needed = dose × volume = 2 mg/L × 50 000 L',
             'Chlorine needed = 100 000 mg = 100 g',
             'Bleaching powder = ' + frac('chlorine needed', 'fraction of chlorine'),
             'Bleaching powder = ' + frac('100', '0.30') + ' g'),
        result('Bleaching powder required = 333 g'),
        p('Sanity check: 333 g of powder in 50 m<sup>3</sup> is about 6.7 g per m<sup>3</sup>, which is a '
          'normal figure for well water — reasonable.'),
        h4('Limitations'),
        bullets('Chlorine forms <b>trihalomethanes</b> with the organic matter in the water, which are '
                'carcinogenic, so the dose must be limited and the organic load removed first.',
                'Chlorine does not kill <i>Cryptosporidium</i> cysts reliably, and it fails at high pH '
                'because HOCl converts to the much weaker OCl<sup>−</sup>.',
                'Chlorine gas is poisonous, so the cylinder room needs ventilation, a gas mask and a '
                'scrubber.'),
    ),
    gu=join(
        h4('પરંપરાગત પદ્ધતિઓ'),
        table(['પદ્ધતિ', 'જીવાણુને કેવી રીતે મારે કે દૂર કરે', 'સામાન્ય ઉપયોગ'], [
            ['<b>ઉકાળવું</b>', '100 °Cની ગરમી cell protein ગંઠાવે — 5–10 મિનિટમાં બધા જીવાણુ અને cyst મરે',
             'ઘરેલું અને નાના પાયાનું પીવાનું પાણી'],
            ['<b>Chlorination</b>', 'મુક્ત chlorine (HOCl) cell wall અને enzyme ને oxidise કરે',
             'નગરપાલિકાનું પાણી, cooling water, plantનું water distribution'],
            ['<b>Bleaching powder / chloramine</b>', 'chlorine જેવું જ, પણ સસ્તું અને ધીમું',
             'ગામડાનો પુરવઠો, કૂવા, swimming pool'],
            ['<b>Ozone treatment</b>', 'ozone chlorine કરતાં વધુ મજબૂત oxidiser, cell wall તોડે',
             'bottling plant અને આધુનિક municipal plant'],
            ['<b>UV irradiation</b>', '254 nmનું ultraviolet પ્રકાશ DNA બગાડે એટલે cell વધી ન શકે',
             'નાના-મધ્યમ unit, pharma અને food plant'],
            ['<b>Membrane filtration</b>', '0.2–0.45 µm membrane કે ultrafilter જીવાણુને ભૌતિક રીતે રોકે',
             'pharmaceutical અને laboratory water'],
            ['<b>Excess lime / ઊંચો pH</b>', '2–3 કલાક pH 11થી ઉપર રાખવાથી મોટા ભાગના જીવાણુ મરે',
             'lime–soda plantનો ભાગ'],
        ]),
        h4('એક પદ્ધતિ વિગતે — chlorination'),
        p('<b>Chlorination</b> એટલે પાણીની demand પૂરી કર્યા પછી થોડું free-chlorine residual રહે એટલા doseમાં '
          'chlorine gas, bleaching powder કે sodium hypochlorite ઉમેરવું. સક્રિય પદાર્થ <b>hypochlorous acid, '
          'HOCl</b> છે, જે Cl<sub>2</sub> + H<sub>2</sub>O → HOCl + HCl પ્રમાણે બને. HOCl નાનું તટસ્થ અણુ છે, '
          'એટલે cell wallમાં ઘૂસીને enzyme system oxidise કરે અને cell મરે.'),
        h4('રચના — ભાગ અને હેતુ'),
        bullets('<b>Chlorine cylinder અને weighing scale</b> — gas રાખે અને કેટલું વપરાય છે તે દેખાડે, જેથી '
                'dose ગણી શકાય.',
                '<b>Chlorinator (rotameter પ્રકાર)</b> — gas ને થોડા પાણીના side streamમાં ઓગાળીને માપીને '
                'મુખ્ય લાઇનમાં મોકલે, એટલે માપેલો dose જાય.',
                '<b>Mixing chamber કે static mixer</b> — chlorine અને પાણીનો સંપર્ક કરાવે, જેથી એક જગ્યાએ '
                'વધુ concentration ન થાય.',
                '<b>Contact tank (baffled, 30 મિનિટ)</b> — મારવા માટે જરૂરી contact time આપે.',
                '<b>Residual chlorine test kit (DPD)</b> — dose સાચો હતો તે સાબિત કરે.'),
        h4('કાર્ય — સ્ટેપ અને કારણ'),
        steps(('Step 1', 'પાણીની chlorine demand testથી શોધાય (સાફ પાણી માટે લગભગ 1–3 mg/L). કારણ: પાણીમાંનો '
                         'organic પદાર્થ અને ammonia પહેલાં chlorine ખાય જાય, એટલે dose એ demand ઉપરાંત '
                         'residual પણ આવરે એવો જોઈએ.'),
              ('Step 2', 'Dose demand + 0.2–0.5 mg/L residual રાખીને chlorinator ગોઠવાય. કારણ: residual '
                         'હોવાથી પાણી વપરાય ત્યાં સુધી સુરક્ષિત રહે, અને 0.2 mg/L સ્વાદ બગાડ્યા વગર પૂરતું છે.'),
              ('Step 3', 'Chlorinated પાણી contact tankમાં લગભગ 30 મિનિટ રોકાય. કારણ: મારવાની ક્રિયા '
                         'first-order છે, એટલે concentration અને સમય બંને ગણાય; pH 8થી નીચે 30 મિનિટમાં '
                         '99.9 %થી વધુ મરે.'),
              ('Step 4', 'Residual માપીને નોંધાય. કારણ: મુખ્ય લાઇનના છેડે residual ઘટે તો ફરી ભેળવાયું છે કે '
                         'dosing બગડી છે તે ખબર પડે.')),
        h4('ઉકેલેલું ઉદાહરણ — bleaching powderનો dose'),
        p('50 m<sup>3</sup> પાણી માટે 2 mg/L available chlorine નો dose જોઈએ. ઉપલબ્ધ bleaching powderમાં 30 % '
          'available chlorine છે. કેટલું ઉમેરવું?'),
        work('Given: volume = 50 m<sup>3</sup> = 50 × 1000 = 50 000 લિટર · dose = 2 mg/L · bleaching '
             'powderની strength = 30 %',
             'જરૂરી chlorine = dose × volume = 2 mg/L × 50 000 L',
             'જરૂરી chlorine = 100 000 mg = 100 g',
             'Bleaching powder = ' + frac('જરૂરી chlorine', 'chlorineનો ભાગ'),
             'Bleaching powder = ' + frac('100', '0.30') + ' g'),
        result('જરૂરી bleaching powder = 333 g'),
        p('Sanity check: 50 m<sup>3</sup>માં 333 g એટલે પ્રતિ m<sup>3</sup> લગભગ 6.7 g, જે કૂવાના પાણી માટે '
          'સામાન્ય આંકડો છે — વ્યાજબી.'),
        h4('મર્યાદાઓ'),
        bullets('Chlorine પાણીમાંના organic પદાર્થ સાથે <b>trihalomethane</b> બનાવે, જે carcinogenic છે, એટલે '
                'dose મર્યાદિત રાખવો પડે અને પહેલાં organic load કાઢવો પડે.',
                'Chlorine <i>Cryptosporidium</i> cyst ને ભરોસાપાત્ર રીતે મારતું નથી, અને ઊંચા pH પર નિષ્ફળ '
                'જાય કારણ કે HOCl, ઘણા નબળા OCl<sup>−</sup>માં ફેરવાય.',
                'Chlorine gas ઝેરી છે, એટલે cylinder roomમાં ventilation, gas mask અને scrubber જરૂરી.'),
    ),
))

Q1['cards'].append(dict(
    number='Q.1 (c)', marks=7, q='Draw neat and well labeled diagram of cold lime soda process',
    en=join(
        h4('Purpose'),
        p('The <b>cold lime–soda process</b> removes both carbonate and non-carbonate hardness from water '
          'at ordinary temperature (20–30 °C) by precipitating calcium and magnesium as insoluble '
          'compounds. Lime Ca(OH)<sub>2</sub> removes the bicarbonate hardness and the magnesium, and soda '
          'ash Na<sub>2</sub>CO<sub>3</sub> removes the sulphate and chloride hardness.'),
        h4('Reactions'),
        p('Ca(HCO<sub>3</sub>)<sub>2</sub> + Ca(OH)<sub>2</sub> → 2CaCO<sub>3</sub>↓ + 2H<sub>2</sub>O'),
        p('Mg(HCO<sub>3</sub>)<sub>2</sub> + 2Ca(OH)<sub>2</sub> → Mg(OH)<sub>2</sub>↓ + '
          '2CaCO<sub>3</sub>↓ + 2H<sub>2</sub>O'),
        p('CaSO<sub>4</sub> + Na<sub>2</sub>CO<sub>3</sub> → CaCO<sub>3</sub>↓ + Na<sub>2</sub>SO<sub>4</sub>'),
        h4('Neat labelled diagram'),
        figure(fig.lime_soda(cold=True),
               'Fig. 1.1 · Cold lime–soda softener — raw water inlet, chemical mixer with slow stirrer, '
               'flocculation and settling tank, sludge blow-down, pressure sand filter and soft-water '
               'outlet.'),
        h4('Construction — part and purpose'),
        table(['Part', 'Purpose'], [
            ['Raw water inlet and flow meter', 'measures the quantity so the lime and soda dose can be '
             'fixed in proportion'],
            ['Lime and soda feed (dry feeder or slurry tank)', 'adds the chemicals in a measured dose'],
            ['Chemical mixer with slow stirrer', 'mixes the chemicals with the water so the reaction '
             'starts and the pH rises'],
            ['Flocculation and settling tank', 'gives time for CaCO<sub>3</sub> and Mg(OH)<sub>2</sub> to '
             'grow into flocs and settle as sludge'],
            ['Sludge blow-down line and sludge sump', 'draws off the sludge from the conical bottom at '
             'intervals'],
            ['Pressure sand filter', 'retains the fine floc that did not settle'],
            ['Soft-water storage tank', 'holds the treated water for boiler or process use'],
        ]),
        h4('Working — step and reason'),
        steps(('Step 1', 'Raw water enters the chemical mixer, where the lime and soda doses are added. '
                         'Reason: the dose is calculated from the analysed hardness, so the correct '
                         'quantity of each chemical is added.'),
              ('Step 2', 'The mixture passes into the settling chamber and the stirrer speed is reduced. '
                         'Reason: slow stirring lets the tiny particles collide and grow into flocs that '
                         'settle; fast stirring would break them up.'),
              ('Step 3', 'The precipitate settles and the sludge is blown down from the bottom. Reason: the '
                         'sludge occupies volume and would otherwise be carried over with the water.'),
              ('Step 4', 'The clear overflow goes to the pressure sand filter. Reason: fine floc that did '
                         'not settle in the tank is trapped here, and the filter also removes turbidity.'),
              ('Step 5', 'Filtered water is stored, with residual hardness of about 30–50 ppm. Reason: '
                         'the cold process is limited by the solubility of CaCO<sub>3</sub>, so zero '
                         'hardness is not possible at this temperature.')),
        h4('Worked example — lime and soda requirement'),
        p('Water contains Ca(HCO<sub>3</sub>)<sub>2</sub> = 81 mg/L and CaSO<sub>4</sub> = 68 mg/L. Find the '
          'lime and soda needed per 1000 litre, taking the molecular masses as Ca(OH)<sub>2</sub> = 74, '
          'Ca(HCO<sub>3</sub>)<sub>2</sub> = 162, CaSO<sub>4</sub> = 136 and Na<sub>2</sub>CO<sub>3</sub> = '
          '106.'),
        work('Given: Ca(HCO<sub>3</sub>)<sub>2</sub> = 81 mg/L · CaSO<sub>4</sub> = 68 mg/L · '
             'volume = 1000 L',
             'Lime: Ca(HCO<sub>3</sub>)<sub>2</sub> + Ca(OH)<sub>2</sub> → 2CaCO<sub>3</sub> + 2H<sub>2</sub>O',
             'Lime for bicarbonate = ' + frac('81 × 74', '162') + ' = 37 mg/L',
             'Soda: CaSO<sub>4</sub> + Na<sub>2</sub>CO<sub>3</sub> → CaCO<sub>3</sub> + '
             'Na<sub>2</sub>SO<sub>4</sub>',
             'Soda for sulphate = ' + frac('68 × 106', '136') + ' = 53 mg/L',
             'For 1000 L: lime = 37 g, soda = 53 g'),
        result('Lime Ca(OH)<sub>2</sub> = 37 g and soda Na<sub>2</sub>CO<sub>3</sub> = 53 g per 1000 litre'),
        p('Sanity check: 37 mg/L of lime is about 1 mmol/L, which matches 81 mg/L of calcium bicarbonate '
          '(0.5 mmol/L) one for one — correct.'),
        h4('Limitations'),
        bullets('Zero hardness cannot be reached; 30–50 ppm remains, so the water is still not good enough '
                'for a high-pressure boiler without further treatment.',
                'Sludge is bulky and holds a lot of water, so disposal is the main running cost.',
                'Excess lime raises the pH and can itself cause scale and foaming in the boiler, so the '
                'dose has to be tested and adjusted every shift.'),
    ),
    gu=join(
        h4('હેતુ'),
        p('<b>Cold lime–soda process</b> સામાન્ય તાપમાને (20–30 °C) carbonate અને non-carbonate બંને hardnessને '
          'અદ્રાવ્ય સંયોજન તરીકે અલગ કરીને પાણીમાંથી કાઢે. ચૂનો Ca(OH)<sub>2</sub> bicarbonate hardness અને '
          'magnesium કાઢે, અને soda ash Na<sub>2</sub>CO<sub>3</sub> sulphate તથા chloride hardness કાઢે.'),
        h4('પ્રક્રિયાઓ'),
        p('Ca(HCO<sub>3</sub>)<sub>2</sub> + Ca(OH)<sub>2</sub> → 2CaCO<sub>3</sub>↓ + 2H<sub>2</sub>O'),
        p('Mg(HCO<sub>3</sub>)<sub>2</sub> + 2Ca(OH)<sub>2</sub> → Mg(OH)<sub>2</sub>↓ + '
          '2CaCO<sub>3</sub>↓ + 2H<sub>2</sub>O'),
        p('CaSO<sub>4</sub> + Na<sub>2</sub>CO<sub>3</sub> → CaCO<sub>3</sub>↓ + Na<sub>2</sub>SO<sub>4</sub>'),
        h4('સ્વચ્છ લેબલવાળી આકૃતિ'),
        figure(fig.lime_soda(cold=True),
               'Fig. 1.1 · Cold lime–soda softener — raw water inlet, slow stirrer વાળું chemical mixer, '
               'flocculation અને settling tank, sludge blow-down, pressure sand filter અને soft-water '
               'outlet.'),
        h4('રચના — ભાગ અને હેતુ'),
        table(['ભાગ', 'હેતુ'], [
            ['Raw water inlet અને flow meter', 'જથ્થો માપે જેથી lime અને sodaનો dose પ્રમાણમાં ઠરાવી શકાય'],
            ['Lime અને soda feed (dry feeder કે slurry tank)', 'માપેલો dose ઉમેરે'],
            ['Slow stirrer વાળું chemical mixer', 'રસાયણોને પાણી સાથે ભેળવે જેથી પ્રક્રિયા શરૂ થાય અને pH વધે'],
            ['Flocculation અને settling tank', 'CaCO<sub>3</sub> અને Mg(OH)<sub>2</sub>ને floc સુધી વધવા અને '
             'sludge તરીકે બેસવા સમય આપે'],
            ['Sludge blow-down લાઇન અને sludge sump', 'conical તળિયેથી સમયે સમયે sludge કાઢે'],
            ['Pressure sand filter', 'ન બેઠેલો બારીક floc રોકે'],
            ['Soft-water storage tank', 'boiler કે process માટે તૈયાર પાણી રાખે'],
        ]),
        h4('કાર્ય — સ્ટેપ અને કારણ'),
        steps(('Step 1', 'Raw water chemical mixerમાં આવે અને lime તથા sodaનો dose ઉમેરાય. કારણ: dose વિશ્લેષિત '
                         'hardness પરથી ગણાય, એટલે દરેક રસાયણનો સાચો જથ્થો જાય.'),
              ('Step 2', 'મિશ્રણ settling chamberમાં જાય અને stirrerની ઝડપ ઘટાડાય. કારણ: ધીમા stirringથી '
                         'નાના કણ ભેગા થઈને floc બને અને બેસે; ઝડપી stirring એમને તોડી નાખે.'),
              ('Step 3', 'Precipitate બેસે અને તળિયેથી sludge blow-down થાય. કારણ: sludge જગ્યા રોકે અને '
                         'ન કાઢીએ તો પાણી સાથે બહાર જાય.'),
              ('Step 4', 'ઉપરનું સાફ પાણી pressure sand filterમાં જાય. કારણ: tankમાં ન બેઠેલો બારીક floc '
                         'અહીં ફસાય, અને turbidity પણ કાઢે.'),
              ('Step 5', 'Filter કરેલું પાણી સંગ્રહાય, residual hardness લગભગ 30–50 ppm રહે. કારણ: આ '
                         'તાપમાને CaCO<sub>3</sub>ની solubility મર્યાદા હોવાથી cold processમાં શૂન્ય hardness '
                         'શક્ય નથી.')),
        h4('ઉકેલેલું ઉદાહરણ — lime અને sodaની જરૂરિયાત'),
        p('પાણીમાં Ca(HCO<sub>3</sub>)<sub>2</sub> = 81 mg/L અને CaSO<sub>4</sub> = 68 mg/L છે. 1000 લિટર માટે '
          'જરૂરી lime અને soda શોધો; Ca(OH)<sub>2</sub> = 74, Ca(HCO<sub>3</sub>)<sub>2</sub> = 162, '
          'CaSO<sub>4</sub> = 136 અને Na<sub>2</sub>CO<sub>3</sub> = 106 લો.'),
        work('Given: Ca(HCO<sub>3</sub>)<sub>2</sub> = 81 mg/L · CaSO<sub>4</sub> = 68 mg/L · '
             'volume = 1000 L',
             'Lime: Ca(HCO<sub>3</sub>)<sub>2</sub> + Ca(OH)<sub>2</sub> → 2CaCO<sub>3</sub> + 2H<sub>2</sub>O',
             'Bicarbonate માટે lime = ' + frac('81 × 74', '162') + ' = 37 mg/L',
             'Soda: CaSO<sub>4</sub> + Na<sub>2</sub>CO<sub>3</sub> → CaCO<sub>3</sub> + '
             'Na<sub>2</sub>SO<sub>4</sub>',
             'Sulphate માટે soda = ' + frac('68 × 106', '136') + ' = 53 mg/L',
             '1000 L માટે: lime = 37 g, soda = 53 g'),
        result('1000 લિટર દીઠ lime Ca(OH)<sub>2</sub> = 37 g અને soda Na<sub>2</sub>CO<sub>3</sub> = 53 g'),
        p('Sanity check: 37 mg/L lime એટલે લગભગ 1 mmol/L, જે 81 mg/L calcium bicarbonate (0.5 mmol/L) સાથે '
          'એક એક પ્રમાણે મળે — સાચું.'),
        h4('મર્યાદાઓ'),
        bullets('શૂન્ય hardness મળે નહીં; 30–50 ppm રહી જાય, એટલે ઊંચા pressureના boiler માટે એ પાણી વધુ '
                'treatment વગર ચાલે નહીં.',
                'Sludge જથ્થાબંધ અને ઘણું પાણી રાખે, એટલે નિકાલ મુખ્ય ખર્ચ બને.',
                'વધુ lime pH વધારે અને પોતે જ boilerમાં scale તથા foaming કરે, એટલે dose દર shiftે ચકાસીને '
                'ગોઠવવો પડે.'),
    ),
))

Q1['cards'].append(dict(
    number='Q.1 (c)', marks=7, tag='OR', q='Draw neat and well labeled diagram of Hot lime soda Process.',
    en=join(
        h4('Purpose'),
        p('The <b>hot lime–soda process</b> works on the same chemistry as the cold process, but at '
          '90–110 °C. Because the reactions are faster and the solubility of CaCO<sub>3</sub> and '
          'Mg(OH)<sub>2</sub> falls at higher temperature, the residual hardness is lower (about 15–25 ppm), '
          'the sludge is denser, and the same output needs a smaller plant.'),
        h4('Reactions'),
        p('Ca(HCO<sub>3</sub>)<sub>2</sub> + Ca(OH)<sub>2</sub> → 2CaCO<sub>3</sub>↓ + 2H<sub>2</sub>O'),
        p('MgSO<sub>4</sub> + Ca(OH)<sub>2</sub> → Mg(OH)<sub>2</sub>↓ + CaSO<sub>4</sub>, and the '
          'CaSO<sub>4</sub> so formed is removed by Na<sub>2</sub>CO<sub>3</sub>: '
          'CaSO<sub>4</sub> + Na<sub>2</sub>CO<sub>3</sub> → CaCO<sub>3</sub>↓ + '
          'Na<sub>2</sub>SO<sub>4</sub>'),
        h4('Neat labelled diagram'),
        figure(fig.lime_soda(cold=False),
               'Fig. 1.2 · Hot lime–soda softener — chemical mixer, heater (90–110 °C), settling tank with '
               'sludge blow-down and sand filter.'),
        h4('Construction — part and purpose'),
        table(['Part', 'Purpose'], [
            ['Chemical mixer with slow stirrer', 'mixes raw water with lime and soda slurry so the reaction '
             'starts'],
            ['Steam heater / deaerating heater', 'raises the temperature to 90–110 °C, which speeds up the '
             'reaction and removes dissolved gases'],
            ['Reaction and settling tank', 'gives the floc time to grow and settle; the hot dense sludge '
             'settles faster than cold sludge'],
            ['Sludge blow-down and sludge sump', 'removes the CaCO<sub>3</sub> and Mg(OH)<sub>2</sub> '
             'sludge'],
            ['Pressure sand filter', 'retains the fine floc carried over from the settling tank'],
            ['Soft-water storage / boiler feed tank', 'holds water at 15–25 ppm hardness for the boiler'],
        ]),
        h4('Working — step and reason'),
        steps(('Step 1', 'Raw water is mixed with the lime and soda dose in the mixer. Reason: the dose is '
                         'calculated from the hardness analysis, so the correct quantity of each chemical '
                         'is added.'),
              ('Step 2', 'The mixture is heated with steam to 90–110 °C. Reason: at higher temperature the '
                         'reaction rate rises and the solubility of CaCO<sub>3</sub> falls, so more '
                         'hardness comes out of solution.'),
              ('Step 3', 'The hot mixture enters the settling tank where the flocs grow and settle quickly. '
                         'Reason: hot water has a lower viscosity, so particles settle faster and the tank '
                         'can be smaller.'),
              ('Step 4', 'Sludge is blown down and the clear water is filtered. Reason: the dense hot sludge '
                         'is easy to filter, so less water is lost with it.'),
              ('Step 5', 'The softened water goes to the boiler feed tank at 15–25 ppm hardness. Reason: '
                         'this water is good enough for a medium-pressure boiler, and it is already hot, '
                         'which saves fuel in the boiler.')),
        h4('Cold and hot process compared'),
        table(['Point', 'Cold lime–soda', 'Hot lime–soda'], [
            ['Temperature', '20–30 °C', '90–110 °C'],
            ['Reaction speed', 'slow, big tank needed', 'fast, smaller tank is enough'],
            ['Residual hardness', 'about 30–50 ppm', 'about 15–25 ppm'],
            ['Sludge', 'bulky, holds more water', 'dense, easy to filter'],
            ['Dissolved gases', 'remain in the water', 'mostly removed by heating'],
            ['Use', 'general plant and process water', 'boiler feed water'],
        ]),
        h4('Worked example — steam needed to heat the water'),
        p('A hot lime–soda plant treats 10 000 kg/h of water from 25 °C to 95 °C. Find the steam needed at '
          '2 bar, where h<sub>fg</sub> = 2202 kJ/kg. Take c<sub>p</sub> of water = 4.18 kJ/kg·K and allow '
          '5 % heat loss.'),
        work('Given: m = 10 000 kg/h · ΔT = 95 − 25 = 70 K · c<sub>p</sub> = 4.18 kJ/kg·K · '
             'h<sub>fg</sub> = 2202 kJ/kg · loss = 5 %',
             'Formula: Q = m · c<sub>p</sub> · ΔT',
             'Substitute: Q = 10 000 × 4.18 × 70 = 2 926 000 kJ/h',
             'With 5 % loss: Q = 2 926 000 × 1.05 = 3 072 300 kJ/h',
             'Steam = ' + frac('Q', 'h<sub>fg</sub>') + ' = ' + frac('3 072 300', '2202') + ' kg/h'),
        result('Steam required ≈ 1395 kg/h ≈ 1.4 t/h'),
        p('Sanity check: heating 10 t/h of water by 70 K is a large duty, and 1.4 t/h of steam is about the '
          'right order — the steam mass is roughly one-seventh of the water mass.'),
        h4('Limitations'),
        bullets('Heating costs money, so the process is economical only where the softened water is boiler '
                'feed and would have to be heated anyway.',
                'A hot plant needs insulated vessels and more careful operation, so the capital cost is '
                'higher than the cold process.',
                'The residual hardness is still not zero, so phosphate or ion-exchange polishing is needed '
                'for a high-pressure boiler.'),
    ),
    gu=join(
        h4('હેતુ'),
        p('<b>Hot lime–soda process</b> cold process જેવી જ રસાયણશાસ્ત્ર પર કામ કરે, પણ 90–110 °C પર. ઊંચા '
          'તાપમાને પ્રક્રિયા ઝડપી થાય અને CaCO<sub>3</sub> તથા Mg(OH)<sub>2</sub>ની solubility ઘટે, એટલે '
          'residual hardness ઓછી રહે (લગભગ 15–25 ppm), sludge ગાઢ બને, અને એટલા જ ઉત્પાદન માટે નાનું plant '
          'પૂરતું થાય.'),
        h4('પ્રક્રિયાઓ'),
        p('Ca(HCO<sub>3</sub>)<sub>2</sub> + Ca(OH)<sub>2</sub> → 2CaCO<sub>3</sub>↓ + 2H<sub>2</sub>O'),
        p('MgSO<sub>4</sub> + Ca(OH)<sub>2</sub> → Mg(OH)<sub>2</sub>↓ + CaSO<sub>4</sub>, અને એમ બનેલું '
          'CaSO<sub>4</sub> Na<sub>2</sub>CO<sub>3</sub>થી કાઢાય: CaSO<sub>4</sub> + '
          'Na<sub>2</sub>CO<sub>3</sub> → CaCO<sub>3</sub>↓ + Na<sub>2</sub>SO<sub>4</sub>'),
        h4('સ્વચ્છ લેબલવાળી આકૃતિ'),
        figure(fig.lime_soda(cold=False),
               'Fig. 1.2 · Hot lime–soda softener — chemical mixer, heater (90–110 °C), sludge blow-down '
               'વાળું settling tank અને sand filter.'),
        h4('રચના — ભાગ અને હેતુ'),
        table(['ભાગ', 'હેતુ'], [
            ['Slow stirrer વાળું chemical mixer', 'raw waterને lime અને sodaની slurry સાથે ભેળવે જેથી પ્રક્રિયા '
             'શરૂ થાય'],
            ['Steam heater / deaerating heater', 'તાપમાન 90–110 °C સુધી લાવે, જેથી પ્રક્રિયા ઝડપી થાય અને '
             'ઓગળેલા gas નીકળે'],
            ['Reaction અને settling tank', 'flocને વધવા અને બેસવા સમય આપે; ગરમ ગાઢ sludge ઠંડા કરતાં ઝડપથી '
             'બેસે'],
            ['Sludge blow-down અને sludge sump', 'CaCO<sub>3</sub> અને Mg(OH)<sub>2</sub>નો sludge કાઢે'],
            ['Pressure sand filter', 'settling tankમાંથી ગયેલો બારીક floc રોકે'],
            ['Soft-water storage / boiler feed tank', '15–25 ppm hardness વાળું પાણી boiler માટે રાખે'],
        ]),
        h4('કાર્ય — સ્ટેપ અને કારણ'),
        steps(('Step 1', 'Raw waterને mixerમાં lime અને sodaના dose સાથે ભેળવાય. કારણ: dose hardnessના '
                         'વિશ્લેષણ પરથી ગણાય, એટલે દરેક રસાયણનો સાચો જથ્થો જાય.'),
              ('Step 2', 'મિશ્રણને steamથી 90–110 °C સુધી ગરમ કરાય. કારણ: ઊંચા તાપમાને પ્રક્રિયાની ઝડપ વધે '
                         'અને CaCO<sub>3</sub>ની solubility ઘટે, એટલે વધુ hardness દ્રાવણમાંથી બહાર આવે.'),
              ('Step 3', 'ગરમ મિશ્રણ settling tankમાં જાય જ્યાં floc ઝડપથી વધે અને બેસે. કારણ: ગરમ પાણીની '
                         'viscosity નીચી હોવાથી કણ ઝડપથી બેસે અને tank નાનું પૂરતું થાય.'),
              ('Step 4', 'Sludge blow-down થાય અને સાફ પાણી filter થાય. કારણ: ગાઢ ગરમ sludge સહેલાઈથી filter '
                         'થાય, એટલે એની સાથે ઓછું પાણી જાય.'),
              ('Step 5', 'Softened પાણી 15–25 ppm hardness પર boiler feed tankમાં જાય. કારણ: આ પાણી મધ્યમ '
                         'pressureના boiler માટે પૂરતું છે, અને એ પહેલેથી ગરમ હોવાથી boilerમાં fuel બચે.')),
        h4('Cold અને hot processની સરખામણી'),
        table(['મુદ્દો', 'Cold lime–soda', 'Hot lime–soda'], [
            ['તાપમાન', '20–30 °C', '90–110 °C'],
            ['પ્રક્રિયાની ઝડપ', 'ધીમી, મોટું tank જોઈએ', 'ઝડપી, નાનું tank પૂરતું'],
            ['Residual hardness', 'લગભગ 30–50 ppm', 'લગભગ 15–25 ppm'],
            ['Sludge', 'જથ્થાબંધ, વધુ પાણી રાખે', 'ગાઢ, filter કરવું સહેલું'],
            ['ઓગળેલા gas', 'પાણીમાં રહી જાય', 'ગરમ કરવાથી મોટા ભાગે નીકળી જાય'],
            ['ઉપયોગ', 'સામાન્ય plant અને process water', 'boiler feed water'],
        ]),
        h4('ઉકેલેલું ઉદાહરણ — પાણી ગરમ કરવા જરૂરી steam'),
        p('Hot lime–soda plant કલાકે 10 000 kg પાણી 25 °Cથી 95 °C સુધી ગરમ કરે છે. 2 bar પર '
          'h<sub>fg</sub> = 2202 kJ/kg લઈને જરૂરી steam શોધો; પાણીનું c<sub>p</sub> = 4.18 kJ/kg·K અને 5 % '
          'heat loss ધરો.'),
        work('Given: m = 10 000 kg/h · ΔT = 95 − 25 = 70 K · c<sub>p</sub> = 4.18 kJ/kg·K · '
             'h<sub>fg</sub> = 2202 kJ/kg · loss = 5 %',
             'Formula: Q = m · c<sub>p</sub> · ΔT',
             'Substitution: Q = 10 000 × 4.18 × 70 = 2 926 000 kJ/h',
             '5 % loss સાથે: Q = 2 926 000 × 1.05 = 3 072 300 kJ/h',
             'Steam = ' + frac('Q', 'h<sub>fg</sub>') + ' = ' + frac('3 072 300', '2202') + ' kg/h'),
        result('જરૂરી steam ≈ 1395 kg/h ≈ 1.4 t/h'),
        p('Sanity check: 10 t/h પાણીને 70 K ગરમ કરવું એ મોટું કામ છે, અને 1.4 t/h steam એ સાચો ક્રમ છે — '
          'steamનું દળ પાણીના દળના લગભગ સાતમા ભાગ જેટલું આવે.'),
        h4('મર્યાદાઓ'),
        bullets('ગરમ કરવાનો ખર્ચ થાય, એટલે જ્યાં softened પાણી boiler feed છે અને કોઈ પણ રીતે ગરમ કરવું પડે '
                'ત્યાં જ આ process આર્થિક છે.',
                'ગરમ plantમાં insulated vessel અને વધુ કાળજી વાળી operation જોઈએ, એટલે capital cost cold '
                'process કરતાં વધે.',
                'Residual hardness હજી શૂન્ય નથી, એટલે ઊંચા pressureના boiler માટે phosphate કે '
                'ion-exchange polishing જરૂરી.'),
    ),
))


# ---------------------------------------------------------------- Q2
Q2 = {
    'title_en': 'Q2 · Sources of water, ozone/UV disinfection, zeolite and ion exchange',
    'title_gu': 'પ્ર.2 · પાણીના સ્રોત, ozone/UV જંતુમુક્તીકરણ, ઝિઓલાઇટ અને આયન વિનિમય',
    'cards': [],
}

Q2['cards'].append(dict(
    number='Q.2 (a)', marks=3, q='List sources of water with suitable examples',
    en=join(
        p('Water for a chemical plant comes from four natural sources. Each one has a different quality, '
          'and therefore a different treatment cost.'),
        table(['Source', 'Examples', 'Quality and treatment needed'], [
            ['<b>Surface water</b>', 'river (Narmada, Tapi), lake, canal, reservoir',
             'turbid, coloured, high organic matter and bacteria; needs coagulation, settling, filtration '
             'and disinfection'],
            ['<b>Ground water</b>', 'dug well, bore well, tube well, spring',
             'clear and free of bacteria, but hard (dissolved Ca and Mg); needs softening, sometimes iron '
             'removal'],
            ['<b>Rain water</b>', 'roof catchment, rainwater harvesting tank',
             'very soft and low in dissolved solids, but seasonal and slightly acidic; needs only '
             'filtration and disinfection'],
            ['<b>Sea water</b>', 'Arabian Sea, Gulf of Khambhat',
             'very high total dissolved solids, about 35 000 ppm; needs desalination (RO or multi-stage '
             'flash) before use, only for cooling or after treatment'],
        ]),
        figure(ufig.water_sources(),
               'Fig. 2.1 · Surface, ground, rain and sea water with their typical quality.'),
        p('<b>Example:</b> a plant at Ankleshwar takes clarified river water for cooling (surface source), '
          'bore-well water for the boiler (after softening, because it is hard), and harvested rain water '
          'for the laboratory, where very low dissolved solids matter.'),
    ),
    gu=join(
        p('Chemical plant માટે પાણી ચાર કુદરતી સ્રોતમાંથી આવે. દરેકની ગુણવત્તા જુદી, એટલે treatmentનો ખર્ચ પણ '
          'જુદો.'),
        table(['સ્રોત', 'ઉદાહરણ', 'ગુણવત્તા અને જરૂરી treatment'], [
            ['<b>Surface water</b>', 'નદી (નર્મદા, તાપી), સરોવર, કેનાલ, જળાશય',
             'turbid, રંગીન, વધુ organic પદાર્થ અને જીવાણુ; coagulation, settling, filtration અને '
             'disinfection જોઈએ'],
            ['<b>Ground water</b>', 'કૂવો, bore well, tube well, ઝરણું',
             'સાફ અને જીવાણુમુક્ત, પણ hard (ઓગળેલા Ca અને Mg); softening જોઈએ, ક્યાંક iron removal પણ'],
            ['<b>Rain water</b>', 'છતનું catchment, rain water harvesting tank',
             'ખૂબ soft અને ઓછા dissolved solids, પણ મોસમી અને થોડું acidic; ફક્ત filtration અને '
             'disinfection પૂરતું'],
            ['<b>Sea water</b>', 'અરબી સમુદ્ર, ખંભાતનો અખાત',
             'ખૂબ ઊંચા total dissolved solids, લગભગ 35 000 ppm; વાપરતાં પહેલાં desalination (RO કે '
             'multi-stage flash) જોઈએ, પછી cooling કે ઉપયોગ'],
        ]),
        figure(ufig.water_sources(),
               'Fig. 2.1 · Surface, ground, rain અને sea water અને એમની સામાન્ય ગુણવત્તા.'),
        p('<b>ઉદાહરણ:</b> અંકલેશ્વરનું plant cooling માટે સાફ કરેલું નદીનું પાણી લે (surface source), '
          'boiler માટે bore-well પાણી (softening પછી, કારણ કે એ hard છે), અને laboratory માટે વરસાદનું પાણી, '
          'જ્યાં ખૂબ ઓછા dissolved solids જરૂરી છે.'),
    ),
))

Q2['cards'].append(dict(
    number='Q.2 (b)', marks=4, q='Explain Sterilization of water using ozone',
    en=join(
        h4('Definition'),
        p('<b>Ozone sterilisation</b> is the disinfection of water by bubbling <b>ozone, O<sub>3</sub></b> '
          'through it. Ozone is an unstable allotrope of oxygen with a very high oxidation potential '
          '(2.07 V, higher than chlorine at 1.36 V), so it attacks the cell wall and the cell membrane of '
          'bacteria, viruses and cysts and destroys them within seconds.'),
        h4('Construction of the plant — part and purpose'),
        table(['Part', 'Purpose'], [
            ['Air dryer and filter', 'removes moisture and dust, because damp air gives less ozone and '
             'attacks the electrodes'],
            ['Ozone generator (silent discharge)', 'a high-voltage AC discharge across a dielectric gap '
             'converts O<sub>2</sub> into O<sub>3</sub>'],
            ['Injector / venturi or diffuser', 'mixes the ozone gas into the water as fine bubbles, '
             'because gas-liquid contact decides the transfer'],
            ['Contact column (2–4 m of water)', 'gives 5–15 minutes of contact for the kill and for the '
             'oxidation of iron, manganese and taste compounds'],
            ['Off-gas destructor', 'destroys the ozone that leaves the column, because ozone is toxic '
             'in the working area'],
            ['Residual ozone monitor', 'proves that enough ozone was dosed and that the excess has '
             'decayed before the water is used'],
        ]),
        figure(ufig.ozone_sterilizer(),
               'Fig. 2.2 · Ozone plant — generator, contact column and sterile water outlet.'),
        h4('Working — step and reason'),
        steps(('Step 1', 'Air or oxygen is dried and filtered. Reason: moisture in the feed reduces the '
                         'ozone yield and corrodes the electrodes.'),
              ('Step 2', 'The dry air passes through the silent-discharge generator, where a high-voltage '
                         'discharge splits O<sub>2</sub> into oxygen atoms which recombine as O<sub>3</sub>. '
                         'Reason: only a high-energy discharge can break the strong O=O bond.'),
              ('Step 3', 'The ozone-air mixture is drawn into the water by a venturi injector. Reason: the '
                         'transfer of ozone into water is fast only when the gas is broken into small '
                         'bubbles with a large surface area.'),
              ('Step 4', 'The water passes up a contact column for 5–15 minutes. Reason: the kill and the '
                         'oxidation of iron and organics need contact time; the column also gives the '
                         'pressure needed to dissolve the ozone.'),
              ('Step 5', 'The treated water leaves, and the surplus ozone is destroyed in the off-gas '
                         'destructor. Reason: ozone irritates the lungs, so it must not escape into the '
                         'plant.')),
        h4('Worked example — ozone dose'),
        p('A bottling plant treats 20 m<sup>3</sup>/h of water at an ozone dose of 1.5 g/m<sup>3</sup>. The '
          'generator produces 100 g/h of ozone from air. Check whether one generator is enough, and give '
          'the residual if the demand of the water is 1.1 g/m<sup>3</sup>.'),
        work('Given: flow = 20 m<sup>3</sup>/h · dose applied = 1.5 g/m<sup>3</sup> · generator capacity = '
             '100 g/h · demand = 1.1 g/m<sup>3</sup>',
             'Ozone needed = flow × dose = 20 × 1.5 = 30 g/h',
             'Generator capacity 100 g/h &gt; 30 g/h, so one generator is enough',
             'Residual = dose − demand = 1.5 − 1.1 = 0.4 g/m<sup>3</sup>'),
        result('One 100 g/h generator is sufficient; residual ozone ≈ 0.4 g/m<sup>3</sup>'),
        p('Sanity check: 0.4 g/m<sup>3</sup> = 0.4 mg/L residual, which is the usual design figure for '
          'ozone (0.2–0.5 mg/L) — correct.'),
        h4('Advantages and limitations'),
        bullets('Ozone is the strongest of the common disinfectants, it kills cysts that chlorine cannot, '
                'and it leaves <b>no residue and no chlorinated by-product</b>, because it decomposes back '
                'to oxygen.',
                'It also removes colour, taste, odour, iron and manganese, so one step does several jobs.',
                'But it gives no protection after treatment, so the water must be used at once; and the '
                'plant is costly because ozone has to be generated on site — it cannot be stored.',
                'Ozone is toxic and corrosive, so the generator room needs ventilation and the off-gas '
                'must be destroyed.'),
    ),
    gu=join(
        h4('વ્યાખ્યા'),
        p('<b>Ozone sterilisation</b> એટલે પાણીમાં <b>ozone, O<sub>3</sub></b> છોડીને જંતુમુક્ત કરવું. Ozone એ '
          'oxygenનું અસ્થિર allotrope છે અને એનો oxidation potential ખૂબ ઊંચો છે (2.07 V, chlorineના 1.36 V '
          'કરતાં વધુ), એટલે એ જીવાણુ, વિષાણુ અને cystની cell wall તથા membrane પર હુમલો કરીને સેકન્ડોમાં '
          'નષ્ટ કરે.'),
        h4('Plantની રચના — ભાગ અને હેતુ'),
        table(['ભાગ', 'હેતુ'], [
            ['Air dryer અને filter', 'ભેજ અને ધૂળ કાઢે, કારણ કે ભીની હવાથી ઓછું ozone મળે અને electrode પર '
             'હુમલો થાય'],
            ['Ozone generator (silent discharge)', 'dielectric gap પર ઊંચા વોલ્ટેજનો AC discharge '
             'O<sub>2</sub>ને O<sub>3</sub>માં ફેરવે'],
            ['Injector / venturi કે diffuser', 'ozone gasને બારીક પરપોટા તરીકે પાણીમાં ભેળવે, કારણ કે '
             'gas-liquid contact transfer નક્કી કરે'],
            ['Contact column (2–4 m પાણી)', 'મારવા અને iron, manganese તથા સ્વાદના પદાર્થ oxidise કરવા '
             '5–15 મિનિટ contact આપે'],
            ['Off-gas destructor', 'columnમાંથી નીકળતું ozone નષ્ટ કરે, કારણ કે ozone કામની જગ્યામાં ઝેરી છે'],
            ['Residual ozone monitor', 'પૂરતું ozone મળ્યું અને વધારાનું વપરાય ત્યાં સુધી ક્ષીણ થઈ ગયું તે '
             'સાબિત કરે'],
        ]),
        figure(ufig.ozone_sterilizer(),
               'Fig. 2.2 · Ozone plant — generator, contact column અને sterile water outlet.'),
        h4('કાર્ય — સ્ટેપ અને કારણ'),
        steps(('Step 1', 'હવા કે oxygen સૂકવાય અને filter થાય. કારણ: feedમાં ભેજ હોય તો ozone yield ઘટે અને '
                         'electrode ખવાય.'),
              ('Step 2', 'સૂકી હવા silent-discharge generatorમાંથી પસાર થાય, જ્યાં ઊંચા વોલ્ટેજના dischargeથી '
                         'O<sub>2</sub> તૂટીને oxygen atom બને અને એ ફરી જોડાઈને O<sub>3</sub> બને. કારણ: મજબૂત '
                         'O=O bond તોડવા માટે ઊંચી energyનો discharge જ પૂરતો.'),
              ('Step 3', 'Ozone-હવાનું મિશ્રણ venturi injector પાણીમાં ખેંચે. કારણ: gas ને નાના પરપોટામાં '
                         'તોડતાં જ surface area વધે અને ozone પાણીમાં ઝડપથી transfer થાય.'),
              ('Step 4', 'પાણી contact columnમાં 5–15 મિનિટ ઉપર જાય. કારણ: મારવા અને iron તથા organic '
                         'oxidise કરવા contact time જોઈએ; column ozone ઓગાળવા જરૂરી pressure પણ આપે.'),
              ('Step 5', 'Treated પાણી બહાર જાય અને વધારાનું ozone off-gas destructorમાં નષ્ટ થાય. કારણ: ozone '
                         'ફેફસાંને બળતરા કરે, એટલે એ plantમાં ફેલાવું ન જોઈએ.')),
        h4('ઉકેલેલું ઉદાહરણ — ozoneનો dose'),
        p('Bottling plant કલાકે 20 m<sup>3</sup> પાણી 1.5 g/m<sup>3</sup> ozone dose પર treat કરે છે. Generator '
          'હવામાંથી 100 g/h ozone આપે છે. એક generator પૂરતો છે કે નહીં તે ચકાસો, અને પાણીની demand '
          '1.1 g/m<sup>3</sup> હોય તો residual આપો.'),
        work('Given: flow = 20 m<sup>3</sup>/h · dose = 1.5 g/m<sup>3</sup> · generator capacity = 100 g/h · '
             'demand = 1.1 g/m<sup>3</sup>',
             'જરૂરી ozone = flow × dose = 20 × 1.5 = 30 g/h',
             'Generator capacity 100 g/h &gt; 30 g/h, એટલે એક generator પૂરતો',
             'Residual = dose − demand = 1.5 − 1.1 = 0.4 g/m<sup>3</sup>'),
        result('એક 100 g/h generator પૂરતો; residual ozone ≈ 0.4 g/m<sup>3</sup>'),
        p('Sanity check: 0.4 g/m<sup>3</sup> = 0.4 mg/L residual, જે ozone માટે સામાન્ય design આંકડો છે '
          '(0.2–0.5 mg/L) — સાચું.'),
        h4('ફાયદા અને મર્યાદાઓ'),
        bullets('Ozone સામાન્ય disinfectantમાં સૌથી મજબૂત છે, chlorine ન મારી શકે એવા cyst પણ મારે, અને '
                '<b>કોઈ residue કે chlorinated by-product</b> રહેતું નથી, કારણ કે એ ફરી oxygenમાં ફેરવાય.',
                'એ રંગ, સ્વાદ, ગંધ, iron અને manganese પણ કાઢે, એટલે એક જ પગલું ઘણાં કામ કરે.',
                'પણ treatment પછી કોઈ protection રહેતું નથી, એટલે પાણી તરત વાપરવું પડે; અને ozone site પર જ '
                'બનાવવું પડે (સંગ્રહ થાય નહીં), એટલે plant મોંઘું.',
                'Ozone ઝેરી અને corrosive છે, એટલે generator roomમાં ventilation જોઈએ અને off-gas નષ્ટ કરવું '
                'પડે.'),
    ),
))

Q2['cards'].append(dict(
    number='Q.2 (c)', marks=7, q='Explain zeolite process in Detail.',
    en=join(
        h4('Definition and principle'),
        p('The <b>zeolite process</b> (base-exchange or ion-exchange softening) removes the hardness of '
          'water by exchanging the calcium and magnesium ions of the water for the sodium ions held on a '
          '<b>zeolite</b> bed. Zeolite is a naturally occurring or synthetic sodium alumino-silicate, '
          'Na<sub>2</sub>O·Al<sub>2</sub>O<sub>3</sub>·nSiO<sub>2</sub>; the synthetic resin form is called '
          'permutit. Because sodium salts are soluble, the water leaves the bed soft — there is no '
          'precipitate at all.'),
        h4('Reactions'),
        p('Na<sub>2</sub>Z + Ca(HCO<sub>3</sub>)<sub>2</sub> → CaZ + 2NaHCO<sub>3</sub>'),
        p('Na<sub>2</sub>Z + CaSO<sub>4</sub> → CaZ + Na<sub>2</sub>SO<sub>4</sub>'),
        p('Na<sub>2</sub>Z + MgCl<sub>2</sub> → MgZ + 2NaCl'),
        p('Regeneration: CaZ + 2NaCl → Na<sub>2</sub>Z + CaCl<sub>2</sub>'),
        h4('Construction — part and purpose'),
        table(['Part', 'Purpose'], [
            ['Zeolite bed in a steel vessel (1–2 m deep)', 'the exchange medium; its capacity is about '
             '30 000 to 60 000 litre of water per m<sup>3</sup> of bed per cycle'],
            ['Support gravel and strainers', 'carry the bed and let the water pass without carrying the '
             'zeolite out'],
            ['Hard water inlet with a flow meter and control valve', 'sets a flow that gives the required '
             'contact time'],
            ['Brine tank and ejector (10 % NaCl)', 'regenerates the bed when it is exhausted'],
            ['Backwash and rinse lines', 'remove dirt and the spent brine before the next run'],
            ['Soft water outlet and hardness test point', 'proves that the water leaving is soft'],
        ]),
        figure(fig.zeolite(),
               'Fig. 2.3 · Zeolite softener — hard water in, zeolite bed, support gravel, brine '
               'regeneration and soft water out.'),
        h4('Working — step and reason'),
        steps(('Step 1 · Service', 'Hard water passes down through the zeolite bed, and Na<sup>+</sup> on '
                                   'the zeolite is exchanged for Ca<sup>2+</sup> and Mg<sup>2+</sup>. '
                                   'Reason: the zeolite has a greater affinity for the divalent ions, so '
                                   'the exchange goes forward.'),
              ('Step 2 · Monitoring', 'The hardness of the outlet is tested at intervals. Reason: the bed '
                                      'has a fixed capacity, and the first rise in outlet hardness marks '
                                      'the break-through, after which the water would be hard again.'),
              ('Step 3 · Backwash', 'Water is passed upwards to loosen and clean the bed. Reason: the bed '
                                    'compacts during service and collects dirt; backwashing regains the '
                                    'void space for the brine.'),
              ('Step 4 · Regeneration', '10 % NaCl brine is passed slowly through the bed, so the '
                                        'Ca<sup>2+</sup> and Mg<sup>2+</sup> go into solution and the '
                                        'zeolite returns to the Na form. Reason: the high concentration of '
                                        'sodium drives the equilibrium backwards.'),
              ('Step 5 · Rinse', 'The bed is rinsed with soft water until the outlet is free of chloride. '
                                 'Reason: any brine left in the bed would make the first soft water salty '
                                 'and would add chloride to the boiler feed.')),
        h4('Worked example — ion-exchange capacity'),
        p('A zeolite softener of 2 m<sup>3</sup> bed has a capacity of 50 000 litre of water per '
          'm<sup>3</sup> of bed per cycle for water of 300 ppm hardness. A plant sends water of 450 ppm '
          'hardness. Find the water that can be softened per cycle, and the salt needed for regeneration '
          'at 0.2 kg NaCl per m<sup>3</sup> of bed.'),
        work('Given: bed volume = 2 m<sup>3</sup> · rated capacity = 50 000 L/m<sup>3</sup> at 300 ppm · '
             'actual hardness = 450 ppm · salt = 0.2 kg/m<sup>3</sup> of bed',
             'Capacity in hardness removed = 50 000 × 300 = 1.5 × 10<sup>7</sup> mg/L·L per m<sup>3</sup> '
             'of bed',
             'Water per m<sup>3</sup> of bed at 450 ppm = ' + frac('1.5 × 10<sup>7</sup>', '450') + ' = '
             '33 333 L',
             'For a 2 m<sup>3</sup> bed = 2 × 33 333 = 66 666 L ≈ 66.7 m<sup>3</sup>',
             'Salt = 0.2 × 2 = 0.4 kg per regeneration'),
        result('Soft water per cycle ≈ 66.7 m<sup>3</sup>; salt for regeneration = 0.4 kg'),
        p('Sanity check: harder water gives less soft water per cycle, as found (33 333 against 50 000 '
          'L/m<sup>3</sup>) — proportional to the ratio 300/450, correct.'),
        h4('Advantages'),
        bullets('Hardness falls to <b>zero</b> (2–5 ppm), which no lime–soda plant can achieve.',
                'The plant is compact and the process is automatic, so labour is low.',
                'No sludge is formed, so there is no disposal problem of the kind that lime–soda has.',
                'It works on water of any hardness, and the same bed works for many cycles.'),
        h4('Limitations'),
        bullets('It removes only hardness — total dissolved solids and alkalinity are <b>not</b> reduced, '
                'so the water is not demineralised.',
                'Water with turbidity, iron or manganese must be pre-treated, because these foul the bed.',
                'Brine is needed in quantity, and the spent brine (calcium chloride) is a disposal load; '
                'it is also corrosive and damages concrete if it is dumped on the floor.',
                'The process adds sodium salts to the boiler feed, which raises the dissolved solids and '
                'therefore the blow-down.'),
    ),
    gu=join(
        h4('વ્યાખ્યા અને સિદ્ધાંત'),
        p('<b>Zeolite process</b> (base-exchange કે ion-exchange softening) પાણીની hardness એ રીતે કાઢે કે '
          'પાણીમાંના calcium અને magnesium ionની જગ્યા <b>zeolite</b> bed પર રહેલા sodium ion લે. Zeolite એ '
          'કુદરતી કે synthetic sodium alumino-silicate છે, Na<sub>2</sub>O·Al<sub>2</sub>O<sub>3</sub>·'
          'nSiO<sub>2</sub>; synthetic resin સ્વરૂપને permutit કહે. Sodiumનાં ક્ષાર દ્રાવ્ય હોવાથી bedમાંથી '
          'નીકળતું પાણી soft થાય — કોઈ precipitate બને જ નહીં.'),
        h4('પ્રક્રિયાઓ'),
        p('Na<sub>2</sub>Z + Ca(HCO<sub>3</sub>)<sub>2</sub> → CaZ + 2NaHCO<sub>3</sub>'),
        p('Na<sub>2</sub>Z + CaSO<sub>4</sub> → CaZ + Na<sub>2</sub>SO<sub>4</sub>'),
        p('Na<sub>2</sub>Z + MgCl<sub>2</sub> → MgZ + 2NaCl'),
        p('Regeneration: CaZ + 2NaCl → Na<sub>2</sub>Z + CaCl<sub>2</sub>'),
        h4('રચના — ભાગ અને હેતુ'),
        table(['ભાગ', 'હેતુ'], [
            ['Steel vesselમાં zeolite bed (1–2 m ઊંડું)', 'exchange medium; capacity લગભગ એક cycleમાં પ્રતિ '
             'm<sup>3</sup> bed 30 000થી 60 000 લિટર પાણી'],
            ['Support gravel અને strainer', 'bed ઉપાડે અને પાણી પસાર કરાવે પણ zeolite બહાર ન જાય'],
            ['Hard water inlet, flow meter અને control valve', 'એવો flow ઠરાવે જેથી જરૂરી contact time '
             'મળે'],
            ['Brine tank અને ejector (10 % NaCl)', 'bed થાકે ત્યારે એને regenerate કરે'],
            ['Backwash અને rinse લાઇન', 'ધૂળ અને વપરાયેલું brine આગલા run પહેલાં કાઢે'],
            ['Soft water outlet અને hardness test point', 'નીકળતું પાણી soft છે તે સાબિત કરે'],
        ]),
        figure(fig.zeolite(),
               'Fig. 2.3 · Zeolite softener — hard water in, zeolite bed, support gravel, brine '
               'regeneration અને soft water out.'),
        h4('કાર્ય — સ્ટેપ અને કારણ'),
        steps(('Step 1 · Service', 'Hard water zeolite bedમાંથી નીચે જાય અને zeolite પરના Na<sup>+</sup>ની '
                                   'જગ્યા Ca<sup>2+</sup> તથા Mg<sup>2+</sup> લે. કારણ: zeoliteનું divalent '
                                   'ion પ્રત્યે વધુ આકર્ષણ હોવાથી exchange આગળ વધે.'),
              ('Step 2 · Monitoring', 'Outletની hardness સમયે સમયે ચકાસાય. કારણ: bedની capacity નિશ્ચિત છે, '
                                      'અને outlet hardness પહેલી વાર વધે તે break-through — એ પછી પાણી ફરી '
                                      'hard થાય.'),
              ('Step 3 · Backwash', 'પાણી ઉપરની દિશામાં પસાર કરીને bed ઢીલું અને સાફ કરાય. કારણ: serviceમાં '
                                    'bed દબાય અને ધૂળ એકઠી કરે; backwashથી brine માટે જગ્યા ફરી મળે.'),
              ('Step 4 · Regeneration', '10 % NaCl brine ધીમે bedમાંથી પસાર થાય, જેથી Ca<sup>2+</sup> અને '
                                        'Mg<sup>2+</sup> દ્રાવણમાં જાય અને zeolite ફરી Na સ્વરૂપે આવે. કારણ: '
                                        'sodiumની ઊંચી concentration સંતુલન ઊલટી દિશામાં ધકેલે.'),
              ('Step 5 · Rinse', 'Outletમાંથી chloride જતું રહે ત્યાં સુધી soft પાણીથી rinse કરાય. કારણ: bedમાં '
                                 'રહી ગયેલું brine પહેલું પાણી ખારું કરે અને boiler feedમાં chloride ઉમેરે.')),
        h4('ઉકેલેલું ઉદાહરણ — ion-exchange capacity'),
        p('2 m<sup>3</sup> bed વાળા zeolite softenerની capacity 300 ppm hardness પર પ્રતિ m<sup>3</sup> bed '
          '50 000 લિટર પાણી છે. Plant 450 ppm hardnessનું પાણી મોકલે છે. એક cycleમાં કેટલું પાણી soft થશે, '
          'અને પ્રતિ m<sup>3</sup> bed 0.2 kg NaCl લઈને regeneration માટે કેટલું salt જોઈએ?'),
        work('Given: bed volume = 2 m<sup>3</sup> · rated capacity = 50 000 L/m<sup>3</sup> at 300 ppm · '
             'actual hardness = 450 ppm · salt = 0.2 kg/m<sup>3</sup> bed',
             'કાઢી શકાતી hardness = 50 000 × 300 = 1.5 × 10<sup>7</sup> mg/L·L પ્રતિ m<sup>3</sup> bed',
             '450 ppm પર પ્રતિ m<sup>3</sup> bed પાણી = ' + frac('1.5 × 10<sup>7</sup>', '450') + ' = '
             '33 333 L',
             '2 m<sup>3</sup> bed માટે = 2 × 33 333 = 66 666 L ≈ 66.7 m<sup>3</sup>',
             'Salt = 0.2 × 2 = 0.4 kg પ્રતિ regeneration'),
        result('એક cycleમાં soft પાણી ≈ 66.7 m<sup>3</sup>; regeneration માટે salt = 0.4 kg'),
        p('Sanity check: વધુ hard પાણી માટે પ્રતિ cycle ઓછું પાણી મળે (50 000ને બદલે 33 333 L/m<sup>3</sup>) — '
          '300/450ના પ્રમાણમાં, સાચું.'),
        h4('ફાયદા'),
        bullets('Hardness <b>શૂન્ય</b> સુધી જાય (2–5 ppm), જે lime–soda plant કરી શકતું નથી.',
                'Plant compact અને process automatic, એટલે મજૂરી ઓછી.',
                'કોઈ sludge બનતું નથી, એટલે lime–soda જેવી નિકાલની તકલીફ નહીં.',
                'કોઈ પણ hardnessના પાણી પર ચાલે, અને એક જ bed ઘણા cycle કામ આવે.'),
        h4('મર્યાદાઓ'),
        bullets('એ ફક્ત hardness કાઢે — total dissolved solids અને alkalinity <b>ઘટાડતું નથી</b>, એટલે પાણી '
                'demineralised થતું નથી.',
                'Turbidity, iron કે manganese વાળું પાણી પહેલાં treat કરવું પડે, કારણ કે એ bed બગાડે.',
                'Brine જથ્થામાં જોઈએ, અને વપરાયેલું brine (calcium chloride) નિકાલનો ભાર છે; એ corrosive છે '
                'અને જમીન પર રેડો તો કોંક્રિટ બગાડે.',
                'Process boiler feedમાં sodium ક્ષાર ઉમેરે, જેનાથી dissolved solids વધે અને blow-down પણ વધે.'),
    ),
))

Q2['cards'].append(dict(
    number='Q.2 (a)', marks=3, tag='OR', q='List and Explain all water purification method.',
    en=join(
        p('Water purification is done in a series of steps, each one removing a particular kind of '
          'impurity. The methods, in the order in which a plant uses them:'),
        table(['Method', 'Removes', 'In one line'], [
            ['<b>Screening</b>', 'leaves, sticks, fish, floating matter', 'a bar screen or drum screen at '
             'the intake'],
            ['<b>Aeration</b>', 'dissolved iron, manganese, H<sub>2</sub>S, taste and odour',
             'water is sprayed into air so the gases escape and the iron oxidises'],
            ['<b>Coagulation and flocculation</b>', 'colloidal clay, colour, turbidity',
             'alum or polyelectrolyte is added and slow stirring grows the flocs'],
            ['<b>Sedimentation</b>', 'settleable floc and silt', 'the water is held still so the floc '
             'settles as sludge'],
            ['<b>Filtration</b>', 'fine suspended matter and part of the bacteria',
             'sand, anthracite or a pressure filter'],
            ['<b>Softening</b>', 'hardness due to Ca and Mg', 'lime–soda, zeolite or ion exchange'],
            ['<b>Demineralisation</b>', 'all dissolved salts', 'cation and anion exchange resins'],
            ['<b>Disinfection</b>', 'bacteria, viruses, cysts', 'chlorine, ozone or UV'],
            ['<b>Reverse osmosis / distillation</b>', 'dissolved salts, especially from sea water',
             'pressure across a membrane, or evaporation'],
        ]),
        p('<b>Example:</b> river water is screened, aerated, coagulated with alum, settled, filtered, '
          'softened by zeolite and finally chlorinated. Bore-well water is clear, so it skips coagulation '
          'and goes straight to softening and disinfection.'),
    ),
    gu=join(
        p('પાણીની શુદ્ધિ શ્રેણીબદ્ધ પગલાંમાં થાય, અને દરેક પગલું એક ખાસ પ્રકારની અશુદ્ધિ કાઢે. Plant જે ક્રમમાં '
          'વાપરે તે પ્રમાણે પદ્ધતિઓ:'),
        table(['પદ્ધતિ', 'શું કાઢે', 'એક લીટીમાં'], [
            ['<b>Screening</b>', 'પાન, લાકડી, માછલી, તરતો કચરો', 'intake પર bar screen કે drum screen'],
            ['<b>Aeration</b>', 'ઓગળેલું iron, manganese, H<sub>2</sub>S, સ્વાદ અને ગંધ',
             'પાણી હવામાં છાંટાય જેથી gas નીકળે અને iron oxidise થાય'],
            ['<b>Coagulation અને flocculation</b>', 'colloidal clay, રંગ, turbidity',
             'alum કે polyelectrolyte ઉમેરાય અને ધીમા stirringથી floc મોટો થાય'],
            ['<b>Sedimentation</b>', 'બેસી શકે એવો floc અને કાંપ', 'પાણી સ્થિર રાખાય જેથી floc sludge તરીકે '
             'બેસે'],
            ['<b>Filtration</b>', 'બારીક તરતા પદાર્થ અને થોડા જીવાણુ', 'sand, anthracite કે pressure filter'],
            ['<b>Softening</b>', 'Ca અને Mgથી થતી hardness', 'lime–soda, zeolite કે ion exchange'],
            ['<b>Demineralisation</b>', 'બધા ઓગળેલા ક્ષાર', 'cation અને anion exchange resin'],
            ['<b>Disinfection</b>', 'જીવાણુ, વિષાણુ, cyst', 'chlorine, ozone કે UV'],
            ['<b>Reverse osmosis / distillation</b>', 'ઓગળેલા ક્ષાર, ખાસ કરીને દરિયાના પાણીમાંથી',
             'membrane પર pressure, કે બાષ્પીભવન'],
        ]),
        p('<b>ઉદાહરણ:</b> નદીનું પાણી screen, aerate, alumથી coagulate, settle, filter, zeoliteથી soft અને '
          'છેવટે chlorinate થાય. Bore-wellનું પાણી સાફ હોય એટલે coagulation છોડીને સીધું softening અને '
          'disinfection પર જાય.'),
    ),
))

Q2['cards'].append(dict(
    number='Q.2 (b)', marks=4, tag='OR', q='Explain Sterilization of water using UV rays',
    en=join(
        h4('Definition'),
        p('<b>UV sterilisation</b> is disinfection of water by passing it through a chamber where a '
          'low-pressure mercury lamp gives <b>ultraviolet light at 254 nm</b>. That wavelength is absorbed '
          'by the nucleic acid of the cell, and the energy damages the DNA so that the organism cannot '
          'replicate. The cell may still be alive but it can no longer multiply, so it cannot infect.'),
        h4('Construction — part and purpose'),
        table(['Part', 'Purpose'], [
            ['Pre-filter (5 µm cartridge)', 'removes turbidity and particles, because a particle shields '
             'the microbes behind it'],
            ['UV chamber (stainless steel, polished inside)', 'holds the water in a thin annulus around the '
             'lamp, so every drop is close to the lamp'],
            ['Low-pressure mercury lamp, 254 nm', 'the source of the germicidal light; it has to be clean '
             'to pass the full output'],
            ['Quartz sleeve', 'separates the lamp from the water but passes UV; quartz is used because '
             'ordinary glass absorbs UV'],
            ['Ballast and lamp monitor', 'runs the lamp and shows that it is still emitting enough '
             'intensity'],
            ['Solenoid valve on the outlet', 'shuts the flow if the lamp fails, so untreated water cannot '
             'pass'],
        ]),
        figure(fig.uv_sterilizer(),
               'Fig. 2.4 · UV steriliser — pre-filter, UV chamber with quartz-sleeved lamp and sterile '
               'water outlet.'),
        h4('Working — step and reason'),
        steps(('Step 1', 'Water is filtered to below 1 NTU turbidity. Reason: turbidity and iron absorb and '
                         'scatter UV, so the dose reaching the microbes would fall.'),
              ('Step 2', 'The water flows through the annular gap around the quartz sleeve in a thin film. '
                         'Reason: UV travels only a short distance in water, so the layer must be thin for '
                         'every drop to receive the dose.'),
              ('Step 3', 'The lamp gives 254 nm light and the water receives a dose of about 30–40 '
                         'mJ/cm<sup>2</sup> in a few seconds. Reason: 30 mJ/cm<sup>2</sup> gives over '
                         '99.9 % inactivation of bacteria and most viruses.'),
              ('Step 4', 'The lamp intensity is monitored and the outlet valve closes on failure. Reason: '
                         'UV leaves no residual, so there is no way to check the water afterwards — the '
                         'protection must be on the lamp itself.')),
        h4('Worked example — contact time in the chamber'),
        p('A UV chamber holds 4 litre of water and the flow is 2 m<sup>3</sup>/h. Find the contact time, '
          'and say whether it is enough for a dose of 30 mJ/cm<sup>2</sup> at an intensity of 10 '
          'mW/cm<sup>2</sup>.'),
        work('Given: chamber volume = 4 L · flow = 2 m<sup>3</sup>/h = 2000 L/h · intensity = 10 '
             'mW/cm<sup>2</sup> · required dose = 30 mJ/cm<sup>2</sup>',
             'Contact time = ' + frac('volume', 'flow') + ' = ' + frac('4', '2000') + ' h',
             'Contact time = 0.002 h = 7.2 s',
             'Dose = intensity × time = 10 mW/cm<sup>2</sup> × 7.2 s',
             'Dose = 72 mJ/cm<sup>2</sup>'),
        result('Contact time = 7.2 s, and the dose delivered = 72 mJ/cm<sup>2</sup> — more than the 30 '
               'mJ/cm<sup>2</sup> required'),
        p('Sanity check: a dose of 72 mJ/cm<sup>2</sup> is over twice the minimum, which is what a real '
          'unit is designed for, since the lamp output falls with age and fouling.'),
        h4('Advantages and limitations'),
        bullets('No chemical is added, so there is <b>no taste, no odour and no by-product</b> such as '
                'trihalomethane; the water tastes the same as before.',
                'The contact time is only a few seconds, so the unit is compact and needs no contact tank.',
                'It kills bacteria, viruses and <i>Cryptosporidium</i> and <i>Giardia</i> cysts, which '
                'chlorine handles poorly.',
                'But it gives <b>no residual protection</b>, so it is used at the point of use; turbidity, '
                'iron and hardness scale shield the microbes and must be removed first; and the lamp ages, '
                'so it is replaced every 8 000–9 000 hours whether it has failed or not.'),
    ),
    gu=join(
        h4('વ્યાખ્યા'),
        p('<b>UV sterilisation</b> એટલે પાણીને એવા chamberમાંથી પસાર કરવું જ્યાં low-pressure mercury lamp '
          '<b>254 nmનું ultraviolet પ્રકાશ</b> આપે. એ wavelength cellના nucleic acid શોષે, અને energy DNA '
          'બગાડે એટલે જીવાણુ વધી શકતું નથી. Cell જીવતું હોઈ શકે પણ ગુણાકાર ન કરી શકે, એટલે ચેપ ન લગાડે.'),
        h4('રચના — ભાગ અને હેતુ'),
        table(['ભાગ', 'હેતુ'], [
            ['Pre-filter (5 µm cartridge)', 'turbidity અને કણ કાઢે, કારણ કે કણ પાછળના જીવાણુને ઢાંકે'],
            ['UV chamber (અંદરથી polished stainless steel)', 'પાણીને lamp ફરતે પાતળા annulusમાં રાખે, જેથી '
             'દરેક બિંદુ lampની નજીક રહે'],
            ['Low-pressure mercury lamp, 254 nm', 'germicidal પ્રકાશનો સ્રોત; પૂરો output જાય એ માટે એ સાફ '
             'રહેવો જોઈએ'],
            ['Quartz sleeve', 'lampને પાણીથી અલગ રાખે પણ UV પસાર કરે; quartz વપરાય કારણ કે સામાન્ય કાચ UV '
             'શોષી લે'],
            ['Ballast અને lamp monitor', 'lamp ચલાવે અને એ પૂરતી intensity આપે છે તે દેખાડે'],
            ['Outlet પર solenoid valve', 'lamp નિષ્ફળ જાય તો flow બંધ કરે, જેથી untreated પાણી ન જાય'],
        ]),
        figure(fig.uv_sterilizer(),
               'Fig. 2.4 · UV steriliser — pre-filter, quartz sleeve વાળા lamp સાથે UV chamber અને sterile '
               'water outlet.'),
        h4('કાર્ય — સ્ટેપ અને કારણ'),
        steps(('Step 1', 'પાણી 1 NTUથી ઓછી turbidity સુધી filter થાય. કારણ: turbidity અને iron UV શોષે તથા '
                         'scatter કરે, એટલે જીવાણુ સુધી પહોંચતો dose ઘટે.'),
              ('Step 2', 'પાણી quartz sleeve ફરતેના પાતળા annulusમાંથી પાતળા સ્તર તરીકે વહે. કારણ: પાણીમાં UV '
                         'ટૂંકું અંતર જ જાય, એટલે દરેક ટીપું dose પામે એ માટે સ્તર પાતળું હોવું જોઈએ.'),
              ('Step 3', 'Lamp 254 nm આપે અને પાણીને થોડી સેકન્ડમાં લગભગ 30–40 mJ/cm<sup>2</sup> dose મળે. '
                         'કારણ: 30 mJ/cm<sup>2</sup>થી જીવાણુના 99.9 %થી વધુ અને મોટા ભાગના વિષાણુ નિષ્ક્રિય '
                         'થાય.'),
              ('Step 4', 'Lampની intensity monitor થાય અને નિષ્ફળતા પર outlet valve બંધ થાય. કારણ: UV કોઈ '
                         'residual રાખતું નથી, એટલે પાછળ પાણી ચકાસવાનો રસ્તો નથી — રક્ષા lamp પર જ '
                         'કરવી પડે.')),
        h4('ઉકેલેલું ઉદાહરણ — chamberમાં contact time'),
        p('UV chamberમાં 4 લિટર પાણી રહે અને flow 2 m<sup>3</sup>/h છે. Contact time શોધો, અને 10 '
          'mW/cm<sup>2</sup> intensity પર 30 mJ/cm<sup>2</sup> dose માટે એ પૂરતો છે કે નહીં કહો.'),
        work('Given: chamber volume = 4 L · flow = 2 m<sup>3</sup>/h = 2000 L/h · intensity = 10 '
             'mW/cm<sup>2</sup> · જરૂરી dose = 30 mJ/cm<sup>2</sup>',
             'Contact time = ' + frac('volume', 'flow') + ' = ' + frac('4', '2000') + ' h',
             'Contact time = 0.002 h = 7.2 s',
             'Dose = intensity × time = 10 mW/cm<sup>2</sup> × 7.2 s',
             'Dose = 72 mJ/cm<sup>2</sup>'),
        result('Contact time = 7.2 s અને મળતો dose = 72 mJ/cm<sup>2</sup> — જરૂરી 30 mJ/cm<sup>2</sup>થી વધુ'),
        p('Sanity check: 72 mJ/cm<sup>2</sup> dose લઘુતમ કરતાં બે ગણાથી વધુ છે, જે સાચી unitમાં હોય છે — '
          'કારણ કે lampનો output ઉંમર અને fouling સાથે ઘટે.'),
        h4('ફાયદા અને મર્યાદાઓ'),
        bullets('કોઈ રસાયણ ઉમેરાતું નથી, એટલે <b>સ્વાદ, ગંધ કે trihalomethane જેવો by-product</b> નથી; પાણીનો '
                'સ્વાદ પહેલા જેવો જ રહે.',
                'Contact time ફક્ત થોડી સેકન્ડ, એટલે unit compact અને contact tankની જરૂર નહીં.',
                'એ જીવાણુ, વિષાણુ અને <i>Cryptosporidium</i> તથા <i>Giardia</i> cyst મારે, જે chlorine મુશ્કેલીથી '
                'કાબૂમાં લે.',
                'પણ એ <b>કોઈ residual protection</b> આપતું નથી, એટલે point of use પર વપરાય; turbidity, iron '
                'અને hardnessનો scale જીવાણુને ઢાંકે એટલે પહેલાં કાઢવા પડે; અને lamp જૂનો થાય એટલે 8 000–9 000 '
                'કલાકે નિષ્ફળ ગયો ન હોય તો પણ બદલવો પડે.'),
    ),
))

Q2['cards'].append(dict(
    number='Q.2 (c)', marks=7, tag='OR', q='Explain ion exchange process in detail',
    en=join(
        h4('Definition and principle'),
        p('<b>Ion exchange</b> is the reversible exchange of ions between a solid resin and a solution '
          'passing through it. In water treatment, <b>cation resin</b> in the H<sup>+</sup> form takes the '
          'Ca<sup>2+</sup>, Mg<sup>2+</sup> and Na<sup>+</sup> from the water and releases H<sup>+</sup>; '
          'then <b>anion resin</b> in the OH<sup>−</sup> form takes the SO<sub>4</sub><sup>2−</sup>, '
          'Cl<sup>−</sup> and HCO<sub>3</sub><sup>−</sup> and releases OH<sup>−</sup>. The H<sup>+</sup> '
          'and OH<sup>−</sup> combine to form water, so the water leaves with almost no dissolved salts — '
          'this is <b>demineralisation</b>.'),
        h4('Reactions'),
        p('Cation: 2R–H + Ca<sup>2+</sup> → R<sub>2</sub>–Ca + 2H<sup>+</sup>'),
        p('Anion: R–OH + Cl<sup>−</sup> → R–Cl + OH<sup>−</sup>'),
        p('Overall: H<sup>+</sup> + OH<sup>−</sup> → H<sub>2</sub>O'),
        p('Regeneration: R<sub>2</sub>–Ca + 2HCl → 2R–H + CaCl<sub>2</sub>, and '
          'R–Cl + NaOH → R–OH + NaCl'),
        h4('Construction — part and purpose'),
        table(['Part', 'Purpose'], [
            ['Cation exchange vessel with resin bed', 'removes the metallic cations and releases H<sup>+</sup>'],
            ['Anion exchange vessel with resin bed', 'removes the acid anions and releases OH<sup>−</sup>'],
            ['Degasser (optional, between the two)', 'removes the CO<sub>2</sub> formed from bicarbonate, '
             'which reduces the load on the anion bed'],
            ['Acid dosing and regeneration system (HCl or H<sub>2</sub>SO<sub>4</sub>)', 'regenerates the '
             'cation resin'],
            ['Alkali dosing system (NaOH)', 'regenerates the anion resin'],
            ['Conductivity meter at the outlet', 'proves the water quality; a rise in conductivity means '
             'break-through'],
            ['Neutralisation pit for the spent regenerant', 'the spent acid and alkali are neutralised '
             'before disposal'],
        ]),
        figure(fig.ion_exchange(),
               'Fig. 2.5 · Ion-exchange demineralisation plant — cation bed, anion bed and regeneration '
               'with acid and alkali.'),
        h4('Working — step and reason'),
        steps(('Step 1 · Cation exchange', 'Water passes down through the cation resin in the H form. '
                                          'Reason: the resin has a strong affinity for divalent cations, so '
                                          'Ca and Mg are held and an equivalent quantity of H<sup>+</sup> '
                                          'is released.'),
              ('Step 2 · Degassing', 'The carbon dioxide formed from bicarbonate is stripped in a degasser. '
                                     'Reason: CO<sub>2</sub> is a gas dissolved in water, and removing it '
                                     'cheaply reduces the anion load and the alkali needed.'),
              ('Step 3 · Anion exchange', 'Water passes through the anion resin in the OH form. Reason: the '
                                          'acid anions are held and OH<sup>−</sup> is released, which '
                                          'neutralises the H<sup>+</sup> from the first bed.'),
              ('Step 4 · Check quality', 'Conductivity is monitored continuously. Reason: demineralised '
                                         'water has a conductivity of only 0.1–1 µS/cm, so any leak of '
                                         'salt shows up at once.'),
              ('Step 5 · Regeneration', 'When the conductivity rises, the beds are backwashed, regenerated '
                                        'with acid and alkali, and rinsed. Reason: the exchange is '
                                        'reversible, so the resin can be used for thousands of cycles.')),
        h4('Worked example — resin capacity and acid requirement'),
        p('A cation bed holds 500 litre of resin of capacity 1.2 eq/L. The raw water has a total cation '
          'content of 5 meq/L. Find the water treated per cycle, and the 33 % HCl needed for regeneration '
          'at 1.5 times the theoretical quantity. Take the equivalent mass of HCl as 36.5 g/eq.'),
        work('Given: resin = 500 L · capacity = 1.2 eq/L · cations = 5 meq/L = 0.005 eq/L · acid excess = '
             '1.5 times · HCl equivalent mass = 36.5 g/eq',
             'Total capacity = 500 × 1.2 = 600 eq',
             'Water per cycle = ' + frac('capacity', 'cation concentration') + ' = ' + frac('600', '0.005'),
             'Water per cycle = 120 000 L = 120 m<sup>3</sup>',
             'HCl needed = 1.5 × 600 × 36.5 = 32 850 g',
             '33 % HCl solution = ' + frac('32 850', '0.33') + ' = 99 545 g'),
        result('Water treated per cycle = 120 m<sup>3</sup>; 33 % HCl required ≈ 99.5 kg'),
        p('Sanity check: 99.5 kg of 33 % acid for 120 m<sup>3</sup> is about 0.8 kg per m<sup>3</sup> — the '
          'normal figure for a demineralisation plant, so the calculation is consistent.'),
        h4('Advantages'),
        bullets('It gives <b>complete demineralisation</b>, not just softening, so the water is suitable '
                'for high-pressure boilers and for pharmaceutical use.',
                'The plant is compact and the quality is monitored continuously, so it can be automatic.',
                'It works at ambient temperature and produces no sludge.'),
        h4('Limitations'),
        bullets('The resins are expensive and are fouled by chlorine, iron and organic matter, so the feed '
                'must be pre-treated.',
                'Acid and alkali are needed in quantity, and the spent regenerant is a corrosive waste '
                'that must be neutralised.',
                'The water is aggressive (low pH, no buffer) and attacks mild steel, so stainless steel or '
                'PVC-lined pipe is required.',
                'The process cannot remove uncharged matter such as silica, and colloidal silica passes '
                'through, which matters at very high boiler pressure.'),
    ),
    gu=join(
        h4('વ્યાખ્યા અને સિદ્ધાંત'),
        p('<b>Ion exchange</b> એટલે ઘન resin અને એમાંથી પસાર થતા દ્રાવણ વચ્ચે ionની ઉલટાવી શકાય એવી અદલાબદલી. '
          'Water treatmentમાં H<sup>+</sup> સ્વરૂપનું <b>cation resin</b> પાણીમાંથી Ca<sup>2+</sup>, '
          'Mg<sup>2+</sup> અને Na<sup>+</sup> લે અને H<sup>+</sup> છોડે; પછી OH<sup>−</sup> સ્વરૂપનું '
          '<b>anion resin</b> SO<sub>4</sub><sup>2−</sup>, Cl<sup>−</sup> અને HCO<sub>3</sub><sup>−</sup> લે '
          'અને OH<sup>−</sup> છોડે. H<sup>+</sup> અને OH<sup>−</sup> મળીને પાણી બને, એટલે પાણીમાં લગભગ કોઈ '
          'ઓગળેલા ક્ષાર રહેતા નથી — આ જ <b>demineralisation</b>.'),
        h4('પ્રક્રિયાઓ'),
        p('Cation: 2R–H + Ca<sup>2+</sup> → R<sub>2</sub>–Ca + 2H<sup>+</sup>'),
        p('Anion: R–OH + Cl<sup>−</sup> → R–Cl + OH<sup>−</sup>'),
        p('કુલ: H<sup>+</sup> + OH<sup>−</sup> → H<sub>2</sub>O'),
        p('Regeneration: R<sub>2</sub>–Ca + 2HCl → 2R–H + CaCl<sub>2</sub>, અને R–Cl + NaOH → R–OH + NaCl'),
        h4('રચના — ભાગ અને હેતુ'),
        table(['ભાગ', 'હેતુ'], [
            ['Cation exchange vessel અને resin bed', 'ધાતુના cation કાઢીને H<sup>+</sup> છોડે'],
            ['Anion exchange vessel અને resin bed', 'acidના anion કાઢીને OH<sup>−</sup> છોડે'],
            ['Degasser (વચ્ચે, વૈકલ્પિક)', 'bicarbonateમાંથી બનેલું CO<sub>2</sub> કાઢે, જેથી anion bed પરનો '
             'ભાર ઘટે'],
            ['Acid dosing અને regeneration system (HCl કે H<sub>2</sub>SO<sub>4</sub>)', 'cation resin '
             'regenerate કરે'],
            ['Alkali dosing system (NaOH)', 'anion resin regenerate કરે'],
            ['Outlet પર conductivity meter', 'પાણીની ગુણવત્તા સાબિત કરે; conductivity વધે એટલે break-through'],
            ['વપરાયેલા regenerant માટે neutralisation pit', 'વપરાયેલું acid અને alkali નિકાલ પહેલાં '
             'neutralise થાય'],
        ]),
        figure(fig.ion_exchange(),
               'Fig. 2.5 · Ion-exchange demineralisation plant — cation bed, anion bed અને acid તથા alkali '
               'સાથે regeneration.'),
        h4('કાર્ય — સ્ટેપ અને કારણ'),
        steps(('Step 1 · Cation exchange', 'પાણી H સ્વરૂપના cation resinમાંથી નીચે જાય. કારણ: resinનું '
                                           'divalent cation પ્રત્યે મજબૂત આકર્ષણ હોવાથી Ca અને Mg પકડાય '
                                           'અને એટલું જ H<sup>+</sup> છૂટે.'),
              ('Step 2 · Degassing', 'Bicarbonateમાંથી બનેલું carbon dioxide degasserમાં કાઢાય. કારણ: '
                                     'CO<sub>2</sub> પાણીમાં ઓગળેલો gas છે, અને એ સસ્તાઈથી કાઢતાં anion bed પરનો '
                                     'ભાર અને alkaliની જરૂરિયાત ઘટે.'),
              ('Step 3 · Anion exchange', 'પાણી OH સ્વરૂપના anion resinમાંથી જાય. કારણ: acidના anion પકડાય '
                                          'અને OH<sup>−</sup> છૂટે, જે પહેલા bedમાંથી આવેલા H<sup>+</sup>ને '
                                          'neutralise કરે.'),
              ('Step 4 · ગુણવત્તા ચકાસો', 'Conductivity સતત monitor થાય. કારણ: demineralised પાણીની '
                                         'conductivity ફક્ત 0.1–1 µS/cm હોય, એટલે કોઈ ક્ષાર લીક થાય તો તરત '
                                         'દેખાય.'),
              ('Step 5 · Regeneration', 'Conductivity વધે ત્યારે bed backwash, acid તથા alkaliથી regenerate '
                                        'અને rinse થાય. કારણ: exchange reversible છે, એટલે એક જ resin હજારો '
                                        'cycle ચાલે.')),
        h4('ઉકેલેલું ઉદાહરણ — resin capacity અને acidની જરૂરિયાત'),
        p('Cation bedમાં 500 લિટર resin છે જેની capacity 1.2 eq/L. Raw waterમાં કુલ cation 5 meq/L છે. એક '
          'cycleમાં કેટલું પાણી treat થશે, અને સૈદ્ધાંતિક જથ્થાના 1.5 ગણા પર 33 % HCl કેટલું જોઈએ? HClનું '
          'equivalent mass 36.5 g/eq લો.'),
        work('Given: resin = 500 L · capacity = 1.2 eq/L · cation = 5 meq/L = 0.005 eq/L · acid excess = '
             '1.5 ગણું · HCl equivalent mass = 36.5 g/eq',
             'કુલ capacity = 500 × 1.2 = 600 eq',
             'પ્રતિ cycle પાણી = ' + frac('capacity', 'cation concentration') + ' = ' + frac('600', '0.005'),
             'પ્રતિ cycle પાણી = 120 000 L = 120 m<sup>3</sup>',
             'જરૂરી HCl = 1.5 × 600 × 36.5 = 32 850 g',
             '33 % HCl દ્રાવણ = ' + frac('32 850', '0.33') + ' = 99 545 g'),
        result('પ્રતિ cycle પાણી = 120 m<sup>3</sup>; જરૂરી 33 % HCl ≈ 99.5 kg'),
        p('Sanity check: 120 m<sup>3</sup> માટે 99.5 kg 33 % acid એટલે પ્રતિ m<sup>3</sup> લગભગ 0.8 kg — '
          'demineralisation plant માટે સામાન્ય આંકડો, એટલે ગણતરી સુસંગત છે.'),
        h4('ફાયદા'),
        bullets('એ <b>સંપૂર્ણ demineralisation</b> આપે, ફક્ત softening નહીં, એટલે ઊંચા pressureના boiler અને '
                'pharmaceutical ઉપયોગ માટે પાણી યોગ્ય બને.',
                'Plant compact અને ગુણવત્તા સતત monitor થાય, એટલે automatic કરી શકાય.',
                'Ambient temperature પર ચાલે અને sludge બનતું નથી.'),
        h4('મર્યાદાઓ'),
        bullets('Resin મોંઘું છે અને chlorine, iron તથા organic પદાર્થથી બગડે, એટલે feed પહેલાં treat કરવું પડે.',
                'Acid અને alkali જથ્થામાં જોઈએ, અને વપરાયેલું regenerant corrosive કચરો છે જે neutralise '
                'કરવો પડે.',
                'Demineralised પાણી આક્રમક છે (નીચો pH, buffer નહીં) અને mild steel પર હુમલો કરે, એટલે '
                'stainless steel કે PVC-lined pipe જોઈએ.',
                'Silica જેવો uncharged પદાર્થ આ process કાઢી શકતું નથી, અને colloidal silica પસાર થઈ જાય, જે '
                'ખૂબ ઊંચા boiler pressure પર મહત્ત્વનું બને.'),
    ),
))
