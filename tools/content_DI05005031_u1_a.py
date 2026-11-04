"""DI05005031 Unit 1, part A: sections 1.1, 1.2 and 1.3 (scope, classification, direction and heat).

Bilingual (English + Gujarati). Each card is written as
    card(heading_en, heading_gu, <parts...>, diagram=..., syllabus_item=...)
so the heading pair is followed by a comma, never by a closing bracket.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from subject_DI05005031 import tr  # noqa: E402
from content_DI05005031_lib import (p, h4, ul, table, math, eq, why, check, pit, derive,
                                    card)  # noqa: E402

NOTES_A = []

# ---------------------------------------------------------------- 1.1 scope
NOTES_A.append({
    "title": tr("1.1 What chemical reaction engineering is for",
                "1.1 Chemical reaction engineering શેના માટે છે"),
    "items": [
        card(
            "The reactor is where the chemistry becomes a product",
            "રિએક્ટર એ જગ્યા છે જ્યાં chemistry નું product બને છે",
            h4("Definition", "વ્યાખ્યા"),
            p("Chemical reaction engineering (CRE) is the branch that turns a reaction written in a "
              "laboratory flask into a vessel that runs day after day in a plant. It answers four "
              "questions: <b>how fast</b> the reaction goes (kinetics), <b>how far</b> it can go "
              "(thermodynamics), <b>how the heat is added or removed</b> (energy balance) and "
              "<b>what the vessel must look like</b> so that the feed reaches the catalyst and the "
              "product leaves (fluid mechanics and mass transfer).",
              "Chemical reaction engineering (CRE) એ શાખા છે જે laboratory ના flask માં લખેલી "
              "પ્રક્રિયાને plant માં રોજ ચાલતા vessel માં ફેરવે છે. તે ચાર પ્રશ્નોના જવાબ આપે છે: "
              "પ્રક્રિયા <b>કેટલી ઝડપથી</b> થાય (kinetics), <b>કેટલી દૂર સુધી</b> જઈ શકે "
              "(thermodynamics), <b>heat કેવી રીતે આપવું કે કાઢવું</b> (energy balance) અને "
              "<b>vessel કેવું હોવું જોઈએ</b> જેથી feed catalyst સુધી પહોંચે અને product બહાર "
              "નીકળે (fluid mechanics અને mass transfer)."),
            p("The reactor is the heart of the plant. Everything upstream - storage, pumps, "
              "preheaters, compressors - exists to prepare its feed, and everything downstream - "
              "distillation, evaporation, dryers - exists to clean up what it makes. A 5 % error in "
              "its volume is a 5 % error in the size of the whole plant.",
              "Plant નું હૃદય reactor છે. ઉપરના દરેક ભાગ - storage, pumps, preheaters, compressors - "
              "તેનું feed તૈયાર કરવા માટે છે, અને નીચેના દરેક ભાગ - distillation, evaporation, "
              "dryers - તે જે બનાવે છે તેને સાફ કરવા માટે છે. તેના volume માં 5 % ભૂલ એ આખા plant ના "
              "size માં 5 % ભૂલ છે."),
            h4("The four questions, and the tool that answers each",
               "ચાર પ્રશ્નો અને દરેકનું tool"),
            table(
                [tr("Question", "પ્રશ્ન"), tr("Tool", "Tool"),
                 tr("Symbol in the design", "Design માં symbol")],
                [[tr("How fast does it go?", "કેટલી ઝડપથી થાય?"),
                  tr("rate law and kinetics", "rate law અને kinetics"), "-rA = f(C, T)"],
                 [tr("How far can it go?", "કેટલી દૂર જઈ શકે?"),
                  tr("equilibrium constant", "equilibrium constant"), "K_eq, X_eq"],
                 [tr("How much heat moves?", "કેટલી heat જાય?"),
                  tr("energy balance", "energy balance"), "dH_r, dT_ad"],
                 [tr("What shape and size?", "કેવો આકાર અને size?"),
                  tr("performance equation", "performance equation"), "V, tau, s"]]),
            h4("Derivation: why the rate law decides the size",
               "Derivation: rate law size કેવી રીતે નક્કી કરે છે"),
            p("A plant has to deliver a fixed number of moles per second of product, FP. The vessel "
              "can only deliver what the reaction gives it, so the volume is the throughput divided "
              "by the rate at which the reaction can supply it:",
              "Plant એ પ્રતિ second નિશ્ચિત moles product FP આપવાના હોય છે. Vessel ફક્ત તેટલું જ "
              "આપી શકે જેટલું પ્રક્રિયા આપે, તેથી volume એ throughput ને પ્રક્રિયાના rate વડે ભાગ્યા "
              "પછી મળે:"),
            derive("moles to make per second = FA0 X",
                   "moles the vessel can make = (-rA) V",
                   "set equal:  FA0 X = (-rA) V",
                   "so  V = FA0 X / (-rA)     (batch: t = ...)"),
            eq("V = FA0 X / (-rA)"),
            p("Read the equation twice: the bigger the throughput the bigger the vessel, and the "
              "faster the reaction the smaller it is. A plant making 10 kmol/h at 80 % conversion "
              "with a rate of 0.02 kmol m-3 s-1 needs V = 10 x 0.8 / (0.02 x 3600) = 0.11 m3 - and "
              "the same plant with a rate ten times smaller needs a vessel ten times larger.",
              "સમીકરણ બે વાર વાંચો: throughput જેટલું મોટું તેટલું vessel મોટું, અને પ્રક્રિયા જેટલી "
              "ઝડપી તેટલું vessel નાનું. 80 % conversion પર 10 kmol/h બનાવતા plant ને 0.02 kmol "
              "m-3 s-1 ના rate સાથે V = 10 x 0.8 / (0.02 x 3600) = 0.11 m3 જોઈએ - અને એ જ plant ને "
              "દસ ગણા ઓછા rate સાથે દસ ગણું મોટું vessel જોઈએ."),
            h4("Why a diploma engineer needs it", "Diploma engineer ને તે કેમ જોઈએ"),
            ul(("To select a reactor for a new product instead of copying an old one.",
                 "નવા product માટે જૂનું copy કરવાને બદલે reactor પસંદ કરવા."),
               ("To fix the operating temperature, pressure and conversion that give the cheapest "
                "product.",
                "સૌથી સસ્તું product આપતું operating temperature, pressure અને conversion ઠરાવવા."),
               ("To judge a plant complaint: is the reactor too small, too cold, or badly mixed?",
                "Plant ની ફરિયાદ પરખવા: reactor નાનું છે, ઠંડું છે કે ખોટી રીતે mixed છે?"),
               ("To read a kinetic paper and know whether its numbers can be used at plant scale.",
                "Kinetic paper વાંચીને ખબર પડે કે તેના આંકડા plant scale પર વાપરી શકાય કે નહીં.")),
            why("The reactor sets the size of everything else: the feed rate decides the pump, the "
                "heat duty decides the exchanger, and the conversion decides the recycle. That is why "
                "the reactor is designed first and the rest of the plant is built around it.",
                "Reactor બાકીના બધાનું size નક્કી કરે છે: feed rate pump નક્કી કરે, heat duty "
                "exchanger નક્કી કરે અને conversion recycle નક્કી કરે. તેથી reactor પહેલાં "
                "design થાય અને આખો plant તેની આસપાસ બને છે."),
            pit("Calling CRE 'just kinetics'. Kinetics gives the rate, but the reactor also has to "
                "hold the temperature, keep the phases in contact and let the product out; a correct "
                "rate law in a badly mixed vessel still gives the wrong product.",
                "CRE ને ફક્ત 'kinetics' કહેવું. Kinetics rate આપે છે, પણ reactor એ temperature "
                "રાખવું, phases નો સંપર્ક રાખવો અને product બહાર કાઢવું પણ જોઈએ; ખોટી રીતે mixed "
                "vessel માં સાચું rate law પણ ખોટું product આપે છે."),
            diagram="u1_map",
            syllabus_item="1.1",
        ),
    ],
})

# ---------------------------------------------------------------- 1.2 classification
NOTES_A.append({
    "title": tr("1.2 Classifying reactions: phases and the catalyst",
                "1.2 પ્રક્રિયાઓનું વર્ગીકરણ: phases અને catalyst"),
    "items": [
        card(
            "Homogeneous or heterogeneous - one phase or an interface",
            "Homogeneous કે heterogeneous - એક phase કે interface",
            h4("The test that decides it", "નિર્ણય કરતી કસોટી"),
            p("Look at the reacting mixture, not at the equation. If every reacting species sits in "
              "one phase - all gas, or all liquid, or all dissolved in the same solution - the "
              "reaction is <b>homogeneous</b>. If the reaction has to happen <b>at the boundary</b> "
              "between two phases, it is <b>heterogeneous</b>, and that boundary is the interface.",
              "પ્રક્રિયાનું સમીકરણ નહીં, પ્રક્રિયામાં ભાગ લેતું મિશ્રણ જુઓ. જો બધા reacting "
              "species એક જ phase માં હોય - બધા gas, અથવા બધા liquid, અથવા એક જ દ્રાવણમાં ઓગળેલા - "
              "તો પ્રક્રિયા <b>homogeneous</b> છે. જો પ્રક્રિયા બે phases વચ્ચેની <b>સીમા પર</b> થવી "
              "પડે તો તે <b>heterogeneous</b> છે, અને તે સીમાને interface કહે છે."),
            table(
                [tr("System", "System"), tr("Type", "પ્રકાર"),
                 tr("What the rate must be based on", "Rate કયા આધાર પર લખવો")],
                [[tr("NaOH + ethyl acetate, both dissolved in water",
                    "NaOH + ethyl acetate, બંને પાણીમાં ઓગળેલા"),
                  tr("homogeneous liquid", "homogeneous liquid"),
                  tr("volume of solution", "solution નું volume")],
                 [tr("H2 + Br2 in one gas mixture", "એક જ gas મિશ્રણમાં H2 + Br2"),
                  tr("homogeneous gas", "homogeneous gas"),
                  tr("volume of gas", "gas નું volume")],
                 [tr("Coal burning in air", "હવામાં કોલસો બળવો"),
                  tr("heterogeneous gas-solid", "heterogeneous gas-solid"),
                  tr("surface area of the coal", "કોલસાનું surface area")],
                 [tr("CO2 absorbed in NaOH solution", "NaOH દ્રાવણમાં CO2 ઓગળવું"),
                  tr("heterogeneous gas-liquid", "heterogeneous gas-liquid"),
                  tr("area of the gas-liquid interface", "gas-liquid interface નું area")]]),
            h4("Catalytic or non-catalytic", "Catalytic કે non-catalytic"),
            p("A <b>catalyst</b> takes part in the reaction and comes out unchanged. It opens a new "
              "path with a lower activation energy (Unit 2), so the same vessel at the same "
              "temperature produces more. Catalysis does not change how far the reaction can go - "
              "the equilibrium conversion is exactly the same with and without it.",
              "<b>Catalyst</b> પ્રક્રિયામાં ભાગ લે છે અને અંતે બદલાયા વિના નીકળે છે. તે ઓછી "
              "activation energy વાળો નવો માર્ગ ખોલે છે (Unit 2), તેથી એ જ vessel એ જ temperature પર "
              "વધુ product આપે છે. Catalysis થી પ્રક્રિયા કેટલી દૂર જશે તે બદલાતું નથી - catalyst "
              "સાથે અને વગર equilibrium conversion બરાબર એ જ રહે છે."),
            h4("Derivation: why grinding speeds a heterogeneous reaction up",
               "Derivation: દળવાથી heterogeneous પ્રક્રિયા કેમ ઝડપી થાય"),
            p("The rate is written per unit of contact area, so what matters is how much area a cubic "
              "metre of bed actually offers. Take spherical particles of diameter dp packed to a "
              "solids fraction (1 - eps):",
              "Rate સંપર્ક area ના એકમ દીઠ લખાય છે, તેથી મહત્વનું એ છે કે bed નો એક ઘન મીટર કેટલું "
              "area આપે છે. વ્યાસ dp વાળા ગોળા (1 - eps) solids fraction સુધી ભરેલા લો:"),
            derive("volume of solids per m3 of bed = (1 - eps)",
                   "number of particles  N = 6 (1-eps) / (pi dp^3)",
                   "area of one particle  = pi dp^2",
                   "area per m3 of bed  a = N pi dp^2",
                   "so  a = 6 (1 - eps) / dp"),
            eq("a = 6 (1 - eps) / dp,   (-rA) = k'' a CA"),
            p("Halving the particle diameter doubles the area and therefore doubles the observed rate "
              "at the same temperature and conversion. That is why a fluidized bed grinds its "
              "catalyst to 50 - 150 micrometre powder while a fixed bed keeps 3 - 10 mm pellets: the "
              "powder wins on area but loses on pressure drop.",
              "કણનો વ્યાસ અડધો કરવાથી area બમણું અને તેથી એ જ temperature તથા conversion પર માપેલો "
              "rate બમણો થાય. તેથી જ fluidized bed તેના catalyst ને 50 - 150 micrometre પાવડર સુધી "
              "દળે છે જ્યારે fixed bed 3 - 10 mm ની pellets રાખે છે: પાવડર area માં જીતે પણ "
              "pressure drop માં હારે."),
            why("A non-catalytic heterogeneous reaction can only happen where the phases touch, so its "
                "rate is written per unit area. That is why its reactor must be full of bubbles, "
                "droplets or packing: the design is a design for <i>area</i>, not for volume.",
                "Non-catalytic heterogeneous પ્રક્રિયા ફક્ત ત્યાં જ થઈ શકે જ્યાં phases અડે છે, "
                "તેથી તેનો rate per unit area લખાય છે. તેથી તેના reactor માં bubbles, droplets કે "
                "packing ભરેલું હોવું જોઈએ: તે design <i>area</i> માટેનું છે, volume માટેનું નહીં."),
            pit("A dissolved salt is not a second phase. NaCl dissolved in water is one liquid phase, "
                "so salt plus acid in water is a homogeneous reaction even though the salt was a "
                "solid when you weighed it.",
                "ઓગળેલું મીઠું બીજો phase નથી. પાણીમાં ઓગળેલું NaCl એક જ liquid phase છે, તેથી "
                "પાણીમાં મીઠું + acid homogeneous પ્રક્રિયા છે, ભલે તોળતી વખતે મીઠું solid હતું."),
            syllabus_item="1.2a",
        ),
    ],
})

# ---------------------------------------------------------------- 1.3 direction and heat
NOTES_A.append({
    "title": tr("1.3 Reversible or irreversible, exothermic or endothermic",
                "1.3 Reversible કે irreversible, exothermic કે endothermic"),
    "items": [
        card(
            "Direction: does the reaction stop, or settle?",
            "દિશા: પ્રક્રિયા અટકે છે કે સંતુલને આવે છે?",
            h4("Two behaviours", "બે વર્તણૂકો"),
            p("An <b>irreversible</b> reaction runs one way until a reactant is finished; its rate "
              "falls only because the concentration falls. A <b>reversible</b> reaction runs both "
              "ways at once; as products build up the reverse rate grows, the two rates become equal "
              "at <b>equilibrium</b>, and there the net rate is zero - however long you wait, nothing "
              "more happens.",
              "<b>Irreversible</b> પ્રક્રિયા એક જ દિશામાં ચાલે જ્યાં સુધી કોઈ reactant પૂરો ન થાય; "
              "તેનો rate ફક્ત concentration ઘટવાથી ઘટે છે. <b>Reversible</b> પ્રક્રિયા એકસાથે બંને "
              "દિશામાં ચાલે છે; products વધતાં reverse rate વધે છે અને <b>equilibrium</b> પર બંને "
              "rate સરખા થાય છે, જ્યાં net rate શૂન્ય થાય છે - કેટલી પણ રાહ જુઓ, આગળ કંઈ થતું "
              "નથી."),
            math("A + B <-> C + D",
                 "net rate = k1 CA CB - k2 CC CD",
                 "at equilibrium: k1 CA CB = k2 CC CD",
                 "K_eq = k1 / k2 = (CC CD) / (CA CB)"),
            p("For design this means a reversible reaction has a <b>ceiling</b>: no reactor, however "
              "large, can pass the equilibrium conversion at that temperature. The usual answers are "
              "to remove a product as it forms, or to run at a temperature where K_eq is larger.",
              "Design માટે તેનો અર્થ એ કે reversible પ્રક્રિયાની એક <b>મર્યાદા</b> હોય છે: તે "
              "temperature ના equilibrium conversion થી આગળ કોઈ પણ reactor, કેટલું પણ મોટું હોય, "
              "જઈ શકતું નથી. સામાન્ય ઉપાય એ છે કે product બનતાં જ કાઢી લેવું, અથવા એ temperature પર "
              "ચલાવવું જ્યાં K_eq વધુ હોય."),
            h4("Heat: where the energy goes", "Heat: energy ક્યાં જાય છે"),
            p("Every reaction either releases heat (<b>exothermic</b>, dH negative) or absorbs it "
              "(<b>endothermic</b>, dH positive). The reactor must carry that duty away or supply it, "
              "otherwise the temperature drifts - and because the rate constant is exponential in "
              "temperature, the rate drifts with it.",
              "દરેક પ્રક્રિયા heat છોડે છે (<b>exothermic</b>, dH ઋણાત્મક) અથવા લે છે "
              "(<b>endothermic</b>, dH ધનાત્મક). Reactor એ તે heat કાઢવી કે આપવી પડે, નહીં તો "
              "temperature ખસી જાય - અને rate constant temperature સાથે exponential હોવાથી rate પણ "
              "તેની સાથે ખસે."),
            h4("Derivation: the adiabatic temperature rise",
               "Derivation: adiabatic temperature rise"),
            p("Take a vessel with no heat exchange, feed at T0, and conversion X. The heat released by "
              "the reaction can only heat the mixture itself:",
              "heat exchange વગરનું vessel લો, feed T0 પર અને conversion X. પ્રક્રિયામાં છૂટેલી heat "
              "મિશ્રણને જ ગરમ કરી શકે છે:"),
            derive("heat released = (-dH_r) nA0 X            [J/s]",
                   "heat to warm  = (sum n_i Cp_i) (T - T0)   [J/s]",
                   "set the two equal and divide by nA0:",
                   "(-dH_r) X = (sum Theta_i Cp_i) (T - T0)",
                   "dT_ad = T - T0 = (-dH_r) X / (sum Theta_i Cp_i)"),
            eq("dT_ad = (-dH_r) X / (sum Theta_i Cp_i)"),
            p("With dH_r = -90 kJ/mol, X = 0.8, CA0 = 4 kmol/m3 and a mixture of mean capacity "
              "2.6 kJ/(kg K), the adiabatic rise is about 110 K. That is why a strongly exothermic "
              "reactor is never run adiabatically: the jacket, the coil or the reflux condenser "
              "exists to take that 110 K away.",
              "dH_r = -90 kJ/mol, X = 0.8, CA0 = 4 kmol/m3 અને 2.6 kJ/(kg K) સરેરાશ capacity વાળા "
              "મિશ્રણ માટે adiabatic rise લગભગ 110 K થાય. તેથી જ જોરદાર exothermic reactor કદી "
              "adiabatic ચલાવાતું નથી: jacket, coil કે reflux condenser એ 110 K કાઢવા માટે જ હોય છે."),
            why("The sign of dH decides the equipment, not the chemistry: dH negative demands cooling "
                "area, dH positive demands a heater or a preheated feed, and the same vessel with the "
                "wrong one either runs away or stalls.",
                "dH નું ચિહ્ન chemistry નહીં, equipment નક્કી કરે છે: dH ઋણાત્મક હોય તો cooling area "
                "જોઈએ, ધનાત્મક હોય તો heater કે ગરમ feed જોઈએ, અને એ જ vessel ખોટા પ્રકાર સાથે કાં "
                "runaway થાય કાં થંભી જાય."),
            check("For the numbers above the capacity must be per m3 of mixture: 1150 kg/m3 x "
                  "2.6 kJ/(kg K) = 2.99 MJ/(m3 K); 90 000 x 4000 x 0.8 / 2.99e6 = 96 K, and with the "
                  "2.6 per kg figure the answer is 110 K. Always state which capacity you used.",
                  "ઉપરના આંકડા માટે capacity મિશ્રણના m3 દીઠ હોવી જોઈએ: 1150 kg/m3 x 2.6 kJ/(kg K) "
                  "= 2.99 MJ/(m3 K); 90 000 x 4000 x 0.8 / 2.99e6 = 96 K, અને 2.6 પ્રતિ kg લેતાં "
                  "જવાબ 110 K આવે. કઈ capacity વાપરી તે હંમેશા લખો."),
            diagram="u1_energy",
            syllabus_item="1.2c, 1.2e",
        ),
    ],
})
