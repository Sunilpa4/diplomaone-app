"""Basics of Electronics (DI01000151) - Unit 2 extras: numericals, equations, viva, exam questions"""


def N(id_, q_en, q_gu, a_en, a_gu):
    return {"id": id_, "q": {"en": q_en, "gu": q_gu}, "a": {"en": a_en, "gu": a_gu}}


NUMERICALS = [
    N("u2n1",
      "Find the intrinsic conductivity and resistivity of pure silicon at 300 K. Given: nᵢ = 1.5 × 10¹⁰ /cm³, μₙ = 1350 cm²/V·s, μₚ = 480 cm²/V·s.",
      "300 K પર શુદ્ધ silicon ની intrinsic conductivity અને resistivity શોધો. આપેલ: nᵢ = 1.5 × 10¹⁰ /cm³, μₙ = 1350 cm²/V·s, μₚ = 480 cm²/V·s.",
      """<p><b>Formula:</b> σᵢ = q nᵢ (μₙ + μₚ)</p>
<p>σᵢ = 1.6 × 10⁻¹⁹ × 1.5 × 10¹⁰ × (1350 + 480)</p>
<p>= 2.4 × 10⁻⁹ × 1830 = <b>4.39 × 10⁻⁶ S/cm</b></p>
<p>Resistivity ρᵢ = 1 / σᵢ = 1 / (4.39 × 10⁻⁶) = <b>2.28 × 10⁵ Ω·cm</b> (≈ 2280 Ω·m)</p>
<p><i>Very high resistivity → pure Si is a poor conductor.</i></p>""",
      """<p><b>સૂત્ર:</b> σᵢ = q nᵢ (μₙ + μₚ)</p>
<p>σᵢ = 1.6 × 10⁻¹⁹ × 1.5 × 10¹⁰ × (1350 + 480)</p>
<p>= 2.4 × 10⁻⁹ × 1830 = <b>4.39 × 10⁻⁶ S/cm</b></p>
<p>Resistivity ρᵢ = 1 / σᵢ = 1 / (4.39 × 10⁻⁶) = <b>2.28 × 10⁵ Ω·cm</b> (≈ 2280 Ω·m)</p>
<p><i>ખૂબ વધુ resistivity → શુદ્ધ Si નબળો conductor છે.</i></p>"""),
    N("u2n2",
      "Silicon is doped with donor atoms N_D = 10¹⁶ /cm³. Find the electron and hole concentrations. (nᵢ = 1.5 × 10¹⁰ /cm³)",
      "Silicon ને donor atoms N_D = 10¹⁶ /cm³ થી doped કરેલ છે. Electron અને hole concentration શોધો. (nᵢ = 1.5 × 10¹⁰ /cm³)",
      """<p>It is an <b>N-type</b> semiconductor. All donor atoms are ionized at room temperature, so:</p>
<p>Electrons (majority): n ≈ N_D = <b>10¹⁶ /cm³</b></p>
<p>Holes (minority), from mass action law n × p = nᵢ²:</p>
<p>p = nᵢ² / n = (1.5 × 10¹⁰)² / 10¹⁶ = 2.25 × 10²⁰ / 10¹⁶ = <b>2.25 × 10⁴ /cm³</b></p>
<p><i>Holes are about 10¹² times fewer than electrons.</i></p>""",
      """<p>આ <b>N-type</b> semiconductor છે. Room temperature પર બધા donor atoms ionized થાય છે, તેથી:</p>
<p>Electrons (majority): n ≈ N_D = <b>10¹⁶ /cm³</b></p>
<p>Holes (minority), mass action law n × p = nᵢ² પરથી:</p>
<p>p = nᵢ² / n = (1.5 × 10¹⁰)² / 10¹⁶ = 2.25 × 10²⁰ / 10¹⁶ = <b>2.25 × 10⁴ /cm³</b></p>
<p><i>Holes, electrons કરતાં આશરે 10¹² ગણા ઓછા છે.</i></p>"""),
    N("u2n3",
      "Silicon has 5 × 10²² atoms/cm³. If it is doped at the rate of 1 impurity atom per 10⁸ silicon atoms, find the impurity concentration.",
      "Silicon માં 5 × 10²² atoms/cm³ છે. જો 10⁸ silicon atoms દીઠ 1 impurity atom ના દરે doping કરવામાં આવે, તો impurity concentration શોધો.",
      """<p>Impurity concentration = 5 × 10²² / 10⁸ = <b>5 × 10¹⁴ atoms/cm³</b></p>
<p>Each impurity atom gives one carrier, so the carriers added ≈ 5 × 10¹⁴ /cm³, which is about <b>33,000 times</b> the intrinsic concentration (1.5 × 10¹⁰ /cm³).</p>""",
      """<p>Impurity concentration = 5 × 10²² / 10⁸ = <b>5 × 10¹⁴ atoms/cm³</b></p>
<p>દરેક impurity atom એક carrier આપે છે, તેથી ઉમેરાયેલા carriers ≈ 5 × 10¹⁴ /cm³, જે intrinsic concentration (1.5 × 10¹⁰ /cm³) કરતાં આશરે <b>33,000 ગણા</b> છે.</p>"""),
    N("u2n4",
      "Find the conductivity of N-type silicon with N_D = 10¹⁶ /cm³ (μₙ = 1350 cm²/V·s). Compare it with intrinsic silicon (σᵢ = 4.39 × 10⁻⁶ S/cm).",
      "N_D = 10¹⁶ /cm³ વાળા N-type silicon ની conductivity શોધો (μₙ = 1350 cm²/V·s). Intrinsic silicon (σᵢ = 4.39 × 10⁻⁶ S/cm) સાથે સરખામણી કરો.",
      """<p>For N-type: σ ≈ q n μₙ</p>
<p>σ = 1.6 × 10⁻¹⁹ × 10¹⁶ × 1350 = <b>2.16 S/cm</b></p>
<p>Resistivity ρ = 1 / 2.16 = <b>0.463 Ω·cm</b></p>
<p>Ratio = 2.16 / (4.39 × 10⁻⁶) ≈ <b>4.9 × 10⁵</b> → doping increased conductivity about <b>5 lakh times</b>.</p>""",
      """<p>N-type માટે: σ ≈ q n μₙ</p>
<p>σ = 1.6 × 10⁻¹⁹ × 10¹⁶ × 1350 = <b>2.16 S/cm</b></p>
<p>Resistivity ρ = 1 / 2.16 = <b>0.463 Ω·cm</b></p>
<p>ગુણોત્તર = 2.16 / (4.39 × 10⁻⁶) ≈ <b>4.9 × 10⁵</b> → doping થી conductivity આશરે <b>5 લાખ ગણી</b> વધી.</p>"""),
]


