"""DI05005031 Unit 4, part A: section 4.1 (features of ideal reactors) and 4.2 batch and semi-batch."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from subject_DI05005031 import tr  # noqa: E402
from content_DI05005031_lib import (p, h4, ul, ol, table, math, eq, why, check, pit, derive,
                                    parts, working, card)  # noqa: E402

NOTES_A = []

NOTES_A.append({
    "title": tr("4.1 What makes a reactor ideal", "4.1 Reactor આદર્શ કેવી રીતે બને"),
    "items": [
        card(
            "Three ideal models, and why engineers start from them",
            "ત્રણ આદર્શ models, અને engineer તેમનાથી કેમ શરૂ કરે",
            p("A real reactor has dead corners, a jet that short-circuits the inlet to the outlet, "
              "catalyst pellets with different amounts of gas on each side. None of that can be put "
              "into an equation directly, so the subject starts from three <b>ideal</b> models - "
              "pictures of perfect behaviour - and designs against them.",
              "સાચા reactor માં મૃત ખૂણા, inlet થી outlet સુધી સીધો જતો jet, અને દરેક બાજુ જુદો gas "
              "ધરાવતા catalyst pellets હોય છે. એમાંથી કંઈ સીધું સમીકરણમાં મૂકી શકાતું નથી, તેથી વિષય "
              "ત્રણ <b>આદર્શ</b> models થી શરૂ થાય છે - સંપૂર્ણ વર્તનનાં ચિત્રો - અને તેમની સામે "
              "design કરે છે."),
            math("ideal batch: no in, no out, perfectly mixed inside",
                 "ideal CSTR : steady in and out, perfectly mixed inside",
                 "ideal PFR  : steady in and out, no mixing along the flow"),
            h4("The assumptions, written down", "ધારણાઓ, લખેલી રીતે"),
            ul(("Perfect mixing: at any instant the composition and temperature are the same at "
                "every point of a batch or CSTR.",
                "Perfect mixing: કોઈ પણ ક્ષણે batch કે CSTR ના દરેક બિંદુએ રચના અને temperature સરખાં."),
               ("Plug flow: in a PFR the velocity is the same across the section, so every element "
                "spends the same time in the reactor.",
                "Plug flow: PFR માં આખા section પર velocity સરખી, તેથી દરેક element reactor માં સરખો "
                "સમય ગાળે."),
               ("Steady state: for the flow reactors nothing changes with time at a fixed point.",
                "Steady state: flow reactors માટે કોઈ બિંદુએ સમય સાથે કંઈ બદલાતું નથી."),
               ("Constant density unless an expansion factor says otherwise (Unit 3).",
                "Expansion factor કહે નહીં ત્યાં સુધી density અચળ (Unit 3).")),
            h4("The three design equations that follow", "ત્યારબાદ મળતાં ત્રણ design equations"),
            derive("batch: t = NA0 x integral dX/(-rA V)          no flow term at all",
                   "CSTR : V = FA0 X / (-rA)exit               one algebraic line",
                   "PFR  : V = FA0 x integral dX/(-rA)         an integral along the tube",
                   "all three come from one mole balance - the difference is only the mixing picture"),
            p("The three equations are the whole of Unit 5. Here they are only written down so that "
              "each reactor in this unit can be judged by the equation it satisfies.",
              "આ ત્રણ equations એ આખું Unit 5 છે. અહીં તે ફક્ત એટલા માટે લખ્યા છે કે આ unit ના દરેક "
              "reactor ને તે જે equation પાળે છે તેનાથી અજમાવી શકાય."),
            table([tr("Model", "Model"), tr("Flow", "Flow"), tr("What varies inside", "અંદર શું બદલાય"),
                   tr("Design variable", "Design variable")],
                  [[tr("Batch", "Batch"), tr("none", "કંઈ નહીં"),
                    tr("composition changes with time", "રચના સમય સાથે બદલાય"),
                    tr("time t", "સમય t")],
                   [tr("CSTR", "CSTR"), tr("in and out", "અંદર અને બહાર"),
                    tr("nothing varies inside", "અંદર કંઈ બદલાતું નથી"),
                    tr("volume V", "volume V")],
                   [tr("PFR", "PFR"), tr("in and out", "અંદર અને બહાર"),
                    tr("composition along the length", "લંબાઈ પર રચના"),
                    tr("volume V", "volume V")]]),
            why("Ideals are useful because they are bounds. A real reactor cannot beat a PFR for a "
                "positive order reaction and cannot do worse than a CSTR, so the two ideals bracket "
                "the plant: design against the bad one, pay for the good one, and measure the gap "
                "with a tracer.",
                "આદર્શ એટલા માટે ઉપયોગી છે કે તે મર્યાદાઓ છે. ધન order ની પ્રક્રિયા માટે સાચો reactor "
                "PFR થી સારો ન હોઈ શકે અને CSTR થી ખરાબ ન હોઈ શકે, તેથી બંને આદર્શ plant ને બંને "
                "બાજુથી બાંધે: ખરાબ વાળા સામે design કરો, સારા વાળાની કિંમત આપો, અને tracer થી "
                "અંતર માપો."),
            check("For first order with 90 % conversion, k tau is 2.303 in a PFR and 9 in a CSTR - a "
                  "factor of 3.9 in volume. Any answer between the two is a real reactor.",
                  "90 % conversion સાથે first order માટે PFR માં k tau 2.303 અને CSTR માં 9 છે - "
                  "volume માં 3.9 ગણો ફરક. બંને વચ્ચેનો કોઈ પણ જવાબ સાચો reactor છે."),
            pit("Calling a stirred tank a CSTR because it is stirred. A CSTR needs the mixing time "
                "far below the space time and a feed and outlet that do not short-circuit; a badly "
                "baffled tank is neither CSTR nor PFR.",
                "હલાવેલી tank ને ફક્ત હલાવે છે તેથી CSTR કહેવું. CSTR માટે mixing time space time કરતાં "
                "ઘણો નાનો જોઈએ અને feed તથા outlet short-circuit ન કરે; ખરાબ baffle વાળી tank CSTR પણ "
                "નથી અને PFR પણ નથી."),
            diagram="u4_models",
            syllabus_item="4.1",
        ),
    ],
})

NOTES_A.append({
    "title": tr("4.2 Batch and semi-batch reactors", "4.2 Batch અને semi-batch reactors"),
    "items": [
        card(
            "The batch reactor: construction and working",
            "Batch reactor: રચના અને કાર્યપદ્ધતિ",
            parts(("Shell with a dished bottom - holds the charge and takes the pressure.",
                   "ચાર્જ ધરાવતું અને pressure ખમતું છીછરા તળિયા વાળું shell."),
                  ("Agitator: motor, gearbox, shaft and impeller - keeps the batch uniform and speeds "
                   "up heat transfer.", "Agitator: motor, gearbox, shaft અને impeller - batch સરખું "
                   "રાખે અને heat transfer ઝડપી કરે."),
                  ("Baffles - stop the liquid rotating as a solid body, so the impeller really mixes.",
                   "Baffles - પ્રવાહીને ઘન પદાર્થની જેમ ફરતું અટકાવે, જેથી impeller ખરેખર મિક્સ કરે."),
                  ("Jacket (or coils) - heating or cooling medium, the only way to hold the "
                   "temperature of an exotherm.", "Jacket (કે coils) - ગરમ કે ઠંડું કરતું માધ્યમ, "
                   "exotherm નું temperature પકડી રાખવાનો એક જ રસ્તો."),
                  ("Thermometer pocket, pressure gauge and relief valve - the batch is watched and "
                   "protected.", "Thermometer pocket, pressure gauge અને relief valve - batch પર "
                   "નજર અને રક્ષણ."),
                  ("Charge nozzle, sight glass, sample point and bottom drain valve - filling, "
                   "watching, testing and emptying.", "Charge nozzle, sight glass, sample point અને "
                   "તળિયાનો drain valve - ભરવું, જોવું, ચકાસવું અને ખાલી કરવું.")),
            working(("Charge: weigh and add the reactants (and the solvent) through the charge nozzle.",
                     "ચાર્જ: reactants (અને solvent) તોળીને charge nozzle થી ઉમેરો."),
                    ("Bring to temperature: jacket heating with the agitator running, so no local "
                     "hot spot forms.", "Temperature પર લાવો: agitator ચાલુ રાખીને jacket થી ગરમ કરો, "
                     "જેથી local hot spot ન બને."),
                    ("React: start the clock at the moment the last reactant is in; sample at set "
                     "times or run for the calculated time.", "પ્રક્રિયા: છેલ્લો reactant ઉમેરાય તે ક્ષણે "
                     "ઘડિયાળ શરૂ કરો; નક્કી સમયે sample લો કે ગણેલા સમય સુધી ચલાવો."),
                    ("Control: jacket cooling takes the heat of reaction away; if the temperature "
                     "runs, the charge rate was too high.", "નિયંત્રણ: jacket નું ઠંડક પ્રક્રિયાની "
                     "heat કાઢે; temperature દોડે તો charge rate વધારે હતો."),
                    ("Discharge: empty through the bottom valve, quench or neutralise, then clean the "
                     "vessel before the next batch.", "ડિસ્ચાર્જ: તળિયાના valve થી ખાલી કરો, quench કે "
                     "neutralise કરો, પછી આગલા batch પહેલાં પાત્ર સાફ કરો.")),
            h4("The design equation", "Design equation"),
            derive("mole balance on A over the whole batch: NA0 dX/dt = -rA V",
                   "constant volume: t = CA0 x integral from 0 to X of dX/(-rA)",
                   "first order: t = (1/k) ln[1/(1 - X)]",
                   "second order, CA0 = CB0: t = X/[k CA0 (1 - X)]"),
            math("example: k = 0.02 min-1, X = 0.95",
                 "t = (1/0.02) ln(1/0.05) = 50 x 3.00 = 150 min"),
            table([tr("Strengths", "તાકાત"), tr("Weaknesses", "નબળાઈ")],
                  [[tr("one vessel does many products; recipe changes are easy",
                       "એક પાત્ર ઘણા products કરે; recipe બદલવી સહેલી"),
                    tr("labour, cleaning and downtime between batches",
                       "batch વચ્ચે મજૂરી, સફાઈ અને downtime")],
                   [tr("high conversion per pass if the batch is left long enough",
                       "batch પૂરતો સમય રહે તો પ્રતિ pass ઊંચું conversion"),
                    tr("batch-to-batch variation, so quality control is harder",
                       "batch દર batch ફરક, તેથી quality control અઘરું")],
                   [tr("small scale is cheap; good for pharma, dyes and polymerisation",
                       "નાના scale પર સસ્તું; pharma, dyes અને polymerisation માટે સારું"),
                    tr("a runaway exotherm has nowhere to go",
                       "runaway exotherm ને જવાની જગ્યા નથી")]]),
            why("Everything in the batch reactor is a function of time alone, because the mixing "
                "assumption removes position from the problem. That is why the batch equations of "
                "Unit 3 apply to it without any correction.",
                "Batch reactor માં બધું ફક્ત સમયનું વિધેય છે, કારણ કે mixing ની ધારણા સ્થાનને સમસ્યામાંથી "
                "કાઢી નાખે છે. તેથી જ Unit 3 ના batch equations કોઈ સુધારા વગર તેના પર લાગુ પડે."),
            check("With a 30 min turnaround the cycle is 180 min, so 8 batches a day fit in; a "
                  "continuous reactor of the same volume would process the same material in 150 min "
                  "of steady running but cannot be cleaned between products.",
                  "30 min turnaround સાથે cycle 180 min છે, તેથી દિવસમાં 8 batch બેસે; એ જ volume નો "
                  "continuous reactor એ જ material 150 min સ્થિર રનમાં પ્રક્રિયા કરે પણ products વચ્ચે "
                  "સાફ ન થઈ શકે."),
            pit("Sizing a batch reactor from the reaction time alone. The vessel must also hold the "
                "fouling allowance, the freeboard for foam, and the time lost in filling, heating "
                "and emptying.",
                "ફક્ત reaction time પરથી batch reactor નું size કરવું. પાત્રમાં fouling માટે જગ્યા, "
                "foam માટે freeboard, અને ભરવા-ગરમ કરવા-ખાલી કરવામાં જતો સમય પણ ગણવો પડે."),
            diagram="u4_batch",
            syllabus_item="4.2",
        ),
        card(
            "The semi-batch reactor: construction and working",
            "Semi-batch reactor: રચના અને કાર્યપદ્ધતિ",
            p("A semi-batch reactor is a batch vessel with one reactant fed in during the run. "
              "There is no outlet, so the volume grows while the reaction proceeds.",
              "Semi-batch reactor એ batch પાત્ર છે જેમાં રન દરમિયાન એક reactant ઉમેરાતો રહે છે. "
              "Outlet નથી, તેથી પ્રક્રિયા ચાલે તેમ volume વધે છે."),
            parts(("Feed tank and feed pump - deliver the second reactant at a set rate.",
                   "Feed tank અને feed pump - બીજો reactant નક્કી rate પર પહોંચાડે."),
                  ("Control valve and flow meter - the feed rate is the operating variable.",
                   "Control valve અને flow meter - feed rate એ ઓપરેટિંગ ચલ છે."),
                  ("Dip tube - puts the feed below the liquid surface so it mixes at once and does "
                   "not flash off.", "Dip tube - feed ને પ્રવાહીની સપાટી નીચે મૂકે, જેથી તે તરત મિક્સ "
                   "થાય અને ઊડી ન જાય."),
                  ("Agitator and baffles - the same duty as in a batch vessel, but now against a "
                   "rising level.", "Agitator અને baffles - batch પાત્ર જેવું જ કામ, પણ હવે વધતી "
                   "સપાટી સામે."),
                  ("Jacket - removes the heat of a reaction that is deliberately fast.",
                   "Jacket - જાણી જોઈને ઝડપી રાખેલી પ્રક્રિયાની heat કાઢે."),
                  ("Level and temperature instruments - the level tells the operator how much has "
                   "been dosed.", "Level અને temperature instruments - level કહે કે કેટલું dose "
                   "થઈ ગયું.")),
            working(("Charge reactant A (often with a solvent) and bring it to temperature.",
                     "Reactant A (ઘણી વાર solvent સાથે) charge કરો અને temperature પર લાવો."),
                    ("Start the agitator, then open the feed of B at the chosen rate - the two start "
                     "together so no slug of B ever sits in the vessel.",
                     "Agitator ચાલુ કરો, પછી B નો feed પસંદ કરેલા rate પર ખોલો - બંને સાથે શરૂ થાય "
                     "જેથી B નો ગઠ્ઠો પાત્રમાં કદી ન રહે."),
                    ("B reacts as it arrives, so its concentration stays low and the heat is spread "
                     "over the whole dosing time.", "B આવતાં જ પ્રક્રિયા કરે, તેથી તેનું "
                     "concentration નીચું રહે અને heat આખા dosing સમય પર વહેંચાય."),
                    ("Stop the feed when the calculated amount is in; let the batch finish reacting "
                     "(the cook-out).", "ગણેલી માત્રા આવી જાય ત્યારે feed બંધ કરો; batch ને પૂરી "
                     "પ્રક્રિયા કરવા દો (cook-out)."),
                    ("Cool, discharge and clean as for a batch.", "ઠંડું કરો, ખાલી કરો અને batch ની જેમ "
                     "સાફ કરો.")),
            h4("The mole balance that makes it different", "જે તેને અલગ બનાવે તે mole balance"),
            derive("for the fed reactant B: accumulation = in - reaction",
                   "dnB/dt = FB0 - (-rB) V",
                   "for the reactant already in the vessel: dnA/dt = -(-rA) V",
                   "volume grows: dV/dt = FB0/CB0  (if the feed is a pure liquid)",
                   "the two balances must be solved together - there is no closed form for a general law"),
            math("special case, B fed into a large excess of A:",
                 "A is nearly constant, so -rB = k' CB with k' = k CA",
                 "CB = (FB0/(k' V)) (1 - exp(-k' t))  -> a plateau, not a decay"),
            table([tr("Why feed instead of charging", "ચાર્જ કરવાને બદલે feed કેમ"),
                    tr("Where it is used", "ક્યાં વપરાય")],
                  [[tr("a fast exotherm is spread over time, so the jacket can cope",
                       "ઝડપી exotherm સમય પર વહેંચાય, તેથી jacket સંભાળી શકે"),
                    tr("nitration, chlorination, sulphonation", "nitration, chlorination, sulphonation")],
                   [tr("the fed reactant stays dilute, which favours the wanted product",
                       "ઉમેરાતો reactant પાતળો રહે, જે ઇચ્છિત product ને ફાયદો આપે"),
                    tr("polymerisation (monomer fed into the initiator)",
                       "polymerisation (monomer ને initiator માં ફીડ)")],
                   [tr("gas-liquid reactions: the gas is sparged in as the second reactant",
                       "gas-liquid પ્રક્રિયા: gas ને બીજા reactant તરીકે sparge કરાય"),
                    tr("hydrogenation, oxidation, fermentation feeds",
                       "hydrogenation, oxidation, fermentation feed")]]),
            why("Semi-batch is the standard answer to a reaction that is too fast to charge and too "
                "exothermic to run in one go: the feed rate becomes the handle on both the rate and "
                "the heat release.",
                "Semi-batch એ એવી પ્રક્રિયાનો પ્રમાણભૂત જવાબ છે જે charge કરવા માટે ખૂબ ઝડપી અને એક "
                "વારમાં ચલાવવા માટે ખૂબ exothermic છે: feed rate જ rate અને heat release બંનેનું "
                "હેન્ડલ બની જાય."),
            check("If the feed stops, the reaction slows within one mixing time - the vessel cannot "
                  "hold a large inventory of the unstable reactant. That is the safety argument in "
                  "one sentence.",
                  "Feed અટકે તો પ્રક્રિયા એક mixing time માં ધીમી પડે - પાત્ર અસ્થિર reactant નો મોટો "
                  "ભંડાર રાખી શકતું નથી. એ જ એક વાક્યમાં સલામતીનો દલીલ છે."),
            pit("Starting the feed before the agitator. The first litres of B then land in a still "
                "vessel and react as a local slug - the classic cause of a runaway in a semi-batch "
                "plant.",
                "Agitator પહેલાં feed ખોલવો. ત્યારે B ના પહેલા લિટર સ્થિર પાત્રમાં પડે અને સ્થાનિક "
                "ગઠ્ઠા તરીકે પ્રક્રિયા કરે - semi-batch plant માં runaway નું પ્રમાણભૂત કારણ."),
            diagram="u4_semibatch",
            syllabus_item="4.2",
        ),
    ],
})
