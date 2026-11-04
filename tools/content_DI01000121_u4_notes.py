"""DI01000121 Applied Physics - Unit 4: Heat and Thermometry (bilingual en + gu).

GTU 4.1-4.7, 8 h, 17 %, 12 marks, CO4.
"""
from content_DI01000121_u1_notes import T, P, H4, UL, OL, TB, card, num, _join

SOURCES = [
    T("GTU DI01000121 Applied Physics syllabus (uploaded PDF, w.e.f. 2024-25)",
      "GTU DI01000121 એપ્લાઇડ ફિઝિક્સ સિલેબસ (અપલોડ કરેલ PDF, 2024-25થી અમલમાં)"),
    T("NCERT Physics Class XI, Part II - Thermal Properties of Matter",
      "NCERT ભૌતિક વિજ્ઞાન ધોરણ 11, ભાગ 2 - દ્રવ્યના ઉષ્મીય ગુણધર્મો"),
    T("H. C. Verma - Concepts of Physics, Vol. II, chapters 23 and 24",
      "એચ. સી. વર્મા - કોન્સેપ્ટ્સ ઓફ ફિઝિક્સ, ભાગ 2, પ્રકરણ 23 અને 24"),
    T("M. N. Avadhanulu - A Textbook of Engineering Physics, heat transfer chapter",
      "એમ. એન. અવધાનુલુ - ટેક્સ્ટબુક ઓફ એન્જિનિયરિંગ ફિઝિક્સ, ઉષ્મા સંક્રમણ પ્રકરણ"),
    T("IS 4825 and manufacturer data for bimetallic and mercury-in-glass thermometers",
      "બાયમેટાલિક અને પારા-કાચ થર્મોમીટર માટે IS 4825 અને ઉત્પાદકના આંકડા"),
]

