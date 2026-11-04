# -*- coding: utf-8 -*-
"""DI04005071 Unit 1 extras: numericals (locked Mass-Transfer style),
formulae, viva, exam + answered practice, sources."""

def tr(en, gu):
    return {"en": en, "gu": gu}

def eq(s):
    return f'<div class="eq">{s}</div>'

def boxed(s):
    return f'<div class="eq boxed">{s}</div>'

# --------------------------------------------------------------- NUMERICALS
NUMERICALS = [
 {"id": "u1n1",
  "q": tr("Numerical 1.N1: A crude sample has specific gravity 0.850 at 15.6 °C. Calculate its API gravity and classify the crude.",
          "Numerical 1.N1: Crude sample ની specific gravity 15.6 °C પર 0.850 છે. તેની API gravity ગણો અને crude નું classification કરો."),
  "a": {
"en": f"""<h4>Given</h4><p>Specific gravity of crude, SG = 0.850 at 15.6 °C (60 °F), referred to water at the same temperature.</p><h4>Find</h4><p>Find the API gravity and state whether the crude is light, medium, heavy or extra-heavy.</p><h4>Formula</h4>{eq("°API = 141.5 / SG − 131.5")}<h4>Substitution and calculation</h4>{eq("°API = 141.5 / 0.850 − 131.5")}{eq("°API = 166.47 − 131.5")}{eq("°API = 34.97")}<h4>Final answer with units</h4>{boxed("°API = 35.0 °API")}{boxed("Classification: Light crude (above 31.1 °API)")}<h4>Validity check</h4><p>The crude is lighter than water (SG below 1), so a positive API well above 10 is expected. The value 35.0 lies just above the 31.1 light-crude limit, so the classification is light — but it is close to the medium band, so the full assay, not API alone, decides the processing route.</p>""",
"gu": f"""<h4>આપેલ</h4><p>Crude ની specific gravity, SG = 0.850, 15.6 °C (60 °F) પર, સરખા temperature ના water ના સંદર્ભમાં.</p><h4>શોધો</h4><p>API gravity શોધો અને crude light, medium, heavy કે extra-heavy છે તે જણાવો.</p><h4>સૂત્ર</h4>{eq("°API = 141.5 / SG − 131.5")}<h4>Substitution તથા Calculation</h4>{eq("°API = 141.5 / 0.850 − 131.5")}{eq("°API = 166.47 − 131.5")}{eq("°API = 34.97")}<h4>Units સાથે અંતિમ જવાબ</h4>{boxed("°API = 35.0 °API")}{boxed("Classification: Light crude (31.1 °API થી ઉપર)")}<h4>Validity Check</h4><p>Crude water કરતાં હલકું છે (SG 1 થી નીચે), તેથી 10 કરતાં સારો એવો positive API અપેક્ષિત છે. 35.0 નું મૂલ્ય 31.1 ની light-crude limit થી થોડું જ ઉપર છે, તેથી classification light છે — પણ તે medium band ની નજીક છે, તેથી processing route ફક્ત API નહીં, full assay નક્કી કરે છે.</p>"""}},
 {"id": "u1n2",
  "q": tr("Numerical 1.N2: A crude fraction has mean average boiling point 300 °C and specific gravity 0.820. Calculate the Watson (UOP) characterisation factor Kw and state the character of the fraction.",
          "Numerical 1.N2: Crude fraction નો mean average boiling point 300 °C તથા specific gravity 0.820 છે. Watson (UOP) characterisation factor Kw ગણો અને fraction નું character જણાવો."),
  "a": {
"en": f"""<h4>Given</h4><p>Mean average boiling point, MeABP = 300 °C; specific gravity, SG = 0.820. Watson factor needs the boiling point on an absolute (Rankine) scale.</p><h4>Find</h4><p>Find K<sub>w</sub> and state whether the fraction is paraffinic, intermediate, naphthenic or aromatic in character.</p><h4>Formula</h4>{eq("K<sub>w</sub> = (T<sub>B</sub>)<sup>1/3</sup> / SG,  with T<sub>B</sub> in Rankine (°R)")}{eq("T<sub>B</sub> (°R) = [MeABP (°C) + 273.15] × 1.8")}<h4>Substitution and calculation</h4>{eq("T<sub>B</sub> = (300 + 273.15) × 1.8 = 1031.67 °R")}{eq("(T<sub>B</sub>)<sup>1/3</sup> = (1031.67)<sup>1/3</sup> = 10.10")}{eq("K<sub>w</sub> = 10.10 / 0.820 = 12.32")}<h4>Final answer with units</h4>{boxed("K<sub>w</sub> = 12.3 (dimensionless)")}{boxed("Character: Paraffinic (K<sub>w</sub> above about 12.1)")}<h4>Validity check</h4><p>K<sub>w</sub> for real petroleum fractions always falls roughly between 10 and 13, and 12.3 is inside that band. A common error is to use Celsius directly: (300)<sup>1/3</sup>/0.820 = 8.2, which is outside the possible band and immediately shows the absolute-scale step was missed.</p>""",
"gu": f"""<h4>આપેલ</h4><p>Mean average boiling point, MeABP = 300 °C; specific gravity, SG = 0.820. Watson factor માટે boiling point absolute (Rankine) scale પર જોઈએ છે.</p><h4>શોધો</h4><p>K<sub>w</sub> શોધો અને fraction paraffinic, intermediate, naphthenic કે aromatic character નું છે તે જણાવો.</p><h4>સૂત્ર</h4>{eq("K<sub>w</sub> = (T<sub>B</sub>)<sup>1/3</sup> / SG,  જ્યાં T<sub>B</sub> Rankine (°R) માં")}{eq("T<sub>B</sub> (°R) = [MeABP (°C) + 273.15] × 1.8")}<h4>Substitution તથા Calculation</h4>{eq("T<sub>B</sub> = (300 + 273.15) × 1.8 = 1031.67 °R")}{eq("(T<sub>B</sub>)<sup>1/3</sup> = (1031.67)<sup>1/3</sup> = 10.10")}{eq("K<sub>w</sub> = 10.10 / 0.820 = 12.32")}<h4>Units સાથે અંતિમ જવાબ</h4>{boxed("K<sub>w</sub> = 12.3 (dimensionless)")}{boxed("Character: Paraffinic (K<sub>w</sub> આશરે 12.1 થી ઉપર)")}<h4>Validity Check</h4><p>વાસ્તવિક petroleum fractions માટે K<sub>w</sub> હંમેશા આશરે 10 થી 13 વચ્ચે હોય છે, અને 12.3 તે band માં છે. સામાન્ય ભૂલ Celsius સીધો વાપરવાની છે: (300)<sup>1/3</sup>/0.820 = 8.2, જે શક્ય band ની બહાર છે અને તરત બતાવે છે કે absolute-scale step ચૂકી ગયું છે.</p>"""}},
 {"id": "u1n3",
  "q": tr("Numerical 1.N3: 1000 kg of crude is distilled in a topping unit. Illustrative yields are: refinery gas and loss 3 %, LPG 3 %, petrol 18 %, kerosene 12 %, diesel 28 %, vacuum gas oil 20 % and residue 16 % by mass. Calculate the mass of each stream and check the balance.",
          "Numerical 1.N3: Topping unit માં 1000 kg crude distill થાય છે. Illustrative yields છે: refinery gas તથા loss 3 %, LPG 3 %, petrol 18 %, kerosene 12 %, diesel 28 %, vacuum gas oil 20 % અને residue 16 % (mass મુજબ). દરેક stream નો mass ગણો અને balance check કરો."),
  "a": {
"en": f"""<h4>Given</h4><p>Feed F = 1000 kg crude. Illustrative mass yields: gas + loss 3 %, LPG 3 %, petrol 18 %, kerosene 12 %, diesel 28 %, vacuum gas oil 20 %, residue 16 %. Yields sum to 100 %. These are teaching yields, not measured plant data.</p><h4>Find</h4><p>Find the mass of each product stream and verify the overall mass balance.</p><h4>Formula</h4>{eq("Mass of product = F × (yield % / 100)")}{eq("F = sum of all product masses + gas and loss")}<h4>Substitution and calculation</h4>{eq("Gas + loss = 1000 × 0.03 = 30 kg")}{eq("LPG = 1000 × 0.03 = 30 kg")}{eq("Petrol = 1000 × 0.18 = 180 kg")}{eq("Kerosene = 1000 × 0.12 = 120 kg")}{eq("Diesel = 1000 × 0.28 = 280 kg")}{eq("Vacuum gas oil = 1000 × 0.20 = 200 kg")}{eq("Residue = 1000 × 0.16 = 160 kg")}{eq("Total out = 30 + 30 + 180 + 120 + 280 + 200 + 160 = 1000 kg")}<h4>Final answer with units</h4>{boxed("Petrol = 180 kg, Kerosene = 120 kg, Diesel = 280 kg")}{boxed("LPG = 30 kg, VGO = 200 kg, Residue = 160 kg, Gas + loss = 30 kg")}<h4>Validity check</h4><p>Total out = 1000 kg = feed, so the balance closes exactly, as it must for stated yields. In a real unit the yields are measured and a small unaccounted loss remains; if a calculated total differs from the feed, a yield or a stream has been missed — the balance, not the feed figure, is corrected first.</p>""",
"gu": f"""<h4>આપેલ</h4><p>Feed F = 1000 kg crude. Illustrative mass yields: gas + loss 3 %, LPG 3 %, petrol 18 %, kerosene 12 %, diesel 28 %, vacuum gas oil 20 %, residue 16 %. Yields નો સરવાળો 100 % થાય છે. આ teaching yields છે, measured plant data નથી.</p><h4>શોધો</h4><p>દરેક product stream નો mass શોધો અને overall mass balance verify કરો.</p><h4>સૂત્ર</h4>{eq("Product નો mass = F × (yield % / 100)")}{eq("F = બધા product masses નો સરવાળો + gas તથા loss")}<h4>Substitution તથા Calculation</h4>{eq("Gas + loss = 1000 × 0.03 = 30 kg")}{eq("LPG = 1000 × 0.03 = 30 kg")}{eq("Petrol = 1000 × 0.18 = 180 kg")}{eq("Kerosene = 1000 × 0.12 = 120 kg")}{eq("Diesel = 1000 × 0.28 = 280 kg")}{eq("Vacuum gas oil = 1000 × 0.20 = 200 kg")}{eq("Residue = 1000 × 0.16 = 160 kg")}{eq("Total out = 30 + 30 + 180 + 120 + 280 + 200 + 160 = 1000 kg")}<h4>Units સાથે અંતિમ જવાબ</h4>{boxed("Petrol = 180 kg, Kerosene = 120 kg, Diesel = 280 kg")}{boxed("LPG = 30 kg, VGO = 200 kg, Residue = 160 kg, Gas + loss = 30 kg")}<h4>Validity Check</h4><p>Total out = 1000 kg = feed, તેથી balance બરાબર close થાય છે, જે stated yields માટે થવું જ જોઈએ. વાસ્તવિક unit માં yields મપાય છે અને નાનો unaccounted loss રહે છે; જો ગણેલો total feed થી જુદો આવે, તો કોઈ yield કે stream ચૂકી ગયો છે — પહેલાં balance સુધારાય છે, feed figure નહીં.</p>"""}},
]

