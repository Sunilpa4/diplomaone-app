"""DI01000181 Unit 4, part D: abrasives and adhesives."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from subject_DI01000181 import tr  # noqa: E402
from content_DI01000181_lib import (p, h4, table, math, eq, why, check, pit, card,  # noqa: E402
                                    ul, ol)

NOTES_D = []

NOTES_D.append({
    "title": tr("4.5 Abrasives and adhesives", "4.5 Abrasives અને adhesives"),
    "items": [
        card(
            "Abrasives: the grain, the bond and the grit number",
            "Abrasives: grain, bond અને grit number",
            p("An abrasive is a material harder than the work it has to cut. The natural ones are "
              "sandstone, emery (60 - 70 % alumina in iron oxide), corundum and diamond; almost "
              "everything sold today is synthetic - silicon carbide, made in an electric furnace since "
              "1891, fused alumina, cubic boron nitride since 1957 and synthetic diamond. The grain is "
              "held in a <b>bond</b> - vitrified clay for a bench wheel, resinoid for a cut-off disc, "
              "rubber and shellac for a polishing wheel, paper or cloth for a coated belt - and it is "
              "sized by a <b>grit number</b>: 8 - 24 coarse, 30 - 60 medium, 80 - 180 fine, 220 - 600 "
              "for lapping.",
              "Abrasive એટલે કાપવાની સામગ્રી કરતાં સખત પદાર્થ. કુદરતી એટલે પથ્થર, emery (iron oxide માં 60 - "
              "70 % alumina), corundum અને diamond; આજે વેચાતું લગભગ બધું synthetic છે - silicon carbide, "
              "1891 થી electric furnace માં બનતું, fused alumina, 1957 થી cubic boron nitride અને synthetic "
              "diamond. Grain <b>bond</b> માં પકડાય છે - bench wheel માટે vitrified માટી, cut-off disc માટે "
              "resinoid, polishing wheel માટે rubber અને shellac, coated belt માટે paper કે કપડું - અને તેનું "
              "માપ <b>grit number</b> થી થાય: 8 - 24 જાડું, 30 - 60 મધ્યમ, 80 - 180 બારીક, lapping માટે "
              "220 - 600."),
            math("wheel speed:  v = pi D N / 60",
                 "D = 0.250 m, N = 2000 rpm:  v = pi x 0.250 x 2000/60 = 26 m/s",
                 "a vitrified wheel is rated 35 m/s, so 26 m/s leaves a margin of 26 %",
                 "the same wheel at 2800 rpm reaches 36.6 m/s and must not be run"),
            table([tr("abrasive", "abrasive"), tr("Knoop", "Knoop"), tr("used on", "શેના પર"),
                   tr("note", "નોંધ")],
                  [[tr("emery", "emery"), tr("1300", "1300"), tr("wood, paint", "લાકડું, પેન્ટ"),
                    tr("natural, cheap", "કુદરતી, સસ્તું")],
                   [tr("fused alumina", "fused alumina"), tr("2100", "2100"),
                    tr("steel, general", "સ્ટીલ, સામાન્ય"), tr("the workshop default", "workshop ની પસંદ")],
                   [tr("silicon carbide", "silicon carbide"), tr("2500", "2500"),
                    tr("cast iron, carbide, stone", "cast iron, carbide, પથ્થર"), tr("sharp and friable", "તીવ્ર અને ભૂરું")],
                   [tr("CBN", "CBN"), tr("4500", "4500"), tr("hardened steel, HSS", "hardened સ્ટીલ, HSS"),
                    tr("no burn, long life", "બળતર નહીં, લાંબું આયુષ્ય")],
                   [tr("diamond", "diamond"), tr("7000", "7000"),
                    tr("carbide, ceramic, glass", "carbide, ceramic, glass (કાચ)"), tr("last resort, expensive", "છેલ્લો ઉપાય, મોંઘું")]]),
            why("a grinding wheel has to sharpen itself. As the grain dulls the force on it rises until "
                "the bond breaks and the worn grain falls out, exposing a new edge - that is "
                "<b>self-sharpening</b>, and it is why the bond is chosen to match the work and not "
                "the grain.",
                "grinding wheel ને પોતાની જાતે ધારી રાખવી પડે. Grain થૂંસાતાં તેના પરનું બળ વધે અને bond "
                "તૂટે, ઘસાયેલો grain નીકળી જાય અને નવી ધાર આવે - એ <b>self-sharpening</b> છે, અને તેથી bond "
                "grain નહીં, કામ પ્રમાણે પસંદ થાય."),
            pit("a glazed wheel is not a dull wheel: the pores have filled with swarf and the grain "
                "cannot cut. Dressing with a star dresser opens it again, and it is the operator's job, "
                "not a reason to buy a new wheel.",
                "glazed wheel dull wheel નથી: છિદ્રોમાં swarf ભરાઈ જાય અને grain કાપી શકે નહીં. Star dresser "
                "થી dressing કરવાથી ફરી ખૂલે, અને એ operator નું કામ છે, નવું wheel ખરીદવાનું કારણ નહીં."),
            diagram="u4_abrasive",
        ),
        card(
            "Adhesives: the joint is the design",
            "Adhesives: જોડાણ જ design છે",
            p("An adhesive joins two parts through surface attraction instead of a rivet or a weld. "
              "Structural adhesives - epoxy, toughened acrylic, polyurethane - carry real load; "
              "cyanoacrylate and hot melt are for small or temporary work; anaerobic grades lock a "
              "thread. The glue is only half the joint: the surface must be <b>degreased</b>, "
              "<b>abraded</b> to 0.5 - 2 um and often primed, because adhesion happens in the first "
              "few molecular layers. A lap joint loaded in <b>shear</b> over the largest area is "
              "strong; the same glue in <b>peel</b> is ten times weaker.",
              "Adhesive બે ભાગને rivet કે weld નહીં, સપાટીના આકર્ષણ થી જોડે. Structural adhesives - epoxy, "
              "toughened acrylic, polyurethane - ખરો લોડ ઉપાડે; cyanoacrylate અને hot melt નાના કે હંગામી "
              "કામ માટે; anaerobic grade thread લોક કરે. ગુંદર અડધું જ જોડાણ છે: સપાટી <b>degrease</b> કરવી "
              "પડે, 0.5 - 2 um સુધી <b>abrade</b> કરવી પડે અને ઘણી વાર primer લગાવવો પડે, કારણ કે adhesion "
              "પહેલા થોડા molecular સ્તરોમાં જ થાય. <b>Shear</b> માં સૌથી મોટા area પર લોડ પડતું lap joint "
              "મજબૂત હોય; એ જ ગુંદર <b>peel</b> માં દસ ગણું નબળું."),
            math("lap shear stress:  tau = P/A",
                 "overlap 25 mm x 40 mm = 1000 mm2, load 5 kN:  tau = 5000/1000 = 5.0 MPa",
                 "epoxy lap shear strength 20 MPa -> factor of safety 20/5 = 4.0",
                 "at a required factor of 3 the joint carries 20/3 x 1000 = 6.67 kN",
                 "the same 5 kN in peel may need 10 times the area"),
            table([tr("adhesive", "adhesive"), tr("shear, MPa", "shear, MPa"), tr("cure", "cure"),
                   tr("used for", "ઉપયોગ")],
                  [[tr("epoxy", "epoxy"), tr("20", "20"), tr("24 h, or 30 min at 80 C", "24 કલાક, કે 80 C પર 30 મિનિટ"),
                    tr("structural, gaps filled", "structural, ખાલી જગ્યા ભરે")],
                   [tr("toughened acrylic", "toughened acrylic"), tr("15", "15"), tr("10 min", "10 મિનિટ"),
                    tr("oily steel, fast line", "તેલવાળું સ્ટીલ, ઝડપી લાઇન")],
                   [tr("cyanoacrylate", "cyanoacrylate"), tr("12", "12"), tr("10 s", "10 સેકન્ડ"),
                    tr("small plastic parts", "નાના plastic ભાગ")],
                   [tr("polyurethane", "polyurethane"), tr("8", "8"), tr("1 - 24 h", "1 - 24 કલાક"),
                    tr("flexible panel, wood", "લચીલું panel, લાકડું")],
                   [tr("PVA", "PVA"), tr("6", "6"), tr("1 h clamp", "1 કલાક clamp"),
                    tr("wood, paper", "લાકડું, કાગળ")],
                   [tr("hot melt", "hot melt"), tr("3", "3"), tr("seconds", "સેકન્ડો"),
                    tr("packaging, trim", "packaging, trim")],
                   [tr("anaerobic", "anaerobic"), tr("10", "10"), tr("20 min", "20 મિનિટ"),
                    tr("thread locking", "thread લોક")]]),
            why("adhesion is surface chemistry, so the joint fails where the chemistry was not done. A "
                "greasy surface is not wetted, the glue sits on the oil instead of on the metal, and "
                "the joint peels at the interface while the glue itself is still intact.",
                "adhesion સપાટીનું રસાયણ છે, તેથી જ્યાં રસાયણ થયું નથી ત્યાં જોડાણ તૂટે. ચીકણી સપાટી ભીંજાતી "
                "નથી, ગુંદર ધાતુ પર નહીં તેલ પર બેસે, અને ગુંદર સાબૂત હોય તોય જોડાણ interface પરથી ઊખડે."),
            pit("a thick glue line is a weak joint. The best bond line is 0.1 - 0.2 mm; a 1 mm gap "
                "filled with brittle epoxy shrinks on cure, leaves voids and cracks under load, which "
                "is why a gap-filling adhesive is a different product.",
                "જાડી ગુંદરની લાઇન નબળું જોડાણ છે. સૌથી સારી bond line 0.1 - 0.2 mm; ભંગુર epoxy થી ભરેલી "
                "1 mm જગ્યા cure માં સંકોચાય, ખાલી જગ્યા રહે અને લોડ નીચે તૂટે, તેથી gap-filling adhesive "
                "અલગ ઉત્પાદન હોય."),
            check("design the joint before choosing the glue: put the load in shear, give it area, and "
                  "keep the peel path out of it. A butt joint on a 20 MPa epoxy carries less than a lap "
                  "joint on a 6 MPa PVA.",
                  "ગુંદર પસંદ કરતાં પહેલાં જોડાણ design કરો: લોડ shear માં રાખો, area આપો, અને peel નો રસ્તો "
                  "દૂર રાખો. 20 MPa epoxy નું butt joint, 6 MPa PVA ના lap joint કરતાં ઓછું ઉપાડે."),
        ),
    ],
})
