"""DI01000121 Applied Physics - Unit 5: Waves, Ultrasonic and Semiconductor (bilingual en + gu).

GTU 5.1-5.8, 10 h, 24 %, 17 marks, CO5.
"""
from content_DI01000121_u1_notes import T, P, H4, UL, OL, TB, card, num, _join

SOURCES = [
    T("GTU DI01000121 Applied Physics syllabus (uploaded PDF, w.e.f. 2024-25)",
      "GTU DI01000121 એપ્લાઇડ ફિઝિક્સ સિલેબસ (અપલોડ કરેલ PDF, 2024-25થી અમલમાં)"),
    T("NCERT Physics Class XI, Part II - Waves, and Class XII - Semiconductor Electronics",
      "NCERT ભૌતિક વિજ્ઞાન ધોરણ 11 ભાગ 2 - તરંગો, અને ધોરણ 12 - અર્ધવાહક ઇલેક્ટ્રોનિક્સ"),
    T("H. C. Verma - Concepts of Physics, Vol. I chapter 15 and Vol. II chapter 45",
      "એચ. સી. વર્મા - કોન્સેપ્ટ્સ ઓફ ફિઝિક્સ, ભાગ 1 પ્રકરણ 15 અને ભાગ 2 પ્રકરણ 45"),
    T("M. N. Avadhanulu - A Textbook of Engineering Physics, acoustics and semiconductor chapters",
      "એમ. એન. અવધાનુલુ - ટેક્સ્ટબુક ઓફ એન્જિનિયરિંગ ફિઝિક્સ, ધ્વનિશાસ્ત્ર અને અર્ધવાહક પ્રકરણો"),
    T("IS 2526 (acoustics) and manufacturer data for ultrasonic and diode devices",
      "IS 2526 (ધ્વનિશાસ્ત્ર) અને અલ્ટ્રાસોનિક તથા ડાયોડ ઉપકરણો માટે ઉત્પાદકના આંકડા"),
]

