"""Content for DI04005041 Unit 5 "Refrigeration Cycles and Systems", GTU Diploma
Chemical Engineering, semester 4, syllabus w.e.f. 2025-26.

Coverage is the official syllabus 5.1 - 5.5:
  5.1 refrigeration, COP, refrigerator capacity (ton of refrigeration)
  5.2 Carnot cycle, vapour-compression cycle and air-refrigeration cycle (theory)
  5.3 types of refrigerants and their codes
  5.4 choice of refrigerant
  5.5 numericals on COP and refrigerator capacity

Reference matter: Narayanan; Smith, Van Ness & Abbott; Gavhane; Rajput.
"""
from d1notes import Unit, bi, derivation, exam, numerical, theory, viva


def E(display, tex=None, note=None):
    return (display, tex or display, note) if note else (display, tex or display)


CODE = "DI04005041"
TITLE = bi("Refrigeration Cycles and Systems", "રેફ્રિજરેશન સાયકલ તથા સિસ્ટમ")

# =============================================================== 5.1 refrigeration, COP, capacity
S1 = [
    theory(
        "5.1",
        bi("Refrigeration, the COP and the capacity of a refrigerator",
           "Refrigeration, COP તથા refrigerator ની capacity"),
        definition=bi(
            "<b>Refrigeration</b> is the process of maintaining a space at a temperature below "
            "that of its surroundings by removing heat from it continuously. The device that "
            "does it consumes work, because heat cannot flow from cold to hot by itself. Its "
            "performance is the <b>coefficient of performance</b>, "
            "<b>COP = Q<sub>C</sub>/W</b> = heat removed ÷ work supplied.",
            "<b>Refrigeration</b> એટલે કોઈ જગ્યાને તેના surroundings કરતાં નીચા temperature પર સતત heat કાઢીને "
            "રાખવાની પ્રક્રિયા. તે કરતું ઉપકરણ work વાપરે છે, કારણ કે heat જાતે ઠંડા થી ગરમ તરફ જઈ શકતી નથી. "
            "તેની કાર્યક્ષમતા <b>coefficient of performance</b> છે, "
            "<b>COP = Q<sub>C</sub>/W</b> = કાઢેલી heat ÷ આપેલું work."),
        theory_text=bi(
            "The older unit of capacity is the <b>ton of refrigeration</b> (TR), defined as the "
            "rate of heat removal that freezes one short ton (2 000 lb = 907 kg) of water at "
            "0 °C into ice at 0 °C in 24 hours. That works out to 3.517 kW, or 12 000 Btu/h, or "
            "50 kcal/min. A domestic fridge is about 0.15 TR; a large cold store is several "
            "hundred.<br><br>"
            "Capacity is a <b>rate</b> — Q<sub>C</sub> in kW — while COP is a <b>ratio</b> and "
            "has no units. The two are independent: a machine can be large and inefficient or "
            "small and efficient. For a heat pump the same hardware is rated by "
            "COP<sub>HP</sub> = Q<sub>H</sub>/W = COP + 1, because the useful output is the heat "
            "delivered to the warm side.",
            "capacity નું જૂનું unit <b>ton of refrigeration</b> (TR) છે, જેની વ્યાખ્યા એ છે કે 0 °C ના 1 short "
            "ton (2 000 lb = 907 kg) પાણીને 24 કલાકમાં 0 °C ના બરફમાં ફેરવવા જેટલી ઝડપે heat કાઢવી. તે "
            "3.517 kW, 12 000 Btu/h કે 50 kcal/min થાય. ઘરેલું fridge લગભગ 0.15 TR; મોટું cold store "
            "સેંકડો ટન.<br><br>"
            "Capacity એ <b>દર</b> છે — kW માં Q<sub>C</sub> — જ્યારે COP એ <b>ગુણોત્તર</b> છે અને તેનું કોઈ "
            "unit નથી. બંને સ્વતંત્ર છે: machine મોટી તથા અક્ષમ હોઈ શકે કે નાની તથા કાર્યક્ષમ. Heat pump માટે "
            "એ જ hardware COP<sub>HP</sub> = Q<sub>H</sub>/W = COP + 1 થી મપાય, કારણ કે ઉપયોગી આઉટપુટ ગરમ "
            "બાજુ આપેલી heat છે."),
        equations=[E("COP = Q_C / W = Q_C / (Q_H − Q_C)", r"COP=\frac{Q_C}{W}"),
                   E("1 TR = 3.517 kW = 12 000 Btu/h = 50 kcal/min = 210 kJ/min", r"1\ \mathrm{TR}=3.517\ \mathrm{kW}"),
                   E("capacity  Q_C = W × COP   (kW)", r"Q_C=W\times COP")],
        list_items=[
            "<b>COP is not an efficiency</b> and may be well above 1; a window air-conditioner runs at 2.5–3.5.",
            "<b>Refrigerating effect</b> is the heat absorbed per kilogram of refrigerant (kJ/kg); capacity is that multiplied by the mass flow (kg/s).",
            "<b>Work</b> in a vapour-compression plant is the compressor work, h₂ − h₁ per kilogram.",
            "<b>Unit check:</b> COP has no unit; TR, kW and Btu/h are all rates and never appear in a COP.",
        ],
        qualification=bi(
            "The COP is defined for a specified pair of temperatures. Quoting a COP without the "
            "evaporating and condensing temperatures is meaningless, because the same machine "
            "gives a much lower COP on a hotter day.",
            "COP નિશ્ચિત temperature જોડી માટે વ્યાખ્યાયિત થાય. Evaporating તથા condensing temperatures વગર "
            "COP જણાવવો અર્થહીન છે, કારણ કે એ જ machine ગરમ દિવસે ઘણો નીચો COP આપે."),
    ),
    theory(
        "5.1",
        bi("Carnot refrigeration cycle — the limiting COP",
           "Carnot refrigeration cycle — મર્યાદિત COP"),
        definition=bi(
            "A refrigerator working on a <b>reversed Carnot cycle</b> takes heat "
            "Q<sub>C</sub> isothermally at T<sub>C</sub>, is compressed isentropically to "
            "T<sub>H</sub>, rejects Q<sub>H</sub> isothermally, and is expanded isentropically "
            "back to T<sub>C</sub>. Its COP, <b>T<sub>C</sub>/(T<sub>H</sub> − T<sub>C</sub>)</b>, "
            "is the highest any refrigerator between those two temperatures can reach.",
            "<b>reversed Carnot cycle</b> પર ચાલતું refrigerator T<sub>C</sub> પર isothermal રીતે "
            "Q<sub>C</sub> લે, isentropically T<sub>H</sub> સુધી compress થાય, isothermal રીતે "
            "Q<sub>H</sub> ફેંકે, અને isentropically પાછું T<sub>C</sub> સુધી expand થાય. તેનો COP, "
            "<b>T<sub>C</sub>/(T<sub>H</sub> − T<sub>C</sub>)</b>, તે બે temperatures વચ્ચે કોઈ પણ "
            "refrigerator પામી શકે તે સૌથી વધુ છે."),
        theory_text=bi(
            "The formula shows everything that matters in practice. As the <b>lift</b> "
            "T<sub>H</sub> − T<sub>C</sub> grows the COP collapses: a freezer at −20 °C rejecting "
            "to 35 °C has a lift of 55 K and a Carnot COP of only 253/55 = 4.6, while an "
            "air-conditioner at 5 °C evaporating and 35 °C condensing has 278/30 = 9.3. This is "
            "why freezing is expensive and why the condenser must be kept clean and the air "
            "around it cool.<br><br>"
            "The Carnot COP is a limit, not a target: real vapour-compression machines reach "
            "40–60 % of it, the loss being irreversibility in the compressor, the finite "
            "temperature differences in both exchangers and the throttling process. Because the "
            "throttle is isenthalpic rather than isentropic, a vapour-compression cycle can never "
            "even in principle equal the Carnot value.",
            "સૂત્ર વ્યવહારની દરેક મહત્ત્વની વાત દર્શાવે છે. <b>lift</b> T<sub>H</sub> − T<sub>C</sub> વધતાં "
            "COP ધરાશાયી થાય: −20 °C નું freezer 35 °C ને heat ફેંકે તો lift 55 K અને Carnot COP ફક્ત "
            "253/55 = 4.6, જ્યારે 5 °C evaporating તથા 35 °C condensing વાળું air-conditioner "
            "278/30 = 9.3 આપે. એટલે જ freezing ખર્ચાળ છે અને condenser સાફ તથા તેની આસપાસની હવા ઠંડી "
            "રાખવી પડે.<br><br>"
            "Carnot COP મર્યાદા છે, લક્ષ્ય નહીં: વાસ્તવિક vapour-compression machines તેના 40–60 % "
            "પામે, અને નુકસાન compressor માં irreversibility, બંને exchangers માં મર્યાદિત temperature "
            "તફાવત તથા throttling પ્રક્રિયાનું હોય. Throttle isentropic ને બદલે isenthalpic હોવાથી "
            "vapour-compression cycle સૈદ્ધાંતિક રીતે પણ Carnot કિંમત સુધી પહોંચી શકે નહીં."),
        equations=[E("COP_Carnot = T_C / (T_H − T_C)", r"COP=\frac{T_C}{T_H-T_C}"),
                   E("COP_HP,Carnot = T_H / (T_H − T_C)", r"COP_{HP}=\frac{T_H}{T_H-T_C}"),
                   E("lift = T_H − T_C        COP falls as the lift grows", r"\Delta T=T_H-T_C")],
        list_items=[
            "<b>Freezer:</b> 253 K evaporating, 308 K condensing → COP ≤ 4.6.",
            "<b>Air-conditioner:</b> 278 K evaporating, 308 K condensing → COP ≤ 9.3.",
            "<b>Practical rule:</b> halving the lift roughly doubles the COP.",
            "<b>Carnot cycle is not built</b> — wet compression and isothermal heat transfer at exactly the reservoir temperature are impractical.",
        ],
        qualification=bi(
            "The Carnot COP uses <i>absolute</i> temperatures. Substituting 0 °C for 273 K turns "
            "a finite COP into a division by zero — the commonest arithmetic error in this topic.",
            "Carnot COP <i>absolute</i> temperatures વાપરે. 273 K ને બદલે 0 °C મૂકવાથી મર્યાદિત COP શૂન્ય વડે "
            "ભાગાકાર બની જાય — આ વિષયની સૌથી સામાન્ય ગણતરીની ભૂલ."),
    ),
]

