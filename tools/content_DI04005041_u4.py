"""Content for DI04005041 Unit 4 "Second Law of Thermodynamics", GTU Diploma
Chemical Engineering, semester 4, syllabus w.e.f. 2025-26.

Coverage is the official syllabus 4.1 - 4.10:
  4.1 limitations of the first law
  4.2 heat reservoir, heat engine and heat pump
  4.3 general statement of the second law
  4.4 concept of entropy
  4.5 Carnot principle; thermodynamic temperature scale; ideal gas as the
      Carnot engine working substance
  4.6 entropy changes: phase change, ideal-gas process, adiabatic mixing,
      isothermal mixing of ideal gases, chemical reaction
  4.7 Clausius inequality
  4.8 mathematical statement of the second law
  4.9 numericals on entropy change and heat-engine efficiency
  4.10 statement of the third law

Reference matter: Narayanan; Smith, Van Ness & Abbott; Gavhane; Rajput.
"""
from d1notes import Unit, bi, derivation, exam, numerical, theory, viva


def E(display, tex=None, note=None):
    return (display, tex or display, note) if note else (display, tex or display)


CODE = "DI04005041"
TITLE = bi("Second Law of Thermodynamics", "થર્મોડાયનેમિક્સનો દ્વિતીય નિયમ")

# =============================================================== 4.1 first-law limits
S1 = [
    theory(
        "4.1",
        bi("Limitations of the first law", "પ્રથમ નિયમની મર્યાદાઓ"),
        definition=bi(
            "The first law is an energy <i>balance</i>: it accounts for what goes in and what "
            "comes out, but it says nothing about whether a process can actually happen, or in "
            "which direction. A process that satisfies Q − W = ΔU may still be impossible — "
            "every statement of the second law is a correction to that silence.",
            "પ્રથમ નિયમ ઊર્જાનું <i>balance</i> છે: તે અંદર જે આવે અને બહાર જે જાય તેનો હિસાબ રાખે છે, પણ "
            "પ્રક્રિયા ખરેખર થઈ શકે કે નહીં, કે કઈ દિશામાં થશે તે કંઈ કહેતો નથી. Q − W = ΔU સંતોષતી "
            "પ્રક્રિયા પણ અશક્ય હોઈ શકે — દ્વિતીય નિયમનું દરેક વિધાન એ સ્થિતિનો સુધારો છે."),
        theory_text=bi(
            "Take a cup of hot coffee and a room. The first law is equally happy with the coffee "
            "cooling to room temperature or the room spontaneously cooling further while the "
            "coffee gets hotter — the energy balances both ways. Only the second law rules the "
            "second process out. In the same way the first law permits an engine that takes "
            "heat from the sea and converts it entirely into work, and it permits heat to flow "
            "from cold to hot without help; neither is observed, and each would give free "
            "energy.<br><br>"
            "The second law therefore supplies three things the first law cannot: the "
            "<b>direction</b> in which a process will go, the <b>condition of equilibrium</b> "
            "where it stops, and the <b>maximum</b> work a given change can deliver.",
            "ગરમ કોફીનો કપ તથા એક રૂમ લો. કોફી રૂમના temperature સુધી ઠંડી થાય કે રૂમ વધુ ઠંડો થઈને "
            "કોફી વધુ ગરમ થાય — પ્રથમ નિયમ બંને સાથે સંતુષ્ટ છે; ઊર્જા બંને રીતે સંતુલિત થાય. ફક્ત દ્વિતીય "
            "નિયમ બીજી પ્રક્રિયાને નકારે છે. એ જ રીતે પ્રથમ નિયમ એવા engine ને માન્ય ગણે જે સમુદ્રમાંથી heat "
            "લઈ આખું work માં ફેરવે, અને heat ને મદદ વગર ઠંડા થી ગરમ તરફ જવા દે; બંને કદી જોવાયા નથી, "
            "અને દરેક મફત ઊર્જા આપે.<br><br>"
            "તેથી દ્વિતીય નિયમ ત્રણ વસ્તુ આપે છે જે પ્રથમ નિયમ નથી આપી શકતું: પ્રક્રિયા જે "
            "<b>દિશામાં</b> જશે, જ્યાં અટકશે તે <b>equilibrium ની શરત</b>, અને આપેલા ફેરફારથી મળી શકતું "
            "<b>મહત્તમ</b> work."),
        list_items=[
            "<b>First law permits:</b> coffee heating itself and cooling the room; an engine running on the sea; ice forming in warm water.",
            "<b>Second law rules out:</b> each of those, without an external work input.",
            "<b>First law gives:</b> how much energy is involved. <b>Second law gives:</b> how much of it can become work.",
            "This is why every real engine's efficiency is measured against the Carnot value, not against 100 %.",
        ],
        qualification=bi(
            "The first law is not wrong; it is incomplete. Both laws must be satisfied together, "
            "and in practice the first law is used to size equipment while the second law decides "
            "whether the scheme is worth building at all.",
            "પ્રથમ નિયમ ખોટો નથી; અપૂર્ણ છે. બંને નિયમો સાથે સંતોષવા પડે, અને વ્યવહારમાં પ્રથમ નિયમ "
            "equipment નું size નક્કી કરવા વપરાય જ્યારે દ્વિતીય નિયમ નક્કી કરે કે યોજના બનાવવા જેવી છે કે નહીં."),
    ),
]

# =============================================================== 4.2 devices
S2 = [
    theory(
        "4.2",
        bi("Heat reservoir, heat engine, refrigerator and heat pump",
           "Heat reservoir, heat engine, refrigerator તથા heat pump"),
        definition=bi(
            "A <b>heat reservoir</b> is a body of such large heat capacity that taking heat from "
            "it or giving heat to it does not change its temperature. A <b>heat engine</b> is a "
            "cyclic device that absorbs Q<sub>H</sub> from a hot reservoir, rejects "
            "Q<sub>C</sub> to a cold reservoir and delivers work W = Q<sub>H</sub> − "
            "Q<sub>C</sub>. A <b>refrigerator</b> and a <b>heat pump</b> run the same cycle in "
            "reverse and consume work to move heat from cold to hot.",
            "<b>Heat reservoir</b> એટલી મોટી heat capacity ધરાવતું શરીર છે કે તેમાંથી heat લેવાય કે "
            "આપાય તો પણ તેનું temperature બદલાય નહીં. <b>Heat engine</b> એ ચક્રીય ઉપકરણ છે જે ગરમ "
            "reservoir માંથી Q<sub>H</sub> લે, ઠંડા reservoir ને Q<sub>C</sub> આપે અને work "
            "W = Q<sub>H</sub> − Q<sub>C</sub> આપે. <b>Refrigerator</b> તથા <b>heat pump</b> એ જ cycle "
            "ઉલટી દિશામાં ચલાવીને ઠંડા થી ગરમ તરફ heat ખસેડવા work વાપરે છે."),
        theory_text=bi(
            "Three performance measures follow from the same energy balance, and they are easy to "
            "confuse. The engine <b>efficiency</b> is what you get out for what you paid for: "
            "η = W/Q<sub>H</sub>. The refrigerator <b>coefficient of performance</b> is what you "
            "remove for the work you buy: COP<sub>R</sub> = Q<sub>C</sub>/W. The heat pump COP is "
            "what you deliver for the same work: COP<sub>HP</sub> = Q<sub>H</sub>/W, and the two "
            "COPs differ by exactly one because Q<sub>H</sub> = Q<sub>C</sub> + W.<br><br>"
            "Because a COP can be greater than one (a domestic heat pump delivers 3–4 kW of heat "
            "per kW of electricity) it is never called an efficiency. An efficiency above one "
            "would be a first-law violation; a COP above one is perfectly normal, because the "
            "extra energy comes from the cold reservoir, not from nowhere.",
            "એક જ energy balance પરથી ત્રણ performance માપ મળે છે, અને તે ભેળવી દેવા સહેલા છે. Engine ની "
            "<b>efficiency</b> એટલે જે મળે તે ભાગ્યે જે આપ્યું: η = W/Q<sub>H</sub>. Refrigerator નો "
            "<b>coefficient of performance</b> એટલે જે work ખરીદ્યું તેના ભાગ્યે જે heat કાઢી: "
            "COP<sub>R</sub> = Q<sub>C</sub>/W. Heat pump નો COP એ જ work માટે જે આપ્યું તે: "
            "COP<sub>HP</sub> = Q<sub>H</sub>/W, અને બંને COP માં બરાબર એકનો તફાવત હોય છે કારણ કે "
            "Q<sub>H</sub> = Q<sub>C</sub> + W.<br><br>"
            "COP એકથી મોટો હોઈ શકે (ઘરેલું heat pump પ્રતિ kW વીજળી 3–4 kW heat આપે) તેથી તેને કદી "
            "efficiency નહીં કહેવાય. એકથી મોટી efficiency પ્રથમ નિયમનો ભંગ થાય, પણ એકથી મોટો COP સાવ "
            "સામાન્ય છે, કારણ કે વધારાની ઊર્જા ઠંડા reservoir માંથી આવે છે, ક્યાંયથી નહીં."),
        equations=[E("engine:  W = Q_H − Q_C ,   η = W / Q_H", r"\eta=\frac{W}{Q_H}"),
                   E("refrigerator:  COP_R = Q_C / W", r"COP_R=\frac{Q_C}{W}"),
                   E("heat pump:  COP_HP = Q_H / W = COP_R + 1", r"COP_{HP}=COP_R+1"),
                   E("Carnot:  η = 1 − T_C/T_H ;  COP_R = T_C/(T_H − T_C)", r"\eta=1-\frac{T_C}{T_H}")],
        list_items=[
            "<b>Reservoir examples:</b> the atmosphere, a river, a large steam main, a furnace — anything whose temperature does not move.",
            "<b>Engine:</b> steam power plant, petrol engine, gas turbine.",
            "<b>Refrigerator:</b> domestic fridge, air-conditioning, cold store.",
            "<b>Heat pump:</b> the same hardware as a fridge, but the useful output is the heat rejected at the warm side.",
        ],
        diagram="d4_heat_devices",
        qualification=bi(
            "A device with η = 100 % would convert all the heat from one reservoir into work. "
            "The Kelvin–Planck statement forbids it, so no engine can reach it, and a real "
            "engine is always judged by how far below the Carnot value it runs.",
            "η = 100 % વાળું ઉપકરણ એક જ reservoir ની આખી heat work માં ફેરવે. Kelvin–Planck વિધાન તેને "
            "નિષેધે, તેથી કોઈ engine તેને પામી શકે નહીં, અને વાસ્તવિક engine હંમેશા Carnot કિંમતથી "
            "કેટલું નીચે છે તેના પરથી મપાય."),
    ),
]

