"""DI02000051 Environmental Sustainability - Unit 3: Renewable Energy Technologies.

GTU 3.1-3.6, 7 h, 25 %, 18 marks, CO3. Every text node carries English and Gujarati.
"""
from content_DI02000051_u1_notes import T, P, H4, UL, OL, TB, card, num, _join

SOURCES = [
    T("GTU DI02000051 Environmental Sustainability syllabus (uploaded PDF, w.e.f. 2024-25)",
      "GTU DI02000051 પર્યાવરણીય ટકાઉપણું સિલેબસ (અપલોડ કરેલ PDF, 2024-25થી અમલમાં)"),
    T("C. S. Solanki - Renewable Energy Technologies: A Practical Guide for Beginners, PHI Learning",
      "સી. એસ. સોલંકી - રિન્યુએબલ એનર્જી ટેક્નોલોજીસ: એ પ્રેક્ટિકલ ગાઇડ ફોર બિગિનર્સ, PHI લર્નિંગ"),
    T("Ministry of New and Renewable Energy (MNRE) annual report and solar, wind and biogas programmes",
      "નવી અને પુનઃપ્રાપ્ય ઊર્જા મંત્રાલય (MNRE) વાર્ષિક અહેવાલ તથા સૌર, પવન અને બાયોગેસ કાર્યક્રમો"),
    T("NISE and NIWE technical notes on solar modules and wind turbine classes",
      "સૌર મોડ્યુલ અને પવન ટર્બાઇન વર્ગો પર NISE અને NIWE ની ટેકનિકલ નોંધ"),
    T("IPCC AR6 WG III chapter on energy systems, and IEA renewable energy market reports",
      "ઊર્જા પ્રણાલી પર IPCC AR6 WG III પ્રકરણ અને IEA ના પુનઃપ્રાપ્ય ઊર્જા બજાર અહેવાલો"),
]

