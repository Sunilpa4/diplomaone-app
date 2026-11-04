"""DI02000051 Environmental Sustainability - Unit 4: Climate Change: Science and Solutions.

GTU 4.1-4.4, 6 h, 20 %, 14 marks, CO4. Every text node carries English and Gujarati.
"""
from content_DI02000051_u1_notes import T, P, H4, UL, OL, TB, card, num, _join

SOURCES = [
    T("GTU DI02000051 Environmental Sustainability syllabus (uploaded PDF, w.e.f. 2024-25)",
      "GTU DI02000051 પર્યાવરણીય ટકાઉપણું સિલેબસ (અપલોડ કરેલ PDF, 2024-25થી અમલમાં)"),
    T("IPCC Sixth Assessment Report, Working Group I (physical science) and Working Group II (impacts)",
      "IPCC છઠ્ઠો આકલન અહેવાલ, કાર્યગણ I (ભૌતિક વિજ્ઞાન) અને કાર્યગણ II (અસરો)"),
    T("IPCC AR6 Synthesis Report, Summary for Policymakers, 2023",
      "IPCC AR6 સંકલન અહેવાલ, નીતિ ઘડવૈયાઓ માટે સારાંશ, 2023"),
    T("India's Third National Communication and Biennial Update Reports to the UNFCCC (MoEFCC)",
      "UNFCCCને ભારતનો ત્રીજો રાષ્ટ્રીય સંદેશ અને દ્વિવાર્ષિક અદ્યતન અહેવાલ (MoEFCC)"),
    T("WMO State of the Global Climate and the India Meteorological Department climate statements",
      "WMO વૈશ્વિક જળવાયુની સ્થિતિ અને ભારતીય હવામાન વિભાગના જળવાયુ નિવેદનો"),
]

