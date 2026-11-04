"""DI01000121 Applied Physics - Unit 3: General Properties of Matter (bilingual en + gu).

GTU 3.1-3.3 (nineteen sub-clauses), 12 h, 28 %, 19 marks, CO3. The largest unit of the subject:
elasticity, surface tension and viscosity.
"""
from content_DI01000121_u1_notes import T, P, H4, UL, OL, TB, card, num, _join

SOURCES = [
    T("GTU DI01000121 Applied Physics syllabus (uploaded PDF, w.e.f. 2024-25)",
      "GTU DI01000121 એપ્લાઇડ ફિઝિક્સ સિલેબસ (અપલોડ કરેલ PDF, 2024-25થી અમલમાં)"),
    T("NCERT Physics Class XI, Part II - Mechanical Properties of Solids and Fluids",
      "NCERT ભૌતિક વિજ્ઞાન ધોરણ 11, ભાગ 2 - ઘન અને પ્રવાહીના યાંત્રિક ગુણધર્મો"),
    T("H. C. Verma - Concepts of Physics, Vol. I, chapters 14 and 15",
      "એચ. સી. વર્મા - કોન્સેપ્ટ્સ ઓફ ફિઝિક્સ, ભાગ 1, પ્રકરણ 14 અને 15"),
    T("M. N. Avadhanulu - A Textbook of Engineering Physics, properties of matter chapters",
      "એમ. એન. અવધાનુલુ - ટેક્સ્ટબુક ઓફ એન્જિનિયરિંગ ફિઝિક્સ, પ્રોપર્ટીઝ ઓફ મેટર પ્રકરણો"),
    T("C. L. Arora - B.Sc. Practical Physics: Searle's modulus, capillary rise, Stokes' law",
      "સી. એલ. અરોરા - પ્રેક્ટિકલ ફિઝિક્સ: સર્લનો ગુણાંક, કેશનળી ચઢાણ, સ્ટોક્સનો નિયમ"),
]