# =============================================================== 4.3 statements
S3 = [
    theory(
        "4.3",
        bi("General statements of the second law", "દ્વિતીય નિયમનાં સામાન્ય વિધાનો"),
        definition=bi(
            "The second law has several equivalent statements; all say that a certain kind of "
            "process is impossible. <b>Kelvin–Planck:</b> no cyclic device can take heat from a "
            "single reservoir and convert it entirely into work. <b>Clausius:</b> no device can "
            "transfer heat from a colder body to a hotter body without work input. "
            "<b>Entropy:</b> the entropy of an isolated system never decreases.",
            "દ્વિતીય નિયમનાં અનેક સમાનાર્થી વિધાનો છે; બધાં કહે છે કે અમુક પ્રકારની પ્રક્રિયા અશક્ય છે. "
            "<b>Kelvin–Planck:</b> કોઈ ચક્રીય ઉપકરણ એક જ reservoir માંથી heat લઈને તેને પૂરેપૂરી work માં "
            "ફેરવી શકે નહીં. <b>Clausius:</b> work input વગર કોઈ ઉપકરણ heat ને ઠંડા શરીરથી ગરમ શરીર તરફ "
            "ખસેડી શકે નહીં. <b>Entropy:</b> isolated system ની entropy કદી ઘટતી નથી."),
        theory_text=bi(
            "The statements look different but are logically identical: if you could violate one "
            "you could build a machine that violates the other, so accepting one forces you to "
            "accept all. A useful way to remember them is by what each forbids — a perpetual "
            "motion machine of the <b>second kind</b> for Kelvin–Planck (work from a single "
            "reservoir), and self-acting refrigeration for Clausius.<br><br>"
            "Note the words 'cyclic device' and 'without work input'. A non-cyclic process can "
            "convert heat entirely into work — an isothermal ideal-gas expansion does exactly "
            "that — but the gas has expanded and cannot repeat without being compressed, and the "
            "compression costs work. The restriction is on a device that returns to its own "
            "starting state, which is what an engine must do.",
            "વિધાનો જુદાં લાગે પણ તાર્કિક રીતે એક જ છે: એકનો ભંગ કરી શકાય તો બીજાનો ભંગ કરતું ઉપકરણ "
            "બનાવી શકાય, તેથી એક સ્વીકારતાં બધાં સ્વીકારવાં પડે. યાદ રાખવાની સારી રીત એ છે કે દરેક શું "
            "નિષેધે તે જોવું — Kelvin–Planck માટે <b>બીજા પ્રકારની</b> perpetual motion machine (એક જ "
            "reservoir માંથી work), અને Clausius માટે જાતે ચાલતું refrigeration.<br><br>"
            "'ચક્રીય ઉપકરણ' તથા 'work input વગર' શબ્દો ધ્યાનમાં લો. બિન-ચક્રીય પ્રક્રિયા heat ને પૂરેપૂરી "
            "work માં ફેરવી શકે — isothermal ideal-gas expansion બરાબર એ જ કરે — પણ gas expand થઈ ગયો છે "
            "અને compress કર્યા વગર ફરી શકે નહીં, અને compression માં work લાગે. પ્રતિબંધ એ ઉપકરણ પર છે જે "
            "પોતાની શરૂઆતની state પર પાછું આવે, જે engine માટે જરૂરી છે."),
        equations=[E("Kelvin–Planck:  W = Q_H  with a single reservoir is impossible",
                     r"W=Q_H\ \text{impossible}"),
                   E("Clausius:  Q_C → Q_H  with W = 0 is impossible", r"Q_C\to Q_H,\ W=0\ \text{impossible}"),
                   E("entropy:  ΔS_universe ≥ 0   (= 0 only for a reversible process)",
                     r"\Delta S_{universe}\ge 0")],
        list_items=[
            "<b>Kelvin–Planck</b> is the statement used for engines: it caps the efficiency.",
            "<b>Clausius</b> is the statement used for refrigerators: it is why a fridge needs a compressor.",
            "<b>Entropy</b> is the statement used for calculations: it gives a number to compare.",
            "A <b>perpetual motion machine of the second kind</b> would extract work from a single reservoir; it is forbidden even though it would satisfy the first law.",
        ],
        qualification=bi(
            "These are statements of experience, not proofs. No exception has ever been found, "
            "and statistical mechanics explains why: the reverse of an entropy-increasing process "
            "is not impossible but so improbable that it never happens on a human timescale.",
            "આ અનુભવનાં વિધાનો છે, સાબિતીઓ નહીં. આજ સુધી કોઈ અપવાદ મળ્યો નથી, અને statistical mechanics "
            "કારણ આપે છે: entropy વધારતી પ્રક્રિયાનું ઉલટું અશક્ય નથી પણ એટલું અસંભવિત છે કે માનવ સમયમાપક્રમ "
            "પર કદી થાય નહીં."),
    ),
]

# =============================================================== 4.4 entropy
S4 = [
    theory(
        "4.4",
        bi("Concept of entropy", "entropy નો ખ્યાલ"),
        definition=bi(
            "<b>Entropy S</b> is a state function defined by the reversible path between two "
            "states: <b>dS = δQ<sub>rev</sub>/T</b>. Its unit is kJ/K. Physically it is a measure "
            "of how the energy of a system is dispersed, and statistically it is S = k ln Ω, "
            "where Ω is the number of microscopic arrangements consistent with the observed "
            "state.",
            "<b>Entropy S</b> એ state function છે જે બે states વચ્ચેના reversible રસ્તા દ્વારા "
            "વ્યાખ્યાયિત થાય: <b>dS = δQ<sub>rev</sub>/T</b>. તેનું unit kJ/K છે. ભૌતિક રીતે તે "
            "system ની ઊર્જા કેટલી વિખેરાયેલી છે તેનું માપ છે, અને આંકડાકીય રીતે S = k ln Ω, જ્યાં Ω "
            "એ દેખાતી state સાથે સુસંગત microscopic ગોઠવણોની સંખ્યા છે."),
        theory_text=bi(
            "Because S is a state function, the change between two states is the same by every "
            "path. To calculate it you therefore integrate along a <b>reversible</b> path between "
            "the two states even if the real process is violently irreversible — the real path "
            "and the reversible path share the same end states, so they share the same ΔS. This "
            "single idea is the trick behind every entropy numerical.<br><br>"
            "For an isolated system the second law becomes <b>ΔS ≥ 0</b>: entropy is created in "
            "every irreversible process and stays constant only in a reversible one. A "
            "reversible adiabatic process is therefore <b>isentropic</b> (ΔS = 0), which is why "
            "ideal compressors and turbines are analysed as isentropic devices.",
            "S state function હોવાથી બે states વચ્ચેનો ફેરફાર દરેક રસ્તે સરખો હોય. તેથી તેને ગણવા માટે "
            "તમે બંને states વચ્ચેના <b>reversible</b> રસ્તે integrate કરો, ભલે વાસ્તવિક પ્રક્રિયા ખૂબ "
            "irreversible હોય — વાસ્તવિક તથા reversible રસ્તાના અંતિમ states સરખા હોય, તેથી ΔS પણ સરખું "
            "હોય. આ એક વિચાર દરેક entropy દાખલાની ચાવી છે.<br><br>"
            "Isolated system માટે દ્વિતીય નિયમ <b>ΔS ≥ 0</b> બને છે: દરેક irreversible પ્રક્રિયામાં "
            "entropy ઉત્પન્ન થાય અને ફક્ત reversible પ્રક્રિયામાં અચળ રહે. તેથી reversible adiabatic "
            "પ્રક્રિયા <b>isentropic</b> (ΔS = 0) છે, એટલે જ ideal compressor તથા turbine નું "
            "વિશ્લેષણ isentropic ઉપકરણ તરીકે થાય."),
        equations=[E("dS = δQ_rev / T        ΔS = ∫₁² δQ_rev / T", r"dS=\frac{\delta Q_{rev}}{T}"),
                   E("S₂ − S₁ = m c_v ln(T₂/T₁) + m R ln(V₂/V₁)", r"\Delta S=mc_v\ln\frac{T_2}{T_1}+mR\ln\frac{V_2}{V_1}"),
                   E("S₂ − S₁ = m c_p ln(T₂/T₁) − m R ln(P₂/P₁)", r"\Delta S=mc_p\ln\frac{T_2}{T_1}-mR\ln\frac{P_2}{P_1}"),
                   E("isolated system:  ΔS ≥ 0        reversible adiabatic:  ΔS = 0", r"\Delta S\ge 0")],
        list_items=[
            "<b>Entropy is extensive:</b> specific entropy s = S/m in kJ/kg·K.",
            "<b>Entropy is not 'disorder' in a vague sense</b> — it counts the number of ways the energy can be arranged. Melting ice increases it because the molecules gain more arrangements.",
            "<b>Reversible adiabatic = isentropic.</b> Irreversible adiabatic still has ΔS > 0.",
            "<b>Heat addition raises entropy; work addition need not.</b> Adiabatic compression raises temperature but not entropy if it is reversible.",
        ],
        qualification=bi(
            "Entropy is not conserved and it is not energy. There is no law of conservation of "
            "entropy — quite the opposite, it is the one quantity that is systematically created. "
            "Writing an 'entropy balance' in the same way as an energy balance is the commonest "
            "mistake in this topic.",
            "Entropy સંરક્ષિત નથી અને તે ઊર્જા નથી. Entropy સંરક્ષણનો કોઈ નિયમ નથી — ઊલટું, તે એક જ રાશિ છે "
            "જે વ્યવસ્થિત રીતે ઉત્પન્ન થાય છે. ઊર્જા balance ની જેમ 'entropy balance' લખવું એ આ વિષયની "
            "સૌથી સામાન્ય ભૂલ છે."),
    ),
]

