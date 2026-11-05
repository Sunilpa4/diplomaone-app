"""DI01000181 Unit 4, part B: ceramics."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from subject_DI01000181 import tr  # noqa: E402
from content_DI01000181_lib import (p, h4, table, math, eq, why, check, pit, card,  # noqa: E402
                                    ul, ol)

NOTES_B = []

NOTES_B.append({
    "title": tr("4.3 Ceramics", "4.3 Ceramics"),
    "items": [
        card(
            "Hard, hot and inert - and brittle for the same reason",
            "સખત, ગરમ અને નિષ્ક્રિય - અને એ જ કારણે ભંગુર",
            p("A ceramic is an inorganic solid held by ionic or covalent bonds: alumina (Al2O3), "
              "zirconia (ZrO2), silicon carbide (SiC), silicon nitride (Si3N4), porcelain, glass and "
              "ordinary brick. The bond is strong and directional, which gives a hardness of 1500 HV "
              "and a melting point above 2000 C on a material of density 3.9 g/cm3; the same bond has "
              "no free electrons, so it insulates and does not corrode. The price is ductility: "
              "alumina carries 2000 MPa in compression and only about 300 MPa in bending, and it does "
              "not yield before it breaks.",
              "Ceramic એ inorganic ઘન છે જે ionic કે covalent bonds થી બંધાયેલું હોય: alumina (Al2O3), "
              "zirconia (ZrO2), silicon carbide (SiC), silicon nitride (Si3N4), porcelain, glass અને "
              "સામાન્ય ઈંટ. Bond મજબૂત અને દિશાવાળો છે, તેથી 3.9 g/cm3 ની density પર 1500 HV સખતાઈ અને "
              "2000 C થી ઉપર ગલનબિંદુ મળે; એ જ bond માં free electrons નથી, તેથી તે અવાહક છે અને કાટ ખાતું "
              "નથી. કિંમત ductility છે: alumina compression માં 2000 MPa ઉપાડે પણ bending માં ફક્ત 300 MPa, "
              "અને તૂટતાં પહેલાં yield થતું નથી."),
            math("thermal stress in a fully constrained part:  sigma = E alpha dT",
                 "alumina:  300e9 x 8.0e-6 x 200 = 480 MPa  ->  above its 300 MPa strength, it cracks",
                 "the safe temperature step alone is 300e6/(300e9 x 8.0e-6) = 125 K",
                 "Griffith: sigma_f = sqrt(2 E gamma / pi a), a 50 um flaw gives 276 MPa",
                 "the same material with a 200 um flaw: 138 MPa - the flaw size sets the strength"),
            table([tr("ceramic", "ceramic"), tr("hardness, HV", "hardness, HV"),
                   tr("flexural, MPa", "flexural, MPa"), tr("max use", "વધુમાં વધુ"),
                   tr("a part it makes", "એનો એક ભાગ")],
                  [[tr("alumina 96 %", "alumina 96 %"), tr("1200", "1200"), tr("300", "300"),
                    tr("1500 C", "1500 C"), tr("spark plug, wear tile", "spark plug, ઘસાતી tile")],
                   [tr("zirconia", "zirconia"), tr("1300", "1300"), tr("900", "900"),
                    tr("1000 C", "1000 C"), tr("die, knife, oxygen sensor", "die, ચાકુ, oxygen sensor")],
                   [tr("silicon carbide", "silicon carbide"), tr("2500", "2500"), tr("450", "450"),
                    tr("1600 C", "1600 C"), tr("kiln furniture, seal", "ભઠ્ઠીનું સામાન, seal")],
                   [tr("silicon nitride", "silicon nitride"), tr("1700", "1700"), tr("800", "800"),
                    tr("1200 C", "1200 C"), tr("turbo rotor, ball", "turbo rotor, દડો")],
                   [tr("porcelain", "porcelain"), tr("600", "600"), tr("70", "70"),
                    tr("1000 C", "1000 C"), tr("insulator, sanitaryware", "insulator, sanitaryware (બેસિન)")]]),
            why("a metal deforms by moving dislocations; in an ionic lattice a dislocation would bring "
                "like charges together, so it cannot move, and the only way left to relieve stress is "
                "a crack. One sentence gives both halves of the behaviour - hard, and brittle.",
                "metal dislocations ખસીને deform થાય; ionic lattice માં dislocation સરખા charge પાસે લાવે, "
                "તેથી તે ખસી શકે નહીં, અને stress ઓછો કરવાનો એક જ રસ્તો રહે - તિરાડ. એક જ વાક્ય બંને અડધા "
                "ગુણધર્મ આપે - સખત, અને ભંગુર."),
            pit("do not design a ceramic for tension or shock. The 2000 MPa compressive figure is real "
                "and the 300 MPa bending figure is real, and a tile under a column is safe while the "
                "same tile dropped on the floor is not.",
                "ceramic ને tension કે ધક્કા માટે design ન કરો. 2000 MPa compression અને 300 MPa bending "
                "બંને સાચા છે, અને સ્તંભ નીચેની tile સલામત છે જ્યારે એ જ tile નીચે પડે તો નહીં."),
            diagram="u4_compare",
        ),
        card(
            "Traditional and advanced ceramics, and where each one goes",
            "Traditional અને advanced ceramics, અને દરેક ક્યાં જાય",
            p("Traditional ceramics are made from clay, feldspar and quartz, shaped wet and fired at "
              "1100 - 1300 C: brick, tile, sanitaryware, porcelain insulators and pottery. Cement and "
              "glass belong here too, though one sets by hydration and the other is melted and "
              "quenched. <b>Advanced</b> ceramics are chemically pure, sintered from a powder with a "
              "controlled grain size, and bought for one property: alumina for wear and insulation, "
              "zirconia for toughness by transformation, silicon carbide for thermal shock, silicon "
              "nitride for a turbocharger rotor that spins at 100000 rpm.",
              "Traditional ceramics clay, feldspar અને quartz માંથી બને, ભીનું આકાર પામે અને 1100 - 1300 C પર "
              "પાકે: ઈંટ, tile, sanitaryware, porcelain insulators અને માટીકામ. Cement અને glass પણ આમાં "
              "આવે, જોકે એક hydration થી જામે અને બીજું ઓગળીને ઠારે. <b>Advanced</b> ceramics રાસાયણિક રીતે "
              "શુદ્ધ હોય, નિયંત્રિત grain size ના powder માંથી sinter થાય, અને એક ગુણધર્મ માટે ખરીદાય: "
              "alumina wear અને insulation માટે, zirconia transformation થી toughness માટે, silicon "
              "carbide thermal shock માટે, silicon nitride 100000 rpm પર ફરતા turbocharger rotor માટે."),
            math("expansion misfit when alumina is sealed to steel:",
                 "alpha(steel) 12e-6, alpha(alumina) 8.0e-6  ->  difference 4.0e-6 per K",
                 "over 800 C: 4.0e-6 x 800 = 3.2e-3 strain",
                 "on a 40 mm joint that is 3.2e-3 x 40 = 0.13 mm of misfit, so a graded seal is used"),
            table([tr("ceramic", "ceramic"), tr("what it is", "શું છે"),
                   tr("bought for", "શેના માટે ખરીદાય"), tr("typical part", "સામાન્ય ભાગ")],
                  [[tr("fireclay", "fireclay"), tr("clay plus grog", "clay અને grog"),
                    tr("cheap, casts easily", "સસ્તું, સરળ cast"), tr("furnace lining, brick", "ભઠ્ઠીનું lining, ઈંટ")],
                   [tr("porcelain", "porcelain"), tr("clay, feldspar, quartz", "clay, feldspar, quartz (માટી)"),
                    tr("insulation, hygiene", "insulation, સ્વચ્છતા"), tr("insulator, basin, tile", "insulator, basin, tile (બેસિન)")],
                   [tr("glass", "glass"), tr("fused silica and oxides", "fused silica અને oxides"),
                    tr("transparency", "પારદર્શકતા"), tr("window, gauge, bottle", "બારી, gauge, બોટલ")],
                   [tr("glass-ceramic", "glass-ceramic"), tr("crystallised glass", "સ્ફટિક થયેલું glass"),
                    tr("near zero expansion", "લગભગ શૂન્ય expansion"), tr("cooktop, lab ware", "cooktop, lab નાં વાસણ")],
                   [tr("alumina", "alumina"), tr("96 or 99.5 % Al2O3", "96 કે 99.5 % Al2O3"),
                    tr("wear, insulation, 1500 C", "ઘસારો, insulation, 1500 C"), tr("spark plug, seal face", "spark plug, seal ની સપાટી")]]),
            why("porosity is what separates the two families. A traditional body is sintered at a "
                "temperature low enough to leave 5 - 15 % open pores, which makes it light and "
                "insulating; an advanced body is sintered to under 1 % porosity, which makes it strong "
                "and is why it costs a hundred times more per kilogram.",
                "બે કુટુંબને porosity જુદા પાડે છે. Traditional body એટલા નીચા તાપમાને sinter થાય કે 5 - 15 % "
                "ખુલ્લા છિદ્ર રહી જાય, જે તેને હલકું અને અવાહક બનાવે; advanced body 1 % થી ઓછા porosity સુધી "
                "sinter થાય, જે તેને મજબૂત બનાવે અને તેથી કિલો દીઠ સો ગણું મોંઘું પડે."),
            pit("firing is not melting. A brick that has been fired has not been liquid, so it keeps its "
                "pores; if you design a 10 % shrinkage allowance as if it were a casting, the part comes "
                "out undersize in every direction.",
                "પાકવું એ ઓગળવું નથી. પાકેલી ઈંટ પ્રવાહી થઈ નથી, તેથી છિદ્ર રહે છે; casting ની જેમ 10 % "
                "shrinkage allowance માનો તો ભાગ દરેક દિશામાં નાનો નીકળે."),
            check("match the expansion before you match the strength. A glass-ceramic cooktop survives "
                  "a hot pan because its expansion is near zero; ordinary window glass of the same "
                  "strength cracks on the same pan.",
                  "તાકાત પહેલાં expansion મેળવો. Glass-ceramic cooktop ગરમ તવા સહન કરે કારણ કે તેનું "
                  "expansion લગભગ શૂન્ય છે; એ જ તાકાતનું સામાન્ય window glass એ જ તવા પર તૂટે."),
            diagram="u4_ceramic",
        ),
    ],
})
