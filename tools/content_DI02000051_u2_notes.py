"""DI02000051 Environmental Sustainability - Unit 2: Waste Management and Pollution Control.

GTU 2.1-2.5, 7 h, 25 %, 18 marks, CO2. Every text node carries English and Gujarati.
"""
from content_DI02000051_u1_notes import T, P, H4, UL, OL, TB, card, num, _join

SOURCES = [
    T("GTU DI02000051 Environmental Sustainability syllabus (uploaded PDF, w.e.f. 2024-25)",
      "GTU DI02000051 પર્યાવરણીય ટકાઉપણું સિલેબસ (અપલોડ કરેલ PDF, 2024-25થી અમલમાં)"),
    T("Aloka Debi - Environmental Science and Engineering, chapter on pollution and waste",
      "અલોકા દેબી - એન્વાયર્નમેન્ટલ સાયન્સ એન્ડ એન્જિનિયરિંગ, પ્રદૂષણ અને કચરાનું પ્રકરણ"),
    T("G. R. Chhatwal et al. - Environmental Noise Pollution and Its Control, Anmol Publications",
      "જી. આર. છત્વાલ અને સાથી - એન્વાયર્નમેન્ટલ નોઇઝ પોલ્યુશન એન્ડ ઇટ્સ કંટ્રોલ, અનમોલ પબ્લિકેશન્સ"),
    T("CPCB - Manual on municipal solid waste management and noise standards",
      "CPCB - નગરપાલિકા ઘન કચરા વ્યવસ્થાપન પરની માર્ગદર્શિકા અને ઘોંઘાટના ધોરણો"),
    T("MoEFCC - Solid Waste Management Rules 2016, Plastic Waste Rules 2016, E-Waste Rules",
      "MoEFCC - ઘન કચરા વ્યવસ્થાપન નિયમો 2016, પ્લાસ્ટિક કચરા નિયમો 2016, ઇ-કચરા નિયમો"),
]

