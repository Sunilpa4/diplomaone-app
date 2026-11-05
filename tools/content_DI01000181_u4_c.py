"""DI01000181 Unit 4, part C: refractories and insulators."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from subject_DI01000181 import tr  # noqa: E402
from content_DI01000181_lib import (p, h4, table, math, eq, why, check, pit, card,  # noqa: E402
                                    ul, ol)

NOTES_C = []

NOTES_C.append({
    "title": tr("4.4 Refractories and insulators", "4.4 Refractories અને insulators"),
    "items": [
        card(
            "Refractories: the bricks that hold 1500 C",
            "Refractories: 1500 C પકડતી ઈંટો",
            p("A refractory is a ceramic that keeps its shape and its strength in a furnace - above "
              "about 1500 C, in contact with slag, flue gas and a heat cycle. Four numbers describe "
              "one: its <b>refractoriness</b> (the pyrometric cone equivalent, PCE), its "
              "<b>refractoriness under load</b> (RUL, the temperature at which it softens by 0.5 % "
              "under 0.2 MPa), its <b>porosity</b> (15 - 25 % in a firebrick) and its resistance to "
              "<b>spalling</b>, the cracking that a heat cycle causes. Fireclay is the cheap general "
              "brick, silica serves glass tanks, magnesia and dolomite serve steel ladles.",
              "Refractory એ ceramic છે જે ભઠ્ઠીમાં આકાર અને તાકાત જાળવે - લગભગ 1500 C ઉપર, slag, flue gas "
              "અને ગરમી-ઠંડીના ચક્રના સંપર્કમાં. ચાર આંકડા તેને વર્ણવે: <b>refractoriness</b> (pyrometric "
              "cone equivalent, PCE), <b>refractoriness under load</b> (RUL, 0.2 MPa નીચે 0.5 % નરમ પડે તે "
              "તાપમાન), <b>porosity</b> (firebrick માં 15 - 25 %) અને <b>spalling</b> સામે ટકાવારી, એટલે "
              "ગરમી-ઠંડીના ચક્રથી પડતી તિરાડ. Fireclay સસ્તી સામાન્ય ઈંટ છે, silica glass tank માટે, "
              "magnesia અને dolomite steel ladle માટે."),
            math("heat through two layers in series:  q = dT / (L1/k1 + L2/k2)",
                 "R1 = 0.230/1.00 = 0.230      R2 = 0.115/0.12 = 0.958      sum = 1.188 m2 K/W",
                 "q = (1200 - 50)/1.188 = 968 W per m2",
                 "interface: T = 1200 - 968 x 0.230 = 977 C",
                 "bare firebrick alone: q = 1150/0.230 = 5000 W per m2, so 80 % is saved"),
            table([tr("refractory", "refractory"), tr("type", "પ્રકાર"),
                   tr("max use", "વધુમાં વધુ"), tr("used in", "ક્યાં વપરાય")],
                  [[tr("fireclay", "fireclay"), tr("semi-acidic", "semi-acidic"),
                    tr("1300 - 1500 C", "1300 - 1500 C"), tr("boiler, kiln, general lining", "boiler, ભઠ્ઠી, સામાન્ય lining")],
                   [tr("silica", "silica"), tr("acidic", "acidic"),
                    tr("1700 C", "1700 C"), tr("glass tank, coke oven", "glass tank, coke ભઠ્ઠી")],
                   [tr("magnesia", "magnesia"), tr("basic", "basic"),
                    tr("2000 C", "2000 C"), tr("steel ladle, cement kiln", "steel ladle, cement ભઠ્ઠી")],
                   [tr("dolomite", "dolomite"), tr("basic", "basic"),
                    tr("1900 C", "1900 C"), tr("converter, ladle lining", "converter, ladle નું lining")],
                   [tr("chromite", "chromite"), tr("neutral", "neutral"),
                    tr("1900 C", "1900 C"), tr("where the slag swings", "જ્યાં slag બદલાય")],
                   [tr("graphite", "graphite"), tr("neutral", "neutral"),
                    tr("2000 C", "2000 C"), tr("monolithic, tap hole", "monolithic, tap hole (છિદ્ર)")],
                   [tr("ceramic fibre", "ceramic fibre"), tr("insulating", "અવાહક"),
                    tr("1260 C", "1260 C"), tr("furnace back-up layer", "ભઠ્ઠીનું પાછળનું સ્તર")]]),
            why("thermal resistances in series add exactly like electrical ones. The same heat has to "
                "cross both layers, so the temperature drop divides in proportion to L/k: 0.230 "
                "against 0.958 means the thin insulating layer takes 81 % of the drop while the thick "
                "firebrick takes 19 %.",
                "series માં thermal resistance બરાબર electrical જેમ જોડાય. એ જ ઉષ્મા બંને સ્તર પાર કરે, તેથી "
                "તાપમાનનો ઘટાડો L/k ના પ્રમાણમાં વહેંચાય: 0.230 સામે 0.958 એટલે પાતળું અવાહક સ્તર 78 % "
                "ઘટાડો લે જ્યારે જાડી firebrick 19 %."),
            pit("matching the slag matters more than the maximum temperature. A silica brick rated "
                "1700 C is eaten through in a few weeks by a basic steel slag, while a magnesia brick "
                "rated lower lasts a campaign in the same place.",
                "Slag મેળવવો વધુમાં વધુ તાપમાન કરતાં વધુ મહત્વનો છે. 1700 C રેટેડ silica ઈંટ basic steel "
                "slag થી થોડા અઠવાડિયામાં ખાઈ જાય, જ્યારે ઓછું રેટેડ magnesia ઈંટ એ જ જગ્યાએ આખું "
                "campaign ટકે."),
            diagram="u4_refract",
        ),
        card(
            "Insulators: stopping a current and stopping a heat flow are two jobs",
            "Insulators: current રોકવો અને ઉષ્મા રોકવી બે જુદાં કામ",
            p("An electrical insulator is judged by its <b>dielectric strength</b>, in kV per mm, and "
              "by its resistivity; a thermal insulator is judged by its conductivity, in W/m K, and "
              "the two lists hardly overlap. Porcelain, glass, epoxy, bakelite, PTFE and dry "
              "transformer oil stop current; glass wool, rock wool, thermocol, ceramic fibre and "
              "aerogel stop heat. The best insulator of all is a still gas - air is 0.026 W/m K and "
              "3 kV/mm - which is why foams, wools and aerogels are mostly trapped air.",
              "Electrical insulator તેની <b>dielectric strength</b>, kV પ્રતિ mm, અને resistivity થી "
              "આંકવાય; thermal insulator તેની conductivity, W/m K, થી, અને બંને યાદી ભાગ્યે જ મળે. "
              "Porcelain, glass, epoxy, bakelite, PTFE અને સૂકું transformer oil current રોકે; glass wool, "
              "rock wool, thermocol, ceramic fibre અને aerogel ઉષ્મા રોકે. સૌથી સારો insulator સ્થિર વાયુ "
              "છે - હવા 0.026 W/m K અને 3 kV/mm - તેથી foam, wool અને aerogel માં મોટે ભાગે ફસાયેલી હવા "
              "હોય છે."),
            math("insulator thickness for a given withstand voltage:  t = V x SF / E_b",
                 "11 kV busbar, factor of safety 3 -> withstand 33 kV",
                 "porcelain E_b = 15 kV/mm:  t = 33/15 = 2.2 mm, so a 3 mm wall is specified",
                 "3 mm of porcelain breaks down at 3 x 15 = 45 kV, a factor of 4.1 on 11 kV",
                 "heat: q = k A dT/L; 50 mm of glass wool at 0.040 W/m K loses 8.0 W per m2 over 10 K"),
            table([tr("insulator", "insulator"), tr("type", "પ્રકાર"), tr("figure", "આંકડો"),
                   tr("used for", "ઉપયોગ")],
                  [[tr("porcelain", "porcelain"), tr("electrical", "વીજ"), tr("15 kV/mm", "15 kV/mm"),
                    tr("line insulator, bushing", "લાઇન insulator, bushing")],
                   [tr("epoxy resin", "epoxy resin"), tr("electrical", "વીજ"), tr("20 kV/mm", "20 kV/mm"),
                    tr("CT, busbar support", "CT, busbar support")],
                   [tr("PTFE", "PTFE"), tr("electrical", "વીજ"), tr("24 kV/mm", "24 kV/mm"),
                    tr("terminal, spacer", "terminal, spacer")],
                   [tr("transformer oil", "transformer oil"), tr("electrical", "વીજ"), tr("12 kV/mm", "12 kV/mm"),
                    tr("cooling and insulation", "ઠંડક અને insulation")],
                   [tr("glass wool", "glass wool"), tr("thermal", "ઉષ્મા"), tr("0.040 W/m K", "0.040 W/m K"),
                    tr("furnace, duct, pipe", "ભઠ્ઠી, duct, પાઇપ")],
                   [tr("aerogel", "aerogel"), tr("thermal", "ઉષ્મા"), tr("0.015 W/m K", "0.015 W/m K"),
                    tr("thin wall, cryogenic", "પાતળી દીવાલ, cryogenic")],
                   [tr("ceramic fibre", "ceramic fibre"), tr("thermal", "ઉષ્મા"), tr("0.10 W/m K", "0.10 W/m K"),
                    tr("furnace lining back-up", "ભઠ્ઠી lining નું પાછળનું સ્તર")]]),
            why("conduction needs something to carry the energy - electrons, or atoms that pass a "
                "vibration along. A still gas has neither, so the trick of every thermal insulator is "
                "to divide a solid into fine cells that hold the gas still; the same reason makes a "
                "dry, dusty surface a far better insulator than a wet one.",
                "વહન માટે ઊર્જા ઉપાડનારું કંઈક જોઈએ - electrons, કે કંપન આગળ પસાર કરતા atoms. સ્થિર વાયુમાં "
                "બંને નથી, તેથી દરેક thermal insulator ની યુક્તિ એ છે કે ઘનને નાના કોષોમાં વહેંચીને વાયુને સ્થિર "
                "રાખવો; એ જ કારણે સૂકી, ધૂળવાળી સપાટી ભીની કરતાં ઘણી સારી અવાહક બને."),
            pit("a damp insulator is a conductor. Water on a porcelain surface drops the surface "
                "resistivity from about 1e16 to 1e8 ohm and the creepage path flashes over, which is "
                "why outdoor insulators have sheds and a long leakage distance.",
                "ભીનું insulator conductor છે. Porcelain ની સપાટી પરનું પાણી surface resistivity 1e16 થી "
                "1e8 ohm સુધી ઘટાડે અને creepage પથ flash over થાય, તેથી બહારના insulator માં છત્રી અને લાંબું "
                "leakage અંતર હોય."),
            check("for an 11 kV support, write three numbers: the withstand voltage, the kV/mm of the "
                  "material and the thickness. Then check the surface path separately - thickness "
                  "stops the puncture, distance stops the flashover.",
                  "11 kV support માટે ત્રણ આંકડા લખો: withstand વોલ્ટેજ, સામગ્રીનું kV/mm અને જાડાઈ. પછી "
                  "સપાટીનો રસ્તો અલગ ચકાસો - જાડાઈ puncture રોકે, અંતર flashover રોકે."),
            diagram="u4_insul",
        ),
    ],
})
