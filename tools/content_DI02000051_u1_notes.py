"""DI02000051 Environmental Sustainability - Unit 1: Introduction to Environmental Sustainability,
Ecosystem and Biodiversity (bilingual en + gu).

GTU 1.1-1.3, 4 h, 10 %, 7 marks, CO1. Every text node carries English and Gujarati, like the other
bilingual subjects in the app; diagram labels stay in English.
"""


def T(en, gu=None):
    """A bilingual node. Symbols and numbers read the same in both languages."""
    return {"en": en, "gu": en if gu is None else gu}


def _join(parts):
    return {"en": "".join(p["en"] for p in parts), "gu": "".join(p["gu"] for p in parts)}


def P(en, gu):
    return T(f"<p>{en}</p>", f"<p>{gu}</p>")


def H4(en, gu):
    return T(f"<h4>{en}</h4>", f"<h4>{gu}</h4>")


def UL(*items):
    return T("<ul>" + "".join(f"<li>{i[0]}</li>" for i in items) + "</ul>",
             "<ul>" + "".join(f"<li>{i[1]}</li>" for i in items) + "</ul>")


def OL(*items):
    return T("<ol>" + "".join(f"<li>{i[0]}</li>" for i in items) + "</ol>",
             "<ol>" + "".join(f"<li>{i[1]}</li>" for i in items) + "</ol>")


def TB(head, rows):
    """head: [(en, gu), ...]; rows: [[(en, gu), ...], ...]"""
    def build(k):
        out = "<table><tr>" + "".join(f"<th>{h[k]}</th>" for h in head) + "</tr>"
        for r in rows:
            out += "<tr>" + "".join(f"<td>{c[k]}</td>" for c in r) + "</tr>"
        return out + "</table>"
    return T(build("en"), build("gu"))


def card(h, parts, diagram=None, syllabus_item=None, examples=None):
    item = {"h": h, "body": _join(parts)}
    if diagram:
        item["diagram"] = diagram
    if syllabus_item:
        item["syllabus_item"] = syllabus_item
    if examples:
        item["examples"] = list(examples)
    return item


def num(id_, h, statement, solution_parts, answer, unit_no=1):
    """A solved numerical: given, step-by-step work and a boxed answer, in both languages."""
    def build(k, given_head, steps_head, answer_head):
        return (f"<h4>{given_head}</h4><p>{statement[k]}</p>"
                f"<h4>{steps_head}</h4>{''.join(p[k] for p in solution_parts)}"
                f"<h4>{answer_head}</h4><p><b>{answer[k]}</b></p>")
    return {"id": id_, "unit": unit_no, "h": h, "q": statement,
            "a": T(build("en", "Given and assumptions", "Step-by-step solution", "Answer"),
                   build("gu", "આપેલી માહિતી", "પગલાવાર ઉકેલ", "જવાબ")),
            "answer": answer}


SOURCES = [
    T("GTU DI02000051 Environmental Sustainability syllabus (uploaded PDF, w.e.f. 2024-25)",
      "GTU DI02000051 પર્યાવરણીય ટકાઉપણું સિલેબસ (અપલોડ કરેલ PDF, 2024-25થી અમલમાં)"),
    T("Anandita Basak - Environmental Studies, Pearson Publications (biodiversity and ecosystems)",
      "આનંદિતા બાસક - એન્વાયર્નમેન્ટલ સ્ટડીઝ, પિયર્સન (જૈવવિવિધતા અને પારિતંત્ર)"),
    T("Aloka Debi - Environmental Science and Engineering, University Press (natural cycles)",
      "અલોકા દેબી - એન્વાયર્નમેન્ટલ સાયન્સ એન્ડ એન્જિનિયરિંગ, યુનિવર્સિટી પ્રેસ (કુદરતી ચક્રો)"),
    T("ENVIS India - state of the environment reports and biodiversity statistics",
      "ENVIS ઇન્ડિયા - પર્યાવરણની સ્થિતિના અહેવાલ અને જૈવવિવિધતાના આંકડા"),
    T("NPTEL - Environmental Science lectures on ecosystems and biodiversity",
      "NPTEL - પારિતંત્ર અને જૈવવિવિધતા પર પર્યાવરણ વિજ્ઞાનના વ્યાખ્યાનો"),
]

