"""Content for DI04005041 Unit 3 "PVT Behavior", GTU Diploma Chemical
Engineering, semester 4, syllabus w.e.f. 2025-26.

Coverage is the official syllabus 3.1 - 3.5:
  3.1 PVT behaviour of pure fluids with PV and PT diagram
  3.2 ideal gas and equation of state
  3.3 ideal gas processes (constant V, P, T, adiabatic, polytropic)
  3.4 equation of state for real gases (Van der Waals, virial, compressibility charts)
  3.5 numericals on ideal and real gas equations

Reference matter: Narayanan; Smith, Van Ness & Abbott; Gavhane; Rajput.
"""
from d1notes import Unit, bi, derivation, exam, numerical, theory, viva


def E(display, tex=None, note=None):
    return (display, tex or display, note) if note else (display, tex or display)


CODE = "DI04005041"
TITLE = bi("PVT Behavior", "PVT વર્તન")

# =============================================================== 3.1 PVT behaviour
S1 = [
    theory(
        "3.1",
        bi("PVT behaviour of a pure fluid", "pure fluid નું PVT વર્તન"),
        definition=bi(
            "The <b>PVT behaviour</b> of a substance is the relationship between its pressure, "
            "volume and temperature. For a pure fluid only <b>two</b> of the three are "
            "independent (F = 2 for a single phase), so the state is completely fixed by any "
            "two of them and the third follows from an equation of state, a table or a diagram.",
            "<b>PVT વર્તન</b> એ પદાર્થના pressure, volume તથા temperature વચ્ચેનો સંબંધ છે. pure "
            "fluid માટે ત્રણમાંથી ફક્ત <b>બે</b> સ્વતંત્ર હોય છે (single phase માટે F = 2), તેથી કોઈપણ "
            "બે પરથી state પૂરી રીતે નક્કી થાય અને ત્રીજું equation of state, table કે diagram પરથી મળે."),
        theory_text=bi(
            "The complete behaviour is a surface in three dimensions. Engineers never draw that "
            "surface; they take two views of it. The <b>P–V diagram</b> (at fixed temperature "
            "slices) shows the familiar isotherms with their flat condensation plateaus and the "
            "saturation dome. The <b>P–T diagram</b> (projecting the phase boundaries) shows "
            "three regions — solid, liquid, vapour — separated by the fusion, sublimation and "
            "vapour-pressure curves, meeting at the triple point.<br><br>"
            "Each line on a P–T diagram carries a definite meaning. On the vapour-pressure line "
            "liquid and vapour coexist, so P = 2 and F = 1: choosing the temperature fixes the "
            "pressure. In the region inside one phase F = 2 and both may be chosen. At the "
            "triple point F = 0 and nature fixes both. Above the critical point there is no "
            "boundary at all, and the substance is called a supercritical fluid.",
            "સંપૂર્ણ વર્તન ત્રિ-પરિમાણીય surface છે. Engineer તે surface દોરતા નથી; તેના બે દૃશ્ય "
            "લે છે. <b>P–V diagram</b> (અચળ temperature ના slice) પરિચિત isotherms, તેમના સપાટ "
            "condensation plateau તથા saturation dome દર્શાવે છે. <b>P–T diagram</b> (phase "
            "boundaries નું projection) ત્રણ પ્રદેશ — solid, liquid, vapour — દર્શાવે છે, જે fusion, "
            "sublimation તથા vapour-pressure curves થી અલગ પડે છે અને triple point પર મળે છે.<br><br>"
            "P–T diagram પરની દરેક રેખાનો ચોક્કસ અર્થ છે. vapour-pressure રેખા પર liquid તથા vapour "
            "સાથે રહે છે, તેથી P = 2 અને F = 1: temperature પસંદ કરતાં pressure નિશ્ચિત થાય. એક જ phase "
            "વાળા પ્રદેશમાં F = 2 અને બંને પસંદ કરી શકાય. triple point પર F = 0 અને પ્રકૃતિ બંને નિશ્ચિત "
            "કરે છે. critical point ઉપર કોઈ boundary જ નથી, અને તે પદાર્થને supercritical fluid કહે છે."),
        equations=[E("P V = Z n R T   (Z = 1 for an ideal gas)", r"PV=ZnRT"),
                   E("critical point:  (∂P/∂V)_T = 0  and  (∂²P/∂V²)_T = 0", r"\left(\frac{\partial P}{\partial V}\right)_T=0"),
                   E("reduced coordinates:  P_r = P/P_c ,  T_r = T/T_c ,  V_r = V/V_c", r"P_r=\frac{P}{P_c}")],
        list_items=[
            "<b>Triple point of water:</b> 0.01 °C and 0.006 11 bar — ice, water and vapour coexist.",
            "<b>Critical point of water:</b> 374.15 °C and 221.2 bar; above it no amount of pressure will liquefy steam.",
            "<b>Critical point of CO₂:</b> 31.0 °C and 73.8 bar — why CO₂ is a convenient supercritical solvent.",
            "<b>Below the triple point</b> a solid sublimes directly to vapour; that is why ice evaporates in a freezer without melting.",
        ],
        diagram="d3_pv_diagram",
        qualification=bi(
            "The P–V diagram shows only one temperature at a time; the P–T diagram shows the "
            "phase boundaries but no volume. Neither alone is enough — an equation of state or a "
            "table gives the third variable, which is why steam tables list v, u, h and s "
            "together.",
            "P–V diagram એક સમયે ફક્ત એક temperature દર્શાવે છે; P–T diagram phase boundaries દર્શાવે છે પણ "
            "volume નહીં. એકલું કોઈ પણ પૂરતું નથી — equation of state કે table ત્રીજું variable આપે છે, "
            "એટલે જ steam tables v, u, h તથા s સાથે આપે છે."),
    ),
]