NOTES = [
    {"title": T("1. Elasticity", "1. સ્થિતિસ્થાપકતા"),
     "items": [
         card(T("1.1 Deforming and restoring force",
                "1.1 વિકૃતિકારક અને પુનઃસ્થાપક બળ"),
              [H4("Definition", "વ્યાખ્યા"),
               P("A <b>deforming force</b> changes the shape or size of a body. The internal force the "
                 "body develops to oppose that change is the <b>restoring force</b>. A body that "
                 "returns to its original shape when the load is removed is <b>elastic</b>; one that "
                 "does not is <b>plastic</b>.",
                 "<b>વિકૃતિકારક બળ</b> શરીરનો આકાર કે માપ બદલે છે. તે ફેરફારનો વિરોધ કરવા શરીરમાં "
                 "ઉત્પન્ન થતું આંતરિક બળ <b>પુનઃસ્થાપક બળ</b> છે. ભાર દૂર કરતાં જે શરીર પોતાનો મૂળ આકાર "
                 "પાછો મેળવે તે <b>સ્થિતિસ્થાપક</b> છે; જે ન મેળવે તે <b>સ્થાયી</b> (પ્લાસ્ટિક) છે."),
               H4("Everyday and engineering examples", "રોજિંદા અને ઇજનેરી ઉદાહરણો"),
               TB([T("Object", "વસ્તુ"), T("Behaviour", "વર્તન")],
                  [[T("rubber band, spring", "રબર બેન્ડ, સ્પ્રિંગ"), T("elastic: returns fully", "સ્થિતિસ્થાપક: પૂરું પાછું આવે")],
                   [T("clay, wet soil", "માટી, ભીની જમીન"), T("plastic: stays deformed", "સ્થાયી: વિકૃત જ રહે")],
                   [T("steel beam of a bridge", "પુલનો સ્ટીલ બીમ"), T("elastic within the design load", "રચનાના ભાર સુધી સ્થિતિસ્થાપક")],
                   [T("copper wire bent many times", "વારંવાર વળેલો તાંબાનો તાર"), T("plastic, then it breaks", "સ્થાયી, પછી તૂટે")]]),
               H4("Worked example", "ઉકેલાયેલ દાખલો"),
               P("A spring stretched by 2 cm with 10 N returns fully when released. Its restoring force "
                 "is 10 N at that extension, and k = F/x = 10/0.02 = 500 N/m.",
                 "2 cm ખેંચેલી સ્પ્રિંગ 10 N સાથે છોડતાં પૂરી પાછી આવે છે. તે ખેંચાણ પર પુનઃસ્થાપક બળ "
                 "10 N છે અને k = F/x = 10/0.02 = 500 N/m."),
               H4("Common mistake", "સામાન્ય ભૂલ"),
               P("Calling every spring elastic at any load. Beyond its elastic limit even steel stays "
                 "stretched, which is how a suspension is ruined by overloading.",
                 "કોઈપણ ભાર પર દરેક સ્પ્રિંગને સ્થિતિસ્થાપક કહેવી. સ્થિતિસ્થાપક મર્યાદા પછી સ્ટીલ પણ "
                 "ખેંચાયેલું રહે છે, અને તેથી જ વધુ ભારથી સસ્પેન્શન બગડે છે.")],
              "u3_stress", syllabus_item="3.1.1"),
         card(T("1.2 Stress and strain, and their types",
                "1.2 પ્રતિબળ અને વિકૃતિ તથા તેમના પ્રકાર"),
              [H4("Definitions", "વ્યાખ્યાઓ"),
               P("<b>Stress</b> = restoring force / area, σ = F/A, in N/m² (pascal). "
                 "<b>Strain</b> = fractional change of dimension; it has no unit.",
                 "<b>પ્રતિબળ</b> = પુનઃસ્થાપક બળ / ક્ષેત્રફળ, σ = F/A, N/m² (પાસ્કલ)માં. "
                 "<b>વિકૃતિ</b> = પરિમાણમાં થતો અંશતઃ ફેરફાર; તેને એકમ હોતું નથી."),
               H4("Three kinds of stress and strain", "ત્રણ પ્રકારનાં પ્રતિબળ અને વિકૃતિ"),
               TB([T("Type", "પ્રકાર"), T("What changes", "શું બદલાય"), T("Strain", "વિકૃતિ")],
                  [[T("tensile / compressive", "તણાવ / સંકોચન"), T("length", "લંબાઈ"), T("ΔL/L", "ΔL/L")],
                   [T("volume (hydraulic)", "ઘનફળ (દ્રવ્યાવસ્થિક)"), T("volume", "ઘનફળ"), T("ΔV/V", "ΔV/V")],
                   [T("shear (tangential)", "શિયર (સ્પર્શીય)"), T("shape, not volume", "આકાર, ઘનફળ નહીં"), T("Δx/h = tan φ", "Δx/h = tan φ")]]),
               H4("Worked example", "ઉકેલાયેલ દાખલો"),
               P("A 100 N load on a wire of cross-section 2 mm² gives σ = 100/(2 × 10⁻⁶) = 5 × 10⁷ N/m². "
                 "Stretching it by 0.5 mm over 2 m is a strain of 2.5 × 10⁻⁴.",
                 "2 mm² કાપવાળા તાર પર 100 N ભાર σ = 100/(2 × 10⁻⁶) = 5 × 10⁷ N/m² આપે. 2 m પર 0.5 mm "
                 "ખેંચાણ એ 2.5 × 10⁻⁴ વિકૃતિ છે."),
               H4("Common mistake", "સામાન્ય ભૂલ"),
               P("Using the diameter instead of the area, and forgetting to convert mm² to m². "
                 "1 mm² = 10⁻⁶ m², which changes the answer by a factor of a million.",
                 "ક્ષેત્રફળને બદલે વ્યાસ વાપરવો, અને mm² ને m² માં ફેરવવાનું ભૂલવું. 1 mm² = 10⁻⁶ m², "
                 "જે જવાબમાં લાખ ગણો ફરક પાડે.")],
              syllabus_item="3.1.2"),
         card(T("1.3 Hooke's law and the elastic limit",
                "1.3 હૂકનો નિયમ અને સ્થિતિસ્થાપક મર્યાદા"),
              [H4("Statement", "વિધાન"),
               P("Within the elastic limit, stress is directly proportional to strain: σ ∝ ε, or "
                 "σ = E ε where E is the modulus of elasticity of the material.",
                 "સ્થિતિસ્થાપક મર્યાદા સુધી પ્રતિબળ વિકૃતિના સમપ્રમાણમાં હોય છે: σ ∝ ε, અથવા "
                 "σ = E ε, જ્યાં E પદાર્થનો સ્થિતિસ્થાપકતા ગુણાંક છે."),
               H4("What it means in practice", "વ્યવહારમાં તેનો અર્થ"),
               UL(("Doubling the load doubles the extension, as long as the limit is not crossed.",
                   "ભાર બમણો કરો તો ખેંચાણ પણ બમણું, જ્યાં સુધી મર્યાદા ન વળંગાય."),
                  ("The spring constant k = F/x is Hooke's law written for a spring.",
                   "સ્પ્રિંગ અચળાંક k = F/x એ સ્પ્રિંગ માટે લખેલો હૂકનો નિયમ છે."),
                  ("A graph of stress against strain is a straight line through the origin only in "
                   "this region.", "પ્રતિબળ–વિકૃતિનો આલેખ ફક્ત આ વિસ્તારમાં ઉદ્ગમમાંથી પસાર થતી સીધી "
                   "રેખા હોય છે.")),
               H4("Worked example", "ઉકેલાયેલ દાખલો"),
               P("A spring of k = 500 N/m stretched 4 cm carries F = 500 × 0.04 = 20 N. Stretch it 10 cm "
                 "and the force is 50 N — until the coils close or the wire yields.",
                 "k = 500 N/m ની સ્પ્રિંગ 4 cm ખેંચાય તો F = 500 × 0.04 = 20 N. 10 cm ખેંચો તો 50 N — "
                 "જ્યાં સુધી કોઇલ બંધ ન થાય કે તાર થાકે નહીં."),
               H4("Common mistake", "સામાન્ય ભૂલ"),
               P("Using Hooke's law past the yield point. A wire loaded beyond its limit keeps "
                 "stretching with no further increase in load.",
                 "ઉપજ મર્યાદા પછી પણ હૂકનો નિયમ વાપરવો. મર્યાદા પછી ભાર વધ્યા વગર પણ તાર ખેંચાતો રહે છે.")],
              syllabus_item="3.1.3"),
         card(T("1.4 Young's, bulk and shear modulus",
                "1.4 યંગ, બલ્ક અને શિયર ગુણાંક"),
              [H4("The three moduli", "ત્રણ ગુણાંક"),
               TB([T("Modulus", "ગુણાંક"), T("Formula", "સૂત્ર"), T("Measures resistance to", "કઈ વિકૃતિ સામે પ્રતિરોધ")],
                  [[T("Young's modulus Y", "યંગ ગુણાંક Y"), T("Y = (F/A)/(ΔL/L) = σ/ε", "Y = (F/A)/(ΔL/L) = σ/ε"), T("stretching of a wire", "તારનું ખેંચાણ")],
                   [T("Bulk modulus K", "બલ્ક ગુણાંક K"), T("K = −ΔP/(ΔV/V)", "K = −ΔP/(ΔV/V)"), T("change of volume of a solid or liquid", "ઘન કે પ્રવાહીના ઘનફળનો ફેરફાર")],
                   [T("Shear modulus G", "શિયર ગુણાંક G"), T("G = (F/A)/(Δx/h)", "G = (F/A)/(Δx/h)"), T("change of shape at constant volume", "અચળ ઘનફળે આકારનો ફેરફાર")]]),
               H4("Typical values", "સામાન્ય મૂલ્યો"),
               TB([T("Material", "પદાર્થ"), T("Young's modulus", "યંગ ગુણાંક")],
                  [[T("steel", "સ્ટીલ"), T("2.0 × 10¹¹ N/m²", "2.0 × 10¹¹ N/m²")],
                   [T("copper", "તાંબું"), T("1.2 × 10¹¹ N/m²", "1.2 × 10¹¹ N/m²")],
                   [T("aluminium", "એલ્યુમિનિયમ"), T("0.70 × 10¹¹ N/m²", "0.70 × 10¹¹ N/m²")],
                   [T("rubber", "રબર"), T("0.01–0.1 × 10¹¹ N/m²", "0.01–0.1 × 10¹¹ N/m²")]]),
               H4("Worked example", "ઉકેલાયેલ દાખલો"),
               P("A steel wire of area 1 mm² carrying 50 N over 2 m: ΔL = FL/(AY) = "
                 "50 × 2/(10⁻⁶ × 2 × 10¹¹) = 0.5 mm.",
                 "1 mm² કાપવાળો સ્ટીલ તાર 2 m પર 50 N લે: ΔL = FL/(AY) = 50 × 2/(10⁻⁶ × 2 × 10¹¹) = 0.5 mm."),
               H4("Common mistake", "સામાન્ય ભૂલ"),
               P("Thinking a stiff material is also strong. Stiffness is Y (resistance to bending), "
                 "strength is the breaking stress; glass is stiff and brittle, rubber is soft and tough.",
                 "કઠણ પદાર્થ મજબૂત પણ હશે એમ માનવું. કઠોરતા Y છે (વળવાનો પ્રતિરોધ), મજબૂતાઈ તૂટવાનું "
                 "પ્રતિબળ છે; કાચ કઠણ પણ ભંગુર છે, રબર નરમ પણ ટકાઉ.")],
              "u3_moduli", syllabus_item="3.1.4"),
         card(T("1.5 The stress-strain curve",
                "1.5 પ્રતિબળ-વિકૃતિ વક્ર"),
              [H4("The five points on the curve", "વક્ર પરનાં પાંચ બિંદુ"),
               TB([T("Point", "બિંદુ"), T("Meaning", "અર્થ")],
                  [[T("O to A", "O થી A"), T("straight line: Hooke's law holds, slope = Y", "સીધી રેખા: હૂકનો નિયમ લાગુ, ઢાળ = Y")],
                   [T("A: proportional limit", "A: સમપ્રમાણ મર્યાદા"), T("the straight line ends here", "સીધી રેખા અહીં પૂરી થાય")],
                   [T("B: elastic limit or yield point", "B: સ્થિતિસ્થાપક મર્યાદા કે ઉપજ બિંદુ"), T("beyond B the wire stays stretched", "B પછી તાર ખેંચાયેલો રહે")],
                   [T("D: ultimate tensile strength", "D: અંતિમ તણાવ મજબૂતાઈ"), T("the highest stress the material carries", "પદાર્થ લઈ શકે તે સૌથી વધુ પ્રતિબળ")],
                   [T("E: fracture point", "E: ભંગ બિંદુ"), T("the wire breaks", "તાર તૂટે")]]),
               H4("Why engineers care", "ઇજનેરો કેમ ધ્યાન આપે"),
               P("Design uses only the straight part OA, with a safety factor: the working stress is "
                 "kept well below the yield stress B so that the part springs back after every load.",
                 "રચના ફક્ત સીધા ભાગ OA નો ઉપયોગ કરે, સલામતી અવયવ સાથે: કાર્યકારી પ્રતિબળ ઉપજ પ્રતિબળ B "
                 "કરતાં ઘણું નીચે રખાય જેથી દરેક ભાર પછી પાર્ટ પાછો સ્થિતિસ્થાપક રહે."),
               H4("Worked example", "ઉકેલાયેલ દાખલો"),
               P("A mild-steel specimen with yield stress 250 MPa and a safety factor of 2.5 may be "
                 "loaded to 100 MPa, which for a 10 mm² section is 1000 N.",
                 "250 MPa ઉપજ પ્રતિબળવાળા માઇલ્ડ સ્ટીલના નમૂના પર 2.5 નો સલામતી અવયવ હોય તો 100 MPa સુધી "
                 "ભાર આપી શકાય, જે 10 mm² કાપ માટે 1000 N છે."),
               H4("Common mistake", "સામાન્ય ભૂલ"),
               P("Reading the curve's height as strength alone. Ductile steel reaches D and then "
                 "stretches far before E; glass breaks at D almost at once.",
                 "વક્રની ઊંચાઈને ફક્ત મજબૂતાઈ ગણવી. નમ્ય સ્ટીલ D સુધી પહોંચીને E પહેલાં ઘણું ખેંચાય છે; "
                 "કાચ D પર જ લગભગ તરત તૂટે છે.")],
              syllabus_item="3.1.5"),
         card(T("1.6 Elastic potential energy and the Searle experiment",
                "1.6 સ્થિતિસ્થાપક સ્થિતિઊર્જા અને સર્લનો પ્રયોગ"),
              [H4("Energy stored", "સંગ્રહાયેલી ઊર્જા"),
               P("Work done in stretching a wire within the elastic limit is stored as elastic potential "
                 "energy: U = ½ F ΔL = ½ × stress × strain × volume.",
                 "સ્થિતિસ્થાપક મર્યાદામાં તાર ખેંચવામાં થતું કાર્ય સ્થિતિસ્થાપક સ્થિતિઊર્જા તરીકે સંગ્રહાય "
                 "છે: U = ½ F ΔL = ½ × પ્રતિબળ × વિકૃતિ × ઘનફળ."),
               H4("The Searle experiment (practical 4)", "સર્લનો પ્રયોગ (પ્રેક્ટિકલ 4)"),
               OL(("Hang a steel wire from a rigid support beside a reference wire.",
                   "કઠણ આધારથી સ્ટીલનો તાર લટકાવો, સાથે સંદર્ભ તાર પણ."),
                  ("Add known loads and read the extension with a vernier scale or micrometer.",
                   "જાણીતા ભાર ઉમેરો અને વર્નિયર કે માઇક્રોમીટરથી ખેંચાણ વાંચો."),
                  ("Measure the wire diameter with a screw gauge and the length with a tape.",
                   "તારનો વ્યાસ સ્ક્રુ ગેજથી અને લંબાઈ ટેપથી માપો."),
                  ("Plot load against extension; Y = (F/A)/(ΔL/L) from the straight part.",
                   "ભાર સામે ખેંચાણનો આલેખ દોરો; સીધા ભાગ પરથી Y = (F/A)/(ΔL/L).")),
               H4("Worked example", "ઉકેલાયેલ દાખલો"),
               P("Stretching a wire by 0.5 mm with 50 N stores U = ½ × 50 × 5 × 10⁻⁴ = 0.0125 J.",
                 "50 N થી 0.5 mm ખેંચાયેલા તારમાં U = ½ × 50 × 5 × 10⁻⁴ = 0.0125 J સંગ્રહાય છે."),
               H4("Common mistake", "સામાન્ય ભૂલ"),
               P("Using U = F ΔL without the ½. The force grows from zero to F, so the average is F/2.",
                 "½ વગર U = F ΔL વાપરવું. બળ શૂન્યથી F સુધી વધે છે, તેથી સરેરાશ F/2 થાય.")],
              syllabus_item="3.1"),
     ]},

    {"title": T("2. Surface Tension", "2. પૃષ્ઠતાણ"),
     "items": [
         card(T("2.1 Surface tension: the concept and its units",
                "2.1 પૃષ્ઠતાણ: ખ્યાલ અને એકમો"),
              [H4("Definition", "વ્યાખ્યા"),
               P("<b>Surface tension</b> T is the force per unit length acting along the surface of a "
                 "liquid, perpendicular to any line drawn on it, tending to reduce the area. "
                 "T = F/L, unit N/m.",
                 "<b>પૃષ્ઠતાણ</b> T એ પ્રવાહીની સપાટી પર દોરેલી કોઈપણ રેખાને લંબરૂપે, એકમ લંબાઈ દીઠ લાગતું "
                 "બળ છે, જે ક્ષેત્રફળ ઘટાડવા પ્રયત્ન કરે. T = F/L, એકમ N/m."),
               P("It also equals the surface energy per unit area (J/m²), which is why the same symbol "
                 "carries two units.",
                 "તે એકમ ક્ષેત્રફળ દીઠ પૃષ્ઠઊર્જા (J/m²) પણ છે, તેથી જ એક જ સંજ્ઞાને બે એકમ હોય છે."),
               H4("Effects you can see", "દેખીતી અસરો"),
               TB([T("Observation", "નિરીક્ષણ"), T("Reason", "કારણ")],
                  [[T("a drop is spherical", "ટીપું ગોળાકાર હોય"), T("a sphere has the least area for a given volume", "આપેલ ઘનફળ માટે ગોળાનું ક્ષેત્રફળ સૌથી ઓછું")],
                   [T("a needle floats on water", "પાણી પર સોય તરે"), T("the surface film bends and supports it", "સપાટીનો પડ વળીને ટેકો આપે")],
                   [T("water rises in a thin tube", "પાતળી નળીમાં પાણી ચઢે"), T("adhesion beats cohesion and the meniscus pulls it up", "આસક્તિ સંસક્તિ પર ભારે, મેનિસ્કસ ઉપર ખેંચે")],
                   [T("rain forms drops, not a sheet", "વરસાદ ટીપાં બનાવે, પડ નહીં"), T("the liquid pulls itself into minimum area", "પ્રવાહી પોતાને લઘુતમ ક્ષેત્રફળમાં ખેંચે")]]),
               H4("Worked example", "ઉકેલાયેલ દાખલો"),
               P("A wire frame with a 10 cm sliding wire and a soap film needs F = 2 T L because the film "
                 "has two surfaces: F = 2 × 0.025 × 0.1 = 5 × 10⁻³ N.",
                 "10 cm સરકતા તારવાળી ફ્રેમ પર સાબુનો પડ માટે F = 2 T L જોઈએ, કારણ કે પડને બે સપાટી હોય: "
                 "F = 2 × 0.025 × 0.1 = 5 × 10⁻³ N."),
               H4("Common mistake", "સામાન્ય ભૂલ"),
               P("Forgetting the factor 2 for a soap film. A film has a front and a back surface; a "
                 "liquid drop boundary has only one.",
                 "સાબુના પડ માટે 2 નો અવયવ ભૂલવો. પડને આગળ અને પાછળ બે સપાટી હોય; પ્રવાહી ટીપાની સીમાને "
                 "ફક્ત એક.")],
              "u3_surface", syllabus_item="3.2.1"),
         card(T("2.2 Cohesive and adhesive forces",
                "2.2 સંસક્તિ અને આસક્તિ બળો"),
              [H4("Definitions", "વ્યાખ્યાઓ"),
               P("<b>Cohesive force</b> is the attraction between molecules of the same substance. "
                 "<b>Adhesive force</b> is the attraction between molecules of different substances.",
                 "<b>સંસક્તિ બળ</b> એ એક જ પદાર્થના અણુઓ વચ્ચેનું આકર્ષણ છે. <b>આસક્તિ બળ</b> એ જુદા "
                 "પદાર્થોના અણુઓ વચ્ચેનું આકર્ષણ છે."),
               H4("What the balance decides", "સંતુલન શું નક્કી કરે"),
               TB([T("Balance", "સંતુલન"), T("Result", "પરિણામ"), T("Example", "ઉદાહરણ")],
                  [[T("cohesion > adhesion", "સંસક્તિ > આસક્તિ"), T("liquid does not wet the solid, meniscus convex", "પ્રવાહી સપાટીને ભીની કરતું નથી, મેનિસ્કસ બહિર્ગોળ"), T("mercury in glass", "કાચમાં પારો")],
                   [T("adhesion > cohesion", "આસક્તિ > સંસક્તિ"), T("liquid wets the solid, meniscus concave", "પ્રવાહી સપાટીને ભીની કરે, મેનિસ્કસ અંતર્ગોળ"), T("water in glass", "કાચમાં પાણી")],
                   [T("cohesion > adhesion to air", "હવા સાથે આસક્તિ કરતાં સંસક્તિ વધુ"), T("liquid forms a drop instead of spreading", "પ્રવાહી ફેલાયા વગર ટીપું બનાવે"), T("water on a waxed surface", "મીણવાળી સપાટી પર પાણી")]]),
               H4("Engineering use", "ઇજનેરી ઉપયોગ"),
               UL(("Paint must adhere to steel more strongly than it coheres to itself, or it peels.",
                   "પેન્ટ સ્ટીલ સાથે પોતાના સંસક્તિ બળ કરતાં વધુ મજબૂતાઈથી જોડાવું જોઈએ, નહીં તો ઊતરી જાય."),
                  ("Lubricants are chosen so that they do not wet the surfaces too strongly, which is "
                   "why oil and water are both used in different bearings.",
                   "લુબ્રિકન્ટ એવા પસંદ થાય જે સપાટીને બહુ ભીની ન કરે, તેથી જુદા બેરિંગમાં તેલ અને પાણી "
                   "બંને વપરાય."),
                  ("Detergents work by lowering the surface tension of water so that it wets the cloth.",
                   "ડિટરજન્ટ પાણીનું પૃષ્ઠતાણ ઘટાડે જેથી તે કપડાને ભીનું કરે.")),
               H4("Common mistake", "સામાન્ય ભૂલ"),
               P("Saying mercury 'repels' glass. It simply coheres to itself more strongly than it "
                 "adheres to glass.",
                 "પારો કાચને 'દૂર કરે' એમ કહેવું. તે કાચ સાથે આસક્તિ કરતાં પોતાની સાથે વધુ સંસક્તિ ધરાવે છે.")],
              syllabus_item="3.2.2"),
         card(T("2.3 Molecular range and the sphere of influence",
                "2.3 આણ્વીય પરાસ અને પ્રભાવ ગોળો"),
              [H4("Definitions", "વ્યાખ્યાઓ"),
               P("<b>Molecular range</b> is the maximum distance (about 10⁻⁹ m) up to which the "
                 "attraction between two molecules is felt. A <b>sphere of influence</b> of radius "
                 "equal to the molecular range is drawn around a molecule: only the molecules inside "
                 "it pull on it.",
                 "<b>આણ્વીય પરાસ</b> એ સૌથી વધુ અંતર (લગભગ 10⁻⁹ m) છે જ્યાં સુધી બે અણુઓ વચ્ચેનું આકર્ષણ "
                 "અનુભવાય. આણ્વીય પરાસ જેટલી ત્રિજ્યાનો <b>પ્રભાવ ગોળો</b> અણુની આસપાસ દોરાય: તેમાં રહેલા "
                 "અણુઓ જ તેને ખેંચે."),
               H4("Why the surface behaves differently", "સપાટી જુદી કેમ વર્તે"),
               TB([T("Molecule", "અણુ"), T("Sphere of influence", "પ્રભાવ ગોળો"), T("Net pull", "ચોખ્ખું આકર્ષણ")],
                  [[T("deep inside", "ઊંડે અંદર"), T("completely filled", "પૂરો ભરેલો"), T("zero, all round", "શૂન્ય, ચારે બાજુ સમાન")],
                   [T("at the surface", "સપાટી પર"), T("half filled, half empty", "અડધો ભરેલો, અડધો ખાલી"), T("inward, so the surface is stretched", "અંદર તરફ, તેથી સપાટી તંગ")]]),
               H4("Worked example", "ઉકેલાયેલ દાખલો"),
               P("If the molecular range is 10⁻⁹ m, a molecule at the surface feels no pull from above "
                 "beyond 1 nm, while one 5 nm deep has a full sphere — that difference is the surface "
                 "energy of about 0.072 J/m² for water.",
                 "આણ્વીય પરાસ 10⁻⁹ m હોય તો સપાટી પરનો અણુ 1 nm ઉપરથી કોઈ ખેંચાણ અનુભવતું નથી, જ્યારે "
                 "5 nm ઊંડે રહેલા અણુનો ગોળો પૂરો છે — એ જ તફાવત પાણી માટે લગભગ 0.072 J/m² પૃષ્ઠઊર્જા છે."),
               H4("Common mistake", "સામાન્ય ભૂલ"),
               P("Thinking the surface layer is thicker than a few molecules. It is only the molecular "
                 "range deep, roughly a nanometre.",
                 "સપાટીનો સ્તર થોડા અણુઓ કરતાં જાડો છે એમ માનવું. તે ફક્ત આણ્વીય પરાસ જેટલો, લગભગ એક "
                 "નેનોમીટર જાડો હોય છે.")],
              syllabus_item="3.2.3"),
         card(T("2.4 Laplace's molecular theory of surface tension",
                "2.4 પૃષ્ઠતાણનો લાપ્લાસનો આણ્વીય સિદ્ધાંત"),
              [H4("The idea", "ખ્યાલ"),
               P("A molecule inside a liquid is pulled equally in all directions. A molecule at the "
                 "surface is pulled only inwards and downwards, so the surface behaves like a stretched "
                 "membrane that tries to shrink.",
                 "પ્રવાહીની અંદરનો અણુ ચારે બાજુ સમાન ખેંચાણ અનુભવે છે. સપાટી પરનો અણુ ફક્ત અંદર અને નીચે "
                 "ખેંચાય છે, તેથી સપાટી તંગ પડ જેવી વર્તે જે સંકોચાવા પ્રયત્ન કરે."),
               H4("What the theory explains", "સિદ્ધાંત શું સમજાવે"),
               OL(("Why the surface has energy: pulling a molecule to the surface needs work.",
                   "સપાટીમાં ઊર્જા કેમ છે: અણુને સપાટી પર લાવવા કાર્ય કરવું પડે."),
                  ("Why a free drop is spherical: minimum surface area for the volume.",
                   "મુક્ત ટીપું ગોળાકાર કેમ છે: ઘનફળ માટે લઘુતમ પૃષ્ઠ ક્ષેત્રફળ."),
                  ("Why surface tension falls with temperature: molecules move faster and the range "
                   "of attraction is less effective.", "તાપમાન સાથે પૃષ્ઠતાણ કેમ ઘટે: અણુઓ ઝડપથી ફરે અને "
                   "આકર્ષણની અસર ઘટે.")),
               H4("Worked example", "ઉકેલાયેલ દાખલો"),
               P("For water T = 0.072 N/m at 20 °C and about 0.059 N/m at 100 °C, a fall of nearly 20 % "
                 "— enough to change how a boiler surface wets and how condensate drains.",
                 "પાણી માટે 20 °C પર T = 0.072 N/m અને 100 °C પર લગભગ 0.059 N/m, એટલે લગભગ 20 % ઘટાડો — "
                 "જે બોઇલરની સપાટી ભીની થવાની રીત અને કન્ડેન્સેટ વહેવાની રીત બદલી નાખે."),
               H4("Common mistake", "સામાન્ય ભૂલ"),
               P("Believing the surface is a real skin. There is no membrane; the effect comes from the "
                 "unbalanced molecular pull.",
                 "સપાટીને સાચી ત્વચા માનવી. કોઈ પડ નથી; અસર અસંતુલિત આણ્વીય ખેંચાણમાંથી આવે છે.")],
              syllabus_item="3.2.4"),
         card(T("2.5 Surface tension and surface energy",
                "2.5 પૃષ્ઠતાણ અને પૃષ્ઠઊર્જા"),
              [H4("The relation", "સંબંધ"),
               P("Work done in increasing the surface area by ΔA is W = T ΔA, so surface tension equals "
                 "the surface energy per unit area: T = W/ΔA. Numerically 1 N/m = 1 J/m².",
                 "સપાટીનું ક્ષેત્રફળ ΔA જેટલું વધારવામાં થતું કાર્ય W = T ΔA છે, તેથી પૃષ્ઠતાણ એકમ ક્ષેત્રફળ "
                 "દીઠ પૃષ્ઠઊર્જા બરાબર છે: T = W/ΔA. આંકડામાં 1 N/m = 1 J/m²."),
               H4("Worked example", "ઉકેલાયેલ દાખલો"),
               P("Blowing a soap bubble of radius 2 cm needs W = T × 2 × 4πr² = 0.025 × 2 × 4π(0.02)² = "
                 "2.5 × 10⁻⁴ J, because a bubble has two surfaces.",
                 "2 cm ત્રિજ્યાનો સાબુનો પરપોટો ફૂંકવા W = T × 2 × 4πr² = 0.025 × 2 × 4π(0.02)² = "
                 "2.5 × 10⁻⁴ J જોઈએ, કારણ કે પરપોટાને બે સપાટી હોય."),
               H4("Engineering reading", "ઇજનેરી અર્થઘટન"),
               P("Atomising a liquid into fine droplets costs surface energy, which is why a nozzle "
                 "needs pressure and why fine sprays are hard to make with viscous liquids.",
                 "પ્રવાહીને ઝીણા ટીપાંમાં છંટકાવવા પૃષ્ઠઊર્જા ખર્ચાય, તેથી નોઝલને દબાણ જોઈએ અને શ્યાન "
                 "પ્રવાહીના ઝીણા ફુવારા બનાવવા અઘરા છે."),
               H4("Common mistake", "સામાન્ય ભૂલ"),
               P("Using 4πr² for a bubble instead of 2 × 4πr², or applying the factor 2 to a drop, "
                 "which has only one surface.",
                 "પરપોટા માટે 2 × 4πr² ને બદલે 4πr² વાપરવું, અથવા ટીપા પર 2 નો અવયવ લગાડવો, જેને ફક્ત એક "
                 "સપાટી હોય.")],
              syllabus_item="3.2.6"),
         card(T("2.6 Angle of contact",
                "2.6 સંપર્ક કોણ"),
              [H4("Definition", "વ્યાખ્યા"),
               P("The <b>angle of contact</b> θ is the angle between the tangent to the liquid surface "
                 "and the solid surface inside the liquid, measured at the point of contact.",
                 "<b>સંપર્ક કોણ</b> θ એ પ્રવાહીની સપાટીને સ્પર્શક અને પ્રવાહીની અંદરની ઘન સપાટી વચ્ચેનો "
                 "ખૂણો છે, જે સંપર્ક બિંદુએ મપાય."),
               TB([T("Liquid and surface", "પ્રવાહી અને સપાટી"), T("Angle of contact", "સંપર્ક કોણ"), T("Meniscus", "મેનિસ્કસ")],
                  [[T("water and clean glass", "પાણી અને સ્વચ્છ કાચ"), T("0° to 8°", "0° થી 8°"), T("concave, rises", "અંતર્ગોળ, ચઢે")],
                   [T("mercury and glass", "પારો અને કાચ"), T("about 140°", "લગભગ 140°"), T("convex, falls", "બહિર્ગોળ, ઉતરે")],
                   [T("water and waxed surface", "પાણી અને મીણવાળી સપાટી"), T("about 110°", "લગભગ 110°"), T("convex", "બહિર્ગોળ")],
                   [T("kerosene and glass", "કેરોસીન અને કાચ"), T("near 0°", "લગભગ 0°"), T("concave", "અંતર્ગોળ")]]),
               H4("What fixes the angle", "કોણ શું નક્કી કરે"),
               P("The angle is set by the balance of three surface tensions: solid–liquid, "
                 "solid–vapour and liquid–vapour. A liquid wets a surface when θ < 90°.",
                 "કોણ ત્રણ પૃષ્ઠતાણના સંતુલનથી નક્કી થાય: ઘન–પ્રવાહી, ઘન–બાષ્પ અને પ્રવાહી–બાષ્પ. θ < 90° "
                 "હોય ત્યારે પ્રવાહી સપાટીને ભીની કરે."),
               H4("Common mistake", "સામાન્ય ભૂલ"),
               P("Measuring the angle outside the liquid. It is always measured inside, which is why "
                 "mercury reads about 140° and not 40°.",
                 "કોણ પ્રવાહીની બહાર માપવો. તે હંમેશા અંદર મપાય, તેથી જ પારો 40° નહીં પણ લગભગ 140° વાંચે.")],
              "u3_capillary", syllabus_item="3.2.5"),
     ]},

    {"title": T("3. Capillarity and the Uses of Surface Tension",
                "3. કેશનળી ચઢાણ અને પૃષ્ઠતાણના ઉપયોગો"),
     "items": [
         card(T("3.1 The Ascent formula (no derivation)",
                "3.1 આરોહણ સૂત્ર (સાબિતી વગર)"),
              [H4("The formula", "સૂત્ર"),
               P("A liquid of surface tension T, density ρ and contact angle θ rises in a tube of "
                 "radius r to height h: <b>h = 2T cos θ / (ρ g r)</b>. Mercury, with θ > 90°, gives a "
                 "negative h, that is a depression.",
                 "પૃષ્ઠતાણ T, ઘનતા ρ અને સંપર્ક કોણ θ વાળું પ્રવાહી r ત્રિજ્યાની નળીમાં h ઊંચાઈ સુધી "
                 "ચઢે: <b>h = 2T cos θ / (ρ g r)</b>. પારા માટે θ > 90° હોવાથી h ઋણ મળે, એટલે ઉતાર."),
               H4("What the formula says", "સૂત્ર શું કહે"),
               UL(("Thinner tube, higher rise: h ∝ 1/r.", "પાતળી નળી, વધુ ચઢાણ: h ∝ 1/r."),
                  ("Lighter liquid, higher rise: h ∝ 1/ρ.", "હલકું પ્રવાહી, વધુ ચઢાણ: h ∝ 1/ρ."),
                  ("Warmer liquid, lower rise because T falls with temperature.",
                   "ગરમ પ્રવાહી, ઓછું ચઢાણ કારણ કે T તાપમાન સાથે ઘટે."),
                  ("For water in glass cos θ ≈ 1, so h = 2T/(ρ g r).",
                   "કાચમાં પાણી માટે cos θ ≈ 1, તેથી h = 2T/(ρ g r).")),
               H4("Worked example", "ઉકેલાયેલ દાખલો"),
               P("Water (T = 0.072 N/m) in a tube of r = 0.2 mm: h = 2 × 0.072/(1000 × 9.8 × 2 × 10⁻⁴) "
                 "= 0.0735 m = 7.35 cm.",
                 "r = 0.2 mm ની નળીમાં પાણી (T = 0.072 N/m): h = 2 × 0.072/(1000 × 9.8 × 2 × 10⁻⁴) = "
                 "0.0735 m = 7.35 cm."),
               H4("Common mistake", "સામાન્ય ભૂલ"),
               P("Using the diameter for r. A 0.2 mm bore has r = 0.1 mm, which doubles the answer.",
                 "r માટે વ્યાસ વાપરવો. 0.2 mm બોરની r = 0.1 mm હોય, જે જવાબ બમણો કરે.")],
              syllabus_item="3.2.5"),
         card(T("3.2 Applications of surface tension",
                "3.2 પૃષ્ઠતાણના ઉપયોગો"),
              [H4("Where it is used deliberately", "જ્યાં તેનો ઉપયોગ થાય"),
               TB([T("Application", "ઉપયોગ"), T("How surface tension acts", "પૃષ્ઠતાણ કેવી રીતે કામ કરે")],
                  [[T("detergents and soap", "ડિટરજન્ટ અને સાબુ"), T("lower T so water wets the cloth and lifts grease", "T ઘટાડે જેથી પાણી કપડાને ભીનું કરી ચરબી ઉપાડે")],
                   [T("waterproofing and wax coating", "વોટરપ્રૂફિંગ અને મીણ કોટિંગ"), T("high contact angle keeps drops from spreading", "વધુ સંપર્ક કોણ ટીપાંને ફેલાવા દેતો નથી")],
                   [T("soldering and brazing", "સોલ્ડરિંગ અને બ્રેઝિંગ"), T("flux lowers T so solder wets the joint", "ફ્લક્સ T ઘટાડે જેથી સોલ્ડર જોડને ભીની કરે")],
                   [T("cooling-tower packing, wicks", "કૂલિંગ ટાવર પેકિંગ, વિક"), T("capillary rise spreads the liquid over the surface", "કેશનળી ચઢાણ પ્રવાહીને સપાટી પર ફેલાવે")],
                   [T("spray nozzles and paints", "સ્પ્રે નોઝલ અને પેન્ટ"), T("droplet size set by T and pressure", "ટીપાનું માપ T અને દબાણ નક્કી કરે")],
                   [T("anti-foam and emulsifiers", "એન્ટી-ફોમ અને ઇમલ્સિફાયર"), T("change T at interfaces to break or hold a foam", "ઇન્ટરફેસ પર T બદલીને ફોમ તોડે કે ટકાવે")]]),
               H4("Worked example", "ઉકેલાયેલ દાખલો"),
               P("A soap film on a frame is pulled flat by surface tension; adding soap to clean water "
                 "drops T from 0.072 to about 0.030 N/m, so the water penetrates a fabric instead of "
                 "beading on it.",
                 "ફ્રેમ પરનો સાબુનો પડ પૃષ્ઠતાણથી સપાટ ખેંચાય; સ્વચ્છ પાણીમાં સાબુ નાખતાં T 0.072 થી "
                 "લગભગ 0.030 N/m થાય, તેથી પાણી કાપડમાં ઊતરે, તેના પર ટીપાં ન બનાવે."),
               H4("Common mistake", "સામાન્ય ભૂલ"),
               P("Thinking detergents clean by 'bubbles'. They work because they lower the surface "
                 "tension and emulsify the grease.",
                 "ડિટરજન્ટ 'પરપોટા'થી સાફ કરે એમ માનવું. તે પૃષ્ઠતાણ ઘટાડીને ચરબીનું ઇમલ્શન બનાવે છે તેથી "
                 "કામ કરે.")],
              syllabus_item="3.2.7"),
         card(T("3.3 Effect of temperature and impurity",
                "3.3 તાપમાન અને અશુદ્ધિની અસર"),
              [H4("Rules", "નિયમો"),
               TB([T("Change", "ફેરફાર"), T("Effect on surface tension", "પૃષ્ઠતાણ પર અસર"), T("Example", "ઉદાહરણ")],
                  [[T("temperature rises", "તાપમાન વધે"), T("T falls, to zero at the critical point", "T ઘટે, ક્રાંતિક બિંદુએ શૂન્ય")],
                   [T("highly soluble impurity (salt, sugar)", "ખૂબ દ્રાવ્ય અશુદ્ધિ (મીઠું, ખાંડ)"), T("T increases slightly", "T થોડું વધે"), T("salt water", "ખારું પાણી")],
                   [T("sparingly soluble impurity (soap, detergent, oil)", "ઓછી દ્રાવ્ય અશુદ્ધિ (સાબુ, ડિટરજન્ટ, તેલ)"), T("T decreases sharply", "T ઝડપથી ઘટે"), T("soap solution", "સાબુનું દ્રાવણ")],
                   [T("dust or dirt on the surface", "સપાટી પર ધૂળ કે ગંદકી"), T("T falls, film weakens", "T ઘટે, પડ નબળો")]]),
               H4("Numbers worth remembering", "યાદ રાખવા જેવા આંકડા"),
               UL(("Water: 0.0756 N/m at 0 °C, 0.0728 at 20 °C, 0.0589 at 100 °C.",
                   "પાણી: 0 °C પર 0.0756 N/m, 20 °C પર 0.0728, 100 °C પર 0.0589."),
                  ("Mercury: about 0.465 N/m at 20 °C, the highest of the common liquids.",
                   "પારો: 20 °C પર લગભગ 0.465 N/m, સામાન્ય પ્રવાહીમાં સૌથી વધુ."),
                  ("A 0.1 % soap addition can halve the value — the reason a clean needle floats and "
                   "a soapy one sinks.", "0.1 % સાબુ ઉમેરવાથી મૂલ્ય અડધું થઈ શકે — તેથી જ સ્વચ્છ સોય તરે "
                   "અને સાબુવાળા પાણીમાં ડૂબે.")),
               H4("Engineering consequence", "ઇજનેરી પરિણામ"),
               P("In a boiler, a temperature rise lowers T and can also change θ, so the water film on "
                 "tubes changes from dropwise to filmwise condensation — a difference in heat-transfer "
                 "coefficient of several times.",
                 "બોઇલરમાં તાપમાન વધવાથી T ઘટે અને θ પણ બદલાય, તેથી ટ્યુબ પરનો પાણીનો પડ ટીપા-આકારમાંથી "
                 "ફિલ્મ-આકારમાં ફેરવાય — ઉષ્મા-સંક્રમણ ગુણાંકમાં ઘણા ગણો ફરક."),
               H4("Common mistake", "સામાન્ય ભૂલ"),
               P("Assuming every impurity raises T. Only highly soluble ones do; soap-like impurities "
                 "lower it.",
                 "દરેક અશુદ્ધિ T વધારે એમ માનવું. ફક્ત ખૂબ દ્રાવ્ય અશુદ્ધિઓ વધારે; સાબુ જેવી અશુદ્ધિઓ "
                 "ઘટાડે.")],
              syllabus_item="3.2.8"),
     ]},

    {"title": T("4. Viscosity", "4. શ્યાનતા"),
     "items": [
         card(T("4.1 Viscosity: the concept and its units",
                "4.1 શ્યાનતા: ખ્યાલ અને એકમો"),
              [H4("Definition", "વ્યાખ્યા"),
               P("<b>Viscosity</b> is the internal friction of a fluid that opposes the relative "
                 "motion of its layers. A fluid at rest has no shear stress, but the moment one layer "
                 "slides over another the friction appears.",
                 "<b>શ્યાનતા</b> એ પ્રવાહીનું આંતરિક ઘર્ષણ છે જે તેના સ્તરોની સાપેક્ષ ગતિનો વિરોધ કરે. "
                 "સ્થિર પ્રવાહીમાં શિયર પ્રતિબળ હોતું નથી, પણ એક સ્તર બીજા પર સરકે ત્યાં જ ઘર્ષણ ઊભું થાય."),
               H4("Units and typical values", "એકમ અને સામાન્ય મૂલ્યો"),
               P("The SI unit of the coefficient is N·s/m² = Pa·s; the CGS unit is the poise, and "
                 "1 Pa·s = 10 poise. Water is the reference thin fluid at about 1 mPa·s.",
                 "ગુણાંકનો SI એકમ N·s/m² = Pa·s છે; CGS એકમ પોઇઝ, અને 1 Pa·s = 10 પોઇઝ. પાણી લગભગ "
                 "1 mPa·s સાથે પાતળા પ્રવાહીનો સંદર્ભ છે."),
               TB([T("Fluid at 20 °C", "20 °C પર પ્રવાહી"), T("η in Pa·s", "η Pa·s માં")],
                  [[T("air", "હવા"), T("1.8 × 10⁻⁵", "1.8 × 10⁻⁵")],
                   [T("water", "પાણી"), T("1.0 × 10⁻³", "1.0 × 10⁻³")],
                   [T("kerosene", "કેરોસીન"), T("1.6 × 10⁻³", "1.6 × 10⁻³")],
                   [T("engine oil (SAE 30)", "એન્જિન ઓઇલ (SAE 30)"), T("0.20–0.30", "0.20–0.30")],
                   [T("glycerine", "ગ્લિસરિન"), T("0.83", "0.83")],
                   [T("honey", "મધ"), T("2–10", "2–10")]]),
               H4("What it means for a machine", "મશીન માટે તેનો અર્થ"),
               P("Viscosity decides whether a fluid can carry a load on a film (bearing), how fast a "
                 "ball settles (Stokes' law), and how much pressure a pump must supply (pipe flow).",
                 "શ્યાનતા નક્કી કરે કે પ્રવાહી પડ પર ભાર ઉપાડી શકે (બેરિંગ), દડો કેટલી ઝડપથી બેસે "
                 "(સ્ટોક્સનો નિયમ), અને પંપે કેટલું દબાણ આપવું પડે (નળીનો પ્રવાહ)."),
               H4("Common mistake", "સામાન્ય ભૂલ"),
               P("Confusing viscosity with density. Mercury is dense yet thin, honey is dense and "
                 "viscous, and air is light and thin.",
                 "શ્યાનતાને ઘનતા સાથે ભેગી કરવી. પારો ભારે છતાં પાતળો, મધ ભારે અને શ્યાન, અને હવા હલકી "
                 "તથા પાતળી છે.")],
              "u3_viscosity", syllabus_item="3.3.1"),
         card(T("4.2 Newton's law of viscosity",
                "4.2 ન્યૂટનનો શ્યાનતાનો નિયમ"),
              [H4("Statement", "વિધાન"),
               P("The viscous force between two layers of a fluid is directly proportional to the area "
                 "of contact and to the velocity gradient between them: <b>F = −η A (dv/dx)</b>. The "
                 "minus sign shows that the force opposes the motion.",
                 "પ્રવાહીના બે સ્તરો વચ્ચેનું શ્યાન બળ તેમના સંપર્ક ક્ષેત્રફળ અને વેગ પ્રવણતાના સીધા "
                 "સમપ્રમાણમાં છે: <b>F = −η A (dv/dx)</b>. ઋણ ચિહ્ન દર્શાવે કે બળ ગતિનો વિરોધ કરે છે."),
               H4("Coefficient of viscosity", "શ્યાનતા ગુણાંક"),
               P("Rearranged, η = F/(A dv/dx): the force per unit area needed to maintain unit velocity "
                 "gradient. It is a property of the fluid and depends strongly on temperature.",
                 "ગોઠવતાં η = F/(A dv/dx): એકમ વેગ પ્રવણતા જાળવવા એકમ ક્ષેત્રફળ દીઠ જરૂરી બળ. તે પ્રવાહીનો "
                 "ગુણધર્મ છે અને તાપમાન પર ખૂબ આધાર રાખે છે."),
               H4("Worked example", "ઉકેલાયેલ દાખલો"),
               P("A 2 mm oil film with the top plate at 0.5 m/s: dv/dx = 250 s⁻¹. With η = 1.0 Pa·s and "
                 "A = 0.5 m², F = 125 N — the force needed to keep the plate moving.",
                 "2 mm તેલના પડમાં ઉપરની પ્લેટ 0.5 m/s પર: dv/dx = 250 s⁻¹. η = 1.0 Pa·s અને A = 0.5 m² "
                 "સાથે F = 125 N — પ્લેટ ચલાવવા જરૂરી બળ."),
               H4("Conditions", "શરતો"),
               P("The law holds for Newtonian fluids — water, air, oil — in laminar flow. A "
                 "non-Newtonian fluid such as paint, blood or toothpaste does not obey it, because its "
                 "η itself changes with the velocity gradient.",
                 "નિયમ ન્યૂટનીય પ્રવાહી — પાણી, હવા, તેલ — માટે સ્તરીય પ્રવાહમાં લાગુ પડે. પેન્ટ, લોહી કે "
                 "ટૂથપેસ્ટ જેવું અન્ય ન્યૂટનીય પ્રવાહી તેનું પાલન કરતું નથી, કારણ કે તેનો η પ્રવણતા સાથે બદલાય."),
               H4("Common mistake", "સામાન્ય ભૂલ"),
               P("Applying the law in turbulent flow. Once eddies form, momentum transfer is dominated "
                 "by mixing and the measured stress is far above η dv/dx.",
                 "વમળીય પ્રવાહમાં નિયમ લગાડવો. વમળ બન્યા પછી વેગમાન સ્થાનાંતરણ મિશ્રણથી થાય અને મપાયેલું "
                 "પ્રતિબળ η dv/dx થી ઘણું ઊંચું હોય.")],
              syllabus_item="3.3.2"),
         card(T("4.3 Viscous force, velocity gradient and the coefficient",
                "4.3 શ્યાન બળ, વેગ પ્રવણતા અને ગુણાંક"),
              [H4("The three quantities", "ત્રણ રાશિઓ"),
               TB([T("Quantity", "રાશિ"), T("Meaning", "અર્થ"), T("Unit", "એકમ")],
                  [[T("viscous force F", "શ્યાન બળ F"), T("drag between two layers", "બે સ્તરો વચ્ચેનો ખેંચાણ"), T("N", "N")],
                   [T("velocity gradient dv/dx", "વેગ પ્રવણતા dv/dx"), T("how fast the speed changes across the gap", "જગ્યા સાથે ઝડપ કેટલી ઝડપથી બદલાય"), T("s⁻¹", "s⁻¹")],
                   [T("coefficient η", "ગુણાંક η"), T("viscous force per unit area per unit gradient", "એકમ ક્ષેત્રફળ અને એકમ પ્રવણતા દીઠ શ્યાન બળ"), T("Pa·s", "Pa·s")]]),
               H4("What the gradient means in a pipe", "નળીમાં પ્રવણતાનો અર્થ"),
               P("The fluid at the wall is at rest and the fluid at the axis moves fastest, so the "
                 "velocity profile is a parabola and dv/dx is largest at the wall — that is where the "
                 "shear and the erosion are worst.",
                 "દીવાલ પાસે પ્રવાહી સ્થિર અને ધરી પાસે સૌથી ઝડપી હોય, તેથી વેગની રૂપરેખા પરવલય બને અને "
                 "dv/dx દીવાલ પાસે સૌથી વધુ હોય — ત્યાં જ શિયર અને ઘસારો સૌથી વધુ થાય."),
               H4("Worked example", "ઉકેલાયેલ દાખલો"),
               P("Two layers 1 mm apart with speeds differing by 0.2 m/s: dv/dx = 200 s⁻¹. If "
                 "η = 0.5 Pa·s, the shear stress is τ = η dv/dx = 100 N/m².",
                 "1 mm દૂરના બે સ્તરોની ઝડપમાં 0.2 m/s ફરક: dv/dx = 200 s⁻¹. η = 0.5 Pa·s હોય તો શિયર "
                 "પ્રતિબળ τ = η dv/dx = 100 N/m²."),
               H4("Common mistake", "સામાન્ય ભૂલ"),
               P("Taking the gradient as v/η or v·x. It is Δv/Δx: speed divided by distance, not by "
                 "viscosity.",
                 "પ્રવણતાને v/η કે v·x લેવી. તે Δv/Δx છે: ઝડપ ભાગ્યા અંતર, શ્યાનતા નહીં.")],
              syllabus_item="3.3.3"),
         card(T("4.4 Streamline and turbulent flow, critical velocity and Reynolds number",
                "4.4 સ્તરીય અને વમળીય પ્રવાહ, ક્રાંતિક વેગ અને રેનોલ્ડ્સ આંક"),
              [H4("Two kinds of flow", "બે પ્રકારના પ્રવાહ"),
               TB([T("Streamline (laminar)", "સ્તરીય"), T("Turbulent", "વમળીય")],
                  [[T("layers slide without mixing", "સ્તરો ભળ્યા વગર સરકે"), T("eddies and mixing across the pipe", "વમળ અને નળીમાં આડું મિશ્રણ")],
                   [T("velocity below the critical value", "વેગ ક્રાંતિક મૂલ્યથી નીચે"), T("velocity above it", "તેનાથી ઉપર")],
                   [T("low energy loss, quiet", "ઓછી ઊર્જા ખોટ, શાંત"), T("loss rises sharply, noisy", "ખોટ ઝડપથી વધે, ઘોંઘાટ")],
                   [T("Re below about 2000", "Re લગભગ 2000થી નીચે"), T("Re above about 4000", "Re લગભગ 4000થી ઉપર")]]),
               H4("The Reynolds number", "રેનોલ્ડ્સ આંક"),
               P("<b>Re = ρ v d / η</b>, a pure number. Below about 2000 the flow is streamline, above "
                 "about 4000 it is turbulent, and in between it is transitional.",
                 "<b>Re = ρ v d / η</b>, પરિમાણરહિત આંક. લગભગ 2000થી નીચે પ્રવાહ સ્તરીય, લગભગ 4000થી ઉપર "
                 "વમળીય, અને વચ્ચે સંક્રમણાવસ્થામાં."),
               H4("Critical velocity", "ક્રાંતિક વેગ"),
               P("v<sub>c</sub> = Re η/(ρ d). For water in a 50 mm pipe with Re = 2000: "
                 "v<sub>c</sub> = 2000 × 10⁻³/(1000 × 0.05) = 0.04 m/s.",
                 "v<sub>c</sub> = Re η/(ρ d). 50 mm નળીમાં પાણી માટે Re = 2000 સાથે: "
                 "v<sub>c</sub> = 2000 × 10⁻³/(1000 × 0.05) = 0.04 m/s."),
               H4("Engineering reading", "ઇજનેરી અર્થઘટન"),
               P("Pipes are sized to stay below Re ≈ 2000 where possible, because turbulent loss "
                 "rises roughly as v², and pumps are chosen for that pressure drop.",
                 "શક્ય હોય ત્યાં સુધી નળીઓ Re ≈ 2000થી નીચે રખાય, કારણ કે વમળીય ખોટ લગભગ v² પ્રમાણે "
                 "વધે, અને પંપ તે દબાણ ઘટાડા માટે પસંદ કરાય."),
               H4("Common mistake", "સામાન્ય ભૂલ"),
               P("Using the radius in Re instead of the diameter. Every textbook value (2000, 4000) is "
                 "defined on the diameter.",
                 "Re માં વ્યાસને બદલે ત્રિજ્યા વાપરવી. દરેક પુસ્તકનું મૂલ્ય (2000, 4000) વ્યાસ પર "
                 "વ્યાખ્યાયિત છે.")],
              syllabus_item="3.3.4"),
         card(T("4.5 Stokes' law and terminal velocity",
                "4.5 સ્ટોક્સનો નિયમ અને અંતિમ વેગ"),
              [H4("Stokes' law", "સ્ટોક્સનો નિયમ"),
               P("A small sphere of radius r falling slowly through a fluid of viscosity η feels a "
                 "retarding force <b>F = 6π η r v</b>. It holds for a smooth sphere, slow steady motion "
                 "and no turbulence.",
                 "શ્યાનતા η વાળા પ્રવાહીમાં ધીમે પડતા r ત્રિજ્યાના નાના ગોળા પર પ્રતિરોધક બળ "
                 "<b>F = 6π η r v</b> લાગે. તે સરખા ગોળા, ધીમી સ્થિર ગતિ અને વમળ વગર માટે માન્ય છે."),
               H4("Terminal velocity", "અંતિમ વેગ"),
               P("When weight equals upthrust plus viscous drag the acceleration is zero and the sphere "
                 "falls at a constant terminal velocity: <b>v<sub>t</sub> = 2r²(ρ − σ)g/(9η)</b>, where "
                 "ρ is the sphere's density and σ the fluid's.",
                 "જ્યારે વજન = ઉત્પ્લાવક બળ + શ્યાન પ્રતિરોધ થાય ત્યારે પ્રવર્ગ શૂન્ય થાય અને ગોળો અચળ "
                 "અંતિમ વેગથી પડે: <b>v<sub>t</sub> = 2r²(ρ − σ)g/(9η)</b>, જ્યાં ρ ગોળાની અને σ પ્રવાહીની "
                 "ઘનતા છે."),
               TB([T("Dependence", "આધાર"), T("Effect", "અસર")],
                  [[T("bigger radius", "મોટી ત્રિજ્યા"), T("falls much faster: v ∝ r²", "ઘણું ઝડપથી પડે: v ∝ r²")],
                   [T("thicker fluid", "જાડું પ્રવાહી"), T("falls slower: v ∝ 1/η", "ધીમે પડે: v ∝ 1/η")],
                   [T("denser sphere", "ઘન ગોળો"), T("falls faster: v ∝ (ρ − σ)", "ઝડપથી પડે: v ∝ (ρ − σ)")],
                   [T("equal densities", "સમાન ઘનતા"), T("never falls, it stays suspended", "કદી ન પડે, સ્થિર રહે")]]),
               H4("Worked example", "ઉકેલાયેલ દાખલો"),
               P("A steel ball of r = 1 mm (ρ = 7800) in glycerine (σ = 1260, η = 0.83): "
                 "v<sub>t</sub> = 2 × 10⁻⁶ × 6540 × 9.8/(9 × 0.83) = 1.7 × 10⁻² m/s = 1.7 cm/s.",
                 "ગ્લિસરિન (σ = 1260, η = 0.83) માં r = 1 mm નો સ્ટીલ દડો (ρ = 7800): "
                 "v<sub>t</sub> = 2 × 10⁻⁶ × 6540 × 9.8/(9 × 0.83) = 1.7 × 10⁻² m/s = 1.7 cm/s."),
               H4("Common mistake", "સામાન્ય ભૂલ"),
               P("Forgetting the buoyancy term (ρ − σ) and using ρ alone. A ball of the same density as "
                 "the fluid never reaches a terminal velocity at all.",
                 "ઉત્પ્લાવકતાનું પદ (ρ − σ) ભૂલીને ફક્ત ρ વાપરવું. પ્રવાહી જેટલી જ ઘનતાવાળો દડો અંતિમ "
                 "વેગ સુધી પહોંચતો જ નથી.")],
              syllabus_item="3.3.5"),
         card(T("4.6 Effect of temperature and the use of viscosity in bearings",
                "4.6 તાપમાનની અસર અને બેરિંગમાં શ્યાનતાનો ઉપયોગ"),
              [H4("Temperature", "તાપમાન"),
               P("Viscosity of <b>liquids falls</b> as temperature rises, because molecules slip past "
                 "each other more easily. Viscosity of <b>gases rises</b>, because the momentum "
                 "transfer between faster molecules increases.",
                 "તાપમાન વધે તેમ <b>પ્રવાહીની શ્યાનતા ઘટે</b>, કારણ કે અણુઓ એકબીજા પરથી સહેલાઈથી સરકે. "
                 "<b>વાયુની શ્યાનતા વધે</b>, કારણ કે ઝડપી અણુઓ વચ્ચે વેગમાનનું સ્થાનાંતરણ વધે."),
               TB([T("Fluid", "પ્રવાહી"), T("20 °C", "20 °C"), T("40 °C", "40 °C"), T("100 °C", "100 °C")],
                  [[T("water (mPa·s)", "પાણી (mPa·s)"), T("1.00", "1.00"), T("0.65", "0.65"), T("0.28", "0.28")],
                   [T("engine oil (Pa·s)", "એન્જિન ઓઇલ (Pa·s)"), T("0.25", "0.25"), T("0.08", "0.08"), T("0.01", "0.01")]]),
               H4("Why a bearing needs the right grade", "બેરિંગને યોગ્ય ગ્રેડ કેમ જોઈએ"),
               UL(("Too thick: the oil cannot enter the clearance, the shaft runs on metal and wears.",
                   "બહુ જાડું: તેલ ગેપમાં જઈ શકતું નથી, શાફ્ટ ધાતુ પર ચાલે અને ઘસાય."),
                  ("Too thin: the film collapses under load and the surfaces touch.",
                   "બહુ પાતળું: ભાર હેઠળ પડ પડી જાય અને સપાટીઓ અડે."),
                  ("A multigrade oil keeps the grade nearly constant from cold start to running "
                   "temperature, which is why 20W-40 is specified instead of a single grade.",
                   "મલ્ટીગ્રેડ તેલ ઠંડા સ્ટાર્ટથી ચાલુ તાપમાન સુધી ગ્રેડ લગભગ અચળ રાખે, તેથી જ એક જ "
                   "ગ્રેડને બદલે 20W-40 સૂચવાય.")),
               H4("Worked example", "ઉકેલાયેલ દાખલો"),
               P("Engine oil at 0.25 Pa·s drags a 0.02 m² bearing surface at 5 m/s across a 0.05 mm film: "
                 "F = η A v/x = 0.25 × 0.02 × 5/5 × 10⁻⁵ = 500 N — the friction the pump must overcome.",
                 "0.25 Pa·s નું એન્જિન ઓઇલ 0.02 m² બેરિંગ સપાટીને 0.05 mm ફિલ્મમાં 5 m/s પર ખેંચે: "
                 "F = η A v/x = 0.25 × 0.02 × 5/5 × 10⁻⁵ = 500 N — પંપે એ ઘર્ષણ દૂર કરવું પડે."),
               H4("Common mistake", "સામાન્ય ભૂલ"),
               P("Assuming every fluid thins on heating. Air and steam thicken, which changes the "
                 "design of a gas bearing completely.",
                 "દરેક પ્રવાહી ગરમ થતાં પાતળું થાય એમ માનવું. હવા અને વરાળ જાડાં થાય છે, જે ગેસ બેરિંગની "
                 "રચના સાવ બદલી નાખે.")],
              syllabus_item="3.3.6"),
     ]},

    {"title": T("5. Practice Questions with Model Answers", "5. સરાવ પ્રશ્નો અને આદર્શ જવાબો"),
     "items": []},
]