NOTES = [
    {"title": T("1. Sustainability and the Ecosystem", "1. ટકાઉપણું અને પારિતંત્ર"),
     "items": [
         card(T("1.1 What sustainability means and how far it reaches",
                "1.1 ટકાઉપણું એટલે શું અને તે કેટલું વ્યાપક છે"),
              [H4("Definition", "વ્યાખ્યા"),
               P("<b>Sustainability</b> is the ability to keep a system running indefinitely without "
                 "using up the resources or the natural capital it depends on. The Brundtland "
                 "Commission (1987) called <b>sustainable development</b> \"development that meets the "
                 "needs of the present without compromising the ability of future generations to meet "
                 "their own needs\".",
                 "<b>ટકાઉપણું</b> એટલે કોઈ પ્રણાલીને અનંત કાળ સુધી ચલાવવાની ક્ષમતા, જે તે વાપરતાં સ્રોતો કે "
                 "કુદરતી મૂડી ખતમ કર્યા વગર શક્ય બને. બ્રુન્ટલેન્ડ આયોગ (1987)એ <b>ટકાઉ વિકાસ</b>ને "
                 "\"આજની જરૂરિયાત પૂરી કરે, પણ આવનારી પેઢી પોતાની જરૂરિયાત પૂરી કરી શકે તેવી ક્ષમતાને "
                 "નુકસાન ન પહોંચાડે\" તેવો વિકાસ કહ્યો."),
               H4("The three pillars", "ત્રણ સ્તંભ"),
               P("Sustainability stands on three pillars that must be satisfied together: "
                 "<b>environmental</b> (air, water, soil and biodiversity stay healthy), "
                 "<b>social</b> (people have health, education and equity) and <b>economic</b> (the "
                 "activity pays for itself). Two pillars only gives a weak result - a cheap factory "
                 "that poisons a river is economically sound but not sustainable.",
                 "ટકાઉપણું ત્રણ સ્તંભ પર ઊભું છે, જે એકસાથે પૂરા થવા જોઈએ: <b>પર્યાવરણીય</b> (હવા, પાણી, "
                 "જમીન અને જૈવવિવિધતા સ્વસ્થ રહે), <b>સામાજિક</b> (લોકોને આરોગ્ય, શિક્ષણ અને સમાનતા મળે) "
                 "અને <b>આર્થિક</b> (પ્રવૃત્તિ પોતાનો ખર્ચ કાઢે). ફક્ત બે સ્તંભ હોય તો પરિણામ નબળું આવે - "
                 "સસ્તી ફેક્ટરી નદીને ઝેરી બનાવે તો આર્થિક રીતે સારી, પણ ટકાઉ નહીં."),
               H4("Scope for a diploma engineer", "ડિપ્લોમા ઇજનેર માટે વ્યાપ્તિ"),
               UL(("Material choice: recycled or renewable material instead of virgin material.",
                   "સામગ્રીની પસંદગી: નવી સામગ્રીને બદલે રિસાઇકલ કે નવીકરણીય સામગ્રી."),
                  ("Energy: a motor of the right size, a variable speed drive, a solar water heater.",
                   "ઊર્જા: યોગ્ય માપનું મોટર, વેરિયેબલ સ્પીડ ડ્રાઇવ, સૌર વોટર હીટર."),
                  ("Waste: separating scrap at the machine instead of at the dump.",
                   "કચરો: કચરાપેટી પર નહીં, મશીન પાસે જ સ્ક્રેપ અલગ કરવો."),
                  ("Design: longer life, repairable parts, less packaging.",
                   "ડિઝાઇન: લાંબું આયુષ્ય, સમારી શકાય તેવા ભાગ, ઓછું પેકિંગ.")),
               H4("Linear and circular thinking", "રેખીય અને ચક્રીય વિચાર"),
               P("The old economy is <b>linear</b>: take, make, use, throw away. The "
                 "<b>circular</b> economy keeps material in use - repair, remanufacture, recycle - so "
                 "that the same kilogram of metal serves many product lives instead of one.",
                 "જૂનું અર્થતંત્ર <b>રેખીય</b> છે: લો, બનાવો, વાપરો, ફેંકો. <b>ચક્રીય</b> અર્થતંત્ર સામગ્રીને "
                 "વપરાશમાં રાખે - સમારકામ, ફરી ઉત્પાદન, રિસાઇકલ - જેથી એક જ કિલો ધાતુ એકને બદલે ઘણા "
                 "ઉત્પાદન-જીવન સેવે."),
               H4("Worked example", "ઉકેલાયેલ દાખલો"),
               P("A workshop buys 2 t of mild steel a month and throws away 0.3 t as scrap. Selling the "
                 "scrap back and cutting the off-cut by 40 % saves about 0.12 t of steel a month - "
                 "economic saving and less mining at the same time, which is exactly what the three "
                 "pillars mean in practice.",
                 "એક વર્કશોપ મહિને 2 ટન માઇલ્ડ સ્ટીલ ખરીદે અને 0.3 ટન સ્ક્રેપ ફેંકે. સ્ક્રેપ પાછો વેચવાથી "
                 "અને કટીંગ 40 % ઘટાડવાથી મહિને લગભગ 0.12 ટન સ્ટીલ બચે - આર્થિક બચત અને ઓછું ખાણકામ "
                 "એકસાથે, જે ત્રણ સ્તંભનો અર્થ છે."),
               H4("Common mistake", "સામાન્ય ભૂલ"),
               P("Treating \"green\" as only about trees and planting drives. Sustainability is a "
                 "balance of environment, society and economy, and an engineering decision that ignores "
                 "any one pillar is not sustainable.",
                 "\"હરિયું\" એટલે ફક્ત વૃક્ષ અને વૃક્ષારોપણ એમ માનવું. ટકાઉપણું એ પર્યાવરણ, સમાજ અને અર્થતંત્ર "
                 "વચ્ચેનું સંતુલન છે, અને કોઈ એક સ્તંભને અવગણતો ઇજનેરી નિર્ણય ટકાઉ ગણાય નહીં.")],
              "u1_pillars", syllabus_item="1.1"),
         card(T("1.2 The structure of an ecosystem", "1.2 પારિતંત્રની રચના"),
              [H4("Definition", "વ્યાખ્યા"),
               P("An <b>ecosystem</b> is a self-regulating unit in which the living community "
                 "(<b>biotic</b> part) interacts with its non-living surroundings (<b>abiotic</b> "
                 "part) and exchanges energy and matter. A pond, a grassland, a mangrove and a city "
                 "park are all ecosystems.",
                 "<b>પારિતંત્ર</b> એ સ્વયં-નિયંત્રિત એકમ છે જેમાં જીવતો સમુદાય (<b>જૈવિક</b> ભાગ) તેની "
                 "નિર્જીવ આસપાસ (<b>અજૈવિક</b> ભાગ) સાથે આંતરક્રિયા કરે અને ઊર્જા તથા દ્રવ્યની આપલે કરે. "
                 "તળાવ, ઘાસનું મેદાન, કાંદલાનું જંગલ અને શહેરી બગીચો - બધાં પારિતંત્ર છે."),
               H4("Components", "ઘટકો"),
               TB([T("Component", "ઘટક"), T("Examples", "ઉદાહરણો"), T("Role", "ભૂમિકા")],
                  [[T("abiotic", "અજૈવિક"), T("light, water, air, soil, minerals, temperature",
                                               "પ્રકાશ, પાણી, હવા, જમીન, ખનિજ, તાપમાન"),
                    T("supply the raw material and the energy", "કાચી સામગ્રી અને ઊર્જા પૂરી પાડે")],
                   [T("producers", "ઉત્પાદક"), T("green plants, algae, phytoplankton",
                                                  "લીલા છોડ, શેવાળ, ફાઇટોપ્લાંકટન"),
                    T("fix sunlight into food", "સૂર્યપ્રકાશને ખોરાકમાં ફેરવે")],
                   [T("consumers", "ઉપભોક્તા"), T("herbivores, carnivores, humans",
                                                    "શાકાહારી, માંસાહારી, માણસ"),
                    T("pass the food energy on", "ખોરાકની ઊર્જા આગળ પહોંચાડે")],
                   [T("decomposers", "વિઘટક"), T("bacteria, fungi, earthworms",
                                                  "જીવાણુ, ફૂગ, અળસિયું"),
                    T("return nutrients to the soil", "પોષક તત્વો જમીનમાં પાછાં આપે")]]),
               H4("Habitat, niche and trophic level", "નિવાસ, નિશાન અને પોષણ સ્તર"),
               UL(("A <b>habitat</b> is the address of an organism; a <b>niche</b> is its job in the "
                    "system - what it eats, when, and who eats it.",
                    "<b>નિવાસ</b> એ જીવનું સરનામું છે; <b>નિશાન</b> એ પ્રણાલીમાં તેનું કામ છે - શું ખાય, "
                    "ક્યારે, અને તેને કોણ ખાય."),
                  ("A <b>trophic level</b> is one step in the food chain: producers are level 1, "
                   "herbivores level 2, and so on.",
                   "<b>પોષણ સ્તર</b> એ ખોરાક શૃંખલાનું એક પગથિયું છે: ઉત્પાદક સ્તર 1, શાકાહારી સ્તર 2, "
                   "એમ આગળ."),
                  ("Two ecosystems next to each other are linked by animals and water, forming a "
                   "<b>landscape</b> or <b>biome</b>.",
                   "પાસપાસેનાં બે પારિતંત્ર પ્રાણીઓ અને પાણીથી જોડાય છે, જેનાથી <b>ભૂદૃશ્ય</b> કે "
                   "<b>બાયોમ</b> બને.")),
               H4("Worked example", "ઉકેલાયેલ દાખલો"),
               P("In a pond, phytoplankton are the producers, zooplankton and small fish the primary "
                 "consumers, and a heron the top consumer; bacteria at the bottom decompose the dead "
                 "fish and return nitrogen and phosphorus to the water - the same nutrients the "
                 "phytoplankton need again.",
                 "તળાવમાં ફાઇટોપ્લાંકટન ઉત્પાદક, ઝૂપ્લાંકટન અને નાની માછલી પ્રાથમિક ઉપભોક્તા અને બગલો "
                 "ટોચનો ઉપભોક્તા છે; તળિયે રહેલા જીવાણુ મરેલી માછલીનું વિઘટન કરી નાઇટ્રોજન અને ફોસ્ફરસ "
                 "પાણીમાં પાછાં આપે - એ જ પોષક તત્વો ફરી ફાઇટોપ્લાંકટનને જોઈએ."),
               H4("Common mistake", "સામાન્ય ભૂલ"),
               P("Calling a group of trees an ecosystem. Without the soil, water, decomposers and "
                 "animals that recycle nutrients, a plantation is only a stand of plants.",
                 "વૃક્ષોના સમૂહને પારિતંત્ર કહેવું. જમીન, પાણી, વિઘટક અને પોષક તત્વો ફરી વાપરતાં પ્રાણી "
                 "વગરનું વાવેતર ફક્ત છોડની હાર છે.")],
              "u1_ecosystem", syllabus_item="1.1"),
         card(T("1.3 How an ecosystem works: energy flow and nutrient cycling",
                "1.3 પારિતંત્ર કેવી રીતે કાર્ય કરે: ઊર્જા પ્રવાહ અને પોષક ચક્ર"),
              [H4("One-way energy, round-trip matter", "ઊર્જા એક દિશામાં, દ્રવ્ય ચક્રમાં"),
               P("Energy enters an ecosystem as sunlight and leaves as heat; it never comes back, so a "
                 "constant supply is needed. Matter - carbon, nitrogen, water - is recycled again and "
                 "again inside the system. This single sentence explains both the food pyramid and the "
                 "need to keep natural cycles intact.",
                 "ઊર્જા પારિતંત્રમાં સૂર્યપ્રકાશ તરીકે આવે અને ઉષ્મા તરીકે નીકળી જાય; તે પાછી આવતી નથી, "
                 "તેથી સતત પુરવઠો જોઈએ. દ્રવ્ય - કાર્બન, નાઇટ્રોજન, પાણી - પ્રણાલીમાં ફરી ફરી ચક્રમાં "
                 "ફરે. આ એક વાક્ય ખોરાકનો પિરામિડ અને કુદરતી ચક્રો સાચવવાની જરૂર - બંને સમજાવે છે."),
               H4("The ten per cent law", "દસ ટકાનો નિયમ"),
               P("Only about <b>10 %</b> of the energy of one trophic level is stored in the next; the "
                 "rest is lost in respiration, movement and heat. Ten thousand joules at the producer "
                 "level give roughly 1000 J to herbivores, 100 J to the first carnivore and 10 J to the "
                 "second - which is why food chains are short and why a meat-rich diet needs far more "
                 "land than a plant diet.",
                 "એક પોષણ સ્તરની ફક્ત લગભગ <b>10 %</b> ઊર્જા આગલા સ્તરમાં સંગ્રહાય; બાકીની શ્વસન, ગતિ અને "
                 "ઉષ્મામાં ખર્ચાય. ઉત્પાદક સ્તરે 10,000 જૂલ હોય તો શાકાહારીને લગભગ 1000 J, પ્રથમ માંસાહારીને "
                 "100 J અને બીજાને 10 J મળે - તેથી જ ખોરાક શૃંખલા ટૂંકી હોય અને માંસાહારી આહારને વનસ્પતિ "
                 "આહાર કરતાં ઘણી વધુ જમીન જોઈએ."),
               H4("Productivity", "ઉત્પાદકતા"),
               TB([T("Term", "શબ્દ"), T("Meaning", "અર્થ"), T("Unit", "એકમ")],
                  [[T("GPP", "GPP"), T("total food made by producers", "ઉત્પાદકો બનાવેલો કુલ ખોરાક"),
                    T("g C/m²/yr", "g C/m²/વર્ષ")],
                   [T("respiration R", "શ્વસન R"), T("food the plants themselves burn",
                                                       "છોડ પોતે વાપરે તે ખોરાક"),
                    T("g C/m²/yr", "g C/m²/વર્ષ")],
                   [T("NPP", "NPP"), T("what is left for the food chain, NPP = GPP - R",
                                       "ખોરાક શૃંખલા માટે બચે તે, NPP = GPP - R"),
                    T("g C/m²/yr", "g C/m²/વર્ષ")]]),
               H4("Ecosystem services", "પારિતંત્ર સેવાઓ"),
               P("Human beings get four kinds of free service: <b>provisioning</b> (food, timber, "
                 "water), <b>regulating</b> (flood control, climate, pollination), <b>cultural</b> "
                 "(recreation, worship) and <b>supporting</b> (soil formation, nutrient cycling). Once "
                 "the system is damaged these services must be paid for with concrete, pumps and "
                 "filters.",
                 "માણસને ચાર પ્રકારની મફત સેવા મળે છે: <b>પુરવઠા</b> (ખોરાક, લાકડું, પાણી), "
                 "<b>નિયમન</b> (પૂર નિયંત્રણ, જળવાયુ, પરાગનયન), <b>સાંસ્કૃતિક</b> (મનોરંજન, પૂજા) અને "
                 "<b>આધાર</b> (જમીન નિર્માણ, પોષક ચક્ર). પ્રણાલી બગડે તો આ સેવાઓ કોંક્રિટ, પંપ અને "
                 "ફિલ્ટરથી ખરીદવી પડે."),
               H4("Common mistake", "સામાન્ય ભૂલ"),
               P("Reversing the pyramid: saying one plant supports ten herbivores. The ten per cent "
                 "law works the other way - many producers are needed for one carnivore, so the number "
                 "and the biomass shrink at every step.",
                 "પિરામિડ ઊંધો સમજવો: એક છોડ દસ શાકાહારીને આધાર આપે એમ કહેવું. દસ ટકાનો નિયમ ઊલટી "
                 "દિશામાં કામ કરે - એક માંસાહારી માટે ઘણા ઉત્પાદક જોઈએ, તેથી દરેક પગથિયે સંખ્યા અને "
                 "બાયોમાસ ઘટે.")],
              "u1_energy", syllabus_item="1.1"),
     ]},
    {"title": T("2. Natural Cycles", "2. કુદરતી ચક્રો"),
     "items": [
         card(T("2.1 The carbon cycle", "2.1 કાર્બન ચક્ર"),
              [H4("Where the carbon is", "કાર્બન ક્યાં રહેલો છે"),
               P("The carbon cycle moves carbon between four reservoirs: the <b>atmosphere</b> as "
                 "carbon dioxide (about 420 ppm, roughly 890 Gt C), the <b>ocean</b> (the largest "
                 "exchangeable store), <b>living biomass and soil</b>, and <b>fossil deposits</b> of "
                 "coal, oil and gas that were buried for millions of years.",
                 "કાર્બન ચક્ર કાર્બનને ચાર ભંડાર વચ્ચે ફેરવે: <b>વાતાવરણ</b> કાર્બન ડાયોક્સાઇડ તરીકે "
                 "(લગભગ 420 ppm, આશરે 890 Gt C), <b>મહાસાગર</b> (સૌથી મોટો વિનિમય ભંડાર), <b>જીવતું "
                 "બાયોમાસ અને જમીન</b>, અને <b>અશ્મિભૂત ભંડાર</b> - કોલસો, તેલ અને ગેસ જે લાખો વર્ષ "
                 "દબાયેલા રહ્યા."),
               H4("The moving parts", "ચક્ર ચલાવતાં પ્રક્રમો"),
               TB([T("Process", "પ્રક્રમ"), T("Direction", "દિશા"), T("What it means", "અર્થ")],
                  [[T("photosynthesis", "પ્રકાશસંશ્લેષણ"), T("air to plant", "હવાથી છોડ તરફ"),
                    T("6CO₂ + 6H₂O to glucose and O₂", "6CO₂ + 6H₂O થી ગ્લુકોઝ અને O₂")],
                   [T("respiration", "શ્વસન"), T("plant to air", "છોડથી હવા તરફ"),
                    T("burns glucose, releases CO₂", "ગ્લુકોઝ બાળે, CO₂ છોડે")],
                   [T("decomposition", "વિઘટન"), T("soil to air", "જમીનથી હવા તરફ"),
                    T("microbes release CO₂ from litter", "જીવાણુ કચરામાંથી CO₂ છોડે")],
                   [T("ocean exchange", "મહાસાગર વિનિમય"), T("both ways", "બંને દિશા"),
                    T("CO₂ dissolves and forms carbonates", "CO₂ ઓગળી કાર્બોનેટ બને")],
                   [T("combustion", "દહન"), T("fossil store to air", "અશ્મિ ભંડારથી હવા તરફ"),
                    T("adds carbon that was out of circulation", "ચક્ર બહાર રહેલો કાર્બન ઉમેરે")]]),
               H4("Why the balance has shifted", "સંતુલન કેમ બદલાયું"),
               P("Nature moves roughly 60 Gt of carbon a year each way between air and land or sea, and "
                 "the two directions almost cancel. Burning fossil fuel adds about <b>10 Gt C a year</b> "
                 "with no matching sink, so the atmospheric stock rises every year - this is the "
                 "physical basis of the greenhouse problem taken up in Unit 4.",
                 "કુદરત હવા અને જમીન કે દરિયા વચ્ચે દર વર્ષે લગભગ 60 Gt કાર્બન બંને દિશામાં ફેરવે અને બંને "
                 "દિશા લગભગ સરખી હોય. અશ્મિ ઇંધણ બાળવાથી દર વર્ષે લગભગ <b>10 Gt C</b> ઉમેરાય છે જેની "
                 "સામે કોઈ શોષક નથી, તેથી વાતાવરણનો ભંડાર દર વર્ષે વધે - આ જ યુનિટ 4માં આવતી હરિતગૃહ "
                 "સમસ્યાનો ભૌતિક આધાર છે."),
               H4("Worked example", "ઉકેલાયેલ દાખલો"),
               P("One hectare of dry deciduous forest adds about 8 t of carbon a year to its biomass. "
                 "That is 8 × 44/12 ≈ 29 t of CO₂ taken out of the air a year - the same as the annual "
                 "emission of seven small cars.",
                 "એક હેક્ટર સૂકું પાનખર જંગલ દર વર્ષે તેના બાયોમાસમાં લગભગ 8 ટન કાર્બન ઉમેરે. તે "
                 "8 × 44/12 ≈ 29 ટન CO₂ દર વર્ષે હવામાંથી લે - સાત નાની મોટરકારના વાર્ષિક ઉત્સર્જન જેટલું."),
               H4("Common mistake", "સામાન્ય ભૂલ"),
               P("Saying trees \"clean\" carbon for ever. A growing tree stores carbon; a mature or "
                 "burnt one gives it back. Only permanent storage - long-life timber, biochar, or "
                 "fossil-free energy - keeps carbon out of the air.",
                 "વૃક્ષો કાયમ કાર્બન \"સાફ\" કરે એમ કહેવું. વધતું વૃક્ષ કાર્બન સંગ્રહે; પુખ્ત કે બળેલું "
                 "વૃક્ષ તેને પાછો આપે. ફક્ત કાયમી સંગ્રહ - લાંબું ટકતું લાકડું, બાયોચાર, કે અશ્મિમુક્ત "
                 "ઊર્જા - કાર્બનને હવાથી દૂર રાખે.")],
              "u1_carbon", syllabus_item="1.2"),
         card(T("2.2 The nitrogen cycle", "2.2 નાઇટ્રોજન ચક્ર"),
              [H4("The problem with nitrogen", "નાઇટ્રોજનની મુશ્કેલી"),
               P("Air is 78 % nitrogen, but as N₂ the two atoms are joined by a triple bond that "
                 "almost no organism can break. The nitrogen cycle is the story of how that inert gas "
                 "is turned into usable ammonia and nitrate, used, and finally returned to the air.",
                 "હવામાં 78 % નાઇટ્રોજન છે, પણ N₂માં બે અણુ ત્રિબંધથી જોડાયેલા હોય છે જે લગભગ કોઈ જીવ "
                 "તોડી શકતું નથી. નાઇટ્રોજન ચક્ર એ વાર્તા છે કે આ નિષ્ક્રિય વાયુને વાપરી શકાય તેવા "
                 "એમોનિયા અને નાઇટ્રેટમાં કેવી રીતે ફેરવાય, વપરાય અને પાછો હવામાં જાય."),
               H4("The five steps", "પાંચ પગથિયાં"),
               OL(("Fixation: lightning, free-living bacteria (Azotobacter), symbiotic Rhizobium in "
                   "legume roots, or the Haber-Bosch plant turn N₂ into NH₃.",
                   "સ્થિરીકરણ: વીજળી, મુક્ત જીવાણુ (એઝોટોબેક્ટર), કઠોળનાં મૂળમાં રહેતો રાઇઝોબિયમ કે "
                   "હેબર-બોશ પ્લાન્ટ N₂ને NH₃માં ફેરવે."),
                  ("Nitrification: Nitrosomonas makes nitrite, Nitrobacter makes nitrate NO₃⁻, the "
                   "form plants absorb.",
                   "નાઇટ્રિફિકેશન: નાઇટ્રોસોમોનસ નાઇટ્રાઇટ અને નાઇટ્રોબેક્ટર નાઇટ્રેટ NO₃⁻ બનાવે, જે "
                   "છોડ શોષે છે."),
                  ("Assimilation: plants build amino acids and proteins; animals get nitrogen by "
                   "eating plants.",
                   "આત્મસાત: છોડ એમિનો એસિડ અને પ્રોટીન બનાવે; પ્રાણીને નાઇટ્રોજન છોડ ખાઈને મળે."),
                  ("Ammonification: decomposers turn dead matter and urine back into ammonia.",
                   "એમોનિફિકેશન: વિઘટક મૃત દ્રવ્ય અને મૂત્રને પાછું એમોનિયામાં ફેરવે."),
                  ("Denitrification: Pseudomonas converts nitrate back to N₂, closing the cycle.",
                   "ડિનાઇટ્રિફિકેશન: સ્યુડોમોનાસ નાઇટ્રેટને પાછું N₂ બનાવે અને ચક્ર પૂરું કરે.")),
               H4("Why it matters to an engineer", "ઇજનેરને કેમ મહત્ત્વનું"),
               UL(("The Haber-Bosch process feeds about half the world but uses 1-2 % of global "
                    "energy and releases CO₂.",
                    "હેબર-બોશ પ્રક્રમ વિશ્વના અડધા લોકોને ખવડાવે, પણ વૈશ્વિક ઊર્જાના 1-2 % જેટલો "
                    "વાપરે અને CO₂ છોડે."),
                  ("Excess fertiliser washes into lakes as nitrate, causing algal bloom and "
                   "eutrophication that strips the water of oxygen.",
                   "વધારાનું ખાતર નાઇટ્રેટ તરીકે સરોવરમાં જાય, જેથી શેવાળનો વિસ્ફોટ અને યુટ્રોફિકેશન "
                   "થાય અને પાણીમાંથી ઓક્સિજન ખતમ થાય."),
                  ("Nitrous oxide from soil is a greenhouse gas about 273 times stronger than CO₂.",
                   "જમીનમાંથી નીકળતો નાઇટ્રસ ઓક્સાઇડ CO₂ કરતાં લગભગ 273 ગણો શક્તિશાળી હરિતગૃહ વાયુ છે."),
                  ("Biological treatment of sewage depends on nitrification and denitrification, so "
                   "the cycle is designed into every STP.",
                   "ગંદા પાણીની જૈવિક સફાઈ નાઇટ્રિફિકેશન અને ડિનાઇટ્રિફિકેશન પર ટકે, તેથી દરેક STPમાં "
                   "આ ચક્ર ડિઝાઇન થાય.")),
               H4("Common mistake", "સામાન્ય ભૂલ"),
               P("Believing plants can use the nitrogen of the air directly. Only after fixation - "
                 "biological or industrial - does nitrogen become available to crops; that is why "
                 "legumes are rotated with cereals.",
                 "છોડ હવાનું નાઇટ્રોજન સીધું વાપરી શકે એમ માનવું. જૈવિક કે ઔદ્યોગિક સ્થિરીકરણ પછી જ "
                 "નાઇટ્રોજન પાકને મળે; તેથી જ કઠોળને અનાજ સાથે ફેરવીને વાવાય છે.")],
              "u1_nitrogen", syllabus_item="1.2"),
         card(T("2.3 The sulphur and phosphorus cycles", "2.3 સલ્ફર અને ફોસ્ફરસ ચક્ર"),
              [H4("The sulphur cycle", "સલ્ફર ચક્ર"),
               P("Sulphur moves between rocks, soil, water and air. Burning coal and smelting ore "
                 "release <b>SO₂</b>; volcanoes and sea spray add more; in the air it becomes sulphate "
                 "and comes down as <b>acid rain</b>. Bacteria such as Desulfovibrio reduce sulphate in "
                 "waterlogged soil to H₂S, the gas that smells of rotten eggs.",
                 "સલ્ફર ખડક, જમીન, પાણી અને હવા વચ્ચે ફરે. કોલસો બાળવાથી અને ધાતુ ગાળવાથી <b>SO₂</b> "
                 "નીકળે; જ્વાળામુખી અને દરિયાના છંટકાવ ઉમેરે; હવામાં તે સલ્ફેટ બની <b>એસિડ વરસાદ</b> "
                 "તરીકે નીચે આવે. ડિસલ્ફોવિબ્રિયો જેવા જીવાણુ પાણીથી ભરેલી જમીનમાં સલ્ફેટને H₂S બનાવે, જે "
                 "સડેલા ઇંડા જેવી ગંધ આપે."),
               H4("The phosphorus cycle", "ફોસ્ફરસ ચક્ર"),
               P("Phosphorus has <b>no gaseous stage</b>: it travels from phosphate rock, through soil "
                 "solution and water, into plants and animals, and back through decomposition and "
                 "sediment. Because it is slow and scarce it is usually the <b>limiting nutrient</b> in "
                 "fresh water.",
                 "ફોસ્ફરસનું <b>વાયુ સ્વરૂપ નથી</b>: તે ફોસ્ફેટ ખડકથી જમીનના દ્રાવણ અને પાણી થઈને "
                 "છોડ તથા પ્રાણીમાં જાય, અને વિઘટન તથા સેડિમેન્ટ દ્વારા પાછો આવે. તે ધીમો અને દુર્લભ "
                 "હોવાથી ગળાયેલા પાણીમાં સામાન્ય રીતે <b>મર્યાદિત પોષક તત્વ</b> હોય."),
               H4("Side by side", "સાથે સરખામણી"),
               TB([T("Point", "મુદ્દો"), T("Sulphur", "સલ્ફર"), T("Phosphorus", "ફોસ્ફરસ")],
                  [[T("main store", "મુખ્ય ભંડાર"), T("rocks and ocean sediment",
                                                      "ખડક અને દરિયાનું સેડિમેન્ટ"),
                    T("phosphate rock", "ફોસ્ફેટ ખડક")],
                   [T("gas phase", "વાયુ સ્વરૂપ"), T("yes, SO₂ and H₂S", "હા, SO₂ અને H₂S"),
                    T("none", "નથી")],
                   [T("human source", "માનવ સ્રોત"), T("coal, smelting", "કોલસો, ધાતુ ગાળવી"),
                    T("fertiliser, detergent, sewage", "ખાતર, ડિટર્જન્ટ, ગંદું પાણી")],
                   [T("pollution effect", "પ્રદૂષણ અસર"), T("acid rain, corrosion",
                                                              "એસિડ વરસાદ, કાટ"),
                    T("eutrophication", "યુટ્રોફિકેશન")]]),
               H4("Worked example", "ઉકેલાયેલ દાખલો"),
               P("A thermal plant burning coal with 0.7 % sulphur, at 2000 t of coal a day, puts out "
                 "about 14 t of sulphur a day, which becomes roughly 28 t of SO₂ - enough to make the "
                 "rain of the surrounding 50 km acidic, which is why a wet scrubber is fitted.",
                 "0.7 % સલ્ફરવાળો કોલસો દિવસે 2000 ટન બાળતો થર્મલ પ્લાન્ટ દિવસે લગભગ 14 ટન સલ્ફર છોડે, જે "
                 "આશરે 28 ટન SO₂ બને - આસપાસના 50 kmનો વરસાદ ઍસિડિક બનાવવા પૂરતું, તેથી જ વેટ સ્ક્રબર "
                 "લગાડાય છે."),
               H4("Common mistake", "સામાન્ય ભૂલ"),
               P("Expecting phosphorus to come back through rain like nitrogen does. With no gas phase "
                 "it can only return through slow rock weathering and sediment, so the phosphate mined "
                 "today is effectively a one-way resource.",
                 "નાઇટ્રોજનની જેમ ફોસ્ફરસ વરસાદથી પાછો આવશે એમ માનવું. વાયુ સ્વરૂપ ન હોવાથી તે ફક્ત ધીમા "
                 "ખડક-ઘસારા અને સેડિમેન્ટ દ્વારા પાછો આવે, તેથી આજે ખણાતો ફોસ્ફેટ ખરેખર એક દિશાનો સ્રોત "
                 "છે.")],
              syllabus_item="1.2"),
     ]},
    {"title": T("3. Biodiversity", "3. જૈવવિવિધતા"),
     "items": [
         card(T("3.1 The levels and value of biodiversity", "3.1 જૈવવિવિધતાનાં સ્તર અને મૂલ્ય"),
              [H4("Definition", "વ્યાખ્યા"),
               P("<b>Biodiversity</b> is the variety of life at three levels: <b>genetic</b> variety "
                 "within a species, <b>species</b> variety within a place, and <b>ecosystem</b> "
                 "variety across the landscape. India, with about 8 % of the world's species on 2.4 % "
                 "of its land, is one of the seventeen <b>megadiverse</b> countries.",
                 "<b>જૈવવિવિધતા</b> એ જીવનની વિવિધતા છે, ત્રણ સ્તરે: એક જાતિની અંદર <b>આનુવંશિક</b> "
                 "વિવિધતા, એક સ્થળમાં <b>જાતિઓની</b> વિવિધતા, અને ભૂદૃશ્યમાં <b>પારિતંત્રોની</b> વિવિધતા. "
                 "ભારત, પોતાની 2.4 % જમીન પર દુનિયાની લગભગ 8 % જાતિઓ ધરાવે છે, તે સત્તર "
                 "<b>મેગાડાઇવર્સ</b> દેશોમાંનો એક છે."),
               H4("Why it is valuable", "તે કેમ મૂલ્યવાન છે"),
               TB([T("Value", "મૂલ્ય"), T("What it gives", "શું આપે"), T("Example", "ઉદાહરણ")],
                  [[T("provisioning", "પુરવઠા"), T("food, fibre, medicine", "ખોરાક, રેસો, દવા"),
                    T("fisheries, herbal drugs", "મત્સ્યઉદ્યોગ, આયુર્વેદિક દવા")],
                   [T("regulating", "નિયમન"), T("climate, water, pollination",
                                                  "જળવાયુ, પાણી, પરાગનયન"),
                    T("mangroves cut storm surge", "કાંદલા તોફાની મોજાં રોકે")],
                   [T("cultural", "સાંસ્કૃતિક"), T("recreation, religion, research",
                                                    "મનોરંજન, ધર્મ, સંશોધન"),
                    T("Gir lion tourism", "ગિર સિંહ પર્યટન")],
                   [T("supporting", "આધાર"), T("soil, nutrients, oxygen",
                                                "જમીન, પોષક તત્વો, ઓક્સિજન"),
                    T("earthworm soil fertility", "અળસિયાથી જમીનની ફળદ્રુપતા")]]),
               H4("Biodiversity of Gujarat", "ગુજરાતની જૈવવિવિધતા"),
               UL(("Asiatic lion in Gir, the only wild population in the world.",
                    "ગિરમાં એશિયાટિક સિંહ, દુનિયાની એકમાત્ર જંગલી વસ્તી."),
                  ("Wild ass in the Little Rann of Kutch and flamingos in the Nal Sarovar.",
                    "નાના રણમાં ઘોરખડ અને નળ સરોવરમાં સુરખાબ."),
                  ("Marine national park at Gulf of Kutch with corals and mangrove creeks.",
                    "કચ્છના અખાતમાં કોરલ અને કાંદલાની ખાડીઓ સાથે દરિયાઈ રાષ્ટ્રીય ઉદ્યાન."),
                  ("About 4 300 flowering plants and 1 100 animal species recorded in the state.",
                    "રાજ્યમાં લગભગ 4 300 ફૂલતા છોડ અને 1 100 પ્રાણી જાતિઓ નોંધાયેલી છે.")),
               H4("Common mistake", "સામાન્ય ભૂલ"),
               P("Judging biodiversity only by the number of big animals. A hectare of mangrove or a "
                 "handful of soil holds more species - and does more work - than a whole herd of "
                 "charismatic mammals.",
                 "જૈવવિવિધતા ફક્ત મોટાં પ્રાણીની સંખ્યાથી માપવી. એક હેક્ટર કાંદલું કે મુઠ્ઠીભર જમીન "
                 "માં ઘણી વધુ જાતિઓ હોય છે - અને ઘણું વધુ કામ કરે છે - એક આખા ટોળા કરતાં.")],
              syllabus_item="1.3"),
         card(T("3.2 Threats to biodiversity", "3.2 જૈવવિવિધતા પરના ભય"),
              [H4("The five main pressures", "પાંચ મુખ્ય દબાણ"),
               TB([T("Threat", "ભય"), T("How it acts", "કેવી રીતે અસર કરે"),
                  T("Local example", "સ્થાનિક ઉદાહરણ")],
                  [[T("habitat loss", "નિવાસનો નાશ"),
                    T("land converted to field, road or town; patches too small to breed",
                      "જમીન ખેતર, રસ્તો કે શહેરમાં ફેરવાય; ટુકડા પ્રજનન માટે નાના પડે"),
                    T("wetland filled for a housing scheme", "ઘર-યોજના માટે પુરાયેલી ભૂમિ")],
                   [T("invasive species", "આક્રમક જાતિઓ"),
                    T("outsiders out-compete natives", "બહારની જાતિ સ્થાનિકને હરાવે"),
                    T("water hyacinth in tanks; Prosopis in grassland",
                      "તળાવમાં વિલાયતી જળકુંભી; ઘાસના મેદાનમાં ગાંડો બાવળ")],
                   [T("pollution", "પ્રદૂષણ"), T("pesticide, plastic, nutrient and noise load",
                                                  "જંતુનાશક, પ્લાસ્ટિક, પોષક તત્વો અને ઘોંઘાટનો ભાર"),
                    T("vulture decline from diclofenac", "ડાયક્લોફેનાકથી ગીધનો ઘટાડો")],
                   [T("over-exploitation", "અતિ-દોહન"),
                    T("hunting, logging, fishing beyond regrowth",
                      "પુનઃવૃદ્ધિથી વધુ શિકાર, કાપ, માછલી પકડ"),
                    T("illegal sand mining in rivers", "નદીમાં ગેરકાયદે રેતી ખનન")],
                   [T("climate change", "જળવાયુ પરિવર્તન"),
                    T("shifts the range faster than species can move",
                      "જાતિ ખસી શકે તેના કરતાં વધુ ઝડપથી વિસ્તાર બદલે"),
                    T("coral bleaching in the Gulf of Kutch", "કચ્છના અખાતમાં કોરલનું ધવલન")]]),
               H4("What the numbers say", "આંકડા શું કહે છે"),
               P("The living planet index of vertebrates has fallen by about 70 % since 1970, and the "
                 "current extinction rate is estimated at a hundred to a thousand times the natural "
                 "background rate. Species are lost long before their habitat disappears completely - "
                 "fragmentation alone can doom a population.",
                 "કરોડરજ્જુવાળા પ્રાણીનો લિવિંગ પ્લેનેટ ઇન્ડેક્સ 1970થી લગભગ 70 % ઘટ્યો છે, અને આજનો "
                 "નાશદર કુદરતી દર કરતાં સો થી હજાર ગણો મનાય છે. નિવાસ પૂરેપૂરો નાશ પામે તે પહેલાં જ જાતિઓ "
                 "ખોવાય છે - ફક્ત વિભાજન પણ વસ્તીને ખતમ કરી શકે."),
               H4("Worked example", "ઉકેલાયેલ દાખલો"),
               P("A forest of 100 km² is cut into ten blocks of 10 km² by roads. The total area is the "
                 "same, but edge-habitat rises from a thin strip to nearly the whole forest, so "
                 "interior species - and any animal needing more than 10 km² - disappear.",
                 "100 km²નું જંગલ રસ્તાથી 10 km²ના દસ ટુકડામાં કપાય. કુલ ક્ષેત્ર એટલું જ રહે, પણ કિનારાનું "
                 "નિવાસ પાતળી પટ્ટીથી લગભગ આખા જંગલ સુધી વધે, તેથી અંદર રહેતી જાતિઓ - અને 10 km²થી વધુ "
                 "જોઈતું કોઈ પણ પ્રાણી - અદૃશ્ય થાય."),
               H4("Common mistake", "સામાન્ય ભૂલ"),
               P("Thinking that planting an equal number of trees compensates for a lost forest. "
                 "Species composition, age, dead wood and soil life take decades to rebuild, and an "
                 "exotic plantation is not a substitute.",
                 "ખોવાયેલા જંગલના બદલે એટલાં જ વૃક્ષ વાવવાથી વળતર મળે એમ માનવું. જાતિઓની રચના, ઉંમર, "
                 "સૂકું લાકડું અને જમીનનું જીવન પાછું બનતાં દાયકાઓ લાગે, અને બહારની જાતિનું વાવેતર "
                 "વિકલ્પ નથી.")],
              syllabus_item="1.3"),
         card(T("3.3 Conservation strategies", "3.3 સંરક્ષણ વ્યૂહરચનાઓ"),
              [H4("Two ways to protect", "બચાવવાની બે રીત"),
               TB([T("Approach", "અભિગમ"), T("What is done", "શું કરાય"),
                  T("Examples", "ઉદાહરણો")],
                  [[T("in-situ", "સ્થાનિક"), T("protect the species inside its own habitat",
                                               "જાતિને તેના જ નિવાસમાં બચાવવી"),
                    T("national park, sanctuary, biosphere reserve, sacred grove",
                      "રાષ્ટ્રીય ઉદ્યાન, અભયારણ્ય, જીવમંડળ અનામત, પવિત્ર વન")],
                   [T("ex-situ", "સ્થાનાંતરિત"), T("keep the species outside its habitat",
                                                    "જાતિને નિવાસ બહાર રાખવી"),
                    T("zoo, botanical garden, seed bank, cryo bank, gene bank",
                      "પ્રાણીસંગ્રહાલય, વનસ્પતિ ઉદ્યાન, બીજ બેંક, ક્રાયો બેંક")],
                   [T("community", "સમુદાય"), T("local people manage and benefit",
                                                 "સ્થાનિક લોકો સંભાળે અને લાભ લે"),
                    T("joint forest management, eco-development committee",
                      "સંયુક્ત વન સંચાલન, પર્યાવરણ વિકાસ સમિતિ")]]),
               H4("The legal backbone in India", "ભારતમાં કાયદાનો આધાર"),
               UL(("Wild Life (Protection) Act 1972 created national parks, sanctuaries and the "
                    "schedule of protected species.",
                    "વન્યજીવ (સંરક્ષણ) અધિનિયમ 1972એ રાષ્ટ્રીય ઉદ્યાન, અભયારણ્ય અને સંરક્ષિત જાતિઓની "
                    "યાદી બનાવી."),
                  ("Forest (Conservation) Act 1980 requires central approval before forest land is "
                   "diverted to any other use.",
                   "વન (સંરક્ષણ) અધિનિયમ 1980 જંગલની જમીન બીજા ઉપયોગમાં લેવા પહેલાં કેન્દ્રની મંજૂરી "
                   "જરૂરી ઠેરવે."),
                  ("Biological Diversity Act 2002 set up the NBA, state boards and Biodiversity "
                   "Management Committees at panchayat level.",
                   "જૈવિક વિવિધતા અધિનિયમ 2002એ NBA, રાજ્ય બોર્ડ અને પંચાયત કક્ષાએ જૈવવિવિધતા "
                   "સંચાલન સમિતિઓ ઊભી કરી."),
                  ("The mitigation hierarchy is the engineering rule: avoid, minimise, restore, and "
                   "only then offset.",
                   "શમન ક્રમ એ ઇજનેરી નિયમ છે: ટાળો, ઘટાડો, પુનઃસ્થાપિત કરો, અને પછી જ વળતર આપો.")),
               H4("Worked example", "ઉકેલાયેલ દાખલો"),
               P("A canal must cross a corridor used by lions. Following the hierarchy, the alignment is "
                 "first shifted (avoid), the crossing is then made underpass-only with fencing "
                 "(minimise), and damaged grass cover is replanted (restore) before any offset land is "
                 "bought.",
                 "એક કેનાલ સિંહના માર્ગને કાપે તેમ છે. ક્રમ પ્રમાણે પહેલાં ગાળો બદલાય (ટાળો), પછી "
                 "ફક્ત અંડરપાસ અને વાડ સાથે પસાર થાય (ઘટાડો), અને નુકસાન પામેલું ઘાસ પાછું વવાય "
                 "(પુનઃસ્થાપન), પછી જ વળતરની જમીન ખરીદાય."),
               H4("Common mistake", "સામાન્ય ભૂલ"),
               P("Assuming a zoo or a seed bank alone saves a species. Ex-situ collections preserve "
                 "genes but lose the ecology; without protecting habitat the species survives only as "
                 "a specimen.",
                 "ફક્ત પ્રાણીસંગ્રહાલય કે બીજ બેંક જાતિને બચાવી લેશે એમ માનવું. સ્થાનાંતરિત સંગ્રહ "
                 "જનીન બચાવે, પણ પરિસ્થિતિ ખોઈ નાખે; નિવાસનું રક્ષણ ન થાય તો જાતિ ફક્ત નમૂના તરીકે "
                 "ટકે.")],
              syllabus_item="1.3"),
     ]},
    {"title": T("4. Micro-project", "4. સૂક્ષ્મ પ્રોજેક્ટ"),
     "items": [
         card(T("Project 1. Poster on the carbon and nitrogen cycles with local examples",
                "પ્રોજેક્ટ 1. સ્થાનિક ઉદાહરણ સાથે કાર્બન અને નાઇટ્રોજન ચક્રનું પોસ્ટર"),
              [H4("Aim", "ઉદ્દેશ"),
               P("Draw both cycles on one A2 sheet and mark where your own town touches them: a "
                 "crematorium or brick kiln as a carbon source, a compost pit or a legume field as a "
                 "nitrogen step, the sewage treatment plant as a place where both cycles meet.",
                 "એક A2 પાના પર બંને ચક્ર દોરો અને તમારું શહેર તેમને ક્યાં સ્પર્શે તે દર્શાવો: ભઠ્ઠી કે "
                 "ચિતા કાર્બન સ્રોત તરીકે, કમ્પોસ્ટ ખાડો કે કઠોળનું ખેતર નાઇટ્રોજન પગથિયા તરીકે, અને "
                 "ગંદા પાણીનો પ્લાન્ટ જ્યાં બંને ચક્ર મળે છે તે સ્થળ તરીકે."),
               H4("Steps", "પગલાં"),
               OL(("Collect three local observations for each cycle with a photograph or a sketch.",
                    "દરેક ચક્ર માટે ત્રણ સ્થાનિક નીરક્ષણ ફોટા કે રેખાચિત્ર સાથે એકઠાં કરો."),
                  ("Show every arrow with its process name: photosynthesis, respiration, "
                   "decomposition, combustion, fixation, nitrification, denitrification.",
                   "દરેક તીર સાથે પ્રક્રમનું નામ લખો: પ્રકાશસંશ્લેષણ, શ્વસન, વિઘટન, દહન, સ્થિરીકરણ, "
                   "નાઇટ્રિફિકેશન, ડિનાઇટ્રિફિકેશન."),
                  ("Estimate one number - for example the CO₂ from your college's monthly LPG or "
                   "diesel use.",
                   "એક આંકડો ગણો - જેમ કે કોલેજના માસિક LPG કે ડીઝલમાંથી નીકળતું CO₂."),
                  ("Add a short paragraph on one action the campus could take.",
                   "કેમ્પસ કરી શકે તેવી એક કાર્યવાહી પર ટૂંકો ફકરો ઉમેરો.")),
               H4("What is assessed", "શું મૂલ્યાંકન પામે"),
               UL(("Correctness of the arrows and of the terms in both cycles.",
                    "બંને ચક્રમાં તીર અને શબ્દોની સચોટતા."),
                  ("Whether local examples are real and specific, not textbook generic.",
                    "સ્થાનિક ઉદાહરણો ખરેખર સ્થાનિક અને ચોક્કસ છે કે ફક્ત પુસ્તકના સામાન્ય."),
                  ("The arithmetic of the one number, with units and a check.",
                    "એક આંકડાનું ગણિત, એકમ અને ચકાસણી સાથે.")),
               H4("Common mistake", "સામાન્ય ભૂલ"),
               P("Copying a printed cycle diagram without arrows for the human-made flows. The whole "
                 "point of the project is to connect the natural cycle to the local, human one.",
                 "છાપેલી આકૃતિ માનવ-નિર્મિત પ્રવાહના તીર વગર ઉતારી લેવી. પ્રોજેક્ટનો આખો ઉદ્દેશ કુદરતી "
                 "ચક્રને સ્થાનિક માનવ ચક્ર સાથે જોડવાનો છે.")],
              syllabus_item="Project.1"),
     ]},
    {"title": T("5. Practice Questions with Model Answers", "5. સરાવ પ્રશ્નો અને આદર્શ જવાબો"),
     "items": []},
]