NOTES = [
    {"title": T("1. Air Pollution and its Control", "1. વાયુ પ્રદૂષણ અને તેનું નિયંત્રણ"),
     "items": [
         card(T("2.1 Air pollution: what it is, how it is classified and where it comes from",
                "2.1 વાયુ પ્રદૂષણ: તે શું છે, કેવી રીતે વર્ગીકૃત થાય અને ક્યાંથી આવે"),
              [H4("Definition", "વ્યાખ્યા"),
               P("<b>Air pollution</b> is the presence in the outdoor or indoor air of one or more "
                 "substances - gases, fine particles or biological material - in a concentration that "
                 "harms people, animals, plants or materials. The substance is a <b>pollutant</b>, its "
                 "source is the <b>emitter</b> and the amount released per hour is the <b>emission "
                 "rate</b>.",
                 "<b>વાયુ પ્રદૂષણ</b> એટલે બહારની કે અંદરની હવામાં એવા પદાર્થોની હાજરી - વાયુઓ, બારીક "
                 "કણો કે જૈવિક દ્રવ્ય - જેની સાંદ્રતા માણસ, પ્રાણી, છોડ કે વસ્તુને નુકસાન પહોંચાડે. પદાર્થ "
                 "<b>પ્રદૂષક</b>, તેનું સ્થળ <b>ઉત્સર્જક</b> અને કલાક દીઠ છૂટું પ્રમાણ <b>ઉત્સર્જન દર</b> છે."),
               H4("Classification", "વર્ગીકરણ"),
               TB([T("Basis", "આધાર"), T("Types", "પ્રકાર"), T("Example", "ઉદાહરણ")],
                  [[T("how formed", "કેવી રીતે બને"), T("primary - emitted as such", "પ્રાથમિક - જેમ છે તેમ નીકળે"), T("SO₂ from coal, CO from vehicles", "કોલસામાંથી SO₂, વાહનોમાંથી CO")],
                   [T("how formed", "કેવી રીતે બને"), T("secondary - formed in the air", "દ્વિતીય - હવામાં બને"), T("ozone, sulphuric acid mist, PAN", "ઓઝોન, સલ્ફ્યુરિક એસિડ ધુમ્મસ")],
                   [T("origin", "ઉદ્ગમ"), T("natural / anthropogenic", "કુદરતી / માનવજન્ય"), T("volcano vs a chimney", "જ્વાળામુખી સામે ચીમની")],
                   [T("shape of source", "સ્રોતનો આકાર"), T("point, line, area", "બિંદુ, રેખા, વિસ્તાર"), T("chimney, highway, landfill", "ચીમની, ધોરીમાર્ગ, કચરાભરાવ")],
                   [T("physical state", "ભૌતિક સ્થિતિ"), T("gaseous / particulate", "વાયુરૂપ / કણરૂપ"), T("NOx vs fly ash and PM2.5", "NOx સામે ફ્લાય એશ અને PM2.5")]]),
               H4("Main pollutants and their effect", "મુખ્ય પ્રદૂષકો અને તેમની અસર"),
               TB([T("Pollutant", "પ્રદૂષક"), T("Main source", "મુખ્ય સ્રોત"), T("Effect", "અસર")],
                  [[T("PM10 / PM2.5", "PM10 / PM2.5"), T("dust, diesel, construction, burning", "ધૂળ, ડીઝલ, બાંધકામ, બળવું"), T("lung and heart disease; the deadliest pollutant", "ફેફસાં અને હૃદયના રોગ; સૌથી ઘાતક પ્રદૂષક")],
                   [T("SO₂", "SO₂"), T("coal and oil with sulphur", "સલ્ફરવાળો કોલસો અને તેલ"), T("acid rain, corrosion, breathing difficulty", "એસિડ વરસાદ, કાટ, શ્વાસમાં તકલીફ")],
                   [T("NOx", "NOx"), T("vehicles and high-temperature furnaces", "વાહનો અને ઊંચા તાપમાનની ભઠ્ઠી"), T("smog, ozone, respiratory damage", "ધૂમ્મસ, ઓઝોન, શ્વસનને નુકસાન")],
                   [T("CO", "CO"), T("incomplete combustion, idling engines", "અપૂર્ણ દહન, બિનજરૂરી એન્જિન"), T("binds haemoglobin, heart strain", "હિમોગ્લોબિન સાથે જોડાય, હૃદય પર ભાર")],
                   [T("CO₂", "CO₂"), T("every fuel fire", "દરેક ઇંધણની આગ"), T("greenhouse gas, climate change", "હરિતગૃહ વાયુ, જળવાયુ પરિવર્તન")],
                   [T("VOC, benzene", "VOC, બેન્ઝિન"), T("paints, solvents, petrol", "રંગ, દ્રાવક, પેટ્રોલ"), T("cancer risk, ground-level ozone", "કેન્સરનું જોખમ, જમીન પાસે ઓઝોન")]]),
               H4("Worked example", "ઉકેલાયેલ દાખલો"),
               P("A 500 MW coal station burning 3,000 t of coal a day with 1 % sulphur sends out 3,000 × "
                 "0.01 = 30 t of sulphur a day, which becomes 60 t of SO₂ - enough to make the rain of a "
                 "whole district acidic without a desulphurisation unit.",
                 "રોજ 3,000 ટન કોલસો બાળતું 500 MW સ્ટેશન, જેમાં 1 % સલ્ફર છે, રોજ 3,000 × 0.01 = 30 ટન "
                 "સલ્ફર છોડે, જે 60 ટન SO₂ બને - ડિસલ્ફરાઇઝેશન યુનિટ વગર આખા જિલ્લાનો વરસાદ એસિડિક કરવા પૂરતું."),
               H4("Common mistake", "સામાન્ય ભૂલ"),
               P("Judging air quality by the smoke you can see. PM2.5, ozone, NO₂ and CO are invisible, "
                 "and they cause most of the health damage; a clear plume is not clean air.",
                 "દેખાતા ધુમાડાથી હવાની ગુણવત્તા માપવી. PM2.5, ઓઝોન, NO₂ અને CO અદૃશ્ય છે અને તે જ "
                 "મોટાભાગનું આરોગ્ય નુકસાન કરે; સ્વચ્છ દેખાતી ચીમની એટલે સ્વચ્છ હવા નહીં.")],
              "u2_air", syllabus_item="2.1"),
         card(T("2.1 Air pollution control equipment and how to choose it",
                "2.1 વાયુ પ્રદૂષણ નિયંત્રણનાં સાધનો અને તેમની પસંદગી"),
              [H4("Three places to act", "કાર્ય કરવાની ત્રણ જગ્યા"),
               OL(("Prevention at the process: cleaner fuel, low-NOx burner, good combustion, no leaks.",
                   "પ્રક્રિયા પર જ અટકાવ: સ્વચ્છ ઇંધણ, ઓછા NOx વાળું બર્નર, સારું દહન, ગળતર નહીં."),
                  ("Collection of the pollutant before it leaves the stack - the control equipment.",
                   "ચીમની છોડે તે પહેલાં પ્રદૂષકનું સંગ્રહ - નિયંત્રણ સાધન."),
                  ("Dispersion through a tall stack for what remains, never as a substitute for control.",
                   "બાકી રહેલા ભાગ માટે ઊંચી ચીમની દ્વારા વિખેરણ, પણ નિયંત્રણનો વિકલ્પ કદી નહીં.")),
               H4("Particulate collectors", "કણ સંગ્રહક"),
               TB([T("Device", "સાધન"), T("Works by", "કેવી રીતે કામ કરે"), T("Best for", "ક્યાં ઉત્તમ")],
                  [[T("settling chamber", "અવસાદન કક્ષ"), T("gravity, the gas slows and dust falls", "ગુરુત્વાકર્ષણ, વાયુ ધીમો પડે ને ધૂળ પડે"), T("particles above 50 µm", "50 µm થી મોટા કણ")],
                   [T("cyclone separator", "સાયક્લોન વિભાજક"), T("centrifugal force in a spinning gas", "ફરતા વાયુમાં કેન્દ્રત્યાગી બળ"), T("10-50 µm, coarse dust", "10-50 µm, જાડી ધૂળ")],
                   [T("bag filter (fabric)", "બેગ ફિલ્ટર (કાપડ)"), T("dust is trapped on filter cloth", "ધૂળ કાપડ પર અટકે"), T("1-10 µm, very high efficiency", "1-10 µm, ખૂબ ઊંચી કાર્યક્ષમતા")],
                   [T("electrostatic precipitator", "ઇલેક્ટ્રોસ્ટેટિક પ્રિસિપિટેટર"), T("particles are charged and pulled to plates", "કણ વીજભારિત થઈ પ્લેટ તરફ ખેંચાય"), T("sub-micron, large gas volumes", "સૂક્ષ્મ કણ, મોટા વાયુ પ્રમાણ")],
                   [T("wet scrubber", "વેટ સ્ક્રબર"), T("water droplets wash the gas", "પાણીના ટીપાં વાયુને ધોઈ નાખે"), T("dust plus soluble gas and cooling", "ધૂળ સાથે દ્રાવ્ય વાયુ અને ઠંડક")]]),
               H4("Gaseous pollutants", "વાયુરૂપ પ્રદૂષકો"),
               P("SO₂ is removed by <b>flue gas desulphurisation</b> - lime slurry absorbs it and gives "
                 "gypsum, which goes to cement; NOx by low-NOx burners, staged combustion or selective "
                 "catalytic reduction with ammonia; CO and VOC by a well-run furnace or an afterburner.",
                 "SO₂ <b>ફ્લુ ગેસ ડિસલ્ફરાઇઝેશન</b> થી દૂર થાય - ચૂનાનું દ્રાવણ શોષે અને જિપ્સમ આપે, જે "
                 "સિમેન્ટમાં જાય; NOx ઓછા-NOx બર્નર, તબક્કાવાર દહન કે એમોનિયા સાથે SCR થી; CO અને VOC સારી "
                 "ભઠ્ઠી કે આફ્ટરબર્નર થી."),
               H4("Worked example", "ઉકેલાયેલ દાખલો"),
               P("Dust in a flue is 12 g/m³ at the inlet and 0.6 g/m³ after the cyclone, so the cyclone "
                 "removes (12 − 0.6)/12 = 95 %. A bag filter after it would take the same gas below "
                 "0.03 g/m³ and meet the standard (limit 0.05 g/m³).",
                 "ચીમનીમાં ધૂળ પ્રવેશે 12 g/m³ અને સાયક્લોન પછી 0.6 g/m³, તેથી સાયક્લોન (12 − 0.6)/12 = "
                 "95 % દૂર કરે. તે પછીનું બેગ ફિલ્ટર એ જ વાયુને 0.03 g/m³ થી નીચે લાવે અને ધોરણ "
                 "(મર્યાદા 0.05 g/m³) પૂરું કરે."),
               H4("Common mistake", "સામાન્ય ભૂલ"),
               P("Buying a collector by price alone. Efficiency depends on particle size and gas "
                 "temperature: a bag filter fails on sticky, moist dust and an ESP loses efficiency when "
                 "the gas is cold or the sulphur is high.",
                 "ફક્ત ભાવ જોઈ સાધન ખરીદવું. કાર્યક્ષમતા કણના કદ અને વાયુના તાપમાન પર આધારિત છે: ચીકણી, "
                 "ભીની ધૂળમાં બેગ ફિલ્ટર નિષ્ફળ જાય અને ઠંડા વાયુ કે વધુ સલ્ફરમાં ESP ની કાર્યક્ષમતા ઘટે.")],
              "u2_control", syllabus_item="2.1"),
     ]},

    {"title": T("2. Water Pollution and Wastewater Treatment",
                "2. જળ પ્રદૂષણ અને ગંદા પાણીની સારવાર"),
     "items": [
         card(T("2.2 Water pollution parameters: BOD, COD, pH, TSS, turbidity and total solids",
                "2.2 જળ પ્રદૂષણના માપદંડ: BOD, COD, pH, TSS, ગંદલાશ અને કુલ ઘન"),
              [H4("Why we measure instead of looking", "જોવાને બદલે માપ કેમ"),
               P("Clean-looking water can carry a heavy organic load. Six measurements tell an engineer "
                 "almost everything about a sample: how much oxygen the microbes will take (BOD), how "
                 "much reducing matter is present (COD), how acidic it is (pH), how much solid is "
                 "suspended, how cloudy it is and how much solid is dissolved.",
                 "ચોખ્ખું દેખાતું પાણી ભારે કાર્બનિક ભાર વહન કરી શકે. છ માપ ઇજનેરને નમૂના વિશે લગભગ બધું "
                 "કહી દે: સૂક્ષ્મજીવો કેટલો ઓક્સિજન લેશે (BOD), કેટલું ક્ષયકારક દ્રવ્ય છે (COD), કેટલું "
                 "એસિડિક છે (pH), કેટલું ઘન તરે છે, કેટલું ગંદું દેખાય છે અને કેટલું ઘન ઓગળેલું છે."),
               H4("The six parameters", "છ માપદંડ"),
               TB([T("Parameter", "માપદંડ"), T("What it means", "તેનો અર્થ"), T("Typical limit", "સામાન્ય મર્યાદા")],
                  [[T("pH", "pH"), T("acidity or alkalinity on a 0-14 scale", "0-14 પ્રમાણમાં એસિડિકતા કે આલ્કલાઇનતા"), T("6.5 to 8.5 for discharge", "છોડવા માટે 6.5 થી 8.5")],
                   [T("BOD₅", "BOD₅"), T("oxygen consumed by microbes in 5 days at 20 °C, mg/L", "20 °C પર 5 દિવસમાં સૂક્ષ્મજીવો લેતો ઓક્સિજન, mg/L"), T("30 mg/L into a river, 20 into land", "નદીમાં 30 mg/L, જમીન પર 20")],
                   [T("COD", "COD"), T("oxygen needed to oxidise everything chemically, mg/L", "બધું રાસાયણિક રીતે ઓક્સિડાઇઝ કરવા જરૂરી ઓક્સિજન, mg/L"), T("250 mg/L", "250 mg/L")],
                   [T("TSS", "TSS"), T("solids that a filter catches, mg/L", "ફિલ્ટર પકડે તે ઘન, mg/L"), T("100 mg/L", "100 mg/L")],
                   [T("turbidity", "ગંદલાશ"), T("cloudiness from suspended particles, NTU", "તરતા કણોને કારણે ધૂંધળાશ, NTU"), T("10 NTU for a river body", "નદી માટે 10 NTU")],
                   [T("total solids", "કુલ ઘન"), T("suspended plus dissolved solids, mg/L", "તરતા અને ઓગળેલા ઘનનો સરવાળો, mg/L"), T("set by the use of the water", "પાણીના ઉપયોગ પ્રમાણે")]]),
               H4("Reading BOD against COD", "BOD અને COD સાથે વાંચવું"),
               P("The <b>BOD/COD ratio</b> says how biodegradable the waste is. Above 0.5 the waste is "
                 "easily treated by microbes (a biological plant will work); around 0.2-0.3 it is only "
                 "partly biodegradable and needs chemical help; below 0.1 the waste is largely "
                 "inorganic or toxic.",
                 "<b>BOD/COD ગુણોત્તર</b> કચરો કેટલો જૈવવિઘટનીય છે તે કહે. 0.5 થી વધુ હોય તો કચરો સૂક્ષ્મજીવો "
                 "દ્વારા સહેલાઈથી સારવાર પામે (જૈવિક પ્લાન્ટ ચાલશે); 0.2-0.3 આસપાસ તે અંશતઃ જ જૈવવિઘટનીય છે "
                 "અને રાસાયણિક મદદ જોઈએ; 0.1 થી નીચે કચરો મોટે ભાગે અકાર્બનિક કે ઝેરી છે."),
               H4("Worked example", "ઉકેલાયેલ દાખલો"),
               P("A dye house effluent reads BOD 240 mg/L and COD 400 mg/L, so BOD/COD = 0.6: the waste "
                 "is mainly organic and an activated sludge plant will remove it. The same works reads "
                 "BOD 20 and COD 900 on a dye-heavy day (ratio 0.02), and the biology collapses - that "
                 "stream must be segregated and treated chemically.",
                 "રંગાઈના ગંદા પાણીમાં BOD 240 mg/L અને COD 400 mg/L છે, તેથી BOD/COD = 0.6: કચરો મુખ્યત્વે "
                 "કાર્બનિક છે અને એક્ટિવેટેડ સ્લજ પ્લાન્ટ તેને દૂર કરશે. રંગ વધુ હોય તેવા દિવસે એ જ કારખાનામાં "
                 "BOD 20 અને COD 900 (ગુણોત્તર 0.02) થાય અને જૈવિક તંત્ર ખસી પડે - તે પ્રવાહ અલગ કરી "
                 "રાસાયણિક સારવાર આપવી પડે."),
               H4("Common mistake", "સામાન્ય ભૂલ"),
               P("Treating pH as a minor reading. Untreated effluent at pH 10 kills the bacteria of the "
                 "treatment plant itself, so an alkaline stream neutralised at the source protects the "
                 "whole plant downstream.",
                 "pH ને નાની બાબત ગણવી. pH 10 નું કાચું પાણી સારવાર પ્લાન્ટના જીવાણુઓને મારી નાખે, તેથી "
                 "સ્રોત પર જ આલ્કલાઇન પ્રવાહ ન્યુટ્રલ કરવો આખા પ્લાન્ટને બચાવે.")],
              None, syllabus_item="2.2"),
         card(T("2.3 Wastewater treatment: primary, secondary and tertiary",
                "2.3 ગંદા પાણીની સારવાર: પ્રાથમિક, દ્વિતીય અને તૃતીય"),
              [H4("The three stages", "ત્રણ તબક્કા"),
               TB([T("Stage", "તબક્કો"), T("Removes", "દૂર કરે"), T("Units used", "વપરાતા એકમો")],
                  [[T("preliminary", "પ્રારંભિક"), T("rags, grit, oil and grease", "ચીંથરાં, રેતી, તેલ અને ચરબી"), T("bar screen, grit chamber, oil trap", "બાર સ્ક્રીન, ગ્રિટ ચેમ્બર, તેલ જાળ")],
                   [T("primary", "પ્રાથમિક"), T("settleable solids, 50-65 % of TSS", "બેસતા ઘન, TSS ના 50-65 %"), T("primary clarifier; chemical dosing if needed", "પ્રાથમિક સેટલિંગ ટાંકી; જરૂર પડે તો રસાયણ")],
                   [T("secondary", "દ્વિતીય"), T("dissolved organic matter, 85-95 % of BOD", "ઓગળેલું કાર્બનિક દ્રવ્ય, BOD ના 85-95 %"), T("activated sludge, trickling filter, UASB, oxidation pond", "એક્ટિવેટેડ સ્લજ, ટ્રિકલિંગ ફિલ્ટર, UASB, ઓક્સિડેશન પોન્ડ")],
                   [T("tertiary", "તૃતીય"), T("nutrients, colour, salts, pathogens", "પોષકતત્વો, રંગ, ક્ષાર, રોગકારક"), T("chemical precipitation, filtration, activated carbon, UV or chlorination", "રાસાયણિક અવક્ષેપન, ફિલ્ટર, એક્ટિવેટેડ કાર્બન, UV કે ક્લોરિનેશન")]]),
               H4("How the secondary stage works", "દ્વિતીય તબક્કો કેવી રીતે કામ કરે"),
               P("In <b>activated sludge</b> the settled sewage meets a dense culture of bacteria in an "
                 "aeration tank; air (or pure oxygen) is blown in, the bacteria eat the organic matter "
                 "and grow, and the flow then passes to a second clarifier where the sludge settles. "
                 "Part of that sludge is returned to keep the culture alive, the rest is wasted and "
                 "thickened. A <b>UASB</b> reactor does the same job anaerobically and produces biogas, "
                 "which suits warm Indian climates and strong effluent.",
                 "<b>એક્ટિવેટેડ સ્લજ</b>માં બેસી ગયેલું ગંદું પાણી એરેશન ટાંકીમાં જીવાણુઓની ગીચ સંસ્કૃતિ "
                 "સાથે મળે; હવા (કે શુદ્ધ ઓક્સિજન) ફૂંકાય, જીવાણુ કાર્બનિક દ્રવ્ય ખાઈને વધે, અને પ્રવાહ પછી "
                 "બીજી સેટલિંગ ટાંકીમાં જાય જ્યાં સ્લજ બેસે. તેમાંથી ભાગ સંસ્કૃતિ જીવતી રાખવા પાછો મોકલાય, "
                 "બાકીનો કાઢી ઘટ્ટ કરાય. <b>UASB</b> રિએક્ટર એ જ કામ વાયુરહિત રીતે કરે અને બાયોગેસ આપે, જે "
                 "ગરમ ભારતીય હવામાન અને ભારે ગંદા પાણી માટે યોગ્ય છે."),
               H4("Worked example", "ઉકેલાયેલ દાખલો"),
               P("A plant receives 2 MLD with BOD 300 mg/L. The load is 2,000 m³ × 0.3 kg/m³ = 600 kg of "
                 "BOD a day. With a primary clarifier taking 30 % and a secondary stage taking 90 % of "
                 "the rest, the outlet carries 600 × 0.7 × 0.1 = 42 kg/day, i.e. 21 mg/L - inside the "
                 "30 mg/L standard.",
                 "પ્લાન્ટમાં રોજ 2 MLD પાણી BOD 300 mg/L સાથે આવે. ભાર 2,000 m³ × 0.3 kg/m³ = 600 kg BOD "
                 "રોજ. પ્રાથમિક ટાંકી 30 % અને દ્વિતીય તબક્કો બાકીનામાંથી 90 % લે તો બહાર જતું પાણી "
                 "600 × 0.7 × 0.1 = 42 kg/રોજ એટલે 21 mg/L વહન કરે - 30 mg/L ધોરણમાં."),
               H4("Common mistake", "સામાન્ય ભૂલ"),
               P("Adding a tertiary stage to fix an overloaded biological plant. If the aeration tank is "
                 "too small or the sludge has been poisoned, no filter at the end will bring the BOD "
                 "down; fix the biology first.",
                 "ભારે ભરાયેલા જૈવિક પ્લાન્ટને સુધારવા તૃતીય તબક્કો ઉમેરવો. એરેશન ટાંકી નાની હોય કે સ્લજ "
                 "ઝેરી થઈ ગયો હોય તો અંતે કોઈ ફિલ્ટર BOD નીચે લાવશે નહીં; પહેલાં જૈવિક ભાગ સુધારો.")],
              "u2_wwt", syllabus_item="2.3"),
     ]},

    {"title": T("3. Solid Waste, its Collection and Disposal",
                "3. ઘન કચરો, તેનો સંગ્રહ અને નિકાલ"),
     "items": [
         card(T("2.3 Solid waste: generation, sources and characteristics",
                "2.3 ઘન કચરો: ઉત્પાદન, સ્રોત અને લક્ષણો"),
              [H4("Sources", "સ્રોત"),
               TB([T("Source", "સ્રોત"), T("What it gives", "તે શું આપે"), T("Share of city waste", "શહેરના કચરામાં હિસ્સો")],
                  [[T("residential", "રહેણાંક"), T("kitchen waste, paper, plastic, glass", "રસોડાનો કચરો, કાગળ, પ્લાસ્ટિક, કાચ"), T("50-60 %", "50-60 %")],
                   [T("commercial", "વ્યાપારી"), T("shops, hotels, markets, packaging", "દુકાનો, હોટેલ, બજાર, પેકિંગ"), T("20-30 %", "20-30 %")],
                   [T("institutional", "સંસ્થાકીય"), T("schools, offices, hospitals (infectious!)", "શાળા, કચેરી, હોસ્પિટલ (ચેપી!)"), T("5-10 %", "5-10 %")],
                   [T("construction and demolition", "બાંધકામ અને તોડી પાડવાનો"), T("concrete, bricks, timber, debris", "કોંક્રિટ, ઈંટ, લાકડું, કચરો"), T("varies with the city", "શહેર પ્રમાણે બદલાય")],
                   [T("industrial", "ઔદ્યોગિક"), T("process scrap, sludge, ash", "પ્રક્રિયાનો ભંગાર, કાદવ, રાખ"), T("handled by the industry", "ઉદ્યોગ પોતે સંભાળે")]]),
               H4("Characteristics that decide the route", "કયો રસ્તો લેવો તે નક્કી કરતાં લક્ષણો"),
               UL(("<b>Moisture</b>: Indian municipal waste is 40-60 % water, which kills incineration "
                   "unless it is dried or segregated first.",
                   "<b>ભેજ</b>: ભારતીય નગરપાલિકા કચરામાં 40-60 % પાણી હોય છે, જે પહેલાં સૂકવ્યા કે અલગ કર્યા "
                   "વગર દહનને નિષ્ફળ બનાવે."),
                  ("<b>Calorific value</b>: wet mixed waste gives 800-1,100 kcal/kg, while dry paper and "
                   "plastic fractions reach 2,500 kcal/kg and can be burnt or made into RDF.",
                   "<b>ઉષ્મા મૂલ્ય</b>: ભીનો મિશ્ર કચરો 800-1,100 kcal/kg આપે, જ્યારે સૂકા કાગળ-પ્લાસ્ટિકનો "
                   "ભાગ 2,500 kcal/kg સુધી પહોંચે અને બાળી શકાય કે RDF બનાવી શકાય."),
                  ("<b>C/N ratio</b>: composting works best at 25-30; too much carbon slows it, too much "
                   "nitrogen releases ammonia and smell.",
                   "<b>C/N ગુણોત્તર</b>: કમ્પોસ્ટ 25-30 પર શ્રેષ્ઠ ચાલે; કાર્બન વધુ હોય તો ધીમું પડે, નાઇટ્રોજન "
                   "વધુ હોય તો એમોનિયા અને દુર્ગંધ નીકળે."),
                  ("<b>Bulk density</b>: loose mixed waste is 250-400 kg/m³, which sets the number of "
                   "trips and the size of the collection vehicle.",
                   "<b>થોક ઘનતા</b>: ઢીલો મિશ્ર કચરો 250-400 kg/m³ હોય, જે ગાડીઓની સંખ્યા અને કદ નક્કી કરે.")),
               H4("Worked example", "ઉકેલાયેલ દાખલો"),
               P("A town of 5 lakh people generating 0.45 kg per person a day produces 225 t of waste a "
                 "day. At a bulk density of 0.4 t/m³ that is about 560 m³ a day, or 23 tipper loads of "
                 "25 m³ - the number the municipal engineer must plan collection for.",
                 "5 લાખ લોકોનું નગર, પ્રતિ વ્યક્તિ રોજ 0.45 kg કચરો પેદા કરે, તો રોજ 225 ટન કચરો બને. "
                 "0.4 t/m³ થોક ઘનતા પર તે લગભગ 560 m³ રોજ, એટલે 25 m³ ની 23 ટિપર - નગરપાલિકાના ઇજનેરે આટલી "
                 "ગાડીઓનું આયોજન કરવું પડે."),
               H4("Common mistake", "સામાન્ય ભૂલ"),
               P("Designing an incinerator for Indian waste as if it were European waste. At 45 % moisture "
                 "and 1,000 kcal/kg the plant needs auxiliary fuel all year and becomes an expensive "
                 "failure.",
                 "ભારતીય કચરા માટે યુરોપીયન કચરાની જેમ ભઠ્ઠી ડિઝાઇન કરવી. 45 % ભેજ અને 1,000 kcal/kg પર "
                 "પ્લાન્ટને આખું વર્ષ સહાયક ઇંધણ જોઈએ અને તે મોંઘી નિષ્ફળતા બને.")],
              "u2_msw", syllabus_item="2.3"),
         card(T("2.4 Collection, disposal of municipal solid waste and hazardous waste",
                "2.4 નગરપાલિકા ઘન કચરા અને જોખમી કચરાનો સંગ્રહ તથા નિકાલ"),
              [H4("The collection chain", "સંગ્રહની શૃંખલા"),
               OL(("Segregation at the source into wet, dry and domestic hazardous - the single step "
                   "that decides the fate of everything downstream.",
                   "સ્રોત પર જ ભીનો, સૂકો અને ઘરેલું જોખમી કચરો અલગ કરવો - આ જ એક પગલું નીચેની આખી પ્રક્રિયાનો "
                   "નિર્ણય કરે."),
                  ("Door-to-door collection in covered bins, with a route sheet and a fixed time.",
                   "ઢાંકેલા ડબ્બામાં ઘરે-ઘરે સંગ્રહ, રૂટ શીટ અને નિશ્ચિત સમય સાથે."),
                  ("Transfer station and transfer vehicle for long hauls, so the small vehicles are not "
                   "wasted on the highway.", "લાંબા અંતર માટે ટ્રાન્સફર સ્ટેશન અને મોટી ગાડી, જેથી નાની ગાડીઓ "
                   "ધોરીમાર્ગ પર ન વેડફાય."),
                  ("Treatment by what the stream allows: composting or biogas for wet waste, recycling "
                   "for dry waste, RDF or incineration only for dry high-calorific waste.",
                   "પ્રવાહ પ્રમાણે સારવાર: ભીનો કચરો કમ્પોસ્ટ કે બાયોગેસમાં, સૂકો રિસાયકલમાં, RDF કે દહન ફક્ત "
                   "સૂકા ઊંચા ઉષ્મા મૂલ્યવાળા કચરા માટે."),
                  ("Sanitary landfill for inert rejects only - a lined, daily-covered cell, never an "
                   "open dump.", "ફક્ત નિષ્ક્રિય અવશેષો માટે સેનિટરી લેન્ડફિલ - આંતરિક અસ્તરવાળું, રોજ ઢાંકેલું "
                   "કોષ, કદી ખુલ્લો ઢગલો નહીં.")),
               H4("Routes compared", "રસ્તાઓની સરખામણી"),
               TB([T("Route", "રસ્તો"), T("Good for", "ક્યાં સારો"), T("Watch out for", "સાવધાની")],
                  [[T("composting / vermicomposting", "કમ્પોસ્ટ / વર્મીકમ્પોસ્ટ"), T("wet kitchen waste", "ભીનો રસોડાનો કચરો"), T("smell and leachate if turned badly", "ખરાબ ઉથલાવો તો દુર્ગંધ અને લીચેટ")],
                   [T("biogas (anaerobic digestion)", "બાયોગેસ (વાયુરહિત પાચન)"), T("wet waste in a campus or market", "કેમ્પસ કે બજારનો ભીનો કચરો"), T("digestate needs a user nearby", "પાચિત કાદવનો નજીકમાં વપરાશકર્તા જોઈએ")],
                   [T("recycling", "રિસાયકલિંગ"), T("paper, metal, glass, PET", "કાગળ, ધાતુ, કાચ, PET"), T("mixed or dirty material has no buyer", "મિશ્ર કે ગંદા માલનો ખરીદનાર ન મળે")],
                   [T("sanitary landfill", "સેનિટરી લેન્ડફિલ"), T("inert rejects and process residue", "નિષ્ક્રિય અવશેષ અને પ્રક્રિયાનો કચરો"), T("leachate and methane if unlined", "અસ્તર વગર લીચેટ અને મિથેન")],
                   [T("incineration / RDF", "દહન / RDF"), T("dry high-calorific waste, hospital waste", "સૂકો ઊંચા ઉષ્મા મૂલ્યવાળો કચરો, હોસ્પિટલ કચરો"), T("dioxin and fly ash need control", "ડાયોક્સિન અને ફ્લાય એશનું નિયંત્રણ જરૂરી")]]),
               H4("Hazardous waste", "જોખમી કચરો"),
               P("Hazardous waste is waste that is flammable, corrosive, reactive, toxic or infectious: "
                 "spent solvents, acids, plating sludge, waste oil, pesticides, batteries, hospital "
                 "sharps. It travels in a documented chain - manifest, licensed transporter, "
                 "treatment-storage-disposal facility (TSDF) - and is treated by incineration, "
                 "neutralisation, or stabilisation and solidification before a secured landfill. "
                 "Mixing one drum of solvent into a truck of municipal waste turns the whole truck into "
                 "hazardous waste.",
                 "જોખમી કચરો એ જ્વલનશીલ, કાટકારક, પ્રતિક્રિયાશીલ, ઝેરી કે ચેપી કચરો છે: વપરાયેલા દ્રાવક, "
                 "એસિડ, પ્લેટિંગ કાદવ, વપરાયેલું તેલ, જંતુનાશક, બેટરી, હોસ્પિટલની સોય. તે દસ્તાવેજી શૃંખલામાં "
                 "ચાલે - મેનિફેસ્ટ, પરવાનગીવાળો વાહક, સારવાર-સંગ્રહ-નિકાલ સુવિધા (TSDF) - અને દહન, "
                 "ન્યુટ્રલાઇઝેશન કે સ્થિરીકરણ-ઘનીકરણ પછી સુરક્ષિત લેન્ડફિલમાં જાય. એક ડ્રમ દ્રાવક નગરપાલિકાના "
                 "કચરાની ટ્રકમાં ભળે તો આખી ટ્રક જોખમી કચરો બની જાય."),
               H4("Worked example", "ઉકેલાયેલ દાખલો"),
               P("A town of 5 lakh people makes 225 t/day. If wet waste is 55 % (124 t) and it is "
                 "composted at a 25 % yield, the town gets 31 t of compost a day instead of sending 124 t "
                 "to a landfill that would need about 19,000 m³ a year of void space for it.",
                 "5 લાખ લોકોનું નગર રોજ 225 ટન કચરો પેદા કરે. ભીનો કચરો 55 % (124 ટન) હોય અને 25 % ઉપજ પર "
                 "કમ્પોસ્ટ કરાય તો નગરને રોજ 31 ટન કમ્પોસ્ટ મળે, અને 124 ટન લેન્ડફિલમાં મોકલવાને બદલે જેને "
                 "વર્ષે લગભગ 19,000 m³ જગ્યા જોઈતી."),
               H4("Common mistake", "સામાન્ય ભૂલ"),
               P("Calling an open dump a landfill. Without a liner, leachate cover and gas vents, a dump "
                 "pollutes groundwater for decades and catches fire every summer.",
                 "ખુલ્લા ઢગલાને લેન્ડફિલ કહેવું. અસ્તર, લીચેટ આવરણ અને ગેસ નિકાસ વગરનો ઢગલો દાયકાઓ સુધી "
                 "ભૂગર્ભજળ પ્રદૂષિત કરે અને દર ઉનાળે આગ પકડે.")],
              None, syllabus_item="2.4"),
     ]},

    {"title": T("4. Noise, Plastic and Electronic Waste", "4. ઘોંઘાટ, પ્લાસ્ટિક અને ઇલેક્ટ્રોનિક કચરો"),
     "items": [
         card(T("2.5 Noise pollution and its effects", "2.5 ઘોંઘાટ પ્રદૂષણ અને તેની અસરો"),
              [H4("What noise is", "ઘોંઘાટ એટલે શું"),
               P("<b>Noise</b> is unwanted sound. It travels as a pressure wave and is measured in "
                 "decibels, a logarithmic scale: a rise of <b>3 dB</b> doubles the sound energy, "
                 "<b>10 dB</b> is ten times the energy and sounds about twice as loud, and the scale "
                 "runs from 0 dB (threshold of hearing) to 120 dB (pain).",
                 "<b>ઘોંઘાટ</b> એટલે અનિચ્છનીય ધ્વનિ. તે દબાણ તરંગ તરીકે ચાલે અને ડેસિબલમાં માપાય, જે "
                 "લઘુગણક માપક્રમ છે: <b>3 dB</b> નો વધારો ધ્વનિ ઊર્જા બમણી કરે, <b>10 dB</b> એ દસ ગણી ઊર્જા "
                 "અને લગભગ બમણો સંભાળાય, અને માપક્રમ 0 dB (સાંભળવાની મર્યાદા) થી 120 dB (પીડા) સુધી ચાલે."),
               H4("Scale and standards", "માપક્રમ અને ધોરણો"),
               TB([T("Source", "સ્રોત"), T("Level", "સ્તર"), T("Zone (day limit in India)", "વિસ્તાર (ભારતમાં દિવસની મર્યાદા)")],
                  [[T("leaves rustling", "પાનની સરસરાહટ"), T("20 dB", "20 dB"), T("silence zone 50 dB", "શાંત વિસ્તાર 50 dB")],
                   [T("normal conversation", "સામાન્ય વાતચીત"), T("60 dB", "60 dB"), T("residential 55 dB", "રહેણાંક 55 dB")],
                   [T("traffic on a busy road", "વ્યસ્ત રસ્તાની ટ્રાફિક"), T("80 dB", "80 dB"), T("commercial 65 dB", "વ્યાપારી 65 dB")],
                   [T("factory floor", "કારખાનાનું ફ્લોર"), T("95 dB", "95 dB"), T("industrial 75 dB", "ઔદ્યોગિક 75 dB")],
                   [T("jet aircraft at 50 m", "50 m પર જેટ વિમાન"), T("120 dB", "120 dB"), T("pain threshold", "પીડાની મર્યાદા")]]),
               H4("Effects", "અસરો"),
               UL(("Hearing: prolonged exposure above 85 dB damages the hair cells of the inner ear, "
                   "and the loss is permanent.", "સાંભળવાની શક્તિ: 85 dB થી વધુ લાંબા સમય સુધી રહેવાથી અંદરના "
                   "કાનના કોષો નાશ પામે અને નુકસાન કાયમી રહે."),
                  ("Non-auditory: raised blood pressure, disturbed sleep, poor concentration, "
                   "irritability and lower performance in school.",
                   "અ-શ્રવણ અસરો: લોહીનું દબાણ વધે, ઊંઘ ડહોળાય, ધ્યાન ઘટે, ચીડિયાપણું અને શાળામાં કામગીરી ઘટે."),
                  ("Wildlife: birds and marine animals change their calls, feeding and migration when "
                   "the background noise rises.", "વન્યજીવન: સ્વર વધે ત્યારે પક્ષી અને દરિયાઈ પ્રાણી પોતાના "
                   "અવાજ, ખોરાક અને સ્થળાંતર બદલે.")),
               H4("Worked example", "ઉકેલાયેલ દાખલો"),
               P("Two identical machines of 70 dB each give 70 + 3 = 73 dB, not 140 dB - the decibel "
                 "scale is logarithmic. Ten such machines would give about 80 dB, which is why enclosing "
                 "one noisy press is worth more than trying to absorb the whole hall.",
                 "70 dB નાં બે સરખાં મશીન 70 + 3 = 73 dB આપે, 140 dB નહીં - ડેસિબલ માપક્રમ લઘુગણક છે. આવાં "
                 "દસ મશીન લગભગ 80 dB આપે, તેથી એક ઘોંઘાટિયું પ્રેસ બંધ કરવું આખા હૉલને શોષવા કરતાં વધુ ફાયદાકારક છે."),
               H4("Common mistake", "સામાન્ય ભૂલ"),
               P("Adding decibels arithmetically. Doubling the number of sources adds only 3 dB, so "
                 "halving a noise source (a 10 dB cut) removes nine tenths of the energy.",
                 "ડેસિબલ સીધા સરવાળે ઉમેરવા. સ્રોત બમણા કરવાથી ફક્ત 3 dB વધે, તેથી ઘોંઘાટ અડધો કરવો (10 dB ઘટાડો) "
                 "ઊર્જાના દશમાં ભાગ જ રહે એમ કરે.")],
              "u2_noise", syllabus_item="2.5"),
         card(T("2.5 Plastic waste and its hazard", "2.5 પ્લાસ્ટિક કચરો અને તેનું જોખમ"),
              [H4("Why plastic is a special problem", "પ્લાસ્ટિક કેમ ખાસ સમસ્યા છે"),
               P("Plastic is light, cheap, strong and almost indestructible - the same properties that "
                 "make it useful make it a waste problem. An estimated 8-12 million tonnes reach the "
                 "ocean every year, and a single-use carry bag is used for 15 minutes and lasts for "
                 "centuries.",
                 "પ્લાસ્ટિક હલકું, સસ્તું, મજબૂત અને લગભગ અવિનાશી છે - જે ગુણ તેને ઉપયોગી બનાવે છે તે જ તેને "
                 "કચરાની સમસ્યા બનાવે છે. વર્ષે અંદાજે 8-12 મિલિયન ટન દરિયામાં પહોંચે છે, અને એક વપરાશની "
                 "થેલી 15 મિનિટ વપરાય પણ સદીઓ સુધી ટકે."),
               H4("Route of the harm", "નુકસાનનો રસ્તો"),
               OL(("Litter blocks drains and causes urban flooding; livestock and stray animals swallow "
                   "bags and die.", "કચરો ગટર રોકે અને શહેરી પૂર લાવે; પશુ અને આવારા પ્રાણી થેલી ગળી જઈ મરે."),
                  ("In the sea it breaks into microplastics below 5 mm, which plankton take up and fish "
                   "pass to people.", "દરિયામાં તે 5 mm થી નાના માઇક્રોપ્લાસ્ટિકમાં તૂટે, જે પ્લાંકટન લે અને "
                   "માછલી મારફતે માણસ સુધી પહોંચે."),
                  ("Burning plastic in the open releases dioxins, furans and black carbon - worse than "
                   "the litter it removes.", "ખુલ્લામાં પ્લાસ્ટિક બાળવાથી ડાયોક્સિન, ફ્યુરાન અને કાળો કાર્બન "
                   "નીકળે - કચરો દૂર કરવા કરતાં વધુ ખરાબ."),
                  ("Additives such as phthalates and BPA leach into water and food.",
                   "થેલેટ અને BPA જેવા ઉમેરણો પાણી અને ખોરાકમાં ઝીણવટથી નીકળે.")),
               H4("Recycling codes and rules", "રિસાયકલ કોડ અને નિયમો"),
               TB([T("Code", "કોડ"), T("Polymer", "પોલિમર"), T("Usual fate", "સામાન્ય અંત")],
                  [[T("1", "1"), T("PET - bottles", "PET - બોટલ"), T("widely recycled into fibre", "રેસામાં વ્યાપક રિસાયકલ")],
                   [T("2", "2"), T("HDPE - cans, pipes", "HDPE - ડબ્બા, પાઇપ"), T("recycled well", "સારી રીતે રિસાયકલ")],
                   [T("4", "4"), T("LDPE - carry bags, film", "LDPE - થેલી, ફિલ્મ"), T("thin film, hard to collect", "પાતળી ફિલ્મ, એકઠી કરવી મુશ્કેલ")],
                   [T("6", "6"), T("PS - cups, packaging", "PS - કપ, પેકિંગ"), T("rarely recycled", "ભાગ્યે જ રિસાયકલ")],
                   [T("7", "7"), T("other, multilayer", "અન્ય, મલ્ટિલેયર"), T("almost never recycled", "લગભગ કદી નહીં")]]),
               P("India's Plastic Waste Management Rules ban thin single-use carry bags, require "
                 "thicker bags, put <b>extended producer responsibility</b> on the maker and packer, and "
                 "make segregation at source a duty. The engineering answer is threefold: less virgin "
                 "plastic in the design, a real take-back channel, and road or RDF use for what cannot "
                 "be recycled.",
                 "ભારતના પ્લાસ્ટિક કચરા નિયમો પાતળી વપરાશની થેલી પર પ્રતિબંધ મૂકે, જાડી થેલી ફરજિયાત કરે, "
                 "ઉત્પાદક અને પેકર પર <b>વિસ્તૃત ઉત્પાદક જવાબદારી</b> મૂકે, અને સ્રોત પર અલગ કરવાની ફરજ કરે. "
                 "ઇજનેરી જવાબ ત્રણ છે: ડિઝાઇનમાં ઓછું કુમાર પ્લાસ્ટિક, સાચો પરત-સંગ્રહ માર્ગ, અને જે રિસાયકલ "
                 "ન થાય તે રસ્તા કે RDF માટે."),
               H4("Worked example", "ઉકેલાયેલ દાખલો"),
               P("A city of 5 lakh people making 225 t/day produces about 8 % plastic, i.e. 18 t/day. If "
                 "40 % is collected clean and recycled, 7.2 t is recovered and 10.8 t still needs a "
                 "route - which is why segregation, not a bigger incinerator, is the deciding step.",
                 "5 લાખ લોકોનું શહેર રોજ 225 ટન કચરો પેદા કરે તેમાં લગભગ 8 % પ્લાસ્ટિક, એટલે 18 ટન રોજ. 40 % "
                 "સ્વચ્છ એકઠું થઈ રિસાયકલ થાય તો 7.2 ટન પુનઃપ્રાપ્ત થાય અને 10.8 ટનને હજી રસ્તો જોઈએ - તેથી "
                 "નિર્ણાયક પગલું મોટી ભઠ્ઠી નહીં, અલગ કરવું છે."),
               H4("Common mistake", "સામાન્ય ભૂલ"),
               P("Believing recycling solves plastic. Only the clean, single-polymer fraction is "
                 "recyclable, and each cycle shortens the chain, so reduction and reuse come first.",
                 "રિસાયકલિંગ પ્લાસ્ટિકનો ઉકેલ છે એમ માનવું. ફક્ત સ્વચ્છ, એક-પોલિમર ભાગ રિસાયકલ થાય, અને દરેક "
                 "ચક્ર સાંકળ ટૂંકી કરે, તેથી ઘટાડો અને ફરી વપરાશ પહેલાં આવે.")],
              None, syllabus_item="2.5"),
         card(T("2.5 Electronic waste and its hazard", "2.5 ઇલેક્ટ્રોનિક કચરો અને તેનું જોખમ"),
              [H4("What it is", "તે શું છે"),
               P("<b>E-waste</b> is discarded electrical and electronic equipment: phones, computers, "
                 "televisions, printers, refrigerators, lamps and batteries. It is the fastest growing "
                 "waste stream in the world, roughly 60 million tonnes a year, and India is among the "
                 "top three generators.",
                 "<b>ઇ-કચરો</b> એ નકામાં વીજ અને ઇલેક્ટ્રોનિક સાધનો છે: ફોન, કમ્પ્યુટર, ટેલિવિઝન, પ્રિન્ટર, "
                 "ફ્રિજ, લેમ્પ અને બેટરી. તે દુનિયામાં સૌથી ઝડપથી વધતો કચરા પ્રવાહ છે, વર્ષે લગભગ 60 મિલિયન "
                 "ટન, અને ભારત ટોચના ત્રણ ઉત્પાદકોમાં છે."),
               H4("What is inside", "અંદર શું છે"),
               TB([T("Part", "ભાગ"), T("Share of mass", "દળમાં હિસ્સો"), T("Hazard", "જોખમ")],
                  [[T("ferrous and non-ferrous metal", "લોહ અને અલોહ ધાતુ"), T("about 50 %", "લગભગ 50 %"), T("valuable if recovered cleanly", "સ્વચ્છ રીતે પુનઃપ્રાપ્ત થાય તો મૂલ્યવાન")],
                   [T("plastic", "પ્લાસ્ટિક"), T("about 21 %", "લગભગ 21 %"), T("brominated flame retardants", "બ્રોમિનયુક્ત જ્વાળા-મંદક")],
                   [T("circuit boards", "સર્કિટ બોર્ડ"), T("small mass, high value", "ઓછું દળ, ઊંચું મૂલ્ય"), T("lead, cadmium, beryllium", "સીસું, કેડમિયમ, બેરિલિયમ")],
                   [T("batteries and lamps", "બેટરી અને લેમ્પ"), T("small", "ઓછું"), T("mercury, cadmium, lithium fire risk", "પારો, કેડમિયમ, લિથિયમ આગનું જોખમ")]]),
               H4("How the hazard reaches people", "જોખમ લોકો સુધી કેવી રીતે પહોંચે"),
               P("Around 90 % of Indian e-waste passes through the informal sector, where cables are "
                 "burnt to recover copper, boards are dipped in acid for gold, and the residue is dumped "
                 "in a drain. Burning releases dioxins and lead fumes over the very settlement that does "
                 "the work, and children are the most exposed.",
                 "ભારતનો લગભગ 90 % ઇ-કચરો અસંગઠિત ક્ષેત્રમાંથી પસાર થાય, જ્યાં તાંબું કાઢવા કેબલ બાળવામાં "
                 "આવે, સોના માટે બોર્ડ એસિડમાં બોળાય, અને અવશેષ ગટરમાં ઠાલવાય. બળવાથી ડાયોક્સિન અને સીસાના "
                 "ધુમાડા એ જ વસાહત પર ફેલાય જે આ કામ કરે છે, અને બાળકો સૌથી વધુ ખુલ્લાં પડે."),
               H4("The rule and the fix", "નિયમ અને ઉકેલ"),
               P("The E-Waste (Management) Rules make the producer responsible for take-back through "
                 "collection points, require authorised dismantlers and recyclers, and ban the informal "
                 "acid and burning routes. For a college or a factory the practical steps are a buy-back "
                 "clause in the purchase order, a locked e-waste store, a record of every item handed "
                 "over, and handing it only to an authorised recycler.",
                 "ઇ-કચરા (વ્યવસ્થાપન) નિયમો ઉત્પાદકને સંગ્રહ કેન્દ્રો દ્વારા પરત-સંગ્રહ માટે જવાબદાર બનાવે, "
                 "અધિકૃત વિઘટક અને રિસાયકલર ફરજિયાત કરે, અને અસંગઠિત એસિડ તથા દહનના રસ્તા પર પ્રતિબંધ "
                 "મૂકે. કોલેજ કે કારખાના માટે વ્યવહારુ પગલાં: ખરીદીના ઓર્ડરમાં પરત-ખરીદીની શરત, તાળું "
                 "વાળું ઇ-કચરા સંગ્રહસ્થાન, દરેક વસ્તુની નોંધ, અને ફક્ત અધિકૃત રિસાયકલરને સોંપવું."),
               H4("Worked example", "ઉકેલાયેલ દાખલો"),
               P("A city of 1 million generating 1.2 kg of e-waste per person a year has 1,200 t to "
                 "handle. Printed circuit boards carry about 0.3 g of gold per kg; even at a 30 % "
                 "recovery from just the 3 % board fraction, that is 1,200,000 × 0.03 × 0.3 × 0.3 g ≈ "
                 "3.2 kg of gold a year - worth recovering properly rather than in an acid bath.",
                 "10 લાખ લોકોનું શહેર, પ્રતિ વ્યક્તિ વર્ષે 1.2 kg ઇ-કચરો, તો 1,200 ટન સંભાળવાનું. પ્રિન્ટેડ "
                 "સર્કિટ બોર્ડમાં પ્રતિ કિલો લગભગ 0.3 g સોનું હોય; ફક્ત 3 % બોર્ડ ભાગમાંથી પણ 30 % પુનઃપ્રાપ્તિ "
                 "ગણતાં 1,200,000 × 0.03 × 0.3 × 0.3 g ≈ 3.2 kg સોનું વર્ષે - જે એસિડના સ્નાનને બદલે યોગ્ય "
                 "રીતે પુનઃપ્રાપ્ત કરવા લાયક છે."),
               H4("Common mistake", "સામાન્ય ભૂલ"),
               P("Selling old computers to the highest scrap bidder. Without a manifest and an "
                 "authorised recycler the college remains responsible for where that waste ends up.",
                 "જૂના કમ્પ્યુટર સૌથી વધુ ભાવ આપનાર ભંગારવાળાને વેચવા. મેનિફેસ્ટ અને અધિકૃત રિસાયકલર વગર "
                 "કચરો ક્યાં જાય તેની જવાબદારી કોલેજ પર જ રહે.")],
              "u2_ewaste", syllabus_item="2.5"),
     ]},
]