NOTES = [
    {"title": T("1. Renewable Energy and the Carbon Footprint",
                "1. પુનઃપ્રાપ્ય ઊર્જા અને કાર્બન ફૂટપ્રિન્ટ"),
     "items": [
         card(T("3.1 Why renewable energy cuts the carbon footprint",
                "3.1 પુનઃપ્રાપ્ય ઊર્જા કાર્બન ફૂટપ્રિન્ટ કેમ ઘટાડે"),
              [H4("The chain that matters", "મહત્ત્વની શૃંખલા"),
               P("About three quarters of the world's greenhouse gas emissions come from burning coal, "
                 "oil and gas for electricity, heat, transport and industry. A renewable plant does not "
                 "burn fuel, so it produces no CO₂ while it runs; its emissions are moved to the "
                 "factory that makes the panels or turbines and to the vehicles that install them. "
                 "That is why a renewable source is judged by its <b>carbon payback</b>: the years a "
                 "wind turbine takes to generate the energy that was spent building it - usually six "
                 "to twelve months for wind and one to two years for solar.",
                 "દુનિયાના લગભગ ત્રણ ચતુર્થાંશ હરિતગૃહ વાયુ ઉત્સર્જન વીજળી, ઉષ્મા, વાહનવ્યવહાર અને ઉદ્યોગ માટે "
                 "કોલસો, તેલ અને ગેસ બાળવાથી આવે. પુનઃપ્રાપ્ય સ્ટેશન ઇંધણ બાળતું નથી, તેથી ચાલુ હોય ત્યારે CO₂ "
                 "બનાવતું નથી; તેનું ઉત્સર્જન પેનલ કે ટર્બાઇન બનાવતી ફેક્ટરી અને ગોઠવણી કરતાં વાહનો તરફ ખસે છે. "
                 "તેથી પુનઃપ્રાપ્ય સ્રોત તેના <b>કાર્બન પરતફેળા</b>થી માપવાય: બાંધવામાં વપરાયેલી ઊર્જા પાછી "
                 "મેળવવા ટર્બાઇનને લાગતાં વર્ષો - સામાન્ય રીતે પવન માટે છથી બાર મહિના અને સૌર માટે એકથી બે વર્ષ."),
               H4("What makes it cheap now", "હવે તે સસ્તું કેમ બન્યું"),
               P("The cost of solar electricity has fallen by roughly ninety per cent in a decade and "
                 "on-shore wind by nearly seventy per cent, because module prices dropped, turbines "
                 "grew taller and financing became cheaper. In India solar and wind now sell power "
                 "below five rupees a unit, cheaper than a new coal plant, which is why the target of "
                 "500 GW of non-fossil capacity by 2030 is being built through auctions rather than "
                 "subsidy alone.",
                 "સૌર વીજળીનો ખર્ચ એક દાયકામાં લગભગ નેવું ટકા અને સ્થળ પરના પવનનો લગભગ સિત્તેર ટકા ઘટ્યો, "
                 "કારણ કે મોડ્યુલના ભાવ ઘટ્યા, ટર્બાઇન ઊંચા થયા અને ધિરાણ સસ્તું થયું. ભારતમાં સૌર અને પવન હવે "
                 "એક યુનિટ પાંચ રૂપિયાથી ઓછામાં વીજળી વેચે, નવા કોલસા સ્ટેશન કરતાં સસ્તું, તેથી 2030 સુધીમાં "
                 "500 GW બિન-અશ્મીય ક્ષમતાનું લક્ષ્ય ફક્ત સબસિડીથી નહીં, હરાજી દ્વારા બની રહ્યું છે."),
               H4("Four benefits, four costs", "ચાર લાભ, ચાર ખર્ચ"),
               TB([T("Benefit", "લાભ"), T("Why it matters", "કેમ મહત્ત્વનું")],
                  [[T("no fuel bill", "ઇંધણનું બિલ નહીં"), T("the sun and wind are free, so the cost is fixed for 25 years", "સૂર્ય અને પવન મફત છે, તેથી 25 વર્ષ ખર્ચ નિશ્ચિત રહે")],
                   [T("energy security", "ઊર્જા સુરક્ષા"), T("imported coal and gas can be cut, and the rupee is saved", "આયાત કોલસો અને ગેસ ઘટે, રૂપિયો બચે")],
                   [T("local jobs", "સ્થાનિક રોજગાર"), T("installation and maintenance work stays in the district", "ગોઠવણી અને જાળવણીનું કામ જિલ્લામાં જ રહે")],
                   [T("clean air too", "સ્વચ્છ હવા પણ"), T("no SO₂, NOx or fly ash at the plant", "સ્ટેશન પર SO₂, NOx કે ફ્લાય એશ નહીં")],
                   [T("intermittent output", "અનિયમિત ઉત્પાદન"), T("no sun at night, no wind on a calm day", "રાત્રે સૂર્ય નહીં, શાંત દિવસે પવન નહીં")],
                   [T("land and roof area", "જમીન અને છતનો વિસ્તાર"), T("about 4 acres per MW of solar, more for wind", "સૌરના 1 MW દીઠ લગભગ 4 એકર, પવન માટે વધુ")],
                   [T("storage or backup", "સંગ્રહ કે બેકઅપ"), T("batteries and gas peakers cost extra", "બેટરી અને ગેસ પીકર વધારાનો ખર્ચ")],
                   [T("grid work", "ગ્રિડનું કામ"), T("lines and substations must be strengthened", "લાઇન અને સબસ્ટેશન મજબૂત કરવા પડે")]]),
               H4("Worked example", "ઉકેલાયેલ દાખલો"),
               P("A 1 MW rooftop plant in Surat runs about 1,450 kWh per kW per year, so it makes "
                 "1,450 MWh. At the Indian grid factor of 0.71 t CO₂ per MWh it avoids about 1,030 t "
                 "of CO₂ a year - the yearly emissions of roughly 500 city cars.",
                 "સુરતમાં 1 MWનું છત પરનું સ્ટેશન દર વર્ષે પ્રતિ kW લગભગ 1,450 kWh બનાવે, એટલે 1,450 MWh. "
                 "ભારતીય ગ્રિડ અવયવ 0.71 t CO₂ પ્રતિ MWh પ્રમાણે તે વર્ષે લગભગ 1,030 t CO₂ બચાવે - જે લગભગ "
                 "500 શહેરી કારના વાર્ષિક ઉત્સર્જન જેટલું છે.")],
              "u3_mix", syllabus_item="3.1"),
         card(T("3.2 Renewable and non-renewable sources compared",
                "3.2 પુનઃપ્રાપ્ય અને બિન-પુનઃપ્રાપ્ય સ્રોતોની સરખામણી"),
              [H4("The dividing line", "ભેદરેખા"),
               P("A <b>non-renewable</b> source holds a fixed stock that was made over millions of "
                 "years - coal, oil, natural gas and uranium. Every unit burnt reduces the stock, and "
                 "the fuel must be mined, transported and paid for again and again. A <b>renewable</b> "
                 "source is a flow that nature refills within a human lifetime - sunlight, wind, "
                 "falling water, heat from the earth, tides, and biomass grown on land.",
                 "<b>બિન-પુનઃપ્રાપ્ય</b> સ્રોતમાં કરોડો વર્ષમાં બનેલો નિશ્ચિત સંગ્રહ હોય - કોલસો, તેલ, કુદરતી "
                 "ગેસ અને યુરેનિયમ. બળે તે દરેક એકમ સંગ્રહ ઘટાડે અને ઇંધણ ખાણમાંથી કાઢી, વહન કરી, વારંવાર ખરીદવું "
                 "પડે. <b>પુનઃપ્રાપ્ય</b> સ્રોત એ પ્રવાહ છે જે કુદરત માણસના આયુષ્યમાં ફરી ભરે - સૂર્યપ્રકાશ, પવન, "
                 "પડતું પાણી, પૃથ્વીની ઉષ્મા, ભરતી અને જમીન પર ઉગતું બાયોમાસ."),
               H4("Side-by-side comparison", "સાથે સરખામણી"),
               TB([T("Point", "મુદ્દો"), T("Renewable", "પુનઃપ્રાપ્ય"), T("Non-renewable", "બિન-પુનઃપ્રાપ્ય")],
                  [[T("availability", "ઉપલબ્ધતા"), T("refilled by nature, never exhausted", "કુદરત ભરે, કદી ખતમ ન થાય"), T("finite stock, 50-150 years at present use", "મર્યાદિત સંગ્રહ, હાલના વપરાશે 50-150 વર્ષ")],
                   [T("running cost", "ચાલુ ખર્ચ"), T("almost zero, no fuel", "લગભગ શૂન્ય, ઇંધણ નહીં"), T("fuel is 60-80 % of the cost", "ઇંધણ ખર્ચના 60-80 %")],
                   [T("capital cost", "મૂડી ખર્ચ"), T("high upfront, then cheap", "શરૂઆતમાં વધુ, પછી સસ્તું"), T("lower per MW but fuel keeps adding", "પ્રતિ MW ઓછું, પણ ઇંધણ ઉમેરાતું રહે")],
                   [T("output", "ઉત્પાદન"), T("variable, depends on weather", "બદલાતું, હવામાન પર આધારિત"), T("firm, dispatchable on demand", "નિશ્ચિત, માંગ પ્રમાણે આપી શકાય")],
                   [T("capacity factor", "ક્ષમતા અવયવ"), T("solar 15-22 %, wind 25-35 %", "સૌર 15-22 %, પવન 25-35 %"), T("coal 55-70 %, nuclear above 80 %", "કોલસો 55-70 %, ન્યુક્લિયર 80 %થી વધુ")],
                   [T("land", "જમીન"), T("large area per MW, can be dual use", "પ્રતિ MW મોટો વિસ્તાર, બેવડો ઉપયોગ શક્ય"), T("compact, but mines and ash ponds spread far", "સંકુચિત, પણ ખાણ અને રાખના તળાવ દૂર સુધી ફેલાય")],
                   [T("emissions", "ઉત્સર્જન"), T("none in operation, small life-cycle share", "ચાલુ સ્થિતિમાં નહીં, જીવનચક્રમાં થોડું"), T("CO₂, SO₂, NOx, ash, mercury", "CO₂, SO₂, NOx, રાખ, પારો")],
                   [T("waste", "કચરો"), T("module and blade waste after 25 years", "25 વર્ષ પછી મોડ્યુલ અને બ્લેડનો કચરો"), T("ash ponds, mine spoils, radioactive spent fuel", "રાખના તળાવ, ખાણનો કચરો, કિરણોત્સર્ગી વપરાયેલ ઇંધણ")]]),
               H4("How to compare fairly", "ન્યાયી સરખામણી કેમ કરવી"),
               P("Never compare a kW with a kW. Compare the <b>levellised cost of energy</b> (LCOE, the "
                 "total lifetime cost divided by the total lifetime units) and the <b>emissions per "
                 "kWh</b> over the whole life. On that basis Indian solar is about 2.5-3.5 rupees a "
                 "unit against 4-6 for new coal, and solar emits 40-50 g CO₂ per kWh against 800-1,000 "
                 "for coal.",
                 "kW ને kW સાથે કદી સરખાવવું નહીં. <b>સમતુલિત ઊર્જા ખર્ચ</b> (LCOE, આખા જીવનનો કુલ ખર્ચ ભાગ્યા "
                 "કુલ યુનિટ) અને આખા જીવનના <b>પ્રતિ kWh ઉત્સર્જન</b> સરખાવો. તે આધારે ભારતીય સૌર યુનિટના "
                 "લગભગ 2.5-3.5 રૂપિયા, નવા કોલસાના 4-6 સામે, અને સૌર પ્રતિ kWh 40-50 g CO₂ છોડે, કોલસાના "
                 "800-1,000 સામે.")],
              syllabus_item="3.2"),
     ]},
    {"title": T("2. Solar Photovoltaics", "2. સૌર ફોટોવોલ્ટેઇક"),
     "items": [
         card(T("3.3 The principle of photovoltaic conversion",
                "3.3 ફોટોવોલ્ટેઇક રૂપાંતરણનો સિદ્ધાંત"),
              [H4("The photovoltaic effect", "ફોટોવોલ્ટેઇક પ્રભાવ"),
               P("A solar cell is a thin sandwich of two differently doped silicon layers. The "
                 "<b>n-layer</b> has extra electrons, the <b>p-layer</b> has holes, and where they meet "
                 "a built-in electric field forms across the <b>junction</b>. When a photon with "
                 "enough energy strikes the silicon it frees an electron; the field pushes that "
                 "electron one way and leaves a hole the other way, so a current flows when the front "
                 "and back contacts are joined through a load. Nothing moves mechanically - light goes "
                 "straight to electricity, which is why a cell has no fuel, no flame and almost no "
                 "maintenance.",
                 "સૌર સેલ એ બે જુદી રીતે ડોપ કરેલા સિલિકોન સ્તરોની પાતળી સેન્ડવિચ છે. <b>n-સ્તર</b>માં વધારાના "
                 "ઇલેક્ટ્રોન, <b>p-સ્તર</b>માં કાણાં હોય અને જ્યાં મળે ત્યાં <b>સંધિ</b> પર આંતરિક વિદ્યુતક્ષેત્ર "
                 "બને. પૂરતી ઊર્જાવાળો ફોટોન સિલિકોન પર પડે ત્યારે ઇલેક્ટ્રોન મુક્ત થાય; ક્ષેત્ર તેને એક તરફ અને "
                 "કાણું બીજી તરફ ધકેલે, તેથી આગળ-પાછળના સંપર્કો ભાર દ્વારા જોડાય તો પ્રવાહ વહે. યાંત્રિક રીતે કંઈ "
                 "ફરતું નથી - પ્રકાશ સીધો વીજળી બને, તેથી સેલમાં ઇંધણ નહીં, જ્યોત નહીં અને જાળવણી લગભગ નહીં."),
               H4("Band gap decides the colour", "બેન્ડ ગેપ રંગ નક્કી કરે"),
               P("Only photons with energy above the <b>band gap</b> can free an electron. Silicon's "
                 "gap is 1.1 eV, matching red and infrared light, so a silicon cell ignores about half "
                 "the solar spectrum as heat and gives up part of each photon's energy as heat as well. "
                 "That double loss is the reason a commercial module reaches only 18-22 % efficiency "
                 "while the theoretical limit for a single junction, the Shockley-Queisser limit, is "
                 "about 33 %.",
                 "ફક્ત <b>બેન્ડ ગેપ</b>થી વધુ ઊર્જાવાળા ફોટોન ઇલેક્ટ્રોન મુક્ત કરી શકે. સિલિકોનનો ગેપ 1.1 eV છે, "
                 "જે લાલ અને ઇન્ફ્રારેડ પ્રકાશને મળે, તેથી સિલિકોન સેલ સૂર્યના લગભગ અડધા વર્ણપટને ઉષ્મા તરીકે "
                 "અવગણે અને દરેક ફોટોનની થોડી ઊર્જા પણ ઉષ્મા તરીકે ગુમાવે. આ બેવડી ખોટને કારણે વ્યાવસાયિક મોડ્યુલ "
                 "ફક્ત 18-22 % કાર્યક્ષમતા પામે, જ્યારે એક સંધિની સૈદ્ધાંતિક મર્યાદા, શોકલી-ક્વાઇસર મર્યાદા, "
                 "લગભગ 33 % છે."),
               H4("Reading the I-V curve", "I-V વણકર વાંચવી"),
               TB([T("Term", "શબ્દ"), T("Meaning", "અર્થ")],
                  [[T("Isc, short-circuit current", "Isc, ટૂંકા પરિપથનો પ્રવાહ"), T("current when the terminals are joined; grows with light", "ટર્મિનલ જોડાય ત્યારે પ્રવાહ; પ્રકાશ સાથે વધે")],
                   [T("Voc, open-circuit voltage", "Voc, ખુલ્લા પરિપથનો વોલ્ટેજ"), T("voltage with no load; about 0.6-0.7 V per silicon cell", "ભાર વગરનો વોલ્ટેજ; સિલિકોન સેલ દીઠ લગભગ 0.6-0.7 V")],
                   [T("MPP, maximum power point", "MPP, મહત્તમ શક્તિ બિંદુ"), T("the knee of the curve, where V × I is largest", "વણકરનું ઘૂંટણ, જ્યાં V × I સૌથી વધુ")],
                   [T("fill factor", "ભરણ અવયવ"), T("MPP power divided by Voc × Isc, typically 0.75-0.82", "MPP શક્તિ ભાગ્યા Voc × Isc, સામાન્ય રીતે 0.75-0.82")],
                   [T("efficiency", "કાર્યક્ષમતા"), T("MPP power divided by the sunlight falling on the cell", "MPP શક્તિ ભાગ્યા સેલ પર પડતો સૂર્યપ્રકાશ")]]),
               H4("What steals the output", "ઉત્પાદન શું ખાઈ જાય"),
               UL(("heat: a hot module loses 0.35-0.45 % of its power per degree above 25 °C", "ઉષ્મા: 25 °C થી ઉપર દરેક ડિગ્રીએ મોડ્યુલ તેની શક્તિના 0.35-0.45 % ગુમાવે"),
                  ("dust and bird droppings: 5-25 % loss without cleaning", "ધૂળ અને પક્ષીના મળ: સફાઈ વગર 5-25 % ખોટ"),
                  ("shade on one cell: bypass diodes save the string but the whole module drops", "એક સેલ પર છાયો: બાયપાસ ડાયોડ શ્રેણી બચાવે પણ આખું મોડ્યુલ નીચે આવે"),
                  ("cable, inverter and mismatch loss: 10-15 % together", "કેબલ, ઇન્વર્ટર અને મેળ ન બેસવાની ખોટ: ભેગી 10-15 %")),
               H4("Common mistake", "સામાન્ય ભૂલ"),
               P("Sizing an inverter for the panel's Voc at 25 °C. In a cold morning the open-circuit "
                 "voltage of a string rises by about 0.3 % per degree below 25 °C and can exceed the "
                 "inverter's limit; always size the string on the record low temperature, not on the "
                 "datasheet value alone.",
                 "25 °C પરની પેનલની Voc પ્રમાણે ઇન્વર્ટર પસંદ કરવું. ઠંડી સવારે શ્રેણીનો ખુલ્લા પરિપથનો વોલ્ટેજ "
                 "25 °C થી નીચે દરેક ડિગ્રીએ લગભગ 0.3 % વધે અને ઇન્વર્ટરની મર્યાદા વટાવી શકે; શ્રેણી હંમેશા "
                 "નોંધાયેલા ન્યૂનતમ તાપમાન પ્રમાણે નક્કી કરો, ફક્ત ડેટાશીટના આંકડા પ્રમાણે નહીં.")],
              "u3_pv", syllabus_item="3.3"),
         card(T("3.3 Types of solar cells and how a module is built",
                "3.3 સૌર સેલના પ્રકાર અને મોડ્યુલ કેવી રીતે બને"),
              [H4("The three families", "ત્રણ કુટુંબ"),
               P("Solar cells are grouped by the material that absorbs the light. <b>Crystalline "
                 "silicon</b>, either monocrystalline or polycrystalline, is more than ninety per cent "
                 "of the market because it is efficient, stable and now cheap. <b>Thin film</b> cells - "
                 "cadmium telluride, copper indium gallium selenide and amorphous silicon - use a "
                 "micrometre of material on glass and win on price per area in very large plants and "
                 "on flexible or curved roofs. <b>Emerging</b> cells, mainly perovskite and organic, "
                 "promise higher efficiency at low cost but are still being tested for twenty-five "
                 "year life.",
                 "સૌર સેલ પ્રકાશ શોષતા પદાર્થ પ્રમાણે વહેંચાય. <b>સ્ફટિકીય સિલિકોન</b>, મોનોક્રિસ્ટાલાઇન કે "
                 "પોલીક્રિસ્ટાલાઇન, બજારના નેવું ટકાથી વધુ છે કારણ કે તે કાર્યક્ષમ, ટકાઉ અને હવે સસ્તું છે. "
                 "<b>પાતળી ફિલ્મ</b> સેલ - કેડમિયમ ટેલ્યુરાઇડ, કોપર ઇન્ડિયમ ગેલિયમ સેલેનાઇડ અને એમોર્ફસ સિલિકોન "
                 "- કાચ પર માઇક્રોમીટર જેટલો પદાર્થ વાપરે અને ખૂબ મોટા સ્ટેશન તથા લવચીક કે વળેલી છત પર "
                 "પ્રતિ વિસ્તાર ભાવમાં જીતે. <b>ઉભરતા</b> સેલ, મુખ્યત્વે પેરોવસ્કાઇટ અને ઓર્ગેનિક, ઓછા ખર્ચે "
                 "વધુ કાર્યક્ષમતાનું વચન આપે છે પણ પચ્ચીસ વર્ષના આયુષ્ય માટે હજી પરીક્ષણમાં છે."),
               H4("Comparison table", "સરખામણી કોષ્ટક"),
               TB([T("Type", "પ્રકાર"), T("Efficiency", "કાર્યક્ષમતા"), T("Strength", "તાકાત"), T("Weakness", "નબળાઈ")],
                  [[T("monocrystalline silicon", "મોનોક્રિસ્ટાલાઇન સિલિકોન"), T("20-23 %", "20-23 %"), T("best output per square metre, 25 year life", "પ્રતિ ચોરસ મીટર શ્રેષ્ઠ ઉત્પાદન, 25 વર્ષ આયુષ્ય"), T("costliest of the three, needs full sun", "ત્રણમાં સૌથી મોંઘું, પૂરો તડકો જોઈએ")],
                   [T("polycrystalline silicon", "પોલીક્રિસ્ટાલાઇન સિલિકોન"), T("15-18 %", "15-18 %"), T("cheapest silicon, simple to make", "સૌથી સસ્તું સિલિકોન, બનાવવું સહેલું"), T("more area for the same kW, lower heat tolerance", "સમાન kW માટે વધુ વિસ્તાર, ઉષ્મા સહન ઓછું")],
                   [T("CdTe thin film", "CdTe પાતળી ફિલ્મ"), T("16-19 %", "16-19 %"), T("cheap large panels, good in weak light", "સસ્તી મોટી પેનલ, નબળા પ્રકાશમાં સારું"), T("cadmium toxicity, tellurium supply", "કેડમિયમ ઝેરીલાપણું, ટેલ્યુરિયમનો પુરવઠો")],
                   [T("CIGS thin film", "CIGS પાતળી ફિલ્મ"), T("17-20 %", "17-20 %"), T("flexible, high yield in heat and shade", "લવચીક, ઉષ્મા અને છાયામાં સારું ઉત્પાદન"), T("indium cost, complex process", "ઇન્ડિયમનો ખર્ચ, જટિલ પ્રક્રિયા")],
                   [T("amorphous silicon", "એમોર્ફસ સિલિકોન"), T("6-9 %", "6-9 %"), T("very cheap, works on curved and dim surfaces", "ખૂબ સસ્તું, વળેલી અને મંદ સપાટી પર ચાલે"), T("low output, degrades in the first months", "ઓછું ઉત્પાદન, શરૂઆતના મહિનામાં ઘટે")],
                   [T("perovskite / tandem", "પેરોવસ્કાઇટ / ટેન્ડમ"), T("25-33 % in the lab", "લેબમાં 25-33 %"), T("highest efficiency, printable, cheap material", "સૌથી વધુ કાર્યક્ષમતા, છપાય, સસ્તો પદાર્થ"), T("moisture and UV instability, lead content", "ભેજ અને UV અસ્થિરતા, સીસાનું પ્રમાણ")]]),
               H4("From cell to array", "સેલથી એરે સુધી"),
               OL(("About 60 or 72 cells are soldered in series and laminated under glass, ethylene vinyl "
                   "acetate and a back sheet to make a <b>module</b>; the series connection adds the "
                   "voltage, not the current.", "લગભગ 60 કે 72 સેલ શ્રેણીમાં જોડી, કાચ, એથિલિન વિનાઇલ "
                   "એસિટેટ અને બેક શીટ નીચે લેમિનેટ કરીને <b>મોડ્યુલ</b> બને; શ્રેણી જોડાણ વોલ્ટેજ ઉમેરે, "
                   "પ્રવાહ નહીં."),
                  ("Modules are mounted on a frame at the local latitude tilt, facing south in India, "
                   "and wired in strings to a <b>combiner box</b>.", "મોડ્યુલ સ્થાનિક અક્ષાંશ જેટલા ઝુકાવ પર, "
                   "ભારતમાં દક્ષિણ તરફ મુખ રાખી ફ્રેમ પર ગોઠવાય અને શ્રેણીમાં જોડાઈ <b>કોમ્બાઇનર બોક્સ</b> "
                   "સુધી જાય."),
                  ("A <b>string inverter</b> or a central inverter converts DC to AC; a transformer "
                   "steps it up to 11 or 33 kV for the grid.", "<b>સ્ટ્રિંગ ઇન્વર્ટર</b> કે કેન્દ્રીય ઇન્વર્ટર DCને AC "
                   "બનાવે; ટ્રાન્સફોર્મર ગ્રિડ માટે 11 કે 33 kV સુધી વધારે."),
                  ("Meters, protection and a data logger complete the plant; the performance ratio "
                   "compares the actual output with the ideal.", "મીટર, રક્ષણ અને ડેટા લોગર સ્ટેશન પૂરું કરે; "
                   "કાર્યદક્ષતા ગુણોત્તર વાસ્તવિક ઉત્પાદનને આદર્શ સાથે સરખાવે.")),
               H4("Worked example", "ઉકેલાયેલ દાખલો"),
               P("A 445 Wp module of 2.1 m² under 1,000 W/m² receives 2,100 W and delivers 445 W, so "
                 "its efficiency is 445 / 2,100 = 21.2 %. Eighteen such modules make an 8 kW array.",
                 "2.1 m² નું 445 Wp મોડ્યુલ 1,000 W/m² હેઠળ 2,100 W પામે અને 445 W આપે, તેથી તેની કાર્યક્ષમતા "
                 "445 / 2,100 = 21.2 % થાય. આવા અઢાર મોડ્યુલ 8 kWની એરે બનાવે.")],
              "u3_cells", syllabus_item="3.3"),
     ]},
    {"title": T("3. Wind Energy", "3. પવન ઊર્જા"),
     "items": [
         card(T("3.4 The wind resource and the power in it",
                "3.4 પવન સંસાધન અને તેમાં રહેલી શક્તિ"),
              [H4("Why wind speed matters so much", "પવનની ગતિ કેમ આટલી મહત્ત્વની"),
               P("The power available in moving air goes with the <b>cube</b> of the speed: double the "
                 "wind and you get eight times the power, so a site with a mean of 7 m/s produces far "
                 "more than twice the energy of a site with 5 m/s. Wind is also slower and steadier "
                 "near the ground, which is why towers are now 100-140 m tall and blades 60-80 m long: "
                 "the swept area grows with the square of the diameter, and every extra metre of rotor "
                 "radius adds output at no extra fuel cost.",
                 "ચાલતી હવામાં ઉપલબ્ધ શક્તિ ગતિના <b>ઘન</b> પ્રમાણમાં હોય: પવન બમણો થાય તો શક્તિ આઠ ગણી, તેથી "
                 "સરેરાશ 7 m/s વાળું સ્થળ 5 m/s વાળા સ્થળ કરતાં બમણાથી ઘણું વધુ ઉત્પાદન આપે. જમીન પાસે પવન ધીમો "
                 "અને અનિયમિત હોય, તેથી હવે ટાવર 100-140 m ઊંચા અને બ્લેડ 60-80 m લાંબા બને: ઘેરાયેલો વિસ્તાર "
                 "વ્યાસના વર્ગ પ્રમાણમાં વધે અને રોટર ત્રિજ્યાનો દરેક વધારાનો મીટર વધારાના ઇંધણ ખર્ચ વગર "
                 "ઉત્પાદન ઉમેરે."),
               H4("The Betz limit", "બેટ્ઝ મર્યાદા"),
               P("A turbine cannot stop the wind completely; if it did, no more air could enter. The "
                 "German physicist Albert Betz showed in 1919 that the best a rotor can do is extract "
                 "16/27, about <b>59.3 %</b>, of the power in the wind. Real machines reach 40-50 % of "
                 "that ideal as a power coefficient Cp, and the best three-bladed designs touch 0.45-0.50, "
                 "which is why a Cp of 0.45 is the normal figure in textbook problems.",
                 "ટર્બાઇન પવનને પૂરો રોકી શકે નહીં; રોકે તો વધુ હવા અંદર આવી ન શકે. જર્મન ભૌતિકશાસ્ત્રી "
                 "આલ્બર્ટ બેટ્ઝે 1919માં દર્શાવ્યું કે રોટર વધુમાં વધુ 16/27, લગભગ <b>59.3 %</b>, શક્તિ ખેંચી "
                 "શકે. વાસ્તવિક મશીન તે આદર્શના 40-50 % સુધી શક્તિ અવયવ Cp તરીકે પહોંચે અને શ્રેષ્ઠ ત્રણ-બ્લેડ "
                 "રચના 0.45-0.50 સ્પર્શે, તેથી પાઠ્યપુસ્તકના દાખલામાં Cp = 0.45 સામાન્ય આંકડો છે."),
               H4("Reading a wind site", "પવન સ્થળ વાંચવું"),
               TB([T("Measure", "માપ"), T("What it tells you", "તે શું કહે")],
                  [[T("mean wind speed at hub height", "હબની ઊંચાઈ પર સરેરાશ પવન ગતિ"), T("first screen; 6 m/s or more is worth developing", "પ્રથમ ગાળણી; 6 m/s કે વધુ વિકાસલાયક")],
                   [T("wind power density, W/m²", "પવન શક્તિ ઘનતા, W/m²"), T("class 1 poor, class 7 excellent", "વર્ગ 1 નબળું, વર્ગ 7 ઉત્તમ")],
                   [T("Weibull shape factor k", "વેઇબુલ આકાર અવયવ k"), T("k near 2 means a steady site; a low k brings violent gusts", "k લગભગ 2 એટલે સ્થિર સ્થળ; નીચો k હિંસક ઝાપટા લાવે")],
                   [T("turbulence intensity", "અશાંતિ તીવ્રતા"), T("high near buildings and forests, shortens gearbox life", "ઇમારત અને જંગલ પાસે વધુ, ગિયરબોક્સનું આયુષ્ય ઘટાડે")],
                   [T("capacity factor", "ક્ષમતા અવયવ"), T("good Indian sites reach 30-38 %", "સારા ભારતીય સ્થળ 30-38 % પામે")]]),
               H4("Worked example", "ઉકેલાયેલ દાખલો"),
               P("A 120 m rotor at 12 m/s in air of 1.225 kg/m³: swept area = π × 60² = 11,310 m², so the "
                 "power in the wind is 0.5 × 1.225 × 11,310 × 12³ = 11.9 MW. At Cp = 0.45 and a drive "
                 "train efficiency of 0.94 the electrical output is 11.9 × 0.45 × 0.94 = 5.05 MW, close "
                 "to the 5 MW rating of the machine.",
                 "1.225 kg/m³ હવામાં 12 m/s પર 120 m રોટર: ઘેરાયેલો વિસ્તાર = π × 60² = 11,310 m², તેથી "
                 "પવનમાં શક્તિ = 0.5 × 1.225 × 11,310 × 12³ = 11.9 MW. Cp = 0.45 અને 0.94 ડ્રાઇવ ટ્રેન "
                 "કાર્યક્ષમતાએ વીજ ઉત્પાદન 11.9 × 0.45 × 0.94 = 5.05 MW, મશીનના 5 MW રેટિંગની નજીક."),
               H4("Common mistake", "સામાન્ય ભૂલ"),
               P("Multiplying the generator rating by 8,760 hours to get annual energy. A 2 MW turbine "
                 "at a 30 % capacity factor makes about 5.3 GWh a year, not 17.5 GWh.",
                 "જનરેટર રેટિંગને 8,760 કલાકથી ગુણીને વાર્ષિક ઊર્જા કાઢવી. 30 % ક્ષમતા અવયવે 2 MW ટર્બાઇન "
                 "વર્ષે લગભગ 5.3 GWh બનાવે, 17.5 GWh નહીં.")],
              "u3_wind", syllabus_item="3.4"),
         card(T("3.4 HAWT and VAWT, the parts of a turbine, and the bladeless idea",
                "3.4 HAWT અને VAWT, ટર્બાઇનના ભાગો અને બ્લેડ વગરની કલ્પના"),
              [H4("Two axes", "બે અક્ષ"),
               P("A <b>horizontal-axis</b> wind turbine (HAWT) has its rotor shaft parallel to the "
                 "ground and the wind, so it must face the wind - a yaw motor turns the nacelle. It "
                 "sweeps a large circle, reaches Cp of 0.45-0.50 and dominates utility-scale wind. A "
                 "<b>vertical-axis</b> turbine (VAWT: Savonius, Darrieus, H-rotor) spins about a "
                 "vertical shaft whatever direction the wind comes from, needs no yaw and puts the "
                 "generator at ground level, but its lower half works in disturbed air and drag, so Cp "
                 "is only 0.15-0.35.",
                 "<b>આડી અક્ષ</b>ની પવન ટર્બાઇન (HAWT)ની રોટર ધરી જમીન અને પવનને સમાંતર હોય, તેથી તેણે પવન "
                 "તરફ મુખ રાખવું પડે - યો મોટર નેસેલ ફેરવે. તે મોટું વર્તુળ ઘેરે, Cp 0.45-0.50 પામે અને "
                 "ઉપયોગિતા-સ્તરના પવન પર રાજ કરે. <b>ઊભી અક્ષ</b>ની ટર્બાઇન (VAWT: સેવોનિયસ, ડેરિયસ, "
                 "H-રોટર) પવન ગમે તે દિશાથી આવે, ઊભી ધરી પર ફરે, યો ન જોઈએ અને જનરેટર જમીન સ્તરે રાખે, પણ "
                 "તેનો નીચેનો અડધો ભાગ ખલેલાયેલી હવામાં અને ડ્રેગમાં કામ કરે, તેથી Cp ફક્ત 0.15-0.35."),
               H4("HAWT against VAWT", "HAWT સામે VAWT"),
               TB([T("Point", "મુદ્દો"), T("HAWT", "HAWT"), T("VAWT", "VAWT")],
                  [[T("axis", "અક્ષ"), T("horizontal, rotor faces the wind", "આડી, રોટર પવન તરફ"), T("vertical, wind from any side", "ઊભી, કોઈ પણ બાજુથી પવન")],
                   [T("efficiency Cp", "કાર્યક્ષમતા Cp"), T("0.45-0.50", "0.45-0.50"), T("0.15-0.35", "0.15-0.35")],
                   [T("size built", "બનેલું માપ"), T("up to 15 MW offshore, 120-260 m rotor", "15 MW સુધી દરિયામાં, 120-260 m રોટર"), T("small, 1-100 kW units", "નાના, 1-100 kW એકમ")],
                   [T("yaw mechanism", "યો પ્રણાલી"), T("needed", "જરૂરી"), T("not needed", "જરૂરી નહીં")],
                   [T("generator position", "જનરેટરનું સ્થાન"), T("on top, in the nacelle", "ઉપર, નેસેલમાં"), T("at ground level", "જમીન સ્તરે")],
                   [T("tower loads", "ટાવર પર ભાર"), T("high bending moment, heavy foundation", "મોટો વળાંક ભાર, ભારે પાયો"), T("lower, lighter foundation", "ઓછો, હલકો પાયો")],
                   [T("noise and birds", "ઘોંઘાટ અને પક્ષી"), T("blade tip noise, bird strike risk", "બ્લેડની ટોચનો ઘોંઘાટ, પક્ષી અથડાવાનું જોખમ"), T("quieter, safer for birds", "શાંત, પક્ષીઓ માટે સુરક્ષિત")],
                   [T("best use", "શ્રેષ્ઠ ઉપયોગ"), T("wind farms, onshore and offshore", "પવન ફાર્મ, જમીન પર અને દરિયામાં"), T("rooftops, streets, pumping, remote sites", "છત, શેરી, પાણી ઉપાડ, દૂરનાં સ્થળ")]]),
               H4("Parts of a HAWT", "HAWTના ભાગો"),
               OL(("The <b>blades</b> - usually three, aerofoil shaped like an aircraft wing - catch the "
                   "wind and turn it into torque; pitch motors twist them to control power.", "<b>બ્લેડ</b> - સામાન્ય રીતે ત્રણ, વિમાનના પાંખ જેવા - પવન પકડીને ટોર્ક બનાવે; પિચ મોટર તેમને વાળીને શક્તિ નિયંત્રિત કરે."),
                  ("The <b>hub</b> joins the blades to the low-speed shaft inside the <b>nacelle</b>.", "<b>હબ</b> બ્લેડને <b>નેસેલ</b>માંની ધીમી ધરી સાથે જોડે."),
                  ("A <b>gearbox</b> raises the 10-20 rpm of the rotor to about 1,500 rpm for the "
                   "generator; direct-drive machines use a large slow multi-pole generator instead.", "<b>ગિયરબોક્સ</b> રોટરના 10-20 rpmને જનરેટર માટે લગભગ 1,500 rpm કરે; ડાયરેક્ટ-ડ્રાઇવ મશીન તેના બદલે મોટું ધીમું બહુ-ધ્રુવ જનરેટર વાપરે."),
                  ("A <b>yaw drive</b> keeps the rotor facing the wind; <b>anemometer and wind vane</b> "
                   "on the nacelle tell the controller what to do.", "<b>યો ડ્રાઇવ</b> રોટરને પવન તરફ રાખે; નેસેલ પરના <b>એનિમોમીટર અને પવન દિશા</b> નિયંત્રકને શું કરવું તે કહે."),
                  ("The <b>tower</b> carries everything to hub height and the <b>foundation</b> holds it "
                   "against overturning; a <b>transformer</b> at the base steps the voltage up.", "<b>ટાવર</b> બધું હબની ઊંચાઈ સુધી લઈ જાય અને <b>પાયો</b> ઊલટવાથી રક્ષે; પાયા પાસેનું <b>ટ્રાન્સફોર્મર</b> વોલ્ટેજ વધારે.")),
               H4("Bladeless wind turbines", "બ્લેડ વગરની પવન ટર્બાઇન"),
               P("A bladeless machine, such as the vortex or the Spanish Vortex Bladeless design, is a "
                 "tapered mast that <b>vibrates</b> when wind sheds vortices behind it - vortex-induced "
                 "vibration, the same effect that once destroyed the Tacoma bridge. Magnets and coils at "
                 "the base turn that sway into electricity. Advantages: no blades, no gearbox, fewer "
                 "moving parts, very quiet, safe for birds, low maintenance and cheap to make. "
                 "Drawbacks: efficiency is only a few per cent of the Betz limit, the output is small "
                 "(a few hundred watts to a few kW), it needs a steady wind and resonance tuning, and "
                 "it cannot yet compete for grid-scale power.",
                 "બ્લેડ વગરનું મશીન, જેમ કે વોર્ટેક્સ કે સ્પેનિશ Vortex Bladeless રચના, એ પાતળું થતું થાંભલું "
                 "છે જે પવન તેની પાછળ વમળ છોડે ત્યારે <b>કંપે</b> - વમળ-જનિત કંપન, જે અસરથી એક સમયે ટેકોમા "
                 "પુલ તૂટ્યો હતો. પાયા પાસેના ચુંબક અને કોઇલ તે ડોલનને વીજળીમાં ફેરવે. લાભ: બ્લેડ નહીં, "
                 "ગિયરબોક્સ નહીં, ઓછા ફરતા ભાગ, ખૂબ શાંત, પક્ષીઓ માટે સુરક્ષિત, ઓછી જાળવણી અને સસ્તું બનાવવું. "
                 "ખામી: કાર્યક્ષમતા બેટ્ઝ મર્યાદાના ફક્ત થોડા ટકા, ઉત્પાદન નાનું (થોડા સો વોટથી થોડા kW), "
                 "સ્થિર પવન અને અનુનાદ ગોઠવણ જોઈએ, અને ગ્રિડ-સ્તરની શક્તિ માટે હજી ટક્કર ન કરી શકે.")],
              syllabus_item="3.4"),
     ]},
    {"title": T("4. Bioenergy", "4. બાયોએનર્જી"),
     "items": [
         card(T("3.5 Biofuels: ethanol and biodiesel", "3.5 જૈવઇંધણ: ઇથેનોલ અને બાયોડીઝલ"),
              [H4("What a biofuel is", "જૈવઇંધણ શું છે"),
               P("A <b>biofuel</b> is a liquid or gas fuel made from recently living matter - plants, "
                 "crop residues, animal dung or algae. The carbon it releases when burnt was taken out "
                 "of the air by the plant while it grew, so in principle the cycle is close to carbon "
                 "neutral. In practice the balance depends on the crop, the fertiliser, the transport "
                 "and whether land or food was displaced, which is why the subject is taught with a "
                 "<b>life-cycle</b> view rather than a single sum.",
                 "<b>જૈવઇંધણ</b> એ તાજેતરમાં જીવતા દ્રવ્યમાંથી બનેલું પ્રવાહી કે વાયુ ઇંધણ છે - છોડ, પાકનો "
                 "અવશેષ, પશુનું છાણ કે શેવાળ. બળે ત્યારે છૂટતો કાર્બન છોડે ઉગતી વખતે હવામાંથી લીધેલો હોય, તેથી "
                 "સિદ્ધાંતમાં ચક્ર લગભગ કાર્બન-તટસ્થ છે. વ્યવહારમાં સંતુલન પાક, ખાતર, વહન અને જમીન કે ખોરાક "
                 "વિસ્થાપિત થયો કે નહીં તેના પર આધારિત છે, તેથી આ વિષય એક જ સરવાળાને બદલે <b>જીવનચક્ર</b>ની "
                 "દૃષ્ટિએ ભણાવાય."),
               H4("Ethanol", "ઇથેનોલ"),
               P("<b>Ethanol</b> (C₂H₅OH) is made by fermenting sugar with yeast and then distilling it "
                 "to 99.5 % purity. Sugar cane juice and molasses are the Indian feedstock; maize, wheat "
                 "and rice straw are used elsewhere, and second-generation plants use crop residue or "
                 "wood after breaking the cellulose down. In India it is blended with petrol - E10 "
                 "means 10 % ethanol by volume - because it raises the octane number and cuts both "
                 "imported oil and CO. Its energy content is about two thirds that of petrol, so a "
                 "20 % blend raises fuel use by roughly 5-7 %.",
                 "<b>ઇથેનોલ</b> (C₂H₅OH) ખમીર સાથે ખાંડને આથો લાવીને અને પછી 99.5 % શુદ્ધતા સુધી નિસ્યંદન "
                 "કરીને બને. શેરડીનો રસ અને ગોળ ભારતીય કાચો માલ છે; મકાઈ, ઘઉં અને ડાંગરનું પરાળ બીજે વપરાય "
                 "અને દ્વિતીય પેઢીના સ્ટેશન સેલ્યુલોઝ તોડીને પાકના અવશેષ કે લાકડું વાપરે. ભારતમાં તે પેટ્રોલમાં "
                 "ભળે - E10 એટલે કદ પ્રમાણે 10 % ઇથેનોલ - કારણ કે તે ઓક્ટેન વધારે અને આયાત તેલ તથા CO બંને "
                 "ઘટાડે. તેની ઊર્જા પેટ્રોલના લગભગ બે તૃતીયાંશ હોય, તેથી 20 % મિશ્રણ ઇંધણનો વપરાશ લગભગ "
                 "5-7 % વધારે."),
               H4("Biodiesel and transesterification", "બાયોડીઝલ અને ટ્રાન્સએસ્ટરીફિકેશન"),
               P("Vegetable oil is too thick to burn cleanly in a diesel engine, so it is reacted with "
                 "methanol and a catalyst (sodium hydroxide) to make <b>fatty acid methyl esters</b> - "
                 "biodiesel - and glycerol as a by-product. One hundred kilograms of oil with about "
                 "twenty kilograms of methanol gives roughly one hundred kilograms of biodiesel and ten "
                 "kilograms of glycerol. Feedstocks include used cooking oil, jatropha and karanja seed, "
                 "palm and cotton-seed oil. Biodiesel has a high cetane number, almost no sulphur and "
                 "good lubricity, but it gels in cold weather and is slightly more expensive.",
                 "વનસ્પતિ તેલ ડીઝલ એન્જિનમાં સ્વચ્છ બળવા પૂરતું ગાઢ છે, તેથી તેને મિથેનોલ અને ઉત્પ્રેરક (સોડિયમ "
                 "હાઇડ્રોક્સાઇડ) સાથે પ્રક્રિયા કરાવીને <b>ફેટી એસિડ મિથાઇલ એસ્ટર</b> - બાયોડીઝલ - અને "
                 "ઉપપેદાશ તરીકે ગ્લિસરોલ બને. લગભગ વીસ કિલો મિથેનોલ સાથે એકસો કિલો તેલ લગભગ એકસો કિલો "
                 "બાયોડીઝલ અને દસ કિલો ગ્લિસરોલ આપે. કાચા માલમાં વપરાયેલું રાંધણ તેલ, જટ્રોફા અને કરંજના બી, "
                 "તાડ અને કપાસિયાનું તેલ આવે. બાયોડીઝલનો સિટેન આંકડો ઊંચો, સલ્ફર લગભગ નહીં અને લ્યુબ્રિકેશન "
                 "સારું, પણ ઠંડામાં થરથરે અને થોડું મોંઘું પડે."),
               H4("The three generations", "ત્રણ પેઢીઓ"),
               TB([T("Generation", "પેઢી"), T("Feedstock", "કાચો માલ"), T("Examples", "ઉદાહરણ"), T("Criticism", "ટીકા")],
                  [[T("first", "પ્રથમ"), T("food crops", "ખાદ્ય પાક"), T("sugarcane ethanol, soya and palm biodiesel", "શેરડીનો ઇથેનોલ, સોયા અને તાડનું બાયોડીઝલ"), T("competes with food and land, indirect land-use change", "ખોરાક અને જમીન સાથે સ્પર્ધા, પરોક્ષ જમીન ઉપયોગ ફેરફાર")],
                   [T("second", "દ્વિતીય"), T("residue and waste", "અવશેષ અને કચરો"), T("rice straw, bagasse, used cooking oil, wood chips", "પરાળ, શેરડીની ચીપ, વપરાયેલ રાંધણ તેલ, લાકડાની ચીપ"), T("collection and pre-treatment cost", "એકઠું કરવા અને પૂર્વ-સારવારનો ખર્ચ")],
                   [T("third", "તૃતીય"), T("algae and microbes", "શેવાળ અને સૂક્ષ્મજીવ"), T("algal oil, engineered cyanobacteria", "શેવાળનું તેલ, બનાવેલા સાયનોબેક્ટેરિયા"), T("still costly, needs water, light and CO₂", "હજી મોંઘું, પાણી, પ્રકાશ અને CO₂ જોઈએ")]]),
               H4("Common mistake", "સામાન્ય ભૂલ"),
               P("Calling every biofuel carbon neutral. Growing the crop, making the fertiliser, "
                 "distilling the ethanol and transporting it all emit CO₂; Indian molasses ethanol "
                 "typically saves 50-70 % against petrol, not 100 %.",
                 "દરેક જૈવઇંધણને કાર્બન-તટસ્થ કહેવું. પાક ઉગાડવો, ખાતર બનાવવું, ઇથેનોલનું નિસ્યંદન અને વહન "
                 "બધું CO₂ છોડે; ભારતીય ગોળનો ઇથેનોલ સામાન્ય રીતે પેટ્રોલ સામે 50-70 % બચાવે, 100 % નહીં.")],
              syllabus_item="3.5"),
         card(T("3.5 Biomass forms, biogas, gasification and algae",
                "3.5 બાયોમાસના સ્વરૂપ, બાયોગેસ, ગેસિફિકેશન અને શેવાળ"),
              [H4("Three forms of biomass", "બાયોમાસનાં ત્રણ સ્વરૂપ"),
               TB([T("Form", "સ્વરૂપ"), T("Examples", "ઉદાહરણ"), T("How it is used", "કેવી રીતે વપરાય")],
                  [[T("solid", "ઘન"), T("firewood, bagasse, rice husk, sawdust, briquettes", "લાકડું, ચીપ, ભૂસું, લાકડાની ધૂળ, બ્રિકેટ"), T("direct combustion for heat and steam", "ઉષ્મા અને વરાળ માટે સીધું દહન")],
                   [T("liquid", "પ્રવાહી"), T("ethanol, biodiesel, pyrolysis oil", "ઇથેનોલ, બાયોડીઝલ, પાયરોલિસિસ તેલ"), T("blended into petrol and diesel, or burnt in engines", "પેટ્રોલ-ડીઝલમાં મિશ્રણ, કે એન્જિનમાં દહન")],
                   [T("gaseous", "વાયુ"), T("biogas, producer gas, hydrogen from biomass", "બાયોગેસ, પ્રોડ્યુસર ગેસ, બાયોમાસમાંથી હાઇડ્રોજન"), T("cooking, engine fuel, electricity", "રાંધણ, એન્જિન ઇંધણ, વીજળી")]]),
               H4("Biogas and the anaerobic digester", "બાયોગેસ અને અવાયુજીવી પાચક"),
               P("In a sealed <b>digester</b> with no oxygen, bacteria break dung and plant waste into "
                 "<b>biogas</b> - about 55-65 % methane and 30-40 % carbon dioxide, with traces of "
                 "hydrogen sulphide - and a nutrient-rich <b>digestate</b> that is a better fertiliser "
                 "than raw dung. A family-size plant of 2 m³ a day needs about 50 kg of dung and gives "
                 "enough gas for a family of six to cook twice a day. The methane is the same gas as "
                 "in natural gas, so it can run an engine or a generator; trapping it also stops a "
                 "gas twenty-eight times stronger than CO₂ from escaping into the air.",
                 "ઓક્સિજન વગરના બંધ <b>પાચક</b>માં બેક્ટેરિયા છાણ અને છોડનો કચરો <b>બાયોગેસ</b>માં તોડે - લગભગ "
                 "55-65 % મિથેન અને 30-40 % કાર્બન ડાયોક્સાઇડ, થોડું હાઇડ્રોજન સલ્ફાઇડ સાથે - અને પોષકતત્ત્વોથી "
                 "ભરપૂર <b>પાચિત ખાતર</b> આપે જે કાચા છાણ કરતાં સારું છે. દિવસે 2 m³નું કુટુંબ-કદનું સ્ટેશન "
                 "લગભગ 50 કિલો છાણ માંગે અને છ વ્યક્તિના કુટુંબને દિવસમાં બે વાર રાંધવા પૂરતો ગેસ આપે. તે "
                 "મિથેન કુદરતી ગેસનો જ વાયુ છે, તેથી એન્જિન કે જનરેટર ચલાવે; તેને પકડવાથી CO₂ કરતાં અઠ્ઠાવીસ ગણો "
                 "શક્તિશાળી વાયુ હવામાં જતો પણ અટકે."),
               H4("Gasification", "ગેસિફિકેશન"),
               P("<b>Gasification</b> is not burning. Biomass is heated to 700-900 °C with a strictly "
                 "limited supply of air, so it does not flame but converts into a combustible "
                 "<b>producer gas</b> of carbon monoxide, hydrogen, methane and nitrogen. That gas "
                 "burns in a engine or a furnace far more cleanly than raw wood, gives a controllable "
                 "flame and leaves a char that can go back to the field. The heat needed comes from "
                 "partial combustion of the biomass itself.",
                 "<b>ગેસિફિકેશન</b> દહન નથી. બાયોમાસને ખૂબ મર્યાદિત હવા સાથે 700-900 °C સુધી ગરમ કરાય, તેથી તે "
                 "જ્યોત પકડતું નથી પણ કાર્બન મોનોક્સાઇડ, હાઇડ્રોજન, મિથેન અને નાઇટ્રોજનના બળતા <b>પ્રોડ્યુસર ગેસ</b>માં "
                 "ફેરવાય. તે ગેસ કાચા લાકડા કરતાં ઘણો સ્વચ્છ બળે, નિયંત્રિત જ્યોત આપે અને બળેલો કોલસો ખેતરમાં "
                 "પાછો જાય. જરૂરી ઉષ્મા બાયોમાસના આંશિક દહનમાંથી આવે."),
               H4("Algae biofuels", "શેવાળ જૈવઇંધણ"),
               P("Microalgae grow in ponds or tubes, use sunlight and CO₂, and can double their mass in "
                 "a day; some strains store 20-50 % of their dry weight as oil. They need no farmland, "
                 "can be grown on saline water beside a power plant and eat its flue gas. The catch is "
                 "harvesting and dewatering, which use more energy than the oil returns, so algal fuel "
                 "is still three to five times the price of diesel and is a research subject rather "
                 "than a commercial one.",
                 "સૂક્ષ્મ શેવાળ તળાવ કે નળીમાં ઊગે, સૂર્યપ્રકાશ અને CO₂ વાપરે અને એક દિવસમાં તેનું દળ બમણું કરી "
                 "શકે; કેટલાક પ્રકાર સૂકા વજનના 20-50 % તેલ તરીકે સંગ્રહે. તેમને ખેતીની જમીન ન જોઈએ, ખારા પાણીમાં "
                 "વીજ સ્ટેશન પાસે ઊગી તેનો ધુમાડો ખાઈ શકે. મુશ્કેલી એ છે કે વીણવું અને પાણી દૂર કરવું એ તેલ "
                 "પાછું આપે તેનાથી વધુ ઊર્જા વાપરે, તેથી શેવાળનું ઇંધણ હજી ડીઝલ કરતાં ત્રણથી પાંચ ગણું મોંઘું "
                 "છે અને વ્યાવસાયિક નહીં, સંશોધનનો વિષય છે."),
               H4("Worked example", "ઉકેલાયેલ દાખલો"),
               P("A 25 m³ village digester fed 500 kg of dung a day at 0.04 m³ of gas per kg yields 20 m³ "
                 "a day. At 6 kWh of heat per m³ that is 120 kWh, enough for about eight households, and "
                 "the digestate fertilises half a hectare.",
                 "દિવસે 500 કિલો છાણ ખાતર 25 m³નું ગામનું પાચક, પ્રતિ કિલો 0.04 m³ ગેસ પ્રમાણે દિવસે 20 m³ "
                 "આપે. પ્રતિ m³ 6 kWh ઉષ્મા પ્રમાણે તે 120 kWh, લગભગ આઠ ઘર માટે પૂરતું, અને પાચિત ખાતર અડધો "
                 "હેક્ટર ખેતરને ફળદ્રૂપ કરે.")],
              "u3_bio", syllabus_item="3.5"),
     ]},
    {"title": T("5. New Energy Sources", "5. નવા ઊર્જા સ્રોત"),
     "items": [
         card(T("3.6 Geothermal energy", "3.6 ભૂતાપીય ઊર્જા"),
              [H4("Where the heat comes from", "ઉષ્મા ક્યાંથી આવે"),
               P("The earth's core is about 5,000 °C and heat flows outward continuously from the "
                 "decay of radioactive isotopes and from the original formation of the planet. The "
                 "average gradient is 25-30 °C per kilometre, so a 3 km well reaches 80-100 °C even "
                 "away from volcanoes. Where the crust is thin - faults, hot springs, volcanic belts - "
                 "the heat is concentrated enough to make steam or hot water at the surface. Unlike "
                 "solar and wind, a geothermal plant runs day and night, which gives it a capacity "
                 "factor of 70-90 %.",
                 "પૃથ્વીનો ગર્ભ લગભગ 5,000 °C છે અને કિરણોત્સર્ગી સમસ્થાનિકોના ક્ષય તથા ગ્રહની રચના વખતની "
                 "ઉષ્મામાંથી સતત બહાર વહે છે. સરેરાશ ઢાળ પ્રતિ કિલોમીટર 25-30 °C છે, તેથી જ્વાળામુખીથી દૂર પણ "
                 "3 કિમીની કૂવો 80-100 °C પામે. જ્યાં પોપડો પાતળો હોય - ભ્રંશ, ગરમ ઝરણાં, જ્વાળામુખી પટ્ટા - "
                 "ત્યાં ઉષ્મા એટલી કેન્દ્રિત થાય કે સપાટી પર વરાળ કે ગરમ પાણી મળે. સૌર અને પવનથી વિપરીત "
                 "ભૂતાપીય સ્ટેશન દિવસ-રાત ચાલે, તેથી તેનો ક્ષમતા અવયવ 70-90 % થાય."),
               H4("Three ways to use it", "વાપરવાની ત્રણ રીત"),
               TB([T("Plant", "સ્ટેશન"), T("How it works", "કેવી રીતે ચાલે"), T("Best for", "કોના માટે શ્રેષ્ઠ")],
                  [[T("dry steam", "સૂકી વરાળ"), T("steam straight from the well spins the turbine", "કૂવાની વરાળ સીધી ટર્બાઇન ફેરવે"), T("very hot fields, above 240 °C", "ખૂબ ગરમ ક્ષેત્ર, 240 °Cથી ઉપર")],
                   [T("flash steam", "ફ્લેશ વરાળ"), T("hot water at 180-240 °C is allowed to boil in a low-pressure tank", "180-240 °Cનું ગરમ પાણી નીચા દબાણની ટાંકીમાં ઉકળવા દેવાય"), T("most fields", "મોટા ભાગનાં ક્ષેત્ર")],
                   [T("binary cycle", "દ્વિચક્ર"), T("brine at 100-180 °C heats a second fluid with a low boiling point, which spins the turbine", "100-180 °Cનું ખારું પાણી નીચા ઉકળાંકવાળો બીજો પ્રવાહી ગરમ કરે, જે ટર્બાઇન ફેરવે"), T("medium heat, no emissions to air", "મધ્યમ ઉષ્મા, હવામાં ઉત્સર્જન નહીં")]]),
               H4("Uses beyond electricity", "વીજળી ઉપરાંતના ઉપયોગ"),
               UL(("direct heating of buildings and greenhouses through district heating networks", "જિલ્લા ગરમી નેટવર્ક દ્વારા ઇમારત અને કાચઘરની સીધી ગરમી"),
                  ("<b>ground source heat pumps</b>: a shallow loop at 15-20 °C heats a building with a "
                   "coefficient of performance of 3-4, so 1 kWh of electricity moves 3-4 kWh of heat", "<b>જમીન સ્રોત ઉષ્મા પંપ</b>: 15-20 °Cનો છીછરો લૂપ 3-4ના કાર્યદક્ષતા ગુણોત્તરે ઇમારત ગરમ કરે, તેથી 1 kWh વીજળી 3-4 kWh ઉષ્મા ખસેડે"),
                  ("hot water for fish farming, drying and industrial processes", "માછલી ઉછેર, સૂકવણી અને ઉદ્યોગની પ્રક્રિયા માટે ગરમ પાણી"),
                  ("India's potential is modest but real in the Puga valley of Ladakh and parts of "
                   "the Deccan, and is used mainly for heating", "ભારતની ક્ષમતા મર્યાદિત પણ લદ્દાખના પુગા ખીણ અને દક્કનના કેટલાક ભાગમાં વાસ્તવિક છે અને મુખ્યત્વે ગરમી માટે વપરાય")),
               H4("Problems", "સમસ્યાઓ"),
               P("Drilling is expensive and a dry well loses the whole investment; the brine carries "
                 "hydrogen sulphide and dissolved salts that corrode pipes; and over-extraction can "
                 "cool the field or cause subsidence, so the spent brine is injected back. In some "
                 "fields the extracted water brings up naturally occurring arsenic or boron.",
                 "ડ્રિલિંગ મોંઘું છે અને સૂકો કૂવો આખું રોકાણ ગુમાવે; ખારા પાણીમાં હાઇડ્રોજન સલ્ફાઇડ અને ઓગળેલા "
                 "ક્ષાર પાઇપમાં કાટ લગાડે; અને વધુ પડતું નિષ્કર્ષણ ક્ષેત્ર ઠંડું કરે કે જમીન ધસી જાય, તેથી વપરાયેલું "
                 "ખારું પાણી પાછું દબાવાય. કેટલાંક ક્ષેત્રોમાં કાઢેલા પાણી સાથે કુદરતી આર્સેનિક કે બોરોન પણ આવે.")],
              "u3_new", syllabus_item="3.6"),
         card(T("3.6 Ocean energy: tidal, wave and thermal",
                "3.6 મહાસાગર ઊર્જા: ભરતી, તરંગ અને ઉષ્મા"),
              [H4("Three different resources", "ત્રણ જુદાં સંસાધન"),
               P("The ocean holds energy in three forms that must not be confused. <b>Tides</b> are the "
                 "slow rise and fall caused by the gravity of the moon and the sun, so tidal power is "
                 "as predictable as the calendar. <b>Waves</b> are wind-driven surface motion, "
                 "strongest in stormy high latitudes. <b>Ocean thermal energy</b> is the temperature "
                 "difference between warm surface water and cold deep water in the tropics, which can "
                 "run a heat engine day and night.",
                 "મહાસાગરમાં ઊર્જા ત્રણ સ્વરૂપે છે જે ભેગાં ન કરવાં. <b>ભરતી</b> ચંદ્ર અને સૂર્યના ગુરુત્વાકર્ષણથી "
                 "ધીમે ચઢ-ઊતર છે, તેથી ભરતી ઊર્જા કેલેન્ડર જેટલી અનુમાનિત છે. <b>તરંગો</b> પવનથી ચાલતી સપાટીની "
                 "હિલચાલ છે, જે તોફાની ઊંચા અક્ષાંશોમાં સૌથી તાકાતવાન હોય. <b>મહાસાગર ઉષ્મા ઊર્જા</b> ઉષ્ણકટિબંધમાં "
                 "ગરમ સપાટીના પાણી અને ઠંડા ઊંડા પાણી વચ્ચેનો તાપમાન તફાવત છે, જે દિવસ-રાત ઉષ્મા એન્જિન ચલાવી શકે."),
               H4("Tidal energy conversion", "ભરતી ઊર્જા રૂપાંતરણ"),
               P("The classic scheme is a <b>barrage</b>: a dam across an estuary with sluice gates and "
                 "turbines. Water fills the basin through the gates at high tide, and when the sea "
                 "falls it is released through the turbines. The energy in one filling is proportional "
                 "to the basin area and to the <b>square</b> of the tidal range, so doubling the range "
                 "quadruples the energy; a site needs at least 5 m of range to be worth building. "
                 "Modern alternatives are <b>tidal stream</b> turbines, which look like wind turbines "
                 "under water and need no dam, and <b>tidal lagoons</b> with a closed wall.",
                 "પરંપરાગત રચના <b>બેરેજ</b> છે: જળમાર્ગ પર દરવાજા અને ટર્બાઇન સાથેનો બંધ. ઊંચી ભરતી વખતે પાણી "
                 "દરવાજામાંથી તળાવ ભરે અને દરિયો ઊતરે ત્યારે ટર્બાઇનમાંથી છોડાય. એક ભરણની ઊર્જા તળાવના વિસ્તારના "
                 "પ્રમાણમાં અને ભરતીના ઊંચાઈ તફાવતના <b>વર્ગ</b> પ્રમાણમાં હોય, તેથી તફાવત બમણો થાય તો ઊર્જા ચાર "
                 "ગણી; બાંધવા લાયક સ્થળે ઓછામાં ઓછો 5 m તફાવત જોઈએ. હવેની રીતો <b>ભરતી પ્રવાહ</b> ટર્બાઇન છે, જે "
                 "પાણી નીચે પવન ટર્બાઇન જેવા દેખાય અને બંધ માંગતા નથી, તથા બંધ દીવાલવાળા <b>ભરતી તળાવો</b>."),
               H4("Wave and OTEC", "તરંગ અને OTEC"),
               P("<b>Wave energy</b> converters are of three kinds: an <b>oscillating water column</b>, "
                 "where the wave compresses air that drives a Wells turbine; a <b>point absorber</b>, a "
                 "floating buoy that pumps hydraulic fluid; and an <b>overtopping device</b> that fills "
                 "a reservoir above sea level. <b>OTEC</b> needs a 20 °C difference, found where surface "
                 "water is at 25-28 °C and water 1,000 m down is at 4 °C; a closed cycle evaporates "
                 "ammonia, spins a turbine on the vapour and condenses it in cold deep water. It yields "
                 "electricity, fresh water and cold water for air conditioning at the same time.",
                 "<b>તરંગ ઊર્જા</b> રૂપાંતરક ત્રણ પ્રકારના હોય: <b>ડોલતો પાણી સ્તંભ</b>, જ્યાં તરંગ હવા દબાવે અને "
                 "તે વેલ્સ ટર્બાઇન ચલાવે; <b>બિંદુ શોષક</b>, તરતો બોયો જે હાઇડ્રોલિક પ્રવાહી દબાવે; અને "
                 "<b>ઓવરટોપિંગ</b> સાધન જે સમુદ્ર સપાટીથી ઊંચી ટાંકી ભરે. <b>OTEC</b>ને 20 °C તફાવત જોઈએ, જે "
                 "ત્યાં મળે જ્યાં સપાટીનું પાણી 25-28 °C અને 1,000 m નીચેનું 4 °C હોય; બંધ ચક્રમાં એમોનિયા બાષ્પિત "
                 "થાય, વરાળ ટર્બાઇન ફેરવે અને ઠંડા ઊંડા પાણીમાં ઘનીભવે. તે સાથે વીજળી, મીઠું પાણી અને "
                 "વાતાનુકૂલન માટે ઠંડું પાણી આપે."),
               H4("Why it is small so far", "હજી નાનું કેમ"),
               P("Sea water is corrosive, storm waves destroy structures, the best sites are far from "
                 "the grid, and every device must be built to survive a fifty-year storm. Tidal range "
                 "is limited to a few estuaries and barrages alter the ecosystem of the very estuary "
                 "they use. India's identified potential is about 8,000 MW of tidal and much more of "
                 "wave and thermal, but only small demonstration units exist in the Gulf of Kutch and "
                 "the Gulf of Khambhat.",
                 "દરિયાનું પાણી કાટ લગાડે, તોફાની તરંગો રચનાઓ તોડે, શ્રેષ્ઠ સ્થળો ગ્રિડથી દૂર છે અને દરેક સાધન "
                 "પચાસ વર્ષના તોફાન સામે ટકે તેમ બાંધવું પડે. ભરતીનો તફાવત થોડાક જ જળમાર્ગો પૂરતો છે અને બેરેજ "
                 "જે જળમાર્ગ વાપરે તેની પારિસ્થિતિકી બદલી નાખે. ભારતની ઓળખાયેલી ક્ષમતા લગભગ 8,000 MW ભરતીની "
                 "અને તરંગ તથા ઉષ્માની વધુ છે, પણ કચ્છના અખાત અને ખંભાતના અખાતમાં ફક્ત નાના પ્રદર્શન એકમ છે.")],
              syllabus_item="3.6"),
         card(T("3.6 Hydrogen energy", "3.6 હાઇડ્રોજન ઊર્જા"),
              [H4("An energy carrier, not a source", "ઊર્જા વાહક, સ્રોત નહીં"),
               P("Hydrogen does not exist free in nature; it must be made, so it stores and carries "
                 "energy rather than producing it. That is why it is called an <b>energy carrier</b>. "
                 "One kilogram carries 33.3 kWh of heat, about three times petrol by mass, and burning "
                 "it gives only water vapour. It is stored as a compressed gas at 350-700 bar, as a "
                 "liquid at −253 °C, or inside metal hydrides and liquid organic carriers.",
                 "હાઇડ્રોજન કુદરતમાં મુક્ત મળતું નથી; તેને બનાવવું પડે, તેથી તે ઊર્જા બનાવવાને બદલે સંગ્રહે અને "
                 "વહન કરે. તેથી તેને <b>ઊર્જા વાહક</b> કહે છે. એક કિલોગ્રામ 33.3 kWh ઉષ્મા ધરે, દળ પ્રમાણે પેટ્રોલ "
                 "કરતાં લગભગ ત્રણ ગણું, અને બળે ત્યારે ફક્ત પાણીની વરાળ આપે. તે 350-700 bar પર દબાયેલા વાયુ "
                 "તરીકે, −253 °C પર પ્રવાહી તરીકે, કે ધાતુ હાઇડ્રાઇડ અને પ્રવાહી કાર્બનિક વાહકમાં સંગ્રહાય."),
               H4("The colour code", "રંગ સંકેત"),
               TB([T("Name", "નામ"), T("Made from", "કઈ રીતે બને"), T("CO₂", "CO₂")],
                  [[T("grey", "ભૂખરું"), T("steam reforming of natural gas", "કુદરતી ગેસનું વરાળ સુધારણ"), T("about 10 kg per kg of H₂", "પ્રતિ કિલો H₂ લગભગ 10 કિલો")],
                   [T("blue", "વાદળી"), T("the same, with carbon capture and storage", "તે જ, કાર્બન પકડ અને સંગ્રહ સાથે"), T("1-2 kg, not zero", "1-2 કિલો, શૂન્ય નહીં")],
                   [T("green", "લીલું"), T("electrolysis of water using renewable electricity", "પુનઃપ્રાપ્ય વીજળીથી પાણીનું વિદ્યુતવિભાજન"), T("almost none", "લગભગ નહીં")],
                   [T("turquoise", "ફિરોઝી"), T("methane pyrolysis, solid carbon as the by-product", "મિથેન પાયરોલિસિસ, ઉપપેદાશ ઘન કાર્બન"), T("none, carbon is captured solid", "નહીં, કાર્બન ઘન સ્વરૂપે પકડાય")]]),
               H4("Electrolysis and the fuel cell", "વિદ્યુતવિભાજન અને ઇંધણ કોષ"),
               P("An <b>electrolyser</b> passes a direct current through water between two electrodes "
                 "and splits it into hydrogen at the cathode and oxygen at the anode; alkaline, PEM and "
                 "solid oxide are the three technologies. Modern stacks need 50-55 kWh of electricity "
                 "per kilogram of hydrogen, which is about 70-75 % efficiency on the higher heating "
                 "value. A <b>fuel cell</b> reverses the process: hydrogen enters the anode, is split "
                 "into protons and electrons, the protons cross a membrane and the electrons drive the "
                 "load, and the only exhaust is water. A PEM fuel cell reaches 50-60 % efficiency, and "
                 "80 % if the waste heat is used.",
                 "<b>વિદ્યુતવિભાજક</b> બે ઇલેક્ટ્રોડ વચ્ચે પાણીમાં એકમાર્ગી પ્રવાહ પસાર કરીને કેથોડ પર હાઇડ્રોજન "
                 "અને એનોડ પર ઓક્સિજન અલગ કરે; આલ્કલાઇન, PEM અને ઘન ઓક્સાઇડ ત્રણ ટેક્નોલોજી છે. આધુનિક સ્ટેકને "
                 "પ્રતિ કિલો હાઇડ્રોજન 50-55 kWh વીજળી જોઈએ, જે ઊંચા ઉષ્મા મૂલ્ય પર લગભગ 70-75 % કાર્યક્ષમતા છે. "
                 "<b>ઇંધણ કોષ</b> પ્રક્રિયા ઊલટાવે: હાઇડ્રોજન એનોડમાં આવે, પ્રોટોન અને ઇલેક્ટ્રોનમાં વિભાજે, "
                 "પ્રોટોન પડદો ઓળંગે અને ઇલેક્ટ્રોન ભાર ચલાવે, અને એકમાત્ર નિકાસ પાણી છે. PEM ઇંધણ કોષ 50-60 % "
                 "કાર્યક્ષમતા પામે, અને કચરાની ઉષ્મા વાપરો તો 80 %."),
               H4("Where it will be used first", "પહેલાં ક્યાં વપરાશે"),
               UL(("steel and fertiliser plants that today use grey hydrogen from gas", "પોલાદ અને ખાતર કારખાનાં જે આજે ગેસમાંથી ભૂખરું હાઇડ્રોજન વાપરે"),
                  ("long-distance trucks, buses and trains where batteries are too heavy", "લાંબા અંતરના ટ્રક, બસ અને ટ્રેન જ્યાં બેટરી ખૂબ ભારે પડે"),
                  ("seasonal storage: hydrogen made in summer sunshine and burnt in winter", "મોસમી સંગ્રહ: ઉનાળાના તડકામાં બનેલું હાઇડ્રોજન શિયાળામાં બળે"),
                  ("shipping and aviation through ammonia and synthetic fuels", "એમોનિયા અને કૃત્રિમ ઇંધણ દ્વારા જહાજવાહન અને વિમાનવાહન")),
               H4("The honest limits", "પ્રામાણિક મર્યાદા"),
               P("Round-trip efficiency is poor: 50 kWh of green electricity becomes 1 kg of hydrogen "
                 "carrying 33 kWh, and a fuel cell gives back only about 17 kWh at the wheels, against "
                 "45 kWh for a battery. Hydrogen also leaks easily, embrittles steel and is explosive "
                 "between 4 and 75 % in air. It makes sense where direct electrification is impossible, "
                 "not as a general replacement for the grid.",
                 "આવ-જાવ કાર્યક્ષમતા નબળી છે: 50 kWh લીલી વીજળી 33 kWh ધરતું 1 કિલો હાઇડ્રોજન બને અને ઇંધણ "
                 "કોષ પૈડાં પર ફક્ત લગભગ 17 kWh પાછું આપે, જ્યારે બેટરી 45 kWh આપે. હાઇડ્રોજન સહેલાઈથી લીક થાય, "
                 "પોલાદને ભુરભુરું કરે અને હવામાં 4-75 % વચ્ચે વિસ્ફોટક છે. જ્યાં સીધું વીજીકરણ અશક્ય હોય ત્યાં "
                 "તે અર્થપૂર્ણ છે, ગ્રિડના સામાન્ય વિકલ્પ તરીકે નહીં.")],
              syllabus_item="3.6"),
     ]},
]