NOTES = [
    {"title": T("1. Heat, Temperature and the Modes of Transfer", "1. ઉષ્મા, તાપમાન અને સંક્રમણની રીતો"),
     "items": [
         card(T("1.1 Heat and temperature are not the same thing",
                "1.1 ઉષ્મા અને તાપમાન એક જ વસ્તુ નથી"),
              [H4("Definitions", "વ્યાખ્યાઓ"),
               P("<b>Heat</b> is energy in transit because of a temperature difference; its unit is the "
                 "joule (J) and the older unit is the calorie (1 cal = 4.186 J). <b>Temperature</b> is "
                 "the degree of hotness that decides the direction of that flow, measured in kelvin (K).",
                 "<b>ઉષ્મા</b> એ તાપમાનના તફાવતને કારણે સ્થાનાંતરિત થતી ઊર્જા છે; તેનો એકમ જૂલ (J) અને "
                 "જૂનો એકમ કેલરી (1 cal = 4.186 J) છે. <b>તાપમાન</b> એ ગરમીનું માપ છે જે સંક્રમણની દિશા "
                 "નક્કી કરે, કેલ્વિન (K) માં મપાય."),
               H4("Why the difference matters", "તફાવત કેમ મહત્ત્વનો"),
               TB([T("Statement", "વિધાન"), T("True or false", "સાચું કે ખોટું")],
                  [[T("a bucket of water at 60 °C has more heat than a spoon at 90 °C",
                     "60 °C ની ડોલમાં 90 °C ના ચમચા કરતાં વધુ ઉષ્મા છે"),
                    T("true: heat depends on mass as well as temperature",
                      "સાચું: ઉષ્મા દળ અને તાપમાન બંને પર આધારિત")],
                   [T("heat is stored inside a body", "ઉષ્મા શરીરમાં સંગ્રહાય છે"),
                    T("false: internal energy is stored, heat is only in transit",
                      "ખોટું: આંતરિક ઊર્જા સંગ્રહાય, ઉષ્મા ફક્ત સ્થાનાંતરણમાં")],
                   [T("two bodies in contact end at the same temperature", "સંપર્કમાં રહેલાં બે શરીર અંતે સમાન તાપમાને આવે"),
                    T("true: this is thermal equilibrium", "સાચું: આ ઉષ્મીય સંતુલન છે")]]),
               H4("Worked example", "ઉકેલાયેલ દાખલો"),
               P("Raising 2 kg of water by 30 K needs Q = m c ΔT = 2 × 4186 × 30 = 2.51 × 10⁵ J, about "
                 "60 kcal — the same energy as lifting that water 12.8 km.",
                 "2 kg પાણીનું તાપમાન 30 K વધારવા Q = m c ΔT = 2 × 4186 × 30 = 2.51 × 10⁵ J જોઈએ, "
                 "લગભગ 60 kcal — એટલી જ ઊર્જા જેટલી એ પાણીને 12.8 km ઊંચું ઉપાડવા લાગે."),
               H4("Common mistake", "સામાન્ય ભૂલ"),
               P("Saying a body 'contains 500 J of heat'. It contains internal energy; 500 J is the heat "
                 "it gave out or took in.",
                 "શરીરમાં '500 J ઉષ્મા છે' એમ કહેવું. તેમાં આંતરિક ઊર્જા હોય છે; 500 J એ તેણે આપેલી કે "
                 "લીધેલી ઉષ્મા છે.")],
              "u4_transfer", syllabus_item="4.1"),
         card(T("1.2 Conduction, convection and radiation",
                "1.2 વહન, સંવહન અને વિકિરણ"),
              [H4("The three modes", "ત્રણ રીતો"),
               TB([T("Mode", "રીત"), T("How heat moves", "ઉષ્મા કેવી રીતે ચાલે"), T("Needs a medium?", "માધ્યમ જોઈએ?")],
                  [[T("conduction", "વહન"), T("molecules pass energy to neighbours, no bulk motion", "અણુઓ પાડોશીને ઊર્જા આપે, પદાર્થ ખસે નહીં"), T("yes, a solid", "હા, ઘન")],
                   [T("convection", "સંવહન"), T("the hot fluid itself moves and carries energy", "ગરમ પ્રવાહી પોતે ખસીને ઊર્જા લઈ જાય"), T("yes, a fluid", "હા, પ્રવાહી કે વાયુ")],
                   [T("radiation", "વિકિરણ"), T("electromagnetic waves carry energy", "વિદ્યુતચુંબકીય તરંગો ઊર્જા લઈ જાય"), T("no, works in vacuum", "ના, શૂન્યાવકાશમાં પણ")]]),
               H4("Where each is used", "દરેક ક્યાં વપરાય"),
               UL(("Conduction: the copper base of a cooking pan, or a heat sink on a transistor.",
                   "વહન: રાંધણ તપેલીનો તાંબાનો તળિયો, કે ટ્રાન્ઝિસ્ટર પરનો હીટ સિંક."),
                  ("Convection: a room radiator, a car radiator, or the draught in a chimney.",
                   "સંવહન: રૂમનો રેડિયેટર, કારનું રેડિયેટર, કે ચિમનીમાંનો ડ્રાફ્ટ."),
                  ("Radiation: the Sun's heat reaching the Earth, or an infrared heater.",
                   "વિકિરણ: સૂર્યની ઉષ્મા પૃથ્વી સુધી પહોંચવી, કે ઇન્ફ્રારેડ હીટર.")),
               H4("Worked example", "ઉકેલાયેલ દાખલો"),
               P("A 2 mm steel plate of area 0.5 m² with 100 K across it conducts "
                 "Q/t = k A ΔT/L = 50 × 0.5 × 100/0.002 = 1.25 × 10⁶ W — which is why the same plate in "
                 "copper (k = 400) would pass eight times more.",
                 "0.5 m² ક્ષેત્રફળની 2 mm સ્ટીલ પ્લેટ પર 100 K તફાવત હોય તો "
                 "Q/t = k A ΔT/L = 50 × 0.5 × 100/0.002 = 1.25 × 10⁶ W — તેથી જ એ જ પ્લેટ તાંબામાં "
                 "(k = 400) આઠ ગણી વધુ પસાર કરે."),
               H4("Common mistake", "સામાન્ય ભૂલ"),
               P("Calling a thermos flask a 'conduction barrier' only. It blocks all three: vacuum stops "
                 "conduction and convection, and the silvered walls cut radiation.",
                 "થર્મોસ ફ્લાસ્કને ફક્ત 'વહન અવરોધ' કહેવું. તે ત્રણેય રોકે: શૂન્યાવકાશ વહન અને સંવહન "
                 "અટકાવે, અને ચાંદીવાળી દીવાલો વિકિરણ કાપે.")],
              "u4_transfer", syllabus_item="4.2"),
     ]},

    {"title": T("2. Temperature Scales and Thermometers", "2. તાપમાનના માપક્રમ અને થર્મોમીટર"),
     "items": [
         card(T("2.1 Kelvin, Celsius and Fahrenheit",
                "2.1 કેલ્વિન, સેલ્સિયસ અને ફેરનહીટ"),
              [H4("The three scales", "ત્રણ માપક્રમ"),
               TB([T("Scale", "માપક્રમ"), T("Ice point", "બરફ બિંદુ"), T("Steam point", "વરાળ બિંદુ"), T("Divisions", "વિભાગ")],
                  [[T("Celsius (°C)", "સેલ્સિયસ (°C)"), T("0", "0"), T("100", "100"), T("100", "100")],
                   [T("Fahrenheit (°F)", "ફેરનહીટ (°F)"), T("32", "32"), T("212", "212"), T("180", "180")],
                   [T("Kelvin (K)", "કેલ્વિન (K)"), T("273.15", "273.15"), T("373.15", "373.15"), T("100", "100")]]),
               H4("Conversions", "રૂપાંતરણ"),
               P("°F = (9/5) °C + 32 and °C = (5/9)(°F − 32); K = °C + 273.15, so a temperature "
                 "difference of 1 K equals 1 °C but equals 1.8 °F.",
                 "°F = (9/5) °C + 32 અને °C = (5/9)(°F − 32); K = °C + 273.15, તેથી 1 K નો તાપમાન તફાવત "
                 "1 °C બરાબર છે પણ 1.8 °F બરાબર છે."),
               H4("Worked example", "ઉકેલાયેલ દાખલો"),
               P("A body at 37 °C is 37 + 273.15 = 310.15 K and (9/5)(37) + 32 = 98.6 °F. The value "
                 "−40 is the one point where both scales read the same.",
                 "37 °C નું શરીર 37 + 273.15 = 310.15 K અને (9/5)(37) + 32 = 98.6 °F છે. −40 એ એક જ "
                 "બિંદુ છે જ્યાં બંને માપક્રમ સમાન વાંચે."),
               H4("Common mistake", "સામાન્ય ભૂલ"),
               P("Adding 273 to a temperature difference. Only an absolute temperature is converted; a "
                 "difference of 20 °C is a difference of 20 K.",
                 "તાપમાનના તફાવતમાં 273 ઉમેરવું. ફક્ત નિરપેક્ષ તાપમાનનું રૂપાંતર થાય; 20 °C નો તફાવત "
                 "20 K નો તફાવત છે.")],
              "u4_scales", syllabus_item="4.3"),
         card(T("2.2 Mercury and bimetallic thermometers",
                "2.2 પારા અને બાયમેટાલિક થર્મોમીટર"),
              [H4("Mercury-in-glass", "પારા-કાચ થર્મોમીટર"),
               P("A fine bore tube with a mercury bulb. Mercury is used because it does not wet glass, "
                 "stays liquid from −39 °C to 357 °C and expands evenly; the reading is taken at the top "
                 "of the column, with the meniscus convex.",
                 "પાતળી બોરવાળી નળી અને પારાનો બલ્બ. પારો વપરાય કારણ કે તે કાચને ભીનો કરતો નથી, −39 °C "
                 "થી 357 °C સુધી પ્રવાહી રહે અને સરખી રીતે ફેલાય; વાંચન સ્તંભની ટોચે લેવાય, મેનિસ્કસ "
                 "બહિર્ગોળ હોય."),
               H4("Bimetallic strip", "બાયમેટાલિક પટ્ટી"),
               P("Two metals with different expansion coefficients are riveted together. On heating the "
                 "pair bends towards the metal that expands less, and that movement switches a contact — "
                 "the basis of an iron, a thermostat and a fire alarm.",
                 "જુદા પ્રસરણ ગુણાંકવાળી બે ધાતુઓ એકબીજા સાથે જોડાય છે. ગરમ કરતાં જોડી ઓછું પ્રસરતી "
                 "ધાતુ તરફ વળે, અને એ હલનચલન સંપર્ક બદલે — ઇસ્ત્રી, થર્મોસ્ટેટ અને આગ-ચેતવણીનો આધાર."),
               TB([T("Property", "ગુણધર્મ"), T("Mercury thermometer", "પારા થર્મોમીટર"), T("Bimetallic strip", "બાયમેટાલિક પટ્ટી")],
                  [[T("output", "આઉટપુટ"), T("a reading", "વાંચન"), T("mechanical movement", "યાંત્રિક હલનચલન")],
                   [T("range", "મર્યાદા"), T("−39 to 357 °C", "−39 થી 357 °C"), T("set by the two metals", "બે ધાતુઓ નક્કી કરે")],
                   [T("use", "ઉપયોગ"), T("clinical and laboratory measurement", "ક્લિનિકલ અને પ્રયોગશાળા માપન"), T("on/off control", "ચાલુ/બંધ નિયંત્રણ")]]),
               H4("Worked example", "ઉકેલાયેલ દાખલો"),
               P("A brass–iron strip of length 5 cm with a 200 K rise bends by about "
                 "ΔL = (19 − 12) × 10⁻⁶ × 5 × 200 = 7 × 10⁻³ cm — 0.07 mm of differential movement, "
                 "enough to open a switch.",
                 "5 cm લાંબી પિત્તળ-લોખંડ પટ્ટી 200 K ગરમ થતાં લગભગ "
                 "ΔL = (19 − 12) × 10⁻⁶ × 5 × 200 = 7 × 10⁻³ cm વળે — 0.07 mm નું વિભેદક ખસવું, જે સ્વિચ "
                 "ખોલવા પૂરતું છે."),
               H4("Common mistake", "સામાન્ય ભૂલ"),
               P("Reading a thermometer immediately after taking it out of the mouth; the column falls "
                 "before the eye reads it. Read it in place.",
                 "મોંમાંથી કાઢતાં જ થર્મોમીટર વાંચવું; આંખ વાંચે તે પહેલાં સ્તંભ ઊતરી જાય. તેને જ્યાં છે "
                 "ત્યાં જ વાંચો.")],
              "u4_thermometer", syllabus_item="4.5"),
         card(T("2.3 Heat capacity and specific heat",
                "2.3 ઉષ્મા ધારિતા અને વિશિષ્ટ ઉષ્મા"),
              [H4("Definitions", "વ્યાખ્યાઓ"),
               P("<b>Heat capacity</b> C = Q/ΔT is the heat needed to raise the whole body by 1 K, in "
                 "J/K. <b>Specific heat</b> c = Q/(m ΔT) is the heat per unit mass per kelvin, in J/(kg·K).",
                 "<b>ઉષ્મા ધારિતા</b> C = Q/ΔT એ આખા શરીરનું તાપમાન 1 K વધારવા જરૂરી ઉષ્મા છે, J/K માં. "
                 "<b>વિશિષ્ટ ઉષ્મા</b> c = Q/(m ΔT) એ એકમ દળ દીઠ પ્રતિ કેલ્વિન ઉષ્મા છે, J/(kg·K) માં."),
               TB([T("Substance", "પદાર્થ"), T("c in J/(kg·K)", "c J/(kg·K) માં")],
                  [[T("water", "પાણી"), T("4186", "4186")],
                   [T("ice", "બરફ"), T("2100", "2100")],
                   [T("aluminium", "એલ્યુમિનિયમ"), T("900", "900")],
                   [T("iron", "લોખંડ"), T("450", "450")],
                   [T("copper", "તાંબું"), T("390", "390")],
                   [T("lead", "સીસું"), T("128", "128")]]),
               H4("Why water is special", "પાણી ખાસ કેમ"),
               P("Water has one of the highest specific heats, so it is used as a coolant and it makes "
                 "the sea slow to heat and slow to cool — the reason coastal climates are mild.",
                 "પાણીની વિશિષ્ટ ઉષ્મા સૌથી વધુમાંથી એક છે, તેથી તે ઠંડક માટે વપરાય અને સમુદ્ર ધીમે ગરમ "
                 "અને ધીમે ઠંડો થાય — તેથી જ દરિયાકાંઠાનું હવામાન સમશીતોષ્ણ રહે."),
               H4("Worked example", "ઉકેલાયેલ દાખલો"),
               P("Heating 0.5 kg of aluminium from 20 °C to 80 °C needs Q = 0.5 × 900 × 60 = 27 000 J, "
                 "while the same heat would raise 0.5 kg of water by only 12.9 K.",
                 "0.5 kg એલ્યુમિનિયમ 20 °C થી 80 °C સુધી ગરમ કરવા Q = 0.5 × 900 × 60 = 27 000 J જોઈએ, "
                 "જ્યારે એટલી જ ઉષ્મા 0.5 kg પાણીનું તાપમાન ફક્ત 12.9 K વધારે."),
               H4("Common mistake", "સામાન્ય ભૂલ"),
               P("Mixing up C and c. Heat capacity belongs to the object (a 2 kg pan), specific heat to "
                 "the material (aluminium).",
                 "C અને c ભેગા કરવા. ઉષ્મા ધારિતા વસ્તુની (2 kg તપેલી) અને વિશિષ્ટ ઉષ્મા પદાર્થની (એલ્યુમિનિયમ) "
                 "હોય છે.")],
              syllabus_item="4.4"),
     ]},

    {"title": T("3. Thermal Conductivity and Expansion", "3. ઉષ્મીય વાહકતા અને પ્રસરણ"),
     "items": [
         card(T("3.1 Coefficient of thermal conductivity",
                "3.1 ઉષ્મીય વાહકતાનો ગુણાંક"),
              [H4("Definition", "વ્યાખ્યા"),
               P("The rate of heat flow through a slab is <b>Q/t = k A ΔT / L</b>, where k is the "
                 "coefficient of thermal conductivity in W/(m·K). It is numerically the heat passing "
                 "per second through 1 m² of a 1 m thick slab with 1 K across it.",
                 "પટ્ટામાંથી ઉષ્મા પ્રવાહનો દર <b>Q/t = k A ΔT / L</b> છે, જ્યાં k ઉષ્મીય વાહકતાનો "
                 "ગુણાંક W/(m·K) માં છે. આંકડામાં તે 1 m જાડા, 1 m² ક્ષેત્રફળવાળા પટ્ટા પર 1 K તફાવત હોય "
                 "ત્યારે પ્રતિ સેકન્ડ પસાર થતી ઉષ્મા છે."),
               TB([T("Material", "પદાર્થ"), T("k in W/(m·K)", "k W/(m·K) માં")],
                  [[T("silver", "ચાંદી"), T("430", "430")],
                   [T("copper", "તાંબું"), T("400", "400")],
                   [T("steel", "સ્ટીલ"), T("50", "50")],
                   [T("brick", "ઇંટ"), T("0.6", "0.6")],
                   [T("glass", "કાચ"), T("0.8", "0.8")],
                   [T("wood", "લાકડું"), T("0.15", "0.15")],
                   [T("air (still)", "હવા (સ્થિર)"), T("0.026", "0.026")]]),
               H4("Why air is the best insulator", "હવા શ્રેષ્ઠ અવાહક કેમ"),
               P("Still air has k about 15 000 times smaller than silver, which is why wool, foam and "
                 "double glazing work: they trap air and stop it from convecting.",
                 "સ્થિર હવાનો k ચાંદી કરતાં લગભગ 15 000 ગણો નાનો છે, તેથી જ ઊન, ફોમ અને બેવડું કાચ કામ "
                 "કરે: તે હવા પકડી રાખે અને સંવહન અટકાવે."),
               H4("Worked example", "ઉકેલાયેલ દાખલો"),
               P("A brick wall 0.2 m thick, 10 m², with 15 K across it loses "
                 "Q/t = 0.6 × 10 × 15/0.2 = 450 W — the size of a small room heater running all day.",
                 "0.2 m જાડી, 10 m² ની ઇંટની દીવાલ પર 15 K તફાવત હોય તો "
                 "Q/t = 0.6 × 10 × 15/0.2 = 450 W ગુમાવે — આખો દિવસ ચાલતા નાના રૂમ હીટર જેટલું."),
               H4("Common mistake", "સામાન્ય ભૂલ"),
               P("Forgetting to convert the thickness to metres, or using the temperature of one side "
                 "instead of the difference ΔT.",
                 "જાડાઈ મીટરમાં ફેરવવાનું ભૂલવું, અથવા તફાવત ΔT ને બદલે એક બાજુનું તાપમાન વાપરવું.")],
              "u4_conduction", syllabus_item="4.6"),
         card(T("3.2 Expansion of solids and the coefficient of linear expansion",
                "3.2 ઘનનું પ્રસરણ અને રેખીય પ્રસરણનો ગુણાંક"),
              [H4("Definition", "વ્યાખ્યા"),
               P("A rod lengthens by <b>ΔL = α L ΔT</b>, where α is the coefficient of linear expansion "
                 "in K⁻¹. Area expands as ΔA = 2α A ΔT and volume as ΔV = 3α V ΔT.",
                 "સળિયાની લંબાઈ <b>ΔL = α L ΔT</b> જેટલી વધે, જ્યાં α રેખીય પ્રસરણનો ગુણાંક K⁻¹ માં છે. "
                 "ક્ષેત્રફળ ΔA = 2α A ΔT અને ઘનફળ ΔV = 3α V ΔT પ્રમાણે વધે."),
               TB([T("Material", "પદાર્થ"), T("α in 10⁻⁶ K⁻¹", "α 10⁻⁶ K⁻¹ માં")],
                  [[T("steel", "સ્ટીલ"), T("12", "12")],
                   [T("iron", "લોખંડ"), T("12", "12")],
                   [T("copper", "તાંબું"), T("17", "17")],
                   [T("brass", "પિત્તળ"), T("19", "19")],
                   [T("aluminium", "એલ્યુમિનિયમ"), T("23", "23")],
                   [T("invar (alloy)", "ઇન્વાર (મિશ્રધાતુ)"), T("1", "1")]]),
               H4("Engineering consequences", "ઇજનેરી પરિણામો"),
               UL(("Railway rails are laid with a gap so that summer expansion does not buckle them.",
                   "રેલવે પાટા વચ્ચે જગ્યા રખાય જેથી ઉનાળાનું પ્રસરણ તેમને વાંકા ન કરે."),
                  ("A bimetallic strip works because α differs between the two metals.",
                   "બાયમેટાલિક પટ્ટી કામ કરે કારણ કે બે ધાતુઓનો α જુદો હોય."),
                  ("Invar is used for the pendulum of a precision clock because its α is almost zero.",
                   "ચોક્કસ ઘડિયાળના લોલક માટે ઇન્વાર વપરાય કારણ કે તેનો α લગભગ શૂન્ય છે.")),
               H4("Worked example", "ઉકેલાયેલ દાખલો"),
               P("A 10 m steel rail on a day that is 40 K hotter: ΔL = 12 × 10⁻⁶ × 10 × 40 = 4.8 mm of "
                 "expansion, so the gap left at laying must be at least 5 mm.",
                 "10 m સ્ટીલ પાટો 40 K વધુ ગરમ દિવસે: ΔL = 12 × 10⁻⁶ × 10 × 40 = 4.8 mm પ્રસરે, તેથી "
                 "નાખતી વખતે ઓછામાં ઓછી 5 mm જગ્યા રાખવી પડે."),
               H4("Common mistake", "સામાન્ય ભૂલ"),
               P("Using the Celsius value for a Fahrenheit difference, or forgetting that ΔT is a "
                 "difference and never negative in the formula.",
                 "ફેરનહીટ તફાવત માટે સેલ્સિયસ મૂલ્ય વાપરવું, અથવા ભૂલવું કે ΔT તફાવત છે અને સૂત્રમાં કદી "
                 "ઋણ નથી.")],
              "u4_expansion", syllabus_item="4.7"),
     ]},

    {"title": T("4. Practice Questions with Model Answers", "4. સરાવ પ્રશ્નો અને આદર્શ જવાબો"),
     "items": []},
]