NUMERICALS = [
    num("u2n01", T("BOD of a diluted sample.", "મંદિત નમૂનાનો BOD."),
        T("5 mL of sewage is made up to 300 mL with dilution water. The dissolved oxygen falls from "
          "8.0 mg/L to 3.0 mg/L in five days. Find the BOD₅.",
          "5 mL ગટરનું પાણી મંદન પાણી સાથે 300 mL સુધી લઈ જવાય છે. પાંચ દિવસમાં ઓગળેલો ઓક્સિજન 8.0 mg/L "
          "થી 3.0 mg/L થાય છે. BOD₅ શોધો."),
        [P("Dilution fraction P = 5/300 = 0.0167", "મંદન અંશ P = 5/300 = 0.0167"),
         P("BOD = (D₁ − D₂) / P = (8.0 − 3.0) / 0.0167", "BOD = (D₁ − D₂) / P = (8.0 − 3.0) / 0.0167"),
         P("= 5.0 × 60 = 300 mg/L", "= 5.0 × 60 = 300 mg/L")],
        T("300 mg/L", "300 mg/L"), unit_no=2),
    num("u2n02", T("COD by titration.", "ટાઇટ્રેશનથી COD."),
        T("A 20 mL sample is refluxed with dichromate. The blank needs 10.0 mL and the sample 6.5 mL of "
          "0.25 N ferrous ammonium sulphate. Find the COD.",
          "20 mL નમૂનો ડાયક્રોમેટ સાથે રિફ્લક્સ કરાય. બ્લેન્કને 10.0 mL અને નમૂનાને 0.25 N ફેરસ "
          "એમોનિયમ સલ્ફેટના 6.5 mL જોઈએ. COD શોધો."),
        [P("COD = (blank − sample) × N × 8000 / volume", "COD = (બ્લેન્ક − નમૂનો) × N × 8000 / ઘનફળ"),
         P("= (10.0 − 6.5) × 0.25 × 8000 / 20", "= (10.0 − 6.5) × 0.25 × 8000 / 20"),
         P("= 3.5 × 0.25 × 400 = 350 mg/L", "= 3.5 × 0.25 × 400 = 350 mg/L")],
        T("350 mg/L", "350 mg/L"), unit_no=2),
    num("u2n03", T("BOD/COD ratio and what to do with the waste.",
                   "BOD/COD ગુણોત્તર અને કચરાનું શું કરવું."),
        T("An effluent has BOD 240 mg/L and COD 400 mg/L. Find the BOD/COD ratio and decide whether a "
          "biological treatment plant will work.",
          "એક પ્રવાહમાં BOD 240 mg/L અને COD 400 mg/L છે. BOD/COD ગુણોત્તર શોધો અને જૈવિક સારવાર પ્લાન્ટ "
          "ચાલશે કે નહીં તે નક્કી કરો."),
        [P("BOD/COD = 240/400 = 0.60", "BOD/COD = 240/400 = 0.60"),
         P("A ratio above 0.5 means the organic matter is easily biodegradable.",
           "0.5 થી વધુ ગુણોત્તર એટલે કાર્બનિક દ્રવ્ય સહેલાઈથી જૈવવિઘટનીય છે."),
         P("So an activated sludge plant will work; keep the effluent free of toxic shock loads.",
           "તેથી એક્ટિવેટેડ સ્લજ પ્લાન્ટ ચાલશે; પ્રવાહને ઝેરી આંચકાથી મુક્ત રાખો.")],
        T("0.60, biodegradable - biological treatment will work", "0.60, જૈવવિઘટનીય - જૈવિક સારવાર ચાલશે"),
        unit_no=2),
    num("u2n04", T("Total suspended solids from a filter test.", "ફિલ્ટર પરીક્ષણથી કુલ નિલંબિત ઘન."),
        T("A glass-fibre filter weighs 0.4000 g dry. After filtering 100 mL of sample and drying, it "
          "weighs 0.4521 g. Find the TSS.",
          "કાચ-રેસાનું ફિલ્ટર સૂકું 0.4000 g વજન ધરાવે છે. 100 mL નમૂનો ગાળીને સૂકવ્યા પછી તે 0.4521 g "
          "થાય છે. TSS શોધો."),
        [P("Mass of solids = 0.4521 − 0.4000 = 0.0521 g = 52.1 mg",
           "ઘનનું દળ = 0.4521 − 0.4000 = 0.0521 g = 52.1 mg"),
         P("TSS = 52.1 mg / 0.1 L", "TSS = 52.1 mg / 0.1 L"),
         P("= 521 mg/L", "= 521 mg/L")],
        T("521 mg/L", "521 mg/L"), unit_no=2),
    num("u2n05", T("Adding noise from two and three machines.",
                   "બે અને ત્રણ મશીનનો ઘોંઘાટ ઉમેરવો."),
        T("A hall has two identical machines, each giving 70 dB at the operator position. Find the level "
          "when both run, and again when a third identical machine is added.",
          "હૉલમાં બે સરખાં મશીન છે, દરેક ઓપરેટરની જગ્યાએ 70 dB આપે છે. બંને ચાલે ત્યારે અને ત્રીજું સરખું "
          "મશીન ઉમેરાય ત્યારે સ્તર શોધો."),
        [P("Two equal sources: L = 70 + 10 log 2 = 70 + 3.0 = 73 dB",
           "બે સરખા સ્રોત: L = 70 + 10 log 2 = 70 + 3.0 = 73 dB"),
         P("Three equal sources: L = 70 + 10 log 3 = 70 + 4.8 = 74.8 dB",
           "ત્રણ સરખા સ્રોત: L = 70 + 10 log 3 = 70 + 4.8 = 74.8 dB"),
         P("Doubling the number of machines adds only 3 dB, so a 3 dB rise is a real doubling of energy.",
           "મશીનની સંખ્યા બમણી કરવાથી ફક્ત 3 dB વધે, તેથી 3 dB નો વધારો ઊર્જા ખરેખર બમણી થઈ એમ દર્શાવે.")],
        T("73 dB, then 74.8 dB", "73 dB, પછી 74.8 dB"), unit_no=2),
    num("u2n06", T("Equivalent continuous level over a shift.", "શિફ્ટ દરમિયાન સમકક્ષ સતત સ્તર."),
        T("A worker is exposed to 85 dB for 4 hours and 75 dB for the other 4 hours. Find the 8-hour "
          "equivalent level Leq.",
          "કારીગર 4 કલાક 85 dB અને બાકીના 4 કલાક 75 dB ના ઘોંઘાટમાં રહે છે. 8 કલાકનું સમકક્ષ સ્તર Leq શોધો."),
        [P("Leq = 10 log [(t₁·10^(L₁/10) + t₂·10^(L₂/10)) / T]",
           "Leq = 10 log [(t₁·10^(L₁/10) + t₂·10^(L₂/10)) / T]"),
         P("= 10 log [(4×10^8.5 + 4×10^7.5) / 8]", "= 10 log [(4×10^8.5 + 4×10^7.5) / 8]"),
         P("= 10 log (1.74×10⁸) = 82.4 dB", "= 10 log (1.74×10⁸) = 82.4 dB")],
        T("82.4 dB over the 8-hour shift", "8 કલાકની શિફ્ટ પર 82.4 dB"), unit_no=2),
    num("u2n07", T("Landfill volume and land for twenty years.",
                   "વીસ વર્ષ માટે લેન્ડફિલનું ઘનફળ અને જમીન."),
        T("A town of 5 lakh people generates 0.45 kg of waste per person a day. Find the daily waste and "
          "the land needed at a compacted density of 0.6 t/m³ for 20 years, filled to 8 m depth.",
          "5 લાખ લોકોનું નગર પ્રતિ વ્યક્તિ રોજ 0.45 kg કચરો પેદા કરે છે. દૈનિક કચરો અને 0.6 t/m³ દબાયેલી "
          "ઘનતા સાથે 20 વર્ષની, 8 m ઊંડાઈ સુધી ભરેલી લેન્ડફિલ માટે જરૂરી જમીન શોધો."),
        [P("Daily waste = 5,00,000 × 0.45 = 225 t/day", "દૈનિક કચરો = 5,00,000 × 0.45 = 225 ટન/રોજ"),
         P("20-year mass = 225 × 365 × 20 = 1.64 × 10⁶ t", "20 વર્ષનું દળ = 225 × 365 × 20 = 1.64 × 10⁶ ટન"),
         P("Volume = 1.64 × 10⁶ / 0.6 = 2.74 × 10⁶ m³; area = volume / 8 m = 3.4 × 10⁵ m² = 34 ha",
           "ઘનફળ = 1.64 × 10⁶ / 0.6 = 2.74 × 10⁶ m³; ક્ષેત્રફળ = ઘનફળ / 8 m = 3.4 × 10⁵ m² = 34 હેક્ટર")],
        T("225 t a day; about 34 ha", "રોજ 225 ટન; લગભગ 34 હેક્ટર"), unit_no=2),
    num("u2n08", T("Efficiency of a cyclone separator.", "સાયક્લોન વિભાજકની કાર્યક્ષમતા."),
        T("Dust in a flue is 12 g/m³ before the cyclone and 0.6 g/m³ after it. Find the collection "
          "efficiency.",
          "ચીમનીમાં ધૂળ સાયક્લોન પહેલાં 12 g/m³ અને પછી 0.6 g/m³ છે. સંગ્રહ કાર્યક્ષમતા શોધો."),
        [P("Efficiency = (inlet − outlet) / inlet × 100", "કાર્યક્ષમતા = (પ્રવેશ − નિકાસ) / પ્રવેશ × 100"),
         P("= (12 − 0.6) / 12 × 100", "= (12 − 0.6) / 12 × 100"),
         P("= 95 %", "= 95 %")],
        T("95 %", "95 %"), unit_no=2),
    num("u2n09", T("Plastic in the city waste stream.", "શહેરના કચરામાં પ્લાસ્ટિક."),
        T("A city generates 225 t of waste a day, of which 8 % is plastic. If 40 % of the plastic is "
          "collected clean and recycled, how much is recovered and how much still needs a route?",
          "એક શહેર રોજ 225 ટન કચરો પેદા કરે છે જેમાં 8 % પ્લાસ્ટિક છે. 40 % પ્લાસ્ટિક સ્વચ્છ એકઠું થઈ "
          "રિસાયકલ થાય તો કેટલું પુનઃપ્રાપ્ત થાય અને કેટલાને હજી રસ્તો જોઈએ?"),
        [P("Plastic = 225 × 0.08 = 18 t/day", "પ્લાસ્ટિક = 225 × 0.08 = 18 ટન/રોજ"),
         P("Recycled = 18 × 0.40 = 7.2 t/day", "રિસાયકલ = 18 × 0.40 = 7.2 ટન/રોજ"),
         P("Balance = 18 − 7.2 = 10.8 t/day", "બાકી = 18 − 7.2 = 10.8 ટન/રોજ")],
        T("7.2 t recycled, 10.8 t still to be routed", "7.2 ટન રિસાયકલ, 10.8 ટનને હજી રસ્તો જોઈએ"),
        unit_no=2),
    num("u2n10", T("Gold recoverable from a city's e-waste.",
                   "શહેરના ઇ-કચરામાંથી પુનઃપ્રાપ્ત થઈ શકે તેવું સોનું."),
        T("A city of 10 lakh people generates 1.2 kg of e-waste per person a year. Circuit boards are "
          "3 % of that mass and carry 0.3 g of gold per kg. Find the gold in the boards and, at 30 % "
          "recovery, the gold actually recovered in a year.",
          "10 લાખ લોકોનું શહેર પ્રતિ વ્યક્તિ વર્ષે 1.2 kg ઇ-કચરો પેદા કરે છે. સર્કિટ બોર્ડ તે દળના 3 % છે "
          "અને પ્રતિ કિલો 0.3 g સોનું ધરાવે છે. બોર્ડમાંનું સોનું અને 30 % પુનઃપ્રાપ્તિ પર વર્ષે ખરેખર "
          "મળતું સોનું શોધો."),
        [P("E-waste = 10,00,000 × 1.2 = 1,200,000 kg = 1,200 t a year",
           "ઇ-કચરો = 10,00,000 × 1.2 = 1,200,000 kg = 1,200 ટન વર્ષે"),
         P("Boards = 1,200,000 × 0.03 = 36,000 kg; gold in them = 36,000 × 0.3 = 10,800 g",
           "બોર્ડ = 1,200,000 × 0.03 = 36,000 kg; તેમાં સોનું = 36,000 × 0.3 = 10,800 g"),
         P("Recovered at 30 % = 10,800 × 0.3 = 3,240 g ≈ 3.2 kg", "30 % પર પુનઃપ્રાપ્ત = 10,800 × 0.3 = 3,240 g ≈ 3.2 kg")],
        T("10.8 kg in the boards, 3.2 kg recovered", "બોર્ડમાં 10.8 kg, પુનઃપ્રાપ્ત 3.2 kg"), unit_no=2),
]