NUMERICALS = [
    num("u1n01", T("Energy left at the fourth trophic level", "ચોથા પોષણ સ્તરે બચતી ઊર્જા"),
        T("Producers in a grassland fix 4 × 10⁴ kJ of energy. Using the ten per cent law, find the "
          "energy available at the third consumer level.",
          "ઘાસના મેદાનમાં ઉત્પાદકો 4 × 10⁴ kJ ઊર્જા સ્થિર કરે છે. દસ ટકાના નિયમથી ત્રીજા ઉપભોક્તા "
          "સ્તરે મળતી ઊર્જા શોધો."),
        [P("Producers: 40 000 kJ. About 10 % passes to each next level.",
           "ઉત્પાદક: 40 000 kJ. દરેક આગલા સ્તરે લગભગ 10 % પસાર થાય."),
         P("Primary consumer = 40 000 × 0.10 = 4 000 kJ; secondary = 400 kJ; tertiary = 40 kJ.",
           "પ્રાથમિક ઉપભોક્તા = 40 000 × 0.10 = 4 000 kJ; દ્વિતીય = 400 kJ; તૃતીય = 40 kJ."),
         P("Check: 40 kJ is 0.1 % of the producer energy, which is 0.1 × 0.1 × 0.1 - consistent with "
           "three tenfold losses.",
           "ચકાસણી: 40 kJ એ ઉત્પાદક ઊર્જાના 0.1 % છે, જે 0.1 × 0.1 × 0.1 - ત્રણ દસગણા નુકસાન સાથે મળે છે.")],
        T("40 kJ at the third consumer level", "ત્રીજા ઉપભોક્તા સ્તરે 40 kJ")),
    num("u1n02", T("Net primary productivity from GPP", "GPP પરથી ચોખ્ખી પ્રાથમિક ઉત્પાદકતા"),
        T("A wheat field has a gross primary productivity of 1 600 g C/m²/yr and respires 550 "
          "g C/m²/yr. Find its NPP and the share of GPP lost to respiration.",
          "ઘઉંના ખેતરની કુલ પ્રાથમિક ઉત્પાદકતા 1 600 g C/m²/વર્ષ છે અને શ્વસન 550 g C/m²/વર્ષ થાય છે. "
          "તેની NPP અને શ્વસનમાં ખર્ચાતો GPPનો હિસ્સો શોધો."),
        [P("NPP = GPP - R = 1 600 - 550 = 1 050 g C/m²/yr.",
           "NPP = GPP - R = 1 600 - 550 = 1 050 g C/m²/વર્ષ."),
         P("Share respired = 550 / 1 600 = 0.344, that is 34.4 %.",
           "શ્વસનનો હિસ્સો = 550 / 1 600 = 0.344, એટલે કે 34.4 %."),
         P("Check: 34.4 % + 65.6 % = 100 %, and 1 050 g C is what the food chain and the soil can "
           "actually use.",
           "ચકાસણી: 34.4 % + 65.6 % = 100 %, અને 1 050 g C એ જ ખોરાક શૃંખલા તથા જમીન ખરેખર વાપરી શકે.")],
        T("NPP = 1 050 g C/m²/yr; 34.4 % of GPP is respired",
          "NPP = 1 050 g C/m²/વર્ષ; GPPના 34.4 % શ્વસનમાં જાય")),
    num("u1n03", T("Carbon dioxide from a college's electricity", "કોલેજના વીજવપરાશનું કાર્બન ડાયોક્સાઇડ"),
        T("A college uses 3 200 kWh of grid electricity a month. With an emission factor of 0.85 kg "
          "CO₂ per kWh, find the monthly and yearly CO₂ emission.",
          "એક કોલેજ મહિને 3 200 kWh વીજળી વાપરે છે. 0.85 kg CO₂ પ્રતિ kWhના ઉત્સર્જન અંકથી માસિક અને "
          "વાર્ષિક CO₂ ઉત્સર્જન શોધો."),
        [P("Monthly CO₂ = 3 200 × 0.85 = 2 720 kg = 2.72 t.",
           "માસિક CO₂ = 3 200 × 0.85 = 2 720 kg = 2.72 ટન."),
         P("Yearly = 2 720 × 12 = 32 640 kg ≈ 32.6 t CO₂.",
           "વાર્ષિક = 2 720 × 12 = 32 640 kg ≈ 32.6 ટન CO₂."),
         P("Check: 3 200 kWh × 12 = 38 400 kWh, and 38 400 × 0.85 = 32 640 kg, the same value.",
           "ચકાસણી: 3 200 kWh × 12 = 38 400 kWh, અને 38 400 × 0.85 = 32 640 kg, એ જ આંકડો.")],
        T("2.72 t CO₂ a month, about 32.6 t a year", "મહિને 2.72 ટન CO₂, વર્ષે લગભગ 32.6 ટન")),
    num("u1n04", T("Carbon and carbon dioxide are not the same mass", "કાર્બન અને કાર્બન ડાયોક્સાઇડનું દળ સરખું નથી"),
        T("A forest survey reports that a plantation stores 12 t of carbon. What mass of CO₂ does that "
          "carbon represent?",
          "વન સર્વે કહે છે કે એક વાવેતર 12 ટન કાર્બન સંગ્રહે છે. એ કાર્બન કેટલા દળના CO₂ બરાબર છે?"),
        [P("CO₂ has molar mass 44 and carbon 12, so 1 t C = 44/12 = 3.667 t CO₂.",
           "CO₂નું મૉલર દળ 44 અને કાર્બનનું 12, તેથી 1 ટન C = 44/12 = 3.667 ટન CO₂."),
         P("CO₂ equivalent = 12 × 3.667 = 44.0 t CO₂.",
           "CO₂ સમાન = 12 × 3.667 = 44.0 ટન CO₂."),
         P("Check: 44 t CO₂ contains 44 × 12/44 = 12 t of carbon, which returns the given value.",
           "ચકાસણી: 44 ટન CO₂માં 44 × 12/44 = 12 ટન કાર્બન છે, જે આપેલું મૂલ્ય પાછું આપે.")],
        T("44 t of CO₂ equivalent", "44 ટન CO₂ સમાન")),
    num("u1n05", T("Ecological footprint of a town", "શહેરની પારિસ્થિતિકી પગથિયું"),
        T("A town of 2.0 lakh people has a per capita ecological footprint of 1.8 gha. The land "
          "available to it has a biocapacity of 0.4 gha per person. Find the total footprint, the "
          "total biocapacity and the deficit.",
          "2.0 લાખ લોકોના શહેરની માથાદીઠ પારિસ્થિતિકી પગથિયું 1.8 gha છે. તેને ઉપલબ્ધ જમીનની વહેંચણી "
          "ક્ષમતા 0.4 gha પ્રતિ વ્યક્તિ છે. કુલ પગથિયું, કુલ ક્ષમતા અને ખાદ્યાન્ન શોધો."),
        [P("Population = 2 00 000. Total footprint = 2 00 000 × 1.8 = 3 60 000 gha.",
           "વસ્તી = 2 00 000. કુલ પગથિયું = 2 00 000 × 1.8 = 3 60 000 gha."),
         P("Total biocapacity = 2 00 000 × 0.4 = 80 000 gha.",
           "કુલ ક્ષમતા = 2 00 000 × 0.4 = 80 000 gha."),
         P("Deficit = 3 60 000 - 80 000 = 2 80 000 gha; the town runs at 4.5 times its own land.",
           "ખાદ્યાન્ન = 3 60 000 - 80 000 = 2 80 000 gha; શહેર પોતાની જમીન કરતાં 4.5 ગણું વાપરે છે."),
         P("Check: 1.8 / 0.4 = 4.5, so the ratio of footprint to biocapacity is 4.5 - consistent.",
           "ચકાસણી: 1.8 / 0.4 = 4.5, તેથી પગથિયા અને ક્ષમતાનો ગુણોત્તર 4.5 - સુસંગત.")],
        T("Footprint 3.6 lakh gha, capacity 0.8 lakh gha, deficit 2.8 lakh gha",
          "પગથિયું 3.6 લાખ gha, ક્ષમતા 0.8 લાખ gha, ખાદ્યાન્ન 2.8 લાખ gha")),
    num("u1n06", T("How much CO₂ one hectare of forest takes up", "એક હેક્ટર જંગલ કેટલું CO₂ લે"),
        T("A dry deciduous forest adds 8 t C/ha/yr to its biomass. Find the CO₂ removed from the air "
          "per hectare per year, and the area needed to absorb 1 000 t CO₂ a year.",
          "સૂકું પાનખર જંગલ વર્ષે 8 ટન C/ha તેના બાયોમાસમાં ઉમેરે છે. પ્રતિ હેક્ટર પ્રતિ વર્ષ હવામાંથી "
          "લેવાતું CO₂ અને વર્ષે 1 000 ટન CO₂ શોષવા જરૂરી ક્ષેત્ર શોધો."),
        [P("CO₂ = 8 × 44/12 = 29.3 t CO₂/ha/yr.",
           "CO₂ = 8 × 44/12 = 29.3 ટન CO₂/ha/વર્ષ."),
         P("Area for 1 000 t = 1 000 / 29.3 = 34.1 ha, about 34 hectares.",
           "1 000 ટન માટે ક્ષેત્ર = 1 000 / 29.3 = 34.1 ha, લગભગ 34 હેક્ટર."),
         P("Check: 34 ha × 29.3 = 996 t, within rounding of the target.",
           "ચકાસણી: 34 ha × 29.3 = 996 ટન, રાઉન્ડિંગની અંદર લક્ષ્યની નજીક.")],
        T("29.3 t CO₂/ha/yr; about 34 ha for 1 000 t a year",
          "29.3 ટન CO₂/ha/વર્ષ; વર્ષે 1 000 ટન માટે લગભગ 34 હેક્ટર")),
    num("u1n07", T("Overall efficiency of a four-level food chain", "ચાર સ્તરની ખોરાક શૃંખલાની કુલ કાર્યક્ષમતા"),
        T("Producers fix 2 × 10⁵ kJ and the top carnivore receives 200 kJ. Find the overall transfer "
          "efficiency and comment on the result.",
          "ઉત્પાદક 2 × 10⁵ kJ સ્થિર કરે અને ટોચનો માંસાહારી 200 kJ મેળવે. કુલ સ્થાનાંતરણ કાર્યક્ષમતા શોધો "
          "અને પરિણામ પર ટિપ્પણી કરો."),
        [P("Efficiency = (200 / 2 00 000) × 100 = 0.1 %.",
           "કાર્યક્ષમતા = (200 / 2 00 000) × 100 = 0.1 %."),
         P("Three steps of 10 % give 0.1 × 0.1 × 0.1 = 0.001, so the value agrees with the ten per "
           "cent law.",
           "10 %ના ત્રણ પગથિયાં 0.1 × 0.1 × 0.1 = 0.001 આપે, તેથી મૂલ્ય દસ ટકાના નિયમ સાથે મળે છે."),
         P("Comment: a long food chain wastes energy, so eating lower on the chain feeds more people "
           "from the same land.",
           "ટિપ્પણી: લાંબી ખોરાક શૃંખલા ઊર્જા વેડફે, તેથી શૃંખલામાં નીચે ખાવાથી એ જ જમીનમાંથી વધુ લોકોને "
           "ખવડાવી શકાય.")],
        T("0.1 % overall; three tenfold losses", "કુલ 0.1 %; ત્રણ દસગણા નુકસાન")),
    num("u1n08", T("Carbon stock of a forest stand", "જંગલના સ્ટેન્ડનો કાર્બન ભંડાર"),
        T("A 50 ha plantation has 120 t/ha of above-ground biomass and a carbon fraction of 0.47. "
          "Find the carbon stock and its CO₂ equivalent.",
          "50 હેક્ટરના વાવેતરમાં 120 ટન/ha ઉપરનું બાયોમાસ અને 0.47 કાર્બન અંશ છે. કાર્બન ભંડાર અને તેનું "
          "CO₂ સમાન શોધો."),
        [P("Carbon per hectare = 120 × 0.47 = 56.4 t C/ha.",
           "પ્રતિ હેક્ટર કાર્બન = 120 × 0.47 = 56.4 ટન C/ha."),
         P("Total carbon = 56.4 × 50 = 2 820 t C.",
           "કુલ કાર્બન = 56.4 × 50 = 2 820 ટન C."),
         P("CO₂ equivalent = 2 820 × 44/12 = 10 340 t CO₂.",
           "CO₂ સમાન = 2 820 × 44/12 = 10 340 ટન CO₂.")],
        T("2 820 t C, equal to 10 340 t CO₂", "2 820 ટન C, જે 10 340 ટન CO₂ બરાબર")),
    num("u1n09", T("Per capita emission from a national total", "રાષ્ટ્રીય કુલમાંથી માથાદીઠ ઉત્સર્જન"),
        T("A country emits 2.9 Gt CO₂ a year with a population of 1.42 billion. Find the per capita "
          "emission and compare it with the world average of 4.7 t per person.",
          "એક દેશ વર્ષે 2.9 Gt CO₂ છોડે છે અને તેની વસ્તી 1.42 અબજ છે. માથાદીઠ ઉત્સર્જન શોધો અને વિશ્વના "
          "સરેરાશ 4.7 ટન પ્રતિ વ્યક્તિ સાથે સરખાવો."),
        [P("2.9 Gt = 2.9 × 10⁹ t; population = 1.42 × 10⁹.",
           "2.9 Gt = 2.9 × 10⁹ ટન; વસ્તી = 1.42 × 10⁹."),
         P("Per capita = 2.9 × 10⁹ / 1.42 × 10⁹ = 2.04 t CO₂ per person per year.",
           "માથાદીઠ = 2.9 × 10⁹ / 1.42 × 10⁹ = 2.04 ટન CO₂ પ્રતિ વ્યક્તિ પ્રતિ વર્ષ."),
         P("Comparison: 2.04 / 4.7 = 0.43, so the country is at 43 % of the world average.",
           "સરખામણી: 2.04 / 4.7 = 0.43, તેથી દેશ વિશ્વ સરેરાશના 43 % પર છે.")],
        T("2.04 t CO₂ per person per year, 43 % of the world average",
          "માથાદીઠ 2.04 ટન CO₂ પ્રતિ વર્ષ, વિશ્વ સરેરાશના 43 %")),
    num("u1n10", T("Water footprint of a cotton T-shirt", "સૂતરના ટી-શર્ટની જળ પગથિયું"),
        T("Growing 1 kg of cotton needs about 10 000 L of water. A T-shirt weighs 250 g. Find the "
          "water behind one shirt and the number of shirts that a 1 000 m³ tank could supply.",
          "1 કિલો કપાસ ઉગાડવા લગભગ 10 000 લિટર પાણી જોઈએ. એક ટી-શર્ટનું વજન 250 ગ્રામ છે. એક શર્ટ પાછળનું "
          "પાણી અને 1 000 m³ ટાંકી કેટલા શર્ટ પૂરી શકે તે શોધો."),
        [P("Water per shirt = 10 000 × 0.25 = 2 500 L.",
           "એક શર્ટ માટે પાણી = 10 000 × 0.25 = 2 500 લિટર."),
         P("Tank volume = 1 000 m³ = 10 00 000 L.",
           "ટાંકીનું ઘનફળ = 1 000 m³ = 10 00 000 લિટર."),
         P("Shirts = 10 00 000 / 2 500 = 400 shirts.",
           "શર્ટ = 10 00 000 / 2 500 = 400 શર્ટ."),
         P("Check: 400 × 2 500 L = 10 00 000 L = 1 000 m³, the whole tank.",
           "ચકાસણી: 400 × 2 500 લિટર = 10 00 000 લિટર = 1 000 m³, આખી ટાંકી.")],
        T("2 500 L per shirt; a 1 000 m³ tank is 400 shirts", "પ્રતિ શર્ટ 2 500 લિટર; 1 000 m³ ટાંકી 400 શર્ટ")),
]