NUMERICALS = [
    num("u3n01", T("Stress in a wire carrying 100 N over 2 mm².",
                   "2 mm² પર 100 N વહેતા તારમાં પ્રતિબળ."),
        T("A wire of cross-section 2 mm² carries a load of 100 N. Find the stress.",
          "2 mm² કાપવાળો તાર 100 N ભાર લે છે. પ્રતિબળ શોધો."),
        [P("A = 2 mm² = 2 × 10⁻⁶ m²", "A = 2 mm² = 2 × 10⁻⁶ m²"),
         P("σ = F/A = 100/(2 × 10⁻⁶)", "σ = F/A = 100/(2 × 10⁻⁶)"),
         P("= 5 × 10⁷ N/m² = 50 MPa", "= 5 × 10⁷ N/m² = 50 MPa")],
        T("5 × 10⁷ N/m² (50 MPa)", "5 × 10⁷ N/m² (50 MPa)"), unit_no=3),
    num("u3n02", T("Strain when a 2 m wire stretches 0.5 mm.",
                   "2 m તાર 0.5 mm ખેંચાય ત્યારે વિકૃતિ."),
        T("A wire 2 m long stretches by 0.5 mm. Find the strain.",
          "2 m લાંબો તાર 0.5 mm ખેંચાય છે. વિકૃતિ શોધો."),
        [P("ΔL = 0.5 mm = 5 × 10⁻⁴ m", "ΔL = 0.5 mm = 5 × 10⁻⁴ m"),
         P("ε = ΔL/L = 5 × 10⁻⁴/2", "ε = ΔL/L = 5 × 10⁻⁴/2"),
         P("= 2.5 × 10⁻⁴ (no unit)", "= 2.5 × 10⁻⁴ (એકમ નહીં)")],
        T("2.5 × 10⁻⁴", "2.5 × 10⁻⁴"), unit_no=3),
    num("u3n03", T("Young's modulus from stress and strain.",
                   "પ્રતિબળ અને વિકૃતિ પરથી યંગ ગુણાંક."),
        T("A material shows a stress of 5 × 10⁷ N/m² at a strain of 2.5 × 10⁻⁴. Find its Young's "
          "modulus.", "પદાર્થમાં 2.5 × 10⁻⁴ વિકૃતિ પર પ્રતિબળ 5 × 10⁷ N/m² છે. તેનો યંગ ગુણાંક શોધો."),
        [P("Y = σ/ε = 5 × 10⁷ / 2.5 × 10⁻⁴", "Y = σ/ε = 5 × 10⁷ / 2.5 × 10⁻⁴"),
         P("= 2 × 10¹¹ N/m²", "= 2 × 10¹¹ N/m²"),
         P("That is the value for steel.", "આ સ્ટીલનું મૂલ્ય છે.")],
        T("2 × 10¹¹ N/m²", "2 × 10¹¹ N/m²"), unit_no=3),
    num("u3n04", T("Extension of a steel wire: 50 N, 2 m, 1 mm².",
                   "સ્ટીલ તારનું ખેંચાણ: 50 N, 2 m, 1 mm²."),
        T("A steel wire of length 2 m and area 1 mm² (Y = 2 × 10¹¹ N/m²) carries 50 N. Find the "
          "extension.", "2 m લંબાઈ અને 1 mm² કાપવાળો સ્ટીલ તાર (Y = 2 × 10¹¹ N/m²) 50 N લે છે. ખેંચાણ શોધો."),
        [P("ΔL = F L/(A Y)", "ΔL = F L/(A Y)"),
         P("= 50 × 2/(10⁻⁶ × 2 × 10¹¹)", "= 50 × 2/(10⁻⁶ × 2 × 10¹¹)"),
         P("= 100/(2 × 10⁵) = 5 × 10⁻⁴ m = 0.5 mm", "= 100/(2 × 10⁵) = 5 × 10⁻⁴ m = 0.5 mm")],
        T("0.5 mm", "0.5 mm"), unit_no=3),
    num("u3n05", T("Bulk modulus from a pressure change.",
                   "દબાણના ફેરફાર પરથી બલ્ક ગુણાંક."),
        T("A liquid suffers a volume change of 5 × 10⁻⁵ of its volume when the pressure rises by "
          "10⁵ Pa. Find its bulk modulus.",
          "દબાણ 10⁵ Pa વધતાં પ્રવાહીના ઘનફળમાં 5 × 10⁻⁵ ફેરફાર થાય છે. તેનો બલ્ક ગુણાંક શોધો."),
        [P("K = ΔP/(ΔV/V)", "K = ΔP/(ΔV/V)"),
         P("= 10⁵/(5 × 10⁻⁵)", "= 10⁵/(5 × 10⁻⁵)"),
         P("= 2 × 10⁹ N/m²", "= 2 × 10⁹ N/m²")],
        T("2 × 10⁹ N/m²", "2 × 10⁹ N/m²"), unit_no=3),
    num("u3n06", T("Shear modulus of a block displaced 0.5 mm.",
                   "0.5 mm ખસેડાયેલા બ્લોકનો શિયર ગુણાંક."),
        T("A tangential force of 500 N acts on the top face (0.01 m²) of a block 5 mm thick and "
          "displaces it by 0.5 mm. Find the shear modulus.",
          "5 mm જાડા બ્લોકની ઉપરની સપાટી (0.01 m²) પર 500 N સ્પર્શીય બળ લાગે અને તે 0.5 mm ખસે છે. "
          "શિયર ગુણાંક શોધો."),
        [P("Shear stress = 500/0.01 = 5 × 10⁴ N/m²", "શિયર પ્રતિબળ = 500/0.01 = 5 × 10⁴ N/m²"),
         P("Shear strain = 0.5/5 = 0.1", "શિયર વિકૃતિ = 0.5/5 = 0.1"),
         P("G = 5 × 10⁴/0.1 = 5 × 10⁵ N/m²", "G = 5 × 10⁴/0.1 = 5 × 10⁵ N/m²")],
        T("5 × 10⁵ N/m²", "5 × 10⁵ N/m²"), unit_no=3),
    num("u3n07", T("Energy stored in a stretched wire.",
                   "ખેંચાયેલા તારમાં સંગ્રહાયેલી ઊર્જા."),
        T("A wire is stretched by 0.5 mm by a force rising to 50 N. Find the energy stored.",
          "તાર 0.5 mm ખેંચાય છે અને બળ 50 N સુધી પહોંચે છે. સંગ્રહાયેલી ઊર્જા શોધો."),
        [P("U = ½ F ΔL", "U = ½ F ΔL"),
         P("= ½ × 50 × 5 × 10⁻⁴", "= ½ × 50 × 5 × 10⁻⁴"),
         P("= 1.25 × 10⁻² J", "= 1.25 × 10⁻² J")],
        T("1.25 × 10⁻² J", "1.25 × 10⁻² J"), unit_no=3),
    num("u3n08", T("Force on a sliding wire with a soap film.",
                   "સાબુના પડ સાથે સરકતા તાર પર બળ."),
        T("A soap film of surface tension 0.025 N/m is held on a frame with a 10 cm sliding wire. "
          "Find the force on the wire.", "0.025 N/m પૃષ્ઠતાણવાળો સાબુનો પડ 10 cm સરકતા તારવાળી ફ્રેમ પર "
          "છે. તાર પરનું બળ શોધો."),
        [P("A film has two surfaces, so F = 2 T L", "પડને બે સપાટી હોય, તેથી F = 2 T L"),
         P("= 2 × 0.025 × 0.1", "= 2 × 0.025 × 0.1"),
         P("= 5 × 10⁻³ N", "= 5 × 10⁻³ N")],
        T("5 × 10⁻³ N", "5 × 10⁻³ N"), unit_no=3),
    num("u3n09", T("Capillary rise of water in a 0.2 mm tube.",
                   "0.2 mm નળીમાં પાણીનું કેશનળી ચઢાણ."),
        T("Find the height to which water (T = 0.072 N/m, θ = 0°) rises in a capillary of radius "
          "0.2 mm.", "r = 0.2 mm ત્રિજ્યાની કેશનળીમાં પાણી (T = 0.072 N/m, θ = 0°) કેટલી ઊંચાઈ સુધી "
          "ચઢે તે શોધો."),
        [P("h = 2T cos θ/(ρ g r)", "h = 2T cos θ/(ρ g r)"),
         P("= 2 × 0.072 × 1/(1000 × 9.8 × 2 × 10⁻⁴)", "= 2 × 0.072 × 1/(1000 × 9.8 × 2 × 10⁻⁴)"),
         P("= 0.144/1.96 = 0.0735 m", "= 0.144/1.96 = 0.0735 m")],
        T("7.35 cm", "7.35 cm"), unit_no=3),
    num("u3n10", T("Radius of a tube from a 5 cm rise.",
                   "5 cm ચઢાણ પરથી નળીની ત્રિજ્યા."),
        T("Water rises 5 cm in a capillary. Find the radius of the tube (T = 0.072 N/m, θ = 0°).",
          "કેશનળીમાં પાણી 5 cm ચઢે છે. નળીની ત્રિજ્યા શોધો (T = 0.072 N/m, θ = 0°)."),
        [P("r = 2T/(ρ g h)", "r = 2T/(ρ g h)"),
         P("= 0.144/(1000 × 9.8 × 0.05)", "= 0.144/(1000 × 9.8 × 0.05)"),
         P("= 0.144/490 = 2.94 × 10⁻⁴ m", "= 0.144/490 = 2.94 × 10⁻⁴ m")],
        T("2.94 × 10⁻⁴ m (0.29 mm)", "2.94 × 10⁻⁴ m (0.29 mm)"), unit_no=3),
    num("u3n11", T("Surface tension from a 6 cm rise in a 0.25 mm tube.",
                   "0.25 mm નળીમાં 6 cm ચઢાણ પરથી પૃષ્ઠતાણ."),
        T("Water rises 6 cm in a tube of radius 0.25 mm. Find the surface tension (θ = 0°).",
          "0.25 mm ત્રિજ્યાની નળીમાં પાણી 6 cm ચઢે છે. પૃષ્ઠતાણ શોધો (θ = 0°)."),
        [P("T = ρ g h r/2", "T = ρ g h r/2"),
         P("= 1000 × 9.8 × 0.06 × 2.5 × 10⁻⁴/2", "= 1000 × 9.8 × 0.06 × 2.5 × 10⁻⁴/2"),
         P("= 0.147/2 = 0.0735 N/m", "= 0.147/2 = 0.0735 N/m")],
        T("0.0735 N/m", "0.0735 N/m"), unit_no=3),
    num("u3n12", T("Excess pressure inside a soap bubble.",
                   "સાબુના પરપોટા અંદર વધારાનું દબાણ."),
        T("Find the excess pressure inside a soap bubble of radius 2 cm with T = 0.025 N/m.",
          "T = 0.025 N/m સાથે 2 cm ત્રિજ્યાના સાબુના પરપોટા અંદરનું વધારાનું દબાણ શોધો."),
        [P("For a bubble with two surfaces, p = 4T/r", "બે સપાટીવાળા પરપોટા માટે p = 4T/r"),
         P("= 4 × 0.025/0.02", "= 4 × 0.025/0.02"),
         P("= 5 Pa", "= 5 Pa")],
        T("5 Pa", "5 Pa"), unit_no=3),
    num("u3n13", T("Velocity gradient in an oil film.",
                   "તેલના પડમાં વેગ પ્રવણતા."),
        T("The top plate of an oil film 2 mm thick moves at 0.5 m/s while the bottom plate is fixed. "
          "Find the velocity gradient and the viscous force with η = 1.0 Pa·s and A = 0.5 m².",
          "2 mm જાડા તેલ પડની ઉપરની પ્લેટ 0.5 m/s પર ચાલે અને નીચેની સ્થિર છે. વેગ પ્રવણતા અને "
          "η = 1.0 Pa·s તથા A = 0.5 m² સાથે શ્યાન બળ શોધો."),
        [P("dv/dx = 0.5/0.002 = 250 s⁻¹", "dv/dx = 0.5/0.002 = 250 s⁻¹"),
         P("F = η A dv/dx", "F = η A dv/dx"),
         P("= 1.0 × 0.5 × 250 = 125 N", "= 1.0 × 0.5 × 250 = 125 N")],
        T("250 s⁻¹ and 125 N", "250 s⁻¹ અને 125 N"), unit_no=3),
    num("u3n14", T("Terminal velocity of a steel ball in glycerine.",
                   "ગ્લિસરિનમાં સ્ટીલના દડાનો અંતિમ વેગ."),
        T("A steel ball of radius 1 mm (ρ = 7800 kg/m³) falls in glycerine (σ = 1260 kg/m³, "
          "η = 0.83 Pa·s). Find the terminal velocity.",
          "1 mm ત્રિજ્યાનો સ્ટીલ દડો (ρ = 7800 kg/m³) ગ્લિસરિન (σ = 1260 kg/m³, η = 0.83 Pa·s)માં પડે છે. "
          "અંતિમ વેગ શોધો."),
        [P("v = 2r²(ρ − σ)g/(9η)", "v = 2r²(ρ − σ)g/(9η)"),
         P("= 2 × 10⁻⁶ × 6540 × 9.8/(9 × 0.83)", "= 2 × 10⁻⁶ × 6540 × 9.8/(9 × 0.83)"),
         P("= 0.1282/7.47 = 1.72 × 10⁻² m/s", "= 0.1282/7.47 = 1.72 × 10⁻² m/s")],
        T("1.72 × 10⁻² m/s (1.7 cm/s)", "1.72 × 10⁻² m/s (1.7 cm/s)"), unit_no=3),
    num("u3n15", T("Viscosity from a measured terminal velocity.",
                   "માપેલા અંતિમ વેગ પરથી શ્યાનતા."),
        T("A ball of radius 2 mm (ρ = 7800 kg/m³) falls at a steady 0.10 m/s in glycerine of density "
          "1260 kg/m³. Find the viscosity.", "2 mm ત્રિજ્યાનો દડો (ρ = 7800 kg/m³) 1260 kg/m³ ઘનતાવાળા "
          "ગ્લિસરિનમાં 0.10 m/s ના અચળ વેગથી પડે છે. શ્યાનતા શોધો."),
        [P("η = 2r²(ρ − σ)g/(9v)", "η = 2r²(ρ − σ)g/(9v)"),
         P("= 2 × 4 × 10⁻⁶ × 6540 × 9.8/(9 × 0.10)", "= 2 × 4 × 10⁻⁶ × 6540 × 9.8/(9 × 0.10)"),
         P("= 0.5127/0.9 = 0.57 Pa·s", "= 0.5127/0.9 = 0.57 Pa·s")],
        T("0.57 Pa·s", "0.57 Pa·s"), unit_no=3),
    num("u3n16", T("Reynolds number of water in a 50 mm pipe.",
                   "50 mm નળીમાં પાણીનો રેનોલ્ડ્સ આંક."),
        T("Water (ρ = 1000 kg/m³, η = 10⁻³ Pa·s) flows at 2 m/s in a pipe of diameter 50 mm. Find Re and "
          "state the type of flow.", "પાણી (ρ = 1000 kg/m³, η = 10⁻³ Pa·s) 50 mm વ્યાસની નળીમાં 2 m/s પર "
          "વહે છે. Re શોધો અને પ્રવાહનો પ્રકાર જણાવો."),
        [P("Re = ρ v d/η", "Re = ρ v d/η"),
         P("= 1000 × 2 × 0.05/10⁻³", "= 1000 × 2 × 0.05/10⁻³"),
         P("= 10⁵, far above 4000, so the flow is turbulent", "= 10⁵, 4000થી ઘણું ઉપર, તેથી પ્રવાહ વમળીય છે")],
        T("Re = 10⁵, turbulent", "Re = 10⁵, વમળીય"), unit_no=3),
    num("u3n17", T("Critical velocity for Re = 2000.",
                   "Re = 2000 માટે ક્રાંતિક વેગ."),
        T("For water in a 50 mm pipe, find the critical velocity at Re = 2000.",
          "50 mm નળીમાં પાણી માટે Re = 2000 પર ક્રાંતિક વેગ શોધો."),
        [P("v_c = Re η/(ρ d)", "v_c = Re η/(ρ d)"),
         P("= 2000 × 10⁻³/(1000 × 0.05)", "= 2000 × 10⁻³/(1000 × 0.05)"),
         P("= 2/50 = 0.04 m/s", "= 2/50 = 0.04 m/s")],
        T("0.04 m/s", "0.04 m/s"), unit_no=3),
    num("u3n18", T("Spring constant from an extension.",
                   "ખેંચાણ પરથી સ્પ્રિંગ અચળાંક."),
        T("A spring extends 2 cm under a load of 10 N. Find its force constant and the extension under "
          "25 N.", "સ્પ્રિંગ 10 N ભાર હેઠળ 2 cm ખેંચાય છે. તેનો બળ અચળાંક અને 25 N હેઠળ ખેંચાણ શોધો."),
        [P("k = F/x = 10/0.02 = 500 N/m", "k = F/x = 10/0.02 = 500 N/m"),
         P("x = F/k = 25/500", "x = F/k = 25/500"),
         P("= 0.05 m = 5 cm", "= 0.05 m = 5 cm")],
        T("500 N/m and 5 cm", "500 N/m અને 5 cm"), unit_no=3),
    num("u3n19", T("Pressure needed to make a 1 mm water drop.",
                   "1 mm પાણીના ટીપા માટે જરૂરી દબાણ."),
        T("Find the excess pressure inside a water drop of radius 1 mm (T = 0.072 N/m).",
          "1 mm ત્રિજ્યાના પાણીના ટીપા અંદરનું વધારાનું દબાણ શોધો (T = 0.072 N/m)."),
        [P("A drop has one surface, so p = 2T/r", "ટીપાને એક સપાટી હોય, તેથી p = 2T/r"),
         P("= 2 × 0.072/10⁻³", "= 2 × 0.072/10⁻³"),
         P("= 144 Pa", "= 144 Pa")],
        T("144 Pa", "144 Pa"), unit_no=3),
    num("u3n20", T("Bearing friction in an oil film.",
                   "તેલના પડમાં બેરિંગનું ઘર્ષણ."),
        T("A bearing surface of 0.02 m² moves at 5 m/s over an oil film 0.05 mm thick with "
          "η = 0.25 Pa·s. Find the viscous force.",
          "0.02 m² બેરિંગ સપાટી 0.05 mm જાડા તેલ પડ પર 5 m/s પર ચાલે છે, η = 0.25 Pa·s. શ્યાન બળ શોધો."),
        [P("F = η A v/x", "F = η A v/x"),
         P("= 0.25 × 0.02 × 5/(5 × 10⁻⁵)", "= 0.25 × 0.02 × 5/(5 × 10⁻⁵)"),
         P("= 0.025/5 × 10⁻⁵ = 500 N", "= 0.025/5 × 10⁻⁵ = 500 N")],
        T("500 N", "500 N"), unit_no=3),
    num("u3n21", T("Height of a mercury column in a 0.2 mm tube.",
                   "0.2 mm નળીમાં પારાના સ્તંભની ઊંચાઈ."),
        T("Mercury (T = 0.465 N/m, ρ = 13 600 kg/m³, θ = 140°) in a tube of radius 0.2 mm: find the "
          "depression.", "0.2 mm ત્રિજ્યાની નળીમાં પારો (T = 0.465 N/m, ρ = 13 600 kg/m³, θ = 140°): "
          "ઉતાર શોધો."),
        [P("h = 2T cos θ/(ρ g r)", "h = 2T cos θ/(ρ g r)"),
         P("cos 140° = −0.766", "cos 140° = −0.766"),
         P("h = 2 × 0.465 × (−0.766)/(13 600 × 9.8 × 2 × 10⁻⁴) = −0.712/26.66 = −0.027 m",
           "h = 2 × 0.465 × (−0.766)/(13 600 × 9.8 × 2 × 10⁻⁴) = −0.712/26.66 = −0.027 m"),
         P("The minus sign means a depression of 2.7 cm.", "ઋણ ચિહ્ન એટલે 2.7 cm નો ઉતાર.")],
        T("2.7 cm depression", "2.7 cm ઉતાર"), unit_no=3),
    num("u3n22", T("Load that a steel rod can carry at 100 MPa.",
                   "100 MPa પર સ્ટીલ સળિયો કેટલો ભાર લઈ શકે."),
        T("A steel rod of cross-section 10 mm² is limited to a working stress of 100 MPa. Find the "
          "safe load.", "10 mm² કાપવાળા સ્ટીલ સળિયા માટે કાર્યકારી પ્રતિબળ 100 MPa સુધી મર્યાદિત છે. "
          "સલામત ભાર શોધો."),
        [P("F = σ A = 100 × 10⁶ × 10 × 10⁻⁶", "F = σ A = 100 × 10⁶ × 10 × 10⁻⁶"),
         P("= 1000 N", "= 1000 N"),
         P("With a yield stress of 250 MPa this is a safety factor of 2.5.",
           "250 MPa ઉપજ પ્રતિબળ સાથે આ 2.5 નો સલામતી અવયવ છે.")],
        T("1000 N", "1000 N"), unit_no=3),
    num("u3n23", T("Surface energy needed to blow a 2 cm soap bubble.",
                   "2 cm સાબુના પરપોટા ફૂંકવા જરૂરી પૃષ્ઠઊર્જા."),
        T("Find the work needed to blow a soap bubble of radius 2 cm (T = 0.025 N/m).",
          "2 cm ત્રિજ્યાનો સાબુનો પરપોટો ફૂંકવા જરૂરી કાર્ય શોધો (T = 0.025 N/m)."),
        [P("A bubble has two surfaces: A = 2 × 4πr²", "પરપોટાને બે સપાટી: A = 2 × 4πr²"),
         P("A = 2 × 4π × 4 × 10⁻⁴ = 1.005 × 10⁻² m²", "A = 2 × 4π × 4 × 10⁻⁴ = 1.005 × 10⁻² m²"),
         P("W = T A = 0.025 × 1.005 × 10⁻² = 2.5 × 10⁻⁴ J", "W = T A = 0.025 × 1.005 × 10⁻² = 2.5 × 10⁻⁴ J")],
        T("2.5 × 10⁻⁴ J", "2.5 × 10⁻⁴ J"), unit_no=3),
    num("u3n24", T("Pipe diameter that keeps water flow streamline at 1 m/s.",
                   "1 m/s પર પાણીનો પ્રવાહ સ્તરીય રહે તેવો નળીનો વ્યાસ."),
        T("For water at 1 m/s, what is the largest pipe diameter that keeps Re below 2000?",
          "1 m/s પર પાણી માટે Re 2000થી નીચે રહે તેવો સૌથી મોટો નળીનો વ્યાસ કેટલો?"),
        [P("Re = ρ v d/η, so d = Re η/(ρ v)", "Re = ρ v d/η, તેથી d = Re η/(ρ v)"),
         P("= 2000 × 10⁻³/(1000 × 1)", "= 2000 × 10⁻³/(1000 × 1)"),
         P("= 2 × 10⁻³ m = 2 mm", "= 2 × 10⁻³ m = 2 mm"),
         P("Any larger pipe is turbulent at 1 m/s — which is why real pipes run slower.",
           "તેનાથી મોટી કોઈ પણ નળી 1 m/s પર વમળીય થાય — તેથી જ વાસ્તવિક નળીઓ ધીમે ચાલે.")],
        T("2 mm", "2 mm"), unit_no=3),
]