# =============================================================== 4.5 Carnot
S5 = [
    theory(
        "4.5",
        bi("The Carnot principle", "Carnot નો સિદ્ધાંત"),
        definition=bi(
            "The <b>Carnot cycle</b> consists of four reversible processes: isothermal "
            "expansion at T<sub>H</sub>, adiabatic expansion to T<sub>C</sub>, isothermal "
            "compression at T<sub>C</sub>, and adiabatic compression back to T<sub>H</sub>. "
            "<b>Carnot's principle:</b> no engine operating between the same two reservoirs can "
            "be more efficient than a reversible engine, and all reversible engines between the "
            "same two reservoirs have the <b>same</b> efficiency, whatever the working substance.",
            "<b>Carnot cycle</b> ચાર reversible પ્રક્રિયાઓનો બનેલો છે: T<sub>H</sub> પર isothermal "
            "expansion, T<sub>C</sub> સુધી adiabatic expansion, T<sub>C</sub> પર isothermal "
            "compression, અને પાછું T<sub>H</sub> સુધી adiabatic compression. <b>Carnot નો સિદ્ધાંત:</b> "
            "બે સરખા reservoirs વચ્ચે ચાલતું કોઈ engine reversible engine કરતાં વધુ efficient ન હોઈ શકે, "
            "અને સરખા બે reservoirs વચ્ચેના બધા reversible engines ની efficiency <b>સરખી</b> જ હોય, working "
            "substance કોઈ પણ હોય."),
        theory_text=bi(
            "The proof is a proof by contradiction and is worth knowing because it is examinable. "
            "Suppose a reversible engine R were less efficient than some other engine E between "
            "the same reservoirs. Run E to drive R backwards as a refrigerator. The pair would "
            "then take heat from the cold reservoir and deliver it to the hot reservoir with no "
            "net work input — a Clausius violation. Therefore R cannot be less efficient than E. "
            "Reversing the roles shows E cannot be more efficient either, so all reversible "
            "engines are equal and no real engine can beat them.<br><br>"
            "The consequence is a temperature scale that does not depend on any substance: "
            "T<sub>C</sub>/T<sub>H</sub> = Q<sub>C</sub>/Q<sub>H</sub> for a reversible engine, so "
            "η = 1 − T<sub>C</sub>/T<sub>H</sub>. This is the <b>thermodynamic temperature "
            "scale</b>, and it agrees with the ideal-gas scale exactly.",
            "સાબિતી વિરોધાભાસ દ્વારા છે અને તે જાણવા જેવી છે કારણ કે પરીક્ષામાં પૂછાય છે. ધારો કે "
            "reversible engine R સરખા reservoirs વચ્ચેના બીજા engine E કરતાં ઓછું efficient છે. E ચલાવીને "
            "R ને ઉલટું refrigerator તરીકે ચલાવો. પછી આ જોડી કોઈ net work input વગર ઠંડા reservoir માંથી "
            "heat લઈને ગરમ reservoir ને આપે — Clausius નો ભંગ. તેથી R એ E કરતાં ઓછું efficient હોઈ શકે "
            "નહીં. ભૂમિકા ઉલટાવતાં દેખાય કે E પણ વધુ efficient ન હોઈ શકે, તેથી બધા reversible engines "
            "સરખા છે અને કોઈ વાસ્તવિક engine તેમને હરાવી શકે નહીં.<br><br>"
            "પરિણામ એ temperature scale છે જે કોઈ પદાર્થ પર આધાર રાખતું નથી: reversible engine માટે "
            "T<sub>C</sub>/T<sub>H</sub> = Q<sub>C</sub>/Q<sub>H</sub>, તેથી η = 1 − T<sub>C</sub>/T<sub>H</sub>. "
            "આ જ <b>thermodynamic temperature scale</b> છે, અને તે ideal-gas scale સાથે બરાબર મળે છે."),
        equations=[E("η_Carnot = 1 − T_C / T_H        (absolute temperatures only)", r"\eta=1-\frac{T_C}{T_H}"),
                   E("reversible engine:  Q_C/Q_H = T_C/T_H", r"\frac{Q_C}{Q_H}=\frac{T_C}{T_H}"),
                   E("COP_R = T_C/(T_H − T_C)        COP_HP = T_H/(T_H − T_C)", r"COP_R=\frac{T_C}{T_H-T_C}")],
        list_items=[
            "<b>Two temperatures only:</b> η depends on T<sub>H</sub> and T<sub>C</sub>, never on the working substance or on the size of the plant.",
            "<b>Raise T<sub>H</sub> or lower T<sub>C</sub></b> to improve efficiency — that is why power stations superheat steam.",
            "<b>Never reach 100 %:</b> η = 1 would need T<sub>C</sub> = 0 K, which is unattainable.",
            "<b>Carnot COP:</b> a refrigerator working between 300 K and 260 K has COP ≤ 6.5, whatever the refrigerant.",
        ],
        diagram="d4_carnot_cycle",
        qualification=bi(
            "The Carnot cycle cannot be built: it needs isothermal heat transfer at exactly the "
            "reservoir temperature (infinitely slow) and adiabatic processes (perfectly "
            "insulated). Its value is as a limit and as a comparison, not as a design.",
            "Carnot cycle બનાવી શકાય નહીં: તેને બરાબર reservoir temperature પર isothermal heat transfer "
            "(અનંત ધીમું) તથા adiabatic પ્રક્રિયાઓ (સંપૂર્ણ insulated) જોઈએ. તેનું મૂલ્ય મર્યાદા તથા "
            "સરખામણી તરીકે છે, design તરીકે નહીં."),
    ),
    derivation(
        "4.6",
        bi("Efficiency of the Carnot cycle with an ideal gas",
           "ideal gas સાથે Carnot cycle ની efficiency"),
        symbols=bi(
            "<b>Model:</b> one mole of an ideal gas as the working substance, taken round the "
            "four reversible steps of the Carnot cycle. <b>Assumptions:</b> ideal gas with "
            "constant c<sub>v</sub>, reversible processes throughout, the two reservoirs at "
            "T<sub>H</sub> and T<sub>C</sub> constant.",
            "<b>Model:</b> working substance તરીકે એક mole ideal gas, Carnot cycle ના ચાર reversible "
            "પગલાંમાં ફેરવાય છે. <b>Assumptions:</b> c<sub>v</sub> અચળ હોય તેવો ideal gas, બધી પ્રક્રિયાઓ "
            "reversible, બે reservoirs T<sub>H</sub> તથા T<sub>C</sub> પર અચળ."),
        steps=[
            (bi("Step 1→2: the gas expands isothermally at T_H, taking in heat Q_H.",
                "Step 1→2: gas T_H પર isothermal રીતે expand થાય, Q_H heat લે."),
             E("Q_H = W₁₂ = R T_H ln(V₂/V₁)", r"Q_H=RT_H\ln\frac{V_2}{V_1}")),
            (bi("Step 2→3: adiabatic expansion to T_C. No heat is exchanged, so Q = 0.",
                "Step 2→3: T_C સુધી adiabatic expansion. કોઈ heat ની આપલે નહીં, તેથી Q = 0."),
             E("T_H V₂^(γ−1) = T_C V₃^(γ−1)", r"T_HV_2^{\gamma-1}=T_CV_3^{\gamma-1}")),
            (bi("Step 3→4: isothermal compression at T_C, rejecting Q_C.",
                "Step 3→4: T_C પર isothermal compression, Q_C બહાર ફેંકાય."),
             E("Q_C = −W₃₄ = R T_C ln(V₃/V₄)", r"Q_C=RT_C\ln\frac{V_3}{V_4}")),
            (bi("Step 4→1: adiabatic compression back to T_H, closing the cycle.",
                "Step 4→1: પાછું T_H સુધી adiabatic compression, cycle પૂરો થાય."),
             E("T_C V₄^(γ−1) = T_H V₁^(γ−1)", r"T_CV_4^{\gamma-1}=T_HV_1^{\gamma-1}")),
            (bi("Divide the relation of step 4→1 by that of step 2→3. The temperatures and the "
                "power cancel, leaving a ratio of volumes.",
                "Step 4→1 નો સંબંધ step 2→3 વડે ભાગો. Temperature તથા power કપાઈ જાય, ફક્ત volumes નો "
                "ગુણોત્તર રહે."),
             E("V₂/V₁ = V₃/V₄", r"\frac{V_2}{V_1}=\frac{V_3}{V_4}")),
            (bi("Use that equality to replace the volume ratio in the two heat expressions, so "
                "Q_C/Q_H contains only temperatures.",
                "એ સમાનતા વાપરીને બંને heat ના સમીકરણમાં volume ગુણોત્તર બદલો, જેથી Q_C/Q_H માં ફક્ત "
                "temperatures રહે."),
             E("Q_C/Q_H = T_C/T_H", r"\frac{Q_C}{Q_H}=\frac{T_C}{T_H}")),
            (bi("Write the efficiency and substitute the heat ratio.",
                "efficiency લખો અને heat ગુણોત્તર મૂકો."),
             E("η = 1 − Q_C/Q_H = 1 − T_C/T_H", r"\eta=1-\frac{Q_C}{Q_H}=1-\frac{T_C}{T_H}")),
        ],
        final=E("η_Carnot = 1 − T_C/T_H", r"\eta=1-\frac{T_C}{T_H}"),
        diagram="d4_ts_diagram",
    ),
]

