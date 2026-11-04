"""Content for DI04005041 (Chemical Engineering Thermodynamics) Unit 2
"First Law of Thermodynamics", GTU Diploma Chemical Engineering, semester 4,
syllabus w.e.f. 2025-26.

Coverage is the official syllabus 2.1 - 2.4:
  2.1 first law of thermodynamics
  2.2 internal energy, enthalpy and heat capacity
  2.3 first law for non-flow processes and for flow processes
  2.4 numericals on the first law and on internal energy, enthalpy, heat capacity

Every teaching card follows the DiplomaOne template (tools/d1notes.py).
Reference matter: Narayanan; Smith, Van Ness & Abbott; Gavhane; Rajput.
Equations carry LaTeX in data-tex so the preview stacks every fraction.
"""
from d1notes import Unit, bi, derivation, exam, numerical, theory, viva


def E(display, tex=None, note=None):
    return (display, tex or display, note) if note else (display, tex or display)


CODE = "DI04005041"
TITLE = bi("First Law of Thermodynamics", "થર્મોડાયનેમિક્સનો પ્રથમ નિયમ")

# =============================================================== 2.1 first law
S1 = [
    theory(
        "2.1",
        bi("Statement of the first law", "પ્રથમ નિયમનું વિધાન"),
        definition=bi(
            "The <b>first law of thermodynamics</b> states that energy can neither be "
            "created nor destroyed, only converted from one form to another. For a closed "
            "system that changes from state 1 to state 2, the heat supplied minus the work "
            "done equals the change of total energy: <b>Q − W = ΔE</b>.",
            "<b>થર્મોડાયનેમિક્સનો પ્રથમ નિયમ</b> કહે છે કે ઊર્જા ઉત્પન્ન કે નષ્ટ થઈ શકતી નથી, ફક્ત એક "
            "સ્વરૂપમાંથી બીજા સ્વરૂપમાં ફેરવાય છે. state 1 થી state 2 માં જતી closed system માટે, "
            "અપાયેલી heat માંથી થયેલું work બાદ કરતાં કુલ ઊર્જાનો ફેરફાર મળે: <b>Q − W = ΔE</b>."),
        theory_text=bi(
            "The law is a statement about the <i>accounting</i>, not about the mechanism. It "
            "says the books must balance: whatever crosses the boundary as heat either leaves "
            "as work or stays inside as a rise of internal, kinetic and potential energy. It "
            "therefore forbids a machine that produces work with no energy input (a "
            "perpetual-motion machine of the first kind), and it makes internal energy a "
            "property with a definite value at every state.<br><br>"
            "For a closed, stationary system the kinetic and potential terms are zero and the "
            "law reduces to the form used in almost every numerical: <b>Q − W = ΔU</b>. When "
            "an ideal gas is the system, ΔU = m c<sub>v</sub> ΔT, so the temperature change "
            "follows from the heat and work alone, whatever the path.",
            "આ નિયમ <i>હિસાબ</i> વિશે છે, mechanism વિશે નથી. તે કહે છે કે હિસાબ બરાબર બેસવો જોઈએ: "
            "boundary પાર heat તરીકે જે જાય તે કાં તો work તરીકે નીકળે, કાં તો અંદર internal, kinetic "
            "તથા potential energy ના વધારા તરીકે રહે. તેથી જે machine કોઈ ઊર્જા લીધા વગર work આપે "
            "(પહેલા પ્રકારની perpetual-motion machine) તેને તે નિષેધે છે, અને internal energy ને દરેક "
            "state પર ચોક્કસ કિંમત ધરાવતી property બનાવે છે.<br><br>"
            "closed, સ્થિર system માટે kinetic તથા potential પદ શૂન્ય થાય અને નિયમ લગભગ દરેક દાખલામાં "
            "વપરાતા સ્વરૂપમાં આવે: <b>Q − W = ΔU</b>. system ideal gas હોય તો ΔU = m c<sub>v</sub> ΔT, "
            "તેથી temperature નો ફેરફાર ફક્ત heat તથા work પરથી મળે, path કોઈ પણ હોય."),
        equations=[E("Q − W = ΔU + Δ(KE) + Δ(PE)", r"Q-W=\Delta U+\Delta KE+\Delta PE"),
                   E("closed, stationary:  Q − W = ΔU", r"Q-W=\Delta U"),
                   E("differential form:  δQ − δW = dU", r"\delta Q-\delta W=dU")],
        list_items=[
            "<b>Sign convention used here:</b> heat added to the system is positive, work done by the system is positive. State the convention before substituting numbers.",
            "<b>Cyclic process:</b> ΔU = 0, so Q<sub>net</sub> = W<sub>net</sub> for the cycle.",
            "<b>Adiabatic:</b> Q = 0, so W = −ΔU: the work comes out of the internal energy.",
            "<b>Perpetual motion of the first kind</b> is a machine giving work without energy input; the first law makes it impossible.",
        ],
        diagram="d2_energy_forms",
        qualification=bi(
            "The first law fixes only the <i>difference</i> Q − W, never Q and W separately, and "
            "it says nothing about direction. A process in which heat flows from cold to hot "
            "would satisfy it, so the second law is still needed before any real cycle can be "
            "analysed.",
            "પ્રથમ નિયમ ફક્ત <i>તફાવત</i> Q − W નિશ્ચિત કરે છે, Q તથા W અલગ અલગ કદી નહીં, અને દિશા "
            "વિશે કંઈ કહેતો નથી. ઠંડા તરફથી ગરમ તરફ heat જાય તેવી પ્રક્રિયા પણ તેને સંતોષે, તેથી કોઈ પણ "
            "વાસ્તવિક cycle વિશ્લેષણ કરતાં પહેલાં બીજો નિયમ પણ જરૂરી છે."),
    ),
]

