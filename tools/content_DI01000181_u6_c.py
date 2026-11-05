"""DI01000181 Unit 6, part C: renewable energy - solar, wind and hydro materials."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from subject_DI01000181 import tr  # noqa: E402
from content_DI01000181_lib import (p, h4, table, math, eq, why, check, pit, card,  # noqa: E402
                                    ul, ol)

NOTES_C = []

NOTES_C.append({
    "title": tr("6.3 Green materials in renewable energy", "6.3 નવીનીકરણીય ઊર્જામાં green materials"),
    "items": [
        card(
            "A solar panel is mostly not silicon",
            "સોલાર પેનલ મોટે ભાગે silicon નથી",
            p("A photovoltaic module converts 20 % of the sunlight that reaches it, so four fifths of "
              "the area is there to hold, protect and cool the cells. On 2 m2 the cells make 400 W at "
              "1000 W/m2 - the standard test condition - and after the inverter and the wiring a "
              "0.8 performance ratio turns 4 peak sun hours into 1.28 kWh a day. The materials are "
              "therefore a system: 3.2 mm toughened glass, EVA encapsulant, the cells, a backsheet, an "
              "anodised aluminium frame and a junction box, and the frame and glass are 70 % of the "
              "module mass.",
              "ફોટોવોલ્ટેઇક module પર પડતા સૂર્યપ્રકાશના 20 % ને વીજળીમાં ફેરવે, તેથી પાંચમાંથી ચાર ભાગ "
              "ક્ષેત્ર cell પકડવા, બચાવવા અને ઠંડા રાખવા માટે હોય. 2 m2 પર 1000 W/m2 - standard test "
              "condition - આગળ cell 400 W બનાવે, અને inverter તથી wiring પછી 0.8 performance ratio 4 peak "
              "sun hour ને દિવસના 1.28 kWh માં ફેરવે. તેથી સામગ્રી એક તંત્ર છે: 3.2 mm toughened કાચ, EVA "
              "encapsulant, cell, backsheet, anodised aluminium frame અને junction box, અને frame તથી કાચ "
              "module ના દળના 70 % છે."),
            math("2 m2 module, 20 % cells, at Surat's 5 peak sun hours:",
                 "peak power = 1000 x 2 x 0.20 = 400 W",
                 "daily energy = 0.4 kW x 5 h x 0.8 = 1.6 kWh, and 3 modules give 4.8 kWh",
                 "area for a 4 kWh a day house = 4/(1 x 0.2 x 5 x 0.8) = 5 m2 of module"),
            table([tr("layer", "સ્તર"), tr("material", "સામગ્રી"),
                   tr("job", "કામ"), tr("why this one", "આ જ કેમ")],
                  [[tr("cover", "cover"), tr("3.2 mm low iron glass", "3.2 mm low iron કાચ"),
                    tr("hail, 25 years of UV", "કરા, 25 વર્ષ UV"),
                    tr("92 % transmission, and it does not yellow", "92 % transmission, પીળું નહીં પડે")],
                   [tr("encapsulant", "encapsulant"), tr("EVA sheet", "EVA શીટ"),
                    tr("seals the cell from water", "cell ને પાણીથી સીલ કરે"),
                    tr("melts and cross-links at 150 C", "150 C પર ઓગળી cross-link થાય")],
                   [tr("cell", "cell"), tr("mono silicon, 20 - 22 %", "mono silicon, 20 - 22 %"),
                    tr("the only part that works", "કામ કરતો એકમાત્ર ભાગ"),
                    tr("150 micrometre wafer of pure silicon", "શુદ્ધ silicon નું 150 માઇક્રોમીટર wafer")],
                   [tr("frame", "frame"), tr("anodised aluminium", "anodised aluminium"),
                    tr("stiffness, mounting", "કઠોરતા, mounting"),
                    tr("extruded, so no machining", "extruded, તેથી machining નહીં")],
                   [tr("backsheet", "backsheet"), tr("PET and aluminium foil", "PET અને aluminium foil"),
                    tr("electrical insulation", "વિદ્યુત insulation"),
                    tr("blocks water vapour at 0.1 g per m2 a day", "દિવસે 0.1 g પ્રતિ m2 બાષ્પ રોકે")]]),
            why("efficiency is a material property and area is what a roof has, so the choice runs the "
                "other way from a machine: a house short of roof buys mono silicon at 22 % and pays for "
                "it, a solar farm with land buys 17 % thin film because the cost per kWh, not the cost "
                "per square metre, is what it sells. The glass, frame and backsheet are the same in "
                "both, which is why they are 70 % of the mass.",
                "efficiency સામગ્રીનો ગુણધર્મ છે અને છત પાસે ક્ષેત્ર હોય છે, તેથી પસંદગી મશીનથી ઊલટી દિશામાં "
                "ચાલે: છત ઓછી હોય તે ઘર 22 % નું mono silicon ખરીદે અને ભરે, જમીન વાળું સોલાર ફાર્મ 17 % "
                "thin film ખરીદે કારણ કે તે પ્રતિ kWh કિંમત વેચે, પ્રતિ ચોરસ મીટર નહીં. કાચ, frame અને "
                "backsheet બંનેમાં એક જ છે, તેથી જ તે દળના 70 % છે."),
            pit("a panel is not a material that can be left to the weather. The encapsulant is the life "
                "limiting part: a pinhole lets water in, the EVA hydrolyses to acetic acid, and the acid "
                "eats the silver fingers on the cell. A 25 year warranty is a statement about the "
                "laminate, not about the silicon.",
                "પેનલ એ હવામાન પર છોડી દેવાય તેવી સામગ્રી નથી. encapsulant જ આયુષ્ય મર્યાદિત કરે: નાનું છિદ્ર "
                "પાણી અંદર લે, EVA hydrolyse થઈ acetic acid બને, અને એસિડ cell પરની silver finger ખાઈ જાય. "
                "25 વર્ષની warranty laminate વિશે છે, silicon વિશે નહીં."),
            check("size a panel in three steps and never in one: energy needed per day, energy one module "
                  "gives in a day at your peak sun hours, and the number of modules rounded up. Surat "
                  "gives about 5 peak sun hours, not the 4 of a European roof.",
                  "પેનલ ત્રણ પગલામાં માપો, એકમાં નહીં: દિવસની જરૂરી ઊર્જા, તમારા peak sun hour આગળ એક "
                  "module દિવસમાં કેટલી આપે, અને module ની સંખ્યા ઉપર તરફ પૂર્ણાંકમાં. સુરત લગભગ 5 peak sun "
                  "hour આપે, યુરોપની છતના 4 નહીં."),
            diagram="u6_solar",
        ),
        card(
            "Wind and hydro: where the tonnes are",
            "પવન અને જળ: ટન ક્યાં છે",
            p("A 3 MW wind turbine is 300 tonnes of material for 3 MW, and almost all of it is ordinary: "
              "200 tonnes of steel in the tower, 20 tonnes of cast iron in the hub and the gearbox "
              "casing, and 60 tonnes of blade. The blade is the interesting part - glass fibre and epoxy "
              "for the shell, carbon fibre in the spar caps that carry the bending - because it must be "
              "25 % lighter than steel for the same stiffness and must survive 10^8 load cycles in salt "
              "air. A direct-drive machine trades the gearbox for 2 tonnes of NdFeB magnets.",
              "3 MW નું પવન turbine 3 MW માટે 300 ટન સામગ્રી છે, અને લગભગ બધું સામાન્ય: tower માં 200 ટન "
              "સ્ટીલ, hub અને gearbox casing માં 20 ટન cast iron, અને blade માં 60 ટન. blade રસપ્રદ ભાગ છે "
              "- shell માટે glass fibre અને epoxy, bending ઉપાડતા spar cap માં carbon fibre - કારણ કે એ જ "
              "કઠોરતા માટે સ્ટીલ કરતાં 25 % હલકું હોવું જોઈએ અને ખારા હવામાં 10^8 load cycle ઝીલવા પડે. "
              "direct-drive મશીન gearbox બદલે 2 ટન NdFeB magnet માંગે."),
            math("why the blade is a composite and the tower is not:",
                 "specific stiffness of steel = 200/7.85 = 25 GPa per g per cm3",
                 "of glass epoxy = 40/1.9 = 21, of carbon epoxy = 120/1.6 = 75",
                 "so a 80 m blade needs carbon in the spar, and a tower does not"),
            table([tr("machine", "મશીન"), tr("the material that matters", "મહત્ત્વની સામગ્રી"),
                   tr("the number", "આંકડો"), tr("the failure it prevents", "જે નિષ્ફળતા રોકે")],
                  [[tr("wind blade", "પવન blade"), tr("glass and carbon epoxy", "glass અને carbon epoxy"),
                    tr("60 t for 3 MW, 10^8 cycles", "3 MW માટે 60 ટન, 10^8 cycle"),
                    tr("fatigue at the root", "root પર fatigue")],
                   [tr("wind tower", "પવન tower"), tr("S355 steel plate", "S355 સ્ટીલ પ્લેટ"),
                    tr("200 t, 120 m", "200 ટન, 120 મીટર"),
                    tr("buckling, and welded fatigue", "buckling, અને weld fatigue")],
                   [tr("direct drive", "direct drive"), tr("NdFeB magnets", "NdFeB magnet"),
                    tr("2 t of magnet, 1.3 T", "2 ટન magnet, 1.3 T"),
                    tr("gearbox failure disappears", "gearbox નિષ્ફળતા જતી રહે")],
                   [tr("hydro runner", "જળ runner"), tr("13Cr-4Ni martensitic stainless", "13Cr-4Ni martensitic stainless"),
                    tr("5 - 15 t, 300 m head", "5 - 15 ટન, 300 મીટર head"),
                    tr("cavitation and silt erosion", "cavitation અને કાંપ ઘસારો")]]),
            why("renewable energy is material-intensive in a way a power station is not: a coal plant "
                "concentrates 500 MW in one building, while a wind farm spreads the same rating over 20 "
                "km2 of blades and towers. The material bill per kWh is therefore dominated by the "
                "structure and not by the generator, and the recycling question arrives 25 years later as "
                "60 tonnes of thermoset blade that cannot be melted.",
                "નવીનીકરણીય ઊર્જા એ રીતે સામગ્રી-ભારે છે જે રીતે વીજળી ઘર નથી: કોલસા પ્લાન્ટ 500 MW એક મકાનમાં "
                "એકઠા કરે, જ્યારે પવન ફાર્મ એ જ ક્ષમતા 20 km2 માં blade અને tower પર ફેલાવે. તેથી પ્રતિ kWh "
                "સામગ્રીનું બિલ મોટે ભાગે માળખાનું હોય, generator નું નહીં, અને recycling નો પ્રશ્ન 25 વર્ષ પછી "
                "60 ટન thermoset blade તરીકે આવે જે ઓગળે નહીં."),
            pit("the greenest machine has the hardest waste. A thermoset blade cannot be re-melted, so "
                "most of the 60 tonnes ends in cement kilns as fuel and filler; a thermoplastic blade is "
                "now being made precisely so that it can be melted back into a new one.",
                "સૌથી green મશીનનો કચરો સૌથી અઘરો હોય. thermoset blade ફરી ઓગળે નહીં, તેથી 60 ટનમાંથી "
                "મોટો ભાગ સિમેન્ટ ભઠ્ઠીમાં બળતણ અને filler તરીકે જાય; thermoplastic blade હવે એટલા માટે જ "
                "બનાવાય છે કે તે ઓગળીને નવું બની શકે."),
            check("count the tonnes before praising the megawatt: a 3 MW turbine is 300 tonnes of "
                  "material, so its 6 g CO2 per kWh is a statement about 25 years of service and not "
                  "about the machine in the yard today.",
                  "megawatt ની પ્રશંસા પહેલાં ટન ગણો: 3 MW turbine 300 ટન સામગ્રી છે, તેથી તેનું 6 g CO2 પ્રતિ "
                  "kWh 25 વર્ષની સેવા વિશે છે, આજે યાર્ડમાં ઊભેલા મશીન વિશે નહીં."),
        ),
    ],
})