# =============================================================== 4.7 entropy changes
S6 = [
    theory(
        "4.7",
        bi("Entropy changes of common processes", "સામાન્ય પ્રક્રિયાઓના entropy ફેરફાર"),
        definition=bi(
            "Because entropy is a state function, the change for any process is found by "
            "integrating δQ<sub>rev</sub>/T along a convenient <b>reversible</b> path between the "
            "same two end states. Five cases cover the syllabus: phase change, ideal-gas "
            "processes, adiabatic mixing, isothermal mixing of ideal gases, and chemical "
            "reaction.",
            "Entropy state function હોવાથી કોઈપણ પ્રક્રિયાનો ફેરફાર સરખા બે અંતિમ states વચ્ચેના અનુકૂળ "
            "<b>reversible</b> રસ્તે δQ<sub>rev</sub>/T ને integrate કરીને મળે. પાંચ કિસ્સા syllabus "
            "આવરે છે: phase change, ideal-gas પ્રક્રિયાઓ, adiabatic mixing, ideal gases નું isothermal "
            "mixing, અને chemical reaction."),
        theory_text=bi(
            "Each case has a signature. A <b>phase change</b> at constant temperature gives "
            "ΔS = ΔH/T, because the heat is the latent heat and T does not move. A general "
            "<b>ideal-gas change</b> of state needs two terms, one for temperature and one for "
            "volume (or pressure), because entropy responds to both. <b>Reversible adiabatic</b> "
            "processes have ΔS = 0 exactly.<br><br>"
            "Mixing is where students lose marks, because the entropy of mixing is not obvious. "
            "Bring two different ideal gases together at the same T and P and ΔS = −R Σ nᵢ ln yᵢ, "
            "which is always positive: the gases expand into each other's volume and entropy "
            "rises even though nothing was heated and no work was done. For a <b>chemical "
            "reaction</b> at temperature T, ΔS = ΣS<sub>products</sub> − "
            "ΣS<sub>reactants</sub>, using tabulated absolute entropies; unlike enthalpy of "
            "formation, these are absolute values on the third-law basis.",
            "દરેક કિસ્સાની પોતાની ઓળખ છે. અચળ temperature પર <b>phase change</b> માટે ΔS = ΔH/T, કારણ કે heat "
            "એ latent heat છે અને T બદલાતું નથી. સામાન્ય <b>ideal-gas state change</b> માટે બે પદ જોઈએ, એક "
            "temperature માટે અને એક volume (કે pressure) માટે, કારણ કે entropy બંને પર પ્રતિક્રિયા આપે. "
            "<b>Reversible adiabatic</b> પ્રક્રિયાઓમાં ΔS બરાબર 0.<br><br>"
            "Mixing માં વિદ્યાર્થી માર્ક ગુમાવે છે, કારણ કે mixing ની entropy સ્પષ્ટ નથી. સરખા T તથા P પર "
            "બે જુદા ideal gases ભેગા કરતાં ΔS = −R Σ nᵢ ln yᵢ, જે હંમેશા ધન હોય: gases એકબીજાના volume માં "
            "expand થાય અને ઊર્જા ગરમ કે work થયા વગર પણ entropy વધે. temperature T પર <b>chemical "
            "reaction</b> માટે ΔS = ΣS<sub>products</sub> − ΣS<sub>reactants</sub>, tabulated absolute "
            "entropies વાપરીને; enthalpy of formation થી વિપરીત આ third-law આધાર પરની નિરપેક્ષ કિંમતો છે."),
        equations=[E("phase change:  ΔS = ΔH_phase / T", r"\Delta S=\frac{\Delta H_{phase}}{T}"),
                   E("ideal gas:  ΔS = m c_v ln(T₂/T₁) + m R ln(V₂/V₁)", r"\Delta S=mc_v\ln\frac{T_2}{T_1}+mR\ln\frac{V_2}{V_1}"),
                   E("reversible adiabatic:  ΔS = 0", r"\Delta S=0"),
                   E("mixing of ideal gases:  ΔS = −R Σ n_i ln y_i  > 0", r"\Delta S=-R\sum n_i\ln y_i"),
                   E("reaction:  ΔS° = ΣS°(products) − ΣS°(reactants)", r"\Delta S^0=\sum S^0_{prod}-\sum S^0_{reac}")],
        list_items=[
            "<b>Melting 1 kg of ice:</b> ΔH = 334 kJ/kg at 273 K, so ΔS = 334/273 = 1.22 kJ/kg·K.",
            "<b>Boiling 1 kg of water:</b> ΔH = 2 257 kJ/kg at 373 K, so ΔS = 6.05 kJ/kg·K — much larger, because vapour is far more dispersed.",
            "<b>Mixing:</b> always positive for ideal gases; the sign never depends on the gases chosen, only on the mole fractions.",
            "<b>Absolute entropies</b> are tabulated from 0 K, so a reaction entropy is a simple subtraction — no reference state ambiguity.",
        ],
        qualification=bi(
            "The formula ΔS = Q/T holds only for an <b>isothermal reversible</b> process. Using "
            "the actual (irreversible) heat divided by the temperature gives the entropy transfer "
            "to the surroundings, not the entropy change of the system; the difference is the "
            "entropy generated.",
            "ΔS = Q/T સૂત્ર ફક્ત <b>isothermal reversible</b> પ્રક્રિયા માટે લાગુ પડે. વાસ્તવિક "
            "(irreversible) heat ને temperature વડે ભાગવાથી surroundings ને થતું entropy transfer મળે, system "
            "નું entropy ફેરફાર નહીં; તફાવત એ ઉત્પન્ન થયેલી entropy છે."),
    ),
]

