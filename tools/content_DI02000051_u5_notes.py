"""DI02000051 Environmental Sustainability - Unit 5: Environmental Policy and Governance.

GTU 5.1-5.5, 6 h, 20 %, 14 marks, CO5. Every text node carries English and Gujarati.
"""
from content_DI02000051_u1_notes import T, P, H4, UL, OL, TB, card, num, _join

SOURCES = [
    T("GTU DI02000051 Environmental Sustainability syllabus (uploaded PDF, w.e.f. 2024-25)",
      "GTU DI02000051 પર્યાવરણીય ટકાઉપણું સિલેબસ (અપલોડ કરેલ PDF, 2024-25થી અમલમાં)"),
    T("MoEFCC - The Air (Prevention and Control of Pollution) Act 1981, Water Act 1974, "
      "Environment (Protection) Act 1986 and the EIA Notification 2006",
      "MoEFCC - વાયુ (પ્રદૂષણ નિયંત્રણ અને નિવારણ) અધિનિયમ 1981, જળ અધિનિયમ 1974, "
      "પર્યાવરણ (સંરક્ષણ) અધિનિયમ 1986 અને EIA જાહેરનામું 2006"),
    T("BIS IS/ISO 14001:2015 Environmental management systems - requirements with guidance for use",
      "BIS IS/ISO 14001:2015 પર્યાવરણીય વ્યવસ્થાપન પ્રણાલી - ઉપયોગ માટે માર્ગદર્શન સાથે આવશ્યકતાઓ"),
    T("IGBC Green New Buildings rating system, GRIHA manual (MNRE and TERI) and BEE ECBC 2017",
      "IGBC લીલી નવી ઇમારત રેટિંગ પ્રણાલી, GRIHA માર્ગદર્શિકા (MNRE અને TERI) અને BEE ECBC 2017"),
    T("CGWA rainwater harvesting guidelines, CPCB guidelines and the Biological Diversity Act 2002",
      "CGWA વરસાદી જળ સંગ્રહ માર્ગદર્શિકા, CPCB માર્ગદર્શિકા અને જૈવિક વિવિધતા અધિનિયમ 2002"),
]