NOTES = [
    {"title": T("1. Waves and their Parameters", "1. તરંગો અને તેમના પરિમાણો"),
     "items": [
         card(T("1.1 Wave motion, longitudinal and transverse waves",
                "1.1 તરંગ ગતિ, સંગત તથા અનુપ્રસ્થ તરંગો"),
              [H4("Definition", "વ્યાખ્યા"),
               P("A <b>wave</b> is a disturbance that carries energy from one place to another without "
                 "carrying matter. In <b>mechanical</b> waves the disturbance travels through a medium; "
                 "in <b>electromagnetic</b> waves it travels as changing fields and needs no medium.",
                 "<b>તરંગ</b> એ એવી વિક્ષોભ છે જે પદાર્થ લઈ જ્યા વગર ઊર્જા એક જગ્યાએથી બીજી જગ્યાએ "
                 "પહોંચાડે. <b>યાંત્રિક</b> તરંગોમાં વિક્ષોભ માધ્યમમાંથી પસાર થાય; "
                 "<b>વિદ્યુતચુંબકીય</b> તરંગોમાં તે બદલાતાં ક્ષેત્રો તરીકે ચાલે અને માધ્યમની જરૂર નથી."),
               H4("Two kinds", "બે પ્રકાર"),
               TB([T("Wave", "તરંગ"), T("Particles move", "કણો ખસે"), T("Examples", "ઉદાહરણો")],
                  [[T("transverse", "અનુપ્રસ્થ"), T("perpendicular to the wave direction", "તરંગની દિશાને લંબરૂપે"), T("light, a wave on a string, ripples on water", "પ્રકાશ, દોરી પરનું તરંગ, પાણી પરની વમળ")],
                   [T("longitudinal", "સંગત"), T("along the wave direction", "તરંગની દિશામાં જ"), T("sound in air, a compression in a spring", "હવામાં ધ્વનિ, સ્પ્રિંગમાં સંકોચન")]]),
               H4("What travels and what does not", "શું ચાલે અને શું નહીં"),
               UL(("Energy travels; the particles only oscillate about a fixed point.",
                   "ઊર્જા ચાલે; કણો ફક્ત પોતાના સ્થાનની આસપાસ દોલિત થાય."),
                  ("Sound needs a medium, which is why a bell in a vacuum jar is silent.",
                   "ધ્વનિને માધ્યમ જોઈએ, તેથી શૂન્યાવકાશના પાત્રમાં ઘંટડી મૌન રહે."),
                  ("A wave carries momentum and can carry information, which is why every "
                   "communication system is built on waves.",
                   "તરંગ વેગમાન અને માહિતી લઈ જાય, તેથી જ દરેક સંદેશાવ્યવહાર તંત્ર તરંગો પર બંધાયું છે.")),
               H4("Worked example", "ઉકેલાયેલ દાખલો"),
               P("A sound wave of 340 m/s passing a point makes the air molecules move back and forth by "
                 "about 10 µm, yet the compression itself travels many metres and reaches your ear.",
                 "340 m/s નું ધ્વનિ તરંગ એક બિંદુ પાસેથી પસાર થાય ત્યારે હવાના અણુઓ લગભગ 10 µm "
                 "આગળ-પાછળ ખસે, પણ સંકોચન પોતે ઘણા મીટર ચાલીને તમારા કાન સુધી પહોંચે."),
               H4("Common mistake", "સામાન્ય ભૂલ"),
               P("Thinking the medium moves with the wave. The medium oscillates in place; only the "
                 "pattern and the energy move forward.",
                 "તરંગ સાથે માધ્યમ પણ ચાલે એમ માનવું. માધ્યમ પોતાની જગ્યાએ દોલિત થાય; ફક્ત આકૃતિ અને "
                 "ઊર્જા આગળ વધે.")],
              "u5_wave", syllabus_item="5.1"),
         card(T("1.2 Frequency, time period, amplitude, wavelength and wave velocity",
                "1.2 આવૃત્તિ, આવર્તકાળ, કંપવિસ્તાર, તરંગલંબાઈ અને તરંગ વેગ"),
              [H4("The five quantities", "પાંચ રાશિઓ"),
               TB([T("Quantity", "રાશિ"), T("Meaning", "અર્થ"), T("Unit", "એકમ")],
                  [[T("amplitude a", "કંપવિસ્તાર a"), T("largest displacement from rest", "સ્થાનથી સૌથી વધુ ખસવું"), T("m", "m")],
                   [T("wavelength λ", "તરંગલંબાઈ λ"), T("distance between two crests", "બે શિખર વચ્ચેનું અંતર"), T("m", "m")],
                   [T("frequency f", "આવૃત્તિ f"), T("oscillations per second", "પ્રતિ સેકન્ડ દોલન"), T("Hz", "Hz")],
                   [T("time period T", "આવર્તકાળ T"), T("time for one oscillation, T = 1/f", "એક દોલનનો સમય, T = 1/f"), T("s", "s")],
                   [T("velocity v", "વેગ v"), T("v = f λ, set by the medium", "v = f λ, માધ્યમ નક્કી કરે"), T("m/s", "m/s")]]),
               H4("The one relation to remember", "યાદ રાખવાનો એક સંબંધ"),
               P("<b>v = f λ</b>. When sound passes from air into water its speed rises and, because the "
                 "source fixes f, the wavelength must rise with it.",
                 "<b>v = f λ</b>. ધ્વનિ હવામાંથી પાણીમાં જાય ત્યારે તેનો વેગ વધે અને, સ્રોત f નક્કી કરતો "
                 "હોવાથી, તરંગલંબાઈ પણ વધવી પડે."),
               H4("Typical speeds", "સામાન્ય વેગ"),
               TB([T("Medium", "માધ્યમ"), T("Speed of sound", "ધ્વનિનો વેગ")],
                  [[T("air at 20 °C", "20 °C પર હવા"), T("343 m/s", "343 m/s")],
                   [T("water", "પાણી"), T("1480 m/s", "1480 m/s")],
                   [T("steel", "સ્ટીલ"), T("about 5000 m/s", "લગભગ 5000 m/s")],
                   [T("light in vacuum", "શૂન્યાવકાશમાં પ્રકાશ"), T("3 × 10⁸ m/s", "3 × 10⁸ m/s")]]),
               H4("Worked example", "ઉકેલાયેલ દાખલો"),
               P("A tuning fork of 256 Hz in air: λ = v/f = 343/256 = 1.34 m and T = 1/256 = 3.9 ms.",
                 "હવામાં 256 Hz નો સ્વરકાંટો: λ = v/f = 343/256 = 1.34 m અને T = 1/256 = 3.9 ms."),
               H4("Common mistake", "સામાન્ય ભૂલ"),
               P("Believing frequency changes when a wave enters a new medium. The source sets f; the "
                 "medium sets v; λ adjusts to keep v = f λ.",
                 "નવા માધ્યમમાં તરંગ જાય ત્યારે આવૃત્તિ બદલાય એમ માનવું. સ્રોત f નક્કી કરે, માધ્યમ v નક્કી "
                 "કરે, અને v = f λ જળવાય તે માટે λ ગોઠવાય.")],
              "u5_wave", syllabus_item="5.2"),
     ]},

    {"title": T("2. Interference, Stationary Waves and Acoustics",
                "2. વ્યતીકરણ, સ્થિર તરંગો અને ધ્વનિશાસ્ત્ર"),
     "items": [
         card(T("2.1 Superposition, interference and stationary waves",
                "2.1 અધ્યારોપણ, વ્યતીકરણ અને સ્થિર તરંગો"),
              [H4("Principle of superposition", "અધ્યારોપણનો સિદ્ધાંત"),
               P("When two or more waves meet at a point, the resultant displacement is the vector sum "
                 "of their displacements. Where they add in phase the result is <b>constructive "
                 "interference</b>; where they cancel it is <b>destructive interference</b>.",
                 "બે કે વધુ તરંગો એક બિંદુએ મળે ત્યારે પરિણામી સ્થાનાંતરણ તેમના સ્થાનાંતરણનો સદિશ સરવાળો "
                 "હોય. સમાન કળામાં ઉમેરાય તો <b>રચનાત્મક વ્યતીકરણ</b>; રદ થાય તો <b>વિનાશાત્મક વ્યતીકરણ</b>."),
               H4("Conditions for a steady interference pattern", "સ્થિર વ્યતીકરણ આકૃતિની શરતો"),
               OL(("The two sources must be coherent: same frequency and a constant phase difference.",
                   "બે સ્રોત સહસંબંધી હોવા જોઈએ: સમાન આવૃત્તિ અને અચળ કળા તફાવત."),
                  ("Their amplitudes should be nearly equal, so that the dark fringes are really dark.",
                   "તેમના કંપવિસ્તાર લગભગ સમાન હોવા જોઈએ જેથી અંધારા પટ્ટા ખરેખર અંધારા દેખાય."),
                  ("The sources must be close together and far from the screen, so the fringes are "
                   "wide enough to see.", "સ્રોત નજીક અને પડદો દૂર હોવો જોઈએ જેથી પટ્ટા પૂરતા પહોળા દેખાય.")),
               H4("Stationary waves", "સ્થિર તરંગો"),
               P("Two identical waves travelling in opposite directions superpose to give a stationary "
                 "wave: points of zero amplitude are <b>nodes</b>, points of maximum amplitude are "
                 "<b>antinodes</b>, and the spacing is λ/2 between nodes.",
                 "વિરુદ્ધ દિશામાં ચાલતાં બે સરખાં તરંગો અધ્યારોપિત થઈને સ્થિર તરંગ આપે: શૂન્ય કંપવિસ્તારવાળાં "
                 "બિંદુ <b>નિસ્પંદ</b>, મહત્તમ કંપવિસ્તારવાળાં બિંદુ <b>પ્રસ્પંદ</b>, અને નિસ્પંદ વચ્ચેનું અંતર λ/2."),
               H4("Worked example", "ઉકેલાયેલ દાખલો"),
               P("A string of 0.75 m fixed at both ends vibrates in its fundamental mode with "
                 "λ = 2L = 1.5 m, so with v = 300 m/s the frequency is f = 300/1.5 = 200 Hz.",
                 "બંને છેડેથી બંધ 0.75 m દોરી પાયાની રીતે દોલિત થાય ત્યારે λ = 2L = 1.5 m, તેથી "
                 "v = 300 m/s સાથે આવૃત્તિ f = 300/1.5 = 200 Hz."),
               H4("Common mistake", "સામાન્ય ભૂલ"),
               P("Calling any two overlapping waves an interference pattern. Without coherence there is "
                 "no fixed pattern, only a moving flicker.",
                 "કોઈપણ બે તરંગોના મિલનને વ્યતીકરણ આકૃતિ કહેવું. સહસંબંધ વગર સ્થિર આકૃતિ હોતી નથી, ફક્ત "
                 "ચલિત ઝબકારો દેખાય.")],
              "u5_stationary", syllabus_item="5.3"),
         card(T("2.2 Reverberation, echo, noise and the absorption coefficient",
                "2.2 પ્રતિધ્વનિ, પડઘો, ઘોંઘાટ અને શોષણ ગુણાંક"),
              [H4("Definitions", "વ્યાખ્યાઓ"),
               P("<b>Reverberation</b> is the persistence of sound in a hall after the source stops, "
                 "because of repeated reflections. <b>Reverberation time</b> T is the time for the "
                 "sound level to fall by 60 dB. An <b>echo</b> is a distinct reflected sound heard "
                 "separately.",
                 "<b>પ્રતિધ્વનિ</b> એ સ્રોત બંધ થયા પછી પણ વારંવાર પરાવર્તનને કારણે ઓરડામાં ધ્વનિ ટકી "
                 "રહેવો છે. <b>પ્રતિધ્વનિ સમય</b> T એ ધ્વનિનું સ્તર 60 dB ઘટવા માટેનો સમય છે. <b>પડઘો</b> એ "
                 "અલગ સંભળાતો પરાવર્તિત ધ્વનિ છે."),
               H4("Absorption coefficient", "શોષણ ગુણાંક"),
               P("The absorption coefficient α of a surface is the fraction of the incident sound energy "
                 "it absorbs: α = 0 (perfect reflector) to α = 1 (open window, absorbs everything).",
                 "સપાટીનો શોષણ ગુણાંક α એ તેના પર પડતી ધ્વનિ ઊર્જાનો શોષાતો ભાગ છે: α = 0 (પૂર્ણ "
                 "પરાવર્તક) થી α = 1 (ખુલ્લી બારી, બધું શોષે)."),
               TB([T("Material", "પદાર્થ"), T("α at 500 Hz", "500 Hz પર α")],
                  [[T("open window", "ખુલ્લી બારી"), T("1.00", "1.00")],
                   [T("plaster on brick", "ઇંટ પર પ્લાસ્ટર"), T("0.02", "0.02")],
                   [T("glass", "કાચ"), T("0.03", "0.03")],
                   [T("wooden floor", "લાકડાનું ફર્શ"), T("0.06", "0.06")],
                   [T("curtain, heavy", "જાડો પડદો"), T("0.50", "0.50")],
                   [T("acoustic tile", "ધ્વનિ-શોષક ટાઇલ"), T("0.70", "0.70")],
                   [T("audience, per person", "શ્રોતા, પ્રતિ વ્યક્તિ"), T("0.45 m²", "0.45 m²")]]),
               H4("Why it matters", "કેમ મહત્ત્વનું"),
               P("Too long a reverberation smears speech, too short a one makes a hall sound dead; about "
                 "1 s is right for speech and 2 s for music. Noise is any unwanted sound, and its "
                 "control is part of the same design.",
                 "પ્રતિધ્વનિ બહુ લાંબી હોય તો બોલાયેલું ધૂંધળું થાય, બહુ ટૂંકી હોય તો હોલ મૃત લાગે; "
                 "બોલાયેલા શબ્દ માટે લગભગ 1 s અને સંગીત માટે 2 s યોગ્ય છે. ઘોંઘાટ એ કોઈપણ અનિચ્છનીય ધ્વનિ "
                 "છે, અને તેનું નિયંત્રણ એ જ રચનાનો ભાગ છે."),
               H4("Worked example", "ઉકેલાયેલ દાખલો"),
               P("A clap heard twice with a 0.6 s gap from a wall 102 m away: d = v t/2 = 340 × 0.6/2 = "
                 "102 m. For a distinct echo the gap must exceed about 0.1 s, i.e. 17 m.",
                 "0.6 s ના અંતરે બે વાર સંભળાતો તાળીનો અવાજ 102 m દૂરની દીવાલથી: d = v t/2 = "
                 "340 × 0.6/2 = 102 m. અલગ પડઘો સંભળાવા માટે અંતર લગભગ 0.1 s, એટલે 17 m થી વધુ હોવું જોઈએ."),
               H4("Common mistake", "સામાન્ય ભૂલ"),
               P("Forgetting the factor 2 in an echo calculation. The sound travels to the wall and back, "
                 "so the distance is v t/2, not v t.",
                 "પડઘાની ગણતરીમાં 2 નો અવયવ ભૂલવો. ધ્વનિ દીવાલ સુધી જાય અને પાછો આવે, તેથી અંતર v t/2 છે, "
                 "v t નહીં.")],
              "u5_reverb", syllabus_item="5.4"),
         card(T("2.3 Sabine's formula and the control of reverberation",
                "2.3 સેબાઇનનું સૂત્ર અને પ્રતિધ્વનિનું નિયંત્રણ"),
              [H4("The formula", "સૂત્ર"),
               P("<b>T = 0.161 V / A</b>, where V is the volume in m³ and A = Σ α S is the total "
                 "absorption in m² sabine, summed over every surface.",
                 "<b>T = 0.161 V / A</b>, જ્યાં V ઘનફળ m³ માં અને A = Σ α S એ m² સેબાઇનમાં કુલ શોષણ છે, "
                 "દરેક સપાટી પરથી સરવાળો."),
               H4("How the design uses it", "રચના તેનો ઉપયોગ કેવી રીતે કરે"),
               UL(("Fix the volume from the seating and the ceiling height.",
                   "બેઠક અને ટોચમર્યાદાની ઊંચાઈ પરથી ઘનફળ નક્કી કરો."),
                  ("Choose a target T (about 1 s for speech, 2 s for music).",
                   "લક્ષ્ય T પસંદ કરો (બોલાયેલા શબ્દ માટે લગભગ 1 s, સંગીત માટે 2 s)."),
                  ("Find the absorption A = 0.161 V/T that the room must have.",
                   "ઓરડામાં જરૂરી શોષણ A = 0.161 V/T શોધો."),
                  ("Add absorbers — tiles, curtains, carpet, audience — until Σ α S reaches A.",
                   "શોષક ઉમેરો — ટાઇલ, પડદા, જાજમ, શ્રોતા — જ્યાં સુધી Σ α S એ A સુધી ન પહોંચે.")),
               H4("Other ways to control it", "નિયંત્રણની બીજી રીતો"),
               TB([T("Problem", "સમસ્યા"), T("Remedy", "ઉપાય")],
                  [[T("T too long, speech unclear", "T લાંબી, બોલાયેલું અસ્પષ્ટ"), T("add absorbers and a sound-absorbing ceiling", "શોષક અને ધ્વનિ-શોષક ટોચમર્યાદા ઉમેરો")],
                   [T("T too short, hall sounds dead", "T ટૂંકી, હોલ મૃત લાગે"), T("use hard reflective panels and a smaller volume", "કઠણ પરાવર્તક પેનલ અને નાનું ઘનફળ વાપરો")],
                   [T("echo from a rear wall", "પાછળની દીવાલથી પડઘો"), T("tilt or treat that wall, or move the stage", "એ દીવાલ નમાવો કે સારવાર આપો, અથવા મંચ ખસેડો")],
                   [T("noise from outside", "બહારથી ઘોંઘાટ"), T("double glazing, seals and a lobby", "બેવડું કાચ, સીલ અને લોબી")]]),
               H4("Worked example", "ઉકેલાયેલ દાખલો"),
               P("A hall 20 × 15 × 8 m has V = 2400 m³. With A = 240 m² sabine, T = 0.161 × 2400/240 = "
                 "1.61 s; to bring it to 1.0 s the room needs A = 386 m², i.e. 146 m² more absorption.",
                 "20 × 15 × 8 m ના હોલનું V = 2400 m³. A = 240 m² સેબાઇન સાથે "
                 "T = 0.161 × 2400/240 = 1.61 s; તેને 1.0 s પર લાવવા A = 386 m² જોઈએ, એટલે 146 m² વધુ શોષણ."),
               H4("Common mistake", "સામાન્ય ભૂલ"),
               P("Adding α values instead of α S products, or forgetting the audience, which is often "
                 "the largest absorber in a full hall.",
                 "α S ગુણાકારને બદલે α નાં મૂલ્યો સરવાળવા, અથવા શ્રોતાઓ ભૂલવા, જે ભરેલા હોલમાં ઘણી વાર "
                 "સૌથી મોટું શોષક હોય છે.")],
              "u5_reverb", syllabus_item="5.5"),
     ]},

    {"title": T("3. Ultrasonic Waves", "3. અલ્ટ્રાસોનિક તરંગો"),
     "items": [
         card(T("3.1 Ultrasonic waves, their properties and applications",
                "3.1 અલ્ટ્રાસોનિક તરંગો, તેમના ગુણધર્મો અને ઉપયોગો"),
              [H4("Definition", "વ્યાખ્યા"),
               P("<b>Ultrasonic</b> waves are sound waves above about 20 kHz, the upper limit of human "
                 "hearing. Infrasonic waves lie below 20 Hz.",
                 "<b>અલ્ટ્રાસોનિક</b> તરંગો લગભગ 20 kHz થી ઉપરનાં ધ્વનિ તરંગો છે, જે માનવ શ્રવણની ઉપલી "
                 "મર્યાદા છે. ઇન્ફ્રાસોનિક તરંગો 20 Hz થી નીચે હોય."),
               H4("Properties", "ગુણધર્મો"),
               UL(("High frequency means a short wavelength: at 40 kHz in air λ is only 8.6 mm.",
                   "વધુ આવૃત્તિ એટલે ટૂંકી તરંગલંબાઈ: હવામાં 40 kHz પર λ ફક્ત 8.6 mm."),
                  ("They travel in a narrow beam, so they can be aimed and focused.",
                   "તેઓ સાંકડા કિરણપુંજમાં ચાલે, તેથી લક્ષ્ય બનાવી શકાય અને કેન્દ્રિત કરી શકાય."),
                  ("They reflect at a boundary, so an echo gives distance and a picture.",
                   "સીમા પર પરાવર્તિત થાય, તેથી પડઘો અંતર અને ચિત્ર આપે."),
                  ("High energy density produces cavitation, used for cleaning and welding.",
                   "ઊંચી ઊર્જા ઘનતા કેવિટેશન ઉત્પન્ન કરે, જે સફાઈ અને વેલ્ડિંગમાં વપરાય."),
                  ("They cause heating, which is used in physiotherapy and in surgery.",
                   "તેઓ ઉષ્મા ઉત્પન્ન કરે, જે ફિઝિયોથેરાપી અને શસ્ત્રક્રિયામાં વપરાય.")),
               H4("Production", "ઉત્પાદન"),
               TB([T("Method", "રીત"), T("How it works", "કેવી રીતે કામ કરે"), T("Typical use", "સામાન્ય ઉપયોગ")],
                  [[T("piezoelectric", "પીઝોઇલેક્ટ્રિક"), T("a quartz plate vibrates when an AC field is applied", "AC ક્ષેત્ર આપતાં ક્વાર્ટ્ઝ પ્લેટ દોલિત થાય"), T("medical probes, SONAR", "મેડિકલ પ્રોબ, સોનાર")],
                   [T("magnetostriction", "મેગ્નેટોસ્ટ્રિક્શન"), T("a nickel rod changes length in a changing magnetic field", "બદલાતા ચુંબકીય ક્ષેત્રમાં નિકલ સળિયાની લંબાઈ બદલાય"), T("industrial cleaners, welding", "ઔદ્યોગિક ક્લીનર, વેલ્ડિંગ")]]),
               H4("Applications", "ઉપયોગો"),
               TB([T("Field", "ક્ષેત્ર"), T("Use", "ઉપયોગ")],
                  [[T("medical", "તબીબી"), T("sonography, echocardiography, lithotripsy", "સોનોગ્રાફી, ઇકોકાર્ડિયોગ્રાફી, લિથોટ્રિપ્સી")],
                   [T("engineering", "ઇજનેરી"), T("flaw detection, thickness gauging, ultrasonic welding", "ખામી શોધ, જાડાઈ માપન, અલ્ટ્રાસોનિક વેલ્ડિંગ")],
                   [T("navigation", "નૌકાવિહાર"), T("SONAR depth sounding and fish finding", "સોનાર ઊંડાઈ માપન અને માછલી શોધ")],
                   [T("industry", "ઉદ્યોગ"), T("cleaning of delicate parts, drilling of hard materials", "નાજુક પાર્ટની સફાઈ, કઠણ પદાર્થમાં કંદરો")],
                   [T("domestic", "ઘરેલું"), T("humidifiers, pest repellents, distance sensors", "હ્યુમિડિફાયર, જીવાત નિવારક, અંતર સેન્સર")]]),
               H4("Common mistake", "સામાન્ય ભૂલ"),
               P("Thinking ultrasound is electromagnetic. It is a mechanical sound wave, so it needs a "
                 "medium and cannot cross a vacuum.",
                 "અલ્ટ્રાસાઉન્ડને વિદ્યુતચુંબકીય માનવું. તે યાંત્રિક ધ્વનિ તરંગ છે, તેથી માધ્યમ જોઈએ અને "
                 "શૂન્યાવકાશ પાર કરી શકે નહીં.")],
              "u5_ultrasonic", syllabus_item="5.6"),
     ]},

    {"title": T("4. Conductors, Semiconductors and Insulators", "4. વાહક, અર્ધવાહક અને અવાહક"),
     "items": [
         card(T("4.1 Energy bands and the band gap",
                "4.1 ઊર્જા પટ્ટા અને પટ્ટા અંતર"),
              [H4("The idea", "ખ્યાલ"),
               P("In a solid the allowed electron energies form bands. The highest filled band is the "
                 "<b>valence band</b> and the next is the <b>conduction band</b>; the energy gap between "
                 "them is the <b>band gap</b> E<sub>g</sub>.",
                 "ઘનમાં ઇલેક્ટ્રોનની મંજૂર ઊર્જા પટ્ટા બનાવે. સૌથી ઊંચો ભરેલો પટ્ટો <b>સંયોજક પટ્ટો</b> અને "
                 "તેના પછીનો <b>વહન પટ્ટો</b> છે; તેમની વચ્ચેનું ઊર્જા અંતર <b>પટ્ટા અંતર</b> E<sub>g</sub> છે."),
               TB([T("Class", "વર્ગ"), T("Band gap", "પટ્ટા અંતર"), T("Conductivity at 300 K", "300 K પર વાહકતા"), T("Example", "ઉદાહરણ")],
                  [[T("conductor", "વાહક"), T("no gap, bands overlap", "અંતર નહીં, પટ્ટા એકબીજામાં"), T("very high, about 10⁷ S/m", "બહુ ઊંચી, લગભગ 10⁷ S/m"), T("copper, silver", "તાંબું, ચાંદી")],
                   [T("semiconductor", "અર્ધવાહક"), T("about 0.1 to 3 eV", "લગભગ 0.1 થી 3 eV"), T("moderate, 10⁻⁴ to 10² S/m", "મધ્યમ, 10⁻⁴ થી 10² S/m"), T("silicon 1.1 eV, germanium 0.7 eV", "સિલિકોન 1.1 eV, જર્મેનિયમ 0.7 eV")],
                   [T("insulator", "અવાહક"), T("more than about 3 eV", "લગભગ 3 eV થી વધુ"), T("almost zero", "લગભગ શૂન્ય"), T("glass 8 eV, diamond 5.5 eV", "કાચ 8 eV, હીરો 5.5 eV")]]),
               H4("Why temperature matters", "તાપમાન કેમ મહત્ત્વનું"),
               P("A semiconductor has a negative temperature coefficient: heating gives electrons enough "
                 "energy to cross the gap, so conductivity rises. A metal behaves the opposite way.",
                 "અર્ધવાહકનો તાપમાન ગુણાંક ઋણ છે: ગરમી ઇલેક્ટ્રોનને અંતર પાર કરવા પૂરતી ઊર્જા આપે, તેથી "
                 "વાહકતા વધે. ધાતુ ઊલટું વર્તે."),
               H4("Worked example", "ઉકેલાયેલ દાખલો"),
               P("The photon energy for a gap of 1.1 eV is E = hc/λ, so λ = 1240/1.1 = 1130 nm — beyond "
                 "the visible range, which is why silicon is used for infrared detectors.",
                 "1.1 eV અંતર માટે ફોટોન ઊર્જા E = hc/λ, તેથી λ = 1240/1.1 = 1130 nm — દૃશ્ય શ્રેણીની બહાર, "
                 "તેથી જ સિલિકોન ઇન્ફ્રારેડ ડિટેક્ટરમાં વપરાય."),
               H4("Common mistake", "સામાન્ય ભૂલ"),
               P("Reading the band gap as a barrier electrons cannot cross. At room temperature a small "
                 "fraction always crosses it, and doping makes it far easier.",
                 "પટ્ટા અંતરને એવો અવરોધ ગણવો જે ઇલેક્ટ્રોન પાર કરી જ ન શકે. ઓરડાના તાપમાને થોડો ભાગ હંમેશા "
                 "પાર કરે, અને ડોપિંગ તેને ઘણું સહેલું કરે.")],
              "u5_band", syllabus_item="5.7"),
         card(T("4.2 Intrinsic and extrinsic semiconductors, P and N type",
                "4.2 આંતરિક અને બાહ્ય અર્ધવાહક, P અને N પ્રકાર"),
              [H4("Intrinsic", "આંતરિક"),
               P("A pure crystal such as silicon has equal numbers of free electrons and holes, so "
                 "n = p = n<sub>i</sub>, and conduction is by both carriers. Its conductivity is low and "
                 "rises quickly with temperature.",
                 "સિલિકોન જેવા શુદ્ધ સ્ફટિકમાં મુક્ત ઇલેક્ટ્રોન અને છિદ્ર સમાન સંખ્યામાં હોય, તેથી "
                 "n = p = n<sub>i</sub>, અને વહન બંને વાહકો દ્વારા થાય. તેની વાહકતા ઓછી હોય અને તાપમાન સાથે "
                 "ઝડપથી વધે."),
               H4("Extrinsic: doping", "બાહ્ય: ડોપિંગ"),
               TB([T("Type", "પ્રકાર"), T("Dopant added", "ઉમેરાતી અશુદ્ધિ"), T("Majority carrier", "બહુમતી વાહક"), T("Donor or acceptor level", "દાતા કે ગ્રાહક સ્તર")],
                  [[T("N type", "N પ્રકાર"), T("pentavalent: P, As, Sb", "પંચસંયોજક: P, As, Sb"), T("electrons (n > p)", "ઇલેક્ટ્રોન (n > p)"), T("donor level just below the conduction band", "વહન પટ્ટાના થોડું નીચે દાતા સ્તર")],
                   [T("P type", "P પ્રકાર"), T("trivalent: B, Al, Ga", "ત્રિસંયોજક: B, Al, Ga"), T("holes (p > n)", "છિદ્ર (p > n)"), T("acceptor level just above the valence band", "સંયોજક પટ્ટાના થોડું ઉપર ગ્રાહક સ્તર")]]),
               H4("Why the name misleads", "નામ કેમ ભ્રામક છે"),
               P("Both types are electrically neutral: the dopant atom brings its own extra electron or "
                 "its missing bond, and the crystal as a whole stays uncharged. 'N' and 'P' describe the "
                 "majority carrier, not a net charge.",
                 "બંને પ્રકાર વિદ્યુતદૃષ્ટિએ તટસ્થ છે: અશુદ્ધિનો અણુ પોતાનો વધારાનો ઇલેક્ટ્રોન કે ખૂટતો બંધ "
                 "સાથે આવે, અને આખો સ્ફટિક વીજભારરહિત રહે. 'N' અને 'P' બહુમતી વાહક દર્શાવે, ચોખ્ખો વીજભાર નહીં."),
               H4("The p-n junction in one line", "એક લીટીમાં p-n સંધિ"),
               P("Join P and N silicon and electrons diffuse across, leaving a depletion layer with a "
                 "built-in field; that barrier is what makes a diode conduct one way only.",
                 "P અને N સિલિકોન જોડો તો ઇલેક્ટ્રોન ફેલાઈને જાય અને વિહીન સ્તર તથા આંતરિક ક્ષેત્ર રહી જાય; "
                 "એ અવરોધ જ ડાયોડને એક દિશામાં જ વહેવા દે."),
               H4("Common mistake", "સામાન્ય ભૂલ"),
               P("Saying an N-type crystal is negatively charged because it has electrons. The extra "
                 "electrons are balanced by the positive donor ions in the lattice.",
                 "N પ્રકારના સ્ફટિકને ઇલેક્ટ્રોન હોવાથી ઋણ ભારિત કહેવું. વધારાના ઇલેક્ટ્રોન સ્ફટિકમાં રહેલા "
                 "ધન દાતા આયનોથી સંતુલિત હોય છે.")],
              "u5_doping", syllabus_item="5.8"),
     ]},

    {"title": T("5. Practice Questions with Model Answers", "5. સરાવ પ્રશ્નો અને આદર્શ જવાબો"),
     "items": []},
]