# =============================================================== 5.2 vapour compression
S2 = [
    theory(
        "5.2",
        bi("The vapour-compression cycle", "vapour-compression cycle"),
        definition=bi(
            "The <b>vapour-compression cycle</b> is the practical refrigeration cycle. A "
            "compressor raises the pressure of saturated vapour, a condenser rejects heat and "
            "condenses it, a throttle valve drops the pressure isenthalpically, and an evaporator "
            "boils the wet mixture at low pressure, absorbing heat from the cold space.",
            "<b>vapour-compression cycle</b> એ વ્યવહારુ refrigeration cycle છે. Compressor saturated "
            "vapour નું pressure વધારે, condenser heat ફેંકીને તેને condense કરે, throttle valve "
            "isenthalpically pressure ઘટાડે, અને evaporator low pressure પર wet mixture ઉકાળીને ઠંડી "
            "જગ્યામાંથી heat શોષે."),
        theory_text=bi(
            "Four processes, four state points, and one energy balance that carries every "
            "numerical: <b>Q<sub>H</sub> = Q<sub>C</sub> + W</b>. Per kilogram of refrigerant, the "
            "refrigerating effect is h₁ − h₄ (the heat taken in the evaporator), the work is "
            "h₂ − h₁ (the enthalpy rise across the compressor) and the heat rejected is "
            "h₂ − h₃. Because point 3→4 is a throttle, h₄ = h₃, which is the single fact that "
            "makes the cycle solvable from a table.<br><br>"
            "The reason a <b>throttle</b> is used rather than an expander is cost and "
            "simplicity: a capillary tube or a valve has no moving parts. The price is that the "
            "work an expander could have recovered is lost, and the evaporator receives a "
            "mixture rather than pure liquid, both of which push the COP below the Carnot value. "
            "The three standard departures from the ideal cycle — <b>superheating</b> at the "
            "evaporator outlet, <b>subcooling</b> at the condenser outlet, and <b>superheating "
            "during compression</b> — each shift the COP a little and are shown on the P–h "
            "diagram.",
            "ચાર પ્રક્રિયાઓ, ચાર state points, અને એક energy balance જે દરેક દાખલો ઉકેલે: "
            "<b>Q<sub>H</sub> = Q<sub>C</sub> + W</b>. પ્રતિ kilogram refrigerant, refrigerating effect "
            "h₁ − h₄ (evaporator માં લેવાયેલી heat), work h₂ − h₁ (compressor પર enthalpy વધારો) અને "
            "ફેંકાયેલી heat h₂ − h₃. Point 3→4 throttle હોવાથી h₄ = h₃, અને એ જ એક હકીકત table માંથી cycle "
            "ઉકેલવા દે છે.<br><br>"
            "<b>throttle</b> કેમ વપરાય અને expander નહીં તેનું કારણ ખર્ચ તથા સરળતા છે: capillary tube કે "
            "valve માં કોઈ ફરતો ભાગ નથી. કિંમત એ છે કે expander પાછું મેળવી શકે તેવું work ગુમાવાય, અને "
            "evaporator ને શુદ્ધ liquid ને બદલે mixture મળે, જે બંને COP ને Carnot કિંમતથી નીચે ધકેલે. "
            "આદર્શ cycle થી ત્રણ પ્રમાણભૂત વિચલનો — evaporator ના આઉટલેટ પર <b>superheating</b>, condenser "
            "ના આઉટલેટ પર <b>subcooling</b>, અને compression દરમિયાન <b>superheating</b> — દરેક COP ને થોડો "
            "ખસેડે છે અને P–h diagram પર દેખાય છે."),
        equations=[E("refrigerating effect  q_C = h₁ − h₄", r"q_C=h_1-h_4"),
                   E("compressor work  w = h₂ − h₁", r"w=h_2-h_1"),
                   E("heat rejected  q_H = h₂ − h₃        throttle:  h₄ = h₃", r"h_4=h_3"),
                   E("COP = (h₁ − h₄)/(h₂ − h₁)", r"COP=\frac{h_1-h_4}{h_2-h_1}")],
        list_items=[
            "<b>Compressor:</b> reciprocating, rotary, scroll or centrifugal; it is the only work-consuming component.",
            "<b>Condenser:</b> air-cooled or water-cooled; it must reject Q<sub>H</sub>, which is larger than Q<sub>C</sub>.",
            "<b>Throttle:</b> capillary tube on small units, thermostatic expansion valve on large ones.",
            "<b>Evaporator:</b> the cold coil; a partly flooded evaporator gives the highest COP but risks liquid carry-over.",
        ],
        diagram="d5_refrigeration_loop",
        qualification=bi(
            "The ideal cycle assumes dry saturated vapour at the compressor inlet and no pressure "
            "loss in the pipes. Real plants superheat the suction line to protect the compressor "
            "from droplets, which raises the discharge temperature and slightly lowers the COP.",
            "આદર્શ cycle compressor inlet પર dry saturated vapour તથા pipes માં pressure loss નહીં તે માને. "
            "વાસ્તવિક plants droplets થી compressor બચાવવા suction line superheat કરે, જેનાથી discharge "
            "temperature વધે અને COP થોડો ઘટે."),
    ),
    theory(
        "5.2",
        bi("The air-refrigeration (reversed Brayton) cycle",
           "air-refrigeration (reversed Brayton) cycle"),
        definition=bi(
            "In the <b>air-refrigeration cycle</b> the working fluid is air, which stays gaseous "
            "throughout. Air is compressed, cooled at constant pressure by the atmosphere, "
            "expanded through a turbine to a low temperature, and passed through the cold space, "
            "where it absorbs heat before returning to the compressor.",
            "<b>air-refrigeration cycle</b> માં working fluid હવા છે, જે આખા cycle દરમિયાન gas જ રહે છે. "
            "હવા compress થાય, atmosphere વડે અચળ pressure પર ઠંડી થાય, turbine માં expand થઈ નીચા temperature "
            "પર આવે, અને ઠંડી જગ્યામાંથી heat લઈને પાછી compressor માં જાય."),
        theory_text=bi(
            "It is exactly the Brayton power cycle run backwards: compression, constant-pressure "
            "cooling, expansion, constant-pressure heating. For a perfect gas with constant "
            "c<sub>p</sub> the COP depends only on the pressure ratio and γ: "
            "<b>COP = 1/(r<sub>p</sub><sup>(γ−1)/γ</sup> − 1)</b>. Note the weakness — the COP is "
            "<i>fixed</i> by the pressure ratio, so it cannot be improved by making the machine "
            "bigger, and at a small temperature lift the air cycle is far worse than a vapour "
            "cycle.<br><br>"
            "Its advantages are equally clear: no refrigerant to leak, charge or recover, a very "
            "light plant, and instant start-up. That is why it survives in <b>aircraft cabin "
            "cooling</b>, where bleed air from the engine is already compressed, and in some "
            "industrial gas liquefaction trains. Below about −70 °C the vapour cycles run out of "
            "usable refrigerant and the air or nitrogen cycle takes over.",
            "તે બરાબર Brayton power cycle ઉલટાવેલો છે: compression, અચળ pressure પર ઠંડક, expansion, અચળ "
            "pressure પર ગરમી. અચળ c<sub>p</sub> વાળા perfect gas માટે COP ફક્ત pressure ratio તથા γ પર "
            "આધાર રાખે: <b>COP = 1/(r<sub>p</sub><sup>(γ−1)/γ</sup> − 1)</b>. નબળાઈ ધ્યાનમાં લો — COP "
            "<i>નિશ્ચિત</i> થાય pressure ratio થી, તેથી machine મોટી કરીને સુધારી શકાય નહીં, અને નાના "
            "temperature lift પર air cycle vapour cycle કરતાં ઘણું ખરાબ છે.<br><br>"
            "તેના ફાયદા પણ સ્પષ્ટ છે: leak, charge કે recover કરવા refrigerant નહીં, ઘણું હલકું plant, અને "
            "તરત શરૂઆત. એટલે જ તે <b>aircraft cabin cooling</b> માં ટકી રહ્યું છે, જ્યાં engine ની bleed air "
            "પહેલેથી compressed હોય, અને કેટલીક industrial gas liquefaction trains માં. લગભગ −70 °C થી નીચે "
            "vapour cycles ને વાપરવા જેવું refrigerant મળતું નથી અને air કે nitrogen cycle કામ લે."),
        equations=[E("COP = 1 / (r_p^((γ−1)/γ) − 1)        r_p = P_high/P_low", r"COP=\frac{1}{r_p^{(\gamma-1)/\gamma}-1}"),
                   E("air cycle:  COP depends only on r_p and γ", r"COP=f(r_p,\gamma)")],
        list_items=[
            "<b>Closed air cycle</b> recirculates the same air; the <b>open</b> cycle (aircraft) uses engine bleed air once and dumps it.",
            "<b>Regeneration</b> with a heat exchanger raises the COP substantially at high pressure ratios.",
            "<b>No phase change</b> means the temperature falls smoothly along the expander, so very low temperatures are easy.",
            "<b>Low COP at small lift</b> is the reason domestic refrigeration never uses air.",
        ],
        diagram="d5_air_refrigeration",
        qualification=bi(
            "The formula assumes a perfect gas with constant c<sub>p</sub> and isentropic "
            "compressor and expander. Real machines add the isentropic efficiencies of both "
            "turbomachines, and the COP falls below the ideal value.",
            "સૂત્ર અચળ c<sub>p</sub> વાળા perfect gas તથા isentropic compressor અને expander માને. વાસ્તવિક "
            "machines બંને turbomachines ની isentropic efficiencies ઉમેરે, અને COP આદર્શ કિંમતથી નીચે આવે."),
    ),
    derivation(
        "5.2",
        bi("COP of the vapour-compression cycle from the P–h diagram",
           "P–h diagram પરથી vapour-compression cycle નો COP"),
        symbols=bi(
            "<b>Model:</b> one kilogram of refrigerant circulating steadily. States: 1 saturated "
            "vapour leaving the evaporator, 2 compressed vapour leaving the compressor, 3 "
            "saturated liquid leaving the condenser, 4 wet mixture after the throttle. "
            "<b>Assumptions:</b> steady flow, negligible kinetic and potential energy, "
            "compression isentropic (ideal case), throttling isenthalpic, no pressure loss in "
            "the pipes.",
            "<b>Model:</b> એક kilogram refrigerant સ્થિર રીતે ફરે છે. States: 1 evaporator માંથી નીકળતું "
            "saturated vapour, 2 compressor માંથી નીકળતું compressed vapour, 3 condenser માંથી નીકળતું "
            "saturated liquid, 4 throttle પછીનું wet mixture. <b>Assumptions:</b> steady flow, kinetic "
            "તથા potential energy નગણ્ય, compression isentropic (આદર્શ કિસ્સો), throttling isenthalpic, "
            "pipes માં pressure loss નહીં."),
        steps=[
            (bi("Apply the steady-flow energy equation to the compressor. It is adiabatic, so the "
                "work is the enthalpy rise.",
                "Compressor પર steady-flow energy equation લગાવો. તે adiabatic છે, તેથી work enthalpy વધારો છે."),
             E("w = h₂ − h₁", r"w=h_2-h_1")),
            (bi("Apply it to the condenser. No work crosses, so the heat rejected is the enthalpy "
                "drop.",
                "Condenser પર લગાવો. કોઈ work નથી, તેથી ફેંકાતી heat enthalpy ઘટાડો છે."),
             E("q_H = h₂ − h₃", r"q_H=h_2-h_3")),
            (bi("Apply it to the throttle. It is adiabatic and does no work, so enthalpy is "
                "constant across it — the key relation of the whole cycle.",
                "Throttle પર લગાવો. તે adiabatic છે અને work કરતું નથી, તેથી enthalpy અચળ રહે — આખા cycle નો "
                "મુખ્ય સંબંધ."),
             E("h₃ = h₄", r"h_3=h_4")),
            (bi("Apply it to the evaporator. The heat absorbed at constant pressure is the "
                "enthalpy rise, and it is the refrigerating effect.",
                "Evaporator પર લગાવો. અચળ pressure પર લેવાયેલી heat enthalpy વધારો છે, અને તે જ refrigerating "
                "effect છે."),
             E("q_C = h₁ − h₄", r"q_C=h_1-h_4")),
            (bi("Write the energy balance round the whole cycle: heat out equals heat in plus "
                "work in.",
                "આખા cycle ની આસપાસ energy balance લખો: બહાર જતી heat = અંદર આવતી heat + અંદર આવતું work."),
             E("q_H = q_C + w", r"q_H=q_C+w")),
            (bi("Substitute the four enthalpy expressions into the balance as a check.",
                "ચારેય enthalpy સમીકરણો balance માં મૂકીને ચકાસો."),
             E("h₂ − h₃ = (h₁ − h₄) + (h₂ − h₁)", r"h_2-h_3=(h_1-h_4)+(h_2-h_1)")),
            (bi("Form the COP as refrigerating effect over compressor work and simplify.",
                "COP ને refrigerating effect ભાગ્યે compressor work તરીકે લખો અને સરળ કરો."),
             E("COP = (h₁ − h₄)/(h₂ − h₁)", r"COP=\frac{h_1-h_4}{h_2-h_1}")),
        ],
        final=E("COP = (h₁ − h₄)/(h₂ − h₁)  with  h₄ = h₃", r"COP=\frac{h_1-h_4}{h_2-h_1}"),
        diagram="d5_ph_cycle",
    ),
]