# =============================================================== 2.2 internal energy
S2 = [
    theory(
        "2.2",
        bi("Internal energy, enthalpy and heat capacity",
           "Internal energy, enthalpy તથા heat capacity"),
        definition=bi(
            "<b>Internal energy U</b> is the total energy of the molecules of the system — "
            "their translational, rotational and vibrational motion plus the energy stored in "
            "molecular bonds. <b>Enthalpy H</b> is the combination <b>H = U + P V</b>. "
            "<b>Heat capacity</b> is the heat needed to raise the temperature of the system by "
            "one degree: C = δQ/dT, and per unit mass c = C/m.",
            "<b>Internal energy U</b> એ system ના molecules ની કુલ ઊર્જા છે — તેમની translational, "
            "rotational તથા vibrational ગતિ ઉપરાંત molecular bonds માં સંગ્રહાયેલી ઊર્જા. "
            "<b>Enthalpy H</b> એ સંયોજન છે <b>H = U + P V</b>. <b>Heat capacity</b> એ system નું "
            "temperature એક ડિગ્રી વધારવા જરૂરી heat છે: C = δQ/dT, અને પ્રતિ એકમ દળ c = C/m."),
        theory_text=bi(
            "Enthalpy looks like an arbitrary grouping, but it is the natural property for a "
            "flow process. When a fluid is pushed into a control volume, the surroundings do "
            "flow work P V on it; adding that to U gives H, and the steady-flow energy equation "
            "then contains h instead of u, with no separate flow-work term. That is why steam "
            "tables tabulate h and not u for most engineering work.<br><br>"
            "Two heat capacities exist because there are two ways to heat a gas. At constant "
            "volume the gas cannot expand, so all the heat raises U: c<sub>v</sub> = "
            "(∂u/∂T)<sub>v</sub>. At constant pressure the gas also does work P Δv while it "
            "expands, so more heat is needed for the same temperature rise: "
            "c<sub>p</sub> = (∂h/∂T)<sub>p</sub>. For an ideal gas the difference is exactly the "
            "gas constant, c<sub>p</sub> − c<sub>v</sub> = R, and the ratio γ = c<sub>p</sub>/"
            "c<sub>v</sub> controls every adiabatic process.",
            "Enthalpy કોઈ મનસ્વી જૂથ જેવું લાગે, પણ flow process માટે તે સ્વાભાવિક property છે. જ્યારે "
            "fluid ને control volume માં ધકેલાય છે ત્યારે surroundings તેના પર flow work P V કરે છે; "
            "તેને U માં ઉમેરતાં H મળે, અને પછી steady-flow energy equation માં u ને બદલે h આવે, "
            "અલગ flow-work પદ વગર. એટલે જ steam tables મોટાભાગના engineering કામ માટે u નહીં પણ h "
            "આપે છે.<br><br>"
            "બે heat capacities છે કારણ કે gas ને ગરમ કરવાની બે રીતો છે. અચળ volume પર gas expand થઈ "
            "શકતું નથી, તેથી આખી heat U વધારે: c<sub>v</sub> = (∂u/∂T)<sub>v</sub>. અચળ pressure પર gas "
            "expand થતાં work P Δv પણ કરે છે, તેથી એટલા જ temperature વધારા માટે વધુ heat જોઈએ: "
            "c<sub>p</sub> = (∂h/∂T)<sub>p</sub>. ideal gas માટે તફાવત બરાબર gas constant જેટલો હોય છે, "
            "c<sub>p</sub> − c<sub>v</sub> = R, અને ગુણોત્તર γ = c<sub>p</sub>/c<sub>v</sub> દરેક "
            "adiabatic પ્રક્રિયાને નિયંત્રિત કરે છે."),
        equations=[E("H = U + P V", r"H=U+PV"),
                   E("h = u + P v", r"h=u+Pv"),
                   E("c_v = (∂u/∂T)_v        c_p = (∂h/∂T)_p", r"c_v=\left(\frac{\partial u}{\partial T}\right)_v,\quad c_p=\left(\frac{\partial h}{\partial T}\right)_p"),
                   E("ideal gas:  c_p − c_v = R        γ = c_p / c_v", r"c_p-c_v=R,\quad \gamma=\frac{c_p}{c_v}")],
        list_items=[
            "<b>U is a state function</b>; absolute U is never needed, only ΔU between two states.",
            "<b>Ideal gas:</b> U and H depend on temperature only (Joule's law), so ΔU = m c<sub>v</sub> ΔT and ΔH = m c<sub>p</sub> ΔT for every path.",
            "<b>Typical values:</b> air c<sub>p</sub> = 1.005 kJ/kg·K, c<sub>v</sub> = 0.718, γ = 1.40; water c<sub>p</sub> = 4.187 kJ/kg·K; steam c<sub>p</sub> ≈ 2.1 kJ/kg·K.",
            "<b>Solids and liquids:</b> c<sub>p</sub> ≈ c<sub>v</sub> ≈ c because they hardly expand, and both U and H are nearly functions of T alone.",
        ],
        diagram="d2_heat_capacity",
        qualification=bi(
            "Heat capacity is not constant. For real gases it rises with temperature, and for "
            "water it peaks near 4 °C. Using a single tabulated c over a wide temperature range "
            "is an approximation that must be stated, and near a phase change heat capacity has "
            "no meaning at all — the latent heat is used instead.",
            "Heat capacity અચળ હોતું નથી. વાસ્તવિક gases માટે તે temperature સાથે વધે છે, અને પાણી માટે "
            "4 °C ની આસપાસ શિખરે છે. મોટા temperature ગાળામાં એક જ tabulated c વાપરવું એ approximation છે "
            "જે લખવી જોઈએ, અને phase change ની નજીક heat capacity નો અર્થ જ નથી — ત્યાં latent heat "
            "વપરાય છે."),
    ),
]