NOTES = [
    {"title": T("1. The Climate System and the Greenhouse Effect",
                "1. જળવાયુ પ્રણાલી અને હરિતગૃહ પ્રભાવ"),
     "items": [
         card(T("4.1 The earth's climate system and the greenhouse effect",
                "4.1 પૃથ્વીની જળવાયુ પ્રણાલી અને હરિતગૃહ પ્રભાવ"),
              [H4("Five parts of one system", "એક પ્રણાલીના પાંચ ભાગ"),
               P("The climate system has five interacting parts: the <b>atmosphere</b>, the "
                 "<b>hydrosphere</b> (oceans, rivers, ice), the <b>cryosphere</b> (glaciers, ice sheets, "
                 "sea ice, permafrost), the <b>lithosphere</b> (soil and rock) and the <b>biosphere</b> "
                 "(plants, animals, microbes). Weather is what one of them does in a day; climate is "
                 "the average and the variability of all five over thirty years or more. Energy comes "
                 "in from the sun and leaves as infrared radiation, and the balance between the two "
                 "sets the temperature.",
                 "જળવાયુ પ્રણાલીમાં પાંચ પરસ્પર જોડાયેલા ભાગ છે: <b>વાતાવરણ</b>, <b>જળગોળ</b> (મહાસાગર, નદી, "
                 "બરફ), <b>હિમગોળ</b> (હિમનદી, બરફનાં પડ, દરિયાઈ બરફ, કાયમી ઠંડું જમીન), <b>શિલાગોળ</b> (જમીન "
                 "અને ખડક) અને <b>જૈવગોળ</b> (છોડ, પ્રાણી, સૂક્ષ્મજીવ). હવામાન એ એક દિવસમાં તેમાંથી એક શું કરે તે છે; "
                 "જળવાયુ એ ત્રીસ કે વધુ વર્ષની બધાની સરેરાશ અને બદલાવ છે. ઊર્જા સૂર્યથી આવે અને ઇન્ફ્રારેડ "
                 "કિરણો તરીકે નીકળે, અને બંને વચ્ચેનું સંતુલન તાપમાન નક્કી કરે."),
               H4("The natural greenhouse effect", "કુદરતી હરિતગૃહ પ્રભાવ"),
               P("Of the sunlight reaching the top of the atmosphere, about 30 % is reflected by "
                 "clouds, ice and deserts - that reflectivity is the <b>albedo</b> - and 70 % is "
                 "absorbed by the surface and the atmosphere. The warm surface radiates that energy "
                 "back as infrared light, and the gases that have "
                 "more than two atoms per molecule - water vapour, carbon dioxide, methane, nitrous "
                 "oxide, ozone - absorb part of it and re-emit half downwards. That back radiation "
                 "keeps the surface at about 15 °C instead of −18 °C, so the natural greenhouse effect "
                 "is what makes life possible; the problem is the extra effect we are adding.",
                 "વાતાવરણની ટોચે પહોંચતા સૂર્યપ્રકાશમાંથી લગભગ 30 % વાદળ, બરફ અને રણ પરાવર્તિત કરે - તે "
                 "પરાવર્તકતા જ <b>આલ્બેડો</b> છે - અને 70 % સપાટી તથા વાતાવરણ શોષે. ગરમ સપાટી તે ઊર્જા "
                 "ઇન્ફ્રારેડ પ્રકાશ તરીકે પાછી ફેંકે અને પ્રતિ "
                 "અણુ બે કરતાં વધુ પરમાણુ ધરાવતા વાયુ - પાણીની વરાળ, કાર્બન ડાયોક્સાઇડ, મિથેન, નાઇટ્રસ "
                 "ઓક્સાઇડ, ઓઝોન - તેનો ભાગ શોષી અડધો નીચે ફેંકે. તે પરાવર્તિત કિરણોત્સર્ગ સપાટીને −18 °Cને "
                 "બદલે લગભગ 15 °C રાખે, તેથી કુદરતી હરિતગૃહ પ્રભાવ જીવન શક્ય બનાવે; સમસ્યા આપણે ઉમેરતો "
                 "વધારાનો પ્રભાવ છે."),
               H4("Forcing, feedback, sensitivity", "બળ, પ્રતિસંદર્શ અને સંવેદનશીલતા"),
               TB([T("Term", "શબ્દ"), T("Meaning", "અર્થ"), T("Example", "ઉદાહરણ")],
                  [[T("radiative forcing", "કિરણોત્સર્ગી બળ"), T("change in energy balance, W/m², from a cause", "કારણથી ઊર્જા સંતુલનમાં ફેરફાર, W/m²"), T("CO₂ at 420 ppm gives about +2.2 W/m²", "420 ppm CO₂ લગભગ +2.2 W/m² આપે")],
                   [T("positive feedback", "ધન પ્રતિસંદર્શ"), T("amplifies the first change", "પ્રથમ ફેરફારને વધારે"), T("less ice means less reflection, so more warming", "ઓછો બરફ એટલે ઓછું પરાવર્તન, તેથી વધુ ગરમી")],
                   [T("negative feedback", "ઋણ પ્રતિસંદર્શ"), T("damps the change", "ફેરફારને દબાવે"), T("a warmer surface radiates more energy away", "ગરમ સપાટી વધુ ઊર્જા ફેંકે")],
                   [T("climate sensitivity", "જળવાયુ સંવેદનશીલતા"), T("warming for a doubling of CO₂", "CO₂ બમણું થવા પર ગરમી"), T("1.5-4.5 °C, best estimate 3 °C", "1.5-4.5 °C, શ્રેષ્ઠ અંદાજ 3 °C")]]),
               H4("Worked example", "ઉકેલાયેલ દાખલો"),
               P("Radiative forcing grows with the logarithm of concentration: ΔF = 5.35 ln(C/280). "
                 "Going from 280 ppm before industry to 420 ppm today gives 5.35 × ln(1.5) = 2.17 W/m², "
                 "which with a sensitivity of 0.8 °C per W/m² means about 1.7 °C of eventual warming - "
                 "close to the 1.2 °C already measured, because the ocean has not caught up yet.",
                 "કિરણોત્સર્ગી બળ સાંદ્રતાના લઘુગણક સાથે વધે: ΔF = 5.35 ln(C/280). ઉદ્યોગ પહેલાંના 280 ppmથી "
                 "આજના 420 ppm સુધી જવાય તો 5.35 × ln(1.5) = 2.17 W/m², જે પ્રતિ W/m² 0.8 °C સંવેદનશીલતાએ "
                 "લગભગ 1.7 °C અંતિમ ગરમી દર્શાવે - માપેલા 1.2 °Cની નજીક, કારણ કે મહાસાગર હજી પકડ્યું નથી."),
               H4("Common mistake", "સામાન્ય ભૂલ"),
               P("Saying the greenhouse effect is bad, or blaming the ozone hole. The natural effect is "
                 "essential; the ozone hole is a separate problem of chlorine chemistry in the "
                 "stratosphere, and ozone depletion is not the cause of global warming.",
                 "હરિતગૃહ પ્રભાવ ખરાબ છે તેમ કહેવું, કે ઓઝોન છિદ્રને દોષ દેવો. કુદરતી પ્રભાવ આવશ્યક છે; ઓઝોન "
                 "છિદ્ર સ્ટ્રેટોસ્ફિયરમાં ક્લોરિન રસાયણની અલગ સમસ્યા છે, અને ઓઝોનનો ક્ષય વૈશ્વિક ગરમીનું કારણ "
                 "નથી.")],
              "u4_balance", syllabus_item="4.1"),
         card(T("4.1 Greenhouse gases, their sources and their strength",
                "4.1 હરિતગૃહ વાયુ, તેમના સ્રોત અને તેમની શક્તિ"),
              [H4("The main gases", "મુખ્ય વાયુ"),
               P("Carbon dioxide is the largest single cause, but it is not the only one and not the "
                 "strongest per kilogram. Each gas is compared with CO₂ by its <b>global warming "
                 "potential</b> (GWP) over one hundred years, which folds in how much infrared it "
                 "absorbs and how long it stays in the air. Methane is about 28 times CO₂ and lives "
                 "only twelve years; nitrous oxide is 265 times and lives 120 years; the fluorinated "
                 "gases used in refrigeration are thousands of times stronger.",
                 "કાર્બન ડાયોક્સાઇડ સૌથી મોટું એક કારણ છે, પણ તે એકમાત્ર નથી અને પ્રતિ કિલો સૌથી શક્તિશાળી પણ "
                 "નથી. દરેક વાયુની સરખામણી તેના સો વર્ષના <b>વૈશ્વિક ગરમી સંભાવના</b> (GWP) દ્વારા CO₂ સાથે થાય, "
                 "જે તે કેટલું ઇન્ફ્રારેડ શોષે અને હવામાં કેટલું ટકે તે બંને સમાવે. મિથેન CO₂ કરતાં લગભગ 28 "
                 "ગણું અને ફક્ત બાર વર્ષ ટકે; નાઇટ્રસ ઓક્સાઇડ 265 ગણું અને 120 વર્ષ ટકે; ઠંડકમાં વપરાતા "
                 "ફ્લોરિનવાળા વાયુ હજારો ગણા શક્તિશાળી છે."),
               H4("Sources and shares", "સ્રોત અને હિસ્સો"),
               TB([T("Gas", "વાયુ"), T("GWP, 100 yr", "GWP, 100 વર્ષ"), T("Main sources", "મુખ્ય સ્રોત"), T("Share of warming", "ગરમીમાં હિસ્સો")],
                  [[T("CO₂", "CO₂"), T("1", "1"), T("coal, oil, gas, cement, land clearing", "કોલસો, તેલ, ગેસ, સિમેન્ટ, જમીન સફાઈ"), T("about 64 %", "લગભગ 64 %")],
                   [T("CH₄", "CH₄"), T("28", "28"), T("cattle, rice paddies, landfills, gas leaks", "ઢોર, ડાંગરનાં ખેતર, કચરાભરાવ, ગેસ લીકેજ"), T("about 17 %", "લગભગ 17 %")],
                   [T("N₂O", "N₂O"), T("265", "265"), T("nitrogen fertiliser, manure, industry", "નાઇટ્રોજન ખાતર, છાણ, ઉદ્યોગ"), T("about 6 %", "લગભગ 6 %")],
                   [T("fluorinated gases", "ફ્લોરિનવાળા વાયુ"), T("up to 14,800", "14,800 સુધી"), T("refrigerants, air conditioning, aerosols", "રેફ્રિજરન્ટ, વાતાનુકૂલન, એરોસોલ"), T("about 3 %", "લગભગ 3 %")],
                   [T("water vapour", "પાણીની વરાળ"), T("not counted", "ગણાય નહીં"), T("evaporation, a feedback not a forcing", "બાષ્પીભવન, બળ નહીં પ્રતિસંદર્શ"), T("amplifies the rest", "બાકીનાને વધારે")]]),
               H4("The carbon cycle and the budget", "કાર્બન ચક્ર અને બજેટ"),
               P("Of every tonne of CO₂ released, about 45 % stays in the air, 25 % is taken by the "
                 "ocean and 30 % by land plants. Because the ocean absorbs slowly and acidifies as it "
                 "does, a pulse of CO₂ warms the earth for centuries. The carbon budget - the total "
                 "that can still be emitted for a given temperature - is therefore the honest way to "
                 "plan: about 250 Gt of CO₂ remain for a 1.5 °C chance and about 1,150 Gt for 2 °C, "
                 "against current emissions near 42 Gt a year.",
                 "છૂટતા દરેક ટન CO₂માંથી લગભગ 45 % હવામાં રહે, 25 % મહાસાગર લે અને 30 % જમીનના છોડ. મહાસાગર ધીમે "
                 "શોષે અને શોષતાં અમ્લિક બને, તેથી CO₂નો એક ધક્કો સદીઓ સુધી પૃથ્વીને ગરમ કરે. તેથી કાર્બન બજેટ - "
                 "આપેલા તાપમાન માટે હજી કુલ કેટલું છોડી શકાય - યોજના માટે પ્રામાણિક માર્ગ છે: 1.5 °Cની શક્યતા માટે "
                 "લગભગ 250 Gt CO₂ અને 2 °C માટે લગભગ 1,150 Gt બાકી છે, જ્યારે હાલનું ઉત્સર્જન વર્ષે 42 Gtની "
                 "નજીક છે."),
               H4("Worked example", "ઉકેલાયેલ દાખલો"),
               P("A city of one million people emits 1.2 t of CO₂ per person a year from fuel, plus "
                 "40,000 t of methane from its landfill. In CO₂ equivalent the landfill adds "
                 "40,000 × 28 = 1.12 Mt, almost as much as the fuel - which is why capping and flaring "
                 "a landfill is one of the cheapest climate actions available.",
                 "દસ લાખ વસ્તીનું શહેર ઇંધણમાંથી વર્ષે પ્રતિ વ્યક્તિ 1.2 t CO₂ છોડે, ઉપરાંત તેના કચરાભરાવમાંથી "
                 "40,000 t મિથેન. CO₂ સમમૂલ્યમાં કચરાભરાવ 40,000 × 28 = 1.12 Mt ઉમેરે, લગભગ ઇંધણ જેટલું જ - "
                 "તેથી કચરાભરાવ ઢાંકવો અને ગેસ બાળવો સૌથી સસ્તા જળવાયુ પગલાંમાં છે.")],
              "u4_ghg", syllabus_item="4.1"),
     ]},
    {"title": T("2. Evidence of Climate Change", "2. જળવાયુ પરિવર્તનના પુરાવા"),
     "items": [
         card(T("4.2 Temperature records and how we know the past",
                "4.2 તાપમાનના રેકોર્ડ અને ભૂતકાળ કેવી રીતે જાણીએ"),
              [H4("Two kinds of thermometer", "બે પ્રકારના તાપમાનમાપક"),
               P("<b>Instrumental records</b> start in the 1850s with land stations and, from the 1950s, "
                 "include weather balloons and satellites; after removing urban heat-island effects and "
                 "correcting for station moves, they show about 1.2 °C of warming since pre-industrial "
                 "times, with the last decade the warmest in the record. <b>Proxy records</b> go back "
                 "much further: tree rings, ice cores with trapped air bubbles, corals, lake sediment "
                 "and stalagmites. Ice cores from Antarctica hold air 800,000 years old in which CO₂ "
                 "never exceeded 300 ppm until the twentieth century.",
                 "<b>ઉપકરણ રેકોર્ડ</b> 1850ના દાયકામાં જમીન સ્ટેશનોથી શરૂ થાય અને 1950થી હવામાન ફુગ્ગા તથા "
                 "ઉપગ્રહોનો સમાવેશ કરે; શહેરી ઉષ્મા-ટાપુ અસર દૂર કરી અને સ્ટેશન ખસેડવાનું સુધારીને તે ઉદ્યોગ "
                 "પહેલાંના સમયથી લગભગ 1.2 °C ગરમી દર્શાવે, અને છેલ્લો દાયકો રેકોર્ડમાં સૌથી ગરમ છે. "
                 "<b>પરોક્ષ રેકોર્ડ</b> ઘણો પાછળ જાય: વૃક્ષના વલય, ફસાયેલા હવાના પરપોટા સાથે બરફના નમૂના, "
                 "પરવાળા, તળાવનો કાંપ અને સ્ટેલેગ્માઇટ. એન્ટાર્કટિકાના બરફના નમૂનામાં 8,00,000 વર્ષ જૂની હવા "
                 "છે જેમાં વીસમી સદી પહેલાં CO₂ કદી 300 ppm વટાવ્યું નથી."),
               H4("What the curve looks like", "વણકર કેવી દેખાય"),
               TB([T("Period", "સમયગાળો"), T("Change", "ફેરફાર"), T("What caused it", "કારણ")],
                  [[T("last 800,000 years", "છેલ્લા 8,00,000 વર્ષ"), T("ice ages with CO₂ 180-280 ppm", "CO₂ 180-280 ppm સાથે હિમયુગ"), T("orbital cycles, the Milankovitch rhythm", "કક્ષીય ચક્ર, મિલાનકોવિચ લય")],
                   [T("1850-1900", "1850-1900"), T("the pre-industrial baseline", "ઉદ્યોગ પહેલાંનો આધાર"), T("almost steady near 280 ppm", "280 ppm નજીક લગભગ સ્થિર")],
                   [T("1901-2023", "1901-2023"), T("+1.2 °C, faster since 1970", "+1.2 °C, 1970થી ઝડપી"), T("fossil fuel burning, land use", "અશ્મી ઇંધણનું દહન, જમીન ઉપયોગ")],
                   [T("1979 to now", "1979થી આજ સુધી"), T("Arctic sea ice down about 40 % in September", "સપ્ટેમ્બરમાં આર્કટિક દરિયાઈ બરફ લગભગ 40 % ઘટ્યો"), T("polar amplification", "ધ્રુવીય વૃદ્ધિ")]]),
               H4("Fingerprints", "અંગૂઠાના નિશાન"),
               P("A warming that came from the sun would heat the whole atmosphere evenly and warm the "
                 "stratosphere too. What is measured instead is a warming troposphere and a cooling "
                 "stratosphere, nights warming faster than days, winters faster than summers, and the "
                 "lower atmosphere warming while the upper atmosphere cools. Each of these is a "
                 "fingerprint of greenhouse gases rather than of a brighter sun, and each is why the "
                 "scientific case is described as settled.",
                 "સૂર્યથી આવતી ગરમી આખા વાતાવરણને સરખું ગરમ કરે અને સ્ટ્રેટોસ્ફિયરને પણ ગરમ કરે. તેના બદલે જે "
                 "માપાય છે તે છે ગરમ થતું ટ્રોપોસ્ફિયર અને ઠંડું થતું સ્ટ્રેટોસ્ફિયર, દિવસ કરતાં રાત વધુ "
                 "ગરમ, ઉનાળા કરતાં શિયાળો વધુ ગરમ, અને નીચું વાતાવરણ ગરમ થાય જ્યારે ઉપરનું ઠંડું થાય. આ દરેક "
                 "તેજસ્વી સૂર્યને બદલે હરિતગૃહ વાયુનું અંગૂઠાનું નિશાન છે, અને તેથી જ વૈજ્ઞાનિક પુરાવાને નિર્ણિત "
                 "કહેવાય છે."),
               H4("Common mistake", "સામાન્ય ભૂલ"),
               P("Pointing at one cold winter as proof that warming has stopped. Climate is a "
                 "thirty-year average; a single season is weather. The test is the trend in a running "
                 "average, not the last cold morning.",
                 "એક ઠંડા શિયાળાને ગરમી થંભી ગઈ હોવાના પુરાવા તરીકે બતાવવું. જળવાયુ ત્રીસ વર્ષની સરેરાશ છે; "
                 "એક ઋતુ હવામાન છે. કસોટી ચાલતી સરેરાશનો ટ્રેન્ડ છે, છેલ્લી ઠંડી સવાર નહીં.")],
              "u4_temp", syllabus_item="4.2"),
         card(T("4.2 Melting ice, rising seas and shifting rain",
                "4.2 પીગળતો બરફ, વધતો દરિયો અને બદલાતો વરસાદ"),
              [H4("Where the water comes from", "પાણી ક્યાંથી આવે"),
               P("Sea level rises for three reasons. <b>Thermal expansion</b>: water expands as it warms, "
                 "which has given about 1.4 mm a year. <b>Glacier and ice-cap melt</b> in the Himalayas, "
                 "Alps and Andes adds about 0.8 mm. <b>Ice sheets</b> in Greenland and West Antarctica "
                 "add about 0.8 mm and are the largest long-term risk, because they hold enough water "
                 "to raise the sea by 65 m. Melting sea ice raises nothing - it is already floating - "
                 "but it removes the bright surface that reflected sunlight.",
                 "દરિયાની સપાટી ત્રણ કારણે વધે. <b>ઉષ્મીય વિસ્તરણ</b>: પાણી ગરમ થતાં ફેલાય, જે વર્ષે લગભગ "
                 "1.4 mm આપ્યું છે. હિમાલય, આલ્પ્સ અને એન્ડીઝમાં <b>હિમનદી અને બરફનાં પડનું પીગળવું</b> લગભગ "
                 "0.8 mm ઉમેરે. ગ્રીનલેન્ડ અને પશ્ચિમ એન્ટાર્કટિકાનાં <b>બરફનાં પડ</b> લગભગ 0.8 mm ઉમેરે અને "
                 "સૌથી મોટું લાંબાગાળાનું જોખમ છે, કારણ કે તેમાં દરિયો 65 m વધારવા પૂરતું પાણી છે. દરિયાઈ બરફ "
                 "પીગળવાથી કંઈ વધતું નથી - તે તો પહેલેથી તરે છે - પણ સૂર્યપ્રકાશ પરાવર્તિત કરતી તેજસ્વી સપાટી "
                 "દૂર થાય."),
               H4("The numbers", "આંકડા"),
               TB([T("Indicator", "સૂચક"), T("Measured change", "માપેલો ફેરફાર"), T("Why it matters", "કેમ મહત્ત્વનું")],
                  [[T("global mean sea level", "વૈશ્વિક સરેરાશ દરિયા સપાટી"), T("+20 cm since 1900, +4.5 mm a year now", "1900થી +20 cm, હવે વર્ષે +4.5 mm"), T("coastal flooding, salt water in wells", "દરિયાકાંઠાનું પૂર, કૂવામાં ખારું પાણી")],
                   [T("Arctic sea ice", "આર્કટિક દરિયાઈ બરફ"), T("September extent down about 13 % a decade", "સપ્ટેમ્બરનો વિસ્તાર દાયકે લગભગ 13 % ઘટ્યો"), T("less reflection, more warming", "ઓછું પરાવર્તન, વધુ ગરમી")],
                   [T("Himalayan glaciers", "હિમાલયની હિમનદી"), T("losing mass faster since 2000", "2000થી ઝડપથી દળ ગુમાવે"), T("Ganga and Indus flow in the dry season", "શુષ્ક ઋતુમાં ગંગા અને સિંધુનો પ્રવાહ")],
                   [T("monsoon rainfall", "ચોમાસાનો વરસાદ"), T("more in fewer, heavier spells", "ઓછી પણ ભારે ઝાપટામાં વધુ"), T("flash floods and longer dry spells", "ઝડપી પૂર અને લાંબા સૂકા સમય")],
                   [T("snow cover", "બરફનું આવરણ"), T("spring snow melting 1-2 weeks earlier", "વસંતનો બરફ 1-2 અઠવાડિયું વહેલો પીગળે"), T("water arrives before the crop needs it", "પાકને જરૂર પડે તે પહેલાં પાણી આવે")]]),
               H4("India in particular", "ખાસ કરીને ભારત"),
               P("India has 7,500 km of coastline and about 40 % of its people live within 100 km of the "
                 "sea, so a 0.5 m rise threatens Mumbai, Surat, Kochi and Chennai through tidal "
                 "flooding, saline intrusion into the coastal aquifer and loss of beaches. The Sundarbans, "
                 "the Delta and the Lakshadweep atolls face the same pressure with a smaller margin.",
                 "ભારતનો 7,500 km દરિયાકિનારો છે અને લગભગ 40 % લોકો દરિયાથી 100 kmમાં રહે છે, તેથી 0.5 m વધારો "
                 "ભરતીના પૂર, કિનારાના જળસ્તરમાં ખારા પાણીના ઘૂસણ અને દરિયાકિનારા ગુમાવીને મુંબઈ, સુરત, કોચી "
                 "અને ચેન્નાઈને ધમકાવે. સુંદરબન, ડેલ્ટા અને લક્ષદ્વીપના પરવાળા ટાપુઓ નાના માર્જિન સાથે એ જ "
                 "દબાણ સહે છે.")],
              "u4_sea", syllabus_item="4.2"),
         card(T("4.2 Extreme weather and how it is attributed",
                "4.2 આત્યંતિક હવામાન અને તેનું કારણ નિર્ધારણ"),
              [H4("Why extremes change first", "આત્યંતિક ઘટનાઓ પહેલાં કેમ બદલાય"),
               P("A small shift in the average moves the tails of the distribution a long way. If the "
                 "mean temperature rises by 1 °C, the chance of a heat wave that used to happen once "
                 "in fifty years may rise three to ten times, and a record that was a one-in-a-thousand "
                 "event becomes a one-in-fifty. Warmer air also holds about 7 % more water vapour for "
                 "every degree, so a storm that does form can rain harder - the same total monsoon rain "
                 "arriving in fewer, more violent spells.",
                 "સરેરાશમાં નાનું ખસેડું વિતરણની પૂંછડીઓને ઘણે દૂર ખસેડે. સરેરાશ તાપમાન 1 °C વધે તો પહેલાં "
                 "પચાસ વર્ષે એક વાર આવતી ગરમીની લહેરની શક્યતા ત્રણથી દસ ગણી વધે, અને હજારમાં એક વારની ઘટના "
                 "પચાસમાં એક વાર બને. ગરમ હવા દરેક ડિગ્રીે લગભગ 7 % વધુ પાણીની વરાળ ધરે, તેથી જે તોફાન બને તે વધુ "
                 "ભારે વરસી શકે - એ જ કુલ ચોમાસાનો વરસાદ ઓછી પણ હિંસક ઝાપટામાં આવે."),
               H4("What India records", "ભારત શું નોંધે"),
               TB([T("Event", "ઘટના"), T("Change observed", "જણાયેલો ફેરફાર"), T("Damage route", "નુકસાનનો રસ્તો")],
                  [[T("heat waves", "ગરમીની લહેર"), T("more frequent, longer and hotter since 1980", "1980થી વધુ વારંવાર, લાંબી અને ગરમ"), T("heat stroke, crop failure, power demand", "લૂ લાગવી, પાક નિષ્ફળ, વીજ માંગ")],
                   [T("heavy rainfall", "ભારે વરસાદ"), T("more one-day extremes, fewer rainy days", "એક દિવસની ચરમસીમા વધુ, વરસાદી દિવસ ઓછા"), T("urban flooding, landslides", "શહેરી પૂર, ભૂસ્ખલન")],
                   [T("cyclones", "વાવાઝોડું"), T("stronger, slower and wetter; not clearly more frequent", "તાકાતવાન, ધીમું અને વધુ પલળતું; સંખ્યા સ્પષ્ટ વધી નથી"), T("storm surge, wind damage, rain flooding", "તોફાની ભરતી, પવનનું નુકસાન, વરસાદી પૂર")],
                   [T("drought", "દુષ્કાળ"), T("more frequent in the rabi season, driven by heat", "રવિ ઋતુમાં વધુ વારંવાર, ઉષ્માથી ચાલિત"), T("groundwater fall, migration", "ભૂગર્ભજળ ઘટે, સ્થળાંતર")],
                   [T("sea-level extremes", "દરિયા સપાટીની ચરમસીમા"), T("once-a-century floods now every few years", "સદીમાં એક વારનું પૂર હવે થોડા વર્ષે"), T("coastal cities, ports, aquifers", "કિનારાનાં શહેર, બંદર, જળાશય")]]),
               H4("Attribution science", "કારણ નિર્ધારણ વિજ્ઞાન"),
               P("Attribution does not ask whether a storm was caused by climate change; it asks how "
                 "much likelier or more severe the event became because of it. The method runs "
                 "thousands of simulations of the same world with and without the measured greenhouse "
                 "forcing, and compares the odds. That is how scientists can now say a particular heat "
                 "wave was thirty times more likely, or that a rainfall total was 10 % heavier, within "
                 "days of the event - and why a single flood is still described as weather, not proof.",
                 "કારણ નિર્ધારણ એ પૂછતું નથી કે તોફાન જળવાયુ પરિવર્તનથી થયું કે નહીં; તે પૂછે છે કે તેના કારણે "
                 "ઘટના કેટલી વધુ શક્ય કે વધુ તીવ્ર બની. આ રીત માપેલા હરિતગૃહ બળ સાથે અને વગર એ જ દુનિયાના "
                 "હજારો અનુકરણ ચલાવી શક્યતા સરખાવે. તેથી વૈજ્ઞાનિકો હવે ઘટનાના થોડા દિવસોમાં કહી શકે કે અમુક "
                 "ગરમીની લહેર ત્રીસ ગણી વધુ શક્ય હતી, કે વરસાદ 10 % વધુ ભારે હતો - અને તેથી જ એક પૂરને હજી "
                 "હવામાન કહેવાય, પુરાવો નહીં."),
               H4("Common mistake", "સામાન્ય ભૂલ"),
               P("Saying that climate change caused a particular flood, or that no single event can be "
                 "linked to it. The correct statement is about probability and severity: the event "
                 "became more likely or more intense because of warming, while its timing and place "
                 "were weather.",
                 "ચોક્કસ પૂર જળવાયુ પરિવર્તનથી થયું છે તેમ કહેવું, કે કોઈ એક ઘટના સાથે તેને જોડી જ ન શકાય તેમ "
                 "કહેવું. સાચું વિધાન શક્યતા અને તીવ્રતા વિશે છે: ગરમીને કારણે ઘટના વધુ શક્ય કે વધુ તીવ્ર બની, "
                 "જ્યારે તેનો સમય અને સ્થળ હવામાન હતા.")],
              syllabus_item="4.2"),
     ]},
    {"title": T("3. Impacts of Climate Change", "3. જળવાયુ પરિવર્તનની અસરો"),
     "items": [
         card(T("4.3 Biodiversity loss, ocean acidification and desertification",
                "4.3 જૈવવિવિધતાનો ક્ષય, મહાસાગરનું અમ્લીકરણ અને મરુસ્થલીકરણ"),
              [H4("Species move uphill and poleward", "જાતિઓ ઊંચાઈ અને ધ્રુવ તરફ ખસે"),
               P("Every species lives inside a range of temperature and rainfall. When the range shifts, "
                 "a mobile animal or a wind-blown seed can follow it; a coral, a mountain frog or a tree "
                 "that takes fifty years to mature cannot. The measured result is that about half of "
                 "studied species have already moved 10-20 km poleward or 10 m uphill per decade, and "
                 "the IPCC finds that 1.5 °C puts 9 % of species at high extinction risk, while 3 °C "
                 "raises that to 29 %. Warming also breaks <b>timing</b>: birds arrive after the insects "
                 "they eat have already hatched, a mismatch called a phenological shift.",
                 "દરેક જાતિ તાપમાન અને વરસાદની એક શ્રેણીમાં જીવે. શ્રેણી ખસે ત્યારે ચલ-વચલું પ્રાણી કે પવનમાં "
                 "ઊડતું બીજ તેની પાછળ જઈ શકે; પરવાળું, પર્વતીય દેડકું કે પચાસ વર્ષમાં પુખ્ત થતું ઝાડ નહીં. માપેલું "
                 "પરિણામ એ છે કે અભ્યાસ કરેલી લગભગ અડધી જાતિઓ દાયકે 10-20 km ધ્રુવ તરફ કે 10 m ઊંચાઈ તરફ "
                 "ખસી છે, અને IPCC ને લાગે છે કે 1.5 °C નવ જાતિઓમાંથી એકને લુપ્ત થવાનું ઊંચું જોખમ આપે, જ્યારે "
                 "3 °C તેને 29 % કરે. ગરમી <b>સમય</b> પણ તોડે: પક્ષીઓ પોતાના ખોરાકના જીવડાં મોસમ પૂરી કર્યા પછી "
                 "આવે, જેને ફિનોલોજિકલ ખસેડું કહે છે."),
               H4("Ocean acidification", "મહાસાગરનું અમ્લીકરણ"),
               P("The ocean has absorbed about a quarter of all the CO₂ people have released. That CO₂ "
                 "forms carbonic acid, and the pH of the surface ocean has fallen from 8.2 to 8.1 - a "
                 "26 % rise in hydrogen ions, because pH is a logarithmic scale. Corals, oysters, "
                 "mussels and some plankton build shells from calcium carbonate, and they build them "
                 "more slowly as the water becomes less alkaline; coral reefs, which shelter a quarter "
                 "of marine species and protect coasts, bleach in hot years and then fail to rebuild. "
                 "This is the second CO₂ problem and it cannot be fixed by cooling alone.",
                 "મહાસાગરે લોકોએ છોડેલા આખા CO₂માંથી લગભગ ચોથા ભાગનું શોષણ કર્યું. તે CO₂ કાર્બોનિક એસિડ બનાવે "
                 "અને સપાટીના મહાસાગરનો pH 8.2થી 8.1 થયો - હાઇડ્રોજન આયનમાં 26 % વધારો, કારણ કે pH લઘુગણક "
                 "માપક્રમ છે. પરવાળા, ઓઇસ્ટર, શંખ અને કેટલાક પ્લવક કેલ્શિયમ કાર્બોનેટમાંથી શેલ બનાવે અને પાણી "
                 "ઓછું આલ્કલાઇન થાય તેમ ધીમે બનાવે; પરવાળાની ભરતી, જે ચોથા ભાગની દરિયાઈ જાતિઓને આશ્રય આપે "
                 "અને કિનારા બચાવે, ગરમ વર્ષોમાં ધવલિત થઈ પછી ફરી ન બની શકે. આ બીજી CO₂ સમસ્યા છે અને ફક્ત "
                 "ઠંડકથી ઠીક ન થાય."),
               H4("Desertification", "મરુસ્થલીકરણ"),
               P("<b>Desertification</b> is land degradation in dry regions, not the advance of sand "
                 "dunes. It comes from overgrazing, deforestation, poor irrigation, salt build-up and "
                 "more frequent drought, and climate change is an amplifier: higher evaporation in "
                 "already dry soil turns a dry spell into a failed season. About 40 % of India's land is "
                 "degraded to some degree - in Rajasthan, Gujarat's Kutch, the Deccan plateau - and each "
                 "hectare lost pushes a family to a city.",
                 "<b>મરુસ્થલીકરણ</b> એ સૂકા વિસ્તારોમાં જમીનનો ક્ષય છે, રેતીના ટેકરા આગળ વધવા નહીં. તે વધુ "
                 "ચરાવાણ, વનનાબૂદી, નબળી સિંચાઈ, ક્ષારનો સંગ્રહ અને વધુ વારંવારના દુષ્કાળમાંથી આવે છે, અને "
                 "જળવાયુ પરિવર્તન તેને વધારે: પહેલેથી સૂકી જમીનમાં વધુ બાષ્પીભવન સૂકા સમયને નિષ્ફળ ઋતુમાં "
                 "ફેરવે. ભારતની લગભગ 40 % જમીન અમુક અંશે ક્ષીણ છે - રાજસ્થાન, ગુજરાતનું કચ્છ, દક્કનનો ઉચ્ચપ્રદેશ "
                 "- અને ગુમાવેલું દરેક હેક્ટર એક કુટુંબને શહેર તરફ ધકેલે.")],
              "u4_impacts", syllabus_item="4.3"),
         card(T("4.3 Social and economic impacts", "4.3 સામાજિક અને આર્થિક અસરો"),
              [H4("Why impact is risk, not just temperature", "અસર તાપમાન નહીં, જોખમ કેમ છે"),
               P("The IPCC frames impact as risk from three things together: <b>hazard</b> (the heat, "
                 "flood or drought), <b>exposure</b> (how many people or fields are in its path) and "
                 "<b>vulnerability</b> (how little capacity they have to cope). A heat wave of 45 °C is a "
                 "hazard everywhere; it kills in a city where the poorest live under tin roofs and has "
                 "little effect in a city with parks, shutters, water and hospitals. That is why the "
                 "same warming is not the same loss everywhere, and why adaptation is not an optional "
                 "extra.",
                 "IPCC અસરને ત્રણ ભેગાં મળીને જોખમ તરીકે ગણે છે: <b>જોખમી ઘટના</b> (ગરમી, પૂર કે દુષ્કાળ), "
                 "<b>સંપર્ક</b> (કેટલા લોકો કે ખેતર તેના રસ્તામાં છે) અને <b>સંવેદનશીલતા</b> (તેમની સામે લડવાની "
                 "ક્ષમતા કેટલી ઓછી છે). 45 °Cની ગરમી દરેક જગ્યાએ જોખમ છે; તે શહેરમાં મારે જ્યાં સૌથી ગરીબ લોકો "
                 "પતરાની છત નીચે રહે, અને બગીચા, બારી, પાણી તથા હોસ્પિટલવાળા શહેરમાં થોડી અસર કરે. તેથી જ એક જ "
                 "ગરમી દરેક જગ્યાએ એક જ નુકસાન નથી, અને તેથી જ અનુકૂલન વૈકલ્પિક વધારો નથી."),
               H4("Sector by sector", "ક્ષેત્ર પ્રમાણે"),
               TB([T("Sector", "ક્ષેત્ર"), T("Impact", "અસર"), T("Indian evidence", "ભારતીય પુરાવો")],
                  [[T("agriculture", "ખેતી"), T("wheat and rice yield fall per degree; pests spread", "દરેક ડિગ્રીે ઘઉં અને ચોખાનું ઉત્પાદન ઘટે; જીવાત ફેલાય"), T("about 6 % fall in wheat for 1 °C", "1 °C માટે ઘઉંમાં લગભગ 6 % ઘટાડો")],
                   [T("water", "પાણી"), T("less snow storage, more evaporation, deeper wells", "ઓછો બરફ સંગ્રહ, વધુ બાષ્પીભવન, ઊંડા કૂવા"), T("groundwater falling in the north-west", "વાયવ્યમાં ભૂગર્ભજળ ઘટે")],
                   [T("health", "આરોગ્ય"), T("heat deaths, dengue and malaria spreading", "ગરમીથી મોત, ડેન્ગ્યુ અને મલેરિયા ફેલાય"), T("heat waves kill thousands since 2010", "2010થી ગરમીની લહેરોએ હજારોને માર્યા")],
                   [T("labour productivity", "શ્રમ ઉત્પાદકતા"), T("outdoor work impossible in the afternoon", "બપોરે બહારનું કામ અશક્ય"), T("construction and farm wages lost", "બાંધકામ અને ખેત મજૂરી ગુમાવાય")],
                   [T("migration", "સ્થળાંતર"), T("drought and coastal erosion move families", "દુષ્કાળ અને કિનારાનો ક્ષય કુટુંબો ખસેડે"), T("seasonal and permanent movement to cities", "શહેરો તરફ મોસમી અને કાયમી ખસેડું")],
                   [T("infrastructure", "માળખું"), T("rails buckle, roads flood, power fails", "પાટા વળે, રસ્તા પૂરમાં, વીજળી જાય"), T("Mumbai 2005, Chennai 2015, Kerala 2018", "મુંબઈ 2005, ચેન્નાઈ 2015, કેરળ 2018")]]),
               H4("The social justice point", "સામાજિક ન્યાયનો મુદ્દો"),
               P("The countries that emitted least are hit first and hardest, because they depend on "
                 "rain-fed farming and cannot pay for air conditioning, sea walls or insurance. Within "
                 "India the same pattern repeats: a landless labourer in Kutch and a farmer in Bihar "
                 "carry a cost that a car-owning household in a serviced city does not. That is the "
                 "meaning of <b>climate justice</b> and the reason the UNFCCC speaks of common but "
                 "differentiated responsibilities.",
                 "જેણે સૌથી ઓછું ઉત્સર્જન કર્યું તે પહેલાં અને સૌથી વધુ માર ખાય, કારણ કે તે વરસાદ આધારિત "
                 "ખેતી પર નિર્ભર છે અને વાતાનુકૂલન, દરિયાની દીવાલ કે વીમો પરવડી શકતું નથી. ભારતમાં પણ એ જ "
                 "નમૂનો પુનરાવર્તિત થાય: કચ્છનો ભૂમિહીન મજૂર અને બિહારનો ખેડૂત એવો ખર્ચ ઉઠાવે જે સેવાવાળા "
                 "શહેરના કારવાળા કુટુંબને નડતો નથી. આ <b>જળવાયુ ન્યાય</b>નો અર્થ છે અને UNFCCC સમાન પણ "
                 "ભિન્ન જવાબદારીઓની વાત કેમ કરે છે તેનું કારણ.")],
              syllabus_item="4.3"),
     ]},
    {"title": T("4. Climate Change Mitigation", "4. જળવાયુ પરિવર્તન શમન"),
     "items": [
         card(T("4.4 Energy efficiency and the renewable transition",
                "4.4 ઊર્જા કાર્યક્ષમતા અને પુનઃપ્રાપ્ય સંક્રમણ"),
              [H4("Two levers, one ladder", "બે લિવર, એક સોપાન"),
               P("Mitigation means cutting the emissions that cause the warming, and it is done in a "
                 "fixed order of cheapness. <b>Efficiency</b> comes first because a unit of energy not "
                 "used costs nothing and emits nothing: an LED lamp, an efficient motor, a well "
                 "insulated roof, a compressor with a variable drive. Then <b>electrification</b> of "
                 "heat and transport, because an electric motor and a heat pump use energy three times "
                 "better than a boiler or a petrol engine. Then <b>clean supply</b> - solar, wind, "
                 "hydro, nuclear - to feed that larger electricity demand.",
                 "શમન એટલે ગરમી કરતું ઉત્સર્જન ઘટાડવું, અને તે સસ્તાઈના નિશ્ચિત ક્રમમાં થાય. <b>કાર્યક્ષમતા</b> "
                 "પહેલાં આવે કારણ કે ન વપરાયેલો ઊર્જા એકમ કંઈ ખર્ચતો નથી અને કંઈ છોડતો નથી: LED દીવો, "
                 "કાર્યક્ષમ મોટર, સારી રીતે ઇન્સ્યુલેટેડ છત, ચલ ડ્રાઇવવાળો કોમ્પ્રેસર. પછી ઉષ્મા અને "
                 "વાહનવ્યવહારનું <b>વીજીકરણ</b>, કારણ કે વીજ મોટર અને ઉષ્મા પંપ બોઇલર કે પેટ્રોલ એન્જિન કરતાં "
                 "ઊર્જા ત્રણ ગણી સારી વાપરે. પછી તે વધેલી વીજ માંગ પૂરી કરવા <b>સ્વચ્છ પુરવઠો</b> - સૌર, પવન, "
                 "જળ, ન્યુક્લિયર."),
               H4("Where the emissions are", "ઉત્સર્જન ક્યાં છે"),
               TB([T("Sector", "ક્ષેત્ર"), T("Share of global CO₂", "વૈશ્વિક CO₂માં હિસ્સો"), T("First cut to make", "પહેલો ઘટાડો")],
                  [[T("electricity and heat", "વીજળી અને ઉષ્મા"), T("about 34 %", "લગભગ 34 %"), T("solar, wind, storage instead of coal", "કોલસાને બદલે સૌર, પવન, સંગ્રહ")],
                   [T("industry", "ઉદ્યોગ"), T("about 24 %", "લગભગ 24 %"), T("efficient furnaces, scrap steel, green hydrogen", "કાર્યક્ષમ ભઠ્ઠી, ભંગાર પોલાદ, લીલું હાઇડ્રોજન")],
                   [T("transport", "વાહનવ્યવહાર"), T("about 15 %", "લગભગ 15 %"), T("public transport, rail, electric two and three wheelers", "જાહેર વાહનવ્યવહાર, રેલ, વીજ બે અને ત્રણ પૈડાં")],
                   [T("buildings", "ઇમારત"), T("about 6 %", "લગભગ 6 %"), T("cooling efficiency, shading, rooftop solar", "ઠંડક કાર્યક્ષમતા, છાયો, છત પર સૌર")],
                   [T("agriculture and land", "ખેતી અને જમીન"), T("about 12 % of all gases", "બધા વાયુમાં લગભગ 12 %"), T("less fertiliser loss, less stubble burning", "ઓછી ખાતર ખોટ, ઓછું પરાળ બાળવું")]]),
               H4("Efficiency is the cheapest tonne", "કાર્યક્ષમતા સૌથી સસ્તું ટન"),
               P("A 9 W LED replaces a 60 W incandescent lamp and gives the same light, saving 51 W for "
                 "eight hours a day - about 150 kWh a year per lamp. In a home with ten lamps that is "
                 "1,500 kWh, or roughly 1.1 t of CO₂ at the Indian grid factor, for an investment of a "
                 "few thousand rupees. No power plant, no land and no fuel are needed, which is why "
                 "efficiency is called the first fuel and is counted before any supply is built.",
                 "9 Wનો LED 60 Wના તાપદીપને બદલે એ જ પ્રકાશ આપે અને દિવસે આઠ કલાક 51 W બચાવે - દીવા દીઠ "
                 "વર્ષે લગભગ 150 kWh. દસ દીવાવાળા ઘરમાં તે 1,500 kWh, એટલે ભારતીય ગ્રિડ અવયવે લગભગ 1.1 t CO₂, "
                 "થોડા હજાર રૂપિયાના રોકાણે. કોઈ સ્ટેશન, જમીન કે ઇંધણ જોઈએ નહીં, તેથી કાર્યક્ષમતાને પ્રથમ "
                 "ઇંધણ કહે છે અને કોઈ પુરવઠો બાંધતાં પહેલાં તેને ગણે છે."),
               H4("Worked example", "ઉકેલાયેલ દાખલો"),
               P("An office block cuts its demand from 200 MWh to 150 MWh a year by better cooling and "
                 "lighting, then buys 150 MWh of solar. The saved 50 MWh is the cheapest part - about "
                 "35 t of CO₂ avoided for a payback of three years - and it also shrinks the size of the "
                 "solar plant that has to be bought, built and maintained.",
                 "એક ઓફિસ ઇમારત સારી ઠંડક અને પ્રકાશથી તેની માંગ વર્ષે 200 MWhથી 150 MWh કરે, પછી 150 MWh સૌર "
                 "ખરીદે. બચેલા 50 MWh સૌથી સસ્તા ભાગ છે - ત્રણ વર્ષના પરતફેળે લગભગ 35 t CO₂ બચે - અને તે "
                 "ખરીદવા, બાંધવા તથા જાળવવા પડતા સૌર સ્ટેશનનું માપ પણ ઘટાડે.")],
              "u4_mitigation", syllabus_item="4.4"),
         card(T("4.4 Carbon capture, land use, forestry and net zero",
                "4.4 કાર્બન પકડ, જમીન ઉપયોગ, વન અને નેટ ઝીરો"),
              [H4("Carbon capture and storage", "કાર્બન પકડ અને સંગ્રહ"),
               P("<b>CCS</b> separates CO₂ from a flue gas or a industrial process, compresses it to about "
                 "100 bar, pipes it to a geological store - a depleted gas field, a saline aquifer - and "
                 "keeps it there for thousands of years. Capture needs 20-30 % of the plant's energy, so "
                 "the same coal station gives less electricity or burns more coal for the same output. "
                 "<b>CCUS</b> adds use: CO₂ for enhanced oil recovery, in soft drinks, or as a feedstock "
                 "for chemicals and fuels. It is the only option for cement and steel, where the CO₂ "
                 "comes from the chemistry itself, not from the fuel.",
                 "<b>CCS</b> ધુમાડાના ગેસ કે ઉદ્યોગની પ્રક્રિયામાંથી CO₂ અલગ કરે, લગભગ 100 bar સુધી દબાવે, "
                 "ભૂસ્તરીય સંગ્રહ સુધી - ખાલી થયેલું ગેસ ક્ષેત્ર, ખારું જળાશય - પાઇપમાં લઈ જાય અને હજારો વર્ષ "
                 "ત્યાં રાખે. પકડ માટે સ્ટેશનની 20-30 % ઊર્જા જોઈએ, તેથી એ જ કોલસા સ્ટેશન ઓછી વીજળી આપે કે એ જ "
                 "ઉત્પાદન માટે વધુ કોલસો બાળે. <b>CCUS</b> ઉપયોગ ઉમેરે: તેલ ઉત્પાદન વધારવા, ઠંડા પીણાંમાં, કે "
                 "રસાયણ અને ઇંધણના કાચા માલ તરીકે CO₂. સિમેન્ટ અને પોલાદ માટે તે એકમાત્ર વિકલ્પ છે, જ્યાં CO₂ "
                 "ઇંધણમાંથી નહીં, રસાયણ પ્રક્રિયામાંથી આવે."),
               H4("Land use and forestry", "જમીન ઉપયોગ અને વન"),
               P("Forests remove CO₂ as they grow: a fast-growing tropical plantation takes up 10-15 t "
                 "of CO₂ per hectare a year while it is young, and a mature forest approaches zero "
                 "because growth and decay balance. So a forest is a <b>sink for decades, then a store</b> "
                 "that must be protected against fire and felling. Soil carbon matters as much: "
                 "no-till farming, mulching, compost and agroforestry add organic matter, and a "
                 "hectare of improved soil can hold 1-3 t of CO₂ a year - while ploughing and bare "
                 "fallow release what was stored.",
                 "વન ઉગતાં CO₂ દૂર કરે: ઝડપથી ઉગતું ઉષ્ણકટિબંધીય વૃક્ષારોપણ જુવાન હોય ત્યારે વર્ષે પ્રતિ હેક્ટર "
                 "10-15 t CO₂ લે, અને પુખ્ત વન શૂન્યની નજીક આવે કારણ કે વૃદ્ધિ અને ક્ષય સંતુલિત થાય. તેથી વન "
                 "<b>દાયકાઓ સુધી શોષક, પછી સંગ્રહ</b> છે જેને આગ અને કાપણીથી બચાવવો પડે. જમીનનો કાર્બન પણ એટલો જ "
                 "મહત્ત્વનો: ખેડ ન કરવી, આચ્છાદન, કમ્પોસ્ટ અને કૃષિવન કાર્બનિક દ્રવ્ય ઉમેરે, અને સુધારેલી જમીનનું "
                 "હેક્ટર વર્ષે 1-3 t CO₂ ધરી શકે - જ્યારે ખેડ અને ખુલ્લી પડતી જમીન સંગ્રહેલું છોડે."),
               H4("Net zero in numbers", "આંકડામાં નેટ ઝીરો"),
               TB([T("Term", "શબ્દ"), T("Meaning", "અર્થ"), T("India's line", "ભારતની રેખા")],
                  [[T("gross emissions", "કુલ ઉત્સર્જન"), T("everything released in a year", "વર્ષમાં છૂટેલું બધું"), T("about 3.0 Gt CO₂e", "લગભગ 3.0 Gt CO₂e")],
                   [T("sinks", "શોષક"), T("forests and soils taking carbon back", "વન અને જમીન કાર્બન પાછું લે"), T("forest and tree cover target of 2.5-3.0 Gt CO₂e", "વન અને વૃક્ષ આવરણનું 2.5-3.0 Gt CO₂e લક્ષ્ય")],
                   [T("net zero", "નેટ ઝીરો"), T("gross minus sinks equals zero", "કુલ ઓછા શોષક શૂન્ય"), T("pledged for 2070", "2070 માટે વચન")],
                   [T("hard to abate", "ઘટાડવો કઠિન"), T("cement, steel, aviation, shipping", "સિમેન્ટ, પોલાદ, વિમાન, જહાજ"), T("need CCS, hydrogen or offsets", "CCS, હાઇડ્રોજન કે ઓફસેટ જોઈએ")]]),
               H4("Common mistake", "સામાન્ય ભૂલ"),
               P("Treating a tree-planting pledge as a substitute for cutting emissions. A hectare of "
                 "new forest takes up 10-15 t of CO₂ a year, while one 500 MW coal station emits "
                 "2.4 Mt - so that single station needs about 1,80,000 hectares of new forest every "
                 "year to offset it. Planting is useful, but it cannot carry the load alone.",
                 "વૃક્ષારોપણના વચનને ઉત્સર્જન ઘટાડવાનો વિકલ્પ ગણવો. નવા વનનું હેક્ટર વર્ષે 10-15 t CO₂ લે, જ્યારે "
                 "એક 500 MW કોલસા સ્ટેશન 2.4 Mt છોડે - તેથી તે એક સ્ટેશનને સરભર કરવા દર વર્ષે લગભગ "
                 "1,80,000 હેક્ટર નવું વન જોઈએ. વાવેતર ઉપયોગી છે, પણ એકલું ભાર ઉપાડી ન શકે.")],
              syllabus_item="4.4"),
     ]},
]

