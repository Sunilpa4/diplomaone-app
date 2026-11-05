"""DI01000181 Unit 1, part B: section 1.2 - the five kinds of bond and what they decide."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from subject_DI01000181 import tr  # noqa: E402
from content_DI01000181_lib import p, h4, table, math, eq, why, check, pit, card  # noqa: E402

NOTES_B = []

NOTES_B.append({
    "title": tr("1.2 Types of bonds and their characteristics",
                "1.2 બંધનના પ્રકાર અને તેમની લાક્ષણિકતાઓ"),
    "items": [
        card(
            "The five kinds of bond",
            "બંધનના પાંચ પ્રકાર",
            p("Atoms join because the joined state has less energy than the separate atoms. There are "
              "only five ways to do it, and they differ in one thing: where the electrons go. An "
              "electron may be transferred, shared, donated by one atom, shared through a hydrogen "
              "bridge, or given up to a pool that belongs to the whole crystal.",
              "Atoms જોડાય છે કારણ કે જોડાયેલી સ્થિતિની ઊર્જા અલગ atoms કરતાં ઓછી હોય છે. તે કરવાની "
              "ફક્ત પાંચ રીતો છે, અને તેમાં ફરક એક જ છે: electrons ક્યાં જાય છે. Electron transferred "
              "થઈ શકે, shared થઈ શકે, એક atom દાન આપી શકે, hydrogen bridge દ્વારા shared થઈ શકે, કે "
              "આખા crystal ના pool માં જતો રહે."),
            table([tr("Bond", "બંધન"), tr("How it is formed", "કેવી રીતે બને"),
                   tr("One property it explains", "એક ગુણધર્મ જે સમજાવે"), tr("Example", "ઉદાહરણ")],
                  [[tr("Electrovalent (ionic)", "Electrovalent (ionic)"),
                    tr("a metal atom loses electrons, a non-metal gains them",
                       "ધાતુ atom electrons ગુમાવે, અધાતુ મેળવે"),
                    tr("high melting point but brittle and soluble", "ઊંચું ગલનબિંદુ પણ ભંગુર અને દ્રાવ્ય"),
                    tr("NaCl, MgO, CaF2", "NaCl, MgO, CaF2")],
                   [tr("Covalent", "Covalent"),
                    tr("two atoms share a pair of electrons", "બે atoms electrons ની જોડી share કરે"),
                    tr("very hard, very high melting point, insulator", "ખૂબ સખત, ઊંચું ગલનબિંદુ, અવાહક"),
                    tr("diamond, silicon carbide, Si", "diamond, silicon carbide, Si")],
                   [tr("Coordinate (dative)", "Coordinate (dative)"),
                    tr("one atom donates both electrons of the pair",
                       "એક atom જોડીના બંને electrons દાન કરે"),
                    tr("explains complex ions and catalysts", "complex ions અને catalysts સમજાવે"),
                    tr("NH3 -> BF3, [Cu(NH3)4]2+", "NH3 -> BF3, [Cu(NH3)4]2+")],
                   [tr("Hydrogen", "Hydrogen"),
                    tr("H of one molecule is attracted to O, N or F of another",
                       "એક molecule નો H બીજા molecule ના O, N કે F તરફ ખેંચાય"),
                    tr("low melting point, high boiling point for its size",
                       "નીચું ગલનબિંદુ, પોતાના માપ માટે ઊંચું ઉકળતું બિંદુ"),
                    tr("water, ice, DNA, cellulose", "water, ice, DNA, cellulose")],
                   [tr("Metallic", "Metallic"),
                    tr("atoms leave their outer electrons in a common pool",
                       "atoms પોતાના બહારના electrons સામાન્ય pool માં છોડે"),
                    tr("conducts heat and current, deforms without breaking",
                       "heat અને current વહન કરે, તૂટ્યા વગર deform થાય"),
                    tr("all metals and alloys", "બધી ધાતુઓ અને alloy")]]),
            math("bond energy (kJ/mol):  H-bond 20  <  metallic Fe-Fe 415  <  ionic NaCl 787",
                 "melting point (C):      ice 0  <  iron 1538  <  rock salt 801",
                 "the stronger the bond, the more heat needed to break it"),
            why("Properties are the bond seen from the outside. A bond that cannot slide explains a "
                "brittle solid; a bond with mobile electrons explains conduction; a bond made of weak "
                "attractions explains why water boils at 100 C but the water molecule itself does not "
                "break until far above that.",
                "ગુણધર્મો એ બહારથી દેખાતું બંધન છે. જે બંધન સરકી ન શકે તે ભંગુર ઘન સમજાવે; જે બંધનમાં "
                " electrons હલે તે વાહકતા સમજાવે; નબળા આકર્ષણનું બંધન સમજાવે કે પાણી 100 C પર કેમ ઉકળે "
                "પણ પાણીનું molecule ઘણા ઊંચા temperature સુધી તૂટતું નથી."),
            check("Predict first, then check: a solid with a melting point above 1000 C and no "
                  "conductivity is covalent or ionic; one that conducts and dents before breaking is "
                  "metallic; one that softens at 120 C is held by hydrogen bonds or van der Waals "
                  "forces.",
                  "પહેલા અનુમાન કરો, પછી ચકાસો: 1000 C થી ઊંચું ગલનબિંદુ અને વાહકતા નહીં તેવો ઘન "
                  "covalent કે ionic છે; જે વહન કરે અને તૂટતા પહેલા દબાય તે metallic છે; જે 120 C પર મૃદુ "
                  "પડે તે hydrogen bonds કે van der Waals થી જોડાયેલો છે."),
            pit("Calling a covalent bond weak because carbon is light. The C-C bond is one of the "
                "strongest known (348 kJ/mol in diamond's network); it is the crystal that is brittle, "
                "not the bond that is weak.",
                "Carbon હલકું છે તેથી covalent bond નબળું ગણવું. C-C bond જાણીતા સૌથી મજબૂત bonds માં "
                "એક છે (diamond ના network માં 348 kJ/mol); ભંગુર crystal છે, bond નબળું નથી."),
            diagram="u1_bonds",
            syllabus_item="1.2",
        ),
        card(
            "What the bond decides: strength, melting point and conduction",
            "બંધન શું નક્કી કરે: તાકાત, ગલનબિંદુ અને વહન",
            p("Bond energy is the energy needed to pull one mole of atoms apart. It is measured in "
              "kilojoules per mole and it runs parallel to the melting point, because melting means "
              "breaking the bonds far enough for the atoms to slide. The same number also decides the "
              "elastic modulus, the hardness and the thermal expansion.",
              "Bond energy એ એક mole atoms અલગ કરવા જરૂરી ઊર્જા છે. તે કિલોજૂલ પ્રતિ mole માં મપાય છે "
              "અને ગલનબિંદુ સાથે સમાંતર ચાલે છે, કારણ કે ગલન એટલે bonds એટલા તોડવા કે atoms સરકી શકે. "
              "એ જ આંકડો elastic modulus, hardness અને thermal expansion પણ નક્કી કરે છે."),
            math("H-bond 20 kJ/mol -> ice melts at 0 C",
                 "Fe-Fe metallic 415 kJ/mol -> iron melts at 1538 C",
                 "NaCl ionic 787 kJ/mol -> rock salt melts at 801 C",
                 "C-C covalent 348 kJ/mol -> graphite sublimes near 3650 C"),
            h4("Why a strong bond does not mean a strong part",
               "મજબૂત bond એટલે મજબૂત ભાગ નહીં, કેમ"),
            p("A high bond energy makes the material hard and heat resistant, but it also makes it "
              "brittle: if the atoms cannot slide, a crack cannot be blunted, and the part breaks "
              "without warning. Toughness needs a bond that can slide a little - which is exactly what "
              "the metallic bond provides.",
              "ઊંચી bond energy સામગ્રીને સખત અને ગરમી સહેનારી બનાવે, પણ ભંગુર પણ બનાવે: atoms સરકી "
              "ન શકે તો crack શમી ન શકે અને ભાગ ચેતવણી વગર તૂટે. Toughness માટે થોડું સરકી શકે તેવું "
              "બંધન જોઈએ - જે metallic bond આપે છે."),
            eq("bond energy -> melting point, modulus, hardness", "mobile electrons -> conduction, ductility"),
            why("Melting is a bond-breaking process, so the heat of fusion and the melting temperature "
                "both scale with bond energy. Conduction is an electron-movement process, so it appears "
                "only where the electrons are free: metals and graphite, not ceramics or polymers.",
                "ગલન એ bond તૂટવાની પ્રક્રિયા છે, તેથી heat of fusion અને ગલનબિંદુ બંને bond energy સાથે "
                "વધે. વહન એ electrons હલવાની પ્રક્રિયા છે, તેથી તે ફક્ત ત્યાં દેખાય જ્યાં electrons મુક્ત "
                "હોય: ધાતુઓ અને graphite, ceramics કે polymers નહીં."),
            check("Two materials can have the same melting point and different toughness. Compare "
                  "alumina (2050 C, brittle) with iron (1538 C, tough): the melting point follows the "
                  "bond energy, the toughness follows whether the bond can slide.",
                  "બે સામગ્રીનું ગલનબિંદુ સરખું અને toughness જુદું હોઈ શકે. alumina (2050 C, ભંગુર) ને "
                  "iron (1538 C, tough) સાથે સરખાવો: ગલનબિંદુ bond energy પાછળ જાય, toughness bond સરકી "
                  "શકે છે કે નહીં તેની પાછળ જાય."),
            pit("Reading a bond-energy table as if it were a strength table. Bond energy is per mole "
                "of bonds; the strength of a part depends also on how many bonds cross a square "
                "millimetre - diamond and polythene differ in both.",
                "Bond-energy કોષ્ટકને તાકાતના કોષ્ટક જેવું વાંચવું. Bond energy એક mole bonds દીઠ છે; "
                "ભાગની તાકાત એના પર પણ આધારે છે કે એક ચોરસ મિલીમીટર કેટલા bonds કાપે - diamond અને "
                "polythene બંનેમાં જુદા પડે."),
            diagram="u1_bondenergy",
            syllabus_item="1.2",
        ),
    ],
})