def E(name_en, name_gu, f, terms_en, terms_gu):
    return {"name": {"en": name_en, "gu": name_gu}, "f": f, "terms": {"en": terms_en, "gu": terms_gu}}


EQUATIONS = [
    {"title": {"en": "Atomic Structure & Energy", "gu": "Atomic Structure અને Energy"}, "items": [
        E("Maximum electrons in a shell", "Shell માં મહત્તમ electrons", "N<sub>max</sub> = 2n²",
          "n = shell number (K = 1, L = 2, M = 3, N = 4) → 2, 8, 18, 32",
          "n = shell નંબર (K = 1, L = 2, M = 3, N = 4) → 2, 8, 18, 32"),
        E("Electron-volt", "Electron-volt", "1 eV = 1.6 × 10⁻¹⁹ J",
          "Unit of energy used for energy gap", "Energy gap માટે વપરાતો ઊર્જાનો એકમ"),
        E("Charge of electron", "Electron નો charge", "q = 1.6 × 10⁻¹⁹ C",
          "Hole has equal positive charge", "Hole નો સમાન positive charge હોય છે"),
        E("Energy gap values", "Energy gap ના મૂલ્યો", "E<sub>g</sub>(Si) = 1.1 eV, E<sub>g</sub>(Ge) = 0.7 eV",
          "Insulator > 5 eV; Conductor = 0 (bands overlap)", "Insulator > 5 eV; Conductor = 0 (bands overlap)"),
    ]},
    {"title": {"en": "Carriers & Conductivity", "gu": "Carriers અને Conductivity"}, "items": [
        E("Intrinsic semiconductor", "Intrinsic semiconductor", "n = p = n<sub>i</sub>",
          "nᵢ = intrinsic carrier concentration (Si ≈ 1.5 × 10¹⁰ /cm³ at 300 K)",
          "nᵢ = intrinsic carrier concentration (300 K પર Si ≈ 1.5 × 10¹⁰ /cm³)"),
        E("Mass action law", "Mass action law", "n × p = n<sub>i</sub>²",
          "Valid for intrinsic and extrinsic semiconductors at a fixed temperature",
          "નિશ્ચિત તાપમાને intrinsic અને extrinsic બંને semiconductors માટે લાગુ"),
        E("N-type carrier concentration", "N-type carrier concentration", "n ≈ N<sub>D</sub>,  p = n<sub>i</sub>² / N<sub>D</sub>",
          "N_D = donor concentration", "N_D = donor concentration"),
        E("P-type carrier concentration", "P-type carrier concentration", "p ≈ N<sub>A</sub>,  n = n<sub>i</sub>² / N<sub>A</sub>",
          "N_A = acceptor concentration", "N_A = acceptor concentration"),
        E("Conductivity of semiconductor", "Semiconductor ની conductivity", "σ = q (n μ<sub>n</sub> + p μ<sub>p</sub>)",
          "μₙ, μₚ = mobility of electrons and holes (cm²/V·s). Si: μₙ ≈ 1350, μₚ ≈ 480",
          "μₙ, μₚ = electrons અને holes ની mobility (cm²/V·s). Si: μₙ ≈ 1350, μₚ ≈ 480"),
        E("Intrinsic conductivity", "Intrinsic conductivity", "σ<sub>i</sub> = q n<sub>i</sub> (μ<sub>n</sub> + μ<sub>p</sub>)",
          "Used for pure semiconductors", "શુદ્ધ semiconductors માટે"),
        E("N-type conductivity", "N-type conductivity", "σ ≈ q N<sub>D</sub> μ<sub>n</sub>",
          "Holes neglected (minority)", "Holes ને અવગણ્યા (minority)"),
        E("P-type conductivity", "P-type conductivity", "σ ≈ q N<sub>A</sub> μ<sub>p</sub>",
          "Electrons neglected (minority)", "Electrons ને અવગણ્યા (minority)"),
        E("Resistivity", "Resistivity", "ρ = 1 / σ",
          "Unit: Ω·m or Ω·cm", "એકમ: Ω·m અથવા Ω·cm"),
    ]},
]