NUMERICALS = [
    num("u4n01", T("Heat needed to raise 2 kg of water by 30 K.",
                   "2 kg પાણીનું તાપમાન 30 K વધારવા જરૂરી ઉષ્મા."),
        T("Find the heat needed to raise 2 kg of water from 20 °C to 50 °C (c = 4186 J/(kg·K)).",
          "2 kg પાણી 20 °C થી 50 °C સુધી ગરમ કરવા જરૂરી ઉષ્મા શોધો (c = 4186 J/(kg·K))."),
        [P("Q = m c ΔT", "Q = m c ΔT"),
         P("= 2 × 4186 × 30", "= 2 × 4186 × 30"),
         P("= 2.51 × 10⁵ J (about 60 kcal)", "= 2.51 × 10⁵ J (લગભગ 60 kcal)")],
        T("2.51 × 10⁵ J", "2.51 × 10⁵ J"), unit_no=4),
    num("u4n02", T("Specific heat from a measured heat input.",
                   "માપેલા ઉષ્મા પ્રવેશ પરથી વિશિષ્ટ ઉષ્મા."),
        T("0.5 kg of a metal takes 27 000 J to rise by 60 K. Find its specific heat.",
          "0.5 kg ધાતુનું તાપમાન 60 K વધારવા 27 000 J જોઈએ. તેની વિશિષ્ટ ઉષ્મા શોધો."),
        [P("c = Q/(m ΔT)", "c = Q/(m ΔT)"),
         P("= 27 000/(0.5 × 60)", "= 27 000/(0.5 × 60)"),
         P("= 900 J/(kg·K), the value for aluminium", "= 900 J/(kg·K), એલ્યુમિનિયમનું મૂલ્ય")],
        T("900 J/(kg·K)", "900 J/(kg·K)"), unit_no=4),
    num("u4n03", T("Convert 37 °C into kelvin and Fahrenheit.",
                   "37 °C ને કેલ્વિન અને ફેરનહીટમાં ફેરવો."),
        T("A patient's temperature is 37 °C. Express it in K and in °F.",
          "દર્દીનું તાપમાન 37 °C છે. તેને K અને °F માં દર્શાવો."),
        [P("K = °C + 273.15 = 310.15 K", "K = °C + 273.15 = 310.15 K"),
         P("°F = (9/5)(37) + 32", "°F = (9/5)(37) + 32"),
         P("= 66.6 + 32 = 98.6 °F", "= 66.6 + 32 = 98.6 °F")],
        T("310.15 K and 98.6 °F", "310.15 K અને 98.6 °F"), unit_no=4),
    num("u4n04", T("The temperature at which °C equals °F.",
                   "જે તાપમાને °C અને °F સમાન થાય."),
        T("At what temperature do the Celsius and Fahrenheit scales read the same number?",
          "કયા તાપમાને સેલ્સિયસ અને ફેરનહીટ માપક્રમ સમાન આંકડો વાંચે?"),
        [P("Set x = (9/5)x + 32", "x = (9/5)x + 32 મૂકો"),
         P("x − 1.8x = 32, so −0.8x = 32", "x − 1.8x = 32, તેથી −0.8x = 32"),
         P("x = −40, so −40 °C = −40 °F", "x = −40, તેથી −40 °C = −40 °F")],
        T("−40°", "−40°"), unit_no=4),
    num("u4n05", T("Heat conducted through a steel plate.",
                   "સ્ટીલ પ્લેટમાંથી વહેતી ઉષ્મા."),
        T("A steel plate 2 mm thick and 0.5 m² in area has 100 K across it (k = 50 W/(m·K)). Find the "
          "heat flow per second.", "2 mm જાડી અને 0.5 m² ક્ષેત્રફળની સ્ટીલ પ્લેટ પર 100 K તફાવત છે "
          "(k = 50 W/(m·K)). પ્રતિ સેકન્ડ ઉષ્મા પ્રવાહ શોધો."),
        [P("Q/t = k A ΔT/L", "Q/t = k A ΔT/L"),
         P("= 50 × 0.5 × 100/0.002", "= 50 × 0.5 × 100/0.002"),
         P("= 1.25 × 10⁶ W", "= 1.25 × 10⁶ W")],
        T("1.25 × 10⁶ W", "1.25 × 10⁶ W"), unit_no=4),
    num("u4n06", T("Heat loss through a brick wall.",
                   "ઇંટની દીવાલમાંથી ઉષ્મા ખોટ."),
        T("A brick wall (k = 0.6 W/(m·K)) is 0.2 m thick and 10 m² in area, with 15 K across it. Find "
          "the rate of heat loss.", "0.6 W/(m·K) વાહકતાવાળી ઇંટની દીવાલ 0.2 m જાડી અને 10 m² ક્ષેત્રફળની "
          "છે, તેના પર 15 K તફાવત છે. ઉષ્મા ખોટનો દર શોધો."),
        [P("Q/t = 0.6 × 10 × 15/0.2", "Q/t = 0.6 × 10 × 15/0.2"),
         P("= 90/0.2", "= 90/0.2"),
         P("= 450 W", "= 450 W")],
        T("450 W", "450 W"), unit_no=4),
    num("u4n07", T("Thickness of insulation for a given loss.",
                   "આપેલી ખોટ માટે અવાહકની જાડાઈ."),
        T("What thickness of brick (k = 0.6) keeps the loss through 20 m² below 300 W with 20 K "
          "across it?", "20 K તફાવતે 20 m² માંથી ખોટ 300 W થી નીચે રાખવા 0.6 વાહકતાવાળી ઇંટની કેટલી "
          "જાડાઈ જોઈએ?"),
        [P("L = k A ΔT/(Q/t)", "L = k A ΔT/(Q/t)"),
         P("= 0.6 × 20 × 20/300", "= 0.6 × 20 × 20/300"),
         P("= 240/300 = 0.8 m", "= 240/300 = 0.8 m")],
        T("0.8 m", "0.8 m"), unit_no=4),
    num("u4n08", T("Expansion of a 10 m steel rail.",
                   "10 m સ્ટીલ પાટાનું પ્રસરણ."),
        T("A steel rail 10 m long warms by 40 K (α = 12 × 10⁻⁶ K⁻¹). Find the expansion and the gap "
          "needed.", "10 m લાંબો સ્ટીલ પાટો 40 K ગરમ થાય (α = 12 × 10⁻⁶ K⁻¹). પ્રસરણ અને જરૂરી જગ્યા શોધો."),
        [P("ΔL = α L ΔT = 12 × 10⁻⁶ × 10 × 40", "ΔL = α L ΔT = 12 × 10⁻⁶ × 10 × 40"),
         P("= 4.8 × 10⁻³ m", "= 4.8 × 10⁻³ m"),
         P("= 4.8 mm, so a gap of 5 mm is left", "= 4.8 mm, તેથી 5 mm જગ્યા રખાય")],
        T("4.8 mm", "4.8 mm"), unit_no=4),
    num("u4n09", T("Linear expansion of an aluminium rod.",
                   "એલ્યુમિનિયમ સળિયાનું રેખીય પ્રસરણ."),
        T("An aluminium rod 2 m long is heated from 20 °C to 120 °C (α = 23 × 10⁻⁶ K⁻¹). Find its new "
          "length.", "2 m લાંબો એલ્યુમિનિયમ સળિયો 20 °C થી 120 °C સુધી ગરમ થાય (α = 23 × 10⁻⁶ K⁻¹). તેની "
          "નવી લંબાઈ શોધો."),
        [P("ΔL = 23 × 10⁻⁶ × 2 × 100 = 4.6 × 10⁻³ m", "ΔL = 23 × 10⁻⁶ × 2 × 100 = 4.6 × 10⁻³ m"),
         P("= 4.6 mm", "= 4.6 mm"),
         P("New length = 2 + 0.0046 = 2.0046 m", "નવી લંબાઈ = 2 + 0.0046 = 2.0046 m")],
        T("2.0046 m", "2.0046 m"), unit_no=4),
    num("u4n10", T("Coefficient α from a measured expansion.",
                   "માપેલા પ્રસરણ પરથી ગુણાંક α."),
        T("A 1.5 m brass rod lengthens by 1.14 mm when heated through 40 K. Find α.",
          "1.5 m પિત્તળનો સળિયો 40 K ગરમ થતાં 1.14 mm લાંબો થાય. α શોધો."),
        [P("α = ΔL/(L ΔT)", "α = ΔL/(L ΔT)"),
         P("= 1.14 × 10⁻³/(1.5 × 40)", "= 1.14 × 10⁻³/(1.5 × 40)"),
         P("= 1.9 × 10⁻⁵ K⁻¹", "= 1.9 × 10⁻⁵ K⁻¹")],
        T("1.9 × 10⁻⁵ K⁻¹", "1.9 × 10⁻⁵ K⁻¹"), unit_no=4),
    num("u4n11", T("Final temperature when hot and cold water mix.",
                   "ગરમ અને ઠંડું પાણી ભળે ત્યારે અંતિમ તાપમાન."),
        T("2 kg of water at 80 °C is mixed with 3 kg at 20 °C. Find the final temperature, ignoring "
          "losses.", "80 °C નું 2 kg પાણી 20 °C ના 3 kg સાથે ભળે છે. ખોટ ગણ્યા વગર અંતિમ તાપમાન શોધો."),
        [P("Heat lost = heat gained: 2 c (80 − θ) = 3 c (θ − 20)", "ખોટ = લાભ: 2 c (80 − θ) = 3 c (θ − 20)"),
         P("160 − 2θ = 3θ − 60", "160 − 2θ = 3θ − 60"),
         P("5θ = 220, θ = 44 °C", "5θ = 220, θ = 44 °C")],
        T("44 °C", "44 °C"), unit_no=4),
    num("u4n12", T("Heat capacity of a copper block.",
                   "તાંબાના બ્લોકની ઉષ્મા ધારિતા."),
        T("Find the heat capacity of a 2 kg copper block (c = 390 J/(kg·K)) and the heat needed to "
          "raise it by 50 K.", "2 kg તાંબાના બ્લોકની ઉષ્મા ધારિતા શોધો (c = 390 J/(kg·K)) અને 50 K "
          "વધારવા જરૂરી ઉષ્મા."),
        [P("C = m c = 2 × 390 = 780 J/K", "C = m c = 2 × 390 = 780 J/K"),
         P("Q = C ΔT", "Q = C ΔT"),
         P("= 780 × 50 = 39 000 J", "= 780 × 50 = 39 000 J")],
        T("780 J/K and 39 000 J", "780 J/K અને 39 000 J"), unit_no=4),
    num("u4n13", T("Volume expansion of a copper cube.",
                   "તાંબાના સમઘનનું ઘનફળ પ્રસરણ."),
        T("A copper cube of side 10 cm is heated through 100 K (α = 17 × 10⁻⁶ K⁻¹). Find the increase "
          "in volume.", "10 cm બાજુવાળો તાંબાનો સમઘન 100 K ગરમ થાય (α = 17 × 10⁻⁶ K⁻¹). ઘનફળમાં વધારો શોધો."),
        [P("V = 0.1³ = 1 × 10⁻³ m³", "V = 0.1³ = 1 × 10⁻³ m³"),
         P("ΔV = 3α V ΔT = 3 × 17 × 10⁻⁶ × 10⁻³ × 100", "ΔV = 3α V ΔT = 3 × 17 × 10⁻⁶ × 10⁻³ × 100"),
         P("= 5.1 × 10⁻⁶ m³ (5.1 cm³)", "= 5.1 × 10⁻⁶ m³ (5.1 cm³)")],
        T("5.1 × 10⁻⁶ m³", "5.1 × 10⁻⁶ m³"), unit_no=4),
    num("u4n14", T("Bimetallic strip movement.",
                   "બાયમેટાલિક પટ્ટીનું ખસવું."),
        T("A brass–iron strip 5 cm long is heated through 200 K. If α(brass) = 19 × 10⁻⁶ and "
          "α(iron) = 12 × 10⁻⁶ K⁻¹, find the difference in expansion.",
          "5 cm લાંબી પિત્તળ-લોખંડ પટ્ટી 200 K ગરમ થાય. α(પિત્તળ) = 19 × 10⁻⁶ અને α(લોખંડ) = 12 × 10⁻⁶ "
          "K⁻¹ હોય તો પ્રસરણનો તફાવત શોધો."),
        [P("ΔL = (α₁ − α₂) L ΔT", "ΔL = (α₁ − α₂) L ΔT"),
         P("= (19 − 12) × 10⁻⁶ × 0.05 × 200", "= (19 − 12) × 10⁻⁶ × 0.05 × 200"),
         P("= 7 × 10⁻⁵ m = 0.07 mm", "= 7 × 10⁻⁵ m = 0.07 mm")],
        T("7 × 10⁻⁵ m (0.07 mm)", "7 × 10⁻⁵ m (0.07 mm)"), unit_no=4),
    num("u4n15", T("Energy to heat water in a geyser.",
                   "ગીઝરમાં પાણી ગરમ કરવાની ઊર્જા."),
        T("A geyser heats 50 kg of water from 25 °C to 65 °C in 40 minutes. Find the power needed.",
          "ગીઝર 50 kg પાણીને 40 મિનિટમાં 25 °C થી 65 °C સુધી ગરમ કરે છે. જરૂરી પાવર શોધો."),
        [P("Q = 50 × 4186 × 40 = 8.37 × 10⁶ J", "Q = 50 × 4186 × 40 = 8.37 × 10⁶ J"),
         P("t = 40 × 60 = 2400 s", "t = 40 × 60 = 2400 s"),
         P("P = Q/t = 3.49 × 10³ W ≈ 3.5 kW", "P = Q/t = 3.49 × 10³ W ≈ 3.5 kW")],
        T("≈ 3.5 kW", "≈ 3.5 kW"), unit_no=4),
    num("u4n16", T("Temperature rise of oil in a bearing.",
                   "બેરિંગમાં તેલનું તાપમાન વધવું."),
        T("2 kg of oil (c = 2000 J/(kg·K)) absorbs 40 000 J of friction heat. Find the temperature "
          "rise.", "2 kg તેલ (c = 2000 J/(kg·K)) 40 000 J ઘર્ષણ ઉષ્મા લે છે. તાપમાન વધારો શોધો."),
        [P("ΔT = Q/(m c)", "ΔT = Q/(m c)"),
         P("= 40 000/(2 × 2000)", "= 40 000/(2 × 2000)"),
         P("= 10 K", "= 10 K")],
        T("10 K", "10 K"), unit_no=4),
    num("u4n17", T("Heat flow through a glass window.",
                   "કાચની બારીમાંથી ઉષ્મા પ્રવાહ."),
        T("A glass window of 1.5 m² and 5 mm thickness (k = 0.8 W/(m·K)) has 25 K across it. Find the "
          "heat loss per second.", "1.5 m² ક્ષેત્રફળ અને 5 mm જાડાઈની કાચની બારી (k = 0.8 W/(m·K)) પર "
          "25 K તફાવત છે. પ્રતિ સેકન્ડ ઉષ્મા ખોટ શોધો."),
        [P("Q/t = 0.8 × 1.5 × 25/0.005", "Q/t = 0.8 × 1.5 × 25/0.005"),
         P("= 30/0.005", "= 30/0.005"),
         P("= 6000 W", "= 6000 W")],
        T("6000 W", "6000 W"), unit_no=4),
    num("u4n18", T("Fahrenheit reading of 100 °C.",
                   "100 °C નું ફેરનહીટ વાંચન."),
        T("Convert 100 °C and −10 °C into °F.", "100 °C અને −10 °C ને °F માં ફેરવો."),
        [P("°F = (9/5)(100) + 32 = 212 °F", "°F = (9/5)(100) + 32 = 212 °F"),
         P("°F = (9/5)(−10) + 32 = −18 + 32", "°F = (9/5)(−10) + 32 = −18 + 32"),
         P("= 14 °F", "= 14 °F")],
        T("212 °F and 14 °F", "212 °F અને 14 °F"), unit_no=4),
]

