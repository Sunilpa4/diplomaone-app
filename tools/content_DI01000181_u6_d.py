"""DI01000181 Unit 6, part D: sustainable materials in industry, and advanced automotive materials."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from subject_DI01000181 import tr  # noqa: E402
from content_DI01000181_lib import (p, h4, table, math, eq, why, check, pit, card,  # noqa: E402
                                    ul, ol)

NOTES_D = []

NOTES_D.append({
    "title": tr("6.4 Sustainable and renewable materials in mechanical industries",
                "6.4 યાંત્રિક ઉદ્યોગોમાં ટકાઉ અને નવીનીકરણીય સામગ્રી"),
    "items": [
        card(
            "Bio-based and recycled materials on the shop floor",
            "કારખાનાના ફ્લોર પર bio-based અને recycled સામગ્રી",
            p("Three families are already in production and not in a laboratory. <b>Natural fibre "
              "composites</b> - jute, hemp, flax in a PLA or epoxy matrix - give 40 to 60 MPa at a "
              "density of 1.4, so a third of the specific strength of glass fibre but at 4 to 10 MJ/kg "
              "instead of 30 to 50. <b>Biolubricants</b> from vegetable esters have a viscosity index of "
              "180 to 220, far above the 95 of a mineral oil, and are 90 % biodegraded in 28 days. "
              "<b>Recycled metals</b> are the strongest case: secondary aluminium at 8 MJ/kg and "
              "electric steel at 10 MJ/kg are the same metals, not substitutes.",
              "ત્રણ કુટુંબ હવે ઉત્પાદનમાં છે, પ્રયોગશાળામાં નહીં. <b>કુદરતી રેસા composite</b> - jute, hemp, "
              "flax, PLA કે epoxy matrix માં - 1.4 ઘનતા પર 40 થી 60 MPa આપે, એટલે glass fibre ના specific "
              "strength નો ત્રીજો ભાગ, પણ 30 - 50 MJ/kg ને બદલે 4 - 10 MJ/kg પર. <b>Biolubricant</b> વનસ્પતિ "
              "ester માંથી બને છે, તેનો viscosity index 180 - 220, mineral oil ના 95 કરતાં ઘણો ઊંચો, અને "
              "28 દિવસમાં 90 % biodegraded થાય. <b>Recycled ધાતુ</b> સૌથી મજબૂત કેસ છે: 8 MJ/kg નું secondary "
              "aluminium અને 10 MJ/kg નું electric સ્ટીલ એ જ ધાતુ છે, વિકલ્પ નહીં."),
            math("the comparison a designer actually makes, specific strength in kN m per kg:",
                 "jute-epoxy: 50 MPa/1.4 = 36;  GFRP: 300/1.9 = 158;  CFRP: 1500/1.6 = 938",
                 "embodied energy: jute 8, glass fibre 40, carbon fibre 400 MJ/kg",
                 "so a natural fibre panel is 5 times lighter in energy and 4 times heavier in mass"),
            table([tr("material", "સામગ્રી"), tr("strength", "મજબૂતાઈ"),
                   tr("MJ/kg", "MJ/kg"), tr("where it is used", "ક્યાં વપરાય")],
                  [[tr("jute - PLA", "jute - PLA"), tr("40 MPa, E 4 GPa", "40 MPa, E 4 GPa"),
                    tr("8", "8"), tr("door trim, parcel shelf", "દરવાજાનો ટ્રિમ, parcel shelf")],
                   [tr("flax - epoxy", "flax - epoxy"), tr("60 MPa, E 6 GPa", "60 MPa, E 6 GPa"),
                    tr("12", "12"), tr("boat hull, sports panels", "હોડીનું હલ, sports પેનલ")],
                   [tr("bamboo", "વાંસ"), tr("150 MPa along fibre", "રેસા દિશામાં 150 MPa"),
                    tr("3", "3"), tr("scaffold boards, flooring", "scaffold બોર્ડ, ફ્લોરિંગ")],
                   [tr("cork", "કોર્ક"), tr("1 MPa, but 0.5 g/cm3", "1 MPa, પણ 0.5 g/cm3"),
                    tr("4", "4"), tr("gaskets, insulation, grips", "gasket, insulation, grip")],
                   [tr("recycled PP", "recycled PP"), tr("25 MPa", "25 MPa"),
                    tr("30", "30"), tr("battery trays, liners", "battery tray, liner")],
                   [tr("biolubricant", "biolubricant"), tr("VI 180 - 220", "VI 180 - 220"),
                    tr("20", "20"), tr("chainsaw, rail, hydraulic in forest", "chainsaw, rail, જંગલમાં hydraulic")]]),
            why("the natural fibre is weaker than glass, so it does not win on strength - it wins on "
                "energy, mass per kilogram of fibre and on what happens at the end: a jute-PLA panel can "
                "be composted, and a glass fibre panel cannot. Where the load is low and the volume is "
                "high - door trims, parcel shelves, packaging trays - that is enough.",
                "કુદરતી રેસા કાચ કરતાં નબળું છે, તેથી મજબૂતાઈમાં જીતતું નથી - તે ઊર્જામાં, રેસાના કિલોગ્રામ "
                "દીઠ દળમાં અને અંતમાં શું થાય તેમાં જીતે: jute-PLA પેનલ compost થઈ શકે, glass fibre પેનલ "
                "નહીં. જ્યાં ભાર ઓછો અને જથ્થો મોટો હોય - દરવાજાનો ટ્રિમ, parcel shelf, પેકેજિંગ ટ્રે - ત્યાં "
                "એ પૂરતું છે."),
            pit("bio-based does not mean compostable and compostable does not mean strong. A PLA part "
                "softens at 60 C, so a dashboard moulding in PLA sags in a parked car in a Surat summer; "
                "the fibre is chosen for the load and the matrix for the temperature, separately.",
                "bio-based એ compostable નથી અને compostable એ મજબૂત નથી. PLA ભાગ 60 C પર નરમ પડે, તેથી "
                "PLA નું dashboard moulding સુરતના ઉનાળામાં પાર્ક કરેલી કારમાં નમી જાય; રેસા ભાર માટે અને "
                "matrix તાપમાન માટે અલગ અલગ પસંદ થાય."),
            check("on a shop floor the greenest move is usually the cheapest one: segregate the swarf by "
                  "alloy and sell it as a grade instead of as mixed scrap, use a water-based coolant with "
                  "a tramp oil separator, and cut dry where the material allows. None of it needs a new "
                  "material, only a new habit.",
                  "કારખાનામાં સૌથી green પગલું ઘણી વાર સૌથી સસ્તું હોય: swarf ને alloy પ્રમાણે અલગ કરીને "
                  "mixed scrap ને બદલે grade તરીકે વેચો, tramp oil separator વાળું water-based coolant વાપરો, "
                  "અને સામગ્રી પરવાનગી આપે ત્યાં dry cut કરો. એમાં નવી સામગ્રી નહીં, નવી ટેવ જોઈએ."),
        ),
    ],
})

NOTES_D.append({
    "title": tr("6.5 Advanced materials for the automotive sector",
                "6.5 ઓટોમોબાઇલ ક્ષેત્ર માટે advanced materials"),
    "items": [
        card(
            "Advanced materials: light, strong, magnetic, cool",
            "Advanced materials: હલકી, મજબૂત, ચુંબકીય, ઠંડી",
            p("The advanced material in a modern car is chosen for a number, not for a name. "
              "<b>Lightweighting</b> is judged by specific strength: steel 57, aluminium and magnesium "
              "115, GFRP 158, titanium 260, CFRP 938 kN m per kg - and a body-in-white that was 400 kg "
              "of steel can be 250 kg in aluminium and AHSS. <b>Magnets</b> are the second: an NdFeB "
              "traction motor gives 1.3 T and 250 to 400 kJ/m3 of energy product, which is why a 150 kW "
              "motor fits in a bag-sized housing. <b>Thermal materials</b> are the third: Al-SiC and "
              "graphite spread the heat of a 200 A inverter, and a 700 bar hydrogen tank is a CFRP "
              "winding with a polymer liner.",
              "આધુનિક કારમાં advanced material નામ માટે નહીં, આંકડા માટે પસંદ થાય. <b>Lightweighting</b> "
              "specific strength થી મપાય: સ્ટીલ 57, aluminium અને magnesium 115, GFRP 158, titanium 260, "
              "CFRP 938 kN m પ્રતિ kg - અને 400 કિલો સ્ટીલનું body-in-white aluminium અને AHSS માં 250 કિલો "
              "થઈ શકે. <b>Magnet</b> બીજું: NdFeB traction motor 1.3 T અને 250 - 400 kJ/m3 energy product "
              "આપે, તેથી 150 kW motor થેલી જેટલા housing માં આવે. <b>Thermal સામગ્રી</b> ત્રીજું: Al-SiC અને "
              "graphite 200 A inverter ની ગરમી ફેલાવે, અને 700 bar hydrogen ટાંકી polymer liner પર CFRP "
              "winding છે."),
            math("the three numbers behind an advanced material choice:",
                 "specific strength = UTS/density: steel 450/7.85 = 57, CFRP 1500/1.6 = 938",
                 "magnet energy product: NdFeB 250 - 400 kJ/m3 against ferrite 30 kJ/m3",
                 "700 bar tank: 5 kg of hydrogen in 100 kg of CFRP, 5 % by mass"),
            table([tr("part", "ભાગ"), tr("advanced material", "advanced સામગ્રી"),
                   tr("number", "આંકડો"), tr("replaces", "બદલે")],
                  [[tr("body structure", "body માળખું"), tr("AHSS 1500 MPa, hot stamped", "AHSS 1500 MPa, hot stamped"),
                    tr("3 times the strength of mild steel", "mild સ્ટીલ કરતાં 3 ગણી મજબૂતાઈ"),
                    tr("thicker mild steel", "જાડું mild સ્ટીલ")],
                   [tr("closures", "closures"), tr("aluminium 6061 sheet", "aluminium 6061 શીટ"),
                    tr("2.7 g/cm3, 300 MPa", "2.7 g/cm3, 300 MPa"),
                    tr("steel at 7.85", "7.85 નું સ્ટીલ")],
                   [tr("motor", "motor"), tr("NdFeB magnet, 1.3 T", "NdFeB magnet, 1.3 T"),
                    tr("150 kW in 40 kg", "40 કિલોમાં 150 kW"),
                    tr("ferrite and a bigger frame", "ferrite અને મોટું frame")],
                   [tr("brake disc", "બ્રેક ડિસ્ક"), tr("Al-SiC composite", "Al-SiC composite"),
                    tr("40 % lighter, 400 C stable", "40 % હલકું, 400 C સ્થિર"),
                    tr("grey cast iron", "grey cast iron")],
                   [tr("hydrogen tank", "hydrogen ટાંકી"), tr("CFRP over HDPE liner", "HDPE liner પર CFRP"),
                    tr("700 bar, 5 kg of H2", "700 bar, 5 કિલો H2"),
                    tr("steel at 300 bar", "300 bar નું સ્ટીલ")]]),
            why("an advanced material is a trade of money against a number that the customer can feel: "
                "CFRP gives 938 kN m per kg and costs thirty times a steel sheet, so it goes where the "
                "number is worth the money - a Formula car, a 700 bar tank, a blade tip - and stays out "
                "of a hatchback floor. The engineering judgement is knowing which number the part is "
                "actually bought for.",
                "advanced સામગ્રી પૈસા અને ગ્રાહકને અનુભવાય તેવા આંકડા વચ્ચેનો સોદો છે: CFRP 938 kN m પ્રતિ "
                "kg આપે અને સ્ટીલ શીટ કરતાં ત્રીસ ગણું મોંઘું પડે, તેથી એ ત્યાં જાય જ્યાં આંકડો પૈસા જેટલો "
                "કીમતી હોય - Formula કાર, 700 bar ટાંકી, blade ની ટોચ - અને hatchback ના ફ્લોરથી દૂર રહે. "
                "એન્જિનિયરિંગની સમજ એ છે કે ભાગ ખરેખર કયા આંકડા માટે ખરીદાય છે."),
            pit("the lightest material is often the least green: CFRP carries 500 MJ/kg and no melting "
                "route, aluminium carries 170 and recycles at 8. Fitting the greenest available material "
                "is therefore a whole-life calculation, and on a car it usually ends at aluminium and "
                "AHSS, not at carbon.",
                "સૌથી હલકી સામગ્રી ઘણી વાર સૌથી ઓછી green હોય: CFRP 500 MJ/kg અને ઓગાળવાનો રસ્તો નહીં, "
                "aluminium 170 અને 8 પર recycle. તેથી ઉપલબ્ધ સૌથી green સામગ્રી લગાવવી એ આખા જીવનનું "
                "ગણિત છે, અને કાર પર એ સામાન્ય રીતે aluminium અને AHSS પર પૂરું થાય, carbon પર નહીં."),
            check("justify an advanced material with three sentences: the number it improves, the money "
                  "it costs per kilogram, and what happens to the part at end of life. A material that "
                  "cannot answer the third sentence is a prototype, not a production choice.",
                  "advanced સામગ્રીને ત્રણ વાક્યથી ન્યાય આપો: જે આંકડો સુધારે, પ્રતિ કિલોગ્રામ કેટલો ખર્ચ, "
                  "અને ભાગનું અંતે શું થાય. ત્રીજા વાક્યનો જવાબ ન આપી શકે તે સામગ્રી prototype છે, "
                  "ઉત્પાદનની પસંદગી નહીં."),
            diagram="u6_light",
        ),
    ],
})
