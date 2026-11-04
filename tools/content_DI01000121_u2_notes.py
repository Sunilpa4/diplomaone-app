"""DI01000121 Applied Physics - Unit 2: Circular Motion (bilingual en + gu).

GTU 2.1-2.3, 8 h, 14 %, 10 marks, CO2. Builders are shared with Unit 1 so both languages always
stay in step.
"""
from content_DI01000121_u1_notes import T, P, H4, UL, OL, TB, card, num, _join

SOURCES = [
    T("GTU DI01000121 Applied Physics syllabus (uploaded PDF, w.e.f. 2024-25)",
      "GTU DI01000121 એપ્લાઇડ ફિઝિક્સ સિલેબસ (અપલોડ કરેલ PDF, 2024-25થી અમલમાં)"),
    T("NCERT Physics Class XI, Part I - Laws of Motion and Motion in a Plane",
      "NCERT ભૌતિક વિજ્ઞાન ધોરણ 11, ભાગ 1 - ગતિના નિયમો અને સમતલમાં ગતિ"),
    T("H. C. Verma - Concepts of Physics, Vol. I, chapters 5 and 7",
      "એચ. સી. વર્મા - કોન્સેપ્ટ્સ ઓફ ફિઝિક્સ, ભાગ 1, પ્રકરણ 5 અને 7"),
    T("M. N. Avadhanulu - A Textbook of Engineering Physics, mechanics chapters",
      "એમ. એન. અવધાનુલુ - ટેક્સ્ટબુક ઓફ એન્જિનિયરિંગ ફિઝિક્સ, મિકેનિક્સ પ્રકરણો"),
    T("IRC 86 - Geometric design standards for hill and ghat roads (banking practice)",
      "IRC 86 - ડુંગરાળ રસ્તાઓ માટે ભૌમિતિક રચના માનક (બેન્કિંગ પદ્ધતિ)"),
]