NOTES = [
    {"title": T("1. Environmental Law in India", "1. ભારતમાં પર્યાવરણીય કાયદો"),
     "items": [
         card(T("5.1 The Water Act 1974 and the Air Act 1981",
                "5.1 જળ અધિનિયમ 1974 અને વાયુ અધિનિયમ 1981"),
              [H4("Why these two came first", "આ બે પહેલાં કેમ આવ્યા"),
               P("India's first environmental statute after independence was the <b>Water (Prevention "
                 "and Control of Pollution) Act, 1974</b>, passed because rivers near industrial towns "
                 "had become open sewers. It created the Central Pollution Control Board and a State "
                 "Pollution Control Board in every state, and made it illegal to discharge sewage or "
                 "trade effluent into a stream without the <b>consent</b> of the Board. The <b>Air "
                 "(Prevention and Control of Pollution) Act, 1981</b> used the same machinery for air, "
                 "added the power to declare <b>air pollution control areas</b> and set standards for "
                 "chimneys, industries and, later, vehicles.",
                 "સ્વતંત્રતા પછીનો ભારતનો પ્રથમ પર્યાવરણીય કાયદો <b>જળ (પ્રદૂષણ નિવારણ અને નિયંત્રણ) અધિનિયમ, "
                 "1974</b> હતો, જે એટલા માટે થયો કે ઔદ્યોગિક નગરો પાસેની નદીઓ ખુલ્લી ગટર બની ગઈ હતી. તેણે કેન્દ્રીય "
                 "પ્રદૂષણ નિયંત્રણ બોર્ડ અને દરેક રાજ્યમાં રાજ્ય પ્રદૂષણ નિયંત્રણ બોર્ડ બનાવ્યા, અને બોર્ડની "
                 "<b>સંમતિ</b> વગર ગટર કે ઉદ્યોગનું પાણી નદીમાં છોડવું ગેરકાયદે ઠેરવ્યું. <b>વાયુ (પ્રદૂષણ "
                 "નિવારણ અને નિયંત્રણ) અધિનિયમ, 1981</b>એ એ જ મશીનરી હવા માટે વાપરી, <b>વાયુ પ્રદૂષણ નિયંત્રણ "
                 "વિસ્તાર</b> જાહેર કરવાની સત્તા ઉમેરી અને ચીમની, ઉદ્યોગો તથા પછીથી વાહનો માટે ધોરણો નક્કી કર્યા."),
               H4("The consent mechanism", "સંમતિની પ્રણાલી"),
               P("A factory that wants to start must apply for <b>Consent to Establish</b> and then "
                 "<b>Consent to Operate</b>, which states the maximum quantity and quality of effluent "
                 "or emission allowed, the monitoring it must do and the conditions it must meet. The "
                 "consent is renewed periodically, can be refused, and can be cancelled if the "
                 "conditions are broken. This single instrument is the backbone of Indian pollution "
                 "control, because the Board inspects against a written permission instead of arguing "
                 "about general duties.",
                 "શરૂ કરવા માંગતા કારખાનાએ પહેલાં <b>સ્થાપના સંમતિ</b> અને પછી <b>સંચાલન સંમતિ</b> મેળવવી પડે, "
                 "જેમાં મંજૂર મહત્તમ પ્રવાહ અને ગુણવત્તા, જરૂરી દેખરેખ અને પાળવાની શરતો લખેલી હોય. સંમતિ સમયાંતરે "
                 "નવીકરણ થાય, નકારી શકાય અને શરતો તૂટે તો રદ થાય. આ એક સાધન ભારતીય પ્રદૂષણ નિયંત્રણનું કરોડરજ્જુ "
                 "છે, કારણ કે બોર્ડ સામાન્ય ફરજો પર દલીલ કરવાને બદલે લેખિત પરવાનગી સામે તપાસ કરે."),
               H4("Standards and who sets them", "ધોરણો અને કોણ નક્કી કરે"),
               TB([T("Body", "સંસ્થા"), T("Role", "ભૂમિકા"), T("Typical output", "સામાન્ય પરિણામ")],
                  [[T("CPCB", "CPCB"), T("national standards, coordination, monitoring", "રાષ્ટ્રીય ધોરણ, સમન્વય, દેખરેખ"), T("effluent and emission standards, AQI", "પ્રવાહ અને ઉત્સર્જન ધોરણ, AQI")],
                   [T("SPCB / PCC", "SPCB / PCC"), T("consent, inspection, prosecution", "સંમતિ, તપાસ, કાર્યવાહી"), T("consent orders, closure directions", "સંમતિ આદેશ, બંધ કરવાની સૂચના")],
                   [T("MoEFCC", "MoEFCC"), T("policy, EIA notification, rules under EPA", "નીતિ, EIA જાહેરનામું, EPA હેઠળ નિયમો"), T("EIA categories, waste rules", "EIA શ્રેણીઓ, કચરા નિયમો")],
                   [T("NGT", "NGT"), T("green tribunal, civil cases on environment", "લીલું ટ્રિબ્યુનલ, પર્યાવરણના દીવાની કેસ"), T("orders, compensation, restitution", "આદેશ, વળતર, પુનઃસ્થાપન")]]),
               H4("Worked example", "ઉકેલાયેલ દાખલો"),
               P("A dyeing unit discharges 500 m³ a day with BOD 250 mg/L. Its consent allows 30 mg/L, so "
                 "the daily load is 500 × 250 / 1,000 = 125 kg of BOD against a permitted 15 kg - an "
                 "excess of 110 kg a day, which is enough for the Board to direct closure under section "
                 "33A of the Water Act.",
                 "એક રંગાઈ એકમ દિવસે 500 m³ પાણી BOD 250 mg/L સાથે છોડે. તેની સંમતિ 30 mg/L મંજૂર કરે, તેથી "
                 "દૈનિક ભાર 500 × 250 / 1,000 = 125 કિલો BOD, મંજૂર 15 કિલો સામે - દિવસે 110 કિલો વધારો, જે જળ "
                 "અધિનિયમની કલમ 33A હેઠળ બોર્ડને એકમ બંધ કરાવવા પૂરતો છે."),
               H4("Common mistake", "સામાન્ય ભૂલ"),
               P("Thinking that a consent is a permanent licence. It is a time-bound permission with "
                 "conditions and a renewal date; operating after expiry is an offence even if the plant "
                 "is complying with the standards.",
                 "સંમતિ કાયમી પરવાનગી છે તેમ માનવું. તે શરતો અને નવીકરણની તારીખ સાથેની સમયબદ્ધ પરવાનગી છે; "
                 "સ્ટેશન ધોરણ પાળતું હોય તો પણ મુદત પૂરી થયા પછી ચલાવવું ગુનો છે.")],
              "u5_law", syllabus_item="5.1"),
         card(T("5.1 The Environment (Protection) Act 1986, Wildlife and Forest Conservation Acts",
                "5.1 પર્યાવરણ (સંરક્ષણ) અધિનિયમ 1986, વન્યજીવ અને વન સંરક્ષણ અધિનિયમ"),
              [H4("The umbrella Act", "છત્રી અધિનિયમ"),
               P("The Bhopal gas leak of 1984 showed that separate laws for water and air could not "
                 "reach a gas that killed thousands in one night, so the <b>Environment (Protection) "
                 "Act, 1986</b> was passed as an umbrella law. It gives the central government power to "
                 "set standards for any pollutant, in any medium, to restrict any industry or process, "
                 "to close a unit, and to make rules without going back to Parliament - which is why "
                 "almost every modern rule sits under it: the EIA Notification, the municipal, "
                 "plastic, e-waste, hazardous waste, construction and demolition and battery waste "
                 "rules, and the coastal regulation zone.",
                 "1984ના ભોપાલ ગેસ લીકેજે દર્શાવ્યું કે પાણી અને હવા માટેના અલગ કાયદા એક રાતમાં હજારોને મારતા "
                 "ગેસ સુધી પહોંચી શકતા નથી, તેથી <b>પર્યાવરણ (સંરક્ષણ) અધિનિયમ, 1986</b> છત્રી કાયદા તરીકે થયો. "
                 "તે કેન્દ્ર સરકારને કોઈ પણ પ્રદૂષક, કોઈ પણ માધ્યમ માટે ધોરણ, કોઈ પણ ઉદ્યોગ કે પ્રક્રિયા પર મર્યાદા, "
                 "એકમ બંધ કરવાની અને સંસદ પાસે પાછા જવા વગર નિયમ બનાવવાની સત્તા આપે - તેથી જ લગભગ દરેક આધુનિક નિયમ "
                 "તેની નીચે છે: EIA જાહેરનામું, નગરપાલિકા, પ્લાસ્ટિક, ઇ-કચરો, જોખમી કચરો, બાંધકામ-પાડકચરો અને "
                 "બેટરી કચરા નિયમો તથા દરિયાકાંઠાનો નિયમન વિસ્તાર."),
               H4("The four older laws", "ચાર જૂના કાયદા"),
               TB([T("Act", "અધિનિયમ"), T("Year", "વર્ષ"), T("What it protects", "શું બચાવે"), T("Key instrument", "મુખ્ય સાધન")],
                  [[T("Wild Life (Protection) Act", "વન્યજીવ (સંરક્ષણ) અધિનિયમ"), T("1972", "1972"), T("schedule species, national parks, sanctuaries", "અનુસૂચિત જાતિઓ, રાષ્ટ્રીય ઉદ્યાન, અભયારણ્ય"), T("protected areas, ban on hunting and trade", "સંરક્ષિત વિસ્તાર, શિકાર અને વ્યાપાર પર પ્રતિબંધ")],
                   [T("Water Act", "જળ અધિનિયમ"), T("1974", "1974"), T("rivers, streams, wells", "નદી, ઝરણાં, કૂવા"), T("consent to discharge", "છોડવાની સંમતિ")],
                   [T("Forest (Conservation) Act", "વન (સંરક્ષણ) અધિનિયમ"), T("1980", "1980"), T("forest land", "વન જમીન"), T("central approval for any diversion", "કોઈ પણ ફેરબદલ માટે કેન્દ્રીય મંજૂરી")],
                   [T("Air Act", "વાયુ અધિનિયમ"), T("1981", "1981"), T("ambient air", "આસપાસની હવા"), T("standards for chimneys and vehicles", "ચીમની અને વાહનોના ધોરણો")],
                   [T("Biological Diversity Act", "જૈવિક વિવિધતા અધિનિયમ"), T("2002", "2002"), T("biodiversity and traditional knowledge", "જૈવવિવિધતા અને પરંપરાગત જ્ઞાન"), T("three-tier boards, access and benefit sharing", "ત્રિસ્તરીય બોર્ડ, પ્રવેશ અને લાભ વહેંચણી")]]),
               H4("EIA: an instrument, not a formality", "EIA: ઔપચારિકતા નહીં, સાધન"),
               P("Under the EIA Notification 2006 a project is placed in category A or B by size and "
                 "type. Category A needs central clearance after an environmental impact assessment, an "
                 "environmental management plan and a public hearing; category B is handled by the "
                 "state. The clearance comes with <b>conditions</b> - a green belt, an effluent plant, a "
                 "monitoring report every six months - and the project can be stopped if they are not "
                 "met. The purpose is to find the problem at the drawing stage, when it costs a design "
                 "change instead of a shutdown.",
                 "EIA જાહેરનામું 2006 હેઠળ પ્રોજેક્ટ કદ અને પ્રકાર પ્રમાણે A કે B શ્રેણીમાં આવે. A શ્રેણીને "
                 "પર્યાવરણીય અસર આકલન, પર્યાવરણીય વ્યવસ્થાપન યોજના અને જાહેર સુનાવણી પછી કેન્દ્રીય મંજૂરી જોઈએ; B "
                 "શ્રેણી રાજ્ય સંભાળે. મંજૂરી <b>શરતો</b> સાથે આવે - લીલો પટ્ટો, પ્રવાહ સારવાર સ્ટેશન, દર છ મહિને "
                 "દેખરેખ અહેવાલ - અને પાળવામાં ન આવે તો પ્રોજેક્ટ થંભાવાય. હેતુ એ છે કે સમસ્યા ડ્રોઇંગના તબક્કે જ "
                 "મળે, જ્યારે તેનો ઉકેલ ડિઝાઇન બદલવાનો ખર્ચ લે, બંધ થવાનો નહીં.")],
              syllabus_item="5.1"),
         card(T("5.1 The Biological Diversity Act 2002 and environmental governance",
                "5.1 જૈવિક વિવિધતા અધિનિયમ 2002 અને પર્યાવરણીય શાસન"),
              [H4("Three tiers", "ત્રણ સ્તર"),
               P("The <b>Biological Diversity Act, 2002</b> answers a different question from the "
                 "pollution laws: who may use India's plants, animals and traditional knowledge, and "
                 "who shares the benefit. It sets up the National Biodiversity Authority at Chennai, a "
                 "State Biodiversity Board in each state and a Biodiversity Management Committee in "
                 "each local body. A foreign company needs NBA approval before using a bio-resource; an "
                 "Indian company needs state approval; and the committee prepares a <b>People's "
                 "Biodiversity Register</b> recording what grows and is used locally, so that a claim "
                 "of traditional knowledge can be proved.",
                 "<b>જૈવિક વિવિધતા અધિનિયમ, 2002</b> પ્રદૂષણ કાયદાઓથી અલગ પ્રશ્નનો જવાબ આપે: ભારતના છોડ, પ્રાણી "
                 "અને પરંપરાગત જ્ઞાન કોણ વાપરી શકે અને લાભ કોણ વહેંચે. તેણે ચેન્નાઈમાં રાષ્ટ્રીય જૈવવિવિધતા સત્તામંડળ, "
                 "દરેક રાજ્યમાં રાજ્ય જૈવવિવિધતા બોર્ડ અને દરેક સ્થાનિક સંસ્થામાં જૈવવિવિધતા વ્યવસ્થાપન સમિતિ ઊભી કરી. "
                 "વિદેશી કંપનીને જૈવ-સ્રોત વાપરતાં પહેલાં NBA મંજૂરી જોઈએ; ભારતીય કંપનીને રાજ્ય મંજૂરી; અને સમિતિ "
                 "<b>લોક જૈવવિવિધતા રજિસ્ટર</b> તૈયાર કરે જે સ્થાનિક રીતે શું ઊગે અને વપરાય તે નોંધે, જેથી પરંપરાગત "
                 "જ્ઞાનનો દાવો પુરવાર થઈ શકે."),
               H4("Who does what", "કોણ શું કરે"),
               TB([T("Layer", "સ્તર"), T("Body", "સંસ્થા"), T("Work", "કામ")],
                  [[T("national", "રાષ્ટ્રીય"), T("NBA, Chennai", "NBA, ચેન્નાઈ"), T("foreign access, IPR, benefit sharing", "વિદેશી પ્રવેશ, બૌદ્ધિક સંપદા, લાભ વહેંચણી")],
                   [T("state", "રાજ્ય"), T("State Biodiversity Board", "રાજ્ય જૈવવિવિધતા બોર્ડ"), T("Indian commercial access, conservation plans", "ભારતીય વ્યાપારી પ્રવેશ, સંરક્ષણ યોજના")],
                   [T("local", "સ્થાનિક"), T("Biodiversity Management Committee", "જૈવવિવિધતા વ્યવસ્થાપન સમિતિ"), T("People's Biodiversity Register, local rules", "લોક જૈવવિવિધતા રજિસ્ટર, સ્થાનિક નિયમો")],
                   [T("judicial", "ન્યાયિક"), T("National Green Tribunal, 2010", "રાષ્ટ્રીય લીલું ટ્રિબ્યુનલ, 2010"), T("hears environment cases in six months", "પર્યાવરણના કેસ છ મહિનામાં સાંભળે")]]),
               H4("The principles behind the law", "કાયદા પાછળના સિદ્ધાંતો"),
               UL(("<b>precautionary principle</b>: a lack of full proof is not a reason to delay action "
                   "when the damage may be serious", "<b>સાવચેતીનો સિદ્ધાંત</b>: નુકસાન ગંભીર હોઈ શકે તો પૂરો "
                   "પુરાવો ન હોવો એ કાર્યવાહી લંબાવવાનું કારણ નથી"),
                  ("<b>polluter pays</b>: the cost of cleaning up falls on the one who caused it", "<b>પ્રદૂષક ચૂકવે</b>: સફાઈનો ખર્ચ જેને કારણે થયો તેના પર"),
                  ("<b>sustainable development</b>: the right to develop is balanced against the right "
                   "of later generations", "<b>ટકાઉ વિકાસ</b>: વિકાસનો અધિકાર પછીની પેઢીઓના અધિકાર સામે "
                   "સંતુલિત"),
                  ("<b>public trust</b>: the state holds air, water and forest in trust for the people", "<b>જાહેર ભરોસો</b>: રાજ્ય હવા, પાણી અને વન લોકો માટે ભરોસામાં રાખે")),
               H4("Worked example", "ઉકેલાયેલ દાખલો"),
               P("A company wants to patent a formulation based on neem that a village has used for "
                 "decades. Under the Act it must apply to the NBA, disclose the source, and share the "
                 "benefit with the Biodiversity Management Committee; a register entry dated before the "
                 "application is the proof that the knowledge is not new.",
                 "એક કંપની ગામ દાખલાઓથી વાપરતું લીમડા આધારિત બનાવ સ્વત્વપેટંટ કરવા માંગે છે. અધિનિયમ હેઠળ તેણે "
                 "NBAમાં અરજી કરવી, સ્રોત જાહેર કરવો અને જૈવવિવિધતા વ્યવસ્થાપન સમિતિ સાથે લાભ વહેંચવો પડે; અરજી "
                 "પહેલાંની રજિસ્ટર નોંધ એ પુરાવો છે કે જ્ઞાન નવું નથી.")],
              syllabus_item="5.1"),
     ]},
    {"title": T("2. Environmental Management Systems", "2. પર્યાવરણીય વ્યવસ્થાપન પ્રણાલી"),
     "items": [
         card(T("5.2 ISO 14000 and the ISO 14001 management system",
                "5.2 ISO 14000 અને ISO 14001 વ્યવસ્થાપન પ્રણાલી"),
              [H4("A family, and one certifiable member", "એક કુટુંબ, અને એક પ્રમાણિત સભ્ય"),
               P("The <b>ISO 14000 family</b> is a set of international standards on environmental "
                 "management. Only <b>ISO 14001</b> states requirements that an organisation can be "
                 "audited and certified against; the others are guidance - ISO 14004 for implementing "
                 "the system, ISO 14031 for performance evaluation, ISO 14040 and 14044 for life cycle "
                 "assessment, and ISO 14064 for greenhouse gas accounting. The family is voluntary: no "
                 "law requires it, but a buyer, a bank or an export market may.",
                 "<b>ISO 14000 કુટુંબ</b> પર્યાવરણીય વ્યવસ્થાપન પરનાં આંતરરાષ્ટ્રીય ધોરણોનો સમૂહ છે. ફક્ત "
                 "<b>ISO 14001</b> આવશ્યકતાઓ આપે જેની સામે સંસ્થાની તપાસ અને પ્રમાણીકરણ થઈ શકે; બાકીનાં માર્ગદર્શન છે "
                 "- અમલ માટે ISO 14004, કાર્યદક્ષતા મૂલ્યાંકન માટે ISO 14031, જીવનચક્ર આકલન માટે ISO 14040 અને "
                 "14044, અને હરિતગૃહ વાયુ હિસાબ માટે ISO 14064. કુટુંબ સ્વૈચ્છિક છે: કોઈ કાયદો તેને ફરજિયાત કરતો "
                 "નથી, પણ ખરીદનાર, બેંક કે નિકાસ બજાર માંગી શકે."),
               H4("The PDCA engine", "PDCA એન્જિન"),
               P("The system runs on the <b>plan-do-check-act</b> cycle. <b>Plan</b>: find the "
                 "environmental aspects of every activity - what it takes from the environment and what "
                 "it puts back - rank them by significance, and set objectives, targets and legal "
                 "obligations. <b>Do</b>: run the documented procedures, train the staff, control the "
                 "significant aspects and keep records. <b>Check</b>: monitor, measure, audit internally "
                 "and record non-conformities. <b>Act</b>: correct the causes, and feed the lessons into "
                 "the next plan. The slogan of the standard is that the system is not a certificate on "
                 "the wall but a wheel that keeps turning.",
                 "પ્રણાલી <b>આયોજન-અમલ-તપાસ-સુધારો</b> (PDCA) ચક્ર પર ચાલે. <b>આયોજન</b>: દરેક પ્રવૃત્તિના "
                 "પર્યાવરણીય પાસાં શોધો - તે પર્યાવરણમાંથી શું લે છે અને શું પાછું આપે છે - તેમને મહત્ત્વ પ્રમાણે "
                 "ગોઠવો અને ઉદ્દેશ, લક્ષ્ય તથા કાનૂની ફરજો નક્કી કરો. <b>અમલ</b>: લેખિત પ્રક્રિયા ચલાવો, કર્મચારીને "
                 "તાલીમ આપો, મહત્ત્વના પાસાં નિયંત્રિત કરો અને નોંધ રાખો. <b>તપાસ</b>: દેખરેખ, માપન, આંતરિક તપાસ "
                 "અને બિન-અનુરૂપતા નોંધો. <b>સુધારો</b>: કારણ સુધારો અને પાઠ આગલા આયોજનમાં ઉમેરો. ધોરણનો સાર એ છે કે "
                 "પ્રણાલી દીવાલ પરનું પ્રમાણપત્ર નહીં, પણ સતત ફરતું ચક્ર છે."),
               H4("From aspect to objective", "પાસાંથી ઉદ્દેશ સુધી"),
               TB([T("Term", "શબ્દ"), T("Meaning", "અર્થ"), T("Example in a plating shop", "પ્લેટિંગ કારખાનામાં ઉદાહરણ")],
                  [[T("environmental aspect", "પર્યાવરણીય પાસું"), T("an activity that interacts with the environment", "પર્યાવરણ સાથે સંબંધ ધરાવતી પ્રવૃત્તિ"), T("spent acid bath, water use, diesel", "વપરાયેલો એસિડ સ્નાન, પાણીનો વપરાશ, ડીઝલ")],
                   [T("environmental impact", "પર્યાવરણીય અસર"), T("the change it causes", "તે જે ફેરફાર કરે"), T("soil contamination, river pollution", "જમીન પ્રદૂષણ, નદી પ્રદૂષણ")],
                   [T("significant aspect", "મહત્ત્વનું પાસું"), T("one that scores high on severity and frequency", "જે તીવ્રતા અને આવૃત્તિમાં ઊંચું અંક પામે"), T("acid bath, because a spill is severe", "એસિડ સ્નાન, કારણ કે ગળતર ગંભીર છે")],
                   [T("objective and target", "ઉદ્દેશ અને લક્ષ્ય"), T("what you will achieve and by when", "શું અને ક્યારે પામશો"), T("cut water use 20 % by 2027", "2027 સુધીમાં પાણીનો વપરાશ 20 % ઘટાડવો")]]),
               H4("What the organisation gains", "સંસ્થાને શું મળે"),
               UL(("legal comfort: the register of legal obligations is kept and checked, so a lapse is "
                   "found before an inspector finds it", "કાનૂની નિરાંત: કાનૂની ફરજોનું રજિસ્ટર રખાય અને "
                   "તપાસાય, તેથી ભૂલ નિરીક્ષક પહેલાં મળે"),
                  ("cost: energy, water and material waste are the same things the system watches, so "
                   "most certified plants save more than the certificate costs", "ખર્ચ: ઊર્જા, પાણી અને "
                   "સામગ્રીનો વ્યય એ જ વસ્તુઓ છે જે પ્રણાલી જુએ, તેથી મોટા ભાગના પ્રમાણિત કારખાનાં પ્રમાણપત્રના "
                   "ખર્ચ કરતાં વધુ બચાવે"),
                  ("market: export buyers and global supply chains ask for it, and it is a condition in "
                   "many tenders", "બજાર: નિકાસ ખરીદનાર અને વૈશ્વિક પુરવઠા શૃંખલા તે માંગે, અને ઘણી "
                   "નિવિદાઓમાં તે શરત છે"),
                  ("trust: an independent audit is evidence, while a claim in an advertisement is only a "
                   "claim", "ભરોસો: સ્વતંત્ર તપાસ પુરાવો છે, જ્યારે જાહેરાતનો દાવો ફક્ત દાવો છે")),
               H4("Common mistake", "સામાન્ય ભૂલ"),
               P("Buying a certificate and keeping the same papers for the audit. Certification requires "
                 "records that are current - monitoring data, training, non-conformity closure - and a "
                 "surveillance audit every year, so a system that exists only on paper is withdrawn.",
                 "પ્રમાણપત્ર ખરીદીને તપાસ માટે એ જ જૂના કાગળ રાખવા. પ્રમાણીકરણને વર્તમાન નોંધ જોઈએ - દેખરેખ "
                 "માહિતી, તાલીમ, બિન-અનુરૂપતાનું નિવારણ - અને દર વર્ષે દેખરેખ તપાસ, તેથી ફક્ત કાગળ પરની પ્રણાલી "
                 "પાછી ખેંચાય.")],
              "u5_iso", syllabus_item="5.2"),
     ]},
    {"title": T("3. Sustainable Practices", "3. ટકાઉ પદ્ધતિઓ"),
     "items": [
         card(T("5.3 Rain water harvesting", "5.3 વરસાદી જળ સંગ્રહ"),
              [H4("Two ways to catch the rain", "વરસાદ પકડવાની બે રીત"),
               P("<b>Surface storage</b> collects roof or ground runoff in a tank, a farm pond or a check "
                 "dam for direct use. <b>Ground water recharge</b> leads the same water through a filter "
                 "pit, a recharge trench or a shaft into the aquifer, where it is stored without "
                 "evaporation and recovered later from a well. A city needs both: it needs water in July "
                 "and it needs the aquifer full in April. The classic rain water harvesting system has five parts - "
                 "catchment, gutters and a first-flush pipe, a filter of gravel and sand, a storage "
                 "tank, and an overflow to a recharge pit.",
                 "<b>સપાટી સંગ્રહ</b> છત કે જમીનનું વહેતું પાણી ટાંકી, ખેત તળાવ કે બંધમાં એકઠું કરે. "
                 "<b>ભૂગર્ભજળ ભરાવો</b> એ જ પાણી ગાળણ ખાડો, ભરાવ ખંડ કે કૂવા દ્વારા જળાશયમાં લઈ જાય, જ્યાં "
                 "બાષ્પીભવન વગર સંગ્રહાય અને પછી કૂવામાંથી નીકળે. શહેરને બંને જોઈએ: જુલાઈમાં પાણી જોઈએ અને "
                 "એપ્રિલમાં જળાશય ભરેલું જોઈએ. પરંપરાગત છત પ્રણાલીમાં પાંચ ભાગ છે - ગ્રાહક સપાટી, ગટર અને "
                 "પ્રથમ-વહાવ પાઇપ, કાંકરા-રેતીનું ગાળક, સંગ્રહ ટાંકી અને ભરાવ ખાડા તરફ વહાવ."),
               H4("Sizing it", "માપ કેમ નક્કી કરવું"),
               P("The water a roof can give is <b>rainfall × area × runoff coefficient</b>. A flat "
                 "concrete roof loses about 15 % to evaporation, wetting and the first flush, so the "
                 "coefficient is 0.85; a sloping tile roof is 0.75. A 200 m² roof in a district with "
                 "1,200 mm of rain therefore yields 200 × 1.2 × 0.85 = 204 m³ a year, enough for about "
                 "1,100 days of a 180 litre household need. The tank is sized on the longest dry spell "
                 "rather than on the annual total, because a tank that overflows in August has been "
                 "sized on the wrong number.",
                 "છત આપી શકે તે પાણી = <b>વરસાદ × ક્ષેત્રફળ × વહેવાનો અવયવ</b>. સપાટ કોંક્રિટ છત બાષ્પીભવન, "
                 "ભીનાશ અને પ્રથમ વહાવમાં લગભગ 15 % ગુમાવે, તેથી અવયવ 0.85; ઢાળવાળી નળિયાની છત 0.75. 1,200 mm "
                 "વરસાદવાળા જિલ્લામાં 200 m² છત વર્ષે 200 × 1.2 × 0.85 = 204 m³ આપે, જે 180 લિટર રોજની જરૂર "
                 "ધરાવતા કુટુંબને લગભગ 1,100 દિવસ પૂરે. ટાંકી વાર્ષિક કુલ પ્રમાણે નહીં, સૌથી લાંબા સૂકા સમય "
                 "પ્રમાણે માપાય, કારણ કે ઓગસ્ટમાં પૂર આવતી ટાંકી ખોટા આંકડા પર માપેલી હોય."),
               H4("Why a city must do it", "શહેરે તે કેમ કરવું જોઈએ"),
               TB([T("Problem", "સમસ્યા"), T("What harvesting does", "સંગ્રહ શું કરે")],
                  [[T("urban flooding", "શહેરી પૂર"), T("holds back the first 20-30 mm of a storm, which is the part that floods the roads", "વાવાઝોડાના પ્રથમ 20-30 mm રોકે, જે રસ્તા ડુબાડતો ભાગ છે")],
                   [T("falling water table", "ઘટતું જળ સ્તર"), T("puts clean water back into the same aquifer the borewell draws from", "બોરવેલ જે જળાશયમાંથી ખેંચે તે જ જળાશયમાં સ્વચ્છ પાણી પાછું ભરે")],
                   [T("salt water in coastal towns", "કિનારાનાં નગરોમાં ખારું પાણી"), T("raises the fresh water lens and pushes the sea back", "ગળ્યા પાણીની પટ્ટી ઊંચી કરી દરિયો પાછો ધકેલે")],
                   [T("hard water and iron", "કઠણ પાણી અને લોહ"), T("rain water is nearly distilled, so it needs no softening", "વરસાદી જળ લગભગ નિસ્યંદિત છે, તેથી નરમ કરવાની જરૂર નહીં")],
                   [T("energy for pumping", "પંપ માટે ઊર્જા"), T("a shallow, full aquifer needs a smaller pump and less electricity", "ઊંડાઈ ઓછી અને ભરેલું જળાશય નાનો પંપ અને ઓછી વીજળી માંગે")]]),
               H4("Worked example", "ઉકેલાયેલ દાખલો"),
               P("A school has a 600 m² roof and needs 3,000 L a day. Rain of 1,100 mm gives "
                 "600 × 1.1 × 0.85 = 561 m³ a year, which is 187 days of that demand; a 50 m³ tank plus "
                 "a recharge pit covers the rest of the year from the borewell that the pit keeps alive.",
                 "એક શાળાની 600 m² છત છે અને દિવસે 3,000 લિટર જોઈએ. 1,100 mm વરસાદ 600 × 1.1 × 0.85 = "
                 "561 m³ વર્ષે આપે, જે તે માંગના 187 દિવસ છે; 50 m³ ટાંકી અને ભરાવ ખાડો વર્ષના બાકીના દિવસો "
                 "તે બોરવેલમાંથી પૂરે જેને ખાડો જીવતું રાખે.")],
              "u5_rwh", syllabus_item="5.3"),
         card(T("5.3 Green buildings and the Indian rating systems",
                "5.3 લીલી ઇમારત અને ભારતીય રેટિંગ પ્રણાલી"),
              [H4("What makes a building green", "ઇમારત લીલી કેવી બને"),
               P("A green building is designed to use less energy and water over its whole life, to use "
                 "material with less embodied carbon, to keep the occupants healthy and to sit lightly "
                 "on its site. The measures are ordinary engineering: orientation and shading before air "
                 "conditioning, insulation and double glazing, a cool or green roof, LED lighting with "
                 "occupancy sensors, low-flow fixtures, rainwater harvesting and a sewage treatment "
                 "plant that reuses water for flushing and gardening, and waste segregation during "
                 "construction.",
                 "લીલી ઇમારત આખા જીવનમાં ઓછી ઊર્જા અને પાણી વાપરવા, ઓછા સન્નિહિત કાર્બનવાળી સામગ્રી વાપરવા, "
                 "રહેવાસીઓને સ્વસ્થ રાખવા અને સ્થળ પર ઓછો ભાર પાડવા રચાય. પગલાં સામાન્ય એન્જિનિયરિંગ છે: "
                 "એરકન્ડીશનિંગ પહેલાં દિશા અને છાયો, ઇન્સ્યુલેશન અને બેવડો કાચ, ઠંડી કે લીલી છત, હાજરી સેન્સરવાળી "
                 "LED લાઇટ, ઓછા પ્રવાહનાં નળ, વરસાદી જળ સંગ્રહ અને ફ્લશિંગ તથા બગીચા માટે પાણી વાપરતો ગટર "
                 "સારવાર એકમ, તથા બાંધકામ દરમિયાન કચરાનું અલગીકરણ."),
               H4("The three Indian labels", "ત્રણ ભારતીય લેબલ"),
               TB([T("System", "પ્રણાલી"), T("Run by", "કોણ ચલાવે"), T("Scale", "માપદંડ"), T("Note", "નોંધ")],
                  [[T("GRIHA", "GRIHA"), T("MNRE and TERI", "MNRE અને TERI"), T("1 to 5 stars", "1 થી 5 સ્ટાર"), T("Indian climate and materials, strong on passive design", "ભારતીય હવામાન અને સામગ્રી, નિષ્ક્રિય ડિઝાઇન પર ભાર")],
                   [T("IGBC", "IGBC"), T("Confederation of Indian Industry", "ભારતીય ઉદ્યોગ પરિષદ"), T("certified, silver, gold, platinum", "પ્રમાણિત, સિલ્વર, ગોલ્ડ, પ્લેટિનમ"), T("widest used in India, many building types", "ભારતમાં સૌથી વધુ વપરાય, ઘણા પ્રકારની ઇમારતો")],
                   [T("LEED", "LEED"), T("US Green Building Council", "અમેરિકન લીલી ઇમારત પરિષદ"), T("40 to 110 points", "40 થી 110 પોઇન્ટ"), T("international, recognised by global tenants", "આંતરરાષ્ટ્રીય, વૈશ્વિક ભાડુઆતો માને")],
                   [T("ECBC", "ECBC"), T("Bureau of Energy Efficiency", "ઊર્જા દક્ષતા બ્યુરો"), T("code, not a label", "નિયમાવલી, લેબલ નહીં"), T("mandatory energy code for commercial buildings", "વ્યાપારી ઇમારતો માટે ફરજિયાત ઊર્જા નિયમાવલી")]]),
               H4("What the numbers look like", "આંકડા કેવા દેખાય"),
               P("A rated building typically cuts energy 30-50 % and water 20-40 % against a conventional "
                 "one of the same size, at a capital cost 3-8 % higher; the payback comes from the "
                 "electricity and water bill within five to seven years, and the rent and resale value "
                 "are higher. The <b>energy performance index</b> (kWh per m² per year) is the number to "
                 "compare: a conventional Indian office runs at 200-250, a good green one at 90-120 and "
                 "a super-efficient one below 70.",
                 "રેટેડ ઇમારત સામાન્ય રીતે સમાન કદની પરંપરાગત ઇમારત સામે ઊર્જા 30-50 % અને પાણી 20-40 % ઘટાડે, "
                 "3-8 % વધુ મૂડી ખર્ચે; પરતફેળો પાંચથી સાત વર્ષમાં વીજળી-પાણીના બિલમાંથી આવે, અને ભાડું તથા "
                 "વેચાણ કિંમત વધુ હોય. સરખાવવાનો આંકડો <b>ઊર્જા કાર્યદક્ષતા સૂચકાંક</b> (વર્ષે પ્રતિ m² kWh) છે: "
                 "સામાન્ય ભારતીય ઓફિસ 200-250, સારી લીલી ઓફિસ 90-120 અને અતિ-કાર્યક્ષમ 70થી નીચે.")],
              syllabus_item="5.3"),
         card(T("5.3 Cradle to cradle, life cycle analysis, green labels and carbon credits",
                "5.3 ક્રેડલ ટુ ક્રેડલ, જીવનચક્ર આકલન, લીલું લેબલ અને કાર્બન ક્રેડિટ"),
              [H4("Cradle to cradle", "ક્રેડલ ટુ ક્રેડલ"),
               P("The old model is <b>cradle to grave</b>: dig, make, use, throw away. <b>Cradle to "
                 "cradle</b> designs the product so that at the end of its life every part becomes food "
                 "for something else - a <b>biological nutrient</b> that returns to the soil, or a "
                 "<b>technical nutrient</b> that returns to industry at the same quality. A chair with "
                 "a glued foam seat cannot be taken apart and becomes waste; the same chair with a "
                 "bolted steel frame and a wool cover becomes a frame and a cover, both reusable.",
                 "જૂનું નમૂનો <b>ક્રેડલ ટુ ગ્રેવ</b> છે: ખોદો, બનાવો, વાપરો, ફેંકો. <b>ક્રેડલ ટુ ક્રેડલ</b> "
                 "ઉત્પાદન એવી રીતે રચે કે તેના આયુષ્યના અંતે દરેક ભાગ બીજા કંઈકનો ખોરાક બને - <b>જૈવિક પોષક</b> "
                 "જે જમીનમાં પાછું જાય, કે <b>ટેકનિકલ પોષક</b> જે એ જ ગુણવત્તાએ ઉદ્યોગમાં પાછું જાય. ગુંદરવાળી ફોમ "
                 "સીટવાળી ખુરશી છૂટી ન થઈ શકે તેથી કચરો બને; એ જ ખુરશી બોલ્ટવાળી પોલાદ ફ્રેમ અને ઊનના આવરણ સાથે "
                 "ફ્રેમ અને આવરણ બંને બને, જે ફરી વપરાય."),
               H4("Life cycle analysis", "જીવનચક્ર આકલન"),
               P("A <b>life cycle analysis</b> adds up every input and output from raw material to "
                 "disposal, in four steps: <b>goal and scope</b> (what is compared and where the "
                 "boundary is drawn), <b>inventory</b> (the energy, water, emissions and waste per unit "
                 "of the product), <b>impact assessment</b> (what that inventory means for warming, "
                 "acidification, water use and toxicity) and <b>interpretation</b>. The boundary decides "
                 "the answer: a paper cup may look better than a ceramic cup if the ceramic one is used "
                 "only five times and washed in hot water.",
                 "<b>જીવનચક્ર આકલન</b> કાચા માલથી નિકાલ સુધીનું દરેક ઇનપુટ-આઉટપુટ ચાર પગલામાં જોડે: "
                 "<b>ધ્યેય અને વ્યાપ</b> (શું સરખાય છે અને સીમા ક્યાં દોરાય), <b>યાદી</b> (ઉત્પાદનના એકમ દીઠ ઊર્જા, "
                 "પાણી, ઉત્સર્જન અને કચરો), <b>અસર આકલન</b> (તે યાદી ગરમી, અમ્લતા, પાણીના વપરાશ અને ઝેર માટે શું "
                 "અર્થ ધરે) અને <b>અર્થઘટન</b>. સીમા જવાબ નક્કી કરે: કાગળનો કપ માટીના કપ કરતાં સારો લાગે જો માટીનો "
                 "કપ ફક્ત પાંચ વાર વપરાય અને ગરમ પાણીથી ધોવાય."),
               H4("Green label and carbon credit", "લીલું લેબલ અને કાર્બન ક્રેડિટ"),
               TB([T("Instrument", "સાધન"), T("What it is", "શું છે"), T("Example", "ઉદાહરણ")],
                  [[T("green label", "લીલું લેબલ"), T("a mark awarded to a product that meets a published environmental criterion", "પ્રકાશિત પર્યાવરણીય માપદંડ પૂરો કરતા ઉત્પાદનને અપાતું ચિહ્ન"), T("BIS Eco Mark, Energy Star, EPEAT for electronics", "BIS ઇકો માર્ક, એનર્જી સ્ટાર, ઇલેક્ટ્રોનિક્સ માટે EPEAT")],
                   [T("green building label", "લીલી ઇમારત લેબલ"), T("a rating for a whole building", "આખી ઇમારત માટે રેટિંગ"), T("GRIHA 4 star, IGBC gold", "GRIHA 4 સ્ટાર, IGBC ગોલ્ડ")],
                   [T("carbon credit", "કાર્બન ક્રેડિટ"), T("one tonne of CO₂ avoided, reduction or removed, verified and tradeable", "ટાળેલું, ઘટાડેલું કે દૂર કરેલું એક ટન CO₂, ચકાસાયેલ અને વ્યાપારી"), T("a cookstove or a wind project earns credits", "ચૂલો કે પવન પ્રોજેક્ટ ક્રેડિટ કમાય")],
                   [T("carbon tax", "કાર્બન કર"), T("a price on every tonne emitted, paid to the government", "છોડેલા દરેક ટન પર ભાવ, સરકારને ચૂકવાય"), T("in force in the EU, not in India", "યુરોપમાં અમલમાં, ભારતમાં નહીં")]]),
               H4("Advantages and disadvantages of carbon credits", "કાર્બન ક્રેડિટના લાભ અને ખામી"),
               UL(("advantage: money from a rich country or company funds a clean project in a poor one, "
                   "which is the cheapest abatement first", "લાભ: શ્રીમંત દેશ કે કંપનીનું નાણું ગરીબ દેશમાં "
                   "સ્વચ્છ પ્રોજેક્ટ ભંડોળે, જે સૌથી સસ્તો ઘટાડો પહેલાં"),
                  ("advantage: the credit pays for itself from the carbon market instead of a subsidy",
                   "લાભ: ક્રેડિટ સબસિડીને બદલે કાર્બન બજારમાંથી પોતાનો ખર્ચ કાઢે"),
                  ("disadvantage: the project may have happened anyway - <b>additionality</b> is hard to "
                   "prove", "ખામી: પ્રોજેક્ટ કોઈ પણ રીતે થાત - <b>અતિરિક્તતા</b> પુરવાર કરવી કઠિન"),
                  ("disadvantage: a cheap credit can excuse a rich buyer who goes on emitting instead of "
                   "cutting", "ખામી: સસ્તી ક્રેડિટ ઘટાડવાને બદલે છોડતા રહેતા શ્રીમંત ખરીદનારને બહાનું આપે"),
                  ("disadvantage: measurement and verification cost, and credits can be double counted",
                   "ખામી: માપન અને ચકાસણીનો ખર્ચ, અને ક્રેડિટ બે વાર ગણાઈ શકે")),
               H4("Worked example", "ઉકેલાયેલ દાખલો"),
               P("A 20 MW wind project in Gujarat generates 48 GWh a year and displaces coal power at "
                 "0.9 t CO₂ per MWh, so it avoids 48,000 × 0.9 = 43,200 t a year. At four dollars a "
                 "credit that is about 1.73 lakh dollars - useful, but far less than the electricity "
                 "revenue, which is why credits complement a viable tariff and cannot replace it.",
                 "ગુજરાતમાં 20 MW પવન પ્રોજેક્ટ વર્ષે 48 GWh બનાવે અને પ્રતિ MWh 0.9 t CO₂ પ્રમાણે કોલસા વીજળી "
                 "બદલે, તેથી વર્ષે 48,000 × 0.9 = 43,200 t CO₂ ટાળે. પ્રતિ ક્રેડિટ ચાર ડોલરે તે લગભગ 1.73 લાખ "
                 "ડોલર - ઉપયોગી, પણ વીજળીની આવક કરતાં ઘણું ઓછું, તેથી ક્રેડિટ ટકાઉ ટેરિફને પૂરક છે, તેનો વિકલ્પ "
                 "નહીં.")],
              "u5_credits", syllabus_item="5.3"),
     ]},
    {"title": T("4. The 5R and Eco Tourism", "4. 5R અને પર્યાવરણ પર્યટન"),
     "items": [
         card(T("5.4 The 5R: refuse, reduce, reuse, repurpose, recycle",
                "5.4 5R: નકારો, ઘટાડો, ફરી વાપરો, નવો ઉપયોગ કરો, રિસાયકલ કરો"),
              [H4("Why the order matters", "ક્રમ કેમ મહત્ત્વનો છે"),
               P("The five Rs are a ladder, and the top rung is the one that saves the most. <b>Refuse</b> "
                 "means not taking what you do not need - the plastic bag, the straw, the extra "
                 "packaging - so nothing has to be made, carried, cleaned or recycled. <b>Reduce</b> "
                 "means using less of what you must take. <b>Reuse</b> means using the same object again "
                 "for the same purpose. <b>Repurpose</b> means giving it a different second life, such "
                 "as a paint tin that becomes a planter. <b>Recycle</b> is last, because it needs "
                 "energy, transport and a market, and it loses quality every time.",
                 "પાંચ R એ સોપાન છે અને સૌથી ઉપરનું પગથિયું સૌથી વધુ બચાવે. <b>નકારો</b> એટલે જે જરૂરી નથી તે "
                 "ન લેવું - પ્લાસ્ટિક થેલી, સ્ટ્રો, વધારાનું પેકિંગ - તેથી કંઈ બનાવવું, લઈ જવું, ધોવું કે રિસાયકલ "
                 "કરવું ન પડે. <b>ઘટાડો</b> એટલે જે લેવું જ પડે તેનો ઓછો વપરાશ. <b>ફરી વાપરો</b> એટલે એ જ વસ્તુ "
                 "એ જ કામ માટે ફરી વાપરવી. <b>નવો ઉપયોગ</b> એટલે તેને બીજું જીવન આપવું, જેમ કે રંગની ટિન બગીચાનું "
                 "કૂંડું બને. <b>રિસાયકલ</b> છેલ્લે, કારણ કે તેને ઊર્જા, વહન અને બજાર જોઈએ, અને દરેક વખતે ગુણવત્તા "
                 "ઘટે."),
               H4("What each rung looks like in practice", "વ્યવહારમાં દરેક પગથિયું કેવું દેખાય"),
               TB([T("R", "R"), T("Meaning", "અર્થ"), T("Household example", "ઘરનું ઉદાહરણ"), T("Savings", "બચત")],
                  [[T("Refuse", "નકારો"), T("do not accept it", "ન સ્વીકારો"), T("cloth bag at the shop, say no to a straw", "દુકાને કાપડની થેલી, સ્ટ્રોને ના"), T("no material, no waste, no cost", "સામગ્રી નહીં, કચરો નહીં, ખર્ચ નહીં")],
                   [T("Reduce", "ઘટાડો"), T("use less of it", "ઓછું વાપરો"), T("bucket bath, half-flush, LED lamp", "ડોલથી સ્નાન, અડધું ફ્લશ, LED દીવો"), T("water 40 %, power 80 %", "પાણી 40 %, વીજ 80 %")],
                   [T("Reuse", "ફરી વાપરો"), T("same object, same job", "એ જ વસ્તુ, એ જ કામ"), T("steel bottle, refilled printer cartridge", "પોલાદની બોટલ, ફરી ભરેલી પ્રિન્ટર શાહી"), T("no new manufacture", "નવું ઉત્પાદન નહીં")],
                   [T("Repurpose", "નવો ઉપયોગ"), T("same object, new job", "એ જ વસ્તુ, નવું કામ"), T("tyre as a planter, jar as a pen stand", "ટાયર કૂંડું, બરણી પેન સ્ટેન્ડ"), T("delays the trip to the bin", "કચરાપેટી સુધીની મુસાફરી લંબાવે")],
                   [T("Recycle", "રિસાયકલ"), T("break it down into material", "તેને સામગ્રીમાં તોડો"), T("paper, metal, PET, e-waste to a recycler", "કાગળ, ધાતુ, PET, ઇ-કચરો રિસાયકલરને"), T("saves ore and energy, loses quality", "ધાતુ અને ઊર્જા બચે, ગુણવત્તા ઘટે")]]),
               H4("Why recycling cannot be the main answer", "રિસાયકલ મુખ્ય જવાબ કેમ ન બની શકે"),
               P("Recycling works only if three things are true at once: the material is clean and "
                 "single, a local processor exists, and there is a buyer for the output. Mixed, wet and "
                 "food-soiled waste fails all three, which is why segregation at source is the whole "
                 "game. A city that collects mixed waste can recycle maybe 10-15 %; the same city with "
                 "two-bin segregation recycles 50-60 % of the dry fraction and composts the wet half.",
                 "રિસાયકલ ત્યારે જ ચાલે જ્યારે ત્રણ વસ્તુ એકસાથે સાચી હોય: સામગ્રી સ્વચ્છ અને એક જ પ્રકારની હોય, "
                 "સ્થાનિક પ્રોસેસર હોય અને પરિણામનો ખરીદનાર હોય. મિશ્ર, ભીનો અને ખોરાકથી મેલો કચરો ત્રણેયમાં નિષ્ફળ "
                 "જાય, તેથી સ્રોત પર અલગીકરણ જ આખી રમત છે. મિશ્ર કચરો ઉપાડતું શહેર લગભગ 10-15 % રિસાયકલ કરી "
                 "શકે; બે-ડબ્બા અલગીકરણવાળું એ જ શહેર સૂકા ભાગનું 50-60 % રિસાયકલ કરે અને ભીનો અડધો ખાતર બનાવે."),
               H4("Worked example", "ઉકેલાયેલ દાખલો"),
               P("A housing society of 200 flats throws 400 kg of waste a day. Refusing and reducing cuts "
                 "it to 340 kg; segregating 60 % as wet waste gives 204 kg of compost a day, worth about "
                 "Rs 2,000 a month, and 136 kg of dry waste that a recycler will pay for - the entire "
                 "waste becomes a resource and the landfill bill disappears.",
                 "200 ફ્લેટની સોસાયટી દિવસે 400 કિલો કચરો ફેંકે. નકારવા અને ઘટાડવાથી તે 340 કિલો થાય; 60 % ભીનો "
                 "કચરો અલગ કરવાથી દિવસે 204 કિલો ખાતર, મહિને લગભગ રૂ. 2,000નું, અને 136 કિલો સૂકો કચરો જે "
                 "રિસાયકલર ખરીદે - આખો કચરો સંસાધન બને અને લેન્ડફિલનું બિલ ગાયબ થાય.")],
              "u5_5r", syllabus_item="5.4"),
         card(T("5.5 Eco tourism: advantages and disadvantages",
                "5.5 પર્યાવરણ પર્યટન: લાભ અને ખામી"),
              [H4("What eco tourism is", "પર્યાવરણ પર્યટન એટલે શું"),
               P("<b>Eco tourism</b> is responsible travel to a natural area that conserves the "
                 "environment, sustains the local people and includes interpretation and education. "
                 "Three tests separate it from ordinary tourism: it protects the place it visits, it "
                 "leaves most of the money with the local community, and it teaches the visitor. A "
                 "homestay run by a village beside a sanctuary that trains local guides and keeps the "
                 "trail clean passes all three; a resort that flies in water and drives jeeps through "
                 "the same sanctuary does not.",
                 "<b>પર્યાવરણ પર્યટન</b> એ કુદરતી વિસ્તારમાં જવાબદાર મુસાફરી છે જે પર્યાવરણ સાચવે, સ્થાનિક "
                 "લોકોને ટકાવે અને સમજૂતી તથા શિક્ષણ સમાવે. સામાન્ય પર્યટનથી તેને ત્રણ કસોટી અલગ પાડે: તે જે "
                 "જગ્યાએ જાય તેને બચાવે, નાણાનો મોટો ભાગ સ્થાનિક સમુદાય સાથે રાખે, અને પ્રવાસીને શીખવે. "
                 "અભયારણ્ય પાસેનું ગામ ચલાવતું હોમસ્ટે જે સ્થાનિક ગાઇડને તાલીમ આપે અને પગપાળા માર્ગ સાફ રાખે તે "
                 "ત્રણેય પૂરો કરે; પાણી વિમાનમાં લાવતું અને એ જ અભયારણ્યમાં જીપ દોડાવતું રિસોર્ટ નહીં."),
               H4("Advantages", "લાભ"),
               UL(("conservation pays: a tiger, a reef or a bird that brings visitors is worth more alive "
                   "than cut", "સંરક્ષણ ચૂકવાય: પ્રવાસી લાવતો વાઘ, ભરતી કે પક્ષી કાપેલા કરતાં જીવતો વધુ "
                   "કિંમતી"),
                  ("local jobs: guides, homestays, drivers, cooks and handicraft, which reduce migration",
                   "સ્થાનિક રોજગાર: ગાઇડ, હોમસ્ટે, ડ્રાઇવર, રસોઇયા અને હસ્તકલા, જે સ્થળાંતર ઘટાડે"),
                  ("education: a visitor who sees a mangrove or a coral reef defends it at home",
                   "શિક્ષણ: કાંદાનું જંગલ કે ભરતી જોયેલો પ્રવાસી ઘરે તેનો બચાવ કરે"),
                  ("income for a protected area, which can pay for patrols and fences instead of the "
                   "forest department alone", "સંરક્ષિત વિસ્તારને આવક, જે પહેરા અને વાડ માટે ચૂકવે, ફક્ત "
                   "વન વિભાગ નહીં"),
                  ("low infrastructure: a trail, a homestay and a guide need less concrete than a theme "
                   "park", "ઓછું માળખું: પગપાળા માર્ગ, હોમસ્ટે અને ગાઇડને થીમ પાર્ક કરતાં ઓછું કોંક્રિટ જોઈએ")),
               H4("Disadvantages", "ખામી"),
               UL(("greenwashing: the label is used for marketing while the operation is ordinary mass "
                   "tourism", "લીલું ધોવું: લેબલ માર્કેટિંગ માટે વપરાય જ્યારે કામ સામાન્ય સામૂહિક પર્યટન હોય"),
                  ("carrying capacity: a trail or a reef has a limit, and beyond it the very thing the "
                   "visitor came to see is damaged", "વહન ક્ષમતા: પગપાળા માર્ગ કે ભરતીની મર્યાદા હોય, અને તે "
                   "પછી પ્રવાસી જે જોવા આવ્યો તે જ વસ્તુ નુકસાન પામે"),
                  ("wildlife disturbance: noise, vehicles, feeding and night lights change animal "
                   "behaviour and breeding", "વન્યજીવનમાં ખલેલ: ઘોંઘાટ, વાહન, ખોરાક આપવો અને રાત્રિના દીવા "
                   "પ્રાણીની આદત અને પ્રજનન બદલે"),
                  ("leakage: in an enclave resort most of the money leaves the district, so the local "
                   "community carries the cost and gets little", "લીકેજ: બંધિયાર રિસોર્ટમાં મોટું નાણું જિલ્લો "
                   "છોડી જાય, તેથી સ્થાનિક સમુદાય ખર્ચ ઉઠાવે અને થોડું પામે"),
                  ("waste and water: a hill homestay can generate more plastic and sewage than the "
                   "village can handle", "કચરો અને પાણી: ડુંગરાળ હોમસ્ટે ગામ સંભાળી શકે તેનાથી વધુ પ્લાસ્ટિક અને "
                   "ગટર બનાવે")),
               H4("How to keep it honest", "તેને પ્રામાણિક કેમ રાખવું"),
               TB([T("Tool", "સાધન"), T("How it works", "કેવી રીતે ચાલે")],
                  [[T("carrying capacity study", "વહન ક્ષમતા અભ્યાસ"), T("fix the number of visitors a trail, beach or reef can take per day", "પગપાળા માર્ગ, દરિયાકિનારો કે ભરતી રોજ કેટલા પ્રવાસી સહે તે નક્કી કરે")],
                   [T("community ownership", "સમુદાય માલિકી"), T("the homestay, the guide cooperative and the gate fee belong to the village", "હોમસ્ટે, ગાઇડ સહકારી મંડળી અને પ્રવેશ ફી ગામની")],
                   [T("permits and zoning", "પરવાનગી અને વિભાજન"), T("core zone closed, buffer for guided walks only", "મુખ્ય વિસ્તાર બંધ, બફરમાં ફક્ત ગાઇડ સાથે પગપાળા")],
                   [T("certification", "પ્રમાણીકરણ"), T("Green Globe, Ecotourism Society or state eco-label audited yearly", "ગ્રીન ગ્લોબ, ઇકોટૂરિઝમ સોસાયટી કે રાજ્ય ઇકો-લેબલ દર વર્ષે તપાસે")]]),
               H4("Worked example", "ઉકેલાયેલ દાખલો"),
               P("A 5 km forest trail can carry 20 visitors a kilometre a day without damage, so the "
                 "ceiling is 100 visitors a day, or 30,000 a year over 300 open days. At a Rs 150 gate "
                 "fee that is Rs 45 lakh a year, enough for four local guides, a toilet block and "
                 "maintenance - provided the ceiling is enforced on the busiest weekends.",
                 "5 કિલોમીટરનો વન માર્ગ નુકસાન વગર કિલોમીટર દીઠ રોજ 20 પ્રવાસી સહે, તેથી મર્યાદા દિવસે 100 "
                 "પ્રવાસી, એટલે 300 ખુલ્લા દિવસમાં વર્ષે 30,000. રૂ. 150 પ્રવેશ ફી પર તે વર્ષે રૂ. 45 લાખ, જે ચાર "
                 "સ્થાનિક ગાઇડ, શૌચાલય અને જાળવણી માટે પૂરતું - જો સૌથી વ્યસ્ત સપ્તાહાંતે મર્યાદા લાગુ પડે.")],
              "u5_eco", syllabus_item="5.5"),
     ]},
]