# =============================================================== 3.1b P-T diagram
S2 = [
    theory(
        "3.2",
        bi("The P–T diagram, triple point and critical point",
           "P–T diagram, triple point તથા critical point"),
        definition=bi(
            "The <b>P–T diagram</b> plots the phase boundaries of a pure substance in the "
            "pressure–temperature plane. Three curves meet at the <b>triple point</b>: the "
            "<b>sublimation</b> curve (solid–vapour), the <b>fusion</b> curve (solid–liquid) and "
            "the <b>vapour-pressure</b> curve (liquid–vapour), which ends at the "
            "<b>critical point</b>.",
            "<b>P–T diagram</b> pure substance ની phase boundaries ને pressure–temperature plane માં "
            "દર્શાવે છે. ત્રણ curves <b>triple point</b> પર મળે છે: <b>sublimation</b> curve (solid–vapour), "
            "<b>fusion</b> curve (solid–liquid) અને <b>vapour-pressure</b> curve (liquid–vapour), જે "
            "<b>critical point</b> પર પૂરી થાય છે."),
        theory_text=bi(
            "Each curve carries one degree of freedom. On the vapour-pressure curve liquid and "
            "vapour coexist, so F = C − P + 2 = 1 − 2 + 2 = 1: a single choice (say the pressure "
            "of a boiler) fixes the boiling temperature. At the triple point all three phases "
            "coexist, F = 1 − 3 + 2 = 0, so for water it occurs at exactly 0.01 °C and 0.006 11 "
            "bar and cannot be shifted.<br><br>"
            "The fusion curve of water slopes <b>backwards</b> (negative slope), which is unusual: "
            "increasing the pressure on ice lowers its melting point, because ice is less dense "
            "than water. That is why a skater's blade melts a thin film under it. For almost "
            "every other substance the fusion curve slopes forward. The vapour-pressure curve "
            "ends at the critical point; beyond it the liquid and gas are indistinguishable and "
            "the term supercritical fluid is used.",
            "દરેક curve એક degree of freedom ધરાવે છે. vapour-pressure curve પર liquid તથા vapour સાથે "
            "રહે, તેથી F = C − P + 2 = 1 − 2 + 2 = 1: એક પસંદગી (જેમ કે boiler નું pressure) ઉકળવાનું "
            "temperature નિશ્ચિત કરે. triple point પર ત્રણેય phases સાથે રહે, F = 1 − 3 + 2 = 0, તેથી "
            "પાણી માટે તે બરાબર 0.01 °C તથા 0.006 11 bar પર થાય અને બદલી શકાય નહીં.<br><br>"
            "પાણીની fusion curve <b>પાછળ તરફ</b> ઢળે છે (ઋણ ઢોળાવ), જે અસામાન્ય છે: બરફ પર pressure "
            "વધારતાં તેનું melting point ઘટે છે, કારણ કે બરફ પાણી કરતાં ઓછા density નો છે. એટલે જ સ્કેટર "
            "ના બ્લેડ નીચે પાતળો પડ ઓગળે છે. લગભગ દરેક બીજા પદાર્થની fusion curve આગળ તરફ ઢળે છે. "
            "vapour-pressure curve critical point પર પૂરી થાય; તેની પાર liquid તથા gas અલગ ઓળખી શકાતા "
            "નથી અને supercritical fluid શબ્દ વપરાય છે."),
        equations=[E("Clausius–Clapeyron:  ln(P₂/P₁) = −(ΔH_vap/R)(1/T₂ − 1/T₁)",
                     r"\ln\frac{P_2}{P_1}=-\frac{\Delta H_{vap}}{R}\left(\frac{1}{T_2}-\frac{1}{T_1}\right)"),
                   E("on a boundary:  F = C − P + 2 = 1", r"F=1"),
                   E("at the triple point:  F = 0", r"F=0")],
        list_items=[
            "<b>Water:</b> triple point 0.01 °C, 0.006 11 bar; critical point 374.15 °C, 221.2 bar.",
            "<b>CO₂:</b> triple point −56.6 °C, 5.18 bar — solid CO₂ (dry ice) sublimes at atmospheric pressure, it never melts.",
            "<b>Clausius–Clapeyron</b> gives the slope of the vapour-pressure curve and is used to estimate boiling points at other pressures.",
            "<b>Supercritical CO₂</b> (above 31 °C, 73.8 bar) is used for decaffeination and dry-cleaning because it is a dense, tunable solvent.",
        ],
        qualification=bi(
            "The P–T diagram says nothing about volume or about how much of each phase is "
            "present — a point on the vapour-pressure line could be 1 % vapour or 99 % vapour. "
            "The P–V diagram or a quality value is needed for that.",
            "P–T diagram volume વિશે કે દરેક phase કેટલી છે તે વિશે કંઈ કહેતું નથી — vapour-pressure રેખા "
            "પરનું બિંદુ 1 % vapour કે 99 % vapour હોઈ શકે. તેના માટે P–V diagram કે quality ની કિંમત "
            "જોઈએ."),
    ),
]


# =============================================================== 3.3 ideal gas
S3 = [
    theory(
        "3.3",
        bi("Ideal gas and the equation of state", "ideal gas તથા equation of state"),
        definition=bi(
            "An <b>ideal gas</b> is a model in which molecules have negligible volume and exert "
            "no forces on one another except during elastic collisions. Its equation of state is "
            "<b>P V = n R T</b>, and it defines the gas constant "
            "R = 8.314 kJ/kmol·K = 0.287 kJ/kg·K for air.",
            "<b>Ideal gas</b> એ model છે જેમાં molecules નું volume નગણ્ય હોય અને elastic collisions "
            "સિવાય એકબીજા પર બળ ન કરે. તેનું equation of state <b>P V = n R T</b> છે, અને gas constant "
            "R = 8.314 kJ/kmol·K = હવા માટે 0.287 kJ/kg·K."),
        theory_text=bi(
            "The model is the baseline against which every real fluid is judged, and its "
            "consequences are worth memorising because they cover most numericals. Internal "
            "energy and enthalpy depend on <b>temperature only</b> (Joule's law), so ΔU = m "
            "c<sub>v</sub> ΔT and ΔH = m c<sub>p</sub> ΔT for every path. At constant temperature "
            "P V is constant; at constant pressure V/T is constant; at constant volume P/T is "
            "constant.<br><br>"
            "The model is accurate at low pressure and high temperature, where molecules are far "
            "apart and their own volume and attraction hardly matter. It fails badly near the "
            "boiling point and near the critical point, which is exactly where real-gas "
            "corrections are needed. Always state the assumption 'behaves as an ideal gas' "
            "before using P V = n R T on a real substance.",
            "આ model એ દરેક વાસ્તવિક fluid ને માપવાનો પાયો છે, અને તેના પરિણામો મોઢે યાદ રાખવા જેવા છે કારણ "
            "કે તે મોટાભાગના દાખલા આવરી લે છે. Internal energy તથા enthalpy ફક્ત <b>temperature</b> પર "
            "આધાર રાખે છે (Joule's law), તેથી દરેક path માટે ΔU = m c<sub>v</sub> ΔT અને "
            "ΔH = m c<sub>p</sub> ΔT. અચળ temperature પર P V અચળ; અચળ pressure પર V/T અચળ; અચળ volume પર "
            "P/T અચળ.<br><br>"
            "આ model નીચા pressure તથા ઊંચા temperature પર સચોટ છે, જ્યાં molecules દૂર દૂર હોય અને તેમનું "
            "volume તથા attraction ભાગ્યે જ મહત્વનાં રહે. boiling point તથા critical point ની નજીક તે ખૂબ "
            "નિષ્ફળ જાય છે, અને ત્યાં જ real-gas corrections જરૂરી થાય. વાસ્તવિક પદાર્થ પર P V = n R T "
            "વાપરતાં પહેલાં 'behaves as an ideal gas' assumption હંમેશા લખો."),
        equations=[E("P V = n R T        P v = R T        P V = m R T", r"PV=nRT"),
                   E("R = 8.314 kJ/kmol·K = 8.314 J/mol·K = 0.083 14 bar·m³/kmol·K", r"R=8.314"),
                   E("at 1 atm, 0 °C:  1 kmol occupies 22.414 m³;  at 1 bar, 0 °C: 22.71 m³",
                     r"V_m=22.414\ \mathrm{m^3/kmol}")],
        list_items=[
            "<b>Boyle's law</b> (T, n constant): P V = constant.",
            "<b>Charles's law</b> (P, n constant): V / T = constant.",
            "<b>Gay-Lussac's law</b> (V, n constant): P / T = constant.",
            "<b>Always use absolute pressure and absolute temperature</b> in P V = n R T.",
        ],
        qualification=bi(
            "No gas is ideal. Air at 300 K and 1 bar is within about 0.1 % of ideal; steam at "
            "10 bar and 180 °C is not. The error grows with pressure and near saturation, so a "
            "result that comes from P V = n R T near the critical point should be checked "
            "against the compressibility chart.",
            "કોઈ gas ideal નથી. 300 K તથા 1 bar પર હવા લગભગ 0.1 % જ ideal ની નજીક છે; 10 bar તથા "
            "180 °C પર steam નથી. pressure સાથે અને saturation ની નજીક ભૂલ વધે છે, તેથી critical point "
            "ની નજીક P V = n R T થી મળેલો જવાબ compressibility chart સાથે ચકાસવો જોઈએ."),
    ),
]