NUMERICALS = [
    num("u4n01", T("How long the 1.5 °C carbon budget lasts.", "1.5 °Cનું કાર્બન બજેટ કેટલું ચાલશે."),
        T("About 250 Gt of CO₂ can still be emitted if warming is to stay near 1.5 °C, and the world "
          "emits 42 Gt a year. Find the years left at the present rate and the cut needed to stretch "
          "the budget to 30 years.",
          "ગરમી 1.5 °C નજીક રાખવી હોય તો હજી લગભગ 250 Gt CO₂ છોડી શકાય અને દુનિયા વર્ષે 42 Gt છોડે છે. "
          "હાલના દરે બાકી વર્ષો અને બજેટ 30 વર્ષ લંબાવવા જરૂરી ઘટાડો શોધો."),
        [P("Years left = 250 / 42 = 5.95 ≈ 6 years", "બાકી વર્ષ = 250 / 42 = 5.95 ≈ 6 વર્ષ"),
         P("For 30 years the rate must be 250 / 30 = 8.3 Gt a year",
           "30 વર્ષ માટે દર 250 / 30 = 8.3 Gt વર્ષે હોવો જોઈએ"),
         P("So emissions must fall by (42 − 8.3) / 42 = 80 %",
           "તેથી ઉત્સર્જન (42 − 8.3) / 42 = 80 % ઘટવું જોઈએ")],
        T("6 years at the present rate; 80 % cut to stretch it to 30 years",
          "હાલના દરે 6 વર્ષ; 30 વર્ષ લંબાવવા 80 % ઘટાડો"), unit_no=4),
    num("u4n02", T("Radiative forcing and the warming it implies.",
                   "કિરણોત્સર્ગી બળ અને તેની ગરમી."),
        T("CO₂ has risen from 280 ppm to 420 ppm. Using ΔF = 5.35 ln(C/C₀) and a climate sensitivity of "
          "0.8 °C per W/m², find the forcing and the equilibrium warming.",
          "CO₂ 280 ppmથી 420 ppm થયું છે. ΔF = 5.35 ln(C/C₀) અને પ્રતિ W/m² 0.8 °C જળવાયુ સંવેદનશીલતા "
          "વાપરીને બળ અને સંતુલન ગરમી શોધો."),
        [P("C/C₀ = 420 / 280 = 1.5", "C/C₀ = 420 / 280 = 1.5"),
         P("ΔF = 5.35 × ln 1.5 = 5.35 × 0.4055 = 2.17 W/m²", "ΔF = 5.35 × ln 1.5 = 5.35 × 0.4055 = 2.17 W/m²"),
         P("ΔT = λ ΔF = 0.8 × 2.17 = 1.74 °C at equilibrium",
           "સંતુલને ΔT = λ ΔF = 0.8 × 2.17 = 1.74 °C"),
         P("About 1.2 °C is observed so far because the ocean is still catching up",
           "હજી લગભગ 1.2 °C જણાય છે કારણ કે મહાસાગર હજી પકડી રહ્યો છે")],
        T("2.17 W/m² and 1.74 °C at equilibrium",
          "2.17 W/m² અને સંતુલને 1.74 °C"), unit_no=4),
    num("u4n03", T("Sea level rise from melting ice.", "બરફ પીગળવાથી દરિયા સપાટીનો વધારો."),
        T("Ice sheets and glaciers lose 400 Gt of ice a year. One millimetre of global sea level is "
          "about 361 Gt of water, and thermal expansion adds 1.4 mm a year. Find the total rise.",
          "બરફનાં પડ અને હિમનદી વર્ષે 400 Gt બરફ ગુમાવે છે. વૈશ્વિક દરિયા સપાટીનો એક મિલીમીટર લગભગ 361 Gt "
          "પાણી છે અને ઉષ્મીય વિસ્તરણ વર્ષે 1.4 mm ઉમેરે છે. કુલ વધારો શોધો."),
        [P("Melt contribution = 400 / 361 = 1.11 mm a year", "પીગળવાનો ફાળો = 400 / 361 = 1.11 mm વર્ષે"),
         P("Total = 1.11 + 1.4 = 2.51 mm a year", "કુલ = 1.11 + 1.4 = 2.51 mm વર્ષે"),
         P("Over 80 years that is about 20 cm, matching the measured rise since 1900",
           "80 વર્ષમાં તે લગભગ 20 cm, 1900થી માપેલા વધારા સાથે મળે")],
        T("About 2.5 mm a year, 20 cm in 80 years",
          "વર્ષે લગભગ 2.5 mm, 80 વર્ષમાં 20 cm"), unit_no=4),
    num("u4n04", T("Emissions of one coal station.", "એક કોલસા સ્ટેશનનું ઉત્સર્જન."),
        T("A 500 MW coal station runs at a 60 % capacity factor and emits 0.9 t of CO₂ per MWh. Find "
          "its yearly energy and emissions, and the CO₂ per kWh.",
          "500 MW કોલસા સ્ટેશન 60 % ક્ષમતા અવયવે ચાલે અને પ્રતિ MWh 0.9 t CO₂ છોડે. તેની વાર્ષિક ઊર્જા અને "
          "ઉત્સર્જન તથા પ્રતિ kWh CO₂ શોધો."),
        [P("Energy = 500 × 8,760 × 0.60 = 2.63 × 10⁶ MWh = 2.63 TWh",
           "ઊર્જા = 500 × 8,760 × 0.60 = 2.63 × 10⁶ MWh = 2.63 TWh"),
         P("CO₂ = 2.63 × 10⁶ × 0.9 = 2.37 × 10⁶ t = 2.37 Mt a year",
           "CO₂ = 2.63 × 10⁶ × 0.9 = 2.37 × 10⁶ t = 2.37 Mt વર્ષે"),
         P("Per kWh = 0.9 kg, which is why one unit of coal power is described as a kilogram of CO₂",
           "પ્રતિ kWh = 0.9 કિલો, તેથી જ એક યુનિટ કોલસા વીજળીને એક કિલો CO₂ કહે છે")],
        T("2.63 TWh and 2.37 Mt of CO₂ a year, 0.9 kg per kWh",
          "વર્ષે 2.63 TWh અને 2.37 Mt CO₂, પ્રતિ kWh 0.9 કિલો"), unit_no=4),
    num("u4n05", T("A greenhouse gas basket in CO₂ equivalent.",
                   "CO₂ સમમૂલ્યમાં હરિતગૃહ વાયુની ટોપલી."),
        T("A factory releases 100 t of CO₂, 2 t of methane and 0.1 t of nitrous oxide in a year. Using "
          "GWP values of 1, 28 and 265, find the total in CO₂ equivalent and the share of methane.",
          "એક કારખાનું વર્ષે 100 t CO₂, 2 t મિથેન અને 0.1 t નાઇટ્રસ ઓક્સાઇડ છોડે છે. GWP 1, 28 અને 265 "
          "વાપરીને CO₂ સમમૂલ્યમાં કુલ અને મિથેનનો હિસ્સો શોધો."),
        [P("CO₂ = 100 × 1 = 100 t", "CO₂ = 100 × 1 = 100 t"),
         P("CH₄ = 2 × 28 = 56 t CO₂e", "CH₄ = 2 × 28 = 56 t CO₂e"),
         P("N₂O = 0.1 × 265 = 26.5 t CO₂e", "N₂O = 0.1 × 265 = 26.5 t CO₂e"),
         P("Total = 182.5 t CO₂e, and methane is 56 / 182.5 = 31 % of it",
           "કુલ = 182.5 t CO₂e, અને મિથેન તેના 56 / 182.5 = 31 % છે")],
        T("182.5 t CO₂e, of which 31 % is methane",
          "182.5 t CO₂e, જેમાં 31 % મિથેન"), unit_no=4),
    num("u4n06", T("Ocean acidification in numbers.", "આંકડામાં મહાસાગરનું અમ્લીકરણ."),
        T("Surface ocean pH has fallen from 8.20 to 8.10. Find the change in hydrogen ion "
          "concentration and explain why it matters to shell-forming life.",
          "સપાટીના મહાસાગરનો pH 8.20થી 8.10 થયો છે. હાઇડ્રોજન આયન સાંદ્રતામાં ફેરફાર શોધો અને શેલ બનાવતા "
          "જીવો માટે તે કેમ મહત્ત્વનું છે તે સમજાવો."),
        [P("[H⁺] = 10^(−pH), so the ratio is 10^(8.20 − 8.10) = 10^0.1 = 1.26",
           "[H⁺] = 10^(−pH), તેથી ગુણોત્તર 10^(8.20 − 8.10) = 10^0.1 = 1.26"),
         P("Hydrogen ions are up 26 %, so the water is 26 % more acidic even though pH moved 0.1",
           "હાઇડ્રોજન આયન 26 % વધ્યા, તેથી pH 0.1 ખસ્યો છતાં પાણી 26 % વધુ અમ્લીય છે"),
         P("Corals and molluscs spend more energy building calcium carbonate and less on growth",
           "પરવાળા અને શંખ કેલ્શિયમ કાર્બોનેટ બનાવવામાં વધુ ઊર્જા ખર્ચે અને વૃદ્ધિ પર ઓછી")],
        T("A 26 % rise in hydrogen ions for a pH fall of 0.1",
          "pH 0.1ના ઘટાડા માટે હાઇડ્રોજન આયનમાં 26 % વધારો"), unit_no=4),
    num("u4n07", T("Forest area needed to offset a coal station.",
                   "કોલસા સ્ટેશનને સરભર કરવા જરૂરી વન વિસ્તાર."),
        T("The station of 2.37 Mt CO₂ a year is to be offset by new forest that takes up 12 t of CO₂ "
          "per hectare a year. Find the area needed, and compare it with the 500 MW station's own land.",
          "વર્ષે 2.37 Mt CO₂ વાળા સ્ટેશનને પ્રતિ હેક્ટર વર્ષે 12 t CO₂ લેતા નવા વનથી સરભર કરવું છે. જરૂરી "
          "વિસ્તાર શોધો અને 500 MW સ્ટેશનની પોતાની જમીન સાથે સરખાવો."),
        [P("Area = 2.37 × 10⁶ / 12 = 1.98 × 10⁵ ha = about 1.98 lakh hectares",
           "વિસ્તાર = 2.37 × 10⁶ / 12 = 1.98 × 10⁵ હેક્ટર = લગભગ 1.98 લાખ હેક્ટર"),
         P("That is 1,980 km², about twice the area of Surat district",
           "તે 1,980 km² છે, લગભગ સુરત જિલ્લાના વિસ્તાર કરતાં બમણું"),
         P("The station itself occupies about 4 km², so planting cannot replace closing it",
           "સ્ટેશન પોતે લગભગ 4 km² લે છે, તેથી વાવેતર તેને બંધ કરવાનો વિકલ્પ ન બને")],
        T("About 1.98 lakh hectares (1,980 km²) every year",
          "દર વર્ષે લગભગ 1.98 લાખ હેક્ટર (1,980 km²)"), unit_no=4),
    num("u4n08", T("Warming from a doubling of CO₂.", "CO₂ બમણું થવાથી ગરમી."),
        T("Doubling CO₂ gives a forcing of 3.71 W/m². Find the equilibrium warming for climate "
          "sensitivities of 0.6, 0.8 and 1.2 °C per W/m² and comment on the range.",
          "CO₂ બમણું થવાથી 3.71 W/m² બળ મળે. પ્રતિ W/m² 0.6, 0.8 અને 1.2 °C સંવેદનશીલતા માટે સંતુલન ગરમી "
          "શોધો અને શ્રેણી પર ટિપ્પણી કરો."),
        [P("For λ = 0.6: ΔT = 0.6 × 3.71 = 2.2 °C", "λ = 0.6 માટે: ΔT = 0.6 × 3.71 = 2.2 °C"),
         P("For λ = 0.8: ΔT = 0.8 × 3.71 = 3.0 °C", "λ = 0.8 માટે: ΔT = 0.8 × 3.71 = 3.0 °C"),
         P("For λ = 1.2: ΔT = 1.2 × 3.71 = 4.5 °C", "λ = 1.2 માટે: ΔT = 1.2 × 3.71 = 4.5 °C"),
         P("The range 2.2-4.5 °C is the IPCC likely range; the water vapour feedback makes the high end likely",
           "2.2-4.5 °Cની શ્રેણી IPCCની સંભવિત શ્રેણી છે; પાણીની વરાળનો પ્રતિસંદર્શ ઊંચા અંતને સંભવિત બનાવે")],
        T("2.2, 3.0 and 4.5 °C, a likely range of 2.2 to 4.5 °C",
          "2.2, 3.0 અને 4.5 °C, લગભગ 2.2 થી 4.5 °C શ્રેણી"), unit_no=4),
    num("u4n09", T("Carbon capture with its energy penalty.",
                   "ઊર્જા ખોટ સાથે કાર્બન પકડ."),
        T("A 600 MW coal plant emits 0.9 t CO₂ per MWh at a 70 % capacity factor. A CCS unit captures "
          "90 % of the CO₂ but uses 25 % of the plant's output. Find the CO₂ captured and the net output.",
          "600 MW કોલસા સ્ટેશન 70 % ક્ષમતા અવયવે પ્રતિ MWh 0.9 t CO₂ છોડે. CCS એકમ 90 % CO₂ પકડે પણ સ્ટેશનના "
          "ઉત્પાદનના 25 % વાપરે. પકડાયેલું CO₂ અને ચોખ્ખું ઉત્પાદન શોધો."),
        [P("Gross energy = 600 × 8,760 × 0.70 = 3.68 × 10⁶ MWh",
           "કુલ ઊર્જા = 600 × 8,760 × 0.70 = 3.68 × 10⁶ MWh"),
         P("CO₂ emitted = 3.68 × 10⁶ × 0.9 = 3.31 Mt; captured = 0.90 × 3.31 = 2.98 Mt",
           "છૂટેલું CO₂ = 3.68 × 10⁶ × 0.9 = 3.31 Mt; પકડાયું = 0.90 × 3.31 = 2.98 Mt"),
         P("Net output = 600 × 0.75 = 450 MW, so 25 % of the capacity is spent on capture",
           "ચોખ્ખું ઉત્પાદન = 600 × 0.75 = 450 MW, તેથી 25 % ક્ષમતા પકડમાં જાય"),
         P("Still 0.33 Mt escapes, so CCS cuts emissions by 90 % and not by 100 %",
           "હજી 0.33 Mt નીકળે, તેથી CCS ઉત્સર્જન 90 % ઘટાડે, 100 % નહીં")],
        T("2.98 Mt captured, 450 MW net instead of 600 MW",
          "2.98 Mt પકડાયું, 600 MWને બદલે 450 MW ચોખ્ખું"), unit_no=4),
    num("u4n10", T("Per capita emissions and a fair share of the budget.",
                   "માથાદીઠ ઉત્સર્જન અને બજેટનો ન્યાયી હિસ્સો."),
        T("India emits about 3.0 Gt CO₂e a year for 1.42 billion people; the world emits 42 Gt for "
          "8.0 billion. Compare the per capita figures and India's share of a 250 Gt budget on an equal "
          "per capita basis.",
          "ભારત 1.42 અબજ લોકો માટે વર્ષે લગભગ 3.0 Gt CO₂e છોડે છે; દુનિયા 8.0 અબજ માટે 42 Gt. માથાદીઠ "
          "આંકડા અને સમાન માથાદીઠ ધોરણે 250 Gt બજેટમાં ભારતનો હિસ્સો સરખાવો."),
        [P("India = 3.0 × 10⁹ / 1.42 × 10⁹ = 2.1 t per person a year",
           "ભારત = 3.0 × 10⁹ / 1.42 × 10⁹ = 2.1 t પ્રતિ વ્યક્તિ વર્ષે"),
         P("World = 42 × 10⁹ / 8.0 × 10⁹ = 5.25 t per person a year",
           "દુનિયા = 42 × 10⁹ / 8.0 × 10⁹ = 5.25 t પ્રતિ વ્યક્તિ વર્ષે"),
         P("Equal share of 250 Gt = 250 / 8.0 = 31 t per person in total; India has 1.42 × 31 = 44 Gt",
           "250 Gtનો સમાન હિસ્સો = 250 / 8.0 = 31 t પ્રતિ વ્યક્તિ કુલ; ભારતને 1.42 × 31 = 44 Gt"),
         P("At 3.0 Gt a year that share lasts about 15 years, so India's 2070 net-zero pledge is a "
           "development question, not only an energy one",
           "વર્ષે 3.0 Gt પર તે હિસ્સો લગભગ 15 વર્ષ ચાલે, તેથી ભારતનું 2070 નેટ-ઝીરો વચન ફક્ત ઊર્જાનો નહીં, "
           "વિકાસનો પ્રશ્ન છે")],
        T("2.1 t against 5.25 t per person; an equal share is 31 t per person",
          "પ્રતિ વ્યક્તિ 2.1 t સામે 5.25 t; સમાન હિસ્સો પ્રતિ વ્યક્તિ 31 t"), unit_no=4),
]