# =============================================================== 2.3 non-flow
S3 = [
    theory(
        "2.3",
        bi("First law for non-flow processes", "non-flow પ્રક્રિયાઓ માટે પ્રથમ નિયમ"),
        definition=bi(
            "A <b>non-flow process</b> is one in which the same fixed mass stays inside the "
            "system — filling, heating, expanding a gas in a cylinder. No mass crosses the "
            "boundary, so the energy equation is simply <b>Q − W = ΔU</b>, with "
            "W = ∫P dV for a reversible path.",
            "<b>Non-flow process</b> એ એવી પ્રક્રિયા છે જેમાં એ જ નિશ્ચિત mass system ની અંદર રહે છે — "
            "cylinder માં gas ભરવો, ગરમ કરવો, expand કરવો. boundary પાર કોઈ mass જતું નથી, તેથી energy "
            "equation સીધું <b>Q − W = ΔU</b> છે, અને reversible path માટે W = ∫P dV."),
        theory_text=bi(
            "Four reversible non-flow paths cover almost every question, and each has a "
            "characteristic P–V signature. In a <b>constant-volume</b> (isochoric) process no "
            "work is done at all, so Q = ΔU = m c<sub>v</sub> ΔT. In a <b>constant-pressure</b> "
            "(isobaric) process the work is P ΔV and the heat supplied equals the enthalpy "
            "change, Q = ΔH = m c<sub>p</sub> ΔT — which is precisely why enthalpy is used for "
            "heaters and reactors. In a <b>constant-temperature</b> (isothermal) process of an "
            "ideal gas ΔU = 0, so all the heat becomes work. In an <b>adiabatic</b> process "
            "Q = 0, so the work comes out of internal energy and the gas cools as it expands.",
            "ચાર reversible non-flow રસ્તા લગભગ દરેક પ્રશ્ન આવરી લે છે, અને દરેકની પોતાની P–V ઓળખ છે. "
            "<b>અચળ volume</b> (isochoric) પ્રક્રિયામાં કોઈ work થતું નથી, તેથી "
            "Q = ΔU = m c<sub>v</sub> ΔT. <b>અચળ pressure</b> (isobaric) પ્રક્રિયામાં work P ΔV થાય અને "
            "અપાયેલી heat enthalpy ના ફેરફાર જેટલી હોય, Q = ΔH = m c<sub>p</sub> ΔT — એટલે જ heaters તથા "
            "reactors માટે enthalpy વપરાય છે. ideal gas ની <b>અચળ temperature</b> (isothermal) પ્રક્રિયામાં "
            "ΔU = 0, તેથી આખી heat work બને છે. <b>Adiabatic</b> પ્રક્રિયામાં Q = 0, તેથી work internal "
            "energy માંથી આવે અને expand થતાં gas ઠંડું થાય છે."),
        equations=[E("constant V:  W = 0 ,  Q = ΔU = m c_v ΔT", r"W=0,\quad Q=\Delta U=mc_v\Delta T"),
                   E("constant P:  W = P ΔV ,  Q = ΔH = m c_p ΔT", r"W=P\Delta V,\quad Q=\Delta H=mc_p\Delta T"),
                   E("isothermal, ideal gas:  ΔU = 0 ,  W = Q = m R T ln(V₂/V₁)", r"\Delta U=0,\quad W=Q=mRT\ln\frac{V_2}{V_1}"),
                   E("adiabatic, ideal gas:  Q = 0 ,  W = −ΔU = m c_v (T₁ − T₂)", r"Q=0,\quad W=-\Delta U=mc_v(T_1-T_2)")],
        list_items=[
            "<b>Isochoric:</b> vertical line on a P–V diagram. Used for a closed vessel being heated.",
            "<b>Isobaric:</b> horizontal line. Used for a heater or a piston free to move.",
            "<b>Isothermal:</b> rectangular hyperbola P V = constant. Used for slow heat exchange with a large bath.",
            "<b>Adiabatic:</b> steeper than the isotherm, P V<sup>γ</sup> = constant. Used for a well-insulated compressor or expansion.",
        ],
        diagram="d2_nonflow_paths",
        qualification=bi(
            "The formulas W = P ΔV and W = ∫P dV apply to the <i>reversible</i> path. In a real "
            "fast expansion the pressure inside the gas is not uniform and the actual work is "
            "less; the work must then be taken from the surroundings side or given directly.",
            "W = P ΔV તથા W = ∫P dV સૂત્રો <i>reversible</i> રસ્તા માટે લાગુ પડે. વાસ્તવિક ઝડપી "
            "expansion માં gas ની અંદર pressure સરખું હોતું નથી અને ખરેખર work ઓછું મળે; ત્યારે work "
            "surroundings ની બાજુથી કે સીધું આપેલું લેવું પડે."),
    ),
    derivation(
        "2.4",
        bi("Steady-flow energy equation",
           "Steady-flow energy equation નું derivation"),
        symbols=bi(
            "<b>Model:</b> a control volume with one inlet (1) and one outlet (2), working "
            "fluid steady, properties uniform across each section. <b>Assumptions:</b> steady "
            "state (nothing accumulates), no chemical reaction, negligible change of surface "
            "energy, single stream in and out.",
            "<b>Model:</b> એક inlet (1) તથા એક outlet (2) વાળું control volume, working fluid steady, "
            "દરેક section પર properties સરખી. <b>Assumptions:</b> steady state (કંઈ સંગ્રહાય નહીં), કોઈ "
            "chemical reaction નહીં, surface energy નો ફેરફાર નગણ્ય, એક જ stream અંદર તથા બહાર."),
        steps=[
            (bi("Take a control volume between sections 1 and 2. In steady state the mass "
                "entering equals the mass leaving, so the same mass m flows in and out.",
                "section 1 તથા 2 વચ્ચે control volume લો. Steady state માં અંદર આવતું mass બહાર જતા "
                "mass જેટલું હોય, તેથી અંદર તથા બહાર એ જ mass m વહે છે."),
             E("m_in = m_out = m", r"\dot m_{in}=\dot m_{out}=\dot m")),
            (bi("Write what enters with the fluid: internal energy, the flow work needed to "
                "push it in, kinetic energy and potential energy.",
                "fluid સાથે અંદર જે આવે તે લખો: internal energy, તેને અંદર ધકેલવા જરૂરી flow work, "
                "kinetic energy તથા potential energy."),
             E("in = m (u₁ + P₁v₁) + ½ m c₁² + m g z₁", r"=m(u_1+P_1v_1)+\tfrac12mc_1^2+mgz_1")),
            (bi("Group u + P v, which is the definition of enthalpy. This is the step that "
                "removes flow work from the equation.",
                "u + P v ને જૂથ કરો, જે enthalpy ની વ્યાખ્યા છે. આ પગલું જ flow work ને સમીકરણમાંથી દૂર કરે છે."),
             E("u + P v = h   ⇒   in = m (h₁ + ½c₁² + g z₁)", r"u+Pv=h")),
            (bi("Write what leaves in the same way, at section 2.",
                "એ જ રીતે section 2 પર જે બહાર જાય તે લખો."),
             E("out = m (h₂ + ½c₂² + g z₂)", r"=m(h_2+\tfrac12c_2^2+gz_2)")),
            (bi("Apply the first law to the control volume: heat in minus work out equals the "
                "energy that left minus the energy that entered. In steady state there is no "
                "change of stored energy inside, so the accumulation is zero.",
                "control volume પર પ્રથમ નિયમ લાગુ કરો: અંદર આવેલી heat માંથી બહાર ગયેલું work બાદ "
                "કરતાં બહાર ગયેલી ઊર્જા ઓછી અંદર આવેલી ઊર્જા બરાબર થાય. Steady state માં અંદર સંગ્રહાયેલી "
                "ઊર્જા બદલાતી નથી, તેથી accumulation શૂન્ય છે."),
             E("Q − W_s = out − in", r"Q-W_s=out-in")),
            (bi("Substitute the two groups and divide by the mass flow, giving the equation in "
                "the form used for compressors, turbines and nozzles.",
                "બંને જૂથ મૂકો અને mass flow વડે ભાગો, જેથી compressor, turbine તથા nozzle માટે "
                "વપરાતું સ્વરૂપ મળે."),
             E("Q − W_s = m [ (h₂ − h₁) + ½(c₂² − c₁²) + g(z₂ − z₁) ]",
               r"Q-W_s=m\left[(h_2-h_1)+\tfrac12(c_2^2-c_1^2)+g(z_2-z_1)\right]")),
        ],
        final=E("q − w_s = (h₂ − h₁) + ½(c₂² − c₁²) + g(z₂ − z₁)   (per unit mass)",
                r"q-w_s=(h_2-h_1)+\tfrac12(c_2^2-c_1^2)+g(z_2-z_1)"),
        diagram="d2_steady_flow",
    ),
]