NUMERICALS = [
    num("u5n01", T("Rain water harvestable from a roof.", "છત પરથી એકઠું કરી શકાય તેવું વરસાદી જળ."),
        T("A building has a 400 m² concrete roof in a district with 900 mm of annual rain. The runoff "
          "coefficient is 0.85. Find the water harvestable in a year and its value at Rs 60 per m³.",
          "એક ઇમારતની 400 m² કોંક્રિટ છત છે અને જિલ્લામાં વર્ષે 900 mm વરસાદ પડે છે. વહેવાનો અવયવ 0.85 છે. "
          "વર્ષમાં એકઠું થતું પાણી અને પ્રતિ m³ રૂ. 60 પ્રમાણે તેની કિંમત શોધો."),
        [P("Rain in metres = 900 / 1,000 = 0.9 m", "વરસાદ મીટરમાં = 900 / 1,000 = 0.9 m"),
         P("Volume = area × rain × coefficient = 400 × 0.9 × 0.85 = 306 m³",
           "ઘનફળ = ક્ષેત્રફળ × વરસાદ × અવયવ = 400 × 0.9 × 0.85 = 306 m³"),
         P("Value = 306 × 60 = Rs 18,360 a year, plus the recharge to the borewell",
           "કિંમત = 306 × 60 = વર્ષે રૂ. 18,360, ઉપરાંત બોરવેલમાં ભરાવો")],
        T("306 m³ a year, worth about Rs 18,400", "વર્ષે 306 m³, લગભગ રૂ. 18,400નું"), unit_no=5),
    num("u5n02", T("Sizing a storage tank for the dry spell.",
                   "સૂકા સમય માટે સંગ્રહ ટાંકીનું માપ."),
        T("A household needs 500 L a day and the longest rainless spell in the district is 70 days. The "
          "tank is to cover half of that spell. Find the tank volume and the roof area needed if the "
          "seasonal rain is 800 mm with a coefficient of 0.8.",
          "ઘરને દિવસે 500 લિટર જોઈએ અને જિલ્લામાં સૌથી લાંબો વરસાદ વગરનો સમય 70 દિવસ છે. ટાંકીએ તે સમયનો "
          "અડધો ભાગ પૂરવો છે. ટાંકીનું ઘનફળ અને જરૂરી છતનું ક્ષેત્રફળ શોધો, જો ઋતુનો વરસાદ 800 mm અને અવયવ 0.8 હોય."),
        [P("Tank = 500 × 35 = 17,500 L = 17.5 m³", "ટાંકી = 500 × 35 = 17,500 લિટર = 17.5 m³"),
         P("A 20 m³ tank leaves a margin for a longer spell", "20 m³ ટાંકી લાંબા સમય માટે માર્જિન રાખે"),
         P("Roof = 17.5 / (0.8 × 0.8) = 27.3 m², so a 30 m² roof fills the tank",
           "છત = 17.5 / (0.8 × 0.8) = 27.3 m², તેથી 30 m² છત ટાંકી ભરે")],
        T("A 20 m³ tank and about 30 m² of roof", "20 m³ ટાંકી અને લગભગ 30 m² છત"), unit_no=5),
    num("u5n03", T("Pollution load against a consent condition.",
                   "સંમતિની શરત સામે પ્રદૂષણ ભાર."),
        T("An effluent stream is 400 m³ a day with BOD 220 mg/L. The consent allows 30 mg/L. Find the "
          "BOD load in kg per day, the permitted load and the excess.",
          "એક પ્રવાહ દિવસે 400 m³ છે અને BOD 220 mg/L છે. સંમતિ 30 mg/L મંજૂર કરે છે. દૈનિક BOD ભાર કિલોમાં, "
          "મંજૂર ભાર અને વધારો શોધો."),
        [P("Load = flow × concentration = 400 × 220 / 1,000 = 88 kg a day",
           "ભાર = પ્રવાહ × સાંદ્રતા = 400 × 220 / 1,000 = 88 કિલો દિવસે"),
         P("Permitted = 400 × 30 / 1,000 = 12 kg a day", "મંજૂર = 400 × 30 / 1,000 = 12 કિલો દિવસે"),
         P("Excess = 88 − 12 = 76 kg a day, 7.3 times the limit",
           "વધારો = 88 − 12 = 76 કિલો દિવસે, મર્યાદાના 7.3 ગણો"),
         P("Section 33A of the Water Act allows the Board to stop the supply of water and power",
           "જળ અધિનિયમની કલમ 33A બોર્ડને પાણી અને વીજળી બંધ કરવાની સત્તા આપે")],
        T("88 kg a day against 12 kg permitted, an excess of 76 kg",
          "મંજૂર 12 કિલો સામે દિવસે 88 કિલો, 76 કિલો વધારો"), unit_no=5),
    num("u5n04", T("Carbon credits earned by a wind project.",
                   "પવન પ્રોજેક્ટ કમાયેલી કાર્બન ક્રેડિટ."),
        T("A 25 MW wind farm runs at a 28 % capacity factor and displaces grid power at 0.82 t CO₂ per "
          "MWh. Find its annual energy, the CO₂ avoided and the credit revenue at 5 dollars a tonne.",
          "25 MW પવન ફાર્મ 28 % ક્ષમતા અવયવે ચાલે અને પ્રતિ MWh 0.82 t CO₂ વાળી ગ્રિડ વીજળી બદલે. તેની "
          "વાર્ષિક ઊર્જા, બચતનું CO₂ અને પ્રતિ ટન 5 ડોલરે ક્રેડિટ આવક શોધો."),
        [P("Energy = 25 × 8,760 × 0.28 = 61,320 MWh = 61.3 GWh",
           "ઊર્જા = 25 × 8,760 × 0.28 = 61,320 MWh = 61.3 GWh"),
         P("CO₂ avoided = 61,320 × 0.82 = 50,282 t a year", "બચતનું CO₂ = 61,320 × 0.82 = 50,282 t વર્ષે"),
         P("Credits = 50,282, worth 50,282 × 5 = 2.51 lakh dollars",
           "ક્રેડિટ = 50,282, કિંમત 50,282 × 5 = 2.51 લાખ ડોલર")],
        T("61.3 GWh, 50,282 t CO₂ avoided, about 2.51 lakh dollars",
          "61.3 GWh, 50,282 t CO₂ બચત, લગભગ 2.51 લાખ ડોલર"), unit_no=5),
    num("u5n05", T("Energy performance index of a green building.",
                   "લીલી ઇમારતનો ઊર્જા કાર્યદક્ષતા સૂચકાંક."),
        T("An office of 4,000 m² uses 9,60,000 kWh a year. A retrofitted version of the same building "
          "uses 5,60,000 kWh. Find the EPI of both and the saving in money and CO₂ at Rs 8 a unit and "
          "0.71 kg CO₂ per kWh.",
          "4,000 m²ની ઓફિસ વર્ષે 9,60,000 kWh વાપરે છે. તે જ ઇમારતનું સુધારેલું સ્વરૂપ 5,60,000 kWh વાપરે છે. "
          "બંનેનો EPI અને પ્રતિ યુનિટ રૂ. 8 તથા પ્રતિ kWh 0.71 કિલો CO₂ પ્રમાણે નાણા અને CO₂ની બચત શોધો."),
        [P("EPI before = 9,60,000 / 4,000 = 240 kWh/m²/yr",
           "પહેલાં EPI = 9,60,000 / 4,000 = 240 kWh/m²/વર્ષ"),
         P("EPI after = 5,60,000 / 4,000 = 140 kWh/m²/yr, a cut of 42 %",
           "પછી EPI = 5,60,000 / 4,000 = 140 kWh/m²/વર્ષ, 42 % ઘટાડો"),
         P("Saving = 4,00,000 kWh = Rs 32 lakh a year", "બચત = 4,00,000 kWh = વર્ષે રૂ. 32 લાખ"),
         P("CO₂ avoided = 4,00,000 × 0.71 / 1,000 = 284 t a year",
           "બચતનું CO₂ = 4,00,000 × 0.71 / 1,000 = 284 t વર્ષે")],
        T("240 down to 140 kWh/m²/yr; Rs 32 lakh and 284 t CO₂ a year",
          "240 થી 140 kWh/m²/વર્ષ; વર્ષે રૂ. 32 લાખ અને 284 t CO₂"), unit_no=5),
    num("u5n06", T("Significance score of an environmental aspect.",
                   "પર્યાવરણીય પાસાંનો મહત્ત્વ અંક."),
        T("An ISO 14001 team scores each aspect as severity × probability × quantity, each on a scale "
          "of 1 to 5. Score the spent acid bath (5, 4, 3), the diesel tank (4, 3, 3) and office paper "
          "(1, 5, 4), and state which aspects are significant above a threshold of 40.",
          "ISO 14001 ટીમ દરેક પાસાંને તીવ્રતા × શક્યતા × માત્રા તરીકે 1 થી 5ના માપે અંક આપે છે. વપરાયેલા "
          "એસિડ સ્નાન (5, 4, 3), ડીઝલ ટાંકી (4, 3, 3) અને ઓફિસ કાગળ (1, 5, 4)ને અંક આપો અને 40થી ઉપરની મર્યાદાએ "
          "કયાં પાસાં મહત્ત્વનાં છે તે જણાવો."),
        [P("Acid bath = 5 × 4 × 3 = 60", "એસિડ સ્નાન = 5 × 4 × 3 = 60"),
         P("Diesel tank = 4 × 3 × 3 = 36", "ડીઝલ ટાંકી = 4 × 3 × 3 = 36"),
         P("Office paper = 1 × 5 × 4 = 20", "ઓફિસ કાગળ = 1 × 5 × 4 = 20"),
         P("Only the acid bath crosses 40, so it gets the written procedure, the secondary containment "
           "and the monthly inspection", "ફક્ત એસિડ સ્નાન 40 વટાવે, તેથી તેને લેખિત પ્રક્રિયા, બેવડું રોકાણ "
           "અને માસિક તપાસ મળે")],
        T("Acid bath 60 is significant; diesel 36 and paper 20 are not",
          "એસિડ સ્નાન 60 મહત્ત્વનું; ડીઝલ 36 અને કાગળ 20 નહીં"), unit_no=5),
    num("u5n07", T("Carrying capacity of an eco tourism trail.",
                   "પર્યાવરણ પર્યટન માર્ગની વહન ક્ષમતા."),
        T("A 6 km trail can take 15 visitors per kilometre a day. It is open 300 days a year and the "
          "gate fee is Rs 120. Find the annual visitor ceiling and the revenue, and the revenue if use "
          "is held to 70 % of the ceiling.",
          "6 કિલોમીટરનો માર્ગ રોજ કિલોમીટર દીઠ 15 પ્રવાસી સહે છે. તે વર્ષે 300 દિવસ ખુલ્લો રહે અને પ્રવેશ ફી "
          "રૂ. 120 છે. વાર્ષિક મર્યાદા અને આવક, તથા મર્યાદાના 70 % પર રાખીએ તો આવક શોધો."),
        [P("Daily ceiling = 6 × 15 = 90 visitors", "દૈનિક મર્યાદા = 6 × 15 = 90 પ્રવાસી"),
         P("Annual = 90 × 300 = 27,000 visitors", "વાર્ષિક = 90 × 300 = 27,000 પ્રવાસી"),
         P("Revenue at the ceiling = 27,000 × 120 = Rs 32.4 lakh",
           "મર્યાદાએ આવક = 27,000 × 120 = રૂ. 32.4 લાખ"),
         P("At 70 % use = 18,900 visitors and Rs 22.7 lakh, which the trail can carry for decades",
           "70 % વપરાશે = 18,900 પ્રવાસી અને રૂ. 22.7 લાખ, જે માર્ગ દાયકાઓ સુધી સહી શકે")],
        T("27,000 a year at the ceiling; 18,900 and Rs 22.7 lakh at 70 %",
          "મર્યાદાએ વર્ષે 27,000; 70 % પર 18,900 અને રૂ. 22.7 લાખ"), unit_no=5),
    num("u5n08", T("Waste after segregation in a housing society.",
                   "સોસાયટીમાં અલગીકરણ પછીનો કચરો."),
        T("A society of 240 flats generates 0.5 kg per flat a day. After the 5R programme the quantity "
          "falls 15 %, and 60 % of what remains is wet waste that becomes compost at 25 % of its mass. "
          "Find the compost per day and the waste that still goes to the landfill.",
          "240 ફ્લેટની સોસાયટી ફ્લેટ દીઠ દિવસે 0.5 કિલો કચરો બનાવે. 5R કાર્યક્રમ પછી માત્રા 15 % ઘટે અને "
          "બાકીના 60 % ભીનો કચરો ખાતર બને જે તેના દળના 25 % થાય. દૈનિક ખાતર અને લેન્ડફિલ જતો કચરો શોધો."),
        [P("Waste = 240 × 0.5 = 120 kg a day", "કચરો = 240 × 0.5 = 120 કિલો દિવસે"),
         P("After 5R = 120 × 0.85 = 102 kg", "5R પછી = 120 × 0.85 = 102 કિલો"),
         P("Wet waste = 0.60 × 102 = 61.2 kg, compost = 0.25 × 61.2 = 15.3 kg",
           "ભીનો કચરો = 0.60 × 102 = 61.2 કિલો, ખાતર = 0.25 × 61.2 = 15.3 કિલો"),
         P("Landfill = 102 − 61.2 = 40.8 kg, less the dry waste a recycler buys",
           "લેન્ડફિલ = 102 − 61.2 = 40.8 કિલો, જેમાંથી રિસાયકલર ખરીદતો સૂકો કચરો બાદ")],
        T("15.3 kg of compost and about 41 kg to the landfill, down from 120 kg",
          "15.3 કિલો ખાતર અને લેન્ડફિલે લગભગ 41 કિલો, 120 કિલોમાંથી"), unit_no=5),
    num("u5n09", T("Water saved by low-flow fixtures.", "ઓછા પ્રવાહનાં નળથી બચતું પાણી."),
        T("A hostel of 150 students replaces 10 L per flush cisterns with 5 L dual-flush and 8 L per "
          "minute taps with 4 L aerated taps. Each student flushes 4 times and uses the tap for 6 "
          "minutes a day. Find the water saved a day and a year.",
          "150 વિદ્યાર્થીઓની છાત્રાલય 10 લિટરના ફ્લશને 5 લિટરના બેવડા ફ્લશથી અને 8 લિટર પ્રતિ મિનિટના નળને "
          "4 લિટર હવા-મિશ્રિત નળથી બદલે છે. દરેક વિદ્યાર્થી દિવસે 4 વાર ફ્લશ કરે અને નળ 6 મિનિટ વાપરે. દૈનિક અને "
          "વાર્ષિક બચત શોધો."),
        [P("Flush saving = 4 × (10 − 5) = 20 L per student a day", "ફ્લશ બચત = 4 × (10 − 5) = 20 લિટર પ્રતિ વિદ્યાર્થી"),
         P("Tap saving = 6 × (8 − 4) = 24 L per student a day", "નળ બચત = 6 × (8 − 4) = 24 લિટર પ્રતિ વિદ્યાર્થી"),
         P("Total = 44 × 150 = 6,600 L a day", "કુલ = 44 × 150 = 6,600 લિટર દિવસે"),
         P("A year = 6,600 × 365 = 24.1 lakh litres, about 2,400 m³",
           "વર્ષે = 6,600 × 365 = 24.1 લાખ લિટર, લગભગ 2,400 m³")],
        T("6,600 L a day and about 2,400 m³ a year",
          "દિવસે 6,600 લિટર અને વર્ષે લગભગ 2,400 m³"), unit_no=5),
    num("u5n10", T("Benefit sharing under the Biological Diversity Act.",
                   "જૈવિક વિવિધતા અધિનિયમ હેઠળ લાભ વહેંચણી."),
        T("A company earns Rs 8 crore a year from a herbal formulation based on a village's knowledge. "
          "The NBA fixes benefit sharing at 5 % of the ex-factory sale price. Find the annual payment, "
          "the share of 12 villages in the register, and the payment if the rate were 2 %.",
          "એક કંપની ગામના જ્ઞાન પર આધારિત જડીબુટ્ટી બનાવમાંથી વર્ષે રૂ. 8 કરોડ કમાય છે. NBA લાભ વહેંચણી "
          "કારખાના વેચાણ ભાવના 5 % નક્કી કરે છે. વાર્ષિક ચુકવણી, રજિસ્ટરમાંના 12 ગામોનો હિસ્સો અને દર 2 % હોય તો "
          "ચુકવણી શોધો."),
        [P("Payment = 0.05 × 8 crore = Rs 40 lakh a year", "ચુકવણી = 0.05 × 8 કરોડ = વર્ષે રૂ. 40 લાખ"),
         P("Per village = 40 lakh / 12 = Rs 3.33 lakh a year", "પ્રતિ ગામ = 40 લાખ / 12 = વર્ષે રૂ. 3.33 લાખ"),
         P("At 2 % = Rs 16 lakh, and per village Rs 1.33 lakh",
           "2 % પર = રૂ. 16 લાખ, અને પ્રતિ ગામ રૂ. 1.33 લાખ"),
         P("The money goes to the Biodiversity Management Committee, which decides how it is used",
           "નાણું જૈવવિવિધતા વ્યવસ્થાપન સમિતિને જાય, જે તેનો ઉપયોગ નક્કી કરે")],
        T("Rs 40 lakh a year, Rs 3.33 lakh per village at 5 %",
          "વર્ષે રૂ. 40 લાખ, 5 % પર પ્રતિ ગામ રૂ. 3.33 લાખ"), unit_no=5),
]

