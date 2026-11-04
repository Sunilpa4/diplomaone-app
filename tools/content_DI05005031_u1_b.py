"""DI05005031 Unit 1, part B: sections 1.4 (molecularity and order) and 1.5 (biochemical, MM)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from subject_DI05005031 import tr  # noqa: E402
from content_DI05005031_lib import (p, h4, ul, table, math, eq, why, check, pit, derive,
                                    card)  # noqa: E402

NOTES_B = []

# ---------------------------------------------------------------- 1.4 molecularity and order
NOTES_B.append({
    "title": tr("1.4 Molecularity, order and the six-way classification",
                "1.4 Molecularity, order અને છ પ્રકારનું વર્ગીકરણ"),
    "items": [
        card(
            "Molecularity is counted, order is measured",
            "Molecularity ગણાય છે, order માપવો પડે છે",
            h4("Molecularity", "Molecularity"),
            p("<b>Molecularity</b> is the number of molecules that collide in one <i>elementary</i> "
              "step: one molecule breaking up is unimolecular, two molecules meeting is bimolecular, "
              "three meeting at once is termolecular. It is a small whole number, it belongs to a "
              "single step, and it is fixed by writing the mechanism - not by measuring anything.",
              "<b>Molecularity</b> એ એક <i>elementary</i> step માં અથડાતા molecules ની સંખ્યા છે: "
              "એક molecule તૂટે તે unimolecular, બે મળે તે bimolecular, ત્રણ એકસાથે મળે તે "
              "termolecular. તે નાની પૂર્ણ સંખ્યા છે, એક જ step ની છે, અને mechanism લખવાથી નક્કી "
              "થાય છે - માપીને નહીં."),
            h4("Order", "Order"),
            p("<b>Order</b> is the power to which a concentration is raised in the rate law that fits "
              "the experiment. It can be 0, 1, 2, 1.5 or even negative, it has no meaning for a "
              "mixture of steps, and it is found by the methods of Unit 3.",
              "<b>Order</b> એ rate law માં concentration નો ઘાત છે, જે પ્રયોગ સાથે મેળ ખાય તે "
              "રીતે નક્કી થાય. તે 0, 1, 2, 1.5 અથવા ઋણાત્મક પણ હોઈ શકે, steps ના મિશ્રણ માટે તેનો "
              "અર્થ નથી, અને તે Unit 3 ની methods થી શોધાય છે."),
            table(
                [tr("Point", "મુદ્દો"), tr("Molecularity", "Molecularity"), tr("Order", "Order")],
                [[tr("From", "ક્યાંથી"), tr("the mechanism, one step", "mechanism, એક step"),
                  tr("the experiment, the rate law", "પ્રયોગ, rate law")],
                 [tr("Values", "મૂલ્યો"), tr("1, 2, 3 (whole numbers)", "1, 2, 3 (પૂર્ણ સંખ્યા)"),
                  tr("0, 0.5, 1, 1.5, 2, -1 ...", "0, 0.5, 1, 1.5, 2, -1 ...")],
                 [tr("For a multi-step reaction", "બહુ-step પ્રક્રિયા માટે"),
                  tr("only for the single step", "ફક્ત એક step માટે"),
                  tr("for the overall rate law", "આખા rate law માટે")],
                 [tr("Can be fractional?", "અપૂર્ણાંક હોઈ શકે?"), tr("no", "ના"), tr("yes", "હા")]]),
            h4("Worked reading of three rate laws", "ત્રણ rate laws નું ઉકેલાયેલું વાંચન"),
            math("2A + B -> products   (elementary)",
                 "  r = k CA^2 CB      order 3, molecularity 3",
                 "H2 + Br2 -> 2 HBr   (chain mechanism)",
                 "  r = k CH2 CBr2^1.5 / (CBr2 + k' CHBr)",
                 "  order 1 in H2, 1.5 in Br2 (not molecularity)",
                 "sugar + H2O -> 2 glucose  (water in excess)",
                 "  r = k' sugar       pseudo first order"),
            p("The third case is the everyday laboratory one: water is in such large excess that its "
              "concentration hardly changes, so a second order law looks first order. The constant "
              "you calculate is then a <b>pseudo first order</b> constant, and it changes if you "
              "change the amount of water.",
              "ત્રીજો કિસ્સો રોજિંદો laboratory કિસ્સો છે: પાણી એટલા વધારામાં છે કે તેનું "
              "concentration લગભગ બદલાતું નથી, તેથી second order law first order જેવો દેખાય છે. "
              "ત્યારે ગણેલો constant <b>pseudo first order</b> constant છે, અને પાણીનો જથ્થો બદલો તો "
              "તે બદલાઈ જાય."),
            why("Only an elementary reaction has order equal to molecularity. Whenever they disagree, "
                "the disagreement is proof that the reaction runs through more than one step.",
                "ફક્ત elementary પ્રક્રિયામાં order અને molecularity સરખા હોય છે. જ્યાં તેઓ ન મળે "
                "ત્યાં તે અસંમતિ એ પુરાવો છે કે પ્રક્રિયા એક કરતાં વધુ step માંથી પસાર થાય છે."),
            pit("Writing 'molecularity 1.5' for a rate law of order 1.5. A collision of one and a "
                "half molecules does not exist; such an order always comes from a chain mechanism.",
                "Order 1.5 વાળા rate law માટે 'molecularity 1.5' લખવું. દોઢ molecule ની અથડામણ "
                "હોતી નથી; એવો order હંમેશા chain mechanism માંથી આવે છે."),
            diagram="u1_tree",
            syllabus_item="1.2b, 1.2d, 1.2f",
        ),
    ],
})

# ---------------------------------------------------------------- 1.5 biochemical
NOTES_B.append({
    "title": tr("1.5 Biochemical reactions and the Michaelis-Menten derivation",
                "1.5 Biochemical પ્રક્રિયાઓ અને Michaelis-Menten derivation"),
    "items": [
        card(
            "An enzyme is a catalyst with a saturable seat",
            "Enzyme એ saturable seat વાળો catalyst છે",
            h4("What is different about a biochemical reaction",
               "Biochemical પ્રક્રિયામાં શું જુદું છે"),
            p("A biochemical reaction is catalysed by an <b>enzyme</b>, a large protein molecule with "
              "a small active site. The substrate must first sit in that site, then be converted, "
              "then leave. Two consequences matter for the reactor: the enzyme works at mild "
              "temperature and pH, and there is only a fixed number of seats, so the rate "
              "<b>saturates</b> instead of rising with concentration for ever.",
              "Biochemical પ્રક્રિયા <b>enzyme</b> થી catalysed થાય છે - નાનું active site ધરાવતું "
              "મોટું protein molecule. Substrate પહેલાં તે site માં બેસે, પછી convert થાય, પછી "
              "નીકળે. Reactor માટે બે બાબતો મહત્વની છે: enzyme હળવા temperature અને pH પર કામ કરે છે, "
              "અને seats ની સંખ્યા નિશ્ચિત હોવાથી rate વધતા concentration સાથે અનંત વધ્યા વિના "
              "<b>saturate</b> થાય છે."),
            h4("Derivation of the Michaelis-Menten rate", "Michaelis-Menten rate નું derivation"),
            p("Mechanism: the enzyme E binds the substrate S reversibly, and the complex ES breaks "
              "down into product P and free enzyme.",
              "Mechanism: enzyme E substrate S ને reversible રીતે બાંધે છે, અને complex ES તૂટીને "
              "product P તથા મુક્ત enzyme આપે છે."),
            math("E + S  --k1-->   ES        binding",
                 "ES     --k-1-->  E + S     unbinding",
                 "ES     --k2-->   E + P     reaction"),
            p("<b>Assumption (steady state):</b> after a short start-up the complex ES is used as "
              "fast as it is formed, so its concentration stays constant.",
              "<b>ધારણા (steady state):</b> થોડા સમય પછી complex ES જેટલું બને એટલું જ વપરાય છે, "
              "તેથી તેનું concentration અચળ રહે છે."),
            derive("d[ES]/dt = k1 [E][S] - k-1 [ES] - k2 [ES] = 0",
                   "so   [ES] = k1 [E][S] / (k-1 + k2)",
                   "the enzyme is conserved:  [E0] = [E] + [ES]",
                   "put [E] = [E0] - [ES] in the line above:",
                   "[ES] = k1 ([E0] - [ES]) [S] / (k-1 + k2)",
                   "[ES] (k-1 + k2 + k1 [S]) = k1 [E0] [S]",
                   "define  Km = (k-1 + k2) / k1",
                   "and the rate is  v = k2 [ES]",
                   "v = k2 [E0] [S] / (Km + [S])"),
            eq("v = Vmax [S] / (Km + [S]),  Vmax = k2 [E0],  Km = (k-1 + k2)/k1"),
            h4("What the three numbers mean", "ત્રણ આંકડાનો અર્થ"),
            ul(("<b>Vmax</b> is reached when every enzyme molecule holds a substrate: it is set by "
                "how much enzyme is charged, not by the substrate.",
                "<b>Vmax</b> ત્યારે મળે જ્યારે દરેક enzyme molecule substrate પકડીને બેઠું હોય: તે "
                "કેટલું enzyme ભરેલું છે તેના પર રહે, substrate પર નહીં."),
               ("<b>Km</b> is the substrate concentration at which the rate is exactly Vmax/2. A "
                "small Km means the enzyme grips the substrate tightly and saturates early.",
                "<b>Km</b> એ substrate concentration છે જ્યાં rate બરાબર Vmax/2 થાય. નાનું Km એટલે "
                "enzyme substrate ને મજબૂત પકડે અને વહેલું saturate થાય."),
               ("<b>The two limits</b>: far below Km the rate is (Vmax/Km)[S], first order in "
                "substrate; far above Km the rate is Vmax, zero order in substrate.",
                "<b>બે મર્યાદા</b>: Km કરતાં ઘણું નીચે rate (Vmax/Km)[S], substrate માં first "
                "order; Km કરતાં ઘણું ઉપર rate Vmax, substrate માં zero order."),
               ("<b>Linear form for the laboratory</b> (Lineweaver-Burk): plot 1/v against 1/[S]; "
                "the intercept is 1/Vmax and the slope is Km/Vmax.",
                "<b>Laboratory માટે linear સ્વરૂપ</b> (Lineweaver-Burk): 1/v ને 1/[S] સામે દોરો; "
                "intercept 1/Vmax અને slope Km/Vmax મળે.")),
            math("1/v = (Km/Vmax)(1/[S]) + 1/Vmax"),
            p("Reactor consequence: an enzyme reactor is best run in the <b>saturating</b> range, where "
              "the rate is zero order and therefore the same everywhere in the vessel - a CSTR and a "
              "PFR then need the same volume (Unit 5). Below Km the rate is first order and the plug "
              "flow reactor wins.",
              "Reactor પર અસર: enzyme reactor <b>saturating</b> શ્રેણીમાં ચલાવવો સારો, જ્યાં rate "
              "zero order હોવાથી vessel માં દરેક જગ્યાએ સરખો રહે - ત્યારે CSTR અને PFR ને સરખું જ "
              "volume જોઈએ (Unit 5). Km નીચે rate first order હોય છે અને plug flow reactor જીતે છે."),
            why("The saturation comes from geometry, not from chemistry: a fixed number of active "
                "sites can hold only a fixed number of substrate molecules, so once every site is "
                "busy, more substrate cannot give more product.",
                "Saturation chemistry થી નહીં, geometry થી આવે છે: નિશ્ચિત active sites નિશ્ચિત "
                "સંખ્યાના substrate molecules જ પકડી શકે, તેથી દરેક site ભરાઈ જાય પછી વધુ "
                "substrate થી વધુ product ન મળે."),
            pit("Treating Km as the concentration at which the reaction stops. It is the concentration "
                "at half the maximum rate; above Km the reaction still runs, just not any faster.",
                "Km ને એ concentration ગણવું જ્યાં પ્રક્રિયા અટકે. તે અડધા કમ્મમ rate વાળું "
                "concentration છે; Km ઉપર પણ પ્રક્રિયા ચાલે છે, ફક્ત વધુ ઝડપી નહીં."),
            diagram="u1_mm",
            syllabus_item="1.3",
        ),
    ],
})