NUMERICALS = [
    num("u5n01", T("Wave velocity from frequency and wavelength.",
                   "આવૃત્તિ અને તરંગલંબાઈ પરથી તરંગ વેગ."),
        T("A wave of frequency 500 Hz has a wavelength of 0.68 m. Find its velocity.",
          "500 Hz આવૃત્તિવાળા તરંગની તરંગલંબાઈ 0.68 m છે. તેનો વેગ શોધો."),
        [P("v = f λ", "v = f λ"),
         P("= 500 × 0.68", "= 500 × 0.68"),
         P("= 340 m/s", "= 340 m/s")],
        T("340 m/s", "340 m/s"), unit_no=5),
    num("u5n02", T("Wavelength of a 256 Hz tuning fork in air.",
                   "હવામાં 256 Hz ના સ્વરકાંટાની તરંગલંબાઈ."),
        T("Find the wavelength and time period of a 256 Hz sound in air at 343 m/s.",
          "343 m/s પર હવામાં 256 Hz ધ્વનિની તરંગલંબાઈ અને આવર્તકાળ શોધો."),
        [P("λ = v/f = 343/256", "λ = v/f = 343/256"),
         P("= 1.34 m", "= 1.34 m"),
         P("T = 1/f = 1/256 = 3.9 × 10⁻³ s", "T = 1/f = 1/256 = 3.9 × 10⁻³ s")],
        T("1.34 m and 3.9 ms", "1.34 m અને 3.9 ms"), unit_no=5),
    num("u5n03", T("Frequency of a 0.25 m wave in water.",
                   "પાણીમાં 0.25 m તરંગની આવૃત્તિ."),
        T("A wave of wavelength 0.25 m travels in water at 1500 m/s. Find its frequency.",
          "0.25 m તરંગલંબાઈનું તરંગ પાણીમાં 1500 m/s પર ચાલે છે. તેની આવૃત્તિ શોધો."),
        [P("f = v/λ", "f = v/λ"),
         P("= 1500/0.25", "= 1500/0.25"),
         P("= 6000 Hz = 6 kHz", "= 6000 Hz = 6 kHz")],
        T("6 kHz", "6 kHz"), unit_no=5),
    num("u5n04", T("Time period of a 50 Hz supply.",
                   "50 Hz પુરવઠાનો આવર્તકાળ."),
        T("Find the time period of a 50 Hz alternating supply and the number of cycles in 0.1 s.",
          "50 Hz પ્રત્યાવર્તી પુરવઠાનો આવર્તકાળ અને 0.1 s માં ચક્રોની સંખ્યા શોધો."),
        [P("T = 1/f = 1/50 = 0.02 s", "T = 1/f = 1/50 = 0.02 s"),
         P("Cycles in 0.1 s = 0.1/0.02", "0.1 s માં ચક્ર = 0.1/0.02"),
         P("= 5 cycles", "= 5 ચક્ર")],
        T("0.02 s and 5 cycles", "0.02 s અને 5 ચક્ર"), unit_no=5),
    num("u5n05", T("Distance to a wall from an echo delay.",
                   "પડઘાના વિલંબ પરથી દીવાલનું અંતર."),
        T("A clap is heard again after 0.6 s from a distant wall. Find the distance (v = 340 m/s).",
          "દૂરની દીવાલથી તાળી 0.6 s પછી ફરી સંભળાય છે. અંતર શોધો (v = 340 m/s)."),
        [P("The sound travels there and back, so 2d = v t", "ધ્વનિ જાય અને પાછો આવે, તેથી 2d = v t"),
         P("d = v t/2 = 340 × 0.6/2", "d = v t/2 = 340 × 0.6/2"),
         P("= 102 m", "= 102 m")],
        T("102 m", "102 m"), unit_no=5),
    num("u5n06", T("Minimum distance for a distinct echo.",
                   "અલગ પડઘા માટે લઘુતમ અંતર."),
        T("The ear can separate an echo after 0.1 s. Find the minimum distance of the reflector.",
          "કાન 0.1 s પછીનો પડઘો અલગ પકડી શકે છે. પરાવર્તકનું લઘુતમ અંતર શોધો."),
        [P("d = v t/2", "d = v t/2"),
         P("= 340 × 0.1/2", "= 340 × 0.1/2"),
         P("= 17 m", "= 17 m")],
        T("17 m", "17 m"), unit_no=5),
    num("u5n07", T("Reverberation time of a hall by Sabine's formula.",
                   "સેબાઇનના સૂત્રથી હોલનો પ્રતિધ્વનિ સમય."),
        T("A hall of volume 2400 m³ has a total absorption of 240 m² sabine. Find its reverberation "
          "time.", "2400 m³ ઘનફળવાળા હોલમાં કુલ શોષણ 240 m² સેબાઇન છે. તેનો પ્રતિધ્વનિ સમય શોધો."),
        [P("T = 0.161 V/A", "T = 0.161 V/A"),
         P("= 0.161 × 2400/240", "= 0.161 × 2400/240"),
         P("= 1.61 s", "= 1.61 s")],
        T("1.61 s", "1.61 s"), unit_no=5),
    num("u5n08", T("Absorption needed for a reverberation time of 1 s.",
                   "1 s પ્રતિધ્વનિ સમય માટે જરૂરી શોષણ."),
        T("What total absorption brings the same 2400 m³ hall to 1.0 s?",
          "એ જ 2400 m³ હોલને 1.0 s પર લાવવા કેટલું કુલ શોષણ જોઈએ?"),
        [P("A = 0.161 V/T", "A = 0.161 V/T"),
         P("= 0.161 × 2400/1.0", "= 0.161 × 2400/1.0"),
         P("= 386 m² sabine, so 146 m² must be added", "= 386 m² સેબાઇન, તેથી 146 m² ઉમેરવું પડે")],
        T("386 m² sabine", "386 m² સેબાઇન"), unit_no=5),
    num("u5n09", T("Average absorption coefficient of a room.",
                   "ઓરડાનો સરેરાશ શોષણ ગુણાંક."),
        T("A room of total surface 500 m² has a total absorption of 75 m² sabine. Find the average "
          "absorption coefficient and the reverberation time if V = 1500 m³.",
          "500 m² કુલ સપાટીવાળા ઓરડામાં કુલ શોષણ 75 m² સેબાઇન છે. સરેરાશ શોષણ ગુણાંક અને, V = 1500 m³ "
          "હોય તો, પ્રતિધ્વનિ સમય શોષો."),
        [P("α = A/S = 75/500 = 0.15", "α = A/S = 75/500 = 0.15"),
         P("T = 0.161 × 1500/75", "T = 0.161 × 1500/75"),
         P("= 3.22 s", "= 3.22 s")],
        T("α = 0.15 and T = 3.22 s", "α = 0.15 અને T = 3.22 s"), unit_no=5),
    num("u5n10", T("Distance between nodes of a stationary wave.",
                   "સ્થિર તરંગના નિસ્પંદ વચ્ચેનું અંતર."),
        T("A stationary wave is formed from waves of wavelength 0.5 m. Find the distance between two "
          "consecutive nodes and between a node and the next antinode.",
          "0.5 m તરંગલંબાઈવાળા તરંગોથી સ્થિર તરંગ બને છે. બે ક્રમિક નિસ્પંદ વચ્ચેનું અને નિસ્પંદ તથા "
          "પ્રસ્પંદ વચ્ચેનું અંતર શોધો."),
        [P("Node to node = λ/2 = 0.25 m", "નિસ્પંદ થી નિસ્પંદ = λ/2 = 0.25 m"),
         P("Node to antinode = λ/4", "નિસ્પંદ થી પ્રસ્પંદ = λ/4"),
         P("= 0.125 m", "= 0.125 m")],
        T("0.25 m and 0.125 m", "0.25 m અને 0.125 m"), unit_no=5),
    num("u5n11", T("Fundamental frequency of a stretched string.",
                   "ખેંચાયેલી દોરીની પાયાની આવૃત્તિ."),
        T("A string 0.75 m long fixed at both ends carries a wave at 300 m/s. Find its fundamental "
          "frequency.", "બંને છેડેથી બંધ 0.75 m લાંબી દોરીમાં તરંગનો વેગ 300 m/s છે. તેની પાયાની આવૃત્તિ શોધો."),
        [P("For the fundamental, λ = 2L = 1.5 m", "પાયાની રીત માટે λ = 2L = 1.5 m"),
         P("f = v/λ = 300/1.5", "f = v/λ = 300/1.5"),
         P("= 200 Hz", "= 200 Hz")],
        T("200 Hz", "200 Hz"), unit_no=5),
    num("u5n12", T("Wavelength of 40 kHz ultrasound in air and in water.",
                   "હવામાં અને પાણીમાં 40 kHz અલ્ટ્રાસાઉન્ડની તરંગલંબાઈ."),
        T("Find the wavelength of 40 kHz ultrasound in air (343 m/s) and in water (1480 m/s).",
          "હવામાં (343 m/s) અને પાણીમાં (1480 m/s) 40 kHz અલ્ટ્રાસાઉન્ડની તરંગલંબાઈ શોધો."),
        [P("Air: λ = 343/40 000 = 8.6 × 10⁻³ m", "હવા: λ = 343/40 000 = 8.6 × 10⁻³ m"),
         P("Water: λ = 1480/40 000", "પાણી: λ = 1480/40 000"),
         P("= 3.7 × 10⁻² m = 3.7 cm", "= 3.7 × 10⁻² m = 3.7 cm")],
        T("8.6 mm in air, 3.7 cm in water", "હવામાં 8.6 mm, પાણીમાં 3.7 cm"), unit_no=5),
    num("u5n13", T("Depth of the sea by SONAR.",
                   "સોનારથી દરિયાની ઊંડાઈ."),
        T("A SONAR pulse returns after 0.8 s in water where sound travels at 1500 m/s. Find the depth.",
          "પાણીમાં ધ્વનિ 1500 m/s પર ચાલે ત્યાં સોનારનો સ્પંદ 0.8 s પછી પાછો આવે છે. ઊંડાઈ શોધો."),
        [P("2d = v t", "2d = v t"),
         P("d = 1500 × 0.8/2", "d = 1500 × 0.8/2"),
         P("= 600 m", "= 600 m")],
        T("600 m", "600 m"), unit_no=5),
    num("u5n14", T("Wavelength of 1 MHz ultrasound in steel.",
                   "સ્ટીલમાં 1 MHz અલ્ટ્રાસાઉન્ડની તરંગલંબાઈ."),
        T("Steel carries sound at about 5000 m/s. Find the wavelength of 1 MHz ultrasound in it, and say "
          "why short wavelengths help flaw detection.",
          "સ્ટીલમાં ધ્વનિ લગભગ 5000 m/s પર ચાલે. તેમાં 1 MHz અલ્ટ્રાસાઉન્ડની તરંગલંબાઈ શોધો અને ટૂંકી "
          "તરંગલંબાઈ ખામી શોધમાં કેમ મદદ કરે તે કહો."),
        [P("λ = v/f = 5000/10⁶", "λ = v/f = 5000/10⁶"),
         P("= 5 × 10⁻³ m = 5 mm", "= 5 × 10⁻³ m = 5 mm"),
         P("A flaw smaller than λ scatters weakly, so a 5 mm wave finds 2 to 3 mm defects",
           "λ થી નાની ખામી નબળી પ્રકીર્ણ કરે, તેથી 5 mm તરંગ 2 થી 3 mm ખામી શોધે")],
        T("5 mm", "5 mm"), unit_no=5),
    num("u5n15", T("Band gap energy from a wavelength.",
                   "તરંગલંબાઈ પરથી પટ્ટા અંતરની ઊર્જા."),
        T("Light of wavelength 1.1 µm is just absorbed by silicon. Find the band gap in eV.",
          "1.1 µm તરંગલંબાઈનો પ્રકાશ સિલિકોનમાં લગભગ શોષાય છે. પટ્ટા અંતર eV માં શોધો."),
        [P("E = hc/λ = 1240/λ(nm)", "E = hc/λ = 1240/λ(nm)"),
         P("= 1240/1100", "= 1240/1100"),
         P("= 1.13 eV", "= 1.13 eV")],
        T("1.13 eV", "1.13 eV"), unit_no=5),
    num("u5n16", T("Wavelength corresponding to a 0.7 eV gap.",
                   "0.7 eV અંતરને અનુરૂપ તરંગલંબાઈ."),
        T("Germanium has a band gap of 0.7 eV. Find the longest wavelength that can free an electron.",
          "જર્મેનિયમનું પટ્ટા અંતર 0.7 eV છે. ઇલેક્ટ્રોન મુક્ત કરી શકે તેવી સૌથી લાંબી તરંગલંબાઈ શોધો."),
        [P("λ = 1240/E(eV) nm", "λ = 1240/E(eV) nm"),
         P("= 1240/0.7", "= 1240/0.7"),
         P("= 1771 nm ≈ 1.77 µm (infrared)", "= 1771 nm ≈ 1.77 µm (ઇન્ફ્રારેડ)")],
        T("1.77 µm", "1.77 µm"), unit_no=5),
    num("u5n17", T("Density of donor atoms at 1 ppm doping.",
                   "1 ppm ડોપિંગ પર દાતા અણુઓની ઘનતા."),
        T("Silicon has 5 × 10²⁸ atoms per m³. If it is doped with 1 part per million of phosphorus, "
          "find the donor density.", "સિલિકોનમાં 5 × 10²⁸ અણુ પ્રતિ m³ હોય છે. તેમાં ફોસ્ફરસનો 1 ભાગ "
          "પ્રતિ મિલિયન ઉમેરાય તો દાતા ઘનતા શોધો."),
        [P("n = 5 × 10²⁸ × 10⁻⁶", "n = 5 × 10²⁸ × 10⁻⁶"),
         P("= 5 × 10²² donors per m³", "= 5 × 10²² દાતા પ્રતિ m³"),
         P("That is about eight orders above the intrinsic carrier density at 300 K",
           "આ 300 K પર આંતરિક વાહક ઘનતાથી લગભગ આઠ ક્રમ ઉપર છે")],
        T("5 × 10²² m⁻³", "5 × 10²² m⁻³"), unit_no=5),
    num("u5n18", T("Number of holes when n and p are compared.",
                   "n અને p સરખાવતાં છિદ્રોની સંખ્યા."),
        T("In an N-type sample n = 10²² m⁻³. If n p = 2.25 × 10³² m⁻⁶ at 300 K, find p.",
          "N પ્રકારના નમૂનામાં n = 10²² m⁻³ છે. 300 K પર n p = 2.25 × 10³² m⁻⁶ હોય તો p શોધો."),
        [P("p = nᵢ²/n with nᵢ² = 2.25 × 10³²", "p = nᵢ²/n, જ્યાં nᵢ² = 2.25 × 10³²"),
         P("p = 2.25 × 10³²/10²²", "p = 2.25 × 10³²/10²²"),
         P("= 2.25 × 10¹⁰ m⁻³, eleven orders smaller", "= 2.25 × 10¹⁰ m⁻³, અગિયાર ક્રમ નાનું")],
        T("2.25 × 10¹⁰ m⁻³", "2.25 × 10¹⁰ m⁻³"), unit_no=5),
    num("u5n19", T("Frequency of a stationary wave in a 0.5 m pipe closed at both ends.",
                   "બંને છેડેથી બંધ 0.5 m નળીમાં સ્થિર તરંગની આવૃત્તિ."),
        T("A pipe 0.5 m long closed at both ends has air at 340 m/s. Find the lowest resonant "
          "frequency.", "બંને છેડેથી બંધ 0.5 m નળીમાં હવાનો વેગ 340 m/s છે. સૌથી નીચી અનુનાદ આવૃત્તિ શોધો."),
        [P("Both ends are nodes, so λ/2 = L", "બંને છેડા નિસ્પંદ છે, તેથી λ/2 = L"),
         P("λ = 1.0 m", "λ = 1.0 m"),
         P("f = 340/1.0 = 340 Hz", "f = 340/1.0 = 340 Hz")],
        T("340 Hz", "340 Hz"), unit_no=5),
    num("u5n20", T("Energy of a photon of 500 nm light.",
                   "500 nm પ્રકાશના ફોટોનની ઊર્જા."),
        T("Find the energy in eV of a photon of wavelength 500 nm, and compare it with a 1.1 eV gap.",
          "500 nm તરંગલંબાઈના ફોટોનની ઊર્જા eV માં શોધો અને 1.1 eV અંતર સાથે સરખાવો."),
        [P("E = 1240/500", "E = 1240/500"),
         P("= 2.48 eV", "= 2.48 eV"),
         P("2.48 eV > 1.1 eV, so visible light can free electrons in silicon",
           "2.48 eV > 1.1 eV, તેથી દૃશ્ય પ્રકાશ સિલિકોનમાં ઇલેક્ટ્રોન મુક્ત કરી શકે")],
        T("2.48 eV", "2.48 eV"), unit_no=5),
]