EQUATIONS = [
    {"title": T("Heat and specific heat", "ઉષ્મા અને વિશિષ્ટ ઉષ્મા"),
     "items": [
         {"name": T("Heat gained or lost", "મેળવેલી કે ગુમાવેલી ઉષ્મા"), "f": "Q = m c ΔT",
          "terms": T("Mass times specific heat times temperature change.",
                     "દળ × વિશિષ્ટ ઉષ્મા × તાપમાન ફેરફાર.")},
         {"name": T("Heat capacity", "ઉષ્મા ધારિતા"), "f": "C = m c = Q/ΔT  (J/K)",
          "terms": T("Belongs to the object, not the material.", "વસ્તુની હોય, પદાર્થની નહીં.")},
         {"name": T("Latent heat", "ગુપ્ત ઉષ્મા"), "f": "Q = m L",
          "terms": T("Heat at constant temperature during a change of state.",
                     "અવસ્થા બદલાય ત્યારે અચળ તાપમાને લાગતી ઉષ્મા.")},
         {"name": T("Calorie", "કેલરી"), "f": "1 cal = 4.186 J",
          "terms": T("Heat to raise 1 g of water by 1 °C.", "1 g પાણીનું તાપમાન 1 °C વધારવાની ઉષ્મા.")},
     ]},
    {"title": T("Thermometry", "તાપમાનમાપન"),
     "items": [
         {"name": T("Celsius to Fahrenheit", "સેલ્સિયસથી ફેરનહીટ"), "f": "°F = (9/5) °C + 32",
          "terms": T("180 Fahrenheit degrees span the same range as 100 Celsius degrees.",
                     "180 ફેરનહીટ અંશ એ 100 સેલ્સિયસ અંશ જેટલી જ શ્રેણી છે.")},
         {"name": T("Celsius to kelvin", "સેલ્સિયસથી કેલ્વિન"), "f": "K = °C + 273.15",
          "terms": T("0 K is absolute zero, about −273.15 °C.",
                     "0 K નિરપેક્ષ શૂન્ય છે, લગભગ −273.15 °C.")},
     ]},
    {"title": T("Conduction and expansion", "વહન અને પ્રસરણ"),
     "items": [
         {"name": T("Fourier's law of conduction", "વહનનો ફોરિયરનો નિયમ"),
          "f": "Q/t = k A ΔT / L",
          "terms": T("Heat per second along a slab of length L.",
                     "L લંબાઈના પટ્ટા સાથે પ્રતિ સેકન્ડ ઉષ્મા.")},
         {"name": T("Linear expansion", "રેખીય પ્રસરણ"), "f": "ΔL = α L ΔT",
          "terms": T("α in K⁻¹, about 12 × 10⁻⁶ for steel.",
                     "α K⁻¹ માં, સ્ટીલ માટે લગભગ 12 × 10⁻⁶.")},
         {"name": T("Area and volume expansion", "ક્ષેત્રફળ અને ઘનફળ પ્રસરણ"),
          "f": "ΔA = 2α A ΔT,  ΔV = 3α V ΔT",
          "terms": T("The factors 2 and 3 come from the three dimensions.",
                     "2 અને 3 અવયવ ત્રણ પરિમાણમાંથી આવે.")},
     ]},
]