EQUATIONS = [
    {"title": T("Ecosystem energy", "પારિતંત્રની ઊર્જા"),
     "items": [
         {"name": T("Ten per cent law", "દસ ટકાનો નિયમ"), "f": "E(n+1) = 0.1 × E(n)",
          "terms": T("Only about a tenth of the energy reaches the next trophic level.",
                     "લગભગ દશમાંશ ઊર્જા જ આગલા પોષણ સ્તરે પહોંચે.")},
         {"name": T("Net primary productivity", "ચોખ્ખી પ્રાથમિક ઉત્પાદકતા"), "f": "NPP = GPP − R",
          "terms": T("GPP is what the producers make, R is what they respire.",
                     "GPP ઉત્પાદકો બનાવે તે, R તેઓ શ્વસનમાં વાપરે તે.")},
         {"name": T("Trophic transfer efficiency", "પોષણ સ્તર સ્થાનાંતરણ કાર્યક્ષમતા"),
          "f": "η = (E_out / E_in) × 100 %",
          "terms": T("Energy stored at one level divided by the energy it received.",
                     "એક સ્તરે સંગ્રહાયેલી ઊર્જા ભાગ્યા તેને મળેલી ઊર્જા.")},
     ]},
    {"title": T("Carbon and footprint accounting", "કાર્બન અને પગથિયાનો હિસાબ"),
     "items": [
         {"name": T("Carbon to carbon dioxide", "કાર્બનથી કાર્બન ડાયોક્સાઇડ"),
          "f": "m(CO₂) = m(C) × 44/12",
          "terms": T("44 is the molar mass of CO₂ and 12 that of carbon.",
                     "44 એ CO₂નું અને 12 કાર્બનનું મૉલર દળ છે.")},
         {"name": T("Carbon stock", "કાર્બન ભંડાર"), "f": "C = biomass × carbon fraction",
          "terms": T("The carbon fraction of dry wood and foliage is about 0.47.",
                     "સૂકા લાકડા અને પાનનો કાર્બન અંશ લગભગ 0.47 હોય.")},
         {"name": T("Emission from electricity", "વીજળીમાંથી ઉત્સર્જન"),
          "f": "CO₂ = kWh × emission factor",
          "terms": T("The Indian grid factor is about 0.71-0.85 kg CO₂ per kWh.",
                     "ભારતીય ગ્રિડનો અંક લગભગ 0.71-0.85 kg CO₂ પ્રતિ kWh છે.")},
         {"name": T("Per capita emission", "માથાદીઠ ઉત્સર્જન"),
          "f": "e = E_total / population",
          "terms": T("Used to compare countries of very different size.",
                     "ઘણા જુદા કદના દેશોની સરખામણી માટે વપરાય.")},
         {"name": T("Ecological deficit", "પારિસ્થિતિકી ખાદ્યાન્ન"),
          "f": "deficit = footprint − biocapacity",
          "terms": T("A positive value means the place imports land from elsewhere.",
                     "ધન મૂલ્ય એટલે તે સ્થળ બીજે ઠેકાણેથી જમીન આયાત કરે છે.")},
     ]},
]