NUMERICALS = [
    num("u3n01", T("Power in the wind and what the turbine keeps.",
                   "પવનમાંની શક્તિ અને ટર્બાઇન કેટલી રાખે."),
        T("A wind turbine has a 100 m rotor and works in 1.225 kg/m³ air at 10 m/s. Find the power in "
          "the wind, the Betz limit, and the electrical output for Cp = 0.45 with a drive train "
          "efficiency of 0.95.",
          "પવન ટર્બાઇનનો રોટર 100 m છે અને 1.225 kg/m³ હવામાં 10 m/s પર ચાલે છે. પવનમાંની શક્તિ, બેટ્ઝ "
          "મર્યાદા અને Cp = 0.45 તથા 0.95 ડ્રાઇવ ટ્રેન કાર્યક્ષમતા માટે વીજ ઉત્પાદન શોધો."),
        [P("Swept area A = πD²/4 = π × 100²/4 = 7,854 m²", "ઘેરાયેલો વિસ્તાર A = πD²/4 = π × 100²/4 = 7,854 m²"),
         P("P = ½ρAv³ = 0.5 × 1.225 × 7,854 × 10³ = 4,810,575 W ≈ 4.81 MW",
           "P = ½ρAv³ = 0.5 × 1.225 × 7,854 × 10³ = 4,810,575 W ≈ 4.81 MW"),
         P("Betz limit = 16/27 = 0.593, so at most 0.593 × 4.81 = 2.85 MW can be extracted",
           "બેટ્ઝ મર્યાદા = 16/27 = 0.593, તેથી વધુમાં વધુ 0.593 × 4.81 = 2.85 MW ખેંચી શકાય"),
         P("Electrical output = 4.81 × 0.45 × 0.95 = 2.06 MW",
           "વીજ ઉત્પાદન = 4.81 × 0.45 × 0.95 = 2.06 MW")],
        T("4.81 MW in the wind, 2.85 MW at Betz, 2.06 MW electrical",
          "પવનમાં 4.81 MW, બેટ્ઝ પર 2.85 MW, વીજળી 2.06 MW"), unit_no=3),
    num("u3n02", T("How close a good turbine comes to the Betz limit.",
                   "સારી ટર્બાઇન બેટ્ઝ મર્યાદાની કેટલી નજીક આવે."),
        T("A turbine extracts 42 % of the power in the wind. Express this as a fraction of the Betz "
          "limit of 16/27.",
          "ટર્બાઇન પવનમાંની 42 % શક્તિ ખેંચે છે. તેને 16/27ની બેટ્ઝ મર્યાદાના અંશ તરીકે દર્શાવો."),
        [P("Betz limit = 16/27 = 0.5926", "બેટ્ઝ મર્યાદા = 16/27 = 0.5926"),
         P("Fraction of the limit = 0.42 / 0.5926 = 0.709", "મર્યાદાનો અંશ = 0.42 / 0.5926 = 0.709"),
         P("Losses: tip vortices, wake rotation, blade profile drag and the gearbox",
           "ખોટ: ટોચના વમળ, વેક ભ્રમણ, બ્લેડ પ્રોફાઇલ ડ્રેગ અને ગિયરબોક્સ")],
        T("70.9 % of the Betz limit, so 42 % of the wind power",
          "બેટ્ઝ મર્યાદાના 70.9 %, એટલે પવન શક્તિના 42 %"), unit_no=3),
    num("u3n03", T("Efficiency of one PV module.", "એક PV મોડ્યુલની કાર્યક્ષમતા."),
        T("A 445 Wp module has an area of 2.1 m² and is tested at 1,000 W/m². Find its efficiency and "
          "the power a 20-module array gives at that irradiance.",
          "445 Wp મોડ્યુલનો વિસ્તાર 2.1 m² છે અને તે 1,000 W/m² પર પરીક્ષણ પામે છે. તેની કાર્યક્ષમતા "
          "અને તે ઇરેડિયન્સ પર 20 મોડ્યુલની એરે કેટલી શક્તિ આપે તે શોધો."),
        [P("Input power = 1,000 × 2.1 = 2,100 W", "ઇનપુટ શક્તિ = 1,000 × 2.1 = 2,100 W"),
         P("η = 445 / 2,100 × 100 = 21.2 %", "η = 445 / 2,100 × 100 = 21.2 %"),
         P("Array = 20 × 445 = 8,900 W = 8.9 kWp at standard test conditions",
           "એરે = 20 × 445 = 8,900 W = 8.9 kWp પ્રમાણભૂત પરીક્ષણ સ્થિતિમાં")],
        T("21.2 % efficiency; 8.9 kWp for 20 modules",
          "21.2 % કાર્યક્ષમતા; 20 મોડ્યુલ માટે 8.9 kWp"), unit_no=3),
    num("u3n04", T("Daily and yearly energy from a rooftop plant.",
                   "છત પરના સ્ટેશનથી દૈનિક અને વાર્ષિક ઊર્જા."),
        T("A 5 kWp plant in Gujarat receives 4.6 peak sun hours a day with a performance ratio of 0.80. "
          "Find the daily and yearly output and the CO₂ avoided at 0.71 t per MWh.",
          "ગુજરાતમાં 5 kWp સ્ટેશનને દિવસે 4.6 પીક સન અવર્સ મળે અને કાર્યદક્ષતા ગુણોત્તર 0.80 છે. દૈનિક "
          "અને વાર્ષિક ઉત્પાદન તથા પ્રતિ MWh 0.71 t પ્રમાણે બચતનું CO₂ શોધો."),
        [P("Ideal daily energy = 5 × 4.6 = 23 kWh", "આદર્શ દૈનિક ઊર્જા = 5 × 4.6 = 23 kWh"),
         P("Actual = 23 × 0.80 = 18.4 kWh a day", "વાસ્તવિક = 23 × 0.80 = 18.4 kWh દિવસે"),
         P("Yearly = 18.4 × 365 = 6,716 kWh ≈ 6.72 MWh", "વાર્ષિક = 18.4 × 365 = 6,716 kWh ≈ 6.72 MWh"),
         P("CO₂ avoided = 6.716 × 0.71 = 4.77 t a year",
           "બચતનું CO₂ = 6.716 × 0.71 = 4.77 t વર્ષે")],
        T("18.4 kWh a day, 6.72 MWh a year, 4.77 t CO₂ avoided",
          "દિવસે 18.4 kWh, વર્ષે 6.72 MWh, 4.77 t CO₂ બચત"), unit_no=3),
    num("u3n05", T("Designing the module layout of an array.",
                   "એરેની મોડ્યુલ ગોઠવણીની રચના."),
        T("An inverter needs 5 kWp of modules. Each module is 250 Wp with Voc = 37.6 V and "
          "Isc = 8.7 A. The inverter accepts 150-450 V DC and 15 A per string. Find the number of "
          "modules and a workable series-parallel layout.",
          "ઇન્વર્ટરને 5 kWp મોડ્યુલ જોઈએ. દરેક મોડ્યુલ 250 Wp છે, Voc = 37.6 V અને Isc = 8.7 A. ઇન્વર્ટર "
          "150-450 V DC અને શ્રેણી દીઠ 15 A સ્વીકારે. મોડ્યુલની સંખ્યા અને યોગ્ય શ્રેણી-સમાંતર ગોઠવણી શોધો."),
        [P("Modules needed = 5,000 / 250 = 20", "જરૂરી મોડ્યુલ = 5,000 / 250 = 20"),
         P("Five in series gives 5 × 37.6 = 188 V, inside the window; eight in series would give 301 V "
           "but leaves little headroom above 450 V in cold weather",
           "પાંચ શ્રેણીમાં 5 × 37.6 = 188 V, મર્યાદામાં; આઠ શ્રેણીમાં 301 V થાય પણ ઠંડીમાં 450 V ઉપર "
           "થોડી જ જગ્યા રહે"),
         P("Strings = 20 / 5 = 4, each carrying 8.7 A, safely below 15 A",
           "શ્રેણી = 20 / 5 = 4, દરેક 8.7 A વહન કરે, 15 Aથી સુરક્ષિત રીતે નીચે"),
         P("Array current = 4 × 8.7 = 34.8 A into the combiner",
           "એરે પ્રવાહ = 4 × 8.7 = 34.8 A કોમ્બાઇનરમાં")],
        T("20 modules as 4 strings of 5; 188 V and 34.8 A",
          "20 મોડ્યુલ, 5ના 4 શ્રેણી; 188 V અને 34.8 A"), unit_no=3),
    num("u3n06", T("Sizing a family biogas plant.", "કુટુંબના બાયોગેસ સ્ટેશનનું માપ."),
        T("A family of six needs 0.4 m³ of gas per person a day. Cattle dung yields 0.04 m³ of biogas "
          "per kg. Find the daily dung needed and the number of cattle at 10 kg of dung per animal a day.",
          "છ વ્યક્તિના કુટુંબને દિવસે પ્રતિ વ્યક્તિ 0.4 m³ ગેસ જોઈએ. પશુનું છાણ પ્રતિ કિલો 0.04 m³ બાયોગેસ "
          "આપે. દૈનિક જરૂરી છાણ અને પ્રતિ પશુ દિવસે 10 કિલો છાણ પ્રમાણે પશુઓની સંખ્યા શોધો."),
        [P("Gas needed = 6 × 0.4 = 2.4 m³ a day", "જરૂરી ગેસ = 6 × 0.4 = 2.4 m³ દિવસે"),
         P("Dung = 2.4 / 0.04 = 60 kg a day", "છાણ = 2.4 / 0.04 = 60 કિલો દિવસે"),
         P("Cattle = 60 / 10 = 6 animals", "પશુ = 60 / 10 = 6 પશુ"),
         P("A 2 m³ Deenbandhu digester is the usual size for this duty",
           "આ કામ માટે 2 m³નો દીનબંધુ પાચક સામાન્ય માપ છે")],
        T("60 kg of dung from 6 cattle; a 2 m³ digester",
          "6 પશુમાંથી 60 કિલો છાણ; 2 m³ પાચક"), unit_no=3),
    num("u3n07", T("Biodiesel needed for a B20 blend.", "B20 મિશ્રણ માટે જરૂરી બાયોડીઝલ."),
        T("A depot sells 20,000 L of diesel a month and must supply it as B20, that is 20 % biodiesel "
          "by volume. Find the volumes and the mass of biodiesel at a density of 0.88 kg/L.",
          "ડેપો મહિને 20,000 L ડીઝલ વેચે અને તેને B20, એટલે કદ પ્રમાણે 20 % બાયોડીઝલ, તરીકે પૂરું પાડવું "
          "પડે. કદ અને 0.88 kg/L ઘનતાએ બાયોડીઝલનું દળ શોધો."),
        [P("Biodiesel = 0.20 × 20,000 = 4,000 L", "બાયોડીઝલ = 0.20 × 20,000 = 4,000 L"),
         P("Diesel = 20,000 − 4,000 = 16,000 L", "ડીઝલ = 20,000 − 4,000 = 16,000 L"),
         P("Mass = 4,000 × 0.88 = 3,520 kg of biodiesel a month",
           "દળ = 4,000 × 0.88 = 3,520 કિલો બાયોડીઝલ મહિને")],
        T("16,000 L diesel + 4,000 L biodiesel = 3,520 kg",
          "16,000 L ડીઝલ + 4,000 L બાયોડીઝલ = 3,520 કિલો"), unit_no=3),
    num("u3n08", T("Molasses needed for an E10 blend.", "E10 મિશ્રણ માટે જરૂરી ગોળ."),
        T("A fuel station sells 50,000 L of petrol a month as E10. One tonne of molasses gives 245 L of "
          "ethanol. Find the ethanol needed and the molasses per month.",
          "ઇંધણ સ્ટેશન મહિને 50,000 L પેટ્રોલ E10 તરીકે વેચે. એક ટન ગોળ 245 L ઇથેનોલ આપે. જરૂરી ઇથેનોલ "
          "અને મહિને ગોળ શોધો."),
        [P("Ethanol = 0.10 × 50,000 = 5,000 L", "ઇથેનોલ = 0.10 × 50,000 = 5,000 L"),
         P("Molasses = 5,000 / 245 = 20.4 t a month", "ગોળ = 5,000 / 245 = 20.4 ટન મહિને"),
         P("Petrol replaced = 5,000 L a month, about 3,600 kg of CO₂ avoided at 2.3 kg per litre "
           "less 30 % fermentation emissions", "બદલાયેલો પેટ્રોલ = મહિને 5,000 L, પ્રતિ લિટર 2.3 કિલો "
           "અને 30 % આથો ઉત્સર્જન બાદ લગભગ 3,600 કિલો CO₂ બચે")],
        T("5,000 L ethanol from 20.4 t of molasses a month",
          "મહિને 20.4 ટન ગોળમાંથી 5,000 L ઇથેનોલ"), unit_no=3),
    num("u3n09", T("Output of a binary geothermal plant.",
                   "દ્વિચક્ર ભૂતાપીય સ્ટેશનનું ઉત્પાદન."),
        T("A binary plant takes 150 kg/s of brine at 160 °C and returns it at 90 °C. The brine has "
          "cp = 4.2 kJ/kg·K and the cycle efficiency is 12 %. Find the heat extracted and the electrical "
          "output.",
          "દ્વિચક્ર સ્ટેશન 160 °C પર 150 kg/s ખારું પાણી લે અને 90 °C પર પાછું આપે. ખારા પાણીનો "
          "cp = 4.2 kJ/kg·K અને ચક્ર કાર્યક્ષમતા 12 % છે. ખેંચાયેલી ઉષ્મા અને વીજ ઉત્પાદન શોધો."),
        [P("Q = ṁ cp ΔT = 150 × 4.2 × (160 − 90) = 44,100 kW = 44.1 MW thermal",
           "Q = ṁ cp ΔT = 150 × 4.2 × (160 − 90) = 44,100 kW = 44.1 MW ઉષ્મા"),
         P("P = η Q = 0.12 × 44.1 = 5.29 MW electrical", "P = η Q = 0.12 × 44.1 = 5.29 MW વીજળી"),
         P("The plant runs 8,000 h a year, so 42.3 GWh a year",
           "સ્ટેશન વર્ષે 8,000 કલાક ચાલે, તેથી વર્ષે 42.3 GWh")],
        T("44.1 MW thermal giving 5.29 MW electrical",
          "44.1 MW ઉષ્મા, 5.29 MW વીજળી"), unit_no=3),
    num("u3n10", T("Energy from a tidal barrage.", "ભરતી બેરેજની ઊર્જા."),
        T("A barrage encloses a basin of 2 km² where the mean tidal range is 6 m. Sea water is "
          "1,025 kg/m³. Find the energy of one filling and the average power over a day with two "
          "emptying cycles.",
          "બેરેજ 2 km² તળાવ ઘેરે છે જ્યાં સરેરાશ ભરતીનો તફાવત 6 m છે. દરિયાનું પાણી 1,025 kg/m³ છે. એક "
          "ભરણની ઊર્જા અને દિવસમાં બે ખાલી કરવાના ચક્ર સાથે સરેરાશ શક્તિ શોધો."),
        [P("E = ½ A ρ g R² = 0.5 × 2×10⁶ × 1,025 × 9.81 × 6² = 3.62 × 10¹¹ J",
           "E = ½ A ρ g R² = 0.5 × 2×10⁶ × 1,025 × 9.81 × 6² = 3.62 × 10¹¹ J"),
         P("Each filling holds 362 GJ, and a day has two fill-empty cycles, so 724 GJ a day",
           "દરેક ભરણમાં 362 GJ અને દિવસમાં બે ભરણ-ખાલી ચક્ર, તેથી દિવસે 724 GJ"),
         P("Average power = 7.24 × 10¹¹ J / 86,400 s = 8.38 MW",
           "સરેરાશ શક્તિ = 7.24 × 10¹¹ J / 86,400 s = 8.38 MW")],
        T("362 GJ per filling, 724 GJ a day, 8.38 MW average",
          "દરેક ભરણે 362 GJ, દિવસે 724 GJ, સરેરાશ 8.38 MW"), unit_no=3),
    num("u3n11", T("Hydrogen from an electrolyser.", "વિદ્યુતવિભાજકમાંથી હાઇડ્રોજન."),
        T("A 10 MW electrolyser uses 52 kWh of electricity per kilogram of hydrogen. Find the hourly "
          "production and the efficiency, taking hydrogen's higher heating value as 39.4 kWh/kg.",
          "10 MW વિદ્યુતવિભાજક પ્રતિ કિલો હાઇડ્રોજન 52 kWh વીજળી વાપરે છે. કલાક દીઠ ઉત્પાદન અને "
          "કાર્યક્ષમતા શોધો; હાઇડ્રોજનનું ઊંચું ઉષ્મા મૂલ્ય 39.4 kWh/kg લો."),
        [P("Energy needed for 1 kg = 52 kWh", "1 કિલો માટે જરૂરી ઊર્જા = 52 kWh"),
         P("Production = 10,000 kW / 52 = 192 kg an hour", "ઉત્પાદન = 10,000 kW / 52 = 192 કિલો કલાકે"),
         P("Energy in the gas = 192 × 39.4 = 7,565 kWh, so η = 7,565 / 10,000 = 75.7 %",
           "ગેસમાંની ઊર્જા = 192 × 39.4 = 7,565 kWh, તેથી η = 7,565 / 10,000 = 75.7 %"),
         P("If the electricity is renewable, the hydrogen is green hydrogen",
           "વીજળી પુનઃપ્રાપ્ય હોય તો હાઇડ્રોજન લીલું હાઇડ્રોજન કહેવાય")],
        T("192 kg an hour at 75.7 % efficiency, green hydrogen",
          "કલાકે 192 કિલો, 75.7 % કાર્યક્ષમતા, લીલું હાઇડ્રોજન"), unit_no=3),
    num("u3n12", T("Carbon payback of a solar module.", "સૌર મોડ્યુલનો કાર્બન પરતફેળો."),
        T("Making a module needs about 600 kWh of energy per square metre, and each square metre makes "
          "210 kWh a year. Find the energy payback time and the carbon payback time if the factory "
          "electricity carries 0.71 kg CO₂ per kWh and the module displaces 0.71 kg CO₂ per kWh.",
          "એક ચોરસ મીટર મોડ્યુલ બનાવવા લગભગ 600 kWh ઊર્જા જોઈએ અને દરેક ચોરસ મીટર વર્ષે 210 kWh બનાવે. "
          "ઊર્જા પરતફેળાનો સમય અને કાર્બન પરતફેળાનો સમય શોધો, જો કારખાનાની વીજળી પ્રતિ kWh 0.71 કિલો CO₂ "
          "ધરે અને મોડ્યુલ પ્રતિ kWh 0.71 કિલો CO₂ બદલે."),
        [P("Energy payback = 600 / 210 = 2.86 years", "ઊર્જા પરતફેળો = 600 / 210 = 2.86 વર્ષ"),
         P("Emissions to make it = 600 × 0.71 = 426 kg CO₂ per m²",
           "બનાવવાનું ઉત્સર્જન = 600 × 0.71 = 426 કિલો CO₂ પ્રતિ m²"),
         P("Savings = 210 × 0.71 = 149 kg CO₂ a year, so carbon payback = 426 / 149 = 2.86 years",
           "બચત = 210 × 0.71 = 149 કિલો CO₂ વર્ષે, તેથી કાર્બન પરતફેળો = 426 / 149 = 2.86 વર્ષ"),
         P("Over 25 years the module returns about 3,700 kg of CO₂ for every 426 kg it cost",
           "25 વર્ષમાં મોડ્યુલ જે 426 કિલો ખર્ચ્યું તેના બદલે લગભગ 3,700 કિલો CO₂ પાછું આપે")],
        T("About 2.9 years for energy and carbon, then 22 years of net saving",
          "ઊર્જા અને કાર્બન બંને માટે લગભગ 2.9 વર્ષ, પછી 22 વર્ષ ચોખ્ખી બચત"), unit_no=3),
]

