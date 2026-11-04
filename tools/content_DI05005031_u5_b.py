"""DI05005031 Unit 5, part B: sections 5.3 and 5.4 - the two flow reactors and the choice between them."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from subject_DI05005031 import tr  # noqa: E402
from content_DI05005031_lib import (p, h4, table, math, eq, why, check, pit, derive,
                                    card)  # noqa: E402

NOTES_B = []

NOTES_B.append({
    "title": tr("5.3 The steady state mixed flow reactor (CSTR)",
                "5.3 સ્થિર સ્થિતિનો mixed flow reactor (CSTR)"),
    "items": [
        card(
            "The CSTR design equation and its rectangle",
            "CSTR નું design equation અને તેનો લંબચોરસ",
            p("In a CSTR the feed and the product leave continuously and the stirrer keeps the "
              "contents uniform, so the reactor has one composition - the outlet composition - at "
              "every point and at every instant. That single fact collapses the mole balance into "
              "one algebraic line, and the line can be read straight off a graph.",
              "CSTR માં feed અને product સતત નીકળે છે અને stirrer અંદરનું સરખું રાખે છે, તેથી "
              "reactor ની રચના એક જ - outlet ની રચના - દરેક જગ્યાએ અને દરેક ક્ષણે. એ એક જ વાત "
              "mole balance ને એક બીજગણિતીય લીટીમાં લાવે, અને એ લીટી graph પરથી સીધી વંચાય."),
            derive("steady state: in - out - reaction = 0",
                   "FA0 - FA - (-rA) V = 0",
                   "with FA = FA0 (1 - X):  V = FA0 X / (-rA)exit",
                   "divide by the feed rate:  tau = V/v0 = CA0 X / (-rA)exit",
                   "first order:  tau = X/[k (1 - X)]",),
            h4("The graphical form", "ગ્રાફિકલ સ્વરૂપ"),
            math("plot 1/(-rA) against X:  V/FA0 = X x [1/(-rA) at the exit]",
                 "that is a rectangle of width X and height 1/(-rA)exit",
                 "first order at X = 0.8: height 5, area 4 = k tau"),
            eq("V = FA0 X/(-rA)exit", "tau = V/v0 = CA0 X/(-rA)exit",
               "first order: k tau = X/(1 - X)"),
            why("The balance has no accumulation term because the reactor is at steady state, and no "
                "integral because there is only one composition to integrate over. What is left is "
                "the rate at the outlet multiplied by the volume - the slowest rate in the system "
                "held constant over the whole vessel.",
                "Balance માં accumulation નો ભાગ નથી કારણ કે reactor steady state માં છે, અને "
                "integral નથી કારણ કે integrate કરવા એક જ રચના છે. જે બાકી રહે તે outlet નો rate ગુણ્યા "
                "volume - system નો સૌથી ધીમો rate આખા પાત્ર પર અચળ."),
            check("Put the answer back through the balance: V = FA0 X/(-rA) = v0 CA0 X/(k CA0 (1-X)) = "
                  "v0 X/[k(1-X)] = v0 tau. If it does not return v0 tau, the exit rate was taken at "
                  "the wrong conversion.",
                  "જવાબ balance માં પાછો મૂકો: V = FA0 X/(-rA) = v0 CA0 X/(k CA0 (1-X)) = "
                  "v0 X/[k(1-X)] = v0 tau. જો v0 tau ન આવે તો exit rate ખોટા conversion પર લેવાયો છે."),
            pit("Treating a stirred tank as a CSTR because it has a stirrer. A CSTR needs a mixing "
                "time much shorter than the space time, a feed that enters below the liquid level "
                "and an overflow that does not short-circuit to the inlet - otherwise the real "
                "vessel behaves like a poor PFR-CSTR mixture and converts less.",
                "Stirrer હોય તો પાત્રને CSTR ગણવું. CSTR ને space time કરતાં ઘણો ટૂંકો mixing time, "
                "પ્રવાહીની સપાટી નીચે પ્રવેશતો feed અને inlet સુધી ટૂંકો રસ્તો ન કરતો overflow જોઈએ - "
                "નહીં તો સાચું પાત્ર નબળા PFR-CSTR મિશ્રણ જેવું વર્તે અને ઓછું convert કરે."),
            diagram="u5_cstr",
            syllabus_item="5.3",
        ),
        card(
            "Two CSTRs in series: the staircase",
            "Series માં બે CSTR: સીડી આકાર",
            p("A single CSTR has to work at the outlet concentration, which is its own worst "
              "handicap. Split the same volume into two tanks in series and the first tank works "
              "between the feed and the mid-point composition, so it converts faster; only the last "
              "tank pays the full penalty. On the 1/(-rA) plot the train becomes a staircase.",
              "એક જ CSTR ને outlet concentration પર કામ કરવું પડે, જે તેની પોતાની સૌથી મોટી "
              "મર્યાદા છે. એ જ volume ને series માં બે ટાંકીમાં વહેંચો તો પહેલી ટાંકી feed અને વચ્ચેની "
              "રચના વચ્ચે કામ કરે, તેથી ઝડપથી convert કરે; પૂરી સજા ફક્ત છેલ્લી ટાંકી ભોગવે. "
              "1/(-rA) ના ગ્રાફ પર શ્રેણી સીડી બની જાય."),
            derive("tank 1: CA1 = CA0/(1 + k tau1)   ->   1 - X1 = 1/(1 + k tau1)",
                   "tank 2: CA2 = CA1/(1 + k tau2)   ->   1 - X2 = 1/[(1 + k tau1)(1 + k tau2)]",
                   "n equal tanks, tau each:  1 - X = 1/(1 + k tau/n)^n",
                   "as n grows at fixed total volume the train approaches a PFR",
                   "two equal tanks at X = 0.8: 1 + k tau = sqrt(5) = 2.236, k tau = 1.236 each"),
            eq("1 - X = 1/(1 + k tau/n)^n", "two equal tanks: k tau = (1 - X)^(-1/2) - 1 = 1.236"),
            math("one CSTR: k tau = X/(1 - X) = 4.0   ->   V = 115 m3",
                 "two CSTRs: 2 x 1.236 = 2.47 in total  ->   V = 71 m3",
                 "one PFR: k tau = ln(5) = 1.61        ->   V = 46 m3"),
            why("Each tank is a fresh CSTR that starts from the composition the previous tank "
                "delivered, so the average rate over the train is higher than the rate at the final "
                "outlet. The improvement is largest for the first extra tank and falls quickly "
                "afterwards, which is why plants stop at two or three.",
                "દરેક ટાંકી નવો CSTR છે જે આગલી ટાંકીએ આપેલી રચનાથી શરૂ થાય, તેથી શ્રેણી પર સરેરાશ "
                "rate છેલ્લા outlet ના rate કરતાં ઊંચો રહે. સુધારો પહેલી વધારાની ટાંકી માટે સૌથી મોટો "
                "હોય અને પછી ઝડપથી ઘટે, તેથી plants બે કે ત્રણ પર અટકે."),
            check("Multiply the two factors back: (1 + 1.236) squared = 5.0, so 1 - X = 1/5 = 0.2 and "
                  "X = 0.80 exactly. Any staircase whose rectangle areas do not add up to the same "
                  "k tau total is drawn wrong.",
                  "બે અવયવ પાછા ગુણો: (1 + 1.236) નો વર્ગ = 5.0, તેથી 1 - X = 1/5 = 0.2 અને X = 0.80 "
                  "બરાબર. જે સીડીના લંબચોરસનું ક્ષેત્રફળ કુલ k tau જેટલું ન થાય તે ખોટી દોરાયેલી છે."),
            pit("Splitting the volume evenly when the tanks are not identical, or forgetting that "
                "the second tank's feed is already partly converted. Size each tank on its own inlet "
                "composition; equal tanks are a convenience, not a rule.",
                "ટાંકીઓ એકસરખી ન હોય તો પણ volume સરખું વહેંચવું, કે બીજી ટાંકીનો feed અગાઉથી "
                "અંશતઃ convert થયેલો છે તે ભૂલવું. દરેક ટાંકી તેના પોતાના inlet composition પર માપો; "
                "સરખી ટાંકી સગવડ છે, નિયમ નહીં."),
            diagram="u5_series",
            syllabus_item="5.3",
        ),
    ],
})

NOTES_B.append({
    "title": tr("5.4 The steady state plug flow reactor (PFR)",
                "5.4 સ્થિર સ્થિતિનો plug flow reactor (PFR)"),
    "items": [
        card(
            "The PFR design equation and its area",
            "PFR નું design equation અને તેનું ક્ષેત્રફળ",
            p("In a PFR the fluid moves as plugs with no mixing along the flow, so the composition "
              "changes continuously from the inlet to the outlet. The balance is written on a slice "
              "of volume dV and integrated along the tube, which on the 1/(-rA) plot is the area "
              "under the curve up to the outlet conversion.",
              "PFR માં પ્રવાહી plug તરીકે આગળ વધે અને flow સાથે મિક્ષ થતું નથી, તેથી રચના inlet થી "
              "outlet સુધી સતત બદલાય. Balance volume ના નાના ટુકડા dV પર લખાય અને નળી પર integrate "
              "થાય, જે 1/(-rA) ના ગ્રાફ પર outlet conversion સુધીના વક્ર નીચેનું ક્ષેત્રફળ છે."),
            derive("slice of volume dV: FA(V) - FA(V + dV) - (-rA) dV = 0",
                   "so dFA/dV = -(-rA), and with FA = FA0 (1 - X):",
                   "FA0 dX/dV = -rA    ->    V = FA0 x integral from 0 to X of dX/(-rA)",
                   "first order:  V = v0 ln[1/(1 - X)]/k, i.e. tau = ln[1/(1 - X)]/k",
                   "second order, CA0 = CB0:  tau = X/[k CA0 (1 - X)]"),
            math("plot 1/(-rA) against X:  V/FA0 = area under the curve from 0 to X",
                 "first order at X = 0.8: area = ln(5) = 1.61 = k tau",
                 "against 4.0 for the CSTR: 2.5 times less volume"),
            eq("V = FA0 x integral dX/(-rA)", "tau = CA0 x integral dX/(-rA)",
               "first order: k tau = ln[1/(1 - X)]"),
            why("The reactant spends the whole residence time at a concentration between CA0 and "
                "CA0(1 - X), while a CSTR spends it all at CA0(1 - X). For a positive order the "
                "average rate is therefore higher in the PFR, and the higher the conversion asked "
                "for, the bigger the advantage.",
                "Reactant આખો residence time CA0 અને CA0(1 - X) વચ્ચેના concentration પર રહે, જ્યારે "
                "CSTR આખો સમય CA0(1 - X) પર રહે. Positive order માટે તેથી PFR માં સરેરાશ rate ઊંચો "
                "રહે, અને conversion જેટલું ઊંચું માંગવામાં આવે તેટલો ફાયદો મોટો."),
            check("Differentiate the answer to get the balance back: d/dV of [v0 ln(1/(1-X))/k] "
                  "gives FA0 dX/dV = k CA0 (1- X), which is the rate law. A PFR answer that does not "
                  "differentiate back to -rA is wrong.",
                  "જવાબનું વિકલન કરી balance પાછું મેળવો: [v0 ln(1/(1-X))/k] નું d/dV એટલે "
                  "FA0 dX/dV = k CA0 (1-X), જે rate law છે. જે PFR જવાબનું વિકલન કરી -rA ન આવે તે "
                  "ખોટો છે."),
            pit("Calling any tube a PFR. Plug flow needs a turbulent or well-distributed velocity "
                "profile and enough length for the radial mixing to average out - in practice L/D of "
                "the order of 50 or more, or a packed tube. A short wide pipe with a laminar profile "
                "has a spread of residence times and converts less than the integral predicts.",
                "કોઈપણ નળીને PFR કહેવી. Plug flow માટે turbulent કે સારી રીતે વહેંચાયેલો velocity "
                "profile અને radial mixing સરખું થવા પૂરતી લંબાઈ જોઈએ - વ્યવહારમાં L/D લગભગ 50 કે "
                "તેથી વધુ, કે packed નળી. ટૂંકી પહોળી નળીમાં laminar profile હોય તો residence time નો "
                "ફેલાવો થાય અને integral કહે તેના કરતાં ઓછું convert થાય."),
            diagram="u5_pfr",
            syllabus_item="5.4",
        ),
        card(
            "Choosing a reactor: same duty, different volume",
            "Reactor પસંદગી: એ જ કામ, જુદું volume",
            p("A design engineer is asked for a conversion, not for a reactor. The same duty can be "
              "met by one tank, a train of tanks or one tube, and the volumes differ by a factor of "
              "two or three - which is why the choice is made on cost, on the reaction's quirks, and "
              "on how the plant is operated, not on the design equation alone.",
              "Design engineer ને reactor નહીં, conversion માંગવામાં આવે છે. એ જ કામ એક ટાંકી, ટાંકીઓની "
              "શ્રેણી કે એક નળીથી થઈ શકે, અને volumes બે-ત્રણ ગણા જુદા પડે - તેથી જ પસંદગી ખર્ચ, "
              "પ્રક્રિયાની વિચિત્રતાઓ અને plant કેવી રીતે ચાલે તેના પર થાય, ફક્ત design equation પર "
              "નહીં."),
            table([tr("Reactor", "Reactor"), tr("k tau at 80 %", "80 % પર k tau"),
                   tr("Volume", "Volume"), tr("Choose it when", "ક્યારે લેવો")],
                  [[tr("one CSTR", "એક CSTR"), tr("4.00", "4.00"), tr("115 m3", "115 m3"),
                    tr("solids or gas must be handled, heat removal, easy cleaning",
                       "solids કે gas સંભાળવાના હોય, heat કાઢવો હોય, સહેલી સફાઈ")],
                   [tr("two CSTRs", "બે CSTR"), tr("2 x 1.236", "2 x 1.236"), tr("71 m3", "71 m3"),
                    tr("a single tank is too tall, or the duty grows in stages",
                       "એક ટાંકી બહુ ઊંચી થાય, કે કામ તબક્કે તબક્કે વધે")],
                   [tr("one PFR", "એક PFR"), tr("1.61", "1.61"), tr("46 m3", "46 m3"),
                    tr("gas phase, high conversion, high temperature, large scale",
                       "gas phase, ઊંચું conversion, ઊંચું temperature, મોટું scale")]]),
            math("first order:  CSTR k tau = X/(1 - X),   PFR k tau = ln[1/(1 - X)]",
                 "X = 0.80: 4.00 against 1.61  ->  ratio 2.5",
                 "X = 0.90: 9.00 against 2.30  ->  ratio 3.9",
                 "X = 0.99: 99.0 against 4.61  ->  ratio 21"),
            eq("volume ratio CSTR/PFR = [X/(1 - X)] / ln[1/(1 - X)]"),
            why("The gap grows with conversion because the CSTR's rate is fixed at the exit, and the "
                "exit concentration falls fastest at high conversion while the PFR keeps meeting "
                "high concentrations early on. At low conversion both reactors see nearly the feed "
                "composition and the volumes are almost equal.",
                "Conversion સાથે gap વધે કારણ કે CSTR નો rate exit પર અટકે છે, અને ઊંચા conversion પર "
                "exit concentration સૌથી ઝડપથી ઘટે જ્યારે PFR શરૂઆતમાં ઊંચા concentration મળે. "
                "નીચા conversion પર બંને reactor લગભગ feed રચના જુએ અને volumes લગભગ સરખા થાય."),
            check("Compare the numbers with the chart: 115, 71 and 46 m3 for the same duty, and "
                  "71/46 = 1.5 while 115/46 = 2.5. The chart is plotted from those three numbers, so "
                  "a bar that does not scale the same way is a plotting error, not a new result.",
                  "આંકડાને ચાર્ટ સાથે સરખાવો: એ જ કામ માટે 115, 71 અને 46 m3, અને 71/46 = 1.5 જ્યારે "
                  "115/46 = 2.5. ચાર્ટ એ જ ત્રણ આંકડા પરથી દોરાયો છે, તેથી જે બાર એ જ પ્રમાણમાં ન "
                  "બેસે તે દોરવાની ભૂલ છે, નવો પરિણામ નહીં."),
            pit("Choosing the smallest volume and ignoring what the reaction needs. A PFR cannot be "
                "emptied to change a deactivated catalyst, cannot take a slurry, and cannot be "
                "cleaned in place easily; a CSTR can do all three. Volume is one line of the "
                "specification, not the whole of it.",
                "સૌથી નાનું volume પસંદ કરી પ્રક્રિયાને શું જોઈએ તે ભૂલવું. PFR ને નિષ્ક્રિય થયેલો "
                "catalyst બદલવા ખાલી કરી શકાય નહીં, slurry લઈ શકાય નહીં, અને સહેલાઈથી in place સાફ "
                "થઈ શકે નહીં; CSTR ત્રણેય કરી શકે. Volume specification ની એક લીટી છે, આખી નહીં."),
            diagram="u5_bars",
            syllabus_item="5.4",
        ),
    ],
})