EQUATIONS = [
    {"title": T("Water and rainwater", "પાણી અને વરસાદી જળ"),
     "items": [
         {"name": T("Harvestable rain", "એકઠું થઈ શકે તેવો વરસાદ"),
          "f": "V = A × rainfall (m) × runoff coefficient",
          "terms": T("The coefficient is 0.85 for a concrete roof, 0.75 for tiles and 0.5 for a lawn.",
                     "અવયવ કોંક્રિટ છત માટે 0.85, નળિયા માટે 0.75 અને ઘાસના મેદાન માટે 0.5 છે.")},
         {"name": T("Tank size", "ટાંકીનું માપ"), "f": "V_tank = daily demand × days of dry spell covered",
          "terms": T("Size on the longest rainless spell, not on the annual total.",
                     "વાર્ષિક કુલ પર નહીં, સૌથી લાંબા વરસાદ વગરના સમય પર માપો.")},
         {"name": T("Pollution load", "પ્રદૂષણ ભાર"), "f": "load (kg/day) = Q (m³/day) × C (mg/L) / 1,000",
          "terms": T("Compare the load with the load allowed by the consent, not only the concentration.",
                     "ફક્ત સાંદ્રતા નહીં, સંમતિએ મંજૂર કરેલા ભાર સાથે ભાર સરખાવો.")},
     ]},
    {"title": T("Energy, carbon and buildings", "ઊર્જા, કાર્બન અને ઇમારત"),
     "items": [
         {"name": T("Energy performance index", "ઊર્જા કાર્યદક્ષતા સૂચકાંક"),
          "f": "EPI = annual kWh / built-up area (m²)",
          "terms": T("Conventional Indian offices run at 200-250, a green one at 90-120.",
                     "સામાન્ય ભારતીય ઓફિસ 200-250, લીલી 90-120 ચાલે.")},
         {"name": T("CO₂ avoided by a plant", "સ્ટેશનથી બચતું CO₂"),
          "f": "m = E (MWh) × EF (t/MWh)",
          "terms": T("The Indian grid factor is about 0.71 t per MWh and coal about 0.9.",
                     "ભારતીય ગ્રિડ અવયવ પ્રતિ MWh લગભગ 0.71 t અને કોલસાનો લગભગ 0.9.")},
         {"name": T("Carbon credits", "કાર્બન ક્રેડિટ"), "f": "credits = tonnes CO₂ avoided, 1 credit = 1 t",
          "terms": T("Revenue = credits × price per tonne, after verification and additionality tests.",
                     "આવક = ક્રેડિટ × પ્રતિ ટન ભાવ, ચકાસણી અને અતિરિક્તતા કસોટી પછી.")},
         {"name": T("Significance of an aspect", "પાસાંનું મહત્ત્વ"),
          "f": "score = severity × probability × quantity",
          "terms": T("Each factor is scored 1 to 5; anything above the threshold gets a written control.",
                     "દરેક અવયવ 1 થી 5 અંક પામે; મર્યાદાથી ઉપરના દરેકને લેખિત નિયંત્રણ મળે.")},
     ]},
    {"title": T("Waste and tourism", "કચરો અને પર્યટન"),
     "items": [
         {"name": T("Waste per day", "દૈનિક કચરો"), "f": "W = population × per capita generation",
          "terms": T("Indian cities generate 0.3-0.6 kg per person a day.",
                     "ભારતીય શહેરો દિવસે પ્રતિ વ્યક્તિ 0.3-0.6 કિલો બનાવે.")},
         {"name": T("Compost yield", "ખાતર ઉત્પાદન"), "f": "compost = wet waste × 0.25",
          "terms": T("About a quarter of the wet mass remains after aerobic composting.",
                     "હવાયુક્ત ખાતર બનાવટ પછી ભીના દળનો લગભગ ચોથો ભાગ રહે.")},
         {"name": T("Carrying capacity", "વહન ક્ષમતા"),
          "f": "visitors/day = trail length × visitors per km per day",
          "terms": T("Fixing and enforcing the ceiling is what separates eco tourism from mass tourism.",
                     "મર્યાદા નક્કી કરી લાગુ કરવી એ જ પર્યાવરણ પર્યટનને સામૂહિક પર્યટનથી અલગ પાડે.")},
     ]},
]