# =============================================================== 5.3 refrigerants and codes
S3 = [
    theory(
        "5.3",
        bi("Types of refrigerants and the numbering code",
           "Refrigerants ના પ્રકાર તથા numbering code"),
        definition=bi(
            "A <b>refrigerant</b> is the working fluid of a refrigeration cycle. The main families "
            "are <b>halocarbons</b> (CFCs, HCFCs, HFCs), <b>inorganics</b> (ammonia, carbon "
            "dioxide, water, air), <b>hydrocarbons</b> (propane, butane, isobutane) and "
            "<b>zeotropic and azeotropic blends</b> such as R-404A and R-410A.",
            "<b>refrigerant</b> એ refrigeration cycle નું working fluid છે. મુખ્ય કુળો છે "
            "<b>halocarbons</b> (CFCs, HCFCs, HFCs), <b>inorganics</b> (ammonia, carbon dioxide, પાણી, હવા), "
            "<b>hydrocarbons</b> (propane, butane, isobutane) અને <b>zeotropic તથા azeotropic blends</b> "
            "જેવા R-404A તથા R-410A."),
        theory_text=bi(
            "The <b>ASHRAE numbering code</b> translates a formula into a number. For a halocarbon "
            "the digits are: number of carbon atoms minus one, number of hydrogen atoms plus one, "
            "number of fluorine atoms, and the letters give the halogen: <b>a</b> = isomer, "
            "<b>B</b> = bromine. R-134a is therefore C₂H₂F₄ — 1 carbon, 3 hydrogens, 4 fluorines "
            "— and R-22 is CHClF₂. Inorganics use <b>700 + molecular mass</b>: R-717 is ammonia, "
            "R-744 is carbon dioxide, R-718 is water.<br><br>"
            "The code hides the environmental history. <b>CFCs</b> (R-11, R-12) were banned by the "
            "Montreal Protocol because chlorine destroys stratospheric ozone; <b>HCFCs</b> "
            "(R-22) were the first replacement and are now themselves being phased out; "
            "<b>HFCs</b> (R-134a, R-410A) are ozone-safe but are strong greenhouse gases and are "
            "being cut under the Kigali Amendment. The industry has moved to HFOs such as R-1234yf "
            "and back to natural refrigerants — ammonia, CO₂ and hydrocarbons — which have ODP 0 "
            "and negligible GWP.",
            "<b>ASHRAE numbering code</b> સૂત્રને નંબરમાં ફેરવે. Halocarbon માટે અંકો છે: carbon atoms ની સંખ્યા "
            "ઓછા એક, hydrogen atoms ની સંખ્યા વત્તા એક, fluorine atoms ની સંખ્યા, અને અક્ષરો halogen આપે: "
            "<b>a</b> = isomer, <b>B</b> = bromine. તેથી R-134a એટલે C₂H₂F₄ — 1 carbon, 3 hydrogen, "
            "4 fluorine — અને R-22 એટલે CHClF₂. Inorganics માટે <b>700 + molecular mass</b>: R-717 એટલે "
            "ammonia, R-744 એટલે carbon dioxide, R-718 એટલે પાણી.<br><br>"
            "Code પાછળ પર્યાવરણનો ઇતિહાસ છુપાયેલો છે. <b>CFCs</b> (R-11, R-12) ને Montreal Protocol દ્વારા "
            "પ્રતિબંધિત કરાયા કારણ કે chlorine stratospheric ozone નો નાશ કરે; <b>HCFCs</b> (R-22) પ્રથમ "
            "વિકલ્પ હતા અને હવે તે પણ દૂર થઈ રહ્યા છે; <b>HFCs</b> (R-134a, R-410A) ozone માટે સલામત છે પણ "
            "પ્રબળ greenhouse gases છે અને Kigali Amendment હેઠળ ઘટાડાઈ રહ્યા છે. ઉદ્યોગ HFOs જેવા GWP-100 વાળા "
            "R-1234yf તરફ અને ફરી natural refrigerants — ammonia, CO₂ તથા hydrocarbons — તરફ ગયો છે, જેમના "
            "ODP 0 અને GWP નગણ્ય છે."),
        equations=[E("halocarbon:  R-(C−1)(H+1)(F)   e.g. R-134a = C₂H₂F₄", r"R\!-\!134a"),
                   E("inorganic:  R-700 + M   → R-717 NH₃, R-744 CO₂, R-718 H₂O", r"R\!-\!717"),
                   E("blends:  R-400 series (zeotropic), R-500 series (azeotropic)", r"R\!-\!400")],
        list_items=[
            "<b>CFC:</b> R-11, R-12 — ozone destruction, banned.",
            "<b>HCFC:</b> R-22 — low ODP, being phased out.",
            "<b>HFC:</b> R-134a, R-410A, R-404A — zero ODP, high GWP.",
            "<b>Natural:</b> R-717 ammonia, R-744 CO₂, R-290 propane — zero ODP, negligible GWP.",
        ],
        diagram="d5_refrigerant_choice",
        qualification=bi(
            "The code says nothing about performance. Two refrigerants with similar numbers can "
            "have very different latent heats, pressures and COPs; the code identifies the "
            "molecule, not the duty.",
            "Code performance વિશે કંઈ કહેતો નથી. સરખા નંબર વાળા બે refrigerants ની latent heat, pressure તથા "
            "COP ઘણા જુદા હોઈ શકે; code અણુ ઓળખાવે છે, કામ નહીં."),
    ),
]