NOTES = [
    {"title": T("1. Force, Momentum and Its Conservation", "1. બળ, વેગમાન અને તેનું સંરક્ષણ"),
     "items": [
         card(T("1.1 Force and the rate of change of momentum",
                "1.1 બળ અને વેગમાનના ફેરફારનો દર"),
              [H4("Definition", "વ્યાખ્યા"),
               P("<b>Momentum</b> p = m v is the quantity of motion a body carries; it is a vector "
                 "pointing along the velocity. Its SI unit is kg·m/s.",
                 "<b>વેગમાન</b> p = m v એ શરીરમાં રહેલી ગતિનો જથ્થો છે; તે વેગની દિશામાં હોય તેવી સદિશ "
                 "રાશિ છે. તેનો SI એકમ kg·m/s છે."),
               P("<b>Force</b> is the rate of change of momentum: F = dp/dt = m a when the mass is "
                 "constant.", "<b>બળ</b> એ વેગમાનના ફેરફારનો દર છે: દ્રવ્યમાન અચળ હોય ત્યારે "
                 "F = dp/dt = m a."),
               H4("Worked example", "ઉકેલાયેલ દાખલો"),
               P("A 1500 kg car at 20 m/s carries p = 1500 × 20 = 30 000 kg·m/s. Bringing it to rest in "
                 "5 s needs F = 30 000/5 = 6000 N.",
                 "1500 kg ની કાર 20 m/s પર p = 1500 × 20 = 30 000 kg·m/s ધરાવે છે. તેને 5 sમાં ઊભી "
                 "કરવા F = 30 000/5 = 6000 N જોઈએ."),
               H4("Why momentum and not just velocity", "ફક્ત વેગ નહીં, વેગમાન કેમ"),
               P("A truck at 2 m/s and a cricket ball at 40 m/s can carry the same momentum, but the "
                 "truck is far harder to stop. Momentum measures both mass and motion, which is what "
                 "a brake, a catch or a collision actually deals with.",
                 "2 m/s પરનો ટ્રક અને 40 m/s પરનો ક્રિકેટ બોલ સમાન વેગમાન ધરાવી શકે, પણ ટ્રકને ઊભો કરવો "
                 "ઘણો અઘરો છે. વેગમાન દ્રવ્યમાન અને ગતિ બંને માપે છે, જે બ્રેક, કેચ કે અથડામણ ખરેખર "
                 "સંભાળે છે."),
               H4("Common mistake", "સામાન્ય ભૂલ"),
               P("Treating momentum as a scalar and adding speeds. Momentum is a vector: a ball that "
                 "rebounds reverses sign, so the change is twice as large as stopping it.",
                 "વેગમાનને અદિશ ગણીને ઝડપો જોડવી. વેગમાન સદિશ છે: પાછો ઉછળતો બોલ ચિહ્ન બદલે છે, તેથી "
                 "ફેરફાર તેને ઊભો કરવા કરતાં બમણો થાય.")],
              syllabus_item="2.1"),
         card(T("1.2 Impulse and why vehicles have crumple zones",
                "1.2 આઘાત (ઇમ્પલ્સ) અને વાહનમાં ક્રમ્પલ ઝોન કેમ હોય"),
              [H4("Definition", "વ્યાખ્યા"),
               P("<b>Impulse</b> J = F × t is the product of a force and the time it acts, and it "
                 "equals the change in momentum: J = Δp = m v − m u. Unit: N·s = kg·m/s.",
                 "<b>આઘાત</b> J = F × t એ બળ અને તે લાગે તે સમયનો ગુણાકાર છે, અને તે વેગમાનના ફેરફાર "
                 "બરાબર છે: J = Δp = m v − m u. એકમ: N·s = kg·m/s."),
               H4("The useful form", "ઉપયોગી સ્વરૂપ"),
               P("F = Δp / t. For a fixed change of momentum, a longer time means a smaller force.",
                 "F = Δp / t. વેગમાનનો ફેરફાર નિશ્ચિત હોય તો સમય લાંબો એટલે બળ નાનું."),
               TB([T("Situation", "પરિસ્થિતિ"), T("Time is made…", "સમય બનાવાય છે…"), T("Force on the body", "શરીર પરનું બળ")],
                  [[T("airbag opens", "એરબેગ ખૂલે"), T("longer", "લાંબો"), T("smaller, so no injury", "નાનું, તેથી ઈજા નહીં")],
                   [T("crumple zone folds", "ક્રમ્પલ ઝોન દબાય"), T("longer", "લાંબો"), T("smaller, cabin survives", "નાનું, કેબિન સલામત")],
                   [T("cricketer lowers the hands", "ક્રિકેટર હાથ નીચે લાવે"), T("longer", "લાંબો"), T("smaller, no stinging catch", "નાનું, હાથમાં દુખાવો નહીં")],
                   [T("hammer hits a nail", "હેમર ખીલી પર પડે"), T("shorter", "ટૂંકો"), T("larger, nail goes in", "મોટું, ખીલી ઘૂસે")]]),
               H4("Worked example", "ઉકેલાયેલ દાખલો"),
               P("A 0.15 kg ball arrives at 20 m/s and leaves at 20 m/s the other way. Δp = 0.15 × "
                 "(20 + 20) = 6 N·s. Stopped in 0.02 s the force is 300 N; in 0.2 s it is 30 N.",
                 "0.15 kg નો બોલ 20 m/s થી આવે અને વિરુદ્ધ દિશામાં 20 m/s થી જાય. Δp = 0.15 × (20 + 20) "
                 "= 6 N·s. 0.02 sમાં ઊભો કરો તો બળ 300 N; 0.2 s લાગે તો 30 N."),
               H4("Common mistake", "સામાન્ય ભૂલ"),
               P("Using only the incoming speed in Δp. When a body reverses, both velocities add in "
                 "magnitude with opposite signs: Δp = m(v + u).",
                 "Δpમાં ફક્ત આવતી ઝડપ વાપરવી. શરીર દિશા બદલે ત્યારે બંને વેગ વિરુદ્ધ ચિહ્ન સાથે મૂલ્યમાં "
                 "જોડાય: Δp = m(v + u).")],
              "u2_momentum", syllabus_item="2.1"),
         card(T("1.3 Law of conservation of linear momentum",
                "1.3 રેખીય વેગમાનના સંરક્ષણનો નિયમ"),
              [H4("Statement", "વિધાન"),
               P("If no external force acts on a system, its total linear momentum stays constant: "
                 "m₁u₁ + m₂u₂ = m₁v₁ + m₂v₂.",
                 "જો સિસ્ટમ પર કોઈ બાહ્ય બળ ન લાગે, તો તેનું કુલ રેખીય વેગમાન અચળ રહે: "
                 "m₁u₁ + m₂u₂ = m₁v₁ + m₂v₂."),
               H4("Why it holds", "કેમ સાચું છે"),
               P("It follows from Newton's third law: the two bodies push each other with equal and "
                 "opposite forces for the same time, so the impulses cancel and the total momentum "
                 "cannot change.",
                 "તે ન્યૂટનના ત્રીજા નિયમમાંથી નીકળે છે: બંને શરીરો સમાન અને વિરુદ્ધ બળ સમાન સમય માટે "
                 "લગાડે છે, તેથી આઘાત રદ થાય અને કુલ વેગમાન બદલાઈ શકતું નથી."),
               H4("Where it is used", "ક્યાં વપરાય"),
               TB([T("Event", "ઘટના"), T("Before", "પહેલાં"), T("After", "પછી")],
                  [[T("collision of two trolleys", "બે ટ્રોલીની અથડામણ"), T("m₁u₁ + m₂u₂", "m₁u₁ + m₂u₂"), T("(m₁ + m₂)v if they stick", "ચોંટે તો (m₁ + m₂)v")],
                   [T("recoil of a gun", "બંદૂકનો રીકોઇલ"), T("0 (both at rest)", "0 (બંને સ્થિર)"), T("m v + M V = 0", "m v + M V = 0")],
                   [T("explosion into two pieces", "બે ટુકડામાં વિસ્ફોટ"), T("0", "0"), T("m₁v₁ + m₂v₂ = 0", "m₁v₁ + m₂v₂ = 0")],
                   [T("person jumping off a boat", "હોડીમાંથી કૂદતો માણસ"), T("0", "0"), T("momentum shared, boat moves back", "વેગમાન વહેંચાય, હોડી પાછળ જાય")]]),
               H4("Worked example", "ઉકેલાયેલ દાખલો"),
               P("A 2 kg trolley at 3 m/s hits a 1 kg trolley at rest and they stick together. "
                 "2 × 3 = (2 + 1) × v, so v = 2 m/s in the original direction.",
                 "2 kg ની ટ્રોલી 3 m/s પર 1 kg ની સ્થિર ટ્રોલી સાથે અથડાઈને ચોંટે છે. 2 × 3 = (2 + 1) × v, "
                 "તેથી v = 2 m/s પહેલાની દિશામાં."),
               H4("Common mistake", "સામાન્ય ભૂલ"),
               P("Forgetting that momentum is conserved only when no external force acts. A ball "
                 "thrown upward loses momentum to gravity all the way up.",
                 "વેગમાન ફક્ત ત્યારે સંરક્ષિત રહે જ્યારે બાહ્ય બળ ન હોય તે ભૂલવું. ઉપર ફેંકેલો દડો ઉપર "
                 "જતી વખતે ગુરુત્વાકર્ષણને કારણે વેગમાન ગુમાવે છે.")],
              syllabus_item="2.1"),
         card(T("1.4 Recoil of a gun",
                "1.4 બંદૂકનો રીકોઇલ"),
              [H4("Method", "રીત"),
               OL(("Before firing both the gun and the bullet are at rest, so the total momentum is "
                   "zero.", "ગોળી ચલાવતા પહેલાં બંદૂક અને ગોળી બંને સ્થિર છે, તેથી કુલ વેગમાન શૂન્ય છે."),
                  ("After firing, m v + M V = 0 where m, v are for the bullet and M, V for the gun.",
                   "ચલાવ્યા પછી m v + M V = 0, જ્યાં m, v ગોળી માટે અને M, V બંદૂક માટે."),
                  ("So V = − m v / M: the gun moves backwards with the opposite momentum.",
                   "તેથી V = − m v / M: બંદૂક વિરુદ્ધ દિશામાં તે જ વેગમાન સાથે પાછી ખસે છે.")),
               H4("Worked example", "ઉકેલાયેલ દાખલો"),
               P("A 20 g bullet leaves a 5 kg rifle at 400 m/s: V = (0.020 × 400)/5 = 1.6 m/s backwards.",
                 "20 g ની ગોળી 5 kg ની રાયફલમાંથી 400 m/s પર નીકળે: V = (0.020 × 400)/5 = 1.6 m/s પાછળ."),
               H4("Engineering reading", "ઇજનેરી અર્થઘટન"),
               UL(("The recoil velocity is small because M ≫ m; the recoil momentum is not.",
                   "M ≫ m હોવાથી રીકોઇલ વેગ નાનો છે; રીકોઇલ વેગમાન નાનું નથી."),
                  ("Recoil energy goes into the shoulder, so the stock is made heavy and the spring "
                   "absorbs part of it.", "રીકોઇલની ઊર્જા ખભામાં જાય, તેથી સ્ટોક ભારે બનાવાય અને સ્પ્રિંગ "
                   "તેનો ભાગ શોષે."),
                  ("The same equation sizes the recoil of a rocket nozzle or a hose jet.",
                   "એ જ સમીકરણ રોકેટ નોઝલ કે પાઇપના જેટના રીકોઇલનું માપ નક્કી કરે છે.")),
               H4("Common mistake", "સામાન્ય ભૂલ"),
               P("Giving the gun the same velocity as the bullet. Momentum is shared in inverse "
                 "proportion to mass, not equally.",
                 "બંદૂકને ગોળી જેટલો જ વેગ આપવો. વેગમાન દ્રવ્યમાનના વ્યસ્ત પ્રમાણમાં વહેંચાય છે, સમાન "
                 "રીતે નહીં.")],
              "u2_recoil", syllabus_item="2.1"),
     ]},

    {"title": T("2. Circular Motion: Angles, Speed and Acceleration",
                "2. વર્તુળ ગતિ: કોણ, ઝડપ અને પ્રવર્ગ"),
     "items": [
         card(T("2.1 Angular displacement and the radian",
                "2.1 કોણીય સ્થાનાંતરણ અને રેડિયન"),
              [H4("Definition", "વ્યાખ્યા"),
               P("<b>Angular displacement</b> θ is the angle swept by the radius joining the body to "
                 "the centre. Its unit is the radian, where one radian is the angle that cuts an arc "
                 "equal to the radius.",
                 "<b>કોણીય સ્થાનાંતરણ</b> θ એ શરીરને કેન્દ્ર સાથે જોડતી ત્રિજ્યા દ્વારા ઘૂમાયેલો કોણ છે. "
                 "તેનો એકમ રેડિયન છે, જ્યાં એક રેડિયન એ ત્રિજ્યા જેટલી ચાપ કાપતો કોણ છે."),
               P("Arc length s = r θ (θ in radians). One full circle is 2π rad = 360°, so "
                 "1 rad = 57.3°.",
                 "ચાપની લંબાઈ s = r θ (θ રેડિયનમાં). પૂરું વર્તુળ 2π રેડિયન = 360°, તેથી "
                 "1 રેડિયન = 57.3°."),
               H4("Conversions you will use constantly", "વારંવાર વપરાતાં રૂપાંતરણ"),
               TB([T("Degrees", "અંશ"), T("Radians", "રેડિયન")],
                  [[T("90°", "90°"), T("π/2 = 1.571", "π/2 = 1.571")],
                   [T("180°", "180°"), T("π = 3.142", "π = 3.142")],
                   [T("360°", "360°"), T("2π = 6.283", "2π = 6.283")],
                   [T("1 revolution", "1 પરિભ્રમણ"), T("2π rad", "2π રેડિયન")]]),
               H4("Worked example", "ઉકેલાયેલ દાખલો"),
               P("A wheel of radius 0.4 m turns through 3 rad. The rim travels s = 0.4 × 3 = 1.2 m, "
                 "which is the length of belt a pulley of that size would move.",
                 "0.4 m ત્રિજ્યાનું ચક્ર 3 રેડિયન ફરે. કિનારો s = 0.4 × 3 = 1.2 m કાપે, જેટલી લંબાઈનો પટ્ટો "
                 "તે માપની ગરગડી ખસેડશે."),
               H4("Common mistake", "સામાન્ય ભૂલ"),
               P("Putting degrees into s = rθ. The formula needs radians; 30° is 0.524 rad, not 30.",
                 "s = rθ માં અંશ મૂકવા. સૂત્રને રેડિયન જોઈએ; 30° એ 0.524 રેડિયન છે, 30 નહીં.")],
              "u2_angular", syllabus_item="2.2"),
         card(T("2.2 Angular velocity and angular acceleration",
                "2.2 કોણીય વેગ અને કોણીય પ્રવર્ગ"),
              [H4("Definitions", "વ્યાખ્યાઓ"),
               P("<b>Angular velocity</b> ω = Δθ/Δt (rad/s) is the rate of change of angular "
                 "displacement. <b>Angular acceleration</b> α = Δω/Δt (rad/s²) is the rate of change "
                 "of angular velocity.",
                 "<b>કોણીય વેગ</b> ω = Δθ/Δt (rad/s) એ કોણીય સ્થાનાંતરણના ફેરફારનો દર છે. "
                 "<b>કોણીય પ્રવર્ગ</b> α = Δω/Δt (rad/s²) એ કોણીય વેગના ફેરફારનો દર છે."),
               H4("The three relations that link line and circle", "રેખા અને વર્તુળ જોડતા ત્રણ સંબંધ"),
               TB([T("Linear", "રેખીય"), T("Angular", "કોણીય"), T("Link", "સંબંધ")],
                  [[T("displacement s", "સ્થાનાંતરણ s"), T("θ", "θ"), T("s = r θ", "s = r θ")],
                   [T("velocity v", "વેગ v"), T("ω", "ω"), T("v = r ω", "v = r ω")],
                   [T("tangential acceleration a", "સ્પર્શીય પ્રવર્ગ a"), T("α", "α"), T("a = r α", "a = r α")]]),
               H4("Period, frequency and rpm", "આવર્તકાળ, આવૃત્તિ અને rpm"),
               P("ω = 2π/T = 2πn, where T is the period in seconds and n the frequency in hertz. For "
                 "a shaft turning N revolutions per minute, ω = 2πN/60.",
                 "ω = 2π/T = 2πn, જ્યાં T સેકન્ડમાં આવર્તકાળ અને n હર્ટ્ઝમાં આવૃત્તિ છે. N પરિભ્રમણ "
                 "પ્રતિ મિનિટ ફરતી શાફ્ટ માટે ω = 2πN/60."),
               H4("Worked example", "ઉકેલાયેલ દાખલો"),
               P("A 300 rpm shaft: ω = 2π × 300/60 = 31.4 rad/s. A 0.4 m pulley on it has rim speed "
                 "v = 0.4 × 31.4 = 12.6 m/s.",
                 "300 rpm ની શાફ્ટ: ω = 2π × 300/60 = 31.4 rad/s. તેના 0.4 m ની ગરગડીની કિનાર ઝડપ "
                 "v = 0.4 × 31.4 = 12.6 m/s."),
               H4("Common mistake", "સામાન્ય ભૂલ"),
               P("Using rpm directly as ω. 300 rpm is 31.4 rad/s, a factor of 31.4 — enough to make a "
                 "belt-drive calculation wrong by an order of magnitude.",
                 "rpm ને સીધું ω તરીકે વાપરવું. 300 rpm એટલે 31.4 rad/s, 31.4 નો અવયવ — પટ્ટા-ચાલકની "
                 "ગણતરી પૂરા ક્રમ જેટલી ખોટી થઈ શકે.")],
              syllabus_item="2.2"),
         card(T("2.3 Equations of rotational motion",
                "2.3 ભ્રમણાત્મક ગતિનાં સમીકરણો"),
              [H4("The three equations", "ત્રણ સમીકરણો"),
               P("They are the straight-line equations with s → θ, u → ω₀, v → ω and a → α:",
                 "તેઓ સુરેખ ગતિનાં સમીકરણો જ છે જ્યાં s → θ, u → ω₀, v → ω અને a → α:"),
               TB([T("Rotational form", "ભ્રમણાત્મક સ્વરૂપ"), T("Linear twin", "સુરેખ જોડિયું")],
                  [[T("ω = ω₀ + α t", "ω = ω₀ + α t"), T("v = u + a t", "v = u + a t")],
                   [T("θ = ω₀ t + ½ α t²", "θ = ω₀ t + ½ α t²"), T("s = u t + ½ a t²", "s = u t + ½ a t²")],
                   [T("ω² = ω₀² + 2 α θ", "ω² = ω₀² + 2 α θ"), T("v² = u² + 2 a s", "v² = u² + 2 a s")]]),
               H4("Worked example", "ઉકેલાયેલ દાખલો"),
               P("A wheel at rest reaches 20 rad/s in 4 s. α = 20/4 = 5 rad/s² and "
                 "θ = 0 + ½ × 5 × 16 = 40 rad, that is 6.37 revolutions.",
                 "સ્થિર ચક્ર 4 sમાં 20 rad/s પર પહોંચે. α = 20/4 = 5 rad/s² અને θ = 0 + ½ × 5 × 16 = "
                 "40 rad, એટલે 6.37 પરિભ્રમણ."),
               H4("When to use which", "ક્યારે કયું વાપરવું"),
               UL(("Time is given or asked: use the first two equations.",
                   "સમય આપેલો કે માગેલો હોય: પહેલાં બે સમીકરણો વાપરો."),
                  ("Time is neither given nor asked: use ω² = ω₀² + 2αθ.",
                   "સમય આપેલો ન હોય કે માગેલો ન હોય: ω² = ω₀² + 2αθ વાપરો."),
                  ("Only for constant α; a varying drive torque needs integration.",
                   "ફક્ત અચળ α માટે; બદલાતા ડ્રાઇવ ટોર્ક માટે સંકલન કરવું પડે.")),
               H4("Common mistake", "સામાન્ય ભૂલ"),
               P("Using θ in degrees. All three equations need radians, because θ = s/r is defined that "
                 "way.", "θ અંશમાં વાપરવું. ત્રણેય સમીકરણોને રેડિયન જોઈએ, કારણ કે θ = s/r એમ જ વ્યાખ્યાયિત છે.")],
              syllabus_item="2.2"),
         card(T("2.4 Uniform and non-uniform circular motion",
                "2.3 સમાન અને અસમાન વર્તુળ ગતિ"),
              [H4("Two cases", "બે સ્થિતિ"),
               TB([T("Uniform circular motion", "સમાન વર્તુળ ગતિ"), T("Non-uniform circular motion", "અસમાન વર્તુળ ગતિ")],
                  [[T("speed constant, direction changes", "ઝડપ અચળ, દિશા બદલાય"), T("both speed and direction change", "ઝડપ અને દિશા બંને બદલાય")],
                   [T("α = 0", "α = 0"), T("α ≠ 0", "α ≠ 0")],
                   [T("only centripetal acceleration a<sub>c</sub> = v²/r", "ફક્ત કેન્દ્રગામી પ્રવર્ગ a<sub>c</sub> = v²/r"), T("a<sub>c</sub> = v²/r plus tangential a<sub>t</sub> = rα", "a<sub>c</sub> = v²/r ઉપરાંત સ્પર્શીય a<sub>t</sub> = rα")],
                   [T("example: a fan at full speed", "ઉદાહરણ: પૂરી ઝડપે ચાલતો પંખો"), T("example: a fan speeding up", "ઉદાહરણ: ઝડપ પકડતો પંખો")]]),
               H4("Resultant acceleration", "પરિણામી પ્રવર્ગ"),
               P("The two components are perpendicular, so the total is a = √(a<sub>c</sub>² + "
                 "a<sub>t</sub>²) and its direction is not towards the centre once α ≠ 0.",
                 "બંને ઘટકો લંબ છે, તેથી કુલ a = √(a<sub>c</sub>² + a<sub>t</sub>²) અને α ≠ 0 હોય ત્યારે "
                 "તેની દિશા કેન્દ્ર તરફ રહેતી નથી."),
               H4("Worked example", "ઉકેલાયેલ દાખલો"),
               P("A 0.3 m wheel spinning at 4 m/s while braking with α = 2 rad/s² has "
                 "a<sub>c</sub> = 16/0.3 = 53.3 m/s² and a<sub>t</sub> = 0.3 × 2 = 0.6 m/s². The "
                 "centripetal part dominates, which is why brake pads see mostly radial loading.",
                 "0.3 m નું ચક્ર 4 m/s પર ફરતાં α = 2 rad/s² થી બ્રેક થાય તો a<sub>c</sub> = 16/0.3 = "
                 "53.3 m/s² અને a<sub>t</sub> = 0.3 × 2 = 0.6 m/s². કેન્દ્રગામી ભાગ પ્રભાવી છે, તેથી જ "
                 "બ્રેક પૅડ પર મુખ્યત્વે ત્રિજ્યાકીય ભાર પડે."),
               H4("Common mistake", "સામાન્ય ભૂલ"),
               P("Saying a body in uniform circular motion has no acceleration because its speed is "
                 "constant. The direction changes every instant, so the velocity does change.",
                 "સમાન વર્તુળ ગતિમાં ઝડપ અચળ હોવાથી પ્રવર્ગ નથી એમ કહેવું. દિશા દર ક્ષણે બદલાય છે, તેથી "
                 "વેગ બદલાય છે જ.")],
              syllabus_item="2.2"),
     ]},

    {"title": T("3. Centripetal and Centrifugal Force", "3. કેન્દ્રગામી અને કેન્દ્રત્યાગી બળ"),
     "items": [
         card(T("3.1 Centripetal force: the force that keeps a body on the circle",
                "3.1 કેન્દ્રગામી બળ: શરીરને વર્તુળ પર રાખતું બળ"),
              [H4("Definition and formula", "વ્યાખ્યા અને સૂત્ર"),
               P("<b>Centripetal force</b> is the inward force needed to keep a body of mass m moving "
                 "on a circle of radius r at speed v: F = m v²/r = m r ω². The acceleration it produces "
                 "is a<sub>c</sub> = v²/r, directed towards the centre.",
                 "<b>કેન્દ્રગામી બળ</b> એ દ્રવ્યમાન m ના શરીરને r ત્રિજ્યાના વર્તુળ પર v ઝડપે રાખવા "
                 "જરૂરી અંદર તરફનું બળ છે: F = m v²/r = m r ω². તે જે પ્રવર્ગ ઉત્પન્ન કરે તે "
                 "a<sub>c</sub> = v²/r છે, જે કેન્દ્ર તરફ છે."),
               H4("Who supplies it", "તે કોણ પૂરું પાડે"),
               TB([T("Situation", "પરિસ્થિતિ"), T("Force that acts as centripetal", "કેન્દ્રગામી બળ પૂરું પાડતું બળ")],
                  [[T("stone on a string", "દોરી સાથેનો પથ્થર"), T("tension in the string", "દોરીમાં તણાવ")],
                   [T("car on a curve", "વળાંક પર કાર"), T("friction between tyre and road", "ટાયર અને રસ્તા વચ્ચેનું ઘર્ષણ")],
                   [T("satellite in orbit", "કક્ષામાં ઉપગ્રહ"), T("gravitational attraction", "ગુરુત્વાકર્ષણ")],
                   [T("electron around a nucleus", "ન્યુક્લિયસ ફરતો ઇલેક્ટ્રોન"), T("electrostatic attraction", "સ્થિરવિદ્યુત આકર્ષણ")],
                   [T("bucket of water whirled overhead", "માથા પર ફેરવાતી પાણીની ડોલ"), T("tension plus weight at the top", "ઉપર તણાવ અને વજન")]]),
               H4("Worked example", "ઉકેલાયેલ દાખલો"),
               P("A 0.2 kg stone on a 0.5 m string moving at 4 m/s needs F = 0.2 × 16/0.5 = 6.4 N of "
                 "tension, which is the minimum strength of the string.",
                 "0.5 m દોરી પર 4 m/s પર ફરતા 0.2 kg પથ્થરને F = 0.2 × 16/0.5 = 6.4 N તણાવ જોઈએ, જે "
                 "દોરીની લઘુતમ મજબૂતાઈ છે."),
               H4("Common mistake", "સામાન્ય ભૂલ"),
               P("Adding a separate 'centripetal force' to the free-body diagram. It is not an extra "
                 "force; it is the name of the net inward force already present.",
                 "મુક્ત-શરીર આકૃતિમાં અલગ 'કેન્દ્રગામી બળ' ઉમેરવું. તે વધારાનું બળ નથી; તે પહેલેથી હાજર "
                 "ચોખ્ખા અંદર તરફના બળનું નામ છે.")],
              "u2_centripetal", syllabus_item="2.3"),
         card(T("3.2 Centrifugal force: real or not?",
                "3.2 કેન્દ્રત્યાગી બળ: સાચું કે નહીં?"),
              [H4("What it is", "તે શું છે"),
               P("<b>Centrifugal force</b> is the outward pseudo force felt in the rotating frame: "
                 "F = m v²/r, equal in size to the centripetal force and opposite in direction. It "
                 "appears because the observer is accelerating, not because something pushes outward.",
                 "<b>કેન્દ્રત્યાગી બળ</b> એ ફરતી ફ્રેમમાં અનુભવાતું બહાર તરફનું આભાસી બળ છે: F = m v²/r, "
                 "જે કદમાં કેન્દ્રગામી બળ જેટલું અને દિશામાં વિરુદ્ધ છે. તે દેખાય છે કારણ કે નિરીક્ષક "
                 "પ્રવર્ગિત છે, એટલા માટે નહીં કે કંઈક બહાર ધકેલે છે."),
               H4("The two side by side", "બંને સાથે"),
               TB([T("Point", "મુદ્દો"), T("Centripetal", "કેન્દ્રગામી"), T("Centrifugal", "કેન્દ્રત્યાગી")],
                  [[T("direction", "દિશા"), T("towards the centre", "કેન્દ્ર તરફ"), T("away from the centre", "કેન્દ્રથી દૂર")],
                   [T("nature", "સ્વરૂપ"), T("real force", "સાચું બળ"), T("pseudo force", "આભાસી બળ")],
                   [T("frame", "ફ્રેમ"), T("inertial frame", "જડત્વીય ફ્રેમ"), T("rotating frame only", "ફક્ત ફરતી ફ્રેમમાં")],
                   [T("example", "ઉદાહરણ"), T("tension, friction, gravity", "તણાવ, ઘર્ષણ, ગુરુત્વાકર્ષણ"), T("mud leaving a tyre, cream pushed out in a centrifuge", "ટાયરમાંથી નીકળતો કાદવ, સેન્ટ્રિફ્યુજમાં બહાર ધકેલાતી ક્રીમ")]]),
               H4("Worked example", "ઉકેલાયેલ દાખલો"),
               P("In a washing machine drum of radius 0.25 m at 1200 rpm, ω = 125.7 rad/s and "
                 "a = rω² ≈ 3950 m/s² ≈ 400 g. Water leaves through the holes because the drum cannot "
                 "supply that much inward force.",
                 "0.25 m ત્રિજ્યાના ધોવાના મશીનના ડ્રમમાં 1200 rpm પર ω = 125.7 rad/s અને a = rω² ≈ "
                 "3950 m/s² ≈ 400 g. પાણી છિદ્રોમાંથી નીકળે છે કારણ કે ડ્રમ એટલું અંદરનું બળ પૂરું પાડી "
                 "શકતું નથી."),
               H4("Common mistake", "સામાન્ય ભૂલ"),
               P("Drawing both forces on the same free-body diagram in the ground frame. Choose one "
                 "frame and stay in it.",
                 "જમીનની ફ્રેમમાં બંને બળ એક જ આકૃતિમાં દોરવાં. એક ફ્રેમ પસંદ કરો અને તેમાં જ રહો.")],
              syllabus_item="2.3"),
         card(T("3.3 Banking of roads",
                "3.3 રસ્તાનું બેન્કિંગ"),
              [H4("Why roads are banked", "રસ્તા કેમ બેન્ક કરાય"),
               P("On a flat curve the friction alone must supply m v²/r. Tilting the road by θ lets "
                 "the normal reaction contribute too, so the same curve can be taken faster and with "
                 "less skidding in rain.",
                 "સપાટ વળાંક પર ફક્ત ઘર્ષણે m v²/r પૂરું પાડવું પડે. રસ્તો θ જેટલો નમાવવાથી અભિલંબ "
                 "પ્રતિક્રિયા પણ ફાળો આપે, તેથી એ જ વળાંક વધુ ઝડપે અને વરસાદમાં ઓછા લપસવા સાથે લઈ શકાય."),
               H4("Derivation (friction ignored)", "સૂત્ર (ઘર્ષણ અવગણીને)"),
               OL(("Resolve: N cos θ balances weight m g, and N sin θ supplies the centripetal force.",
                   "ઘટકો પાડો: N cos θ વજન m g ને સંતુલિત કરે અને N sin θ કેન્દ્રગામી બળ પૂરું પાડે."),
                  ("N sin θ = m v²/r and N cos θ = m g.", "N sin θ = m v²/r અને N cos θ = m g."),
                  ("Divide: <b>tan θ = v²/(r g)</b>.", "ભાગાકાર કરો: <b>tan θ = v²/(r g)</b>.")),
               H4("With friction it is safer still", "ઘર્ષણ સાથે વધુ સલામત"),
               P("v<sub>max</sub> = √(r g (μ + tan θ)/(1 − μ tan θ)). With no banking (θ = 0) this "
                 "reduces to v<sub>max</sub> = √(μ r g).",
                 "v<sub>max</sub> = √(r g (μ + tan θ)/(1 − μ tan θ)). બેન્કિંગ ન હોય (θ = 0) તો તે "
                 "v<sub>max</sub> = √(μ r g) થાય."),
               H4("Worked example", "ઉકેલાયેલ દાખલો"),
               P("A curve of radius 100 m designed for 72 km/h (20 m/s): tan θ = 400/(100 × 9.8) = "
                 "0.408, so θ = 22.2°.",
                 "72 km/h (20 m/s) માટે રચાયેલ 100 m ત્રિજ્યાનો વળાંક: tan θ = 400/(100 × 9.8) = 0.408, "
                 "તેથી θ = 22.2°."),
               H4("Common mistake", "સામાન્ય ભૂલ"),
               P("Forgetting to convert km/h to m/s before squaring. 72 km/h is 20 m/s, and the square "
                 "is 400, not 5184.",
                 "વર્ગ કરતાં પહેલાં km/h ને m/s માં ફેરવવાનું ભૂલવું. 72 km/h એટલે 20 m/s, અને તેનો વર્ગ "
                 "400 છે, 5184 નહીં.")],
              "u2_banking", syllabus_item="2.3"),
         card(T("3.4 Centrifugal machines: pump, separator, governor",
                "3.4 કેન્દ્રત્યાગી મશીનો: પંપ, વિભાજક, ગવર્નર"),
              [H4("One idea, three machines", "એક ખ્યાલ, ત્રણ મશીન"),
               TB([T("Machine", "મશીન"), T("What the rotation does", "ભ્રમણ શું કરે"), T("Design quantity", "રચનાની રાશિ")],
                  [[T("centrifugal pump", "સેન્ટ્રિફ્યુગલ પંપ"), T("throws water outward into the casing", "પાણીને બહાર કેસિંગમાં ફેંકે"), T("head ∝ ω² r²", "હેડ ∝ ω² r²")],
                   [T("cream separator", "ક્રીમ વિભાજક"), T("heavier milk moves out, cream stays in", "ભારે દૂધ બહાર જાય, ક્રીમ અંદર રહે"), T("separation ∝ ω² r", "અલગીકરણ ∝ ω² r")],
                   [T("fly-ball governor", "ફ્લાય-બોલ ગવર્નર"), T("balls rise as speed rises", "ઝડપ વધે તેમ દડા ઉપર જાય"), T("lift ∝ ω² r", "ઉપર ઉઠવું ∝ ω² r")],
                   [T("spin dryer", "સ્પિન ડ્રાયર"), T("water leaves through the drum holes", "ડ્રમના છિદ્રોમાંથી પાણી નીકળે"), T("extraction ∝ ω² r", "નિષ્કર્ષણ ∝ ω² r")]]),
               H4("Worked example", "ઉકેલાયેલ દાખલો"),
               P("A separator of radius 0.1 m at 6000 rpm: ω = 628 rad/s and a = r ω² ≈ 39 400 m/s² ≈ "
                 "4000 g, which separates cream in seconds.",
                 "0.1 m ત્રિજ્યાનો વિભાજક 6000 rpm પર: ω = 628 rad/s અને a = r ω² ≈ 39 400 m/s² ≈ 4000 g, "
                 "જે ક્રીમને સેકન્ડોમાં અલગ કરે."),
               H4("The engineering catch", "ઇજનેરી ચેતવણી"),
               P("The load rises with the square of speed, so a 10 % overspeed means 21 % more stress. "
                 "That is why every one of these machines has a speed limit and a guard.",
                 "ભાર ઝડપના વર્ગ પ્રમાણે વધે, તેથી 10 % વધુ ઝડપ એટલે 21 % વધુ પ્રતિબળ. તેથી જ આ દરેક મશીન "
                 "પર ઝડપ મર્યાદા અને ગાર્ડ હોય છે."),
               H4("Common mistake", "સામાન્ય ભૂલ"),
               P("Sizing the motor from the flow alone. The casing and the impeller are sized by the "
                 "centrifugal pressure, which grows with ω².",
                 "ફક્ત પ્રવાહ પરથી મોટરનું માપ નક્કી કરવું. કેસિંગ અને ઇમ્પેલરનું માપ કેન્દ્રત્યાગી દબાણ "
                 "પ્રમાણે થાય, જે ω² સાથે વધે.")],
              syllabus_item="2.3"),
         card(T("3.5 Bending of a cyclist on a curve",
                "3.4 વળાંક પર સાયકલ સવારનું નમવું"),
              [H4("The physics", "ભૌતિકી"),
               P("A cyclist leans inward by an angle θ so that the resultant of weight m g and the "
                 "normal reaction passes through the line joining the tyre contact to the centre of "
                 "mass. Otherwise the torque would topple the cycle.",
                 "સાયકલ સવાર અંદર તરફ θ કોણે નમે છે જેથી વજન m g અને અભિલંબ પ્રતિક્રિયાનું પરિણામ ટાયરના "
                 "સંપર્કથી દ્રવ્યમાન કેન્દ્ર સુધીની રેખામાંથી પસાર થાય. નહીં તો ટોર્ક સાયકલને ઢોળી "
                 "નાખે."),
               P("<b>tan θ = v²/(r g)</b> — exactly the banking angle for the same speed and radius.",
                 "<b>tan θ = v²/(r g)</b> — તે જ ઝડપ અને ત્રિજ્યા માટે બેન્કિંગ કોણ જેટલું જ."),
               H4("Worked example", "ઉકેલાયેલ દાખલો"),
               P("At 5 m/s on a 10 m radius, tan θ = 25/98 = 0.255 and θ = 14.3° from the vertical.",
                 "10 m ત્રિજ્યા પર 5 m/s પર tan θ = 25/98 = 0.255 અને ઊર્ધ્વથી θ = 14.3°."),
               H4("Consequences an engineer uses", "ઇજનેર વાપરે તેવા પરિણામો"),
               UL(("Lean depends on v², so doubling the speed quadruples the lean.",
                   "નમવું v² પર આધારિત છે, તેથી ઝડપ બમણી કરો તો નમવું ચાર ગણું થાય."),
                  ("A loaded carrier needs the same lean angle but its higher centre of mass makes "
                   "the margin smaller.", "ભાર વહેતા વાહનને એ જ કોણ જોઈએ, પણ ઊંચું દ્રવ્યમાન કેન્દ્ર "
                   "માર્જિન ઘટાડે."),
                  ("Wet roads reduce μ, so the lean angle at which the tyre slips arrives earlier.",
                   "ભીના રસ્તા μ ઘટાડે, તેથી ટાયર લપસે તેવો કોણ વહેલો આવે.")),
               H4("Common mistake", "સામાન્ય ભૂલ"),
               P("Leaning outward, or thinking the lean is for balance only. The lean is what supplies "
                 "the centripetal force through the ground reaction.",
                 "બહાર તરફ નમવું, અથવા નમવું ફક્ત સંતુલન માટે છે એમ માનવું. નમવું એ જ જમીનની પ્રતિક્રિયા "
                 "દ્વારા કેન્દ્રગામી બળ પૂરું પાડે છે.")],
              syllabus_item="2.3"),
     ]},

    {"title": T("4. Circular Motion in the Workshop and on the Road",
                "4. કાર્યશાળા અને રસ્તા પર વર્તુળ ગતિ"),
     "items": [
         card(T("4.1 Choosing the right formula",
                "4.1 યોગ્ય સૂત્રની પસંદગી"),
              [H4("A decision table", "નિર્ણય કોષ્ટક"),
               TB([T("Question asks for", "પ્રશ્ન શું માગે"), T("Use", "વાપરો")],
                  [[T("momentum of a moving body", "ગતિમાન શરીરનું વેગમાન"), T("p = m v", "p = m v")],
                   [T("force from a change of momentum in time t", "સમય t માં વેગમાનના ફેરફારથી બળ"), T("F = Δp / t", "F = Δp / t")],
                   [T("recoil or explosion", "રીકોઇલ કે વિસ્ફોટ"), T("m₁v₁ + m₂v₂ = 0", "m₁v₁ + m₂v₂ = 0")],
                   [T("speed of a shaft in rpm", "શાફ્ટની ઝડપ rpm માં"), T("ω = 2πN/60", "ω = 2πN/60")],
                   [T("rim speed from angular speed", "કોણીય ઝડપથી કિનારની ઝડપ"), T("v = r ω", "v = r ω")],
                   [T("acceleration towards the centre", "કેન્દ્ર તરફનો પ્રવર્ગ"), T("a = v²/r = r ω²", "a = v²/r = r ω²")],
                   [T("maximum speed on a flat curve", "સપાટ વળાંક પર મહત્તમ ઝડપ"), T("v = √(μ r g)", "v = √(μ r g)")],
                   [T("banking angle", "બેન્કિંગ કોણ"), T("tan θ = v²/(r g)", "tan θ = v²/(r g)")]]),
               H4("Checklist before substituting", "આંકડા મૂકતાં પહેલાંની ચકાસણી"),
               OL(("Write every quantity in SI: m, kg, s, rad/s.", "દરેક રાશિ SIમાં લખો: m, kg, s, rad/s."),
                  ("Convert rpm to rad/s and km/h to m/s first.", "પહેલાં rpm ને rad/s અને km/h ને m/s માં ફેરવો."),
                  ("Decide the direction and keep signs for vectors.", "દિશા નક્કી કરો અને સદિશો માટે ચિહ્ન રાખો."),
                  ("Check the answer against a known case: a car on a 100 m curve is a few hundred kN of force, not a few newtons.",
                   "જાણીતી સ્થિતિ સાથે જવાબ ચકાસો: 100 m વળાંક પર કાર પર થોડા ન્યૂટન નહીં, થોડા લાખ ન્યૂટન બળ પડે.")),
               H4("Common mistake", "સામાન્ય ભૂલ"),
               P("Mixing units: 20 m/s with a radius in cm. Convert, then calculate.",
                 "એકમ ભેગાં કરવાં: 20 m/s સાથે ત્રિજ્યા cm માં. પહેલાં રૂપાંતરણ, પછી ગણતરી.")],
              syllabus_item="2.3"),
         card(T("4.2 Where circular motion decides a design",
                "4.2 વર્તુળ ગતિ કઈ રચના નક્કી કરે"),
              [H4("Five everyday examples", "પાંચ રોજિંદા ઉદાહરણ"),
               TB([T("Machine or situation", "મશીન કે પરિસ્થિતિ"), T("What is designed with it", "તેનાથી શું રચાય")],
                  [[T("centrifugal pump", "સેન્ટ્રિફ્યુગલ પંપ"), T("impeller radius sets the head at a given rpm", "આપેલ rpm પર ઇમ્પેલરની ત્રિજ્યા હેડ નક્કી કરે")],
                   [T("washing machine spin", "ધોવાના મશીનનું સ્પિન"), T("drum speed high enough for water to leave", "પાણી નીકળે તેટલી ડ્રમની ઝડપ")],
                   [T("road curve", "રસ્તાનો વળાંક"), T("banking angle and speed limit", "બેન્કિંગ કોણ અને ઝડપ મર્યાદા")],
                   [T("grinding wheel", "ઘંટીનું ચક્ર"), T("burst speed from safe rim velocity", "સલામત કિનાર ઝડપથી ફાટવાની ઝડપ")],
                   [T("roller bearing", "રોલર બેરિંગ"), T("centripetal load on the cage at speed", "ઝડપે કેજ પર કેન્દ્રગામી ભાર")]]),
               H4("Worked example: the speed limit of a curve", "ઉકેલાયેલ દાખલો: વળાંકની ઝડપ મર્યાદા"),
               P("A flat curve of radius 50 m with μ = 0.4: v = √(0.4 × 50 × 9.8) = 14 m/s = 50 km/h. "
                 "In rain μ falls to 0.25, giving 11 m/s = 40 km/h, which is why the sign shows two limits.",
                 "μ = 0.4 સાથે 50 m ત્રિજ્યાનો સપાટ વળાંક: v = √(0.4 × 50 × 9.8) = 14 m/s = 50 km/h. "
                 "વરસાદમાં μ ઘટીને 0.25 થાય, તેથી 11 m/s = 40 km/h — તેથી જ બોર્ડ પર બે મર્યાદા હોય છે."),
               H4("Common mistake", "સામાન્ય ભૂલ"),
               P("Designing for the posted speed only. Loaded trucks have a higher centre of mass and "
                 "roll over long before they slide.",
                 "ફક્ત લખેલી ઝડપ માટે રચના કરવી. ભરેલા ટ્રકનું દ્રવ્યમાન કેન્દ્ર ઊંચું હોય છે અને તે "
                 "લપસે તે પહેલાં ઊંધા પડે.")],
              syllabus_item="2.3"),
         card(T("4.3 What the exam asks from Unit 2",
                "4.3 યુનિટ 2 પરથી પરીક્ષામાં શું પૂછાય"),
              [H4("Question types", "પ્રશ્નના પ્રકાર"),
               TB([T("Question", "પ્રશ્ન"), T("What to write", "શું લખવું"), T("Marks", "માર્ક્સ")],
                  [[T("State and prove conservation of linear momentum", "રેખીય વેગમાનના સંરક્ષણનો નિયમ જણાવી સાબિત કરો"), T("statement + Newton's third law argument + equation", "વિધાન + ન્યૂટનના ત્રીજા નિયમની દલીલ + સમીકરણ"), T("4", "4")],
                   [T("Explain the recoil of a gun", "બંદૂકનો રીકોઇલ સમજાવો"), T("before/after momentum + formula + one numerical", "પહેલાં/પછીનું વેગમાન + સૂત્ર + એક દાખલો"), T("3-4", "3-4")],
                   [T("Define angular displacement, velocity, acceleration", "કોણીય સ્થાનાંતરણ, વેગ, પ્રવર્ગની વ્યાખ્યા"), T("three definitions with units + v = rω", "ત્રણ વ્યાખ્યા એકમ સાથે + v = rω"), T("3", "3")],
                   [T("Derive tan θ = v²/rg for a banked road", "બેન્ક કરેલા રસ્તા માટે tan θ = v²/rg સાબિત કરો"), T("resolved components + division + one line of meaning", "ઘટકો + ભાગાકાર + એક લાઇન અર્થ"), T("4-7", "4-7")],
                   [T("Numerical on centripetal force", "કેન્દ્રગામી બળ પર દાખલો"), T("formula, substitution, unit, direction", "સૂત્ર, આંકડા, એકમ, દિશા"), T("3-4", "3-4")]]),
               H4("Time plan for a 7-mark answer", "7 માર્કના જવાબનો સમય પ્લાન"),
               OL(("Statement and the one assumption (no external force).", "વિધાન અને એક ધારણા (બાહ્ય બળ નહીં)."),
                  ("A labelled diagram with before and after.", "પહેલાં અને પછી દર્શાવતું લેબલવાળું ચિત્ર."),
                  ("The equation, then one substitution with units.", "સમીકરણ, પછી એકમ સાથે એક આંકડા મૂકવા."),
                  ("One engineering application in a sentence.", "એક વાક્યમાં એક ઇજનેરી ઉપયોગ.")),
               H4("Common mistake", "સામાન્ય ભૂલ"),
               P("Writing only the formula. The marks for a derivation sit in the resolved components "
                 "and the division step.",
                 "ફક્ત સૂત્ર લખવું. સાબિતીના માર્ક્સ ઘટકો પાડવામાં અને ભાગાકારના પગલામાં છે.")],
              syllabus_item="2.1"),
     ]},

    {"title": T("5. Practice Questions with Model Answers", "5. સરાવ પ્રશ્નો અને આદર્શ જવાબો"),
     "items": []},
]