# =============================================================== 3.3 processes
S4 = [
    theory(
        "3.4",
        bi("Ideal-gas processes: constant V, P, T, adiabatic and polytropic",
           "ideal-gas પ્રક્રિયાઓ: અચળ V, P, T, adiabatic તથા polytropic"),
        definition=bi(
            "An <b>ideal-gas process</b> is a path on which one relation between P, V and T is "
            "maintained. Five are used: constant volume (<b>isochoric</b>), constant pressure "
            "(<b>isobaric</b>), constant temperature (<b>isothermal</b>), no heat transfer "
            "(<b>adiabatic</b>) and the general <b>polytropic</b> path P V<sup>n</sup> = "
            "constant, of which the first four are special cases.",
            "<b>Ideal-gas process</b> એ એવો રસ્તો છે જેમાં P, V તથા T વચ્ચેનો એક સંબંધ જળવાય. પાંચ "
            "વપરાય છે: અચળ volume (<b>isochoric</b>), અચળ pressure (<b>isobaric</b>), અચળ temperature "
            "(<b>isothermal</b>), heat transfer વગર (<b>adiabatic</b>) અને સામાન્ય <b>polytropic</b> રસ્તો "
            "P V<sup>n</sup> = અચળ, જેમાં પહેલા ચાર તેના ખાસ કિસ્સા છે."),
        theory_text=bi(
            "The polytropic relation is the key to the whole topic. Putting n = 0 gives P = "
            "constant (isobaric), n = 1 gives P V = constant (isothermal, ideal gas), n = γ "
            "gives the adiabatic path and n → ∞ gives V = constant (isochoric). A single formula "
            "for the work, W = m R (T₁ − T₂)/(n − 1), therefore covers every case except the "
            "isothermal one, where the denominator vanishes and the logarithmic form must be "
            "used instead.<br><br>"
            "An adiabatic path is always <b>steeper</b> than an isothermal one through the same "
            "point, because γ > 1. That is why a gas cools as it expands adiabatically — the "
            "work comes out of its internal energy — and why a compressor gets hot. During the "
            "suction and discharge strokes of a real compressor the pressure falls and rises at "
            "nearly constant volume, which is why the indicator diagram has rounded ends rather "
            "than clean verticals.",
            "polytropic સંબંધ આખા વિષયની ચાવી છે. n = 0 મૂકતાં P = અચળ (isobaric), n = 1 મૂકતાં "
            "P V = અચળ (isothermal, ideal gas), n = γ મૂકતાં adiabatic રસ્તો અને n → ∞ મૂકતાં V = અચળ "
            "(isochoric) મળે. તેથી work માટેનું એક જ સૂત્ર W = m R (T₁ − T₂)/(n − 1) isothermal સિવાય "
            "દરેક કિસ્સો આવરી લે છે; ત્યાં denominator શૂન્ય થાય તેથી logarithmic સ્વરૂપ વાપરવું પડે.<br><br>"
            "એક જ બિંદુમાંથી પસાર થતો adiabatic રસ્તો isothermal કરતાં હંમેશા <b>ઢોળાવવાળો</b> હોય છે, "
            "કારણ કે γ > 1. એટલે જ adiabatic રીતે expand થતાં gas ઠંડું થાય — work તેની internal energy "
            "માંથી આવે — અને એટલે જ compressor ગરમ થાય. વાસ્તવિક compressor ના suction તથા discharge "
            "stroke દરમિયાન pressure લગભગ અચળ volume પર ઘટે તથા વધે, એટલે indicator diagram ના છેડા "
            "ગોળ હોય છે, સીધા ઊભા નહીં."),
        equations=[E("polytropic:  P V^n = c ,   W = m R (T₁ − T₂) / (n − 1)", r"PV^n=c"),
                   E("isothermal (n = 1):  W = m R T ln(V₂/V₁) = m R T ln(P₁/P₂)", r"W=mRT\ln\frac{V_2}{V_1}"),
                   E("adiabatic:  T₂/T₁ = (P₂/P₁)^((γ−1)/γ) = (V₁/V₂)^(γ−1)", r"\frac{T_2}{T_1}=\left(\frac{P_2}{P_1}\right)^{\frac{\gamma-1}{\gamma}}"),
                   E("heat in a polytropic process:  Q = m c_v (T₂ − T₁) (γ − n)/(γ − 1)",
                     r"Q=mc_v(T_2-T_1)\frac{\gamma-n}{\gamma-1}")],
        list_items=[
            "<b>n = 0</b> isobaric, <b>n = 1</b> isothermal, <b>n = γ</b> adiabatic, <b>n = ∞</b> isochoric; real compression often has n ≈ 1.2–1.35.",
            "<b>Adiabatic:</b> Q = 0, so W = −ΔU and the gas cools on expansion.",
            "<b>Isothermal:</b> ΔU = 0 for an ideal gas, so W = Q.",
            "<b>Watch the sign:</b> work done by the gas is positive; a compressor that consumes work reports W negative.",
        ],
        diagram="d3_ideal_processes",
        qualification=bi(
            "The formula W = m R (T₁ − T₂)/(n − 1) fails as n → 1, where it becomes 0/0; use the "
            "logarithmic form there. It also assumes constant heat capacity over the temperature "
            "range, which is a poor assumption for a wide range and for gases such as CO₂.",
            "W = m R (T₁ − T₂)/(n − 1) સૂત્ર n → 1 આસપાસ નિષ્ફળ જાય છે, ત્યાં 0/0 થાય; તેથી ત્યાં "
            "logarithmic સ્વરૂપ વાપરો. તે આખા temperature ગાળામાં c અચળ હોવાનું પણ ધારે છે, જે મોટા "
            "ગાળા માટે તથા CO₂ જેવા gases માટે નબળું assumption છે."),
    ),
    derivation(
        "3.5",
        bi("Adiabatic relation P V^γ = constant",
           "adiabatic સંબંધ P V^γ = અચળ"),
        symbols=bi(
            "<b>Model:</b> an ideal gas in a perfectly insulated cylinder, compressed "
            "reversibly and adiabatically. <b>Assumptions:</b> ideal gas with constant "
            "c<sub>v</sub> and c<sub>p</sub>, reversible path, no heat transfer (Q = 0), no "
            "change of kinetic or potential energy.",
            "<b>Model:</b> સંપૂર્ણ insulated cylinder માં ideal gas, reversible તથા adiabatic રીતે "
            "compress થાય છે. <b>Assumptions:</b> c<sub>v</sub> તથા c<sub>p</sub> અચળ હોય તેવો ideal "
            "gas, reversible path, heat transfer નહીં (Q = 0), kinetic કે potential energy નો ફેરફાર નહીં."),
        steps=[
            (bi("Start from the first law for a closed system and set Q = 0 for an adiabatic path.",
                "closed system માટે પ્રથમ નિયમ થી શરૂ કરો અને adiabatic રસ્તા માટે Q = 0 મૂકો."),
             E("δQ − δW = dU   ⇒   −P dV = m c_v dT", r"-P\,dV=m c_v\,dT")),
            (bi("Write the ideal-gas law for the same mass and differentiate it at constant mass.",
                "એ જ mass માટે ideal-gas law લખો અને અચળ mass પર તેનું differential લો."),
             E("P V = m R T   ⇒   P dV + V dP = m R dT", r"P\,dV+V\,dP=mR\,dT")),
            (bi("Eliminate dT between the two equations to get a relation between P and V alone.",
                "બંને સમીકરણો વચ્ચે dT દૂર કરો જેથી ફક્ત P તથા V વચ્ચેનો સંબંધ મળે."),
             E("m R dT = (R/c_v)(−P dV)   ⇒   P dV + V dP = −(R/c_v) P dV", r"P\,dV+V\,dP=-\frac{R}{c_v}P\,dV")),
            (bi("Collect the P dV terms. Use R/c_v = γ − 1, which follows from c_p − c_v = R and "
                "γ = c_p/c_v.",
                "P dV ના પદ એકઠાં કરો. R/c_v = γ − 1 વાપરો, જે c_p − c_v = R તથા γ = c_p/c_v પરથી મળે."),
             E("V dP = −γ P dV", r"V\,dP=-\gamma P\,dV")),
            (bi("Separate the variables so that P is with dP and V is with dV.",
                "Variables અલગ કરો જેથી P સાથે dP અને V સાથે dV રહે."),
             E("dP / P = −γ dV / V", r"\frac{dP}{P}=-\gamma\frac{dV}{V}")),
            (bi("Integrate between states 1 and 2 with γ constant.",
                "γ અચળ રાખીને state 1 તથા 2 વચ્ચે integrate કરો."),
             E("ln(P₂/P₁) = −γ ln(V₂/V₁)", r"\ln\frac{P_2}{P_1}=-\gamma\ln\frac{V_2}{V_1}")),
            (bi("Take the exponential of both sides and rearrange to the standard form.",
                "બંને બાજુ exponential લો અને પ્રમાણભૂત સ્વરૂપમાં ગોઠવો."),
             E("P₁ V₁^γ = P₂ V₂^γ  ⇒  P V^γ = constant", r"PV^\gamma=\text{const}")),
        ],
        final=E("P V^γ = c        T V^(γ−1) = c        T / P^((γ−1)/γ) = c",
                r"PV^\gamma=c"),
        diagram="d3_ideal_processes",
    ),
]

