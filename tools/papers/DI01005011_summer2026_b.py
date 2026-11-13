"""DI01005011 Summer 2026 — Q3, Q4 and Q5 answer parts (Plant Utilities)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from paperkit import frac, work, steps, result, table, bullets, numbered, h4, p, eq, figure
import chemfigs as fig
import utilfigs as ufig


def join(*chunks):
    return "\n".join(c for c in chunks if c)


# ---------------------------------------------------------------- Q3
Q3 = {
    'title_en': 'Q3 · Steam generators, steam, locomotive and Lancashire boilers',
    'title_gu': 'પ્ર.3 · સ્ટીમ જનરેટર, વરાળ, લોકોમોટિવ અને લેન્કશાયર બોઈલર',
    'cards': [],
}

Q3['cards'].append(dict(
    number='Q.3 (a)', marks=3, q='Draw well labeled diagram of steam generator',
    en=join(
        p('A <b>steam generator</b> (boiler) is a closed pressure vessel in which water is converted into '
          'steam by the heat of combustion. In a <b>water-tube</b> generator the water is inside the tubes '
          'and the hot gas is outside, which is the arrangement used for all modern high-capacity plants.'),
        figure(ufig.steam_generator(),
               'Fig. 3.1 · Water-tube steam generator — steam drum, water walls, furnace, superheater, '
               'economiser and air preheater.'),
        h4('The labelled parts, in one line each'),
        table(['Part', 'Job'], [
            ['Steam drum', 'separates steam from water and holds the water level'],
            ['Water walls (furnace tubes)', 'absorb radiant heat and protect the furnace wall'],
            ['Furnace', 'where the fuel burns; the radiant zone'],
            ['Superheater', 'dries and heats the steam above saturation'],
            ['Economiser', 'heats the feed water using the leaving flue gas'],
            ['Air preheater', 'heats the combustion air and cools the gas further'],
        ]),
        p('<b>Note:</b> water tubes can take a much higher pressure than a fire-tube shell, so the '
          'water-tube layout is used above about 20 bar, and always where a large steam rate is needed.'),
    ),
    gu=join(
        p('<b>Steam generator</b> (boiler) એ બંધ pressure vessel છે જેમાં દહનની ગરમીથી પાણી વરાળમાં ફેરવાય. '
          '<b>Water-tube</b> generatorમાં પાણી tubeની અંદર અને ગરમ gas બહાર હોય — આધુનિક ઊંચા ક્ષમતાવાળા બધા '
          'plantમાં આ જ ગોઠવણી વપરાય.'),
        figure(ufig.steam_generator(),
               'Fig. 3.1 · Water-tube steam generator — steam drum, water walls, furnace, superheater, '
               'economiser અને air preheater.'),
        h4('લેબલ કરેલા ભાગ, એક લીટીમાં'),
        table(['ભાગ', 'કામ'], [
            ['Steam drum', 'વરાળને પાણીથી અલગ કરે અને water level રાખે'],
            ['Water walls (furnace tubes)', 'radiant heat લે અને furnaceની દીવાલ બચાવે'],
            ['Furnace', 'જ્યાં fuel બળે; radiant વિસ્તાર'],
            ['Superheater', 'વરાળ સૂકવીને saturationથી ઉપર ગરમ કરે'],
            ['Economiser', 'નીકળતા flue gas વડે feed water ગરમ કરે'],
            ['Air preheater', 'combustion air ગરમ કરે અને gas વધુ ઠંડું કરે'],
        ]),
        p('<b>નોંધ:</b> Water tube fire-tube shell કરતાં ઘણું ઊંચું pressure ઝીલી શકે, એટલે લગભગ 20 barથી '
          'ઉપર અને જ્યાં મોટો steam rate જોઈએ ત્યાં water-tube ગોઠવણી જ વપરાય.'),
    ),
))

Q3['cards'].append(dict(
    number='Q.3 (b)', marks=4, q='Define Wet steam, Saturated Steam, Superheated steam',
    en=join(
        h4('The three states, defined'),
        p('<b>Wet steam</b> is steam that carries fine droplets of water in suspension — a two-phase '
          'mixture of dry saturated vapour and water. Its <b>dryness fraction</b> x = mass of vapour / '
          'total mass, and it is always less than 1.'),
        p('<b>Saturated steam</b> is steam in equilibrium with water at a given pressure. Its temperature '
          'is fixed by the pressure (<b>saturation temperature</b>), and any addition of heat at constant '
          'pressure simply evaporates more water instead of raising the temperature. <b>Dry saturated '
          'steam</b> has x = 1.'),
        p('<b>Superheated steam</b> is steam heated above its saturation temperature at the same pressure. '
          'The difference between its actual temperature and the saturation temperature is the '
          '<b>degree of superheat</b>.'),
        h4('Comparison'),
        table(['Point', 'Wet steam', 'Saturated (dry) steam', 'Superheated steam'], [
            ['Dryness fraction', 'x &lt; 1', 'x = 1', 'x = 1, and T &gt; T<sub>sat</sub>'],
            ['Temperature', 'T = T<sub>sat</sub> for the pressure', 'T = T<sub>sat</sub>',
             'T &gt; T<sub>sat</sub>'],
            ['Behaviour on adding heat at constant pressure', 'the droplets evaporate, T stays constant',
             'becomes superheated', 'temperature rises'],
            ['Condition', 'contains water droplets, so it is wet and gives up latent heat quickly',
             'no droplets', 'dry and gas-like'],
            ['Use', 'heating and sterilising where the latent heat is wanted',
             'process heating, evaporators', 'steam turbines and engines, because no droplets means no '
             'blade erosion'],
            ['Typical figure', 'x = 0.90–0.98 at the boiler outlet', 'h<sub>g</sub> = 2674 kJ/kg at 1 bar',
             '30–60 °C of superheat at the superheater outlet'],
        ]),
        h4('Worked example — dryness fraction and superheat'),
        p('Steam at 10 bar has a saturation temperature of 180 °C and h<sub>f</sub> = 763 kJ/kg, '
          'h<sub>fg</sub> = 2015 kJ/kg. (i) Find the enthalpy of wet steam with x = 0.95. (ii) A sample of '
          'steam at the same pressure is at 250 °C; find the degree of superheat.'),
        work('Given: P = 10 bar · T<sub>sat</sub> = 180 °C · h<sub>f</sub> = 763 kJ/kg · '
             'h<sub>fg</sub> = 2015 kJ/kg · x = 0.95 · actual temperature = 250 °C',
             'Formula: h = h<sub>f</sub> + x · h<sub>fg</sub>',
             '(i) h = 763 + 0.95 × 2015 = 763 + 1914.3',
             '(i) h = 2677.3 kJ/kg',
             '(ii) Degree of superheat = actual temperature − saturation temperature',
             '(ii) = 250 − 180'),
        result('(i) Wet steam enthalpy = 2677.3 kJ/kg · (ii) Degree of superheat = 70 °C'),
        p('Sanity check: h<sub>g</sub> at 10 bar is 763 + 2015 = 2778 kJ/kg, so the wet steam at 2677 kJ/kg '
          'is below it — correct for x = 0.95.'),
        h4('Limitation and importance'),
        p('Wet steam is a problem, not a goal: the droplets erode turbine blades and carry dissolved salts '
          'into the superheater, where they form scale. That is why steam is dried in the drum with a '
          'separator and then superheated before it goes to a turbine.'),
    ),
    gu=join(
        h4('ત્રણ અવસ્થાઓ, વ્યાખ્યા સાથે'),
        p('<b>Wet steam</b> એટલે એવી વરાળ જેમાં પાણીના બારીક ટીપાં તરે છે — dry saturated વરાળ અને પાણીનું '
          'દ્વિ-અવસ્થા મિશ્રણ. એનો <b>dryness fraction</b> x = વરાળનું દળ / કુલ દળ, અને એ હંમેશા 1થી ઓછો હોય.'),
        p('<b>Saturated steam</b> એટલે આપેલા pressure પર પાણી સાથે સંતુલનમાં રહેલી વરાળ. એનું તાપમાન pressureથી '
          'નિશ્ચિત થાય (<b>saturation temperature</b>), અને અચલ pressure પર heat આપતાં તાપમાન ન વધે પણ વધુ પાણી '
          'બાષ્પીભવન થાય. <b>Dry saturated steam</b>માં x = 1.'),
        p('<b>Superheated steam</b> એટલે એ જ pressure પર saturation temperatureથી ઉપર ગરમ કરેલી વરાળ. એના ખરા '
          'તાપમાન અને saturation temperature વચ્ચેના ફરકને <b>degree of superheat</b> કહે.'),
        h4('સરખામણી'),
        table(['મુદ્દો', 'Wet steam', 'Saturated (dry) steam', 'Superheated steam'], [
            ['Dryness fraction', 'x &lt; 1', 'x = 1', 'x = 1, અને T &gt; T<sub>sat</sub>'],
            ['તાપમાન', 'T = pressureનું T<sub>sat</sub>', 'T = T<sub>sat</sub>', 'T &gt; T<sub>sat</sub>'],
            ['અચલ pressure પર heat આપતાં', 'ટીપાં બાષ્પીભવન થાય, T અચલ', 'superheated બને', 'તાપમાન વધે'],
            ['સ્થિતિ', 'પાણીના ટીપાં, એટલે ભીની અને latent heat ઝડપથી આપે', 'ટીપાં નહીં',
             'સૂકી અને gas જેવી'],
            ['ઉપયોગ', 'latent heat જોઈએ ત્યાં heating અને sterilising', 'process heating, evaporator',
             'steam turbine અને engine, કારણ કે ટીપાં ન હોવાથી blade ઘસાય નહીં'],
            ['સામાન્ય આંકડો', 'boiler outlet પર x = 0.90–0.98', '1 bar પર h<sub>g</sub> = 2674 kJ/kg',
             'superheater outlet પર 30–60 °C superheat'],
        ]),
        h4('ઉકેલેલું ઉદાહરણ — dryness fraction અને superheat'),
        p('10 bar પર વરાળનું saturation temperature 180 °C છે, h<sub>f</sub> = 763 kJ/kg અને '
          'h<sub>fg</sub> = 2015 kJ/kg. (i) x = 0.95 વાળી wet steamની enthalpy શોધો. (ii) એ જ pressure પર '
          'વરાળનું તાપમાન 250 °C છે; degree of superheat શોધો.'),
        work('Given: P = 10 bar · T<sub>sat</sub> = 180 °C · h<sub>f</sub> = 763 kJ/kg · '
             'h<sub>fg</sub> = 2015 kJ/kg · x = 0.95 · ખરું તાપમાન = 250 °C',
             'Formula: h = h<sub>f</sub> + x · h<sub>fg</sub>',
             '(i) h = 763 + 0.95 × 2015 = 763 + 1914.3',
             '(i) h = 2677.3 kJ/kg',
             '(ii) Degree of superheat = ખરું તાપમાન − saturation temperature',
             '(ii) = 250 − 180'),
        result('(i) Wet steam enthalpy = 2677.3 kJ/kg · (ii) Degree of superheat = 70 °C'),
        p('Sanity check: 10 bar પર h<sub>g</sub> = 763 + 2015 = 2778 kJ/kg, એટલે 2677 kJ/kg વાળી wet steam '
          'એનાથી નીચે છે — x = 0.95 માટે સાચું.'),
        h4('મર્યાદા અને મહત્ત્વ'),
        p('Wet steam લક્ષ્ય નથી, સમસ્યા છે: ટીપાં turbine blade ઘસે અને ઓગળેલા ક્ષાર superheaterમાં લઈ '
          'જઈને scale બનાવે. એટલે જ વરાળને drumમાં separator વડે સૂકવીને, પછી turbine પર મોકલતાં પહેલાં '
          'superheat કરાય છે.'),
    ),
))

Q3['cards'].append(dict(
    number='Q.3 (c)', marks=7, q='Explain construction and working of Locomotive boiler with sketch',
    en=join(
        h4('Definition and use'),
        p('The <b>locomotive boiler</b> is a horizontal, multi-tubular <b>fire-tube</b> boiler with an '
          'internal firebox, developed for steam locomotives. It is compact, light, and able to make steam '
          'quickly, because the whole boiler is mounted on the engine frame and travels with it.'),
        h4('Construction — part by part'),
        table(['Part', 'Material / shape', 'Purpose'], [
            ['Shell (barrel)', 'steel plate, cylindrical, about 1.5 m diameter and 4 m long', 'the pressure '
             'vessel that holds the water and steam'],
            ['Fire box', 'copper or steel, of rectangular section inside the shell at the front',
             'the combustion space; surrounded by water on five sides, so the heat is absorbed'],
            ['Fire grate', 'cast iron bars at the bottom of the firebox', 'carries the burning coal, and the '
             'air comes up through it'],
            ['Fire tubes (about 150–250 tubes)', 'steel tubes of 50–70 mm diameter through the barrel',
             'the hot gases pass through them and heat the surrounding water'],
            ['Smoke box and chimney', 'at the rear end of the barrel', 'collects the gas and takes it away; '
             'the blast pipe makes the draught'],
            ['Steam dome', 'on top of the barrel', 'collects dry steam and keeps the droplets below'],
            ['Safety valve, water gauge, pressure gauge', 'mountings on the shell', 'protect the boiler and '
             'show the water level and pressure'],
            ['Regulator and steam pipe', 'from the dome to the cylinders', 'controls the steam to the engine'],
        ]),
        figure(fig.locomotive_boiler(),
               'Fig. 3.2 · Locomotive boiler — fire box, grate, combustion chamber, fire tubes, smoke box, '
               'dome, safety valve and steam pipe to the cylinders.'),
        h4('Working — step and reason'),
        steps(('Step 1', 'Coal is burnt on the grate in the fire box. Reason: the fire box has a large '
                         'radiant surface, so a lot of heat is transferred to the water around it.'),
              ('Step 2', 'The hot gases pass from the firebox through the combustion chamber and then '
                         'through the fire tubes to the smoke box. Reason: passing through many small tubes '
                         'gives a large heating surface in a short length, which is why the boiler is '
                         'compact.'),
              ('Step 3', 'The gases leave up the chimney, and the exhaust steam from the cylinders is blown '
                         'up the chimney through the blast pipe. Reason: the blast creates a partial vacuum '
                         'in the smoke box, which pulls the air through the grate — the draught is free and '
                         'needs no fan.'),
              ('Step 4', 'Water in the shell absorbs the heat and boils, and steam collects in the steam '
                         'space and the dome. Reason: the dome is raised above the water level, so any '
                         'droplets fall back and dry steam goes to the cylinders.'),
              ('Step 5', 'Feed water is added through the feed check valve and the level is watched in the '
                         'water gauge. Reason: a low water level would uncover the firebox crown, which '
                         'would collapse — the most dangerous failure of this boiler.')),
        h4('Worked example — evaporation rate'),
        p('A locomotive boiler has a heating surface of 120 m<sup>2</sup> and a coal firing rate of 1.2 t/h '
          'of coal of calorific value 30 MJ/kg. If the overall efficiency is 70 %, find the steam produced '
          'per hour, taking h<sub>g</sub> − h<sub>f,feed</sub> = 2400 kJ/kg.'),
        work('Given: heating surface = 120 m<sup>2</sup> · coal = 1.2 t/h = 1200 kg/h · CV = 30 000 kJ/kg · '
             'η = 0.70 · heat per kg steam = 2400 kJ/kg',
             'Heat available = m<sub>coal</sub> × CV × η = 1200 × 30 000 × 0.70',
             'Heat available = 2.52 × 10<sup>7</sup> kJ/h',
             'Steam = ' + frac('heat available', 'heat per kg of steam') + ' = '
             + frac('2.52 × 10<sup>7</sup>', '2400')),
        result('Steam produced ≈ 10 500 kg/h ≈ 10.5 t/h'),
        p('Sanity check: the evaporation rate per m<sup>2</sup> of heating surface is 10 500/120 = 87 '
          'kg/m<sup>2</sup>·h, which is high but normal for a locomotive boiler — it is designed for a '
          'forced draught and a high rate.'),
        h4('Advantages and limitations'),
        bullets('Compact, light and self-contained, with a high evaporation rate for its size, and free '
                'draught from the exhaust steam.',
                'The small water volume means steam can be raised quickly from cold — essential for a '
                'locomotive.',
                'But the small water volume is also a danger: the water level falls fast and the firebox '
                'crown can be uncovered, so the boiler is sensitive to the driver and to the feed.',
                'It cannot take more than about 15–20 bar because the shell is large, the firebox stays are '
                'highly stressed, and scale is hard to clean from the small tubes; it also cannot use coal '
                'efficiently and is limited to a single fuel bed.'),
    ),
    gu=join(
        h4('વ્યાખ્યા અને ઉપયોગ'),
        p('<b>Locomotive boiler</b> એ આડું, multi-tubular <b>fire-tube</b> boiler છે જેમાં અંદર firebox હોય, '
          'અને steam locomotive માટે બન્યું. એ compact, હલકું અને ઝડપથી વરાળ બનાવી શકે, કારણ કે આખું boiler '
          'engineના frame પર બેસીને એની સાથે ચાલે.'),
        h4('રચના — ભાગ પ્રમાણે'),
        table(['ભાગ', 'Material / આકાર', 'હેતુ'], [
            ['Shell (barrel)', 'steel plate, cylinder જેવું, લગભગ 1.5 m વ્યાસ અને 4 m લાંબું',
             'પાણી અને વરાળ રાખતું pressure vessel'],
            ['Fire box', 'copper કે steel, પહેલા છેડે shellની અંદર લંબચોરસ', 'દહનની જગ્યા; પાંચ બાજુએ પાણીથી '
             'ઘેરાયેલું, એટલે ગરમી શોષાય'],
            ['Fire grate', 'fireboxના તળિયે cast iron દાંડીઓ', 'બળતો કોલસો ઉપાડે, અને હવા એમાંથી ઉપર આવે'],
            ['Fire tubes (લગભગ 150–250)', '50–70 mm વ્યાસની steel tube barrelમાંથી', 'ગરમ gas એમાંથી પસાર થઈને '
             'આસપાસનું પાણી ગરમ કરે'],
            ['Smoke box અને chimney', 'barrelના પાછળના છેડે', 'gas એકઠું કરીને દૂર લઈ જાય; blast pipe draught '
             'બનાવે'],
            ['Steam dome', 'barrelની ઉપર', 'સૂકી વરાળ એકઠી કરે અને ટીપાં નીચે રહે'],
            ['Safety valve, water gauge, pressure gauge', 'shell પરના mounting', 'boiler બચાવે અને water '
             'level તથા pressure દેખાડે'],
            ['Regulator અને steam pipe', 'domeથી cylinder સુધી', 'engineને વરાળ નિયંત્રિત કરે'],
        ]),
        figure(fig.locomotive_boiler(),
               'Fig. 3.2 · Locomotive boiler — fire box, grate, combustion chamber, fire tubes, smoke box, '
               'dome, safety valve અને cylinder સુધીનો steam pipe.'),
        h4('કાર્ય — સ્ટેપ અને કારણ'),
        steps(('Step 1', 'Fire boxના grate પર કોલસો બળે. કારણ: fire boxની સપાટી મોટી હોવાથી radiant heat '
                         'એની આસપાસના પાણીમાં ઘણી જાય.'),
              ('Step 2', 'ગરમ gas fireboxમાંથી combustion chamber સુધી અને પછી fire tubesમાંથી smoke box સુધી '
                         'જાય. કારણ: ઘણી નાની tubeમાંથી પસાર કરવાથી ટૂંકી લંબાઈમાં મોટી heating surface '
                         'મળે, એટલે boiler compact બને.'),
              ('Step 3', 'Gas chimneyમાંથી બહાર જાય, અને cylinderમાંથી નીકળતી exhaust steam blast pipe દ્વારા '
                         'chimneyમાં ફૂંકાય. કારણ: blast smoke boxમાં આંશિક vacuum બનાવે જે grateમાંથી હવા '
                         'ખેંચે — draught મફત મળે, fan ન જોઈએ.'),
              ('Step 4', 'Shellમાંનું પાણી ગરમી લઈને ઉકળે, અને વરાળ steam space તથા domeમાં એકઠી થાય. કારણ: '
                         'dome water levelથી ઉપર હોવાથી ટીપાં નીચે પડે અને cylinderમાં સૂકી વરાળ જાય.'),
              ('Step 5', 'Feed check valve દ્વારા feed water ઉમેરાય અને water gaugeમાં level જોવાય. કારણ: '
                         'level નીચે જાય તો fireboxનું crown ખુલ્લું પડે અને પડી જાય — આ boilerની સૌથી '
                         'ખતરનાક નિષ્ફળતા.')),
        h4('ઉકેલેલું ઉદાહરણ — evaporation rate'),
        p('Locomotive boilerની heating surface 120 m<sup>2</sup> છે અને કલાકે 1.2 t કોલસો બળે છે જેની '
          'calorific value 30 MJ/kg છે. Overall efficiency 70 % અને h<sub>g</sub> − h<sub>f,feed</sub> = '
          '2400 kJ/kg લઈને કલાકની વરાળ શોધો.'),
        work('Given: heating surface = 120 m<sup>2</sup> · કોલસો = 1.2 t/h = 1200 kg/h · CV = 30 000 kJ/kg · '
             'η = 0.70 · પ્રતિ kg વરાળ heat = 2400 kJ/kg',
             'ઉપલબ્ધ heat = m<sub>coal</sub> × CV × η = 1200 × 30 000 × 0.70',
             'ઉપલબ્ધ heat = 2.52 × 10<sup>7</sup> kJ/h',
             'વરાળ = ' + frac('ઉપલબ્ધ heat', 'પ્રતિ kg વરાળ heat') + ' = '
             + frac('2.52 × 10<sup>7</sup>', '2400')),
        result('ઉત્પન્ન વરાળ ≈ 10 500 kg/h ≈ 10.5 t/h'),
        p('Sanity check: પ્રતિ m<sup>2</sup> heating surface evaporation 10 500/120 = 87 kg/m<sup>2</sup>·h છે, '
          'જે ઊંચું પણ locomotive boiler માટે સામાન્ય છે — એ forced draught અને ઊંચા દર માટે બન્યું છે.'),
        h4('ફાયદા અને મર્યાદાઓ'),
        bullets('Compact, હલકું અને self-contained, કદ પ્રમાણે ઊંચો evaporation rate, અને exhaust steamથી '
                'મફત draught.',
                'પાણીનું ઓછું volume એટલે ઠંડાથી ઝડપથી વરાળ ઊપડે — locomotive માટે જરૂરી.',
                'પણ એ જ ઓછું volume ખતરો પણ છે: water level ઝડપથી ઘટે અને fireboxનું crown ખુલ્લું પડે, એટલે '
                'boiler driver અને feed પ્રત્યે સંવેદનશીલ.',
                'Shell મોટું હોવાથી લગભગ 15–20 barથી વધુ pressure ઝીલી ન શકે, fireboxના stays પર ઘણો stress '
                'પડે, અને નાની tubeમાંથી scale સાફ કરવું મુશ્કેલ; કોલસાનો ઉપયોગ પણ કાર્યક્ષમ નથી અને એક જ '
                'fuel bed સુધી મર્યાદિત.'),
    ),
))

Q3['cards'].append(dict(
    number='Q.3 (a)', marks=3, tag='OR', q='List the factors affecting selection of boiler.',
    en=join(
        p('Choosing a boiler means matching its design to the duty and to the site. The factors that '
          'decide the choice:'),
        table(['Factor', 'What it decides'], [
            ['<b>Steam demand and its variation</b>', 'the capacity in kg/h and whether the load is steady '
             'or fluctuating — a fluctuating load needs a larger water volume (fire-tube)'],
            ['<b>Working pressure and temperature</b>', 'above about 20 bar a water-tube boiler is needed; '
             'superheat if the steam drives a turbine'],
            ['<b>Fuel available and its cost</b>', 'coal, oil, gas or biomass decides the furnace and the '
             'grate type; a cheap local fuel can pay for a less efficient boiler'],
            ['<b>Efficiency and running cost</b>', 'the boiler with an economiser and air preheater costs '
             'more but saves fuel every day'],
            ['<b>Floor area and headroom</b>', 'a packaged water-tube unit is tall; a Lancashire boiler needs '
             'a long brick setting'],
            ['<b>Feed water quality</b>', 'hard water needs a bigger blow-down and easier cleaning, so '
             'large-tube designs are preferred'],
            ['<b>Load factor and stand-by</b>', 'whether one spare boiler must be kept, and how the load is '
             'shared between units'],
            ['<b>Safety, code and statutory limits</b>', 'IBR registration, the pressure part class, and '
             'the operator skill available'],
            ['<b>Initial cost against life cost</b>', 'capital cost, erection, and the 15–20 year running '
             'cost have to be compared, not the price tag alone'],
        ]),
        p('<b>Example:</b> a plant needing 20 t/h of steam at 45 bar for a turbine must use a water-tube '
          'boiler with a superheater and an economiser, whatever the fuel; a small plant needing 2 t/h at '
          '7 bar for process heating is better served by a packaged fire-tube boiler because it is cheap '
          'and simple.'),
    ),
    gu=join(
        p('Boiler પસંદ કરવો એટલે એનું design કામ અને site સાથે મેળવવું. પસંદગી નક્કી કરતાં પરિબળો:'),
        table(['પરિબળ', 'શું નક્કી કરે'], [
            ['<b>Steamની માંગ અને એનો ફેરફાર</b>', 'kg/hમાં ક્ષમતા અને load સ્થિર છે કે બદલાય છે — બદલાતા '
             'load માટે મોટું water volume (fire-tube) જોઈએ'],
            ['<b>Working pressure અને temperature</b>', 'લગભગ 20 barથી ઉપર water-tube જરૂરી; turbine ચલાવવા '
             'માટે superheat'],
            ['<b>ઉપલબ્ધ fuel અને એનો ખર્ચ</b>', 'કોલસો, oil, gas કે biomass furnace અને grateનો પ્રકાર નક્કી '
             'કરે; સસ્તું સ્થાનિક fuel ઓછી efficiency ભોગવી લે'],
            ['<b>Efficiency અને running cost</b>', 'economiser તથા air preheater વાળું boiler મોંઘું પડે પણ '
             'રોજ fuel બચાવે'],
            ['<b>Floor area અને ઊંચાઈ</b>', 'packaged water-tube ઊંચું હોય; Lancashire boilerને લાંબું brick '
             'setting જોઈએ'],
            ['<b>Feed waterની ગુણવત્તા</b>', 'hard પાણીમાં વધુ blow-down અને સહેલી સફાઈ જોઈએ, એટલે મોટી tube '
             'વાળું design પસંદ'],
            ['<b>Load factor અને stand-by</b>', 'એક spare boiler રાખવું પડે કે નહીં, અને load કેવી રીતે વહેંચાય'],
            ['<b>સલામતી, code અને કાયદેસર મર્યાદા</b>', 'IBR registration, pressure partનો વર્ગ, અને ઉપલબ્ધ '
             'operatorની કુશળતા'],
            ['<b>Initial cost સામે life cost</b>', 'capital cost, erection અને 15–20 વર્ષનો running cost '
             'સરખાવવો પડે, ફક્ત ભાવ નહીં'],
        ]),
        p('<b>ઉદાહરણ:</b> turbine માટે 45 bar પર 20 t/h વરાળ જોઈએ તો fuel ગમે તે હોય, superheater અને '
          'economiser સાથે water-tube boiler જ જોઈએ; process heating માટે 7 bar પર 2 t/h જોઈએ તો packaged '
          'fire-tube boiler સસ્તું અને સાદું હોવાથી સારું.'),
    ),
))

Q3['cards'].append(dict(
    number='Q.3 (b)', marks=4, tag='OR', q='Classify steam generators and explain any one.',
    en=join(
        h4('Classification'),
        table(['Basis', 'Types', 'Examples'], [
            ['<b>By the position of the water and the gas</b>', 'fire-tube · water-tube',
             'locomotive, Lancashire / Babcock and Wilcox, Stirling'],
            ['<b>By the axis</b>', 'horizontal · vertical', 'Lancashire and B&W horizontal; vertical '
             'cross-tube'],
            ['<b>By the number of tubes</b>', 'single-tube · multi-tube', 'Cornish (single flue) / '
             'locomotive and B&W'],
            ['<b>By the firing</b>', 'internally fired · externally fired', 'locomotive (internal firebox) / '
             'Lancashire (external grate)'],
            ['<b>By the draught</b>', 'natural draught · forced draught · induced draught · balanced',
             'Lancashire natural / packaged unit with FD and ID fans'],
            ['<b>By the pressure</b>', 'low (up to 20 bar) · medium (20–60 bar) · high (above 60 bar; '
             'supercritical)', 'Lancashire / B&W / once-through supercritical'],
            ['<b>By the circulation</b>', 'natural circulation · forced circulation · once-through',
             'B&W natural / forced circulation boiler / Benson and once-through'],
            ['<b>By the use</b>', 'stationary · portable or mobile', 'power plant / locomotive and marine'],
        ]),
        h4('One type explained — the Babcock and Wilcox boiler (water-tube)'),
        p('The <b>Babcock and Wilcox</b> boiler is a horizontal, multi-tubular, water-tube boiler with '
          'natural circulation, and it is the classic industrial water-tube design.'),
        table(['Part', 'Purpose'], [
            ['Steam and water drum', 'the horizontal drum on top; separates steam and holds the water level'],
            ['Water tubes (inclined at 10–15°)', 'the water is inside; the incline helps natural '
             'circulation'],
            ['Headers (upper and lower)', 'connect the tubes to the drum and make the circulation loop'],
            ['Furnace and grate', 'below the tube bank; the gas rises across the tubes'],
            ['Baffles', 'make the gas travel in a zig-zag across the tubes, so it gives up more heat'],
            ['Superheater', 'in the gas path before the outlet, to superheat the steam'],
            ['Economiser and air preheater', 'in the gas path after the tube bank, to recover the waste '
             'heat'],
        ]),
        h4('Working — step and reason'),
        steps(('Step 1', 'Coal burns on the grate and the hot gas rises. Reason: the furnace is below the '
                         'tube bank, so the gas must cross the tubes on its way out.'),
              ('Step 2', 'The gas is made to zig-zag by the baffles. Reason: a longer path and a higher gas '
                         'velocity across the tubes raise the heat transfer.'),
              ('Step 3', 'Water in the inclined tubes absorbs the heat and becomes a steam–water mixture, '
                         'which rises to the drum. Reason: the mixture is lighter than the water in the '
                         'down-comers, so natural circulation sets up without a pump.'),
              ('Step 4', 'Steam is separated in the drum and drawn off; the water returns down the rear '
                         'tubes. Reason: a continuous circulation keeps the tube metal cool and prevents '
                         'overheating.'),
              ('Step 5', 'The gas finally passes the economiser and the air preheater. Reason: the feed '
                         'water and the combustion air are preheated, which raises the overall efficiency '
                         'by 5–8 %.')),
        h4('Advantages and limitations'),
        bullets('It can take high pressure (up to about 60 bar) because the tubes are small in diameter, '
                'and it can be built very large — 100 t/h and more.',
                'The heating surface is large for the floor area, the tubes can be replaced individually, '
                'and the boiler can be dismantled and transported in parts.',
                'But it needs pure feed water, because scale in small tubes causes rapid overheating; it '
                'needs more skilled operation and more auxiliaries (fans, pumps), and the initial cost is '
                'higher than a fire-tube boiler.'),
    ),
    gu=join(
        h4('વર્ગીકરણ'),
        table(['આધાર', 'પ્રકાર', 'ઉદાહરણ'], [
            ['<b>પાણી અને gasની જગ્યા પ્રમાણે</b>', 'fire-tube · water-tube',
             'locomotive, Lancashire / Babcock and Wilcox, Stirling'],
            ['<b>અક્ષ પ્રમાણે</b>', 'horizontal · vertical', 'Lancashire અને B&W horizontal; vertical '
             'cross-tube'],
            ['<b>Tubeની સંખ્યા પ્રમાણે</b>', 'single-tube · multi-tube', 'Cornish (એક flue) / locomotive '
             'અને B&W'],
            ['<b>Firing પ્રમાણે</b>', 'internally fired · externally fired', 'locomotive (અંદર firebox) / '
             'Lancashire (બહાર grate)'],
            ['<b>Draught પ્રમાણે</b>', 'natural · forced · induced · balanced',
             'Lancashire natural / FD અને ID fan વાળું packaged unit'],
            ['<b>Pressure પ્રમાણે</b>', 'low (20 bar સુધી) · medium (20–60 bar) · high (60 barથી ઉપર; '
             'supercritical)', 'Lancashire / B&W / once-through supercritical'],
            ['<b>Circulation પ્રમાણે</b>', 'natural · forced · once-through',
             'B&W natural / forced circulation / Benson once-through'],
            ['<b>ઉપયોગ પ્રમાણે</b>', 'stationary · portable કે mobile', 'power plant / locomotive અને marine'],
        ]),
        h4('એક પ્રકાર વિગતે — Babcock and Wilcox boiler (water-tube)'),
        p('<b>Babcock and Wilcox</b> boiler આડું, multi-tubular water-tube boiler છે જેમાં natural circulation '
          'હોય, અને ઔદ્યોગિક water-tube designનું classic ઉદાહરણ છે.'),
        table(['ભાગ', 'હેતુ'], [
            ['Steam અને water drum', 'ઉપરનું આડું drum; વરાળ અલગ કરે અને water level રાખે'],
            ['Water tubes (10–15° નમેલી)', 'પાણી અંદર; નમણાઈ natural circulationમાં મદદ કરે'],
            ['Header (ઉપર અને નીચે)', 'tubeને drum સાથે જોડે અને circulation loop બનાવે'],
            ['Furnace અને grate', 'tube bankની નીચે; gas ઉપર ચઢીને tube પાર કરે'],
            ['Baffle', 'gasને zig-zag ચલાવે જેથી વધુ heat આપે'],
            ['Superheater', 'outlet પહેલાં gas pathમાં, વરાળ superheat કરવા'],
            ['Economiser અને air preheater', 'tube bank પછી gas pathમાં, waste heat વાપરવા'],
        ]),
        h4('કાર્ય — સ્ટેપ અને કારણ'),
        steps(('Step 1', 'Grate પર કોલસો બળે અને ગરમ gas ઉપર જાય. કારણ: furnace tube bankની નીચે હોવાથી gasે '
                         'બહાર જતાં tube પાર કરવી પડે.'),
              ('Step 2', 'Baffle gasને zig-zag ચલાવે. કારણ: લાંબો રસ્તો અને tube પર ઊંચો gas velocity heat '
                         'transfer વધારે.'),
              ('Step 3', 'નમેલી tubeમાંનું પાણી ગરમી લઈને steam–water મિશ્રણ બને અને drum સુધી ચઢે. કારણ: '
                         'મિશ્રણ down-comerના પાણી કરતાં હલકું હોય, એટલે pump વગર natural circulation '
                         'ચાલે.'),
              ('Step 4', 'Drumમાં વરાળ અલગ થાય અને લેવાય; પાણી પાછળની tubeમાંથી નીચે જાય. કારણ: સતત '
                         'circulation tubeની ધાતુ ઠંડી રાખે અને overheat અટકાવે.'),
              ('Step 5', 'Gas છેવટે economiser અને air preheaterમાંથી પસાર થાય. કારણ: feed water અને '
                         'combustion air પહેલેથી ગરમ થવાથી overall efficiency 5–8 % વધે.')),
        h4('ફાયદા અને મર્યાદાઓ'),
        bullets('Tubeનો વ્યાસ નાનો હોવાથી લગભગ 60 bar સુધી pressure ઝીલે, અને 100 t/hથી વધુ ક્ષમતા સુધી '
                'બની શકે.',
                'Floor area પ્રમાણે heating surface મોટી, tube એક-એક બદલી શકાય, અને boiler ભાગોમાં તોડીને '
                'વાહનમાં લઈ જઈ શકાય.',
                'પણ શુદ્ધ feed water જરૂરી, કારણ કે નાની tubeમાં scale ઝડપથી overheat કરે; વધુ કુશળ '
                'operation અને વધુ auxiliaries (fan, pump) જોઈએ, અને initial cost fire-tube કરતાં વધુ.'),
    ),
))

Q3['cards'].append(dict(
    number='Q.3 (c)', marks=7, tag='OR', q='Explain construction and working of Lancashire boiler with sketch',
    en=join(
        h4('Definition'),
        p('The <b>Lancashire boiler</b> is a horizontal, stationary, <b>fire-tube</b> boiler with two large '
          'internal flues and an external furnace. It is the classic low-pressure industrial boiler for '
          'steady steam demand, and it is still found in process plants and in sugar and textile mills.'),
        h4('Construction — part by part'),
        table(['Part', 'Description', 'Purpose'], [
            ['Shell', 'horizontal cylindrical steel shell, 2–3 m diameter and 7–9 m long',
             'holds the water and steam under pressure'],
            ['Furnace grate (external)', 'at the front, outside the shell, in a brick chamber',
             'the coal burns here and the hot gas enters the flues'],
            ['Fire brick and baffle (fire bridge)', 'a brick wall at the end of the grate',
             'turns the gas down into the flue and stops the fuel being drawn in'],
            ['First flue (internal)', 'a large corrugated steel tube through the lower part of the shell',
             'carries the hot gas from the grate to the back and heats the water around it'],
            ['Second flue (internal)', 'a second tube above the first, running back to the front',
             'returns the gas to the front, so the heating surface is doubled'],
            ['Smoke box and chimney', 'at the front after the second flue', 'collects the gas and creates '
             'the natural draught'],
            ['Dome and safety valve on the shell', 'on top', 'collects dry steam and relieves excess '
             'pressure'],
            ['Mountings: water gauge, pressure gauge, feed check valve, blow-down', 'on the shell',
             'show and control the level, pressure, feed and the dissolved solids'],
            ['Brick setting', 'around the shell', 'insulates the boiler and forms the gas passages'],
        ]),
        figure(fig.lancashire_boiler(),
               'Fig. 3.3 · Lancashire boiler — grate and furnace, first and second flue, smoke box, '
               'chimney, dome, safety valve, feed water and blow-down.'),
        h4('Working — step and reason'),
        steps(('Step 1', 'Coal is burnt on the grate in the external furnace. Reason: the brick furnace '
                         'allows a long flame and a cheap fuel, and the flame does not touch the cold shell '
                         'directly.'),
              ('Step 2', 'The hot gas passes down the first flue to the back of the boiler. Reason: the flue '
                         'is surrounded by water, so heat is transferred along its whole length, and the '
                         'corrugations give extra surface and allow for expansion.'),
              ('Step 3', 'At the back the gas turns and travels forward through the second flue. Reason: the '
                         'return pass doubles the heating surface, so more heat is taken from the same gas.'),
              ('Step 4', 'The gas leaves through the smoke box to the chimney. Reason: the chimney gives the '
                         'natural draught that pulls the air through the grate.'),
              ('Step 5', 'Water boils and steam collects in the dome; feed is added and the level is watched. '
                         'Reason: the large water volume stores heat, so the boiler rides out a fluctuating '
                         'steam demand.')),
        h4('Worked example — efficiency by the indirect method'),
        p('A Lancashire boiler burns 800 kg/h of coal of calorific value 25 MJ/kg. The flue gas carries '
          'away 12 % of the heat, the water vapour in the gas 5 %, radiation and unburnt losses 6 %. '
          'Find the boiler efficiency and the steam raised, taking h<sub>g</sub> − h<sub>feed</sub> = 2300 '
          'kJ/kg.'),
        work('Given: coal = 800 kg/h · CV = 25 000 kJ/kg · flue loss = 12 % · vapour loss = 5 % · '
             'radiation and unburnt = 6 % · heat per kg steam = 2300 kJ/kg',
             'Total loss = 12 + 5 + 6 = 23 %',
             'Efficiency η = 100 − 23 = 77 %',
             'Heat to steam = 800 × 25 000 × 0.77 = 1.54 × 10<sup>7</sup> kJ/h',
             'Steam = ' + frac('1.54 × 10<sup>7</sup>', '2300') + ' kg/h'),
        result('Efficiency = 77 %; steam raised ≈ 6700 kg/h ≈ 6.7 t/h'),
        p('Sanity check: 6.7 t/h from 0.8 t/h of coal is about 8.4 kg of steam per kg of coal — a normal '
          'figure for a Lancashire boiler.'),
        h4('Advantages and limitations'),
        bullets('Simple, robust and cheap to build and repair, with a large water and steam storage, so it '
                'answers a fluctuating load well. It can burn cheap fuel on a large grate.',
                'The gas path is long and the boiler is easy to clean through the flues, which matters with '
                'moderately hard water.',
                'But it is very heavy for its output, it needs a large brick setting and a big floor area, '
                'and it cannot be moved once erected.',
                'It is limited to about 15–20 bar because the shell is large, it is slow to raise steam '
                'from cold, and the efficiency is lower than a modern water-tube boiler because the exit '
                'gas is hot.'),
    ),
    gu=join(
        h4('વ્યાખ્યા'),
        p('<b>Lancashire boiler</b> એ આડું, stationary <b>fire-tube</b> boiler છે જેમાં બે મોટા અંદરના flue અને '
          'બહારનું furnace હોય. સ્થિર steam માંગ માટેનું આ classic low-pressure ઔદ્યોગિક boiler છે, અને '
          'process plant તથા ખાંડ-કાપડની millમાં આજે પણ જોવા મળે.'),
        h4('રચના — ભાગ પ્રમાણે'),
        table(['ભાગ', 'વર્ણન', 'હેતુ'], [
            ['Shell', 'આડું cylindrical steel shell, 2–3 m વ્યાસ અને 7–9 m લાંબું', 'pressureમાં પાણી અને વરાળ '
             'રાખે'],
            ['Furnace grate (બહાર)', 'આગળના ભાગે, shellની બહાર, brick chamberમાં', 'કોલસો અહીં બળે અને ગરમ gas '
             'flueમાં જાય'],
            ['Fire brick અને baffle (fire bridge)', 'grateના છેડે ઈંટની દીવાલ', 'gasને નીચે flueમાં વાળે અને fuel '
             'ખેંચાતું અટકાવે'],
            ['પહેલો flue (અંદરનો)', 'shellના નીચેના ભાગમાંથી જતી મોટી corrugated steel tube',
             'grateથી પાછળ સુધી ગરમ gas લઈ જાય અને આસપાસનું પાણી ગરમ કરે'],
            ['બીજો flue (અંદરનો)', 'પહેલાથી ઉપર બીજી tube, આગળ સુધી પાછી', 'gasને આગળ પાછી લાવે, એટલે heating '
             'surface બમણી થાય'],
            ['Smoke box અને chimney', 'બીજા flue પછી આગળ', 'gas એકઠું કરે અને natural draught બનાવે'],
            ['Shell પર dome અને safety valve', 'ઉપર', 'સૂકી વરાળ એકઠી કરે અને વધુ pressure કાઢે'],
            ['Mounting: water gauge, pressure gauge, feed check valve, blow-down', 'shell પર',
             'level, pressure, feed અને dissolved solids દેખાડે તથા નિયંત્રિત કરે'],
            ['Brick setting', 'shellની આસપાસ', 'boiler ગરમ રાખે અને gasના રસ્તા બનાવે'],
        ]),
        figure(fig.lancashire_boiler(),
               'Fig. 3.3 · Lancashire boiler — grate અને furnace, પહેલો તથા બીજો flue, smoke box, chimney, '
               'dome, safety valve, feed water અને blow-down.'),
        h4('કાર્ય — સ્ટેપ અને કારણ'),
        steps(('Step 1', 'બહારના furnaceમાં grate પર કોલસો બળે. કારણ: ઈંટનું furnace લાંબી જ્યોત અને સસ્તું '
                         'fuel દે, અને જ્યોત ઠંડા shellને સીધી અડતી નથી.'),
              ('Step 2', 'ગરમ gas પહેલા flueમાંથી boilerના પાછળના ભાગ સુધી જાય. કારણ: flue ચારે બાજુ પાણીથી '
                         'ઘેરાયેલી હોવાથી આખી લંબાઈમાં heat જાય, અને corrugation વધુ surface આપે તથા '
                         'expansion સહે.'),
              ('Step 3', 'પાછળ gas વળીને બીજા flueમાંથી આગળ આવે. કારણ: પાછો pass heating surface બમણી કરે, '
                         'એટલે એ જ gasમાંથી વધુ heat નીકળે.'),
              ('Step 4', 'Gas smoke box થઈને chimneyમાં જાય. કારણ: chimney natural draught આપે જે grateમાંથી '
                         'હવા ખેંચે.'),
              ('Step 5', 'પાણી ઉકળે અને domeમાં વરાળ એકઠી થાય; feed ઉમેરાય અને level જોવાય. કારણ: પાણીનું '
                         'મોટું volume ગરમી સંઘરે, એટલે boiler બદલાતી steam માંગ સહેલાઈથી ઝીલે.')),
        h4('ઉકેલેલું ઉદાહરણ — indirect રીતે efficiency'),
        p('Lancashire boiler કલાકે 800 kg કોલસો બાળે છે જેની calorific value 25 MJ/kg છે. Flue gas 12 %, gasમાંની '
          'વરાળ 5 %, radiation અને unburnt 6 % heat લઈ જાય છે. Boilerની efficiency અને બનતી વરાળ શોધો; '
          'h<sub>g</sub> − h<sub>feed</sub> = 2300 kJ/kg લો.'),
        work('Given: કોલસો = 800 kg/h · CV = 25 000 kJ/kg · flue loss = 12 % · vapour loss = 5 % · '
             'radiation અને unburnt = 6 % · પ્રતિ kg વરાળ heat = 2300 kJ/kg',
             'કુલ loss = 12 + 5 + 6 = 23 %',
             'Efficiency η = 100 − 23 = 77 %',
             'વરાળમાં ગયેલી heat = 800 × 25 000 × 0.77 = 1.54 × 10<sup>7</sup> kJ/h',
             'વરાળ = ' + frac('1.54 × 10<sup>7</sup>', '2300') + ' kg/h'),
        result('Efficiency = 77 %; બનતી વરાળ ≈ 6700 kg/h ≈ 6.7 t/h'),
        p('Sanity check: 0.8 t/h કોલસામાંથી 6.7 t/h વરાળ એટલે પ્રતિ kg કોલસે લગભગ 8.4 kg વરાળ — Lancashire '
          'boiler માટે સામાન્ય આંકડો.'),
        h4('ફાયદા અને મર્યાદાઓ'),
        bullets('સાદું, મજબૂત અને બનાવવા-સમારવા સસ્તું, પાણી અને વરાળનો મોટો સંગ્રહ એટલે બદલાતો load સારી રીતે '
                'ઝીલે. મોટા grate પર સસ્તું fuel બળી શકે.',
                'Gasનો રસ્તો લાંબો અને flueમાંથી સફાઈ સહેલી, જે થોડું hard પાણી હોય ત્યારે મહત્ત્વનું.',
                'પણ ઉત્પાદન પ્રમાણે ખૂબ ભારે, મોટું brick setting અને મોટી જગ્યા જોઈએ, અને એક વાર ઊભું કર્યા '
                'પછી ખસેડી શકાય નહીં.',
                'Shell મોટું હોવાથી લગભગ 15–20 bar સુધી મર્યાદિત, ઠંડાથી વરાળ ઊપડવામાં ધીમું, અને બહાર '
                'જતો gas ગરમ હોવાથી આધુનિક water-tube boiler કરતાં efficiency ઓછી.'),
    ),
))


# ---------------------------------------------------------------- Q4
Q4 = {
    'title_en': 'Q4 · Compressors, economiser, steam trap, boiler accessories and mountings',
    'title_gu': 'પ્ર.4 · કોમ્પ્રેસર, ઇકોનોમાઇઝર, સ્ટીમ ટ્રેપ, બોઈલર એસેસરીઝ અને માઉન્ટિંગ્સ',
    'cards': [],
}

Q4['cards'].append(dict(
    number='Q.4 (a)', marks=3, q='Draw a neat Figure of Rotary compressors',
    en=join(
        p('A <b>rotary compressor</b> is a positive-displacement or dynamic machine in which the air is '
          'compressed by the rotation of a rotor inside a casing, without any reciprocating piston. The '
          'two common positive-displacement types are the <b>sliding-vane</b> and the <b>twin-screw</b>.'),
        figure(ufig.rotary_compressor(),
               'Fig. 4.1 · Rotary compressors — sliding vane (eccentric rotor with vanes) and twin screw '
               '(two intermeshing rotors in a casing).'),
        h4('Labelled parts'),
        table(['Type', 'Parts', 'How the air is compressed'], [
            ['Sliding vane', 'casing, eccentric rotor, radial vanes, inlet port, outlet port',
             'the rotor is off-centre, so the space between two vanes shrinks as it turns from the inlet '
             'to the outlet'],
            ['Twin screw', 'casing, male (4-lobe) rotor, female (6-lobe) rotor, inlet and outlet ports',
             'the meshing rotors trap a pocket of air and reduce its volume as the pocket moves axially '
             'to the outlet'],
        ]),
        p('<b>Note:</b> a rotary compressor gives a steady, pulse-free delivery and is compact, which is '
          'why it is used for instrument air and for large flows at moderate pressure.'),
    ),
    gu=join(
        p('<b>Rotary compressor</b> એ positive-displacement કે dynamic machine છે જેમાં casingની અંદર rotorના '
          'ફરવાથી હવા compress થાય, કોઈ reciprocating piston વગર. સામાન્ય positive-displacement પ્રકારો '
          '<b>sliding-vane</b> અને <b>twin-screw</b> છે.'),
        figure(ufig.rotary_compressor(),
               'Fig. 4.1 · Rotary compressors — sliding vane (eccentric rotor અને vanes) અને twin screw '
               '(casingમાં બે intermeshing rotor).'),
        h4('લેબલ કરેલા ભાગ'),
        table(['પ્રકાર', 'ભાગ', 'હવા કેવી રીતે compress થાય'], [
            ['Sliding vane', 'casing, eccentric rotor, radial vane, inlet port, outlet port',
             'rotor off-centre હોવાથી બે vane વચ્ચેની જગ્યા inletથી outlet સુધી ફરતાં ઘટે'],
            ['Twin screw', 'casing, male (4-lobe) rotor, female (6-lobe) rotor, inlet અને outlet port',
             'meshing rotor હવાનું ખિસ્સું ફસાવે અને outlet સુધી જતાં એનું volume ઘટાડે'],
        ]),
        p('<b>નોંધ:</b> Rotary compressor સ્થિર, pulse વગરનો પુરવઠો આપે અને compact હોય, એટલે instrument air '
          'તથા મધ્યમ pressure પર મોટા flow માટે વપરાય.'),
    ),
))

Q4['cards'].append(dict(
    number='Q.4 (b)', marks=4, q='Explain economizer and steam trap',
    en=join(
        h4('Economiser'),
        p('An <b>economiser</b> is a heat exchanger placed in the flue-gas path after the boiler, in which '
          'the feed water is heated by the leaving flue gas. It is called an economiser because it '
          'economises fuel: every 6 °C rise in feed water temperature saves about 1 % of the fuel.'),
        table(['Part', 'Purpose'], [
            ['Cast-iron or steel gilled tubes in a bank', 'give the large surface needed to take heat from a '
             'gas that is only 250–400 °C'],
            ['Headers and return bends', 'connect the tubes and let the water travel up and down in passes'],
            ['Soot blowers', 'blow the soot off the gas side, because a soot layer of 1 mm can cut the '
             'heat transfer by 10 %'],
            ['Bypass duct and damper', 'protect the economiser during start-up, when the gas is wet and '
             'corrosive'],
            ['Safety valve and vent on the water side', 'protect the economiser if the feed is stopped while '
             'the gas is still hot'],
        ]),
        figure(ufig.economizer_trap(),
               'Fig. 4.2 · Economiser tubes in the gas path, and a steam trap on a steam line.'),
        h4('Working of the economiser'),
        steps(('Step 1', 'Feed water from the pump enters at the bottom and flows up through the tubes. '
                         'Reason: counter-flow gives the best heat transfer, so the warmest water meets the '
                         'hottest gas.'),
              ('Step 2', 'The flue gas passes outside the tubes at 250–400 °C. Reason: the gas is still hot '
                         'enough to heat the water but too cool to be useful in the furnace.'),
              ('Step 3', 'The feed water leaves 40–60 °C hotter and enters the drum. Reason: this heat would '
                         'otherwise have gone up the chimney, so less fuel is burnt for the same steam.')),
        h4('Steam trap'),
        p('A <b>steam trap</b> is an automatic valve that lets condensate, air and other non-condensable '
          'gases out of a steam line or a steam-heated equipment, but holds back the live steam. Without '
          'it, condensate collects at the bottom of the line, causes water hammer, and reduces the '
          'heating; if it were simply a hole, steam would escape and be wasted.'),
        table(['Type', 'How it works', 'Use'], [
            ['Thermodynamic', 'a disc closes on the flash steam that forms as the condensate passes the '
             'orifice', 'main steam lines, tracing'],
            ['Ball float + thermostatic air vent', 'a float opens the valve to let the condensate out and '
             'closes on steam', 'heat exchangers and vessels with a large condensate load'],
            ['Inverted bucket', 'a bucket floats over the condensate and falls to open the valve, then '
             'fills and rises', 'high-pressure and superheated steam lines'],
            ['Thermostatic (bimetallic)', 'the expansion of a bimetallic element opens the valve in the '
             'cold condensate', 'radiators and small heaters'],
        ]),
        h4('Worked example — fuel saved by an economiser'),
        p('A boiler makes 10 t/h of steam, burning 800 kg/h of coal. The feed water enters the economiser '
          'at 40 °C and leaves at 100 °C; c<sub>p</sub> = 4.18 kJ/kg·K and coal CV = 25 MJ/kg. Find the '
          'heat recovered and the coal saved.'),
        work('Given: steam = 10 000 kg/h · feed heated from 40 °C to 100 °C · c<sub>p</sub> = 4.18 kJ/kg·K · '
             'CV = 25 000 kJ/kg',
             'Heat recovered = m · c<sub>p</sub> · ΔT = 10 000 × 4.18 × 60',
             'Heat recovered = 2.508 × 10<sup>6</sup> kJ/h',
             'Coal saved = ' + frac('heat recovered', 'CV') + ' = ' + frac('2.508 × 10<sup>6</sup>',
                                                                       '25 000') + ' kg/h'),
        result('Heat recovered ≈ 2.51 × 10<sup>6</sup> kJ/h; coal saved ≈ 100 kg/h'),
        p('Sanity check: 100 kg out of 800 kg is a saving of 12.5 %, which matches the well-known rule '
          'that a 60 °C rise saves about 10 % of the fuel.'),
        h4('Limitations'),
        bullets('An economiser works only if you keep it clean: soot on the gas side and scale on the water '
                'side both cut the saving.',
                'The gas-side tubes can drop below the dew point during start-up, and the condensation of '
                'acid is corrosive, so a bypass is needed.',
                'A steam trap that fails open wastes steam; one that fails closed floods the line. Traps '
                'therefore need routine testing, by sound, by temperature or with an ultrasonic tester.'),
    ),
    gu=join(
        h4('Economiser'),
        p('<b>Economiser</b> એ boiler પછી flue-gasના રસ્તામાં ગોઠવેલો heat exchanger છે જેમાં નીકળતા flue gas '
          'વડે feed water ગરમ થાય. એને economiser કહે છે કારણ કે એ fuel બચાવે: feed waterનું તાપમાન 6 °C વધે '
          'તો લગભગ 1 % fuel બચે.'),
        table(['ભાગ', 'હેતુ'], [
            ['Cast-iron કે steel gilled tubeની બેંક', '250–400 °Cના gasમાંથી heat લેવા મોટી surface આપે'],
            ['Header અને return bend', 'tube જોડે અને પાણી ઉપર-નીચે passમાં ફરે'],
            ['Soot blower', 'gas બાજુનો soot ઉડાડે, કારણ કે 1 mm soot heat transfer 10 % ઘટાડે'],
            ['Bypass duct અને damper', 'start-up વખતે economiser બચાવે, જ્યારે gas ભીનો અને corrosive હોય'],
            ['પાણી બાજુ safety valve અને vent', 'gas ગરમ હોય ત્યારે feed બંધ થાય તો economiser બચાવે'],
        ]),
        figure(ufig.economizer_trap(),
               'Fig. 4.2 · Gasના રસ્તામાં economiserની tube, અને steam લાઇન પર steam trap.'),
        h4('Economiserનું કાર્ય'),
        steps(('Step 1', 'Pumpમાંથી feed water નીચેથી દાખલ થઈને tubeમાં ઉપર જાય. કારણ: counter-flowમાં '
                         'સૌથી સારો heat transfer મળે, એટલે ગરમ પાણી સૌથી ગરમ gasને મળે.'),
              ('Step 2', 'Flue gas 250–400 °C પર tubeની બહાર જાય. કારણ: gas હજી પાણી ગરમ કરવા પૂરતો ગરમ છે '
                         'પણ furnaceમાં કામ લાગે એટલો નથી.'),
              ('Step 3', 'Feed water 40–60 °C વધુ ગરમ થઈને drumમાં જાય. કારણ: આ heat ન હોત તો ચીમનીમાં જ '
                         'જાત, એટલે એટલી જ વરાળ માટે ઓછો fuel બળે.')),
        h4('Steam trap'),
        p('<b>Steam trap</b> એ automatic valve છે જે steam લાઇન કે steam-heated equipmentમાંથી condensate, '
          'હવા અને બીજા non-condensable gas બહાર કાઢે, પણ જીવતી વરાળ રોકી રાખે. એના વગર condensate લાઇનના '
          'તળિયે એકઠું થઈને water hammer કરે અને heating ઘટાડે; અને ફક્ત છિદ્ર હોય તો વરાળ વેડફાય.'),
        table(['પ્રકાર', 'કેવી રીતે કામ કરે', 'ઉપયોગ'], [
            ['Thermodynamic', 'condensate orifice પાર થાય ત્યારે બનતી flash steam પર disc બંધ થાય',
             'મુખ્ય steam લાઇન, tracing'],
            ['Ball float + thermostatic air vent', 'float valve ખોલીને condensate જવા દે અને વરાળ પર બંધ '
             'થાય', 'heat exchanger અને મોટા condensate load વાળાં vessel'],
            ['Inverted bucket', 'bucket condensate પર તરે અને નીચે જઈને valve ખોલે, પછી ભરાઈને ઉપર જાય',
             'ઊંચા pressure અને superheated steam લાઇન'],
            ['Thermostatic (bimetallic)', 'ઠંડા condensateમાં bimetallic element ફેલાઈને valve ખોલે',
             'radiator અને નાના heater'],
        ]),
        h4('ઉકેલેલું ઉદાહરણ — economiserથી બચતું fuel'),
        p('Boiler કલાકે 10 t વરાળ બનાવે છે અને 800 kg કોલસો બાળે છે. Feed water economiserમાં 40 °C પર આવે '
          'અને 100 °C પર નીકળે; c<sub>p</sub> = 4.18 kJ/kg·K અને કોલસાની CV = 25 MJ/kg. પાછી મળતી heat અને '
          'બચતો કોલસો શોધો.'),
        work('Given: steam = 10 000 kg/h · feed 40 °C થી 100 °C · c<sub>p</sub> = 4.18 kJ/kg·K · '
             'CV = 25 000 kJ/kg',
             'પાછી મળતી heat = m · c<sub>p</sub> · ΔT = 10 000 × 4.18 × 60',
             'પાછી મળતી heat = 2.508 × 10<sup>6</sup> kJ/h',
             'બચતો કોલસો = ' + frac('પાછી મળતી heat', 'CV') + ' = ' + frac('2.508 × 10<sup>6</sup>',
                                                                          '25 000') + ' kg/h'),
        result('પાછી મળતી heat ≈ 2.51 × 10<sup>6</sup> kJ/h; બચતો કોલસો ≈ 100 kg/h'),
        p('Sanity check: 800 kgમાંથી 100 kg એટલે 12.5 % બચત, જે સુવિખ્યાત નિયમ સાથે મળે — 60 °C વધારો '
          'લગભગ 10 % fuel બચાવે.'),
        h4('મર્યાદાઓ'),
        bullets('Economiser ફક્ત સાફ રહે તો જ ફાયદો આપે: gas બાજુ soot અને પાણી બાજુ scale બંને બચત ઘટાડે.',
                'Start-up વખતે gas-side tube dew pointથી નીચે જાય તો acid ઘનીભવન થઈને corrosive બને, એટલે '
                'bypass જરૂરી.',
                'Steam trap ખુલ્લો રહી જાય તો વરાળ વેડફાય, બંધ થઈ જાય તો લાઇનમાં પાણી ભરાય. એટલે trap નિયમિત '
                'ચકાસવા પડે — અવાજથી, તાપમાનથી કે ultrasonic testerથી.'),
    ),
))

Q4['cards'].append(dict(
    number='Q.4 (c)', marks=7, q='Explain boiler Accessories and mountings',
    en=join(
        h4('The difference'),
        p('<b>Boiler mountings</b> are the fittings mounted <b>on</b> the boiler shell itself, and they are '
          'needed for its safe operation and for control of the steam and water — they are part of the '
          'pressure part and are covered by the boiler code. <b>Boiler accessories</b> are the auxiliary '
          'equipment installed <b>around</b> the boiler to improve its efficiency and to handle the air, '
          'gas, water and fuel; they are not pressure parts of the shell.'),
        h4('Mountings'),
        table(['Mounting', 'Function', 'Why it is compulsory'], [
            ['<b>Safety valve</b> (two, usually)', 'opens at the set pressure and lets the steam out',
             'the only protection against over-pressure and a burst boiler'],
            ['<b>Water level indicator</b> (gauge glass)', 'shows the water level in the drum',
             'a low level uncovers the heating surface and causes a collapse'],
            ['<b>Pressure gauge</b>', 'shows the steam pressure', 'the operator must know the pressure at '
             'all times'],
            ['<b>Fusible plug</b>', 'a low-melting plug in the furnace crown that melts if the water level '
             'falls', 'extinguishes the fire before the crown plate overheats'],
            ['<b>Feed check valve</b>', 'lets the feed water in and stops it flowing back',
             'protects the pump and keeps the water level'],
            ['<b>Blow-down valve / cock</b>', 'drains water from the lowest point',
             'removes the sludge and controls the dissolved solids'],
            ['<b>Steam stop valve</b>', 'isolates the boiler from the steam main', 'control and isolation '
             'for maintenance'],
            ['<b>Air vent</b>', 'lets the air out while filling and raising steam', 'air in the boiler '
             'causes corrosion and a false pressure reading'],
        ]),
        h4('Accessories'),
        table(['Accessory', 'Where it sits', 'What it does'], [
            ['<b>Economiser</b>', 'in the flue-gas path after the boiler', 'heats the feed water from the '
             'waste gas, saving 8–12 % fuel'],
            ['<b>Air preheater</b>', 'last in the gas path', 'heats the combustion air, so the furnace '
             'temperature is higher and the gas leaves cooler'],
            ['<b>Superheater</b>', 'in the gas path before the outlet', 'dries and superheats the steam for '
             'the turbine'],
            ['<b>Feed water pump</b>', 'before the economiser', 'forces the feed water into the drum '
             'against the boiler pressure'],
            ['<b>Forced / induced draught fans</b>', 'at the air inlet and after the air preheater',
             'supply the combustion air and pull the gas through the boiler'],
            ['<b>Soot blowers</b>', 'on the tube banks', 'blow the soot off the gas side, keeping the heat '
             'transfer up'],
            ['<b>Steam trap and separators</b>', 'on the steam main', 'remove the condensate and droplets '
             'before the steam reaches the turbine'],
            ['<b>Water treatment plant</b>', 'before the feed pump', 'softens or demineralises the water, '
             'which prevents scale and corrosion'],
        ]),
        h4('Working — how the two together keep the boiler safe and efficient'),
        steps(('Step 1', 'The feed pump pushes water through the economiser and the feed check valve into '
                         'the drum. Reason: the feed must overcome the boiler pressure, and the check valve '
                         'stops the back-flow when the pump stops.'),
              ('Step 2', 'The water level is watched in the gauge glass and the pressure in the gauge. '
                         'Reason: these two readings are the only direct information about the state of '
                         'the boiler.'),
              ('Step 3', 'If the level falls too far, the fusible plug melts and the safety valve and the '
                         'operator act. Reason: the plug is the last automatic defence against a furnace '
                         'explosion.'),
              ('Step 4', 'The air preheater and the fans supply hot air, the fuel burns, and the gas passes '
                         'the superheater, the tube bank, the economiser and the air preheater. Reason: '
                         'each of these takes heat from the gas before it reaches the chimney.'),
              ('Step 5', 'The blow-down valve is opened at intervals. Reason: the dissolved solids left '
                         'behind by the evaporation must be removed, or they cause priming, foaming and '
                         'scale.')),
        h4('Worked example — blow-down required'),
        p('A boiler evaporates 10 000 kg/h of water. The feed water has 400 ppm dissolved solids and the '
          'boiler water must be held at 3000 ppm. Find the blow-down rate.'),
        work('Given: evaporation = 10 000 kg/h · feed TDS = 400 ppm · boiler water limit = 3000 ppm',
             'Formula: B = ' + frac('E × S<sub>feed</sub>', 'S<sub>boiler</sub> − S<sub>feed</sub>'),
             'Substitute: B = ' + frac('10 000 × 400', '3000 − 400') + ' = ' + frac('4 × 10<sup>6</sup>',
                                                                                 '2600')),
        result('Blow-down ≈ 1538 kg/h, about 15 % of the evaporation'),
        p('Sanity check: a blow-down of 5–10 % is normal, so 15 % shows that this feed water is rather salty '
          '— which is the reason a softener or demineraliser is put before the boiler.'),
        h4('Limitations'),
        bullets('The mountings are only as good as their maintenance: a gauge glass that is isolated, a '
                'safety valve that is stuck or a fusible plug that has already melted but not been replaced '
                'gives false confidence.',
                'Accessories raise the efficiency but also add pressure drop on the gas side, and they cost '
                'money and need space; the economiser and air preheater also risk acid corrosion at '
                'start-up.',
                'A very high blow-down, used to control the solids, wastes heat — which is why water '
                'treatment is cheaper than blow-down.'),
    ),
    gu=join(
        h4('ફરક'),
        p('<b>Boiler mountings</b> એ boilerના shell <b>પર</b> બેસાડેલા fitting છે, જે સલામત operation અને વરાળ તથા '
          'પાણીના નિયંત્રણ માટે જરૂરી છે — એ pressure partનો ભાગ છે અને boiler code હેઠળ આવે. '
          '<b>Boiler accessories</b> એ boilerની <b>આસપાસ</b> ગોઠવેલા auxiliary equipment છે જે efficiency વધારે '
          'અને હવા, gas, પાણી તથા fuel સંભાળે; એ shellના pressure part નથી.'),
        h4('Mountings'),
        table(['Mounting', 'કામ', 'કેમ ફરજિયાત'], [
            ['<b>Safety valve</b> (સામાન્ય રીતે બે)', 'set pressure પર ખૂલીને વરાળ બહાર કાઢે',
             'over-pressure અને boiler ફાટવા સામે એક જ રક્ષા'],
            ['<b>Water level indicator</b> (gauge glass)', 'drumમાં water level દેખાડે',
             'level નીચે જાય તો heating surface ખુલ્લી થઈને પડી જાય'],
            ['<b>Pressure gauge</b>', 'steam pressure દેખાડે', 'operatorને દર વખતે pressure ખબર હોવી જોઈએ'],
            ['<b>Fusible plug</b>', 'furnace crownમાં નીચા melting pointનું plug, level ઘટે તો ઓગળે',
             'crown plate ગરમ થાય એ પહેલાં આગ ઓલવે'],
            ['<b>Feed check valve</b>', 'feed water અંદર જવા દે અને પાછું વહેવા ન દે', 'pump બચાવે અને water '
             'level રાખે'],
            ['<b>Blow-down valve / cock</b>', 'સૌથી નીચલા ભાગેથી પાણી કાઢે', 'sludge કાઢે અને dissolved solids '
             'નિયંત્રિત કરે'],
            ['<b>Steam stop valve</b>', 'boilerને steam mainથી અલગ કરે', 'નિયંત્રણ અને maintenance માટે '
             'isolation'],
            ['<b>Air vent</b>', 'ભરતી વખતે અને વરાળ ઊપાડતી વખતે હવા બહાર કાઢે', 'boilerમાં હવા corrosion અને ખોટું '
             'pressure વાંચન કરે'],
        ]),
        h4('Accessories'),
        table(['Accessory', 'ક્યાં બેસે', 'શું કરે'], [
            ['<b>Economiser</b>', 'boiler પછી flue-gasના રસ્તામાં', 'waste gasથી feed water ગરમ કરે, 8–12 % '
             'fuel બચાવે'],
            ['<b>Air preheater</b>', 'gasના રસ્તામાં સૌથી છેલ્લે', 'combustion air ગરમ કરે, જેથી furnaceનું '
             'તાપમાન વધે અને gas ઠંડો નીકળે'],
            ['<b>Superheater</b>', 'outlet પહેલાં gasના રસ્તામાં', 'વરાળ સૂકવીને turbine માટે superheat કરે'],
            ['<b>Feed water pump</b>', 'economiser પહેલાં', 'boilerના pressure સામે feed water ધકેલે'],
            ['<b>Forced / induced draught fan</b>', 'air inlet પર અને air preheater પછી',
             'combustion air આપે અને gasને boilerમાંથી ખેંચે'],
            ['<b>Soot blower</b>', 'tube bank પર', 'gas બાજુનો soot ઉડાડીને heat transfer ટકાવે'],
            ['<b>Steam trap અને separator</b>', 'steam main પર', 'turbine સુધી પહોંચતાં પહેલાં condensate અને '
             'ટીપાં કાઢે'],
            ['<b>Water treatment plant</b>', 'feed pump પહેલાં', 'પાણી soft કે demineralise કરે, જેથી scale અને '
             'corrosion ન થાય'],
        ]),
        h4('કાર્ય — બંને મળીને boiler સલામત અને કાર્યક્ષમ કેવી રીતે રાખે'),
        steps(('Step 1', 'Feed pump economiserમાંથી પાણી ધકેલીને feed check valve દ્વારા drumમાં મોકલે. કારણ: '
                         'feedએ boilerના pressure સામે જવું પડે, અને pump બંધ થાય ત્યારે check valve પાછું '
                         'વહેવા દે નહીં.'),
              ('Step 2', 'Water level gauge glassમાં અને pressure gaugeમાં જોવાય. કારણ: boilerની સ્થિતિની સીધી '
                         'માહિતી આ બે વાંચનથી જ મળે.'),
              ('Step 3', 'Level બહુ નીચે જાય તો fusible plug ઓગળે, અને safety valve તથા operator કામ કરે. '
                         'કારણ: furnace ફાટવા સામે plug છેલ્લો automatic બચાવ છે.'),
              ('Step 4', 'Air preheater અને fan ગરમ હવા આપે, fuel બળે, અને gas superheater, tube bank, '
                         'economiser તથા air preheaterમાંથી પસાર થાય. કારણ: chimney સુધી પહોંચતાં પહેલાં '
                         'દરેક ભાગ gasમાંથી heat લે.'),
              ('Step 5', 'Blow-down valve સમયે સમયે ખોલાય. કારણ: બાષ્પીભવનથી બાકી રહેતા dissolved solids કાઢવા '
                         'પડે, નહીં તો priming, foaming અને scale થાય.')),
        h4('ઉકેલેલું ઉદાહરણ — જરૂરી blow-down'),
        p('Boiler કલાકે 10 000 kg પાણી બાષ્પીભવન કરે છે. Feed waterમાં 400 ppm dissolved solids છે અને boilerનું '
          'પાણી 3000 ppm પર રાખવું છે. Blow-downનો દર શોધો.'),
        work('Given: evaporation = 10 000 kg/h · feed TDS = 400 ppm · boiler પાણીની મર્યાદા = 3000 ppm',
             'Formula: B = ' + frac('E × S<sub>feed</sub>', 'S<sub>boiler</sub> − S<sub>feed</sub>'),
             'Substitution: B = ' + frac('10 000 × 400', '3000 − 400') + ' = ' + frac('4 × 10<sup>6</sup>',
                                                                                   '2600')),
        result('Blow-down ≈ 1538 kg/h, એટલે evaporationના લગભગ 15 %'),
        p('Sanity check: 5–10 % blow-down સામાન્ય છે, એટલે 15 % દર્શાવે છે કે આ feed water થોડું ખારું છે — '
          'એટલે જ boiler પહેલાં softener કે demineraliser મુકાય.'),
        h4('મર્યાદાઓ'),
        bullets('Mounting એટલા જ સારા જેટલી એમની maintenance: isolation કરેલું gauge glass, અટકી ગયેલો safety '
                'valve કે પહેલેથી ઓગળેલું પણ ન બદલેલું fusible plug ખોટો ભરોસો આપે.',
                'Accessories efficiency વધારે પણ gas બાજુ pressure drop ઉમેરે, અને ખર્ચ તથા જગ્યા માગે; '
                'economiser અને air preheater start-up વખતે acid corrosionનું જોખમ પણ લાવે.',
                'Solids કાબૂમાં રાખવા ખૂબ ઊંચો blow-down વપરાય તો heat વેડફાય — એટલે જ water treatment '
                'blow-down કરતાં સસ્તું પડે.'),
    ),
))

Q4['cards'].append(dict(
    number='Q.4 (a)', marks=3, tag='OR', q='Define Compressed Air, Blower Air and Fan Air',
    en=join(
        p('These three names describe air moved by a machine, and they are separated by the <b>pressure '
          'ratio</b> the machine develops, which is also what decides the type of machine.'),
        table(['Term', 'Definition', 'Pressure rise', 'Machine used'], [
            ['<b>Fan air</b>', 'air moved at almost constant density for ventilation or for a small '
             'pressure difference', 'up to about 0.1 bar (compression ratio 1.1)', 'centrifugal or axial '
             'fan'],
            ['<b>Blower air</b>', 'air delivered at a moderate pressure, where the density still changes '
             'little', 'about 0.1–1 bar (ratio 1.1–2)', 'Roots blower, centrifugal blower'],
            ['<b>Compressed air</b>', 'air compressed to a much higher pressure and stored, so it carries '
             'energy for tools and instruments', 'above 1 bar, typically 6–10 bar (ratio 3–10)',
             'reciprocating, rotary screw or centrifugal compressor'],
        ]),
        p('<b>Example:</b> a cooling tower uses a <b>fan</b> to move a large volume of air at a few '
          'millibar; a sewage aeration tank uses a <b>blower</b> at about 0.6 bar; and the workshop '
          '<b>compressed air</b> line runs at 7 bar to drive a pneumatic drill. The same air, three '
          'different machines, because the pressure ratio is different.'),
        h4('Worked check — compression ratio'),
        p('Find the compression ratio for a fan that raises the pressure from 1.0 to 1.05 bar absolute, a '
          'blower to 1.8 bar absolute, and a compressor to 8 bar absolute.'),
        work('Given: P<sub>1</sub> = 1.0 bar · P<sub>fan</sub> = 1.05 bar · P<sub>blower</sub> = 1.8 bar · '
             'P<sub>compressor</sub> = 8 bar',
             'Formula: compression ratio = ' + frac('P<sub>2</sub>', 'P<sub>1</sub>'),
             'Fan = ' + frac('1.05', '1.0') + ' = 1.05',
             'Blower = ' + frac('1.8', '1.0') + ' = 1.8',
             'Compressor = ' + frac('8', '1.0') + ' = 8'),
        result('Ratios 1.05, 1.8 and 8 — which is why a fan, a blower and a compressor are different '
               'machines'),
        p('Sanity check: the usual dividing line in practice is a ratio of about 1.1 for a fan and about 2 '
          'for a blower, so the three values fall in the right bands.'),
    ),
    gu=join(
        p('આ ત્રણ નામ મશીનથી ખસેડાતી હવાને વર્ણવે છે, અને એમને મશીન જે <b>pressure ratio</b> બનાવે એ અલગ પાડે — '
          'એ જ મશીનનો પ્રકાર પણ નક્કી કરે.'),
        table(['શબ્દ', 'વ્યાખ્યા', 'Pressure rise', 'વપરાતું મશીન'], [
            ['<b>Fan air</b>', 'ventilation કે નાના pressure ફરક માટે લગભગ અચલ densityએ ખસેડાતી હવા',
             'લગભગ 0.1 bar સુધી (ratio 1.1)', 'centrifugal કે axial fan'],
            ['<b>Blower air</b>', 'મધ્યમ pressure પર પુરવઠો, જ્યાં density થોડી બદલાય',
             'લગભગ 0.1–1 bar (ratio 1.1–2)', 'Roots blower, centrifugal blower'],
            ['<b>Compressed air</b>', 'ઘણા ઊંચા pressure પર compress કરીને સંગ્રહેલી હવા, જે સાધનો અને '
             'instrument માટે energy રાખે', '1 barથી ઉપર, સામાન્ય રીતે 6–10 bar (ratio 3–10)',
             'reciprocating, rotary screw કે centrifugal compressor'],
        ]),
        p('<b>ઉદાહરણ:</b> Cooling tower થોડા millibar પર મોટું volume ખસેડવા <b>fan</b> વાપરે; sewageની '
          'aeration tank લગભગ 0.6 bar પર <b>blower</b> વાપરે; અને workshopની <b>compressed air</b> લાઇન 7 bar પર '
          'ચાલીને pneumatic drill ચલાવે. એક જ હવા, ત્રણ જુદાં મશીન, કારણ કે pressure ratio જુદું છે.'),
        h4('ઉકેલેલી ચકાસણી — compression ratio'),
        p('Fan જે pressure 1.0થી 1.05 bar absolute કરે, blower 1.8 bar absolute અને compressor 8 bar absolute '
          'કરે — દરેકનું compression ratio શોધો.'),
        work('Given: P<sub>1</sub> = 1.0 bar · P<sub>fan</sub> = 1.05 bar · P<sub>blower</sub> = 1.8 bar · '
             'P<sub>compressor</sub> = 8 bar',
             'Formula: compression ratio = ' + frac('P<sub>2</sub>', 'P<sub>1</sub>'),
             'Fan = ' + frac('1.05', '1.0') + ' = 1.05',
             'Blower = ' + frac('1.8', '1.0') + ' = 1.8',
             'Compressor = ' + frac('8', '1.0') + ' = 8'),
        result('Ratio 1.05, 1.8 અને 8 — એટલે જ fan, blower અને compressor જુદાં મશીન છે'),
        p('Sanity check: વ્યવહારમાં fan માટે લગભગ 1.1 અને blower માટે લગભગ 2ની હદ હોય, એટલે ત્રણેય કિંમત સાચા '
          'વર્ગમાં પડે.'),
    ),
))

Q4['cards'].append(dict(
    number='Q.4 (b)', marks=4, tag='OR', q='Sketch and describe the figure of super heater.',
    en=join(
        h4('Definition'),
        p('A <b>superheater</b> is a bank of tubes placed in the flue-gas path of a boiler in which the '
          'saturated steam from the drum is heated above its saturation temperature, at constant pressure. '
          'It dries the steam and raises its temperature, which raises the cycle efficiency and prevents '
          'erosion and corrosion in a turbine.'),
        figure(ufig.superheater(),
               'Fig. 4.3 · Convection superheater — serpentine coils in the gas pass, saturated steam in and '
               'superheated steam out.'),
        h4('Description'),
        table(['Part', 'Purpose'], [
            ['Serpentine coils of alloy steel tube', 'give a long path in a short space, so the steam picks '
             'up heat in a small gas pass'],
            ['Inlet header (saturated steam)', 'distributes the steam equally to all the coils'],
            ['Outlet header (superheated steam)', 'collects the steam and takes it to the turbine'],
            ['Support and spacers', 'hold the coils against vibration and thermal expansion'],
            ['Attemperator (desuperheater)', 'sprays a little water into the steam to control the final '
             'temperature, which matters for the turbine metal'],
            ['Gas baffles', 'make the gas cross the coils at the right velocity'],
        ]),
        h4('Working — step and reason'),
        steps(('Step 1', 'Saturated steam leaves the drum and enters the inlet header. Reason: the steam is '
                         'first separated from the water, because droplets would carry salts into the '
                         'superheater and scale it.'),
              ('Step 2', 'The steam passes through the serpentine coils in the hot gas stream at 600–900 °C. '
                         'Reason: the gas is hotter than the steam, so heat flows from gas to steam without '
                         'any flame touching the tube.'),
              ('Step 3', 'The steam leaves 30–60 °C above saturation. Reason: this degree of superheat is '
                         'enough to keep the last stages of the turbine dry, and the tube metal stays within '
                         'its creep limit.'),
              ('Step 4', 'The attemperator trims the outlet temperature. Reason: the gas temperature varies '
                         'with the load, and the turbine cannot accept a steam temperature above its '
                         'design value.')),
        h4('Worked example — superheat added'),
        p('Steam at 20 bar leaves the drum dry saturated at 212 °C with h<sub>g</sub> = 2799 kJ/kg. It leaves '
          'the superheater at 350 °C with h = 3060 kJ/kg, at a rate of 20 t/h. Find the heat added in the '
          'superheater.'),
        work('Given: h<sub>1</sub> = 2799 kJ/kg · h<sub>2</sub> = 3060 kJ/kg · m = 20 000 kg/h · '
             'T<sub>sat</sub> = 212 °C · T<sub>out</sub> = 350 °C',
             'Degree of superheat = 350 − 212 = 138 °C',
             'Formula: Q = m (h<sub>2</sub> − h<sub>1</sub>)',
             'Substitute: Q = 20 000 × (3060 − 2799) = 20 000 × 261'),
        result('Heat added in the superheater = 5.22 × 10<sup>6</sup> kJ/h ≈ 1450 kW'),
        p('Sanity check: 261 kJ/kg is about 10 % of the total enthalpy of the steam, which is the normal '
          'share taken by a convection superheater — correct.'),
        h4('Types and limitations'),
        bullets('<b>Convection</b> superheaters sit in the tube bank and gain superheat as the load rises; '
                '<b>radiant</b> superheaters sit in the furnace and lose superheat as the load rises; a '
                '<b>combined</b> design is used so the outlet temperature stays nearly flat over the load '
                'range.',
                'The tubes run hotter than any other part of the boiler, so they must be of an alloy steel '
                'and must have steam flowing through them at all times — no steam flow means a burnt-out '
                'tube.',
                'Superheated steam has a lower heat-transfer coefficient than wet steam, so the superheater '
                'needs a large surface; and the steam is dry, so a superheater cannot be protected by the '
                'evaporating water in the way the water walls are.'),
    ),
    gu=join(
        h4('વ્યાખ્યા'),
        p('<b>Superheater</b> એ boilerના flue-gas રસ્તામાં ગોઠવેલી tubeની બેંક છે જેમાં drumમાંથી આવતી saturated '
          'વરાળ અચલ pressure પર saturation temperatureથી ઉપર ગરમ થાય. એ વરાળ સૂકવે અને તાપમાન વધારે, જેથી '
          'cycle efficiency વધે અને turbineમાં ઘસારો તથા corrosion અટકે.'),
        figure(ufig.superheater(),
               'Fig. 4.3 · Convection superheater — gas passમાં serpentine coil, saturated steam અંદર અને '
               'superheated steam બહાર.'),
        h4('વર્ણન'),
        table(['ભાગ', 'હેતુ'], [
            ['Alloy steel tubeના serpentine coil', 'ટૂંકી જગ્યામાં લાંબો રસ્તો આપે, એટલે નાના gas passમાં વરાળ '
             'heat લે'],
            ['Inlet header (saturated steam)', 'વરાળ બધા coilમાં સરખી વહેંચે'],
            ['Outlet header (superheated steam)', 'વરાળ એકઠી કરીને turbine સુધી લઈ જાય'],
            ['Support અને spacer', 'vibration અને thermal expansion સામે coil ટકાવે'],
            ['Attemperator (desuperheater)', 'વરાળમાં થોડું પાણી છાંટીને અંતિમ તાપમાન નિયંત્રિત કરે, જે '
             'turbineની ધાતુ માટે મહત્ત્વનું'],
            ['Gas baffle', 'gas સાચા velocityએ coil પાર કરે એ ગોઠવે'],
        ]),
        h4('કાર્ય — સ્ટેપ અને કારણ'),
        steps(('Step 1', 'Saturated વરાળ drumમાંથી નીકળીને inlet headerમાં જાય. કારણ: વરાળ પહેલાં પાણીથી અલગ '
                         'થવી જોઈએ, કારણ કે ટીપાં ક્ષાર લઈ જઈને superheater પર scale બનાવે.'),
              ('Step 2', 'વરાળ 600–900 °Cના ગરમ gasમાં serpentine coilમાંથી પસાર થાય. કારણ: gas વરાળ કરતાં '
                         'ગરમ હોય એટલે gasથી વરાળમાં heat જાય, અને કોઈ જ્યોત tubeને અડતી નથી.'),
              ('Step 3', 'વરાળ saturationથી 30–60 °C ઉપર નીકળે. કારણ: એટલું superheat turbineના છેલ્લા stage '
                         'સૂકા રાખવા પૂરતું છે, અને tubeની ધાતુ creep મર્યાદામાં રહે.'),
              ('Step 4', 'Attemperator outletનું તાપમાન ગોઠવે. કારણ: load સાથે gasનું તાપમાન બદલાય, અને '
                         'turbine designથી ઉપરનું steam temperature ઝીલી ન શકે.')),
        h4('ઉકેલેલું ઉદાહરણ — ઉમેરાતું superheat'),
        p('20 bar પર વરાળ drumમાંથી 212 °C પર dry saturated નીકળે છે, h<sub>g</sub> = 2799 kJ/kg. Superheaterમાંથી '
          '350 °C પર h = 3060 kJ/kg સાથે, 20 t/hના દરે નીકળે છે. Superheaterમાં ઉમેરાતી heat શોધો.'),
        work('Given: h<sub>1</sub> = 2799 kJ/kg · h<sub>2</sub> = 3060 kJ/kg · m = 20 000 kg/h · '
             'T<sub>sat</sub> = 212 °C · T<sub>out</sub> = 350 °C',
             'Degree of superheat = 350 − 212 = 138 °C',
             'Formula: Q = m (h<sub>2</sub> − h<sub>1</sub>)',
             'Substitution: Q = 20 000 × (3060 − 2799) = 20 000 × 261'),
        result('Superheaterમાં ઉમેરાતી heat = 5.22 × 10<sup>6</sup> kJ/h ≈ 1450 kW'),
        p('Sanity check: 261 kJ/kg એ વરાળની કુલ enthalpyના લગભગ 10 % છે, જે convection superheaterનો સામાન્ય '
          'ભાગ છે — સાચું.'),
        h4('પ્રકારો અને મર્યાદાઓ'),
        bullets('<b>Convection</b> superheater tube bankમાં બેસે અને load વધે તો superheat વધે; <b>radiant</b> '
                'superheater furnaceમાં બેસે અને load વધે તો superheat ઘટે; એટલે load આખી રેન્જમાં outletનું '
                'તાપમાન લગભગ સ્થિર રહે એ માટે <b>combined</b> design વપરાય.',
                'Superheaterની tube boilerના બીજા ભાગ કરતાં વધુ ગરમ ચાલે, એટલે alloy steel જોઈએ અને એમાં '
                'હંમેશા વરાળ વહેતી રહેવી જોઈએ — વરાળ બંધ થાય તો tube બળી જાય.',
                'Superheated વરાળનો heat-transfer coefficient wet વરાળ કરતાં નીચો હોવાથી મોટી surface જોઈએ; '
                'અને વરાળ સૂકી હોવાથી superheaterને water wallની જેમ બાષ્પીય પાણીનું રક્ષણ મળતું નથી.'),
    ),
))

Q4['cards'].append(dict(
    number='Q.4 (c)', marks=7, tag='OR',
    q='Give Comparison of Reciprocating, Rotary vane, Rotary screw and Centrifugal type of Air compressor',
    en=join(
        h4('The four types'),
        p('<b>Reciprocating:</b> a piston in a cylinder draws in air, compresses it and pushes it out — '
          'positive displacement. <b>Rotary vane:</b> an eccentric rotor with sliding vanes squeezes the '
          'air between the vanes and the casing. <b>Rotary screw:</b> two intermeshing rotors trap the air '
          'and reduce its volume along the axis. <b>Centrifugal:</b> a high-speed impeller gives the air a '
          'velocity, and a diffuser converts that velocity into pressure — dynamic compression.'),
        h4('Comparison'),
        table(['Point', 'Reciprocating', 'Rotary vane', 'Rotary screw', 'Centrifugal'], [
            ['Principle', 'positive displacement, piston', 'positive displacement, sliding vanes',
             'positive displacement, meshing rotors', 'dynamic, impeller + diffuser'],
            ['Pressure', 'very high, up to 1000 bar in stages; usual 6–15 bar', 'low to medium, up to '
             'about 8 bar', 'medium, 7–13 bar in one or two stages', 'low to medium, 2–8 bar per stage; '
             'high with many stages'],
            ['Capacity (free air)', 'small to medium, up to about 3000 m<sup>3</sup>/h',
             'small, up to about 2000 m<sup>3</sup>/h', 'medium to large, up to about 30 000 '
             'm<sup>3</sup>/h', 'very large, up to 200 000 m<sup>3</sup>/h and more'],
            ['Flow', 'pulsating; needs a receiver and a dampener', 'steady', 'very steady', 'continuous and '
             'smooth'],
            ['Efficiency', 'highest at high pressure; volumetric efficiency falls with clearance',
             'moderate; falls as the vanes wear', 'good over a wide range; better than vane',
             'high only near the design point, poor at part load'],
            ['Speed', 'low, 300–1000 rpm', 'moderate, 1000–3000 rpm', 'high, 3000–20 000 rpm',
             'very high, 10 000–50 000 rpm'],
            ['Size and weight', 'bulky and heavy for the flow; needs a strong foundation',
             'compact and light', 'compact, about half the size of a reciprocating unit',
             'small and light for a very large flow'],
            ['Air quality', 'oil is carried over from the cylinder walls', 'oil from the vanes and casing',
             'oil-flooded types carry oil; oil-free types are available', 'oil-free delivery is normal'],
            ['Maintenance', 'valves, rings and bearings; many wearing parts',
             'vane wear, so periodic vane and seal replacement', 'few parts; the rotors do not touch, so '
             'long life', 'very few parts, but sensitive to dirt and to surge'],
            ['Delivery temperature', 'high, needs an aftercooler', 'high', 'moderate (oil-flooded is '
             'cooler)', 'low to moderate'],
            ['Control', 'unloading, clearance pockets, speed', 'modulating valve, blow-off',
             'slide valve, variable speed, load/unload', 'inlet guide vanes, blow-off to avoid surge'],
            ['Cost', 'cheapest for small capacity and high pressure', 'low first cost for small capacity',
             'higher first cost, but cheaper per m<sup>3</sup> at large capacity', 'high first cost, '
             'cheapest at very large flow'],
            ['Typical use', 'workshop air, high-pressure process, gas compression, instrument air',
             'small packaged units, mobile tyre inflation', 'plant air, instrument air, refrigeration '
             'compressors', 'large plant air, blast furnace air, ventilation, process air'],
        ]),
        h4('How to choose — step and reason'),
        steps(('Step 1', 'Fix the flow and the pressure first. Reason: these two numbers eliminate most '
                         'types before any cost comparison — below 8 bar and above 5000 m<sup>3</sup>/h, a '
                         'centrifugal is the natural choice.'),
              ('Step 2', 'Look at the duty cycle. Reason: a compressor that runs at part load for most of '
                         'the day is cheaper as a screw with a slide valve than as a centrifugal, whose '
                         'efficiency collapses away from the design point.'),
              ('Step 3', 'Check the air quality needed. Reason: an oil-free process needs a screw or a '
                         'centrifugal; a reciprocating unit needs a good filter and a dryer.'),
              ('Step 4', 'Compare the life cost, not the price. Reason: the electricity is about 70–80 % of '
                         'the cost of compressed air over ten years, so a 5 % better efficiency beats a '
                         'lower price tag.')),
        h4('Worked example — specific power'),
        p('A plant needs 20 m<sup>3</sup>/min of free air at 7 bar. A reciprocating unit takes 110 kW and a '
          'screw unit takes 100 kW. Find the specific power of each and the annual saving at 6000 h/y and '
          '₹ 8 per kWh.'),
        work('Given: flow = 20 m<sup>3</sup>/min · P<sub>recip</sub> = 110 kW · P<sub>screw</sub> = 100 kW · '
             'hours = 6000 per year · tariff = ₹ 8/kWh',
             'Specific power (recip) = ' + frac('110', '20') + ' = 5.5 kW per m<sup>3</sup>/min',
             'Specific power (screw) = ' + frac('100', '20') + ' = 5.0 kW per m<sup>3</sup>/min',
             'Power saved = 110 − 100 = 10 kW',
             'Annual energy saved = 10 × 6000 = 60 000 kWh',
             'Annual saving = 60 000 × 8 = ₹ 4 80 000'),
        result('Specific power 5.5 against 5.0 kW per m<sup>3</sup>/min; annual saving ≈ ₹ 4.8 lakh'),
        p('Sanity check: a specific power of 5–6 kW per m<sup>3</sup>/min at 7 bar is the accepted figure '
          'for industrial compressors, so both machines are in the normal range and the screw is the '
          'better buy.'),
        h4('Limitations'),
        bullets('A reciprocating unit is limited by its valves and by the clearance volume, and it delivers '
                'pulsating air, so a receiver is compulsory.',
                'A vane compressor loses efficiency as the vanes and the casing wear, so it is used mainly '
                'in small and mobile units.',
                'A screw compressor needs clean oil (in the flooded type) and its rotors must not touch, so '
                'the timing gears and the seals are critical.',
                'A centrifugal compressor surges at low flow, so it must always be run with a blow-off or '
                'inlet guide vane control, and it cannot be restarted against a full discharge line.'),
    ),
    gu=join(
        h4('ચાર પ્રકાર'),
        p('<b>Reciprocating:</b> cylinderમાં piston હવા ખેંચે, compress કરે અને બહાર ધકેલે — positive '
          'displacement. <b>Rotary vane:</b> sliding vane વાળો eccentric rotor vane અને casing વચ્ચેની હવા '
          'દબાવે. <b>Rotary screw:</b> બે intermeshing rotor હવા ફસાવીને અક્ષ સાથે એનું volume ઘટાડે. '
          '<b>Centrifugal:</b> ઊંચી ઝડપનું impeller હવાને velocity આપે અને diffuser એ velocityને pressureમાં '
          'ફેરવે — dynamic compression.'),
        h4('સરખામણી'),
        table(['મુદ્દો', 'Reciprocating', 'Rotary vane', 'Rotary screw', 'Centrifugal'], [
            ['સિદ્ધાંત', 'positive displacement, piston', 'positive displacement, sliding vane',
             'positive displacement, meshing rotor', 'dynamic, impeller + diffuser'],
            ['Pressure', 'ખૂબ ઊંચું, stageમાં 1000 bar સુધી; સામાન્ય 6–15 bar', 'નીચાથી મધ્યમ, લગભગ 8 bar '
             'સુધી', 'મધ્યમ, એક-બે stageમાં 7–13 bar', 'નીચાથી મધ્યમ, પ્રતિ stage 2–8 bar; ઘણા stage સાથે '
             'ઊંચું'],
            ['ક્ષમતા (free air)', 'નાનીથી મધ્યમ, લગભગ 3000 m<sup>3</sup>/h સુધી',
             'નાની, લગભગ 2000 m<sup>3</sup>/h સુધી', 'મધ્યમથી મોટી, લગભગ 30 000 m<sup>3</sup>/h સુધી',
             'ખૂબ મોટી, 200 000 m<sup>3</sup>/h અને એથી વધુ'],
            ['Flow', 'pulsating; receiver અને dampener જોઈએ', 'સ્થિર', 'ખૂબ સ્થિર', 'સતત અને સરખો'],
            ['Efficiency', 'ઊંચા pressure પર સૌથી વધુ; clearance સાથે volumetric efficiency ઘટે',
             'મધ્યમ; vane ઘસાય તેમ ઘટે', 'વિશાળ રેન્જમાં સારી; vane કરતાં સારી',
             'ફક્ત design point પાસે ઊંચી, part load પર નબળી'],
            ['ઝડપ', 'નીચી, 300–1000 rpm', 'મધ્યમ, 1000–3000 rpm', 'ઊંચી, 3000–20 000 rpm',
             'ખૂબ ઊંચી, 10 000–50 000 rpm'],
            ['કદ અને વજન', 'flow પ્રમાણે મોટું-ભારે; મજબૂત foundation જોઈએ', 'compact અને હલકું',
             'compact, reciprocating કરતાં લગભગ અડધું', 'ખૂબ મોટા flow માટે નાનું અને હલકું'],
            ['હવાની ગુણવત્તા', 'cylinder wallથી oil જાય', 'vane અને casingથી oil જાય',
             'oil-flooded પ્રકારમાં oil જાય; oil-free પણ મળે', 'સામાન્ય રીતે oil-free પુરવઠો'],
            ['Maintenance', 'valve, ring અને bearing; ઘણા ઘસાતા ભાગ',
             'vane ઘસાય, એટલે નિયમિત vane અને seal બદલવા પડે', 'ઓછા ભાગ; rotor અડતા નથી એટલે લાંબું આયુ',
             'ખૂબ ઓછા ભાગ, પણ ધૂળ અને surge પ્રત્યે સંવેદનશીલ'],
            ['Delivery temperature', 'ઊંચું, aftercooler જોઈએ', 'ઊંચું', 'મધ્યમ (oil-flooded વધુ ઠંડું)',
             'નીચાથી મધ્યમ'],
            ['નિયંત્રણ', 'unloading, clearance pocket, speed', 'modulating valve, blow-off',
             'slide valve, variable speed, load/unload', 'inlet guide vane, surge ટાળવા blow-off'],
            ['ખર્ચ', 'નાની ક્ષમતા અને ઊંચા pressure માટે સૌથી સસ્તું', 'નાની ક્ષમતા માટે ઓછો first cost',
             'first cost વધુ, પણ મોટી ક્ષમતાએ પ્રતિ m<sup>3</sup> સસ્તું', 'first cost ઊંચો, ખૂબ મોટા flow એ '
             'સૌથી સસ્તું'],
            ['સામાન્ય ઉપયોગ', 'workshop air, ઊંચા pressureની process, gas compression, instrument air',
             'નાના packaged unit, mobile ટાયર inflation', 'plant air, instrument air, refrigeration '
             'compressor', 'મોટું plant air, blast furnace air, ventilation, process air'],
        ]),
        h4('પસંદગી કેવી રીતે — સ્ટેપ અને કારણ'),
        steps(('Step 1', 'પહેલાં flow અને pressure નક્કી કરો. કારણ: આ બે આંકડા ખર્ચ સરખાવ્યા પહેલાં મોટા ભાગના '
                         'પ્રકાર બાદ કરી નાખે — 8 barથી નીચે અને 5000 m<sup>3</sup>/hથી ઉપર centrifugal સ્વાભાવિક '
                         'પસંદગી.'),
              ('Step 2', 'Duty cycle જુઓ. કારણ: દિવસનો મોટો ભાગ part load પર ચાલતો compressor slide valve '
                         'વાળા screw તરીકે સસ્તો પડે; centrifugalની efficiency design pointથી દૂર ધરાશાયી થાય.'),
              ('Step 3', 'જરૂરી હવાની ગુણવત્તા ચકાસો. કારણ: oil-free process માટે screw કે centrifugal જોઈએ; '
                         'reciprocating હોય તો સારો filter અને dryer જરૂરી.'),
              ('Step 4', 'ભાવ નહીં, life cost સરખાવો. કારણ: દસ વર્ષમાં compressed airનો 70–80 % ખર્ચ '
                         'electricity છે, એટલે 5 % સારી efficiency સસ્તા ભાવને હરાવે.')),
        h4('ઉકેલેલું ઉદાહરણ — specific power'),
        p('Plantને 7 bar પર 20 m<sup>3</sup>/min free air જોઈએ. Reciprocating unit 110 kW લે છે અને screw unit '
          '100 kW. બંનેનું specific power અને વર્ષે 6000 કલાક તથા ₹ 8 પ્રતિ kWh પર વાર્ષિક બચત શોધો.'),
        work('Given: flow = 20 m<sup>3</sup>/min · P<sub>recip</sub> = 110 kW · P<sub>screw</sub> = 100 kW · '
             'વર્ષે કલાક = 6000 · tariff = ₹ 8/kWh',
             'Specific power (recip) = ' + frac('110', '20') + ' = 5.5 kW પ્રતિ m<sup>3</sup>/min',
             'Specific power (screw) = ' + frac('100', '20') + ' = 5.0 kW પ્રતિ m<sup>3</sup>/min',
             'બચતું power = 110 − 100 = 10 kW',
             'વર્ષની બચતેલી energy = 10 × 6000 = 60 000 kWh',
             'વાર્ષિક બચત = 60 000 × 8 = ₹ 4 80 000'),
        result('Specific power 5.5 સામે 5.0 kW પ્રતિ m<sup>3</sup>/min; વાર્ષિક બચત ≈ ₹ 4.8 લાખ'),
        p('Sanity check: 7 bar પર 5–6 kW પ્રતિ m<sup>3</sup>/min એ ઔદ્યોગિક compressor માટે સ્વીકૃત આંકડો છે, '
          'એટલે બંને મશીન સામાન્ય રેન્જમાં છે અને screw સારી ખરીદી છે.'),
        h4('મર્યાદાઓ'),
        bullets('Reciprocating unit પોતાના valve અને clearance volumeથી મર્યાદિત છે, અને pulsating હવા આપે એટલે '
                'receiver ફરજિયાત.',
                'Vane compressor vane અને casing ઘસાય તેમ efficiency ગુમાવે, એટલે મુખ્યત્વે નાના અને mobile '
                'unitમાં વપરાય.',
                'Screw compressorને (flooded પ્રકારમાં) ચોખ્ખું oil જોઈએ અને rotor અડવા ન જોઈએ, એટલે timing gear '
                'અને seal નિર્ણાયક.',
                'Centrifugal compressor નીચા flow પર surge કરે, એટલે blow-off કે inlet guide vane સાથે જ '
                'ચલાવવું પડે, અને ભરેલી discharge લાઇન સામે ફરી શરૂ કરી શકાય નહીં.'),
    ),
))


# ---------------------------------------------------------------- Q5
Q5 = {
    'title_en': 'Q5 · Refrigerants, COP and TOR, steam-jet and vapour-compression refrigeration',
    'title_gu': 'પ્ર.5 · રેફ્રિજરન્ટ, COP અને TOR, સ્ટીમ-જેટ અને વેપર-કમ્પ્રેશન રેફ્રિજરેશન',
    'cards': [],
}

Q5['cards'].append(dict(
    number='Q.5 (a)', marks=3, q='Write a short note on primary and secondary refrigerants',
    en=join(
        h4('Primary refrigerant'),
        p('A <b>primary refrigerant</b> is the working fluid of the refrigeration cycle: it is the fluid '
          'that is compressed, condensed and evaporated, and it absorbs heat from the space directly at '
          'the evaporator. Examples: ammonia (R-717), carbon dioxide (R-744), the halocarbons R-12, R-22, '
          'R-134a and R-410A, and the hydrocarbons propane and isobutane.'),
        h4('Secondary refrigerant'),
        p('A <b>secondary refrigerant</b> (brine or coolant) is a fluid that is <b>cooled</b> by the '
          'primary refrigerant in a heat exchanger and then pumped to the place where the cooling is '
          'needed, returning warm. It never goes through the compressor. It is used when the load is far '
          'from the machine room, when a leak in the cooled space would be dangerous (ammonia in a food '
          'store), or when several cold rooms must run from one plant. Examples: calcium chloride brine, '
          'sodium chloride brine, glycol–water, and in air conditioning simply chilled water.'),
        h4('Comparison'),
        table(['Point', 'Primary refrigerant', 'Secondary refrigerant'], [
            ['Role', 'the working fluid of the cycle', 'a heat-carrier between the plant and the load'],
            ['Circulation', 'through compressor, condenser, expansion valve and evaporator',
             'pumped through the cooling coils only'],
            ['Examples', 'R-134a, ammonia, CO<sub>2</sub>, propane', 'CaCl<sub>2</sub> brine, glycol, '
             'chilled water'],
            ['Quantity needed', 'small, in a closed circuit', 'large, filling the whole pipe network'],
            ['Leak risk', 'leak is dangerous, especially ammonia', 'leak is less serious, but brine '
             'corrodes'],
            ['Cost', 'expensive per kg', 'cheap'],
        ]),
        p('<b>Example:</b> a dairy cools its milk with chilled water at 2 °C. R-134a in the machine room is '
          'the primary refrigerant, and the chilled water pumped to the milk chiller is the secondary '
          'refrigerant.'),
    ),
    gu=join(
        h4('Primary refrigerant'),
        p('<b>Primary refrigerant</b> એ refrigeration cycleનું working fluid છે: એ જ પ્રવાહી compress, '
          'condense અને evaporate થાય, અને evaporatorમાં સીધું જગ્યામાંથી heat લે. ઉદાહરણ: ammonia '
          '(R-717), carbon dioxide (R-744), halocarbon R-12, R-22, R-134a અને R-410A, તથા hydrocarbon '
          'propane અને isobutane.'),
        h4('Secondary refrigerant'),
        p('<b>Secondary refrigerant</b> (brine કે coolant) એ પ્રવાહી છે જે heat exchangerમાં primary '
          'refrigerantથી <b>ઠંડું</b> થાય અને પછી જ્યાં ઠંડક જોઈએ ત્યાં pump થાય, ગરમ થઈને પાછું આવે. એ '
          'compressorમાંથી કદી પસાર થતું નથી. જ્યાં load machine roomથી દૂર હોય, જ્યાં ઠંડી જગ્યામાં leak ખતરનાક '
          'હોય (food storeમાં ammonia), કે જ્યાં એક plantથી ઘણા cold room ચલાવવા હોય ત્યાં વપરાય. ઉદાહરણ: '
          'calcium chloride brine, sodium chloride brine, glycol–water, અને air conditioningમાં સાદું chilled '
          'water.'),
        h4('સરખામણી'),
        table(['મુદ્દો', 'Primary refrigerant', 'Secondary refrigerant'], [
            ['ભૂમિકા', 'cycleનું working fluid', 'plant અને load વચ્ચે heat લઈ જનાર'],
            ['Circulation', 'compressor, condenser, expansion valve અને evaporatorમાંથી',
             'ફક્ત cooling coilમાં pump થાય'],
            ['ઉદાહરણ', 'R-134a, ammonia, CO<sub>2</sub>, propane', 'CaCl<sub>2</sub> brine, glycol, '
             'chilled water'],
            ['જરૂરી જથ્થો', 'ઓછો, બંધ circuitમાં', 'મોટો, આખા pipe networkમાં'],
            ['Leakનું જોખમ', 'leak ખતરનાક, ખાસ કરીને ammonia', 'leak ઓછું ગંભીર, પણ brine corrosive'],
            ['ખર્ચ', 'પ્રતિ kg મોંઘું', 'સસ્તું'],
        ]),
        p('<b>ઉદાહરણ:</b> Dairy પોતાનું દૂધ 2 °Cના chilled waterથી ઠંડું કરે છે. Machine roomમાં R-134a '
          'primary refrigerant છે, અને milk chiller સુધી pump થતું chilled water secondary refrigerant છે.'),
    ),
))

Q5['cards'].append(dict(
    number='Q.5 (b)', marks=4, q='List out primary refrigerant and explain any one.',
    en=join(
        h4('List of primary refrigerants'),
        table(['Group', 'Refrigerant', 'Boiling point at 1 atm', 'Note'], [
            ['Halocarbon', 'R-12 (CCl<sub>2</sub>F<sub>2</sub>)', '−29.8 °C', 'CFC, banned by the Montreal '
             'Protocol'],
            ['Halocarbon', 'R-22 (CHClF<sub>2</sub>)', '−40.8 °C', 'HCFC, being phased out'],
            ['Halocarbon', 'R-134a (CH<sub>2</sub>FCF<sub>3</sub>)', '−26.1 °C', 'HFC, the common '
             'replacement for R-12'],
            ['Halocarbon blend', 'R-410A (R-32/R-125)', '−51 °C', 'HFC blend for air conditioning'],
            ['Inorganic', 'Ammonia (R-717, NH<sub>3</sub>)', '−33.3 °C', 'excellent properties, toxic'],
            ['Inorganic', 'Carbon dioxide (R-744, CO<sub>2</sub>)', '−78.5 °C (sublimes)',
             'safe, but very high pressure'],
            ['Hydrocarbon', 'Propane (R-290), isobutane (R-600a)', '−42 °C, −11.7 °C',
             'good properties, flammable'],
            ['Inorganic', 'Water (R-718)', '100 °C', 'used in absorption systems only'],
        ]),
        h4('One explained — ammonia, R-717'),
        p('<b>Ammonia</b> is the best-known inorganic refrigerant and is still the standard for large '
          'industrial refrigeration, cold stores and ice plants.'),
        bullets('<b>Properties:</b> it has a very high latent heat of vaporisation (about 1370 kJ/kg at '
                '−15 °C, several times that of R-134a), so the mass flow for a given duty is small; it is '
                'cheap, easily available, and it has a small global warming potential and zero ozone '
                'depletion potential.',
                '<b>Behaviour:</b> it is detectable by smell at 5 ppm, which is a safety advantage, and it '
                'does not mix with oil in the usual way, so an oil separator is needed.',
                '<b>Materials:</b> it attacks copper and its alloys, so steel and iron are used throughout; '
                'it is not compatible with the usual copper tubing.',
                '<b>Use:</b> cold storage, ice plants, dairy and brewery chilling, and large ammonia '
                'absorption plants.'),
        h4('Worked example — mass flow of refrigerant'),
        p('A plant of 50 TR capacity works with ammonia at an evaporating temperature of −15 °C, where the '
          'latent heat is 1370 kJ/kg. Compare the refrigerant mass flow with R-134a, whose latent heat is '
          'about 210 kJ/kg at the same condition. Take 1 TR = 3.517 kW.'),
        work('Given: capacity = 50 TR · 1 TR = 3.517 kW · h<sub>fg,NH3</sub> = 1370 kJ/kg · '
             'h<sub>fg,R134a</sub> = 210 kJ/kg',
             'Cooling load = 50 × 3.517 = 175.9 kW = 175.9 kJ/s',
             'Mass flow of ammonia = ' + frac('175.9', '1370') + ' = 0.128 kg/s',
             'Mass flow of R-134a = ' + frac('175.9', '210') + ' = 0.838 kg/s'),
        result('Ammonia needs 0.128 kg/s; R-134a needs 0.838 kg/s — about 6.5 times more'),
        p('Sanity check: the ratio of the latent heats, 1370/210 = 6.5, is exactly the ratio of the mass '
          'flows, so the arithmetic is consistent and the ammonia circuit is much smaller.'),
        h4('Limitations'),
        p('Ammonia is <b>toxic</b> and flammable in a narrow range, so the machine room needs gas detection, '
          'emergency ventilation and a water spray; it corrodes copper, and it is not suitable for small '
          'domestic units, where the hydrocarbons or R-134a are used instead.'),
    ),
    gu=join(
        h4('Primary refrigerantની યાદી'),
        table(['જૂથ', 'Refrigerant', '1 atm પર boiling point', 'નોંધ'], [
            ['Halocarbon', 'R-12 (CCl<sub>2</sub>F<sub>2</sub>)', '−29.8 °C', 'CFC, Montreal Protocolથી '
             'પ્રતિબંધિત'],
            ['Halocarbon', 'R-22 (CHClF<sub>2</sub>)', '−40.8 °C', 'HCFC, ધીમે ધીમે બંધ થાય છે'],
            ['Halocarbon', 'R-134a (CH<sub>2</sub>FCF<sub>3</sub>)', '−26.1 °C', 'HFC, R-12નો સામાન્ય વિકલ્પ'],
            ['Halocarbon blend', 'R-410A (R-32/R-125)', '−51 °C', 'Air conditioning માટે HFC blend'],
            ['Inorganic', 'Ammonia (R-717, NH<sub>3</sub>)', '−33.3 °C', 'ઉત્તમ properties, ઝેરી'],
            ['Inorganic', 'Carbon dioxide (R-744, CO<sub>2</sub>)', '−78.5 °C (sublime થાય)',
             'સુરક્ષિત, પણ ખૂબ ઊંચું pressure'],
            ['Hydrocarbon', 'Propane (R-290), isobutane (R-600a)', '−42 °C, −11.7 °C',
             'સારી properties, જ્વલનશીલ'],
            ['Inorganic', 'Water (R-718)', '100 °C', 'ફક્ત absorption systemમાં વપરાય'],
        ]),
        h4('એક વિગતે — ammonia, R-717'),
        p('<b>Ammonia</b> સૌથી જાણીતું inorganic refrigerant છે અને મોટા ઔદ્યોગિક refrigeration, cold store '
          'તથા ice plant માટે આજે પણ માનક છે.'),
        bullets('<b>ગુણધર્મ:</b> vaporisationની latent heat ખૂબ ઊંચી (આશરે −15 °C પર 1370 kJ/kg, R-134a '
                'કરતાં ઘણી ગણી), એટલે એટલા જ કામ માટે mass flow ઓછો; સસ્તું, સહેલાઈથી મળે, global warming '
                'potential નાનું અને ozone depletion potential શૂન્ય.',
                '<b>વર્તન:</b> 5 ppm પર જ ગંધથી પકડાય, જે સલામતીનો ફાયદો છે, અને સામાન્ય રીતે oil સાથે ભળતું '
                'નથી, એટલે oil separator જોઈએ.',
                '<b>Material:</b> એ copper અને એના alloy પર હુમલો કરે, એટલે આખે રસ્તે steel અને iron વપરાય; '
                'સામાન્ય copper tubing ચાલે નહીં.',
                '<b>ઉપયોગ:</b> cold storage, ice plant, dairy અને breweryનું chilling, અને મોટા ammonia '
                'absorption plant.'),
        h4('ઉકેલેલું ઉદાહરણ — refrigerantનો mass flow'),
        p('50 TR ક્ષમતાનું plant ammonia સાથે −15 °C evaporating temperature પર ચાલે છે, જ્યાં latent heat '
          '1370 kJ/kg છે. એ જ સ્થિતિમાં R-134a સાથેનો mass flow સરખાવો, જેની latent heat લગભગ 210 kJ/kg છે. '
          '1 TR = 3.517 kW લો.'),
        work('Given: capacity = 50 TR · 1 TR = 3.517 kW · h<sub>fg,NH3</sub> = 1370 kJ/kg · '
             'h<sub>fg,R134a</sub> = 210 kJ/kg',
             'Cooling load = 50 × 3.517 = 175.9 kW = 175.9 kJ/s',
             'Ammoniaનો mass flow = ' + frac('175.9', '1370') + ' = 0.128 kg/s',
             'R-134aનો mass flow = ' + frac('175.9', '210') + ' = 0.838 kg/s'),
        result('Ammoniaને 0.128 kg/s જોઈએ; R-134aને 0.838 kg/s — લગભગ 6.5 ગણો વધુ'),
        p('Sanity check: latent heatનું પ્રમાણ 1370/210 = 6.5 બરાબર mass flowના પ્રમાણ જેટલું છે, એટલે '
          'ગણતરી સુસંગત છે અને ammonia circuit ઘણું નાનું પડે.'),
        h4('મર્યાદાઓ'),
        p('Ammonia <b>ઝેરી</b> છે અને ચોક્કસ રેન્જમાં જ્વલનશીલ, એટલે machine roomમાં gas detection, '
          'emergency ventilation અને પાણીનો spray જરૂરી; એ copperને ખાય છે, અને નાના ઘરેલું unit માટે યોગ્ય '
          'નથી — ત્યાં hydrocarbon કે R-134a વપરાય.'),
    ),
))

Q5['cards'].append(dict(
    number='Q.5 (c)', marks=7, q='Explain Steam-jet refrigeration system',
    en=join(
        h4('Definition and principle'),
        p('A <b>steam-jet (ejector) refrigeration system</b> produces chilled water without any compressor. '
          'The compressor is replaced by a <b>steam ejector</b>: high-pressure motive steam expands through '
          'a converging–diverging nozzle, its velocity rises to over 1000 m/s and its pressure falls below '
          'the pressure in the flash chamber. That low pressure draws vapour out of the flash chamber, so '
          'the water in the chamber boils (flashes) at a low temperature and cools itself. In this way '
          'water at 5–10 °C is produced with steam as the only energy input.'),
        h4('Construction — part and purpose'),
        table(['Part', 'Purpose'], [
            ['Steam nozzle (converging–diverging)', 'expands the motive steam to a very high velocity and a '
             'low pressure'],
            ['Mixing chamber and diffuser (the ejector)', 'the high-velocity steam drags the vapour along, '
             'and the diffuser converts the velocity back into pressure'],
            ['Flash chamber (evaporator)', 'holds water at 5–10 °C; the vapour is drawn off, so the '
             'remaining water cools'],
            ['Chilled-water pump', 'circulates the chilled water to the cooling load'],
            ['Condenser (surface or barometric)', 'condenses the mixture of motive steam and vapour at '
             '35–40 °C'],
            ['Air removal (vacuum) system', 'keeps the condenser pressure low; air leakage would raise it '
             'and spoil the vacuum'],
            ['Cooling-water pump', 'supplies the condenser cooling water'],
        ]),
        figure(ufig.steam_jet_refrigeration(),
               'Fig. 5.1 · Steam-jet refrigeration — motive steam, ejector, flash chamber, condenser and '
               'chilled-water circuit.'),
        h4('Working — step and reason'),
        steps(('Step 1', 'Motive steam at 7–10 bar enters the nozzle and expands. Reason: the pressure energy '
                         'converts to velocity, so a very low pressure is created at the nozzle exit — this '
                         'low pressure is the "compressor suction".'),
              ('Step 2', 'The low pressure in the mixing chamber draws vapour from the flash chamber. Reason: '
                         'the flash chamber is at a pressure corresponding to 5–10 °C, so vapour leaves the '
                         'water to fill the ejector.'),
              ('Step 3', 'The water that is left behind loses its latent heat and cools to 5–10 °C. Reason: '
                         'the heat of vaporisation comes from the water itself, so evaporation cools the '
                         'remaining liquid — this is flashing.'),
              ('Step 4', 'The mixture of motive steam and vapour is compressed through the diffuser to the '
                         'condenser pressure. Reason: the diffuser slows the mixture down, and the kinetic '
                         'energy is converted back to pressure, so the vapour can be condensed at 35–40 °C '
                         'against cooling water.'),
              ('Step 5', 'The condensate is pumped away and the chilled water is pumped to the load. Reason: '
                         'the cycle is completed with liquid water, which is then flashed again.')),
        h4('Worked example — chilled water and motive steam'),
        p('A steam-jet plant cools 20 000 kg/h of water from 15 °C to 8 °C. The flash chamber works at 8 °C, '
          'where the latent heat is 2400 kJ/kg, and the motive steam supplies 1.5 kg per kg of vapour '
          'evaporated. Find the vapour evaporated and the motive steam needed.'),
        work('Given: water = 20 000 kg/h · cooled from 15 °C to 8 °C · c<sub>p</sub> = 4.18 kJ/kg·K · '
             'h<sub>fg</sub> = 2400 kJ/kg · motive steam = 1.5 kg per kg vapour',
             'Heat to be removed = m · c<sub>p</sub> · ΔT = 20 000 × 4.18 × (15 − 8) = 20 000 × 4.18 × 7',
             'Heat = 585 200 kJ/h',
             'Vapour evaporated = ' + frac('heat removed', 'latent heat') + ' = ' + frac('585 200', '2400')
             + ' = 243.8 kg/h',
             'Motive steam = 1.5 × 243.8 = 365.7 kg/h'),
        result('Vapour evaporated ≈ 244 kg/h; motive steam required ≈ 366 kg/h'),
        p('Sanity check: the vapour evaporated is only 244 kg out of 20 000 kg of water — a flash of about '
          '1.2 %, which is the normal figure for a 7 °C drop.'),
        h4('Advantages'),
        bullets('No compressor and no moving part in the refrigeration circuit, so the plant is simple, '
                'cheap and reliable.',
                'It can use waste or low-grade steam, and it is safe where a refrigerant leak would be '
                'dangerous, because the working fluid is water.',
                'The capacity is controlled simply by a valve on the motive steam, and the plant is compact '
                'for a large water-chilling duty.'),
        h4('Limitations'),
        bullets('The <b>COP is low</b>, about 0.2–0.5, because a large quantity of motive steam is needed '
                'for a small cooling effect — it is economical only where steam is cheap or waste.',
                'It cannot go below about 2–5 °C, because the flash chamber would freeze; it is a '
                'water-chilling system, not a freezer.',
                'It needs a good vacuum and a reliable air-removal system, and the condenser must be large, '
                'because it condenses both the motive steam and the vapour.',
                'The ejector is efficient only at its design point, so a part-load duty is inefficient.'),
    ),
    gu=join(
        h4('વ્યાખ્યા અને સિદ્ધાંત'),
        p('<b>Steam-jet (ejector) refrigeration system</b> કોઈ compressor વગર ઠંડું પાણી બનાવે. Compressorની '
          'જગ્યા <b>steam ejector</b> લે છે: ઊંચા pressureની motive steam converging–diverging nozzleમાંથી '
          'પસાર થાય, એનો velocity 1000 m/sથી વધુ થાય અને pressure flash chamberના pressureથી નીચે જાય. એ '
          'નીચું pressure flash chamberમાંથી વરાળ ખેંચે, એટલે chamberમાંનું પાણી નીચા તાપમાને ઉકળે (flash '
          'થાય) અને પોતે ઠંડું પડે. આમ ફક્ત steamની energy વાપરીને 5–10 °Cનું પાણી મળે.'),
        h4('રચના — ભાગ અને હેતુ'),
        table(['ભાગ', 'હેતુ'], [
            ['Steam nozzle (converging–diverging)', 'motive steamને ખૂબ ઊંચા velocity અને નીચા pressure સુધી '
             'ફેલાવે'],
            ['Mixing chamber અને diffuser (ejector)', 'ઊંચા velocityની steam વરાળને સાથે ખેંચે, અને diffuser '
             'velocity ફરી pressureમાં ફેરવે'],
            ['Flash chamber (evaporator)', '5–10 °C પર પાણી રાખે; વરાળ નીકળતાં બાકીનું પાણી ઠંડું થાય'],
            ['Chilled-water pump', 'ઠંડું પાણી cooling load સુધી ફેરવે'],
            ['Condenser (surface કે barometric)', 'motive steam અને વરાળનું મિશ્રણ 35–40 °C પર ઘનીભૂત કરે'],
            ['Air removal (vacuum) system', 'condenserનું pressure નીચું રાખે; હવા ઘૂસે તો vacuum બગડે'],
            ['Cooling-water pump', 'condenserને cooling water પૂરે'],
        ]),
        figure(ufig.steam_jet_refrigeration(),
               'Fig. 5.1 · Steam-jet refrigeration — motive steam, ejector, flash chamber, condenser અને '
               'chilled-water circuit.'),
        h4('કાર્ય — સ્ટેપ અને કારણ'),
        steps(('Step 1', '7–10 barની motive steam nozzleમાં દાખલ થઈને ફેલાય. કારણ: pressure energy velocityમાં '
                         'ફેરવાય, એટલે nozzleના મુખ પર ખૂબ નીચું pressure બને — એ જ "compressor suction".'),
              ('Step 2', 'Mixing chamberનું નીચું pressure flash chamberમાંથી વરાળ ખેંચે. કારણ: flash chamberનું '
                         'pressure 5–10 °Cને અનુરૂપ હોય, એટલે પાણીમાંથી વરાળ નીકળીને ejector ભરે.'),
              ('Step 3', 'બાકી રહેલું પાણી latent heat ગુમાવીને 5–10 °C સુધી ઠંડું થાય. કારણ: બાષ્પીભવનની heat '
                         'પાણી પોતે આપે, એટલે બાકીનું પ્રવાહી ઠંડું પડે — આ જ flashing.'),
              ('Step 4', 'Motive steam અને વરાળનું મિશ્રણ diffuserમાંથી condenserના pressure સુધી compress થાય. '
                         'કારણ: diffuser મિશ્રણની ઝડપ ઘટાડે અને kinetic energy ફરી pressure બને, એટલે વરાળ '
                         'cooling water સામે 35–40 °C પર ઘનીભૂત થઈ શકે.'),
              ('Step 5', 'Condensate pump થઈને નીકળે અને ઠંડું પાણી load પર જાય. કારણ: cycle પ્રવાહી પાણીથી પૂરું '
                         'થાય, જે ફરી flash થાય.')),
        h4('ઉકેલેલું ઉદાહરણ — ઠંડું પાણી અને motive steam'),
        p('Steam-jet plant કલાકે 20 000 kg પાણી 15 °Cથી 8 °C સુધી ઠંડું કરે છે. Flash chamber 8 °C પર કામ કરે છે '
          'જ્યાં latent heat 2400 kJ/kg છે, અને motive steam પ્રતિ kg વરાળે 1.5 kg જોઈએ. બાષ્પીભવન થતી વરાળ '
          'અને જરૂરી motive steam શોધો.'),
        work('Given: પાણી = 20 000 kg/h · 15 °C થી 8 °C · c<sub>p</sub> = 4.18 kJ/kg·K · '
             'h<sub>fg</sub> = 2400 kJ/kg · પ્રતિ kg વરાળે motive steam = 1.5 kg',
             'કાઢવાની heat = m · c<sub>p</sub> · ΔT = 20 000 × 4.18 × (15 − 8) = 20 000 × 4.18 × 7',
             'Heat = 585 200 kJ/h',
             'બાષ્પીભવન થતી વરાળ = ' + frac('કાઢેલી heat', 'latent heat') + ' = ' + frac('585 200', '2400')
             + ' = 243.8 kg/h',
             'Motive steam = 1.5 × 243.8 = 365.7 kg/h'),
        result('બાષ્પીભવન થતી વરાળ ≈ 244 kg/h; જરૂરી motive steam ≈ 366 kg/h'),
        p('Sanity check: 20 000 kgમાંથી ફક્ત 244 kg વરાળ બને એટલે લગભગ 1.2 % flash, જે 7 °Cના ઘટાડા માટે '
          'સામાન્ય આંકડો છે.'),
        h4('ફાયદા'),
        bullets('Refrigeration circuitમાં કોઈ compressor કે ફરતો ભાગ નહીં, એટલે plant સાદું, સસ્તું અને '
                'ભરોસાપાત્ર.',
                'Waste કે low-grade steam વાપરી શકે, અને જ્યાં refrigerant leak ખતરનાક હોય ત્યાં સુરક્ષિત, કારણ '
                'કે working fluid પાણી છે.',
                'Motive steam પરના valveથી capacity સહેલાઈથી નિયંત્રિત થાય, અને મોટા water-chilling કામ માટે '
                'plant compact હોય.'),
        h4('મર્યાદાઓ'),
        bullets('<b>COP નીચો</b>, લગભગ 0.2–0.5, કારણ કે નાની cooling effect માટે ઘણી motive steam જોઈએ — '
                'ફક્ત જ્યાં steam સસ્તી કે waste હોય ત્યાં આર્થિક.',
                'લગભગ 2–5 °Cથી નીચે જઈ શકે નહીં, કારણ કે flash chamber freeze થાય; એ water-chilling system '
                'છે, freezer નહીં.',
                'સારો vacuum અને ભરોસાપાત્ર air-removal system જોઈએ, અને condenser મોટું જોઈએ, કારણ કે એ '
                'motive steam તથા વરાળ બંને ઘનીભૂત કરે.',
                'Ejector ફક્ત design point પર કાર્યક્ષમ, એટલે part load પર નબળું.'),
    ),
))

Q5['cards'].append(dict(
    number='Q.5 (a)', marks=3, tag='OR', q='List and Explain secondary Refrigerants.',
    en=join(
        p('A <b>secondary refrigerant</b> is a fluid that is cooled by the primary refrigerant and then '
          'pumped to the load, so that the primary circuit stays in the machine room. The common ones:'),
        table(['Secondary refrigerant', 'Working range', 'Note'], [
            ['<b>Calcium chloride brine (CaCl<sub>2</sub>)</b>', 'down to about −35 °C',
             'the standard brine for ice plants and cold stores; cheap and with a low freezing point, but '
             'very corrosive'],
            ['<b>Sodium chloride brine (NaCl)</b>', 'down to about −18 °C', 'cheaper but limited to milder '
             'temperatures, because the eutectic is at −21 °C'],
            ['<b>Propylene glycol / ethylene glycol solution</b>', 'down to −30 °C', 'used in food plant '
             '(propylene glycol is safe) and in chilled-water systems that must not freeze'],
            ['<b>Chilled water</b>', '5–12 °C', 'the commonest air-conditioning secondary; cheap, high '
             'specific heat, but limited to above 0 °C'],
            ['<b>Alcohol–water (methanol or ethanol) mixture</b>', 'down to −20 °C', 'used in small '
             'installations; flammable'],
            ['<b>Air</b>', 'any', 'in an air-conditioning duct or a cold store, the air itself carries the '
             'heat; simple but needs large ducts'],
        ]),
        h4('Explanation — calcium chloride brine'),
        p('A <b>brine</b> is a solution of a salt in water, used because a salt solution freezes at a much '
          'lower temperature than water. Calcium chloride brine at a 25 % concentration freezes at about '
          '−20 °C, so it can carry heat at −10 °C or −15 °C without freezing in the pipes.'),
        bullets('<b>Properties:</b> high density and specific heat, low freezing point, cheap.',
                '<b>Corrosion:</b> brine is very corrosive to steel, so an inhibitor is added and the '
                'circuit is kept alkaline (pH 8–9); air must not be allowed into the circuit, because '
                'dissolved oxygen makes the attack much worse.',
                '<b>Circulation:</b> the brine is cooled in a brine cooler by the evaporating primary '
                'refrigerant and then pumped to the ice cans or the cold-room coils.',
                '<b>Use:</b> ice plants, cold stores, and any large installation where the load must be '
                'kept away from the ammonia circuit.',
                '<b>Limitation:</b> the brine concentration must be checked, because a weak brine freezes '
                'and a strong one is more viscous and costs more pumping power.'),
        p('<b>Example:</b> an ice plant makes ice in cans standing in a brine tank at −10 °C; the brine is '
          'a calcium chloride solution, and the primary refrigerant ammonia is confined to the machine '
          'room.'),
    ),
    gu=join(
        p('<b>Secondary refrigerant</b> એ પ્રવાહી છે જે primary refrigerantથી ઠંડું થાય અને પછી load પર pump થાય, '
          'જેથી primary circuit machine roomમાં જ રહે. સામાન્ય પ્રકારો:'),
        table(['Secondary refrigerant', 'કામની રેન્જ', 'નોંધ'], [
            ['<b>Calcium chloride brine (CaCl<sub>2</sub>)</b>', 'લગભગ −35 °C સુધી',
             'ice plant અને cold storeનું માનક brine; સસ્તું અને નીચું freezing point, પણ ખૂબ corrosive'],
            ['<b>Sodium chloride brine (NaCl)</b>', 'લગભગ −18 °C સુધી', 'વધુ સસ્તું પણ હળવા તાપમાન સુધી જ, '
             'કારણ કે eutectic −21 °C પર'],
            ['<b>Propylene glycol / ethylene glycol દ્રાવણ</b>', 'લગભગ −30 °C સુધી', 'food plantમાં '
             '(propylene glycol સુરક્ષિત) અને ન થિજે એવા chilled-water systemમાં'],
            ['<b>Chilled water</b>', '5–12 °C', 'air conditioningનું સૌથી સામાન્ય secondary; સસ્તું, ઊંચી '
             'specific heat, પણ 0 °Cથી ઉપર જ'],
            ['<b>Alcohol–water (methanol કે ethanol) મિશ્રણ</b>', 'લગભગ −20 °C સુધી', 'નાના installationમાં '
             'વપરાય; જ્વલનશીલ'],
            ['<b>Air</b>', 'કોઈ પણ', 'air-conditioning duct કે cold storeમાં હવા પોતે heat લઈ જાય; સાદું પણ '
             'મોટા duct જોઈએ'],
        ]),
        h4('સમજ — calcium chloride brine'),
        p('<b>Brine</b> એટલે પાણીમાં ક્ષારનું દ્રાવણ, જે વપરાય કારણ કે ક્ષારના દ્રાવણનું freezing point પાણી '
          'કરતાં ઘણું નીચે હોય. 25 % concentration વાળું calcium chloride brine લગભગ −20 °C પર થિજે, એટલે '
          '−10 °C કે −15 °C પર pipeમાં થિજ્યા વગર heat લઈ જઈ શકે.'),
        bullets('<b>ગુણધર્મ:</b> ઊંચી density અને specific heat, નીચું freezing point, સસ્તું.',
                '<b>Corrosion:</b> brine steel પર ખૂબ હુમલો કરે, એટલે inhibitor ઉમેરાય અને circuit alkaline '
                '(pH 8–9) રાખાય; circuitમાં હવા ઘૂસવા ન દેવી, કારણ કે ઓગળેલો oxygen હુમલો ઘણો વધારે.',
                '<b>Circulation:</b> brine, evaporate થતા primary refrigerantથી brine coolerમાં ઠંડું થાય અને '
                'પછી ice can કે cold-room coil પર pump થાય.',
                '<b>ઉપયોગ:</b> ice plant, cold store, અને જ્યાં loadને ammonia circuitથી દૂર રાખવું હોય એવા '
                'મોટા installation.',
                '<b>મર્યાદા:</b> brineની concentration ચકાસવી પડે, કારણ કે નબળું brine થિજે અને ગાઢ brineની '
                'viscosity વધુ હોવાથી pumping power વધે.'),
        p('<b>ઉદાહરણ:</b> Ice plant −10 °Cના brine tankમાં ઊભેલા canમાં બરફ બનાવે છે; brine calcium chlorideનું '
          'દ્રાવણ છે, અને primary refrigerant ammonia machine roomમાં જ મર્યાદિત રહે છે.'),
    ),
))

Q5['cards'].append(dict(
    number='Q.5 (b)', marks=4, tag='OR', q='Explain COP and TOR',
    en=join(
        h4('COP — coefficient of performance'),
        p('The <b>coefficient of performance</b> of a refrigerator is the heat removed from the cold body '
          'divided by the work supplied to do it:'),
        p('<b>COP = ' + frac('heat absorbed at the evaporator (Q<sub>L</sub>)',
                             'work input to the compressor (W)') + '</b>'),
        p('For a reversible cycle between T<sub>L</sub> (cold) and T<sub>H</sub> (hot), '
          '<b>COP<sub>rev</sub> = ' + frac('T<sub>L</sub>', 'T<sub>H</sub> − T<sub>L</sub>') +
          '</b>, with the temperatures in kelvin. A COP of 4 means 4 units of cooling for 1 unit of work, '
          'which is why a refrigerator can move more heat than the work it takes.'),
        h4('TOR — tonne of refrigeration'),
        p('A <b>tonne of refrigeration (TR or TOR)</b> is the rate of cooling needed to freeze 1 tonne '
          '(1000 kg) of water at 0 °C into ice at 0 °C in 24 hours. It is the practical unit of capacity:'),
        p('<b>1 TR = ' + frac('1000 kg × 334 kJ/kg', '24 × 3600 s') + ' = 3.86 kJ/s ≈ 3.5 kW</b>'),
        p('The latent heat of fusion of ice is 334 kJ/kg. In the older British unit, 1 TR = 12 000 Btu/h = '
          '200 Btu/min = 12000/3.968 = 3024 kcal/h.'),
        h4('Worked example'),
        p('A refrigeration plant of 20 TR capacity works between an evaporator at −10 °C and a condenser at '
          '35 °C, and its actual COP is 55 % of the Carnot COP. Find the cooling load in kW and the power '
          'required.'),
        work('Given: capacity = 20 TR · 1 TR = 3.5 kW · T<sub>L</sub> = −10 °C = 263 K · '
             'T<sub>H</sub> = 35 °C = 308 K · actual COP = 0.55 × COP<sub>rev</sub>',
             'Cooling load Q<sub>L</sub> = 20 × 3.5 = 70 kW',
             'Carnot COP = ' + frac('T<sub>L</sub>', 'T<sub>H</sub> − T<sub>L</sub>') + ' = '
             + frac('263', '308 − 263') + ' = ' + frac('263', '45') + ' = 5.84',
             'Actual COP = 0.55 × 5.84 = 3.21',
             'Work W = ' + frac('Q<sub>L</sub>', 'COP') + ' = ' + frac('70', '3.21')),
        result('Cooling load = 70 kW; compressor power = 21.8 kW'),
        p('Sanity check: 70 kW of cooling for 21.8 kW of power is a COP of 3.2, which is typical of a real '
          'plant in this temperature range, so the answer is consistent.'),
        h4('Why the two are used together'),
        bullets('<b>COP</b> compares the plant with the ideal and shows how good the design and the '
                'operation are; it does not depend on the size of the plant.',
                '<b>TOR</b> is a practical measure of how much cooling the plant can deliver, which is what '
                'the customer buys.',
                'The two together give the power: W = Q<sub>L</sub> / COP. A plant with a low COP for the '
                'same TOR costs more to run, which is why an ammonia plant with COP 4 is preferred to an '
                'old R-12 plant with COP 2.5 for the same duty.'),
    ),
    gu=join(
        h4('COP — coefficient of performance'),
        p('Refrigeratorનો <b>coefficient of performance</b> એટલે ઠંડા પદાર્થમાંથી કાઢેલી heat ભાગ્યા એ કામ '
          'કરવા આપેલી work:'),
        p('<b>COP = ' + frac('evaporatorમાં શોષાયેલી heat (Q<sub>L</sub>)',
                             'compressorને આપેલી work (W)') + '</b>'),
        p('T<sub>L</sub> (ઠંડું) અને T<sub>H</sub> (ગરમ) વચ્ચે reversible cycle માટે '
          '<b>COP<sub>rev</sub> = ' + frac('T<sub>L</sub>', 'T<sub>H</sub> − T<sub>L</sub>') +
          '</b>, તાપમાન kelvinમાં. COP 4 એટલે એક unit work સામે 4 unit cooling, એટલે જ refrigerator જેટલી '
          'work લે એનાથી વધુ heat ખસેડી શકે.'),
        h4('TOR — tonne of refrigeration'),
        p('<b>Tonne of refrigeration (TR કે TOR)</b> એટલે 24 કલાકમાં 1 ટન (1000 kg) પાણીને 0 °C પરથી 0 °Cના '
          'બરફમાં ફેરવવા જરૂરી coolingનો દર. ક્ષમતાનું વ્યવહારુ એકમ:'),
        p('<b>1 TR = ' + frac('1000 kg × 334 kJ/kg', '24 × 3600 s') + ' = 3.86 kJ/s ≈ 3.5 kW</b>'),
        p('બરફની latent heat of fusion 334 kJ/kg છે. જૂના British એકમમાં 1 TR = 12 000 Btu/h = 200 Btu/min '
          '= 3024 kcal/h.'),
        h4('ઉકેલેલું ઉદાહરણ'),
        p('20 TR ક્ષમતાનું plant −10 °Cના evaporator અને 35 °Cના condenser વચ્ચે ચાલે છે, અને એનો ખરો COP '
          'Carnot COPના 55 % છે. Cooling load kWમાં અને જરૂરી power શોધો.'),
        work('Given: capacity = 20 TR · 1 TR = 3.5 kW · T<sub>L</sub> = −10 °C = 263 K · '
             'T<sub>H</sub> = 35 °C = 308 K · ખરો COP = 0.55 × COP<sub>rev</sub>',
             'Cooling load Q<sub>L</sub> = 20 × 3.5 = 70 kW',
             'Carnot COP = ' + frac('T<sub>L</sub>', 'T<sub>H</sub> − T<sub>L</sub>') + ' = '
             + frac('263', '308 − 263') + ' = ' + frac('263', '45') + ' = 5.84',
             'ખરો COP = 0.55 × 5.84 = 3.21',
             'Work W = ' + frac('Q<sub>L</sub>', 'COP') + ' = ' + frac('70', '3.21')),
        result('Cooling load = 70 kW; compressor power = 21.8 kW'),
        p('Sanity check: 21.8 kW power પર 70 kW cooling એ COP 3.2 છે, જે આ તાપમાન રેન્જમાં ખરા plant માટે '
          'સામાન્ય છે, એટલે જવાબ સુસંગત.'),
        h4('બંને ભેગા કેમ વપરાય'),
        bullets('<b>COP</b> plantને આદર્શ સાથે સરખાવે અને design તથા operation કેટલા સારા છે તે દેખાડે; એ '
                'plantના કદ પર આધારિત નથી.',
                '<b>TOR</b> એ વ્યવહારુ માપ છે કે plant કેટલી cooling આપી શકે, જે ગ્રાહક ખરીદે છે.',
                'બંને ભેગા power આપે: W = Q<sub>L</sub> / COP. એ જ TOR પર ઓછા COP વાળા plantનો ખર્ચ વધુ પડે, '
                'એટલે જ એ જ કામ માટે COP 4 વાળું ammonia plant જૂના COP 2.5 વાળા R-12 plant કરતાં પસંદ '
                'પડે.'),
    ),
))

Q5['cards'].append(dict(
    number='Q.5 (c)', marks=7, tag='OR', q='Explain Vapour refrigeration cycle.',
    en=join(
        h4('Definition'),
        p('The <b>vapour-compression refrigeration cycle</b> is the cycle in which a volatile liquid '
          'refrigerant is evaporated at low pressure to absorb heat, the vapour is then compressed, '
          'condensed at high pressure by rejecting heat, and expanded back to the evaporator pressure '
          'through a throttle. It is the cycle used in almost every domestic refrigerator, air conditioner '
          'and industrial chiller.'),
        h4('The four processes'),
        table(['Process', 'From → to', 'What happens'], [
            ['1 → 2 · Compression', 'evaporator to condenser', 'the dry saturated vapour is compressed '
             'isentropically from P<sub>1</sub> to P<sub>2</sub>; the temperature rises above the condenser '
             'temperature'],
            ['2 → 3 · Condensation', 'in the condenser', 'heat Q<sub>H</sub> is rejected at constant '
             'pressure, and the vapour condenses to a liquid'],
            ['3 → 4 · Expansion', 'through the expansion valve', 'the liquid is throttled at constant '
             'enthalpy to the evaporator pressure, and part of it flashes off'],
            ['4 → 1 · Evaporation', 'in the evaporator', 'the wet mixture boils at constant pressure and '
             'temperature, absorbing Q<sub>L</sub> from the space'],
        ]),
        figure(fig.vapour_compression(),
               'Fig. 5.2 · Vapour-compression cycle — compressor, condenser, expansion valve and '
               'evaporator.'),
        h4('Construction — part and purpose'),
        table(['Part', 'Purpose'], [
            ['Compressor', 'raises the pressure from the evaporator to the condenser pressure; it also '
             'circulates the refrigerant'],
            ['Condenser', 'rejects the heat Q<sub>H</sub> = Q<sub>L</sub> + W to the cooling water or air, '
             'and liquefies the refrigerant'],
            ['Expansion valve (or capillary tube)', 'drops the pressure and meters the flow; it also controls '
             'the evaporator filling'],
            ['Evaporator', 'the cooling coil, where the refrigerant boils and takes heat from the space'],
            ['Receiver and drier', 'stores the liquid and removes moisture, which would freeze at the '
             'expansion valve'],
            ['Oil separator and accumulator', 'keeps the oil in the compressor and stops liquid refrigerant '
             'reaching the compressor'],
        ]),
        h4('Working — step and reason'),
        steps(('Step 1', 'The wet vapour in the evaporator absorbs Q<sub>L</sub> and leaves as dry saturated '
                         'vapour at P<sub>1</sub>. Reason: a liquid must evaporate to absorb its latent '
                         'heat, and the vapour must be dry so that no droplets damage the compressor.'),
              ('Step 2', 'The compressor raises the pressure to P<sub>2</sub> and the temperature above the '
                         'condenser temperature. Reason: heat can be rejected to the surroundings only if '
                         'the refrigerant is hotter than the cooling medium.'),
              ('Step 3', 'In the condenser the vapour gives up Q<sub>H</sub> and becomes liquid. Reason: at '
                         'high pressure the saturation temperature is high, so the vapour condenses with '
                         'cooling water at 30–35 °C.'),
              ('Step 4', 'The expansion valve drops the pressure to P<sub>1</sub>, and the liquid partially '
                         'flashes. Reason: the pressure must fall to the evaporator pressure for the '
                         'refrigerant to boil at a low temperature; the work done in the valve is zero, so '
                         'enthalpy stays constant.')),
        h4('Worked example — full cycle calculation'),
        p('An R-134a plant works between an evaporator at −10 °C and a condenser at 40 °C. The enthalpies '
          'are h<sub>1</sub> = 392 kJ/kg, h<sub>2</sub> = 428 kJ/kg, h<sub>3</sub> = h<sub>4</sub> = 249 '
          'kJ/kg. Find the refrigerating effect, the work, the COP and the capacity for a mass flow of '
          '0.15 kg/s.'),
        work('Given: h<sub>1</sub> = 392 kJ/kg · h<sub>2</sub> = 428 kJ/kg · h<sub>3</sub> = '
             'h<sub>4</sub> = 249 kJ/kg · m = 0.15 kg/s · 1 TR = 3.5 kW',
             'Refrigerating effect = h<sub>1</sub> − h<sub>4</sub> = 392 − 249 = 143 kJ/kg',
             'Work of compression = h<sub>2</sub> − h<sub>1</sub> = 428 − 392 = 36 kJ/kg',
             'COP = ' + frac('h<sub>1</sub> − h<sub>4</sub>', 'h<sub>2</sub> − h<sub>1</sub>') + ' = '
             + frac('143', '36') + ' = 3.97',
             'Cooling capacity = m × (h<sub>1</sub> − h<sub>4</sub>) = 0.15 × 143 = 21.45 kW',
             'Capacity in TR = ' + frac('21.45', '3.5') + ' = 6.13 TR'),
        result('COP = 3.97 and capacity ≈ 21.5 kW ≈ 6.1 TR'),
        p('Sanity check: the Carnot COP for 263 K and 313 K is 263/50 = 5.26, and the actual 3.97 is 75 % '
          'of it — a good real plant, so the figures agree.'),
        h4('Advantages and limitations'),
        bullets('The COP is high, so it is the most efficient of the common cycles; the plant is compact, '
                'and the same cycle works for domestic and for large industrial duty.',
                'But it needs a compressor, which has moving parts and needs maintenance, and it is noisy.',
                'The refrigerant must be chosen with care: a CFC damages the ozone layer, an HCFC is being '
                'phased out, and a flammable hydrocarbon needs special precautions.',
                'Wet compression must be avoided, the condenser must not be fouled (or the pressure and '
                'power rise), and a leak of the refrigerant into the plant is a working hazard — the very '
                'reasons that limit the use of a vapour cycle inside a food store, where a secondary '
                'refrigerant is used instead.'),
    ),
    gu=join(
        h4('વ્યાખ્યા'),
        p('<b>Vapour-compression refrigeration cycle</b> એ એ cycle છે જેમાં ઊડતું પ્રવાહી refrigerant નીચા '
          'pressure પર બાષ્પીભવન થઈને heat લે, પછી વરાળ compress થાય, ઊંચા pressure પર heat છોડીને ઘનીભૂત '
          'થાય, અને throttle દ્વારા ફરી evaporatorના pressure પર આવે. લગભગ દરેક ઘરેલું refrigerator, '
          'air conditioner અને ઔદ્યોગિક chillerમાં આ જ cycle વપરાય.'),
        h4('ચાર પ્રક્રિયાઓ'),
        table(['પ્રક્રિયા', 'ક્યાંથી → ક્યાં', 'શું થાય'], [
            ['1 → 2 · Compression', 'evaporator થી condenser', 'dry saturated વરાળ isentropically '
             'P<sub>1</sub>થી P<sub>2</sub> સુધી compress થાય; તાપમાન condenserના તાપમાનથી ઉપર જાય'],
            ['2 → 3 · Condensation', 'condenserમાં', 'અચલ pressure પર heat Q<sub>H</sub> નીકળે અને વરાળ પ્રવાહી '
             'બને'],
            ['3 → 4 · Expansion', 'expansion valveમાંથી', 'પ્રવાહી અચલ enthalpy પર evaporatorના pressure સુધી '
             'throttle થાય, અને એનો ભાગ flash થાય'],
            ['4 → 1 · Evaporation', 'evaporatorમાં', 'wet મિશ્રણ અચલ pressure અને તાપમાને ઉકળે, અને જગ્યામાંથી '
             'Q<sub>L</sub> લે'],
        ]),
        figure(fig.vapour_compression(),
               'Fig. 5.2 · Vapour-compression cycle — compressor, condenser, expansion valve અને evaporator.'),
        h4('રચના — ભાગ અને હેતુ'),
        table(['ભાગ', 'હેતુ'], [
            ['Compressor', 'pressureને evaporatorથી condenserના pressure સુધી લાવે; refrigerantનું circulation '
             'પણ કરે'],
            ['Condenser', 'heat Q<sub>H</sub> = Q<sub>L</sub> + W cooling water કે હવાને આપે અને refrigerantને '
             'પ્રવાહી કરે'],
            ['Expansion valve (કે capillary tube)', 'pressure ઘટાડે અને flow માપે; evaporator ભરાવાનું પણ '
             'નિયંત્રણ કરે'],
            ['Evaporator', 'cooling coil, જ્યાં refrigerant ઉકળીને જગ્યામાંથી heat લે'],
            ['Receiver અને drier', 'પ્રવાહી સંગ્રહે અને ભેજ કાઢે, જે expansion valve પર થિજી જાય'],
            ['Oil separator અને accumulator', 'oil compressorમાં રાખે અને પ્રવાહી refrigerant compressor સુધી '
             'પહોંચતું અટકાવે'],
        ]),
        h4('કાર્ય — સ્ટેપ અને કારણ'),
        steps(('Step 1', 'Evaporatorમાંની wet વરાળ Q<sub>L</sub> લઈને P<sub>1</sub> પર dry saturated વરાળ તરીકે '
                         'નીકળે. કારણ: latent heat લેવા પ્રવાહીએ બાષ્પીભવન થવું પડે, અને વરાળ સૂકી હોવી જોઈએ '
                         'જેથી ટીપાં compressorને નુકસાન ન કરે.'),
              ('Step 2', 'Compressor pressureને P<sub>2</sub> અને તાપમાન condenserના તાપમાનથી ઉપર લાવે. કારણ: '
                         'refrigerant આસપાસના medium કરતાં ગરમ હોય તો જ એને heat આપી શકે.'),
              ('Step 3', 'Condenserમાં વરાળ Q<sub>H</sub> આપીને પ્રવાહી બને. કારણ: ઊંચા pressure પર saturation '
                         'તાપમાન ઊંચું હોય, એટલે 30–35 °Cના cooling water સામે વરાળ ઘનીભૂત થાય.'),
              ('Step 4', 'Expansion valve pressureને P<sub>1</sub> સુધી ઘટાડે અને પ્રવાહીનો ભાગ flash થાય. '
                         'કારણ: refrigerant નીચા તાપમાને ઉકળે એ માટે pressure evaporatorના pressure સુધી '
                         'ઘટવું જોઈએ; valveમાં કોઈ work થતું નથી, એટલે enthalpy અચલ રહે.')),
        h4('ઉકેલેલું ઉદાહરણ — આખા cycleની ગણતરી'),
        p('R-134aનું plant −10 °Cના evaporator અને 40 °Cના condenser વચ્ચે ચાલે છે. Enthalpy '
          'h<sub>1</sub> = 392 kJ/kg, h<sub>2</sub> = 428 kJ/kg અને h<sub>3</sub> = h<sub>4</sub> = '
          '249 kJ/kg છે. 0.15 kg/sના mass flow માટે refrigerating effect, work, COP અને capacity શોધો.'),
        work('Given: h<sub>1</sub> = 392 kJ/kg · h<sub>2</sub> = 428 kJ/kg · h<sub>3</sub> = '
             'h<sub>4</sub> = 249 kJ/kg · m = 0.15 kg/s · 1 TR = 3.5 kW',
             'Refrigerating effect = h<sub>1</sub> − h<sub>4</sub> = 392 − 249 = 143 kJ/kg',
             'Work of compression = h<sub>2</sub> − h<sub>1</sub> = 428 − 392 = 36 kJ/kg',
             'COP = ' + frac('h<sub>1</sub> − h<sub>4</sub>', 'h<sub>2</sub> − h<sub>1</sub>') + ' = '
             + frac('143', '36') + ' = 3.97',
             'Cooling capacity = m × (h<sub>1</sub> − h<sub>4</sub>) = 0.15 × 143 = 21.45 kW',
             'TRમાં capacity = ' + frac('21.45', '3.5') + ' = 6.13 TR'),
        result('COP = 3.97 અને capacity ≈ 21.5 kW ≈ 6.1 TR'),
        p('Sanity check: 263 K અને 313 K માટે Carnot COP 263/50 = 5.26 છે, અને ખરો 3.97 એ એના 75 % છે — '
          'સારું ખરું plant, એટલે આંકડા મળે.'),
        h4('ફાયદા અને મર્યાદાઓ'),
        bullets('<b>COP ઊંચો</b>, એટલે સામાન્ય cycleમાં સૌથી કાર્યક્ષમ; plant compact, અને એ જ cycle ઘરેલું '
                'તથા મોટા ઔદ્યોગિક કામ બંને માટે ચાલે.',
                'પણ compressor જોઈએ, જેમાં ફરતા ભાગ હોય અને maintenance જોઈએ, તથા અવાજ કરે.',
                'Refrigerant કાળજીપૂર્વક પસંદ કરવો પડે: CFC ozone સ્તર બગાડે, HCFC બંધ થઈ રહ્યું છે, અને '
                'જ્વલનશીલ hydrocarbon માટે ખાસ સાવધાની જોઈએ.',
                'Wet compression ટાળવું પડે, condenser ગંદું ન થવું જોઈએ (નહીં તો pressure અને power વધે), અને '
                'refrigerant leak કામનું જોખમ છે — એટલે જ food storeની અંદર vapour cycle ન વાપરતાં secondary '
                'refrigerant વપરાય.'),
    ),
))