NUMERICALS = [
    num("u2n01", T("Momentum of a 1500 kg car at 20 m/s.", "20 m/s પર 1500 kg કારનું વેગમાન."),
        T("A car of mass 1500 kg moves at 20 m/s. Find its linear momentum.",
          "1500 kg દ્રવ્યમાનની કાર 20 m/s પર ચાલે છે. તેનું રેખીય વેગમાન શોધો."),
        [P("p = m v = 1500 × 20", "p = m v = 1500 × 20"),
         P("= 30 000 kg·m/s, along the velocity.", "= 30 000 kg·m/s, વેગની દિશામાં.")],
        T("30 000 kg·m/s", "30 000 kg·m/s"), unit_no=2),
    num("u2n02", T("Impulse needed to stop that car in 5 s.", "તે કારને 5 sમાં ઊભી કરવા જરૂરી આઘાત."),
        T("The same 1500 kg car at 20 m/s is brought to rest in 5 s. Find the impulse and the force.",
          "એ જ 1500 kg કાર 20 m/s થી 5 sમાં ઊભી કરાય છે. આઘાત અને બળ શોધો."),
        [P("Impulse J = Δp = 30 000 − 0 = 30 000 N·s", "આઘાત J = Δp = 30 000 − 0 = 30 000 N·s"),
         P("F = J/t = 30 000/5 = 6000 N", "F = J/t = 30 000/5 = 6000 N"),
         P("The force opposes the motion, so the car stops.", "બળ ગતિની વિરુદ્ધ છે, તેથી કાર ઊભી રહે.")],
        T("30 000 N·s and 6000 N", "30 000 N·s અને 6000 N"), unit_no=2),
    num("u2n03", T("Change of momentum of a rebounding ball.",
                   "પાછો ઉછળતા બોલના વેગમાનમાં ફેરફાર."),
        T("A 0.15 kg ball hits a wall at 20 m/s and rebounds at 20 m/s opposite. Find the change of "
          "momentum and the force if contact lasts 0.02 s.",
          "0.15 kg નો બોલ 20 m/s પર દીવાલે અથડાઈને વિરુદ્ધ દિશામાં 20 m/s પર પાછો આવે છે. વેગમાનનો ફેરફાર "
          "અને 0.02 s સંપર્ક માટે બળ શોધો."),
        [P("Take the incoming direction as positive: u = +20 m/s, v = −20 m/s.",
           "આવતી દિશાને ધન ગણો: u = +20 m/s, v = −20 m/s."),
         P("Δp = m(v − u) = 0.15 × (−20 − 20) = −6 N·s", "Δp = m(v − u) = 0.15 × (−20 − 20) = −6 N·s"),
         P("Magnitude 6 N·s; F = 6/0.02 = 300 N.", "મૂલ્ય 6 N·s; F = 6/0.02 = 300 N.")],
        T("6 N·s and 300 N", "6 N·s અને 300 N"), unit_no=2),
    num("u2n04", T("Recoil velocity of a 5 kg rifle.", "5 kg રાયફલનો રીકોઇલ વેગ."),
        T("A 20 g bullet leaves a 5 kg rifle at 400 m/s. Find the recoil velocity of the rifle.",
          "20 g ગોળી 5 kg રાયફલમાંથી 400 m/s પર નીકળે છે. રાયફલનો રીકોઇલ વેગ શોધો."),
        [P("Before firing, total momentum = 0.", "ચલાવતા પહેલાં કુલ વેગમાન = 0."),
         P("After: m v + M V = 0, so V = −m v/M", "પછી: m v + M V = 0, તેથી V = −m v/M"),
         P("V = −(0.020 × 400)/5 = −1.6 m/s", "V = −(0.020 × 400)/5 = −1.6 m/s")],
        T("1.6 m/s backwards", "1.6 m/s પાછળ તરફ"), unit_no=2),
    num("u2n05", T("Two trolleys sticking together.", "ચોંટતી બે ટ્રોલી."),
        T("A 2 kg trolley at 3 m/s collides with a stationary 1 kg trolley and they move together. "
          "Find the common velocity.",
          "2 kg ટ્રોલી 3 m/s પર સ્થિર 1 kg ટ્રોલી સાથે અથડાઈને સાથે ચાલે છે. સામાન્ય વેગ શોધો."),
        [P("m₁u₁ + m₂u₂ = (m₁ + m₂)v", "m₁u₁ + m₂u₂ = (m₁ + m₂)v"),
         P("2 × 3 + 1 × 0 = 3 v", "2 × 3 + 1 × 0 = 3 v"),
         P("v = 6/3 = 2 m/s in the original direction", "v = 6/3 = 2 m/s પહેલાની દિશામાં")],
        T("2 m/s", "2 m/s"), unit_no=2),
    num("u2n06", T("Shaft speed 300 rpm in rad/s.", "300 rpm શાફ્ટની ઝડપ rad/s માં."),
        T("A shaft turns at 300 revolutions per minute. Find its angular velocity.",
          "શાફ્ટ 300 પરિભ્રમણ પ્રતિ મિનિટ ફરે છે. તેનો કોણીય વેગ શોધો."),
        [P("ω = 2πN/60", "ω = 2πN/60"),
         P("= 2π × 300/60 = 10π", "= 2π × 300/60 = 10π"),
         P("= 31.4 rad/s", "= 31.4 rad/s")],
        T("31.4 rad/s", "31.4 rad/s"), unit_no=2),
    num("u2n07", T("Rim speed of a 0.4 m pulley at 300 rpm.", "300 rpm પર 0.4 m ગરગડીની કિનાર ઝડપ."),
        T("The pulley of radius 0.4 m is on the shaft of 31.4 rad/s. Find the speed of a point on its rim.",
          "0.4 m ત્રિજ્યાની ગરગડી 31.4 rad/s ની શાફ્ટ પર છે. તેની કિનાર પરના બિંદુની ઝડપ શોધો."),
        [P("v = r ω = 0.4 × 31.4", "v = r ω = 0.4 × 31.4"),
         P("= 12.6 m/s", "= 12.6 m/s")],
        T("12.6 m/s", "12.6 m/s"), unit_no=2),
    num("u2n08", T("Angular velocity for a period of 0.5 s.", "0.5 s આવર્તકાળ માટે કોણીય વેગ."),
        T("A body completes one revolution in 0.5 s. Find its angular velocity and frequency.",
          "શરીર 0.5 sમાં એક પરિભ્રમણ પૂરું કરે છે. તેનો કોણીય વેગ અને આવૃત્તિ શોધો."),
        [P("ω = 2π/T = 2π/0.5", "ω = 2π/T = 2π/0.5"),
         P("= 12.57 rad/s", "= 12.57 rad/s"),
         P("n = 1/T = 2 Hz", "n = 1/T = 2 Hz")],
        T("12.57 rad/s and 2 Hz", "12.57 rad/s અને 2 Hz"), unit_no=2),
    num("u2n09", T("Angular acceleration of a wheel spun up in 4 s.",
                   "4 sમાં ઝડપ પકડતા ચક્રનો કોણીય પ્રવર્ગ."),
        T("A wheel at rest reaches 20 rad/s in 4 s. Find its angular acceleration and the angle turned.",
          "સ્થિર ચક્ર 4 sમાં 20 rad/s પર પહોંચે છે. તેનો કોણીય પ્રવર્ગ અને ઘૂમેલો કોણ શોધો."),
        [P("α = (ω − ω₀)/t = 20/4 = 5 rad/s²", "α = (ω − ω₀)/t = 20/4 = 5 rad/s²"),
         P("θ = ω₀t + ½αt² = 0 + ½ × 5 × 16 = 40 rad", "θ = ω₀t + ½αt² = 0 + ½ × 5 × 16 = 40 rad"),
         P("40 rad is 6.37 revolutions.", "40 રેડિયન એટલે 6.37 પરિભ્રમણ.")],
        T("5 rad/s² and 40 rad", "5 rad/s² અને 40 rad"), unit_no=2),
    num("u2n10", T("Tangential acceleration on a 0.3 m wheel.",
                   "0.3 m ચક્ર પર સ્પર્શીય પ્રવર્ગ."),
        T("A wheel of radius 0.3 m has an angular acceleration of 2 rad/s². Find the tangential "
          "acceleration of a point on its rim.",
          "0.3 m ત્રિજ્યાના ચક્રનો કોણીય પ્રવર્ગ 2 rad/s² છે. કિનાર પરના બિંદુનો સ્પર્શીય પ્રવર્ગ શોધો."),
        [P("a = r α = 0.3 × 2", "a = r α = 0.3 × 2"),
         P("= 0.6 m/s² along the tangent", "= 0.6 m/s² સ્પર્શની દિશામાં")],
        T("0.6 m/s²", "0.6 m/s²"), unit_no=2),
    num("u2n11", T("Centripetal acceleration at 10 m/s on a 20 m circle.",
                   "20 m વર્તુળ પર 10 m/s પર કેન્દ્રગામી પ્રવર્ગ."),
        T("A body moves at 10 m/s on a circle of radius 20 m. Find its centripetal acceleration.",
          "શરીર 20 m ત્રિજ્યાના વર્તુળ પર 10 m/s પર ચાલે છે. તેનો કેન્દ્રગામી પ્રવર્ગ શોધો."),
        [P("a = v²/r = 10²/20", "a = v²/r = 10²/20"),
         P("= 5 m/s² towards the centre", "= 5 m/s² કેન્દ્ર તરફ")],
        T("5 m/s²", "5 m/s²"), unit_no=2),
    num("u2n12", T("Tension in a string whirling a 0.2 kg stone.",
                   "0.2 kg પથ્થર ફેરવતી દોરીમાં તણાવ."),
        T("A 0.2 kg stone on a 0.5 m string moves at 4 m/s in a horizontal circle. Find the tension.",
          "0.5 m દોરી પરનો 0.2 kg પથ્થર સમક્ષિતિજ વર્તુળમાં 4 m/s પર ફરે છે. તણાવ શોધો."),
        [P("Centripetal force is supplied by the tension.", "કેન્દ્રગામી બળ દોરીનો તણાવ પૂરો પાડે છે."),
         P("T = m v²/r = 0.2 × 16/0.5", "T = m v²/r = 0.2 × 16/0.5"),
         P("= 6.4 N", "= 6.4 N")],
        T("6.4 N", "6.4 N"), unit_no=2),
    num("u2n13", T("Maximum speed on a flat curve of 50 m, μ = 0.4.",
                   "50 m સપાટ વળાંક પર મહત્તમ ઝડપ, μ = 0.4."),
        T("A car takes a flat curve of radius 50 m where μ = 0.4. Find the maximum speed without "
          "skidding.", "કાર 50 m ત્રિજ્યાના સપાટ વળાંક પર ફરે છે જ્યાં μ = 0.4 છે. લપસ્યા વગરની મહત્તમ ઝડપ શોધો."),
        [P("Friction supplies m v²/r and can be at most μ m g.", "ઘર્ષણ m v²/r પૂરું પાડે અને વધુમાં વધુ μ m g હોઈ શકે."),
         P("v² = μ r g = 0.4 × 50 × 9.8 = 196", "v² = μ r g = 0.4 × 50 × 9.8 = 196"),
         P("v = 14 m/s = 50.4 km/h", "v = 14 m/s = 50.4 km/h")],
        T("14 m/s (about 50 km/h)", "14 m/s (લગભગ 50 km/h)"), unit_no=2),
    num("u2n14", T("Banking angle for 20 m/s on a 100 m curve.",
                   "100 m વળાંક પર 20 m/s માટે બેન્કિંગ કોણ."),
        T("A curve of radius 100 m is designed for 20 m/s with no friction. Find the banking angle.",
          "100 m ત્રિજ્યાનો વળાંક ઘર્ષણ વગર 20 m/s માટે રચાય છે. બેન્કિંગ કોણ શોધો."),
        [P("tan θ = v²/(r g) = 400/(100 × 9.8)", "tan θ = v²/(r g) = 400/(100 × 9.8)"),
         P("= 0.408", "= 0.408"),
         P("θ = tan⁻¹ 0.408 = 22.2°", "θ = tan⁻¹ 0.408 = 22.2°")],
        T("22.2°", "22.2°"), unit_no=2),
    num("u2n15", T("Lean of a cyclist at 5 m/s on a 10 m curve.",
                   "10 m વળાંક પર 5 m/s પર સાયકલ સવારનું નમવું."),
        T("A cyclist takes a curve of radius 10 m at 5 m/s. At what angle must he lean?",
          "સાયકલ સવાર 10 m ત્રિજ્યાનો વળાંક 5 m/s પર લે છે. તેણે કેટલા કોણે નમવું જોઈએ?"),
        [P("tan θ = v²/(r g) = 25/(10 × 9.8)", "tan θ = v²/(r g) = 25/(10 × 9.8)"),
         P("= 0.255", "= 0.255"),
         P("θ = 14.3° from the vertical", "ઊર્ધ્વથી θ = 14.3°")],
        T("14.3°", "14.3°"), unit_no=2),
    num("u2n16", T("Angle turned in 5 revolutions.", "5 પરિભ્રમણમાં ઘૂમેલો કોણ."),
        T("A wheel makes 5 revolutions. Express the angular displacement in radians and degrees.",
          "ચક્ર 5 પરિભ્રમણ કરે છે. કોણીય સ્થાનાંતરણ રેડિયન અને અંશમાં દર્શાવો."),
        [P("θ = 5 × 2π = 10π", "θ = 5 × 2π = 10π"),
         P("= 31.4 rad", "= 31.4 rad"),
         P("= 5 × 360° = 1800°", "= 5 × 360° = 1800°")],
        T("31.4 rad = 1800°", "31.4 rad = 1800°"), unit_no=2),
    num("u2n17", T("Angular velocity of the earth on its axis.",
                   "પોતાની ધરી પર પૃથ્વીનો કોણીય વેગ."),
        T("The earth turns once in 24 hours. Find its angular velocity.",
          "પૃથ્વી 24 કલાકમાં એક વાર ફરે છે. તેનો કોણીય વેગ શોધો."),
        [P("T = 24 × 3600 = 86 400 s", "T = 24 × 3600 = 86 400 s"),
         P("ω = 2π/T = 6.283/86 400", "ω = 2π/T = 6.283/86 400"),
         P("= 7.27 × 10⁻⁵ rad/s", "= 7.27 × 10⁻⁵ rad/s")],
        T("7.27 × 10⁻⁵ rad/s", "7.27 × 10⁻⁵ rad/s"), unit_no=2),
    num("u2n18", T("Centripetal force on a 1200 kg car at 15 m/s on a 45 m curve.",
                   "45 m વળાંક પર 15 m/s પર 1200 kg કાર પર કેન્દ્રગામી બળ."),
        T("A 1200 kg car takes a curve of radius 45 m at 15 m/s. Find the centripetal force needed.",
          "1200 kg કાર 45 m ત્રિજ્યાનો વળાંક 15 m/s પર લે છે. જરૂરી કેન્દ્રગામી બળ શોધો."),
        [P("F = m v²/r = 1200 × 225/45", "F = m v²/r = 1200 × 225/45"),
         P("= 6000 N", "= 6000 N"),
         P("That force must come from friction: μ needed = 6000/(1200 × 9.8) = 0.51.",
           "એ બળ ઘર્ષણમાંથી આવવું જોઈએ: જરૂરી μ = 6000/(1200 × 9.8) = 0.51.")],
        T("6000 N (μ ≥ 0.51)", "6000 N (μ ≥ 0.51)"), unit_no=2),
    num("u2n19", T("Force on a wall from a ball bouncing every 0.5 s.",
                   "દર 0.5 sે ઉછળતા બોલથી દીવાલ પર બળ."),
        T("A 0.2 kg ball hits a wall at 10 m/s and rebounds at 10 m/s, repeating every 0.5 s. Find the "
          "average force on the wall.",
          "0.2 kg બોલ 10 m/s પર દીવાલે અથડાઈને 10 m/s પર પાછો આવે છે અને દર 0.5 sે પુનરાવર્તન થાય છે. "
          "દીવાલ પર સરેરાશ બળ શોધો."),
        [P("Δp per hit = m(v − u) = 0.2 × (−10 − 10) = −4 kg·m/s",
           "દરેક અથડામણમાં Δp = m(v − u) = 0.2 × (−10 − 10) = −4 kg·m/s"),
         P("Average force = |Δp|/t = 4/0.5", "સરેરાશ બળ = |Δp|/t = 4/0.5"),
         P("= 8 N on the wall, opposite to the ball's return.", "= 8 N દીવાલ પર, બોલના પરત ફરવાની વિરુદ્ધ.")],
        T("8 N", "8 N"), unit_no=2),
]