# =============================================================== 4.8 Clausius inequality
S7 = [
    theory(
        "4.8",
        bi("The Clausius inequality and the mathematical statement",
           "Clausius inequality તથા ગાણિતિક વિધાન"),
        definition=bi(
            "The <b>Clausius inequality</b> states that for any cycle "
            "<b>∮ δQ/T ≤ 0</b>, where T is the temperature of the boundary at which the heat "
            "δQ crosses. The equality holds for a reversible cycle and the strict inequality for "
            "an irreversible one. It is the mathematical form of the second law.",
            "<b>Clausius inequality</b> કહે છે કે કોઈપણ cycle માટે <b>∮ δQ/T ≤ 0</b>, જ્યાં T એ boundary નું "
            "temperature છે જ્યાં heat δQ પસાર થાય. સમાનતા reversible cycle માટે અને કડક અસમાનતા "
            "irreversible માટે. આ દ્વિતીય નિયમનું ગાણિતિક સ્વરૂપ છે."),
        theory_text=bi(
            "For a reversible cycle ∮δQ/T = 0, so the integral between two states is independent "
            "of the path — which is exactly the statement that S is a state function. Removing "
            "the cyclic restriction gives the entropy balance for a closed system: "
            "<b>dS = δQ/T + δS<sub>gen</sub></b>, where δS<sub>gen</sub> ≥ 0, with equality only "
            "for a reversible process.<br><br>"
            "That single line contains everything: for an isolated system Q = 0 so dS = "
            "δS<sub>gen</sub> ≥ 0 (entropy never decreases); for a reversible adiabatic process "
            "dS = 0 (isentropic); and for any real process the generated entropy is positive, "
            "producing the <b>lost work</b> I = T₀ S<sub>gen</sub> that no design can recover.",
            "Reversible cycle માટે ∮δQ/T = 0, તેથી બે states વચ્ચેનું integral path પર આધાર રાખતું નથી — "
            "જે બરાબર એ વિધાન છે કે S state function છે. ચક્રીય મર્યાદા દૂર કરતાં closed system માટે "
            "entropy balance મળે: <b>dS = δQ/T + δS<sub>gen</sub></b>, જ્યાં δS<sub>gen</sub> ≥ 0, અને "
            "સમાનતા ફક્ત reversible પ્રક્રિયા માટે.<br><br>"
            "એ એક લીટીમાં બધું છે: isolated system માટે Q = 0 તેથી dS = δS<sub>gen</sub> ≥ 0 (entropy કદી "
            "ઘટે નહીં); reversible adiabatic પ્રક્રિયા માટે dS = 0 (isentropic); અને કોઈપણ વાસ્તવિક "
            "પ્રક્રિયા માટે ઉત્પન્ન થયેલી entropy ધન હોય, જે <b>lost work</b> I = T₀ S<sub>gen</sub> પેદા કરે "
            "જે કોઈ design પાછું મેળવી શકે નહીં."),
        equations=[E("∮ δQ/T ≤ 0        (= 0 reversible, < 0 irreversible)", r"\oint\frac{\delta Q}{T}\le 0"),
                   E("closed system:  dS = δQ/T + δS_gen ,  δS_gen ≥ 0", r"dS=\frac{\delta Q}{T}+\delta S_{gen}"),
                   E("isolated system:  ΔS ≥ 0        lost work:  I = T₀ S_gen", r"\Delta S\ge 0")],
        list_items=[
            "<b>Equality test:</b> if a proposed cycle gives ∮δQ/T > 0 it is impossible, whatever the energy balance says.",
            "<b>Entropy generation</b> is the numerical measure of irreversibility; it is never negative.",
            "<b>Lost work</b> I = T₀S<sub>gen</sub> is the work a reversible plant would have produced but a real one cannot.",
            "<b>Isentropic efficiency</b> of a turbine or compressor is the ratio of actual to isentropic work, and is always below one.",
        ],
        diagram="d4_clausius",
        qualification=bi(
            "The inequality compares temperatures of the <i>boundary where the heat crosses</i>, "
            "not the system temperature. For heat supplied from a reservoir at T<sub>H</sub> the "
            "term is Q/T<sub>H</sub>; for a real exchanger with a finite approach the boundary "
            "temperature differs from the fluid's, and that difference is exactly where entropy "
            "is generated.",
            "અસમાનતા <i>heat જ્યાં પસાર થાય તે boundary</i> ના temperatures સરખાવે છે, system ના "
            "temperature નહીં. T<sub>H</sub> પરના reservoir થી મળતી heat માટે પદ Q/T<sub>H</sub> છે; "
            "મર્યાદિત approach વાળા વાસ્તવિક exchanger માં boundary temperature fluid કરતાં જુદું હોય છે, "
            "અને એ જ તફાવતમાં entropy ઉત્પન્ન થાય છે."),
    ),
]

# =============================================================== 4.9 third law
S8 = [
    theory(
        "4.9",
        bi("The third law of thermodynamics", "થર્મોડાયનેમિક્સનો તૃતીય નિયમ"),
        definition=bi(
            "<b>Third law:</b> the entropy of a perfect crystalline substance is zero at absolute "
            "zero, and no finite sequence of processes can cool a system to exactly 0 K in a "
            "finite number of steps. It fixes the zero of the entropy scale.",
            "<b>તૃતીય નિયમ:</b> absolute zero પર સંપೂರ್ಣ સ્ફટિકીય પદાર્થની entropy શૂન્ય હોય છે, અને કોઈ "
            "પણ મર્યાદિત પ્રક્રિયાઓની શ્રેણી કોઈ system ને મર્યાદિત પગલાંમાં બરાબર 0 K સુધી ઠંડું કરી શકતી "
            "નથી. તે entropy scale નું શૂન્ય નિશ્ચિત કરે છે."),
        theory_text=bi(
            "The first two laws only ever needed differences of entropy, so the origin of the "
            "scale was arbitrary. The third law supplies that origin, and it is what makes "
            "tabulated <b>absolute entropies</b> possible: S° of a compound at 298 K is the "
            "integral of c<sub>p</sub>/T from 0 K, with latent heats added at every phase change "
            "on the way. Every standard entropy in the tables is built this way.<br><br>"
            "The law also explains why absolute zero is unattainable. As T → 0 the heat capacity "
            "of every substance falls towards zero, so each successive cooling step removes less "
            "and less heat, and the temperature falls in a geometric tail that never reaches "
            "zero. Reaching 0 K would require an infinite number of steps, which is the "
            "unattainability statement.",
            "પહેલા બે નિયમોને ફક્ત entropy ના તફાવતની જરૂર પડતી, તેથી scale નું ઉદ્ગમ મનસ્વી હતું. તૃતીય નિયમ "
            "એ ઉદ્ગમ આપે છે, અને એટલે જ tabulated <b>absolute entropies</b> શક્ય બને છે: 298 K પર "
            "સંયોજનની S° એ 0 K થી c<sub>p</sub>/T નું integral છે, જેમાં રસ્તામાં દરેક phase change પર latent "
            "heats ઉમેરાય. Tables માંની દરેક standard entropy આ રીતે બનેલી છે.<br><br>"
            "નિયમ એ પણ સમજાવે છે કે absolute zero કેમ પામી શકાય નહીં. T → 0 થતાં દરેક પદાર્થની heat "
            "capacity શૂન્ય તરફ ઘટે, તેથી દરેક આગળના cooling પગલામાં ઓછી ને ઓછી heat નીકળે, અને temperature "
            "એ ભૌમિતિક શ્રેણીમાં ઘટે જે કદી શૂન્ય ન પહોંચે. 0 K પર પહોંચવા અનંત પગલાં જોઈએ, જે "
            "unattainability વિધાન છે."),
        equations=[E("perfect crystal at 0 K:  S = 0", r"S(0\ \mathrm{K})=0"),
                   E("absolute entropy:  S°(T) = ∫₀ᵀ (c_p/T) dT + Σ (ΔH_phase/T_phase)", r"S^0(T)=\int_0^T\frac{c_p}{T}dT")],
        list_items=[
            "<b>Why it matters:</b> it turns the entropy tables into absolute numbers and makes ΔS of reaction a plain subtraction.",
            "<b>Residual entropy:</b> a glass or a disordered solid retains entropy at 0 K because it is not a perfect crystal — CO and ice have measurable residual entropy.",
            "<b>Unattainability:</b> laboratories reach nanokelvin but never zero; the third law forbids exact 0 K.",
            "<b>Practical use:</b> cryogenic design relies on the third law to predict how much cooling each stage can deliver.",
        ],
        qualification=bi(
            "The third law is a statement about perfect crystals in internal equilibrium. "
            "Supercooled liquids and glasses are not in equilibrium, so their entropy at 0 K is "
            "not zero and the tables must not be used for them.",
            "તૃતીય નિયમ આંતરિક equilibrium માં રહેલા સંપૂર્ણ સ્ફટિકો વિશેનું વિધાન છે. Supercooled liquids તથા "
            "glasses equilibrium માં નથી, તેથી 0 K પર તેમની entropy શૂન્ય નથી અને તેમના માટે tables "
            "વાપરવી ન જોઈએ."),
    ),
]

# =============================================================== numericals
N1 = numerical(
    "N1",
    bi("Carnot efficiency and work output",
       "Carnot efficiency તથા work output"),
    given=bi("A reversible engine works between a source at 600 K and a sink at 300 K. It "
             "receives 2 000 kJ of heat per cycle from the source.",
             "reversible engine 600 K ના source તથા 300 K ના sink વચ્ચે ચાલે છે. તે દરેક cycle માં "
             "source માંથી 2 000 kJ heat લે છે."),
    find=bi("Carnot efficiency, work output per cycle and heat rejected.",
            "Carnot efficiency, દરેક cycle નું work તથા બહાર ફેંકાતી heat."),
    formula=[E("η = 1 − T_C/T_H", r"\eta=1-\frac{T_C}{T_H}"),
             E("W = η Q_H        Q_C = Q_H − W", r"W=\eta Q_H")],
    substitution=bi(
        "η = 1 − 300/600 = 0.50. W = 0.50 × 2 000 = 1 000 kJ. "
        "Q_C = 2 000 − 1 000 = 1 000 kJ.",
        "η = 1 − 300/600 = 0.50. W = 0.50 × 2 000 = 1 000 kJ. "
        "Q_C = 2 000 − 1 000 = 1 000 kJ."),
    answer=bi("η = 50 %;  W = 1 000 kJ per cycle;  Q_C = 1 000 kJ rejected to the sink.",
              "η = 50 %;  W = 1 000 kJ પ્રતિ cycle;  Q_C = 1 000 kJ sink ને ફેંકાય."),
    check=bi("A 300 K sink against a 600 K source gives exactly one half — the temperatures "
             "differ by a factor of two. The energy balance also checks: 2 000 in, 1 000 out as "
             "work, 1 000 out as heat.",
             "600 K source સામે 300 K sink બરાબર અડધું આપે — temperatures બે ગણા છે. Energy balance પણ "
             "મળે: 2 000 અંદર, 1 000 work તરીકે બહાર, 1 000 heat તરીકે બહાર."),
)