EQUATIONS = [
    {"title": T("Wave motion", "તરંગ ગતિ"),
     "items": [
         {"name": T("Wave velocity", "તરંગ વેગ"), "f": "v = f λ",
          "terms": T("The medium fixes v and the source fixes f, so λ adjusts.",
                     "માધ્યમ v નક્કી કરે અને સ્રોત f, તેથી λ ગોઠવાય.")},
         {"name": T("Time period", "આવર્તકાળ"), "f": "T = 1/f",
          "terms": T("One full oscillation, in seconds.", "એક પૂરું દોલન, સેકન્ડમાં.")},
         {"name": T("Node spacing", "નિસ્પંદ અંતર"), "f": "node to node = λ/2, node to antinode = λ/4",
          "terms": T("Both apply to every stationary wave.", "બંને દરેક સ્થિર તરંગને લાગુ પડે.")},
         {"name": T("Echo distance", "પડઘાનું અંતર"), "f": "d = v t / 2",
          "terms": T("Half the path, because the sound goes and returns.",
                     "અડધો રસ્તો, કારણ કે ધ્વનિ જાય અને પાછો આવે.")},
     ]},
    {"title": T("Acoustics", "ધ્વનિશાસ્ત્ર"),
     "items": [
         {"name": T("Sabine's formula", "સેબાઇનનું સૂત્ર"), "f": "T = 0.161 V / A",
          "terms": T("V in m³ and A = Σ α S in m² sabine.", "V m³ માં અને A = Σ α S m² સેબાઇનમાં.")},
         {"name": T("Total absorption", "કુલ શોષણ"), "f": "A = Σ α S",
          "terms": T("Sum of coefficient times area for every surface.",
                     "દરેક સપાટી માટે ગુણાંક ગુણ્યા ક્ષેત્રફળનો સરવાળો.")},
         {"name": T("Absorption needed for a target time", "લક્ષ્ય સમય માટે જરૂરી શોષણ"),
          "f": "A = 0.161 V / T",
          "terms": T("Rearranged Sabine formula, used to size the absorbers.",
                     "સેબાઇનનું ગોઠવેલું સૂત્ર, શોષકનું માપ નક્કી કરવા વપરાય.")},
         {"name": T("Absorption coefficient", "શોષણ ગુણાંક"), "f": "α = absorbed energy / incident energy",
          "terms": T("0 for a perfect reflector, 1 for an open window.",
                     "પૂર્ણ પરાવર્તક માટે 0, ખુલ્લી બારી માટે 1.")},
     ]},
    {"title": T("Ultrasonics and semiconductors", "અલ્ટ્રાસોનિક્સ અને અર્ધવાહક"),
     "items": [
         {"name": T("Ultrasonic range", "અલ્ટ્રાસોનિક શ્રેણી"), "f": "f > 20 kHz",
          "terms": T("Above human hearing; infrasonic is below 20 Hz.",
                     "માનવ શ્રવણથી ઉપર; ઇન્ફ્રાસોનિક 20 Hz થી નીચે.")},
         {"name": T("SONAR depth", "સોનાર ઊંડાઈ"), "f": "d = v t / 2",
          "terms": T("Same echo geometry, with v = 1500 m/s in water.",
                     "એ જ પડઘાની ભૂમિતિ, પાણીમાં v = 1500 m/s સાથે.")},
         {"name": T("Photon energy and band gap", "ફોટોન ઊર્જા અને પટ્ટા અંતર"),
          "f": "E (eV) = 1240 / λ (nm)",
          "terms": T("Light frees an electron only if E is at least E_g.",
                     "પ્રકાશ ઇલેક્ટ્રોન મુક્ત કરે ફક્ત જો E ઓછામાં ઓછું E_g હોય.")},
         {"name": T("Mass action law", "દ્રવ્ય-ક્રિયા નિયમ"), "f": "n p = nᵢ²",
          "terms": T("Holds for intrinsic and doped silicon alike.",
                     "આંતરિક અને ડોપ કરેલા સિલિકોન બંને માટે લાગુ.")},
     ]},
]