def V(q_en, q_gu, a_en, a_gu):
    return {"q": {"en": q_en, "gu": q_gu}, "a": {"en": a_en, "gu": a_gu}}


VIVA = [
    {"title": {"en": "Atomic Structure", "gu": "Atomic Structure"}, "items": [
        V("What are valence electrons?", "Valence electrons એટલે શું?",
          "Electrons present in the outermost shell of an atom.", "atom ના સૌથી બહારના shell માં રહેલા electrons."),
        V("What are free electrons?", "Free electrons એટલે શું?",
          "Electrons that have left their atom and move freely in the material; they carry current.",
          "atom છોડીને પદાર્થમાં મુક્ત રીતે ફરતા electrons; તે current વહન કરે છે."),
        V("How many valence electrons does silicon have?", "Silicon માં કેટલા valence electrons છે?",
          "Four (2, 8, 4).", "ચાર (2, 8, 4)."),
        V("Give two examples of trivalent impurities.", "Trivalent impurity ના બે ઉદાહરણ આપો.",
          "Boron and Gallium (also Aluminium, Indium).", "Boron અને Gallium (Aluminium, Indium પણ)."),
        V("Give two examples of pentavalent impurities.", "Pentavalent impurity ના બે ઉદાહરણ આપો.",
          "Phosphorus and Arsenic (also Antimony).", "Phosphorus અને Arsenic (Antimony પણ)."),
        V("What is the forbidden energy gap?", "Forbidden energy gap એટલે શું?",
          "Energy gap between valence band and conduction band where no electron can exist.",
          "Valence band અને conduction band વચ્ચેનો energy gap જ્યાં કોઈ electron રહી શકતો નથી."),
        V("Energy gap of Si and Ge?", "Si અને Ge નો energy gap?",
          "Si = 1.1 eV, Ge = 0.7 eV.", "Si = 1.1 eV, Ge = 0.7 eV."),
        V("What is the energy gap of a conductor?", "Conductor નો energy gap કેટલો?",
          "Zero – valence and conduction bands overlap.", "શૂન્ય – valence અને conduction bands overlap થાય છે."),
    ]},
    {"title": {"en": "Semiconductors & Doping", "gu": "Semiconductors અને Doping"}, "items": [
        V("What is a semiconductor?", "Semiconductor એટલે શું?",
          "A material with conductivity between conductors and insulators, e.g. Si, Ge.",
          "Conductors અને insulators ની વચ્ચે conductivity ધરાવતો પદાર્થ, દા.ત. Si, Ge."),
        V("How does semiconductor resistance change with temperature?", "તાપમાન સાથે semiconductor નો resistance કેવી રીતે બદલાય?",
          "It decreases (negative temperature coefficient).", "તે ઘટે છે (negative temperature coefficient)."),
        V("Why is Si preferred over Ge?", "Ge કરતાં Si શા માટે પસંદ થાય?",
          "Larger energy gap, lower leakage current, works at higher temperature, cheaper and abundant.",
          "મોટો energy gap, ઓછો leakage current, વધુ તાપમાને કાર્ય, સસ્તું અને વિપુલ."),
        V("What is a covalent bond?", "Covalent bond એટલે શું?",
          "A bond formed by sharing a pair of electrons between two atoms.", "બે atoms વચ્ચે electron જોડીની ભાગીદારીથી બનતો bond."),
        V("What is an intrinsic semiconductor?", "Intrinsic semiconductor એટલે શું?",
          "A pure semiconductor without any impurity.", "કોઈ impurity વગરનો શુદ્ધ semiconductor."),
        V("What is a hole?", "Hole એટલે શું?",
          "The vacancy of an electron in a covalent bond; it acts as a positive charge.",
          "Covalent bond માં electron ની ખાલી જગ્યા; તે positive charge તરીકે વર્તે છે."),
        V("Behaviour of pure semiconductor at 0 K?", "0 K પર શુદ્ધ semiconductor નું વર્તન?",
          "It behaves as a perfect insulator.", "તે સંપૂર્ણ insulator તરીકે વર્તે છે."),
        V("What is doping?", "Doping એટલે શું?",
          "Adding a small controlled amount of impurity to a pure semiconductor to increase its conductivity.",
          "Conductivity વધારવા શુદ્ધ semiconductor માં impurity ની ઓછી, નિયંત્રિત માત્રા ઉમેરવી."),
        V("What is the usual doping ratio?", "સામાન્ય doping ગુણોત્તર કેટલો?",
          "About 1 impurity atom per 10⁶ to 10⁸ semiconductor atoms.", "આશરે 10⁶ થી 10⁸ semiconductor atoms દીઠ 1 impurity atom."),
        V("What is recombination?", "Recombination એટલે શું?",
          "A free electron falling back into a hole, so both disappear.", "Free electron ફરી hole માં પડે, જેથી બંને નાશ પામે."),
    ]},
    {"title": {"en": "P-type & N-type", "gu": "P-type અને N-type"}, "items": [
        V("Majority carriers in N-type?", "N-type માં majority carriers?", "Electrons.", "Electrons."),
        V("Majority carriers in P-type?", "P-type માં majority carriers?", "Holes.", "Holes."),
        V("Why is pentavalent impurity called a donor?", "Pentavalent impurity ને donor કેમ કહે છે?",
          "Because each atom donates one free electron.", "કારણ કે દરેક atom એક free electron આપે (donate) છે."),
        V("Why is trivalent impurity called an acceptor?", "Trivalent impurity ને acceptor કેમ કહે છે?",
          "Because it creates a hole that accepts an electron.", "કારણ કે તે hole બનાવે છે જે electron સ્વીકારે (accept) છે."),
        V("Is N-type semiconductor negatively charged?", "શું N-type semiconductor negatively charged છે?",
          "No, it is electrically neutral as a whole.", "ના, તે સમગ્ર રીતે electrically neutral છે."),
        V("Minority carriers are produced by?", "Minority carriers શેનાથી ઉત્પન્ન થાય?",
          "Thermal generation (heat breaking covalent bonds).", "Thermal generation (ઉષ્માથી covalent bonds તૂટવાથી)."),
        V("State mass action law.", "Mass action law લખો.",
          "n × p = nᵢ² at a constant temperature.", "અચળ તાપમાને n × p = nᵢ²."),
        V("Which has higher mobility, electrons or holes?", "કોની mobility વધુ, electrons કે holes?",
          "Electrons.", "Electrons."),
    ]},
]