VIVA = [
    {"title": T("Law and management systems", "કાયદો અને વ્યવસ્થાપન પ્રણાલી"),
     "items": [
         {"q": T("What is the difference between the Water Act and the Environment (Protection) Act?",
                 "જળ અધિનિયમ અને પર્યાવરણ (સંરક્ષણ) અધિનિયમ વચ્ચે શું ફરક છે?"),
          "a": T("The Water Act 1974 deals with one medium, water: it creates the pollution control "
                 "boards and requires consent to discharge. The Environment (Protection) Act 1986 is an "
                 "umbrella law that covers every medium and every pollutant, and gives the central "
                 "government power to set standards, restrict industries and frame rules - which is why "
                 "the EIA Notification and all the waste rules sit under it. The 1974 Act answered a "
                 "river problem; the 1986 Act answered Bhopal.",
                 "જળ અધિનિયમ 1974 એક જ માધ્યમ, પાણી સાથે વ્યવહાર કરે: તે પ્રદૂષણ નિયંત્રણ બોર્ડ બનાવે અને છોડવાની "
                 "સંમતિ માંગે. પર્યાવરણ (સંરક્ષણ) અધિનિયમ 1986 છત્રી કાયદો છે જે દરેક માધ્યમ અને દરેક પ્રદૂષકને "
                 "આવરે, અને કેન્દ્ર સરકારને ધોરણ, ઉદ્યોગ પર મર્યાદા અને નિયમ બનાવવાની સત્તા આપે - તેથી જ EIA "
                 "જાહેરનામું અને બધા કચરા નિયમો તેની નીચે છે. 1974નો અધિનિયમ નદીની સમસ્યાનો જવાબ હતો; 1986નો "
                 "ભોપાલનો.")},
         {"q": T("What is consent to establish and consent to operate?",
                 "સ્થાપના સંમતિ અને સંચાલન સંમતિ શું છે?"),
          "a": T("Two permissions from the State Pollution Control Board. Consent to establish is taken "
                 "before construction and checks that the site, the process and the planned pollution "
                 "control are acceptable. Consent to operate is taken before production starts and "
                 "states the permitted quantity and quality of effluent and emission, the monitoring and "
                 "the conditions. Both are time-bound and renewable, and operating beyond the conditions "
                 "or after expiry is an offence under the Water and Air Acts.",
                 "રાજ્ય પ્રદૂષણ નિયંત્રણ બોર્ડની બે પરવાનગી. સ્થાપના સંમતિ બાંધકામ પહેલાં લેવાય અને સ્થળ, "
                 "પ્રક્રિયા તથા યોજાયેલું પ્રદૂષણ નિયંત્રણ સ્વીકાર્ય છે કે નહીં તે તપાસે. સંચાલન સંમતિ ઉત્પાદન "
                 "શરૂ કરતાં પહેલાં લેવાય અને મંજૂર પ્રવાહ તથા ઉત્સર્જનનું પ્રમાણ અને ગુણવત્તા, દેખરેખ અને શરતો "
                 "જણાવે. બંને સમયબદ્ધ અને નવીકરણપાત્ર છે, અને શરતોથી બહાર કે મુદત પછી ચલાવવું જળ અને વાયુ "
                 "અધિનિયમો હેઠળ ગુનો છે.")},
         {"q": T("Which projects need environmental clearance, and what does it contain?",
                 "કયા પ્રોજેક્ટને પર્યાવરણીય મંજૂરી જોઈએ અને તેમાં શું હોય?"),
          "a": T("Under the EIA Notification 2006, projects are listed in a schedule and placed in "
                 "category A (central appraisal) or B (state appraisal) by size and type: mining, thermal "
                 "power, cement, chemicals, ports, highways, airports, large buildings and water "
                 "projects. The clearance contains the environmental management plan, the conditions - "
                 "green belt, effluent treatment, air quality monitoring, a six-monthly compliance "
                 "report - and the period of validity. It can be amended, suspended or revoked.",
                 "EIA જાહેરનામું 2006 હેઠળ પ્રોજેક્ટ અનુસૂચિમાં હોય અને કદ તથા પ્રકાર પ્રમાણે A શ્રેણી (કેન્દ્રીય "
                 "આકલન) કે B શ્રેણી (રાજ્ય આકલન)માં આવે: ખાણ, થર્મલ વીજ, સિમેન્ટ, રસાયણ, બંદર, ધોરીમાર્ગ, "
                 "વિમાનમથક, મોટી ઇમારત અને પાણીના પ્રોજેક્ટ. મંજૂરીમાં પર્યાવરણીય વ્યવસ્થાપન યોજના, શરતો - લીલો "
                 "પટ્ટો, પ્રવાહ સારવાર, હવાની ગુણવત્તાની દેખરેખ, દર છ મહિને અનુપાલન અહેવાલ - અને માન્યતા સમય "
                 "હોય. તે સુધારી, સ્થગિત કે રદ કરી શકાય.")},
         {"q": T("What does ISO 14001 actually require?",
                 "ISO 14001 ખરેખર શું માંગે છે?"),
          "a": T("A documented environmental management system built on plan-do-check-act: a scope and "
                 "policy, a register of environmental aspects and impacts with the significant ones "
                 "identified, a register of legal and other requirements, objectives with targets and "
                 "programmes, defined roles and training, documented operational control and emergency "
                 "preparedness, monitoring and measurement, internal audit, management review and "
                 "corrective action. There is no absolute performance standard - a certified plant is "
                 "not automatically clean, it has a system that keeps improving.",
                 "આયોજન-અમલ-તપાસ-સુધારો પર બનેલી લેખિત પર્યાવરણીય વ્યવસ્થાપન પ્રણાલી: વ્યાપ અને નીતિ, "
                 "પર્યાવરણીય પાસાં અને અસરોનું રજિસ્ટર જેમાં મહત્ત્વનાં ઓળખાય, કાનૂની અને બીજી ફરજોનું રજિસ્ટર, "
                 "લક્ષ્ય સાથેના ઉદ્દેશ અને કાર્યક્રમ, નક્કી કરેલી ભૂમિકા અને તાલીમ, લેખિત સંચાલન નિયંત્રણ અને "
                 "આપાતકાલીન તૈયારી, દેખરેખ અને માપન, આંતરિક તપાસ, વ્યવસ્થાપન સમીક્ષા અને સુધારાત્મક કાર્ય. કોઈ "
                 "નિરપેક્ષ કાર્યદક્ષતા ધોરણ નથી - પ્રમાણિત કારખાનું આપોઆપ સ્વચ્છ નથી, તેની પાસે સતત સુધરતી "
                 "પ્રણાલી છે.")},
     ]},
    {"title": T("Green practice, 5R and tourism", "લીલી પદ્ધતિ, 5R અને પર્યટન"),
     "items": [
         {"q": T("What is cradle to cradle and how is it different from recycling?",
                 "ક્રેડલ ટુ ક્રેડલ શું છે અને રિસાયકલથી કેવી રીતે જુદું છે?"),
          "a": T("Recycling breaks a product down, often into a lower grade, and is done after the "
                 "product becomes waste. Cradle to cradle designs the product from the start so that it "
                 "has no waste: every material is either a biological nutrient that safely returns to "
                 "the soil or a technical nutrient that returns to industry at the same quality, and the "
                 "product is assembled so that it can be taken apart. It also asks that the energy and "
                 "water used are renewable and clean, and that the whole supply chain is designed "
                 "around that loop.",
                 "રિસાયકલ ઉત્પાદનને તોડે છે, ઘણી વાર નીચી કક્ષામાં, અને તે ઉત્પાદન કચરો બન્યા પછી થાય. "
                 "ક્રેડલ ટુ ક્રેડલ ઉત્પાદનને શરૂઆતથી એવી રીતે રચે કે તેમાં કચરો જ ન હોય: દરેક સામગ્રી કાં તો "
                 "જૈવિક પોષક છે જે સુરક્ષિત રીતે જમીનમાં પાછું જાય, કાં તો ટેકનિકલ પોષક જે એ જ ગુણવત્તાએ ઉદ્યોગમાં "
                 "પાછું જાય, અને ઉત્પાદન એવી રીતે જોડાય કે તે છૂટું થઈ શકે. તે એ પણ માંગે કે વપરાતી ઊર્જા અને "
                 "પાણી પુનઃપ્રાપ્ય તથા સ્વચ્છ હોય, અને આખી પુરવઠા શૃંખલા તે ચક્ર પર રચાય.")},
         {"q": T("What are the four steps of a life cycle analysis?",
                 "જીવનચક્ર આકલનનાં ચાર પગલાં કયાં છે?"),
          "a": T("Goal and scope definition - what is compared, the functional unit and where the "
                 "boundary is drawn, cradle to gate or cradle to grave. Inventory analysis - the energy, "
                 "water, raw material, emission and waste per functional unit, collected from the "
                 "process. Impact assessment - the inventory translated into categories such as global "
                 "warming, acidification, eutrophication, water scarcity and toxicity, using "
                 "characterisation factors. Interpretation - the significant findings, the sensitivity "
                 "and the recommendation, with the assumption that would change the answer stated "
                 "openly.",
                 "ધ્યેય અને વ્યાપની વ્યાખ્યા - શું સરખાય છે, કાર્યાત્મક એકમ શું અને સીમા ક્યાં છે, ક્રેડલ ટુ "
                 "ગેટ કે ક્રેડલ ટુ ગ્રેવ. યાદી વિશ્લેષણ - કાર્યાત્મક એકમ દીઠ ઊર્જા, પાણી, કાચો માલ, ઉત્સર્જન અને "
                 "કચરો, પ્રક્રિયામાંથી એકઠા કરેલા. અસર આકલન - યાદીને વૈશ્વિક ગરમી, અમ્લતા, પોષકતત્ત્વ વૃદ્ધિ, "
                 "પાણીની તંગી અને ઝેર જેવી શ્રેણીઓમાં ગુણધર્મ અવયવ વાપરીને ફેરવવી. અર્થઘટન - મહત્ત્વનાં તારણો, "
                 "સંવેદનશીલતા અને સૂચન, અને જે ધારણા જવાબ બદલી શકે તે ખુલ્લેઆમ જણાવવી.")},
         {"q": T("What are the advantages and disadvantages of carbon credits?",
                 "કાર્બન ક્રેડિટના લાભ અને ખામી શું છે?"),
          "a": T("Advantages: they move money from high-emitting buyers to low-cost clean projects, so "
                 "the cheapest abatement happens first; they create a revenue stream for a project that "
                 "a local tariff cannot fully fund; and they put a price on carbon without a tax. "
                 "Disadvantages: additionality is hard to prove, so a credit may pay for something that "
                 "would have happened anyway; a rich buyer can use a cheap credit to avoid cutting its "
                 "own emissions; verification costs money; credits can be double counted between two "
                 "registries; and a project that is destroyed by fire or flood leaves the promised "
                 "reduction unearned.",
                 "લાભ: નાણું વધુ છોડતા ખરીદનાર પાસેથી ઓછા ખર્ચવાળા સ્વચ્છ પ્રોજેક્ટ તરફ ખસે, તેથી સૌથી સસ્તો "
                 "ઘટાડો પહેલાં થાય; સ્થાનિક ટેરિફ પૂરો ભંડોળ ન કરી શકે તેવા પ્રોજેક્ટને આવક મળે; અને કર વગર "
                 "કાર્બનને ભાવ મળે. ખામી: અતિરિક્તતા પુરવાર કરવી કઠિન છે, તેથી ક્રેડિટ કોઈ પણ રીતે થાત તેવા કામ "
                 "માટે ચૂકવાઈ શકે; શ્રીમંત ખરીદનાર સસ્તી ક્રેડિટ વાપરીને પોતાનું ઉત્સર્જન ઘટાડવાનું ટાળી શકે; "
                 "ચકાસણી પૈસા માંગે; બે રજિસ્ટર વચ્ચે ક્રેડિટ બે વાર ગણાઈ શકે; અને આગ કે પૂરથી નષ્ટ થયેલો પ્રોજેક્ટ "
                 "વચન આપેલો ઘટાડો અધૂરો છોડે.")},
         {"q": T("Explain the 5R with one example each.",
                 "દરેકના એક ઉદાહરણ સાથે 5R સમજાવો."),
          "a": T("Refuse: carry a cloth bag so the shop's plastic bag is never made. Reduce: a five-star "
                 "air conditioner or a bucket bath instead of a shower. Reuse: a steel water bottle "
                 "refilled for years. Repurpose: a tyre becomes a planter, an ice-cream tub becomes a "
                 "storage box. Recycle: newspaper, aluminium cans and PET bottles go to a recycler who "
                 "turns them back into material. The order is a preference order, because the rungs "
                 "above recycling need no energy, no transport and no market.",
                 "નકારો: કાપડની થેલી લઈ જાઓ જેથી દુકાનની પ્લાસ્ટિક થેલી બનેજ નહીં. ઘટાડો: પાંચ સ્ટાર "
                 "એરકન્ડીશનર કે ફુવારાને બદલે ડોલથી સ્નાન. ફરી વાપરો: પોલાદની પાણીની બોટલ વર્ષો સુધી ફરી ભરાય. "
                 "નવો ઉપયોગ: ટાયર કૂંડું બને, આઇસ્ક્રીમનું ડબ્બો સંગ્રહ પેટી બને. રિસાયકલ: છાપું, એલ્યુમિનિયમનાં "
                 "ડબ્બા અને PET બોટલ રિસાયકલરને જાય જે તેમને ફરી સામગ્રી બનાવે. ક્રમ પસંદગીનો ક્રમ છે, કારણ કે "
                 "રિસાયકલની ઉપરનાં પગથિયાંને ઊર્જા, વહન કે બજાર જોઈએ નહીં.")},
         {"q": T("What is carrying capacity in eco tourism?",
                 "પર્યાવરણ પર્યટનમાં વહન ક્ષમતા શું છે?"),
          "a": T("The number of visitors a place can absorb per day or per season without damaging what "
                 "they came to see - the trail, the nesting beach, the coral, the water supply and the "
                 "local community. It is found by study, not by guess: vegetation loss on the trail, "
                 "animal flight distance, sewage load, parking and noise. Once the number is set it must "
                 "be enforced with permits, timed entry, a closed day each week and a fee that rises in "
                 "the peak, because a capacity that exists only on paper is not a capacity.",
                 "પ્રવાસીઓ જે જોવા આવ્યા તેને - પગપાળા માર્ગ, ઇંડા મૂકતો દરિયાકિનારો, ભરતી, પાણી પુરવઠો અને "
                 "સ્થાનિક સમુદાય - નુકસાન પહોંચાડ્યા વગર જગ્યા રોજ કે ઋતુ દીઠ કેટલા પ્રવાસી સહી શકે તે સંખ્યા. તે "
                 "અભ્યાસથી મળે, અનુમાનથી નહીં: માર્ગ પર વનસ્પતિનું નુકસાન, પ્રાણીનું ભાગી જવાનું અંતર, ગટરનો ભાર, "
                 "પાર્કિંગ અને ઘોંઘાટ. સંખ્યા નક્કી થાય પછી પરવાનગી, સમયબદ્ધ પ્રવેશ, અઠવાડિયે એક બંધ દિવસ અને "
                 "ટોચની ઋતુમાં વધતી ફી દ્વારા લાગુ કરવી પડે, કારણ કે ફક્ત કાગળ પરની ક્ષમતા ક્ષમતા નથી.")},
         {"q": T("Why is a green building not just a building with solar panels?",
                 "લીલી ઇમારત ફક્ત સૌર પેનલવાળી ઇમારત કેમ નથી?"),
          "a": T("Because most of the saving comes before any equipment is bought. Orientation, shading, "
                 "insulation, glazing, a cool roof and natural ventilation reduce the cooling load, and "
                 "an efficient chiller, LED lighting and controls reduce what is left; a solar array "
                 "sized to a badly designed building must be two or three times larger for the same "
                 "comfort. A rated building also cuts water use, uses low-carbon material, manages "
                 "construction waste, and provides daylight and fresh air for the occupants, which is "
                 "measured in productivity as well as in units.",
                 "કારણ કે મોટાભાગની બચત કોઈ પણ સાધન ખરીદતાં પહેલાં આવે. દિશા, છાયો, ઇન્સ્યુલેશન, કાચ, ઠંડી છત "
                 "અને કુદરતી હવાડો ઠંડકનો ભાર ઘટાડે, અને કાર્યક્ષમ ચિલર, LED લાઇટ તથા નિયંત્રણ બાકીનું ઘટાડે; "
                 "ખરાબ રચાયેલી ઇમારત માટે માપેલી સૌર એરે એ જ આરામ માટે બે-ત્રણ ગણી મોટી જોઈએ. રેટેડ ઇમારત પાણીનો "
                 "વપરાશ પણ ઘટાડે, ઓછા કાર્બનવાળી સામગ્રી વાપરે, બાંધકામનો કચરો સંભાળે, અને રહેવાસીઓને દિવસનો "
                 "પ્રકાશ તથા તાજી હવા આપે, જે યુનિટ ઉપરાંત ઉત્પાદકતામાં પણ માપાય.")},
         {"q": T("What is a green label and why does it matter to a buyer?",
                 "લીલું લેબલ શું છે અને ખરીદનાર માટે તે કેમ મહત્ત્વનું છે?"),
          "a": T("A green label is a mark awarded by a third party to a product or building that meets a "
                 "published environmental criterion, such as energy use, water use, recycled content, "
                 "emissions or recyclability. It matters because it turns a claim into verified "
                 "information: a buyer cannot measure the embodied carbon of a paint tin or the power "
                 "draw of a refrigerator, but an auditor can. It also rewards the manufacturer who "
                 "spends money on the improvement, and it is only as good as the audit behind it - a "
                 "label with no surveillance is advertising.",
                 "લીલું લેબલ ત્રીજા પક્ષે પ્રકાશિત પર્યાવરણીય માપદંડ - જેમ કે ઊર્જા વપરાશ, પાણી વપરાશ, "
                 "રિસાયકલ સામગ્રી, ઉત્સર્જન કે રિસાયકલ થઈ શકે તેવાપણું - પૂરો કરતા ઉત્પાદન કે ઇમારતને આપેલું "
                 "ચિહ્ન છે. તે મહત્ત્વનું છે કારણ કે દાવાને ચકાસાયેલી માહિતીમાં ફેરવે: ખરીદનાર રંગની ટિનનો સન્નિહિત "
                 "કાર્બન કે ફ્રિજનો વીજ વપરાશ માપી ન શકે, પણ તપાસકર્તા માપી શકે. તે સુધારા પર પૈસો ખર્ચતા ઉત્પાદકને "
                 "બક્ષીશ પણ આપે, અને તે પાછળની તપાસ જેટલું જ સારું છે - દેખરેખ વગરનું લેબલ જાહેરાત છે.")},
     ]},
]