# =============================================================== 5.4 choice
S4 = [
    theory(
        "5.4",
        bi("Choice of refrigerant", "refrigerant ની પસંદગી"),
        definition=bi(
            "No single fluid is best for every duty, so a refrigerant is chosen by weighing five "
            "groups of properties: <b>thermodynamic</b> (pressure, latent heat, COP), "
            "<b>safety</b> (toxicity, flammability), <b>environmental</b> (ODP, GWP, "
            "atmospheric lifetime), <b>physical</b> (leak detection, oil miscibility, "
            "corrosivity) and <b>economic</b> (cost, availability, ease of recovery).",
            "દરેક કામ માટે એક જ fluid શ્રેષ્ઠ નથી, તેથી refrigerant પાંચ ગુણધર્મ-જૂથ તોળીને પસંદ કરાય: "
            "<b>thermodynamic</b> (pressure, latent heat, COP), <b>safety</b> (toxicity, flammability), "
            "<b>environmental</b> (ODP, GWP, atmospheric lifetime), <b>physical</b> (leak detection, "
            "oil miscibility, corrosivity) અને <b>economic</b> (ખર્ચ, ઉપલબ્ધતા, recovery ની સરળતા)."),
        theory_text=bi(
            "The thermodynamic requirements are the ones you can calculate. The <b>evaporating "
            "pressure</b> should be slightly above atmospheric so that any leak goes out rather "
            "than air and moisture coming in; the <b>condensing pressure</b> should be modest so "
            "the compressor and condenser do not have to be heavy. A large <b>latent heat</b> "
            "keeps the circulation rate small, and a <b>high critical temperature</b> keeps the "
            "cycle well below the critical point where the COP collapses.<br><br>"
            "Safety is ranked by ASHRAE as a letter and a number: <b>A</b> for lower toxicity, "
            "<b>B</b> for higher; <b>1</b> for no flame propagation, <b>2L</b> for mildly "
            "flammable, <b>2</b> and <b>3</b> for increasingly flammable. R-134a is A1, ammonia "
            "is B2L, propane is A3 — which is why a hydrocarbon fridge needs a sealed, spark-free "
            "compartment. Ammonia remains the standard for large industrial plant because its "
            "latent heat is enormous and it is cheap, despite being toxic and incompatible with "
            "copper.",
            "Thermodynamic જરૂરિયાતો ગણી શકાય તેવી છે. <b>Evaporating pressure</b> atmosphere થી થોડું ઉપર હોવું "
            "જોઈએ જેથી leak થાય તો gas બહાર જાય, હવા તથા ભેજ અંદર ન આવે; <b>condensing pressure</b> મર્યાદિત "
            "હોવું જોઈએ જેથી compressor તથા condenser ભારે ન બને. મોટી <b>latent heat</b> circulation rate "
            "નાની રાખે, અને ઊંચું <b>critical temperature</b> cycle ને critical point થી ઘણું નીચે રાખે જ્યાં "
            "COP ધરાશાયી થાય.<br><br>"
            "Safety ને ASHRAE એક અક્ષર તથા એક અંકથી ક્રમ આપે: ઓછી toxicity માટે <b>A</b>, વધુ માટે <b>B</b>; "
            "જ્યોત ન ફેલાય તે માટે <b>1</b>, હળવી જ્વલનશીલતા માટે <b>2L</b>, વધતી જ્વલનશીલતા માટે <b>2</b> તથા "
            "<b>3</b>. R-134a એ A1, ammonia એ B2L, propane એ A3 — એટલે જ hydrocarbon fridge ને sealed, "
            "spark-free compartment જોઈએ. Ammonia મોટા industrial plant માટે standard રહ્યું છે કારણ કે તેની "
            "latent heat ખૂબ મોટી અને તે સસ્તું છે, જો કે તે toxic છે અને copper સાથે મળતું નથી."),
        equations=[E("ODP:  R-11 = 1.0 (reference);  HFCs and naturals = 0", r"\mathrm{ODP}"),
                   E("GWP₁₀₀:  CO₂ = 1,  R-134a = 1430,  R-404A = 3922,  NH₃ < 1", r"\mathrm{GWP}")],
        list_items=[
            "<b>Domestic fridge / car:</b> R-134a or R-600a — safe, cheap, modest pressures.",
            "<b>Room air-conditioner:</b> R-32 or R-410A — high volumetric capacity, A2L or A1.",
            "<b>Industrial cold store:</b> ammonia — unbeatable latent heat, cheap, but B2L.",
            "<b>Very low temperature:</b> R-744 (CO₂) or a cascade with ethylene — no HFC works below about −60 °C.",
        ],
        qualification=bi(
            "A refrigerant that is perfect thermodynamically but banned environmentally is not a "
            "choice at all. Since Montreal and Kigali, the environmental screen is applied "
            "<i>first</i>, and the thermodynamic optimisation happens only among the fluids that "
            "survive it.",
            "Thermodynamically પરફેક્ટ પણ પર્યાવરણીય રીતે પ્રતિબંધિત refrigerant પસંદગી જ નથી. Montreal તથા "
            "Kigali પછી પર્યાવરણીય ગાળણી <i>પહેલાં</i> લાગે, અને thermodynamic optimisation ફક્ત તેમાંથી "
            "પસાર થતા fluids વચ્ચે થાય."),
    ),
]