# =============================================================== 2.4 work forms
S4 = [
    theory(
        "2.5",
        bi("Forms of work: displacement, flow and shaft",
           "Work નાં સ્વરૂપો: displacement, flow તથા shaft"),
        definition=bi(
            "Work is energy in transit across a boundary under the action of a force. Three "
            "forms dominate chemical engineering: <b>displacement work</b> W = ∫P dV, done "
            "when a boundary moves against pressure; <b>flow work</b> P V, done by the "
            "surroundings to push fluid into or out of a control volume; and <b>shaft work</b> "
            "W = 2π N T, delivered through a rotating shaft.",
            "Work એ boundary પાર બળની અસર હેઠળ પસાર થતી ઊર્જા છે. Chemical engineering માં ત્રણ "
            "સ્વરૂપ પ્રભાવી છે: <b>displacement work</b> W = ∫P dV, જ્યારે boundary pressure સામે "
            "ખસે ત્યારે થાય; <b>flow work</b> P V, જે surroundings fluid ને control volume માં કે બહાર "
            "ધકેલવા કરે; અને <b>shaft work</b> W = 2π N T, ફરતા shaft દ્વારા મળે."),
        theory_text=bi(
            "The distinction matters because only displacement and shaft work appear as W in the "
            "first law; flow work is never written separately — it is absorbed into enthalpy "
            "precisely so that the equation stays short. A student who adds a flow-work term to "
            "the steady-flow equation is counting the same energy twice.<br><br>"
            "Sign follows the boundary, not the machine. Work done <i>by</i> the system on the "
            "surroundings is positive here, so an expanding gas does positive work and a "
            "compressor that consumes work reports a negative W. In an electrical heater the "
            "work is negative and the heat supplied is positive, both crossing the same "
            "boundary — which is why the account still balances.",
            "આ ભેદ મહત્વનો છે કારણ કે પ્રથમ નિયમમાં W તરીકે ફક્ત displacement તથા shaft work આવે; "
            "flow work કદી અલગ લખાતું નથી — તેને enthalpy માં સમાવી લેવાય છે જેથી સમીકરણ ટૂંકું રહે. "
            "steady-flow equation માં flow-work પદ ઉમેરનાર વિદ્યાર્થી એ જ ઊર્જા બે વાર ગણે છે.<br><br>"
            "ચિહ્ન boundary પરથી આવે, machine પરથી નહીં. અહીં system <i>દ્વારા</i> surroundings પર થયેલું "
            "work ધન છે, તેથી expand થતો gas ધન work કરે અને work વાપરતો compressor ઋણ W આપે. "
            "Electrical heater માં work ઋણ અને અપાયેલી heat ધન હોય, બંને એ જ boundary પાર જાય — એટલે "
            "હિસાબ બેસી જાય છે."),
        equations=[E("displacement:  W = ∫ P dV", r"W=\int P\,dV"),
                   E("flow work:  W_flow = P V  (absorbed into h)", r"W_{flow}=PV"),
                   E("shaft work:  W_s = 2π N T", r"W_s=2\pi NT")],
        list_items=[
            "<b>Displacement work</b> is the area under the process curve on a P–V diagram.",
            "<b>Flow work</b> P V is not a separate term once enthalpy is used: h = u + P v already contains it.",
            "<b>Shaft work</b> is what a pump, compressor, turbine or stirrer delivers; it is positive when the shaft delivers work to the surroundings.",
            "<b>Electrical and magnetic work</b> also cross the boundary without a moving part and must be counted in W.",
        ],
        qualification=bi(
            "The integral ∫P dV gives the work only when the path is reversible, because only "
            "then is the pressure inside the gas the same as the pressure at the boundary. For "
            "free expansion into vacuum the external pressure is zero, so no work is done even "
            "though the gas expands.",
            "∫P dV એ ફક્ત ત્યારે જ work આપે જ્યારે path reversible હોય, કારણ કે ત્યારે જ gas ની અંદરનું "
            "pressure boundary પરના pressure જેટલું હોય. શૂન્યાવકાશમાં free expansion માં બહારનું "
            "pressure શૂન્ય હોય, તેથી gas expand થાય છતાં કોઈ work થતું નથી."),
    ),
    derivation(
        "2.6",
        bi("Relation between c_p and c_v for an ideal gas",
           "ideal gas માટે c_p તથા c_v વચ્ચેનો સંબંધ"),
        symbols=bi(
            "<b>Model:</b> one mole of an ideal gas, P V = R T, heated through the same "
            "temperature rise twice — once at constant volume, once at constant pressure. "
            "<b>Assumptions:</b> ideal gas, no change of kinetic or potential energy, "
            "reversible heating.",
            "<b>Model:</b> એક mole ideal gas, P V = R T, એ જ temperature વધારા માટે બે વાર ગરમ — "
            "એક વાર અચળ volume પર, એક વાર અચળ pressure પર. <b>Assumptions:</b> ideal gas, kinetic કે "
            "potential energy નો ફેરફાર નહીં, reversible heating."),
        steps=[
            (bi("Heat one mole at constant volume by dT. No work is done, so all the heat raises "
                "internal energy and defines c_v.",
                "એક mole ને અચળ volume પર dT ગરમ કરો. કોઈ work થતું નથી, તેથી આખી heat internal "
                "energy વધારે અને c_v વ્યાખ્યાયિત કરે."),
             E("δQ_v = dU = c_v dT", r"\delta Q_v=dU=c_v\,dT")),
            (bi("Heat one mole at constant pressure by the same dT. Now the gas also does work "
                "P dV, so the heat supplied must cover both the internal energy and that work.",
                "એક mole ને અચળ pressure પર એ જ dT ગરમ કરો. હવે gas work P dV પણ કરે છે, તેથી અપાયેલી "
                "heat બંને — internal energy તથા એ work — આવરે."),
             E("δQ_p = dU + P dV = c_p dT", r"\delta Q_p=dU+P\,dV=c_p\,dT")),
            (bi("Subtract the constant-volume result from the constant-pressure result.",
                "અચળ pressure ના પરિણામમાંથી અચળ volume નું પરિણામ બાદ કરો."),
             E("c_p dT − c_v dT = P dV", r"(c_p-c_v)\,dT=P\,dV")),
            (bi("Differentiate the ideal-gas law P V = R T at constant pressure, so that P dV "
                "can be replaced.",
                "અચળ pressure પર ideal-gas law P V = R T નું differential લો, જેથી P dV ને બદલી શકાય."),
             E("P dV = R dT   (constant P)", r"P\,dV=R\,dT")),
            (bi("Substitute and cancel dT from both sides to obtain Mayer's relation.",
                "મૂકો અને બંને બાજુથી dT કાપો, જેથી Mayer નો સંબંધ મળે."),
             E("(c_p − c_v) dT = R dT  ⇒  c_p − c_v = R", r"c_p-c_v=R")),
            (bi("Divide by c_v to get the ratio that controls adiabatic pressure–volume behaviour.",
                "અચળ pressure અને volume વચ્ચેના adiabatic વર્તનને નિયંત્રિત કરતો ગુણોત્તર મેળવવા c_v વડે ભાગો."),
             E("γ = c_p / c_v  ⇒  c_p = γR/(γ−1),  c_v = R/(γ−1)", r"\gamma=\frac{c_p}{c_v}")),
        ],
        final=E("c_p − c_v = R        c_v = R/(γ − 1)        c_p = γR/(γ − 1)",
                r"c_p-c_v=R"),
    ),
]


# =============================================================== numericals
N1 = numerical(
    "N1",
    bi("Work and heat in a closed cylinder of gas",
       "Closed cylinder માં gas નું work તથા heat"),
    given=bi("0.5 kg of air is heated in a rigid closed vessel from 27 °C to 227 °C. Take "
             "c_v = 0.718 kJ/kg·K.",
             "0.5 kg હવા દૃઢ closed પાત્રમાં 27 °C થી 227 °C સુધી ગરમ કરાય છે. "
             "c_v = 0.718 kJ/kg·K લો."),
    find=bi("Work done, heat supplied and change of internal energy.",
            "થયેલું work, અપાયેલી heat તથા internal energy નો ફેરફાર."),
    formula=[E("rigid vessel:  W = 0", r"W=0"),
             E("Q = ΔU = m c_v ΔT", r"Q=\Delta U=mc_v\Delta T")],
    substitution=bi(
        "ΔT = 227 − 27 = 200 K. ΔU = 0.5 × 0.718 × 200 = 71.8 kJ. Since W = 0, Q = 71.8 kJ.",
        "ΔT = 227 − 27 = 200 K. ΔU = 0.5 × 0.718 × 200 = 71.8 kJ. W = 0 હોવાથી Q = 71.8 kJ."),
    answer=bi("W = 0;  ΔU = 71.8 kJ;  Q = 71.8 kJ (heat supplied to the air).",
              "W = 0;  ΔU = 71.8 kJ;  Q = 71.8 kJ (હવાને અપાયેલી heat)."),
    check=bi("A rigid vessel cannot change volume, so no displacement work is possible; every "
             "joule of heat must appear as internal energy. 0.5 × 0.718 × 200 is the right order "
             "for a 200 K rise of half a kilogram of air.",
             "દૃઢ પાત્ર volume બદલી શકતું નથી, તેથી displacement work શક્ય નથી; heat નો દરેક જૂલ "
             "internal energy તરીકે જ આવવો જોઈએ. અડધા કિલો હવાના 200 K વધારા માટે "
             "0.5 × 0.718 × 200 સાચો ક્રમ છે."),
)