EQUATIONS = [
    {"title": T("Water pollution", "જળ પ્રદૂષણ"),
     "items": [
         {"name": T("BOD by dilution", "મંદનથી BOD"), "f": "BOD = (D₁ − D₂) / P, P = sample / total volume",
          "terms": T("D₁ and D₂ are the dissolved oxygen before and after five days, in mg/L.",
                     "D₁ અને D₂ એ પાંચ દિવસ પહેલાં અને પછીનો ઓગળેલો ઓક્સિજન, mg/L માં.")},
         {"name": T("COD by titration", "ટાઇટ્રેશનથી COD"),
          "f": "COD = (V_blank − V_sample) × N × 8000 / V_sample",
          "terms": T("8000 is the oxygen equivalent of 1 N dichromate per litre.",
                     "8000 એ પ્રતિ લિટર 1 N ડાયક્રોમેટનું ઓક્સિજન સમમૂલ્ય છે.")},
         {"name": T("Biodegradability", "જૈવવિઘટનક્ષમતા"), "f": "BOD / COD",
          "terms": T("Above 0.5 easily treated biologically; below 0.1 largely inorganic or toxic.",
                     "0.5 થી વધુ સહેલાઈથી જૈવિક રીતે સારવાર પામે; 0.1 થી નીચે મોટે ભાગે અકાર્બનિક કે ઝેરી.")},
         {"name": T("Suspended solids", "નિલંબિત ઘન"), "f": "TSS = (W₂ − W₁) × 1000 / V (mL) mg/L",
          "terms": T("W is the dry filter weight in grams before and after filtration.",
                     "W એ ગાળણી પહેલાં અને પછી ફિલ્ટરનું સૂકું વજન ગ્રામમાં.")},
     ]},
    {"title": T("Noise and solid waste", "ઘોંઘાટ અને ઘન કચરો"),
     "items": [
         {"name": T("Adding equal sources", "સરખા સ્રોત ઉમેરવા"), "f": "L = L₁ + 10 log n",
          "terms": T("Two identical machines add 3 dB, ten add 10 dB.",
                     "બે સરખાં મશીન 3 dB ઉમેરે, દસ 10 dB.")},
         {"name": T("Equivalent level", "સમકક્ષ સ્તર"),
          "f": "Leq = 10 log [(Σ tᵢ·10^(Lᵢ/10)) / T]",
          "terms": T("Averages a varying exposure over the shift, not over a single moment.",
                     "એક ક્ષણને બદલે આખી શિફ્ટના બદલાતા સંપર્કનું સરેરાશ.")},
         {"name": T("Waste per day", "દૈનિક કચરો"), "f": "W = population × per-capita generation",
          "terms": T("Indian towns run at 0.3-0.5 kg per person a day.",
                     "ભારતીય નગરો પ્રતિ વ્યક્તિ રોજ 0.3-0.5 kg પર ચાલે.")},
         {"name": T("Landfill volume", "લેન્ડફિલનું ઘનફળ"), "f": "V = mass / compacted density",
          "terms": T("Compacted municipal waste is 0.6-0.9 t/m³; divide by depth for the land area.",
                     "દબાયેલો નગરપાલિકા કચરો 0.6-0.9 t/m³; જમીનના ક્ષેત્રફળ માટે ઊંડાઈથી ભાગો.")},
         {"name": T("Collector efficiency", "સંગ્રહક કાર્યક્ષમતા"),
          "f": "η = (C_in − C_out) / C_in × 100 %",
          "terms": T("Applies to a cyclone, a bag filter, an ESP or a scrubber.",
                     "સાયક્લોન, બેગ ફિલ્ટર, ESP કે સ્ક્રબરને લાગુ પડે.")},
     ]},
]