# =============================================================== 3.5 real gases
S6 = [
    theory(
        "3.6",
        bi("Equations of state for real gases", "વાસ્તવિક gases માટે equations of state"),
        definition=bi(
            "A <b>real gas</b> deviates from P V = n R T because its molecules have finite "
            "volume and attract one another. The deviation is measured by the "
            "<b>compressibility factor Z = P V / n R T</b>, which equals 1 for an ideal gas and "
            "departs from 1 as pressure rises or as the temperature approaches the critical "
            "temperature.",
            "<b>વાસ્તવિક gas</b> P V = n R T થી વિચલિત થાય છે કારણ કે તેના molecules નું ચોક્કસ volume "
            "હોય છે અને એકબીજાને આકર્ષે છે. વિચલન <b>compressibility factor Z = P V / n R T</b> થી "
            "મપાય છે, જે ideal gas માટે 1 થાય અને pressure વધતાં કે temperature critical temperature "
            "ની નજીક આવતાં 1 થી દૂર જાય."),
        theory_text=bi(
            "Two corrections explain the shape of the Z curve. At moderate pressure the "
            "<b>attraction</b> between molecules pulls them closer than ideal, so the volume is "
            "smaller and Z falls below 1. At high pressure the molecules' own <b>volume</b> "
            "leaves less free space, so Z rises above 1. At very low pressure both effects "
            "vanish and Z → 1, which is why the ideal-gas law works so well near atmospheric "
            "conditions.<br><br>"
            "Three tools are used in practice. The <b>Van der Waals equation</b> "
            "(P + a/V²)(V − b) = R T applies the two corrections explicitly and is the basis of "
            "every later cubic equation. The <b>virial equation</b> Z = 1 + B/V + C/V² + … "
            "expands Z in powers of volume with experimentally fitted coefficients. The "
            "<b>compressibility chart</b> uses the principle of corresponding states: all gases "
            "obey nearly the same Z curve when plotted against reduced pressure and temperature, "
            "so one chart serves every gas.",
            "Z curve નો આકાર બે corrections સમજાવે છે. મધ્યમ pressure પર molecules વચ્ચેનું "
            "<b>attraction</b> તેમને ideal કરતાં નજીક ખેંચે છે, તેથી volume નાનું થાય અને Z 1 થી નીચે જાય. "
            "ઊંચા pressure પર molecules નું પોતાનું <b>volume</b> ઓછી ખાલી જગ્યા છોડે છે, તેથી Z 1 થી ઉપર "
            "જાય. ખૂબ નીચા pressure પર બંને અસરો જતી રહે અને Z → 1 થાય, એટલે જ atmospheric conditions ની "
            "નજીક ideal-gas law ખૂબ સારી કામ કરે છે.<br><br>"
            "વ્યવહારમાં ત્રણ સાધનો વપરાય છે. <b>Van der Waals equation</b> (P + a/V²)(V − b) = R T "
            "બંને corrections સ્પષ્ટ લાગુ કરે છે અને પછીના દરેક cubic equation નો પાયો છે. "
            "<b>virial equation</b> Z = 1 + B/V + C/V² + … Z ને volume ની ઘાતોમાં વિસ્તારે છે અને તેના "
            "coefficients પ્રયોગથી મળે છે. <b>compressibility chart</b> corresponding states ના સિદ્ધાંત "
            "વાપરે છે: બધા gases reduced pressure તથા temperature સામે દોરતાં લગભગ એ જ Z curve પાળે છે, "
            "તેથી એક જ chart દરેક gas માટે કામ લાગે છે."),
        equations=[E("Z = P V / n R T", r"Z=\frac{PV}{nRT}"),
                   E("Van der Waals:  (P + a/V²)(V − b) = R T", r"\left(P+\frac{a}{V^2}\right)(V-b)=RT"),
                   E("virial:  Z = 1 + B/V + C/V² + …   or   Z = 1 + B′P + C′P² + …", r"Z=1+\frac{B}{V}+\frac{C}{V^2}"),
                   E("critical constants:  a = 27R²Tc²/(64Pc) ,  b = RTc/(8Pc)", r"a=\frac{27R^2T_c^2}{64P_c}")],
        list_items=[
            "<b>Van der Waals constants:</b> a measures attraction (large for polar gases), b measures molecular volume.",
            "<b>Critical constants from a and b:</b> Tc = 8a/(27Rb), Pc = a/(27b²), Vc = 3b.",
            "<b>Virial:</b> B is the second virial coefficient, negative at low temperature (attraction dominates) and positive at high temperature.",
            "<b>Corresponding states:</b> all gases have Z ≈ 1 when Tr is large, so the chart is used mainly for 0.8 < Tr < 3.",
        ],
        diagram="d3_compressibility",
        qualification=bi(
            "The Van der Waals equation is qualitative, not accurate: it predicts the critical "
            "compressibility factor Z<sub>c</sub> = 3/8 = 0.375 for every gas, whereas real gases "
            "range from about 0.23 to 0.29. It is used to explain behaviour and to introduce "
            "cubic equations, not to size equipment.",
            "Van der Waals equation ગુણાત્મક છે, સચોટ નથી: તે દરેક gas માટે critical compressibility "
            "factor Z<sub>c</sub> = 3/8 = 0.375 આપે છે, જ્યારે વાસ્તવિક gases લગભગ 0.23 થી 0.29 સુધી "
            "હોય છે. તેનો ઉપયોગ વર્તન સમજાવવા તથા cubic equations નો પરિચય આપવા માટે થાય, equipment નું "
            "size નક્કી કરવા માટે નહીં."),
    ),
]