EQUATIONS = [
    {"title": T("Elasticity", "સ્થિતિસ્થાપકતા"),
     "items": [
         {"name": T("Stress", "પ્રતિબળ"), "f": "σ = F/A  (N/m²)",
          "terms": T("Restoring force per unit area.", "એકમ ક્ષેત્રફળ દીઠ પુનઃસ્થાપક બળ.")},
         {"name": T("Strain", "વિકૃતિ"), "f": "ε = ΔL/L, ΔV/V or Δx/h",
          "terms": T("No unit; a pure ratio.", "એકમ નહીં; શુદ્ધ ગુણોત્તર.")},
         {"name": T("Hooke's law", "હૂકનો નિયમ"), "f": "σ = E ε",
          "terms": T("Valid only up to the elastic limit.", "ફક્ત સ્થિતિસ્થાપક મર્યાદા સુધી માન્ય.")},
         {"name": T("Young's modulus", "યંગ ગુણાંક"), "f": "Y = (F/A)/(ΔL/L) = F L/(A ΔL)",
          "terms": T("Slope of the straight part of the stress-strain curve.",
                     "પ્રતિબળ-વિકૃતિ વક્રના સીધા ભાગનો ઢાળ.")},
         {"name": T("Bulk modulus", "બલ્ક ગુણાંક"), "f": "K = −ΔP/(ΔV/V)",
          "terms": T("Negative sign keeps K positive for compression.",
                     "ઋણ ચિહ્ન સંકોચનમાં K ધન રાખે.")},
         {"name": T("Shear modulus", "શિયર ગુણાંક"), "f": "G = (F/A)/(Δx/h)",
          "terms": T("Shape changes, volume does not.", "આકાર બદલાય, ઘનફળ નહીં.")},
         {"name": T("Elastic energy", "સ્થિતિસ્થાપક ઊર્જા"), "f": "U = ½ F ΔL",
          "terms": T("Stored in a stretched spring or wire.", "ખેંચાયેલી સ્પ્રિંગ કે તારમાં સંગ્રહાય.")},
     ]},
    {"title": T("Surface tension and capillarity", "પૃષ્ઠતાણ અને કેશનળી ચઢાણ"),
     "items": [
         {"name": T("Surface tension", "પૃષ્ઠતાણ"), "f": "T = F/L  (N/m) = energy/area (J/m²)",
          "terms": T("Force along the surface per unit length.", "સપાટી પર એકમ લંબાઈ દીઠ બળ.")},
         {"name": T("Soap film force", "સાબુના પડનું બળ"), "f": "F = 2 T L",
          "terms": T("Two surfaces; a drop boundary has one.", "બે સપાટી; ટીપાની સીમાને એક.")},
         {"name": T("Surface energy", "પૃષ્ઠઊર્જા"), "f": "W = T ΔA",
          "terms": T("Work to create new surface.", "નવી સપાટી બનાવવાનું કાર્ય.")},
         {"name": T("Excess pressure, drop", "ટીપામાં વધારાનું દબાણ"), "f": "p = 2T/r",
          "terms": T("Smaller drop, larger pressure.", "નાનું ટીપું, વધુ દબાણ.")},
         {"name": T("Excess pressure, bubble", "પરપોટામાં વધારાનું દબાણ"), "f": "p = 4T/r",
          "terms": T("Because a bubble has two surfaces.", "કારણ કે પરપોટાને બે સપાટી હોય.")},
         {"name": T("Ascent formula", "આરોહણ સૂત્ર"), "f": "h = 2T cos θ/(ρ g r)",
          "terms": T("Negative h for mercury: a depression.", "પારા માટે h ઋણ: ઉતાર.")},
     ]},
    {"title": T("Viscosity", "શ્યાનતા"),
     "items": [
         {"name": T("Newton's law of viscosity", "ન્યૂટનનો શ્યાનતાનો નિયમ"),
          "f": "F = −η A (dv/dx)",
          "terms": T("Force proportional to area and velocity gradient.",
                     "બળ ક્ષેત્રફળ અને વેગ પ્રવણતાના સમપ્રમાણમાં.")},
         {"name": T("Coefficient of viscosity", "શ્યાનતા ગુણાંક"),
          "f": "η = F/(A dv/dx)  (Pa·s)",
          "terms": T("1 Pa·s = 10 poise.", "1 Pa·s = 10 પોઇઝ.")},
         {"name": T("Reynolds number", "રેનોલ્ડ્સ આંક"), "f": "Re = ρ v d/η",
          "terms": T("Below 2000 streamline, above 4000 turbulent.",
                     "2000થી નીચે સ્તરીય, 4000થી ઉપર વમળીય.")},
         {"name": T("Critical velocity", "ક્રાંતિક વેગ"), "f": "v_c = Re η/(ρ d)",
          "terms": T("Speed above which the flow breaks into eddies.",
                     "જેનાથી ઉપર પ્રવાહ વમળમાં તૂટે.")},
         {"name": T("Stokes' law", "સ્ટોક્સનો નિયમ"), "f": "F = 6π η r v",
          "terms": T("Drag on a small sphere moving slowly.", "ધીમે ચાલતા નાના ગોળા પરનો પ્રતિરોધ.")},
         {"name": T("Terminal velocity", "અંતિમ વેગ"),
          "f": "v_t = 2r²(ρ − σ)g/(9η)",
          "terms": T("Reached when weight = upthrust + drag.", "વજન = ઉત્પ્લાવક + પ્રતિરોધ ત્યારે મળે.")},
     ]},
]