_PRACTICE = [
    (T("Explain the main environmental laws of India and the instrument each one uses.",
       "ભારતના મુખ્ય પર્યાવરણીય કાયદા અને દરેક વાપરતું સાધન સમજાવો."), 5,
     [P("Water Act 1974: created the CPCB and SPCBs and made consent to establish and consent to "
        "operate compulsory for any discharge; the instrument is a time-bound permission with effluent "
        "standards. Air Act 1981: extended the same board machinery to air, allowed air pollution "
        "control areas and set emission standards for chimneys and vehicles.",
        "જળ અધિનિયમ 1974: CPCB અને SPCB બનાવ્યા અને કોઈ પણ પ્રવાહ માટે સ્થાપના તથા સંચાલન સંમતિ ફરજિયાત કરી; "
        "સાધન સમયબદ્ધ પરવાનગી છે જેમાં પ્રવાહના ધોરણ હોય. વાયુ અધિનિયમ 1981: એ જ બોર્ડ મશીનરી હવા સુધી "
        "લંબાવી, વાયુ પ્રદૂષણ નિયંત્રણ વિસ્તારની મંજૂરી આપી અને ચીમની તથા વાહનો માટે ઉત્સર્જન ધોરણ નક્કી કર્યા."),
      P("Environment (Protection) Act 1986: the umbrella that followed Bhopal, covering every pollutant "
        "in every medium, and the parent of the EIA Notification and the waste rules; its instrument is "
        "a rule-making and standard-setting power plus closure directions. Wild Life (Protection) Act "
        "1972 protects scheduled species and creates national parks and sanctuaries; Forest "
        "(Conservation) Act 1980 requires central approval before any forest land is diverted.",
        "પર્યાવરણ (સંરક્ષણ) અધિનિયમ 1986: ભોપાલ પછીનો છત્રી કાયદો, દરેક માધ્યમમાં દરેક પ્રદૂષકને આવરે, અને EIA "
        "જાહેરનામા તથા કચરા નિયમોનો પિતા; તેનું સાધન નિયમ અને ધોરણ બનાવવાની સત્તા તથા બંધ કરવાની સૂચના છે. "
        "વન્યજીવ (સંરક્ષણ) અધિનિયમ 1972 અનુસૂચિત જાતિઓ બચાવે અને રાષ્ટ્રીય ઉદ્યાન તથા અભયારણ્ય બનાવે; વન "
        "(સંરક્ષણ) અધિનિયમ 1980 વન જમીન ફેરવતાં પહેલાં કેન્દ્રીય મંજૂરી માંગે."),
      P("Biological Diversity Act 2002: three-tier governance (NBA, state board, local committee) with "
        "access and benefit sharing for bio-resources and traditional knowledge. Add the courts: the "
        "National Green Tribunal, 2010, hears environment cases with a six-month target and can award "
        "compensation and restitution. The principles behind all of them are precaution, polluter pays, "
        "sustainable development and public trust.",
        "જૈવિક વિવિધતા અધિનિયમ 2002: ત્રિસ્તરીય શાસન (NBA, રાજ્ય બોર્ડ, સ્થાનિક સમિતિ) સાથે જૈવ-સ્રોત અને "
        "પરંપરાગત જ્ઞાન માટે પ્રવેશ અને લાભ વહેંચણી. અદાલતો ઉમેરો: રાષ્ટ્રીય લીલું ટ્રિબ્યુનલ, 2010, પર્યાવરણના "
        "કેસ છ મહિનાના લક્ષ્યે સાંભળે અને વળતર તથા પુનઃસ્થાપન આપી શકે. બધા પાછળના સિદ્ધાંતો સાવચેતી, પ્રદૂષક ચૂકવે, "
        "ટકાઉ વિકાસ અને જાહેર ભરોસો છે.")]),
    (T("Describe ISO 14001 with its PDCA cycle and list the benefits of certification.",
       "ISO 14001 તેના PDCA ચક્ર સાથે વર્ણવો અને પ્રમાણીકરણના લાભ ગણાવો."), 5,
     [P("Plan: define the scope and policy, identify environmental aspects and impacts, score them for "
        "significance, list the legal and other requirements, and set objectives, targets and "
        "programmes. Do: assign roles and training, write operational controls for the significant "
        "aspects, prepare for emergencies and keep records. Check: monitor and measure the key "
        "parameters, calibrate instruments, audit internally and record non-conformities. Act: correct "
        "the root cause, update the risk assessment and feed the result into the next plan.",
        "આયોજન: વ્યાપ અને નીતિ નક્કી કરો, પર્યાવરણીય પાસાં અને અસરો ઓળખો, તેમને મહત્ત્વ માટે અંક આપો, કાનૂની "
        "તથા બીજી ફરજોની યાદી બનાવો, અને ઉદ્દેશ, લક્ષ્ય તથા કાર્યક્રમ નક્કી કરો. અમલ: ભૂમિકા અને તાલીમ સોંપો, "
        "મહત્ત્વનાં પાસાં માટે સંચાલન નિયંત્રણ લખો, આપાતકાલ માટે તૈયારી કરો અને નોંધ રાખો. તપાસ: મુખ્ય માપદંડોની "
        "દેખરેખ અને માપન કરો, સાધનો કેલિબ્રેટ કરો, આંતરિક તપાસ કરો અને બિન-અનુરૂપતા નોંધો. સુધારો: મૂળ કારણ સુધારો, "
        "જોખમ આકલન સુધારો અને પરિણામ આગલા આયોજનમાં ઉમેરો."),
      P("The written procedure for a significant aspect is the heart of the system: the plating shop "
        "writes how an acid bath is filled, used, drained, stored and inspected, who may do it, what "
        "happens if it spills, and how the records prove it. That is why an audit can test the system - "
        "it looks for the document, the training record and the monitoring data, and asks the operator "
        "to explain the procedure.",
        "મહત્ત્વના પાસાં માટેની લેખિત પ્રક્રિયા પ્રણાલીનું હૃદય છે: પ્લેટિંગ કારખાનું લખે કે એસિડ સ્નાન કેવી રીતે "
        "ભરાય, વપરાય, ખાલી થાય, સંગ્રહાય અને તપાસાય, કોણ કરી શકે, ગળે તો શું થાય, અને નોંધ કેવી રીતે પુરાવો આપે. "
        "તેથી જ તપાસ પ્રણાલી કસી શકે - તે દસ્તાવેજ, તાલીમ નોંધ અને દેખરેખ માહિતી શોધે, અને ઓપરેટરને પ્રક્રિયા "
        "સમજાવવા કહે."),
      P("Benefits: legal compliance becomes a checked register instead of a hope; energy, water and "
        "material waste fall because they are the aspects being watched; export customers, banks and "
        "insurers accept the certificate as evidence; and the workforce is trained to notice a leak "
        "before it becomes a fine. The limitation is that ISO 14001 certifies the system, not the "
        "performance - a certified plant can still be a heavy polluter if its objectives are weak.",
        "લાભ: કાનૂની અનુપાલન આશાને બદલે તપાસાયેલું રજિસ્ટર બને; ઊર્જા, પાણી અને સામગ્રીનો વ્યય ઘટે કારણ કે તે જ "
        "જોવાતાં પાસાં છે; નિકાસ ખરીદનાર, બેંક અને વીમા કંપની પ્રમાણપત્રને પુરાવા તરીકે સ્વીકારે; અને કર્મચારી "
        "ગળતર દંડ બનતાં પહેલાં જોવા તાલીમ પામે. મર્યાદા એ છે કે ISO 14001 પ્રણાલીનું પ્રમાણીકરણ કરે, કાર્યદક્ષતાનું "
        "નહીં - ઉદ્દેશ નબળા હોય તો પ્રમાણિત કારખાનું હજી ભારે પ્રદૂષક રહી શકે.")]),
    (T("Design a rain water harvesting system for a school and calculate what it saves.",
       "શાળા માટે વરસાદી જળ સંગ્રહ પ્રણાલી રચો અને તે કેટલું બચાવે તે ગણો."), 5,
     [P("Catchment: the 800 m² terrace, sloping to four downpipes. Conveyance: 110 mm PVC gutters with "
        "a mesh strainer at each outlet, and a first-flush diverter that throws away the first 2 mm of "
        "rain, which carries most of the dust and bird droppings. Filtration: a sand and gravel filter "
        "with a charcoal layer. Storage: a 40 m³ underground tank of RCC with a mosquito-proof cover. "
        "Recharge: an overflow pipe to a 3 m × 3 m recharge pit filled with boulders, gravel and sand, "
        "so that surplus goes into the aquifer instead of the drain.",
        "ગ્રાહક સપાટી: 800 m² ટેરેસ, ચાર ઉતરતી નળીઓ તરફ ઢળતી. વહન: દરેક મુખ પર જાળીવાળા 110 mm PVC ગટર, અને "
        "પ્રથમ-વહાવ વાળક જે પ્રથમ 2 mm વરસાદ ફેંકે, જેમાં મોટાભાગની ધૂળ અને પક્ષીના મળ હોય. ગાળણ: કોલસાના સ્તર "
        "સાથે રેતી-કાંકરાનું ગાળક. સંગ્રહ: મચ્છર-રક્ષી ઢાંકણવાળી 40 m³ ભૂગર્ભ ટાંકી. ભરાવો: 3 m × 3 m ભરાવ "
        "ખાડા તરફ વહાવ પાઇપ, જે પથ્થર, કાંકરા અને રેતીથી ભરેલો, જેથી વધારાનું પાણી ગટરને બદલે જળાશયમાં જાય."),
      P("Calculation: 800 m² at 1,000 mm of rain with a coefficient of 0.85 gives "
        "800 × 1.0 × 0.85 = 680 m³ a year, which is 6,80,000 litres. The school needs 2,000 L a day for "
        "drinking, washing and toilets, so the harvest covers 340 days - nearly the whole academic year. "
        "At Rs 60 per m³ of tanker water that is Rs 40,800 a year, and the recharge pit also lifts the "
        "borewell, so the pump runs for fewer hours.",
        "ગણતરી: 1,000 mm વરસાદમાં 800 m² અને 0.85 અવયવ 800 × 1.0 × 0.85 = 680 m³ વર્ષે, એટલે 6,80,000 લિટર "
        "આપે. શાળાને પીવા, ધોવા અને શૌચાલય માટે દિવસે 2,000 લિટર જોઈએ, તેથી સંગ્રહ 340 દિવસ પૂરે - લગભગ આખું "
        "શૈક્ષણિક વર્ષ. પ્રતિ m³ ટેન્કર પાણીના રૂ. 60 પ્રમાણે તે વર્ષે રૂ. 40,800, અને ભરાવ ખાડો બોરવેલ પણ ઊંચું "
        "કરે, તેથી પંપ ઓછા કલાક ચાલે."),
      P("Cost and upkeep: about Rs 4-5 lakh for the tank and pit, so the payback is eight to ten years "
        "on water alone, and faster once the flooding of the playground and the pump hours are counted. "
        "Maintenance is the part that decides whether it works: clean the strainer before the monsoon, "
        "remove the first-flush water, desilt the tank every year and keep the pit free of leaves.",
        "ખર્ચ અને જાળવણી: ટાંકી અને ખાડા માટે લગભગ રૂ. 4-5 લાખ, તેથી ફક્ત પાણી પર પરતફેળો આઠથી દસ વર્ષ, અને "
        "રમતના મેદાનમાં પૂર તથા પંપના કલાક ગણીએ તો વધુ ઝડપી. જાળવણી જ નક્કી કરે કે તે ચાલશે કે નહીં: ચોમાસા પહેલાં "
        "જાળી સાફ કરો, પ્રથમ-વહાવ પાણી કાઢો, દર વર્ષે ટાંકીનો કાંપ કાઢો અને ખાડો પાંદડાંથી મુક્ત રાખો.")]),
    (T("Compare GRIHA, IGBC and LEED and explain what a rating measures.",
       "GRIHA, IGBC અને LEEDની સરખામણી કરો અને રેટિંગ શું માપે તે સમજાવો."), 4,
     [P("GRIHA is India's own system, developed by TERI with MNRE, and awards one to five stars. It is "
        "built on the Indian climate, the National Building Code and the Energy Conservation Building "
        "Code, and it gives heavy weight to passive design - orientation, shading, daylight, "
        "ventilation - and to reducing the life-cycle cost of the building, with points for soil and "
        "water conservation.",
        "GRIHA ભારતની પોતાની પ્રણાલી છે, TERI દ્વારા MNRE સાથે વિકસાવેલી, અને એકથી પાંચ સ્ટાર આપે. તે ભારતીય "
        "હવામાન, રાષ્ટ્રીય ઇમારત નિયમાવલી અને ઊર્જા સંરક્ષણ ઇમારત નિયમાવલી પર બનેલી છે, અને નિષ્ક્રિય ડિઝાઇન - "
        "દિશા, છાયો, દિવસનો પ્રકાશ, હવાડો - તથા ઇમારતનો જીવનચક્ર ખર્ચ ઘટાડવા પર ભાર મૂકે, જમીન અને પાણી સંરક્ષણને "
        "પોઇન્ટ આપે."),
      P("IGBC, run by the Confederation of Indian Industry, is the most widely used in India and has "
        "separate rating tools for homes, offices, factories, schools, townships and existing "
        "buildings; it awards certified, silver, gold and platinum. LEED, from the US Green Building "
        "Council, is international and is often required by global tenants and investors; it scores "
        "energy, water, materials, indoor quality, location and innovation out of 110 points.",
        "IGBC, ભારતીય ઉદ્યોગ પરિષદ દ્વારા ચાલતી, ભારતમાં સૌથી વધુ વપરાય છે અને ઘર, ઓફિસ, કારખાનું, શાળા, "
        "ટાઉનશિપ અને જૂની ઇમારતો માટે અલગ રેટિંગ સાધનો ધરાવે; તે પ્રમાણિત, સિલ્વર, ગોલ્ડ અને પ્લેટિનમ આપે. LEED, "
        "અમેરિકન લીલી ઇમારત પરિષદની, આંતરરાષ્ટ્રીય છે અને વૈશ્વિક ભાડુઆત તથા રોકાણકાર માંગે છે; તે 110માંથી ઊર્જા, "
        "પાણી, સામગ્રી, અંદરની ગુણવત્તા, સ્થાન અને નવીનતાને અંક આપે."),
      P("A rating measures design intent and modelled performance against a checklist, verified by "
        "documents and sometimes by an audit. It does not measure how the building is actually run, "
        "which is why a rated building can underperform if the operators leave the chillers on and the "
        "sensors off. The honest comparison is the measured energy performance index and the water "
        "consumption per person over a full year.",
        "રેટિંગ ચેકલિસ્ટ સામે ડિઝાઇનનો ઇરાદો અને નમૂનિત કાર્યદક્ષતા માપે, જે દસ્તાવેજોથી અને કેટલીક વાર તપાસથી "
        "ચકાસાય. તે માપતું નથી કે ઇમારત ખરેખર કેવી ચાલે છે, તેથી ઓપરેટર ચિલર ચાલુ અને સેન્સર બંધ રાખે તો રેટેડ "
        "ઇમારત પણ નબળી પડે. પ્રામાણિક સરખામણી આખા વર્ષનો માપેલો ઊર્જા કાર્યદક્ષતા સૂચકાંક અને વ્યક્તિ દીઠ પાણી "
        "વપરાશ છે.")]),
    (T("Explain cradle to cradle, life cycle analysis and a green label with one example each.",
       "ક્રેડલ ટુ ક્રેડલ, જીવનચક્ર આકલન અને લીલું લેબલ દરેકના એક ઉદાહરણ સાથે સમજાવો."), 5,
     [P("Cradle to cradle is a design philosophy: waste equals food. A PET bottle designed to be "
        "chemically recycled back into a food-grade bottle, or a cotton shirt with a removable button "
        "and a single-fibre label that can be shredded into new yarn, is cradle to cradle; the same "
        "bottle laminated to a foil sleeve is not, because the two materials cannot be separated.",
        "ક્રેડલ ટુ ક્રેડલ રચના દર્શન છે: કચરો એટલે ખોરાક. રાસાયણિક રીતે ફરી ખાદ્ય-દરજ્જાની બોટલ બનતી PET બોટલ, "
        "કે છૂટા થઈ શકતા બટન અને એક જ તંતુના લેબલવાળું કપાસનું શર્ટ જે ફરી ધાગો બને, તે ક્રેડલ ટુ ક્રેડલ છે; એ જ "
        "બોટલ ફોઇલના આવરણ સાથે લેમિનેટ કરેલી નહીં, કારણ કે બે સામગ્રી છૂટી ન થઈ શકે."),
      P("Life cycle analysis is the accounting behind the claim. For a cotton bag against a plastic bag "
        "the functional unit is 'carry 10 kg of shopping once'; the inventory counts the cotton, the "
        "dye, the water and energy for growing and sewing, the transport; the impact assessment turns "
        "that into water scarcity, global warming and eutrophication; and the interpretation may find "
        "that the cotton bag wins only if it is used more than fifty times, which is the number the "
        "buyer then has to act on.",
        "જીવનચક્ર આકલન દાવા પાછળનો હિસાબ છે. પ્લાસ્ટિક થેલી સામે કપાસની થેલી માટે કાર્યાત્મક એકમ 'એક વાર 10 કિલો "
        "સામાન ઉપાડવો' છે; યાદી કપાસ, રંગ, ઉગાડવા અને સીવવાનું પાણી તથા ઊર્જા, અને વહન ગણે; અસર આકલન તેને પાણીની "
        "તંગી, વૈશ્વિક ગરમી અને પોષકતત્ત્વ વૃદ્ધિમાં ફેરવે; અને અર્થઘટન કદાચ જણાવે કે કપાસની થેલી પચાસ વારથી વધુ "
        "વપરાય તો જ જીતે, જે સંખ્યા પર ખરીદનારે પછી કામ કરવાનું છે."),
      P("A green label is the summary a shopper can use: the BIS Eco Mark, the BEE star for an "
        "appliance, EPEAT for a laptop, FSC for timber, or a GRIHA star for a building. Its value "
        "depends on three things - a published criterion, an independent check and a surveillance "
        "audit - and without the last two the label is only a logo. The examiner wants the three linked: "
        "design, evidence, and the label the market can read.",
        "લીલું લેબલ એ ખરીદનાર વાપરી શકે તેવો સારાંશ છે: BIS ઇકો માર્ક, સાધન માટે BEE સ્ટાર, લેપટોપ માટે EPEAT, "
        "લાકડા માટે FSC, કે ઇમારત માટે GRIHA સ્ટાર. તેની કિંમત ત્રણ વસ્તુ પર છે - પ્રકાશિત માપદંડ, સ્વતંત્ર તપાસ "
        "અને દેખરેખ તપાસ - અને છેલ્લી બે વગર લેબલ ફક્ત લોગો છે. પરીક્ષકને ત્રણ જોડેલાં જોઈએ: રચના, પુરાવો અને "
        "બજાર વાંચી શકે તેવું લેબલ.")]),
    (T("Explain the carbon credit system with its advantages and disadvantages.",
       "કાર્બન ક્રેડિટ પ્રણાલી તેના લાભ અને ખામી સાથે સમજાવો."), 5,
     [P("Mechanism: a project that reduces, avoids or removes greenhouse gases beyond what the law "
        "requires is measured against a baseline. A verifier approved by a standard body - Gold "
        "Standard, Verra, or a government scheme - checks the measurement and issues one credit per "
        "tonne of CO₂ equivalent. The credit is sold to a buyer who needs it for compliance or for a "
        "voluntary net-zero claim, and retired so that it cannot be used twice.",
        "પ્રણિયંત્રણ: કાયદો માંગે તેનાથી વધુ હરિતગૃહ વાયુ ઘટાડતો, ટાળતો કે દૂર કરતો પ્રોજેક્ટ આધાર રેખા સામે "
        "માપાય. ધોરણ સંસ્થા - ગોલ્ડ સ્ટાન્ડર્ડ, વેરા કે સરકારી યોજના - માન્ય તપાસકર્તા માપન ચકાસે અને પ્રતિ ટન "
        "CO₂ સમમૂલ્યે એક ક્રેડિટ આપે. ક્રેડિટ અનુપાલન કે સ્વૈચ્છિક નેટ-ઝીરો દાવા માટે જરૂરી ખરીદનારને વેચાય, અને "
        "બે વાર ન વપરાય તેમ રદ થાય."),
      P("Advantages: it finds the cheapest reduction first, wherever it is, which is efficient for the "
        "atmosphere; it brings private money to cookstoves, biogas, wind and forest projects in "
        "countries that cannot subsidise them; it gives a developing country a route to finance without "
        "debt; and it creates a measurable unit that companies can report.",
        "લાભ: તે સૌથી સસ્તો ઘટાડો પહેલાં શોધે, જ્યાં પણ હોય, જે વાતાવરણ માટે કાર્યક્ષમ છે; તે ચૂલા, બાયોગેસ, પવન "
        "અને વન પ્રોજેક્ટમાં ખાનગી નાણું લાવે તેવા દેશોમાં જે સબસિડી આપી શકતા નથી; તે વિકાસશીલ દેશને દેવા વગર "
        "ભંડોળનો રસ્તો આપે; અને તે માપી શકાય તેવો એકમ બનાવે જે કંપની જાહેર કરી શકે."),
      P("Disadvantages: additionality, because a profitable wind farm may not need the credit at all; "
        "permanence, because a forest that burns releases the carbon back; leakage, because a project "
        "may push the damage somewhere else; double counting between registries; verification cost that "
        "small projects cannot bear; and the moral hazard that a buyer uses credits to avoid cutting "
        "its own emissions. The answer is not to abolish the mechanism but to use it last, with strong "
        "rules on additionality, permanence and retirement.",
        "ખામી: અતિરિક્તતા, કારણ કે નફાકારક પવન ફાર્મને ક્રેડિટની જરૂર જ ન હોય; ટકાઉપણું, કારણ કે બળેલું વન કાર્બન "
        "પાછું છોડે; લીકેજ, કારણ કે પ્રોજેક્ટ નુકસાન બીજે ધકેલે; રજિસ્ટર વચ્ચે બે વાર ગણતરી; નાના પ્રોજેક્ટ પરવડી ન "
        "શકે તેવો ચકાસણી ખર્ચ; અને નૈતિક જોખમ કે ખરીદનાર ક્રેડિટ વાપરી પોતાનું ઉત્સર્જન ઘટાડવાનું ટાળે. જવાબ "
        "પ્રણાલી નાબૂદ કરવો નહીં, પણ તેને છેલ્લે વાપરવી, અતિરિક્તતા, ટકાઉપણું અને રદ કરવા પર કડક નિયમો સાથે.")]),
    (T("A city council asks you to cut its waste. Prepare a 5R plan with numbers.",
       "એક નગર પરિષદ તમને તેનો કચરો ઘટાડવા કહે છે. આંકડા સાથે 5R યોજના બનાવો."), 5,
     [P("Baseline: the city generates 300 t a day for 6 lakh people, that is 0.5 kg per person, and "
        "spends Rs 1,800 per tonne on collection, transport and landfill, so about Rs 19.7 crore a year. "
        "Of the 300 t, roughly 55 % is wet, 30 % dry recyclable and 15 % inert or hazardous.",
        "આધાર રેખા: શહેર 6 લાખ લોકો માટે દિવસે 300 t કચરો બનાવે, એટલે પ્રતિ વ્યક્તિ 0.5 કિલો, અને ઉપાડ, વહન "
        "તથા લેન્ડફિલ પર ટન દીઠ રૂ. 1,800 ખર્ચે, એટલે વર્ષે લગભગ રૂ. 19.7 કરોડ. 300 tમાંથી લગભગ 55 % ભીનો, "
        "30 % સૂકો રિસાયકલ થઈ શકે તેવો અને 15 % નિષ્ક્રિય કે જોખમી છે."),
      P("Refuse and reduce: ban single-use plastic cutlery and carry bags, and promote cloth bags and "
        "refill stations; a 5 % reduction is 15 t a day. Reuse and repurpose: a repair cafe at every "
        "ward and a construction-material bank for used bricks, doors and tiles, which keeps the "
        "15 t a day of construction waste out of the bin.",
        "નકારો અને ઘટાડો: એક વાર વપરાતા પ્લાસ્ટિકના ચમચા અને થેલી પર પ્રતિબંધ, અને કાપડની થેલી તથા ફરી ભરવાના "
        "કેન્દ્રને પ્રોત્સાહન; 5 % ઘટાડો એટલે દિવસે 15 t. ફરી વાપરો અને નવો ઉપયોગ: દરેક વોર્ડમાં સમારકામ કેન્દ્ર અને "
        "વપરાયેલી ઈંટ, દરવાજા તથા ટાઇલ માટે બાંધકામ સામગ્રી બેંક, જે દિવસે 15 t બાંધકામ કચરો કચરાપેટીમાંથી બહાર રાખે."),
      P("Recycle and recover: two-bin segregation at source, 165 t of wet waste a day to five decentralised "
        "compost yards giving 41 t of compost, and 90 t of dry waste to a materials recovery facility "
        "that recovers about 60 t of paper, metal, glass and PET; only the 15 t of inert and hazardous "
        "waste goes to a sanitary landfill. The saving is about 250 t a day of transport, roughly "
        "Rs 16 crore a year, and the compost and recyclables earn another Rs 3-4 crore - the plan pays "
        "for itself in the first two years.",
        "રિસાયકલ અને પુનઃપ્રાપ્તિ: સ્રોત પર બે-ડબ્બા અલગીકરણ, દિવસે 165 t ભીનો કચરો પાંચ વિકેન્દ્રિત ખાતર "
        "યાર્ડને જે 41 t ખાતર આપે, અને 90 t સૂકો કચરો સામગ્રી પુનઃપ્રાપ્તિ કેન્દ્રને જે લગભગ 60 t કાગળ, ધાતુ, કાચ "
        "અને PET કાઢે; ફક્ત 15 t નિષ્ક્રિય તથા જોખમી કચરો સ્વચ્છ લેન્ડફિલમાં જાય. બચત દિવસે લગભગ 250 t વહન, એટલે "
        "વર્ષે લગભગ રૂ. 16 કરોડ, અને ખાતર તથા રિસાયકલ વસ્તુ વધુ રૂ. 3-4 કરોડ કમાય - યોજના પ્રથમ બે વર્ષમાં પોતાનો "
        "ખર્ચ કાઢે છે.")]),
    (T("Explain eco tourism with five advantages, five disadvantages and one way to regulate it.",
       "પાંચ લાભ, પાંચ ખામી અને નિયંત્રણની એક રીત સાથે પર્યાવરણ પર્યટન સમજાવો."), 5,
     [P("Definition and advantages: eco tourism is travel to a natural area that conserves it, "
        "benefits the local people and educates the visitor. Advantages - conservation becomes an "
        "income (a reef that pays for itself), local jobs in guiding, homestays and crafts, less "
        "migration, education that turns a visitor into an advocate, and low infrastructure cost "
        "compared with a theme park.",
        "વ્યાખ્યા અને લાભ: પર્યાવરણ પર્યટન એ કુદરતી વિસ્તારમાં મુસાફરી છે જે તેને સાચવે, સ્થાનિક લોકોને લાભ આપે "
        "અને પ્રવાસીને શીખવે. લાભ - સંરક્ષણ આવક બને (પોતાનો ખર્ચ કાઢતી ભરતી), ગાઇડ, હોમસ્ટે અને હસ્તકલામાં "
        "સ્થાનિક રોજગાર, ઓછું સ્થળાંતર, પ્રવાસીને હિમાયતી બનાવતું શિક્ષણ, અને થીમ પાર્ક સામે ઓછો માળખા ખર્ચ."),
      P("Disadvantages: greenwashing of ordinary mass tourism, exceeding the carrying capacity of a "
        "trail, beach or reef, disturbance of wildlife by noise and vehicles, leakage of revenue to "
        "enclave resorts so the community keeps little, and the plastic and sewage that a small village "
        "cannot manage. Each has a fix in design, but none fixes itself.",
        "ખામી: સામાન્ય સામૂહિક પર્યટનનું લીલું ધોવું, પગપાળા માર્ગ, દરિયાકિનારો કે ભરતીની વહન ક્ષમતા વટાવવી, "
        "ઘોંઘાટ અને વાહનથી વન્યજીવનમાં ખલેલ, બંધિયાર રિસોર્ટ તરફ આવકનું લીકેજ જેથી સમુદાય થોડું રાખે, અને નાનું "
        "ગામ સંભાળી ન શકે તેવું પ્લાસ્ટિક તથા ગટર. દરેકનો ઉકેલ રચનામાં છે, પણ કોઈ જાતે સુધરતું નથી."),
      P("One regulation that works: a scientifically set daily carrying capacity, enforced by timed "
        "entry permits sold by the village committee, with a closed day each week and a fee that is "
        "higher at the peak. The number is published, the gate is staffed by local people, and the "
        "revenue pays for the guides and the trail's own maintenance - the three tests of eco tourism "
        "in a single instrument.",
        "કામ કરતું એક નિયંત્રણ: વૈજ્ઞાનિક રીતે નક્કી કરેલી દૈનિક વહન ક્ષમતા, જે ગામ સમિતિ વેચતી સમયબદ્ધ પ્રવેશ "
        "પરવાનગીથી લાગુ પડે, અઠવાડિયે એક બંધ દિવસ અને ટોચની ઋતુમાં વધુ ફી સાથે. સંખ્યા જાહેર થાય, દરવાજે સ્થાનિક "
        "લોકો હોય, અને આવક ગાઇડ તથા માર્ગની જાળવણી ચૂકવે - એક જ સાધનમાં પર્યાવરણ પર્યટનની ત્રણ કસોટી.")]),
    (T("Explain the Biological Diversity Act 2002 with an example of benefit sharing.",
       "જૈવિક વિવિધતા અધિનિયમ 2002 લાભ વહેંચણીના ઉદાહરણ સાથે સમજાવો."), 4,
     [P("Purpose: India is one of the world's megadiverse countries and its knowledge of plants is "
        "traditional and undocumented, so a company could patent a remedy that a village had used for "
        "generations. The Act regulates access to biological resources, asks for prior approval, and "
        "makes benefit sharing a condition - money, technology, training or a share of the royalty.",
        "હેતુ: ભારત દુનિયાના અતિ-જૈવવિવિધતાવાળા દેશોમાં છે અને તેનું છોડનું જ્ઞાન પરંપરાગત તથા અલેખિત છે, તેથી કંપની "
        "ગામ દાખલાઓથી વાપરતા ઉપચારને સ્વત્વપેટંટ કરી શકે. અધિનિયમ જૈવિક સ્રોતમાં પ્રવેશનું નિયમન કરે, પહેલી મંજૂરી "
        "માંગે, અને લાભ વહેંચણી શરત બનાવે - નાણું, ટેક્નોલોજી, તાલીમ કે રોયલ્ટીનો હિસ્સો."),
      P("Structure: the NBA at Chennai for foreign access and intellectual property, a State "
        "Biodiversity Board for Indian commercial access, and a Biodiversity Management Committee in "
        "each local body that prepares the People's Biodiversity Register. The register is the practical "
        "weapon: an entry dated years before a patent application is evidence that the knowledge is "
        "prior art.",
        "રચના: વિદેશી પ્રવેશ અને બૌદ્ધિક સંપદા માટે ચેન્નાઈમાં NBA, ભારતીય વ્યાપારી પ્રવેશ માટે રાજ્ય જૈવવિવિધતા "
        "બોર્ડ, અને દરેક સ્થાનિક સંસ્થામાં જૈવવિવિધતા વ્યવસ્થાપન સમિતિ જે લોક જૈવવિવિધતા રજિસ્ટર તૈયાર કરે. રજિસ્ટર "
        "વ્યવહારનું હથિયાર છે: પેટંટ અરજી પહેલાં વર્ષોની નોંધ એ પુરાવો છે કે જ્ઞાન પહેલેથી અસ્તિત્વમાં છે."),
      P("Example: a company earns Rs 8 crore a year from a herbal formulation, so a 5 % benefit share "
        "is Rs 40 lakh a year; twelve villages in the register divide it as Rs 3.33 lakh each, and the "
        "committee decides whether to spend it on a water tank, a school bus or a seed bank. The money "
        "is small, but it changes the politics: the forest is now an asset that the village is paid to "
        "protect.",
        "ઉદાહરણ: કંપની જડીબુટ્ટી બનાવમાંથી વર્ષે રૂ. 8 કરોડ કમાય, તેથી 5 % લાભ હિસ્સો વર્ષે રૂ. 40 લાખ; રજિસ્ટરમાંના "
        "બાર ગામ દરેકને રૂ. 3.33 લાખ વહેંચે, અને સમિતિ નક્કી કરે કે પાણીની ટાંકી, શાળા બસ કે બીજ બેંક પર ખર્ચવું. "
        "નાણું નાનું છે, પણ રાજકારણ બદલે: વન હવે એવી સંપત્તિ છે જેને બચાવવા ગામને ચૂકવાય છે.")]),
    (T("How would you verify that a campus is really sustainable and not only painted green?",
       "કેમ્પસ ખરેખર ટકાઉ છે કે ફક્ત લીલું રંગાયું છે તે કેવી રીતે ચકાસશો?"), 5,
     [P("Measure, do not believe the brochure. Take the electricity bill for twelve months and divide "
        "by the built-up area to get the energy performance index; take the water bill or the borewell "
        "meter reading and divide by the number of users; weigh the waste leaving the gate for a week "
        "and check how much is segregated. Put the four numbers on a board next to the green flag.",
        "માનો નહીં, માપો - બ્રોશર પર ભરોસો ન કરો. બાર મહિનાનું વીજ બિલ લો અને બાંધેલા વિસ્તારથી ભાગો, જેથી ઊર્જા "
        "કાર્યદક્ષતા સૂચકાંક મળે; પાણીનું બિલ કે બોરવેલ મીટરનું વાંચન લો અને વપરાશકારોની સંખ્યાથી ભાગો; એક અઠવાડિયું "
        "ગેટમાંથી નીકળતો કચરો તોળો અને કેટલો અલગ થયો તે તપાસો. ચાર આંકડા લીલા ધ્વજ પાસેના બોર્ડ પર મૂકો."),
      P("Then check the claims one by one. A rainwater tank: is it connected, and is it full in August? "
        "A solar roof: what does the inverter log show for the last month, and does it match the meter? "
        "A compost yard: is there compost, and who takes it? A green cover claim: count the trees and "
        "measure the canopy from a satellite image, not from a planting-day photograph.",
        "પછી દરેક દાવો એક પછી એક તપાસો. વરસાદી ટાંકી: જોડાયેલી છે, અને ઓગસ્ટમાં ભરેલી છે? સૌર છત: ઇન્વર્ટરનો "
        "લોગ છેલ્લા મહિનાનું શું કહે છે અને મીટર સાથે મળે છે? ખાતર યાર્ડ: ખાતર છે, અને કોણ લે છે? લીલા આવરણનો "
        "દાવો: વૃક્ષ ગણો અને ઉપગ્રહ ચિત્ર પરથી છત્ર માપો, વાવેતર દિવસના ફોટોગ્રાફ પરથી નહીં."),
      P("Finally, look at governance: is there a written environmental policy, a committee with "
        "students on it, an annual audit published on the website, and a budget line for maintenance? A "
        "campus with an ISO 14001 style register and a public annual report is sustainable even if it "
        "has no green flag; a campus with a flag and a dry tank is not.",
        "છેલ્લે શાસન જુઓ: લેખિત પર્યાવરણીય નીતિ છે, વિદ્યાર્થીઓ સાથેની સમિતિ છે, વેબસાઇટ પર પ્રકાશિત વાર્ષિક તપાસ "
        "છે, અને જાળવણી માટે બજેટ લાઇન છે? ISO 14001 જેવું રજિસ્ટર અને જાહેર વાર્ષિક અહેવાલવાળું કેમ્પસ લીલો ધ્વજ "
        "ન હોય તો પણ ટકાઉ છે; ધ્વજ અને સૂકી ટાંકીવાળું કેમ્પસ નથી.")]),
    (T("Write short notes on the National Green Tribunal and the polluter pays principle.",
       "રાષ્ટ્રીય લીલું ટ્રિબ્યુનલ અને પ્રદૂષક ચૂકવે સિદ્ધાંત પર ટૂંકી નોંધ લખો."), 4,
     [P("The National Green Tribunal was set up in 2010 under its own Act as a specialised court for "
        "environmental cases, so that a matter does not wait twenty years in a civil court. It has "
        "principal benches at Delhi and four zonal benches, hears both original applications and "
        "appeals, is not bound by the procedure of the Code of Civil Procedure but follows the "
        "principles of natural justice, and is required to dispose of a case within six months. Its "
        "orders can award compensation, order restitution of the environment and direct a regulator to "
        "act.",
        "રાષ્ટ્રીય લીલું ટ્રિબ્યુનલ 2010માં તેના પોતાના અધિનિયમ હેઠળ પર્યાવરણીય કેસ માટે વિશેષ અદાલત તરીકે ઊભું "
        "થયું, જેથી બાબત દીવાની અદાલતમાં વીસ વર્ષ રાહ ન જુએ. તેની મુખ્ય બેન્ચ દિલ્હીમાં અને ચાર ક્ષેત્રીય બેન્ચ છે, "
        "મૂળ અરજી અને અપીલ બંને સાંભળે, દીવાની કાર્યવિધિ સંહિતાથી બંધાયેલું નથી પણ કુદરતી ન્યાયના સિદ્ધાંતો પાળે, અને "
        "છ મહિનામાં કેસ નિકાલ કરવાનું જરૂરી છે. તેના આદેશ વળતર આપે, પર્યાવરણનું પુનઃસ્થાપન કરાવે અને નિયંત્રકને કામ "
        "કરવાનું કહે."),
      P("Polluter pays: the cost of preventing, controlling and remedying pollution falls on the person "
        "who caused it, and it is read into Indian law through the constitutional right to a clean "
        "environment and the Supreme Court's interpretation of Article 21. In practice it means a "
        "consent condition that requires an effluent plant, a compensation order after a spill, a "
        "clean-up cost recovered from the unit, and a fine that is at least as large as the saving from "
        "non-compliance - otherwise pollution is simply cheaper than compliance.",
        "પ્રદૂષક ચૂકવે: પ્રદૂષણ નિવારવા, નિયંત્રિત કરવા અને સુધારવાનો ખર્ચ જેને કારણે થયો તેના પર પડે, અને તે "
        "સ્વચ્છ પર્યાવરણના બંધારણીય અધિકાર તથા અનુચ્છેદ 21ના સર્વોચ્ચ અદાલતના અર્થઘટન દ્વારા ભારતીય કાયદામાં "
        "વંચાય છે. વ્યવહારમાં તેનો અર્થ પ્રવાહ સારવાર સ્ટેશન માંગતી સંમતિની શરત, ગળતર પછી વળતરનો આદેશ, એકમ પાસેથી "
        "વસૂલાત કરેલો સફાઈ ખર્ચ, અને અનુપાલન ન કરવાની બચત કરતાં ઓછામાં ઓછો એટલો જ મોટો દંડ - નહીં તો પ્રદૂષણ "
        "અનુપાલન કરતાં સસ્તું પડે.")]),
]