# ----------------------------------------------------------------- FORMULAE
SYNTAX = [
 {"title": tr("Density and characterisation", "Density તથા characterisation"),
  "items": [
   {"name": tr("API gravity", "API gravity"),
    "f": "°API = 141.5 / SG − 131.5  (SG at 15.6 °C / 60 °F)",
    "terms": tr("Higher °API = lighter crude. Bands: light above 31.1, medium 22.3–31.1, heavy 10–22.3, extra-heavy below 10.",
                "વધુ °API = હલકું crude. Bands: light 31.1 થી ઉપર, medium 22.3–31.1, heavy 10–22.3, extra-heavy 10 થી નીચે.")},
   {"name": tr("Specific gravity", "Specific gravity"),
    "f": "SG = density of oil / density of water at the same temperature",
    "terms": tr("Water has SG 1.000 and 10 °API. Most crudes: SG about 0.80–0.95.",
                "Water નો SG 1.000 અને 10 °API છે. મોટાભાગના crudes: SG આશરે 0.80–0.95.")},
   {"name": tr("Watson (UOP) characterisation factor", "Watson (UOP) characterisation factor"),
    "f": "Kw = (TB)^(1/3) / SG,  TB = mean average boiling point in °R",
    "terms": tr("Above ~12.1 paraffinic; 11.5–12.1 intermediate; 11.0–11.5 naphthenic; below 11 aromatic. TB must be absolute.",
                "આશરે 12.1 થી ઉપર paraffinic; 11.5–12.1 intermediate; 11.0–11.5 naphthenic; 11 થી નીચે aromatic. TB absolute જ હોવો જોઈએ.")},
   {"name": tr("Sweet / sour line", "Sweet / sour line"),
    "f": "Sweet: sulfur below about 0.5 % by mass;  Sour: above about 0.5 %",
    "terms": tr("A convention, not a law of nature; sour crudes need desulfurisation (Unit IV) and usually sell cheaper.",
                "એક convention છે, કુદરતી નિયમ નથી; sour crudes ને desulfurisation (Unit IV) જોઈએ છે અને સામાન્ય રીતે સસ્તા વેચાય છે.")},
  ]},
 {"title": tr("Refinery bookkeeping and conversions", "Refinery bookkeeping તથા conversions"),
  "items": [
   {"name": tr("Product yield", "Product yield"),
    "f": "Yield % of a product = (mass or volume of product / feed) × 100",
    "terms": tr("State whether the yield is on mass or volume basis; the two differ because products have different densities.",
                "Yield mass કે volume basis પર છે તે જણાવો; બંને જુદા પડે છે કારણ કે products ની densities જુદી છે.")},
   {"name": tr("Overall mass balance", "Overall mass balance"),
    "f": "Feed = all products + fuel consumed + loss",
    "terms": tr("Every unit calculation starts here. A balance that does not close means a missed stream, not new matter.",
                "દરેક unit calculation અહીંથી શરૂ થાય છે. Close ન થતો balance એટલે ચૂકાયેલો stream, નવું matter નહીં.")},
   {"name": tr("Barrel conversions", "Barrel conversions"),
    "f": "1 barrel (bbl) = 42 US gallons ≈ 159 litres;  1 m³ ≈ 6.29 bbl",
    "terms": tr("Refinery capacities are quoted in barrels per day. Mass per barrel varies with crude density — there is no fixed kg-per-barrel.",
                "Refinery capacities barrels per day માં દર્શાવાય છે. Barrel દીઠ mass crude density મુજબ બદલાય છે — નિશ્ચિત kg-per-barrel નથી.")},
  ]},
]