VIVA = [
    {"title": T("Sustainability and ecosystems", "ટકાઉપણું અને પારિતંત્ર"),
     "items": [
         {"q": T("Define sustainability and sustainable development.",
                 "ટકાઉપણું અને ટકાઉ વિકાસની વ્યાખ્યા આપો."),
          "a": T("Sustainability is the ability of a system to keep working indefinitely without "
                 "exhausting the resources or natural capital it depends on. Sustainable development "
                 "meets the needs of the present without compromising the ability of future "
                 "generations to meet their own needs (Brundtland, 1987).",
                 "ટકાઉપણું એ પ્રણાલીની ક્ષમતા છે કે તે પોતાના આધારભૂત સ્રોતો કે કુદરતી મૂડી ખતમ કર્યા વગર "
                 "અનંત ચાલે. ટકાઉ વિકાસ આજની જરૂરિયાત પૂરી કરે, પણ આવનારી પેઢીની ક્ષમતાને નુકસાન ન "
                 "પહોંચાડે (બ્રુન્ટલેન્ડ, 1987).")},
         {"q": T("Name the three pillars of sustainability and give one engineering example of each.",
                 "ટકાઉપણાના ત્રણ સ્તંભ જણાવો અને દરેકનું એક ઇજનેરી ઉદાહરણ આપો."),
          "a": T("Environmental - a factory's effluent plant keeps the river clean; social - the same "
                 "plant protects the health of the villagers downstream; economic - the recovered "
                 "water is reused, so the plant pays part of its own cost.",
                 "પર્યાવરણીય - ફેક્ટરીનો ઇફ્લુઅન્ટ પ્લાન્ટ નદી સ્વચ્છ રાખે; સામાજિક - એ જ પ્લાન્ટ નીચે "
                 "વસતા લોકોનું આરોગ્ય બચાવે; આર્થિક - સાફ કરેલું પાણી ફરી વપરાય, તેથી પ્લાન્ટ પોતાનો "
                 "ખર્ચનો ભાગ કાઢે.")},
         {"q": T("What is an ecosystem? Name its four components.",
                 "પારિતંત્ર એટલે શું? તેના ચાર ઘટકો જણાવો."),
          "a": T("An ecosystem is a self-regulating unit where a living community interacts with its "
                 "non-living surroundings. Its components are abiotic matter, producers, consumers "
                 "and decomposers.",
                 "પારિતંત્ર એ સ્વયં-નિયંત્રિત એકમ છે જ્યાં જીવતો સમુદાય નિર્જીવ આસપાસ સાથે આંતરક્રિયા "
                 "કરે. તેના ઘટકો અજૈવિક દ્રવ્ય, ઉત્પાદક, ઉપભોક્તા અને વિઘટક છે.")},
         {"q": T("Why are food chains short? State the ten per cent law.",
                 "ખોરાક શૃંખલા ટૂંકી કેમ હોય? દસ ટકાનો નિયમ જણાવો."),
          "a": T("Because only about 10 % of the energy of one trophic level is stored in the next; "
                 "the rest is lost as heat in respiration and movement. After four or five steps so "
                 "little energy is left that no further level can be supported.",
                 "કારણ કે એક પોષણ સ્તરની ફક્ત લગભગ 10 % ઊર્જા આગલા સ્તરમાં સંગ્રહાય; બાકીની શ્વસન અને "
                 "ગતિમાં ઉષ્મા તરીકે ખર્ચાય. ચાર-પાંચ પગથિયા પછી એટલી ઓછી ઊર્જા બચે કે આગલું સ્તર ટકી "
                 "શકે નહીં.")},
     ]},
    {"title": T("Natural cycles", "કુદરતી ચક્રો"),
     "items": [
         {"q": T("List the processes of the carbon cycle that remove CO₂ from the air.",
                 "કાર્બન ચક્રની કઈ પ્રક્રિયાઓ હવામાંથી CO₂ દૂર કરે તે જણાવો."),
          "a": T("Photosynthesis by plants, algae and phytoplankton; dissolution of CO₂ in ocean "
                 "water; and, on a geological timescale, the formation of carbonate shells and fossil "
                 "deposits.",
                 "છોડ, શેવાળ અને ફાઇટોપ્લાંકટનનું પ્રકાશસંશ્લેષણ; દરિયાના પાણીમાં CO₂નું ઓગળવું; અને "
                 "ભૂસ્તરીય સમયમાપક્રમે કાર્બોનેટ કવચ તથા અશ્મિ ભંડારનું બનવું.")},
         {"q": T("Why can plants not use the nitrogen of the air directly?",
                 "છોડ હવાનું નાઇટ્રોજન સીધું કેમ વાપરી શકતા નથી?"),
          "a": T("Because the two nitrogen atoms in N₂ are held by a strong triple bond that plant "
                 "enzymes cannot break. Nitrogen must first be fixed into ammonia or nitrate by "
                 "bacteria, lightning or the Haber-Bosch process.",
                 "કારણ કે N₂માં બે નાઇટ્રોજન અણુ મજબૂત ત્રિબંધથી જોડાયેલા છે જે છોડના ઉત્સેચક તોડી શકતા "
                 "નથી. નાઇટ્રોજન પહેલાં જીવાણુ, વીજળી કે હેબર-બોશ પ્રક્રમથી એમોનિયા કે નાઇટ્રેટમાં "
                 "સ્થિર થવું પડે.")},
         {"q": T("How is the phosphorus cycle different from the carbon cycle?",
                 "ફોસ્ફરસ ચક્ર કાર્બન ચક્રથી કેવી રીતે જુદું છે?"),
          "a": T("Phosphorus has no gaseous phase: it moves only through rock weathering, soil, water, "
                 "organisms and sediment. The cycle is therefore slow and the resource is effectively "
                 "one-way, while carbon circulates through the atmosphere quickly.",
                 "ફોસ્ફરસનું વાયુ સ્વરૂપ નથી: તે ફક્ત ખડક-ઘસારા, જમીન, પાણી, જીવો અને સેડિમેન્ટ દ્વારા "
                 "ચાલે. તેથી ચક્ર ધીમું અને સ્રોત અસરકારક રીતે એક દિશાનો છે, જ્યારે કાર્બન વાતાવરણ "
                 "દ્વારા ઝડપથી ફરે છે.")},
         {"q": T("What is acid rain and which cycle produces it?",
                 "એસિડ વરસાદ એટલે શું અને કયું ચક્ર તેને જન્મ આપે?"),
          "a": T("Acid rain is rain with pH below about 5.6, formed when SO₂ and nitrogen oxides "
                 "dissolve in cloud water and become sulphuric and nitric acid. For SO₂ the sulphur "
                 "cycle is responsible; coal burning and ore smelting are the main sources.",
                 "એસિડ વરસાદ એ લગભગ 5.6થી નીચે pHવાળો વરસાદ છે, જે ત્યારે બને જ્યારે SO₂ અને નાઇટ્રોજન "
                 "ઓક્સાઇડ વાદળના પાણીમાં ઓગળી સલ્ફ્યુરિક અને નાઇટ્રિક ઍસિડ બને. SO₂ માટે સલ્ફર ચક્ર "
                 "જવાબદાર છે; કોલસો બાળવો અને ધાતુ ગાળવી મુખ્ય સ્રોત છે.")},
         {"q": T("What is eutrophication and which nutrient usually causes it?",
                 "યુટ્રોફિકેશન એટલે શું અને સામાન્ય રીતે કયું પોષક તત્વ તેને કારણે છે?"),
          "a": T("Eutrophication is over-enrichment of a water body with nutrients, causing an algal "
                 "bloom; the algae die, decompose and consume the dissolved oxygen, killing fish. In "
                 "fresh water phosphorus is usually the limiting nutrient that triggers it.",
                 "યુટ્રોફિકેશન એ જળાશયમાં પોષક તત્વોનું અતિ-સંવર્ધન છે, જેનાથી શેવાળનો વિસ્ફોટ થાય; "
                 "શેવાળ મરીને સડે અને ઓગળેલો ઓક્સિજન વાપરી નાખે, જેથી માછલી મરે. ગળાયેલા પાણીમાં "
                 "સામાન્ય રીતે ફોસ્ફરસ જ મર્યાદિત પોષક તત્વ હોય છે.")},
     ]},
    {"title": T("Biodiversity", "જૈવવિવિધતા"),
     "items": [
         {"q": T("What are the three levels of biodiversity?",
                 "જૈવવિવિધતાનાં ત્રણ સ્તર કયાં છે?"),
          "a": T("Genetic diversity within a species, species diversity within a community, and "
                 "ecosystem diversity across a landscape.",
                 "એક જાતિની અંદર આનુવંશિક વિવિધતા, સમુદાયમાં જાતિઓની વિવિધતા, અને ભૂદૃશ્યમાં "
                 "પારિતંત્રોની વિવિધતા.")},
         {"q": T("Name four ecosystem services with one example each.",
                 "ચાર પારિતંત્ર સેવાઓ દરેકનું એક ઉદાહરણ આપીને જણાવો."),
          "a": T("Provisioning - fish from a lake; regulating - mangroves reducing a storm surge; "
                 "cultural - a pilgrimage grove; supporting - earthworms building soil fertility.",
                 "પુરવઠા - તળાવની માછલી; નિયમન - તોફાની મોજાં ઘટાડતાં કાંદલાં; સાંસ્કૃતિક - યાત્રાધામનું "
                 "વન; આધાર - જમીનની ફળદ્રુપતા બનાવતું અળસિયું.")},
         {"q": T("Give the five main threats to biodiversity.",
                 "જૈવવિવિધતા પરના પાંચ મુખ્ય ભય જણાવો."),
          "a": T("Habitat loss and fragmentation, invasive alien species, pollution, "
                 "over-exploitation of species, and climate change.",
                 "નિવાસનો નાશ અને વિભાજન, આક્રમક બહારની જાતિઓ, પ્રદૂષણ, જાતિઓનું અતિ-દોહન, અને જળવાયુ "
                 "પરિવર્તન.")},
         {"q": T("Distinguish in-situ and ex-situ conservation.",
                 "સ્થાનિક અને સ્થાનાંતરિત સંરક્ષણમાં ભેદ આપો."),
          "a": T("In-situ conservation protects a species inside its own habitat - national parks, "
                 "sanctuaries, biosphere reserves and sacred groves. Ex-situ keeps it outside the "
                 "habitat - zoos, botanical gardens, seed and cryo banks - which preserves genes but "
                 "not the ecology.",
                 "સ્થાનિક સંરક્ષણ જાતિને તેના જ નિવાસમાં બચાવે - રાષ્ટ્રીય ઉદ્યાન, અભયારણ્ય, જીવમંડળ "
                 "અનામત અને પવિત્ર વન. સ્થાનાંતરિત તેને નિવાસ બહાર રાખે - પ્રાણીસંગ્રહાલય, વનસ્પતિ "
                 "ઉદ્યાન, બીજ અને ક્રાયો બેંક - જે જનીન બચાવે, પણ પરિસ્થિતિ નહીં.")},
         {"q": T("Which two Acts of India deal directly with wildlife and forest land?",
                 "ભારતના કયા બે અધિનિયમ વન્યજીવ અને જંગલની જમીન સાથે સીધા સંબંધિત છે?"),
          "a": T("The Wild Life (Protection) Act 1972, which created protected areas and the schedule "
                 "of species, and the Forest (Conservation) Act 1980, which needs central approval "
                 "before forest land is used for anything else.",
                 "વન્યજીવ (સંરક્ષણ) અધિનિયમ 1972, જેણે સંરક્ષિત ક્ષેત્રો અને જાતિઓની યાદી બનાવી, અને વન "
                 "(સંરક્ષણ) અધિનિયમ 1980, જે જંગલની જમીન બીજા ઉપયોગમાં લેવા પહેલાં કેન્દ્રની મંજૂરી "
                 "માગે છે.")},
     ]},
]

