"""DI01000181 Unit 5, part D: paints and varnishes, corrosion."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from subject_DI01000181 import tr  # noqa: E402
from content_DI01000181_lib import (p, h4, table, math, eq, why, check, pit, card,  # noqa: E402
                                    ul, ol)

NOTES_D = []

NOTES_D.append({
    "title": tr("5.4 Paints and varnishes", "5.4 Paints અને varnishes"),
    "items": [
        card(
            "Paint is a system of coats, not a colour",
            "Paint એ કોટિંગનું તંત્ર છે, રંગ નહીં",
            p("A paint is a <b>binder</b> (the resin that forms the film), a <b>pigment</b> (the "
              "colour, the opacity and the corrosion inhibitor), a <b>solvent</b> (which only has to "
              "disappear) and small amounts of additives. A <b>varnish</b> is the same binder and "
              "solvent with no pigment; an <b>enamel</b> is a pigmented varnish; a <b>lacquer</b> dries "
              "only by solvent evaporation; a <b>powder coating</b> has no solvent at all and is "
              "melted on. A protective system is applied in coats, each with its own job: a primer "
              "for adhesion and inhibition, an intermediate for build and barrier, a topcoat for "
              "colour and weather.",
              "Paint એટલે <b>binder</b> (ફિલ્મ બનાવતો resin), <b>pigment</b> (રંગ, અપારદર્શકતા અને કાટ "
              "રોકતું દ્રવ્ય), <b>solvent</b> (જેને ફક્ત ઊડી જવાનું હોય) અને થોડા additives. "
              "<b>Varnish</b> એ જ binder અને solvent, પણ pigment વગર; <b>enamel</b> એ pigmented varnish; "
              "<b>lacquer</b> ફક્ત solvent ઊડીને સુકાય; <b>powder coating</b> માં solvent જ નથી અને તે "
              "ઓગાળીને ચઢાવાય. રક્ષણનું તંત્ર કોટમાં ચઢે, દરેકનું પોતાનું કામ: adhesion અને અવરોધ માટે "
              "primer, જાડાઈ અને અવરોધ માટે intermediate, રંગ અને હવામાન માટે topcoat."),
            math("wet film thickness = dry film thickness x 100/% volume solids",
                 "75 micron DFT at 60 % solids: WFT = 75/0.60 = 125 micron",
                 "120 m2 at 125 micron wet = 120 x 125e-6 = 0.015 m3 = 15 litres",
                 "with a 15 % application loss: 15 x 1.15 = 17.3 litres"),
            table([tr("coat", "કોટ"), tr("job", "કામ"), tr("DFT, micron", "DFT, માઇક્રોમીટર"),
                   tr("resin", "resin")],
                  [[tr("blast and prime", "blast અને primer"), tr("adhesion, rust inhibition", "adhesion, કાટ રોકવો"),
                    tr("60 - 75", "60 - 75"), tr("zinc rich epoxy", "zinc ભરપૂર epoxy")],
                   [tr("intermediate", "intermediate"), tr("build, barrier", "જાડાઈ, અવરોધ"),
                    tr("100 - 125", "100 - 125"), tr("epoxy MIO", "epoxy MIO")],
                   [tr("topcoat", "topcoat"), tr("colour, UV, rain", "રંગ, UV, વરસાદ"),
                    tr("40 - 50", "40 - 50"), tr("polyurethane", "polyurethane")],
                   [tr("total system", "કુલ તંત્ર"), tr("10 - 15 years", "10 - 15 વર્ષ"),
                    tr("200 - 250", "200 - 250"), tr("-", "-")],
                   [tr("powder coat", "powder coat"), tr("one coat, no solvent", "એક કોટ, solvent નહીં"),
                    tr("60 - 100", "60 - 100"), tr("polyester", "polyester")]]),
            why("a paint protects in two ways and the thickness is shared between them: as a barrier "
                "it keeps water and oxygen out, and with an inhibitive pigment it keeps the steel "
                "passive where the barrier is broken. That is why the primer carries the inhibitor "
                "and the topcoat carries the weather resistance.",
                "પેન્ટ બે રીતે રક્ષે અને જાડાઈ બંનેમાં વહેંચાય: અવરોધ તરીકે તે પાણી અને oxygen બહાર રાખે, "
                "અને inhibitive pigment સાથે અવરોધ તૂટ્યાં જ્યાં સ્ટીલને passive રાખે. તેથી primer માં "
                "inhibitor અને topcoat માં હવામાન સામે ટકાવારી રહે."),
            pit("most coating failures are preparation failures. Paint applied over mill scale, rust or "
                "oil let go of the steel within a year, and the report then blames the paint; the same "
                "paint on a Sa 2 1/2 blast lasts ten years.",
                "મોટા ભાગની કોટિંગ નિષ્ફળતા સફાઈની નિષ્ફળતા છે. Mill scale, કાટ કે તેલ પર ચઢાવેલો પેન્ટ વર્ષમાં "
                "સ્ટીલ પરથી નીકળી જાય, અને પછી રિપોર્ટ પેન્ટને દોષ દે; એ જ પેન્ટ Sa 2 1/2 blast પર દસ વર્ષ ટકે."),
            check("specify the system as four lines - preparation grade, each coat with its DFT, the "
                  "total DFT and the recoat window - and inspect the first two, because the last two "
                  "cannot be repaired later.",
                  "તંત્ર ચાર લીટીમાં લખો - preparation grade, દરેક કોટ તેના DFT સાથે, કુલ DFT અને recoat "
                  "window - અને પહેલી બે ચકાસો, કારણ કે છેલ્લી બે પછી સુધારી શકાય નહીં."),
            diagram="u5_paint",
        ),
    ],
})

NOTES_D.append({
    "title": tr("5.5 Corrosion: why it happens and what it looks like",
                "5.5 કાટ: કેમ થાય અને કેવો દેખાય"),
    "items": [
        card(
            "Corrosion is a cell, and the cell needs four things",
            "કાટ એક cell છે, અને cell ને ચાર વસ્તુ જોઈએ",
            p("Corrosion is electrochemical: at one place on the surface iron gives up electrons and "
              "dissolves as Fe2+, and at another place oxygen takes those electrons and water turns "
              "into hydroxide. The two places are the <b>anode</b> and the <b>cathode</b>, the water "
              "film between them is the <b>electrolyte</b>, and the metal is the <b>path</b>. Rust is "
              "what happens next: the Fe2+ meets oxygen and water and becomes hydrated iron oxide, "
              "which occupies six to seven times the volume of the iron it came from - so a rust "
              "layer lifts paint and splits concrete.",
              "કાટ electrochemical છે: સપાટી પર એક જગ્યાએ લોખંડ electrons છોડીને Fe2+ તરીકે ઓગળે, અને બીજી "
              "જગ્યાએ oxygen એ electrons લે અને પાણી hydroxide બને. બે જગ્યા <b>anode</b> અને <b>cathode</b> છે, "
              "તેમની વચ્ચેની પાણીની ફિલ્મ <b>electrolyte</b> છે, અને ધાતુ <b>રસ્તો</b> છે. પછી કાટ થાય છે: "
              "Fe2+ oxygen અને પાણીને મળીને hydrated iron oxide બને, જે પોતાના લોખંડ કરતાં છ-સાત ગણું "
              "કદ લે - તેથી કાટનું સ્તર પેન્ટ ઉપાડે અને કોંક્રિટ ફાડે."),
            math("Faraday again, now eating metal instead of depositing it:",
                 "m = M I t/(n F);  iron: M = 0.0558 kg/mol, n = 2",
                 "i = 0.1 A/m2 on steel: rate = (0.0558 x 0.1)/(2 x 96500 x 7850)",
                 "rate = 3.68e-12 m/s = 0.116 mm per year",
                 "cell voltage: zinc to copper 0.76 + 0.34 = 1.10 V; zinc to iron 0.32 V"),
            table([tr("environment", "પર્યાવરણ"), tr("rate, mm/year", "દર, mm/વર્ષ"),
                   tr("what drives it", "શું ચલાવે"), tr("typical part", "સામાન્ય ભાગ")],
                  [[tr("rural air", "ગ્રામ્ય હવા"), tr("0.005 - 0.02", "0.005 - 0.02"),
                    tr("a little moisture", "થોડી ભેજ"), tr("fence, roof sheet", "વાડ, છતની ચાદર")],
                   [tr("urban or coastal", "શહેરી કે દરિયાઈ"), tr("0.05 - 0.1", "0.05 - 0.1"),
                    tr("chloride, sulphur", "chloride, sulphur"), tr("railing, structure", "રેલિંગ, ઢાંચો")],
                   [tr("industrial flue gas", "ઔદ્યોગિક flue gas"), tr("0.1 - 0.5", "0.1 - 0.5"),
                    tr("SO2 and acid condensate", "SO2 અને એસિડ condensate"), tr("duct, chimney", "duct, ચીમની")],
                   [tr("seawater, immersed", "દરિયાનું પાણી"), tr("0.1 - 0.3", "0.1 - 0.3"),
                    tr("oxygen plus chloride", "oxygen અને chloride"), tr("hull, jetty pile", "હલ, jetty નો થાંભલો")],
                   [tr("dilute acid", "પાતળું એસિડ"), tr("1 - 10", "1 - 10"),
                    tr("hydrogen evolution", "hydrogen નીકળવો"), tr("tank, pipe", "ટાંકી, પાઇપ")]]),
            why("the cathode is protected and the anode is eaten, so the area ratio decides the damage. "
                "A small anode carrying the current for a large cathode dissolves very fast: a "
                "stainless bolt in a painted steel frame, or a scratch in a coating on a big tank, is "
                "the worst geometry there is.",
                "cathode સુરક્ષિત રહે અને anode ખવાય, તેથી area નું પ્રમાણ નુકસાન નક્કી કરે. મોટા cathode માટે "
                "current ઉપાડતો નાનો anode ખૂબ ઝડપથી ઓગળે: પેન્ટ કરેલા સ્ટીલ ફ્રેમમાં stainless bolt, કે "
                "મોટી ટાંકી પર કોટિંગમાં એક ખરોચ, સૌથી ખરાબ ભૂમિતિ છે."),
            pit("'stainless' does not mean 'does not corrode'. Its protection is a passive film a few "
                "atoms thick, and in warm chloride water that film breaks locally and cannot re-form - "
                "so the attack goes in as a pit instead of spreading as rust.",
                "'stainless' એટલે 'કાટ ન ખાય' નહીં. તેનું રક્ષણ થોડા atoms જાડું passive ફિલ્મ છે, અને "
                "ગરમ chloride વાળા પાણીમાં એ ફિલ્મ સ્થાનિક રીતે તૂટે અને ફરી બની શકે નહીં - તેથી હુમલો "
                "કાટ તરીકે ફેલાવાને બદલે pitting તરીકે અંદર જાય."),
            check("compute the life before choosing the material: rate times years gives the metal that "
                  "will be lost, and a corrosion allowance is that number written on the drawing. "
                  "0.25 mm/year for 10 years is 2.5 mm of wall.",
                  "સામગ્રી પસંદ કરતાં પહેલાં આયુષ્ય ગણો: દર ગુણ્યા વર્ષ એટલે જે ધાતુ જશે, અને corrosion "
                  "allowance એ જ આંકડો ડ્રોઇંગ પર લખાય. 10 વર્ષ માટે 0.25 mm/વર્ષ એટલે 2.5 mm દીવાલ."),
            diagram="u5_corr",
        ),
        card(
            "The six shapes of corrosion, and one defence for each",
            "કાટના છ આકાર, અને દરેક માટે એક બચાવ",
            p("The shape of the damage names the mechanism. <b>Uniform</b> attack eats the whole area "
              "at the same rate and can be paid for with a corrosion allowance. <b>Galvanic</b> attack "
              "happens where two metals touch. <b>Pitting</b> is a local break in a passive film, "
              "<b>crevice</b> attack is stagnant liquid under a gasket, <b>intergranular</b> attack "
              "follows the grain boundaries of a sensitised stainless steel, and <b>stress corrosion "
              "cracking</b> needs a tensile stress and a chloride at the same time. <b>Erosion "
              "corrosion</b> is a film that is scrubbed away as fast as it forms.",
              "નુકસાનનો આકાર જ પ્રક્રિયાનું નામ કહે છે. <b>Uniform</b> હુમલો આખા ભાગને સરખા દરે ખાય અને તેને "
              "corrosion allowance થી ચૂકવી શકાય. <b>Galvanic</b> હુમલો જ્યાં બે ધાતુ અડે ત્યાં થાય. "
              "<b>Pitting</b> એ passive ફિલ્મમાં સ્થાનિક ભંગ છે, <b>crevice</b> હુમલો gasket નીચે સ્થિર પડેલું "
              "પ્રવાહી છે, <b>intergranular</b> હુમલો sensitised stainless સ્ટીલના grain boundaries પર ચાલે, "
              "અને <b>stress corrosion cracking</b> ને એક જ સમયે tensile stress અને chloride જોઈએ. "
              "<b>Erosion corrosion</b> એ એવી ફિલ્મ છે જે બનવા જેટલી ઝડપે ઘસાઈ જાય."),
            math("corrosion allowance = rate x design life",
                 "0.25 mm/year over 10 years = 2.5 mm",
                 "wall: 6.0 mm now, minimum 4.5 mm, so 1.5 mm is available",
                 "2.5 mm > 1.5 mm, so plain steel fails life 6;  either 7.0 mm wall or a coating"),
            table([tr("type", "પ્રકાર"), tr("where it starts", "ક્યાં શરૂ થાય"),
                   tr("defence", "બચાવ"), tr("design rule", "design નિયમ")],
                  [[tr("uniform", "uniform"), tr("open area, atmosphere", "ખુલ્લો ભાગ, હવામાન"),
                    tr("corrosion allowance, coating", "corrosion allowance, કોટિંગ"), tr("add thickness", "જાડાઈ ઉમેરો")],
                   [tr("galvanic", "galvanic"), tr("joint of two metals", "બે ધાતુનું જોડાણ"),
                    tr("insulating washer, coat both", "insulating washer, બંનેને કોટ"), tr("no dissimilar pair", "અસમાન જોડી નહીં")],
                   [tr("pitting", "pitting"), tr("chloride on passive film", "passive ફિલ્મ પર chloride"),
                    tr("higher Mo grade, clean surface", "વધુ Mo grade, સાફ સપાટી"), tr("keep it dry", "સૂકું રાખો")],
                   [tr("crevice", "crevice"), tr("under gasket, lap joint", "gasket, lap joint નીચે"),
                    tr("seal the gap or weld it", "જગ્યા seal કરો કે weld કરો"), tr("no stagnant gap", "સ્થિર જગ્યા નહીં")],
                   [tr("intergranular", "intergranular"), tr("weld heat affected zone", "weld નો ગરમ ભાગ"),
                    tr("low carbon or stabilised grade", "ઓછા carbon કે stabilised grade"), tr("solution anneal", "solution anneal")],
                   [tr("stress cracking", "stress cracking"), tr("tensile stress plus chloride", "tensile stress અને chloride"),
                    tr("stress relieve, lower stress", "stress relieve, stress ઓછો"), tr("choose duplex", "duplex પસંદ કરો")],
                   [tr("erosion", "erosion"), tr("fast wet flow, bends", "ઝડપી ભીનો પ્રવાહ, વળાંક"),
                    tr("change geometry, hard facing", "ભૂમિતિ બદલો, hard facing"), tr("keep velocity down", "ઝડપ ઓછી રાખો")]]),
            why("all six are the same cell with a different geometry and a different control. Coatings "
                "remove the electrolyte, cathodic protection makes the whole surface the cathode, "
                "inhibitors adsorb on the anode, and alloying changes the anode itself - four "
                "different ways to break one circuit.",
                "છેય એક જ cell છે, ફરક ફક્ત ભૂમિતિ અને નિયંત્રણનો છે. કોટિંગ electrolyte દૂર કરે, cathodic "
                "protection આખી સપાટીને cathode બનાવે, inhibitor anode પર ચોંટે, અને alloying anode જ બદલે - "
                "એક circuit તોડવાના ચાર રસ્તા."),
            pit("never coat a crevice. Paint inside a lap joint or under a gasket leaves a small bare "
                "path at the edge, and that small anode with a large painted cathode pits straight "
                "through the plate.",
                "crevice પર કદી કોટ ન કરો. Lap joint કે gasket નીચે પેન્ટ કરવાથી ધાર પર નાનો ખુલ્લો રસ્તો "
                "રહે, અને મોટા પેન્ટ કરેલા cathode સામે એ નાનો anode પ્લેટમાં સીધો પાર થઈ જાય."),
            check("if the answer is a corrosion allowance, say how it will be inspected; if the answer "
                  "is a coating, say how it will be maintained. A defence that cannot be inspected is "
                  "a hope, not a design.",
                  "જવાબ corrosion allowance હોય તો તે કેમ ચકાસાશે કહો; જવાબ કોટિંગ હોય તો તે કેમ જાળવાશે "
                  "કહો. જે બચાવ ચકાસી શકાય નહીં તે આશા છે, design નહીં."),
            diagram="u5_types",
        ),
    ],
})