N2 = numerical(
    "N2",
    bi("Isothermal expansion of air",
       "હવાનું isothermal expansion"),
    given=bi("2 kg of air expands reversibly and isothermally at 400 K from 1.5 bar to "
             "0.5 bar. R = 0.287 kJ/kg·K.",
             "2 kg હવા 400 K પર 1.5 bar થી 0.5 bar સુધી reversible તથા isothermal રીતે expand થાય છે. "
             "R = 0.287 kJ/kg·K."),
    find=bi("Work done, heat transferred and change of internal energy.",
            "થયેલું work, transfer થયેલી heat તથા internal energy નો ફેરફાર."),
    formula=[E("W = m R T ln(P₁/P₂)", r"W=mRT\ln\frac{P_1}{P_2}"),
             E("isothermal, ideal gas:  ΔU = 0  ⇒  Q = W", r"\Delta U=0\Rightarrow Q=W")],
    substitution=bi(
        "W = 2 × 0.287 × 400 × ln(1.5/0.5) = 229.6 × ln 3 = 229.6 × 1.0986 = 252.3 kJ.",
        "W = 2 × 0.287 × 400 × ln(1.5/0.5) = 229.6 × ln 3 = 229.6 × 1.0986 = 252.3 kJ."),
    answer=bi("W = 252.3 kJ by the air;  Q = 252.3 kJ absorbed;  ΔU = 0.",
              "W = 252.3 kJ હવા દ્વારા;  Q = 252.3 kJ લેવાઈ;  ΔU = 0."),
    check=bi("Pressure falls by a factor of three, so the volume triples and the work is "
             "mRT ln 3. ΔU = 0 is the signature of an isothermal ideal-gas process: the whole "
             "heat input leaves as work.",
             "Pressure ત્રણ ગણું ઘટે છે, તેથી volume ત્રણ ગણું થાય અને work mRT ln 3 મળે. ΔU = 0 એ "
             "isothermal ideal-gas પ્રક્રિયાની ઓળખ છે: આખી heat work તરીકે નીકળી જાય."),
)

N3 = numerical(
    "N3",
    bi("Adiabatic compression of air",
       "હવાનું adiabatic compression"),
    given=bi("1 kg of air at 300 K and 1 bar is compressed adiabatically and reversibly to "
             "5 bar. γ = 1.4, c_v = 0.718 kJ/kg·K.",
             "1 bar તથા 300 K પરની 1 kg હવા 5 bar સુધી adiabatic તથા reversible રીતે compress થાય છે. "
             "γ = 1.4, c_v = 0.718 kJ/kg·K."),
    find=bi("Final temperature, work input and change of internal energy.",
            "અંતિમ temperature, અપાયેલું work તથા internal energy નો ફેરફાર."),
    formula=[E("T₂/T₁ = (P₂/P₁)^((γ−1)/γ)", r"\frac{T_2}{T_1}=\left(\frac{P_2}{P_1}\right)^{\frac{\gamma-1}{\gamma}}"),
             E("Q = 0  ⇒  W = −ΔU = m c_v (T₁ − T₂)", r"Q=0\Rightarrow W=-\Delta U")],
    substitution=bi(
        "(γ−1)/γ = 0.4/1.4 = 0.2857. T₂ = 300 × (5)^0.2857 = 300 × 1.584 = 475.1 K. "
        "ΔU = 1 × 0.718 × (475.1 − 300) = 125.7 kJ. W = −125.7 kJ, i.e. 125.7 kJ of work is "
        "put in.",
        "(γ−1)/γ = 0.4/1.4 = 0.2857. T₂ = 300 × (5)^0.2857 = 300 × 1.584 = 475.1 K. "
        "ΔU = 1 × 0.718 × (475.1 − 300) = 125.7 kJ. W = −125.7 kJ, એટલે કે 125.7 kJ work અંદર "
        "નાખવું પડે."),
    answer=bi("T₂ = 475 K;  work input = 125.7 kJ/kg;  ΔU = +125.7 kJ/kg.",
              "T₂ = 475 K;  work input = 125.7 kJ/kg;  ΔU = +125.7 kJ/kg."),
    check=bi("Adiabatic compression always heats the gas: 300 K to 475 K for a fivefold "
             "pressure rise is the standard result, and because Q = 0 the work input must equal "
             "the internal-energy rise exactly. The negative sign of W follows the convention "
             "that work done <i>by</i> the gas is positive.",
             "Adiabatic compression હંમેશા gas ને ગરમ કરે: પાંચ ગણા pressure વધારા માટે 300 K થી "
             "475 K પ્રમાણભૂત પરિણામ છે, અને Q = 0 હોવાથી work input બરાબર internal-energy વધારા "
             "જેટલું જ હોવું જોઈએ. W નું ઋણ ચિહ્ન એ convention પરથી છે કે gas <i>દ્વારા</i> થયેલું work ધન છે."),
)

N4 = numerical(
    "N4",
    bi("Steady-flow compressor",
       "Steady-flow compressor"),
    given=bi("Air enters a compressor at 1 bar, 300 K with negligible velocity and leaves at "
             "6 bar, 480 K. Mass flow 0.05 kg/s. Heat loss from the casing 3 kW. "
             "c_p = 1.005 kJ/kg·K.",
             "Air compressor માં 1 bar, 300 K પર લગભગ શૂન્ય velocity સાથે આવે છે અને 6 bar, 480 K પર "
             "નીકળે છે. Mass flow 0.05 kg/s. Casing થી heat loss 3 kW. c_p = 1.005 kJ/kg·K."),
    find=bi("Shaft power required, and the error made by neglecting the kinetic energy.",
            "જરૂરી shaft power, તથા kinetic energy નગણ્ય ગણવાથી થતી ભૂલ."),
    formula=[E("Q − W_s = m [ (h₂ − h₁) + ½(c₂² − c₁²) ]", r"Q-W_s=\dot m\left[(h_2-h_1)+\tfrac12(c_2^2-c_1^2)\right]"),
             E("Δh = c_p (T₂ − T₁)", r"\Delta h=c_p(T_2-T_1)")],
    substitution=bi(
        "Δh = 1.005 × (480 − 300) = 180.9 kJ/kg. With Q = −3 kW (heat lost) and KE neglected: "
        "−3 − W_s = 0.05 × 180.9 = 9.045 ⇒ W_s = −12.05 kW. The negative sign means 12.05 kW of "
        "shaft power must be supplied.",
        "Δh = 1.005 × (480 − 300) = 180.9 kJ/kg. Q = −3 kW (heat ગઈ) તથા KE નગણ્ય લેતાં: "
        "−3 − W_s = 0.05 × 180.9 = 9.045 ⇒ W_s = −12.05 kW. ઋણ ચિહ્ન એટલે 12.05 kW shaft power "
        "આપવું પડે."),
    answer=bi("Shaft power = 12.05 kW input.  Kinetic energy is negligible only if the exit "
              "velocity is small; at 50 m/s it would add ½c² = 1.25 kJ/kg, about 0.7 %.",
              "Shaft power = 12.05 kW input. Exit velocity નાની હોય તો જ kinetic energy નગણ્ય; "
              "50 m/s પર તે ½c² = 1.25 kJ/kg ઉમેરે, લગભગ 0.7 %."),
    check=bi("For 0.05 kg/s and 180 K rise the gas alone needs 9 kW; adding the 3 kW lost as "
             "heat gives about 12 kW, which is the right order for a small compressor. Heat "
             "loss <i>increases</i> the power needed, as the sign of Q shows.",
             "0.05 kg/s તથા 180 K વધારા માટે ફક્ત gas ને 9 kW જોઈએ; ગઈ 3 kW heat ઉમેરતાં લગભગ "
             "12 kW મળે, જે નાના compressor માટે સાચો ક્રમ છે. Heat loss powerની જરૂરિયાત "
             "<i>વધારે</i> છે, જે Q નું ચિહ્ન દર્શાવે છે."),
)

