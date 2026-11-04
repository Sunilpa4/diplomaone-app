"""DI05005031 Unit 4, part B: the flow reactors (CSTR and PFR) and the packed beds (fixed and
fluidised)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from subject_DI05005031 import tr  # noqa: E402
from content_DI05005031_lib import (p, h4, ul, ol, table, math, eq, why, check, pit, derive,
                                    parts, working, card)  # noqa: E402

NOTES_B = []

NOTES_B.append({
    "title": tr("4.2 The flow reactors: CSTR and PFR", "4.2 Flow reactors: CSTR અને PFR"),
    "items": [
        card(
            "The CSTR (mixed flow reactor): construction and working",
            "CSTR (mixed flow reactor): રચના અને કાર્યપદ્ધતિ",
            p("The continuous stirred tank reactor is a stirred vessel with a continuous feed and a "
              "continuous overflow. Because the stirrer works faster than the feed, the contents are "
              "uniform - and the outlet carries exactly the composition that is inside.",
              "Continuous stirred tank reactor એ સતત feed અને સતત overflow વાળું હલાવેલું પાત્ર છે. Stirrer "
              "feed કરતાં ઝડપી કામ કરે છે, તેથી અંદરનું બધું સરખું હોય - અને outlet અંદરની જ રચના "
              "ધરાવે."),
            parts(("Shell with a dished bottom - sized for the space time, not for the reaction time.",
                   "છીછરા તળિયા વાળું shell - space time માટે, reaction time માટે નહીં."),
                  ("Overflow nozzle at the liquid level - fixes the volume, so the level never rises.",
                   "પ્રવાહી સપાટી પરનું overflow nozzle - volume નક્કી રાખે, તેથી level કદી ન વધે."),
                  ("Feed pump and inlet nozzle - brings the mixed feed to the bottom of the impeller.",
                   "Feed pump અને inlet nozzle - મિશ્ર feed ને impeller ના તળિયે લાવે."),
                  ("Turbine impeller and baffles - the impeller alone makes a swirl; the baffles turn "
                   "it into real mixing.", "Turbine impeller અને baffles - ફક્ત impeller વંટોળ બનાવે; "
                   "baffles તેને ખરું mixing બનાવે."),
                  ("Jacket or internal coil - holds the temperature at the exit condition, which is "
                   "the only condition the reactor ever sees.",
                   "Jacket કે અંદરની coil - temperature exit ની શરત પર રાખે, જે એક જ શરત reactor જુએ છે."),
                  ("Level and temperature control loops - a CSTR that loses its level loses its "
                   "residence time.", "Level અને temperature control loops - level ગુમાવતો CSTR પોતાનો "
                   "residence time ગુમાવે.")),
            working(("Feed enters below the impeller and is thrown outward into the baffled bulk.",
                     "Feed impeller નીચે આવે અને baffles વાળા જથ્થામાં બહાર ફેંકાય."),
                    ("One pass of the impeller mixes the whole vessel in a time of the order of a few "
                     "seconds to a minute.", "Impeller નો એક ફેરો આખું પાત્ર કેટલાક second થી એક "
                     "મિનિટમાં મિક્સ કરે."),
                    ("The mixture leaves through the overflow at the same composition as the bulk.",
                     "મિશ્રણ overflow થી જથ્થાની જ રચના સાથે નીકળે."),
                    ("Steady state is reached after about three space times; the product from then on "
                     "is constant.", "લગભગ ત્રણ space times પછી steady state આવે; ત્યાર પછીનું product "
                     "અચળ."),
                    ("The conversion is set by the space time, so the operator changes flow or "
                     "temperature, never the level.",
                     "Conversion space time નક્કી કરે, તેથી ઓપરેટર flow કે temperature બદલે, level નહીં.")),
            h4("The design equation", "Design equation"),
            derive("mole balance on A at steady state: in - out - reaction = 0",
                   "FA0 - FA - (-rA) V = 0",
                   "with FA = FA0(1 - X):   V = FA0 X / (-rA)exit",
                   "dividing by the feed rate:  tau = V/v0 = CA0 X / (-rA)exit",
                   "first order: tau = X/[k(1 - X)]"),
            math("first order, X = 0.90: tau = 0.9/(k x 0.1) = 9/k",
                 "PFR for the same duty: tau = ln(10)/k = 2.30/k, so 3.9 times less volume"),
            why("The CSTR is the only reactor that always works at the outlet concentration, which is "
                "the lowest concentration in the system. For a positive order reaction that is the "
                "slowest possible rate, which is exactly why it needs the largest volume - and "
                "exactly why it is the safest to control.",
                "CSTR એ જ reactor છે જે હંમેશા outlet concentration પર કામ કરે, જે system માં સૌથી નીચું "
                "concentration છે. ધન order ની પ્રક્રિયા માટે એ સૌથી ધીમો possible rate છે, તેથી જ તેને "
                "સૌથી મોટું volume જોઈએ - અને તેથી જ તે નિયંત્રણમાં સૌથી સલામત છે."),
            check("With X = 0.9 the CSTR needs k tau = 9 while a PFR needs 2.3; with X = 0.5 the two "
                  "are 1 and 0.69, so the penalty of a CSTR is worst at high conversion.",
                  "X = 0.9 સાથે CSTR ને k tau = 9 જોઈએ જ્યારે PFR ને 2.3; X = 0.5 પર બંને 1 અને 0.69 "
                  "છે, તેથી CSTR ની સજા ઊંચા conversion પર સૌથી વધુ છે."),
            pit("Putting a CSTR in series with itself and expecting the same volume. Two equal CSTRs "
                "in series reach 90 % in k tau = 4.3 instead of 9 - half the volume for the same "
                "duty, which is why trains of tanks are common.",
                "CSTR ને તેની જ સાથે series માં મૂકીને એ જ volumeની અપેક્ષા રાખવી. બે સરખા CSTR series "
                "માં 90 % સુધી k tau = 4.3 માં પહોંચે, 9 ને બદલે - એટલે અડધું volume, તેથી tank ની "
                "શ્રેણી સામાન્ય છે."),
            diagram="u4_cstr",
            syllabus_item="4.2",
        ),
        card(
            "The tubular (plug flow) reactor: construction and working",
            "Tubular (plug flow) reactor: રચના અને કાર્યપદ્ધતિ",
            p("A PFR is a tube. Fluid enters at one end and leaves at the other, and the only mixing "
              "is across the tube - none along it. Every element therefore sees the same history, "
              "and the concentration falls steadily from inlet to outlet.",
              "PFR એ નળી છે. પ્રવાહી એક છેડેથી આવે અને બીજા છેડેથી નીકળે, અને mixing ફક્ત નળીની પહોળાઈમાં "
              "થાય - લંબાઈમાં નહીં. તેથી દરેક element સરખો ઇતિહાસ જુએ, અને concentration inlet થી outlet "
              "સુધી સ્થિર રીતે ઘટે."),
            parts(("Tube or a bundle of tubes - gives the length and the volume; no moving parts at "
                   "all.", "નળી કે નળીઓનો bundle - લંબાઈ અને volume આપે; કોઈ હલતો ભાગ નહીં."),
                  ("Jacket or shell around the tubes - removes or adds heat along the whole length.",
                   "નળીઓ ફરતું jacket કે shell - આખી લંબાઈ પર heat કાઢે કે ઉમેરે."),
                  ("Inlet distributor and outlet header - spread the feed evenly over all the tubes.",
                   "Inlet distributor અને outlet header - feed ને બધી નળીઓ પર સરખો વહેંચે."),
                  ("Baffles in the shell side - force the coolant across the tubes so the heat "
                   "transfer coefficient stays high.", "Shell બાજુના baffles - coolant ને નળીઓની આડે "
                   "ફેરવે જેથી heat transfer coefficient ઊંચો રહે."),
                  ("Support plates and expansion joint - hold long tubes and let them grow when hot.",
                   "Support plates અને expansion joint - લાંબી નળીઓ પકડે અને ગરમ થતાં વધવા દે.")),
            working(("Feed is pushed through the tube by a pump or a compressor at a steady rate.",
                     "Feed ને pump કે compressor સ્થિર rate પર નળીમાં ધકેલે."),
                    ("Across any cross-section the fluid is mixed; along the tube it is not, so a "
                     "slice moves like a piston.", "કોઈ પણ cross-section માં પ્રવાહી મિક્સ હોય; લંબાઈમાં "
                     "નહીં, તેથી slice piston ની જેમ આગળ વધે."),
                    ("Reaction starts at the inlet and slows towards the outlet, because the "
                     "concentration is falling.", "પ્રક્રિયા inlet પર શરૂ થાય અને outlet તરફ ધીમી પડે, "
                     "કારણ કે concentration ઘટે છે."),
                    ("Heat is exchanged along the length, so a PFR is also a heat exchanger - its "
                     "temperature profile is a design variable.", "લંબાઈ પર heat ની આપલે થાય, તેથી PFR "
                     "heat exchanger પણ છે - તેનો temperature profile design નું ચલ છે."),
                    ("All the fluid leaves after the same residence time tau = V/v0.",
                     "બધું પ્રવાહી સરખા residence time tau = V/v0 પછી નીકળે.")),
            h4("The design equation", "Design equation"),
            derive("mole balance on a slice dV: FA(V) - FA(V + dV) - (-rA) dV = 0",
                   "so dFA/dV = -(-rA), and with FA = FA0(1 - X):",
                   "FA0 dX/dV = -rA   ->   V = FA0 x integral from 0 to X of dX/(-rA)",
                   "first order: V = v0 ln[1/(1 - X)] / k,  i.e. tau = ln[1/(1 - X)]/k"),
            math("first order, X = 0.90: tau = 2.303/k",
                 "the same duty in one CSTR: tau = 9/k"),
            table([tr("CSTR", "CSTR"), tr("PFR", "PFR")],
                  [[tr("mixed: works at the exit concentration", "મિશ્ર: exit concentration પર કામ કરે"),
                    tr("unmixed: concentration falls along the tube",
                       "અમિશ્ર: concentration નળીમાં ઘટે")],
                   [tr("large volume at high conversion", "ઊંચા conversion પર મોટું volume"),
                    tr("smallest volume for a positive order reaction",
                       "ધન order પ્રક્રિયા માટે સૌથી નાનું volume")],
                   [tr("temperature uniform and easy to hold",
                       "temperature સરખું અને પકડવું સહેલું"),
                    tr("temperature profile along the length; hot spots possible",
                       "લંબાઈ પર temperature profile; hot spots શક્ય")],
                   [tr("good for slow reactions, autocatalytic ones and crystallisation",
                       "ધીમી, autocatalytic અને crystallisation માટે સારું"),
                    tr("good for gas phase, high temperature and large scale",
                       "gas phase, ઊંચા temperature અને મોટા scale માટે સારું")]]),
            why("Plug flow is the best possible arrangement for a positive order reaction: the "
                "reactant is kept at its highest concentration for as long as possible, and the "
                "integral of the rate is maximised.",
                "ધન order પ્રક્રિયા માટે plug flow સૌથી સારી ગોઠવણી છે: reactant પોતાના સૌથી ઊંચા "
                "concentration પર શક્ય તેટલો સમય રહે, અને rate નો integral મહત્તમ થાય."),
            check("At X = 0.99 the PFR needs 4.61/k but the CSTR needs 99/k - a factor of 21. The "
                  "higher the conversion asked for, the stronger the case for a tube.",
                  "X = 0.99 પર PFR ને 4.61/k જોઈએ પણ CSTR ને 99/k - 21 ગણો ફરક. જેટલું ઊંચું conversion "
                  "માંગો તેટલો નળીનો પક્ષ મજબૂત."),
            pit("Treating a long pipe as a PFR without checking. Axial dispersion, laminar velocity "
                "profiles and natural convection all break plug flow; a tube is only a PFR while the "
                "dispersion number stays small.",
                "લાંબી પાઇપને ચકાસ્યા વગર PFR ગણવી. Axial dispersion, laminar velocity profile અને "
                "natural convection plug flow તોડે છે; dispersion number નાનો રહે ત્યાં સુધી જ નળી PFR "
                "છે."),
            diagram="u4_pfr",
            syllabus_item="4.2",
        ),
    ],
})

NOTES_B.append({
    "title": tr("4.2 Packed beds: the fixed bed and the fluidised bed",
                "4.2 Packed beds: fixed bed અને fluidised bed"),
    "items": [
        card(
            "The fixed bed reactor: construction and working",
            "Fixed bed reactor: રચના અને કાર્યપદ્ધતિ",
            parts(("Shell - a vertical vessel, usually refractory-lined for high temperature service.",
                   "Shell - ઊભું પાત્ર, ઊંચા temperature માટે સામાન્ય રીતે refractory લાઇનિંગ વાળું."),
                  ("Inlet distributor - spreads the gas over the whole cross-section so no channel "
                   "forms.", "Inlet distributor - gas ને આખા cross-section પર વહેંચે જેથી channel ન "
                   "બને."),
                  ("Catalyst bed - pellets or rings of 3-10 mm, held between inert layers at top and "
                   "bottom.", "Catalyst bed - 3-10 mm ના pellets કે rings, ઉપર-નીચે inert સ્તર વચ્ચે."),
                  ("Support grid and support balls - carry the weight of the bed without blocking "
                   "the flow.", "Support grid અને support balls - flow રોક્યા વગર bed નું વજન ઉપાડે."),
                  ("Jacket, coils or a quench line - take away the heat of reaction; the alternative "
                   "is a bed of several stages.", "Jacket, coils કે quench line - પ્રક્રિયાની heat "
                   "કાઢે; બીજો રસ્તો કેટલાક તબક્કાનો bed છે."),
                  ("Thermocouples in a well - the only way to see the hot spot forming.",
                   "Well માં thermocouples - બનતો hot spot જોવાનો એક જ રસ્તો.")),
            working(("Gas enters at the top, passes through the distributor and spreads over the bed.",
                     "Gas ઉપરથી આવે, distributor માંથી પસાર થાય અને bed પર ફેલાય."),
                    ("It threads through the voids between pellets; the reaction happens on the "
                     "wetted pellet surface.", "તે pellets વચ્ચેના voids માંથી પસાર થાય; પ્રક્રિયા "
                     "ભીની pellet સપાટી પર થાય."),
                    ("The gas leaves at the bottom through the support grid, cooler or hotter than it "
                     "entered.", "Gas તળિયે support grid થી નીકળે, આવ્યું તેના કરતાં ઠંડું કે ગરમ."),
                    ("Pressure drop rises as the bed fouls; it is the operating signal that the bed "
                     "must be cleaned or replaced.", "Bed ગંદું થાય તેમ pressure drop વધે; એ જ સંકેત "
                     "કે bed સાફ કે બદલવો પડશે."),
                    ("Regeneration or replacement needs the unit shut down - the fixed bed's one big "
                     "disadvantage.", "Regeneration કે replacement માટે unit બંધ કરવું પડે - fixed bed "
                     "ની એક મોટી ખામી.")),
            h4("The design relations", "Design ના સંબંધો"),
            derive("rate per unit mass of catalyst: -rA' = -rA/rho_b",
                   "design: W = FA0 x integral from 0 to X of dX/(-rA')",
                   "space velocity: WHSV = mass feed per hour / mass of catalyst",
                   "void fraction: eps = void volume / bed volume, so bed volume = W/(rho_p (1 - eps))"),
            math("Ergun for the pressure drop through a packed bed:",
                 "dP/L = 150 mu u (1-eps)^2/(eps^3 dp^2) + 1.75 rho u^2 (1-eps)/(eps^3 dp)"),
            table([tr("Strengths", "તાકાત"), tr("Weaknesses", "નબળાઈ")],
                  [[tr("big catalyst area in a small volume, no moving parts",
                       "નાના volume માં મોટું catalyst area, હલતો ભાગ નહીં"),
                    tr("pressure drop, and it grows as the bed fouls",
                       "pressure drop, અને bed ગંદું થાય તેમ વધે")],
                   [tr("plug flow gives the highest conversion per unit volume",
                       "plug flow પ્રતિ volume સૌથી ઊંચું conversion આપે"),
                    tr("hot spots and possible runaway near the inlet",
                       "inlet પાસે hot spots અને runaway શક્ય")],
                   [tr("simple, well understood, easy to scale up in diameter",
                       "સાદું, સારી રીતે સમજાયેલું, વ્યાસમાં scale up સહેલું"),
                    tr("catalyst cannot be changed while running; gas channelling",
                       "ચાલુ સ્થિતિમાં catalyst બદલાય નહીં; gas channelling")]]),
            why("A fixed bed is a PFR as seen by the gas, with the catalyst counted in kilograms "
                "instead of cubic metres. Every PFR design equation therefore applies, with -rA' and "
                "W in place of -rA and V.",
                "Fixed bed એ gas ના દૃષ્ટિકોણથી PFR છે, જેમાં catalyst ઘન મીટરને બદલે કિલોગ્રામમાં "
                "ગણાય. તેથી દરેક PFR design equation લાગુ પડે, -rA અને V ની જગ્યાએ -rA' અને W સાથે."),
            check("A bed of 250 kg with a 500 kg/h feed runs at WHSV = 2 h-1, i.e. a space time of "
                  "0.5 h. If the same duty needed WHSV = 1, the bed would have to be 500 kg.",
                  "250 kg નો bed અને 500 kg/h feed સાથે WHSV = 2 h-1, એટલે space time 0.5 h. એ જ કામ "
                  "માટે WHSV = 1 જોઈએ તો bed 500 kg નો કરવો પડે."),
            pit("Using the bed volume as if it were all catalyst. The gas only passes through the "
                "voids, so eps (usually 0.35-0.45) decides the actual residence time and the pressure "
                "drop.",
                "આખા bed volume ને catalyst ગણવું. Gas ફક્ત voids માંથી પસાર થાય, તેથી eps (સામાન્ય "
                "0.35-0.45) ખરો residence time અને pressure drop નક્કી કરે."),
            diagram="u4_fixed",
            syllabus_item="4.2",
        ),
        card(
            "The fluidised bed reactor: construction and working",
            "Fluidised bed reactor: રચના અને કાર્યપદ્ધતિ",
            p("If the gas is pushed through a bed of particles fast enough, the particles are lifted "
              "and the bed behaves like a boiling liquid. That single change - a bed that flows - "
              "solves the fixed bed's heat problem and creates a new set of its own.",
              "જો gas ને particles ના bed માંથી પૂરતી ઝડપે ધકેલવામાં આવે તો particles ઊંચકાય અને bed "
              "ઉકળતા પ્રવાહી જેવો વર્તે. એ એક ફેરફાર - વહેતો bed - fixed bed ની heat સમસ્યા ઉકેલે છે "
              "અને પોતાની નવી સમસ્યાઓ ઊભી કરે છે."),
            parts(("Distributor plate (tuyere or perforated grid) - the single most important part: "
                   "it must give every hole the same gas flow.", "Distributor plate - સૌથી અગત્યનો ભાગ: "
                   "દરેક છિદ્રને સરખો gas flow આપવો પડે."),
                  ("Dense bed - 0.3 to 1 m of catalyst powder (50-150 micron), bubbling like a liquid.",
                   "Dense bed - 0.3 થી 1 m catalyst પાવડર (50-150 micron), પ્રવાહીની જેમ ઉકળતો."),
                  ("Freeboard - the empty space above the bed where the particles fall back.",
                   "Freeboard - bed ઉપરની ખાલી જગ્યા જ્યાં particles પાછા પડે."),
                  ("Cyclones and diplegs - catch the entrained catalyst and return it to the bed; "
                   "without them the bed is lost in a day.", "Cyclones અને diplegs - ઊડી જતો catalyst "
                   "પકડીને bed માં પાછો મોકલે; તેમના વગર bed એક દિવસમાં ખતમ."),
                  ("Internal coils or a cooled wall - take the heat out of a bed that mixes "
                   "perfectly.", "અંદરની coils કે ઠંડી દીવાલ - સંપૂર્ણ મિશ્ર bed માંથી heat કાઢે."),
                  ("Catalyst withdrawal and make-up lines - the bed can be refreshed while the unit "
                   "runs.", "Catalyst કાઢવાની અને ભરવાની લાઇન - unit ચાલુ હોય ત્યારે bed તાજો થઈ શકે.")),
            working(("Gas enters the windbox below the distributor and is spread evenly.",
                     "Gas distributor નીચેના windbox માં આવે અને સરખી રીતે ફેલાય."),
                    ("Above the minimum fluidisation velocity the particles lift and the bed expands.",
                     "Minimum fluidisation velocity ઉપર particles ઊંચકાય અને bed ફેલાય."),
                    ("Extra gas passes through as bubbles that rise, grow and burst at the surface.",
                     "વધારાનો gas bubbles તરીકે પસાર થાય, જે ઉપર જાય, મોટા થાય અને સપાટી પર ફૂટે."),
                    ("The dense phase behaves like a CSTR (strong back-mixing); the bubbles carry gas "
                     "through almost unreacted.", "ઘન phase CSTR જેવો વર્તે (જોરદાર back-mixing); "
                     "bubbles gas ને લગભગ પ્રક્રિયા વગર પસાર કરે."),
                    ("Gas leaves through the cyclones, which return the fines to the bed.",
                     "Gas cyclones થી નીકળે, જે fines ને bed માં પાછા આપે.")),
            h4("The relations that decide the design", "Design નક્કી કરતા સંબંધો"),
            derive("minimum fluidisation: weight of bed = drag at Umf",
                   "Umf ~ dp^2 (rho_p - rho_g) g / (1650 mu)      for small particles",
                   "the bed is fluidised when U > Umf; bubbling starts near 2-3 Umf",
                   "bed height from the solids: W = rho_p A H (1 - eps)"),
            math("dp = 100 micron, rho_p = 2500 kg/m3, rho_g = 1.2, mu = 1.8e-5 Pa s:",
                 "Umf = (1e-4)^2 x 2499 x 9.81/(1650 x 1.8e-5) = 8.3e-3 m/s",
                 "so any gas velocity above about 8 mm/s fluidises this powder"),
            table([tr("Strengths", "તાકાત"), tr("Weaknesses", "નબળાઈ")],
                  [[tr("uniform temperature: no hot spot, so strong exotherms are safe",
                       "સરખું temperature: hot spot નહીં, તેથી તીવ્ર exotherm સલામત"),
                    tr("gas back-mixes like a CSTR, so conversion per pass is lower",
                       "gas CSTR ની જેમ back-mix થાય, તેથી પ્રતિ pass conversion ઓછું")],
                   [tr("catalyst can be withdrawn and replaced while running",
                       "ચાલુ state માં catalyst કાઢી બદલી શકાય"),
                    tr("attrition of the particles, and the fines must be caught",
                       "particles ઘસાય, અને fines પકડવા પડે")],
                   [tr("high heat transfer to coils; handles fine, cheap catalyst",
                       "coils સુધી ઊંચો heat transfer; બારીક, સસ્તો catalyst ચાલે"),
                    tr("erosion, scale-up difficulty, and a distributor that must not block",
                       "erosion, scale-up અઘરું, અને ન બંધાય તેવો distributor")]]),
            why("Fluidisation trades plug flow for perfect mixing of the solids and near-perfect "
                "mixing of the gas. That is a bad trade for conversion and a very good trade for "
                "temperature control, which is why catalytic crackers use it and ammonia synthesis "
                "does not.",
                "Fluidisation plug flow ને ઘન પદાર્થના સંપૂર્ણ mixing અને gas ના લગભગ સંપૂર્ણ mixing સાથે "
                "બદલે. એ conversion માટે ખરાબ સોદો અને temperature control માટે ખૂબ સારો સોદો છે, તેથી "
                "catalytic cracker તે વાપરે અને ammonia synthesis નહીં."),
            check("At 3 Umf the gas spends about a third of its time as bubbles; if the reaction is "
                  "fast, much of the conversion happens in the dense phase and the bubbles are "
                  "wasted - which is why internals are fitted to break them.",
                  "3 Umf પર gas નો લગભગ ત્રીજો ભાગ bubbles તરીકે જાય; પ્રક્રિયા ઝડપી હોય તો ઘણું "
                  "conversion ઘન phase માં થાય અને bubbles વેડફાય - તેથી તેમને તોડવા internals "
                  "બેસાડાય છે."),
            pit("Designing a fluidised bed from the reactor equation alone. The gas that bypasses in "
                "bubbles never meets the catalyst, so the two-phase model - not the simple CSTR "
                "equation - is what the design is checked against.",
                "ફક્ત reactor equation પરથી fluidised bed design કરવું. Bubbles માંથી પસાર થતો gas "
                "catalyst ને મળતો જ નથી, તેથી design two-phase model સામે ચકાસાય છે, સાદા CSTR "
                "equation સામે નહીં."),
            diagram="u4_fluidised",
            syllabus_item="4.2",
        ),
    ],
})