EQUATIONS = [
    {"title": T("Forcing and temperature", "બળ અને તાપમાન"),
     "items": [
         {"name": T("Radiative forcing of CO₂", "CO₂નું કિરણોત્સર્ગી બળ"), "f": "ΔF = 5.35 ln(C / C₀)",
          "terms": T("C is the present concentration in ppm and C₀ the pre-industrial 280 ppm.",
                     "C એ હાલની સાંદ્રતા ppmમાં અને C₀ ઉદ્યોગ પહેલાંનું 280 ppm.")},
         {"name": T("Equilibrium warming", "સંતુલન ગરમી"), "f": "ΔT = λ ΔF",
          "terms": T("λ is about 0.8 °C per W/m²; the IPCC likely range of λ gives 2.2-4.5 °C for a doubling.",
                     "λ લગભગ 0.8 °C પ્રતિ W/m²; IPCCની સંભવિત શ્રેણી બમણા માટે 2.2-4.5 °C આપે.")},
         {"name": T("CO₂ equivalent", "CO₂ સમમૂલ્ય"), "f": "CO₂e = Σ (mass × GWP)",
          "terms": T("GWP is 1 for CO₂, 28 for methane and 265 for nitrous oxide over 100 years.",
                     "100 વર્ષમાં GWP CO₂ માટે 1, મિથેન માટે 28 અને નાઇટ્રસ ઓક્સાઇડ માટે 265 છે.")},
         {"name": T("Carbon budget", "કાર્બન બજેટ"), "f": "years = budget / annual emissions",
          "terms": T("The budget is the total CO₂ that can still be emitted for a temperature goal.",
                     "બજેટ એ તાપમાન લક્ષ્ય માટે હજી છોડી શકાય તેવું કુલ CO₂ છે.")},
     ]},
    {"title": T("Ice, sea and ocean chemistry", "બરફ, દરિયો અને મહાસાગર રસાયણ"),
     "items": [
         {"name": T("Sea level from melt", "પીગળવાથી દરિયા સપાટી"), "f": "SLR (mm) = mass lost (Gt) / 361",
          "terms": T("361 Gt of water spread over the ocean raises it by about one millimetre.",
                     "મહાસાગર પર ફેલાયેલું 361 Gt પાણી તેને લગભગ એક મિલીમીટર વધારે.")},
         {"name": T("Hydrogen ion change", "હાઇડ્રોજન આયન ફેરફાર"),
          "f": "[H⁺] = 10^(−pH),  ratio = 10^(pH_old − pH_new)",
          "terms": T("A fall of 0.1 in pH is a 26 % rise in acidity, not 1 %.",
                     "pH માં 0.1નો ઘટાડો અમ્લતામાં 26 % વધારો છે, 1 % નહીં.")},
     ]},
    {"title": T("Mitigation arithmetic", "શમનનું ગણિત"),
     "items": [
         {"name": T("Emissions of a plant", "સ્ટેશનનું ઉત્સર્જન"),
          "f": "m_CO₂ = P × 8,760 × CF × EF", 
          "terms": T("P is the rating in MW, CF the capacity factor and EF the emission factor in t per MWh.",
                     "P એ MWમાં રેટિંગ, CF ક્ષમતા અવયવ અને EF એ પ્રતિ MWh ટનમાં ઉત્સર્જન અવયવ.")},
         {"name": T("Emitted CO₂ avoided", "બચતનું CO₂"), "f": "m = E × (EF_grid − EF_new)",
          "terms": T("For solar against the Indian grid: EF_grid about 0.71 t per MWh and EF_solar about 0.05.",
                     "ભારતીય ગ્રિડ સામે સૌર માટે: EF_grid લગભગ 0.71 t પ્રતિ MWh અને EF_solar લગભગ 0.05.")},
         {"name": T("Capture with a penalty", "ખોટ સાથે પકડ"),
          "f": "m_captured = η_capture × m_emitted;  P_net = P × (1 − penalty)",
          "terms": T("A capture unit of 90 % efficiency with a 25 % energy penalty leaves 10 % escaping.",
                     "90 % કાર્યક્ષમતાનો પકડ એકમ 25 % ઊર્જા ખોટ સાથે 10 % નીકળવા દે.")},
         {"name": T("Land sink", "જમીન શોષક"), "f": "area = emissions / uptake per hectare",
          "terms": T("Young tropical forest takes up 10-15 t CO₂ per hectare a year.",
                     "જુવાન ઉષ્ણકટિબંધીય વન વર્ષે પ્રતિ હેક્ટર 10-15 t CO₂ લે.")},
     ]},
]