N5 = numerical(
    "N5",
    bi("Heat capacity relation for an ideal gas",
       "ideal gas માટે heat capacity નો સંબંધ"),
    given=bi("For a certain ideal gas c_p = 1.005 kJ/kg·K and R = 0.287 kJ/kg·K. 2 kg of the "
             "gas is heated at constant pressure through 100 K.",
             "એક ideal gas માટે c_p = 1.005 kJ/kg·K તથા R = 0.287 kJ/kg·K. 2 kg gas અચળ pressure પર "
             "100 K ગરમ કરાય છે."),
    find=bi("c_v, γ, ΔH, ΔU and the work done.",
            "c_v, γ, ΔH, ΔU તથા થયેલું work."),
    formula=[E("c_v = c_p − R", r"c_v=c_p-R"),
             E("γ = c_p / c_v", r"\gamma=\frac{c_p}{c_v}"),
             E("ΔH = m c_p ΔT ,  ΔU = m c_v ΔT ,  W = P ΔV = m R ΔT", r"W=mR\Delta T")],
    substitution=bi(
        "c_v = 1.005 − 0.287 = 0.718 kJ/kg·K. γ = 1.005/0.718 = 1.40. "
        "ΔH = 2 × 1.005 × 100 = 201.0 kJ. ΔU = 2 × 0.718 × 100 = 143.6 kJ. "
        "W = 2 × 0.287 × 100 = 57.4 kJ.",
        "c_v = 1.005 − 0.287 = 0.718 kJ/kg·K. γ = 1.005/0.718 = 1.40. "
        "ΔH = 2 × 1.005 × 100 = 201.0 kJ. ΔU = 2 × 0.718 × 100 = 143.6 kJ. "
        "W = 2 × 0.287 × 100 = 57.4 kJ."),
    answer=bi("c_v = 0.718 kJ/kg·K, γ = 1.40;  ΔH = 201.0 kJ;  ΔU = 143.6 kJ;  W = 57.4 kJ; "
              "Q = ΔH = 201.0 kJ.",
              "c_v = 0.718 kJ/kg·K, γ = 1.40;  ΔH = 201.0 kJ;  ΔU = 143.6 kJ;  W = 57.4 kJ; "
              "Q = ΔH = 201.0 kJ."),
    check=bi("The two routes must agree: Q = ΔU + W = 143.6 + 57.4 = 201.0 kJ, which equals ΔH. "
             "That agreement is the definition H = U + P V showing up numerically, and it is the "
             "quickest check in any constant-pressure problem.",
             "બંને રસ્તા મળવા જોઈએ: Q = ΔU + W = 143.6 + 57.4 = 201.0 kJ, જે ΔH જેટલું છે. આ મેળ એ "
             "H = U + P V વ્યાખ્યા આંકડામાં દેખાય તે છે, અને કોઈપણ constant-pressure દાખલામાં સૌથી ઝડપી "
             "ચકાસણી છે."),
)

N6 = numerical(
    "N6",
    bi("Nozzle: converting enthalpy into velocity",
       "Nozzle: enthalpy ને velocity માં ફેરવવી"),
    given=bi("Steam enters a well-insulated nozzle at 10 bar, 320 °C with velocity 40 m/s and "
             "leaves at 3 bar. The inlet enthalpy is 3 082 kJ/kg and the exit enthalpy "
             "2 902 kJ/kg.",
             "Steam well-insulated nozzle માં 10 bar, 320 °C પર 40 m/s velocity સાથે આવે છે અને 3 bar પર "
             "નીકળે છે. Inlet enthalpy 3 082 kJ/kg તથા exit enthalpy 2 902 kJ/kg."),
    find=bi("Exit velocity and the mass flow needed for 0.5 kg/s of steam to give a thrust.",
            "Exit velocity અને 0.5 kg/s steam માટે જરૂરી mass flow."),
    formula=[E("Q = 0, W_s = 0, Δz = 0 ⇒ h₁ + ½c₁² = h₂ + ½c₂²", r"h_1+\tfrac12c_1^2=h_2+\tfrac12c_2^2"),
             E("c₂ = √(2 (h₁ − h₂) + c₁²)", r"c_2=\sqrt{2(h_1-h_2)+c_1^2}")],
    substitution=bi(
        "h₁ − h₂ = 180 kJ/kg = 180 000 J/kg. Then c₂² = 2 × 180 000 + 40² = 360 000 + 1 600 "
        "= 361 600 ⇒ c₂ = 601.3 m/s.",
        "h₁ − h₂ = 180 kJ/kg = 180 000 J/kg. પછી c₂² = 2 × 180 000 + 40² = 360 000 + 1 600 "
        "= 361 600 ⇒ c₂ = 601.3 m/s."),
    answer=bi("c₂ ≈ 601 m/s (the 1 600 term is only 0.4 % of the total, so inlet velocity is "
              "usually neglected). For 0.5 kg/s the momentum change is 0.5 × 601 ≈ 300 N of "
              "thrust.",
              "c₂ ≈ 601 m/s (1 600 પદ કુલના ફક્ત 0.4 % છે, તેથી inlet velocity સામાન્ય રીતે નગણ્ય "
              "ગણાય). 0.5 kg/s માટે momentum ફેરફાર 0.5 × 601 ≈ 300 N thrust."),
    check=bi("Nozzles are adiabatic and do no shaft work, so the whole enthalpy drop becomes "
             "kinetic energy — 180 kJ/kg giving about 600 m/s is the standard order for steam. "
             "Note the unit conversion: kJ/kg must be multiplied by 1 000 to give m²/s².",
             "Nozzle adiabatic હોય અને shaft work કરતું નથી, તેથી આખો enthalpy ઘટાડો kinetic energy "
             "બને — 180 kJ/kg માટે લગભગ 600 m/s steam માટે પ્રમાણભૂત ક્રમ છે. Unit conversion ધ્યાનમાં "
             "રાખો: m²/s² મળે તે માટે kJ/kg ને 1 000 વડે ગુણવું પડે."),
)

