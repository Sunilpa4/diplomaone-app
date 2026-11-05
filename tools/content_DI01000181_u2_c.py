"""DI01000181 Unit 2, part C: sections 2.5 and 2.6 - the iron-carbon diagram and heat treatment."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from subject_DI01000181 import tr  # noqa: E402
from content_DI01000181_lib import (p, h4, table, math, eq, why, check, pit, card,  # noqa: E402
                                    ul, ol)

NOTES_C = []

NOTES_C.append({
    "title": tr("2.5 The iron-iron carbide diagram", "2.5 Iron-iron carbide diagram અને તેનાં બિંદુઓ"),
    "items": [
        card(
            "Iron changes its own lattice, and that is the whole subject",
            "Iron પોતાનું lattice બદલે છે, અને આખો વિષય એમાં જ છે",
            p("Pure iron is <b>allotropic</b>: between 912 C and 1394 C it is FCC (austenite, γ), below "
              "912 C and above 1394 C it is BCC (ferrite, α, and the high-temperature δ which is also "
              "BCC). The FCC lattice has a bigger hole in the middle, so austenite can hold 2.14 % "
              "carbon while ferrite holds only 0.02 %. That single fact explains the whole heat "
              "treatment of steel: heat it into the austenite range, the carbon dissolves; cool it "
              "slowly, the carbon comes back out as cementite; cool it fast, the carbon is trapped.",
              "શુદ્ધ iron <b>allotropic</b> છે: 912 C થી 1394 C વચ્ચે તે FCC (austenite, γ) છે, 912 C "
              "ની નીચે અને 1394 C ની ઉપર BCC (ferrite, α, અને ઊંચા temperature નું δ જે પણ BCC છે) છે. FCC "
              "lattice માં વચ્ચેની ખાલી જગ્યા મોટી હોય છે, તેથી austenite 2.14 % carbon રાખી શકે જ્યારે "
              "ferrite ફક્ત 0.02 % રાખે. આ એક જ હકીકત સ્ટીલની આખી heat treatment સમજાવે છે: austenite ના "
              "વિસ્તારમાં ગરમ કરો તો carbon ઓગળે; ધીમે ઠંડું કરો તો carbon cementite સ્વરૂપે પાછું નીકળે; "
              "ઝડપથી ઠંડું કરો તો carbon ફસાઈ જાય."),
            table([tr("Point", "બિંદુ"), tr("C %", "C %"), tr("T (C)", "T (C)"),
                   tr("Meaning", "અર્થ")],
                  [[tr("A", "A"), tr("0", "0"), tr("1538", "1538"), tr("melting point of pure iron", "શુદ્ધ iron નું ગલનબિંદુ")],
                   [tr("N", "N"), tr("0", "0"), tr("1394", "1394"), tr("δ -> γ (BCC to FCC)", "δ -> γ (BCC થી FCC)")],
                   [tr("G", "G"), tr("0", "0"), tr("912", "912"), tr("γ -> α, the A3 of pure iron", "γ -> α, શુદ્ધ iron નું A3")],
                   [tr("E", "E"), tr("2.14", "2.14"), tr("1147", "1147"), tr("most carbon austenite can hold", "austenite રાખી શકે તેવો વધુમાં વધુ carbon")],
                   [tr("C", "C"), tr("4.3", "4.3"), tr("1147", "1147"), tr("eutectic: L -> γ + Fe3C (ledeburite)", "eutectic: L -> γ + Fe3C (ledeburite) એટલે પ્રવાહીમાંથી બે ઘન")],
                   [tr("S", "S"), tr("0.8", "0.8"), tr("727", "727"), tr("eutectoid: γ -> α + Fe3C (pearlite)", "eutectoid: γ -> α + Fe3C (pearlite) એટલે ઘનમાંથી બે ઘન")],
                   [tr("P", "P"), tr("0.02", "0.02"), tr("727", "727"), tr("carbon left in ferrite", "ferrite માં બચતો carbon")],
                   [tr("K", "K"), tr("6.67", "6.67"), tr("727", "727"), tr("cementite, Fe3C", "cementite, Fe3C")]]),
            math("eutectic  (1147 C):  L(4.3 % C)  ->  gamma(2.14 %) + Fe3C(6.67 %)   F = 0",
                 "eutectoid (727 C):   gamma(0.8 % C) -> alpha(0.02 %) + Fe3C(6.67 %)  F = 1",
                 "",
                 "steel:      0.02 to 2.14 % C   (hypoeutectoid below 0.8, hypereutectoid above)",
                 "cast iron:  2.14 to 6.67 % C  (eutectic, so it is cast, not rolled)"),
            why("The line E-S (the Acm) and the line G-S (the A3) are the two boundaries a heat "
                "treater aims at. Heat a 0.4 % steel above A3 and it becomes all austenite; hold it "
                "there and the carbon is evenly spread; cool it and whatever you cool it into is the "
                "structure you get. Every heat treatment is a choice of temperature on this diagram "
                "and a choice of cooling rate off it.",
                "E-S રેખા (Acm) અને G-S રેખા (A3) એ બે સીમા છે જેને heat treater ધ્યાનમાં રાખે. 0.4 % "
                "સ્ટીલને A3 ઉપર ગરમ કરો તો આખું austenite થાય; ત્યાં રાખો તો carbon સરખો ફેલાય; ઠંડું "
                "કરો તો જેમાં ઠંડું કરો તે structure મળે. દરેક heat treatment એ આ diagram પર temperature "
                "ની પસંદગી અને તેની ઉપરથી cooling rate ની પસંદગી છે."),
            pit("Cementite is not a phase you can see as a metal - it is a compound, Fe3C, 6.67 % "
                "carbon, hard and brittle. Pearlite is not a third phase either: it is a two-phase "
                "mixture of ferrite and cementite, and it is called a micro-constituent, not a phase.",
                "Cementite એ ધાતુ તરીકે દેખાતો phase નથી - તે compound Fe3C છે, 6.67 % carbon, સખત અને "
                "ભંગુર. Pearlite પણ ત્રીજો phase નથી: તે ferrite અને cementite નું બે-phase મિશ્રણ છે, "
                "તેને micro-constituent કહે છે, phase નહીં."),
            diagram="u2_fec",
        ),
        card(
            "The three steels across the eutectoid, and what carbon does",
            "Eutectoid આસપાસનાં ત્રણ સ્ટીલ, અને carbon શું કરે",
            p("Cool a steel slowly from the austenite range and the microstructure that comes out "
              "depends on one number, the carbon content. Below 0.8 % the first thing to form is "
              "<b>proeutectoid ferrite</b>, which grows as pale grains, and the remaining austenite "
              "then turns into pearlite at 727 C - so the micrograph is ferrite with islands of "
              "pearlite. At exactly 0.8 % the whole grain is pearlite. Above 0.8 % the first thing "
              "out is <b>proeutectoid cementite</b>, which appears as a bright network on the old "
              "austenite grain boundaries, and the rest is pearlite.",
              "Austenite વિસ્તારથી સ્ટીલને ધીમે ઠંડું કરો તો નીકળતું microstructure એક જ આંકડા પર "
              "આધારે છે, carbon content. 0.8 % થી નીચે પહેલું બનતું <b>proeutectoid ferrite</b> છે, જે "
              "આછા grains તરીકે વધે, અને બાકીનું austenite પછી 727 C પર pearlite થાય - તેથી micrograph "
              "માં ferrite વચ્ચે pearlite ના ટાપુઓ દેખાય. બરાબર 0.8 % પર આખો grain pearlite હોય. 0.8 % થી "
              "ઉપર પહેલું નીકળતું <b>proeutectoid cementite</b> છે, જે જૂની austenite grain boundary પર "
              "તેજસ્વી જાળી તરીકે દેખાય, અને બાકીનું pearlite."),
            math("pearlite % = (C - 0.02)/(0.80 - 0.02) x 100      Fe3C % = (C - 0.80)/(6.67 - 0.80) x 100",
                 "",
                 "0.4 % C:  pearlite = 0.38/0.78 = 48.7 %   ferrite = 51.3 %",
                 "0.8 % C:  pearlite = 1.00/0.78 = 100 %",
                 "1.2 % C:  Fe3C = 0.40/5.87 = 6.8 %       pearlite = 93.2 %",
                 "",
                 "in 5 kg of 0.4 % steel: 2.44 kg pearlite and 2.56 kg ferrite"),
            table([tr("Carbon", "Carbon"), tr("Microstructure", "Microstructure"),
                   tr("Strength", "તાકાત"), tr("Ductility", "Ductility"), tr("Used for", "ક્યાં વપરાય")],
                  [[tr("0.1 - 0.2 %", "0.1 - 0.2 %"), tr("mostly ferrite", "મોટે ભાગે ferrite"),
                    tr("low, ~400 MPa UTS", "ઓછી, ~400 MPa UTS"), tr("very high", "ખૂબ ઊંચી"),
                    tr("sheet, wire, nails, car body", "પાતળી ચાદર, તાર, ખીલા, car body")],
                   [tr("0.3 - 0.5 %", "0.3 - 0.5 %"), tr("ferrite + pearlite", "ferrite + pearlite"),
                    tr("medium, ~600 MPa UTS", "મધ્યમ, ~600 MPa UTS"), tr("good", "સારી"),
                    tr("shafts, gears, axles, rails", "ધરી, ગિયર, axles, rails")],
                   [tr("0.8 %", "0.8 %"), tr("all pearlite", "આખું pearlite"),
                    tr("high, ~800 MPa UTS", "ઊંચી, ~800 MPa UTS"), tr("low", "ઓછી"),
                    tr("springs, piano wire, cutting edges", "સ્પ્રિંગ, piano wire, cutting edges")],
                   [tr("1.0 - 1.4 %", "1.0 - 1.4 %"), tr("pearlite + Fe3C network", "pearlite + Fe3C જાળી"),
                    tr("very high, but brittle", "ખૂબ ઊંચી, પણ ભંગુર"), tr("very low", "ખૂબ ઓછી"),
                    tr("files, razors, ball bearings, dies", "પાની, razors, ball bearings, dies")]]),
            check("Ask which is stronger and the answer is not simply 'more carbon'. Up to about 0.8 % "
                  "carbon raises strength; above it the cementite network makes the steel brittle, so "
                  "toughness falls even though hardness rises.",
                  "કયું વધુ મજબૂત છે એ પૂછો તો જવાબ ફક્ત 'વધુ carbon' નથી. લગભગ 0.8 % સુધી carbon તાકાત "
                  "વધારે; તેનાથી ઉપર cementite ની જાળી સ્ટીલને ભંગુર કરે, તેથી hardness વધે પણ toughness "
                  "ઘટે."),
            diagram="u2_micro",
        ),
    ],
})

NOTES_C.append({
    "title": tr("2.6 The concept of heat treatment", "2.6 Heat treatment નો ખ્યાલ"),
    "items": [
        card(
            "Heat treatment: three steps, one purpose",
            "Heat treatment: ત્રણ પગલાં, એક હેતુ",
            p("<b>Heat treatment</b> is the controlled heating and cooling of a solid metal to change "
              "its structure, and through the structure its properties - without changing the shape "
              "of the part and without changing its composition. Every treatment has the same three "
              "steps: <b>heat</b> to a chosen temperature and hold it until the structure is uniform, "
              "then <b>cool</b> at a chosen rate. The temperature decides what structure you start "
              "from; the cooling rate decides what structure you finish with.",
              "<b>Heat treatment</b> એ ઘન ધાતુને નિયંત્રિત રીતે ગરમ કરીને અને ઠંડી કરીને તેની રચના "
              "બદલવી છે, અને રચના દ્વારા તેના ગુણધર્મો - ભાગનો આકાર બદલ્યા વગર અને composition બદલ્યા "
              "વગર. દરેક treatment માં એ જ ત્રણ પગલાં છે: પસંદ કરેલા temperature સુધી <b>ગરમ કરો</b> અને "
              "રચના સરખી ન થાય ત્યાં સુધી રાખો, પછી પસંદ કરેલા દરથી <b>ઠંડું કરો</b>. Temperature નક્કી "
              "કરે કે કઈ રચનાથી શરૂ કરવું; cooling rate નક્કી કરે કે કઈ રચના પર પૂરું કરવું."),
            table([tr("Treatment", "Treatment"), tr("Heat to", "કેટલું ગરમ"),
                   tr("Cool by", "કેવી રીતે ઠંડું"), tr("What it gives", "શું મળે")],
                  [[tr("Full annealing", "Full annealing"), tr("30-50 C above A3 (or A1 for hypereutectoid)", "A3 થી 30-50 C ઉપર (hypereutectoid માટે A1)"),
                    tr("furnace cooling, very slow", "furnace માં, ખૂબ ધીમે"),
                    tr("soft, coarse pearlite; easy to machine", "નરમ, જાડું pearlite; machining સહેલું")],
                   [tr("Normalising", "Normalising"), tr("30-50 C above A3", "A3 થી 30-50 C ઉપર"),
                    tr("still air", "શાંત હવામાં"),
                    tr("finer pearlite, higher strength than annealed", "નાનું pearlite, annealed કરતાં વધુ તાકાત")],
                   [tr("Hardening", "Hardening"), tr("30-50 C above A3 or Acm", "A3 કે Acm થી 30-50 C ઉપર"),
                    tr("quench in water, oil or brine", "water, oil કે brine માં quench"),
                    tr("martensite: hardest, most brittle", "martensite: સૌથી સખત, સૌથી ભંગુર")],
                   [tr("Tempering", "Tempering"), tr("below A1, 150-650 C", "A1 ની નીચે, 150-650 C"),
                    tr("any, then air cool", "કોઈ પણ, પછી હવામાં"),
                    tr("toughness back; hardness set by the temperature", "toughness પાછી; hardness temperature થી નક્કી")],
                   [tr("Case hardening", "Case hardening"), tr("surface only, with carbon or nitrogen", "ફક્ત ઉપરની સપર, carbon કે nitrogen સાથે"),
                    tr("quench after diffusing", "diffuse કરીને quench"),
                    tr("hard skin on a tough core", "તough core પર સખત skin")]]),
            math("A1 = 727 C for every steel (the eutectoid line)",
                 "A3 falls from 912 C at 0 % C to 727 C at 0.8 % C (hypoeutectoid steels)",
                 "Acm rises from 727 C at 0.8 % C to 1147 C at 2.14 % C (hypereutectoid steels)",
                 "",
                 "so 0.4 % C steel is austenitised at about 800-830 C",
                 "and 1.2 % C steel at about 750-780 C - above A1, below Acm"),
            why("Hardening is not about the carbon alone: it is about how fast the austenite is "
                "cooled. Slow cooling gives the carbon time to diffuse out and form cementite; fast "
                "cooling does not, and the carbon is trapped in a strained lattice. That trapped "
                "structure, martensite, is hard because the carbon has nowhere to go - and it is "
                "brittle for the same reason, which is why it is always tempered.",
                "Hardening ફક્ત carbon ની વાત નથી: austenite કેટલી ઝડપથી ઠંડું થાય તેની છે. ધીમે ઠંડું "
                "કરો તો carbon ને બહાર નીકળી cementite બનવા સમય મળે; ઝડપથી કરો તો નહીં, અને carbon "
                "તણાયેલા lattice માં ફસાય. એ ફસાયેલી રચના, martensite, સખત છે કારણ કે carbon ને જવાની "
                "જગ્યા નથી - અને એ જ કારણે ભંગુર પણ છે, તેથી તેને હંમેશા temper કરાય છે."),
            check("The three steps answer three different questions: temperature decides which phase "
                  "you begin with, holding time decides how even it is, cooling rate decides what you "
                  "end with. An answer that mentions only temperature is half an answer.",
                  "ત્રણ પગલાં ત્રણ જુદા પ્રશ્નોના જવાબ છે: temperature નક્કી કરે કયા phase થી શરૂ કરવું, "
                  "holding time નક્કી કરે તે કેટલું સરખું છે, cooling rate નક્કી કરે અંતે શું મળે. ફક્ત "
                  "temperature લખો તો અડધો જવાબ છે."),
            diagram=None,
        ),
    ],
})
