"""DI01000181 Unit 1, part A: section 1.1 - classification of materials and the selection of one."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from subject_DI01000181 import tr  # noqa: E402
from content_DI01000181_lib import p, h4, table, math, eq, why, check, pit, card  # noqa: E402

NOTES_A = []

NOTES_A.append({
    "title": tr("1.1 Classification of engineering materials",
                "1.1 ઇજનેરી સામગ્રીનું વર્ગીકરણ"),
    "items": [
        card(
            "Classification of engineering materials",
            "ઇજનેરી સામગ્રીનું વર્ગીકરણ",
            p("Every engineering material belongs to one of four families, and the family fixes what "
              "the material can and cannot do. Metals are strong in tension and conduct heat and "
              "current; ceramics are hard, brittle and heat resistant; polymers are light, cheap and "
              "easy to shape; composites take the best of two materials by putting strong fibres in a "
              "light matrix. Two newer groups sit beside them - semiconductors and smart materials.",
              "દરેક ઇજનેરી સામગ્રી ચાર પૈકી એક કુટુંબમાં આવે છે, અને કુટુંબ જ નક્કી કરે છે કે સામગ્રી "
              "શું કરી શકે અને શું ન કરી શકે. ધાતુઓ tension માં મજબૂત હોય છે અને heat તથા current વહન "
              "કરે; ceramics સખત, ભંગુર અને ગરમી સહેનારાં હોય; polymers હલકા, સસ્તા અને આકાર આપવામાં "
              "સહેલા હોય; composites હલકા matrix માં મજબૂત fibres નાખીને બે સામગ્રીનું શ્રેષ્ઠ લે છે. "
              "તેમની બાજુમાં બે નવા સમૂહ છે - semiconductors અને smart materials."),
            table([tr("Family", "કુટુંબ"), tr("Typical members", "સામાન્ય સભ્યો"),
                   tr("One strength", "એક તાકાત"), tr("One weakness", "એક નબળાઈ")],
                  [[tr("Metals", "ધાતુઓ"),
                    tr("steel, cast iron, copper, brass, aluminium", "steel, cast iron, copper, brass, aluminium"),
                    tr("strong and tough, easy to machine and weld", "મજબૂત અને tough, સહેલા machine તથા weld થાય"),
                    tr("rusts, heavy, loses strength when hot", "કાટ લાગે, ભારે, ગરમીમાં તાકાત ઘટે")],
                   [tr("Ceramics", "Ceramics"),
                    tr("alumina, silicon carbide, glass, cement", "alumina, silicon carbide, glass, cement"),
                    tr("hard, wear resistant, survives 1000 C", "સખત, ઘસારો સહે, 1000 C સહે"),
                    tr("brittle, no plastic deformation", "ભંગુર, plastic deformation નહીં")],
                   [tr("Polymers", "Polymers"),
                    tr("PE, PVC, nylon, epoxy, rubber", "PE, PVC, nylon, epoxy, rubber"),
                    tr("light, cheap, corrosion proof, mouldable", "હલકા, સસ્તા, કાટરહિત, mould થાય"),
                    tr("softens when hot, creeps under load", "ગરમીમાં મૃદુ પડે, load નીચે creep થાય")],
                   [tr("Composites", "Composites"),
                    tr("CFRP, GFRP, cermet, plywood", "CFRP, GFRP, cermet, plywood"),
                    tr("highest strength per kilogram", "કિલોગ્રામ દીઠ સૌથી વધુ તાકાત"),
                    tr("costly, hard to recycle, brittle fibre", "ખર્ચાળ, recycle કરવું અઘરું, fibre ભંગુર")]]),
            math("metals: free electrons -> conduct heat and current, deform before breaking",
                 "ceramics: ionic or covalent bonds -> no slip, so hard and brittle",
                 "polymers: long chain molecules -> low strength, large elongation",
                 "composites: fibre carries load, matrix transfers and protects"),
            why("The family decides the bonding, the bonding decides how the atoms are held together, "
                "and that decides the properties. That is why the classification is the first thing to "
                "learn: from the family you can predict the strength, the melting point, the "
                "conductivity and the way the material will fail.",
                "કુટુંબ bonding નક્કી કરે, bonding નક્કી કરે કે atoms કેવી રીતે જોડાયેલા છે, અને તે "
                "ગુણધર્મો નક્કી કરે. તેથી વર્ગીકરણ પહેલું શીખવાનું હોય: કુટુંબ પરથી તમે તાકાત, ગલનબિંદુ, "
                "વાહકતા અને નિષ્ફળ થવાની રીત અનુમાન કરી શકો."),
            check("Test a classification by its exceptions: graphite is a non-metal that conducts, "
                  "silicon is a metalloid, and a cermet is a ceramic-metal composite. If a family "
                  "cannot describe the exception, the exception belongs to two families at once.",
                  "વર્ગીકરણને તેના અપવાદોથી ચકાસો: graphite અધાતુ છે પણ current વહન કરે, silicon "
                  "metalloid છે, અને cermet એ ceramic-metal composite છે. જે કુટુંબ અપવાદનું વર્ણન ન "
                  "કરી શકે તે અપવાદ એકસાથે બે કુટુંબનો હોય."),
            pit("Saying \"steel is the strongest material\" without the duty. Steel is the strongest "
                "per rupee, not per kilogram: titanium and carbon fibre beat it by three to eight "
                "times on strength per unit weight, and alumina beats it on wear at 1000 C.",
                "\"steel સૌથી મજબૂત સામગ્રી છે\" એમ કામ જણાવ્યા વગર કહેવું. Steel રૂપિયા દીઠ સૌથી "
                "મજબૂત છે, કિલોગ્રામ દીઠ નહીં: titanium અને carbon fibre તેને વજન દીઠ તાકાતમાં ત્રણથી "
                "આઠ ગણા વટાવે છે, અને alumina 1000 C પર ઘસારામાં તેને વટાવે છે."),
            diagram="u1_class",
            syllabus_item="1.1",
        ),
        card(
            "Choosing a material: strength per unit weight, then cost",
            "સામગ્રી પસંદગી: વજન દીઠ તાકાત, પછી ખર્ચ",
            p("A material is chosen in a fixed order: the duty first (what load, what temperature, what "
              "corrosion), then the property that the duty demands, then the process that can make the "
              "shape, and only then the price. For anything that moves - a bicycle, a fan blade, a "
              "connecting rod - the deciding property is not strength but strength per unit weight.",
              "સામગ્રી એક નિશ્ચિત ક્રમમાં પસંદ થાય: પહેલા કામ (કેટલો load, કેટલું temperature, કેવો "
              "કાટ), પછી કામ માંગે તે ગુણધર્મ, પછી જે આકાર બનાવી શકે તે process, અને પછી જ ભાવ. જે "
              "પણ હલે છે તેના માટે - સાયકલ, fan blade, connecting rod - નિર્ણાયક ગુણધર્મ તાકાત નહીં, "
              "વજન દીઠ તાકાત છે."),
            math("specific strength = UTS / density        (kN m / kg when UTS is in MPa)",
                 "steel   : 450 / 7.85 =  57 kN m/kg",
                 "aluminium: 310 / 2.70 = 115 kN m/kg",
                 "titanium : 950 / 4.43 = 214 kN m/kg",
                 "CFRP     : 700 / 1.60 = 438 kN m/kg"),
            table([tr("Step", "પગલું"), tr("Question", "પ્રશ્ન"), tr("What it removes", "શું કાઢે")],
                  [[tr("1 duty", "1 કામ"), tr("load, temperature, corrosion, wear", "load, temperature, કાટ, ઘસારો"),
                    tr("families that cannot survive", "જે કુટુંબ ટકી ન શકે")],
                   [tr("2 property", "2 ગુણધર્મ"),
                    tr("strength, stiffness, conductivity, weight", "તાકાત, stiffness, વાહકતા, વજન"),
                    tr("materials that are too weak or too heavy", "બહુ નબળી કે બહુ ભારે સામગ્રી")],
                   [tr("3 process", "3 process"), tr("cast, forge, weld, machine, mould", "cast, forge, weld, machine, mould"),
                    tr("materials that cannot make the shape", "જે આકાર ન બનાવી શકે")],
                   [tr("4 cost", "4 ખર્ચ"), tr("price per kg, per part, per year of life", "કિલો દીઠ, ભાગ દીઠ, આયુષ્ય દીઠ ભાવ"),
                    tr("the ones that are affordable now", "જે અત્યારે પરવડે તે")]]),
            eq("specific strength = UTS / rho", "material index = strength^(2/3) / rho for a light beam"),
            why("Weight saved in a moving part is saved again every second: a lighter connecting rod "
                "reduces the inertia force, which allows a higher speed, which gives more power from "
                "the same engine. That is why the specific strength and not the strength is the "
                "design number in transport.",
                "હલતા ભાગમાં બચેલું વજન દર સેકન્ડે ફરી બચે છે: હલકો connecting rod inertia force "
                "ઘટાડે, જે વધુ ઝડપ આપે, જે એ જ engine માંથી વધુ power આપે. તેથી વાહનમાં design નો "
                "આંકડો તાકાત નહીં, specific strength છે."),
            check("Check the unit: MPa = N/mm2 and density = g/cm3, so MPa/(g/cm3) = 1000 N m/kg = "
                  "1 kN m/kg. A specific strength quoted in m2/s2 is the same number multiplied by "
                  "1000, which is where most unit mistakes in this topic come from.",
                  "એકમ ચકાસો: MPa = N/mm2 અને density = g/cm3, તેથી MPa/(g/cm3) = 1000 N m/kg = "
                  "1 kN m/kg. m2/s2 માં લખાયેલી specific strength એ જ આંકડો 1000 ગણો છે, અને આ topic "
                  "ની મોટા ભાગની એકમ ભૂલો ત્યાંથી જ આવે છે."),
            pit("Choosing by strength alone and then paying for the weight. A steel bracket that is "
                "three times stronger than needed but five times heavier than an aluminium one is the "
                "wrong choice for a drone and the right choice for a machine bed.",
                "ફક્ત તાકાત પરથી પસંદગી કરી પછી વજનની કિંમત ચૂકવવી. જરૂર કરતાં ત્રણ ગણું મજબૂત પણ "
                "aluminium કરતાં પાંચ ગણું ભારે steel bracket drone માટે ખોટી પસંદગી છે અને machine "
                "bed માટે સાચી."),
            diagram="u1_select",
            syllabus_item="1.1",
        ),
    ],
})