# --------------------------------------------------------------------- VIVA
VIVA = [
 {"title": tr("Unit 1 viva — occurrence, composition, classification, refinery types and products",
              "Unit 1 viva — occurrence, composition, classification, refinery types તથા products"),
  "items": [
   {"q": tr("What is petroleum?", "Petroleum એટલે શું?"),
    "a": tr("Petroleum is a naturally occurring mixture of hydrocarbons, found as liquid crude oil and natural gas in porous underground rock, formed from buried organic matter.",
            "Petroleum એ hydrocarbons નું કુદરતી mixture છે, જે liquid crude oil તથા natural gas રૂપે છિદ્રાળુ underground rock માં મળે છે અને દટાયેલા organic matter માંથી બન્યું છે.")},
   {"q": tr("Name the five conditions needed for a commercial oil deposit.", "Commercial oil deposit માટે જરૂરી પાંચ conditions જણાવો."),
    "a": tr("A source rock with kerogen, heat and time for generation (the oil window), migration, a porous-permeable reservoir rock, and an impermeable cap rock with a trap.",
            "Kerogen વાળો source rock, generation માટે heat તથા time (oil window), migration, porous-permeable reservoir rock, અને trap સાથે impermeable cap rock.")},
   {"q": tr("What is kerogen and the oil window?", "Kerogen તથા oil window એટલે શું?"),
    "a": tr("Kerogen is the solid organic matter in source rock that cracks on burial heating, first to oil and then to gas. The oil window is the approximate 60–150 °C range in which most oil forms.",
            "Kerogen એ source rock માંનું solid organic matter છે જે burial heating થી પહેલાં oil અને પછી gas માં crack થાય છે. Oil window એ આશરે 60–150 °C નો range છે જેમાં મોટાભાગનું oil બને છે.")},
   {"q": tr("Name the four hydrocarbon families in crude oil.", "Crude oil ની ચાર hydrocarbon families જણાવો."),
    "a": tr("Paraffins (chain alkanes), naphthenes (saturated rings), aromatics (benzene rings), and resins/asphaltenes (the heaviest, polar part).",
            "Paraffins (chain alkanes), naphthenes (saturated rings), aromatics (benzene rings), અને resins/asphaltenes (સૌથી ભારે, polar ભાગ).")},
   {"q": tr("Why must crude be desalted before heating?", "Crude ને ગરમ કરતા પહેલાં desalt કેમ કરવું પડે છે?"),
    "a": tr("The salt, present in produced water, fouls preheat exchangers and its chlorides form hydrochloric acid at high temperature, causing severe corrosion in the crude unit overhead system.",
            "Produced water માં રહેલું salt preheat exchangers foul કરે છે અને તેના chlorides ઊંચા temperature પર hydrochloric acid બનાવી crude unit overhead system માં ગંભીર corrosion કરે છે.")},
   {"q": tr("Define API gravity. Is a 40 °API crude lighter or heavier than a 20 °API crude?",
            "API gravity વ્યાખ્યાયિત કરો. 40 °API crude 20 °API crude કરતાં હલકું છે કે ભારે?"),
    "a": tr("API gravity = 141.5/SG − 131.5 and measures lightness: the higher the API, the lighter the oil. A 40 °API crude is therefore much lighter than a 20 °API crude.",
            "API gravity = 141.5/SG − 131.5 અને હલકાપણું માપે છે: API વધુ એટલે oil હલકું. તેથી 40 °API crude 20 °API crude કરતાં ઘણું હલકું છે.")},
   {"q": tr("What do sweet and sour crude mean?", "Sweet તથા sour crude એટલે શું?"),
    "a": tr("By a common convention, a crude with less than about 0.5 % sulfur is sweet and one with more is sour. Sour crudes need desulfurisation and are cheaper to buy but costlier to process.",
            "સામાન્ય convention મુજબ, આશરે 0.5 % થી ઓછું sulfur હોય તે crude sweet અને વધુ હોય તે sour છે. Sour crudes ને desulfurisation જોઈએ છે અને ખરીદવામાં સસ્તા પણ process કરવામાં મોંઘા પડે છે.")},
   {"q": tr("What does the Watson factor Kw tell you?", "Watson factor Kw શું દર્શાવે છે?"),
    "a": tr("Kw = (mean average boiling point in °R)^(1/3)/SG expresses chemical character: above about 12.1 the fraction is paraffinic, near 11 naphthenic and below 11 aromatic.",
            "Kw = (mean average boiling point °R માં)^(1/3)/SG chemical character દર્શાવે છે: આશરે 12.1 થી ઉપર fraction paraffinic, 11 ની આસપાસ naphthenic અને 11 થી નીચે aromatic.")},
   {"q": tr("Give one physical and one chemical refinery process.", "એક physical અને એક chemical refinery process આપો."),
    "a": tr("Distillation is physical — molecules are only separated by boiling point. Cracking is chemical — large molecules are broken into smaller petrol- and LPG-range molecules.",
            "Distillation physical છે — molecules ફક્ત boiling point થી છૂટા પડે છે. Cracking chemical છે — મોટા molecules નાના petrol- તથા LPG-range molecules માં તૂટે છે.")},
   {"q": tr("How does a topping refinery differ from a conversion refinery?", "Topping refinery conversion refinery થી કેવી રીતે જુદી પડે છે?"),
    "a": tr("A topping refinery only distils crude, so it can sell only the fractions naturally present and makes much fuel oil. A conversion refinery adds FCC/hydrocracking (and similar) units that convert heavy fractions into petrol, LPG and diesel.",
            "Topping refinery ફક્ત crude distill કરે છે, તેથી કુદરતી રીતે હાજર fractions જ વેચી શકે છે અને ઘણું fuel oil બનાવે છે. Conversion refinery FCC/hydrocracking (અને સમાન) units ઉમેરે છે જે heavy fractions ને petrol, LPG તથા diesel માં ફેરવે છે.")},
   {"q": tr("Name the refinery products in boiling-range order.", "Refinery products boiling-range ના ક્રમમાં જણાવો."),
    "a": tr("Refinery gas and LPG, naphtha/petrol, kerosene/ATF, diesel, vacuum gas oil, then fuel oil and vacuum residue (bitumen/coke feed) as the heaviest products.",
            "Refinery gas તથા LPG, naphtha/petrol, kerosene/ATF, diesel, vacuum gas oil, પછી સૌથી ભારે products તરીકે fuel oil તથા vacuum residue (bitumen/coke feed).")},
   {"q": tr("Why can distillation alone not maximise petrol production?", "ફક્ત distillation petrol production મહત્તમ કેમ કરી શકતું નથી?"),
    "a": tr("Because distillation only separates the petrol-range molecules already present in the crude; it creates none. Extra petrol comes only from chemical conversion of heavier fractions, by cracking and reforming.",
            "કારણ કે distillation ફક્ત crude માં પહેલેથી હાજર petrol-range molecules ને જ છૂટા પાડે છે; તે એક પણ બનાવતું નથી. વધારાનું petrol ફક્ત ભારે fractions ના chemical conversion — cracking તથા reforming — થી જ મળે છે.")},
  ]}
]