# =============================================================== numericals
N1 = numerical(
    "N1",
    bi("COP and capacity of a refrigerator",
       "refrigerator નો COP તથા capacity"),
    given=bi("A refrigerator removes 12 000 kJ/h from a cold space and consumes 1.5 kW of "
             "compressor power.",
             "Refrigerator ઠંડી જગ્યામાંથી 12 000 kJ/h heat કાઢે છે અને 1.5 kW compressor power વાપરે છે."),
    find=bi("The COP, the heat rejected to the surroundings, and the capacity in tons of "
            "refrigeration.",
            "COP, surroundings ને ફેંકાતી heat, અને tons of refrigeration માં capacity."),
    formula=[E("COP = Q_C/W", r"COP=\frac{Q_C}{W}"),
             E("Q_H = Q_C + W", r"Q_H=Q_C+W"),
             E("capacity (TR) = Q_C (kW)/3.517", r"\mathrm{TR}=\frac{Q_C}{3.517}")],
    substitution=bi(
        "Q_C = 12 000/3 600 = 3.333 kW. COP = 3.333/1.5 = 2.22. "
        "Q_H = 3.333 + 1.5 = 4.833 kW. Capacity = 3.333/3.517 = 0.95 TR.",
        "Q_C = 12 000/3 600 = 3.333 kW. COP = 3.333/1.5 = 2.22. "
        "Q_H = 3.333 + 1.5 = 4.833 kW. Capacity = 3.333/3.517 = 0.95 TR."),
    answer=bi("COP = 2.22;  Q_H = 4.83 kW;  capacity = 0.95 TR (about a large domestic fridge).",
              "COP = 2.22;  Q_H = 4.83 kW;  capacity = 0.95 TR (મોટા ઘરેલું fridge જેટલી)."),
    check=bi("The first law is satisfied: 3.33 kW in as heat, 1.5 kW in as work, 4.83 kW out as "
             "heat. A COP of 2.2 is typical for a domestic unit; the Carnot COP for the same "
             "temperatures would be near 4.",
             "પ્રથમ નિયમ સંતોષાય: heat તરીકે 3.33 kW અંદર, work તરીકે 1.5 kW અંદર, heat તરીકે 4.83 kW "
             "બહાર. ઘરેલું unit માટે COP 2.2 સામાન્ય; એ જ temperatures માટે Carnot COP લગભગ 4 થાય."),
)

N2 = numerical(
    "N2",
    bi("Carnot COP and comparison with the actual machine",
       "Carnot COP તથા વાસ્તવિક machine સાથે સરખામણી"),
    given=bi("A cold store is maintained at −18 °C when the outside air is at 32 °C. The plant "
             "actually consumes 8 kW to remove 20 kW.",
             "બહારની હવા 32 °C હોય ત્યારે cold store −18 °C પર રખાય છે. Plant 20 kW heat કાઢવા વાસ્તવમાં "
             "8 kW વાપરે છે."),
    find=bi("The Carnot COP, the actual COP, and the second-law efficiency of the plant.",
            "Carnot COP, વાસ્તવિક COP, અને plant ની second-law efficiency."),
    formula=[E("COP_Carnot = T_C/(T_H − T_C)", r"COP=\frac{T_C}{T_H-T_C}"),
             E("η_II = COP_actual/COP_Carnot", r"\eta_{II}=\frac{COP}{COP_{Carnot}}")],
    substitution=bi(
        "T_C = 255 K, T_H = 305 K. COP_Carnot = 255/(305 − 255) = 255/50 = 5.10. "
        "COP_actual = 20/8 = 2.50. η_II = 2.50/5.10 = 0.49 = 49 %.",
        "T_C = 255 K, T_H = 305 K. COP_Carnot = 255/(305 − 255) = 255/50 = 5.10. "
        "COP_actual = 20/8 = 2.50. η_II = 2.50/5.10 = 0.49 = 49 %."),
    answer=bi("COP_Carnot = 5.10;  COP_actual = 2.50;  second-law efficiency = 49 %.",
              "COP_Carnot = 5.10;  COP_actual = 2.50;  second-law efficiency = 49 %."),
    check=bi("A 50 K lift halves the Carnot COP compared with a 25 K lift, which is why a freezer "
             "is so much less efficient than an air-conditioner. A second-law efficiency near "
             "50 % is a normal, well-run plant.",
             "50 K નો lift 25 K ના lift કરતાં Carnot COP અડધો કરે, એટલે જ freezer air-conditioner કરતાં "
             "ઘણું ઓછું કાર્યક્ષમ છે. 50 % ની નજીકની second-law efficiency સામાન્ય, સારી રીતે ચાલતી plant છે."),
)