EQUATIONS = [
    {"title": T("Solar and wind", "સૌર અને પવન"),
     "items": [
         {"name": T("Module efficiency", "મોડ્યુલ કાર્યક્ષમતા"), "f": "η = P_max / (G × A)",
          "terms": T("G is the irradiance in W/m² and A the module area in m².",
                     "G એ W/m²માં ઇરેડિયન્સ અને A એ m²માં મોડ્યુલનો વિસ્તાર છે.")},
         {"name": T("Fill factor", "ભરણ અવયવ"), "f": "FF = P_max / (V_oc × I_sc)",
          "terms": T("0.75-0.82 for a healthy silicon module; a drop means a hot spot or a bad contact.",
                     "સ્વસ્થ સિલિકોન મોડ્યુલ માટે 0.75-0.82; ઘટે તો હોટ સ્પોટ કે ખરાબ સંપર્ક.")},
         {"name": T("Daily energy yield", "દૈનિક ઊર્જા ઉત્પાદન"), "f": "E = P × PSH × PR",
          "terms": T("PSH is peak sun hours and PR the performance ratio, about 0.75-0.85.",
                     "PSH એ પીક સન અવર્સ અને PR કાર્યદક્ષતા ગુણોત્તર, લગભગ 0.75-0.85.")},
         {"name": T("Power in the wind", "પવનમાંની શક્તિ"), "f": "P = ½ ρ A v³",
          "terms": T("ρ is air density, about 1.225 kg/m³ at sea level; A is the swept area.",
                     "ρ હવાની ઘનતા, સમુદ્ર સપાટીએ લગભગ 1.225 kg/m³; A ઘેરાયેલો વિસ્તાર.")},
         {"name": T("Betz limit", "બેટ્ઝ મર્યાદા"), "f": "P_max = (16/27) × ½ ρ A v³ = 0.593 P_wind",
          "terms": T("No rotor can extract more than 59.3 % of the power in the wind.",
                     "કોઈ રોટર પવનમાંની શક્તિના 59.3 %થી વધુ ખેંચી શકે નહીં.")},
         {"name": T("Capacity factor", "ક્ષમતા અવયવ"), "f": "CF = actual energy / (rating × 8,760 h)",
          "terms": T("Solar 15-22 %, wind 25-35 %, coal 55-70 %.",
                     "સૌર 15-22 %, પવન 25-35 %, કોલસો 55-70 %.")},
     ]},
    {"title": T("Bioenergy", "બાયોએનર્જી"),
     "items": [
         {"name": T("Biogas yield", "બાયોગેસ ઉત્પાદન"), "f": "V_gas = m_dung × y", 
          "terms": T("y is about 0.04 m³ of biogas per kg of fresh cattle dung.",
                     "y એ તાજા પશુના છાણના પ્રતિ કિલો લગભગ 0.04 m³ બાયોગેસ છે.")},
         {"name": T("Blend ratio", "મિશ્રણ ગુણોત્તર"), "f": "V_bio = f × V_total,  V_fossil = (1 − f) V_total",
          "terms": T("E10 is 10 % ethanol, B20 is 20 % biodiesel, both by volume.",
                     "E10 એટલે 10 % ઇથેનોલ, B20 એટલે 20 % બાયોડીઝલ, બંને કદ પ્રમાણે.")},
         {"name": T("Transesterification", "ટ્રાન્સએસ્ટરીફિકેશન"), "f": "triglyceride + 3 CH₃OH → 3 FAME + glycerol",
          "terms": T("About 100 kg of oil with 20 kg of methanol gives 100 kg of biodiesel and 10 kg of glycerol.",
                     "લગભગ 100 કિલો તેલ અને 20 કિલો મિથેનોલ 100 કિલો બાયોડીઝલ તથા 10 કિલો ગ્લિસરોલ આપે.")},
     ]},
    {"title": T("Geothermal, ocean and hydrogen", "ભૂતાપ, મહાસાગર અને હાઇડ્રોજન"),
     "items": [
         {"name": T("Geothermal heat", "ભૂતાપીય ઉષ્મા"), "f": "Q = ṁ cp ΔT,  P = η Q",
          "terms": T("ṁ is the brine flow in kg/s and cp about 4.2 kJ/kg·K for water.",
                     "ṁ એ kg/sમાં ખારા પાણીનો પ્રવાહ અને પાણી માટે cp લગભગ 4.2 kJ/kg·K.")},
         {"name": T("Tidal barrage energy", "ભરતી બેરેજની ઊર્જા"), "f": "E = ½ A ρ g R²",
          "terms": T("A is the basin area and R the tidal range; doubling R gives four times the energy.",
                     "A તળાવનો વિસ્તાર અને R ભરતીનો તફાવત; R બમણો થાય તો ઊર્જા ચાર ગણી.")},
         {"name": T("Hydrogen efficiency", "હાઇડ્રોજન કાર્યક્ષમતા"), "f": "η = HHV_H₂ / electricity per kg",
          "terms": T("52 kWh per kg against 39.4 kWh of higher heating value gives 75.7 %.",
                     "પ્રતિ કિલો 52 kWh સામે 39.4 kWh ઊંચું ઉષ્મા મૂલ્ય 75.7 % આપે.")},
         {"name": T("CO₂ avoided", "બચતનું CO₂"), "f": "m_CO₂ = E × EF",
          "terms": T("EF is the grid emission factor, about 0.71 t CO₂ per MWh in India.",
                     "EF એ ગ્રિડ ઉત્સર્જન અવયવ, ભારતમાં પ્રતિ MWh લગભગ 0.71 t CO₂.")},
     ]},
]