# =============================================================== numericals
N1 = numerical(
    "N1",
    bi("Ideal-gas law: volume of a gas at given conditions",
       "ideal-gas law: આપેલી શરતો પર gas નું volume"),
    given=bi("3 kmol of an ideal gas is held at 4 bar and 320 K. R = 8.314 kJ/kmol·K.",
             "3 kmol ideal gas 4 bar તથા 320 K પર રખાય છે. R = 8.314 kJ/kmol·K."),
    find=bi("The volume occupied by the gas.",
            "Gas દ્વારા રોકાયેલું volume."),
    formula=[E("P V = n R T  ⇒  V = n R T / P", r"V=\frac{nRT}{P}")],
    substitution=bi(
        "P = 4 bar = 400 kPa. V = 3 × 8.314 × 320 / 400 = 7 981.4 / 400 = 19.95 m³.",
        "P = 4 bar = 400 kPa. V = 3 × 8.314 × 320 / 400 = 7 981.4 / 400 = 19.95 m³."),
    answer=bi("V = 19.95 m³ ≈ 20 m³.", "V = 19.95 m³ ≈ 20 m³."),
    check=bi("One kmol at 320 K and 4 bar should occupy about 22.4 × (320/273) × (1/4) ≈ "
             "6.6 m³, so three kmol give about 20 m³ — the answer is the right order.",
             "320 K તથા 4 bar પર એક kmol લગભગ 22.4 × (320/273) × (1/4) ≈ 6.6 m³ રોકે, તેથી ત્રણ kmol "
             "લગભગ 20 m³ આપે — જવાબ સાચો ક્રમ છે."),
)

N2 = numerical(
    "N2",
    bi("Adiabatic compression with the PV^γ relation",
       "PV^γ સંબંધ સાથે adiabatic compression"),
    given=bi("2 kg of air at 1 bar and 300 K is compressed adiabatically and reversibly to "
             "8 bar. γ = 1.4, R = 0.287 kJ/kg·K, c_v = 0.718 kJ/kg·K.",
             "1 bar તથા 300 K પરની 2 kg હવા 8 bar સુધી adiabatic તથા reversible રીતે compress થાય છે. "
             "γ = 1.4, R = 0.287 kJ/kg·K, c_v = 0.718 kJ/kg·K."),
    find=bi("Final temperature, work input and heat transfer.",
            "અંતિમ temperature, work input તથા heat transfer."),
    formula=[E("T₂ = T₁ (P₂/P₁)^((γ−1)/γ)", r"T_2=T_1\left(\frac{P_2}{P_1}\right)^{\frac{\gamma-1}{\gamma}}"),
             E("W = m R (T₁ − T₂)/(γ − 1)      Q = 0", r"W=\frac{mR(T_1-T_2)}{\gamma-1}")],
    substitution=bi(
        "(γ−1)/γ = 0.2857. T₂ = 300 × 8^0.2857 = 300 × 1.811 = 543.3 K. "
        "W = 2 × 0.287 × (300 − 543.3)/0.4 = 0.574 × (−243.3)/0.4 = −349.1 kJ. "
        "The negative sign means 349.1 kJ of work is supplied.",
        "(γ−1)/γ = 0.2857. T₂ = 300 × 8^0.2857 = 300 × 1.811 = 543.3 K. "
        "W = 2 × 0.287 × (300 − 543.3)/0.4 = 0.574 × (−243.3)/0.4 = −349.1 kJ. "
        "ઋણ ચિહ્ન એટલે 349.1 kJ work આપવું પડે."),
    answer=bi("T₂ = 543 K;  W = −349.1 kJ (work input);  Q = 0;  ΔU = +349.1 kJ.",
              "T₂ = 543 K;  W = −349.1 kJ (work input);  Q = 0;  ΔU = +349.1 kJ."),
    check=bi("Check with ΔU: m c_v ΔT = 2 × 0.718 × 243.3 = 349.3 kJ, which matches the work "
             "within rounding — as it must, because Q = 0 means all the work becomes internal "
             "energy.",
             "ΔU થી ચકાસો: m c_v ΔT = 2 × 0.718 × 243.3 = 349.3 kJ, જે round-off ની અંદર work સાથે "
             "મળે — એ જરૂરી છે, કારણ કે Q = 0 એટલે આખું work internal energy બને."),
)

N3 = numerical(
    "N3",
    bi("Compressibility factor and real volume",
       "compressibility factor તથા વાસ્તવિક volume"),
    given=bi("Carbon dioxide at 310 K and 70 bar. Tc = 304.2 K, Pc = 73.8 bar. "
             "The compressibility chart gives Z ≈ 0.72 at these reduced conditions. "
             "R = 0.1889 kJ/kg·K.",
             "310 K તથા 70 bar પર carbon dioxide. Tc = 304.2 K, Pc = 73.8 bar. આ reduced શરતો પર "
             "compressibility chart Z ≈ 0.72 આપે છે. R = 0.1889 kJ/kg·K."),
    find=bi("Reduced properties, Z, and the actual specific volume compared with the ideal value.",
            "Reduced properties, Z, તથા વાસ્તવિક specific volume ની ideal કિંમત સાથે સરખામણી."),
    formula=[E("T_r = T / T_c ,   P_r = P / P_c", r"T_r=\frac{T}{T_c}"),
             E("v = Z R T / P", r"v=\frac{ZRT}{P}")],
    substitution=bi(
        "T_r = 310/304.2 = 1.019;  P_r = 70/73.8 = 0.949. "
        "Ideal volume: v_ideal = 0.1889 × 310/7 000 = 8.366 × 10⁻³ m³/kg. "
        "Actual: v = 0.72 × 8.366 × 10⁻³ = 6.02 × 10⁻³ m³/kg.",
        "T_r = 310/304.2 = 1.019;  P_r = 70/73.8 = 0.949. "
        "Ideal volume: v_ideal = 0.1889 × 310/7 000 = 8.366 × 10⁻³ m³/kg. "
        "Actual: v = 0.72 × 8.366 × 10⁻³ = 6.02 × 10⁻³ m³/kg."),
    answer=bi("T_r = 1.02, P_r = 0.95, Z = 0.72;  v = 6.02 × 10⁻³ m³/kg, about 28 % below the "
              "ideal value.",
              "T_r = 1.02, P_r = 0.95, Z = 0.72;  v = 6.02 × 10⁻³ m³/kg, ideal કરતાં લગભગ 28 % ઓછું."),
    check=bi("Tr ≈ 1 means the gas is close to its critical temperature, where Z is far from 1; "
             "had we used the ideal-gas law the volume would be over-estimated by 39 %. This is "
             "why CO₂ near 31 °C is a poor ideal gas but an excellent dense solvent.",
             "Tr ≈ 1 એટલે gas પોતાના critical temperature ની નજીક છે, જ્યાં Z 1 થી ઘણું દૂર હોય; "
             "ideal-gas law વાપર્યું હોત તો volume 39 % વધારે આવત. એટલે જ 31 °C ની નજીક CO₂ નબળો ideal "
             "gas છે પણ ઉત્તમ dense solvent છે."),
)