_PRACTICE = [
    (T("Define sustainability, sustainable development and the three pillars it stands on.",
       "ટકાઉપણું, ટકાઉ વિકાસ અને તેના ત્રણ સ્તંભોની વ્યાખ્યા આપો."),
     4,
     [P("Sustainability is the ability of a system to continue indefinitely without exhausting the "
        "resources or natural capital on which it depends; sustainable development applies that idea "
        "to human progress.",
        "ટકાઉપણું એ પ્રણાલીની અનંત ચાલવાની ક્ષમતા છે, જે તેના આધારભૂત સ્રોતો કે કુદરતી મૂડી ખતમ કર્યા વગર "
        "શક્ય બને; ટકાઉ વિકાસ એ જ વિચારને માનવ પ્રગતિ પર લાગુ કરે છે."),
      P("The Brundtland Commission (1987) defined it as development that meets the needs of the "
        "present without compromising the ability of future generations to meet their own needs.",
        "બ્રુન્ટલેન્ડ આયોગ (1987)એ તેને આજની જરૂરિયાત પૂરી કરતો, પણ આવનારી પેઢીની ક્ષમતાને નુખસાન ન "
        "પહોંચાડતો વિકાસ કહ્યો."),
      P("It stands on three pillars that must hold together: environmental (healthy air, water, soil "
        "and biodiversity), social (health, education and equity) and economic (the activity pays for "
        "itself over its whole life).",
        "તે ત્રણ સ્તંભ પર ઊભું છે જે એકસાથે ટકવા જોઈએ: પર્યાવરણીય (સ્વસ્થ હવા, પાણી, જમીન અને "
        "જૈવવિવિધતા), સામાજિક (આરોગ્ય, શિક્ષણ અને સમાનતા) અને આર્થિક (પ્રવૃત્તિ આખા જીવનકાળ દરમિયાન "
        "પોતાનો ખર્ચ કાઢે)."),
      P("For a diploma engineer the pillars become concrete: a motor of the right size, scrap "
        "segregated at the machine, effluent treated before it leaves the gate, and a design that can "
        "be repaired rather than replaced.",
        "ડિપ્લોમા ઇજનેર માટે સ્તંભો મૂર્ત બને છે: યોગ્ય માપનું મોટર, મશીન પાસે અલગ કરેલો સ્ક્રેપ, "
        "ગેટ છોડતાં પહેલાં સાફ કરેલું ગંદું પાણી, અને બદલવાને બદલે સમારી શકાય તેવી ડિઝાઇન.")]),
    (T("Explain the structure and function of an ecosystem with a pond as the example.",
       "તળાવના ઉદાહરણ સાથે પારિતંત્રની રચના અને કાર્ય સમજાવો."),
     4,
     [P("An ecosystem is a self-regulating unit in which a living community interacts with its "
        "non-living surroundings and exchanges energy and matter. Its structure has two halves: the "
        "abiotic part (light, water, air, soil, minerals, temperature) and the biotic part.",
        "પારિતંત્ર એ સ્વયં-નિયંત્રિત એકમ છે જ્યાં જીવતો સમુદાય નિર્જીવ આસપાસ સાથે આંતરક્રિયા કરી ઊર્જા "
        "અને દ્રવ્યની આપલે કરે. તેની રચનાના બે ભાગ છે: અજૈવિક (પ્રકાશ, પાણી, હવા, જમીન, ખનિજ, તાપમાન) "
        "અને જૈવિક."),
      P("The biotic part has producers (phytoplankton), consumers (zooplankton, small fish, heron) and "
        "decomposers (bacteria at the bottom); together they form trophic levels, and each organism "
        "has a habitat and a niche.",
        "જૈવિક ભાગમાં ઉત્પાદક (ફાઇટોપ્લાંકટન), ઉપભોક્તા (ઝૂપ્લાંકટન, નાની માછલી, બગલો) અને વિઘટક (તળિયાના "
        "જીવાણુ) આવે; તે મળીને પોષણ સ્તર બનાવે, અને દરેક જીવનું નિવાસ તથા નિશાન હોય."),
      P("Function means energy flow and nutrient cycling: sunlight is fixed by photosynthesis, about "
        "10 % passes to each next level and the rest leaves as heat, while carbon, nitrogen and "
        "phosphorus are recycled by decomposers.",
        "કાર્ય એટલે ઊર્જા પ્રવાહ અને પોષક ચક્ર: પ્રકાશસંશ્લેષણ સૂર્યપ્રકાશ સ્થિર કરે, લગભગ 10 % દરેક "
        "આગલા સ્તરે જાય અને બાકીની ઉષ્મા તરીકે નીકળે, જ્યારે કાર્બન, નાઇટ્રોજન અને ફોસ્ફરસ વિઘટકો "
        "દ્વારા ફરી વપરાય."),
      P("The pond therefore delivers ecosystem services - fish, water purification, habitat - and "
        "stops delivering them the moment the nutrient load or the oxygen balance is disturbed.",
        "તેથી તળાવ પારિતંત્ર સેવાઓ આપે - માછલી, પાણીની શુદ્ધિ, નિવાસ - અને પોષક ભાર કે ઓક્સિજનનું "
        "સંતુલન બગડે ત્યારે આપવાનું બંધ કરે.")]),
    (T("Describe the carbon cycle and explain how human activity has disturbed its balance.",
       "કાર્બન ચક્ર વર્ણવો અને માનવ પ્રવૃત્તિએ તેનું સંતુલન કેવી રીતે બગાડ્યું તે સમજાવો."),
     5,
     [P("Carbon is exchanged between four reservoirs: the atmosphere (about 890 Gt C as CO₂), the "
        "ocean, living biomass and soil, and fossil deposits. Photosynthesis takes CO₂ into plants, "
        "respiration and decomposition return it, and the ocean absorbs and releases it as dissolved "
        "CO₂ and carbonates.",
        "કાર્બન ચાર ભંડાર વચ્ચે ફરે છે: વાતાવરણ (CO₂ તરીકે લગભગ 890 Gt C), મહાસાગર, જીવતું બાયોમાસ અને "
        "જમીન, અને અશ્મિ ભંડાર. પ્રકાશસંશ્લેષણ CO₂ને છોડમાં લે, શ્વસન અને વિઘટન તેને પાછું આપે, અને "
        "મહાસાગર ઓગળેલા CO₂ તથા કાર્બોનેટ તરીકે લે-આપે."),
      P("In the natural cycle the two directions are almost equal, of the order of 60 Gt C a year "
        "each way between air and land or sea, so the atmospheric stock stays nearly constant over "
        "centuries.",
        "કુદરતી ચક્રમાં બંને દિશા લગભગ સરખી હોય, હવા અને જમીન કે દરિયા વચ્ચે દર વર્ષે અંદાજે 60 Gt C, તેથી "
        "વાતાવરણનો ભંડાર સદીઓ સુધી લગભગ અચળ રહે."),
      P("Burning coal, oil and gas adds about 10 Gt C a year that had been out of circulation for "
        "millions of years, and land-use change adds more; there is no matching sink, so the "
        "atmospheric concentration has risen from 280 ppm to over 420 ppm.",
        "કોલસો, તેલ અને ગેસ બાળવાથી દર વર્ષે લગભગ 10 Gt C ઉમેરાય છે જે લાખો વર્ષ ચક્ર બહાર હતો, અને "
        "જમીન-ઉપયોગ બદલાવ વધુ ઉમેરે; સામે કોઈ શોષક નથી, તેથી વાતાવરણનું પ્રમાણ 280 ppmથી 420 ppmથી "
        "વધુ થઈ ગયું છે."),
      P("The correction has to come from the same balance sheet: cut the fossil input (efficiency, "
        "renewables) and strengthen the sinks (forests, soil carbon, carbon capture).",
        "સુધારો એ જ હિસાબમાંથી આવવો પડે: અશ્મિ ઇનપુટ ઘટાડવો (કાર્યક્ષમતા, નવીકરણીય ઊર્જા) અને શોષક "
        "મજબૂત કરવા (જંગલ, જમીનનો કાર્બન, કાર્બન કેપ્ચર).")]),
    (T("Explain the nitrogen cycle with its five steps and one environmental problem it causes.",
       "નાઇટ્રોજન ચક્ર તેના પાંચ પગલાં અને તેનાથી થતી એક પર્યાવરણીય સમસ્યા સાથે સમજાવો."),
     4,
     [P("Nitrogen is 78 % of the air but as N₂ it is inert because of its triple bond; the cycle is "
        "the route by which it becomes usable and returns to the air.",
        "હવામાં 78 % નાઇટ્રોજન છે, પણ N₂ તરીકે તે ત્રિબંધને કારણે નિષ્ક્રિય છે; ચક્ર એ માર્ગ છે જેનાથી "
        "તે વપરાય તેવો બને અને પાછો હવામાં જાય."),
      P("The five steps are fixation (Rhizobium, Azotobacter, lightning, Haber-Bosch), nitrification "
        "(Nitrosomonas then Nitrobacter), assimilation into amino acids, ammonification by "
        "decomposers, and denitrification back to N₂ by Pseudomonas.",
        "પાંચ પગલાં છે સ્થિરીકરણ (રાઇઝોબિયમ, એઝોટોબેક્ટર, વીજળી, હેબર-બોશ), નાઇટ્રિફિકેશન "
        "(નાઇટ્રોસોમોનસ પછી નાઇટ્રોબેક્ટર), એમિનો એસિડમાં આત્મસાત, વિઘટકો દ્વારા એમોનિફિકેશન, અને "
        "સ્યુડોમોનાસ દ્વારા ડિનાઇટ્રિફિકેશન પાછું N₂."),
      P("The environmental problem is nitrate leaching: excess fertiliser washes into ponds and "
        "rivers, causes an algal bloom and then oxygen depletion, so the water body dies - this is "
        "eutrophication.",
        "પર્યાવરણીય સમસ્યા નાઇટ્રેટનું ધોવાણ છે: વધારાનું ખાતર તળાવ અને નદીમાં જાય, શેવાળનો વિસ્ફોટ કરે "
        "અને પછી ઓક્સિજન ખતમ કરે, તેથી જળાશય મૃત થાય - આ જ યુટ્રોફિકેશન છે."),
      P("Soil also releases nitrous oxide, a greenhouse gas about 273 times stronger than CO₂, so "
        "fertiliser management is both a water and a climate issue.",
        "જમીન નાઇટ્રસ ઓક્સાઇડ પણ છોડે છે, જે CO₂ કરતાં લગભગ 273 ગણો શક્તિશાળી હરિતગૃહ વાયુ છે, તેથી ખાતરનું "
        "સંચાલન પાણી અને જળવાયુ - બંનેની બાબત છે.")]),
    (T("What is biodiversity? State its levels, its values and the threats it faces.",
       "જૈવવિવિધતા એટલે શું? તેનાં સ્તર, મૂલ્ય અને ભય જણાવો."),
     5,
     [P("Biodiversity is the variety of life at three levels: genetic diversity within a species, "
        "species diversity within a community, and ecosystem diversity across a landscape.",
        "જૈવવિવિધતા એ ત્રણ સ્તરે જીવનની વિવિધતા છે: એક જાતિની અંદર આનુવંશિક વિવિધતા, સમુદાયમાં જાતિઓની "
        "વિવિધતા, અને ભૂદૃશ્યમાં પારિતંત્રોની વિવિધતા."),
      P("Its value is counted in four kinds of ecosystem service: provisioning (food, fibre, "
        "medicine), regulating (climate, water, pollination), cultural (recreation, religion) and "
        "supporting (soil formation, nutrient cycling).",
        "તેનું મૂલ્ય ચાર પ્રકારની પારિતંત્ર સેવામાં ગણાય છે: પુરવઠા (ખોરાક, રેસો, દવા), નિયમન (જળવાયુ, "
        "પાણી, પરાગનયન), સાંસ્કૃતિક (મનોરંજન, ધર્મ) અને આધાર (જમીન નિર્માણ, પોષક ચક્ર)."),
      P("The five main threats are habitat loss and fragmentation, invasive alien species, pollution, "
        "over-exploitation and climate change; in India all five act at once because of high "
        "population density.",
        "પાંચ મુખ્ય ભય છે નિવાસનો નાશ અને વિભાજન, આક્રમક બહારની જાતિઓ, પ્રદૂષણ, અતિ-દોહન અને જળવાયુ "
        "પરિવર્તન; ભારતમાં વસ્તીની ઊંચી ઘનતાને કારણે પાંચેય એકસાથે કામ કરે છે."),
      P("Conservation answers them at two levels - in-situ protection of habitat and ex-situ gene "
        "banks - supported by the Wild Life (Protection) Act 1972 and the Biological Diversity Act "
        "2002.",
        "સંરક્ષણ તેમને બે સ્તરે જવાબ આપે - નિવાસનું સ્થાનિક રક્ષણ અને સ્થાનાંતરિત જનીન બેંક - જેને વન્યજીવ "
        "(સંરક્ષણ) અધિનિયમ 1972 અને જૈવિક વિવિધતા અધિનિયમ 2002 ટેકો આપે છે.")]),
    (T("Explain the structure of an ecosystem and state why energy flow is one-way.",
       "પારિતંત્રની રચના સમજાવો અને ઊર્જા પ્રવાહ એક દિશાનો કેમ છે તે જણાવો."),
     4,
     [P("Structure means the abiotic components (light, water, air, soil, minerals, temperature) and "
        "the biotic components: producers, consumers and decomposers, arranged in trophic levels.",
        "રચના એટલે અજૈવિક ઘટકો (પ્રકાશ, પાણી, હવા, જમીન, ખનિજ, તાપમાન) અને જૈવિક ઘટકો: ઉત્પાદક, "
        "ઉપભોક્તા અને વિઘટક, જે પોષણ સ્તરમાં ગોઠવાયેલા હોય."),
      P("Energy enters as sunlight and is fixed by photosynthesis into chemical energy; at every "
        "transfer about 90 % is lost as heat in respiration and only 10 % is stored in the next "
        "level.",
        "ઊર્જા સૂર્યપ્રકાશ તરીકે આવે અને પ્રકાશસંશ્લેષણ તેને રાસાયણિક ઊર્જામાં સ્થિર કરે; દરેક "
        "સ્થાનાંતરણમાં લગભગ 90 % શ્વસનમાં ઉષ્મા તરીકે ખર્ચાય અને ફક્ત 10 % આગલા સ્તરમાં સંગ્રહાય."),
      P("The loss is irreversible because respiration converts chemical energy into heat, which "
        "cannot be used again by living things - so energy never cycles back, unlike matter.",
        "નુકસાન પાછું ન ફરે તેવું છે કારણ કે શ્વસન રાસાયણિક ઊર્જાને ઉષ્મામાં ફેરવે, જે જીવો ફરી વાપરી "
        "શકતા નથી - તેથી ઊર્જા કદી ચક્રમાં પાછી ન આવે, દ્રવ્યની જેમ."),
      P("The consequence is practical: only a short chain can support a top consumer, and the "
        "ecosystem must receive sunlight continuously or it collapses.",
        "પરિણામ વ્યવહારુ છે: ફક્ત ટૂંકી શૃંખલા ટોચના ઉપભોક્તાને ટકાવી શકે, અને પારિતંત્રને સતત સૂર્યપ્રકાશ "
        "મળવો જોઈએ નહીં તો તે ઢળી પડે.")]),
    (T("Describe the phosphorus cycle and explain why it is called a sedimentary cycle.",
       "ફોસ્ફરસ ચક્ર વર્ણવો અને તેને સેડિમેન્ટરી ચક્ર કેમ કહે છે તે સમજાવો."),
     4,
     [P("Phosphorus is stored in phosphate rock and marine sediment. Weathering releases phosphate "
        "into soil water, plants absorb it, animals eat the plants, and decomposers return it to the "
        "soil.",
        "ફોસ્ફરસ ફોસ્ફેટ ખડક અને દરિયાના સેડિમેન્ટમાં સંગ્રહાય છે. ઘસારો ફોસ્ફેટને જમીનના પાણીમાં "
        "છોડે, છોડ શોષે, પ્રાણી છોડ ખાય, અને વિઘટક તેને જમીનમાં પાછો આપે."),
      P("Some phosphate is washed to the sea, where it settles as sediment and returns to land only "
        "through geological uplift over millions of years.",
        "કેટલોક ફોસ્ફેટ દરિયામાં ધોવાઈ જાય, જ્યાં સેડિમેન્ટ તરીકે બેસે અને લાખો વર્ષના ભૂસ્તરીય ઉન્નયન "
        "દ્વારા જ જમીન પર પાછો આવે."),
      P("It is called sedimentary because its main reservoir is rock and sediment and there is no "
        "gaseous stage, so it cannot return through the atmosphere.",
        "તેને સેડિમેન્ટરી કહે છે કારણ કે તેનો મુખ્ય ભંડાર ખડક અને સેડિમેન્ટ છે અને વાયુ સ્વરૂપ નથી, તેથી "
        "તે વાતાવરણ દ્વારા પાછો આવી શકતો નથી."),
      P("Because the supply is small and slow, phosphorus is the limiting nutrient in most fresh "
        "water, and the phosphate mined today is a one-way resource that has no substitute.",
        "પુરવઠો ઓછો અને ધીમો હોવાથી મોટા ભાગના ગળાયેલા પાણીમાં ફોસ્ફરસ મર્યાદિત પોષક તત્વ છે, અને આજે "
        "ખણાતો ફોસ્ફેટ એક દિશાનો સ્રોત છે જેનો વિકલ્પ નથી.")]),
    (T("Compare the sulphur and phosphorus cycles in a table with four points.",
       "ચાર મુદ્દા સાથે કોષ્ટકમાં સલ્ફર અને ફોસ્ફરસ ચક્રની સરખામણી કરો."),
     3,
     [P("Main reservoir: sulphur is stored in rocks and ocean sediment and also in the atmosphere; "
        "phosphorus only in phosphate rock and sediment.",
        "મુખ્ય ભંડાર: સલ્ફર ખડક અને દરિયાના સેડિમેન્ટમાં તથા વાતાવરણમાં પણ સંગ્રહાય; ફોસ્ફરસ ફક્ત "
        "ફોસ્ફેટ ખડક અને સેડિમેન્ટમાં."),
      P("Gas phase: sulphur has SO₂ and H₂S, phosphorus has none - which is why one causes acid rain "
        "and the other cannot travel through air.",
        "વાયુ સ્વરૂપ: સલ્ફરમાં SO₂ અને H₂S છે, ફોસ્ફરસમાં નથી - તેથી એક એસિડ વરસાદ કરે અને બીજો હવામાં "
        "પ્રવાસ કરી શકતો નથી."),
      P("Human source: sulphur from coal burning and ore smelting; phosphorus from fertiliser, "
        "detergent and sewage.",
        "માનવ સ્રોત: સલ્ફર કોલસો બાળવાથી અને ધાતુ ગાળવાથી; ફોસ્ફરસ ખાતર, ડિટર્જન્ટ અને ગંદા પાણીથી."),
      P("Pollution effect: sulphur gives acid rain and metal corrosion; phosphorus gives "
        "eutrophication of lakes and rivers.",
        "પ્રદૂષણ અસર: સલ્ફર એસિડ વરસાદ અને ધાતુનો કાટ આપે; ફોસ્ફરસ સરોવર અને નદીનું યુટ્રોફિકેશન આપે.")]),
    (T("Explain in-situ and ex-situ conservation and give two examples of each.",
       "સ્થાનિક અને સ્થાનાંતરિત સંરક્ષણ સમજાવો અને દરેકનાં બે ઉદાહરણ આપો."),
     4,
     [P("In-situ conservation protects a species inside its own habitat, so the whole community and "
        "its interactions survive together; examples are Gir National Park for the Asiatic lion and "
        "the Nal Sarovar sanctuary for water birds.",
        "સ્થાનિક સંરક્ષણ જાતિને તેના જ નિવાસમાં બચાવે, જેથી આખો સમુદાય અને તેની આંતરક્રિયા સાથે ટકે; "
        "ઉદાહરણ એશિયાટિક સિંહ માટે ગિર રાષ્ટ્રીય ઉદ્યાન અને જળપક્ષીઓ માટે નળ સરોવર અભયારણ્ય."),
      P("Ex-situ conservation keeps the species outside its habitat: zoos, botanical gardens, seed "
        "banks, cryo banks and gene banks, for example the seed bank at NBPGR or a cactus collection "
        "in a botanical garden.",
        "સ્થાનાંતરિત સંરક્ષણ જાતિને નિવાસ બહાર રાખે: પ્રાણીસંગ્રહાલય, વનસ્પતિ ઉદ્યાન, બીજ બેંક, ક્રાયો "
        "બેંક અને જનીન બેંક, જેમ કે NBPGRની બીજ બેંક કે વનસ્પતિ ઉદ્યાનમાં કેક્ટસનો સંગ્રહ."),
      P("Ex-situ preserves genes but not ecology: a species kept only in a zoo has lost its habitat, "
        "its pollinators and its role in the food web.",
        "સ્થાનાંતરિત સંગ્રહ જનીન બચાવે, પણ પરિસ્થિતિ નહીં: ફક્ત પ્રાણીસંગ્રહાલયમાં રહેતી જાતિએ પોતાનું "
        "નિવાસ, પરાગનયન કરનારા અને ખોરાક જાળમાંની ભૂમિકા ગુમાવી છે."),
      P("The two therefore work as a pair: in-situ is the primary strategy and ex-situ is the "
        "insurance policy for species whose habitat has already shrunk.",
        "તેથી બંને જોડી તરીકે કામ કરે: સ્થાનિક પ્રાથમિક વ્યૂહરચના છે અને સ્થાનાંતરિત એ જાતિઓ માટે "
        "વીમા પોલિસી છે જેમનું નિવાસ પહેલેથી સંકોચાઈ ગયું છે.")]),
    (T("A town of 1 lakh people has a footprint of 2.0 gha per person and a biocapacity of "
       "0.5 gha per person. Find the deficit and suggest two measures.",
       "1 લાખ લોકોના શહેરની માથાદીઠ પગથિયું 2.0 gha અને વહેંચણી ક્ષમતા 0.5 gha છે. ખાદ્યાન્ન શોધો અને "
       "બે પગલાં સૂચવો."),
     4,
     [P("Total footprint = 1 00 000 × 2.0 = 2 00 000 gha; total biocapacity = 1 00 000 × 0.5 = "
        "50 000 gha.",
        "કુલ પગથિયું = 1 00 000 × 2.0 = 2 00 000 gha; કુલ વહેંચણી ક્ષમતા = 1 00 000 × 0.5 = 50 000 gha."),
      P("Deficit = 2 00 000 - 50 000 = 1 50 000 gha, so the town uses four times the land it has "
        "(2.0 / 0.5 = 4).",
        "ખાદ્યાન્ન = 2 00 000 - 50 000 = 1 50 000 gha, તેથી શહેર પોતાની પાસેની જમીન કરતાં ચાર ગણું વાપરે "
        "(2.0 / 0.5 = 4)."),
      P("Measure one: cut the energy footprint by rooftop solar, LED lighting and efficient pumps, "
        "since fossil energy is the largest part of most urban footprints.",
        "પગલું એક: છત પરની સૌર પેનલ, LED લાઇટિંગ અને કાર્યક્ષમ પંપથી ઊર્જા પગથિયું ઘટાડવું, કારણ કે "
        "મોટા ભાગના શહેરી પગથિયાંનો સૌથી મોટો ભાગ અશ્મિ ઊર્જા છે."),
      P("Measure two: segregate and compost wet waste locally to cut transport and landfill land, and "
        "protect the remaining orchards and water bodies as they are the town's own biocapacity.",
        "પગલું બે: ભીનો કચરો અલગ કરીને સ્થાનિક રીતે કમ્પોસ્ટ કરવાથી વાહનવ્યવહાર અને લેન્ડફિલ જમીન બચે, "
        "અને બાકીના બગીચા તથા જળાશયો સાચવવા કારણ કે તે જ શહેરની પોતાની વહેંચણી ક્ષમતા છે.")]),
    (T("State the ten per cent law. Producers fix 5 × 10⁴ kJ - find the energy at the tertiary "
       "consumer level.",
       "દસ ટકાનો નિયમ જણાવો. ઉત્પાદક 5 × 10⁴ kJ સ્થિર કરે - તૃતીય ઉપભોક્તા સ્તરે ઊર્જા શોધો."),
     3,
     [P("The ten per cent law states that only about 10 % of the energy of one trophic level is "
        "transferred to the next; the rest is lost as heat in respiration.",
        "દસ ટકાનો નિયમ કહે છે કે એક પોષણ સ્તરની ફક્ત લગભગ 10 % ઊર્જા આગલા સ્તરે જાય; બાકીની શ્વસનમાં "
        "ઉષ્મા તરીકે ખર્ચાય."),
      P("Producers 50 000 kJ; primary consumer 5 000 kJ; secondary 500 kJ; tertiary 50 kJ.",
        "ઉત્પાદક 50 000 kJ; પ્રાથમિક ઉપભોક્તા 5 000 kJ; દ્વિતીય 500 kJ; તૃતીય 50 kJ."),
      P("Answer 50 kJ, which is 0.1 % of the producer energy - three successive tenfold losses, as "
        "the law predicts.",
        "જવાબ 50 kJ, જે ઉત્પાદક ઊર્જાના 0.1 % છે - નિયમ પ્રમાણે સળંગ ત્રણ દસગણા નુકસાન.")]),
    (T("Explain why biodiversity loss matters to an engineer, with two examples from construction "
       "or manufacturing.",
       "જૈવવિવિધતાનો નાશ ઇજનેર માટે કેમ મહત્ત્વનો છે તે બાંધકામ કે ઉત્પાદનનાં બે ઉદાહરણ સાથે સમજાવો."),
     4,
     [P("Biodiversity supplies services that engineering normally takes for free: pollination, water "
        "purification, flood buffering, soil stability and raw material.",
        "જૈવવિવિધતા એ સેવાઓ આપે છે જે ઇજનેરી સામાન્ય રીતે મફત માને છે: પરાગનયન, પાણીની શુદ્ધિ, પૂર "
        "રોકવું, જમીનની સ્થિરતા અને કાચી સામગ્રી."),
      P("Example one: a coastal project that removes mangroves loses its wave buffer and then has to "
        "build a sea wall, paying with concrete what the trees gave free.",
        "ઉદાહરણ એક: કાંદલાં દૂર કરતો દરિયાકિનારા પ્રોજેક્ટ પોતાનું મોજાં-રક્ષક ખોઈ બેસે અને પછી દરિયાઈ "
        "દીવાલ બાંધવી પડે, એટલે વૃક્ષોએ મફત આપેલું કોંક્રિટથી ખરીદવું પડે."),
      P("Example two: loss of pollinators raises the cost and uncertainty of the cotton and "
        "vegetable supply chain that a textile or food plant depends on.",
        "ઉદાહરણ બે: પરાગનયન કરનારા જીવોનો નાશ કપાસ અને શાકભાજીના પુરવઠા શૃંખલાનો ખર્ચ અને અનિશ્ચિતતા "
        "વધારે, જેના પર કાપડ કે ખાદ્ય ઉત્પાદન એકમ આધાર રાખે."),
      P("The engineering response is the mitigation hierarchy - avoid, minimise, restore, offset - "
        "built into the project from the survey stage, not added after the damage.",
        "ઇજનેરી જવાબ છે શમન ક્રમ - ટાળો, ઘટાડો, પુનઃસ્થાપિત કરો, વળતર આપો - જે નુકસાન પછી નહીં, પણ "
        "સર્વેના તબક્કેથી પ્રોજેક્ટમાં સામેલ હોવો જોઈએ.")]),
    (T("What is eutrophication? Trace it from a fertiliser bag to a dead pond in four steps.",
       "યુટ્રોફિકેશન એટલે શું? ખાતરની થેલીથી મૃત તળાવ સુધીનો ચાર પગલાંનો માર્ગ દર્શાવો."),
     4,
     [P("Eutrophication is the over-enrichment of a water body with nutrients, mainly nitrate and "
        "phosphate, which upsets the oxygen balance and kills aquatic life.",
        "યુટ્રોફિકેશન એ જળાશયમાં પોષક તત્વો, મુખ્યત્વે નાઇટ્રેટ અને ફોસ્ફેટનું અતિ-સંવર્ધન છે, જે ઓક્સિજનનું "
        "સંતુલન બગાડી જળજીવન મારી નાખે છે."),
      P("Step one: rain washes the excess fertiliser from the field into a drain. Step two: the drain "
        "carries it to the pond, where nitrate and phosphate act as fertiliser for algae.",
        "પગલું એક: વરસાદ ખેતરનું વધારાનું ખાતર નાળામાં ધોઈ લાવે. પગલું બે: નાળું તેને તળાવ સુધી પહોંચાડે, જ્યાં "
        "નાઇટ્રેટ અને ફોસ્ફેટ શેવાળ માટે ખાતર બને."),
      P("Step three: the algae multiply into a bloom that covers the surface and blocks sunlight; "
        "then they die. Step four: bacteria decompose them and consume the dissolved oxygen, fish "
        "suffocate and the pond turns foul.",
        "પગલું ત્રણ: શેવાળ વિસ્ફોટ કરી સપાટી ઢાંકે અને સૂર્યપ્રકાશ રોકે; પછી મરે. પગલું ચાર: જીવાણુ તેમનું "
        "વિઘટન કરી ઓગળેલો ઓક્સિજન વાપરે, માછલી ગૂંગળાય અને તળાવ બદબો ફેલાવે."),
      P("The engineering fix is at the source: right fertiliser dose, buffer strips, and nutrient "
        "removal in the sewage treatment plant before the water is let out.",
        "ઇજનેરી ઉકેલ સ્રોત પર જ છે: યોગ્ય ખાતર માત્રા, છોડની પટ્ટીઓ, અને પાણી છોડતાં પહેલાં ગંદા પાણીના "
        "પ્લાન્ટમાં પોષક તત્વો દૂર કરવા.")]),
]

EXAM = [{"q": q, "marks": m} for q, m, _parts in _PRACTICE]
PRACTICE_ANSWERS = [_join(parts) for _q, _m, parts in _PRACTICE]

LESSON_COUNT = sum(len(s["items"]) for s in NOTES)
