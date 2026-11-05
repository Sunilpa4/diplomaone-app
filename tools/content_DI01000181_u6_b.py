"""DI01000181 Unit 6, part B: the automotive sector - the car and its battery."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from subject_DI01000181 import tr  # noqa: E402
from content_DI01000181_lib import (p, h4, table, math, eq, why, check, pit, card,  # noqa: E402
                                    ul, ol)

NOTES_B = []

NOTES_B.append({
    "title": tr("6.2 Green materials in the automotive sector",
                "6.2 ઓટોમોબાઇલ ક્ષેત્રે green materials"),
    "items": [
        card(
            "The materials of an electric car",
            "ઇલેક્ટ્રિક કારની સામગ્રી",
            p("An electric car is not built of new materials; it is the old list rearranged around a "
              "battery. Of 1500 kg, 675 kg is still steel and high strength steel for the body and the "
              "safety cage, 300 kg is aluminium for bonnet, doors and subframe, 225 kg is the pack, 180 "
              "kg is polymer and composite, 75 kg is copper and 45 kg is glass. What changed is the "
              "copper - 75 kg against 23 kg in a car with an engine, because the motor windings, the "
              "busbars and the charger all carry heavy current - and the pack, which is 15 % of the car "
              "and 100 % of the new material problem.",
              "ઇલેક્ટ્રિક કાર નવી સામગ્રીની બનતી નથી; એ જૂની યાદી છે જે battery ફરતે ગોઠવાઈ છે. 1500 કિલોમાં "
              "675 કિલો હજી સ્ટીલ અને high strength steel છે - body અને safety cage માટે, 300 કિલો "
              "aluminium - bonnet, દરવાજા અને subframe, 225 કિલો pack, 180 કિલો polymer અને composite, "
              "75 કિલો copper અને 45 કિલો કાચ. બદલાયું છે copper - એન્જિન વાળી કારના 23 કિલો સામે 75 કિલો, "
              "કારણ કે motor winding, busbar અને charger બધા ભારે current વહન કરે - અને pack, જે કારના "
              "15 % અને નવી સામગ્રી સમસ્યાના 100 % છે."),
            math("the two numbers that drive every material decision on the car:",
                 "mass: every 100 kg removed is about 0.4 kWh less per 100 km",
                 "so 300 kg of aluminium instead of steel is 1.2 kWh per 100 km, about 8 %",
                 "and the pack that stores 35 kWh weighs 225 kg: 155 Wh per kg of pack"),
            table([tr("material", "સામગ્રી"), tr("mass, kg", "દળ, kg"),
                   tr("why it is there", "કેમ છે"), tr("green issue", "green મુદ્દો")],
                  [[tr("steel and AHSS", "સ્ટીલ અને AHSS"), tr("675", "675"),
                    tr("crash structure, 1500 MPa in the pillars", "crash માળખું, pillar માં 1500 MPa"),
                    tr("85 % recycled, easy to sort", "85 % recycled, છૂટું પડે સહેલું")],
                   [tr("aluminium", "aluminium"), tr("300", "300"),
                    tr("half the weight of steel", "સ્ટીલ કરતાં અડધું દળ"),
                    tr("170 MJ/kg, but 8 from scrap", "170 MJ/kg, પણ scrap થી 8")],
                   [tr("battery pack", "battery pack"), tr("225", "225"),
                    tr("35 kWh of energy on board", "બોર્ડ પર 35 kWh ઊર્જા"),
                    tr("Li, Ni and Co recovery needed", "Li, Ni અને Co recovery જરૂરી")],
                   [tr("polymers", "polymer"), tr("180", "180"),
                    tr("bumpers, trim, insulation", "bumper, trim, insulation"),
                    tr("9 % recycled worldwide", "દુનિયાભરમાં 9 % recycled")],
                   [tr("copper", "copper"), tr("75", "75"),
                    tr("windings, busbars, 12 V and HV wiring", "winding, busbar, 12 V અને HV wiring"),
                    tr("high value, well recycled", "ઊંચી કિંમત, સારી રીતે recycled")]]),
            why("lightweighting and greening pull in the same direction up to a point and then pull "
                "apart: aluminium saves fuel in service but costs seven times the embodied energy of the "
                "steel it replaces, and CFRP saves more fuel still at 500 MJ/kg and with no melting "
                "route at end of life. The green car is therefore not the lightest car; it is the car "
                "whose saved energy has paid back its extra energy.",
                "lightweighting અને greening એક બિંદુ સુધી એક જ દિશામાં ખેંચે, પછી અલગ પડે: aluminium સેવામાં "
                "બળતણ બચાવે પણ તે બદલતા સ્ટીલ કરતાં સાત ગણી embodied energy માંગે, અને CFRP 500 MJ/kg પર "
                "વધુ બચાવે પણ અંતે ઓગાળવાનો રસ્તો નથી. તેથી green કાર સૌથી હલકી કાર નથી; એ કાર છે જેની "
                "બચાવેલી ઊર્જાએ તેની વધારાની ઊર્જા ચૂકવી નાખી છે."),
            pit("a battery pack is not a fuel tank that can be drained and scrapped. It is 225 kg of "
                "material with a second life as a stationary store, and only then a recycling problem - "
                "so write the end-of-life route into the design, not into the disposal contract.",
                "battery pack એ ખાલી કરીને ભંગાર કરી શકાય તેવી fuel ટાંકી નથી. એ 225 કિલો સામગ્રી છે જેનું "
                "બીજું જીવન stationary store તરીકે છે, અને પછી જ recycling સમસ્યા - તેથી end-of-life માર્ગ "
                "design માં લખો, disposal કરારમાં નહીં."),
            check("when a part is made lighter, ask two questions: how many kilometres before the extra "
                  "energy is paid back, and what happens to this material at end of life. A 12 kg steel "
                  "subframe replaced by primary aluminium never pays back inside 200 000 km; the same "
                  "part in 60 % recycled aluminium pays back in 180 000 km, and in scrap-only aluminium "
                  "it saves energy from the first kilometre.",
                  "ભાગ હલકો કરો ત્યારે બે પ્રશ્ન પૂછો: વધારાની ઊર્જા પાછી મળતાં કેટલા કિલોમીટર, અને અંતે આ "
                  "સામગ્રીનું શું થાય. 12 કિલોનું સ્ટીલ subframe primary aluminium થી બદલો તો 200,000 "
                  "કિલોમીટરમાં પણ payback થતું નથી; એ જ ભાગ 60 % recycled aluminium માં 180,000 કિલોમીટરમાં "
                  "payback થાય, અને ફક્ત scrap ના aluminium માં પહેલા કિલોમીટરથી ઊર્જા બચે."),
            diagram="u6_ev",
        ),
        card(
            "The battery: five materials, one cell",
            "Battery: પાંચ સામગ્રી, એક cell",
            p("A lithium-ion cell is five materials stacked 150 micrometres thick: an aluminium foil "
              "current collector, a cathode of lithium metal oxide 60 micrometres thick, a separator "
              "with liquid electrolyte 20 micrometres, a graphite anode 50 micrometres, and a copper "
              "foil. Lithium does not sit in the electrodes as metal; it sits <b>inside</b> the crystal "
              "lattice of the cathode and the graphite - intercalation - and moves back and forth on "
              "every charge, which is why the cell ages by counting cycles rather than by corroding.",
              "લિથિયમ-ion cell એ 150 માઇક્રોમીટર જાડાઈમાં ગોઠવાયેલી પાંચ સામગ્રી છે: aluminium foil "
              "current collector, 60 માઇક્રોમીટર જાડું lithium metal oxide નું cathode, 20 માઇક્રોમીટરનું "
              "separator અને liquid electrolyte, 50 માઇક્રોમીટરનું graphite anode, અને copper foil. "
              "લિથિયમ ધાતુ તરીકે electrode માં બેસતું નથી; તે cathode અને graphite ના crystal lattice "
              "<b>અંદર</b> બેસે - intercalation - અને દરેક charge પર આમતેમ ફરે, તેથી cell કાટ ખાઈને નહીં, "
              "cycle ગણીને વૃદ્ધ થાય."),
            math("cell 3.7 V and 50 Ah:",
                 "energy = 3.7 x 50 = 185 Wh, and mass about 0.9 kg -> 205 Wh per kg of cell",
                 "96 in series: 355 V and 50 Ah = 17.8 kWh; two strings in parallel: 35.5 kWh",
                 "the pack weighs 236 kg, so 150 Wh per kg of pack - 73 % of it is cells"),
            table([tr("chemistry", "chemistry"), tr("Wh/kg cell", "cell Wh/kg"),
                   tr("cycles", "cycle"), tr("where it wins", "ક્યાં જીતે")],
                  [[tr("lead-acid", "lead-acid"), tr("35", "35"), tr("400", "400"),
                    tr("cost, and it is 99 % recycled", "કિંમત, અને 99 % recycled")],
                   [tr("LFP", "LFP"), tr("140", "140"), tr("3000", "3000"),
                    tr("safety, life, no cobalt", "સલામતી, આયુષ્ય, cobalt નહીં")],
                   [tr("NMC", "NMC"), tr("220", "220"), tr("1500", "1500"),
                    tr("range in a small pack", "નાના pack માં વધુ અંતર")],
                   [tr("LTO", "LTO"), tr("70", "70"), tr("20 000", "20 000"),
                    tr("fast charge, cold, buses", "ઝડપી charge, ઠંડી, બસ")],
                   [tr("sodium-ion", "sodium-ion"), tr("140", "140"), tr("3000", "3000"),
                    tr("no lithium, cheap salt", "લિથિયમ નહીં, સસ્તું ક્ષાર")]]),
            why("the cathode is the expensive, the heavy and the contested part: nickel and cobalt cost "
                "money and come from few countries, so LFP - iron and phosphorus - has come back and now "
                "carries most of the world's new car cells. The anode, the separator and the electrolyte "
                "set the safety: a separator that shuts its pores at 130 C is a safety device, not a "
                "packing sheet.",
                "cathode મોંઘો, ભારે અને વિવાદિત ભાગ છે: nickel અને cobalt પૈસા માગે અને થોડા દેશોમાંથી "
                "આવે, તેથી LFP - લોહ અને ફોસ્ફરસ - પાછું આવ્યું અને હવે દુનિયાના નવા car cell મોટા ભાગે "
                "તે જ છે. anode, separator અને electrolyte સલામતી નક્કી કરે: 130 C પર છિદ્ર બંધ કરતું "
                "separator સલામતીનું સાધન છે, પેકિંગ કાગળ નહીં."),
            pit("capacity fade is not 'the battery wearing out'. It is lithium lost to side reactions, "
                "cracks in the cathode particles and a growing film on the anode - and a cell kept at "
                "45 C ages about twice as fast as one kept at 25 C, which is why the pack has a cooling "
                "plate and not just a box.",
                "capacity ઘટવું એ 'battery ઘસાઈ જવું' નથી. એ આડી પ્રક્રિયાઓમાં ગુમાવેલું લિથિયમ, cathode "
                "કણોમાં તિરાડો અને anode પર વધતી ફિલ્મ છે - અને 45 C પર રખાયેલો cell 25 C કરતાં લગભગ બમણો "
                "ઝડપથી વૃદ્ધ થાય, તેથી pack માં ફક્ત ખોખું નહીં, cooling plate હોય."),
            check("read a pack spec as three numbers and not one: kWh (range), kg (the mass it costs) and "
                  "cycles (the life). 35 kWh at 150 Wh/kg and 1500 cycles is a different product from 35 "
                  "kWh at 120 Wh/kg and 3000 cycles, even though both say 35 kWh on the label.",
                  "pack ની spec એક નહીં, ત્રણ આંકડા તરીકે વાંચો: kWh (અંતર), kg (જે દળ ખર્ચે) અને cycle "
                  "(આયુષ્ય). 150 Wh/kg અને 1500 cycle વાળું 35 kWh, 120 Wh/kg અને 3000 cycle વાળા 35 kWh "
                  "કરતાં જુદું ઉત્પાદન છે, જોકે બંને લેબલ પર 35 kWh લખે."),
            diagram="u6_batt",
        ),
    ],
})