N2 = numerical(
    "N2",
    bi("Entropy change of water being heated",
       "પાણી ગરમ કરવાનો entropy ફેરફાર"),
    given=bi("5 kg of water is heated from 20 °C to 80 °C at constant pressure. "
             "c_p = 4.187 kJ/kg·K.",
             "5 kg પાણી અચળ pressure પર 20 °C થી 80 °C સુધી ગરમ કરાય છે. c_p = 4.187 kJ/kg·K."),
    find=bi("The entropy change of the water.",
            "પાણીનો entropy ફેરફાર."),
    formula=[E("ΔS = m c_p ln(T₂/T₁)", r"\Delta S=mc_p\ln\frac{T_2}{T_1}")],
    substitution=bi(
        "T₁ = 293 K, T₂ = 353 K. ΔS = 5 × 4.187 × ln(353/293) = 20.935 × ln 1.2048 "
        "= 20.935 × 0.1864 = 3.90 kJ/K.",
        "T₁ = 293 K, T₂ = 353 K. ΔS = 5 × 4.187 × ln(353/293) = 20.935 × ln 1.2048 "
        "= 20.935 × 0.1864 = 3.90 kJ/K."),
    answer=bi("ΔS = 3.90 kJ/K for the water.", "પાણી માટે ΔS = 3.90 kJ/K."),
    check=bi("Heating always raises entropy, and the logarithmic form is essential — using "
             "Q/T with a single average temperature would give a rough answer only. The result "
             "is about 1.7 % of the water's own heat capacity per kelvin, which is the right "
             "order for a 60 K rise.",
             "ગરમ કરવાથી entropy હંમેશા વધે, અને logarithmic સ્વરૂપ જરૂરી છે — એક સરેરાશ temperature સાથે "
             "Q/T વાપરતાં ફક્ત આશરે જવાબ મળે. પરિણામ પાણીની heat capacity ના લગભગ 1.7 % પ્રતિ kelvin છે, "
             "જે 60 K વધારા માટે સાચો ક્રમ છે."),
)

N3 = numerical(
    "N3",
    bi("Entropy change in a phase change",
       "phase change માં entropy ફેરફાર"),
    given=bi("2 kg of saturated water at 100 °C is completely evaporated at the same "
             "temperature. Latent heat of vaporisation = 2 257 kJ/kg.",
             "100 °C પરનું 2 kg saturated પાણી એ જ temperature પર પૂરેપૂરું બાષ્પીભવન થાય છે. "
             "વાષ્પીભવનની latent heat = 2 257 kJ/kg."),
    find=bi("Heat absorbed and the entropy change of the water.",
            "લેવાયેલી heat તથા પાણીનો entropy ફેરફાર."),
    formula=[E("Q = m L        ΔS = Q/T = m L / T", r"\Delta S=\frac{mL}{T}")],
    substitution=bi(
        "T = 373 K. Q = 2 × 2 257 = 4 514 kJ. ΔS = 4 514/373 = 12.10 kJ/K.",
        "T = 373 K. Q = 2 × 2 257 = 4 514 kJ. ΔS = 4 514/373 = 12.10 kJ/K."),
    answer=bi("Q = 4 514 kJ;  ΔS = 12.10 kJ/K (entropy increases on vaporisation).",
              "Q = 4 514 kJ;  ΔS = 12.10 kJ/K (વાષ્પીભવનમાં entropy વધે)."),
    check=bi("Vaporisation greatly increases the number of molecular arrangements, so a large "
             "positive ΔS is expected — here 6.05 kJ/kg·K, and condensing the same steam would "
             "give exactly the negative of this value.",
             "વાષ્પીભવનથી molecular ગોઠવણો ઘણી વધે, તેથી મોટો ધન ΔS અપેક્ષિત છે — અહીં 6.05 kJ/kg·K, અને "
             "એ જ steam condense કરતાં બરાબર આનું ઋણ મળે."),
)

N4 = numerical(
    "N4",
    bi("Entropy of mixing two ideal gases",
       "બે ideal gases ના mixing ની entropy"),
    given=bi("1 kmol of nitrogen and 3 kmol of oxygen are mixed at the same temperature and "
             "pressure. R = 8.314 kJ/kmol·K.",
             "1 kmol nitrogen તથા 3 kmol oxygen સરખા temperature તથા pressure પર મિશ્ર કરાય છે. "
             "R = 8.314 kJ/kmol·K."),
    find=bi("The entropy of mixing.",
            "mixing ની entropy."),
    formula=[E("ΔS_mix = −R Σ n_i ln y_i", r"\Delta S_{mix}=-R\sum n_i\ln y_i")],
    substitution=bi(
        "n_total = 4 kmol; y_N₂ = 0.25, y_O₂ = 0.75. "
        "ΔS = −8.314 [1 × ln 0.25 + 3 × ln 0.75] = −8.314 [(−1.3863) + 3(−0.2877)] "
        "= −8.314 [−1.3863 − 0.8631] = −8.314 × (−2.2494) = 18.70 kJ/K.",
        "n_total = 4 kmol; y_N₂ = 0.25, y_O₂ = 0.75. "
        "ΔS = −8.314 [1 × ln 0.25 + 3 × ln 0.75] = −8.314 [(−1.3863) + 3(−0.2877)] "
        "= −8.314 [−1.3863 − 0.8631] = −8.314 × (−2.2494) = 18.70 kJ/K."),
    answer=bi("ΔS_mix = +18.70 kJ/K — positive, as it must be for spontaneous mixing.",
              "ΔS_mix = +18.70 kJ/K — ધન, જે સ્વયંભૂ mixing માટે હોવું જ જોઈએ."),
    check=bi("Mixing is irreversible, so entropy must increase. The value is largest for an "
             "equimolar mixture and falls to zero when one component dominates — try 0.5/0.5 and "
             "you get 23.1 kJ/K, the maximum.",
             "Mixing irreversible છે, તેથી entropy વધવી જ જોઈએ. સમાન mole હોય ત્યારે કિંમત સૌથી વધુ હોય અને "
             "એક component પ્રભાવી થતાં શૂન્ય થાય — 0.5/0.5 લેતાં 23.1 kJ/K મળે, જે મહત્તમ છે."),
)

N5 = numerical(
    "N5",
    bi("Isentropic efficiency of a turbine",
       "turbine ની isentropic efficiency"),
    given=bi("Steam enters a turbine at 40 bar, 400 °C (h₁ = 3 214 kJ/kg, s₁ = 6.769 kJ/kg·K) "
             "and leaves at 0.1 bar. The isentropic exit enthalpy is 2 216 kJ/kg; the actual "
             "exit enthalpy is 2 350 kJ/kg.",
             "Steam turbine માં 40 bar, 400 °C પર આવે છે (h₁ = 3 214 kJ/kg, s₁ = 6.769 kJ/kg·K) અને "
             "0.1 bar પર નીકળે છે. Isentropic exit enthalpy 2 216 kJ/kg; વાસ્તવિક exit enthalpy "
             "2 350 kJ/kg."),
    find=bi("Isentropic work, actual work, isentropic efficiency and the entropy generated.",
            "isentropic work, વાસ્તવિક work, isentropic efficiency તથા ઉત્પન્ન થયેલી entropy."),
    formula=[E("w_s = h₁ − h₂", r"w_s=h_1-h_2"),
             E("η_is = (h₁ − h₂)/(h₁ − h₂s)", r"\eta_{is}=\frac{h_1-h_2}{h_1-h_{2s}}"),
             E("w_lost = T₀ (s₂ − s₁)", r"w_{lost}=T_0(s_2-s_1)")],
    substitution=bi(
        "w_s,ideal = 3 214 − 2 216 = 998 kJ/kg. w_s,actual = 3 214 − 2 350 = 864 kJ/kg. "
        "η_is = 864/998 = 0.866 = 86.6 %. The lost work at 300 K surroundings is "
        "T₀(s₂ − s₁) = 300 × (6.847 − 6.769) = 23.4 kJ/kg.",
        "w_s,ideal = 3 214 − 2 216 = 998 kJ/kg. w_s,actual = 3 214 − 2 350 = 864 kJ/kg. "
        "η_is = 864/998 = 0.866 = 86.6 %. 300 K surroundings પર lost work "
        "T₀(s₂ − s₁) = 300 × (6.847 − 6.769) = 23.4 kJ/kg."),
    answer=bi("η_is = 86.6 %;  the turbine loses 134 kJ/kg compared with an ideal one, of which "
              "23.4 kJ/kg is lost work at 300 K.",
              "η_is = 86.6 %;  turbine ideal કરતાં 134 kJ/kg ગુમાવે, જેમાંથી 300 K પર 23.4 kJ/kg "
              "lost work છે."),
    check=bi("Isentropic efficiency is always below 100 % and 86.6 % is typical for a large "
             "steam turbine. The entropy at exit is higher than at inlet, which is the "
             "signature of an irreversible adiabatic expansion.",
             "Isentropic efficiency હંમેશા 100 % થી નીચે હોય અને મોટા steam turbine માટે 86.6 % સામાન્ય છે. "
             "Exit પર entropy inlet કરતાં વધુ છે, જે irreversible adiabatic expansion ની ઓળખ છે."),
)