N3 = numerical(
    "N3",
    bi("Vapour-compression cycle using R-134a enthalpies",
       "R-134a enthalpies વાપરીને vapour-compression cycle"),
    given=bi("R-134a leaves the evaporator at 1.5 bar as saturated vapour (h₁ = 389.6 kJ/kg) and "
             "leaves the condenser at 8 bar as saturated liquid (h₃ = 220.5 kJ/kg). The "
             "compressor discharge enthalpy is h₂ = 424.7 kJ/kg and the refrigerant flow is "
             "0.05 kg/s.",
             "R-134a evaporator માંથી 1.5 bar પર saturated vapour તરીકે નીકળે (h₁ = 389.6 kJ/kg) અને "
             "condenser માંથી 8 bar પર saturated liquid તરીકે (h₃ = 220.5 kJ/kg). Compressor discharge "
             "enthalpy h₂ = 424.7 kJ/kg અને refrigerant flow 0.05 kg/s."),
    find=bi("Refrigerating effect, compressor work, COP and the cooling capacity in TR.",
            "Refrigerating effect, compressor work, COP તથા TR માં cooling capacity."),
    formula=[E("q_C = h₁ − h₄ = h₁ − h₃", r"q_C=h_1-h_3"),
             E("w = h₂ − h₁", r"w=h_2-h_1"),
             E("COP = q_C/w        Q_C = m q_C", r"COP=\frac{q_C}{w}")],
    substitution=bi(
        "h₄ = h₃ = 220.5 kJ/kg (throttle). q_C = 389.6 − 220.5 = 169.1 kJ/kg. "
        "w = 424.7 − 389.6 = 35.1 kJ/kg. COP = 169.1/35.1 = 4.82. "
        "Q_C = 0.05 × 169.1 = 8.46 kW = 8.46/3.517 = 2.41 TR.",
        "h₄ = h₃ = 220.5 kJ/kg (throttle). q_C = 389.6 − 220.5 = 169.1 kJ/kg. "
        "w = 424.7 − 389.6 = 35.1 kJ/kg. COP = 169.1/35.1 = 4.82. "
        "Q_C = 0.05 × 169.1 = 8.46 kW = 8.46/3.517 = 2.41 TR."),
    answer=bi("q_C = 169.1 kJ/kg;  w = 35.1 kJ/kg;  COP = 4.82;  capacity = 2.41 TR.",
              "q_C = 169.1 kJ/kg;  w = 35.1 kJ/kg;  COP = 4.82;  capacity = 2.41 TR."),
    check=bi("The COP of 4.8 is high because the lift is small — 1.5 bar evaporating against "
             "8 bar condensing is roughly −20 °C against +30 °C. The heat rejected is "
             "0.05 × (424.7 − 220.5) = 10.2 kW, which equals 8.46 + 1.76 kW of work.",
             "COP 4.8 ઊંચો છે કારણ કે lift નાનો છે — 1.5 bar evaporating સામે 8 bar condensing એટલે લગભગ "
             "−20 °C સામે +30 °C. ફેંકાતી heat 0.05 × (424.7 − 220.5) = 10.2 kW, જે 8.46 + 1.76 kW work "
             "બરાબર થાય."),
)

N4 = numerical(
    "N4",
    bi("Air-refrigeration cycle COP",
       "air-refrigeration cycle નો COP"),
    given=bi("An air refrigerator takes air at 1 bar and 300 K, compresses it to 4 bar, cools it "
             "back to 300 K in the aftercooler, and expands it through a turbine to 1 bar. "
             "γ = 1.4.",
             "Air refrigerator 1 bar તથા 300 K પર હવા લે, તેને 4 bar સુધી compress કરે, aftercooler માં "
             "પાછી 300 K સુધી ઠંડી કરે, અને turbine માં 1 bar સુધી expand કરે. γ = 1.4."),
    find=bi("The COP of the ideal cycle.",
            "આદર્શ cycle નો COP."),
    formula=[E("COP = 1/(r_p^((γ−1)/γ) − 1)", r"COP=\frac{1}{r_p^{(\gamma-1)/\gamma}-1}")],
    substitution=bi(
        "(γ−1)/γ = 0.4/1.4 = 0.2857. r_p^0.2857 = 4^0.2857 = 1.486. "
        "COP = 1/(1.486 − 1) = 1/0.486 = 2.06.",
        "(γ−1)/γ = 0.4/1.4 = 0.2857. r_p^0.2857 = 4^0.2857 = 1.486. "
        "COP = 1/(1.486 − 1) = 1/0.486 = 2.06."),
    answer=bi("COP = 2.06 for a pressure ratio of 4.",
              "pressure ratio 4 માટે COP = 2.06."),
    check=bi("A vapour cycle on the same duty would reach a COP near 4, so the air cycle loses "
             "about half. Raising the pressure ratio raises the COP slightly but also raises the "
             "compressor discharge temperature, which is why regeneration is used.",
             "એ જ કામ પર vapour cycle લગભગ 4 COP પામે, તેથી air cycle લગભગ અડધું ગુમાવે. Pressure ratio "
             "વધારતાં COP થોડો વધે પણ compressor discharge temperature પણ વધે, એટલે જ regeneration વપરાય."),
)

N5 = numerical(
    "N5",
    bi("Refrigerant flow rate and compressor power from a capacity",
       "capacity પરથી refrigerant flow rate તથા compressor power"),
    given=bi("A plant of 25 TR capacity uses R-22 with a refrigerating effect of 155 kJ/kg and a "
             "compressor work of 38 kJ/kg.",
             "25 TR capacity વાળી plant R-22 વાપરે છે, refrigerating effect 155 kJ/kg તથા compressor "
             "work 38 kJ/kg."),
    find=bi("The mass flow of refrigerant, the compressor power and the COP.",
            "refrigerant નો mass flow, compressor power તથા COP."),
    formula=[E("Q_C = 25 × 3.517 kW", r"Q_C=25\times3.517"),
             E("m = Q_C/q_C        P = m w", r"m=\frac{Q_C}{q_C}"),
             E("COP = q_C/w", r"COP=\frac{q_C}{w}")],
    substitution=bi(
        "Q_C = 25 × 3.517 = 87.9 kW. m = 87.9/155 = 0.567 kg/s. "
        "P = 0.567 × 38 = 21.6 kW. COP = 155/38 = 4.08.",
        "Q_C = 25 × 3.517 = 87.9 kW. m = 87.9/155 = 0.567 kg/s. "
        "P = 0.567 × 38 = 21.6 kW. COP = 155/38 = 4.08."),
    answer=bi("m = 0.567 kg/s;  compressor power = 21.6 kW;  COP = 4.08.",
              "m = 0.567 kg/s;  compressor power = 21.6 kW;  COP = 4.08."),
    check=bi("Check by the energy route: Q_H = 87.9 + 21.6 = 109.5 kW, and COP_HP = 109.5/21.6 = "
             "5.08 = 4.08 + 1, exactly as the heat pump relation requires.",
             "Energy માર્ગે ચકાસો: Q_H = 87.9 + 21.6 = 109.5 kW, અને COP_HP = 109.5/21.6 = 5.08 = "
             "4.08 + 1, જે heat pump સંબંધ પ્રમાણે બરાબર છે."),
)