VIVA = [
    {"title": T("Elasticity", "સ્થિતિસ્થાપકતા"),
     "items": [
         {"q": T("Define stress and strain with their units.",
                 "પ્રતિબળ અને વિકૃતિ તેમના એકમ સાથે સમજાવો."),
          "a": T("Stress is restoring force per unit area (N/m²); strain is the fractional change of "
                 "dimension and has no unit.",
                 "પ્રતિબળ એકમ ક્ષેત્રફળ દીઠ પુનઃસ્થાપક બળ (N/m²) છે; વિકૃતિ પરિમાણમાં અંશતઃ ફેરફાર છે અને "
                 "તેને એકમ નથી.")},
         {"q": T("State Hooke's law and its limit.", "હૂકનો નિયમ અને તેની મર્યાદા જણાવો."),
          "a": T("Within the elastic limit stress is proportional to strain, σ = E ε; beyond the yield "
                 "point the material stays deformed.",
                 "સ્થિતિસ્થાપક મર્યાદા સુધી પ્રતિબળ વિકૃતિના સમપ્રમાણમાં, σ = E ε; ઉપજ બિંદુ પછી પદાર્થ "
                 "વિકૃત જ રહે.")},
         {"q": T("Name the three moduli of elasticity and the deformation each resists.",
                 "સ્થિતિસ્થાપકતાના ત્રણ ગુણાંક અને દરેક કઈ વિકૃતિનો પ્રતિરોધ કરે તે જણાવો."),
          "a": T("Young's modulus resists stretching, bulk modulus resists volume change and shear "
                 "modulus resists change of shape.",
                 "યંગ ગુણાંક ખેંચાણનો, બલ્ક ગુણાંક ઘનફળના ફેરફારનો અને શિયર ગુણાંક આકારના ફેરફારનો પ્રતિરોધ "
                 "કરે.")},
         {"q": T("What do the points A, B, D and E on a stress-strain curve mean?",
                 "પ્રતિબળ-વિકૃતિ વક્ર પર A, B, D અને E બિંદુનો અર્થ શું?"),
          "a": T("A is the proportional limit where the straight line ends, B the elastic limit, D the "
                 "ultimate tensile strength and E the fracture point.",
                 "A સમપ્રમાણ મર્યાદા જ્યાં સીધી રેખા પૂરી થાય, B સ્થિતિસ્થાપક મર્યાદા, D અંતિમ તણાવ "
                 "મજબૂતાઈ અને E ભંગ બિંદુ છે.")},
         {"q": T("Why is a safety factor used in design?",
                 "રચનામાં સલામતી અવયવ કેમ વપરાય?"),
          "a": T("The working stress is kept well below the yield stress so that the part springs back "
                 "after every load and survives overloads and fatigue.",
                 "કાર્યકારી પ્રતિબળ ઉપજ પ્રતિબળથી ઘણું નીચે રખાય જેથી દરેક ભાર પછી પાર્ટ પાછો આવે અને "
                 "ઓવરલોડ તથા થાક સહે.")},
     ]},
    {"title": T("Surface tension", "પૃષ્ઠતાણ"),
     "items": [
         {"q": T("Define surface tension and give both its units.",
                 "પૃષ્ઠતાણની વ્યાખ્યા આપો અને તેના બંને એકમ જણાવો."),
          "a": T("Force per unit length along the surface, N/m, which is also surface energy per unit "
                 "area, J/m².",
                 "સપાટી પર એકમ લંબાઈ દીઠ બળ, N/m, જે એકમ ક્ષેત્રફળ દીઠ પૃષ્ઠઊર્જા J/m² પણ છે.")},
         {"q": T("Why does a liquid surface behave like a stretched membrane?",
                 "પ્રવાહીની સપાટી તંગ પડ જેવી કેમ વર્તે?"),
          "a": T("A molecule at the surface has only part of its sphere of influence filled, so it is "
                 "pulled inwards; the surface stores energy and tries to shrink.",
                 "સપાટી પરના અણુનો પ્રભાવ ગોળો અંશતઃ ભરેલો હોય, તેથી તે અંદર ખેંચાય; સપાટી ઊર્જા ધરાવે "
                 "અને સંકોચાવા પ્રયત્ન કરે.")},
         {"q": T("What is the angle of contact, and what does θ > 90° mean?",
                 "સંપર્ક કોણ શું છે અને θ > 90° નો અર્થ શું?"),
          "a": T("The angle between the liquid surface tangent and the solid inside the liquid; θ > 90° "
                 "means the liquid does not wet the solid — mercury in glass.",
                 "પ્રવાહીની સપાટીના સ્પર્શક અને પ્રવાહીની અંદરની ઘન સપાટી વચ્ચેનો ખૂણો; θ > 90° એટલે "
                 "પ્રવાહી ઘનને ભીનું કરતું નથી — કાચમાં પારો.")},
         {"q": T("State the Ascent formula and say what happens for mercury.",
                 "આરોહણ સૂત્ર જણાવો અને પારા માટે શું થાય તે કહો."),
          "a": T("h = 2T cos θ/(ρ g r); for mercury cos θ is negative, so h is negative and the liquid "
                 "is depressed in the tube.",
                 "h = 2T cos θ/(ρ g r); પારા માટે cos θ ઋણ હોય, તેથી h ઋણ થાય અને નળીમાં પ્રવાહી ઉતરે.")},
         {"q": T("How do temperature and impurity change surface tension?",
                 "તાપમાન અને અશુદ્ધિ પૃષ્ઠતાણ કેવી રીતે બદલે?"),
          "a": T("Surface tension falls as temperature rises; highly soluble impurities raise it "
                 "slightly and sparingly soluble ones such as soap lower it sharply.",
                 "તાપમાન વધે તેમ પૃષ્ઠતાણ ઘટે; ખૂબ દ્રાવ્ય અશુદ્ધિ થોડું વધારે અને સાબુ જેવી ઓછી દ્રાવ્ય "
                 "અશુદ્ધિ ઝડપથી ઘટાડે.")},
         {"q": T("Why is water used in a capillary tube and mercury not?",
                 "કેશનળીમાં પાણી વપરાય અને પારો કેમ નહીં?"),
          "a": T("Water wets glass (θ ≈ 0), so it rises and the height is easy to read; mercury has "
                 "θ ≈ 140°, so it is depressed and the column is short.",
                 "પાણી કાચને ભીનું કરે (θ ≈ 0), તેથી ચઢે અને ઊંચાઈ વાંચવી સહેલી; પારાનો θ ≈ 140° હોવાથી "
                 "ઉતરે અને સ્તંભ ટૂંકો રહે.")},
     ]},
    {"title": T("Viscosity", "શ્યાનતા"),
     "items": [
         {"q": T("Define viscosity and its SI unit.", "શ્યાનતા અને તેનો SI એકમ જણાવો."),
          "a": T("The internal friction of a fluid opposing relative motion of its layers, measured by "
                 "the coefficient η in Pa·s (= 10 poise).",
                 "પ્રવાહીનું આંતરિક ઘર્ષણ જે તેના સ્તરોની સાપેક્ષ ગતિનો વિરોધ કરે, જે ગુણાંક η થી "
                 "મપાય, Pa·s (= 10 પોઇઝ).")},
         {"q": T("State Newton's law of viscosity.", "ન્યૂટનનો શ્યાનતાનો નિયમ જણાવો."),
          "a": T("The viscous force between two layers is proportional to their area and to the "
                 "velocity gradient: F = −η A dv/dx.",
                 "બે સ્તરો વચ્ચેનું શ્યાન બળ તેમના ક્ષેત્રફળ અને વેગ પ્રવણતાના સમપ્રમાણમાં છે: "
                 "F = −η A dv/dx.")},
         {"q": T("What is the Reynolds number and what do its values mean?",
                 "રેનોલ્ડ્સ આંક શું છે અને તેનાં મૂલ્યોનો અર્થ શું?"),
          "a": T("Re = ρ v d/η, a dimensionless number; below about 2000 the flow is streamline, above "
                 "about 4000 turbulent.",
                 "Re = ρ v d/η, પરિમાણરહિત આંક; લગભગ 2000થી નીચે પ્રવાહ સ્તરીય, 4000થી ઉપર વમળીય.")},
         {"q": T("State Stokes' law and the conditions for its use.",
                 "સ્ટોક્સનો નિયમ અને તેના ઉપયોગની શરતો જણાવો."),
          "a": T("F = 6π η r v for a smooth sphere moving slowly and steadily through an infinite "
                 "viscous fluid with no turbulence.",
                 "સરખા ગોળા માટે F = 6π η r v, જે વમળ વગરના અનંત શ્યાન પ્રવાહીમાં ધીમે અને સ્થિર ગતિએ "
                 "માન્ય છે.")},
         {"q": T("Why does terminal velocity depend on r²?",
                 "અંતિમ વેગ r² પર કેમ આધારિત છે?"),
          "a": T("Weight and upthrust both grow as r³ while the drag at a given speed grows only as r, "
                 "so the balance is reached at a speed proportional to r².",
                 "વજન અને ઉત્પ્લાવક બંને r³ પ્રમાણે વધે જ્યારે આપેલ ઝડપે પ્રતિરોધ ફક્ત r પ્રમાણે વધે, તેથી "
                 "સંતુલન r² પ્રમાણવાળી ઝડપે મળે.")},
         {"q": T("How does temperature affect the viscosity of a liquid and of a gas?",
                 "તાપમાન પ્રવાહી અને વાયુની શ્યાનતાને કેવી રીતે અસર કરે?"),
          "a": T("Liquid viscosity falls as temperature rises because molecules slip past each other; "
                 "gas viscosity rises because molecular momentum transfer increases.",
                 "તાપમાન વધે તેમ પ્રવાહીની શ્યાનતા ઘટે કારણ કે અણુઓ સરકી જાય; વાયુની શ્યાનતા વધે કારણ કે "
                 "આણ્વીય વેગમાન સ્થાનાંતરણ વધે.")},
     ]},
]