VIVA = [
    {"title": T("Science and evidence", "વિજ્ઞાન અને પુરાવા"),
     "items": [
         {"q": T("What is the greenhouse effect and why is it necessary?",
                 "હરિતગૃહ પ્રભાવ શું છે અને તે કેમ આવશ્યક છે?"),
          "a": T("Short-wave sunlight passes through the atmosphere and warms the surface; the surface "
                 "re-emits that energy as long-wave infrared, which water vapour, CO₂, methane and "
                 "nitrous oxide absorb and re-radiate, half of it back downwards. Without this natural "
                 "effect the mean surface temperature would be about −18 °C instead of 15 °C, and "
                 "liquid water and life as we know it would not exist. The problem is the extra "
                 "trapping we add by raising the concentration of those gases.",
                 "ટૂંકી તરંગલંબાઈનો સૂર્યપ્રકાશ વાતાવરણમાંથી પસાર થઈ સપાટીને ગરમ કરે; સપાટી તે ઊર્જા લાંબી "
                 "તરંગલંબાઈના ઇન્ફ્રારેડ તરીકે પાછી ફેંકે, જે પાણીની વરાળ, CO₂, મિથેન અને નાઇટ્રસ ઓક્સાઇડ શોષી "
                 "ફરી કિરણોત્સર્ગ કરે, અડધું નીચે. આ કુદરતી પ્રભાવ વગર સરેરાશ સપાટીનું તાપમાન 15 °Cને બદલે "
                 "લગભગ −18 °C હોત, અને પ્રવાહી પાણી તથા આપણે જાણીએ તેવું જીવન ન હોત. સમસ્યા તે વાયુઓની "
                 "સાંદ્રતા વધારીને આપણે ઉમેરતું વધારાનું રોકાણ છે.")},
         {"q": T("How do we know the warming is caused by greenhouse gases and not by the sun?",
                 "ગરમી સૂર્યથી નહીં પણ હરિતગૃહ વાયુથી છે તે આપણે કેવી રીતે જાણીએ?"),
          "a": T("Three fingerprints. First, the pattern with height: greenhouse gases warm the "
                 "troposphere and cool the stratosphere, while a brighter sun would warm both. Second, "
                 "the pattern in time: nights warm faster than days and winters faster than summers, "
                 "which a stronger sun does not do. Third, the spectrum measured from space shows less "
                 "outgoing infrared at exactly the wavelengths that CO₂ and methane absorb. Satellites "
                 "also measure the total solar output directly and find no upward trend since 1980, "
                 "while the earth has warmed about 0.6 °C in that time.",
                 "ત્રણ અંગૂઠાનાં નિશાન. પ્રથમ, ઊંચાઈ પ્રમાણેનો નમૂનો: હરિતગૃહ વાયુ ટ્રોપોસ્ફિયરને ગરમ અને "
                 "સ્ટ્રેટોસ્ફિયરને ઠંડું કરે, જ્યારે તેજસ્વી સૂર્ય બંનેને ગરમ કરે. બીજું, સમય પ્રમાણેનો નમૂનો: "
                 "દિવસ કરતાં રાત અને ઉનાળા કરતાં શિયાળો ઝડપથી ગરમ થાય, જે વધુ તાકાતવાન સૂર્ય ન કરે. ત્રીજું, "
                 "અવકાશથી માપેલા વર્ણપટમાં બરાબર તે તરંગલંબાઈ પર ઓછું ઇન્ફ્રારેડ નીકળે જે CO₂ અને મિથેન શોષે. "
                 "ઉપગ્રહો કુલ સૌર ઉત્પાદન પણ સીધું માપે અને 1980થી ઉપરનો ટ્રેન્ડ જોતા નથી, જ્યારે પૃથ્વી તે "
                 "સમયમાં લગભગ 0.6 °C ગરમ થઈ છે.")},
         {"q": T("What are the main greenhouse gases and their sources?",
                 "મુખ્ય હરિતગૃહ વાયુ અને તેમના સ્રોત કયા છે?"),
          "a": T("CO₂ from coal, oil, gas, cement and land clearing is the largest, at about 64 % of the "
                 "warming. Methane at 28 times the strength comes from cattle, rice paddies, landfills, "
                 "coal mines and gas leaks, and 17 % of the warming. Nitrous oxide at 265 times comes "
                 "mainly from nitrogen fertiliser and manure, 6 %. Fluorinated gases from refrigeration "
                 "and air conditioning are thousands of times stronger but small in mass, 3 %. Water "
                 "vapour is the strongest absorber of all, but it is a feedback rather than a forcing.",
                 "કોલસો, તેલ, ગેસ, સિમેન્ટ અને જમીન સફાઈમાંથી CO₂ સૌથી મોટું છે, લગભગ 64 % ગરમી. 28 ગણા "
                 "શક્તિશાળી મિથેન ઢોર, ડાંગરનાં ખેતર, કચરાભરાવ, કોલસાની ખાણ અને ગેસ લીકેજમાંથી આવે અને 17 % "
                 "ગરમી. 265 ગણું નાઇટ્રસ ઓક્સાઇડ મુખ્યત્વે નાઇટ્રોજન ખાતર અને છાણમાંથી, 6 %. ઠંડક અને "
                 "વાતાનુકૂલનના ફ્લોરિનવાળા વાયુ હજારો ગણા શક્તિશાળી પણ દળમાં નાના, 3 %. પાણીની વરાળ સૌથી "
                 "શક્તિશાળી શોષક છે, પણ તે બળ નહીં, પ્રતિસંદર્શ છે.")},
         {"q": T("What is albedo and how does melting ice change it?",
                 "આલ્બેડો શું છે અને બરફ પીગળવાથી તે કેવી રીતે બદલાય?"),
          "a": T("Albedo is the fraction of sunlight a surface reflects. Fresh snow reflects 80-90 %, "
                 "sea ice 50-70 %, forest 10-15 %, bare soil 20-30 % and open ocean only 6 %. When white "
                 "ice melts it exposes darker water or land, which absorbs the energy instead of "
                 "reflecting it, so the surface warms further and melts more ice. This ice-albedo "
                 "feedback is why the Arctic warms three to four times faster than the global average "
                 "and why losing summer sea ice matters far more than its area suggests.",
                 "આલ્બેડો એ સપાટી જે પ્રમાણમાં સૂર્યપ્રકાશ પરાવર્તિત કરે તે છે. તાજો બરફ 80-90 %, દરિયાઈ બરફ "
                 "50-70 %, વન 10-15 %, ખુલ્લી જમીન 20-30 % અને ખુલ્લો મહાસાગર ફક્ત 6 % પરાવર્તિત કરે. સફેદ બરફ "
                 "પીગળે ત્યારે ઘેરું પાણી કે જમીન ખુલે, જે ઊર્જા પરાવર્તિત કરવાને બદલે શોષે, તેથી સપાટી વધુ ગરમ "
                 "થાય અને વધુ બરફ પીગળે. આ બરફ-આલ્બેડો પ્રતિસંદર્શને કારણે જ આર્કટિક વૈશ્વિક સરેરાશ કરતાં ત્રણથી "
                 "ચાર ગણું ઝડપથી ગરમ થાય અને ઉનાળાનો દરિયાઈ બરફ ગુમાવવો તેના વિસ્તાર કરતાં ઘણો વધુ મહત્ત્વનો છે.")},
         {"q": T("What is a carbon budget and why is it used?",
                 "કાર્બન બજેટ શું છે અને તે કેમ વપરાય છે?"),
          "a": T("It is the total amount of CO₂ that can still be released while keeping warming below a "
                 "chosen limit, and it exists because the temperature responds to the cumulative total, "
                 "not to the emissions in any one year. About 250 Gt remain for a good chance of 1.5 °C "
                 "and about 1,150 Gt for 2 °C, against 42 Gt a year today. It is used because it turns "
                 "a vague promise into an arithmetic test: at the present rate the 1.5 °C budget lasts "
                 "about six years, which is why every year of delay makes the later cuts steeper.",
                 "તે એ કુલ CO₂ છે જે પસંદ કરેલી મર્યાદાથી નીચે ગરમી રાખવા હજી છોડી શકાય, અને તે એટલા માટે છે કે "
                 "તાપમાન કુલ સરવાળા પર પ્રતિક્રિયા આપે, કોઈ એક વર્ષના ઉત્સર્જન પર નહીં. 1.5 °Cની સારી શક્યતા "
                 "માટે લગભગ 250 Gt અને 2 °C માટે લગભગ 1,150 Gt બાકી છે, આજે વર્ષે 42 Gt સામે. તે વપરાય કારણ કે "
                 "અસ્પષ્ટ વચનને ગણિતની કસોટીમાં ફેરવે: હાલના દરે 1.5 °Cનું બજેટ લગભગ છ વર્ષ ચાલે, તેથી જ "
                 "દરેક વર્ષની મોડ પછીના ઘટાડા વધુ તીવ્ર કરે.")},
     ]},
    {"title": T("Impacts and mitigation", "અસરો અને શમન"),
     "items": [
         {"q": T("Why do extreme events change even when the average moves only a little?",
                 "સરેરાશ થોડું જ ખસે તો પણ આત્યંતિક ઘટનાઓ કેમ બદલાય?"),
          "a": T("Because the extremes sit in the tails of a distribution. A shift of the whole curve by "
                 "one degree moves the tail much further in probability terms: an event that happened "
                 "once in fifty years may become once in ten. In addition, warmer air holds about 7 % "
                 "more water vapour per degree, so when it does rain the total can be heavier. That is "
                 "why the record shows more heat records than cold ones and more one-day rainfall "
                 "extremes even where the annual total has not changed.",
                 "કારણ કે આત્યંતિક ઘટનાઓ વિતરણની પૂંછડીમાં બેસે છે. આખી વણકર એક ડિગ્રીે ખસે તો શક્યતાની "
                 "દૃષ્ટિએ પૂંછડી ઘણે દૂર ખસે: પચાસ વર્ષે એક વારની ઘટના દસ વર્ષે એક વાર બની શકે. વધુમાં, ગરમ "
                 "હવા દરેક ડિગ્રીે લગભગ 7 % વધુ પાણીની વરાળ ધરે, તેથી જ્યારે વરસે ત્યારે કુલ ભારે હોઈ શકે. તેથી જ "
                 "રેકોર્ડમાં ઠંડા કરતાં વધુ ગરમ રેકોર્ડ અને એક દિવસના વરસાદની વધુ ચરમસીમા દેખાય, જ્યાં વાર્ષિક "
                 "કુલ ન બદલ્યું હોય ત્યાં પણ.")},
         {"q": T("What is ocean acidification and how is it different from warming?",
                 "મહાસાગરનું અમ્લીકરણ શું છે અને તે ગરમીથી કેવી રીતે જુદું છે?"),
          "a": T("It is a chemical change, not a thermal one. The CO₂ that dissolves in sea water forms "
                 "carbonic acid, which releases hydrogen ions and lowers pH from 8.2 to 8.1 - a 26 % "
                 "rise in acidity. Warming is about heat; acidification is about chemistry, and cooling "
                 "the ocean would not reverse it. The consequence is that corals, oysters and some "
                 "plankton find it harder to build calcium carbonate shells and skeletons, so reefs "
                 "grow more slowly and dissolve faster, which threatens fish nurseries and coastal "
                 "protection.",
                 "તે ઉષ્મીય નહીં, રાસાયણિક ફેરફાર છે. દરિયાના પાણીમાં ઓગળતું CO₂ કાર્બોનિક એસિડ બનાવે, જે "
                 "હાઇડ્રોજન આયન છોડે અને pH 8.2થી 8.1 કરે - અમ્લતામાં 26 % વધારો. ગરમી ઉષ્મા વિશે છે; "
                 "અમ્લીકરણ રસાયણ વિશે છે, અને મહાસાગરને ઠંડો કરવાથી તે ઊલટાવાય નહીં. પરિણામ એ છે કે પરવાળા, "
                 "ઓઇસ્ટર અને કેટલાક પ્લવકને કેલ્શિયમ કાર્બોનેટ શેલ અને હાડપિંજર બનાવવું મુશ્કેલ થાય, તેથી ભરતી "
                 "ધીમે વધે અને ઝડપથી ઓગળે, જે માછલીના બચ્ચાં અને કિનારાના રક્ષણને ધમકાવે.")},
         {"q": T("What is desertification and how is it linked to climate change?",
                 "મરુસ્થલીકરણ શું છે અને તે જળવાયુ પરિવર્તન સાથે કેવી રીતે જોડાય છે?"),
          "a": T("It is the degradation of land in dry regions - loss of vegetation, soil and "
                 "productivity - caused by overgrazing, deforestation, bad irrigation, salt build-up "
                 "and repeated drought. Climate change amplifies it because higher temperature raises "
                 "evaporation from already dry soil, so the same rainfall produces less growth and a dry "
                 "spell becomes a failed crop. About 40 % of India's land is degraded to some degree, "
                 "and the loss pushes families from Kutch, Rajasthan and the Deccan towards cities.",
                 "તે સૂકા વિસ્તારોમાં જમીનનો ક્ષય છે - વનસ્પતિ, જમીન અને ઉત્પાદકતાનું નુકસાન - જે વધુ ચરાવાણ, "
                 "વનનાબૂદી, ખરાબ સિંચાઈ, ક્ષારનો સંગ્રહ અને વારંવારના દુષ્કાળથી થાય. જળવાયુ પરિવર્તન તેને "
                 "વધારે કારણ કે ઊંચું તાપમાન પહેલેથી સૂકી જમીનમાંથી બાષ્પીભવન વધારે, તેથી એ જ વરસાદ ઓછી "
                 "વૃદ્ધિ આપે અને સૂકો સમય નિષ્ફળ પાક બને. ભારતની લગભગ 40 % જમીન અમુક અંશે ક્ષીણ છે, અને "
                 "નુકસાન કચ્છ, રાજસ્થાન અને દક્કનના કુટુંબોને શહેરો તરફ ધકેલે છે.")},
         {"q": T("Distinguish mitigation from adaptation with two examples each.",
                 "શમન અને અનુકૂલનને દરેકના બે ઉદાહરણ સાથે જુદા પાડો."),
          "a": T("Mitigation attacks the cause by cutting emissions: a solar plant replacing coal "
                 "generation, or a bus fleet shifted to electric. Adaptation accepts that the warming "
                 "is already here and reduces the damage: a heat action plan that opens cooling shelters "
                 "and changes working hours, or a coastal embankment and mangrove belt against storm "
                 "surge. Mitigation is global in benefit and slow to show; adaptation is local and "
                 "immediate. A country must do both, and India's National Action Plan on Climate Change "
                 "has separate missions for each.",
                 "શમન કારણ પર હુમલો કરે, ઉત્સર્જન ઘટાડીને: કોલસા ઉત્પાદનને બદલતું સૌર સ્ટેશન, કે ઇલેક્ટ્રિક "
                 "થયેલી બસ સેવા. અનુકૂલન સ્વીકારે કે ગરમી પહેલેથી છે અને નુકસાન ઘટાડે: ઠંડા આશ્રય ખોલતી અને "
                 "કામનો સમય બદલતી ગરમી કાર્ય યોજના, કે તોફાની ભરતી સામે કિનારાનો બંધ અને કાંદા (મેનગ્રોવ)નો "
                 "પટ્ટો. શમનનો લાભ વૈશ્વિક અને દેખાવા માટે ધીમો; અનુકૂલન સ્થાનિક અને તાત્કાલિક. દેશે બંને "
                 "કરવાં પડે, અને ભારતની રાષ્ટ્રીય જળવાયુ કાર્ય યોજનામાં દરેક માટે અલગ મિશન છે.")},
         {"q": T("How does carbon capture and storage work, and what are its limits?",
                 "કાર્બન પકડ અને સંગ્રહ કેવી રીતે ચાલે અને તેની મર્યાદા શું છે?"),
          "a": T("CO₂ is separated from the flue gas by an amine solvent, a membrane or oxy-fuel burning, "
                 "compressed to about 100 bar, transported by pipeline and injected 1-3 km down into a "
                 "saline aquifer or a depleted gas field where a cap rock seals it. Limits: the capture "
                 "unit uses 20-30 % of the plant's energy, so more fuel is burnt for the same output; "
                 "capture efficiency is 85-95 %, so some CO₂ still escapes; pipelines, storage sites and "
                 "monitoring cost money; and a leak or a well failure would release the stored gas. It is "
                 "essential for cement and steel, where the CO₂ comes from the chemistry, and should not "
                 "be used to keep an old coal station alive.",
                 "CO₂ ને એમાઇન દ્રાવક, પડદો કે ઓક્સી-ફ્યુઅલ દહનથી ધુમાડામાંથી અલગ કરાય, લગભગ 100 bar સુધી "
                 "દબાવાય, પાઇપલાઇનથી લઈ જઈ 1-3 km નીચે ખારા જળાશય કે ખાલી ગેસ ક્ષેત્રમાં દબાવાય જ્યાં ઢાંકણ "
                 "ખડક તેને સીલ કરે. મર્યાદા: પકડ એકમ સ્ટેશનની 20-30 % ઊર્જા વાપરે, તેથી એ જ ઉત્પાદન માટે વધુ "
                 "ઇંધણ બળે; પકડ કાર્યક્ષમતા 85-95 % છે, તેથી થોડું CO₂ હજી નીકળે; પાઇપલાઇન, સંગ્રહ સ્થળ અને "
                 "દેખરેખ પૈસા માંગે; અને લીકેજ કે કૂવાની નિષ્ફળતા સંગ્રહેલો ગેસ છોડે. સિમેન્ટ અને પોલાદ માટે તે "
                 "આવશ્યક છે, જ્યાં CO₂ રસાયણમાંથી આવે, અને જૂનું કોલસા સ્ટેશન જીવતું રાખવા વાપરવું ન જોઈએ.")},
         {"q": T("Why is energy efficiency called the first fuel?",
                 "ઊર્જા કાર્યક્ષમતાને પ્રથમ ઇંધણ કેમ કહેવાય?"),
          "a": T("Because a unit of energy saved needs no fuel, no plant, no land, no transmission line "
                 "and no subsidy, and it produces no emissions. It is almost always the cheapest option "
                 "per tonne of CO₂ and is available immediately: an LED lamp, a five-star air "
                 "conditioner, an efficient pump, a variable speed drive on a motor. The saved energy "
                 "also multiplies down the system - a smaller load needs a smaller transformer, a "
                 "smaller solar plant and fewer batteries - which is why efficiency is counted before "
                 "any new supply in every serious climate plan.",
                 "કારણ કે બચેલો ઊર્જા એકમ કોઈ ઇંધણ, સ્ટેશન, જમીન, ટ્રાન્સમિશન લાઇન કે સબસિડી માંગતો નથી "
                 "અને કોઈ ઉત્સર્જન કરતો નથી. તે લગભગ હંમેશા પ્રતિ ટન CO₂ સૌથી સસ્તો વિકલ્પ હોય અને તરત "
                 "ઉપલબ્ધ હોય: LED દીવો, પાંચ સ્ટાર એરકન્ડીશનર, કાર્યક્ષમ પંપ, મોટર પર ચલ ગતિ ડ્રાઇવ. બચેલી "
                 "ઊર્જા આખી પ્રણાલીમાં ગુણાકાર કરે - નાનો ભાર નાનું ટ્રાન્સફોર્મર, નાનું સૌર સ્ટેશન અને ઓછી "
                 "બેટરી માંગે - તેથી જ દરેક ગંભીર જળવાયુ યોજનામાં કાર્યક્ષમતા કોઈ પણ નવા પુરવઠા પહેલાં ગણાય.")},
         {"q": T("What does net zero mean, and why is 2070 India's target?",
                 "નેટ ઝીરો એટલે શું, અને 2070 ભારતનું લક્ષ્ય કેમ છે?"),
          "a": T("Net zero means the CO₂ still released is balanced by the CO₂ removed by forests, soils "
                 "and engineered sinks, so the net addition to the atmosphere is zero. It is not the "
                 "same as zero emissions, which is impossible for cement, steel and aviation with "
                 "today's technology. India chose 2070 because the country still needs to build houses, "
                 "steel and power for a growing population, and a 2050 date would have meant importing "
                 "the technology and paying for it before the economy could afford it; 2070 with 500 GW "
                 "of non-fossil capacity by 2030 and a 45 % cut in emission intensity is the development "
                 "path that also cuts carbon.",
                 "નેટ ઝીરો એટલે હજી છૂટતું CO₂ વન, જમીન અને ઇજનેરી શોષક દૂર કરે તેના દ્વારા સંતુલિત થાય, "
                 "તેથી વાતાવરણમાં ચોખ્ખો ઉમેરો શૂન્ય. તે શૂન્ય ઉત્સર્જન નથી, જે આજની ટેક્નોલોજીથી સિમેન્ટ, "
                 "પોલાદ અને વિમાન માટે અશક્ય છે. ભારતે 2070 પસંદ કર્યું કારણ કે દેશે વધતી વસ્તી માટે હજી ઘર, "
                 "પોલાદ અને વીજળી બાંધવાં છે, અને 2050ની તારીખનો અર્થ ટેક્નોલોજી આયાત કરીને અર્થતંત્ર પરવડે "
                 "તે પહેલાં ભરપાઈ કરવો થાત; 2030 સુધીમાં 500 GW બિન-અશ્મીય ક્ષમતા અને ઉત્સર્જન તીવ્રતામાં "
                 "45 % ઘટાડા સાથે 2070 એ વિકાસનો રસ્તો છે જે કાર્બન પણ ઘટાડે.")},
         {"q": T("Why is methane called a short-lived but powerful lever?",
                 "મિથેનને ટૂંકા આયુષ્યનો પણ શક્તિશાળી લિવર કેમ કહેવાય?"),
          "a": T("Methane absorbs about 28 times more heat than CO₂ over a century, but its lifetime in "
                 "the air is only about twelve years, because sunlight and the hydroxyl radical destroy "
                 "it. That short life is the good news: cutting a methane source gives almost the whole "
                 "benefit within a decade, whereas a CO₂ cut accumulates slowly. It is therefore the "
                 "fastest way to slow the rate of warming and to reduce peak temperature, which is why "
                 "landfill capping, preventing gas leaks and better manure and paddy management appear "
                 "at the top of every cheap-abatement list.",
                 "મિથેન સદીમાં CO₂ કરતાં લગભગ 28 ગણી વધુ ઉષ્મા શોષે, પણ હવામાં તેનું આયુષ્ય ફક્ત લગભગ બાર વર્ષ છે, "
                 "કારણ કે સૂર્યપ્રકાશ અને હાઇડ્રોક્સિલ રેડિકલ તેને નષ્ટ કરે. તે ટૂંકું આયુષ્ય સારા સમાચાર છે: મિથેનનો "
                 "સ્રોત ઘટાડવાથી લગભગ આખો લાભ દાયકામાં મળે, જ્યારે CO₂નો ઘટાડો ધીમે એકઠો થાય. તેથી તે ગરમીનો દર "
                 "ધીમો કરવાનો અને ટોચનું તાપમાન ઘટાડવાનો સૌથી ઝડપી રસ્તો છે, અને તેથી જ કચરાભરાવ ઢાંકવો, ગેસ લીકેજ "
                 "અટકાવવું અને છાણ તથા ડાંગરનું સારું સંચાલન દરેક સસ્તા-ઘટાડાની યાદીમાં ટોચે આવે.")},
         {"q": T("What is climate justice?",
                 "જળવાયુ ન્યાય એટલે શું?"),
          "a": T("It is the observation that the people who caused least of the emissions suffer most of "
                 "the damage, and can afford least of the protection. A farmer in Kutch or Bihar faces "
                 "failed rain while a high-consuming household in a serviced city does not, and the "
                 "countries that industrialised first have already used most of the carbon budget. "
                 "Climate justice therefore argues for finance and technology transfer from rich to poor "
                 "countries, for loss-and-damage funds, and for the UNFCCC principle of common but "
                 "differentiated responsibilities and respective capabilities.",
                 "તે એ નિરીક્ષણ છે કે જેણે સૌથી ઓછું ઉત્સર્જન કર્યું તે સૌથી વધુ નુકસાન સહે છે અને સૌથી ઓછું "
                 "રક્ષણ પરવડી શકે છે. કચ્છ કે બિહારનો ખેડૂત નિષ્ફળ વરસાદ સહે જ્યારે સેવાવાળા શહેરનું વધુ વપરાશકર્તા "
                 "કુટુંબ નહીં, અને જેણે પહેલાં ઉદ્યોગીકરણ કર્યું તે દેશોએ કાર્બન બજેટનો મોટો ભાગ પહેલેથી વાપરી "
                 "લીધો છે. તેથી જળવાયુ ન્યાય શ્રીમંત દેશોમાંથી ગરીબ દેશો તરફ નાણું અને ટેક્નોલોજીના હસ્તાંતરણ, "
                 "નુકસાન-વળતર ફંડ અને UNFCCCના સમાન પણ ભિન્ન જવાબદારીઓ તથા સંબંધિત ક્ષમતાના સિદ્ધાંતની "
                 "વકીલાત કરે છે.")},
     ]},
]