# =============================================================== viva
VIVA = [
    viva(bi("State the first law of thermodynamics and give its mathematical form for a closed system.",
            "થર્મોડાયનેમિક્સનો પ્રથમ નિયમ જણાવો અને closed system માટે તેનું ગાણિતિક સ્વરૂપ આપો."),
         bi("Energy can neither be created nor destroyed, only converted. For a closed system "
            "Q − W = ΔU + Δ(KE) + Δ(PE), and for a closed stationary system Q − W = ΔU.",
            "ઊર્જા ઉત્પન્ન કે નષ્ટ થઈ શકતી નથી, ફક્ત રૂપાંતરિત થાય. closed system માટે "
            "Q − W = ΔU + Δ(KE) + Δ(PE), અને closed સ્થિર system માટે Q − W = ΔU.")),
    viva(bi("What is internal energy? Why is only its change calculated?",
            "Internal energy શું છે? તેનો ફક્ત ફેરફાર જ કેમ ગણાય છે?"),
         bi("Internal energy is the sum of the molecular kinetic and potential energies of the "
            "system. Its absolute value depends on an arbitrary reference state, which does not "
            "affect any energy balance, so only differences between states are used.",
            "Internal energy એ system ના molecular kinetic તથા potential energy નો સરવાળો છે. તેની "
            "નિરપેક્ષ કિંમત મનસ્વી reference state પર આધાર રાખે, જે કોઈ energy balance ને અસર કરતી "
            "નથી, તેથી ફક્ત states વચ્ચેના તફાવત વપરાય છે.")),
    viva(bi("Define enthalpy and explain why it is used for flow processes.",
            "Enthalpy ની વ્યાખ્યા આપો અને flow processes માટે તે કેમ વપરાય છે તે સમજાવો."),
         bi("H = U + P V. For a flowing fluid the surroundings also do flow work P V to push it "
            "across the boundary; grouping that with U gives H, so the steady-flow equation "
            "contains h with no separate flow-work term. That is why steam tables give h.",
            "H = U + P V. વહેતા fluid માટે surroundings તેને boundary પાર ધકેલવા flow work P V પણ કરે "
            "છે; તેને U સાથે જૂથ કરવાથી H મળે, તેથી steady-flow equation માં અલગ flow-work પદ વગર h "
            "આવે. એટલે જ steam tables h આપે છે.")),
    viva(bi("Why is c_p greater than c_v for a gas?",
            "Gas માટે c_p એ c_v કરતાં મોટું કેમ હોય છે?"),
         bi("At constant volume no work is done, so all the heat raises internal energy. At "
            "constant pressure the gas also expands and does work P Δv, so extra heat is needed "
            "for the same temperature rise. For an ideal gas c_p − c_v = R.",
            "અચળ volume પર કોઈ work થતું નથી, તેથી આખી heat internal energy વધારે. અચળ pressure પર gas "
            "expand થઈને work P Δv પણ કરે છે, તેથી એટલા જ temperature વધારા માટે વધુ heat જોઈએ. ideal "
            "gas માટે c_p − c_v = R.")),
    viva(bi("Write the steady-flow energy equation and state its assumptions.",
            "Steady-flow energy equation લખો અને તેની assumptions જણાવો."),
         bi("q − w_s = (h₂ − h₁) + ½(c₂² − c₁²) + g(z₂ − z₁). Assumptions: steady state, one "
            "inlet and one outlet, uniform properties at each section, no reaction, and changes "
            "of kinetic and potential energy often neglected.",
            "q − w_s = (h₂ − h₁) + ½(c₂² − c₁²) + g(z₂ − z₁). Assumptions: steady state, એક inlet તથા "
            "એક outlet, દરેક section પર સરખી properties, કોઈ reaction નહીં, અને ઘણી વાર kinetic તથા "
            "potential energy ના ફેરફાર નગણ્ય.")),
    viva(bi("Distinguish between a non-flow and a flow process with one example each.",
            "Non-flow તથા flow પ્રક્રિયા વચ્ચે ભેદ આપો, દરેકનું એક ઉદાહરણ આપો."),
         bi("In a non-flow process a fixed mass stays in the system and no mass crosses the "
            "boundary (gas heated in a closed cylinder, Q − W = ΔU). In a flow process mass "
            "enters and leaves continuously (compressor, turbine, nozzle) and the equation uses "
            "enthalpy instead of internal energy.",
            "Non-flow પ્રક્રિયામાં નિશ્ચિત mass system માં રહે છે અને boundary પાર mass જતું નથી "
            "(closed cylinder માં ગરમ થતો gas, Q − W = ΔU). Flow પ્રક્રિયામાં mass સતત અંદર આવે તથા "
            "બહાર જાય (compressor, turbine, nozzle) અને સમીકરણ internal energy ને બદલે enthalpy વાપરે.")),
    viva(bi("Show that Q_net = W_net for a cyclic process.",
            "Cyclic પ્રક્રિયા માટે Q_net = W_net સાબિત કરો."),
         bi("A cycle returns the system to its initial state, so ΔU = 0. The first law Q − W = ΔU "
            "then gives Q_net = W_net: the net heat supplied equals the net work delivered.",
            "Cycle system ને પ્રારંભિક state પર પાછું લાવે છે, તેથી ΔU = 0. પ્રથમ નિયમ Q − W = ΔU પરથી "
            "Q_net = W_net મળે: ચોખ્ખી અપાયેલી heat ચોખ્ખા આપેલા work જેટલી.")),
    viva(bi("What is a perpetual-motion machine of the first kind?",
            "પહેલા પ્રકારની perpetual-motion machine શું છે?"),
         bi("A machine that would deliver work continuously with no energy input. The first law "
            "forbids it because the energy account could never balance.",
            "એવી machine જે કોઈ ઊર્જા લીધા વગર સતત work આપે. પ્રથમ નિયમ તેને નિષેધે છે કારણ કે ઊર્જાનો "
            "હિસાબ કદી બેસી શકે નહીં.")),
]