VIVA = [
    {"title": T("Air and water pollution", "વાયુ અને જળ પ્રદૂષણ"),
     "items": [
         {"q": T("What is air pollution and how are pollutants classified?",
                 "વાયુ પ્રદૂષણ એટલે શું અને પ્રદૂષકોનું વર્ગીકરણ કેવી રીતે થાય?"),
          "a": T("Air pollution is the presence of gases, particles or biological material in the air at "
                 "a concentration that harms health, vegetation or materials. Pollutants are classified "
                 "as primary (emitted as such, like SO₂) or secondary (formed in the air, like ozone), "
                 "as natural or anthropogenic, and by the shape of the source - point, line or area.",
                 "વાયુ પ્રદૂષણ એટલે હવામાં વાયુ, કણ કે જૈવિક દ્રવ્યની એવી સાંદ્રતામાં હાજરી જે આરોગ્ય, "
                 "વનસ્પતિ કે વસ્તુને નુકસાન પહોંચાડે. પ્રદૂષકો પ્રાથમિક (જેમ છે તેમ નીકળે, જેમ કે SO₂) કે "
                 "દ્વિતીય (હવામાં બને, જેમ કે ઓઝોન) એમ, કુદરતી કે માનવજન્ય એમ, અને સ્રોતના આકાર પ્રમાણે - "
                 "બિંદુ, રેખા કે વિસ્તાર - વર્ગીકૃત થાય.")},
         {"q": T("Name five air pollutants, their sources and one effect each.",
                 "પાંચ વાયુ પ્રદૂષક, તેમના સ્રોત અને દરેકની એક અસર જણાવો."),
          "a": T("PM2.5 from vehicles, construction and open burning causes lung and heart disease; SO₂ "
                 "from sulphur-bearing coal causes acid rain and breathing difficulty; NOx from hot "
                 "engines forms smog and ozone; CO from incomplete combustion blocks haemoglobin; CO₂ "
                 "from every fuel fire drives climate change.",
                 "વાહન, બાંધકામ અને ખુલ્લા દહનમાંથી PM2.5 ફેફસાં-હૃદયના રોગ કરે; સલ્ફરવાળા કોલસામાંથી SO₂ "
                 "એસિડ વરસાદ અને શ્વાસની તકલીફ કરે; ગરમ એન્જિનમાંથી NOx ધૂમ્મસ અને ઓઝોન બનાવે; અપૂર્ણ દહનમાંથી "
                 "CO હિમોગ્લોબિન અટકાવે; દરેક ઇંધણની આગમાંથી CO₂ જળવાયુ પરિવર્તન લાવે.")},
         {"q": T("Which control equipment would you choose for coarse dust and for fine fume?",
                 "જાડી ધૂળ માટે અને બારીક ધુમાડા માટે કયું નિયંત્રણ સાધન પસંદ કરશો?"),
          "a": T("For coarse dust above 10 µm a cyclone separator is cheapest and needs no water; for "
                 "fine fume below 10 µm a bag filter or an electrostatic precipitator is needed. If the "
                 "gas is also hot, corrosive or carries a soluble gas, a wet scrubber gives cooling and "
                 "gas removal in one step.",
                 "10 µm થી મોટી જાડી ધૂળ માટે સાયક્લોન સૌથી સસ્તું છે અને પાણી જરૂરી નથી; 10 µm થી નીચેના "
                 "બારીક ધુમાડા માટે બેગ ફિલ્ટર કે ESP જરૂરી છે. વાયુ ગરમ, કાટકારક કે દ્રાવ્ય વાયુવાળો હોય તો "
                 "વેટ સ્ક્રબર એક જ પગલે ઠંડક અને વાયુ નિવારણ આપે.")},
         {"q": T("Define BOD and COD and say why both are measured.",
                 "BOD અને COD ની વ્યાખ્યા આપો અને બંને કેમ માપાય તે કહો."),
          "a": T("BOD₅ is the oxygen consumed by microorganisms while oxidising organic matter in five "
                 "days at 20 °C; COD is the oxygen needed to oxidise the same matter chemically with "
                 "dichromate. BOD measures what biology can eat, COD measures almost everything "
                 "oxidisable, and the ratio between them tells whether a biological plant will work.",
                 "BOD₅ એ 20 °C પર પાંચ દિવસમાં સૂક્ષ્મજીવો કાર્બનિક દ્રવ્ય ઓક્સિડાઇઝ કરતાં લેતો ઓક્સિજન છે; "
                 "COD એ ડાયક્રોમેટથી એ જ દ્રવ્ય રાસાયણિક રીતે ઓક્સિડાઇઝ કરવા જરૂરી ઓક્સિજન છે. BOD માપે કે "
                 "જીવવિજ્ઞાન શું ખાઈ શકે, COD લગભગ બધું ઓક્સિડાઇઝ થઈ શકે તે માપે, અને તેમનો ગુણોત્તર કહે કે "
                 "જૈવિક પ્લાન્ટ ચાલશે કે નહીં.")},
         {"q": T("Why is pH measured before and after treatment?",
                 "સારવાર પહેલાં અને પછી pH કેમ માપાય છે?"),
          "a": T("Before treatment pH decides whether the waste is compatible with the biology: below 6 "
                 "or above 9 the bacteria of an activated sludge plant are inhibited. After treatment "
                 "pH decides whether the effluent may be discharged, since the standard is 6.5 to 8.5, "
                 "and it also controls the chemical dose needed for coagulation.",
                 "સારવાર પહેલાં pH નક્કી કરે કે કચરો જૈવિક તંત્રને અનુકૂળ છે કે નહીં: 6 થી નીચે કે 9 થી ઉપર "
                 "એક્ટિવેટેડ સ્લજ પ્લાન્ટના જીવાણુ અટકી જાય. સારવાર પછી pH નક્કી કરે કે પાણી છોડી શકાય કે નહીં, "
                 "કારણ કે ધોરણ 6.5 થી 8.5 છે, અને તે કોગ્યુલેશન માટે જરૂરી રસાયણની માત્રા પણ નિયંત્રિત કરે.")},
     ]},
    {"title": T("Solid waste, noise and e-waste", "ઘન કચરો, ઘોંઘાટ અને ઇ-કચરો"),
     "items": [
         {"q": T("What are the three stages of wastewater treatment and what does each remove?",
                 "ગંદા પાણીની સારવારના ત્રણ તબક્કા અને દરેક શું દૂર કરે?"),
          "a": T("Primary removes settleable solids and floating matter by screening, grit removal and "
                 "sedimentation, taking out half to two thirds of the suspended solids. Secondary "
                 "removes dissolved organic matter with bacteria in an activated sludge, trickling "
                 "filter or UASB unit, taking out most of the BOD. Tertiary removes what biology "
                 "cannot - nutrients, colour, salts and pathogens - by chemical precipitation, "
                 "filtration, carbon or disinfection.",
                 "પ્રાથમિક તબક્કો બેસતા ઘન અને તરતું દ્રવ્ય સ્ક્રીનિંગ, ગ્રિટ દૂર કરવા અને અવસાદનથી દૂર કરે, "
                 "અને નિલંબિત ઘનમાંથી અડધાથી બે-તૃતીયાંશ લઈ લે. દ્વિતીય તબક્કો ઓગળેલું કાર્બનિક દ્રવ્ય "
                 "એક્ટિવેટેડ સ્લજ, ટ્રિકલિંગ ફિલ્ટર કે UASB એકમમાં જીવાણુઓથી દૂર કરે અને મોટાભાગનો BOD લઈ લે. "
                 "તૃતીય તબક્કો જે જીવવિજ્ઞાન ન કરી શકે તે દૂર કરે - પોષકતત્વો, રંગ, ક્ષાર અને રોગકારક - "
                 "રાસાયણિક અવક્ષેપન, ફિલ્ટર, કાર્બન કે કીટાણુનાશન દ્વારા.")},
         {"q": T("Why is segregation at source the most important step in solid waste management?",
                 "ઘન કચરા વ્યવસ્થાપનમાં સ્રોત પર અલગ કરવું સૌથી મહત્ત્વનું પગલું કેમ છે?"),
          "a": T("Because every later option depends on it. Mixed waste is too wet to burn, too "
                 "contaminated to compost and too dirty to recycle, so it can only go to a landfill. "
                 "When wet, dry and hazardous waste arrive separately, each stream can go to the "
                 "cheapest correct route - composting, recycling, RDF and a small secure landfill.",
                 "કારણ કે પછીનો દરેક વિકલ્પ તેના પર આધારિત છે. મિશ્ર કચરો બળવા પૂરતો સૂકો નથી, કમ્પોસ્ટ થવા "
                 "પૂરતો શુદ્ધ નથી અને રિસાયકલ થવા પૂરતો સ્વચ્છ નથી, તેથી તે ફક્ત લેન્ડફિલમાં જઈ શકે. ભીનો, "
                 "સૂકો અને જોખમી કચરો અલગ આવે તો દરેક પ્રવાહ સૌથી સસ્તા યોગ્ય રસ્તે જાય - કમ્પોસ્ટ, રિસાયકલ, "
                 "RDF અને નાની સુરક્ષિત લેન્ડફિલ.")},
         {"q": T("Differentiate a sanitary landfill from an open dump.",
                 "સેનિટરી લેન્ડફિલ અને ખુલ્લા ઢગલા વચ્ચે ભેદ આપો."),
          "a": T("A sanitary landfill is engineered: a clay or geomembrane liner, leachate collection and "
                 "treatment, gas vents or recovery, waste compacted in cells and covered daily, and "
                 "groundwater monitoring after closure. An open dump has none of these, so leachate "
                 "reaches the water table, methane escapes, vectors breed and the pile catches fire.",
                 "સેનિટરી લેન્ડફિલ ઇજનેરી રચના છે: માટી કે જીઓમેમ્બ્રેન અસ્તર, લીચેટ સંગ્રહ અને સારવાર, ગેસ "
                 "નિકાસ કે પુનઃપ્રાપ્તિ, કોષમાં દબાવેલો કચરો અને રોજ આવરણ, અને બંધ થયા પછી ભૂગર્ભજળની દેખરેખ. "
                 "ખુલ્લા ઢગલામાં આમાંથી કંઈ નથી, તેથી લીચેટ જળસ્તર સુધી પહોંચે, મિથેન નીકળે, વાહકો વધે અને ઢગલો આગ પકડે.")},
         {"q": T("What is hazardous waste and how is it handled?",
                 "જોખમી કચરો એટલે શું અને તેને કેવી રીતે સંભાળવાય?"),
          "a": T("Waste that is flammable, corrosive, reactive, toxic or infectious - spent solvents, "
                 "acids, plating sludge, waste oil, pesticides, batteries, hospital sharps. It is kept "
                 "separate, sent with a manifest through a licensed transporter to a TSDF, and treated "
                 "by incineration, neutralisation or stabilisation and solidification before a secured "
                 "landfill.",
                 "જે કચરો જ્વલનશીલ, કાટકારક, પ્રતિક્રિયાશીલ, ઝેરી કે ચેપી છે - વપરાયેલા દ્રાવક, એસિડ, પ્લેટિંગ "
                 "કાદવ, વપરાયેલું તેલ, જંતુનાશક, બેટરી, હોસ્પિટલની સોય. તે અલગ રખાય, મેનિફેસ્ટ સાથે પરવાનગીવાળા "
                 "વાહક દ્વારા TSDF સુધી મોકલાય, અને દહન, ન્યુટ્રલાઇઝેશન કે સ્થિરીકરણ-ઘનીકરણ પછી સુરક્ષિત "
                 "લેન્ડફિલમાં જાય.")},
         {"q": T("What does a 3 dB rise in noise mean?",
                 "ઘોંઘાટમાં 3 dB ના વધારાનો અર્થ શું?"),
          "a": T("The decibel scale is logarithmic, so 3 dB more means twice the sound energy, which is "
                 "roughly the smallest change a listener notices as louder. Two identical machines "
                 "therefore give the level of one plus 3 dB, and halving the number of sources lowers "
                 "the level by 3 dB.",
                 "ડેસિબલ માપક્રમ લઘુગણક છે, તેથી 3 dB વધુ એટલે ધ્વનિ ઊર્જા બમણી, જે સાંભળનારને લગભગ "
                 "નોંધાય તેવો સૌથી નાનો ફેરફાર છે. તેથી બે સરખાં મશીન એકના સ્તર + 3 dB આપે, અને સ્રોત અડધા "
                 "કરવાથી સ્તર 3 dB ઘટે.")},
         {"q": T("State the day-time noise limits for the four zones.",
                 "ચાર વિસ્તારો માટે દિવસના ઘોંઘાટની મર્યાદા જણાવો."),
          "a": T("In India the day-time limits are 50 dB in a silence zone, 55 dB in a residential "
                 "area, 65 dB in a commercial area and 75 dB in an industrial area, each 5 dB lower at "
                 "night. A silence zone is 100 m around a hospital, school or court.",
                 "ભારતમાં દિવસની મર્યાદા શાંત વિસ્તારમાં 50 dB, રહેણાંકમાં 55 dB, વ્યાપારીમાં 65 dB અને "
                 "ઔદ્યોગિકમાં 75 dB છે, અને રાત્રે દરેક 5 dB ઓછી. શાંત વિસ્તાર એટલે હોસ્પિટલ, શાળા કે "
                 "કોર્ટની 100 m આસપાસનો વિસ્તાર.")},
         {"q": T("Why is plastic waste harder to manage than paper waste?",
                 "પ્લાસ્ટિક કચરો કાગળના કચરા કરતાં સંભાળવો કેમ મુશ્કેલ છે?"),
          "a": T("Paper is a single material that rots and recycles easily. Plastic is many polymers "
                 "and multilayer laminates that cannot be sorted by hand, do not biodegrade, release "
                 "toxic fumes when burnt and break into microplastics that enter the food chain. Only "
                 "clean single-polymer fractions have a recycling market.",
                 "કાગળ એક જ પદાર્થ છે જે સડે છે અને સહેલાઈથી રિસાયકલ થાય. પ્લાસ્ટિક ઘણા પોલિમર અને મલ્ટિલેયર "
                 "સ્તરો છે જે હાથે અલગ ન થાય, જૈવવિઘટન પામતા નથી, બળે ત્યારે ઝેરી ધુમાડો છોડે અને માઇક્રોપ્લાસ્ટિકમાં "
                 "તૂટીને ખોરાક શૃંખલામાં પેસે. ફક્ત સ્વચ્છ એક-પોલિમર ભાગને રિસાયકલ બજાર મળે.")},
         {"q": T("What is extended producer responsibility?",
                 "વિસ્તૃત ઉત્પાદક જવાબદારી એટલે શું?"),
          "a": T("A rule that puts the responsibility for a product's end of life on the company that "
                 "makes or packs it: collect back a target share of the plastic or electronic waste it "
                 "puts on the market, fund the collection system and report the quantities. It turns "
                 "waste cost into a design cost, which is why packaging gets thinner and more "
                 "recyclable.",
                 "એવો નિયમ જે ઉત્પાદનના અંતિમ જીવનની જવાબદારી બનાવનાર કે પેક કરનાર કંપની પર મૂકે: બજારમાં "
                 "મૂકેલા પ્લાસ્ટિક કે ઇલેક્ટ્રોનિક કચરાનો નિશ્ચિત હિસ્સો પરત એકઠો કરે, સંગ્રહ તંત્રને ભંડોળ આપે "
                 "અને જથ્થાનો હિસાબ આપે. તે કચરાનો ખર્ચ ડિઝાઇનના ખર્ચમાં ફેરવે, તેથી પેકિંગ પાતળું અને વધુ "
                 "રિસાયકલયોગ્ય બને.")},
         {"q": T("What are the hazards of informal e-waste recycling?",
                 "અસંગઠિત ઇ-કચરા રિસાયકલિંગનાં જોખમો શું?"),
          "a": T("Cables are burnt in the open to recover copper and boards are dipped in acid for gold, "
                 "which releases dioxins, lead and mercury fumes over the settlement doing the work. "
                 "Children are most exposed, the acid residue goes into drains and soil, and the "
                 "recovered metal is sold without any record.",
                 "તાંબું કાઢવા કેબલ ખુલ્લામાં બાળવામાં આવે અને સોના માટે બોર્ડ એસિડમાં બોળાય, જેનાથી ડાયોક્સિન, "
                 "સીસું અને પારાનો ધુમાડો એ જ વસાહત પર ફેલાય જે આ કામ કરે. બાળકો સૌથી વધુ ખુલ્લાં પડે, એસિડનો "
                 "અવશેષ ગટર અને જમીનમાં જાય, અને પુનઃપ્રાપ્ત ધાતુ કોઈ નોંધ વગર વેચાય.")},
     ]},
]