EQUATIONS = [
    {"title": T("Momentum, impulse and collisions", "વેગમાન, આઘાત અને અથડામણ"),
     "items": [
         {"name": T("Linear momentum", "રેખીય વેગમાન"), "f": "p = m v",
          "terms": T("A vector along the velocity, unit kg·m/s.",
                     "વેગની દિશામાં સદિશ, એકમ kg·m/s.")},
         {"name": T("Force", "બળ"), "f": "F = dp/dt = m a",
          "terms": T("Rate of change of momentum.", "વેગમાનના ફેરફારનો દર.")},
         {"name": T("Impulse", "આઘાત"), "f": "J = F t = Δp = m(v − u)",
          "terms": T("Same Δp over a longer time means a smaller force.",
                     "એ જ Δp લાંબા સમયમાં એટલે નાનું બળ.")},
         {"name": T("Conservation of momentum", "વેગમાનનું સંરક્ષણ"),
          "f": "m₁u₁ + m₂u₂ = m₁v₁ + m₂v₂",
          "terms": T("Valid when no external force acts.", "બાહ્ય બળ ન હોય ત્યારે માન્ય.")},
         {"name": T("Recoil of a gun", "બંદૂકનો રીકોઇલ"), "f": "V = − m v / M",
          "terms": T("The gun moves back with the bullet's momentum.",
                     "બંદૂક ગોળીના વેગમાન સાથે પાછી ખસે.")},
     ]},
    {"title": T("Circular motion", "વર્તુળ ગતિ"),
     "items": [
         {"name": T("Arc and angle", "ચાપ અને કોણ"), "f": "s = r θ",
          "terms": T("θ must be in radians.", "θ રેડિયનમાં હોવો જોઈએ.")},
         {"name": T("Angular velocity", "કોણીય વેગ"), "f": "ω = Δθ/Δt = 2π/T = 2πN/60",
          "terms": T("N is revolutions per minute.", "N પ્રતિ મિનિટ પરિભ્રમણ છે.")},
         {"name": T("Angular acceleration", "કોણીય પ્રવર્ગ"), "f": "α = Δω/Δt",
          "terms": T("Unit rad/s².", "એકમ rad/s².")},
         {"name": T("Line and circle", "રેખા અને વર્તુળ"), "f": "v = r ω,  a = r α",
          "terms": T("Rim speed and tangential acceleration.", "કિનારની ઝડપ અને સ્પર્શીય પ્રવર્ગ.")},
         {"name": T("Centripetal force", "કેન્દ્રગામી બળ"), "f": "F = m v²/r = m r ω²",
          "terms": T("Directed towards the centre.", "કેન્દ્ર તરફ દિશિત.")},
         {"name": T("Banking, no friction", "બેન્કિંગ, ઘર્ષણ વગર"), "f": "tan θ = v²/(r g)",
          "terms": T("Same angle for a cyclist leaning into the curve.",
                     "વળાંકમાં નમતા સાયકલ સવાર માટે એ જ કોણ.")},
         {"name": T("Flat curve, friction only", "સપાટ વળાંક, ફક્ત ઘર્ષણ"),
          "f": "v_max = √(μ r g)",
          "terms": T("Wet roads lower μ and lower the limit.", "ભીના રસ્તા μ ઘટાડે અને મર્યાદા ઘટાડે.")},
         {"name": T("Banked curve with friction", "ઘર્ષણ સાથે બેન્ક કરેલો વળાંક"),
          "f": "v_max = √(r g (μ + tan θ)/(1 − μ tan θ))",
          "terms": T("Reduces to √(μ r g) when θ = 0.", "θ = 0 હોય તો √(μ r g) થાય.")},
     ]},
]