N6 = numerical(
    "N6",
    bi("Refrigerator COP and power input",
       "Refrigerator COP તથા power input"),
    given=bi("A refrigerator maintains a cold space at −15 °C while rejecting heat to "
             "surroundings at 30 °C. It must remove 12 kW of heat.",
             "Refrigerator ઠંડી જગ્યાને −15 °C પર રાખે છે અને 30 °C ના surroundings ને heat ફેંકે છે. "
             "તેને 12 kW heat કાઢવી પડે છે."),
    find=bi("Maximum possible COP, the minimum power required, and the COP if the actual "
            "machine needs 4.5 kW.",
            "મહત્તમ શક્ય COP, લઘુત્તમ જરૂરી power, અને વાસ્તવિક machine ને 4.5 kW જોઈએ તો COP."),
    formula=[E("COP_Carnot = T_C/(T_H − T_C)", r"COP=\frac{T_C}{T_H-T_C}"),
             E("COP_actual = Q_C / W", r"COP=\frac{Q_C}{W}")],
    substitution=bi(
        "T_C = 258 K, T_H = 303 K. COP_max = 258/(303 − 258) = 258/45 = 5.73. "
        "W_min = 12/5.73 = 2.09 kW. Actual: COP = 12/4.5 = 2.67, so the machine is at "
        "2.67/5.73 = 47 % of the reversible limit.",
        "T_C = 258 K, T_H = 303 K. COP_max = 258/(303 − 258) = 258/45 = 5.73. "
        "W_min = 12/5.73 = 2.09 kW. વાસ્તવિક: COP = 12/4.5 = 2.67, તેથી machine reversible મર્યાદાના "
        "2.67/5.73 = 47 % પર છે."),
    answer=bi("COP_max = 5.73;  W_min = 2.09 kW;  actual COP = 2.67 (47 % of the Carnot limit).",
              "COP_max = 5.73;  W_min = 2.09 kW;  વાસ્તવિક COP = 2.67 (Carnot મર્યાદાના 47 %)."),
    check=bi("A COP above 1 is normal for a refrigerator and violates nothing: the extra heat "
             "comes from the cold space. The Carnot COP is very sensitive to the temperature "
             "lift — 45 K here — which is why a fridge works harder on a hot day.",
             "Refrigerator માટે COP એકથી વધુ હોવો સામાન્ય છે અને કોઈ નિયમનો ભંગ નથી: વધારાની heat ઠંડી "
             "જગ્યા માંથી આવે. Carnot COP temperature lift પર ખૂબ સંવેદનશીલ છે — અહીં 45 K — એટલે જ ગરમ "
             "દિવસે fridge વધુ મહેનત કરે."),
)

# =============================================================== viva
VIVA = [
    viva(bi("Why is a second law needed when the first law is already satisfied?",
            "પ્રથમ નિયમ સંતોષાય તો પણ દ્વિતીય નિયમ કેમ જરૂરી છે?"),
         bi("The first law is only an energy balance; it fixes Q − W but not the direction. "
            "Processes such as heat flowing from cold to hot, or an engine running on one "
            "reservoir, satisfy the first law but never occur. The second law supplies "
            "direction, the equilibrium condition and the maximum work.",
            "પ્રથમ નિયમ ફક્ત energy balance છે; તે Q − W નિશ્ચિત કરે પણ દિશા નહીં. ઠંડા થી ગરમ તરફ heat "
            "જવી, કે એક જ reservoir પર engine ચાલવું — આવી પ્રક્રિયાઓ પ્રથમ નિયમ સંતોષે પણ કદી થતી નથી. "
            "દ્વિતીય નિયમ દિશા, equilibrium ની શરત તથા મહત્તમ work આપે છે.")),
    viva(bi("State the Kelvin–Planck and Clausius statements and show they are equivalent.",
            "Kelvin–Planck તથા Clausius વિધાનો જણાવો અને બંને સમાનાર્થી છે તે દર્શાવો."),
         bi("Kelvin–Planck: no cyclic device can convert all the heat from a single reservoir "
            "into work. Clausius: no device can move heat from cold to hot without work input. "
            "If one were violated the other could be: a device violating Kelvin–Planck would "
            "give free work, which could drive a refrigerator and violate Clausius, and vice "
            "versa.",
            "Kelvin–Planck: કોઈ ચક્રીય ઉપકરણ એક જ reservoir ની આખી heat work માં ફેરવી શકે નહીં. "
            "Clausius: work input વગર કોઈ ઉપકરણ heat ને ઠંડા થી ગરમ તરફ ખસેડી શકે નહીં. એકનો ભંગ થાય તો "
            "બીજાનો પણ થઈ શકે: Kelvin–Planck નો ભંગ કરતું ઉપકરણ મફત work આપે, જે refrigerator ચલાવીને "
            "Clausius નો ભંગ કરે, અને ઊલટું.")),
    viva(bi("Define entropy and state why it is a state function.",
            "entropy ની વ્યાખ્યા આપો અને તે state function કેમ છે તે જણાવો."),
         bi("dS = δQ_rev/T. It is a state function because for a reversible cycle ∮δQ/T = 0, so "
            "the integral between two states does not depend on the path — which is the defining "
            "property of a state function.",
            "dS = δQ_rev/T. તે state function છે કારણ કે reversible cycle માટે ∮δQ/T = 0, તેથી બે "
            "states વચ્ચેનું integral path પર આધાર રાખતું નથી — જે state function ની ઓળખ છે.")),
    viva(bi("State and prove the Carnot principle.",
            "Carnot નો સિદ્ધાંત જણાવો અને સાબિત કરો."),
         bi("No engine between two reservoirs can exceed the efficiency of a reversible engine, "
            "and all reversible engines have the same efficiency. Proof by contradiction: if a "
            "reversible engine were less efficient, running it backwards with a better engine "
            "would move heat from cold to hot with no work input, violating Clausius.",
            "બે reservoirs વચ્ચેનું કોઈ engine reversible engine ની efficiency કરતાં વધુ ન હોઈ શકે, અને "
            "બધા reversible engines ની efficiency સરખી. વિરોધાભાસ દ્વારા સાબિતી: reversible engine ઓછું "
            "efficient હોય તો તેને ઉલટું ચલાવીને વધુ સારા engine સાથે કોઈ work input વગર heat ને ઠંડા થી "
            "ગરમ તરફ ખસેડી શકાય, જે Clausius નો ભંગ છે.")),
    viva(bi("Write the Clausius inequality and explain each of its cases.",
            "Clausius inequality લખો અને તેના દરેક કિસ્સા સમજાવો."),
         bi("∮δQ/T ≤ 0, with T the boundary temperature. Equality for a reversible cycle, less "
            "than zero for an irreversible one. It gives dS = δQ/T + δS_gen with δS_gen ≥ 0, "
            "from which ΔS_universe ≥ 0 follows for an isolated system.",
            "∮δQ/T ≤ 0, જ્યાં T boundary temperature છે. reversible cycle માટે સમાનતા, irreversible માટે "
            "શૂન્યથી ઓછું. તે dS = δQ/T + δS_gen આપે જ્યાં δS_gen ≥ 0, જેમાંથી isolated system માટે "
            "ΔS_universe ≥ 0 મળે.")),
    viva(bi("Calculate the entropy change when two different ideal gases are mixed at the same "
            "T and P, and explain the sign.",
            "સરખા T તથા P પર બે જુદા ideal gases મિશ્ર કરતાં entropy ફેરફાર ગણો અને ચિહ્ન સમજાવો."),
         bi("ΔS = −R Σ nᵢ ln yᵢ, which is always positive. Each gas expands into the volume "
            "previously occupied by the other at constant temperature, and expansion always "
            "increases entropy. The maximum occurs for an equimolar mixture.",
            "ΔS = −R Σ nᵢ ln yᵢ, જે હંમેશા ધન. દરેક gas અચળ temperature પર બીજાના પહેલાંના volume માં "
            "expand થાય, અને expansion હંમેશા entropy વધારે. મહત્તમ સમાન mole મિશ્રણ માટે મળે.")),
    viva(bi("State the third law and explain what it is used for.",
            "તૃતીય નિયમ જણાવો અને તે શેના માટે વપરાય તે સમજાવો."),
         bi("The entropy of a perfect crystal is zero at 0 K, and absolute zero is unattainable "
            "in a finite number of steps. It fixes the zero of the entropy scale, making "
            "absolute entropies (and so ΔS of reaction) tabulable.",
            "0 K પર સંપૂર્ણ સ્ફટિકની entropy શૂન્ય, અને મર્યાદિત પગલાંમાં absolute zero પામી શકાય નહીં. તે "
            "entropy scale નું શૂન્ય નિશ્ચિત કરે, જેથી absolute entropies (અને તેથી reaction નું ΔS) "
            "table માં આપી શકાય.")),
    viva(bi("Why is the Carnot cycle not used in practice?",
            "Carnot cycle વ્યવહારમાં કેમ વપરાતું નથી?"),
         bi("It requires isothermal heat transfer at exactly the reservoir temperature, which "
            "means infinitely slow processes, and perfectly insulated adiabatic steps. Both are "
            "impossible in a real machine, so it serves as an efficiency limit, not a design.",
            "તેને બરાબર reservoir temperature પર isothermal heat transfer જોઈએ, એટલે અનંત ધીમી પ્રક્રિયાઓ, "
            "અને સંપૂર્ણ insulated adiabatic પગલાં. બંને વાસ્તવિક machine માં અશક્ય છે, તેથી તે efficiency "
            "મર્યાદા તરીકે કામ લાગે, design તરીકે નહીં.")),
]