# =============================================================== exam
EXAM = [
    exam(bi("State the first law of thermodynamics. Express it for (i) a closed system, "
            "(ii) a closed stationary system, (iii) a cyclic process.",
            "થર્મોડાયનેમિક્સનો પ્રથમ નિયમ જણાવો. તેને (i) closed system, (ii) closed સ્થિર system, "
            "(iii) cyclic પ્રક્રિયા માટે લખો."), 4),
    exam(bi("Define internal energy and enthalpy. Derive the relation H = U + P V and explain "
            "why enthalpy appears in flow processes.",
            "Internal energy તથા enthalpy ની વ્યાખ્યા આપો. H = U + P V સંબંધ મેળવો અને flow processes "
            "માં enthalpy કેમ આવે તે સમજાવો."), 4),
    exam(bi("Explain why c_p is greater than c_v for a gas. Show that c_p − c_v = R for an "
            "ideal gas.",
            "Gas માટે c_p એ c_v કરતાં મોટું કેમ છે તે સમજાવો. ideal gas માટે c_p − c_v = R દર્શાવો."), 4),
    exam(bi("Derive the steady-flow energy equation for a control volume with one inlet and "
            "one outlet, stating all assumptions clearly.",
            "એક inlet તથા એક outlet વાળા control volume માટે steady-flow energy equation મેળવો અને "
            "બધી assumptions સ્પષ્ટ લખો."), 4),
    exam(bi("Distinguish between a non-flow and a flow process. Write the first-law equation "
            "for each and give two examples of each.",
            "Non-flow તથા flow પ્રક્રિયા વચ્ચે ભેદ આપો. દરેકના પ્રથમ નિયમનું સમીકરણ લખો અને દરેકના બે "
            "ઉદાહરણ આપો."), 4),
    exam(bi("0.5 kg of air is heated in a rigid vessel from 27 °C to 227 °C. Calculate W, ΔU "
            "and Q. Take c_v = 0.718 kJ/kg·K.",
            "0.5 kg હવા દૃઢ પાત્રમાં 27 °C થી 227 °C સુધી ગરમ કરાય છે. W, ΔU તથા Q ગણો. "
            "c_v = 0.718 kJ/kg·K લો."), 4),
    exam(bi("2 kg of air expands isothermally at 400 K from 1.5 bar to 0.5 bar. Find the work "
            "done and the heat transferred. R = 0.287 kJ/kg·K.",
            "2 kg હવા 400 K પર 1.5 bar થી 0.5 bar સુધી isothermal રીતે expand થાય છે. થયેલું work તથા "
            "transfer થયેલી heat શોધો. R = 0.287 kJ/kg·K."), 4),
    exam(bi("1 kg of air at 300 K is compressed adiabatically and reversibly to 5 bar. Find the "
            "final temperature and the work input. Take γ = 1.4, c_v = 0.718 kJ/kg·K.",
            "300 K પરની 1 kg હવા 5 bar સુધી adiabatic તથા reversible રીતે compress થાય છે. અંતિમ "
            "temperature તથા work input શોધો. γ = 1.4, c_v = 0.718 kJ/kg·K લો."), 4),
    exam(bi("Air enters a compressor at 1 bar, 300 K and leaves at 6 bar, 480 K. Mass flow "
            "0.05 kg/s, heat loss 3 kW, c_p = 1.005 kJ/kg·K. Calculate the shaft power.",
            "Air compressor માં 1 bar, 300 K પર આવે છે અને 6 bar, 480 K પર નીકળે છે. Mass flow "
            "0.05 kg/s, heat loss 3 kW, c_p = 1.005 kJ/kg·K. Shaft power ગણો."), 4),
    exam(bi("Steam enters an insulated nozzle at 3 082 kJ/kg and leaves at 2 902 kJ/kg. If the "
            "inlet velocity is 40 m/s, find the exit velocity.",
            "Steam insulated nozzle માં 3 082 kJ/kg પર આવે છે અને 2 902 kJ/kg પર નીકળે છે. Inlet "
            "velocity 40 m/s હોય તો exit velocity શોધો."), 4),
    exam(bi("For an ideal gas c_p = 1.005 and R = 0.287 kJ/kg·K. Find c_v and γ, and calculate "
            "ΔH, ΔU and W when 2 kg is heated at constant pressure through 100 K.",
            "ideal gas માટે c_p = 1.005 તથા R = 0.287 kJ/kg·K. c_v તથા γ શોધો, અને 2 kg ને અચળ "
            "pressure પર 100 K ગરમ કરતાં ΔH, ΔU તથા W ગણો."), 4),
    exam(bi("State the limitations of the first law of thermodynamics and explain why a second "
            "law is needed.",
            "થર્મોડાયનેમિક્સના પ્રથમ નિયમની મર્યાદાઓ જણાવો અને બીજો નિયમ કેમ જરૂરી છે તે સમજાવો."), 4),
]

# =============================================================== formula sheet
SYNTAX = [
    {"title": bi("First law forms", "પ્રથમ નિયમનાં સ્વરૂપો"),
     "items": [
         {"title": bi("Closed system", "Closed system"),
          "f": "Q − W = ΔU  (stationary);  Q − W = ΔU + ΔKE + ΔPE  (general)",
          "terms": "Heat in and work out are positive in this course."},
         {"title": bi("Steady flow", "Steady flow"),
          "f": "q − w_s = (h₂ − h₁) + ½(c₂² − c₁²) + g(z₂ − z₁)",
          "terms": "One inlet, one outlet, properties uniform at each section."},
         {"title": bi("Cycle", "Cycle"),
          "f": "∮dU = 0  ⇒  Q_net = W_net",
          "terms": "ΔU of a complete cycle is zero."},
     ]},
    {"title": bi("Properties and heat capacity", "Properties તથા heat capacity"),
     "items": [
         {"title": bi("Enthalpy", "Enthalpy"),
          "f": "H = U + P V;   h = u + P v",
          "terms": "h replaces u in every flow equation, with no flow-work term."},
         {"title": bi("Ideal gas", "Ideal gas"),
          "f": "ΔU = m c_v ΔT;   ΔH = m c_p ΔT;   c_p − c_v = R;   γ = c_p / c_v",
          "terms": "True for every path when the gas is ideal."},
         {"title": bi("Non-flow work", "Non-flow work"),
          "f": "W = ∫P dV (reversible);  constant P: W = P ΔV;  constant V: W = 0",
          "terms": "Valid for a reversible path only."},
         {"title": bi("Isothermal and adiabatic", "Isothermal તથા adiabatic"),
          "f": "isothermal: W = mRT ln(V₂/V₁);  adiabatic: T₂/T₁ = (P₂/P₁)^((γ−1)/γ)",
          "terms": "Adiabatic also: P V^γ = constant, T V^(γ−1) = constant."},
     ]},
]

# =============================================================== build
def build() -> Unit:
    u = Unit(CODE, 2, TITLE, hours=7, weightage=18,
             tabs=["notes", "programs", "diagrams", "syntax", "viva", "exam"],
             tab_labels={"programs": bi("Solved numericals", "ઉકેલેલા દાખલા"),
                         "syntax": bi("Formulae and conversions", "સૂત્રો તથા conversions")})
    u.section(bi("2.1  Statement of the first law", "2.1  પ્રથમ નિયમનું વિધાન"), S1)
    u.section(bi("2.2  Internal energy, enthalpy and heat capacity",
                 "2.2  Internal energy, enthalpy તથા heat capacity"), S2)
    u.section(bi("2.3  Non-flow processes and the steady-flow equation",
                 "2.3  Non-flow પ્રક્રિયાઓ તથા steady-flow equation"), S3)
    u.section(bi("2.4  Forms of work and the c_p - c_v relation",
                 "2.4  Work નાં સ્વરૂપો તથા c_p - c_v સંબંધ"), S4)
    u.data["programs"] = [N1, N2, N3, N4, N5, N6]
    u.diagram("d2_energy_forms",
              bi("The energy account of a closed system", "closed system નું energy હિસાબ"),
              "diagrams/d2_energy_forms.svg")
    u.diagram("d2_nonflow_paths",
              bi("Same two states, two paths: Q and W differ, ΔU does not",
                 "સરખી બે states, બે રસ્તા: Q તથા W જુદા, ΔU નહીં"),
              "diagrams/d2_nonflow_paths.svg")
    u.diagram("d2_steady_flow",
              bi("Steady-flow energy equation across a control volume",
                 "control volume પર steady-flow energy equation"),
              "diagrams/d2_steady_flow.svg")
    u.diagram("d2_heat_capacity",
              bi("Heat capacity at constant volume and at constant pressure",
                 "અચળ volume તથા અચળ pressure પર heat capacity"),
              "diagrams/d2_heat_capacity.svg")
    for s in SYNTAX:
        u.data.setdefault("syntax", []).append(s)
    u.data["viva"] = VIVA
    u.data["exam_questions"] = EXAM
    return u


if __name__ == "__main__":
    unit = build()
    problems = unit.validate()
    out = unit.write("content/chemical/sem4/DI04005041/unit2.json")
    print("wrote", out)
    print("problems:", problems or "none")