VIVA = [
    {"title": T("Momentum and impulse", "વેગમાન અને આઘાત"),
     "items": [
         {"q": T("Define linear momentum and give its unit.",
                 "રેખીય વેગમાનની વ્યાખ્યા આપો અને તેનો એકમ જણાવો."),
          "a": T("The product of mass and velocity, p = m v, a vector along the velocity, measured in "
                 "kg·m/s.",
                 "દ્રવ્યમાન અને વેગનો ગુણાકાર, p = m v, વેગની દિશામાં સદિશ, kg·m/s માં મપાય.")},
         {"q": T("State Newton's second law in terms of momentum.",
                 "વેગમાનના સંદર્ભમાં ન્યૂટનનો બીજો નિયમ જણાવો."),
          "a": T("The rate of change of momentum of a body is equal to the applied force and takes "
                 "place in the direction of the force: F = dp/dt.",
                 "શરીરના વેગમાનના ફેરફારનો દર લાગુ બળ જેટલો હોય છે અને બળની દિશામાં થાય છે: F = dp/dt.")},
         {"q": T("What is impulse, and how is it useful in vehicle safety?",
                 "આઘાત શું છે અને વાહન સલામતીમાં કેમ ઉપયોગી છે?"),
          "a": T("Impulse is force × time and equals the change of momentum. An airbag or crumple "
                 "zone stretches the same Δp over a longer time, so the force on the body falls.",
                 "આઘાત એટલે બળ × સમય અને તે વેગમાનના ફેરફાર જેટલો. એરબેગ કે ક્રમ્પલ ઝોન એ જ Δp લાંબા સમય "
                 "સુધી ફેલાવે, તેથી શરીર પરનું બળ ઘટે.")},
         {"q": T("State the law of conservation of linear momentum.",
                 "રેખીય વેગમાનના સંરક્ષણનો નિયમ જણાવો."),
          "a": T("If no external force acts on a system, the total linear momentum of the system stays "
                 "constant, which gives m₁u₁ + m₂u₂ = m₁v₁ + m₂v₂ for two bodies.",
                 "જો સિસ્ટમ પર બાહ્ય બળ ન લાગે તો કુલ રેખીય વેગમાન અચળ રહે, જે બે શરીરો માટે "
                 "m₁u₁ + m₂u₂ = m₁v₁ + m₂v₂ આપે.")},
         {"q": T("Why does a gun recoil?", "બંદૂક પાછી કેમ ખસે?"),
          "a": T("The total momentum before firing is zero, so after firing the bullet's forward "
                 "momentum must be balanced by the gun's backward momentum; the gun's velocity is "
                 "smaller by the mass ratio M/m.",
                 "ચલાવતા પહેલાં કુલ વેગમાન શૂન્ય છે, તેથી પછી ગોળીના આગળના વેગમાનની સામે બંદૂકના પાછળના "
                 "વેગમાને સંતુલન કરવું પડે; દ્રવ્યમાન ગુણોત્તર M/m જેટલો બંદૂકનો વેગ નાનો હોય.")},
         {"q": T("Give one example of momentum conservation in engineering.",
                 "ઇજનેરીમાં વેગમાન સંરક્ષણનું એક ઉદાહરણ આપો."),
          "a": T("A rocket: exhaust leaves backwards, so the rocket gains equal forward momentum; the "
                 "same equation gives the thrust of a water jet or a hose.",
                 "રોકેટ: એક્ઝોસ્ટ પાછળ નીકળે, તેથી રોકેટ સમાન આગળનું વેગમાન મેળવે; એ જ સમીકરણ પાણીના જેટ "
                 "કે પાઇપનું થ્રસ્ટ આપે.")},
     ]},
    {"title": T("Circular motion", "વર્તુળ ગતિ"),
     "items": [
         {"q": T("Define angular displacement and its unit.",
                 "કોણીય સ્થાનાંતરણ અને તેનો એકમ જણાવો."),
          "a": T("The angle swept by the radius, measured in radians where one radian cuts an arc "
                 "equal to the radius.",
                 "ત્રિજ્યા દ્વારા ઘૂમાયેલો કોણ, રેડિયનમાં મપાય જ્યાં એક રેડિયન ત્રિજ્યા જેટલી ચાપ કાપે.")},
         {"q": T("Write the relation between linear and angular velocity.",
                 "રેખીય અને કોણીય વેગ વચ્ચેનો સંબંધ લખો."),
          "a": T("v = r ω, with ω in rad/s; for a shaft at N rpm, ω = 2πN/60.",
                 "v = r ω, ω rad/s માં; N rpm પરની શાફ્ટ માટે ω = 2πN/60.")},
         {"q": T("What is centripetal force, and who supplies it for a car on a curve?",
                 "કેન્દ્રગામી બળ શું છે અને વળાંક પરની કાર માટે તે કોણ પૂરું પાડે?"),
          "a": T("The inward force F = m v²/r that keeps a body on the circle; for a car it is "
                 "friction between the tyres and the road, helped by banking.",
                 "શરીરને વર્તુળ પર રાખતું અંદર તરફનું બળ F = m v²/r; કાર માટે તે ટાયર અને રસ્તા વચ્ચેનું "
                 "ઘર્ષણ છે, જેને બેન્કિંગ મદદ કરે.")},
         {"q": T("Is centrifugal force a real force?", "કેન્દ્રત્યાગી બળ સાચું બળ છે?"),
          "a": T("No. It is a pseudo force that appears only in a rotating frame, equal to m v²/r and "
                 "directed outward; in the ground frame only the inward centripetal force exists.",
                 "ના. તે આભાસી બળ છે જે ફક્ત ફરતી ફ્રેમમાં દેખાય, m v²/r જેટલું અને બહાર તરફ; જમીનની ફ્રેમમાં "
                 "ફક્ત અંદર તરફનું કેન્દ્રગામી બળ હોય.")},
         {"q": T("Why are roads banked on curves?", "વળાંક પર રસ્તા કેમ બેન્ક કરાય?"),
          "a": T("Banking lets the normal reaction supply part of the centripetal force, so the curve "
                 "can be taken faster and with less dependence on friction, which matters on wet roads.",
                 "બેન્કિંગથી અભિલંબ પ્રતિક્રિયા કેન્દ્રગામી બળનો ભાગ પૂરો પાડે, તેથી વળાંક વધુ ઝડપે અને "
                 "ઘર્ષણ પર ઓછા આધારે લઈ શકાય, જે ભીના રસ્તે મહત્વનું છે.")},
         {"q": T("At what angle does a cyclist lean, and why?",
                 "સાયકલ સવાર કેટલા કોણે નમે છે અને કેમ?"),
          "a": T("He leans inward by θ with tan θ = v²/(r g) so that the resultant of weight and "
                 "ground reaction passes through the centre of mass; otherwise the torque would "
                 "topple the cycle.",
                 "તે અંદર તરફ θ નમે છે જ્યાં tan θ = v²/(r g), જેથી વજન અને જમીનની પ્રતિક્રિયાનું પરિણામ "
                 "દ્રવ્યમાન કેન્દ્રમાંથી પસાર થાય; નહીં તો ટોર્ક સાયકલ ઢોળી નાખે.")},
     ]},
]