_PRACTICE = [
    (T("Define stress, strain and Young's modulus, and derive Y = FL/(A ΔL).",
       "પ્રતિબળ, વિકૃતિ અને યંગ ગુણાંકની વ્યાખ્યા આપી Y = FL/(A ΔL) મેળવો."),
     5,
     [P("Stress is the restoring force per unit area, σ = F/A, in N/m²; strain is the fractional "
        "change of length, ε = ΔL/L, with no unit.",
        "પ્રતિબળ એકમ ક્ષેત્રફળ દીઠ પુનઃસ્થાપક બળ છે, σ = F/A, N/m² માં; વિકૃતિ લંબાઈમાં અંશતઃ ફેરફાર છે, "
        "ε = ΔL/L, જેને એકમ નથી."),
      P("Young's modulus is the ratio within the elastic limit: Y = σ/ε = (F/A)/(ΔL/L) = FL/(A ΔL). "
        "The rearrangement is what the Searle experiment uses.",
        "યંગ ગુણાંક સ્થિતિસ્થાપક મર્યાદામાં ગુણોત્તર છે: Y = σ/ε = (F/A)/(ΔL/L) = FL/(A ΔL). આ ગોઠવણી જ "
        "સર્લના પ્રયોગમાં વપરાય છે."),
      P("A steel wire of 1 mm² and 2 m carrying 50 N extends by 0.5 mm, giving "
        "Y = 50 × 2/(10⁻⁶ × 5 × 10⁻⁴) = 2 × 10¹¹ N/m².",
        "1 mm² અને 2 m નો સ્ટીલ તાર 50 N સાથે 0.5 mm ખેંચાય, તેથી Y = 50 × 2/(10⁻⁶ × 5 × 10⁻⁴) = "
        "2 × 10¹¹ N/m².")]),
    (T("Explain the stress-strain curve and mark its important points.",
       "પ્રતિબળ-વિકૃતિ વક્ર સમજાવો અને તેના મહત્વના બિંદુ દર્શાવો."),
     4,
     [P("The curve starts with a straight line OA through the origin where Hooke's law holds; the slope "
        "of that line is Young's modulus.",
        "વક્ર ઉદ્ગમમાંથી પસાર થતી સીધી રેખા OA થી શરૂ થાય જ્યાં હૂકનો નિયમ લાગુ પડે; તે રેખાનો ઢાળ યંગ "
        "ગુણાંક છે."),
      P("A is the proportional limit, B the elastic limit or yield point, D the ultimate tensile "
        "strength and E the fracture point. Between B and D the wire stretches plastically.",
        "A સમપ્રમાણ મર્યાદા, B સ્થિતિસ્થાપક મર્યાદા કે ઉપજ બિંદુ, D અંતિમ તણાવ મજબૂતાઈ અને E ભંગ બિંદુ છે. "
        "B અને D વચ્ચે તાર સ્થાયી રીતે ખેંચાય છે."),
      P("Ductile materials such as mild steel have a long B–E region, brittle ones such as glass break "
        "just after D; design always stays below B with a safety factor.",
        "માઇલ્ડ સ્ટીલ જેવા નમ્ય પદાર્થોમાં B–E વિસ્તાર લાંબો હોય, કાચ જેવા ભંગુર D પછી તરત તૂટે; રચના "
        "હંમેશા સલામતી અવયવ સાથે B નીચે રહે.")]),
    (T("Explain surface tension on the basis of molecular theory and give its two units.",
       "આણ્વીય સિદ્ધાંતના આધારે પૃષ્ઠતાણ સમજાવો અને તેના બે એકમ આપો."),
     4,
     [P("A molecule inside a liquid has its sphere of influence full of other molecules, so the "
        "attraction cancels; a molecule at the surface has it only half full, so there is a net inward "
        "pull.",
        "પ્રવાહીની અંદરના અણુનો પ્રભાવ ગોળો બીજા અણુઓથી ભરેલો હોય, તેથી આકર્ષણ રદ થાય; સપાટી પરના અણુનો "
        "અડધો ભરેલો હોય, તેથી ચોખ્ખું અંદર તરફ ખેંચાણ રહે."),
      P("That inward pull makes the surface behave like a stretched membrane, and its strength is the "
        "force per unit length T = F/L in N/m.",
        "એ અંદર તરફના ખેંચાણથી સપાટી તંગ પડ જેવી વર્તે, અને તેની મજબૂતાઈ એકમ લંબાઈ દીઠ બળ T = F/L, N/m છે."),
      P("Pulling a molecule to the surface needs work, so T is also the surface energy per unit area, "
        "J/m²; for water T ≈ 0.072 N/m at 20 °C.",
        "અણુને સપાટી પર લાવવા કાર્ય કરવું પડે, તેથી T એકમ ક્ષેત્રફળ દીઠ પૃષ્ઠઊર્જા પણ છે, J/m²; "
        "20 °C પર પાણી માટે T ≈ 0.072 N/m.")]),
    (T("Derive or state the Ascent formula and explain one engineering use of capillarity.",
       "આરોહણ સૂત્ર જણાવો અને કેશનળી ચઢાણનો એક ઇજનેરી ઉપયોગ સમજાવો."),
     5,
     [P("The formula is h = 2T cos θ/(ρ g r), where T is the surface tension, θ the contact angle, ρ "
        "the density and r the tube radius.",
        "સૂત્ર h = 2T cos θ/(ρ g r) છે, જ્યાં T પૃષ્ઠતાણ, θ સંપર્ક કોણ, ρ ઘનતા અને r નળીની ત્રિજ્યા છે."),
      P("Water in a 0.2 mm tube rises h = 0.144/(1000 × 9.8 × 2 × 10⁻⁴) = 7.35 cm; mercury with "
        "θ = 140° gives a negative h, so the column is depressed.",
        "0.2 mm નળીમાં પાણી h = 0.144/(1000 × 9.8 × 2 × 10⁻⁴) = 7.35 cm ચઢે; θ = 140° વાળો પારો ઋણ h આપે, "
        "તેથી સ્તંભ ઉતરે."),
      P("Engineering use: wicks and cooling-tower packing rely on capillary rise to spread water over "
        "a large surface without a pump, and soil moisture moves the same way.",
        "ઇજનેરી ઉપયોગ: વિક અને કૂલિંગ ટાવર પેકિંગ કેશનળી ચઢાણથી પંપ વગર પાણીને મોટી સપાટી પર ફેલાવે, "
        "અને જમીનનો ભેજ પણ એ જ રીતે ચાલે.")]),
    (T("What is the angle of contact? Explain why water wets glass but mercury does not.",
       "સંપર્ક કોણ શું છે? પાણી કાચને ભીનું કરે પણ પારો કેમ નહીં તે સમજાવો."),
     4,
     [P("The angle of contact is measured inside the liquid between the tangent to its surface and "
        "the solid wall; it is set by the balance of the solid–liquid, solid–vapour and "
        "liquid–vapour surface tensions.",
        "સંપર્ક કોણ પ્રવાહીની અંદર તેની સપાટીના સ્પર્શક અને ઘન દીવાલ વચ્ચે મપાય; તે ઘન–પ્રવાહી, ઘન–બાષ્પ "
        "અને પ્રવાહી–બાષ્પ પૃષ્ઠતાણના સંતુલનથી નક્કી થાય."),
      P("For water on clean glass adhesion is stronger than cohesion, so θ is nearly zero and the "
        "meniscus is concave; for mercury cohesion wins, θ ≈ 140°, and the meniscus is convex.",
        "સ્વચ્છ કાચ પર પાણી માટે આસક્તિ સંસક્તિ કરતાં વધુ મજબૂત છે, તેથી θ લગભગ શૂન્ય અને મેનિસ્કસ "
        "અંતર્ગોળ; પારા માટે સંસક્તિ જીતે, θ ≈ 140°, અને મેનિસ્કસ બહિર્ગોળ."),
      P("The consequence is practical: water climbs a capillary and soaks a wick, mercury is pushed "
        "down and reads a depression, which is exactly what a mercury barometer corrects for.",
        "પરિણામ વ્યવહારુ છે: પાણી કેશનળીમાં ચઢે અને વિક ભીનો કરે, પારો નીચે ધકેલાય અને ઉતાર દર્શાવે, જે "
        "પારા બેરોમીટરમાં સુધારા તરીકે ગણાય.")]),
    (T("Explain surface tension, surface energy and their relation with a numerical example.",
       "પૃષ્ઠતાણ, પૃષ્ઠઊર્જા અને તેમનો સંબંધ દાખલા સાથે સમજાવો."),
     4,
     [P("Surface tension is the force per unit length along a liquid surface; surface energy is the "
        "work needed to create unit area of new surface. They are numerically equal: 1 N/m = 1 J/m².",
        "પૃષ્ઠતાણ પ્રવાહીની સપાટી પર એકમ લંબાઈ દીઠ બળ છે; પૃષ્ઠઊર્જા નવી સપાટીના એકમ ક્ષેત્રફળ માટે જરૂરી "
        "કાર્ય છે. બંને આંકડામાં સમાન છે: 1 N/m = 1 J/m²."),
      P("Blowing a soap bubble of 2 cm radius: A = 2 × 4πr² = 1.005 × 10⁻² m², so W = 0.025 × "
        "1.005 × 10⁻² = 2.5 × 10⁻⁴ J.",
        "2 cm ત્રિજ્યાનો સાબુનો પરપોટો ફૂંકતાં: A = 2 × 4πr² = 1.005 × 10⁻² m², તેથી W = 0.025 × "
        "1.005 × 10⁻² = 2.5 × 10⁻⁴ J."),
      P("The factor two appears because the bubble has an inside and an outside surface; a drop has "
        "only one, which is why the excess pressure formulas differ (4T/r against 2T/r).",
        "2 નો અવયવ એટલા માટે કે પરપોટાને અંદર અને બહાર બે સપાટી હોય; ટીપાને ફક્ત એક, તેથી જ વધારાના દબાણનાં "
        "સૂત્ર જુદાં પડે (4T/r સામે 2T/r).")]),
    (T("State Newton's law of viscosity and define the coefficient of viscosity with its units.",
       "ન્યૂટનનો શ્યાનતાનો નિયમ જણાવો અને શ્યાનતા ગુણાંક તેના એકમ સાથે સમજાવો."),
     4,
     [P("Newton's law: the viscous force between two layers is proportional to their area and to the "
        "velocity gradient, F = −η A dv/dx.",
        "ન્યૂટનનો નિયમ: બે સ્તરો વચ્ચેનું શ્યાન બળ તેમના ક્ષેત્રફળ અને વેગ પ્રવણતાના સમપ્રમાણમાં છે, "
        "F = −η A dv/dx."),
      P("The constant η is the coefficient of viscosity, numerically the force per unit area per unit "
        "velocity gradient, with SI unit Pa·s and CGS unit poise (1 Pa·s = 10 poise).",
        "અચળાંક η શ્યાનતા ગુણાંક છે, આંકડામાં એકમ ક્ષેત્રફળ અને એકમ વેગ પ્રવણતા દીઠ બળ, SI એકમ Pa·s અને "
        "CGS એકમ પોઇઝ (1 Pa·s = 10 પોઇઝ)."),
      P("Water has η = 10⁻³ Pa·s and glycerine 0.83 Pa·s at 20 °C, which is why a steel ball sinks in "
        "water at once but drifts down glycerine at about 1.7 cm/s.",
        "20 °C પર પાણીનો η = 10⁻³ Pa·s અને ગ્લિસરિનનો 0.83 Pa·s છે, તેથી જ સ્ટીલનો દડો પાણીમાં તરત "
        "ઊતરે પણ ગ્લિસરિનમાં લગભગ 1.7 cm/s પર સરકે.")]),
    (T("Distinguish streamline and turbulent flow, and explain the Reynolds number.",
       "સ્તરીય અને વમળીય પ્રવાહમાં ભેદ સમજાવો અને રેનોલ્ડ્સ આંક સમજાવો."),
     4,
     [P("In streamline flow the layers slide past one another without mixing, the loss is small and "
        "the flow is quiet; in turbulent flow eddies form, the loss rises steeply with speed and the "
        "flow is noisy.",
        "સ્તરીય પ્રવાહમાં સ્તરો ભળ્યા વગર સરકે, ખોટ ઓછી અને પ્રવાહ શાંત; વમળીય પ્રવાહમાં વમળ બને, ઝડપ સાથે "
        "ખોટ ઝડપથી વધે અને પ્રવાહ ઘોંઘાટિયો."),
      P("The Reynolds number Re = ρ v d/η compares inertia to viscosity; below about 2000 the flow is "
        "streamline, above about 4000 turbulent.",
        "રેનોલ્ડ્સ આંક Re = ρ v d/η જડત્વની શ્યાનતા સાથે સરખામણી કરે; લગભગ 2000થી નીચે પ્રવાહ સ્તરીય, "
        "4000થી ઉપર વમળીય."),
      P("Water at 2 m/s in a 50 mm pipe gives Re = 10⁵, so the flow is fully turbulent and the pump "
        "must supply a pressure drop that grows as v².",
        "50 mm નળીમાં 2 m/s પર પાણી Re = 10⁵ આપે, તેથી પ્રવાહ પૂરો વમળીય છે અને પંપે v² પ્રમાણે વધતો "
        "દબાણ ઘટાડો પૂરો પાડવો પડે.")]),
    (T("State Stokes' law, define terminal velocity and derive its expression.",
       "સ્ટોક્સનો નિયમ જણાવો, અંતિમ વેગની વ્યાખ્યા આપો અને તેનું સૂત્ર મેળવો."),
     5,
     [P("Stokes' law: a sphere of radius r moving slowly at speed v through a fluid of viscosity η "
        "feels F = 6π η r v.",
        "સ્ટોક્સનો નિયમ: η શ્યાનતાવાળા પ્રવાહીમાં v ઝડપે ધીમે ચાલતા r ત્રિજ્યાના ગોળા પર F = 6π η r v લાગે."),
      P("Three forces act: weight (4/3)πr³ρg down, upthrust (4/3)πr³σg up, and drag 6πηrv up. Terminal "
        "velocity is reached when they balance.",
        "ત્રણ બળ લાગે: વજન (4/3)πr³ρg નીચે, ઉત્પ્લાવક (4/3)πr³σg ઉપર અને પ્રતિરોધ 6πηrv ઉપર. સંતુલન થાય "
        "ત્યારે અંતિમ વેગ મળે."),
      P("Setting them equal gives v_t = 2r²(ρ − σ)g/(9η); for a 1 mm steel ball in glycerine that is "
        "1.72 × 10⁻² m/s.",
        "તેમને સમાન ગણતાં v_t = 2r²(ρ − σ)g/(9η) મળે; ગ્લિસરિનમાં 1 mm સ્ટીલ દડા માટે તે 1.72 × 10⁻² m/s છે.")]),
    (T("How does temperature affect viscosity? Why do liquids and gases behave differently?",
       "તાપમાન શ્યાનતાને કેવી રીતે અસર કરે? પ્રવાહી અને વાયુ જુદા કેમ વર્તે?"),
     4,
     [P("Liquid viscosity falls with temperature: water goes from 1.00 mPa·s at 20 °C to 0.28 at "
        "100 °C, and engine oil from 0.25 to about 0.01 Pa·s.",
        "તાપમાન સાથે પ્રવાહીની શ્યાનતા ઘટે: પાણી 20 °C પર 1.00 mPa·s થી 100 °C પર 0.28 થાય, અને એન્જિન "
        "ઓઇલ 0.25 થી લગભગ 0.01 Pa·s."),
      P("The reason is that in a liquid the molecules are held by close-range attraction; heating "
        "gives them enough energy to slip past each other, so the internal friction drops.",
        "કારણ કે પ્રવાહીમાં અણુઓ નજીકના આકર્ષણથી બંધાયેલા હોય; ગરમી તેમને એકબીજા પરથી સરકવા પૂરતી ઊર્જા "
        "આપે, તેથી આંતરિક ઘર્ષણ ઘટે."),
      P("In a gas the viscosity comes from momentum transfer between molecules, and heating speeds "
        "them up, so gas viscosity rises — about 1.8 × 10⁻⁵ Pa·s for air at 20 °C, rising with "
        "temperature.",
        "વાયુમાં શ્યાનતા અણુઓ વચ્ચે વેગમાન સ્થાનાંતરણથી આવે, અને ગરમી તેમને ઝડપી કરે, તેથી વાયુની શ્યાનતા "
        "વધે — 20 °C પર હવા માટે લગભગ 1.8 × 10⁻⁵ Pa·s, જે તાપમાન સાથે વધે.")]),
    (T("A steel ball of 2 mm radius falls steadily at 0.1 m/s in glycerine of density 1260 kg/m³. Find "
       "the viscosity.", "2 mm ત્રિજ્યાનો સ્ટીલ દડો 1260 kg/m³ ઘનતાવાળા ગ્લિસરિનમાં 0.1 m/s ના અચળ વેગથી "
       "પડે છે. શ્યાનતા શોધો."),
     5,
     [P("Use v_t = 2r²(ρ − σ)g/(9η) with ρ = 7800 kg/m³ for steel and r = 2 × 10⁻³ m.",
        "ρ = 7800 kg/m³ (સ્ટીલ) અને r = 2 × 10⁻³ m સાથે v_t = 2r²(ρ − σ)g/(9η) વાપરો."),
      P("η = 2 × (2 × 10⁻³)² × 6540 × 9.8/(9 × 0.1) = 0.5127/0.9 = 0.57 Pa·s.",
        "η = 2 × (2 × 10⁻³)² × 6540 × 9.8/(9 × 0.1) = 0.5127/0.9 = 0.57 Pa·s."),
      P("The handbook value for glycerine at 20 °C is about 0.83 Pa·s, so this sample is warmer or "
        "slightly diluted — which is exactly how the experiment is used to check purity.",
        "20 °C પર ગ્લિસરિન માટે પુસ્તકનું મૂલ્ય લગભગ 0.83 Pa·s છે, તેથી આ નમૂનો ગરમ કે થોડો ભળેલો છે — "
        "આ પ્રયોગ શુદ્ધતા ચકાસવા એમ જ વપરાય છે.")]),
    (T("Why does a bearing need oil of the right viscosity? Use Newton's law to argue.",
       "બેરિંગને યોગ્ય શ્યાનતાવાળું તેલ કેમ જોઈએ? ન્યૂટનના નિયમથી દલીલ કરો."),
     4,
     [P("The oil film carries the shaft: F = η A v/x. If η is too low the film cannot support the "
        "load and the surfaces touch; if η is too high the friction loss is large and the oil cannot "
        "enter the clearance.",
        "તેલનો પડ શાફ્ટ ઉપાડે: F = η A v/x. η ખૂબ ઓછું હોય તો પડ ભાર ઉપાડી શકતું નથી અને સપાટીઓ અડે; "
        "ખૂબ વધુ હોય તો ઘર્ષણ ખોટ મોટી થાય અને તેલ ગેપમાં જઈ શકતું નથી."),
      P("A 0.02 m² surface at 5 m/s over a 0.05 mm film with η = 0.25 Pa·s gives 500 N of drag, so the "
        "oil pump has to supply that much work away as heat.",
        "0.25 Pa·s સાથે 0.05 mm ફિલ્મ પર 5 m/s પર 0.02 m² સપાટી 500 N ખેંચાણ આપે, તેથી તેલ પંપે એટલું "
        "કાર્ય ઉષ્મા તરીકે દૂર કરવું પડે."),
      P("Because η falls with temperature in a liquid, a multigrade oil is specified so that the film "
        "is still thick enough when the engine is hot.",
        "પ્રવાહીમાં તાપમાન સાથે η ઘટતું હોવાથી મલ્ટીગ્રેડ તેલ સૂચવાય, જેથી એન્જિન ગરમ હોય ત્યારે પણ પડ પૂરતો "
        "જાડો રહે.")]),
    (T("Explain two engineering applications of surface tension and two of viscosity.",
       "પૃષ્ઠતાણના બે અને શ્યાનતાના બે ઇજનેરી ઉપયોગો સમજાવો."),
     4,
     [P("Surface tension: in soldering a flux lowers T so that the solder wets the joint instead of "
        "beading, and in a cooling tower capillary rise spreads water over the packing so that air "
        "meets a thin film rather than a stream.",
        "પૃષ્ઠતાણ: સોલ્ડરિંગમાં ફ્લક્સ T ઘટાડે જેથી સોલ્ડર ટીપાં ન બનાવી જોડને ભીની કરે, અને કૂલિંગ ટાવરમાં "
        "કેશનળી ચઢાણ પાણીને પેકિંગ પર ફેલાવે જેથી હવા ધારાને બદલે પાતળી ફિલ્મને મળે."),
      P("Viscosity: the oil film in a journal bearing separates the shaft from the bush so that wear "
        "is replaced by fluid friction, and the dashpot of a shock absorber uses viscous drag to turn "
        "motion into heat.",
        "શ્યાનતા: જર્નલ બેરિંગમાં તેલનો પડ શાફ્ટને બુશથી અલગ રાખે જેથી ઘસારાને બદલે પ્રવાહી ઘર્ષણ રહે, અને "
        "શોક એબ્ઝોર્બરનો ડેશપોટ શ્યાન પ્રતિરોધથી ગતિને ઉષ્મામાં ફેરવે."),
      P("Both are about controlling an interface: surface tension acts at a free surface, viscosity "
        "acts between two layers of the same fluid.",
        "બંને એક ઇન્ટરફેસ નિયંત્રણ વિશે છે: પૃષ્ઠતાણ મુક્ત સપાટી પર કામ કરે, શ્યાનતા એક જ પ્રવાહીના બે સ્તરો "
        "વચ્ચે.")]),
    (T("A wire of 2 m and 1 mm² hangs a 50 N load. Find the stress, the strain and the extension "
       "(Y = 2 × 10¹¹ N/m²).", "2 m અને 1 mm² નો તાર 50 N ભાર લટકાવે છે. Y = 2 × 10¹¹ N/m² સાથે પ્રતિબળ, "
       "વિકૃતિ અને ખેંચાણ શોધો."),
     4,
     [P("σ = F/A = 50/10⁻⁶ = 5 × 10⁷ N/m².", "σ = F/A = 50/10⁻⁶ = 5 × 10⁷ N/m²."),
      P("ε = σ/Y = 5 × 10⁷/2 × 10¹¹ = 2.5 × 10⁻⁴.", "ε = σ/Y = 5 × 10⁷/2 × 10¹¹ = 2.5 × 10⁻⁴."),
      P("ΔL = ε L = 2.5 × 10⁻⁴ × 2 = 5 × 10⁻⁴ m = 0.5 mm, which matches the direct formula "
        "FL/(AY).", "ΔL = ε L = 2.5 × 10⁻⁴ × 2 = 5 × 10⁻⁴ m = 0.5 mm, જે FL/(AY) સૂત્ર સાથે મળે છે."),
      P("Check the answer: 0.5 mm in 2 m is a working stress of 50 MPa, far below the 250 MPa yield "
        "stress of mild steel, so the wire is safe and springs back fully. The weight of the wire "
        "itself has been neglected, which is justified because 2 m of 1 mm² steel weighs only about "
        "0.15 N against the 50 N load.",
        "જવાબ ચકાસો: 2 m માં 0.5 mm એટલે 50 MPa કાર્યકારી પ્રતિબળ, જે માઇલ્ડ સ્ટીલના 250 MPa ઉપજ "
        "પ્રતિબળ કરતાં ઘણું નીચે છે, તેથી તાર સલામત છે અને પૂરો પાછો આવે. તારનું પોતાનું વજન ગણતરીમાં "
        "લીધું નથી, જે વાજબી છે કારણ કે 1 mm² ના 2 m સ્ટીલનું વજન 50 N સામે ફક્ત લગભગ 0.15 N થાય.")]),
    (T("Why is steel used for springs and not cast iron? Answer with the stress-strain curve.",
       "સ્પ્રિંગ માટે સ્ટીલ વપરાય અને કાસ્ટ આયર્ન નહીં કેમ? પ્રતિબળ-વિકૃતિ વક્રથી જવાબ આપો."),
     4,
     [P("A spring must return to its shape after every cycle, so it must work well inside the elastic "
        "region and have a high yield point.",
        "સ્પ્રિંગે દરેક ચક્ર પછી પોતાનો આકાર પાછો મેળવવો પડે, તેથી તેને સ્થિતિસ્થાપક વિસ્તારમાં સારી રીતે "
        "કામ કરવું પડે અને ઊંચું ઉપજ બિંદુ જોઈએ."),
      P("Spring steel has a long straight OA and a high yield point B, so it stores large elastic "
        "energy U = ½F ΔL without permanent set.",
        "સ્પ્રિંગ સ્ટીલમાં લાંબો સીધો OA અને ઊંચું ઉપજ બિંદુ B હોય, તેથી તે સ્થાયી વિકૃતિ વગર મોટી "
        "સ્થિતિસ્થાપક ઊર્જા U = ½F ΔL સંગ્રહે."),
      P("Cast iron is brittle: it reaches D and breaks almost immediately with little plastic region, "
        "so a spring made of it would snap instead of deflecting.",
        "કાસ્ટ આયર્ન ભંગુર છે: તે D સુધી પહોંચીને લગભગ તરત તૂટે, સ્થાયી વિસ્તાર ઓછો હોય, તેથી તેની સ્પ્રિંગ "
        "નમવાને બદલે તૂટી પડે."),
      P("The energy a spring can store per unit volume is ½ × stress × strain = σ²/(2Y) at the yield "
        "stress, so a steel with a high yield stress and a moderate Y stores the most — that is the "
        "reason spring steel is alloyed and heat-treated rather than simply hardened.",
        "સ્પ્રિંગ એકમ ઘનફળમાં જેટલી ઊર્જા સંગ્રહી શકે તે ઉપજ પ્રતિબળ પાસે ½ × પ્રતિબળ × વિકૃતિ = σ²/(2Y) "
        "છે, તેથી ઊંચું ઉપજ પ્રતિબળ અને સામાન્ય Y વાળું સ્ટીલ સૌથી વધુ સંગ્રહે — તેથી જ સ્પ્રિંગ સ્ટીલને ફક્ત "
        "કઠણ કરવાને બદલે મિશ્રધાતુ બનાવી ઉષ્મા-પ્રક્રિયા આપાય છે.")]),
    (T("Water rises 7.35 cm in a capillary of radius 0.1 mm. Find the surface tension.",
       "0.1 mm ત્રિજ્યાની કેશનળીમાં પાણી 7.35 cm ચઢે છે. પૃષ્ઠતાણ શોધો."),
     3,
     [P("Use T = ρ g h r/2 with θ = 0°.", "θ = 0° સાથે T = ρ g h r/2 વાપરો."),
      P("T = 1000 × 9.8 × 0.0735 × 10⁻⁴/2.", "T = 1000 × 9.8 × 0.0735 × 10⁻⁴/2."),
      P("= 0.072 N/m, the standard value for water at about 20 °C — which is why the capillary-rise "
        "method is used as a practical.",
        "= 0.072 N/m, જે લગભગ 20 °C પર પાણીનું માનક મૂલ્ય છે — તેથી જ કેશનળી ચઢાણ રીત પ્રેક્ટિકલ તરીકે "
        "વપરાય."),
      P("The result is only as good as the assumptions behind it: the tube must be clean so that "
        "θ ≈ 0°, the bore must be uniform, and the meniscus is read at its lowest point. A 0.1 mm "
        "error in the radius changes T by about 0.07 %, so the radius is measured with a "
        "travelling microscope.",
        "પરિણામ તેટલું જ સારું જેટલી તેની પાછળની ધારણાઓ: નળી સ્વચ્છ હોવી જોઈએ જેથી θ ≈ 0°, બોર સરખું "
        "હોવું જોઈએ, અને મેનિસ્કસ તેના સૌથી નીચા બિંદુએ વંચાય. ત્રિજ્યામાં 0.1 mm ની ભૂલ T માં લગભગ "
        "0.07 % ફરક પાડે, તેથી ત્રિજ્યા ટ્રાવેલિંગ માઇક્રોસ્કોપથી મપાય.")]),
]

EXAM = [{"q": q, "marks": m} for q, m, _parts in _PRACTICE]
PRACTICE_ANSWERS = [_join(parts) for _q, _m, parts in _PRACTICE]

LESSON_COUNT = sum(len(s["items"]) for s in NOTES)