_PRACTICE = [
    (T("Explain the greenhouse effect with a diagram and list the gases responsible.",
       "રેખાચિત્ર સાથે હરિતગૃહ પ્રભાવ સમજાવો અને જવાબદાર વાયુઓની યાદી આપો."), 5,
     [P("Draw the earth as a circle with three arrows in and three out. Incoming short-wave solar "
        "radiation brings about 340 W/m² at the top of the atmosphere. Roughly 100 W/m² is reflected by "
        "clouds, ice and deserts - the albedo - and about 240 W/m² is absorbed by the surface and the "
        "atmosphere. The warm surface emits long-wave infrared, of which about 390 W/m² leaves the "
        "surface, and the greenhouse gases absorb part of it in the lower atmosphere and re-emit half "
        "upwards and half downwards.",
        "પૃથ્વીને વર્તુળ તરીકે અને અંદર તથા બહાર ત્રણ તીર દોરો. આવતું ટૂંકા તરંગનું સૂર્યકિરણોત્સર્ગ વાતાવરણની ટોચે "
        "લગભગ 340 W/m² લાવે. લગભગ 100 W/m² વાદળ, બરફ અને રણ પરાવર્તિત કરે - આલ્બેડો - અને લગભગ "
        "240 W/m² સપાટી તથા વાતાવરણ શોષે. ગરમ સપાટી લાંબા તરંગનું ઇન્ફ્રારેડ ફેંકે, જેમાંથી લગભગ "
        "390 W/m² સપાટી છોડે, અને હરિતગૃહ વાયુ તેનો ભાગ નીચલા વાતાવરણમાં શોષી અડધો ઉપર અને અડધો નીચે ફેંકે."),
      P("The gases are those with three or more atoms per molecule, because such molecules can vibrate "
        "in bending modes that absorb infrared: water vapour (the largest absorber), carbon dioxide, "
        "methane, nitrous oxide, ozone and the fluorinated gases. Nitrogen and oxygen, with two atoms, "
        "are transparent to infrared, which is why 99 % of the atmosphere does not cause the effect.",
        "વાયુ તે છે જેમના પ્રતિ અણુ ત્રણ કે વધુ પરમાણુ હોય, કારણ કે તેવા અણુ વળાંક પ્રકારે કંપી ઇન્ફ્રારેડ શોષી "
        "શકે: પાણીની વરાળ (સૌથી મોટું શોષક), કાર્બન ડાયોક્સાઇડ, મિથેન, નાઇટ્રસ ઓક્સાઇડ, ઓઝોન અને ફ્લોરિનવાળા "
        "વાયુ. બે પરમાણુવાળા નાઇટ્રોજન અને ઓક્સિજન ઇન્ફ્રારેડ માટે પારદર્શક છે, તેથી જ વાતાવરણના 99 % "
        "પ્રભાવ ન કરે."),
      P("Quantitatively, the natural effect lifts the surface from −18 °C to 15 °C, a gain of 33 °C. "
        "Since 1750 the CO₂ concentration has gone from 280 to 420 ppm, adding 2.17 W/m² of forcing, and "
        "all the gases together add about 3 W/m². That looks small against 340 W/m², but it is a net "
        "imbalance of nearly 1 %, which is why the earth accumulates heat equal to several Hiroshima "
        "bombs per second.",
        "આંકડાકીય રીતે કુદરતી પ્રભાવ સપાટીને −18 °Cથી 15 °C કરે, એટલે 33 °Cનો લાભ. 1750થી CO₂ સાંદ્રતા "
        "280થી 420 ppm થઈ, 2.17 W/m² બળ ઉમેર્યું, અને બધા વાયુ ભેગા લગભગ 3 W/m² ઉમેરે. 340 W/m² સામે તે "
        "નાનું લાગે, પણ તે લગભગ 1 %નું ચોખ્ખું અસંતુલન છે, તેથી જ પૃથ્વી દર સેકન્ડે અનેક હિરોશિમા બોમ્બ જેટલી "
        "ઉષ્મા એકઠી કરે.")]),
    (T("Give five lines of evidence that the climate is changing and explain each.",
       "જળવાયુ બદલાઈ રહ્યું છે તેના પાંચ પુરાવા આપી દરેક સમજાવો."), 5,
     [P("Temperature: the instrumental record from 1850 shows +1.2 °C, with the ten warmest years all "
        "since 2010, and the warming is confirmed by proxies such as tree rings, ice cores and corals "
        "that extend the record 800,000 years. Ice: Arctic September sea ice has shrunk about 13 % a "
        "decade, mountain glaciers have lost mass every year since the 1980s, and the Greenland and "
        "Antarctic sheets are losing ice faster than they gain it.",
        "તાપમાન: 1850થી ઉપકરણ રેકોર્ડ +1.2 °C દર્શાવે, સૌથી ગરમ દસ વર્ષ 2010 પછીના છે, અને વૃક્ષવલય, બરફના "
        "નમૂના તથા પરવાળા જેવા પરોક્ષ પુરાવા રેકોર્ડને 8,00,000 વર્ષ સુધી લંબાવી તેની પુષ્ટિ કરે. બરફ: આર્કટિકનો "
        "સપ્ટેમ્બરનો દરિયાઈ બરફ દાયકે લગભગ 13 % ઘટ્યો, પર્વતીય હિમનદી 1980થી દર વર્ષે દળ ગુમાવે છે, અને "
        "ગ્રીનલેન્ડ તથા એન્ટાર્કટિકનાં પડ મેળવે તેના કરતાં ઝડપથી બરફ ગુમાવે છે."),
      P("Sea level: about 20 cm since 1900, now rising 4.5 mm a year, from thermal expansion, glacier "
        "melt and ice sheets - measured by tide gauges and since 1992 by satellite altimetry. "
        "Precipitation: the total monsoon rain is nearly unchanged but it arrives in fewer, heavier "
        "spells, and the number of rainy days has fallen, so dry spells are longer and floods sharper.",
        "દરિયા સપાટી: 1900થી લગભગ 20 cm, હવે વર્ષે 4.5 mm વધે, ઉષ્મીય વિસ્તરણ, હિમનદી પીગળવા અને બરફનાં પડમાંથી "
        "- ભરતી માપક અને 1992થી ઉપગ્રહ ઊંચાઈ માપનથી માપાય. વરસાદ: કુલ ચોમાસાનો વરસાદ લગભગ અબદલ છે પણ ઓછી, "
        "ભારે ઝાપટામાં આવે, અને વરસાદી દિવસોની સંખ્યા ઘટી, તેથી સૂકા સમય લાંબા અને પૂર વધુ તીવ્ર."),
      P("Extremes: heat waves are more frequent, longer and hotter; the number of record hot days "
        "exceeds record cold days by a wide margin; and the sea surface is warmer, so cyclones carry "
        "more moisture and stall longer. Underlying all five is the measured rise in greenhouse gases, "
        "which is the only driver that explains the pattern with height - a warming troposphere and a "
        "cooling stratosphere - that is actually observed.",
        "આત્યંતિક ઘટનાઓ: ગરમીની લહેરો વધુ વારંવાર, લાંબી અને ગરમ; રેકોર્ડ ગરમ દિવસો ઠંડા દિવસો કરતાં ઘણા વધુ; "
        "અને દરિયાની સપાટી ગરમ, તેથી વાવાઝોડું વધુ ભેજ લઈ જાય અને લાંબું થોભે. પાંચેયની નીચે માપેલો હરિતગૃહ "
        "વાયુનો વધારો છે, જે એકમાત્ર એવું કારણ છે જે ઊંચાઈ પ્રમાણેનો નમૂનો - ગરમ ટ્રોપોસ્ફિયર અને ઠંડું "
        "સ્ટ્રેટોસ્ફિયર - સમજાવે, જે ખરેખર જણાય છે.")]),
    (T("Describe the impacts of climate change on Indian agriculture, water and health.",
       "ભારતની ખેતી, પાણી અને આરોગ્ય પર જળવાયુ પરિવર્તનની અસરોનું વર્ણન કરો."), 5,
     [P("Agriculture: wheat is the most sensitive crop because it fills grain in February and March, "
        "exactly when the temperature is now rising fastest. Studies put the loss at about 5-7 % of "
        "wheat yield per degree of warming, with the Indo-Gangetic plain worst affected; rice is less "
        "sensitive but suffers from heat at flowering, and pulses and mustard lose from warm winters. "
        "Pests and diseases move to new areas, and the stubble-burning season now overlaps with "
        "earlier harvests.",
        "ખેતી: ઘઉં સૌથી સંવેદનશીલ પાક છે કારણ કે તે ફેબ્રુઆરી-માર્ચમાં દાણો ભરે, બરાબર જ્યારે તાપમાન હવે "
        "સૌથી ઝડપથી વધે છે. અભ્યાસ દરેક ડિગ્રી ગરમીે ઘઉંના ઉત્પાદનમાં લગભગ 5-7 % ખોટ દર્શાવે, જેમાં "
        "સૌથી વધુ અસર સિંધુ-ગંગાના મેદાન પર; ચોખા ઓછા સંવેદનશીલ પણ ફૂલ આવતી વખતે ગરમીથી પીડાય, અને કઠોળ તથા "
        "રાયડો ગરમ શિયાળાથી ગુમાવે. જીવાત અને રોગ નવા વિસ્તારોમાં જાય, અને પરાળ બાળવાની ઋતુ હવે વહેલી કાપણી "
        "સાથે મળી જાય છે."),
      P("Water: the Himalayan glaciers feed the Ganga, Indus and Brahmaputra in the pre-monsoon months, "
        "and their retreat first increases and then reduces that flow; groundwater is already falling "
        "in Punjab, Haryana and western Uttar Pradesh because evapotranspiration rises with "
        "temperature; and heavier rain in shorter spells means more runoff and less recharge, so the "
        "same annual total recharges the aquifer less.",
        "પાણી: હિમાલયની હિમનદી ચોમાસા પહેલાંના મહિનામાં ગંગા, સિંધુ અને બ્રહ્મપુત્રને પોષે, અને તેમનો ક્ષય પહેલાં "
        "પ્રવાહ વધારે પછી ઘટાડે; પંજાબ, હરિયાણા અને પશ્ચિમ ઉત્તર પ્રદેશમાં ભૂગર્ભજળ પહેલેથી ઘટે છે કારણ કે "
        "તાપમાન સાથે બાષ્પવાહન વધે; અને ઓછા સમયમાં વધુ ભારે વરસાદ એટલે વધુ વહી જવું અને ઓછું ભરાવું, તેથી એ જ "
        "વાર્ષિક કુલ જળાશયને ઓછું ભરે."),
      P("Health: heat waves kill the poorest first - outdoor workers, the elderly, slum residents under "
        "tin roofs - and the 2010 Ahmedabad and 2015 Andhra heat waves showed how a simple action plan "
        "saves lives. Warmer, wetter conditions extend the season and range of dengue, malaria and "
        "chikungunya; floods bring diarrhoea and leptospirosis; and air pollution, which shares the same "
        "fossil fuels, multiplies the harm. The economic cost appears as lost labour hours, lower "
        "yields and higher food prices.",
        "આરોગ્ય: ગરમીની લહેરો સૌથી ગરીબને પહેલાં મારે - બહારના કામદાર, વૃદ્ધો, પતરાની છત નીચેના ઝૂંપડપટ્ટીના "
        "રહેવાસી - અને 2010ના અમદાવાદ તથા 2015ના આંધ્રની ગરમીની લહેરોએ દર્શાવ્યું કે સાદી કાર્ય યોજના "
        "જીવ બચાવે. ગરમ, ભેજવાળી સ્થિતિ ડેન્ગ્યુ, મલેરિયા અને ચિકનગુનિયાની ઋતુ તથા વિસ્તાર લંબાવે; પૂર ઝાડા "
        "અને લેપ્ટોસ્પાઇરોસિસ લાવે; અને એ જ અશ્મી ઇંધણમાંથી આવતું વાયુ પ્રદૂષણ નુકસાનને ગુણકારે. આર્થિક ખર્ચ "
        "ગુમાવેલા શ્રમ કલાક, ઓછા ઉત્પાદન અને વધુ ખાદ્ય ભાવ તરીકે દેખાય.")]),
    (T("List the mitigation options for greenhouse gases in order of cost and explain any three.",
       "હરિતગૃહ વાયુ માટેના શમન વિકલ્પો ખર્ચના ક્રમમાં ગણાવો અને કોઈ પણ ત્રણ સમજાવો."), 5,
     [P("Cheapest first: energy efficiency in buildings, industry and appliances; methane capture from "
        "landfills, coal mines and gas leaks; solar and wind generation; fuel switching from coal to gas "
        "where a plant is young; electrification of two and three wheelers, buses and low-temperature "
        "process heat; afforestation and soil carbon; then, most expensive, carbon capture on cement and "
        "steel, green hydrogen for steel and fertiliser, and direct air capture.",
        "સૌથી સસ્તું પહેલાં: ઇમારત, ઉદ્યોગ અને સાધનોમાં ઊર્જા કાર્યક્ષમતા; કચરાભરાવ, કોલસાની ખાણ અને ગેસ "
        "લીકેજમાંથી મિથેન પકડ; સૌર અને પવન ઉત્પાદન; નવું હોય તેવા સ્ટેશનમાં કોલસાથી ગેસ તરફ ઇંધણ બદલો; બે "
        "અને ત્રણ પૈડાં, બસ તથા નીચા તાપમાનની પ્રક્રિયા ઉષ્માનું વીજીકરણ; વનરોપણ અને જમીન કાર્બન; પછી સૌથી મોંઘું "
        "- સિમેન્ટ અને પોલાદ પર કાર્બન પકડ, પોલાદ-ખાતર માટે લીલું હાઇડ્રોજન અને હવામાંથી સીધું પકડ."),
      P("Methane capture: a landfill or a coal mine releases methane for decades. Covering the waste, "
        "flaring the gas or burning it in a small engine converts CH₄ to CO₂, and since GWP is 28 the "
        "climate benefit per tonne is large for a small cost; a single well-run landfill can cut "
        "thousands of tonnes of CO₂e a year. It is the classic example of a cheap, fast win.",
        "મિથેન પકડ: કચરાભરાવ કે કોલસાની ખાણ દાયકાઓ સુધી મિથેન છોડે. કચરો ઢાંકવો, ગેસ બાળવો કે નાના એન્જિનમાં "
        "બાળવો CH₄ને CO₂માં ફેરવે, અને GWP 28 હોવાથી ટન દીઠ જળવાયુ લાભ ઓછા ખર્ચે મોટો થાય; એક સારી રીતે ચાલતો "
        "કચરાભરાવ વર્ષે હજારો ટન CO₂e ઘટાડે. સસ્તા, ઝડપી લાભનું તે ઉત્તમ ઉદાહરણ છે."),
      P("Solar and wind: the levelised cost is now 2.5-3.8 rupees a unit against 4.5-6 for new coal, "
        "so the switch is an economic decision as much as a climate one; the constraint is not cost but "
        "the grid, storage and land. CCS: essential for cement and steel where the CO₂ comes from "
        "chemistry, but it consumes 20-30 % of the plant's energy and is still expensive. The honest "
        "conclusion is that the first six options can deliver most of the cut needed by 2030 and CCS is "
        "needed for the last hard 15 %.",
        "સૌર અને પવન: સમતુલિત ખર્ચ હવે યુનિટના 2.5-3.8 રૂપિયા, નવા કોલસાના 4.5-6 સામે, તેથી બદલો જળવાયુ જેટલો "
        "આર્થિક નિર્ણય પણ છે; મર્યાદા ખર્ચ નહીં, ગ્રિડ, સંગ્રહ અને જમીન છે. CCS: સિમેન્ટ અને પોલાદ માટે આવશ્યક "
        "જ્યાં CO₂ રસાયણમાંથી આવે, પણ તે સ્ટેશનની 20-30 % ઊર્જા ખાય અને હજી મોંઘું છે. પ્રામાણિક નિષ્કર્ષ એ છે કે "
        "પ્રથમ છ વિકલ્પો 2030 સુધીમાં જરૂરી ઘટાડાનો મોટો ભાગ આપી શકે અને છેલ્લા કઠિન 15 % માટે CCS જોઈએ.")]),
    (T("What is climate sensitivity and why is its range so wide?",
       "જળવાયુ સંવેદનશીલતા શું છે અને તેની શ્રેણી આટલી પહોળી કેમ છે?"), 4,
     [P("Climate sensitivity is the equilibrium warming caused by a doubling of CO₂, usually quoted as "
        "the range 1.5-4.5 °C with a best estimate near 3 °C. It is a property of the planet, not of the "
        "emissions path: it says how much warming one unit of forcing finally produces once the oceans "
        "and ice have caught up, which takes centuries for some parts.",
        "જળવાયુ સંવેદનશીલતા એ CO₂ બમણું થવાથી થતી સંતુલન ગરમી છે, સામાન્ય રીતે 1.5-4.5 °C શ્રેણી અને લગભગ "
        "3 °C શ્રેષ્ઠ અંદાજ તરીકે કહેવાય. તે ગ્રહનો ગુણધર્મ છે, ઉત્સર્જન માર્ગનો નહીં: તે કહે છે કે બળના એક એકમથી "
        "આખરે કેટલી ગરમી થાય, જ્યારે મહાસાગર અને બરફ પકડી લે, જે કેટલાક ભાગોમાં સદીઓ લે."),
      P("The range is wide because of the feedbacks. The strongest, water vapour, roughly doubles the "
        "direct warming and is well measured. The cloud feedback is the uncertain one: low clouds "
        "reflect sunlight and cool, high thin clouds trap heat and warm, and models disagree on how the "
        "balance shifts as the pattern of sea surface temperature changes. Ice-albedo and permafrost "
        "carbon add further positive feedback, and each uncertainty multiplies into the final number.",
        "શ્રેણી પહોળી છે કારણ કે પ્રતિસંદર્શ છે. સૌથી શક્તિશાળી પાણીની વરાળ સીધી ગરમી લગભગ બમણી કરે અને સારી "
        "રીતે માપાય છે. વાદળનો પ્રતિસંદર્શ અનિશ્ચિત છે: નીચલા વાદળ સૂર્યપ્રકાશ પરાવર્તિત કરી ઠંડક આપે, ઊંચા પાતળા "
        "વાદળ ઉષ્મા રોકી ગરમી આપે, અને દરિયાની સપાટીના તાપમાનનો નમૂનો બદલાતાં સંતુલન કેવી રીતે ખસે તેમાં "
        "નમૂનાઓ સહમત નથી. બરફ-આલ્બેડો અને કાયમી ઠંડી જમીનનો કાર્બન વધુ ધન પ્રતિસંદર્શ ઉમેરે, અને દરેક અનિશ્ચિતતા "
        "અંતિમ આંકડામાં ગુણાકાર કરે."),
      P("The number matters for policy. At 2 °C per doubling, a 2 °C target allows a larger carbon "
        "budget and slower action; at 4.5 °C, even the present concentration already commits us to "
        "dangerous change. That is why the uncertainty is not a reason to wait - it is a reason to "
        "insure, because the downside is much worse than the upside is good.",
        "આંકડો નીતિ માટે મહત્ત્વનો છે. પ્રતિ બમણા 2 °C પર, 2 °Cનું લક્ષ્ય મોટું કાર્બન બજેટ અને ધીમી કાર્યવાહી "
        "પરવડે; 4.5 °C પર, હાલની સાંદ્રતા પણ આપણને ખતરનાક પરિવર્તન માટે બંધાયેલા કરે. તેથી જ અનિશ્ચિતતા "
        "રાહ જોવાનું કારણ નથી - તે વીમો લેવાનું કારણ છે, કારણ કે નુકસાનની બાજુ લાભની બાજુ કરતાં ઘણી ખરાબ છે.")]),
    (T("Explain carbon capture and storage with a block diagram and its limitations.",
       "બ્લોક ડાયાગ્રામ સાથે કાર્બન પકડ અને સંગ્રહ તથા તેની મર્યાદા સમજાવો."), 4,
     [P("The chain has four blocks: capture, compression, transport and storage. Capture is done in "
        "three ways - post-combustion, where an amine solvent absorbs CO₂ from the flue gas and is "
        "regenerated with heat; pre-combustion, where the fuel is turned into hydrogen and CO₂ before "
        "burning, as in an IGCC plant; and oxy-fuel, where the fuel is burnt in pure oxygen so the flue "
        "gas is almost pure CO₂ and needs no separation.",
        "શૃંખલામાં ચાર બ્લોક છે: પકડ, દબાવટ, વહન અને સંગ્રહ. પકડ ત્રણ રીતે થાય - દહન પછી, જ્યાં એમાઇન દ્રાવક "
        "ધુમાડામાંથી CO₂ શોષે અને ઉષ્માથી ફરી મુક્ત થાય; દહન પહેલાં, જ્યાં ઇંધણ બાળતાં પહેલાં હાઇડ્રોજન અને CO₂માં "
        "ફેરવાય, જેમ કે IGCC સ્ટેશનમાં; અને ઓક્સી-ફ્યુઅલ, જ્યાં ઇંધણ શુદ્ધ ઓક્સિજનમાં બળે તેથી ધુમાડો લગભગ શુદ્ધ CO₂ "
        "હોય અને અલગ કરવો ન પડે."),
      P("The captured CO₂ is dried and compressed to about 100 bar, when it becomes a dense "
        "supercritical fluid that can be pumped like a liquid. It travels by pipeline, often hundreds of "
        "kilometres, and is injected 1-3 km down into a saline aquifer or a depleted oil or gas field, "
        "where a cap rock of shale or salt seals it; monitoring wells check that it stays. Storage "
        "capacity worldwide is estimated in thousands of gigatonnes, far more than the emissions of a "
        "century.",
        "પકડાયેલું CO₂ સૂકવી લગભગ 100 bar સુધી દબાવાય, જ્યારે તે ગાઢ અતિક્રાંતિક પ્રવાહી બને જે પ્રવાહીની જેમ "
        "પંપાય. તે પાઇપલાઇનથી, ઘણી વાર સેંકડો કિલોમીટર, જાય અને 1-3 km નીચે ખારા જળાશય કે ખાલી તેલ-ગેસ ક્ષેત્રમાં "
        "દબાવાય, જ્યાં શેલ કે મીઠાનો ઢાંકણ ખડક સીલ કરે; દેખરેખ કૂવા તેને રહેવાની ખાતરી કરે. દુનિયાભરની સંગ્રહ ક્ષમતા "
        "હજારો ગીગાટન આંકાય છે, જે સદીના ઉત્સર્જન કરતાં ઘણી વધુ."),
      P("Limitations: the capture unit costs 20-30 % of the plant's output, so more coal is burnt for "
        "the same electricity; capture is 85-95 %, so 5-15 % escapes; the amine solvent degrades and "
        "needs replacing; pipeline and storage need capital and public acceptance; and CCS is a "
        "reason to keep burning fuel, so it must not displace cheaper efficiency and renewables. Its "
        "true niche is cement and steel, where 50-60 % of the CO₂ comes from the process chemistry and "
        "cannot be avoided by changing the fuel.",
        "મર્યાદા: પકડ એકમ સ્ટેશનના ઉત્પાદનના 20-30 % ખર્ચે, તેથી એ જ વીજળી માટે વધુ કોલસો બળે; પકડ 85-95 % છે, "
        "તેથી 5-15 % નીકળે; એમાઇન દ્રાવક બગડે અને બદલવો પડે; પાઇપલાઇન અને સંગ્રહને મૂડી તથા લોકસ્વીકૃતિ જોઈએ; "
        "અને CCS ઇંધણ બાળવાનું કારણ બને, તેથી તે સસ્તી કાર્યક્ષમતા અને પુનઃપ્રાપ્યને હટાવવું ન જોઈએ. તેની ખરી જગ્યા "
        "સિમેન્ટ અને પોલાદ છે, જ્યાં 50-60 % CO₂ પ્રક્રિયા રસાયણમાંથી આવે અને ઇંધણ બદલીને ટાળી ન શકાય.")]),
    (T("A city wants to reach net zero. Prepare a ten-point plan with a rough priority order.",
       "એક શહેર નેટ ઝીરો પામવા માંગે છે. અંદાજિત પ્રાથમિકતા ક્રમ સાથે દસ મુદ્દાની યોજના બનાવો."), 5,
     [P("1. Measure: build a greenhouse gas inventory for electricity, transport, buildings, waste and "
        "industry, because you cannot manage what you do not measure. 2. Efficiency first: LED street "
        "lighting, five-star appliances, insulation and cool roofs, which cut demand 15-25 % before any "
        "new supply is built. 3. Rooftop and ground solar with net metering, using the 500 m² of every "
        "school and hospital. 4. Electrify the bus fleet and the two and three wheelers, with charging "
        "at depots.",
        "1. માપો: વીજળી, વાહનવ્યવહાર, ઇમારત, કચરો અને ઉદ્યોગ માટે હરિતગૃહ વાયુ ગણતરી બનાવો, કારણ કે જે માપી "
        "ન શકાય તેનું સંચાલન ન થાય. 2. પહેલાં કાર્યક્ષમતા: LED શેરી દીવા, પાંચ સ્ટાર સાધનો, ઇન્સ્યુલેશન અને "
        "ઠંડી છત, જે કોઈ નવો પુરવઠો બાંધતાં પહેલાં માંગ 15-25 % ઘટાડે. 3. નેટ મીટરિંગ સાથે છત અને જમીન પરનું સૌર, "
        "દરેક શાળા અને હોસ્પિટલની 500 m² વાપરીને. 4. ડેપો પર ચાર્જિંગ સાથે બસ સેવા તથા બે અને ત્રણ પૈડાંનું "
        "વીજીકરણ."),
      P("5. Waste: segregate at source, compost the wet half, and capture landfill gas - the cheapest "
        "tonne in the plan. 6. Water: pump with solar, repair leaks, and recharge with rainwater "
        "harvesting, because pumping is the city's largest single electricity load. 7. Buildings: make "
        "the green building code mandatory for new construction above 500 m² under the local "
        "rating system. 8. Industry: waste heat recovery, efficient boilers and a cluster-level "
        "common facility.",
        "5. કચરો: સ્રોત પર અલગ કરો, ભીનો અડધો ખાતર બનાવો અને કચરાભરાવનો ગેસ પકડો - યોજનાનું સૌથી સસ્તું ટન. "
        "6. પાણી: સૌરથી પંપ ચલાવો, લીકેજ સુધારો અને વરસાદી જળ સંગ્રહથી ભરાવો, કારણ કે પંપ શહેરનો સૌથી મોટો "
        "એક વીજ ભાર છે. 7. ઇમારત: 500 m²થી મોટા નવા બાંધકામ માટે સ્થાનિક રેટિંગ પ્રણાલી હેઠળ લીલા ઇમારત "
        "નિયમાવલી ફરજિયાત કરો. 8. ઉદ્યોગ: કચરા ઉષ્માનો પુનઃઉપયોગ, કાર્યક્ષમ બોઇલર અને ક્લસ્ટર સ્તરે સામાન્ય સુવિધા."),
      P("9. Sinks: protect and expand the city forest, plant along roads and canals, and turn the "
        "landfill into a park once it is capped. 10. Governance and money: a climate cell with a "
        "budget, green municipal bonds, a carbon registry and an annual public report. The order "
        "matters: measurement and efficiency first, because they pay for themselves and make every "
        "later step smaller, and offsets last, because a city that buys credits without cutting its own "
        "emissions has not reached net zero.",
        "9. શોષક: શહેરી વન સાચવો અને વધારો, રસ્તા અને કેનાલ પર વાવો, અને ઢાંક્યા પછી કચરાભરાવને બગીચો બનાવો. "
        "10. શાસન અને નાણું: બજેટ સાથે જળવાયુ કોષ, લીલા નગરપાલિકા બોન્ડ, કાર્બન નોંધ અને વાર્ષિક જાહેર અહેવાલ. "
        "ક્રમ મહત્ત્વનો છે: પહેલાં માપન અને કાર્યક્ષમતા, કારણ કે તે પોતાનો ખર્ચ કાઢે અને પછીનું દરેક પગલું નાનું "
        "કરે, અને ઓફસેટ છેલ્લે, કારણ કે પોતાનું ઉત્સર્જન ઘટાડ્યા વગર ક્રેડિટ ખરીદતું શહેર નેટ ઝીરો પામ્યું નથી.")]),
    (T("Explain the evidence for sea level rise and its threat to Indian coastal cities.",
       "દરિયા સપાટીના વધારાના પુરાવા અને ભારતીય કિનારાનાં શહેરો માટેના જોખમને સમજાવો."), 4,
     [P("Evidence: tide gauges show about 20 cm since 1900; satellite altimetry since 1992 shows the "
        "rate has doubled to 4.5 mm a year; the three contributors are measured separately - thermal "
        "expansion 1.4 mm, glaciers 0.8 mm, ice sheets 0.8 mm - and the budget closes, which is what "
        "makes the result trustworthy. Gravity satellites show Greenland losing about 250 Gt of ice a "
        "year and Antarctica about 150 Gt.",
        "પુરાવા: ભરતી માપક 1900થી લગભગ 20 cm દર્શાવે; 1992થી ઉપગ્રહ ઊંચાઈ માપન દર વર્ષે 4.5 mm સુધી બમણો થયો "
        "દર્શાવે; ત્રણ ફાળાવાળા ઘટક અલગ માપાય - ઉષ્મીય વિસ્તરણ 1.4 mm, હિમનદી 0.8 mm, બરફનાં પડ 0.8 mm - અને "
        "ગણતરી મળી જાય, તેથી જ પરિણામ ભરોસાપાત્ર બને. ગુરુત્વ ઉપગ્રહ ગ્રીનલેન્ડ વર્ષે લગભગ 250 Gt અને "
        "એન્ટાર્કટિકા લગભગ 150 Gt બરફ ગુમાવતું દર્શાવે."),
      P("Threat to India: 7,500 km of coast, 40 % of the population within 100 km of the sea, and "
        "twelve major ports. Mumbai's reclaimed land and its storm-water drains, Surat's Tapi estuary, "
        "Kochi's backwaters and Chennai's beaches all face three hazards together: tidal flooding on "
        "spring tides, salt water pushing into the coastal aquifer as the sea rises, and stronger "
        "cyclone surge. A 0.5 m rise is expected to put about 35 million Indians at risk of "
        "once-a-century flooding.",
        "ભારત માટે જોખમ: 7,500 km કિનારો, 40 % વસ્તી દરિયાથી 100 kmમાં અને બાર મોટાં બંદર. મુંબઈની ભરાવટવાળી "
        "જમીન અને વરસાદી ગટર, સુરતનું તાપી મુખ, કોચીનું કાલ કેનાલ અને ચેન્નાઈના દરિયાકિનારા ત્રણ જોખમ સાથે મળે "
        "છે: અમાસ-પૂનમની ભરતીનું પૂર, દરિયો વધતાં કિનારાના જળાશયમાં ખારું પાણી ઘૂસવું અને વધુ તાકાતવાન વાવાઝોડાની "
        "ભરતી. 0.5 m વધારો લગભગ 3.5 કરોડ ભારતીયોને સદીમાં એક વારના પૂરના જોખમમાં મૂકશે તેમ અપેક્ષિત છે."),
      P("Response: a mix of protection, accommodation and retreat. Protection means sea walls, "
        "embankments and mangrove belts, as in the Sundarbans where mangroves absorb surge energy. "
        "Accommodation means raised plinths, flood-proof drainage, salt-tolerant crops and early "
        "warning. Retreat means no new construction in the highest-risk zones, with planned relocation "
        "rather than a rushed evacuation after the next flood.",
        "પ્રતિસાદ: રક્ષણ, અનુકૂલન અને પીછેહઠનું મિશ્રણ. રક્ષણ એટલે દરિયાની દીવાલ, બંધ અને કાંદાના પટ્ટા, જેમ કે "
        "સુંદરબનમાં જ્યાં કાંદા ભરતીની ઊર્જા શોષે. અનુકૂલન એટલે ઊંચા પાયા, પૂર-પ્રતિરોધી ગટર, ખારા-સહિષ્ણુ પાક અને "
        "વહેલી ચેતવણી. પીછેહઠ એટલે સૌથી વધુ જોખમવાળા વિસ્તારોમાં નવું બાંધકામ નહીં, અને આગલા પૂર પછીની ઉતાવળી "
        "ખાલી કરાવવાને બદલે યોજનાબદ્ધ સ્થળાંતર.")]),
    (T("What is extreme event attribution? Answer with one heat wave and one rainfall example.",
       "આત્યંતિક ઘટના કારણ નિર્ધારણ શું છે? એક ગરમીની લહેર અને એક વરસાદના ઉદાહરણ સાથે જવાબ આપો."), 4,
     [P("Attribution asks a conditional question: given the world as it is, how did greenhouse warming "
        "change the probability or the intensity of this event? The method runs two large ensembles of "
        "a climate model - one with the actual greenhouse gas concentrations, one with pre-industrial "
        "concentrations - and compares how often an event of that size occurs in each. The answer is a "
        "ratio or a percentage, not a yes or no.",
        "કારણ નિર્ધારણ શરતી પ્રશ્ન પૂછે: આજની દુનિયામાં હરિતગૃહ ગરમીએ આ ઘટનાની શક્યતા કે તીવ્રતા કેવી રીતે બદલી? "
        "આ રીત જળવાયુ નમૂનાના બે મોટા સમૂહ ચલાવે - એક વાસ્તવિક હરિતગૃહ વાયુ સાંદ્રતા સાથે, એક ઉદ્યોગ પહેલાંની "
        "સાંદ્રતા સાથે - અને દરેકમાં તે માપની ઘટના કેટલી વાર આવે તે સરખાવે. જવાબ હા કે ના નહીં, ગુણોત્તર કે "
        "ટકા હોય."),
      P("Heat wave example: the 2022 India-Pakistan pre-monsoon heat, with 49 °C in Delhi in April, was "
        "found to be about thirty times more likely and about 1 °C hotter because of human-caused "
        "warming. The physics is direct: the baseline temperature is higher, so the same weather pattern "
        "produces a more extreme maximum.",
        "ગરમીની લહેરનું ઉદાહરણ: 2022ના ભારત-પાકિસ્તાનના ચોમાસા પહેલાંની ગરમીમાં દિલ્હીમાં એપ્રિલમાં 49 °C, "
        "માનવજન્ય ગરમીને કારણે લગભગ ત્રીસ ગણી વધુ શક્ય અને લગભગ 1 °C વધુ ગરમ મળી. ભૌતિકશાસ્ત્ર સીધું છે: "
        "આધાર તાપમાન ઊંચું હોવાથી એ જ હવામાન નમૂનો વધુ તીવ્ર મહત્તમ બનાવે."),
      P("Rainfall example: in the 2018 Kerala floods, attribution studies found that the heaviest "
        "three-day totals were about 6-18 % heavier than they would have been without warming, because "
        "the air held more moisture. Note the wording in both cases: the event still happened because "
        "of a weather pattern, and warming changed its odds or its size. That is exactly the statement "
        "the IPCC makes, and it is why a single flood is not proof but a thousand floods are a pattern.",
        "વરસાદનું ઉદાહરણ: 2018ના કેરળ પૂરમાં કારણ નિર્ધારણ અભ્યાસે જણાવ્યું કે સૌથી ભારે ત્રણ દિવસનો કુલ "
        "વરસાદ ગરમી વગર કરતાં લગભગ 6-18 % વધુ ભારે હતો, કારણ કે હવામાં વધુ ભેજ હતો. બંને કિસ્સામાં શબ્દો ધ્યાનમાં "
        "લો: ઘટના હજી હવામાનના નમૂનાને કારણે થઈ, અને ગરમીએ તેની શક્યતા કે માપ બદલ્યું. IPCC બરાબર એ જ વિધાન કરે "
        "છે, અને તેથી જ એક પૂર પુરાવો નથી પણ હજાર પૂર એક નમૂનો છે.")]),
    (T("Explain the difference between the ozone hole and global warming.",
       "ઓઝોન છિદ્ર અને વૈશ્વિક ગરમી વચ્ચેનો ફરક સમજાવો."), 3,
     [P("They are two different problems that are often confused. The ozone hole is a thinning of the "
        "stratospheric ozone layer 15-35 km up, caused by chlorofluorocarbons. It lets more harmful "
        "ultraviolet-B radiation reach the ground, raising skin cancer and crop damage, and it is worst "
        "over Antarctica in spring. Global warming is the trapping of outgoing infrared radiation in the "
        "troposphere by greenhouse gases.",
        "તે બે જુદી સમસ્યા છે જે ઘણી વાર ભેગી થાય. ઓઝોન છિદ્ર 15-35 km ઉપરના સ્ટ્રેટોસ્ફિયરના ઓઝોન સ્તરનું "
        "પાતળું થવું છે, જે ક્લોરોફ્લોરોકાર્બનથી થાય. તે વધુ હાનિકારક પારજાંબલી-B કિરણો જમીન સુધી પહોંચવા દે, "
        "જે ત્વચાના કેન્સર અને પાકના નુકસાનને વધારે, અને વસંતમાં એન્ટાર્કટિકા પર સૌથી વધુ હોય. વૈશ્વિક ગરમી "
        "ટ્રોપોસ્ફિયરમાં હરિતગૃહ વાયુ દ્વારા બહાર જતા ઇન્ફ્રારેડ કિરણોને રોકવાની છે."),
      P("The links are indirect. CFCs are themselves potent greenhouse gases, so phasing them out under "
        "the Montreal Protocol also slowed warming - the single most successful environmental treaty. "
        "And a cooler stratosphere, which greenhouse warming produces, makes polar ozone depletion "
        "slightly worse. But ozone does not cause global warming and cutting CO₂ will not repair the "
        "ozone layer; each problem needed its own treaty and its own control measure.",
        "સંબંધ પરોક્ષ છે. CFC પોતે શક્તિશાળી હરિતગૃહ વાયુ છે, તેથી મોન્ટ્રિયલ પ્રોટોકોલ હેઠળ તેમને દૂર કરવાથી "
        "ગરમી પણ ધીમી પડી - સૌથી સફળ પર્યાવરણ સંધિ. અને હરિતગૃહ ગરમી ઉત્પન્ન કરતું ઠંડું સ્ટ્રેટોસ્ફિયર ધ્રુવીય "
        "ઓઝોન ક્ષયને થોડો વધારે. પણ ઓઝોન વૈશ્વિક ગરમીનું કારણ નથી અને CO₂ ઘટાડવાથી ઓઝોન સ્તર સુધરશે નહીં; દરેક "
        "સમસ્યાને પોતાની સંધિ અને પોતાનું નિયંત્રણ પગલું જોઈએ.")]),
    (T("Why is adaptation necessary even if mitigation succeeds?",
       "શમન સફળ થાય તો પણ અનુકૂલન કેમ આવશ્યક છે?"), 4,
     [P("Because of the lag in the system. The ocean has absorbed more than 90 % of the extra heat, and "
        "it releases it slowly, so about 0.5 °C of further warming is already locked in even if "
        "emissions stopped today; sea level will keep rising for centuries because the ice sheets "
        "respond over hundreds of years. Mitigation decides how bad it gets after 2050; adaptation "
        "decides how many people are hurt before then.",
        "પ્રણાલીના વિલંબને કારણે. મહાસાગરે વધારાની 90 %થી વધુ ઉષ્મા શોષી છે અને તે ધીમે છોડે, તેથી આજે ઉત્સર્જન "
        "બંધ થાય તો પણ લગભગ 0.5 °C વધુ ગરમી પહેલેથી નિશ્ચિત છે; દરિયા સપાટી સદીઓ સુધી વધતી રહેશે કારણ કે બરફનાં "
        "પડ સેંકડો વર્ષમાં પ્રતિક્રિયા આપે. શમન નક્કી કરે કે 2050 પછી કેટલું ખરાબ થશે; અનુકૂલન નક્કી કરે કે ત્યાં "
        "સુધીમાં કેટલા લોકોને નુકસાન થશે."),
      P("Adaptation is also cheaper. A heat action plan in Ahmedabad cost about one crore rupees and "
        "saved an estimated 1,100 lives in its first decade; a sea wall costs a fraction of the damage "
        "from one flood; drought-resistant seed and micro-irrigation protect a farmer's whole income. "
        "And adaptation buys time for mitigation to work - a city that floods every year spends its "
        "budget on repair instead of on the transition.",
        "અનુકૂલન સસ્તું પણ છે. અમદાવાદની ગરમી કાર્ય યોજના લગભગ એક કરોડ રૂપિયાની થઈ અને પ્રથમ દાયકામાં અંદાજે "
        "1,100 જીવ બચાવ્યા; દરિયાની દીવાલ એક પૂરના નુકસાનના થોડા ભાગમાં પડે; દુષ્કાળ-સહિષ્ણુ બીજ અને સૂક્ષ્મ સિંચાઈ "
        "ખેડૂતની આખી આવક બચાવે. અને અનુકૂલન શમનને કામ કરવા સમય આપે - દર વર્ષે પૂરમાં ડૂબતું શહેર તેનું બજેટ "
        "સુધારણા પર ખર્ચે, સંક્રમણ પર નહીં.")]),
    (T("State India's climate commitments and the three numbers behind them.",
       "ભારતની જળવાયુ પ્રતિબદ્ધતાઓ અને તેમની પાછળના ત્રણ આંકડા જણાવો."), 4,
     [P("India's updated Nationally Determined Contribution and the Panchamrit pledges of 2021 are "
        "usually summarised as five numbers: 500 GW of non-fossil electricity capacity by 2030; 50 % of "
        "installed capacity from non-fossil sources by 2030; a 1 billion tonne reduction in projected "
        "CO₂ by 2030; a 45 % cut in emission intensity of GDP against 2005 by 2030; and net zero by "
        "2070. It has also led the International Solar Alliance and the LiFE mission on lifestyle.",
        "ભારતનું અદ્યતન રાષ્ટ્રીય નિર્ધારિત યોગદાન અને 2021ના પંચામૃત વચન સામાન્ય રીતે પાંચ આંકડામાં "
        "સારાંશાય: 2030 સુધીમાં 500 GW બિન-અશ્મીય વીજ ક્ષમતા; 2030 સુધીમાં સ્થાપિત ક્ષમતાના 50 % બિન-અશ્મીય સ્રોતમાંથી; "
        "2030 સુધીમાં અંદાજિત CO₂માં 1 અબજ ટન ઘટાડો; 2030 સુધીમાં 2005 સામે GDPની ઉત્સર્જન તીવ્રતામાં 45 % ઘટાડો; "
        "અને 2070 સુધીમાં નેટ ઝીરો. તેણે આંતરરાષ્ટ્રીય સૌર ગઠબંધન અને જીવનશૈલી પર LiFE મિશનનું નેતૃત્વ પણ કર્યું છે."),
      P("The three numbers that decide whether the pledges are real are money, land and grid. Money: "
        "about 2.5-3 lakh crore rupees a year of investment is needed for the 500 GW, and most must "
        "come from private capital, which needs stable auctions and payment security. Land: 500 GW of "
        "solar alone needs about 8,000 km², so rooftop, agrivoltaics and wasteland matter. Grid: the "
        "inter-state transmission system and storage must grow with the plants, or the capacity is "
        "built and not used.",
        "વચનો ખરાં છે કે નહીં તે નક્કી કરતા ત્રણ આંકડા નાણું, જમીન અને ગ્રિડ છે. નાણું: 500 GW માટે વર્ષે લગભગ "
        "2.5-3 લાખ કરોડ રૂપિયાનું રોકાણ જોઈએ, અને મોટો ભાગ ખાનગી મૂડીમાંથી આવવો જોઈએ, જેને સ્થિર હરાજી અને "
        "ચુકવણી સુરક્ષા જોઈએ. જમીન: ફક્ત 500 GW સૌરને લગભગ 8,000 km² જોઈએ, તેથી છત, કૃષિ-સૌર અને બંજર જમીન "
        "મહત્ત્વનાં. ગ્રિડ: આંતર-રાજ્ય ટ્રાન્સમિશન પ્રણાલી અને સંગ્રહ સ્ટેશનો સાથે વધવાં જોઈએ, નહીં તો ક્ષમતા "
        "બનશે પણ વપરાશે નહીં.")]),
]

EXAM = [{"q": q, "marks": m} for q, m, _parts in _PRACTICE]
PRACTICE_ANSWERS = [_join(parts) for _q, _m, parts in _PRACTICE]
LESSON_COUNT = sum(len(s["items"]) for s in NOTES)