EXAM = [{"q": q, "marks": m} for q, m, _parts in _PRACTICE]
PRACTICE_ANSWERS = [_join(parts) for _q, _m, parts in _PRACTICE]
LESSON_COUNT = sum(len(s["items"]) for s in NOTES)

VIVA[0]["items"].extend([
    {"q": T("What is the precautionary principle and how does it change a decision?",
            "સાવચેતીનો સિદ્ધાંત શું છે અને તે નિર્ણય કેવી રીતે બદલે?"),
     "a": T("It says that where there is a threat of serious or irreversible damage, a lack of full "
            "scientific certainty is not a reason to postpone a cheap measure that prevents it. It "
            "reverses the usual burden: the promoter must show that the risk is acceptable rather than "
            "the public proving harm after it has happened. A dyeing unit that wants to discharge into "
            "a river must first show the effluent is safe, and a new chemical must be tested before "
            "release, not after a fish kill - which is why the principle is written into the "
            "Environment (Protection) Act and the EIA process.",
            "તે કહે છે કે ગંભીર કે પાછું ન ફરે તેવું નુકસાન થવાની ધમકી હોય ત્યાં પૂરી વૈજ્ઞાનિક ખાતરી ન હોવી એ "
            "તેને રોકતા સસ્તા પગલાને મુલતવી રાખવાનું કારણ નથી. તે સામાન્ય ભાર ઊંધો કરે: જાહેર જનતા નુકસાન થયા "
            "પછી પુરવાર કરે તેને બદલે પ્રસ્તાવકે જોખમ સ્વીકાર્ય છે તે બતાવવું પડે. નદીમાં છોડવા માંગતા રંગાઇ "
            "એકમે પહેલાં પ્રવાહ સુરક્ષિત છે તે બતાવવું પડે, અને નવું રસાયણ માછલી મર્યા પછી નહીં, છોડતાં પહેલાં "
            "કસાય - તેથી જ આ સિદ્ધાંત પર્યાવરણ (સંરક્ષણ) અધિનિયમ અને EIA પ્રક્રિયામાં લખાયેલો છે.")},
    {"q": T("What is an environmental aspect and what is an environmental impact?",
            "પર્યાવરણીય પાસું શું છે અને પર્યાવરણીય અસર શું છે?"),
     "a": T("An aspect is the element of an activity, product or service that interacts with the "
            "environment - what the plant does. An impact is the resulting change in the environment - "
            "what the environment suffers. In a foundry, 'charging the furnace with scrap' and 'pouring "
            "molten metal' are aspects; 'dust in the ambient air', 'heat stress for the workers' and "
            "'sand going to landfill' are impacts. One aspect can have several impacts, and the "
            "significance score combines severity, likelihood, legal limit and stakeholder concern. "
            "The system only works if the two columns are kept apart.",
            "પાસું એ પ્રવૃત્તિ, ઉત્પાદન કે સેવાનું પર્યાવરણ સાથે સંબંધ ધરાવતું અંગ છે - કારખાનું શું કરે છે. "
            "અસર એ પર્યાવરણમાં થતો પરિણામી ફેરફાર છે - પર્યાવરણને શું સહેવું પડે છે. ફાઉન્ડ્રીમાં 'ભઠ્ઠીમાં "
            "ભંગાર ભરવો' અને 'ઓગળેલી ધાતુ રેડવી' પાસાં છે; 'આસપાસની હવામાં ધૂળ', 'કામદારો પર ગરમીનો તણાવ' અને "
            "'રેતી લેન્ડફિલમાં જવી' અસરો છે. એક પાસાની ઘણી અસરો હોઈ શકે, અને મહત્ત્વનો અંક ગંભીરતા, શક્યતા, "
            "કાનૂની મર્યાદા અને હિતધારકની ચિંતા જોડે. બે કોલમ અલગ રહે તો જ પ્રણાલી ચાલે.")},
    {"q": T("Why did the Bhopal gas tragedy lead to a new law?",
            "ભોપાલ ગેસ દુર્ઘટના નવો કાયદો કેમ લાવી?"),
     "a": T("On the night of 2-3 December 1984 methyl isocyanate escaped from a pesticide plant in "
            "Bhopal and killed several thousand people and injured lakhs. The legal gap it exposed was "
            "that the existing laws controlled pollution from a running factory into a river or a "
            "chimney, but had no power over a stored chemical, an accident, an emergency plan or the "
            "liability of a multinational. Parliament answered with the Environment (Protection) Act "
            "1986, which covers handling of hazardous substances, gives the centre power to set "
            "standards and order closure, and was followed by the Public Liability Insurance Act, the "
            "hazardous waste rules and the National Green Tribunal. The lesson for an engineer is that "
            "the most dangerous part of a plant is often the storage tank, not the chimney.",
            "2-3 ડિસેમ્બર 1984ની રાત્રે ભોપાલની જંતનાશક કારખાનામાંથી મિથાઇલ આઇસોસાયનેટ નીકળીને હજારો લોકોને મારી "
            "નાખ્યા અને લાખોને ઘાયલ કર્યા. તે જે કાનૂની ખાલી જગ્યા ખોલી તે એ હતી કે હાલના કાયદા ચાલુ કારખાનાના "
            "નદી કે ચીમનીમાં પ્રદૂષણને નિયંત્રિત કરતા, પણ સંગ્રહિત રસાયણ, અકસ્માત, આપાતકાલીન યોજના કે બહુરાષ્ટ્રીય "
            "કંપનીની જવાબદારી પર સત્તા નહોતી. સંસદે પર્યાવરણ (સંરક્ષણ) અધિનિયમ 1986થી જવાબ આપ્યો, જે જોખમી પદાર્થની "
            "સંભાળ આવરે, કેન્દ્રને ધોરણ નક્કી કરવા અને બંધ કરવાની સત્તા આપે, અને પછી જાહેર જવાબદારી વીમા અધિનિયમ, "
            "જોખમી કચરા નિયમો અને રાષ્ટ્રીય લીલું ટ્રિબ્યુનલ આવ્યાં. ઇજનેર માટે પાઠ એ છે કે કારખાનાનો સૌથી જોખમી "
            "ભાગ ઘણી વાર સંગ્રહ ટાંકી હોય, ચીમની નહીં.")},
])