# ------------------------------------------------------------- EXAM + ANSWERS
_PRACTICE = [
 ("Practice: Define petroleum and explain, with a neat sketch, the conditions needed for its occurrence and accumulation.",
  "Practice: Petroleum વ્યાખ્યાયિત કરો અને સુઘડ sketch સાથે તેની પ્રાપ્તિ તથા accumulation માટે જરૂરી conditions સમજાવો.", 4),
 ("Practice: Describe the composition of crude oil, explaining the four hydrocarbon families with their general formulas and one refining effect of each.",
  "Practice: Crude oil નું composition વર્ણવો, ચાર hydrocarbon families તેમના general formulas તથા દરેકની એક refining effect સાથે સમજાવો.", 7),
 ("Practice: A crude has specific gravity 0.850 at 15.6 °C. Calculate its API gravity and classify it. Show every calculation step.",
  "Practice: Crude ની specific gravity 15.6 °C પર 0.850 છે. તેની API gravity ગણો અને classification કરો. દરેક calculation step બતાવો.", 4),
 ("Practice: Classify crude oil by chemical base, by API gravity and by sulfur content, stating the limits you use.",
  "Practice: Crude oil નું chemical base, API gravity તથા sulfur content મુજબ classification કરો, તમે વાપરેલા limits જણાવો.", 4),
 ("Practice: With a block diagram, explain the types of refineries and state which type suits a heavy, sour crude when fuel-oil demand is low.",
  "Practice: Block diagram સાથે refineries ના પ્રકાર સમજાવો અને fuel-oil demand ઓછી હોય ત્યારે heavy, sour crude માટે કયો પ્રકાર યોગ્ય છે તે જણાવો.", 7),
 ("Practice: Distinguish between physical and chemical refinery processes, giving three examples of each and stating what each type can and cannot do.",
  "Practice: Physical તથા chemical refinery processes વચ્ચે તફાવત કરો, દરેકના ત્રણ examples આપો અને દરેક પ્રકાર શું કરી શકે અને શું ન કરી શકે તે જણાવો.", 4),
 ("Practice: List the products of a refinery in boiling-range order with approximate ranges and one main use of each, and explain why a boiling range alone does not make a finished product.",
  "Practice: Refinery ના products boiling-range ના ક્રમમાં આશરે ranges તથા દરેકના એક મુખ્ય ઉપયોગ સાથે જણાવો, અને ફક્ત boiling range finished product કેમ બનાવતું નથી તે સમજાવો.", 4),
 ("Practice: Explain how the non-hydrocarbon part of crude — sulfur, wax, asphaltenes and salt — decides which treating and conversion units a refinery must install.",
  "Practice: Crude નો non-hydrocarbon ભાગ — sulfur, wax, asphaltenes તથા salt — refinery એ કયા treating તથા conversion units સ્થાપવા પડશે તે કેવી રીતે નક્કી કરે છે તે સમજાવો.", 4),
]
EXAM = [{"q": tr(en, gu), "marks": m} for (en, gu, m) in _PRACTICE]

