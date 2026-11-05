"""DI01000181 Unit 5, part A: surface engineering, cleaning and mechanical finishing."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from subject_DI01000181 import tr  # noqa: E402
from content_DI01000181_lib import (p, h4, table, math, eq, why, check, pit, card,  # noqa: E402
                                    ul, ol)

NOTES_A = []

NOTES_A.append({
    "title": tr("5.1 Surface engineering, cleaning and mechanical finishing",
                "5.1 Surface engineering, સફાઈ અને mechanical finishing"),
    "items": [
        card(
            "The surface is a different material",
            "સપાટી એ જુદી જ સામગ્રી છે",
            p("Almost nothing fails in the middle of a part. Wear, fretting, fatigue, pitting and "
              "corrosion all begin in the first few micrometres, because that is where the highest "
              "stress, the environment and the relative motion all meet. <b>Surface engineering</b> "
              "is the deliberate control of that zone: a hard film on a tough core for wear, a "
              "barrier for corrosion, a compressive skin for fatigue, a low-friction layer for "
              "sliding. The core keeps the load and the surface takes the attack.",
              "લગભગ કંઈ પણ ભાગની વચ્ચે નિષ્ફળ જતું નથી. ઘસારો, fretting, fatigue, pitting અને કાટ બધું પહેલા "
              "થોડા માઇક્રોમીટરમાં શરૂ થાય, કારણ કે ત્યાં જ સૌથી વધુ stress, પર્યાવરણ અને સાપેક્ષ ગતિ "
              "મળે છે. <b>Surface engineering</b> એ એ જ ઝોનનું જાણી જોઈને નિયંત્રણ છે: ઘસારા માટે લચીલા "
              "core પર સખત ફિલ્મ, કાટ માટે અવરોધ, fatigue માટે સંકોચાયેલું સ્તર, સરકવા માટે ઓછા ઘર્ષણનું "
              "સ્તર. Core લોડ ઉપાડે અને સપાટી હુમલો ઝીલે."),
            math("bending stress varies linearly across the section, so:",
                 "share of the moment in the outer 10 % of the radius = 1 - 0.9^2 = 19 %",
                 "share of the moment in the outer 1 %  = 1 - 0.99^2 = 2 %",
                 "coatings of 5 - 25 micron therefore sit where the stress is already highest"),
            table([tr("what fails", "શું નિષ્ફળ જાય"), tr("surface process", "surface process"),
                   tr("the number", "આંકડો"), tr("life it buys", "કેટલું આયુષ્ય")],
                  [[tr("wear", "ઘસારો"), tr("gas nitriding", "gas nitriding"),
                    tr("900 - 1100 HV skin", "900 - 1100 HV સ્તર"), tr("3 - 5 times", "3 - 5 ગણું")],
                   [tr("corrosion", "કાટ"), tr("hot dip galvanising", "hot dip galvanising"),
                    tr("80 micron of zinc", "80 માઇક્રોમીટર zinc"), tr("20 years rural", "ગ્રામ્યમાં 20 વર્ષ")],
                   [tr("fatigue", "fatigue"), tr("shot peening", "shot peening"),
                    tr("- 400 MPa residual", "- 400 MPa residual"), tr("2 - 3 times", "2 - 3 ગણું")],
                   [tr("friction", "ઘર્ષણ"), tr("phosphate plus oil", "phosphate અને તેલ"),
                    tr("2 - 10 micron", "2 - 10 માઇક્રોમીટર"), tr("scuffing stops", "scuffing અટકે")],
                   [tr("appearance", "દેખાવ"), tr("paint system", "paint system"),
                    tr("200 - 250 micron DFT", "200 - 250 માઇક્રોમીટર DFT"), tr("10 years", "10 વર્ષ")]]),
            why("the stress is highest at the surface, the environment touches only the surface, and "
                "two sliding parts meet only at the surface - so a treatment that changes the top "
                "20 micrometres changes the life of the part while the chemistry of the core stays "
                "cheap and tough.",
                "stress સપાટી પર સૌથી વધુ હોય, પર્યાવરણ ફક્ત સપાટીને અડે, અને સરકતા બે ભાગ ફક્ત સપાટી પર "
                "મળે - તેથી ઉપરના 20 માઇક્રોમીટર બદલતી પ્રક્રિયા ભાગનું આયુષ્ય બદલે જ્યારે core નું રસાયણ "
                "સસ્તું અને લચીલું રહે."),
            pit("a coating is not a repair. Plating or painting over a fatigue crack hides it, and the "
                "crack keeps growing under the paint until the part breaks; the surface is treated "
                "before it is damaged, not after.",
                "કોટિંગ સમારકામ નથી. Fatigue તિરાડ પર plating કે પેન્ટ કરવાથી તે છુપાય છે, અને તિરાડ પેન્ટ "
                "નીચે વધતી રહે જ્યાં સુધી ભાગ તૂટે; સપાટી બગડ્યા પછી નહીં, પહેલાં સારવાર પામે."),
            check("ask what is killing the part - abrasion, rust, alternating load or friction - and "
                  "only then choose the millimetres. A 20 micron nitride on a part that is actually "
                  "corroding is money spent on the wrong failure.",
                  "ભાગને શું મારી રહ્યું છે તે પૂછો - ઘસારો, કાટ, alternating load કે ઘર્ષણ - અને પછી જ "
                  "માઇક્રોમીટર પસંદ કરો. જે ભાગ ખરેખર કાટ ખાય છે તેના પર 20 માઇક્રોમીટર nitride એ ખોટી "
                  "નિષ્ફળતા પર ખર્ચેલા પૈસા છે."),
            diagram="u5_surface",
        ),
        card(
            "Cleaning and mechanical finishing: the roughness you buy",
            "સફાઈ અને mechanical finishing: કઈ ખરબચડાઈ ખરીદો છો",
            p("No coating works on a dirty surface, so the order is fixed: <b>degrease</b> with an "
              "alkali or a solvent, <b>pickle</b> in acid to remove scale and rust, <b>blast</b> to a "
              "controlled profile, and coat within a few hours before the steel re-rusts. Mechanical "
              "finishing comes in the same ladder everywhere: turning at about 3.2 micron Ra, grinding "
              "at 0.8, honing at 0.2, lapping at 0.05. Each step costs roughly three times the last "
              "and buys about half the roughness, so the drawing asks for the finish the function "
              "needs and no finer.",
              "કોઈ પણ કોટિંગ ગંદી સપાટી પર ચાલતું નથી, તેથી ક્રમ નિશ્ચિત છે: alkali કે solvent થી "
              "<b>degrease</b>, scale અને કાટ કાઢવા એસિડમાં <b>pickle</b>, નિયંત્રિત profile સુધી "
              "<b>blast</b>, અને સ્ટીલ ફરી કાટ ન ખાય તે પહેલાં થોડા કલાકમાં કોટિંગ. Mechanical finishing "
              "દરેક જગ્યાએ એ જ નિસરણીમાં આવે: turning લગભગ 3.2 માઇક્રોમીટર Ra, grinding 0.8, honing 0.2, "
              "lapping 0.05. દરેક પગલું આગલા કરતાં લગભગ ત્રણ ગણું મોંઘું પડે અને અડધી ખરબચડાઈ આપે, તેથી "
              "ડ્રોઇંગ કામને જે finish જોઈએ તેટલું જ માંગે, તેનાથી વધુ બારીક નહીં."),
            math("theoretical roughness of a turned surface:  Ra = f^2/(32 r)",
                 "feed f = 0.20 mm/rev, tool nose radius r = 0.8 mm",
                 "Ra = 0.04/(32 x 0.8) = 0.00156 mm = 1.56 micron",
                 "halve the feed to 0.10 mm/rev: Ra = 0.01/25.6 = 0.39 micron, a quarter"),
            table([tr("process", "પ્રક્રિયા"), tr("Ra, micron", "Ra, માઇક્રોમીટર"),
                   tr("what it is for", "શેના માટે"), tr("cost index", "ખર્ચ")],
                  [[tr("drilling / sawing", "drilling / sawing"), tr("6.3 - 12.5", "6.3 - 12.5"),
                    tr("clearing a hole", "છિદ્ર કાઢવું"), tr("1", "1")],
                   [tr("turning", "turning"), tr("1.6 - 3.2", "1.6 - 3.2"),
                    tr("general machined faces", "સામાન્ય machined સપાટી"), tr("2", "2")],
                   [tr("grinding", "grinding"), tr("0.4 - 0.8", "0.4 - 0.8"),
                    tr("hardened steel, bearing seats", "hardened સ્ટીલ, bearing seat"), tr("5", "5")],
                   [tr("honing", "honing"), tr("0.1 - 0.4", "0.1 - 0.4"),
                    tr("cylinder bores, cross-hatch", "cylinder bore, cross-hatch"), tr("10", "10")],
                   [tr("lapping", "lapping"), tr("0.025 - 0.1", "0.025 - 0.1"),
                    tr("gauge faces, valve seats", "gauge સપાટી, valve seat"), tr("20", "20")]]),
            why("the finish is geometry, not magic: a round tool nose of radius r leaves a scallop "
                "every feed, and the depth of that scallop is f squared over 8r, so the feed matters "
                "twice as much as the tool radius. It also explains why a plating copies the profile "
                "it grows on - a bright plating on a torn surface is a bright torn surface.",
                "finish ભૂમિતિ છે, જાદુ નહીં: r ત્રિજ્યાનું ગોળ tool nose દરેક feed પર એક લહેર છોડે, અને "
                "તે લહેરની ઊંડાઈ f વર્ગ બટા 8r છે, તેથી feed નું મહત્વ tool ત્રિજ્યા કરતાં બમણું છે. એ જ "
                "કારણે plating જે profile પર ઊગે તેની નકલ કરે - ફાટેલી સપાટી પર ચળકતું plating એ ચળકતી "
                "ફાટેલી સપાટી જ છે."),
            pit("blasting is not free either. On a part that lives in fatigue, a coarse blast raises "
                "the stress at the bottoms of the pits it makes; the same treatment that helps a "
                "painted structure can shorten the life of a spring.",
                "blasting પણ મફત નથી. Fatigue માં જીવતા ભાગ પર જાડું blasting તેનાથી પડેલા ખાડાના તળિયે "
                "stress વધારે; જે પ્રક્રિયા પેન્ટ કરેલા ઢાંચાને મદદ કરે તે જ spring નું આયુષ્ય ટૂંકાવી શકે."),
            check("write the finish as a number on the drawing, not as 'smooth'. Ra 0.8 with a 50 - 75 "
                  "micron blast profile and Sa 2 1/2 is a specification; 'well finished' is not.",
                  "finish ડ્રોઇંગ પર આંકડા તરીકે લખો, 'smooth' તરીકે નહીં. Ra 0.8, 50 - 75 માઇક્રોમીટર "
                  "blast profile અને Sa 2 1/2 એ specification છે; 'સારું finished' નથી."),
            diagram="u5_finish",
        ),
    ],
})