_PRACTICE = [
    (T("State and explain the law of conservation of linear momentum with one example.",
       "રેખીય વેગમાનના સંરક્ષણનો નિયમ જણાવીને એક ઉદાહરણ સાથે સમજાવો."),
     4,
     [P("If no external force acts on a system, its total linear momentum remains constant: "
        "m₁u₁ + m₂u₂ = m₁v₁ + m₂v₂.",
        "જો સિસ્ટમ પર બાહ્ય બળ ન લાગે તો તેનું કુલ રેખીય વેગમાન અચળ રહે: m₁u₁ + m₂u₂ = m₁v₁ + m₂v₂."),
      P("It follows from Newton's third law. During an interaction the two bodies exert equal and "
        "opposite forces for the same time, so the two impulses are equal and opposite and cancel; "
        "the momentum gained by one is exactly the momentum lost by the other.",
        "તે ન્યૂટનના ત્રીજા નિયમમાંથી નીકળે. ક્રિયાપ્રતિક્રિયા દરમિયાન બંને શરીરો સમાન સમય માટે સમાન અને "
        "વિરુદ્ધ બળ લગાડે, તેથી બંને આઘાત સમાન અને વિરુદ્ધ હોઈ રદ થાય; એકે મેળવેલું વેગમાન બીજાએ ગુમાવેલા "
        "વેગમાન જેટલું જ હોય."),
      P("Example: a 20 g bullet leaving a 5 kg rifle at 400 m/s gives the rifle a recoil of "
        "0.020 × 400/5 = 1.6 m/s backwards, because the total momentum must stay zero.",
        "ઉદાહરણ: 20 g ગોળી 5 kg રાયફલમાંથી 400 m/s પર નીકળે તો રાયફલને 0.020 × 400/5 = 1.6 m/s પાછળનો "
        "રીકોઇલ મળે, કારણ કે કુલ વેગમાન શૂન્ય જ રહેવું જોઈએ.")]),
    (T("Define impulse and show that it equals the change of momentum.",
       "આઘાતની વ્યાખ્યા આપો અને તે વેગમાનના ફેરફાર જેટલો છે તે દર્શાવો."),
     4,
     [P("Impulse is the product of a force and the time for which it acts: J = F × t, measured in "
        "N·s.",
        "આઘાત એ બળ અને તે લાગે તે સમયનો ગુણાકાર છે: J = F × t, એકમ N·s."),
      P("From Newton's second law F = Δp/Δt, so F t = Δp and therefore J = m v − m u.",
        "ન્યૂટનના બીજા નિયમ F = Δp/Δt પરથી F t = Δp, તેથી J = m v − m u."),
      P("This is why an airbag works: the same Δp spread over 0.2 s instead of 0.02 s cuts the force "
        "by a factor of ten and keeps the occupant inside the survival limit.",
        "તેથી જ એરબેગ કામ કરે: એ જ Δp 0.02 s ને બદલે 0.2 s સુધી ફેલાય તો બળ દશ ગણું ઘટે અને મુસાફર "
        "જીવિત રહે તે મર્યાદામાં રહે."),
      P("Worked check: a 0.15 kg ball arriving at 20 m/s and leaving at 20 m/s the other way changes "
        "momentum by 6 N·s, so stopping it in 0.02 s needs 300 N and in 0.2 s only 30 N.",
        "ઉકેલાયેલ ચકાસણી: 0.15 kg બોલ 20 m/s પર આવીને વિરુદ્ધ દિશામાં 20 m/s પર જાય તો વેગમાનમાં 6 N·s "
        "ફેરફાર થાય, તેથી 0.02 sમાં ઊભો કરવા 300 N અને 0.2 sમાં ફક્ત 30 N જોઈએ.")]),
    (T("Explain the recoil of a gun using conservation of momentum.",
       "વેગમાનના સંરક્ષણનો ઉપયોગ કરીને બંદૂકનો રીકોઇલ સમજાવો."),
     4,
     [P("Before firing, the gun and the bullet are at rest, so the total momentum is zero.",
        "ચલાવતા પહેલાં બંદૂક અને ગોળી સ્થિર છે, તેથી કુલ વેગમાન શૂન્ય છે."),
      P("After firing, 0 = m v + M V, so V = −m v/M: the gun moves backwards with equal momentum.",
        "ચલાવ્યા પછી 0 = m v + M V, તેથી V = −m v/M: બંદૂક સમાન વેગમાન સાથે પાછળ ખસે છે."),
      P("The negative sign only fixes the direction. Because M ≫ m the recoil speed is small, but the "
        "recoil energy m²v²/2M still has to be absorbed by the shoulder or the recoil spring.",
        "ઋણ ચિહ્ન ફક્ત દિશા બતાવે છે. M ≫ m હોવાથી રીકોઇલની ઝડપ નાની છે, પણ રીકોઇલની ઊર્જા m²v²/2M "
        "છતાં ખભા કે રીકોઇલ સ્પ્રિંગે શોષવી પડે.")]),
    (T("Define angular displacement, angular velocity and angular acceleration, and give their "
       "relations with the linear quantities.",
       "કોણીય સ્થાનાંતરણ, કોણીય વેગ અને કોણીય પ્રવર્ગની વ્યાખ્યા આપી રેખીય રાશિઓ સાથેનો સંબંધ જણાવો."),
     5,
     [P("Angular displacement θ is the angle swept by the radius, in radians; angular velocity "
        "ω = Δθ/Δt in rad/s; angular acceleration α = Δω/Δt in rad/s².",
        "કોણીય સ્થાનાંતરણ θ એ ત્રિજ્યા દ્વારા ઘૂમાયેલો કોણ, રેડિયનમાં; કોણીય વેગ ω = Δθ/Δt, "
        "rad/s માં; કોણીય પ્રવર્ગ α = Δω/Δt, rad/s² માં."),
      P("The links are s = r θ, v = r ω and a = r α. Every point on a rigid rotating body has the same "
        "ω and α but a different v and a, proportional to its distance from the axis.",
        "સંબંધ s = r θ, v = r ω અને a = r α છે. કઠણ ફરતા શરીરના દરેક બિંદુનું ω અને α સમાન હોય, પણ v "
        "અને a ધરીથી અંતર પ્રમાણે જુદા હોય."),
      P("For a shaft at N rpm, ω = 2πN/60; 300 rpm is 31.4 rad/s, and a 0.4 m pulley on it gives a rim "
        "speed of 12.6 m/s.",
        "N rpm પરની શાફ્ટ માટે ω = 2πN/60; 300 rpm એટલે 31.4 rad/s, અને તેના 0.4 m ગરગડીની કિનાર ઝડપ "
        "12.6 m/s.")]),
    (T("Derive the expression for the banking angle of a road and state what happens when friction is "
       "also present.", "રસ્તાના બેન્કિંગ કોણનું સૂત્ર સાબિત કરો અને ઘર્ષણ હાજર હોય ત્યારે શું થાય તે જણાવો."),
     5,
     [P("On a road banked at θ, the normal reaction N is perpendicular to the surface. Resolving "
        "vertically and horizontally: N cos θ = m g and N sin θ = m v²/r.",
        "θ કોણે બેન્ક કરેલા રસ્તા પર અભિલંબ પ્રતિક્રિયા N સપાટીને લંબ છે. ઊર્ધ્વ અને સમક્ષિતિજ ઘટકો: "
        "N cos θ = m g અને N sin θ = m v²/r."),
      P("Dividing the second by the first removes N and m: tan θ = v²/(r g). For r = 100 m and "
        "v = 20 m/s this gives tan θ = 0.408, that is θ = 22.2°.",
        "બીજાને પહેલાથી ભાગતાં N અને m જતાં રહે: tan θ = v²/(r g). r = 100 m અને v = 20 m/s માટે "
        "tan θ = 0.408, એટલે θ = 22.2°."),
      P("With friction the tyre can also push along the surface, and the limit becomes "
        "v_max = √(r g (μ + tan θ)/(1 − μ tan θ)), which falls back to √(μ r g) on a flat road.",
        "ઘર્ષણ સાથે ટાયર સપાટી પર પણ ધકેલી શકે, અને મર્યાદા v_max = √(r g (μ + tan θ)/(1 − μ tan θ)) "
        "થાય, જે સપાટ રસ્તે √(μ r g) બને છે.")]),
    (T("A car of 1200 kg takes a 45 m curve at 15 m/s. Find the centripetal force and the friction "
       "coefficient needed.", "1200 kg કાર 45 m વળાંક 15 m/s પર લે છે. કેન્દ્રગામી બળ અને જરૂરી ઘર્ષણ "
       "ગુણાંક શોધો."),
     4,
     [P("F = m v²/r = 1200 × 225/45 = 6000 N towards the centre of the curve.",
        "F = m v²/r = 1200 × 225/45 = 6000 N વળાંકના કેન્દ્ર તરફ."),
      P("Friction must supply it, and the maximum available is μ m g, so μ ≥ 6000/(1200 × 9.8) = "
        "0.51.", "તે ઘર્ષણે પૂરું પાડવું પડે, અને વધુમાં વધુ μ m g મળે, તેથી μ ≥ 6000/(1200 × 9.8) = 0.51."),
      P("Dry asphalt gives about 0.7 and wet asphalt about 0.4, so this curve would be posted at a "
        "lower speed in rain or banked to reduce the demand on friction.",
        "સૂકા ડામર પર લગભગ 0.7 અને ભીના પર 0.4 મળે, તેથી આ વળાંક વરસાદમાં ઓછી ઝડપે લેવો પડે અથવા "
        "ઘર્ષણ પરની માગ ઘટાડવા બેન્ક કરવો પડે.")]),
    (T("Why does a cyclist lean while turning? Derive the lean angle.",
       "સાયકલ સવાર વળાંક વખતે કેમ નમે છે? નમવાનું કોણ સાબિત કરો."),
     4,
     [P("The weight acts through the centre of mass and the ground reaction through the tyre contact. "
        "If the cycle stayed upright, these two would form a couple and topple it outward.",
        "વજન દ્રવ્યમાન કેન્દ્રમાંથી અને જમીનની પ્રતિક્રિયા ટાયરના સંપર્કમાંથી લાગે. સાયકલ સીધી રહે તો "
        "બંને કપલ બનાવીને બહાર તરફ ઢોળે."),
      P("Leaning inward by θ makes the resultant pass through the contact point, and its horizontal "
        "component supplies m v²/r: tan θ = v²/(r g).",
        "અંદર તરફ θ નમવાથી પરિણામ સંપર્ક બિંદુમાંથી પસાર થાય, અને તેનો સમક્ષિતિજ ઘટક m v²/r પૂરો પાડે: "
        "tan θ = v²/(r g)."),
      P("At 5 m/s on a 10 m radius the lean is 14.3°; doubling the speed to 10 m/s quadruples tan θ "
        "and takes the lean to 45.6°, which is why fast turns feel so committed.",
        "10 m ત્રિજ્યા પર 5 m/s પર નમવું 14.3° છે; ઝડપ 10 m/s કરતાં tan θ ચાર ગણું થાય અને નમવું 45.6° "
        "થાય, તેથી જ ઝડપી વળાંક ખૂબ નમેલા લાગે.")]),
    (T("Distinguish between centripetal and centrifugal force.",
       "કેન્દ્રગામી અને કેન્દ્રત્યાગી બળ વચ્ચેનો ભેદ સમજાવો."),
     4,
     [P("Centripetal force is a real inward force, such as tension, friction or gravity, that keeps a "
        "body on its circle; its magnitude is m v²/r.",
        "કેન્દ્રગામી બળ સાચું અંદર તરફનું બળ છે, જેમ કે તણાવ, ઘર્ષણ કે ગુરુત્વાકર્ષણ, જે શરીરને વર્તુળ "
        "પર રાખે; તેનું મૂલ્ય m v²/r છે."),
      P("Centrifugal force is a pseudo force of the same magnitude but directed outward, and it exists "
        "only for an observer in the rotating frame.",
        "કેન્દ્રત્યાગી બળ એ જ મૂલ્યનું પણ બહાર તરફનું આભાસી બળ છે, અને તે ફક્ત ફરતી ફ્રેમમાં રહેલા "
        "નિરીક્ષક માટે હોય છે."),
      P("In the ground frame, a stone on a string has only tension; in the frame of the stone, the "
        "string's tension is balanced by the outward centrifugal force and the stone appears at rest.",
        "જમીનની ફ્રેમમાં દોરી પરના પથ્થર પર ફક્ત તણાવ છે; પથ્થરની ફ્રેમમાં તણાવને બહાર તરફનું કેન્દ્રત્યાગી "
        "બળ સંતુલિત કરે અને પથ્થર સ્થિર દેખાય.")]),
    (T("A shaft turns at 1200 rpm. Find ω, and the rim speed of a 0.05 m grinding wheel on it. Comment "
       "on the result.", "શાફ્ટ 1200 rpm પર ફરે છે. ω અને તેના 0.05 m ઘંટી ચક્રની કિનાર ઝડપ શોધો. "
       "પરિણામ પર ટીકા કરો."),
     4,
     [P("ω = 2πN/60 = 2π × 1200/60 = 125.7 rad/s, that is 20 revolutions per second.",
        "ω = 2πN/60 = 2π × 1200/60 = 125.7 rad/s, એટલે પ્રતિ સેકન્ડ 20 પરિભ્રમણ."),
      P("Rim speed v = r ω = 0.05 × 125.7 = 6.28 m/s, a safe surface speed for a bonded wheel.",
        "કિનાર ઝડપ v = r ω = 0.05 × 125.7 = 6.28 m/s, જે બોન્ડેડ ચક્ર માટે સલામત સપાટી ઝડપ છે."),
      P("The centripetal acceleration is r ω² ≈ 790 m/s², about 80 g, so the wheel must be rated for "
        "that bursting load and guarded in case it fails.",
        "કેન્દ્રગામી પ્રવર્ગ r ω² ≈ 790 m/s², લગભગ 80 g છે, તેથી ચક્ર એ ફાટવાના ભાર માટે રેટેડ હોવું જોઈએ "
        "અને ફાટે તો બચાવ માટે ગાર્ડ હોવો જોઈએ.")]),
    (T("Explain with a diagram-free argument why a centrifuge separates cream from milk.",
       "કેન્દ્રત્યાગી યંત્ર ક્રીમને દૂધથી કેમ અલગ કરે છે તે ચિત્ર વગર સમજાવો."),
     3,
     [P("Every particle in the spinning bowl needs an inward force m v²/r to stay on its circle. The "
        "bowl supplies this only through the milk around the particle.",
        "ફરતા વાટકામાંના દરેક કણને વર્તુળ પર રહેવા અંદર તરફનું બળ m v²/r જોઈએ. વાટકો તે પોતાની આસપાસના "
        "દૂધ દ્વારા જ પૂરું પાડે."),
      P("Denser particles need a larger force than the fluid can give, so they move outward; lighter "
        "fat globules are pushed inward. The separation therefore follows density, not weight.",
        "ઘનતાવાળા કણોને પ્રવાહી આપી શકે તેનાથી વધુ બળ જોઈએ, તેથી તેઓ બહાર જાય; હલકા ચરબીના ગોળા અંદર "
        "ધકેલાય. તેથી અલગીકરણ ઘનતા પ્રમાણે થાય, વજન પ્રમાણે નહીં."),
      P("At 1200 rpm in a 0.25 m drum the acceleration is about 400 g, which separates in seconds what "
        "gravity would take hours to do.",
        "0.25 m ડ્રમમાં 1200 rpm પર પ્રવર્ગ લગભગ 400 g થાય, જે ગુરુત્વાકર્ષણને કલાકો લાગે તે કામ સેકન્ડોમાં "
        "કરે.")]),
    (T("What is the maximum speed of a car on a flat curve of radius 80 m if μ = 0.35, and how does "
       "banking at 10° change it?", "μ = 0.35 સાથે 80 m ત્રિજ્યાના સપાટ વળાંક પર કારની મહત્તમ ઝડપ કેટલી, "
       "અને 10° બેન્કિંગ તેને કેવી રીતે બદલે?"),
     5,
     [P("On a flat curve friction alone supplies the centripetal force, so v = √(μ r g) = "
        "√(0.35 × 80 × 9.8) = √274.4 = 16.6 m/s ≈ 60 km/h.",
        "સપાટ વળાંક પર ફક્ત ઘર્ષણ કેન્દ્રગામી બળ પૂરું પાડે, તેથી v = √(μ r g) = √(0.35 × 80 × 9.8) = "
        "√274.4 = 16.6 m/s ≈ 60 km/h."),
      P("With 10° banking, tan θ = 0.176, and v_max = √(r g (μ + tan θ)/(1 − μ tan θ)) = "
        "√(784 × 0.526/0.938) = √439 = 21.0 m/s ≈ 75 km/h.",
        "10° બેન્કિંગ સાથે tan θ = 0.176 અને v_max = √(r g (μ + tan θ)/(1 − μ tan θ)) = "
        "√(784 × 0.526/0.938) = √439 = 21.0 m/s ≈ 75 km/h."),
      P("Banking therefore buys about 25 % more speed for the same tyres, which is why highway curves "
        "are tilted long before friction becomes the limiting factor.",
        "તેથી બેન્કિંગ એ જ ટાયર માટે લગભગ 25 % વધુ ઝડપ આપે, અને તેથી જ હાઇવેના વળાંક ઘર્ષણ મર્યાદિત "
        "બને તે પહેલાં નમાવાય છે.")]),
    (T("Show that in uniform circular motion the speed is constant but the velocity is not.",
       "સમાન વર્તુળ ગતિમાં ઝડપ અચળ પણ વેગ અચળ નથી તે દર્શાવો."),
     3,
     [P("Speed is the magnitude of velocity. In uniform circular motion the body covers equal arcs in "
        "equal times, so the magnitude v stays the same.",
        "ઝડપ એ વેગનું મૂલ્ય છે. સમાન વર્તુળ ગતિમાં શરીર સમાન સમયમાં સમાન ચાપ કાપે, તેથી મૂલ્ય v અચળ રહે."),
      P("The direction of motion is always along the tangent, and the tangent turns as the body moves, "
        "so the velocity vector changes every instant.",
        "ગતિની દિશા હંમેશા સ્પર્શ રેખા પર હોય, અને શરીર ખસે તેમ સ્પર્શ રેખા ફરે, તેથી વેગ સદિશ દર ક્ષણે "
        "બદલાય."),
      P("That change of direction is the centripetal acceleration a = v²/r, directed towards the "
        "centre, and it is what the centripetal force produces.",
        "દિશાનો એ ફેરફાર જ કેન્દ્રગામી પ્રવર્ગ a = v²/r છે, જે કેન્દ્ર તરફ છે, અને કેન્દ્રગામી બળ તે જ "
        "ઉત્પન્ન કરે છે.")]),
    (T("A 0.5 kg stone is whirled in a vertical circle of radius 1 m at 4 m/s. Find the tension at the "
       "top and at the bottom.", "0.5 kg પથ્થર 1 m ત્રિજ્યાના ઊર્ધ્વ વર્તુળમાં 4 m/s પર ફેરવાય છે. "
       "ઉપર અને નીચે તણાવ શોધો."),
     5,
     [P("At the top, tension and weight both act towards the centre: T + m g = m v²/r.",
        "ઉપર તણાવ અને વજન બંને કેન્દ્ર તરફ લાગે: T + m g = m v²/r."),
      P("T = m v²/r − m g = 0.5 × 16/1 − 0.5 × 9.8 = 8 − 4.9 = 3.1 N.",
        "T = m v²/r − m g = 0.5 × 16/1 − 0.5 × 9.8 = 8 − 4.9 = 3.1 N."),
      P("At the bottom the weight points away, so T = m v²/r + m g = 8 + 4.9 = 12.9 N; the string is "
        "most likely to break at the bottom, which is why the cord is chosen for that value.",
        "નીચે વજન બહાર તરફ હોય, તેથી T = m v²/r + m g = 8 + 4.9 = 12.9 N; દોરી નીચે જ તૂટવાની સંભાવના "
        "વધુ હોય, તેથી દોરી એ મૂલ્ય માટે પસંદ કરાય."),
      P("The minimum speed at the top follows from T = 0, giving v = √(r g) = 3.13 m/s: below that the "
        "stone leaves the circle instead of completing it.",
        "ઉપર લઘુતમ ઝડપ T = 0 પરથી મળે, v = √(r g) = 3.13 m/s: તેનાથી ઓછી ઝડપે પથ્થર વર્તુળ પૂરું ન "
        "કરી શકે અને છૂટી જાય.")]),
    (T("Why must the least count of a speedometer-free measurement (rpm from a tachometer) be matched "
       "to the machine? Answer with the circular-motion relation.",
       "ટેકોમીટરથી મપાયેલી rpm ની ચોકસાઈ મશીનને અનુરૂપ કેમ હોવી જોઈએ? વર્તુળ ગતિના સંબંધથી જવાબ આપો."),
     3,
     [P("The rim speed is v = r ω, so an error of 1 % in ω is an error of 1 % in v, but the centripetal "
        "load goes as ω², so an error of 1 % in speed becomes about 2 % in force and in stress.",
        "કિનાર ઝડપ v = r ω છે, તેથી ω માં 1 % ભૂલ એ v માં 1 % ભૂલ છે, પણ કેન્દ્રગામી ભાર ω² પ્રમાણે "
        "હોવાથી ઝડપની 1 % ભૂલ બળ અને પ્રતિબળમાં લગભગ 2 % ભૂલ બને."),
      P("A tachometer reading 2 % high therefore understates the stress on a grinding wheel or a "
        "turbine disc by about 4 %, which is the wrong side of a safety margin.",
        "2 % વધુ વાંચતું ટેકોમીટર ઘંટી ચક્ર કે ટર્બાઇન ડિસ્ક પરના પ્રતિબળને લગભગ 4 % ઓછું આંકે, જે સલામતી "
        "માર્જિનની ખોટી બાજુ છે."),
      P("Calibration against a stroboscope or an optical tachometer keeps the reading honest, the same "
        "argument as for the vernier in Unit 1.",
        "સ્ટ્રોબોસ્કોપ કે ઓપ્ટિકલ ટેકોમીટર સામે કેલિબ્રેશન વાંચન સાચું રાખે, જે યુનિટ 1 ના વર્નિયર જેવી જ "
        "દલીલ છે.")]),
]

EXAM = [{"q": q, "marks": m} for q, m, _parts in _PRACTICE]
PRACTICE_ANSWERS = [_join(parts) for _q, _m, parts in _PRACTICE]

LESSON_COUNT = sum(len(s["items"]) for s in NOTES)