VIVA = [
    {"title": T("Heat and temperature", "ઉષ્મા અને તાપમાન"),
     "items": [
         {"q": T("Distinguish heat from temperature.",
                 "ઉષ્મા અને તાપમાનમાં ભેદ આપો."),
          "a": T("Heat is energy in transit due to a temperature difference, measured in joules; "
                 "temperature is the degree of hotness, measured in kelvin, and it decides the "
                 "direction of flow.",
                 "ઉષ્મા એ તાપમાનના તફાવતને કારણે સ્થાનાંતરિત થતી ઊર્જા છે, જૂલમાં મપાય; તાપમાન એ ગરમીનું "
                 "માપ છે, કેલ્વિનમાં મપાય, અને સંક્રમણની દિશા નક્કી કરે.")},
         {"q": T("Name the three modes of heat transfer and one example of each.",
                 "ઉષ્મા સંક્રમણની ત્રણ રીતો અને દરેકનું એક ઉદાહરણ આપો."),
          "a": T("Conduction through a metal spoon in hot tea, convection in a room radiator, and "
                 "radiation from the Sun reaching the Earth through vacuum.",
                 "ગરમ ચાના ચમચામાં વહન, રૂમ રેડિયેટરમાં સંવહન, અને શૂન્યાવકાશમાંથી સૂર્યનું વિકિરણ પૃથ્વી સુધી.")},
         {"q": T("Why is a thermos flask effective?", "થર્મોસ ફ્લાસ્ક કેમ અસરકારક છે?"),
          "a": T("The vacuum between the walls stops conduction and convection, and the silvered "
                 "surfaces reflect radiation, so all three modes are blocked.",
                 "દીવાલો વચ્ચેનો શૂન્યાવકાશ વહન અને સંવહન અટકાવે છે, અને ચાંદીવાળી સપાટીઓ વિકિરણ પરાવર્તે "
                 "છે, તેથી ત્રણેય રીતો અટકે છે.")},
     ]},
    {"title": T("Thermometry", "તાપમાનમાપન"),
     "items": [
         {"q": T("Why is mercury used in a glass thermometer?",
                 "કાચના થર્મોમીટરમાં પારો કેમ વપરાય?"),
          "a": T("It does not wet glass, it expands uniformly, it is opaque and easy to read, and it "
                 "stays liquid over a wide range from −39 °C to 357 °C.",
                 "તે કાચને ભીનો કરતો નથી, સરખી રીતે ફેલાય, અપારદર્શક અને વાંચવા સહેલો છે, અને −39 °C થી "
                 "357 °C સુધી પ્રવાહી રહે.")},
         {"q": T("How does a bimetallic strip work?", "બાયમેટાલિક પટ્ટી કેવી રીતે કામ કરે?"),
          "a": T("Two metals with different α are joined; on heating the pair bends towards the metal "
                 "with the smaller expansion, and that bending can open or close a switch.",
                 "જુદા α વાળી બે ધાતુઓ જોડાય છે; ગરમ કરતાં જોડી ઓછા પ્રસરણવાળી ધાતુ તરફ વળે, અને એ વળવું "
                 "સ્વિચ ખોલી કે બંધ કરી શકે.")},
         {"q": T("Which temperature is the same on both scales?",
                 "કયું તાપમાન બંને માપક્રમ પર સમાન છે?"),
          "a": T("−40°, because −40 °C converts to (9/5)(−40) + 32 = −40 °F.",
                 "−40°, કારણ કે −40 °C નું (9/5)(−40) + 32 = −40 °F થાય.")},
     ]},
    {"title": T("Conduction and expansion", "વહન અને પ્રસરણ"),
     "items": [
         {"q": T("Define the coefficient of thermal conductivity and give its unit.",
                 "ઉષ્મીય વાહકતાના ગુણાંકની વ્યાખ્યા અને એકમ આપો."),
          "a": T("The heat conducted per second through unit area of unit thickness with unit "
                 "temperature difference across it, in W/(m·K).",
                 "એકમ ક્ષેત્રફળ, એકમ જાડાઈ અને એકમ તાપમાન તફાવત માટે પ્રતિ સેકન્ડ વહેતી ઉષ્મા, W/(m·K) માં.")},
         {"q": T("Why do gaps get left between railway rails?",
                 "રેલવે પાટા વચ્ચે જગ્યા કેમ રખાય?"),
          "a": T("To leave room for ΔL = α L ΔT in summer; without a gap the expansion would buckle "
                 "the track sideways.",
                 "ઉનાળામાં ΔL = α L ΔT માટે જગ્યા રહે તે માટે; જગ્યા ન હોય તો પ્રસરણ પાટાને બાજુમાં વાંકો "
                 "કરી નાખે.")},
         {"q": T("Which metal is the best conductor of heat and why is it not always used?",
                 "કઈ ધાતુ ઉષ્માની શ્રેષ્ઠ વાહક છે અને તે હંમેશા કેમ વપરાતી નથી?"),
          "a": T("Silver, with k = 430 W/(m·K), followed closely by copper at 400; silver is too "
                 "expensive and soft for pipes and heat sinks, so copper is used instead.",
                 "ચાંદી, k = 430 W/(m·K), પછી તરત તાંબું 400 સાથે; ચાંદી પાઇપ અને હીટ સિંક માટે બહુ "
                 "મોંઘી અને નરમ છે, તેથી તેના સ્થાને તાંબું વપરાય.")},
         {"q": T("Why is a difference of 1 °C equal to a difference of 1 K?",
                 "1 °C નો તફાવત 1 K ના તફાવત જેટલો કેમ છે?"),
          "a": T("The two scales have the same size of degree and differ only in their zero, so a "
                 "difference is the same number on both; only absolute readings shift by 273.15.",
                 "બંને માપક્રમમાં અંશનું માપ સરખું છે અને ફક્ત શૂન્ય જુદું છે, તેથી તફાવત બંનેમાં સમાન આંકડો "
                 "થાય; ફક્ત નિરપેક્ષ વાંચન 273.15 જેટલું ખસે.")},
         {"q": T("Why does a car engine need a radiator and not just a fan?",
                 "કાર એન્જિનને ફક્ત પંખાને બદલે રેડિયેટર કેમ જોઈએ?"),
          "a": T("The fan only moves air; the radiator first passes the heat from the coolant to the "
                 "metal tubes by conduction and then to the air by convection over a large area, which "
                 "is what actually removes the heat.",
                 "પંખો ફક્ત હવા ખસેડે; રેડિયેટર પહેલાં ઠારકની ઉષ્મા વહનથી ધાતુની નળીમાં અને પછી મોટા "
                 "ક્ષેત્રફળ પર સંવહનથી હવામાં લઈ જાય, અને એ જ ખરેખર ઉષ્મા દૂર કરે.")},
         {"q": T("Why is invar used in precision instruments?",
                 "ચોક્કસ ઉપકરણોમાં ઇન્વાર કેમ વપરાય?"),
          "a": T("Its coefficient of linear expansion is about 1 × 10⁻⁶ K⁻¹, roughly twelve times "
                 "smaller than steel, so its length hardly changes with temperature.",
                 "તેનો રેખીય પ્રસરણ ગુણાંક લગભગ 1 × 10⁻⁶ K⁻¹ છે, સ્ટીલ કરતાં લગભગ બાર ગણો નાનો, તેથી તેની "
                 "લંબાઈ તાપમાન સાથે ભાગ્યે જ બદલાય.")},
     ]},
]

