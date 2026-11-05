"""DI01000181 Unit 1, part C: section 1.3 - crystal structure, packing and density."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from subject_DI01000181 import tr  # noqa: E402
from content_DI01000181_lib import p, h4, table, math, eq, why, check, pit, card  # noqa: E402

NOTES_C = []

NOTES_C.append({
    "title": tr("1.3 Structure of solids: crystal, unit cell, BCC, FCC and HCP",
                "1.3 ઘનની રચના: crystal, unit cell, BCC, FCC અને HCP"),
    "items": [
        card(
            "Crystal, lattice and unit cell",
            "Crystal, lattice અને unit cell",
            p("A metal is crystalline: its atoms sit on a repeating pattern, and the smallest block that "
              "can be repeated to build the whole solid is the unit cell. Three cells cover almost "
              "every engineering metal - body centred cubic, face centred cubic and hexagonal close "
              "packed - and the cell a metal has decides its density, its ductility and the way it "
              "behaves when it is heated.",
              "ધાતુ crystalline છે: તેના atoms એક પુનરાવર્તી ભાત પર બેસે છે, અને આખો ઘન બનાવવા "
              "પુનરાવર્તિત થઈ શકે તેવો સૌથી નાનો ટુકડો unit cell છે. ત્રણ cell લગભગ દરેક ઇજનેરી ધાતુને "
              "આવરે છે - body centred cubic, face centred cubic અને hexagonal close packed - અને ધાતુ "
              "માં કયો cell છે તે તેની density, ductility અને ગરમ કરવા પરનું વર્તન નક્કી કરે છે."),
            math("lattice: the repeating set of points;  basis: the atom(s) at each point",
                 "unit cell: the smallest block that tiles the crystal",
                 "BCC: atoms at 8 corners + 1 at the body centre  ->  8 x 1/8 + 1 = 2 atoms",
                 "FCC: atoms at 8 corners + 1 at each of 6 faces ->  8 x 1/8 + 6 x 1/2 = 4 atoms",
                 "HCP: 6 atoms in a hexagonal prism (12 x 1/6 + 2 x 1/2 + 3 = 6)"),
            table([tr("Structure", "રચના"), tr("Atoms per cell", "cell દીઠ atoms"),
                   tr("Coordination number", "Coordination number"), tr("Typical metals", "સામાન્ય ધાતુઓ")],
                  [[tr("BCC", "BCC"), tr("2", "2"), tr("8", "8"),
                    tr("Fe below 912 C, Cr, W, Mo, V", "912 C નીચે Fe, Cr, W, Mo, V")],
                   [tr("FCC", "FCC"), tr("4", "4"), tr("12", "12"),
                    tr("Cu, Al, Ni, Ag, Au, Fe 912-1394 C", "Cu, Al, Ni, Ag, Au, Fe 912-1394 C")],
                   [tr("HCP", "HCP"), tr("6", "6"), tr("12", "12"),
                    tr("Mg, Zn, Cd, Ti, Co", "Mg, Zn, Cd, Ti, Co")]]),
            h4("Single crystal against polycrystal", "Single crystal સામે polycrystal"),
            p("A turbine blade grown as one crystal has no grain boundaries to creep along; a cast "
              "bracket is a polycrystal with millions of grains in random orientation and behaves the "
              "same in every direction. Most engineering metals are polycrystalline, and Unit 2 takes "
              "the grain as its subject.",
              "એક crystal તરીકે ઉગાડેલા turbine blade માં creep થવા માટે grain boundaries હોતી નથી; "
              "casting કરેલો bracket લાખો grains વાળો polycrystal છે અને દરેક દિશામાં સરખો વર્તે છે. "
              "મોટા ભાગની ઇજનેરી ધાતુઓ polycrystalline છે, અને Unit 2 grain ને વિષય બનાવે છે."),
            why("The cell is a counting device. Once the cell and its atoms are known, the number of "
                "atoms in a gram, the density, the gap between atoms and the number of slip systems can "
                "all be calculated - which is why the three cells are learnt by heart.",
                "Cell એ ગણતરીનું સાધન છે. Cell અને તેના atoms ખબર હોય તો એક ગ્રામમાં atoms ની સંખ્યા, "
                "density, atoms વચ્ચેનું અંતર અને slip systems ની સંખ્યા બધું ગણી શકાય - તેથી જ ત્રણ "
                "cells મોઢે ગોખાય છે."),
            check("Count the fractions before trusting the table: a corner atom is shared by eight "
                  "cells and a face atom by two, so BCC is 8 x 1/8 + 1 = 2 and FCC is "
                  "8 x 1/8 + 6 x 1/2 = 4. Any other count means the cell was drawn wrong.",
                  "કોષ્ટક માનતા પહેલા અંશ ગણો: corner atom આઠ cells વચ્ચે અને face atom બે વચ્ચે વહેંચાય "
                  "છે, તેથી BCC 8 x 1/8 + 1 = 2 અને FCC 8 x 1/8 + 6 x 1/2 = 4. બીજી કોઈ ગણતરી આવે તો "
                  "cell ખોટો દોરાયો છે."),
            pit("Drawing a unit cell as if the atoms were inside a box that belongs to them. The cell "
                "shares its corner and face atoms with its neighbours, and forgetting that inflates "
                "the atom count by a factor of four or more.",
                "Unit cell એવી રીતે દોરવો કે જાણે atoms તેમના જ box ની અંદર હોય. Cell પોતાના corner અને "
                "face atoms પાડોશી સાથે વહેંચે છે, અને તે ભૂલવાથી atom ની ગણતરી ચાર કે તેથી વધુ ગણી "
                "વધી જાય."),
            diagram="u1_cells",
            syllabus_item="1.3",
        ),
        card(
            "Packing fraction: why close-packed metals are denser",
            "Packing fraction: close-packed ધાતુઓ ઘન કેમ હોય",
            p("Packing fraction is the fraction of the cell volume that the atoms themselves occupy. It "
              "depends only on how the spheres of equal size are stacked, not on which metal they are: "
              "simple cubic fills 52 %, body centred cubic 68 %, and the two close-packed arrangements "
              "74 %.",
              "Packing fraction એ cell ના volume નો જે ભાગ atoms પોતે રોકે છે તે અંશ છે. તે ફક્ત એના પર "
              "આધારે છે કે સરખા માપના ગોળા કેવી રીતે ગોઠવાયા છે, ધાતુ કઈ છે તેના પર નહીં: simple cubic "
              "52 %, body centred cubic 68 %, અને બે close-packed ગોઠવણી 74 % ભરે છે."),
            math("APF = volume of atoms in the cell / volume of the cell",
                 "BCC: atoms touch along the body diagonal, 4R = a sqrt(3), so a = 4R/sqrt(3), n = 2",
                 "      APF = 2 (4/3 pi R^3)/(4R/sqrt(3))^3 = pi sqrt(3)/8 = 0.680",
                 "FCC: atoms touch along the face diagonal, 4R = a sqrt(2), so a = 2 sqrt(2) R, n = 4",
                 "      APF = 4 (4/3 pi R^3)/(2 sqrt(2) R)^3 = pi/(3 sqrt(2)) = 0.740"),
            eq("APF BCC = pi sqrt(3)/8 = 0.68", "APF FCC = APF HCP = pi/(3 sqrt(2)) = 0.74"),
            table([tr("Structure", "રચના"), tr("APF", "APF"), tr("Empty space", "ખાલી જગ્યા"),
                   tr("What the gap is used for", "જગ્યાનો ઉપયોગ")],
                  [[tr("Simple cubic", "Simple cubic"), tr("0.52", "0.52"), tr("48 %", "48 %"),
                    tr("no engineering metal uses it", "કોઈ ઇજનેરી ધાતુ તેનો ઉપયોગ કરતી નથી")],
                   [tr("BCC", "BCC"), tr("0.68", "0.68"), tr("32 %", "32 %"),
                    tr("carbon fits only in the small holes, 0.025 % solubility",
                       "carbon ફક્ત નાના છિદ્રોમાં બેસે, 0.025 % દ્રાવ્યતા")],
                   [tr("FCC / HCP", "FCC / HCP"), tr("0.74", "0.74"), tr("26 %", "26 %"),
                    tr("the larger holes take 2 % carbon - why FCC iron is used for carburising",
                       "મોટા છિદ્રો 2 % carbon લે - તેથી carburising માં FCC iron વપરાય")]]),
            why("A close-packed structure leaves less empty space, so the same atoms give a larger "
                "density and a slightly larger expansion when heated. The same holes are the reason "
                "carbon dissolves in FCC iron twenty times more easily than in BCC iron, which is the "
                "whole basis of the heat treatment in Unit 2.",
                "Close-packed રચના ઓછી ખાલી જગ્યા રાખે, તેથી એ જ atoms વધુ density આપે અને ગરમ કરવા પર "
                "થોડું વધુ પ્રસરે. એ જ છિદ્રોનાં કારણે carbon FCC iron માં BCC iron કરતાં વીસ ગણું "
                "સહેલાઈથી ઓગળે, જે Unit 2 ના heat treatment નો આખો પાયો છે."),
            check("Sanity check the arithmetic: pi sqrt(3)/8 = 3.1416 x 1.7321/8 = 0.6802 and "
                  "pi/(3 sqrt(2)) = 3.1416/4.2426 = 0.7405. Both must be below 0.8, because spheres "
                  "cannot fill all the space.",
                  "ગણતરી ચકાસો: pi sqrt(3)/8 = 3.1416 x 1.7321/8 = 0.6802 અને pi/(3 sqrt(2)) = "
                  "3.1416/4.2426 = 0.7405. બંને 0.8 થી નીચે જ હોવા જોઈએ, કારણ કે ગોળા આખી જગ્યા ભરી "
                  "શકતા નથી."),
            pit("Using 0.74 for BCC iron because iron is \"close packed\" in daily speech. Iron is BCC "
                "at room temperature, so its APF is 0.68 - it becomes close packed only above 912 C.",
                "રોજિંદી ભાષામાં iron \"close packed\" હોવાથી BCC iron માટે 0.74 વાપરવું. Room "
                "temperature પર iron BCC છે, તેથી તેનું APF 0.68 છે - તે 912 C ઉપર જ close packed થાય."),
            diagram="u1_packing",
            syllabus_item="1.3",
        ),
        card(
            "Density from the unit cell",
            "Unit cell પરથી density",
            p("The density of a metal can be calculated from its cell alone: count the atoms in the "
              "cell, multiply by the atomic mass, and divide by the volume of the cell times "
              "Avogadro's number. The answer comes within one per cent of the handbook value, which is "
              "the best proof that the cell model is right.",
              "ધાતુની density ફક્ત તેના cell પરથી ગણાય: cell માં atoms ગણો, atomic mass થી ગુણો, અને "
              "cell ના volume ગુણ્યા Avogadro's number થી ભાગો. જવાબ handbook ના મૂલ્યની એક ટકાની "
              "અંદર આવે છે, જે cell model સાચું છે તેનો સૌથી સારો પુરાવો છે."),
            math("rho = n A /(N_A a^3)     n = atoms per cell, a = cell edge, N_A = 6.022e23",
                 "BCC iron: n = 2, A = 55.85, a = 0.2866 nm",
                 "  a^3 = (2.866e-8 cm)^3 = 2.354e-23 cm3",
                 "  rho = 2 x 55.85/(6.022e23 x 2.354e-23) = 111.7/14.18 = 7.88 g/cm3  (measured 7.87)",
                 "FCC copper: n = 4, A = 63.55, a = 0.3615 nm",
                 "  rho = 4 x 63.55/(6.022e23 x 4.725e-23) = 254.2/28.45 = 8.94 g/cm3  (measured 8.96)"),
            h4("Atoms per cubic millimetre", "ઘન મિલીમીટર દીઠ atoms"),
            math("atoms per cell / cell volume = n/a^3",
                 "iron: 2/(2.866e-7 mm)^3 = 2/2.354e-20 = 8.5e19 atoms per mm3"),
            eq("rho = n A/(N_A a^3)", "atoms per unit volume = n/a^3"),
            why("Density is mass per volume, and the cell gives both: n atoms of mass A/N_A inside a "
                "volume a^3. Nothing else is needed, so a density that disagrees with the handbook by "
                "more than a per cent means the wrong cell, the wrong n or the wrong unit of a.",
                "Density એ volume દીઠ દળ છે, અને cell બંને આપે: a^3 volume માં A/N_A દળના n atoms. "
                "બીજું કંઈ જરૂરી નથી, તેથી handbook સાથે એક ટકાથી વધુ ફરક આવે તો ખોટો cell, ખોટો n કે "
                "a નો ખોટો એકમ છે."),
            check("Work in centimetres throughout: 1 nm = 1e-7 cm, so 0.2866 nm = 2.866e-8 cm and "
                  "a^3 = 2.354e-23 cm3. Mixing nanometres with grams per cubic centimetre is the most "
                  "common mistake in the whole calculation.",
                  "આખી ગણતરી સેન્ટીમીટરમાં કરો: 1 nm = 1e-7 cm, તેથી 0.2866 nm = 2.866e-8 cm અને "
                  "a^3 = 2.354e-23 cm3. નેનોમીટરને ગ્રામ પ્રતિ ઘન સેન્ટીમીટર સાથે ભેગા કરવું આખી "
                  "ગણતરીની સૌથી સામાન્ય ભૂલ છે."),
            pit("Using the lattice parameter of one metal for another, or forgetting that a is an edge "
                "and not a radius. The cell edge of iron is 0.287 nm but its atomic radius is 0.124 nm, "
                "and mixing the two changes the density by a factor of ten.",
                "એક ધાતુનો lattice parameter બીજા માટે વાપરવો, કે a radius નહીં પણ edge છે તે ભૂલવું. "
                "iron નો cell edge 0.287 nm છે પણ atomic radius 0.124 nm, અને બંને ભેગા કરવાથી density "
                "દશ ગણી બદલાય."),
            syllabus_item="1.3",
        ),
    ],
})