N4 = numerical(
    "N4",
    bi("Van der Waals equation for one mole",
       "એક mole માટે Van der Waals equation"),
    given=bi("One mole of a gas occupies 0.5 L at 300 K. For the gas, a = 3.592 bar·L²/mol² and "
             "b = 0.042 67 L/mol. R = 0.083 14 bar·L/mol·K.",
             "એક mole gas 300 K પર 0.5 L રોકે છે. gas માટે a = 3.592 bar·L²/mol² તથા "
             "b = 0.042 67 L/mol. R = 0.083 14 bar·L/mol·K."),
    find=bi("The pressure from the ideal-gas law and from the Van der Waals equation.",
            "ideal-gas law તથા Van der Waals equation થી pressure."),
    formula=[E("ideal:  P = R T / V", r"P=\frac{RT}{V}"),
             E("Van der Waals:  P = R T/(V − b) − a/V²", r"P=\frac{RT}{V-b}-\frac{a}{V^2}")],
    substitution=bi(
        "Ideal: P = 0.083 14 × 300/0.5 = 49.88 bar. "
        "Van der Waals: V − b = 0.5 − 0.042 67 = 0.457 33 L. "
        "R T/(V − b) = 24.942/0.457 33 = 54.54 bar. a/V² = 3.592/0.25 = 14.37 bar. "
        "P = 54.54 − 14.37 = 40.17 bar.",
        "Ideal: P = 0.083 14 × 300/0.5 = 49.88 bar. "
        "Van der Waals: V − b = 0.5 − 0.042 67 = 0.457 33 L. "
        "R T/(V − b) = 24.942/0.457 33 = 54.54 bar. a/V² = 3.592/0.25 = 14.37 bar. "
        "P = 54.54 − 14.37 = 40.17 bar."),
    answer=bi("P_ideal = 49.9 bar;  P_vdW = 40.2 bar — the ideal law over-predicts by about 24 %.",
              "P_ideal = 49.9 bar;  P_vdW = 40.2 bar — ideal law લગભગ 24 % વધારે આપે છે."),
    check=bi("The two corrections pull in opposite directions: the volume correction (V − b) "
             "raises the pressure, the attraction term (a/V²) lowers it, and here attraction "
             "wins. At this density the gas is far from ideal, which is the expected conclusion "
             "for half a litre per mole.",
             "બંને corrections વિરુદ્ધ દિશામાં ખેંચે છે: volume correction (V − b) pressure વધારે છે, "
             "attraction પદ (a/V²) ઘટાડે છે, અને અહીં attraction જીતે છે. આ density પર gas ideal થી ઘણું "
             "દૂર છે, જે પ્રતિ mole અડધા લિટર માટે અપેક્ષિત નિષ્કર્ષ છે."),
)

N5 = numerical(
    "N5",
    bi("Polytropic compression of air",
       "હવાનું polytropic compression"),
    given=bi("1.5 kg of air is compressed from 1 bar, 290 K to 6 bar according to "
             "P V^1.25 = constant. R = 0.287 kJ/kg·K, c_v = 0.718 kJ/kg·K, γ = 1.4.",
             "1.5 kg હવા 1 bar, 290 K થી 6 bar સુધી P V^1.25 = અચળ પ્રમાણે compress થાય છે. "
             "R = 0.287 kJ/kg·K, c_v = 0.718 kJ/kg·K, γ = 1.4."),
    find=bi("Final temperature, work input, heat transfer and the polytropic index check.",
            "અંતિમ temperature, work input, heat transfer તથા polytropic index ની ચકાસણી."),
    formula=[E("T₂ = T₁ (P₂/P₁)^((n−1)/n)", r"T_2=T_1\left(\frac{P_2}{P_1}\right)^{\frac{n-1}{n}}"),
             E("W = m R (T₁ − T₂)/(n − 1)", r"W=\frac{mR(T_1-T_2)}{n-1}"),
             E("Q = m c_v (T₂ − T₁)(γ − n)/(γ − 1)", r"Q=mc_v(T_2-T_1)\frac{\gamma-n}{\gamma-1}")],
    substitution=bi(
        "(n−1)/n = 0.25/1.25 = 0.2. T₂ = 290 × 6^0.2 = 290 × 1.431 = 415.0 K. "
        "W = 1.5 × 0.287 × (290 − 415)/0.25 = 0.4305 × (−125)/0.25 = −215.3 kJ. "
        "Q = 1.5 × 0.718 × 125 × (1.4 − 1.25)/0.4 = 1.077 × 125 × 0.375 = −50.5 kJ.",
        "(n−1)/n = 0.25/1.25 = 0.2. T₂ = 290 × 6^0.2 = 290 × 1.431 = 415.0 K. "
        "W = 1.5 × 0.287 × (290 − 415)/0.25 = 0.4305 × (−125)/0.25 = −215.3 kJ. "
        "Q = 1.5 × 0.718 × 125 × (1.4 − 1.25)/0.4 = 1.077 × 125 × 0.375 = −50.5 kJ."),
    answer=bi("T₂ = 415 K;  work input = 215.3 kJ;  heat rejected ≈ 50.5 kJ. Since 1 < n < γ, "
              "the gas is cooled during compression as well as compressed.",
              "T₂ = 415 K;  work input = 215.3 kJ;  heat rejected ≈ 50.5 kJ. 1 < n < γ હોવાથી "
              "compress થતાં gas ઠંડું પણ થાય છે."),
    check=bi("Check with the first law: ΔU = m c_v ΔT = 1.5 × 0.718 × 125 = 134.6 kJ. "
             "Q − W = −50.5 − (−215.3) = 164.8 kJ, which should equal ΔU. The gap is rounding "
             "in c_v; use c_v = R/(γ − 1) = 0.7175 for exact agreement.",
             "પ્રથમ નિયમ થી ચકાસો: ΔU = m c_v ΔT = 1.5 × 0.718 × 125 = 134.6 kJ. "
             "Q − W = −50.5 − (−215.3) = 164.8 kJ, જે ΔU જેટલું હોવું જોઈએ. તફાવત c_v માં round-off નો "
             "છે; બરાબર મેળ માટે c_v = R/(γ − 1) = 0.7175 વાપરો."),
)