VIVA = [
    {"title": T("Waves", "તરંગો"),
     "items": [
         {"q": T("Define a wave and say what travels in it.",
                 "તરંગની વ્યાખ્યા આપો અને તેમાં શું ચાલે તે કહો."),
          "a": T("A wave is a disturbance that carries energy and momentum from one point to another "
                 "without transporting matter; the particles of the medium only oscillate about their "
                 "mean positions.",
                 "તરંગ એ વિક્ષોભ છે જે પદાર્થ લઈ જ્યા વગર ઊર્જા અને વેગમાન એક બિંદુથી બીજા બિંદુ સુધી "
                 "પહોંચાડે; માધ્યમના કણો ફક્ત પોતાના સ્થાનની આસપાસ દોલિત થાય.")},
         {"q": T("Distinguish longitudinal from transverse waves with one example each.",
                 "સંગત અને અનુપ્રસ્થ તરંગમાં દરેકનું એક ઉદાહરણ આપીને ભેદ બતાવો."),
          "a": T("In a longitudinal wave the particles move along the direction of travel, as in sound "
                 "in air; in a transverse wave they move perpendicular to it, as on a stretched string "
                 "or in light.",
                 "સંગત તરંગમાં કણો ગતિની દિશામાં જ ખસે, જેમ હવામાં ધ્વનિ; અનુપ્રસ્થ તરંગમાં તેઓ તેની "
                 "લંબરૂપે ખસે, જેમ તંગ દોરી પર કે પ્રકાશમાં.")},
         {"q": T("What happens to frequency and wavelength when sound enters water?",
                 "ધ્વનિ પાણીમાં પ્રવેશે ત્યારે આવૃત્તિ અને તરંગલંબાઈનું શું થાય?"),
          "a": T("Frequency stays the same because the source fixes it; speed rises from about 343 to "
                 "1480 m/s, so the wavelength rises in the same proportion to keep v = f λ.",
                 "આવૃત્તિ એ જ રહે કારણ કે સ્રોત તે નક્કી કરે; વેગ 343 થી 1480 m/s સુધી વધે, તેથી v = f λ "
                 "જાળવવા તરંગલંબાઈ એ જ પ્રમાણમાં વધે.")},
         {"q": T("Write the relation between wave velocity, frequency and wavelength.",
                 "તરંગ વેગ, આવૃત્તિ અને તરંગલંબાઈ વચ્ચેનો સંબંધ લખો."),
          "a": T("v = f λ; a 256 Hz fork in air has λ = 343/256 = 1.34 m.",
                 "v = f λ; હવામાં 256 Hz ના સ્વરકાંટા માટે λ = 343/256 = 1.34 m.")},
     ]},
    {"title": T("Interference and acoustics", "વ્યતીકરણ અને ધ્વનિશાસ્ત્ર"),
     "items": [
         {"q": T("State the principle of superposition.", "અધ્યારોપણનો સિદ્ધાંત જણાવો."),
          "a": T("When two or more waves arrive at a point, the resultant displacement is the vector "
                 "sum of their individual displacements.",
                 "બે કે વધુ તરંગો એક બિંદુએ પહોંચે ત્યારે પરિણામી સ્થાનાંતરણ તેમના અલગ સ્થાનાંતરણનો સદિશ "
                 "સરવાળો હોય.")},
         {"q": T("Give the conditions for a steady interference pattern.",
                 "સ્થિર વ્યતીકરણ આકૃતિની શરતો જણાવો."),
          "a": T("The sources must be coherent with the same frequency and a constant phase difference, "
                 "of comparable amplitude, and close together compared with their distance from the "
                 "screen.",
                 "સ્રોત સહસંબંધી હોવા જોઈએ, સમાન આવૃત્તિ અને અચળ કળા તફાવત સાથે, લગભગ સમાન કંપવિસ્તારવાળા, "
                 "અને પડદાથી તેમના અંતરની સરખામણીમાં નજીક હોવા જોઈએ.")},
         {"q": T("What are nodes and antinodes?", "નિસ્પંદ અને પ્રસ્પંદ શું છે?"),
          "a": T("Points of zero amplitude in a stationary wave are nodes and points of maximum "
                 "amplitude are antinodes; they are λ/4 apart, with λ/2 between successive nodes.",
                 "સ્થિર તરંગમાં શૂન્ય કંપવિસ્તારવાળાં બિંદુ નિસ્પંદ અને મહત્તમ કંપવિસ્તારવાળાં પ્રસ્પંદ છે; "
                 "તેઓ λ/4 દૂર હોય, અને ક્રમિક નિસ્પંદ વચ્ચે λ/2.")},
         {"q": T("Define reverberation time and give a good value for a lecture hall.",
                 "પ્રતિધ્વનિ સમયની વ્યાખ્યા આપો અને વ્યાખ્યાન હોલ માટે યોગ્ય મૂલ્ય આપો."),
          "a": T("It is the time for the sound level to fall by 60 dB after the source stops; about 1 s "
                 "suits speech, while 2 s suits music.",
                 "સ્રોત બંધ થયા પછી ધ્વનિનું સ્તર 60 dB ઘટવાનો સમય; બોલાયેલા શબ્દ માટે લગભગ 1 s અને "
                 "સંગીત માટે 2 s યોગ્ય.")},
         {"q": T("What is the absorption coefficient of an open window and why is it 1?",
                 "ખુલ્લી બારીનો શોષણ ગુણાંક શું છે અને તે 1 કેમ છે?"),
          "a": T("Unity, because the window lets all the incident sound energy pass out of the room "
                 "without reflection, so nothing comes back.",
                 "એક, કારણ કે બારી પર પડતી બધી ધ્વનિ ઊર્જા પરાવર્તન વગર ઓરડાની બહાર જવા દે, તેથી પાછું "
                 "કંઈ આવતું નથી.")},
         {"q": T("State Sabine's formula and name its symbols.",
                 "સેબાઇનનું સૂત્ર જણાવો અને સંજ્ઞાઓનાં નામ આપો."),
          "a": T("T = 0.161 V/A, with T the reverberation time in seconds, V the volume in m³ and A the "
                 "total absorption in m² sabine.",
                 "T = 0.161 V/A, જ્યાં T પ્રતિધ્વનિ સમય સેકન્ડમાં, V ઘનફળ m³ માં અને A કુલ શોષણ m² "
                 "સેબાઇનમાં.")},
     ]},
    {"title": T("Ultrasonics and semiconductors", "અલ્ટ્રાસોનિક્સ અને અર્ધવાહક"),
     "items": [
         {"q": T("What are ultrasonic waves and how are they produced?",
                 "અલ્ટ્રાસોનિક તરંગો શું છે અને તે કેવી રીતે ઉત્પન્ન થાય?"),
          "a": T("Sound above 20 kHz; they are produced by the piezoelectric effect in quartz or by "
                 "magnetostriction in nickel, driven by a high-frequency oscillator.",
                 "20 kHz થી ઉપરનો ધ્વનિ; તે ક્વાર્ટ્ઝમાં પીઝોઇલેક્ટ્રિક અસરથી કે નિકલમાં મેગ્નેટોસ્ટ્રિક્શનથી "
                 "ઉત્પન્ન થાય, જે ઉચ્ચ-આવૃત્તિના દોલકથી ચાલે.")},
         {"q": T("Give three applications of ultrasound in engineering.",
                 "ઇજનેરીમાં અલ્ટ્રાસાઉન્ડના ત્રણ ઉપયોગો આપો."),
          "a": T("Flaw detection in castings and welds, thickness gauging from one side only, and "
                 "ultrasonic welding or cleaning of delicate parts.",
                 "કાસ્ટિંગ અને વેલ્ડમાં ખામી શોધ, એક જ બાજુથી જાડાઈ માપન, અને નાજુક પાર્ટનું અલ્ટ્રાસોનિક "
                 "વેલ્ડિંગ કે સફાઈ.")},
         {"q": T("How does a SONAR measure depth?", "સોનાર ઊંડાઈ કેવી રીતે માપે?"),
          "a": T("It sends a pulse, times the echo, and halves the path: d = v t/2, with v about "
                 "1500 m/s in sea water.",
                 "તે સ્પંદ મોકલે, પડઘાનો સમય માપે અને રસ્તાનો અડધો ભાગ લે: d = v t/2, જ્યાં દરિયાના પાણીમાં "
                 "v લગભગ 1500 m/s.")},
         {"q": T("On what basis are solids classed as conductors, semiconductors and insulators?",
                 "ઘનને વાહક, અર્ધવાહક અને અવાહકમાં કયા આધારે વહેંચાય?"),
          "a": T("On the band gap: no gap for a conductor, roughly 0.1 to 3 eV for a semiconductor and "
                 "more than about 3 eV for an insulator.",
                 "પટ્ટા અંતર પર: વાહકમાં અંતર નહીં, અર્ધવાહકમાં લગભગ 0.1 થી 3 eV અને અવાહકમાં લગભગ 3 eV થી વધુ.")},
         {"q": T("What is doping and why is it done?", "ડોપિંગ શું છે અને તે કેમ કરાય?"),
          "a": T("Adding a controlled trace of a pentavalent or trivalent impurity to pure silicon so "
                 "that its conductivity rises by several orders of magnitude and can be set to a "
                 "design value.",
                 "શુદ્ધ સિલિકોનમાં પંચસંયોજક કે ત્રિસંયોજક અશુદ્ધિનો નિયંત્રિત થોડો ભાગ ઉમેરવો જેથી તેની "
                 "વાહકતા ઘણા ક્રમ વધે અને રચનાના મૂલ્ય પર ગોઠવી શકાય.")},
         {"q": T("In a P-type crystal, what is the majority carrier and is the crystal charged?",
                 "P પ્રકારના સ્ફટિકમાં બહુમતી વાહક કયો છે અને સ્ફટિક ભારિત છે?"),
          "a": T("Holes are the majority carrier, and the crystal is electrically neutral because the "
                 "acceptor ions balance the extra holes.",
                 "છિદ્ર બહુમતી વાહક છે, અને સ્ફટિક વિદ્યુતદૃષ્ટિએ તટસ્થ છે કારણ કે ગ્રાહક આયનો વધારાનાં "
                 "છિદ્રોને સંતુલિત કરે.")},
     ]},
]

