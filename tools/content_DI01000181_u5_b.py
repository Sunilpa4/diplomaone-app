"""DI01000181 Unit 5, part B: electroplating, conversion coatings and thin films."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from subject_DI01000181 import tr  # noqa: E402
from content_DI01000181_lib import (p, h4, table, math, eq, why, check, pit, card,  # noqa: E402
                                    ul, ol)

NOTES_B = []

NOTES_B.append({
    "title": tr("5.2 Metallic coatings, conversion coatings and thin films",
                "5.2 Metallic coatings, conversion coatings અને thin films"),
    "items": [
        card(
            "Electroplating, electroless plating and anodising",
            "Electroplating, electroless plating અને anodising",
            p("In electroplating the work is the cathode in a bath of the coating metal's own salt, "
              "and a plate of that metal is the anode. Metal dissolves from the anode, crosses the "
              "electrolyte as an ion and is deposited on the work, so the bath keeps its composition "
              "and only the addition agents decide whether the deposit is bright or dull, hard or "
              "soft. <b>Electroless</b> plating (nickel with sodium hypophosphite) needs no current, "
              "so it covers a complex shape evenly. <b>Anodising</b> does not add a metal: it grows "
              "the aluminium's own oxide, 5 - 25 micron thick, which is hard, insulating and porous "
              "enough to take a dye.",
              "Electroplating માં કામ એ કોટિંગ ધાતુના ક્ષારના સ્નાનમાં cathode છે, અને એ જ ધાતુની પ્લેટ anode "
              "છે. ધાતુ anode માંથી ઓગળે, ion તરીકે electrolyte પાર કરે અને કામ પર જમા થાય, તેથી સ્નાનની "
              "રચના ટકે અને ફક્ત addition agents નક્કી કરે કે deposit ચળકતું કે ઝાંખું, સખત કે નરમ. "
              "<b>Electroless</b> plating (sodium hypophosphite સાથે nickel) ને current ન જોઈએ, તેથી તે "
              "જટિલ આકારને સમાન રીતે ઢાંકે. <b>Anodising</b> ધાતુ ઉમેરતું નથી: તે aluminium ના પોતાના oxide ને "
              "5 - 25 માઇક્રોમીટર જાડું ઉગાડે, જે સખત, અવાહક અને રંગ ઝીલી શકે તેટલું છિદ્રાળુ છે."),
            math("Faraday: m = M I t/(n F),  with F = 96500 C/mol",
                 "per ampere-hour: 58.7/(2 x 96500) x 3600 = 1.095 g of nickel",
                 "thickness t = M i t_sec eta/(n F rho);  i = 300 A/m2, eta = 0.95, 20 min",
                 "t = (58.7e-3 x 300 x 1200 x 0.95)/(2 x 96500 x 8900) = 11.7e-6 m = 11.7 micron"),
            table([tr("coating", "કોટિંગ"), tr("thickness", "જાડાઈ"),
                   tr("how it protects", "કેમ રક્ષે"), tr("where", "ક્યાં")],
                  [[tr("zinc, electroplated", "zinc, electroplated"), tr("8 - 25 micron", "8 - 25 માઇક્રોમીટર"),
                    tr("sacrificial: it corrodes first", "બલિદાન: પહેલું તે કાટ ખાય"),
                    tr("fasteners, brackets", "fasteners, brackets")],
                   [tr("zinc, hot dip", "zinc, hot dip"), tr("60 - 100 micron", "60 - 100 માઇક્રોમીટર"),
                    tr("same, much thicker", "એ જ, ઘણું જાડું"), tr("structures, poles", "ઢાંચા, થાંભલા")],
                   [tr("nickel", "nickel"), tr("10 - 25 micron", "10 - 25 માઇક્રોમીટર"),
                    tr("barrier plus a base for chrome", "અવરોધ અને chrome નો આધાર"),
                    tr("bathroom fittings", "બાથરૂમનાં ફિટિંગ")],
                   [tr("hard chromium", "hard chromium"), tr("20 - 100 micron", "20 - 100 માઇક્રોમીટર"),
                    tr("1000 HV, low friction", "1000 HV, ઓછું ઘર્ષણ"), tr("hydraulic rods, dies", "hydraulic rod, die")],
                   [tr("electroless nickel", "electroless nickel"), tr("10 - 25 micron", "10 - 25 માઇક્રોમીટર"),
                    tr("even on any shape", "કોઈ પણ આકાર પર સમાન"), tr("valve bodies, moulds", "valve body, mould")],
                   [tr("anodised aluminium", "anodised aluminium"), tr("5 - 25 micron", "5 - 25 માઇક્રોમીટર"),
                    tr("its own oxide, dyeable", "પોતાનું oxide, રંગી શકાય"), tr("window frames, pots", "બારીની ફ્રેમ, વાસણ")]]),
            why("Faraday's law is counting atoms. Every 96500 coulomb liberates one mole of electrons, "
                "and a nickel ion needs two of them, so a coulomb always deposits the same 0.304 mg "
                "of nickel - the only variables left are the current, the time and how much of the "
                "current is wasted on hydrogen.",
                "Faraday નો નિયમ atoms ગણે છે. દર 96500 કૂલમ્બ એક mole electrons મુક્ત કરે, અને nickel ion "
                "ને તેમાંથી બે જોઈએ, તેથી એક કૂલમ્બ હંમેશા એ જ 0.304 mg nickel જમા કરે - બાકી ફક્ત current, "
                "સમય અને hydrogen પર વેડફાતો current રહે."),
            pit("plating does not fill a scratch and it does not make a part stronger. Worse, hydrogen "
                "from the plating bath enters a hardened steel and embrittles it, so a plated high "
                "strength part must be baked at about 200 C within a few hours.",
                "plating scratch પૂરતું નથી અને ભાગ મજબૂત કરતું નથી. વધુ ખરાબ, plating સ્નાનનું hydrogen "
                "hardened સ્ટીલમાં ઘૂસીને તેને ભંગુર બનાવે, તેથી plated ઊંચી તાકાતવાળા ભાગને થોડા કલાકમાં "
                "લગભગ 200 C પર bake કરવો પડે."),
            check("say which mechanism you are buying: zinc protects by corroding itself, nickel and "
                  "chrome protect only by sealing the steel off, and anodising changes the metal "
                  "rather than covering it. A barrier that is scratched is a barrier that has failed.",
                  "કઈ રીતે રક્ષણ ખરીદો છો તે કહો: zinc પોતે કાટ ખાઈને રક્ષે, nickel અને chrome ફક્ત સ્ટીલને "
                  "બંધ કરીને રક્ષે, અને anodising ઢાંકવાને બદલે ધાતુ બદલે. ખરોચેલો અવરોધ નિષ્ફળ ગયેલો અવરોધ છે."),
            diagram="u5_plate",
        ),
        card(
            "Conversion coatings, electropolishing and thin films",
            "Conversion coatings, electropolishing અને thin films",
            p("A conversion coating has no interface to peel, because the surface is turned into the "
              "coating: <b>phosphating</b> grows a 2 - 10 micron crystalline zinc or iron phosphate "
              "that keys paint and holds oil, <b>chromating</b> passivates zinc, and <b>bluing</b> "
              "grows the 1 - 3 micron oxide on a gun. <b>Electropolishing</b> is the reverse of "
              "plating - the work is the anode and the surface is dissolved away, 10 - 50 micron, "
              "leaving a bright, burr-free, hygienic face. <b>Photo-etching</b> uses the same "
              "dissolution through a resist to cut a pattern.",
              "Conversion coating ને છોડી શકાય એવો interface હોતો નથી, કારણ કે સપાટી જ કોટિંગમાં ફેરવાય છે: "
              "<b>phosphating</b> 2 - 10 માઇક્રોમીટરનું સ્ફટિકીય zinc કે iron phosphate ઉગાડે જે પેન્ટ પકડે "
              "અને તેલ રાખે, <b>chromating</b> zinc ને passive કરે, અને <b>bluing</b> બંદૂક પર 1 - 3 "
              "માઇક્રોમીટરનું oxide ઉગાડે. <b>Electropolishing</b> plating નું ઊલટું છે - કામ anode છે અને "
              "સપાટી 10 - 50 માઇક્રોમીટર ઓગળી જાય, જેથી ચળકતી, burr વગરની, સ્વચ્છ સપાટી રહે. "
              "<b>Photo-etching</b> એ જ ઓગાળવાની ક્રિયા resist મારફતે વાપરીને આકાર કાપે છે."),
            math("thin films:  PVD 0.1 - 5 micron, CVD 5 - 20 micron",
                 "PVD TiN at 480 C: 2500 HV, line of sight, so the fixture turns",
                 "CVD at 1000 C: better throwing power and adhesion, but the substrate must take the heat",
                 "one 3 micron TiN coating on an insert: Rs 8 extra, 3 times the tool life",
                 "20 parts/insert at Rs 60 = Rs 3.00 per part;  60 parts at Rs 68 = Rs 1.13 per part"),
            table([tr("process", "પ્રક્રિયા"), tr("thickness", "જાડાઈ"),
                   tr("temperature", "તાપમાન"), tr("used for", "ઉપયોગ")],
                  [[tr("phosphating", "phosphating"), tr("2 - 10 micron", "2 - 10 માઇક્રોમીટર"),
                    tr("55 - 70 C bath", "55 - 70 C સ્નાન"), tr("paint base, bolt threads", "પેન્ટનો આધાર, bolt thread")],
                   [tr("chromate", "chromate"), tr("0.1 - 0.5 micron", "0.1 - 0.5 માઇક્રોમીટર"),
                    tr("room", "રૂમ"), tr("on top of zinc plating", "zinc plating પર")],
                   [tr("anodising", "anodising"), tr("5 - 25 micron", "5 - 25 માઇક્રોમીટર"),
                    tr("20 C, 20 V", "20 C, 20 V"), tr("aluminium, dye and seal", "aluminium, રંગ અને seal")],
                   [tr("electropolishing", "electropolishing"), tr("10 - 50 micron removed", "10 - 50 માઇક્રોમીટર દૂર"),
                    tr("60 - 80 C", "60 - 80 C"), tr("hygienic, bright, deburred", "સ્વચ્છ, ચળકતું, burr વગર")],
                   [tr("PVD, TiN", "PVD, TiN"), tr("1 - 5 micron", "1 - 5 માઇક્રોમીટર"),
                    tr("under 500 C", "500 C ની નીચે"), tr("tool inserts, drills, dies", "tool insert, drill, die")],
                   [tr("CVD", "CVD"), tr("5 - 20 micron", "5 - 20 માઇક્રોમીટર"),
                    tr("900 - 1100 C", "900 - 1100 C"), tr("carbide inserts, wear plates", "carbide insert, wear plate")]]),
            why("a conversion coating cannot peel because there is nothing to peel - the boundary "
                "between coating and metal has been dissolved into a gradient. A thin film is the "
                "opposite: it is an added layer, so its adhesion is a real number and a warm "
                "substrate, a clean surface and a rotating fixture are what buy it.",
                "conversion coating ઊખડી શકે નહીં કારણ કે ઊખડવા જેવું કંઈ નથી - કોટિંગ અને ધાતુ વચ્ચેની "
                "સીમા ઓગળીને એક gradient બની ગઈ છે. Thin film ઊલટું છે: તે ઉમેરાયેલું સ્તર છે, તેથી તેનું "
                "adhesion ખરો આંકડો છે અને ગરમ substrate, સાફ સપાટી તથી ફરતું fixture જ તે ખરીદે."),
            pit("an anodised surface is an insulator and a sponge. If it is not sealed in boiling water "
                "or a cold sealant, the dye bleeds out in service and the open pores become the start "
                "of a pitting cell.",
                "anodised સપાટી અવાહક અને સ્પોન્જ છે. જો તેને ઉકળતા પાણી કે ઠંડા sealant માં seal ન કરો તો "
                "સેવામાં રંગ નીકળી જાય અને ખુલ્લા છિદ્રો pitting ની શરૂઆત બની જાય."),
            check("pick the coating for the shape as well as the duty: PVD is line of sight, so a deep "
                  "bore gets nothing; electroless nickel and phosphating cover inside and out. That "
                  "one sentence decides most real coating choices.",
                  "કામ સાથે આકાર પ્રમાણે પણ કોટિંગ પસંદ કરો: PVD line of sight છે, તેથી ઊંડા bore ને કંઈ "
                  "ન મળે; electroless nickel અને phosphating અંદર-બહાર ઢાંકે. એ એક વાક્ય મોટા ભાગની ખરી "
                  "પસંદગી નક્કી કરે."),
            diagram="u5_thick",
        ),
    ],
})