_ANSWERS_EN = [
 "<h4>Definition</h4><p>Petroleum is a natural mixture of hydrocarbons occurring as crude oil and natural gas in porous rock, formed from buried organic matter.</p><h4>Explanation and application</h4><ul><li>Source rock kerogen generates oil in the 60–150 °C oil window on burial.</li><li>Oil migrates upward into a porous, permeable reservoir rock.</li><li>An impermeable cap rock in an anticline, fault or stratigraphic trap stops it, with gas above oil above water.</li></ul><p>Sketch: source rock below, reservoir in an arch sealed by shale, gas/oil/water layers marked (as in diagram ref1_trap).</p>",
 "<h4>Definition</h4><p>Crude is thousands of hydrocarbons, C 83–87 %, H 10–14 %, S 0.05–6 %, N 0.1–2 %, O 0.05–2 %, plus trace metals.</p><h4>Explanation and application</h4><ul><li>Paraffins C<sub>n</sub>H<sub>2n+2</sub>: chains; good fuels, long ones form wax.</li><li>Naphthenes C<sub>n</sub>H<sub>2n</sub>: saturated rings; lube/solvent character.</li><li>Aromatics: benzene rings; raise octane, heavier and soot-forming.</li><li>Resins/asphaltenes: heaviest polar part; viscosity, fouling and coke.</li></ul>",
 "<h4>Given and assumptions</h4><p>SG = 0.850 at 15.6 °C. Use °API = 141.5/SG − 131.5.</p><h4>Step-by-step solution</h4><p>°API = 141.5/0.850 − 131.5 = 166.47 − 131.5 = 34.97.</p><h4>Interpretation and check</h4><p><b>°API = 35.0 — light crude</b> (above 31.1). Full working in the locked numerical style is in Numerical 1.N1.</p>",
 "<h4>Definition</h4><p>Classification predicts products and processing difficulty before detailed design.</p><h4>Explanation and application</h4><ul><li>By base: paraffinic, naphthenic, aromatic, mixed — supported by Watson Kw.</li><li>By API: light above 31.1, medium 22.3–31.1, heavy 10–22.3, extra-heavy below 10.</li><li>By sulfur: sweet below about 0.5 % S, sour above.</li></ul><p>Limits are conventions; final design uses the crude assay.</p>",
 "<h4>Definition</h4><p>Refinery types are classed by conversion complexity beyond distillation.</p><h4>Explanation and application</h4><ul><li>Topping: distillation only. Hydro-skimming: adds hydrotreater and reformer.</li><li>Conversion: adds FCC/hydrocracker. Deep conversion: adds coker/residue conversion.</li><li>Lube type: adds solvent extraction and dewaxing.</li></ul><p>For a heavy, sour crude with low fuel-oil demand, a deep-conversion refinery is suitable (block flow as in diagram ref1_refinery_block).</p>",
 "<h4>Definition</h4><p>Physical processes separate unchanged molecules; chemical processes break or rearrange bonds to form new molecules.</p><h4>Comparison</h4><ul><li>Physical: desalting, distillation, solvent extraction/dewaxing — cannot create extra petrol.</li><li>Chemical: cracking, reforming, hydrotreating — can convert heavy fractions and improve quality.</li><li>Chemical routes cost catalyst, hydrogen and energy; physical routes are limited by equilibrium.</li></ul>",
 "<h4>Definition</h4><p>Products follow the barrel in boiling-range order.</p><h4>Key points and data</h4><ul><li>LPG below ~40 °C; petrol ~30–180 °C; kerosene/ATF ~150–275 °C; diesel ~200–360 °C; VGO above ~360 °C; residue last.</li><li>Uses: LPG fuel, petrol engines, jet fuel, diesel engines, cracking feed, fuel/bitumen.</li></ul><p>A range alone is not a finished product because octane, vapour pressure, sulfur and other specifications must also be met.</p>",
 "<h4>Definition</h4><p>The small non-hydrocarbon part controls corrosion, catalyst life and product quality.</p><h4>Explanation and application</h4><ul><li>Sulfur → hydrotreating, sweetening, desulfurisation (Unit IV) and sulfur recovery.</li><li>Salt/water → desalting before heating; wax → dewaxing; asphaltenes → blending care and residue conversion/coking.</li></ul><p>Hence a sour, waxy, asphaltic crude forces a more complex and costly refinery than a sweet light crude.</p>",
]
_ANSWERS_GU = [
 "<h4>વ્યાખ્યા</h4><p>Petroleum એ hydrocarbons નું કુદરતી mixture છે જે crude oil તથા natural gas રૂપે છિદ્રાળુ rock માં મળે છે અને દટાયેલા organic matter માંથી બન્યું છે.</p><h4>સમજૂતી તથા ઉપયોગ</h4><ul><li>Source rock kerogen burial પર 60–150 °C oil window માં oil generate કરે છે.</li><li>Oil ઉપર તરફ porous, permeable reservoir rock માં migrate થાય છે.</li><li>Anticline, fault કે stratigraphic trap માં impermeable cap rock તેને અટકાવે છે, gas નીચે oil અને નીચે water સાથે.</li></ul><p>Sketch: નીચે source rock, shale થી sealed arch માં reservoir, gas/oil/water layers mark કરો (diagram ref1_trap મુજબ).</p>",
 "<h4>વ્યાખ્યા</h4><p>Crude હજારો hydrocarbons છે: C 83–87 %, H 10–14 %, S 0.05–6 %, N 0.1–2 %, O 0.05–2 %, સાથે trace metals.</p><h4>સમજૂતી તથા ઉપયોગ</h4><ul><li>Paraffins C<sub>n</sub>H<sub>2n+2</sub>: chains; સારા fuels, લાંબા wax બનાવે છે.</li><li>Naphthenes C<sub>n</sub>H<sub>2n</sub>: saturated rings; lube/solvent character.</li><li>Aromatics: benzene rings; octane વધારે, ભારે તથા soot-forming.</li><li>Resins/asphaltenes: સૌથી ભારે polar ભાગ; viscosity, fouling તથા coke.</li></ul>",
 "<h4>આપેલ તથા ધારણાઓ</h4><p>SG = 0.850, 15.6 °C પર. °API = 141.5/SG − 131.5 વાપરો.</p><h4>Step-by-step solution</h4><p>°API = 141.5/0.850 − 131.5 = 166.47 − 131.5 = 34.97.</p><h4>અર્થઘટન તથા check</h4><p><b>°API = 35.0 — light crude</b> (31.1 થી ઉપર). સંપૂર્ણ working locked numerical style માં Numerical 1.N1 માં છે.</p>",
 "<h4>વ્યાખ્યા</h4><p>Classification detailed design પહેલાં products તથા processing difficulty નો અંદાજ આપે છે.</p><h4>સમજૂતી તથા ઉપયોગ</h4><ul><li>Base મુજબ: paraffinic, naphthenic, aromatic, mixed — Watson Kw થી support સાથે.</li><li>API મુજબ: light 31.1 થી ઉપર, medium 22.3–31.1, heavy 10–22.3, extra-heavy 10 થી નીચે.</li><li>Sulfur મુજબ: આશરે 0.5 % S થી નીચે sweet, ઉપર sour.</li></ul><p>Limits conventions છે; final design crude assay વાપરે છે.</p>",
 "<h4>વ્યાખ્યા</h4><p>Refinery types distillation થી આગળની conversion complexity મુજબ વર્ગીકૃત થાય છે.</p><h4>સમજૂતી તથા ઉપયોગ</h4><ul><li>Topping: ફક્ત distillation. Hydro-skimming: hydrotreater તથા reformer ઉમેરે છે.</li><li>Conversion: FCC/hydrocracker ઉમેરે છે. Deep conversion: coker/residue conversion ઉમેરે છે.</li><li>Lube type: solvent extraction તથા dewaxing ઉમેરે છે.</li></ul><p>ઓછી fuel-oil demand સાથે heavy, sour crude માટે deep-conversion refinery યોગ્ય છે (diagram ref1_refinery_block મુજબ block flow).</p>",
 "<h4>વ્યાખ્યા</h4><p>Physical processes યથાવત molecules ને છૂટા પાડે છે; chemical processes bonds તોડી કે rearrange કરી નવા molecules બનાવે છે.</p><h4>Comparison</h4><ul><li>Physical: desalting, distillation, solvent extraction/dewaxing — વધારાનું petrol બનાવી શકતા નથી.</li><li>Chemical: cracking, reforming, hydrotreating — heavy fractions convert કરી quality સુધારી શકે છે.</li><li>Chemical routes માટે catalyst, hydrogen તથા energy ખર્ચાય; physical routes equilibrium થી મર્યાદિત છે.</li></ul>",
 "<h4>વ્યાખ્યા</h4><p>Products barrel ને boiling-range ક્રમમાં અનુસરે છે.</p><h4>મુખ્ય મુદ્દા તથા data</h4><ul><li>LPG આશરે 40 °C થી નીચે; petrol ~30–180 °C; kerosene/ATF ~150–275 °C; diesel ~200–360 °C; VGO ~360 °C થી ઉપર; residue છેલ્લે.</li><li>ઉપયોગો: LPG fuel, petrol engines, jet fuel, diesel engines, cracking feed, fuel/bitumen.</li></ul><p>ફક્ત range finished product બનાવતું નથી કારણ કે octane, vapour pressure, sulfur તથા અન્ય specifications પણ પૂરા થવા જોઈએ.</p>",
 "<h4>વ્યાખ્યા</h4><p>નાનો non-hydrocarbon ભાગ corrosion, catalyst life તથા product quality નિયંત્રિત કરે છે.</p><h4>સમજૂતી તથા ઉપયોગ</h4><ul><li>Sulfur → hydrotreating, sweetening, desulfurisation (Unit IV) તથા sulfur recovery.</li><li>Salt/water → ગરમ કરતા પહેલાં desalting; wax → dewaxing; asphaltenes → blending care તથા residue conversion/coking.</li></ul><p>તેથી sour, waxy, asphaltic crude sweet light crude કરતાં વધુ complex તથા મોંઘી refinery ફરજ પાડે છે.</p>",
]
ANSWERED = {
 "title": tr("Answered practice — model answers", "Answered practice — model answers"),
 "items": [
   {"h": tr(f"Practice {i+1}. {en_q[len('Practice: '):]}", f"Practice {i+1}. {gu_q[len('Practice: '):]}"),
    "body": {"en": _ANSWERS_EN[i], "gu": _ANSWERS_GU[i]}}
   for i, (en_q, gu_q, _m) in enumerate(_PRACTICE)
 ]
}

SOURCES = [
 {"title": "Bhaskar Rao, B. K. — Modern Petroleum Refining Processes, Oxford and IBH, 2007 (GTU syllabus book 1)", "url": ""},
 {"title": "Gopala Rao, M. & Sittig, M. — Outlines of Chemical Technology, 3rd ed., East-West Press (GTU syllabus book 2)", "url": ""},
 {"title": "Austin, G. T. — Shreve's Chemical Process Industries, 5th ed., McGraw Hill (GTU syllabus book 3)", "url": ""},
 {"title": "Bhaskar Rao, B. K. — A Text on Petrochemicals, 2nd ed., Khanna Publishers, 1998 (GTU syllabus book 4)", "url": ""},
 {"title": "Nelson, W. L. — Petroleum Refinery Engineering, McGraw Hill (GTU syllabus book 5)", "url": ""},
 {"title": "NPTEL — Petroleum Refining course (syllabus open-source link 1)", "url": "https://onlinecourses.nptel.ac.in/noc23_ch64"},
 {"title": "Penn State e-Education — Refinery Products and Processes overview (syllabus open-source link 2)", "url": "https://www.e-education.psu.edu/fsc432/content/overview-refinery-products-and-processes"},
]