_PRACTICE = [
    (T("Define a wave and distinguish longitudinal from transverse waves.",
       "તરંગની વ્યાખ્યા આપો અને સંગત તથા અનુપ્રસ્થ તરંગમાં ભેદ આપો."),
     3,
     [P("A wave is a disturbance that transfers energy and momentum without transferring matter; the "
        "medium's particles oscillate about fixed positions and only the pattern moves.",
        "તરંગ એ વિક્ષોભ છે જે પદાર્થનું સ્થાનાંતરણ કર્યા વગર ઊર્જા અને વેગમાન પહોંચાડે; માધ્યમના કણો નિશ્ચિત "
        "સ્થાનની આસપાસ દોલિત થાય અને ફક્ત આકૃતિ આગળ વધે."),
      P("In a longitudinal wave the particles vibrate along the direction of propagation, forming "
        "compressions and rarefactions, as sound does in air.",
        "સંગત તરંગમાં કણો પ્રસરણની દિશામાં જ દોલિત થાય, જેનાથી સંકોચન અને વિસ્તરણ બને, જેમ હવામાં ધ્વનિ."),
      P("In a transverse wave they vibrate perpendicular to it, forming crests and troughs, as on a "
        "string or in light; a transverse wave can be polarised, a longitudinal one cannot.",
        "અનુપ્રસ્થ તરંગમાં તેઓ તેની લંબરૂપે દોલિત થાય, જેનાથી શિખર અને ગર્ત બને, જેમ દોરી પર કે પ્રકાશમાં; "
        "અનુપ્રસ્થ તરંગનું ધ્રુવીકરણ થઈ શકે, સંગતનું નહીં.")]),
    (T("Write the relation v = f λ and explain what changes when sound enters water.",
       "v = f λ સંબંધ લખો અને ધ્વનિ પાણીમાં જાય ત્યારે શું બદલાય તે સમજાવો."),
     3,
     [P("For any wave, velocity equals frequency times wavelength: v = f λ, where f is in hertz and λ "
        "in metres.",
        "કોઈપણ તરંગ માટે વેગ એ આવૃત્તિ ગુણ્યા તરંગલંબાઈ છે: v = f λ, જ્યાં f હર્ટ્ઝમાં અને λ મીટરમાં."),
      P("The source fixes the frequency, so f does not change at a boundary; the medium fixes the "
        "speed, which rises from 343 m/s in air to about 1480 m/s in water.",
        "સ્રોત આવૃત્તિ નક્કી કરે, તેથી સીમા પર f બદલાતી નથી; માધ્યમ વેગ નક્કી કરે, જે હવામાં 343 m/s થી "
        "પાણીમાં લગભગ 1480 m/s થાય."),
      P("The wavelength must therefore rise in the same ratio, from 1.34 m to about 5.8 m for a 256 Hz "
        "note, which is why sound bends and spreads differently underwater.",
        "તેથી તરંગલંબાઈ એ જ પ્રમાણમાં વધવી પડે, 256 Hz સૂર માટે 1.34 m થી લગભગ 5.8 m, અને તેથી જ પાણીમાં "
        "ધ્વનિ જુદી રીતે વળે અને ફેલાય.")]),
    (T("State the principle of superposition and the conditions for steady interference.",
       "અધ્યારોપણનો સિદ્ધાંત અને સ્થિર વ્યતીકરણની શરતો જણાવો."),
     4,
     [P("The principle says the resultant displacement at a point is the vector sum of the "
        "displacements due to each wave arriving there.",
        "સિદ્ધાંત કહે છે કે કોઈ બિંદુએ પરિણામી સ્થાનાંતરણ ત્યાં પહોંચતા દરેક તરંગના સ્થાનાંતરણનો સદિશ સરવાળો છે."),
      P("For a steady pattern the two sources must be coherent — same frequency and a constant phase "
        "difference — of nearly equal amplitude, and close together compared with their distance from "
        "the screen.",
        "સ્થિર આકૃતિ માટે બે સ્રોત સહસંબંધી હોવા જોઈએ — સમાન આવૃત્તિ અને અચળ કળા તફાવત — લગભગ સમાન "
        "કંપવિસ્તારવાળા, અને પડદાથી તેમના અંતરની સરખામણીમાં નજીક."),
      P("When the waves travel in opposite directions with equal amplitude the sum is a stationary "
        "wave with fixed nodes λ/2 apart, which is how a string or an organ pipe resonates.",
        "તરંગો સમાન કંપવિસ્તાર સાથે વિરુદ્ધ દિશામાં ચાલે ત્યારે સરવાળો સ્થિર તરંગ બને, જેમાં નિસ્પંદ λ/2 "
        "અંતરે સ્થિર રહે, અને તેથી જ દોરી કે ઓર્ગન પાઇપ અનુનાદ કરે.")]),
    (T("Define reverberation time, echo and absorption coefficient.",
       "પ્રતિધ્વનિ સમય, પડઘો અને શોષણ ગુણાંકની વ્યાખ્યા આપો."),
     3,
     [P("Reverberation time is the time taken for the sound level in a hall to fall by 60 dB after the "
        "source stops; it is the single number that describes how 'live' a room is.",
        "પ્રતિધ્વનિ સમય એ સ્રોત બંધ થયા પછી હોલમાં ધ્વનિનું સ્તર 60 dB ઘટવા લાગતો સમય છે; ઓરડો કેટલો "
        "'જીવંત' છે તે દર્શાવતો એક જ આંકડો તે છે."),
      P("An echo is a reflected sound heard separately, which needs a delay of at least about 0.1 s, "
        "so the reflector must be roughly 17 m away.",
        "પડઘો એ અલગ સંભળાતો પરાવર્તિત ધ્વનિ છે, જેના માટે ઓછામાં ઓછો લગભગ 0.1 s વિલંબ જોઈએ, તેથી પરાવર્તક "
        "લગભગ 17 m દૂર હોવું જોઈએ."),
      P("The absorption coefficient α is the fraction of incident sound energy a surface absorbs: 0.02 "
        "for plaster, 0.5 for a heavy curtain and 1.00 for an open window.",
        "શોષણ ગુણાંક α એ સપાટી પર પડતી ધ્વનિ ઊર્જાનો શોષાતો ભાગ છે: પ્લાસ્ટર માટે 0.02, જાડા પડદા માટે "
        "0.5 અને ખુલ્લી બારી માટે 1.00.")]),
    (T("State Sabine's formula and solve one numerical with it.",
       "સેબાઇનનું સૂત્ર જણાવો અને તેનો એક દાખલો ઉકેલો."),
     4,
     [P("T = 0.161 V/A, where V is the volume in m³ and A = Σ α S is the total absorption in m² sabine.",
        "T = 0.161 V/A, જ્યાં V ઘનફળ m³ માં અને A = Σ α S કુલ શોષણ m² સેબાઇનમાં."),
      P("For a hall 20 × 15 × 8 m, V = 2400 m³; with A = 240 m² sabine the time is "
        "0.161 × 2400/240 = 1.61 s.",
        "20 × 15 × 8 m ના હોલ માટે V = 2400 m³; A = 240 m² સેબાઇન સાથે સમય 0.161 × 2400/240 = 1.61 s."),
      P("To reach 1.0 s the room needs A = 386 m², so 146 m² of extra absorption — about 290 m² of "
        "curtain, or 320 seats, which shows why a full hall sounds different from an empty one.",
        "1.0 s સુધી પહોંચવા ઓરડાને A = 386 m² જોઈએ, એટલે 146 m² વધુ શોષણ — લગભગ 290 m² પડદો, કે 320 "
        "બેઠક, જે દર્શાવે કે ભરેલો હોલ ખાલી કરતાં જુદો કેમ સંભળાય.")]),
    (T("How is reverberation controlled in a hall? Give four measures.",
       "હોલમાં પ્રતિધ્વનિ કેવી રીતે નિયંત્રિત થાય? ચાર ઉપાય આપો."),
     4,
     [P("The first step is to compute T from Sabine's formula and compare it with the target: about 1 s "
        "for speech and 2 s for music.",
        "પ્રથમ પગલું એ છે કે સેબાઇનના સૂત્રથી T ગણીને લક્ષ્ય સાથે સરખાવવું: બોલાયેલા શબ્દ માટે લગભગ 1 s "
        "અને સંગીત માટે 2 s."),
      P("If T is too long, absorbers are added: acoustic tiles on the ceiling, heavy curtains over "
        "glass, carpet on the floor and upholstered seating.",
        "T લાંબી હોય તો શોષક ઉમેરાય: ટોચમર્યાદા પર ધ્વનિ-શોષક ટાઇલ, કાચ પર જાડા પડદા, ફર્શ પર જાજમ અને "
        "ગાદીવાળી બેઠક."),
      P("If T is too short the hall sounds dead, so hard reflective panels are kept and the volume is "
        "reduced; a curved rear wall is avoided because it focuses an echo on the stage.",
        "T ટૂંકી હોય તો હોલ મૃત લાગે, તેથી કઠણ પરાવર્તક પેનલ રખાય અને ઘનફળ ઘટાડાય; વળેલી પાછળની દીવાલ "
        "ટાળાય કારણ કે તે પડઘાને મંચ પર કેન્દ્રિત કરે.")]),
    (T("What is the difference between ultrasonic and infrasonic waves? Give two uses of ultrasound.",
       "અલ્ટ્રાસોનિક અને ઇન્ફ્રાસોનિક તરંગોમાં શું ફરક છે? અલ્ટ્રાસાઉન્ડના બે ઉપયોગ આપો."),
     3,
     [P("Ultrasonic waves are above about 20 kHz, the upper limit of human hearing; infrasonic waves "
        "are below 20 Hz, as produced by earthquakes and large machinery.",
        "અલ્ટ્રાસોનિક તરંગો લગભગ 20 kHz થી ઉપર, માનવ શ્રવણની ઉપલી મર્યાદા છે; ઇન્ફ્રાસોનિક તરંગો 20 Hz થી "
        "નીચે, જે ભૂકંપ અને મોટા યંત્રો ઉત્પન્ન કરે."),
      P("Ultrasound has a short wavelength, travels in a narrow beam and reflects at boundaries, which "
        "makes it useful for imaging and for depth measurement.",
        "અલ્ટ્રાસાઉન્ડની તરંગલંબાઈ ટૂંકી હોય, સાંકડા કિરણપુંજમાં ચાલે અને સીમા પર પરાવર્તિત થાય, તેથી "
        "તે ચિત્રણ અને ઊંડાઈ માપન માટે ઉપયોગી બને."),
      P("Uses: sonography in hospitals and SONAR at sea, and in industry flaw detection in castings and "
        "ultrasonic cleaning of jewellery.",
        "ઉપયોગ: હોસ્પિટલમાં સોનોગ્રાફી અને દરિયામાં સોનાર, તથા ઉદ્યોગમાં કાસ્ટિંગની ખામી શોધ અને દાગીનાની "
        "અલ્ટ્રાસોનિક સફાઈ.")]),
    (T("Explain conductors, semiconductors and insulators on the basis of the band gap.",
       "પટ્ટા અંતરના આધારે વાહક, અર્ધવાહક અને અવાહક સમજાવો."),
     4,
     [P("In a solid the electron energies lie in bands: the valence band is the highest filled one and "
        "the conduction band is the next, separated by the energy gap.",
        "ઘનમાં ઇલેક્ટ્રોનની ઊર્જા પટ્ટામાં હોય: સંયોજક પટ્ટો સૌથી ઊંચો ભરેલો અને વહન પટ્ટો તેના પછીનો, "
        "જે ઊર્જા અંતરથી અલગ હોય."),
      P("A conductor has overlapping bands, so electrons move freely; a semiconductor has a gap of about "
        "0.1 to 3 eV, small enough for thermal energy to lift a few electrons across; an insulator has "
        "more than about 3 eV, so almost none cross.",
        "વાહકમાં પટ્ટા એકબીજામાં હોય, તેથી ઇલેક્ટ્રોન મુક્ત ફરે; અર્ધવાહકમાં લગભગ 0.1 થી 3 eV નું અંતર "
        "હોય, જે થોડા ઇલેક્ટ્રોનને ઉષ્મીય ઊર્જાથી પાર કરાવે; અવાહકમાં લગભગ 3 eV થી વધુ, તેથી લગભગ કોઈ પાર "
        "કરતું નથી."),
      P("Silicon (1.1 eV) and germanium (0.7 eV) are the practical semiconductors, and their negative "
        "temperature coefficient — conductivity rising with heat — is the opposite of a metal.",
        "સિલિકોન (1.1 eV) અને જર્મેનિયમ (0.7 eV) વ્યવહારુ અર્ધવાહક છે, અને તેમનો ઋણ તાપમાન ગુણાંક — ગરમી "
        "સાથે વાહકતા વધવી — ધાતુથી ઊલટો છે.")]),
    (T("What is doping? Distinguish N-type from P-type material.",
       "ડોપિંગ શું છે? N પ્રકાર અને P પ્રકારના દ્રવ્યમાં ભેદ આપો."),
     4,
     [P("Doping is the addition of a controlled trace of impurity — typically one atom in a million — "
        "to pure silicon so that its conductivity rises by several orders of magnitude.",
        "ડોપિંગ એ શુદ્ધ સિલિકોનમાં અશુદ્ધિનો નિયંત્રિત થોડો ભાગ — સામાન્ય રીતે દશ લાખમાં એક અણુ — ઉમેરવો "
        "છે જેથી તેની વાહકતા ઘણા ક્રમ વધે."),
      P("Adding a pentavalent atom such as phosphorus gives an N-type crystal, where electrons are the "
        "majority carriers and a donor level sits just below the conduction band.",
        "ફોસ્ફરસ જેવો પંચસંયોજક અણુ ઉમેરતાં N પ્રકારનો સ્ફટિક મળે, જેમાં ઇલેક્ટ્રોન બહુમતી વાહક હોય અને "
        "દાતા સ્તર વહન પટ્ટાના થોડું નીચે હોય."),
      P("Adding a trivalent atom such as boron gives a P-type crystal with holes as the majority "
        "carrier and an acceptor level just above the valence band. Both remain electrically neutral.",
        "બોરોન જેવો ત્રિસંયોજક અણુ ઉમેરતાં P પ્રકારનો સ્ફટિક મળે, જેમાં છિદ્ર બહુમતી વાહક હોય અને ગ્રાહક "
        "સ્તર સંયોજક પટ્ટાના થોડું ઉપર. બંને વિદ્યુતદૃષ્ટિએ તટસ્થ રહે.")]),
    (T("How are ultrasonic waves produced? Explain piezoelectric and magnetostriction methods.",
       "અલ્ટ્રાસોનિક તરંગો કેવી રીતે ઉત્પન્ન થાય? પીઝોઇલેક્ટ્રિક અને મેગ્નેટોસ્ટ્રિક્શન રીતો સમજાવો."),
     4,
     [P("In the piezoelectric method a quartz or barium titanate plate is cut along a crystal axis and "
        "an alternating voltage is applied across it; the plate expands and contracts at the driving "
        "frequency.",
        "પીઝોઇલેક્ટ્રિક રીતમાં ક્વાર્ટ્ઝ કે બેરિયમ ટાઇટેનેટની પ્લેટ સ્ફટિકની ધરી પર કાપાય અને તેના પર "
        "પ્રત્યાવર્તી વોલ્ટેજ આપાય; પ્લેટ ચાલક આવૃત્તિ પર ફેલાય અને સંકોચાય."),
      P("In the magnetostriction method a nickel rod is wound with a coil fed from a valve oscillator; "
        "the changing magnetic field changes the rod's length, and it vibrates at the driving frequency.",
        "મેગ્નેટોસ્ટ્રિક્શન રીતમાં નિકલના સળિયા પર કોઇલ વીંટાય જે દોલકથી ચાલે; બદલાતું ચુંબકીય ક્ષેત્ર "
        "સળિયાની લંબાઈ બદલે, અને તે ચાલક આવૃત્તિ પર દોલિત થાય."),
      P("Both produce a beam of the same frequency as the oscillator, typically 20 kHz to a few MHz, "
        "which is why the oscillator frequency must be stable for imaging work.",
        "બંને દોલક જેટલી જ આવૃત્તિનું કિરણ આપે, સામાન્ય રીતે 20 kHz થી થોડા MHz સુધી, અને તેથી જ ચિત્રણના "
        "કામ માટે દોલકની આવૃત્તિ સ્થિર હોવી જોઈએ.")]),
    (T("A hall of 2400 m³ has a reverberation time of 1.6 s. Find the absorption and the value needed "
       "for 1.0 s.", "2400 m³ ના હોલનો પ્રતિધ્વનિ સમય 1.6 s છે. શોષણ શોધો અને 1.0 s માટે જરૂરી મૂલ્ય."),
     4,
     [P("From Sabine's formula, A = 0.161 V/T = 0.161 × 2400/1.6 = 241 m² sabine.",
        "સેબાઇનના સૂત્રથી, A = 0.161 V/T = 0.161 × 2400/1.6 = 241 m² સેબાઇન."),
      P("For 1.0 s, A = 0.161 × 2400/1.0 = 386 m², so the extra absorption needed is 145 m².",
        "1.0 s માટે A = 0.161 × 2400/1.0 = 386 m², તેથી વધારાનું શોષણ 145 m² જોઈએ."),
      P("That could be about 290 m² of heavy curtain at α = 0.5, or simply a full audience of 320, "
        "which is why the reverberation of a hall changes when the seats are filled.",
        "તે α = 0.5 પર લગભગ 290 m² જાડો પડદો હોઈ શકે, કે ફક્ત 320 શ્રોતાઓ, અને તેથી જ હોલ ભરાય ત્યારે "
        "પ્રતિધ્વનિ બદલાય."),
      P("Check the direction: more absorption means a shorter time, so the second answer must be larger "
        "than the first and the time must fall — 1.6 s down to 1.0 s, which is what a change from 241 to "
        "386 m² gives.",
        "દિશા ચકાસો: વધુ શોષણ એટલે ટૂંકો સમય, તેથી બીજો જવાબ પહેલા કરતાં મોટો હોવો જોઈએ અને સમય ઘટવો "
        "જોઈએ — 1.6 s થી 1.0 s, જે 241 થી 386 m² ના ફેરફારથી મળે.")]),
    (T("Ultrasound of 40 kHz is used in water. Find its wavelength and the depth if the echo returns in "
       "0.4 s.", "પાણીમાં 40 kHz અલ્ટ્રાસાઉન્ડ વપરાય છે. તેની તરંગલંબાઈ અને 0.4 s માં પડઘો આવે તો ઊંડાઈ શોધો."),
     4,
     [P("λ = v/f = 1480/40 000 = 3.7 × 10⁻² m = 3.7 cm.", "λ = v/f = 1480/40 000 = 3.7 × 10⁻² m = 3.7 cm."),
      P("The pulse travels down and back, so d = v t/2 = 1480 × 0.4/2 = 296 m.",
        "સ્પંદ નીચે જાય અને પાછું આવે, તેથી d = v t/2 = 1480 × 0.4/2 = 296 m."),
      P("The short wavelength is what makes this possible: a 3.7 cm wave resolves objects of a few "
        "centimetres, while a 17 m audible wave would give no detail at all.",
        "ટૂંકી તરંગલંબાઈ જ આ શક્ય બનાવે: 3.7 cm તરંગ થોડા સેન્ટીમીટરની વસ્તુ અલગ ઓળખે, જ્યારે 17 m નું "
        "શ્રાવ્ય તરંગ કોઈ વિગત આપે જ નહીં."),
      P("Two practical notes: the speed must be the speed in water and not in air, and the echo time "
        "must be halved, because the pulse travels to the seabed and back before it is timed.",
        "બે વ્યવહારુ નોંધ: વેગ પાણીમાંનો લેવો જોઈએ, હવામાંનો નહીં, અને પડઘાનો સમય અડધો કરવો જોઈએ, કારણ કે "
        "સ્પંદ સમય માપતા પહેલાં દરિયાતળ સુધી જાય અને પાછું આવે.")]),
    (T("Silicon has a band gap of 1.1 eV. Find the maximum wavelength that can create an electron–hole "
       "pair.", "સિલિકોનનું પટ્ટા અંતર 1.1 eV છે. ઇલેક્ટ્રોન-છિદ્ર જોડ બનાવી શકે તેવી મહત્તમ તરંગલંબાઈ શોધો."),
     3,
     [P("The photon must carry at least E_g, so hc/λ = 1.1 eV.", "ફોટોને ઓછામાં ઓછું E_g જોઈએ, તેથી hc/λ = 1.1 eV."),
      P("Using E(eV) = 1240/λ(nm): λ = 1240/1.1 = 1127 nm.", "E(eV) = 1240/λ(nm) વાપરતાં: λ = 1240/1.1 = 1127 nm."),
      P("That is in the near infrared, beyond human vision, which is why silicon detectors are used for "
        "infrared sensing and why the material looks opaque to visible light but transparent to longer "
        "wavelengths.",
        "તે નજીકના ઇન્ફ્રારેડમાં છે, માનવ દૃષ્ટિથી બહાર, તેથી જ સિલિકોન ડિટેક્ટર ઇન્ફ્રારેડ સંવેદનમાં વપરાય "
        "અને તેથી જ તે દૃશ્ય પ્રકાશ માટે અપારદર્શક પણ લાંબી તરંગલંબાઈ માટે પારદર્શક લાગે.")]),
    (T("Why is a semiconductor called a material with a negative temperature coefficient?",
       "અર્ધવાહકને ઋણ તાપમાન ગુણાંકવાળો પદાર્થ કેમ કહેવાય?"),
     3,
     [P("In a semiconductor the number of free carriers is set by how many electrons can cross the band "
        "gap, and heating increases that number sharply.",
        "અર્ધવાહકમાં મુક્ત વાહકોની સંખ્યા એના પર આધારિત છે કે કેટલા ઇલેક્ટ્રોન પટ્ટા અંતર પાર કરી શકે, અને "
        "ગરમી તે સંખ્યા ઝડપથી વધારે."),
      P("The rise in carriers outweighs the fall in their mobility, so the resistivity falls and the "
        "conductivity rises with temperature — the opposite of a metal.",
        "વાહકોનો વધારો તેમની ગતિશીલતાના ઘટાડા કરતાં ભારે પડે, તેથી અવરોધકતા ઘટે અને વાહકતા તાપમાન સાથે "
        "વધે — ધાતુથી ઊલટું."),
      P("This is why a thermistor is made of semiconductor material and why a power device must be kept "
        "cool: a hot junction would conduct when it should block.",
        "તેથી જ થર્મિસ્ટર અર્ધવાહક પદાર્થનું બને છે અને પાવર ઉપકરણ ઠંડું રાખવું પડે: ગરમ સંધિ જ્યારે "
        "અવરોધ કરવો જોઈએ ત્યારે વહન કરી દે.")]),
]

EXAM = [{"q": q, "marks": m} for q, m, _parts in _PRACTICE]
PRACTICE_ANSWERS = [_join(parts) for _q, _m, parts in _PRACTICE]

LESSON_COUNT = sum(len(s["items"]) for s in NOTES)