_PRACTICE.append(
    (T("What is an environmental management system? Explain its elements with the PDCA cycle and "
       "state the limitation of certification.",
       "પર્યાવરણીય વ્યવસ્થાપન પ્રણાલી શું છે? PDCA ચક્ર સાથે તેનાં અંગો સમજાવો અને પ્રમાણીકરણની મર્યાદા જણાવો."), 5,
     [P("An environmental management system is the organised way an organisation controls what it "
        "does to the environment: a policy, a register of aspects and impacts, a register of legal "
        "duties, objectives with targets and programmes, operational controls, monitoring, audit and "
        "review. ISO 14001 is the international standard for it, and the standard requires the system "
        "to be documented so that an auditor can test it.",
        "પર્યાવરણીય વ્યવસ્થાપન પ્રણાલી એ સંસ્થા પર્યાવરણ પર કરતી અસરને નિયંત્રિત કરવાની વ્યવસ્થિત રીત છે: "
        "નીતિ, પાસાં અને અસરોનું રજિસ્ટર, કાનૂની ફરજોનું રજિસ્ટર, લક્ષ્ય સાથેના ઉદ્દેશ અને કાર્યક્રમ, સંચાલન "
        "નિયંત્રણ, દેખરેખ, તપાસ અને સમીક્ષા. ISO 14001 તેના માટેનું આંતરરાષ્ટ્રીય ધોરણ છે, અને ધોરણ માંગે કે પ્રણાલી "
        "લેખિત હોય જેથી તપાસકર્તા તેને કસી શકે."),
      P("Plan: scope, policy, aspects and impacts scored for significance, legal register, objectives "
        "and targets. Do: roles, training, written operational control for each significant aspect, "
        "emergency preparedness. Check: monitoring and measurement, calibration, internal audit and "
        "non-conformity records. Act: root-cause correction, revised risk assessment, management review "
        "and input to the next plan.",
        "આયોજન: વ્યાપ, નીતિ, મહત્ત્વ માટે અંકાયેલાં પાસાં અને અસરો, કાનૂની રજિસ્ટર, ઉદ્દેશ અને લક્ષ્ય. અમલ: "
        "ભૂમિકા, તાલીમ, દરેક મહત્ત્વના પાસાં માટે લેખિત સંચાલન નિયંત્રણ, આપાતકાલીન તૈયારી. તપાસ: દેખરેખ અને માપન, "
        "કેલિબ્રેશન, આંતરિક તપાસ અને બિન-અનુરૂપતાની નોંધ. સુધારો: મૂળ કારણ સુધારો, સુધારેલું જોખમ આકલન, "
        "વ્યવસ્થાપન સમીક્ષા અને આગલા આયોજનમાં ઇનપુટ."),
      P("The limitation: the certificate says the system exists and is followed, not that the "
        "performance is good. A plant with weak targets can be certified and still be a heavy polluter. "
        "That is why the sensible buyer asks for the objectives, the monitoring data and the measured "
        "energy and water figures, and treats the certificate as the beginning of the conversation, "
        "not the end of it.",
        "મર્યાદા: પ્રમાણપત્ર કહે છે કે પ્રણાલી અસ્તિત્વમાં છે અને પાળાય છે, એ નહીં કે કાર્યદક્ષતા સારી છે. નબળા "
        "ઉદ્દેશવાળું કારખાનું પ્રમાણિત થઈને પણ ભારે પ્રદૂષક રહી શકે. તેથી જ સમજદાર ખરીદનાર ઉદ્દેશ, દેખરેખ માહિતી અને "
        "માપેલા ઊર્જા તથા પાણીના આંકડા માંગે, અને પ્રમાણપત્રને વાતચીતની શરૂઆત ગણે, અંત નહીં.")]))

# The practice list is extended above, so the derived views are rebuilt here.
EXAM = [{"q": q, "marks": m} for q, m, _parts in _PRACTICE]
PRACTICE_ANSWERS = [_join(parts) for _q, _m, parts in _PRACTICE]