# =============================================================== viva
VIVA = [
    viva(bi("Explain PVT behaviour of a pure fluid and state how many properties fix its state.",
            "pure fluid નું PVT વર્તન સમજાવો અને કેટલી properties તેની state નક્કી કરે તે જણાવો."),
         bi("PVT behaviour is the relation between pressure, volume and temperature. For a pure "
            "fluid in a single phase only two of the three are independent (F = 2), so fixing "
            "any two fixes the third through an equation of state or a table.",
            "PVT વર્તન એ pressure, volume તથા temperature વચ્ચેનો સંબંધ છે. single phase માં pure fluid "
            "માટે ત્રણમાંથી ફક્ત બે સ્વતંત્ર હોય (F = 2), તેથી કોઈપણ બે નિશ્ચિત કરતાં ત્રીજું equation of "
            "state કે table દ્વારા નિશ્ચિત થાય.")),
    viva(bi("Draw and explain the P–V diagram of a pure substance.",
            "pure substance નું P–V diagram દોરો અને સમજાવો."),
         bi("Isotherms below Tc show a flat plateau where liquid and vapour coexist. The plateau "
            "shortens as T rises and vanishes at the critical point. Above Tc the isotherm is "
            "continuous — no phase change. The dome joins all plateau ends.",
            "Tc થી નીચે isotherms સપાટ plateau દર્શાવે છે જ્યાં liquid તથા vapour સાથે રહે છે. T વધતાં "
            "plateau ટૂંકું થાય અને critical point પર અદૃશ્ય થાય. Tc ઉપર isotherm સતત હોય — phase change "
            "નહીં. dome બધા plateau ના છેડા જોડે છે.")),
    viva(bi("State the ideal-gas law and the conditions under which it applies.",
            "ideal-gas law જણાવો અને તે કઈ શરતોમાં લાગુ પડે તે જણાવો."),
         bi("P V = n R T. It applies at low pressure and high temperature, where molecular volume "
            "and intermolecular attraction are negligible. It fails near the critical point and "
            "near saturation.",
            "P V = n R T. તે નીચા pressure તથા ઊંચા temperature પર લાગુ પડે છે, જ્યાં molecular volume "
            "તથા intermolecular attraction નગણ્ય હોય. critical point તથા saturation ની નજીક તે નિષ્ફળ જાય.")),
    viva(bi("What is a polytropic process? What do n = 0, 1, γ and ∞ represent?",
            "polytropic process શું છે? n = 0, 1, γ તથા ∞ શું દર્શાવે છે?"),
         bi("A process following P V^n = constant. n = 0 is isobaric, n = 1 is isothermal, "
            "n = γ is adiabatic and n → ∞ is isochoric. Real compression usually has "
            "n between 1.2 and 1.35.",
            "P V^n = અચળ પાળતી પ્રક્રિયા. n = 0 isobaric, n = 1 isothermal, n = γ adiabatic અને "
            "n → ∞ isochoric. વાસ્તવિક compression માં n સામાન્ય રીતે 1.2 થી 1.35 હોય છે.")),
    viva(bi("Why is an adiabatic curve steeper than an isothermal curve?",
            "adiabatic curve isothermal કરતાં ઢોળાવવાળો કેમ હોય છે?"),
         bi("On an adiabatic path no heat enters, so the work comes out of internal energy and "
            "the temperature falls as the gas expands. The isothermal path keeps T constant by "
            "taking in heat. Since γ > 1 the adiabatic relation P V^γ = c falls faster than "
            "P V = c.",
            "adiabatic રસ્તા પર કોઈ heat અંદર આવતી નથી, તેથી work internal energy માંથી આવે અને gas "
            "expand થતાં temperature ઘટે. isothermal રસ્તો heat લઈને T અચળ રાખે. γ > 1 હોવાથી "
            "P V^γ = c એ P V = c કરતાં ઝડપથી ઘટે છે.")),
    viva(bi("Define compressibility factor Z and explain why it can be less or greater than 1.",
            "compressibility factor Z ની વ્યાખ્યા આપો અને તે 1 થી ઓછું કે વધુ કેમ હોઈ શકે તે સમજાવો."),
         bi("Z = P V / n R T. Below 1 when intermolecular attraction dominates and the volume is "
            "smaller than ideal; above 1 when molecular volume dominates at high pressure. Z → 1 "
            "as P → 0.",
            "Z = P V / n R T. intermolecular attraction પ્રભાવી હોય અને volume ideal કરતાં નાનું હોય ત્યારે "
            "1 થી નીચે; ઊંચા pressure પર molecular volume પ્રભાવી હોય ત્યારે 1 થી ઉપર. P → 0 થતાં Z → 1.")),
    viva(bi("Write the Van der Waals equation and state the meaning of a and b.",
            "Van der Waals equation લખો અને a તથા b નો અર્થ જણાવો."),
         bi("(P + a/V²)(V − b) = R T. The constant a corrects for intermolecular attraction and "
            "b for the finite volume occupied by the molecules themselves.",
            "(P + a/V²)(V − b) = R T. a અચળ intermolecular attraction સુધારે છે અને b molecules દ્વારા "
            "રોકાયેલા ચોક્કસ volume માટે.")),
    viva(bi("What is the principle of corresponding states?",
            "corresponding states નો સિદ્ધાંત શું છે?"),
         bi("All gases obey nearly the same compressibility relation when expressed in reduced "
            "coordinates Pr = P/Pc and Tr = T/Tc. One generalised chart therefore serves every "
            "gas, which is why the compressibility chart is universal.",
            "બધા gases reduced coordinates Pr = P/Pc તથા Tr = T/Tc માં લખતાં લગભગ એ જ compressibility "
            "સંબંધ પાળે છે. તેથી એક generalised chart દરેક gas માટે કામ લાગે, એટલે જ compressibility "
            "chart સાર્વત્રિક છે.")),
]

# =============================================================== exam
EXAM = [
    exam(bi("Explain the PVT behaviour of a pure substance with the help of P–V and P–T "
            "diagrams. Mark the triple point and the critical point.",
            "P–V તથા P–T diagrams ની મદદથી pure substance નું PVT વર્તન સમજાવો. triple point તથા "
            "critical point દર્શાવો."), 4),
    exam(bi("State the ideal-gas law and explain its limitations. Why does it fail near the "
            "critical point?", "ideal-gas law જણાવો અને તેની મર્યાદાઓ સમજાવો. critical point ની નજીક "
            "તે કેમ નિષ્ફળ જાય?"), 4),
    exam(bi("Derive P V^γ = constant for a reversible adiabatic process of an ideal gas, "
            "stating the assumptions.",
            "ideal gas ની reversible adiabatic પ્રક્રિયા માટે P V^γ = અચળ મેળવો અને assumptions જણાવો."), 4),
    exam(bi("Draw the five ideal-gas processes on a P–V diagram and give the work done and heat "
            "transferred for each.",
            "P–V diagram પર પાંચ ideal-gas પ્રક્રિયાઓ દોરો અને દરેક માટે થયેલું work તથા heat આપો."), 4),
    exam(bi("Explain the deviation of real gases from ideal behaviour. Define Z and explain why "
            "it can be less or greater than 1.",
            "વાસ્તવિક gases નું ideal વર્તનથી વિચલન સમજાવો. Z વ્યાખ્યાયિત કરો અને તે 1 થી ઓછું કે વધુ "
            "કેમ હોઈ શકે તે સમજાવો."), 4),
    exam(bi("Write the Van der Waals equation and explain its constants. Show that it reduces to "
            "the ideal-gas law at low pressure.",
            "Van der Waals equation લખો અને તેના constants સમજાવો. નીચા pressure પર તે ideal-gas law "
            "માં કેમ ફેરવાય તે દર્શાવો."), 4),
    exam(bi("Write the virial equation and explain the significance of the second virial "
            "coefficient.",
            "virial equation લખો અને second virial coefficient નું મહત્વ સમજાવો."), 4),
    exam(bi("What is a generalised compressibility chart? Explain the principle of corresponding "
            "states and the procedure for using the chart.",
            "generalised compressibility chart શું છે? corresponding states નો સિદ્ધાંત તથા chart "
            "વાપરવાની રીત સમજાવો."), 4),
    exam(bi("3 kmol of an ideal gas is held at 4 bar and 320 K. Calculate its volume. "
            "R = 8.314 kJ/kmol·K.",
            "3 kmol ideal gas 4 bar તથા 320 K પર છે. તેનું volume ગણો. R = 8.314 kJ/kmol·K."), 4),
    exam(bi("2 kg of air at 1 bar, 300 K is compressed adiabatically and reversibly to 8 bar. "
            "Find T₂ and the work input. γ = 1.4, R = 0.287 kJ/kg·K.",
            "1 bar, 300 K પરની 2 kg હવા 8 bar સુધી adiabatic તથા reversible રીતે compress થાય છે. "
            "T₂ તથા work input શોધો. γ = 1.4, R = 0.287 kJ/kg·K."), 4),
    exam(bi("CO₂ at 310 K and 70 bar has Tc = 304.2 K and Pc = 73.8 bar. Find the reduced "
            "properties, and using Z = 0.72 calculate the specific volume and compare it with the "
            "ideal value.",
            "310 K તથા 70 bar પર CO₂ માટે Tc = 304.2 K તથા Pc = 73.8 bar છે. Reduced properties શોધો "
            "અને Z = 0.72 વાપરીને specific volume ગણો તથા ideal કિંમત સાથે સરખાવો."), 4),
    exam(bi("1.5 kg of air is compressed from 1 bar, 290 K to 6 bar following P V^1.25 = "
            "constant. Calculate T₂, the work input and the heat transfer.",
            "1.5 kg હવા 1 bar, 290 K થી 6 bar સુધી P V^1.25 = અચળ પ્રમાણે compress થાય છે. T₂, work "
            "input તથા heat transfer ગણો."), 4),
]