# =============================================================== exam
EXAM = [
    exam(bi("State the limitations of the first law of thermodynamics and explain, with two "
            "examples, why the second law is required.",
            "પ્રથમ નિયમની મર્યાદાઓ જણાવો અને બે ઉદાહરણ સાથે દ્વિતીય નિયમ કેમ જરૂરી છે તે સમજાવો."), 4),
    exam(bi("Define heat engine, refrigerator and heat pump. Derive the expressions for "
            "efficiency and coefficient of performance.",
            "Heat engine, refrigerator તથા heat pump વ્યાખ્યાયિત કરો. Efficiency તથા coefficient of "
            "performance ના સૂત્રો મેળવો."), 4),
    exam(bi("State the Kelvin–Planck and Clausius statements of the second law and prove their "
            "equivalence.", "Kelvin–Planck તથા Clausius વિધાનો જણાવો અને તેમની સમાનાર્થતા સાબિત કરો."), 4),
    exam(bi("Define entropy. Show that it is a state function and derive ΔS for an ideal gas in "
            "terms of T and V.",
            "Entropy વ્યાખ્યાયિત કરો. તે state function છે તે દર્શાવો અને T તથા V ના પદમાં ideal gas "
            "માટે ΔS મેળવો."), 4),
    exam(bi("Describe the Carnot cycle with neat P–V and T–S diagrams and derive its efficiency. "
            "Why can no engine be more efficient?",
            "સ્વચ્છ P–V તથા T–S diagrams સાથે Carnot cycle વર્ણવો અને તેની efficiency મેળવો. કોઈ engine "
            "તેનાથી વધુ efficient કેમ ન હોઈ શકે?"), 4),
    exam(bi("Explain the thermodynamic temperature scale based on the Carnot cycle and show that "
            "it is independent of the working substance.",
            "Carnot cycle પર આધારિત thermodynamic temperature scale સમજાવો અને તે working substance પરથી "
            "સ્વતંત્ર છે તે દર્શાવો."), 4),
    exam(bi("Calculate the entropy change for (i) melting of ice, (ii) an ideal gas heated at "
            "constant pressure, (iii) isothermal mixing of two ideal gases.",
            "entropy ફેરફાર ગણો: (i) બરફ ઓગળવો, (ii) અચળ pressure પર ગરમ થતો ideal gas, "
            "(iii) બે ideal gases નું isothermal mixing."), 4),
    exam(bi("State the Clausius inequality. Derive the mathematical statement of the second law "
            "for a closed system and define entropy generation.",
            "Clausius inequality જણાવો. closed system માટે દ્વિતીય નિયમનું ગાણિતિક વિધાન મેળવો અને "
            "entropy generation વ્યાખ્યાયિત કરો."), 4),
    exam(bi("State the third law of thermodynamics. Explain how it makes absolute entropies "
            "possible and why absolute zero cannot be reached.",
            "તૃતીય નિયમ જણાવો. તે absolute entropies કેમ શક્ય બનાવે છે અને absolute zero કેમ પામી શકાય "
            "નહીં તે સમજાવો."), 4),
    exam(bi("A reversible engine works between 600 K and 300 K and receives 2 000 kJ per cycle. "
            "Find its efficiency, work output and heat rejected.",
            "reversible engine 600 K તથા 300 K વચ્ચે ચાલે છે અને પ્રતિ cycle 2 000 kJ લે છે. તેની "
            "efficiency, work તથા ફેંકાતી heat શોધો."), 4),
    exam(bi("5 kg of water is heated at constant pressure from 20 °C to 80 °C. Calculate the "
            "entropy change. c_p = 4.187 kJ/kg·K.",
            "5 kg પાણી અચળ pressure પર 20 °C થી 80 °C સુધી ગરમ કરાય છે. entropy ફેરફાર ગણો. "
            "c_p = 4.187 kJ/kg·K."), 4),
    exam(bi("1 kmol of nitrogen and 3 kmol of oxygen mix at the same temperature and pressure. "
            "Calculate the entropy of mixing. R = 8.314 kJ/kmol·K.",
            "1 kmol nitrogen તથા 3 kmol oxygen સરખા temperature તથા pressure પર મિશ્ર થાય. mixing ની "
            "entropy ગણો. R = 8.314 kJ/kmol·K."), 4),
]

# =============================================================== formulae
SYNTAX = [
    {"title": bi("Performance measures", "performance નાં માપ"),
     "items": [
         {"title": bi("Heat engine", "Heat engine"),
          "f": "η = W/Q_H = 1 − Q_C/Q_H;  Carnot: η = 1 − T_C/T_H",
          "terms": "Efficiency can never reach 1 because T_C = 0 K is unattainable."},
         {"title": bi("Refrigerator", "Refrigerator"),
          "f": "COP_R = Q_C/W;  Carnot: COP_R = T_C/(T_H − T_C)",
          "terms": "COP may exceed 1 — it is not an efficiency."},
         {"title": bi("Heat pump", "Heat pump"),
          "f": "COP_HP = Q_H/W = COP_R + 1",
          "terms": "Same cycle as a refrigerator; the useful output is the warm-side heat."},
     ]},
    {"title": bi("Entropy changes", "entropy ફેરફારો"),
     "items": [
         {"title": bi("Definition", "વ્યાખ્યા"),
          "f": "dS = δQ_rev/T;  S₂ − S₁ = ∫₁² δQ_rev/T",
          "terms": "Entropy is a state function; integrate along any reversible path."},
         {"title": bi("Ideal gas", "Ideal gas"),
          "f": "ΔS = m c_v ln(T₂/T₁) + m R ln(V₂/V₁);  or  m c_p ln(T₂/T₁) − m R ln(P₂/P₁)",
          "terms": "Reversible adiabatic gives ΔS = 0 exactly."},
         {"title": bi("Phase change", "Phase change"),
          "f": "ΔS = ΔH_phase/T",
          "terms": "Isothermal, so the simple Q/T form applies."},
         {"title": bi("Mixing", "Mixing"),
          "f": "ΔS_mix = −R Σ nᵢ ln yᵢ  > 0",
          "terms": "Zero for identical gases, maximum for equimolar mixtures."},
     ]},
    {"title": bi("Second-law statements", "દ્વિતીય નિયમનાં વિધાનો"),
     "items": [
         {"title": bi("Clausius inequality", "Clausius inequality"),
          "f": "∮ δQ/T ≤ 0  (=0 reversible, <0 irreversible)",
          "terms": "T is the boundary temperature where the heat crosses."},
         {"title": bi("Entropy balance", "Entropy balance"),
          "f": "dS = δQ/T + δS_gen;  δS_gen ≥ 0;  I = T₀ δS_gen",
          "terms": "Lost work I is the work a reversible plant would have produced."},
         {"title": bi("Third law", "તૃતીય નિયમ"),
          "f": "S = 0 for a perfect crystal at 0 K",
          "terms": "Fixes the zero of the entropy scale; abs0 is unattainable."},
     ]},
]

# =============================================================== build
def build() -> Unit:
    u = Unit(CODE, 4, TITLE, hours=13, weightage=26,
             tabs=["notes", "programs", "diagrams", "syntax", "viva", "exam"],
             tab_labels={"programs": bi("Solved numericals", "ઉકેલેલા દાખલા"),
                         "syntax": bi("Formulae and conversions", "સૂત્રો તથા conversions")})
    u.section(bi("4.1  Limitations of the first law", "4.1  પ્રથમ નિયમની મર્યાદાઓ"), S1)
    u.section(bi("4.2  Heat reservoir, engine, refrigerator and heat pump",
                 "4.2  Heat reservoir, engine, refrigerator તથા heat pump"), S2)
    u.section(bi("4.3  Statements of the second law", "4.3  દ્વિતીય નિયમનાં વિધાનો"), S3)
    u.section(bi("4.4  Concept of entropy", "4.4  entropy નો ખ્યાલ"), S4)
    u.section(bi("4.5  The Carnot principle and thermodynamic scale",
                 "4.5  Carnot સિદ્ધાંત તથા thermodynamic scale"), S5)
    u.section(bi("4.6  Entropy changes of common processes",
                 "4.6  સામાન્ય પ્રક્રિયાઓના entropy ફેરફાર"), S6)
    u.section(bi("4.7  Clausius inequality and the mathematical statement",
                 "4.7  Clausius inequality તથા ગાણિતિક વિધાન"), S7)
    u.section(bi("4.8  The third law of thermodynamics",
                 "4.8  થર્મોડાયનેમિક્સનો તૃતીય નિયમ"), S8)
    u.data["programs"] = [N1, N2, N3, N4, N5, N6]
    u.diagram("d4_heat_devices",
              bi("Heat engine, refrigerator and heat pump",
                 "Heat engine, refrigerator તથા heat pump"),
              "diagrams/d4_heat_devices.svg")
    u.diagram("d4_carnot_cycle",
              bi("The Carnot cycle on a P–V diagram", "P–V diagram પર Carnot cycle"),
              "diagrams/d4_carnot_cycle.svg")
    u.diagram("d4_ts_diagram",
              bi("The same Carnot cycle on a T–S diagram", "T–S diagram પર એ જ Carnot cycle"),
              "diagrams/d4_ts_diagram.svg")
    u.diagram("d4_clausius",
              bi("Entropy generation and the Clausius inequality",
                 "entropy generation તથા Clausius inequality"),
              "diagrams/d4_clausius.svg")
    for s in SYNTAX:
        u.data.setdefault("syntax", []).append(s)
    u.data["viva"] = VIVA
    u.data["exam_questions"] = EXAM
    return u


if __name__ == "__main__":
    unit = build()
    problems = unit.validate()
    out = unit.write("content/chemical/sem4/DI04005041/unit4.json")
    print("wrote", out)
    print("problems:", problems or "none")