_PRACTICE = [
    (T("Distinguish heat from temperature and give the unit of each.",
       "ઉષ્મા અને તાપમાનમાં ભેદ આપો અને દરેકનો એકમ જણાવો."),
     3,
     [P("Heat is energy that flows from a hotter body to a colder one; its SI unit is the joule and "
        "1 cal = 4.186 J. Temperature measures the degree of hotness and its SI unit is the kelvin.",
        "ઉષ્મા એ ઊર્જા છે જે ગરમ શરીરથી ઠંડા તરફ વહે; તેનો SI એકમ જૂલ અને 1 cal = 4.186 J. તાપમાન ગરમીનું "
        "માપ છે અને તેનો SI એકમ કેલ્વિન છે."),
      P("The same temperature does not mean the same heat: a bucket of water at 60 °C holds more "
        "internal energy than a spoon at 90 °C, because heat also depends on mass.",
        "સમાન તાપમાન એટલે સમાન ઉષ્મા નહીં: 60 °C ની ડોલમાં 90 °C ના ચમચા કરતાં વધુ આંતરિક ઊર્જા હોય, કારણ કે "
        "ઉષ્મા દળ પર પણ આધાર રાખે."),
      P("In equations heat appears as Q = m c ΔT, while temperature appears as ΔT alone. Two bodies in "
        "contact stop exchanging heat when their temperatures are equal, not when their heats are equal.",
        "સૂત્રોમાં ઉષ્મા Q = m c ΔT તરીકે આવે, જ્યારે તાપમાન ફક્ત ΔT તરીકે. સંપર્કમાં રહેલાં બે શરીર જ્યારે "
        "તેમનાં તાપમાન સમાન થાય ત્યારે ઉષ્મા બદલવાનું બંધ કરે, ઉષ્મા સમાન થાય ત્યારે નહીં.")]),
    (T("Explain conduction, convection and radiation with one engineering example each.",
       "વહન, સંવહન અને વિકિરણ દરેકના એક ઇજનેરી ઉદાહરણ સાથે સમજાવો."),
     4,
     [P("Conduction passes energy molecule to molecule without bulk motion, so it needs a solid "
        "medium; the copper base of a pan and a transistor heat sink rely on it.",
        "વહન અણુથી અણુ ઊર્જા પસાર કરે, પદાર્થ ખસે નહીં, તેથી તેને ઘન માધ્યમ જોઈએ; તપેલીનો તાંબાનો તળિયો "
        "અને ટ્રાન્ઝિસ્ટરનો હીટ સિંક તેના પર આધાર રાખે."),
      P("Convection carries energy by moving the fluid itself: hot fluid rises and cold fluid sinks. "
        "A car radiator and a room radiator both work this way.",
        "સંવહન પ્રવાહીને પોતાને ખસેડીને ઊર્જા લઈ જાય: ગરમ પ્રવાહી ઉપર જાય અને ઠંડું નીચે આવે. કારનું "
        "રેડિયેટર અને રૂમનું રેડિયેટર બંને એમ કામ કરે."),
      P("Radiation needs no medium at all, because energy travels as electromagnetic waves; the Sun "
        "warming the Earth through vacuum is the standard example, and an infrared heater in a workshop "
        "uses the same mechanism.",
        "વિકિરણને કોઈ માધ્યમની જરૂર જ નથી, કારણ કે ઊર્જા વિદ્યુતચુંબકીય તરંગો તરીકે ચાલે; શૂન્યાવકાશમાંથી "
        "સૂર્યની ઉષ્મા પૃથ્વી સુધી પહોંચવી એ મુખ્ય ઉદાહરણ છે, અને કારખાનાનો ઇન્ફ્રારેડ હીટર એ જ રીતે કામ કરે.")]),
    (T("Convert 50 °C into K and °F, and state the conversion formulas.",
       "50 °C ને K અને °F માં ફેરવો અને સૂત્રો જણાવો."),
     3,
     [P("Formulas: K = °C + 273.15 and °F = (9/5) °C + 32, with the inverse °C = (5/9)(°F − 32).",
        "સૂત્રો: K = °C + 273.15 અને °F = (9/5) °C + 32, તેમજ વ્યસ્ત °C = (5/9)(°F − 32)."),
      P("For 50 °C: K = 50 + 273.15 = 323.15 K and °F = 90 + 32 = 122 °F.",
        "50 °C માટે: K = 50 + 273.15 = 323.15 K અને °F = 90 + 32 = 122 °F."),
      P("Note that only absolute temperatures are shifted by 273.15; a difference of 50 °C is a "
        "difference of 50 K but of 90 °F, which is where most conversion errors come from.",
        "ધ્યાન રાખો કે ફક્ત નિરપેક્ષ તાપમાનમાં 273.15 ઉમેરાય; 50 °C નો તફાવત 50 K નો પણ 90 °F નો તફાવત "
        "છે, અને મોટા ભાગની ભૂલો ત્યાં જ થાય.")]),
    (T("Define specific heat and heat capacity, and explain why water is a good coolant.",
       "વિશિષ્ટ ઉષ્મા અને ઉષ્મા ધારિતાની વ્યાખ્યા આપો અને પાણી સારું ઠારક કેમ છે તે સમજાવો."),
     4,
     [P("Specific heat c = Q/(m ΔT) is the heat per kilogram per kelvin, in J/(kg·K); heat capacity "
        "C = m c = Q/ΔT is the same for a whole object, in J/K.",
        "વિશિષ્ટ ઊષ્મા c = Q/(m ΔT) એ પ્રતિ કિલોગ્રામ પ્રતિ કેલ્વિન ઉષ્મા છે, J/(kg·K) માં; ઉષ્મા ધારિતા "
        "C = m c = Q/ΔT એ આખી વસ્તુ માટે એ જ છે, J/K માં."),
      P("Water has c = 4186 J/(kg·K), about ten times that of copper, so for the same heat it warms up "
        "far less; that is why it carries heat away in a radiator or a cooling tower.",
        "પાણીનો c = 4186 J/(kg·K) છે, તાંબા કરતાં લગભગ દશ ગણો, તેથી એટલી જ ઉષ્મા માટે તે ઘણું ઓછું ગરમ "
        "થાય; તેથી જ તે રેડિયેટર કે કૂલિંગ ટાવરમાં ઉષ્મા દૂર લઈ જાય."),
      P("Heating 2 kg of water by 30 K takes 2.51 × 10⁵ J, whereas the same energy would raise 2 kg of "
        "copper by over 300 K — a useful check when choosing a coolant.",
        "2 kg પાણીનું તાપમાન 30 K વધારવા 2.51 × 10⁵ J જોઈએ, જ્યારે એટલી જ ઊર્જા 2 kg તાંબાનું તાપમાન "
        "300 K થી વધુ વધારે — ઠારક પસંદ કરતી વખતે આ ઉપયોગી ચકાસણી છે.")]),
    (T("Describe a mercury thermometer and a bimetallic thermometer with their uses.",
       "પારા થર્મોમીટર અને બાયમેટાલિક થર્મોમીટર તેમના ઉપયોગ સાથે વર્ણવો."),
     4,
     [P("A mercury thermometer is a glass bulb with a fine uniform bore; the mercury expands up the "
        "tube and the reading is taken at the top of the convex column against a graduated scale.",
        "પારા થર્મોમીટરમાં કાચનો બલ્બ અને સરખી પાતળી બોર હોય; પારો નળીમાં ઉપર ચઢે અને વાંચન ક્રમાંકિત "
        "માપપટ્ટી સામે બહિર્ગોળ સ્તંભની ટોચે લેવાય."),
      P("Mercury suits this because it does not wet glass, is opaque, expands evenly and stays liquid "
        "from −39 °C to 357 °C; the range is its main limitation.",
        "પારો એટલા માટે યોગ્ય છે કે તે કાચને ભીનો કરતો નથી, અપારદર્શક છે, સરખી રીતે ફેલાય અને −39 °C થી "
        "357 °C સુધી પ્રવાહી રહે; એ શ્રેણી તેની મુખ્ય મર્યાદા છે."),
      P("A bimetallic thermometer joins two strips of different α; heating bends the pair and the free "
        "end moves a pointer or a switch. It gives no fine number but switches a circuit, so it is used "
        "in irons, ovens and fire alarms.",
        "બાયમેટાલિક થર્મોમીટર જુદા α વાળી બે પટ્ટીઓ જોડે; ગરમ કરતાં જોડી વળે અને મુક્ત છેડો સૂચક કે સ્વિચ "
        "ખસેડે. તે સૂક્ષ્મ આંકડો આપતું નથી પણ પરિપથ બદલે, તેથી ઇસ્ત્રી, ઓવન અને આગ-ચેતવણીમાં વપરાય.")]),
    (T("Define the coefficient of thermal conductivity and solve one problem with it.",
       "ઉષ્મીય વાહકતાના ગુણાંકની વ્યાખ્યા આપો અને તેનો એક દાખલો ઉકેલો."),
     4,
     [P("k is the heat conducted per second through 1 m² of a slab 1 m thick when the faces differ by "
        "1 K: Q/t = k A ΔT/L, with k in W/(m·K).",
        "k એ 1 K તફાવતવાળા, 1 m જાડા અને 1 m² ક્ષેત્રફળના પટ્ટામાંથી પ્રતિ સેકન્ડ વહેતી ઉષ્મા છે: "
        "Q/t = k A ΔT/L, k W/(m·K) માં."),
      P("For a brick wall 0.2 m thick and 10 m² with 15 K across it: Q/t = 0.6 × 10 × 15/0.2 = 450 W.",
        "0.2 m જાડી, 10 m² અને 15 K તફાવતવાળી ઇંટની દીવાલ માટે: Q/t = 0.6 × 10 × 15/0.2 = 450 W."),
      P("Because air has k = 0.026 W/(m·K), the best insulators are materials that trap still air — "
        "wool, foam, fibre glass and double glazing — rather than dense solids.",
        "હવાનો k = 0.026 W/(m·K) હોવાથી શ્રેષ્ઠ અવાહક એવા પદાર્થો છે જે સ્થિર હવા પકડે — ઊન, ફોમ, "
        "ફાઇબર ગ્લાસ અને બેવડું કાચ — ઘન પદાર્થ નહીં.")]),
    (T("Explain linear expansion and derive the expression for it from the definition of α.",
       "રેખીય પ્રસરણ સમજાવો અને α ની વ્યાખ્યામાંથી તેનું સૂત્ર મેળવો."),
     4,
     [P("When a rod of length L is heated through ΔT, experiment shows ΔL ∝ L and ΔL ∝ ΔT for small "
        "changes, so ΔL = α L ΔT.",
        "L લંબાઈનો સળિયો ΔT ગરમ થાય ત્યારે પ્રયોગ દર્શાવે કે નાના ફેરફાર માટે ΔL ∝ L અને ΔL ∝ ΔT, "
        "તેથી ΔL = α L ΔT."),
      P("Here α is the fractional change of length per kelvin, in K⁻¹: α = (ΔL/L)/ΔT. For steel it is "
        "12 × 10⁻⁶ K⁻¹.",
        "અહીં α એ પ્રતિ કેલ્વિન લંબાઈમાં અંશતઃ ફેરફાર છે, K⁻¹ માં: α = (ΔL/L)/ΔT. સ્ટીલ માટે તે "
        "12 × 10⁻⁶ K⁻¹ છે."),
      P("A 10 m rail heated by 40 K therefore grows by 4.8 mm, which is why a gap is left at every "
        "joint, and why a bimetallic strip bends when the two metals expand differently.",
        "તેથી 10 m પાટો 40 K ગરમ થતાં 4.8 mm વધે, અને તેથી જ દરેક જોડ પર જગ્યા રખાય, અને બે ધાતુઓ જુદી "
        "રીતે પ્રસરે ત્યારે બાયમેટાલિક પટ્ટી વળે.")]),
    (T("A wall 0.2 m thick loses 450 W through 10 m² with 15 K across it. Find k.",
       "0.2 m જાડી દીવાલ 10 m² માંથી 15 K તફાવતે 450 W ગુમાવે છે. k શોધો."),
     3,
     [P("Use Q/t = k A ΔT/L and rearrange for k.", "Q/t = k A ΔT/L વાપરો અને k માટે ગોઠવો."),
      P("k = (Q/t) L/(A ΔT) = 450 × 0.2/(10 × 15) = 90/150 = 0.6 W/(m·K).",
        "k = (Q/t) L/(A ΔT) = 450 × 0.2/(10 × 15) = 90/150 = 0.6 W/(m·K)."),
      P("That is the handbook value for brick, which confirms the measurement; the same wall in "
        "copper would pass about 600 times more heat.",
        "આ ઇંટ માટે પુસ્તકનું મૂલ્ય છે, જે માપન ચકાસે; એ જ દીવાલ તાંબાની હોય તો લગભગ 600 ગણી વધુ ઉષ્મા "
        "પસાર કરે."),
      P("Note the units: 450 W of heat flow with 90 W·m⁻¹·K⁻¹ of k A ΔT and 0.2 m of length gives "
        "0.6 W/(m·K), and a thicker wall of the same material would cut the loss in proportion.",
        "એકમ ધ્યાનમાં લો: 450 W ઉષ્મા પ્રવાહ, k A ΔT નું 90 W·m⁻¹·K⁻¹ અને 0.2 m લંબાઈ સાથે 0.6 W/(m·K) "
        "આપે, અને એ જ પદાર્થની જાડી દીવાલ ખોટ એ જ પ્રમાણમાં ઘટાડે.")]),
    (T("Why does a bimetallic strip bend on heating? Give two applications.",
       "બાયમેટાલિક પટ્ટી ગરમ થતાં કેમ વળે? બે ઉપયોગો આપો."),
     3,
     [P("The two metals have different coefficients of linear expansion, so for the same ΔT one grows "
        "more than the other; since they are joined, the pair must curve.",
        "બે ધાતુઓના રેખીય પ્રસરણ ગુણાંક જુદા હોય, તેથી એ જ ΔT માટે એક બીજા કરતાં વધુ વધે; બંને જોડાયેલા "
        "હોવાથી જોડીએ વળવું પડે."),
      P("A brass–iron strip 5 cm long with 200 K rise moves by (19 − 12) × 10⁻⁶ × 0.05 × 200 = 0.07 mm, "
        "and a longer strip multiplies that movement.",
        "5 cm લાંબી પિત્તળ-લોખંડ પટ્ટી 200 K વધારે ત્યારે (19 − 12) × 10⁻⁶ × 0.05 × 200 = 0.07 mm ખસે, "
        "અને લાંબી પટ્ટી એ હલનચલન ગણું કરે."),
      P("Applications: the thermostat in an electric iron, which opens the contact above the set "
        "temperature, and the fire alarm or the bimetallic thermometer, where the movement drives a "
        "pointer.",
        "ઉપયોગો: ઇલેક્ટ્રિક ઇસ્ત્રીનો થર્મોસ્ટેટ, જે નક્કી કરેલા તાપમાનથી ઉપર સંપર્ક ખોલે, અને આગ-ચેતવણી "
        "કે બાયમેટાલિક થર્મોમીટર, જ્યાં હલનચલન સૂચક ચલાવે.")]),
    (T("50 kg of water is heated from 25 °C to 65 °C in 40 minutes. Find the heat and the power.",
       "50 kg પાણી 40 મિનિટમાં 25 °C થી 65 °C સુધી ગરમ થાય. ઉષ્મા અને પાવર શોધો."),
     4,
     [P("Q = m c ΔT = 50 × 4186 × 40 = 8.37 × 10⁶ J.", "Q = m c ΔT = 50 × 4186 × 40 = 8.37 × 10⁶ J."),
      P("t = 40 minutes = 2400 s, so P = Q/t = 8.37 × 10⁶/2400 = 3.49 × 10³ W.",
        "t = 40 મિનિટ = 2400 s, તેથી P = Q/t = 8.37 × 10⁶/2400 = 3.49 × 10³ W."),
      P("A real geyser is rated higher, about 4 to 5 kW, because the tank and the surroundings also take "
        "up heat; the extra rating covers those losses.",
        "વાસ્તવિક ગીઝર વધુ ક્ષમતાનું, લગભગ 4 થી 5 kW, હોય છે, કારણ કે ટાંકી અને આસપાસ પણ ઉષ્મા લે; વધારાની "
        "ક્ષમતા એ ખોટ પૂરી કરે."),
      P("The bill follows the energy, not the power: 3.5 kW for 40 minutes is 2.3 kWh, so the running "
        "cost is set by the 8.37 MJ of heat and by the efficiency of the element.",
        "બિલ પાવરને નહીં પણ ઊર્જાને અનુસરે: 40 મિનિટ માટે 3.5 kW એટલે 2.3 kWh, તેથી ખર્ચ 8.37 MJ ઉષ્મા અને "
        "હીટિંગ એલિમેન્ટની કાર્યક્ષમતાથી નક્કી થાય.")]),
    (T("Explain why still air is a better insulator than most solids.",
       "સ્થિર હવા મોટા ભાગના ઘન કરતાં સારું અવાહક કેમ છે તે સમજાવો."),
     4,
     [P("Heat in a gas is carried by molecular collisions, and air molecules are far apart, so the "
        "conductivity of still air is only 0.026 W/(m·K), against 400 for copper and 0.6 for brick.",
        "વાયુમાં ઉષ્મા અણુઓની અથડામણથી ચાલે, અને હવાના અણુઓ ઘણા દૂર હોય, તેથી સ્થિર હવાની વાહકતા ફક્ત "
        "0.026 W/(m·K) છે, જ્યારે તાંબાની 400 અને ઇંટની 0.6."),
      P("The catch is that air must be trapped: if it can move, convection carries heat quickly, which "
        "is why a single pane of glass is a poor insulator but two panes with a sealed gap are good.",
        "શરત એ છે કે હવા પકડાયેલી રહે: જો તે ખસી શકે તો સંવહન ઝડપથી ઉષ્મા લઈ જાય, તેથી જ એક પાનાનો કાચ "
        "નબળો અવાહક છે પણ સીલબંધ જગ્યાવાળા બે પાના સારા."),
      P("Wool, foam and fibreglass work the same way: they are mostly air held in small pockets, and "
        "their solid part contributes very little conduction.",
        "ઊન, ફોમ અને ફાઇબરગ્લાસ એ જ રીતે કામ કરે: તેમાં મોટા ભાગે નાના ખાનાંમાં પકડાયેલી હવા હોય, અને તેમનો "
        "ઘન ભાગ વહનમાં ઘણું ઓછું ફાળો આપે.")]),
    (T("2 kg of water at 80 °C is mixed with 3 kg at 20 °C. Find the final temperature.",
       "80 °C નું 2 kg પાણી 20 °C ના 3 kg સાથે ભળે છે. અંતિમ તાપમાન શોધો."),
     3,
     [P("Heat lost by the hot water equals heat gained by the cold water: m₁c(80 − θ) = m₂c(θ − 20).",
        "ગરમ પાણીની ખોટ = ઠંડા પાણીનો લાભ: m₁c(80 − θ) = m₂c(θ − 20)."),
      P("2(80 − θ) = 3(θ − 20), so 160 − 2θ = 3θ − 60 and 5θ = 220.",
        "2(80 − θ) = 3(θ − 20), તેથી 160 − 2θ = 3θ − 60 અને 5θ = 220."),
      P("θ = 44 °C; it lies nearer 20 °C than 80 °C because there is more cold water — a quick check "
        "that the answer is sensible.", "θ = 44 °C; તે 80 °C કરતાં 20 °C ની નજીક છે કારણ કે ઠંડું પાણી "
        "વધુ છે — જવાબ વાજબી છે તેની ઝડપી ચકાસણી."),
      P("The specific heat cancels because both masses are water; with two different liquids it does "
        "not, and the same working becomes m₁c₁(80 − θ) = m₂c₂(θ − 20), which is how a calorimeter "
        "measures an unknown specific heat.",
        "બંને દળ પાણી હોવાથી વિશિષ્ટ ઉષ્મા રદ થાય; બે જુદા પ્રવાહી હોય તો ન રદ થાય, અને એ જ ગણતરી "
        "m₁c₁(80 − θ) = m₂c₂(θ − 20) બને, જે રીતે કેલરીમીટર અજાણી વિશિષ્ટ ઉષ્મા માપે.")]),
    (T("Why must the thickness be in metres and ΔT be a difference in Fourier's law?",
       "ફોરિયરના નિયમમાં જાડાઈ મીટરમાં અને ΔT તફાવત કેમ હોવો જોઈએ?"),
     3,
     [P("The law Q/t = k A ΔT/L is written for SI units, so k in W/(m·K) expects A in m², L in m and a "
        "difference in K (or °C, which is the same size).",
        "નિયમ Q/t = k A ΔT/L SI એકમો માટે લખાયો છે, તેથી W/(m·K) માંનો k એ A ને m², L ને m અને તફાવતને "
        "K (કે °C, જે સમાન માપ છે) માં ધારે."),
      P("Using 2 mm as 2 instead of 0.002 m makes the answer a thousand times too small, a mistake that "
        "shows up immediately as a wall losing almost no heat.",
        "2 mm ને 0.002 m ને બદલે 2 લેવાથી જવાબ હજાર ગણો નાનો થાય, અને એ ભૂલ તરત દેખાય કે દીવાલ લગભગ ઉષ્મા "
        "ગુમાવતી જ નથી."),
      P("ΔT must be the difference between the two faces, never the temperature of one face, because "
        "heat flow depends on the gradient and not on the absolute level.",
        "ΔT બે સપાટી વચ્ચેનો તફાવત હોવો જોઈએ, એક સપાટીનું તાપમાન નહીં, કારણ કે ઉષ્મા પ્રવાહ પ્રવણતા પર "
        "આધાર રાખે, નિરપેક્ષ સ્તર પર નહીં."),
      P("The check is the size of the answer: a 10 m² wall with a 15 K difference should lose a few "
        "hundred watts. Any result in megawatts, or a wall that loses almost nothing, points to a unit "
        "slip rather than to a new effect.",
        "ચકાસણી જવાબના માપમાં છે: 15 K તફાવતવાળી 10 m² દીવાલે થોડા સો વૉટ ગુમાવવા જોઈએ. મેગાવૉટમાં આવતો "
        "જવાબ, કે લગભગ કંઈ જ ન ગુમાવતી દીવાલ, નવી અસરને બદલે એકમની ભૂલ દર્શાવે.")]),
]

EXAM = [{"q": q, "marks": m} for q, m, _parts in _PRACTICE]
PRACTICE_ANSWERS = [_join(parts) for _q, _m, parts in _PRACTICE]

LESSON_COUNT = sum(len(s["items"]) for s in NOTES)
