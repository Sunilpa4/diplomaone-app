"""DI01000181 Unit 6, part A: the green material idea and the accounting behind it."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from subject_DI01000181 import tr  # noqa: E402
from content_DI01000181_lib import (p, h4, table, math, eq, why, check, pit, card,  # noqa: E402
                                    ul, ol)

NOTES_A = []

NOTES_A.append({
    "title": tr("6.1 Green materials: the idea and the account",
                "6.1 Green materials: વિચાર અને હિસાબ"),
    "items": [
        card(
            "What makes a material green",
            "સામગ્રી green ક્યારે કહેવાય",
            p("A material is not green or dirty by itself; the whole life of the part it becomes is "
              "green or dirty. Four questions decide it: is the raw material <b>renewable</b>, can the "
              "material be <b>recycled</b> at the end, how much <b>energy, water and emission</b> went "
              "into each kilogram, and does the part <b>last</b>. The fourth question is the one "
              "students forget and designers cannot: a bamboo chair that is reglued every two years "
              "costs more material, more glue and more transport than a steel one that outlives its "
              "owner.",
              "સામગ્રી પોતે green કે ગંદી હોતી નથી; તે જે ભાગ બને તેનું આખું જીવન green કે ગંદું હોય. ચાર "
              "પ્રશ્નો તે નક્કી કરે: કાચો માલ <b>renewable</b> છે કે નહીં, અંતે સામગ્રી <b>recycle</b> થઈ "
              "શકે કે નહીં, દરેક કિલોગ્રામ પાછળ કેટલી <b>ઊર્જા, પાણી અને emission</b> ગઈ, અને ભાગ "
              "<b>ટકે</b> છે કે નહીં. ચોથો પ્રશ્ન વિદ્યાર્થી ભૂલે અને designer ભૂલી ન શકે: દર બે વર્ષે ફરી "
              "ગુંદાયેલી bamboo ખુરશી એ સ્ટીલની ખુરશી કરતાં વધુ સામગ્રી, ગુંદર અને વહન માંગે જે તેના "
              "માલિક કરતાં વધુ ટકે છે."),
            math("the four counts, as a designer writes them:",
                 "renewable: regrown in a human lifetime - wood, bamboo, cork, jute, PLA",
                 "recyclable: a second life at a fraction of the first energy - all metals",
                 "low impact: MJ, litres and kg of CO2 per kilogram delivered",
                 "durable: years of service per kilogram, which multiplies all three"),
            table([tr("material", "સામગ્રી"), tr("renewable", "renewable"),
                   tr("recycled today", "આજે recycle થાય"), tr("the catch", "અડચણ")],
                  [[tr("steel", "સ્ટીલ"), tr("no", "ના"), tr("85 - 90 %", "85 - 90 %"),
                    tr("25 MJ/kg to make", "બનાવવા 25 MJ/kg")],
                   [tr("aluminium", "aluminium"), tr("no", "ના"), tr("75 %", "75 %"),
                    tr("170 MJ/kg new, 8 from scrap", "નવું 170, scrap થી 8 MJ/kg")],
                   [tr("concrete", "concrete"), tr("no", "ના"), tr("little", "થોડું"),
                    tr("1 MJ/kg, but 4 billion tonnes a year", "1 MJ/kg, પણ વર્ષે 4 અબજ ટન")],
                   [tr("timber", "લાકડું"), tr("yes", "હા"), tr("yes", "હા"),
                    tr("1 - 5 MJ/kg, but land and glue", "1 - 5 MJ/kg, પણ જમીન અને ગુંદર")],
                   [tr("CFRP", "CFRP"), tr("no", "ના"), tr("almost none", "લગભગ નહીં"),
                    tr("500 MJ/kg, and it cannot be melted", "500 MJ/kg, અને ઓગળે નહીં")]]),
            why("every kilogram of material carries a bill that was paid before the part existed - a "
                "mine, a furnace, a refinery, a lorry - and that bill is paid again every time the part "
                "is replaced. Green design is therefore mostly arithmetic on mass and life, not a "
                "choice of fashionable material.",
                "ભાગ અસ્તિત્વમાં આવે તે પહેલાં જ દરેક કિલોગ્રામનું બિલ ભરાઈ ગયું હોય છે - ખાણ, ભઠ્ઠી, "
                "રિફાઇનરી, લારી - અને ભાગ બદલાય ત્યારે એ બિલ ફરી ભરાય. તેથી green design મોટે ભાગે દળ "
                "અને આયુષ્યનું ગણિત છે, ફેશનેબલ સામગ્રીની પસંદગી નહીં."),
            pit("a bio-based label is not a life cycle. A jute composite bonded with an epoxy, shipped "
                "wet and painted with a solvent paint can carry more energy than a glass fibre part made "
                "two hundred kilometres away; ask for the MJ per kilogram of the finished part, not of "
                "the fibre.",
                "bio-based લેબલ એ જીવનચક્ર નથી. epoxy સાથે જોડાયેલું, ભીનું વહન થયેલું અને solvent પેન્ટ "
                "કરેલું jute composite બસો કિલોમીટર દૂર બનેલા glass fibre ભાગ કરતાં વધુ ઊર્જા "
                "વાળું હોઈ શકે; fiber નહીં, તૈયાર ભાગના MJ પ્રતિ કિલોગ્રામ માંગો."),
            check("for the part in front of you, write four numbers: mass, embodied energy, expected "
                  "life and what happens at end of life. If any of the four is unknown, the material "
                  "choice is not yet a decision, it is a preference.",
                  "તમારી સામેનો ભાગ લો અને ચાર આંકડા લખો: દળ, embodied energy, અપેક્ષિત આયુષ્ય અને અંતે "
                  "શું થાય. ચારમાંથી એક પણ અજાણ્યો હોય તો સામગ્રીની પસંદગી હજી નિર્ણય નથી, પસંદગી માત્ર છે."),
            diagram="u6_cycle",
        ),
        card(
            "The account: embodied energy, carbon and the payback",
            "હિસાબ: embodied energy, carbon અને payback",
            p("The number that makes the argument is <b>embodied energy</b>: the primary energy needed "
              "to deliver one kilogram of a material ready to use, in MJ/kg. Aluminium is 170 and "
              "concrete is 1, a factor of a hundred and seventy before a single part is machined. "
              "Multiplying by mass gives the bill for the part, and dividing the extra energy of a "
              "lightweight choice by the energy it saves in service gives the <b>energy payback "
              "distance</b> - and that distance, not the mass on the drawing, decides whether the "
              "lighter part is a green part or only a lighter one.",
              "દલીલ કરતો આંકડો છે <b>embodied energy</b>: વાપરવા તૈયાર એક કિલોગ્રામ સામગ્રી પહોંચાડવા જોઈતી "
              "પ્રાથમિક ઊર્જા, MJ/kg માં. aluminium 170 અને concrete 1, એટલે એક ભાગ machined થાય તે પહેલાં જ "
              "સો સિત્તેર ગણો ફરક. દળ સાથે ગુણવાથી ભાગનું બિલ મળે, અને હલકી પસંદગીની વધારાની ઊર્જાને સેવામાં "
              "બચતલી ઊર્જાથી ભાગીએ તો <b>energy payback distance</b> મળે - અને એ અંતર જ નક્કી કરે કે હલકો ભાગ "
              "green ભાગ છે કે ફક્ત હલકો."),
            math("part 12 kg in steel, replaced by 6.19 kg of aluminium that is equally stiff:",
                 "extra embodied energy = 6.19 x 170 - 12 x 25 = 1052 - 300 = 752 MJ",
                 "saving in use for 5.81 kg = 0.4 x 0.0581 = 0.0232 kWh per 100 km = 0.836 kJ/km",
                 "payback = 752/0.000836 = 900 000 km - primary aluminium does not pay back"),
            table([tr("material", "સામગ્રી"), tr("MJ/kg new", "નવું MJ/kg"),
                   tr("MJ/kg recycled", "recycled MJ/kg"), tr("kg CO2 per kg", "kg CO2 પ્રતિ kg")],
                  [[tr("concrete", "concrete"), tr("1", "1"), tr("0.9", "0.9"), tr("0.1", "0.1")],
                   [tr("glass", "કાચ"), tr("15", "15"), tr("12", "12"), tr("1.3", "1.3")],
                   [tr("steel", "સ્ટીલ"), tr("25", "25"), tr("10", "10"), tr("1.9", "1.9")],
                   [tr("PET", "PET"), tr("80", "80"), tr("40", "40"), tr("2.7", "2.7")],
                   [tr("aluminium", "aluminium"), tr("170", "170"), tr("8", "8"), tr("11.5", "11.5")],
                   [tr("CFRP", "CFRP"), tr("500", "500"), tr("300", "300"), tr("25", "25")]]),
            why("the account is additive along the chain, so the biggest number wins: melting recycled "
                "aluminium takes 5 % of the electricity of smelting it from alumina, and that single "
                "fact is why a scrap yard is a mine with better ore. The same arithmetic on steel gives "
                "60 %, on glass 20 % and on a thermoplastic 50 %, because a polymer can only be "
                "re-melted, not re-refined.",
                "હિસાબ સાંકળ પર ઉમેરાય, તેથી સૌથી મોટો આંકડો જીતે: recycled aluminium ઓગાળવા alumina થી "
                "smelt કરતાં 5 % વીજળી જોઈએ, અને એ એક હકીકત જ કારણ છે કે ભંગારનું યાર્ડ સારો ore ધરાવતી "
                "ખાણ છે. એ જ ગણિત સ્ટીલમાં 60 %, કાચમાં 20 % અને thermoplastic માં 50 % આપે, કારણ કે "
                "polymer ફરી ઓગળે, ફરી refine ન થાય."),
            pit("one number is not an LCA. A full life cycle assessment (ISO 14040/14044) adds "
                "extraction, manufacture, transport, use and end of life, and the answer can flip with "
                "the grid: an aluminium part made with hydroelectricity is a different material from the "
                "same part made with coal power.",
                "એક આંકડો LCA નથી. પૂરું life cycle assessment (ISO 14040/14044) extraction, ઉત્પાદન, "
                "વહન, વપરાશ અને અંત જોડે, અને જવાબ grid સાથે ઊલટો થઈ શકે: જળવિદ્યુતથી બનેલો aluminium "
                "ભાગ કોલસાની વીજળીથી બનેલા એ જ ભાગ કરતાં જુદી સામગ્રી છે."),
            check("quote embodied energy per kilogram of the finished part, with the recycling route "
                  "stated: 'aluminium, 170 MJ/kg new, 8 MJ/kg from scrap, 60 % recycled content' is a "
                  "claim that can be checked; 'eco-friendly aluminium' is not.",
                  "તૈયાર ભાગના કિલોગ્રામ દીઠ embodied energy કહો અને recycling માર્ગ પણ: 'aluminium, નવું "
                  "170 MJ/kg, scrap થી 8, 60 % recycled content' ચકાસી શકાય તેવો દાવો છે; "
                  "'eco-friendly aluminium' નથી."),
            diagram="u6_energy",
        ),
    ],
})