VIVA = [
    {"title": T("Solar and wind", "સૌર અને પવન"),
     "items": [
         {"q": T("What is the photovoltaic effect?", "ફોટોવોલ્ટેઇક પ્રભાવ શું છે?"),
          "a": T("When light of sufficient energy strikes a semiconductor junction, photons free "
                 "electrons and the built-in field separates them, so a voltage appears across the "
                 "cell and a current flows through an external circuit. The energy of the photon must "
                 "exceed the band gap, 1.1 eV for silicon.",
                 "પૂરતી ઊર્જાવાળો પ્રકાશ અર્ધવાહક સંધિ પર પડે ત્યારે ફોટોન ઇલેક્ટ્રોન મુક્ત કરે અને આંતરિક "
                 "ક્ષેત્ર તેમને અલગ કરે, તેથી સેલ પર વોલ્ટેજ દેખાય અને બહારના પરિપથમાં પ્રવાહ વહે. ફોટોનની "
                 "ઊર્જા બેન્ડ ગેપ, સિલિકોન માટે 1.1 eV, થી વધુ હોવી જોઈએ.")},
         {"q": T("Why is the efficiency of a silicon module only about 20 % when the "
                 "Shockley-Queisser limit is 33 %?",
                 "શોકલી-ક્વાઇસર મર્યાદા 33 % હોવા છતાં સિલિકોન મોડ્યુલની કાર્યક્ષમતા ફક્ત 20 % કેમ?"),
          "a": T("The theoretical limit assumes one junction, no reflection and perfect contacts. A "
                 "real module loses light by reflection and shade, loses the low-energy photons below "
                 "the gap, loses the excess energy of high-energy photons as heat, and pays for "
                 "resistance in the contacts and the busbars. Temperature adds a further 10-15 % loss "
                 "on a hot afternoon, and inverter and cable losses about 10 %.",
                 "સૈદ્ધાંતિક મર્યાદા એક સંધિ, કોઈ પરાવર્તન નહીં અને સંપૂર્ણ સંપર્ક ધારે છે. વાસ્તવિક મોડ્યુલ "
                 "પરાવર્તન અને છાયાથી પ્રકાશ ગુમાવે, ગેપથી નીચેના ઓછી ઊર્જાવાળા ફોટોન ગુમાવે, ઊંચી ઊર્જાવાળા "
                 "ફોટોનની વધારાની ઊર્જા ઉષ્મા તરીકે ગુમાવે અને સંપર્ક તથા બસબારના અવરોધનો ભોગ બને. ગરમ બપોરે "
                 "તાપમાન 10-15 % વધુ ખોટ ઉમેરે અને ઇન્વર્ટર-કેબલની ખોટ લગભગ 10 %.")},
         {"q": T("Which is better, a monocrystalline or a polycrystalline module?",
                 "મોનોક્રિસ્ટાલાઇન કે પોલીક્રિસ્ટાલાઇન મોડ્યુલ કયું સારું?"),
          "a": T("Monocrystalline gives 20-23 % against 15-18 %, so it needs 20-25 % less roof area for "
                 "the same kW and today costs only slightly more. It is the right choice where area is "
                 "limited, as on a city roof. Polycrystalline is chosen only when the budget per kW is "
                 "the deciding factor and area is free; on a large ground plant the extra land usually "
                 "costs more than the saving.",
                 "મોનોક્રિસ્ટાલાઇન 20-23 % આપે, પોલીક્રિસ્ટાલાઇન 15-18 %, તેથી સમાન kW માટે 20-25 % ઓછી "
                 "છતની જગ્યા જોઈએ અને આજે ભાવ થોડો જ વધુ છે. જ્યાં જગ્યા મર્યાદિત હોય, જેમ કે શહેરની છત પર, "
                 "તે યોગ્ય પસંદગી છે. પોલીક્રિસ્ટાલાઇન ત્યારે જ પસંદ કરાય જ્યાં પ્રતિ kW બજેટ નિર્ણાયક હોય "
                 "અને જમીન મફત હોય; મોટા જમીન સ્ટેશનમાં વધારાની જમીનનો ખર્ચ સામાન્ય રીતે બચત કરતાં વધુ પડે.")},
         {"q": T("What is the Betz limit and why does it exist?",
                 "બેટ્ઝ મર્યાદા શું છે અને તે કેમ અસ્તિત્વમાં છે?"),
          "a": T("Betz showed that a rotor can extract at most 16/27, about 59.3 %, of the power in the "
                 "wind. The wind that leaves the rotor must still be moving, otherwise no more air "
                 "could enter the disc; the slower it leaves, the more energy is taken but the less "
                 "mass flows through, and the product is maximum at one third of the approach speed. "
                 "Real turbines reach 70-80 % of this limit, that is Cp of 0.40-0.50.",
                 "બેટ્ઝે દર્શાવ્યું કે રોટર પવનમાંની શક્તિના વધુમાં વધુ 16/27, લગભગ 59.3 %, ખેંચી શકે. રોટર "
                 "છોડીને જતો પવન હજી ચાલતો હોવો જોઈએ, નહીં તો વધુ હવા ડિસ્કમાં આવી ન શકે; જેટલો ધીમો નીકળે "
                 "તેટલી વધુ ઊર્જા લેવાય પણ ઓછું દળ પસાર થાય, અને ગુણાકાર આવનારી ગતિના એક તૃતીયાંશ પર મહત્તમ "
                 "થાય. વાસ્તવિક ટર્બાઇન આ મર્યાદાના 70-80 %, એટલે Cp 0.40-0.50, પામે.")},
         {"q": T("Why are wind turbines built so tall with such long blades?",
                 "પવન ટર્બાઇન આટલા ઊંચા અને બ્લેડ આટલા લાંબા કેમ બનાવાય?"),
          "a": T("Wind speed rises with height because the ground and buildings slow the air, so a hub "
                 "at 120 m sees 20-30 % more wind than at 50 m, and power goes with the cube of speed. "
                 "The swept area goes with the square of the blade length, so doubling the blade gives "
                 "four times the area and roughly four times the energy from the same wind, while the "
                 "cost of the tower and blades grows much more slowly.",
                 "જમીન અને ઇમારતો હવાને ધીમી કરતાં હોવાથી પવનની ગતિ ઊંચાઈ સાથે વધે, તેથી 120 m પરનું હબ "
                 "50 m કરતાં 20-30 % વધુ પવન જુએ અને શક્તિ ગતિના ઘન પ્રમાણમાં હોય. ઘેરાયેલો વિસ્તાર બ્લેડની "
                 "લંબાઈના વર્ગ પ્રમાણમાં હોય, તેથી બ્લેડ બમણી થાય તો વિસ્તાર ચાર ગણો અને સમાન પવનમાંથી લગભગ "
                 "ચાર ગણી ઊર્જા મળે, જ્યારે ટાવર અને બ્લેડનો ખર્ચ ઘણો ધીમે વધે.")},
         {"q": T("What is the difference between kWp and kWh?",
                 "kWp અને kWh વચ્ચે શું ફરક છે?"),
          "a": T("kWp is the peak power a module or plant can deliver at standard test conditions - "
                 "1,000 W/m² and 25 °C - so it describes the size of the equipment. kWh is the energy "
                 "actually delivered over a period, so it describes the work done. A 5 kWp plant that "
                 "runs 4.6 peak sun hours at a performance ratio of 0.80 gives 5 × 4.6 × 0.80 = 18.4 "
                 "kWh a day. The ratio of the two is the capacity factor, and it is the number that "
                 "decides the cost per unit.",
                 "kWp એ પ્રમાણભૂત પરીક્ષણ સ્થિતિ - 1,000 W/m² અને 25 °C - પર મોડ્યુલ કે સ્ટેશન આપી શકે "
                 "તેવી ટોચની શક્તિ છે, તેથી તે સાધનનું માપ કહે. kWh એ સમયગાળામાં ખરેખર આપેલી ઊર્જા છે, તેથી "
                 "તે થયેલું કામ કહે. 5 kWp સ્ટેશન 4.6 પીક સન અવર્સ અને 0.80 કાર્યદક્ષતા ગુણોત્તરે દિવસે "
                 "5 × 4.6 × 0.80 = 18.4 kWh આપે. બંનેનો ગુણોત્તર ક્ષમતા અવયવ છે અને તે જ પ્રતિ યુનિટ ખર્ચ "
                 "નક્કી કરે.")},
         {"q": T("Where would you use a VAWT instead of a HAWT?",
                 "HAWTને બદલે VAWT ક્યાં વાપરશો?"),
          "a": T("A VAWT accepts wind from any direction, needs no yaw drive, is quiet and safe for "
                 "birds, and puts its generator at ground level, so it suits rooftops, street lamps, "
                 "water pumping in remote fields and places with turbulent, shifting wind. Its low Cp "
                 "of 0.15-0.35 rules it out for wind farms, where a HAWT with a large swept area and "
                 "Cp near 0.45 is far cheaper per unit of energy.",
                 "VAWT ગમે તે દિશાનો પવન સ્વીકારે, યો ડ્રાઇવ ન જોઈએ, શાંત છે અને પક્ષીઓ માટે સુરક્ષિત છે, "
                 "અને જનરેટર જમીન સ્તરે રાખે, તેથી તે છત, શેરી દીવા, દૂરના ખેતરમાં પાણી ઉપાડવા અને અશાંત "
                 "બદલાતા પવનવાળાં સ્થળો માટે યોગ્ય છે. તેનો નીચો Cp 0.15-0.35 તેને પવન ફાર્મ માટે અયોગ્ય કરે, "
                 "જ્યાં મોટા ઘેરાયેલા વિસ્તાર અને 0.45ની નજીક Cp વાળું HAWT પ્રતિ યુનિટ ઊર્જા ઘણું સસ્તું પડે.")},
     ]},
    {"title": T("Bioenergy and new sources", "બાયોએનર્જી અને નવા સ્રોત"),
     "items": [
         {"q": T("What is the difference between gasification and combustion of biomass?",
                 "બાયોમાસના ગેસિફિકેશન અને દહનમાં શું ફરક છે?"),
          "a": T("Combustion supplies enough oxygen for complete burning and gives heat, CO₂ and water. "
                 "Gasification supplies only 20-30 % of the air needed, so the biomass cannot burn "
                 "fully; it is cracked at 700-900 °C into producer gas containing CO, H₂, CH₄ and N₂. "
                 "That gas can be piped, cleaned and burnt in an engine, which gives electricity from "
                 "biomass with better control and lower tar and smoke than a plain chulha.",
                 "દહન પૂરતો ઓક્સિજન આપે છે અને ઉષ્મા, CO₂ તથા પાણી આપે. ગેસિફિકેશન જરૂરી હવાના ફક્ત 20-30 % "
                 "આપે, તેથી બાયોમાસ પૂરેપૂરું બળી શકતું નથી; તે 700-900 °C પર તૂટીને CO, H₂, CH₄ અને N₂ "
                 "ધરતો પ્રોડ્યુસર ગેસ બને. તે ગેસ પાઇપમાં લઈ જઈ, સાફ કરી એન્જિનમાં બાળી શકાય, જેથી બાયોમાસમાંથી "
                 "વધુ નિયંત્રણ અને સાદા ચૂલા કરતાં ઓછા ડામર અને ધુમાડા સાથે વીજળી મળે.")},
         {"q": T("Why is biogas called a better fuel than dung cake?",
                 "બાયોગેસ છાણના થાપા કરતાં સારું ઇંધણ કેમ કહેવાય?"),
          "a": T("Biogas is 55-65 % methane, so it burns with a clean blue flame, no smoke and high "
                 "efficiency, and can run an engine. Dung cake burns badly, fills the kitchen with "
                 "smoke and PM2.5, wastes the nitrogen as ammonia, and destroys the organic matter "
                 "the soil needs. Digesting the dung first traps the methane that would otherwise "
                 "escape, gives the gas for cooking, and leaves a digestate that is a better "
                 "fertiliser than the raw dung, so one input gives fuel, health and soil.",
                 "બાયોગેસ 55-65 % મિથેન છે, તેથી તે સ્વચ્છ ભૂરી જ્યોતથી બળે, ધુમાડો નહીં અને કાર્યક્ષમતા "
                 "ઊંચી, અને એન્જિન ચલાવી શકે. છાણનો થાપો ખરાબ બળે, રસોડું ધુમાડા અને PM2.5થી ભરે, નાઇટ્રોજનને "
                 "એમોનિયા તરીકે વેડફે અને જમીનને જરૂરી કાર્બનિક દ્રવ્ય નષ્ટ કરે. છાણનું પ્રથમ પાચન જે મિથેન "
                 "હવામાં જતું રહેતું તે પકડે, રાંધવા ગેસ આપે અને કાચા છાણ કરતાં સારું ખાતર આપે, તેથી એક જ "
                 "ઇનપુટ ઇંધણ, આરોગ્ય અને જમીન ત્રણેય આપે.")},
         {"q": T("What is the difference between tidal and wave energy?",
                 "ભરતી અને તરંગ ઊર્જામાં શું ફરક છે?"),
          "a": T("Tides are the slow vertical rise and fall of the sea caused by the gravity of the moon "
                 "and the sun; their timing is fixed by astronomy, so tidal energy is predictable years "
                 "in advance but needs a barrage or a strong tidal stream. Waves are wind-driven "
                 "surface motion, strong and continuous but irregular; wave devices must survive "
                 "storms and produce intermittent power. Tidal has high capital cost and few sites, "
                 "wave has many sites but immature technology.",
                 "ભરતી એ ચંદ્ર અને સૂર્યના ગુરુત્વાકર્ષણથી થતું દરિયાનું ધીમું ઊભું ચઢ-ઊતર છે; તેનો સમય "
                 "ખગોળશાસ્ત્રથી નિશ્ચિત હોય, તેથી ભરતી ઊર્જા વર્ષો પહેલાં અનુમાનિત છે પણ તેને બેરેજ કે તાકાતવાન "
                 "ભરતી પ્રવાહ જોઈએ. તરંગો પવનથી ચાલતી સપાટીની હિલચાલ છે, તાકાતવાન અને સતત પણ અનિયમિત; તરંગ "
                 "સાધનોએ તોફાન સહેવું પડે અને વીજળી અનિયમિત આપે. ભરતીનો મૂડી ખર્ચ ઊંચો અને સ્થળો ઓછાં, "
                 "તરંગનાં સ્થળો ઘણાં પણ ટેક્નોલોજી અપરિપક્વ.")},
         {"q": T("Why is hydrogen called an energy carrier and not an energy source?",
                 "હાઇડ્રોજનને ઊર્જા સ્રોત નહીં પણ ઊર્જા વાહક કેમ કહેવાય?"),
          "a": T("Because it does not occur free in useful quantities on earth; it is locked in water "
                 "and hydrocarbons and must be made with another source of energy, so it stores and "
                 "carries energy from where it was produced to where it is used. Burning it or running "
                 "it through a fuel cell gives back less energy than was spent making and compressing "
                 "it, exactly like a battery, so it is compared with batteries and transmission lines "
                 "rather than with coal or the sun.",
                 "કારણ કે તે પૃથ્વી પર ઉપયોગી પ્રમાણમાં મુક્ત મળતું નથી; તે પાણી અને હાઇડ્રોકાર્બનમાં બંધ છે "
                 "અને બીજા ઊર્જા સ્રોતથી બનાવવું પડે, તેથી તે ઊર્જા સંગ્રહે અને જ્યાં બન્યું ત્યાંથી જ્યાં "
                 "વપરાય ત્યાં લઈ જાય. તેને બાળવાથી કે ઇંધણ કોષમાંથી ચલાવવાથી બનાવવા અને દબાવવામાં ખર્ચેલી "
                 "ઊર્જા કરતાં ઓછી ઊર્જા પાછી મળે, બરાબર બેટરી જેવું, તેથી તેની સરખામણી કોલસા કે સૂર્ય સાથે "
                 "નહીં, બેટરી અને ટ્રાન્સમિશન લાઇન સાથે થાય.")},
         {"q": T("What decides the colour of hydrogen, and why does it matter?",
                 "હાઇડ્રોજનનો રંગ શું નક્કી કરે અને તે કેમ મહત્ત્વનું છે?"),
          "a": T("The colour names the production route, not the gas. Grey comes from steam reforming "
                 "of natural gas and emits about ten kilograms of CO₂ per kilogram of hydrogen; blue "
                 "is the same plant with carbon capture, one to two kilograms; green is electrolysis "
                 "with renewable electricity and almost none; turquoise is methane pyrolysis, which "
                 "gives solid carbon. It matters because only green and turquoise hydrogen actually "
                 "cut emissions, and hydrogen is sold on that guarantee.",
                 "રંગ ગેસ નહીં, ઉત્પાદન માર્ગનું નામ છે. ભૂખરું કુદરતી ગેસના વરાળ સુધારણમાંથી આવે અને પ્રતિ "
                 "કિલો હાઇડ્રોજન લગભગ દસ કિલો CO₂ છોડે; વાદળી તે જ સ્ટેશન કાર્બન પકડ સાથે, એકથી બે કિલો; "
                 "લીલું પુનઃપ્રાપ્ય વીજળીથી વિદ્યુતવિભાજન, લગભગ શૂન્ય; ફિરોઝી મિથેન પાયરોલિસિસ, જે ઘન કાર્બન "
                 "આપે. તે મહત્ત્વનું છે કારણ કે ફક્ત લીલું અને ફિરોઝી હાઇડ્રોજન ખરેખર ઉત્સર્જન ઘટાડે, અને "
                 "હાઇડ્રોજન તે ખાતરી પર વેચાય.")},
         {"q": T("What is the capacity factor and why does it matter more than the rating?",
                 "ક્ષમતા અવયવ શું છે અને તે રેટિંગ કરતાં વધુ કેમ મહત્ત્વનો છે?"),
          "a": T("Capacity factor is the actual energy produced in a year divided by the energy the "
                 "plant would make running flat out all year. A 2 MW turbine at 32 % makes 5.6 GWh; "
                 "the same 2 MW at a poor 18 % site makes 3.2 GWh. Since the capital cost is nearly the "
                 "same, the cost per unit changes by 75 %, so a wind site is judged by its capacity "
                 "factor and not by the nameplate rating painted on the nacelle.",
                 "ક્ષમતા અવયવ એ વર્ષમાં ખરેખર ઉત્પાદિત ઊર્જા ભાગ્યા સ્ટેશન આખું વર્ષ પૂરી ક્ષમતાએ ચાલે તો "
                 "બનતી ઊર્જા છે. 32 % પર 2 MW ટર્બાઇન 5.6 GWh બનાવે; નબળા 18 % સ્થળે તે જ 2 MW 3.2 GWh બનાવે. "
                 "મૂડી ખર્ચ લગભગ સરખો હોય તેથી પ્રતિ યુનિટ ખર્ચ 75 % બદલાય, તેથી પવન સ્થળ તેના ક્ષમતા અવયવથી "
                 "માપાય, નેસેલ પર લખેલા રેટિંગથી નહીં.")},
         {"q": T("Why can a renewable plant not replace a coal plant unit for unit?",
                 "પુનઃપ્રાપ્ય સ્ટેશન કોલસા સ્ટેશનને એકના એક બદલી કેમ ન શકે?"),
          "a": T("Because its output is not firm. A coal plant can be asked for 500 MW at any hour; a "
                 "solar plant gives nothing after sunset and a wind plant nothing in a calm spell, and "
                 "the grid must keep supply and demand equal every second. So a renewable plant is "
                 "paired with storage, a gas peaker, demand response or a stronger grid, and the "
                 "comparison is made on firm capacity and on the total system cost, not on the "
                 "cheapest hour of the day.",
                 "કારણ કે તેનું ઉત્પાદન નિશ્ચિત નથી. કોલસા સ્ટેશન પાસે ગમે તે કલાકે 500 MW માંગી શકાય; સૌર "
                 "સ્ટેશન સૂર્યાસ્ત પછી કંઈ ન આપે અને પવન સ્ટેશન શાંત સમયે કંઈ ન આપે, જ્યારે ગ્રિડે દરેક સેકન્ડે "
                 "પુરવઠો અને માંગ સમાન રાખવાં પડે. તેથી પુનઃપ્રાપ્ય સ્ટેશન સંગ્રહ, ગેસ પીકર, માંગ પ્રતિભાવ કે "
                 "મજબૂત ગ્રિડ સાથે જોડાય, અને સરખામણી નિશ્ચિત ક્ષમતા તથા કુલ પ્રણાલી ખર્ચ પર થાય, દિવસના "
                 "સૌથી સસ્તા કલાક પર નહીં.")},
     ]},
]