# =============================================================== formulae
SYNTAX = [
    {"title": bi("Ideal-gas relations", "ideal-gas સંબંધો"),
     "items": [
         {"title": bi("Equation of state", "Equation of state"),
          "f": "P V = n R T;  P v = R T;  P V = m R T",
          "terms": "Absolute pressure and absolute temperature only."},
         {"title": bi("Gas constant", "Gas constant"),
          "f": "R = 8.314 kJ/kmol·K = 0.287 kJ/kg·K (air);  R_u = M R",
          "terms": "Molar and specific forms differ by the molar mass."},
         {"title": bi("Standard volume", "Standard volume"),
          "f": "22.414 m³/kmol at 1 atm, 0 °C;  22.71 m³/kmol at 1 bar, 0 °C",
          "terms": "Handy for converting a gas flow to a molar flow."},
     ]},
    {"title": bi("Process relations (ideal gas)", "પ્રક્રિયા સંબંધો (ideal gas)"),
     "items": [
         {"title": bi("Polytropic", "Polytropic"),
          "f": "P V^n = c;  W = mR(T₁ − T₂)/(n − 1);  Q = m c_v (T₂ − T₁)(γ − n)/(γ − 1)",
          "terms": "Covers isobaric, isothermal, adiabatic and isochoric as special cases."},
         {"title": bi("Isothermal (n = 1)", "Isothermal (n = 1)"),
          "f": "W = Q = m R T ln(V₂/V₁) = m R T ln(P₁/P₂)",
          "terms": "Denominator n − 1 vanishes, so use the logarithmic form."},
         {"title": bi("Adiabatic", "Adiabatic"),
          "f": "T₂/T₁ = (P₂/P₁)^((γ−1)/γ);  P V^γ = c;  T V^(γ−1) = c",
          "terms": "Q = 0, so W = −ΔU = m c_v (T₁ − T₂)."},
     ]},
    {"title": bi("Real-gas relations", "વાસ્તવિક-gas સંબંધો"),
     "items": [
         {"title": bi("Compressibility factor", "Compressibility factor"),
          "f": "Z = P V / n R T;  V = Z n R T / P",
          "terms": "Read Z from the chart using Pr and Tr."},
         {"title": bi("Reduced coordinates", "Reduced coordinates"),
          "f": "P_r = P/P_c;  T_r = T/T_c;  V_r = V/V_c",
          "terms": "Principle of corresponding states: all gases collapse onto one chart."},
         {"title": bi("Van der Waals", "Van der Waals"),
          "f": "(P + a/V²)(V − b) = R T;  Tc = 8a/(27Rb);  Pc = a/(27b²)",
          "terms": "Predicts Zc = 3/8 for every gas, so use it qualitatively."},
         {"title": bi("Virial", "Virial"),
          "f": "Z = 1 + B/V + C/V² + …",
          "terms": "B negative at low T (attraction), positive at high T."},
     ]},
]

# =============================================================== build
def build() -> Unit:
    u = Unit(CODE, 3, TITLE, hours=10, weightage=22,
             tabs=["notes", "programs", "diagrams", "syntax", "viva", "exam"],
             tab_labels={"programs": bi("Solved numericals", "ઉકેલેલા દાખલા"),
                         "syntax": bi("Formulae and conversions", "સૂત્રો તથા conversions")})
    u.section(bi("3.1  PVT behaviour and the P–V / P–T diagrams",
                 "3.1  PVT વર્તન તથા P–V / P–T diagrams"), S1)
    u.section(bi("3.2  The P–T diagram, triple and critical points",
                 "3.2  P–T diagram, triple તથા critical points"), S2)
    u.section(bi("3.3  Ideal gas and the equation of state",
                 "3.3  Ideal gas તથા equation of state"), S3)
    u.section(bi("3.4  Ideal-gas processes and the adiabatic relation",
                 "3.4  Ideal-gas પ્રક્રિયાઓ તથા adiabatic સંબંધ"), S4)
    u.section(bi("3.5  Equations of state for real gases",
                 "3.5  વાસ્તવિક gases માટે equations of state"), S6)
    u.data["programs"] = [N1, N2, N3, N4, N5]
    u.diagram("d3_pv_diagram",
              bi("The P–V diagram of a pure substance", "pure substance નું P–V diagram"),
              "diagrams/d3_pv_diagram.svg")
    u.diagram("d3_ideal_processes",
              bi("The five ideal-gas processes on a P–V diagram",
                 "P–V diagram પર પાંચ ideal-gas પ્રક્રિયાઓ"),
              "diagrams/d3_ideal_processes.svg")
    u.diagram("d3_compressibility",
              bi("Generalised compressibility chart", "generalised compressibility chart"),
              "diagrams/d3_compressibility.svg")
    u.diagram("d3_real_gas_z",
              bi("Why real gases deviate: the compressibility factor Z",
                 "વાસ્તવિક gases કેમ વિચલિત થાય: compressibility factor Z"),
              "diagrams/d3_real_gas_z.svg")
    for s in SYNTAX:
        u.data.setdefault("syntax", []).append(s)
    u.data["viva"] = VIVA
    u.data["exam_questions"] = EXAM
    return u


if __name__ == "__main__":
    unit = build()
    problems = unit.validate()
    out = unit.write("content/chemical/sem4/DI04005041/unit3.json")
    print("wrote", out)
    print("problems:", problems or "none")