# =============================================================== viva
VIVA = [
    viva(bi("Define COP and explain why it can be greater than one.",
            "COP વ્યાખ્યાયિત કરો અને તે એકથી વધુ કેમ હોઈ શકે તે સમજાવો."),
         bi("COP = Q_C/W, the heat removed per unit work. It exceeds one because the heat is not "
            "created by the work — the work only moves heat from a low-temperature source, and "
            "most of the heat delivered comes from that source. Only the first law's energy "
            "accounting is involved, and it balances as Q_H = Q_C + W.",
            "COP = Q_C/W, પ્રતિ unit work કાઢેલી heat. તે એકથી વધુ થાય કારણ કે heat work થી ઉત્પન્ન થતી નથી "
            "— work ફક્ત નીચા temperature ના source માંથી heat ખસેડે છે, અને મોટા ભાગની heat એ source માંથી "
            "આવે. ફક્ત પ્રથમ નિયમનો હિસાબ છે, અને Q_H = Q_C + W તરીકે સંતુલિત થાય.")),
    viva(bi("What is a ton of refrigeration? Convert it to kW.",
            "ton of refrigeration એટલે શું? તેને kW માં ફેરવો."),
         bi("The heat removal needed to freeze one short ton (907 kg) of water at 0 °C into ice at "
            "0 °C in 24 h. Using the latent heat 334 kJ/kg: 907 × 334/86 400 = 3.51 kW, usually "
            "quoted as 3.517 kW = 12 000 Btu/h.",
            "0 °C ના 1 short ton (907 kg) પાણીને 24 કલાકમાં 0 °C ના બરફમાં ફેરવવા જેટલી heat કાઢવી. Latent "
            "heat 334 kJ/kg વાપરીને: 907 × 334/86 400 = 3.51 kW, સામાન્ય રીતે 3.517 kW = 12 000 Btu/h.")),
    viva(bi("Derive the Carnot COP of a refrigerator.",
            "refrigerator નો Carnot COP મેળવો."),
         bi("For a reversible cycle Q_C/Q_H = T_C/T_H and W = Q_H − Q_C, so "
            "COP = Q_C/(Q_H − Q_C) = T_C/(T_H − T_C). It is the maximum for the given two "
            "temperatures and needs absolute temperatures.",
            "reversible cycle માટે Q_C/Q_H = T_C/T_H અને W = Q_H − Q_C, તેથી "
            "COP = Q_C/(Q_H − Q_C) = T_C/(T_H − T_C). આપેલા બે temperatures માટે તે મહત્તમ છે અને absolute "
            "temperatures માંગે છે.")),
    viva(bi("Why is a throttle valve used instead of an expander in a vapour-compression plant?",
            "vapour-compression plant માં expander ને બદલે throttle valve કેમ વપરાય?"),
         bi("A throttle has no moving parts and is cheap and reliable. An expander would recover "
            "some work and give a better COP, but it is expensive, needs lubrication and is "
            "unreliable when the fluid is wet. The lost work is accepted as the price of "
            "simplicity.",
            "Throttle માં ફરતો ભાગ નથી અને તે સસ્તું તથા ભરોસાપાત્ર છે. Expander થોડું work પાછું મેળવીને સારો "
            "COP આપે, પણ તે ખર્ચાળ છે, lubrication માંગે છે અને fluid ભીનું હોય ત્યારે ભરોસાપાત્ર નથી. ગુમાવેલું "
            "work સરળતાની કિંમત તરીકે સ્વીકારાય.")),
    viva(bi("Explain the R-numbering code with two examples.",
            "બે ઉદાહરણ સાથે R-numbering code સમજાવો."),
         bi("For halocarbons: C−1, H+1, F in order. R-134a = 1 carbon, 3 hydrogen, 4 fluorine = "
            "C₂H₂F₄. Inorganics: R-700 + molar mass, so R-717 = ammonia (M = 17) and R-744 = "
            "carbon dioxide (M = 44).",
            "Halocarbons માટે: C−1, H+1, F એ ક્રમમાં. R-134a એટલે 1 carbon, 3 hydrogen, 4 fluorine = "
            "C₂H₂F₄. Inorganics: R-700 + molar mass, તેથી R-717 = ammonia (M = 17) અને R-744 = "
            "carbon dioxide (M = 44).")),
    viva(bi("What do ODP and GWP mean, and why did the industry leave CFCs?",
            "ODP તથા GWP એટલે શું, અને ઉદ્યોગે CFCs કેમ છોડ્યા?"),
         bi("ODP is the ozone depletion potential relative to R-11, GWP the global warming "
            "potential relative to CO₂ over 100 years. CFCs contain chlorine, which destroys "
            "stratospheric ozone, and they persist for decades; the Montreal Protocol banned "
            "them, and HFCs that replaced them are now being cut under Kigali for their high GWP.",
            "ODP એટલે R-11 ના સંદર્ભમાં ozone depletion potential, GWP એટલે 100 વર્ષમાં CO₂ ના સંદર્ભમાં "
            "global warming potential. CFCs માં chlorine હોય છે જે stratospheric ozone નો નાશ કરે, અને તે "
            "દાયકાઓ સુધી ટકે; Montreal Protocol એ તેમના પર પ્રતિબંધ મૂક્યો, અને તેમના વિકલ્પ HFCs હવે ઊંચા GWP "
            "માટે Kigali હેઠળ ઘટાડાઈ રહ્યા છે.")),
    viva(bi("Give the properties a good refrigerant should have.",
            "સારા refrigerant માં કયા ગુણધર્મ હોવા જોઈએ?"),
         bi("Evaporating pressure just above atmospheric, moderate condensing pressure, large "
            "latent heat, high critical temperature, low toxicity and flammability, zero ODP, low "
            "GWP, good oil miscibility, easy leak detection and low cost.",
            "Evaporating pressure atmosphere થી થોડું ઉપર, મર્યાદિત condensing pressure, મોટી latent heat, "
            "ઊંચું critical temperature, ઓછી toxicity તથા flammability, શૂન્ય ODP, નીચું GWP, સારી oil "
            "miscibility, સહેલું leak detection તથા ઓછો ખર્ચ.")),
    viva(bi("Why does an air refrigerator have a lower COP than a vapour one?",
            "air refrigerator નો COP vapour કરતાં નીચો કેમ હોય?"),
         bi("Air has no latent heat, so a large mass of it must be circulated to move a given heat, "
            "and the sensible-heat swing is limited. Its COP is fixed by the pressure ratio, so it "
            "cannot be tuned. The vapour cycle gains from the large latent heat of condensation.",
            "હવામાં latent heat નથી, તેથી આપેલી heat ખસેડવા મોટો mass ફેરવવો પડે, અને sensible-heat ફેરફાર "
            "મર્યાદિત છે. તેનો COP pressure ratio થી નિશ્ચિત થાય, તેથી ગોઠવી શકાય નહીં. Vapour cycle ને "
            "condensation ની મોટી latent heat ફાયદો આપે.")),
]