_PRACTICE = [
    (T("Explain, with figures, how a renewable source reduces the carbon footprint of a campus.",
       "આંકડા સાથે સમજાવો કે પુનઃપ્રાપ્ય સ્રોત કેમ્પસનું કાર્બન ફૂટપ્રિન્ટ કેવી રીતે ઘટાડે."), 5,
     [P("Start from the campus electricity bill. Suppose the college uses 4,00,000 kWh a year and the "
        "grid factor is 0.71 kg CO₂ per kWh, so the annual emission is 400 × 0.71 = 284 t CO₂. A "
        "200 kWp rooftop plant with 4.6 peak sun hours and a performance ratio of 0.80 makes "
        "200 × 4.6 × 0.80 = 736 kWh a day, about 2,69,000 kWh a year, which is 67 % of the demand.",
        "કેમ્પસના વીજળી બિલથી શરૂ કરો. ધારો કે કોલેજ વર્ષે 4,00,000 kWh વાપરે અને ગ્રિડ અવયવ પ્રતિ kWh "
        "0.71 કિલો CO₂ છે, તેથી વાર્ષિક ઉત્સર્જન 400 × 0.71 = 284 t CO₂. 4.6 પીક સન અવર્સ અને 0.80 "
        "કાર્યદક્ષતા ગુણોત્તરવાળું 200 kWp છત સ્ટેશન દિવસે 200 × 4.6 × 0.80 = 736 kWh, વર્ષે લગભગ "
        "2,69,000 kWh બનાવે, જે માંગના 67 % છે."),
      P("The saving is 269 × 0.71 = 191 t CO₂ a year, so the footprint falls from 284 t to 93 t, a cut "
        "of 67 %. The plant itself costs about 600 kWh per square metre of module and 1,300 m² of "
        "module makes 600 × 1,300 = 7,80,000 kWh of embodied energy, which the array returns in about "
        "2.9 years.",
        "બચત 269 × 0.71 = 191 t CO₂ વર્ષે, તેથી ફૂટપ્રિન્ટ 284 t થી 93 t થાય, એટલે 67 % ઘટે. સ્ટેશન પોતે "
        "પ્રતિ ચોરસ મીટર મોડ્યુલ લગભગ 600 kWh વાપરે અને 1,300 m² મોડ્યુલ 600 × 1,300 = 7,80,000 kWh "
        "સન્નિહિત ઊર્જા બનાવે, જે એરે લગભગ 2.9 વર્ષમાં પાછી મેળવે."),
      P("Add the indirect gains: no SO₂, NOx or fly ash at the point of use, a shaded roof that cuts "
        "air-conditioning load by 2-3 °C, and a visible meter that teaches the students. State the "
        "limits honestly - the plant gives nothing after sunset, so about a third of the night load "
        "still comes from the grid or from a battery.",
        "પરોક્ષ લાભ ઉમેરો: વપરાશના સ્થળે SO₂, NOx કે ફ્લાય એશ નહીં, છાયાવાળી છત જે એરકન્ડીશનિંગનો ભાર 2-3 °C "
        "ઘટાડે, અને વિદ્યાર્થીઓને શીખવતું દેખાતું મીટર. મર્યાદા પ્રામાણિકપણે જણાવો - સૂર્યાસ્ત પછી સ્ટેશન કંઈ "
        "ન આપે, તેથી રાત્રિના ભારનો લગભગ ત્રીજો ભાગ હજી ગ્રિડ કે બેટરીમાંથી આવે.")]),
    (T("Compare renewable and non-renewable energy sources on at least six points and conclude.",
       "ઓછામાં ઓછા છ મુદ્દા પર પુનઃપ્રાપ્ય અને બિન-પુનઃપ્રાપ્ય ઊર્જા સ્રોતોની સરખામણી કરી નિષ્કર્ષ આપો."), 5,
     [P("Availability: a renewable flow is refilled by nature and never exhausted, while a fossil stock "
        "is finite and India imports over 80 % of its crude oil. Running cost: a renewable plant has "
        "no fuel bill, whereas fuel is 60-80 % of the cost of a coal unit and is exposed to every "
        "price shock. Capital cost: solar and wind need almost all the money upfront, which is why "
        "financing cost decides the tariff.",
        "ઉપલબ્ધતા: પુનઃપ્રાપ્ય પ્રવાહ કુદરત ભરે અને કદી ખતમ ન થાય, જ્યારે અશ્મી સંગ્રહ મર્યાદિત છે અને ભારત "
        "તેના કાચા તેલના 80 %થી વધુ આયાત કરે. ચાલુ ખર્ચ: પુનઃપ્રાપ્ય સ્ટેશનમાં ઇંધણનું બિલ નહીં, જ્યારે "
        "કોલસા એકમના ખર્ચના 60-80 % ઇંધણ છે અને તે દરેક ભાવવધારાનો ભોગ બને. મૂડી ખર્ચ: સૌર અને પવનને લગભગ "
        "આખો પૈસો શરૂઆતમાં જોઈએ, તેથી ધિરાણ ખર્ચ ટેરિફ નક્કી કરે."),
      P("Output: renewables are variable, with capacity factors of 15-35 %, while coal gives a firm "
        "55-70 % and can be dispatched on demand. Land: solar needs about 4 acres per MW and wind more, "
        "while a coal plant is compact but its mines and ash ponds spread across districts. Emissions: "
        "renewables emit nothing at the plant and 40-50 g CO₂ per kWh over the whole life, against "
        "800-1,000 for coal.",
        "ઉત્પાદન: પુનઃપ્રાપ્ય બદલાતાં હોય, ક્ષમતા અવયવ 15-35 %, જ્યારે કોલસો નિશ્ચિત 55-70 % આપે અને માંગ "
        "પ્રમાણે આપી શકાય. જમીન: સૌરને પ્રતિ MW લગભગ 4 એકર અને પવનને વધુ જોઈએ, જ્યારે કોલસા સ્ટેશન સંકુચિત છે પણ "
        "તેની ખાણ અને રાખના તળાવ જિલ્લાઓમાં ફેલાય. ઉત્સર્જન: પુનઃપ્રાપ્ય સ્ટેશન પર કંઈ છોડતું નથી અને આખા "
        "જીવનમાં પ્રતિ kWh 40-50 g CO₂, કોલસાના 800-1,000 સામે."),
      P("Waste and social cost: coal leaves ash ponds that fail in monsoon, mine spoil and mercury, "
        "while renewables leave modules and blades to be recycled after 25 years and take far less "
        "water. Conclusion: no single plant is best at everything, so the honest comparison is the "
        "levellised cost of firm energy and the life-cycle emission. On both, Indian solar and wind "
        "now beat new coal, which is why the plan is a mix - renewables for energy, storage and gas "
        "for the evening peak, and coal retired gradually rather than switched off overnight.",
        "કચરો અને સામાજિક ખર્ચ: કોલસો ચોમાસામાં તૂટતાં રાખના તળાવ, ખાણનો કચરો અને પારો છોડે, જ્યારે પુનઃપ્રાપ્ય "
        "25 વર્ષ પછી મોડ્યુલ અને બ્લેડ રિસાયકલ કરવાનાં છોડે અને ઘણું ઓછું પાણી વાપરે. નિષ્કર્ષ: કોઈ એક સ્ટેશન "
        "દરેક બાબતમાં શ્રેષ્ઠ નથી, તેથી પ્રામાણિક સરખામણી નિશ્ચિત ઊર્જાના સમતુલિત ખર્ચ અને જીવનચક્ર ઉત્સર્જનની "
        "છે. બંનેમાં ભારતીય સૌર અને પવન હવે નવા કોલસાને હરાવે, તેથી યોજના મિશ્રણની છે - ઊર્જા માટે પુનઃપ્રાપ્ય, "
        "સાંજના ભાર માટે સંગ્રહ અને ગેસ, અને કોલસો ધીમે ધીમે નિવૃત્ત, રાતોરાત બંધ નહીં.")]),
    (T("Describe a solar PV cell with a sketch and explain how a module, a string and an array differ.",
       "સૌર PV સેલનું રેખાચિત્ર સાથે વર્ણન કરો અને મોડ્યુલ, શ્રેણી તથા એરે કેવી રીતે જુદા પડે તે સમજાવો."), 4,
     [P("A cell is five layers: a tempered glass cover, an anti-reflective coating, an n-type silicon "
        "layer, a p-type silicon layer and a back contact, with a metal grid on the front. The "
        "junction between n and p creates a depletion region with a built-in field. Light passing "
        "through the glass frees electron-hole pairs in the silicon within a diffusion length of the "
        "junction; the field sweeps electrons to the n side and holes to the p side, so the front grid "
        "becomes negative and the back contact positive.",
        "સેલમાં પાંચ સ્તર છે: ટેમ્પર્ડ કાચનું આવરણ, પ્રતિબિંબરોધી પડ, n-પ્રકારનું સિલિકોન સ્તર, p-પ્રકારનું "
        "સિલિકોન સ્તર અને પાછળનો સંપર્ક, જેની ઉપર ધાતુની જાળી હોય. n અને p વચ્ચેની સંધિ આંતરિક ક્ષેત્રવાળો "
        "ક્ષય વિસ્તાર બનાવે. કાચમાંથી પસાર થતો પ્રકાશ સંધિથી પ્રસરણ લંબાઈમાં સિલિકોનમાં ઇલેક્ટ્રોન-કાણાંની "
        "જોડી મુક્ત કરે; ક્ષેત્ર ઇલેક્ટ્રોનને n બાજુ અને કાણાંને p બાજુ ધકેલે, તેથી આગળની જાળી ઋણ અને પાછળનો "
        "સંપર્ક ધન બને."),
      P("A module seals 60 or 72 such cells in series under glass and laminate, so the voltages add: "
        "72 × 0.62 ≈ 45 V, and a 445 Wp module delivers about 10 A at that voltage. A string joins "
        "modules in series to build the DC voltage the inverter wants, say 20 modules at 45 V = 900 V "
        "with the same 10 A. An array is the whole set of strings in parallel on one inverter: four "
        "strings give 40 A at 900 V, about 36 kW, so power adds in parallel while voltage stays fixed.",
        "મોડ્યુલ આવા 60 કે 72 સેલને કાચ અને લેમિનેટ નીચે શ્રેણીમાં સીલ કરે, તેથી વોલ્ટેજ ઉમેરાય: "
        "72 × 0.62 ≈ 45 V, અને 445 Wp મોડ્યુલ તે વોલ્ટેજ પર લગભગ 10 A આપે. શ્રેણી મોડ્યુલને શ્રેણીમાં જોડી "
        "ઇન્વર્ટરને જોઈતું DC વોલ્ટેજ બનાવે, જેમ કે 20 મોડ્યુલ 45 V પર = 900 V, પ્રવાહ તે જ 10 A. એરે એ "
        "એક ઇન્વર્ટર પર સમાંતર જોડાયેલી આખી શ્રેણીઓ છે: ચાર શ્રેણી 900 V પર 40 A આપે, લગભગ 36 kW, તેથી "
        "સમાંતરમાં શક્તિ ઉમેરાય જ્યારે વોલ્ટેજ અચળ રહે."),
      P("The engineering point is matching: the string Voc at the coldest morning must stay below the "
        "inverter maximum, the string Vmp must stay inside the MPPT window on a hot afternoon, and "
        "parallel strings must have the same module count, otherwise the weaker string drags the "
        "current down.",
        "એન્જિનિયરિંગ મુદ્દો મેળ બેસાડવાનો છે: સૌથી ઠંડી સવારે શ્રેણીની Voc ઇન્વર્ટરની મહત્તમ મર્યાદાથી "
        "નીચે રહેવી જોઈએ, ગરમ બપોરે શ્રેણીની Vmp MPPT વિસ્તારમાં રહેવી જોઈએ, અને સમાંતર શ્રેણીઓમાં મોડ્યુલની "
        "સંખ્યા સરખી હોવી જોઈએ, નહીં તો નબળી શ્રેણી પ્રવાહ નીચે ખેંચે.")]),
    (T("What are the main types of solar cells? Give efficiency and one use of each.",
       "સૌર સેલના મુખ્ય પ્રકાર કયા છે? દરેકની કાર્યક્ષમતા અને એક ઉપયોગ આપો."), 4,
     [P("Monocrystalline silicon: 20-23 %, made from a single crystal ingot, black and uniform; used "
        "on city rooftops where roof area is limited. Polycrystalline silicon: 15-18 %, cast from "
        "molten silicon with visible grain; used in large ground plants where land is cheap and "
        "budget matters. Both dominate the market because they are stable for 25 years.",
        "મોનોક્રિસ્ટાલાઇન સિલિકોન: 20-23 %, એક જ સ્ફટિકના ગઠ્ઠામાંથી બને, કાળું અને સરખું; શહેરની છત પર "
        "વપરાય જ્યાં છતની જગ્યા મર્યાદિત છે. પોલીક્રિસ્ટાલાઇન સિલિકોન: 15-18 %, ઓગળેલા સિલિકોનમાંથી ઢાળેલું, "
        "દેખાતા દાણા સાથે; મોટા જમીન સ્ટેશનમાં વપરાય જ્યાં જમીન સસ્તી છે અને બજેટ મહત્ત્વનું છે. બંને બજાર પર "
        "રાજ કરે કારણ કે 25 વર્ષ ટકે છે."),
      P("Thin film: cadmium telluride at 16-19 %, CIGS at 17-20 % and amorphous silicon at 6-9 %. They "
        "use a micrometre of material, perform better in weak light and high temperature, and are used "
        "on very large plants, curved roofs, facades and solar pumps. Emerging cells: perovskite and "
        "tandem reach 25-33 % in the laboratory but still fail in humidity and ultraviolet light; "
        "they are being tested in pilot modules. The choice depends on area, climate and budget, not "
        "on efficiency alone.",
        "પાતળી ફિલ્મ: કેડમિયમ ટેલ્યુરાઇડ 16-19 %, CIGS 17-20 % અને એમોર્ફસ સિલિકોન 6-9 %. તે માઇક્રોમીટર "
        "જેટલો પદાર્થ વાપરે, નબળા પ્રકાશ અને ઊંચા તાપમાનમાં સારું કામ કરે, અને ખૂબ મોટા સ્ટેશન, વળેલી છત, "
        "મોભ અને સૌર પંપ પર વપરાય. ઉભરતા સેલ: પેરોવસ્કાઇટ અને ટેન્ડમ પ્રયોગશાળામાં 25-33 % પામે પણ ભેજ અને "
        "પારજાંબલી પ્રકાશમાં હજી નિષ્ફળ જાય; તે પ્રાયોગિક મોડ્યુલમાં પરીક્ષણ પામે છે. પસંદગી જગ્યા, હવામાન અને "
        "બજેટ પર આધારિત છે, ફક્ત કાર્યક્ષમતા પર નહીં.")]),
    (T("Compare HAWT and VAWT with a neat sketch and state where each is used.",
       "સ્વચ્છ રેખાચિત્ર સાથે HAWT અને VAWTની સરખામણી કરો અને દરેક ક્યાં વપરાય તે જણાવો."), 5,
     [P("A HAWT has its rotor shaft horizontal and facing the wind, with two or three long aerofoil "
        "blades sweeping a vertical disc. It needs a yaw drive to follow the wind direction, a tower "
        "120 m tall and a heavy foundation, but it reaches a Cp of 0.45-0.50 and is the only design "
        "used for utility wind farms on land and offshore, where units of 5-15 MW are normal.",
        "HAWTની રોટર ધરી આડી અને પવન તરફ હોય છે, બે કે ત્રણ લાંબા પાંખ જેવા બ્લેડ ઊભું વર્તુળ ઘેરે છે. "
        "પવનની દિશા પકડવા યો ડ્રાઇવ, 120 m ઊંચો ટાવર અને ભારે પાયો જોઈએ, પણ તે Cp 0.45-0.50 પામે અને "
        "જમીન પર તથા દરિયામાં ઉપયોગિતા પવન ફાર્મ માટે એકમાત્ર રચના છે, જ્યાં 5-15 MW એકમ સામાન્ય છે."),
      P("A VAWT has a vertical shaft with curved or straight blades - Savonius drag type, Darrieus lift "
        "type or H-rotor - and accepts wind from any direction without yaw. The generator sits at the "
        "ground, the tower sees less bending, it is quiet and safer for birds, but the blades pass "
        "through their own wake and Cp falls to 0.15-0.35, so units are small, 1-100 kW.",
        "VAWTની ધરી ઊભી અને બ્લેડ વળેલા કે સીધા - સેવોનિયસ ડ્રેગ પ્રકાર, ડેરિયસ લિફ્ટ પ્રકાર કે H-રોટર - "
        "હોય છે અને ગમે તે દિશાનો પવન યો વગર સ્વીકારે. જનરેટર જમીન પર બેસે, ટાવર પર વળાંકનો ભાર ઓછો, તે શાંત "
        "અને પક્ષીઓ માટે સુરક્ષિત છે, પણ બ્લેડ પોતાના વેકમાંથી પસાર થાય તેથી Cp 0.15-0.35 થાય, એટલે એકમ નાના, "
        "1-100 kW."),
      P("So the choice is a compromise between efficiency and convenience: for energy at scale take a "
        "HAWT, for a rooftop, a street lamp, a remote water pump or a place where wind shifts "
        "constantly take a VAWT. The bladeless vortex machine is a third option, extremely quiet and "
        "simple but at only a few per cent efficiency, useful for small sensors rather than for power "
        "supply.",
        "તેથી પસંદગી કાર્યક્ષમતા અને સુવિધા વચ્ચેનો સમજૂતી છે: મોટા પ્રમાણમાં ઊર્જા માટે HAWT લો, છત, શેરી "
        "દીવો, દૂરનો પાણી પંપ કે સતત બદલાતો પવન હોય ત્યાં VAWT લો. બ્લેડ વગરનું વમળ મશીન ત્રીજો વિકલ્પ છે, "
        "અત્યંત શાંત અને સાદું પણ ફક્ત થોડા ટકા કાર્યક્ષમતા સાથે, નાના સેન્સર માટે ઉપયોગી, વીજ પુરવઠા માટે નહીં.")]),
    (T("Describe the parts and operation of a horizontal-axis wind turbine.",
       "આડી અક્ષની પવન ટર્બાઇનના ભાગો અને કાર્યપદ્ધતિનું વર્ણન કરો."), 4,
     [P("The rotor is three blades bolted to a hub. Wind flowing over the aerofoil creates lift, just "
        "as on an aircraft wing, and the lift component in the plane of rotation produces torque, so "
        "the rotor turns at 10-20 rpm. Blade pitch motors can twist each blade about its axis: at low "
        "wind they set the best angle for maximum lift, and above the rated wind speed they feather "
        "the blade to spill the extra power and protect the gearbox.",
        "રોટર એ હબ પર બોલ્ટ કરેલા ત્રણ બ્લેડ છે. પાંખ જેવી સપાટી પર વહેતો પવન લિફ્ટ બનાવે, વિમાનની પાંખની જેમ, "
        "અને ભ્રમણના સમતલમાં લિફ્ટનો ઘટક ટોર્ક બનાવે, તેથી રોટર 10-20 rpm પર ફરે. બ્લેડ પિચ મોટર દરેક બ્લેડને "
        "ધરી પર વાળે: ઓછા પવનમાં મહત્તમ લિફ્ટ માટે શ્રેષ્ઠ ખૂણો રાખે અને રેટેડ ગતિથી ઉપર બ્લેડ વાળીને વધારાની "
        "શક્તિ છોડે તથા ગિયરબોક્સ બચાવે."),
      P("Behind the hub, the low-speed shaft enters the nacelle through the main bearing and turns the "
        "gearbox, which raises the speed to about 1,500 rpm for the generator; a direct-drive machine "
        "replaces the gearbox with a large multi-pole generator. The nacelle also holds the brake, the "
        "yaw drive with its ring gear, the anemometer and wind vane, and a crane hatch. The tower, "
        "100-140 m, carries the nacelle, and the foundation resists the overturning moment.",
        "હબની પાછળ ધીમી ધરી મુખ્ય બેરિંગમાંથી નેસેલમાં પ્રવેશે અને ગિયરબોક્સ ફેરવે, જે ગતિ જનરેટર માટે લગભગ "
        "1,500 rpm કરે; ડાયરેક્ટ-ડ્રાઇવ મશીન ગિયરબોક્સને બદલે મોટું બહુ-ધ્રુવ જનરેટર વાપરે. નેસેલમાં બ્રેક, "
        "રિંગ ગિયર સાથેની યો ડ્રાઇવ, એનિમોમીટર અને પવન દિશા તથા ક્રેન બારણું પણ હોય. 100-140 mનો ટાવર "
        "નેસેલ ઉપાડે અને પાયો ઊલટવાના ભાર સામે ટકે."),
      P("Operation is a control loop. Below cut-in, about 3 m/s, the turbine is parked; between cut-in "
        "and rated, about 12 m/s, it tracks the maximum Cp by adjusting tip-speed ratio, so power rises "
        "with the cube of wind speed; between rated and cut-out, about 25 m/s, pitch control holds the "
        "power constant; above cut-out the machine yaws out of the wind and stops for safety.",
        "કાર્યપદ્ધતિ નિયંત્રણ ચક્ર છે. કટ-ઇન લગભગ 3 m/sથી નીચે ટર્બાઇન ઊભું રહે; કટ-ઇન અને રેટેડ વચ્ચે, "
        "લગભગ 12 m/s, ટોચ-ગતિ ગુણોત્તર ગોઠવીને મહત્તમ Cp પકડે, તેથી શક્તિ પવન ગતિના ઘન પ્રમાણમાં વધે; રેટેડ "
        "અને કટ-આઉટ વચ્ચે, લગભગ 25 m/s, પિચ નિયંત્રણ શક્તિ અચળ રાખે; કટ-આઉટથી ઉપર મશીન પવનમાંથી બહાર વળીને "
        "સુરક્ષા માટે થોભે.")]),
    (T("What is a bladeless wind turbine? State its advantages and limitations.",
       "બ્લેડ વગરની પવન ટર્બાઇન શું છે? તેના લાભ અને મર્યાદા જણાવો."), 3,
     [P("It is a tapered mast fixed at the base that sways when wind flows past it. The wind sheds "
        "vortices alternately from each side - the von Karman vortex street - and the changing pressure "
        "pushes the mast back and forth at its natural frequency. This is vortex-induced vibration, "
        "the same effect that destroyed the Tacoma Narrows bridge in 1940. Magnets on the mast move "
        "past coils at the base and generate electricity, so there is no blade, no gearbox, no yaw "
        "and only one moving part.",
        "તે પાયા પર જડાયેલો પાતળો થતો થાંભલો છે જે પવન પસાર થાય ત્યારે ડોલે. પવન બંને બાજુથી વારાફરતી વમળ છોડે - "
        "ફોન કાર્મન વમળ શ્રેણી - અને બદલાતું દબાણ થાંભલાને તેની કુદરતી આવૃત્તિ પર આગળ-પાછળ ધકેલે. આ વમળ-જનિત "
        "કંપન છે, જે અસરથી 1940માં ટેકોમા નેરોઝ પુલ તૂટ્યો. થાંભલા પરના ચુંબક પાયા પાસેની કોઇલ પાસેથી પસાર "
        "થઈ વીજળી બનાવે, તેથી બ્લેડ નહીં, ગિયરબોક્સ નહીં, યો નહીં અને ફક્ત એક ફરતો ભાગ."),
      P("Advantages: very few parts, so low manufacturing and maintenance cost; extremely quiet; no "
        "blade tips to kill birds or bats; safe to stand beside a road or a house; works in turbulent "
        "city wind and starts at low speed. Limitations: efficiency is only a few per cent, a small "
        "fraction of the Betz limit, so output per unit is hundreds of watts; it is tuned to one "
        "resonance, so it suffers far off that wind speed; a tall slender mast in a storm needs the "
        "same care as any other structure; and it cannot yet supply grid power economically.",
        "લાભ: ખૂબ ઓછા ભાગ, તેથી બનાવવાનો અને જાળવણીનો ખર્ચ ઓછો; અત્યંત શાંત; પક્ષી કે ચામાચીડિયાં મારતી બ્લેડની "
        "ટોચ નહીં; રસ્તા કે ઘર પાસે ઊભું કરવું સુરક્ષિત; શહેરના અશાંત પવનમાં ચાલે અને ઓછી ગતિએ શરૂ થાય. મર્યાદા: "
        "કાર્યક્ષમતા ફક્ત થોડા ટકા, બેટ્ઝ મર્યાદાનો નાનો અંશ, તેથી પ્રતિ એકમ ઉત્પાદન સેંકડો વોટ; તે એક અનુનાદ "
        "પર ગોઠવાયેલું હોય તેથી તે ગતિથી દૂર ખૂબ હાલે; તોફાનમાં ઊંચો પાતળો થાંભલો બીજી કોઈ પણ રચના જેવી "
        "કાળજી માંગે; અને તે હજી ગ્રિડ શક્તિ આર્થિક રીતે આપી શકતું નથી.")]),
    (T("Explain the production of ethanol and biodiesel in India with the reactions and blends.",
       "ભારતમાં ઇથેનોલ અને બાયોડીઝલના ઉત્પાદનને પ્રક્રિયા અને મિશ્રણ સાથે સમજાવો."), 5,
     [P("Ethanol: molasses or cane juice is diluted, yeast is added and fermentation converts sugar "
        "to ethanol and CO₂ in 30-48 hours - C₆H₁₂O₆ → 2 C₂H₅OH + 2 CO₂. The broth, at 8-12 % alcohol, "
        "is distilled to 95 % and dehydrated with molecular sieves to fuel grade. One tonne of "
        "molasses gives about 245 L. India blends E10 and is moving to E20, which needs about "
        "1,000 crore litres a year and is fed by sugarcane, surplus grain and now rice straw.",
        "ઇથેનોલ: ગોળ કે શેરડીનો રસ મંદ કરાય, ખમીર ઉમેરાય અને આથો 30-48 કલાકમાં ખાંડને ઇથેનોલ અને CO₂માં "
        "ફેરવે - C₆H₁₂O₆ → 2 C₂H₅OH + 2 CO₂. 8-12 % દારૂવાળું મિશ્રણ 95 % સુધી નિસ્યંદિત થાય અને મોલેક્યુલર "
        "ચાળણીથી પાણી કાઢી ઇંધણ-દરજ્જું બને. એક ટન ગોળ લગભગ 245 L આપે. ભારત E10 ભેળવે છે અને E20 તરફ જાય છે, "
        "જેને વર્ષે લગભગ 1,000 કરોડ લિટર જોઈએ અને જે શેરડી, વધારાના અનાજ અને હવે પરાળથી પૂરું પડે છે."),
      P("Biodiesel: oil or fat is heated with methanol and a base catalyst, usually 6 mol of methanol "
        "to 1 mol of triglyceride, for an hour at 60 °C. The triglyceride is broken into three methyl "
        "esters - the biodiesel - and glycerol settles out. The glycerol is 10 % by mass and is sold to "
        "soap and pharma units; the biodiesel is washed, dried and blended as B5 to B20. Feedstock is "
        "used cooking oil from hotels, jatropha and karanja grown on waste land, and cotton-seed oil.",
        "બાયોડીઝલ: તેલ કે ચરબી મિથેનોલ અને ક્ષારક ઉત્પ્રેરક સાથે, સામાન્ય રીતે 1 મોલ ટ્રાઇગ્લિસરાઇડ માટે "
        "6 મોલ મિથેનોલ, 60 °C પર એક કલાક ગરમ કરાય. ટ્રાઇગ્લિસરાઇડ તૂટીને ત્રણ મિથાઇલ એસ્ટર - બાયોડીઝલ - બને "
        "અને ગ્લિસરોલ નીચે બેસે. ગ્લિસરોલ દળ પ્રમાણે 10 % હોય અને સાબુ તથા દવા એકમોને વેચાય; બાયોડીઝલ ધોવાય, "
        "સૂકાય અને B5 થી B20 તરીકે ભળે. કાચો માલ હોટેલનું વપરાયેલું રાંધણ તેલ, બંજર જમીન પરનાં જટ્રોફા અને "
        "કરંજ તથા કપાસિયાનું તેલ છે."),
      P("Two cautions for the exam answer. First, ethanol has about two-thirds the energy of petrol, "
        "so a 20 % blend raises fuel consumption slightly, and it is hygroscopic, so storage needs "
        "care. Second, the real saving is 50-70 %, not 100 %, because the crop, the fertiliser and the "
        "distillation all use energy; and diverting food grain to fuel is a policy question, not only "
        "a technical one.",
        "પરીક્ષાના જવાબમાં બે ચેતવણી. પ્રથમ, ઇથેનોલની ઊર્જા પેટ્રોલના લગભગ બે તૃતીયાંશ છે, તેથી 20 % મિશ્રણ "
        "ઇંધણ વપરાશ થોડો વધારે, અને તે ભેજ શોષે છે, તેથી સંગ્રહમાં કાળજી જોઈએ. બીજું, ખરી બચત 50-70 % છે, "
        "100 % નહીં, કારણ કે પાક, ખાતર અને નિસ્યંદન બધું ઊર્જા વાપરે છે; અને ખાદ્ય અનાજને ઇંધણ તરફ વાળવું "
        "ફક્ત ટેકનિકલ નહીં, નીતિનો પ્રશ્ન છે.")]),
    (T("Explain biomass gasification with a block diagram and compare it with anaerobic digestion.",
       "બ્લોક ડાયાગ્રામ સાથે બાયોમાસ ગેસિફિકેશન સમજાવો અને અવાયુજીવી પાચન સાથે સરખાવો."), 5,
     [P("Gasification takes place in four zones of a downdraft or fluidised bed reactor. In the drying "
        "zone moisture leaves at 100-150 °C; in the pyrolysis zone, 300-600 °C with little air, the "
        "biomass breaks into char, tar and gas; in the oxidation zone the char burns with the injected "
        "air at 900-1,100 °C and supplies all the heat; in the reduction zone CO₂ and water react with "
        "hot char to give CO and H₂. The producer gas leaves at 300-500 °C with 18-22 % CO, 15-20 % H₂, "
        "2-4 % CH₄ and the rest nitrogen, and a heating value of 4-6 MJ/m³ - low, but enough for an "
        "engine.",
        "ગેસિફિકેશન ડાઉનડ્રાફ્ટ કે ફ્લુઇડાઇઝ્ડ બેડ રિએક્ટરના ચાર વિભાગમાં થાય. સૂકવણી વિભાગમાં 100-150 °C પર "
        "ભેજ નીકળે; પાયરોલિસિસ વિભાગમાં, ઓછી હવા સાથે 300-600 °C પર, બાયોમાસ કોલસા, ડામર અને ગેસમાં તૂટે; "
        "ઓક્સિડેશન વિભાગમાં દાખલ કરેલી હવા સાથે કોલસો 900-1,100 °C પર બળે અને આખી ઉષ્મા આપે; ક્ષય વિભાગમાં "
        "CO₂ અને પાણી ગરમ કોલસા સાથે પ્રક્રિયા કરી CO અને H₂ આપે. પ્રોડ્યુસર ગેસ 300-500 °C પર 18-22 % CO, "
        "15-20 % H₂, 2-4 % CH₄ અને બાકી નાઇટ્રોજન સાથે નીકળે અને તેનું ઉષ્મા મૂલ્ય 4-6 MJ/m³ - ઓછું, પણ "
        "એન્જિન માટે પૂરતું."),
      P("Digestion is a biological route at 35-55 °C with no air at all: hydrolysis, acidogenesis, "
        "acetogenesis and methanogenesis take 20-40 days and give biogas of 55-65 % methane with a "
        "heating value of 20-25 MJ/m³, plus a wet digestate. So gasification is fast, dry, needs a "
        "clean dry fuel and gives a low-grade gas; digestion is slow, wet, tolerates dung and food "
        "waste and gives a richer gas. Gasification suits rice husk and wood chips for engines; "
        "digestion suits cattle dung and kitchen waste for cooking and small power.",
        "પાચન 35-55 °C પર હવા વગરનો જૈવિક માર્ગ છે: જળવિભાજન, એસિડજનન, એસિટોજનન અને મિથેનજનન 20-40 દિવસ લે "
        "અને 55-65 % મિથેનવાળો બાયોગેસ, જેનું ઉષ્મા મૂલ્ય 20-25 MJ/m³, તથા ભીનું પાચિત ખાતર આપે. તેથી "
        "ગેસિફિકેશન ઝડપી, સૂકું, સ્વચ્છ સૂકું ઇંધણ માંગે અને નીચી કક્ષાનો ગેસ આપે; પાચન ધીમું, ભીનું, છાણ "
        "અને રસોડાનો કચરો સહે અને વધુ શક્તિશાળી ગેસ આપે. ગેસિફિકેશન ભૂસું અને લાકડાની ચીપને એન્જિન માટે યોગ્ય "
        "છે; પાચન પશુના છાણ અને રસોડાના કચરાને રાંધણ અને નાની વીજળી માટે.")]),
    (T("Explain geothermal energy with its three plant types and India's position.",
       "ભૂતાપીય ઊર્જા તેના ત્રણ સ્ટેશન પ્રકાર અને ભારતની સ્થિતિ સાથે સમજાવો."), 4,
     [P("Heat comes from the decay of uranium, thorium and potassium in the crust and from the "
        "original heat of formation, and flows outward at 60-80 mW/m², giving a gradient of 25-30 °C "
        "per kilometre. A well 3 km deep therefore finds water at 80-100 °C almost anywhere, and more "
        "in a fault zone. The three plant types are chosen by temperature.",
        "ઉષ્મા પોપડામાં યુરેનિયમ, થોરિયમ અને પોટેશિયમના ક્ષય તથા રચના વખતની મૂળ ઉષ્મામાંથી આવે અને 60-80 mW/m² "
        "દરે બહાર વહે, જે પ્રતિ કિલોમીટર 25-30 °C ઢાળ આપે. તેથી 3 કિમી ઊંડો કૂવો લગભગ દરેક જગ્યાએ 80-100 °Cનું "
        "પાણી પામે અને ભ્રંશ વિસ્તારમાં વધુ. ત્રણ સ્ટેશન પ્રકાર તાપમાન પ્રમાણે પસંદ થાય."),
      P("Dry steam plants use steam straight from the well above 240 °C. Flash plants let water at "
        "180-240 °C boil in a low-pressure vessel and use the steam. Binary plants pass brine at "
        "100-180 °C through a heat exchanger to vaporise a low-boiling fluid such as isobutane, which "
        "spins the turbine; they emit nothing to the air and can use moderate heat, which is why they "
        "are the most widely built today. A 150 kg/s flow cooled from 160 to 90 °C carries 44 MW of "
        "heat and gives about 5 MW of electricity at 12 % efficiency.",
        "સૂકી વરાળ સ્ટેશન 240 °Cથી ઉપર કૂવાની વરાળ સીધી વાપરે. ફ્લેશ સ્ટેશન 180-240 °Cનું પાણી નીચા દબાણની "
        "ટાંકીમાં ઉકાળીને વરાળ વાપરે. દ્વિચક્ર સ્ટેશન 100-180 °Cનું ખારું પાણી ઉષ્મા વિનિમયકમાંથી પસાર કરી "
        "નીચા ઉકળાંકવાળો પ્રવાહી, જેમ કે આઇસોબ્યુટેન, બાષ્પિત કરે, જે ટર્બાઇન ફેરવે; તે હવામાં કંઈ છોડતું નથી "
        "અને મધ્યમ ઉષ્મા વાપરી શકે, તેથી આજે સૌથી વધુ બનાવાય છે. 160 થી 90 °C સુધી ઠંડું થતું 150 kg/s પ્રવાહ "
        "44 MW ઉષ્મા ધરે અને 12 % કાર્યક્ષમતાએ લગભગ 5 MW વીજળી આપે."),
      P("India has no high-temperature field; the Puga valley in Ladakh, Manikaran in Himachal and "
        "parts of the Deccan have moderate heat and are used for space heating, bathing and greenhouses. "
        "The Geological Survey of India estimates about 10 GW of potential, but drilling cost, "
        "corrosion by hydrogen sulphide and the distance from the grid have kept the installed base "
        "under 10 MW, mostly demonstration.",
        "ભારતમાં ઊંચા તાપમાનનું ક્ષેત્ર નથી; લદ્દાખની પુગા ખીણ, હિમાચલનું મણિકરણ અને દક્કનના કેટલાક ભાગમાં મધ્યમ "
        "ઉષ્મા છે, જે જગ્યા ગરમ કરવા, સ્નાન અને કાચઘર માટે વપરાય. ભારતીય ભૂસ્તરીય સર્વેક્ષણ લગભગ 10 GW "
        "ક્ષમતા આંકે, પણ ડ્રિલિંગ ખર્ચ, હાઇડ્રોજન સલ્ફાઇડનો કાટ અને ગ્રિડથી અંતરને કારણે સ્થાપિત ક્ષમતા "
        "10 MWથી ઓછી, મોટે ભાગે પ્રદર્શન.")]),
    (T("Write short notes on ocean energy and hydrogen as a future fuel.",
       "મહાસાગર ઊર્જા અને ભવિષ્યના ઇંધણ તરીકે હાઇડ્રોજન પર ટૂંકી નોંધ લખો."), 5,
     [P("Ocean energy has three branches. Tidal range uses a barrage across an estuary; the energy of "
        "one filling is ½AρgR², so the range matters twice as much as the area, and a 2 km² basin with "
        "6 m range stores 362 GJ per filling. Tidal stream uses underwater turbines that look like wind "
        "turbines and need no dam. Wave devices convert the heave, surge or pitch of the surface - "
        "oscillating water column, point absorber, overtopping. OTEC uses the 20 °C difference between "
        "warm surface water and cold water at 1,000 m to run a closed ammonia cycle and gives "
        "electricity, fresh water and cooling together.",
        "મહાસાગર ઊર્જાની ત્રણ શાખા છે. ભરતીના તફાવતમાં જળમાર્ગ પર બેરેજ વપરાય; એક ભરણની ઊર્જા ½AρgR² છે, તેથી "
        "તફાવત વિસ્તાર કરતાં બમણો મહત્ત્વનો છે, અને 6 m તફાવતવાળું 2 km² તળાવ પ્રતિ ભરણે 362 GJ સંગ્રહે. "
        "ભરતી પ્રવાહમાં પવન ટર્બાઇન જેવા પાણી નીચેના ટર્બાઇન વપરાય અને બંધ ન જોઈએ. તરંગ સાધનો સપાટીના "
        "ઊંચા-નીચા, આગળ-પાછળ કે ઝુકાવને ફેરવે - ડોલતો પાણી સ્તંભ, બિંદુ શોષક, ઓવરટોપિંગ. OTEC ગરમ "
        "સપાટીના પાણી અને 1,000 m નીચેના ઠંડા પાણી વચ્ચેના 20 °C તફાવતથી બંધ એમોનિયા ચક્ર ચલાવે અને સાથે "
        "વીજળી, મીઠું પાણી તથા ઠંડક આપે."),
      P("Hydrogen is an energy carrier with 33.3 kWh of heat per kilogram, three times petrol by mass, "
        "and only water vapour as exhaust. Green hydrogen is made by electrolysis of water with "
        "renewable electricity at 50-55 kWh per kilogram, an efficiency of about 70-75 %; a PEM fuel "
        "cell returns 50-60 % of that. It will first replace grey hydrogen in refineries, steel and "
        "fertiliser, then run long-distance trucks, buses and ships.",
        "હાઇડ્રોજન ઊર્જા વાહક છે, પ્રતિ કિલો 33.3 kWh ઉષ્મા, દળ પ્રમાણે પેટ્રોલ કરતાં ત્રણ ગણું, અને નિકાસમાં "
        "ફક્ત પાણીની વરાળ. લીલું હાઇડ્રોજન પુનઃપ્રાપ્ય વીજળીથી પાણીના વિદ્યુતવિભાજન દ્વારા પ્રતિ કિલો 50-55 kWh "
        "વાપરીને બને, લગભગ 70-75 % કાર્યક્ષમતા; PEM ઇંધણ કોષ તેમાંથી 50-60 % પાછું આપે. તે પહેલાં રિફાઇનરી, "
        "પોલાદ અને ખાતરમાં ભૂખરા હાઇડ્રોજનને બદલશે, પછી લાંબા અંતરના ટ્રક, બસ અને જહાજ ચલાવશે."),
      P("The honest limits: round-trip efficiency of power-to-gas-to-power is only 30-35 %, so "
        "hydrogen is the last choice after direct electrification and batteries; storage at 350-700 "
        "bar or at −253 °C costs energy; hydrogen embrittles steel and leaks through small gaps; and "
        "the flame is almost invisible, so leak detection is a safety issue. Ocean energy has the "
        "mirror problem - a huge but dilute resource in a corrosive, stormy environment far from the "
        "grid.",
        "પ્રામાણિક મર્યાદા: વીજળી-થી-ગેસ-થી-વીજળીની આવ-જાવ કાર્યક્ષમતા ફક્ત 30-35 % છે, તેથી સીધા વીજીકરણ અને "
        "બેટરી પછી હાઇડ્રોજન છેલ્લી પસંદગી છે; 350-700 bar પર કે −253 °C પર સંગ્રહ ઊર્જા ખર્ચે; હાઇડ્રોજન "
        "પોલાદને ભુરભુરું કરે અને નાના છિદ્રમાંથી લીક થાય; અને તેની જ્યોત લગભગ અદૃશ્ય છે, તેથી લીક શોધ સુરક્ષાનો "
        "પ્રશ્ન છે. મહાસાગર ઊર્જાની વિરુદ્ધ સમસ્યા છે - વિશાળ પણ પાતળું સંસાધન, કાટ લગાડતા તોફાની વાતાવરણમાં "
        "અને ગ્રિડથી દૂર.")]),
    (T("A village of 400 homes needs 250 kWh a day. Design a solar-wind hybrid and justify it.",
       "400 ઘરવાળા ગામને દિવસે 250 kWh જોઈએ. સૌર-પવન સંકર પ્રણાલી રચો અને તેનું સમર્થન કરો."), 5,
     [P("Load: 250 kWh a day is about 91,000 kWh a year, an average of 10.4 kW and a peak of perhaps "
        "40 kW. Solar alone at 4.6 peak sun hours and a performance ratio of 0.80 needs "
        "250 / (4.6 × 0.80) = 68 kWp; but solar makes nothing from 6 p.m. to 6 a.m., when village load "
        "is at its evening peak. Wind alone at a 25 % capacity factor needs 250 / (24 × 0.25) = 42 kW, "
        "but a calm week would leave the village dark.",
        "ભાર: દિવસે 250 kWh એટલે વર્ષે લગભગ 91,000 kWh, સરેરાશ 10.4 kW અને ટોચ લગભગ 40 kW. ફક્ત સૌર, "
        "4.6 પીક સન અવર્સ અને 0.80 કાર્યદક્ષતા ગુણોત્તરે, 250 / (4.6 × 0.80) = 68 kWp માંગે; પણ સૌર સાંજે 6 થી "
        "સવારે 6 સુધી કંઈ બનાવતું નથી, જ્યારે ગામનો ભાર સાંજે ટોચે હોય. ફક્ત પવન 25 % ક્ષમતા અવયવે "
        "250 / (24 × 0.25) = 42 kW માંગે, પણ શાંત અઠવાડિયું ગામને અંધારું રાખે."),
      P("Hybrid design: 45 kWp solar (about 250 m² of roof and shed), a 20 kW wind turbine on a 30 m "
        "mast at the pond bund, a 100 kWh lithium battery for the evening peak, a 30 kVA inverter and "
        "a diesel generator of 40 kVA only for the monsoon emergency. Solar then gives about "
        "45 × 4.6 × 0.8 = 166 kWh a day and wind about 20 × 24 × 0.25 = 120 kWh, so the two together "
        "give 286 kWh against a 250 kWh need, a margin of 14 % for bad weather.",
        "સંકર રચના: 45 kWp સૌર (લગભગ 250 m² છત અને શેડ), તળાવના પાળા પર 30 m થાંભલે 20 kW પવન ટર્બાઇન, "
        "સાંજની ટોચ માટે 100 kWh લિથિયમ બેટરી, 30 kVA ઇન્વર્ટર અને ફક્ત ચોમાસાની કટોકટી માટે 40 kVA ડીઝલ "
        "જનરેટર. પછી સૌર દિવસે લગભગ 45 × 4.6 × 0.8 = 166 kWh અને પવન લગભગ 20 × 24 × 0.25 = 120 kWh આપે, "
        "તેથી બંને ભેગા 250 kWhની જરૂર સામે 286 kWh આપે, ખરાબ હવામાન માટે 14 % માર્જિન."),
      P("Justification: the two resources are anti-correlated. In Gujarat the monsoon months have "
        "cloud and little sun but strong wind, while winter has clear sun and lighter wind, so the "
        "hybrid needs a smaller battery than either alone and the battery is cycled less, which "
        "doubles its life. Sharing one inverter, one controller and one maintenance team cuts the "
        "cost per kWh. The design also matches the load curve - solar carries the day load and pumps "
        "water, wind and the battery carry the evening.",
        "સમર્થન: બંને સંસાધનો વિરોધી સહસંબંધ ધરાવે. ગુજરાતમાં ચોમાસાના મહિનામાં વાદળ અને ઓછો તડકો પણ તાકાતવાન "
        "પવન હોય, જ્યારે શિયાળામાં સ્વચ્છ તડકો અને હળવો પવન, તેથી સંકર પ્રણાલીને એકલા કોઈ પણ કરતાં નાની બેટરી "
        "જોઈએ અને બેટરી ઓછી ચક્રાવે, જે તેનું આયુષ્ય બમણું કરે. એક ઇન્વર્ટર, એક નિયંત્રક અને એક જાળવણી ટીમ "
        "વહેંચવાથી પ્રતિ kWh ખર્ચ ઘટે. રચના ભાર વણકરને પણ મળે - સૌર દિવસનો ભાર અને પાણી ઉપાડે, પવન અને બેટરી "
        "સાંજ સંભાળે.")]),
]

EXAM = [{"q": q, "marks": m} for q, m, _parts in _PRACTICE]
PRACTICE_ANSWERS = [_join(parts) for _q, _m, parts in _PRACTICE]
LESSON_COUNT = sum(len(s["items"]) for s in NOTES)