def X(q_en, q_gu, marks):
    return {"q": {"en": q_en, "gu": q_gu}, "marks": marks}


EXAM_QS = [
    X("Define: (i) Valence electrons (ii) Free electrons (iii) Forbidden energy gap.", "વ્યાખ્યા આપો: (i) Valence electrons (ii) Free electrons (iii) Forbidden energy gap.", 3),
    X("Explain trivalent, tetravalent and pentavalent materials with examples.", "Trivalent, tetravalent અને pentavalent પદાર્થો ઉદાહરણ સાથે સમજાવો.", 3),
    X("Classify materials as conductor, semiconductor and insulator on the basis of energy band diagram.", "Energy band diagram ના આધારે પદાર્થોનું conductor, semiconductor અને insulator માં વર્ગીકરણ કરો.", 4),
    X("Compare conductor, semiconductor and insulator.", "Conductor, semiconductor અને insulator ની સરખામણી કરો.", 4),
    X("What is doping? State its purpose and types of impurities.", "Doping એટલે શું? તેનો હેતુ અને impurity ના પ્રકારો લખો.", 3),
    X("Explain intrinsic semiconductor with neat diagram.", "સ્વચ્છ આકૃતિ સાથે intrinsic semiconductor સમજાવો.", 4),
    X("Differentiate between intrinsic and extrinsic semiconductors.", "Intrinsic અને extrinsic semiconductors વચ્ચે તફાવત લખો.", 3),
    X("Explain the formation of N-type semiconductor with diagram.", "આકૃતિ સાથે N-type semiconductor ની રચના સમજાવો.", 4),
    X("Explain the formation of P-type semiconductor with diagram.", "આકૃતિ સાથે P-type semiconductor ની રચના સમજાવો.", 4),
    X("Explain majority and minority charge carriers in P-type and N-type semiconductors.", "P-type અને N-type semiconductors માં majority અને minority charge carriers સમજાવો.", 3),
    X("Compare P-type and N-type semiconductors.", "P-type અને N-type semiconductors ની સરખામણી કરો.", 4),
    X("Explain N-type and P-type semiconductors with diagrams and compare them.", "આકૃતિ સાથે N-type અને P-type semiconductors સમજાવો અને તેમની સરખામણી કરો.", 7),
]