# =============================================================== exam
EXAM = [
    exam(bi("Define refrigeration and coefficient of performance. Derive the COP of a reversed "
            "Carnot cycle and explain why no refrigerator can exceed it.",
            "Refrigeration તથા coefficient of performance વ્યાખ્યાયિત કરો. reversed Carnot cycle નો COP મેળવો "
            "અને કોઈ refrigerator તેને કેમ વટાવી શકે નહીં તે સમજાવો."), 4),
    exam(bi("What is a ton of refrigeration? Show that 1 TR = 3.517 kW.",
            "ton of refrigeration એટલે શું? 1 TR = 3.517 kW દર્શાવો."), 4),
    exam(bi("With a neat sketch, describe the vapour-compression refrigeration cycle and mark the "
            "four processes on a P–h diagram.",
            "સ્વચ્છ આકૃતિ સાથે vapour-compression refrigeration cycle વર્ણવો અને P–h diagram પર ચાર પ્રક્રિયાઓ "
            "દર્શાવો."), 4),
    exam(bi("Derive the expression COP = (h₁ − h₄)/(h₂ − h₁) for a vapour-compression cycle and "
            "state the assumption used at the expansion device.",
            "vapour-compression cycle માટે COP = (h₁ − h₄)/(h₂ − h₁) મેળવો અને expansion device પર વપરાયેલી "
            "ધારણા જણાવો."), 4),
    exam(bi("Describe the air-refrigeration cycle with a sketch and derive its COP in terms of the "
            "pressure ratio. Give two applications.",
            "સ્કેચ સાથે air-refrigeration cycle વર્ણવો અને pressure ratio ના પદમાં તેનો COP મેળવો. બે ઉપયોગો "
            "જણાવો."), 4),
    exam(bi("Classify refrigerants and explain the ASHRAE numbering system with four examples.",
            "Refrigerants નું વર્ગીકરણ કરો અને ચાર ઉદાહરણ સાથે ASHRAE numbering system સમજાવો."), 4),
    exam(bi("Discuss the factors that govern the choice of a refrigerant, including the "
            "environmental considerations of ODP and GWP.",
            "Refrigerant ની પસંદગી નક્કી કરતા પરિબળો ચર્ચો, જેમાં ODP તથા GWP ની પર્યાવરણીય બાબતો સામેલ કરો."), 4),
    exam(bi("A refrigerator removes 12 000 kJ/h and consumes 1.5 kW. Find the COP, the heat "
            "rejected and the capacity in TR.",
            "Refrigerator 12 000 kJ/h કાઢે છે અને 1.5 kW વાપરે છે. COP, ફેંકાતી heat તથા TR માં capacity શોધો."), 4),
    exam(bi("A cold store at −18 °C rejects heat to 32 °C air. Find the Carnot COP and the actual "
            "COP if 8 kW produces 20 kW of cooling.",
            "−18 °C નું cold store 32 °C હવાને heat ફેંકે છે. 8 kW વાપરીને 20 kW cooling મળે તો Carnot COP તથા "
            "વાસ્તવિક COP શોધો."), 4),
    exam(bi("An R-134a plant works between 1.5 bar and 8 bar with h₁ = 389.6, h₂ = 424.7 and "
            "h₃ = 220.5 kJ/kg at 0.05 kg/s. Find the COP and the capacity.",
            "R-134a plant 1.5 bar તથા 8 bar વચ્ચે ચાલે, h₁ = 389.6, h₂ = 424.7 તથા h₃ = 220.5 kJ/kg, "
            "flow 0.05 kg/s. COP તથા capacity શોધો."), 4),
    exam(bi("An air refrigerator works between 1 bar and 4 bar with γ = 1.4. Calculate its COP "
            "and compare it with a vapour cycle on the same lift.",
            "Air refrigerator 1 bar તથા 4 bar વચ્ચે ચાલે, γ = 1.4. તેનો COP ગણો અને એ જ lift પરના vapour "
            "cycle સાથે સરખાવો."), 4),
    exam(bi("A 25 TR plant uses a refrigerant of refrigerating effect 155 kJ/kg and compressor "
            "work 38 kJ/kg. Find the mass flow, the power and the COP.",
            "25 TR plant માં refrigerating effect 155 kJ/kg તથા compressor work 38 kJ/kg છે. mass flow, "
            "power તથા COP શોધો."), 4),
]

# =============================================================== formulae
SYNTAX = [
    {"title": bi("Performance and capacity", "performance તથા capacity"),
     "items": [
         {"title": bi("COP", "COP"),
          "f": "COP = Q_C/W = Q_C/(Q_H − Q_C);  heat pump: COP + 1",
          "terms": "COP has no unit; it is not an efficiency and may exceed one."},
         {"title": bi("Carnot limit", "Carnot મર્યાદા"),
          "f": "COP_max = T_C/(T_H − T_C)",
          "terms": "Absolute temperatures only; the COP falls as the lift grows."},
         {"title": bi("Capacity", "Capacity"),
          "f": "1 TR = 3.517 kW = 12 000 Btu/h = 50 kcal/min = 210 kJ/min",
          "terms": "Capacity is a rate; COP is a ratio. They are independent."},
     ]},
    {"title": bi("Cycle equations", "cycle ના સમીકરણો"),
     "items": [
         {"title": bi("Vapour compression", "vapour compression"),
          "f": "q_C = h₁ − h₄,  w = h₂ − h₁,  q_H = h₂ − h₃,  COP = q_C/w",
          "terms": "Throttle is isenthalpic, so h₄ = h₃ — that is what closes the cycle."},
         {"title": bi("Air cycle", "air cycle"),
          "f": "COP = 1/(r_p^((γ−1)/γ) − 1)",
          "terms": "Depends only on pressure ratio and γ, so it cannot be tuned."},
         {"title": bi("Energy balance", "energy balance"),
          "f": "Q_H = Q_C + W;  Q_H > Q_C always",
          "terms": "The condenser must reject more heat than the evaporator absorbs."},
     ]},
    {"title": bi("Refrigerant data", "refrigerant માહિતી"),
     "items": [
         {"title": bi("Numbering", "numbering"),
          "f": "halocarbon: C−1, H+1, F;  inorganic: R-700 + M",
          "terms": "R-134a = C₂H₂F₄;  R-717 = NH₃;  R-744 = CO₂."},
         {"title": bi("Environment", "environment"),
          "f": "ODP: CFC 1.0 → HCFC 0.05 → HFC 0;  GWP₁₀₀: R-134a 1430, R-404A 3922",
          "terms": "Naturals (NH₃, CO₂, hydrocarbons) have ODP 0 and GWP ≈ 0 or 1."},
         {"title": bi("Safety class", "safety class"),
          "f": "A = lower toxicity, B = higher;  1 / 2L / 2 / 3 = flammability",
          "terms": "R-134a A1, R-410A A1, NH₃ B2L, propane A3."},
     ]},
]

# =============================================================== build
def build() -> Unit:
    u = Unit(CODE, 5, TITLE, hours=6, weightage=16,
             tabs=["notes", "programs", "diagrams", "syntax", "viva", "exam"],
             tab_labels={"programs": bi("Solved numericals", "ઉકેલેલા દાખલા"),
                         "syntax": bi("Formulae and conversions", "સૂત્રો તથા conversions")})
    u.section(bi("5.1  Refrigeration, COP and capacity", "5.1  Refrigeration, COP તથા capacity"), S1)
    u.section(bi("5.2  The vapour-compression cycle", "5.2  vapour-compression cycle"), S2)
    u.section(bi("5.3  Refrigerants and their codes", "5.3  Refrigerants તથા તેમના codes"), S3)
    u.section(bi("5.4  Choice of refrigerant", "5.4  refrigerant ની પસંદગી"), S4)
    u.data["programs"] = [N1, N2, N3, N4, N5]
    u.diagram("d5_refrigeration_loop",
              bi("The vapour-compression refrigerator", "vapour-compression refrigerator"),
              "diagrams/d5_refrigeration_loop.svg")
    u.diagram("d5_ph_cycle",
              bi("The cycle on a P–h diagram", "P–h diagram પર cycle"),
              "diagrams/d5_ph_cycle.svg")
    u.diagram("d5_air_refrigeration",
              bi("The reversed Brayton (air) cycle", "reversed Brayton (air) cycle"),
              "diagrams/d5_air_refrigeration.svg")
    u.diagram("d5_refrigerant_choice",
              bi("Choosing a refrigerant", "refrigerant ની પસંદગી"),
              "diagrams/d5_refrigerant_choice.svg")
    for s in SYNTAX:
        u.data.setdefault("syntax", []).append(s)
    u.data["viva"] = VIVA
    u.data["exam_questions"] = EXAM
    return u


if __name__ == "__main__":
    unit = build()
    problems = unit.validate()
    out = unit.write("content/chemical/sem4/DI04005041/unit5.json")
    print("wrote", out)
    print("problems:", problems or "none")