_PRACTICE = [
    (T("Explain the classification of air pollutants with two examples of each type.",
       "વાયુ પ્રદૂષકોનું વર્ગીકરણ દરેક પ્રકારનાં બે ઉદાહરણ સાથે સમજાવો."), 4,
     [P("Air pollutants are classified in four useful ways. By formation, primary pollutants are "
        "emitted as they are - SO₂ from sulphur-bearing coal, CO from an idling engine - while "
        "secondary pollutants are made in the air, such as ozone from NOx and hydrocarbons, or "
        "sulphuric acid mist from SO₂.",
        "વાયુ પ્રદૂષકો ચાર ઉપયોગી રીતે વર્ગીકૃત થાય. બનવાની રીત પ્રમાણે, પ્રાથમિક પ્રદૂષકો જેમ છે તેમ નીકળે "
        "- સલ્ફરવાળા કોલસામાંથી SO₂, બિનજરૂરી એન્જિનમાંથી CO - જ્યારે દ્વિતીય પ્રદૂષકો હવામાં બને, જેમ કે "
        "NOx અને હાઇડ્રોકાર્બનમાંથી ઓઝોન કે SO₂ માંથી સલ્ફ્યુરિક એસિડ ધુમ્મસ."),
      P("By origin they are natural (volcanic SO₂, dust from deserts, methane from wetlands) or "
        "anthropogenic (chimneys, vehicles, burning of waste). By the shape of the source they are "
        "point sources such as a chimney, line sources such as a highway, and area sources such as a "
        "landfill or a whole industrial estate.",
        "ઉદ્ગમ પ્રમાણે તે કુદરતી (જ્વાળામુખીનું SO₂, રણની ધૂળ, ભીની જમીનનું મિથેન) કે માનવજન્ય (ચીમની, "
        "વાહનો, કચરાનું દહન) હોય. સ્રોતના આકાર પ્રમાણે તે ચીમની જેવા બિંદુ સ્રોત, ધોરીમાર્ગ જેવા રેખા સ્રોત "
        "અને કચરાભરાવ કે આખા ઔદ્યોગિક વિસ્તાર જેવા ક્ષેત્ર સ્રોત હોય."),
      P("By physical state they are gaseous (SO₂, NOx, CO, VOC) or particulate (PM10, PM2.5, fly ash). "
        "The classification matters in practice because it decides the control: a cyclone cannot "
        "remove a gas, and a scrubber is wasted on dry coarse dust.",
        "ભૌતિક સ્થિતિ પ્રમાણે તે વાયુરૂપ (SO₂, NOx, CO, VOC) કે કણરૂપ (PM10, PM2.5, ફ્લાય એશ) હોય. "
        "વર્ગીકરણ વ્યવહારમાં મહત્ત્વનું છે કારણ કે તે નિયંત્રણ નક્કી કરે: સાયક્લોન વાયુ દૂર ન કરી શકે, "
        "અને સૂકી જાડી ધૂળ પર સ્ક્રબર વેડફાય.")]),
    (T("Compare a cyclone separator, a bag filter and an electrostatic precipitator, and state where "
       "each is used.", "સાયક્લોન, બેગ ફિલ્ટર અને ઇલેક્ટ્રોસ્ટેટિક પ્રિસિપિટેટરની સરખામણી કરો અને "
       "દરેક ક્યાં વપરાય તે જણાવો."), 4,
     [P("All three collect dust from a gas stream but by different forces. A cyclone spins the gas so "
        "that centrifugal force throws the particles to the wall; it handles coarse dust above about "
        "10 µm, has low pressure drop, no moving parts and needs no water, so it is used as a "
        "pre-cleaner before a finer device or on a small boiler.",
        "ત્રણેય વાયુ પ્રવાહમાંથી ધૂળ એકઠી કરે પણ જુદાં બળથી. સાયક્લોન વાયુને ફેરવે જેથી કેન્દ્રત્યાગી બળ કણ "
        "દીવાલ તરફ ફેંકે; તે લગભગ 10 µm થી મોટી જાડી ધૂળ સંભાળે, દબાણ ઘટાડો ઓછો, ફરતા ભાગ નહીં અને પાણી "
        "જરૂરી નહીં, તેથી તે પૂર્વ-સફાઈ તરીકે કે નાની બોઈલર પર વપરાય."),
      P("A bag filter passes the gas through woven or felted cloth, so dust is trapped on the surface "
        "and efficiency exceeds 99 % even below 5 µm. It runs on cement kilns, foundries and "
        "incinerators, but it cannot take sticky or condensing dust and the bags must be cleaned by "
        "pulse jets and replaced periodically.",
        "બેગ ફિલ્ટર વાયુને વણાયેલા કે ફેલ્ટ કાપડમાંથી પસાર કરે, તેથી ધૂળ સપાટી પર અટકે અને 5 µm થી નીચે પણ "
        "કાર્યક્ષમતા 99 % થી વધે. તે સિમેન્ટ ભઠ્ઠી, ફાઉન્ડ્રી અને ભઠ્ઠીમાં ચાલે, પણ ચીકણી કે ઘનીભવતી ધૂળ "
        "સહન ન કરે અને થેલા પલ્સ જેટથી સાફ કરી બદલવા પડે."),
      P("An electrostatic precipitator charges the particles and collects them on plates at very high "
        "efficiency for sub-micron dust at huge gas volumes - the standard choice for a coal-fired "
        "power station - but it is large, costly, and its efficiency falls if the gas is cold or the "
        "sulphur content changes.",
        "ઇલેક્ટ્રોસ્ટેટિક પ્રિસિપિટેટર કણને વીજભારિત કરી પ્લેટ પર એકઠા કરે, મોટા વાયુ પ્રમાણમાં સૂક્ષ્મ ધૂળ માટે "
        "ખૂબ ઊંચી કાર્યક્ષમતા સાથે - કોલસા સ્ટેશન માટે પ્રમાણભૂત પસંદગી - પણ તે મોટું, મોંઘું છે અને વાયુ "
        "ઠંડો કે સલ્ફર બદલાય તો કાર્યક્ષમતા ઘટે.")]),
    (T("Describe the primary, secondary and tertiary stages of wastewater treatment with a flow "
       "diagram in words.", "શબ્દોમાં પ્રવાહ આકૃતિ સાથે ગંદા પાણીની સારવારના પ્રાથમિક, દ્વિતીય અને "
       "તૃતીય તબક્કા વર્ણવો."), 5,
     [P("Sewage first passes a bar screen that catches rags and plastic, then a grit chamber where sand "
        "and eggshell settle because the flow is slowed, and an oil trap where floating grease is "
        "skimmed. This preliminary work protects every pump and valve downstream.",
        "ગટરનું પાણી પહેલાં બાર સ્ક્રીનમાંથી પસાર થાય જે ચીંથરાં અને પ્લાસ્ટિક પકડે, પછી ગ્રિટ ચેમ્બરમાં જ્યાં "
        "પ્રવાહ ધીમો પડતાં રેતી અને કવચ બેસે, અને તેલ જાળમાં જ્યાં તરતી ચરબી ઉપરથી લઈ લેવાય. આ પ્રારંભિક "
        "કામ નીચેના દરેક પંપ અને વાલ્વને બચાવે."),
      P("The primary clarifier is a slow tank where settleable solids sink as sludge and scum rises; it "
        "removes 50-65 % of suspended solids and 25-35 % of BOD. The effluent then enters the secondary "
        "stage: in an activated sludge tank air is blown through a dense bacterial culture that eats the "
        "dissolved organics, and a second clarifier separates the grown sludge, part of which is "
        "returned as return activated sludge.",
        "પ્રાથમિક સેટલિંગ ટાંકી ધીમી ટાંકી છે જ્યાં બેસતા ઘન કાદવ તરીકે નીચે અને ફીણ ઉપર આવે; તે નિલંબિત ઘનના "
        "50-65 % અને BOD ના 25-35 % દૂર કરે. પછી પાણી દ્વિતીય તબક્કામાં જાય: એક્ટિવેટેડ સ્લજ ટાંકીમાં ગીચ "
        "જીવાણુ સંસ્કૃતિમાં હવા ફૂંકાય જે ઓગળેલું કાર્બનિક ખાય, અને બીજી સેટલિંગ ટાંકી વધેલો કાદવ અલગ કરે જેમાંથી "
        "ભાગ પરત કાદવ તરીકે પાછો મોકલાય."),
      P("Tertiary treatment polishes what is left: chemical dosing precipitates phosphate, filtration "
        "and activated carbon remove colour and traces, and UV or chlorination kills pathogens before "
        "discharge or reuse. Sludge from both clarifiers is thickened, digested to make biogas and "
        "dewatered, and the dried cake goes to a landfill or to composting. Each stage has a defined "
        "job, and the plant fails if any one of them is undersized.",
        "તૃતીય સારવાર બાકી રહેલું શુદ્ધ કરે: રસાયણથી ફોસ્ફેટ અવક્ષેપિત થાય, ફિલ્ટર અને એક્ટિવેટેડ કાર્બન રંગ "
        "અને અંશ દૂર કરે, અને છોડતાં કે ફરી વાપરતાં પહેલાં UV કે ક્લોરિન રોગકારક મારે. બંને ટાંકીનો કાદવ ઘટ્ટ "
        "કરી, બાયોગેસ માટે પચાવી, પાણી કાઢી સૂકવાય, અને સૂકો પિંડ લેન્ડફિલ કે કમ્પોસ્ટમાં જાય. દરેક તબક્કાનું "
        "નિશ્ચિત કામ છે, અને કોઈ એક નાનું પડે તો પ્લાન્ટ નિષ્ફળ જાય.")]),
    (T("Explain how you would manage the municipal solid waste of a town of two lakh people.",
       "બે લાખ લોકોના નગરનો નગરપાલિકા ઘન કચરો કેવી રીતે સંભાળશો તે સમજાવો."), 5,
     [P("The town makes about 2,00,000 × 0.4 = 80 t of waste a day. The first decision is segregation "
        "into wet, dry and domestic hazardous, collected door to door in covered vehicles on a fixed "
        "route, because mixed waste can only be dumped.",
        "નગર રોજ લગભગ 2,00,000 × 0.4 = 80 ટન કચરો પેદા કરે. પહેલો નિર્ણય ભીનો, સૂકો અને ઘરેલું જોખમી કચરો "
        "અલગ કરવાનો છે, જે ઢાંકેલી ગાડીમાં નિશ્ચિત રૂટ પર ઘરે-ઘરે એકઠો થાય, કારણ કે મિશ્ર કચરો ફક્ત ઠાલવી શકાય."),
      P("With 55 % wet waste, about 44 t a day goes to decentralised composting or a biogas plant, "
        "ideally at ward level so that transport is short; dry waste goes to a materials recovery "
        "facility where paper, metal, glass and PET are baled and sold, and the rest becomes RDF for a "
        "cement kiln. Rejects and inert material go to a sanitary landfill with a liner, leachate "
        "collection and gas vents.",
        "55 % ભીનો કચરો હોય તો લગભગ 44 ટન રોજ વિકેન્દ્રિત કમ્પોસ્ટ કે બાયોગેસ પ્લાન્ટમાં જાય, શક્ય હોય તો વોર્ડ "
        "સ્તરે જેથી વહન ટૂંકું રહે; સૂકો કચરો પદાર્થ પુનઃપ્રાપ્તિ કેન્દ્રમાં જાય જ્યાં કાગળ, ધાતુ, કાચ અને PET "
        "ની ગાંસડી બની વેચાય, અને બાકીનું સિમેન્ટ ભઠ્ઠી માટે RDF બને. નકામો અને નિષ્ક્રિય માલ અસ્તર, લીચેટ "
        "સંગ્રહ અને ગેસ નિકાસવાળી સેનિટરી લેન્ડફિલમાં જાય."),
      P("The plan must carry its own economics and its own people: a user fee or a tipping fee, "
        "compost sold to farmers, an authorised e-waste and hazardous waste channel, safety gear and "
        "training for the collection staff, and a monthly published record of tonnage in and out. "
        "Without the record nobody can prove that the landfill is shrinking rather than growing.",
        "યોજના પોતાનું અર્થશાસ્ત્ર અને પોતાના માણસો સાથે ચાલવી જોઈએ: વપરાશ ફી કે ટિપિંગ ફી, ખેડૂતોને વેચાતું "
        "કમ્પોસ્ટ, ઇ-કચરા અને જોખમી કચરા માટે અધિકૃત માર્ગ, સંગ્રહ કર્મચારીઓ માટે સલામતી સાધન અને તાલીમ, અને "
        "દર મહિને પ્રગટ થતો અંદર-બહારના ટનનો હિસાબ. હિસાબ વગર લેન્ડફિલ ઘટે છે કે વધે તે કોઈ સાબિત કરી શકે નહીં.")]),
    (T("Explain the effects of noise pollution on health and the measures to control it.",
       "ઘોંઘાટ પ્રદૂષણની આરોગ્ય પરની અસરો અને તેના નિયંત્રણના પગલાં સમજાવો."), 4,
     [P("Noise damages health in two ways. Auditory damage begins above 85 dB over a working day: the "
        "hair cells of the inner ear are destroyed and the loss is permanent, first at 4 kHz, then "
        "across speech frequencies. Impulse noise such as a hammer blow can rupture the eardrum at "
        "once.",
        "ઘોંઘાટ આરોગ્યને બે રીતે નુકસાન કરે. શ્રવણને નુકસાન કામકાજના દિવસ દરમિયાન 85 dB થી ઉપર શરૂ થાય: અંદરના "
        "કાનના કોષો નાશ પામે અને નુકસાન કાયમી રહે, પહેલાં 4 kHz પર, પછી બોલીની આવૃત્તિઓ પર. હથોડીના ઘા જેવો "
        "આંચકા ઘોંઘાટ તરત કાનનો પડદો ફાડી શકે."),
      P("Non-auditory effects appear much earlier: raised blood pressure and heart rate, disturbed "
        "sleep even at 45 dB, poor concentration in class, irritability and lower work output. Children "
        "near airports and highways show measurably slower reading progress.",
        "અ-શ્રવણ અસરો ઘણી વહેલી દેખાય: લોહીનું દબાણ અને ધબકારા વધે, 45 dB પર પણ ઊંઘ ડહોળાય, વર્ગમાં ધ્યાન "
        "ઘટે, ચીડિયાપણું અને કામનું ઉત્પાદન ઘટે. વિમાનમથક અને ધોરીમાર્ગ પાસેના બાળકોમાં વાંચનની પ્રગતિ "
        "માપી શકાય તેટલી ધીમી થાય."),
      P("Control works at three points. At the source: quieter machines, silencers, rubber mounts, "
        "enclosure, and shifting compressors and generators away from houses. Along the path: sound "
        "barriers, plantation belts and thick walls. At the receiver: ear plugs and muffs, rotation of "
        "duty, and a quiet room for rest - the last line of defence, never the first.",
        "નિયંત્રણ ત્રણ જગ્યાએ થાય. સ્રોત પર: શાંત મશીન, સાયલન્સર, રબર માઉન્ટ, આવરણ, અને કોમ્પ્રેસર તથા "
        "જનરેટર ઘરોથી દૂર ખસેડવાં. માર્ગ પર: ધ્વનિ અવરોધ, વૃક્ષ પટ્ટી અને જાડી દીવાલ. ગ્રાહક પાસે: કાનપણાં "
        "અને મફ, ફરિયાદ બદલવી, અને આરામ માટે શાંત ઓરડો - છેલ્લી રક્ષા, કદી પહેલી નહીં.")]),
    (T("What are the hazards of plastic waste, and which plastic codes are recyclable?",
       "પ્લાસ્ટિક કચરાનાં જોખમો શું છે અને કયા પ્લાસ્ટિક કોડ રિસાયકલયોગ્ય છે?"), 4,
     [P("Plastic litter blocks drains and is a direct cause of urban flooding; stray cattle and marine "
        "animals swallow bags and starve. In the environment it fragments into microplastics below 5 mm "
        "that plankton absorb and fish pass up the food chain to people, and additives such as "
        "phthalates leach out along the way.",
        "પ્લાસ્ટિક કચરો ગટર રોકે અને શહેરી પૂરનું સીધું કારણ બને; આવારા ઢોર અને દરિયાઈ પ્રાણી થેલી ગળી જઈ "
        "ભૂખ્યાં મરે. પર્યાવરણમાં તે 5 mm થી નાના માઇક્રોપ્લાસ્ટિકમાં તૂટે જે પ્લાંકટન શોષે અને માછલી મારફતે "
        "ખોરાક શૃંખલામાં માણસ સુધી પહોંચે, અને સાથે થેલેટ જેવા ઉમેરણો ઝીણવટથી છૂટે."),
      P("Open burning is worse than the litter: at 300-800 °C it releases dioxins, furans and black "
        "carbon, and the residue ash stays toxic. Landfill plastic takes centuries to break down, and "
        "its leachate carries the additives into groundwater.",
        "ખુલ્લામાં બાળવું કચરા કરતાં વધુ ખરાબ છે: 300-800 °C પર તે ડાયોક્સિન, ફ્યુરાન અને કાળો કાર્બન છોડે, "
        "અને બાકી રહેલી રાખ ઝેરી રહે. લેન્ડફિલમાં પ્લાસ્ટિક તૂટતાં સદીઓ લાગે, અને તેનો લીચેટ ઉમેરણોને "
        "ભૂગર્ભજળમાં લઈ જાય."),
      P("Of the seven resin codes, code 1 (PET bottles), 2 (HDPE cans and pipes) and 5 (PP containers) "
        "have strong recycling markets in India; code 4 (LDPE film and carry bags) is collected but hard "
        "to sort; code 3 (PVC) and 6 (PS) are rarely recycled because they are difficult and their "
        "recyclate is of poor quality; code 7 covers multilayer laminates, which are practically "
        "unrecyclable and belong in RDF.",
        "સાત રેઝિન કોડમાં, કોડ 1 (PET બોટલ), 2 (HDPE ડબ્બા અને પાઇપ) અને 5 (PP પાત્રો)ને ભારતમાં મજબૂત "
        "રિસાયકલ બજાર છે; કોડ 4 (LDPE ફિલ્મ અને થેલી) એકઠો થાય પણ અલગ કરવો મુશ્કેલ છે; કોડ 3 (PVC) અને 6 (PS) "
        "ભાગ્યે જ રિસાયકલ થાય કારણ કે તે મુશ્કેલ છે અને તેમનો રિસાયકલેટ નબળી ગુણવત્તાનો હોય; કોડ 7 મલ્ટિલેયર "
        "સ્તરો માટે છે, જે લગભગ રિસાયકલ ન થાય અને RDF માં જવા યોગ્ય છે.")]),
    (T("Discuss e-waste: its composition, the hazards of informal recycling and the rules that govern "
       "it.", "ઇ-કચરો ચર્ચો: તેની રચના, અસંગઠિત રિસાયકલિંગનાં જોખમો અને તેને નિયંત્રિત કરતા નિયમો."), 5,
     [P("E-waste is discarded electrical and electronic equipment, and it is the fastest growing waste "
        "stream in the world at about 60 million tonnes a year. By mass it is roughly half metal, a "
        "fifth plastic and the rest glass, ceramic and composite, but the small circuit-board and "
        "battery fractions carry the value and the hazard.",
        "ઇ-કચરો એ નકામાં વીજ અને ઇલેક્ટ્રોનિક સાધનો છે, અને તે દુનિયામાં સૌથી ઝડપથી વધતો કચરા પ્રવાહ છે, વર્ષે "
        "લગભગ 60 મિલિયન ટન. દળ પ્રમાણે તે લગભગ અડધું ધાતુ, પાંચમા ભાગનું પ્લાસ્ટિક અને બાકીનું કાચ, કેરામિક "
        "તથા સંયુક્ત છે, પણ નાનો સર્કિટ બોર્ડ અને બેટરીનો ભાગ મૂલ્ય તથા જોખમ બંને ધરાવે."),
      P("Informal recycling is where the harm happens: cables burnt to recover copper, boards bathed in "
        "acid for gold, toner and screens broken open, and the residue tipped into a drain. That "
        "releases dioxins, lead, mercury and cadmium over the settlement that does the work, and "
        "children handle the material directly.",
        "નુકસાન અસંગઠિત રિસાયકલિંગમાં થાય: તાંબું કાઢવા કેબલ બાળવી, સોના માટે બોર્ડ એસિડમાં બોળવા, ટોનર અને "
        "સ્ક્રીન ફೋડી નાખવા, અને અવશેષ ગટરમાં ઠાલવવો. તેનાથી ડાયોક્સિન, સીસું, પારો અને કેડમિયમ એ જ વસાહત "
        "પર ફેલાય જે આ કામ કરે, અને બાળકો સીધા સંપર્કમાં આવે."),
      P("The E-Waste (Management) Rules put the duty on the producer through extended producer "
        "responsibility, licence authorised collection points, dismantlers and recyclers, require a "
        "record of every consignment and ban open burning and acid leaching. An institution complies "
        "when it buys with a take-back clause, stores scrap in a locked room and hands it over only to "
        "an authorised recycler against a manifest.",
        "ઇ-કચરા (વ્યવસ્થાપન) નિયમો વિસ્તૃત ઉત્પાદક જવાબદારી દ્વારા ઉત્પાદક પર ફરજ મૂકે, અધિકૃત સંગ્રહ કેન્દ્ર, "
        "વિઘટક અને રિસાયકલરને પરવાનો આપે, દરેક ખેપની નોંધ ફરજિયાત કરે અને ખુલ્લા દહન તથા એસિડ લીચિંગ પર "
        "પ્રતિબંધ મૂકે. સંસ્થા ત્યારે પાલન કરે જ્યારે તે પરત-ખરીદીની શરત સાથે ખરીદે, ભંગાર તાળાવાળા ઓરડામાં "
        "રાખે અને મેનિફેસ્ટ સામે ફક્ત અધિકૃત રિસાયકલરને સોંપે.")]),
    (T("A factory produces 400 m³ of effluent a day with BOD 500 mg/L and pH 10.5. Suggest a treatment "
       "train.", "એક કારખાનું રોજ 400 m³ ગંદું પાણી BOD 500 mg/L અને pH 10.5 સાથે છોડે છે. સારવારની "
       "શૃંખલા સૂચવો."), 5,
     [P("The load is 400 × 0.5 = 200 kg of BOD a day, which is strong sewage, and the pH of 10.5 is "
        "enough to kill a biological culture. The first step is therefore neutralisation with acid or "
        "flue gas in a mixing tank, controlled to pH 7-8.5, before any biology.",
        "ભાર 400 × 0.5 = 200 kg BOD રોજ છે, જે ભારે ગટર જેવો છે, અને pH 10.5 જૈવિક સંસ્કૃતિ મારી નાખવા પૂરતું "
        "છે. તેથી પહેલું પગલું મિશ્રણ ટાંકીમાં એસિડ કે ફ્લુ ગેસથી ન્યુટ્રલાઇઝેશન છે, જે pH 7-8.5 પર નિયંત્રિત થાય, "
        "કોઈ પણ જૈવિક તબક્કા પહેલાં."),
      P("Then equalisation to level the flow and strength over the day, primary clarification to drop "
        "the settleable solids, and an activated sludge plant or, because the waste is warm and strong, "
        "a UASB reactor followed by an aerobic polishing tank. With 90 % removal at the secondary stage "
        "the outlet carries about 20 kg of BOD, i.e. 50 mg/L, which still needs tertiary polishing for "
        "a 30 mg/L consent.",
        "પછી દિવસભરનો પ્રવાહ અને તીવ્રતા સમાન કરવા ઇક્વલાઇઝેશન, બેસતા ઘન પાડવા પ્રાથમિક સેટલિંગ, અને "
        "એક્ટિવેટેડ સ્લજ પ્લાન્ટ અથવા, કચરો ગરમ અને ભારે હોવાથી, UASB રિએક્ટર પછી વાયુયુક્ત પોલિશિંગ ટાંકી. "
        "દ્વિતીય તબક્કે 90 % દૂર થાય તો બહાર જતું પાણી લગભગ 20 kg BOD એટલે 50 mg/L વહન કરે, જેને 30 mg/L "
        "મંજૂરી માટે હજી તૃતીય પોલિશિંગ જોઈએ."),
      P("The train ends with disinfection and a flow meter at the outlet, sludge thickening and "
        "dewatering, and a monthly analysis of BOD, COD, TSS and pH kept beside the consent order so "
        "that the record proves compliance.",
        "શૃંખલા છોડ પર કીટાણુનાશન અને ફ્લો મીટર સાથે પૂરી થાય, કાદવ ઘટ્ટ કરી પાણી કાઢવાનું, અને BOD, COD, "
        "TSS તથા pH નું માસિક વિશ્લેષણ મંજૂરી હુકમની સાથે રખાય જેથી નોંધ પાલન સાબિત કરે.")]),
    (T("Explain the difference between composting, biogas generation and incineration of waste, and "
       "state when each is appropriate.", "કચરાના કમ્પોસ્ટિંગ, બાયોગેસ ઉત્પાદન અને દહન વચ્ચેનો ભેદ "
       "સમજાવો અને દરેક ક્યારે યોગ્ય છે તે જણાવો."), 4,
     [P("Composting is aerobic: microorganisms break wet organic waste in the presence of air, the heap "
        "heats to 55-65 °C, and the product is a stable humus used as manure at about 25 % of the input "
        "mass. It suits segregated kitchen and market waste and needs turning, moisture control and 6-8 "
        "weeks.",
        "કમ્પોસ્ટિંગ વાયુયુક્ત છે: સૂક્ષ્મજીવો હવાની હાજરીમાં ભીનો કાર્બનિક કચરો તોડે, ઢગલો 55-65 °C સુધી ગરમ "
        "થાય, અને ઉત્પાદન સ્થિર હ્યુમસ છે જે ખાતર તરીકે વપરાય, લગભગ ઇનપુટના 25 % દળ પર. તે અલગ કરેલા રસોડા "
        "અને બજારના કચરા માટે યોગ્ય છે અને ઉથલાવવું, ભેજ નિયંત્રણ અને 6-8 અઠવાડિયાં જોઈએ."),
      P("Anaerobic digestion keeps the same wet waste away from air in a closed reactor, where bacteria "
        "make biogas of 55-65 % methane in 20-30 days; the gas runs a engine or a kitchen, and the "
        "digestate is a liquid fertiliser. It suits a campus, a market or a dairy where the waste is wet "
        "and a gas user sits nearby.",
        "વાયુરહિત પાચન એ જ ભીનો કચરો હવાથી દૂર બંધ રિએક્ટરમાં રાખે, જ્યાં જીવાણુ 20-30 દિવસમાં 55-65 % મિથેનવાળો "
        "બાયોગેસ બનાવે; ગેસ એન્જિન કે રસોડું ચલાવે, અને પાચિત કાદવ પ્રવાહી ખાતર છે. તે કેમ્પસ, બજાર કે ડેરી માટે "
        "યોગ્ય છે જ્યાં કચરો ભીનો હોય અને નજીકમાં ગેસનો વપરાશકર્તા હોય."),
      P("Incineration burns dry, high-calorific waste at 850-1,100 °C, cutting the volume by about 90 % "
        "and giving heat or power, but it needs waste above roughly 1,500 kcal/kg, gas cleaning for "
        "dioxins and a secured landfill for the fly ash. Indian mixed waste at 45 % moisture cannot feed "
        "it; segregated dry waste, RDF or hospital waste can. Choosing wrongly is expensive: a "
        "composter on mixed waste smells and fails, and an incinerator on wet waste needs oil all year.",
        "દહન સૂકા, ઊંચા ઉષ્મા મૂલ્યવાળા કચરાને 850-1,100 °C પર બાળે, ઘનફળ લગભગ 90 % ઘટાડે અને ઉષ્મા કે વીજળી "
        "આપે, પણ તેને લગભગ 1,500 kcal/kg થી વધુ કચરો, ડાયોક્સિન માટે ગેસ સફાઈ અને ફ્લાય એશ માટે સુરક્ષિત લેન્ડફિલ "
        "જોઈએ. 45 % ભેજવાળો ભારતીય મિશ્ર કચરો તેને ખવડાવી શકાય નહીં; અલગ કરેલો સૂકો કચરો, RDF કે હોસ્પિટલ કચરો "
        "શક્ય છે. ખોટી પસંદગી મોંઘી પડે: મિશ્ર કચરા પર કમ્પોસ્ટર દુર્ગંધ ફેલાવી નિષ્ફળ જાય, અને ભીનો કચરો "
        "બાળતી ભઠ્ઠીને આખું વર્ષ તેલ જોઈએ.")]),
    (T("Two machines of 75 dB each and one of 80 dB work in a room. Find the combined level, and suggest "
       "how to bring it under 85 dB at the operator's ear.",
       "એક ઓરડામાં 75 dB નાં બે મશીન અને 80 dB નું એક મશીન ચાલે છે. સંયુક્ત સ્તર શોધો, અને ઓપરેટરના કાન "
       "પાસે તેને 85 dB થી નીચે લાવવાના ઉપાય સૂચવો."), 4,
     [P("Add in energy terms, not in decibels: total = 10 log (10^7.5 + 10^7.5 + 10^8.0) = "
        "10 log (3.16×10⁷ + 3.16×10⁷ + 1.00×10⁸) = 10 log (1.63×10⁸) = 82.1 dB.",
        "સીધા ડેસિબલમાં નહીં, ઊર્જાના સંદર્ભમાં ઉમેરો: કુલ = 10 log (10^7.5 + 10^7.5 + 10^8.0) = "
        "10 log (3.16×10⁷ + 3.16×10⁷ + 1.00×10⁸) = 10 log (1.63×10⁸) = 82.1 dB."),
      P("The answer is a useful surprise: the two 75 dB machines together add only 3 dB, so the single "
        "80 dB machine dominates. Treating that one is worth more than anything done to the other two.",
        "જવાબ ઉપયોગી આશ્ચર્ય છે: 75 dB નાં બે મશીન ભેગાં ફક્ત 3 dB ઉમેરે, તેથી એકલું 80 dB મશીન પ્રભુત્વ ધરાવે. "
        "તેને સુધારવું બાકીનાં બે પર કોઈ પણ કામ કરતાં વધુ ફાયદાકારક છે."),
      P("82 dB is already inside the 85 dB limit for an 8-hour day, but the margin is thin. Practical "
        "steps: an acoustic enclosure and anti-vibration mounts on the 80 dB unit, rubber pads under "
        "the base of all three, moving the compressor to a corner away from the ear, a 2-hour job "
        "rotation, and ear muffs of 25 dB SNR as the last line rather than the first.",
        "82 dB પહેલેથી 8 કલાકના દિવસ માટે 85 dB મર્યાદામાં છે, પણ ગાળિયો પાતળો છે. વ્યવહારુ પગલાં: 80 dB "
        "એકમ પર ધ્વનિ આવરણ અને કંપન-રોધક માઉન્ટ, ત્રણેયના પાયા નીચે રબર પેડ, કોમ્પ્રેસરને કાનથી દૂર ખૂણામાં "
        "ખસેડવું, 2 કલાકની ફરિયાદ, અને પહેલી નહીં પણ છેલ્લી રક્ષા તરીકે 25 dB SNR નાં કાનપણાં.")]),
    (T("Why is leachate a problem at a landfill, and how is it controlled?",
       "લેન્ડફિલ પર લીચેટ સમસ્યા કેમ છે અને તેને કેવી રીતે નિયંત્રિત કરાય?"), 4,
     [P("Rain falling on waste percolates through it and dissolves whatever it touches, producing a "
        "dark liquid with very high BOD, COD, ammonia and heavy metals - typical values of 5,000-20,000 "
        "mg/L BOD and 20,000-50,000 mg/L COD. If it escapes, it contaminates groundwater for decades "
        "and the damage cannot be undone.",
        "કચરા પર પડતો વરસાદ તેમાંથી પસાર થઈ જે અડે તે ઓગાળે, અને બહુ ઊંચા BOD, COD, એમોનિયા અને ભારે ધાતુવાળું "
        "કાળું પ્રવાહી બને - સામાન્ય રીતે 5,000-20,000 mg/L BOD અને 20,000-50,000 mg/L COD. તે બહાર નીકળે તો "
        "દાયકાઓ સુધી ભૂગર્ભજળ પ્રદૂષિત કરે અને નુકસાન પાછું વાળી ન શકાય."),
      P("Control starts with water: a clay or geomembrane liner at the base, a drain and collection "
        "pipe system above it, and daily compaction and cover so that rain cannot enter the waste. The "
        "collected leachate is recirculated to speed decomposition or treated in a dedicated plant with "
        "anaerobic digestion and membrane filtration.",
        "નિયંત્રણ પાણીથી શરૂ થાય: પાયામાં માટી કે જીઓમેમ્બ્રેન અસ્તર, તેની ઉપર નાળી અને સંગ્રહ પાઇપ તંત્ર, અને "
        "રોજ દબાવીને આવરણ જેથી વરસાદ કચરામાં ન પેસે. એકઠું થયેલું લીચેટ વિઘટન ઝડપી કરવા પાછું છાંટાય છે કે "
        "વાયુરહિત પાચન અને મેમ્બ્રેન ગાળણવાળા સમર્પિત પ્લાન્ટમાં સારવાર પામે."),
      P("Monitoring closes the loop: piezometers around the site for groundwater level and quality, a "
        "gas extraction well for methane, and a post-closure plan for thirty years after the last "
        "truck. A landfill without leachate control is simply an open dump with paperwork.",
        "દેખરેખ ચક્ર પૂરું કરે: સ્થળની આસપાસ જળસ્તર અને ગુણવત્તા માટે પાઇઝોમીટર, મિથેન માટે ગેસ નિકાસ કૂવો, "
        "અને છેલ્લી ગાડી પછી ત્રીસ વર્ષની બંધ પછીની યોજના. લીચેટ નિયંત્રણ વગરની લેન્ડફિલ એટલે કાગળ પરનો "
        "ખુલ્લો ઢગલો.")]),
    (T("Describe the collection and disposal system you would propose for the hazardous waste of an "
       "industrial estate.", "ઔદ્યોગિક વિસ્તારના જોખમી કચરા માટે સૂચવેલી સંગ્રહ અને નિકાલ પ્રણાલી "
       "વર્ણવો."), 4,
     [P("First identify and quantify: a register of every unit in the estate, the waste streams it "
        "produces, their hazard class, monthly quantity and current route. Most estates find that a "
        "handful of units produce most of the hazardous waste, and that some streams are so dilute "
        "that they could be treated on site.",
        "પહેલાં ઓળખ અને ગણતરી: વિસ્તારના દરેક એકમનું રજિસ્ટર, તેનો કચરા પ્રવાહ, જોખમ વર્ગ, માસિક જથ્થો અને હાલનો "
        "રસ્તો. મોટા ભાગના વિસ્તારોમાં થોડા એકમો મોટાભાગનો જોખમી કચરો પેદા કરતા હોય છે, અને કેટલાક પ્રવાહ એટલા પાતળા "
        "હોય કે સ્થળ પર જ સારવાર થઈ શકે."),
      P("Then separate and store: a covered, bunded, ventilated store at each unit with labelled drums, "
        "different areas for acid, solvent, oxidiser and oil, an impervious floor, a fire extinguisher "
        "and a spill kit. Every drum carries a label and every movement a manifest, so the chain of "
        "custody is traceable from the shop floor to the final disposal cell.",
        "પછી અલગ કરી સંગ્રહ: દરેક એકમ પર ઢાંકેલું, ફરતે ઓરડીવાળું, હવાઉજાસવાળું સંગ્રહસ્થાન, લેબલવાળા ડ્રમ, એસિડ, "
        "દ્રાવક, ઓક્સિડાઇઝર અને તેલ માટે જુદા વિભાગ, અભેદ્ય ફર્શ, અગ્નિશામક અને ગળતર સાફ કરવાની કિટ. દરેક ડ્રમ પર "
        "લેબલ અને દરેક હલનચલન પર મેનિફેસ્ટ, જેથી જવાબદારીની શૃંખલા દુકાનના ફર્શથી અંતિમ નિકાલના કોષ સુધી દેખાય."),
      P("Finally treat: a common facility for the estate treats acids by neutralisation, waste oil by "
        "re-refining, oily sludge and plating waste by stabilisation and solidification, and clinical "
        "or solvent waste by high-temperature incineration, with the residue going to a secured "
        "landfill and the emission to a continuous monitor. Training, a doctor on call and a spill "
        "drill twice a year make the system real.",
        "અંતે સારવાર: વિસ્તાર માટેની સામાન્ય સુવિધા એસિડને ન્યુટ્રલાઇઝેશનથી, વપરાયેલા તેલને ફરી શુદ્ધ કરીને, તેલવાળા "
        "કાદવ અને પ્લેટિંગ કચરાને સ્થિરીકરણ-ઘનીકરણથી અને ક્લિનિકલ કે દ્રાવક કચરાને ઊંચા તાપમાનના દહનથી સારવાર કરે, "
        "અવશેષ સુરક્ષિત લેન્ડફિલમાં અને ઉત્સર્જન સતત મોનિટર પર જાય. તાલીમ, ફોન પર ડૉક્ટર અને વર્ષે બે વાર ગળતર "
        "કવાયત પ્રણાલીને વાસ્તવિક બનાવે.")]),
]

EXAM = [{"q": q, "marks": m} for q, m, _parts in _PRACTICE]
PRACTICE_ANSWERS = [_join(parts) for _q, _m, parts in _PRACTICE]

LESSON_COUNT = sum(len(s["items"]) for s in NOTES)
