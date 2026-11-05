"""DI01000181 Unit 4, part E: equations, viva, six solved numericals and sources."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from subject_DI01000181 import tr  # noqa: E402
from content_DI01000181_lib import (p, h4, table, math, eq, why, check, pit,  # noqa: E402
                                    body, ul, ol)

EQUATIONS = [
    {"title": tr("Rubber and elastomers", "Rubber અને elastomers"),
     "items": [
         {"name": tr("Modulus of an elastomer", "Elastomer નું modulus"),
          "f": "E = 3G",
          "terms": tr("Rubber is nearly incompressible, so its tensile modulus is three times the "
                      "shear modulus: G 1.0 MPa gives E 3.0 MPa.",
                      "Rubber લગભગ incompressible છે, તેથી tensile modulus shear modulus ના ત્રણ ગણું: "
                      "G 1.0 MPa એટલે E 3.0 MPa.")},
         {"name": tr("Stress in a strained rubber", "ખેંચાયેલા rubber માં stress"),
          "f": "sigma = E eps   (secant: sigma/eps at that strain)",
          "terms": tr("Rubber softens as it stretches, so the secant modulus is quoted at 100 % "
                      "strain rather than at 1 %.",
                      "Rubber ખેંચાતાં નરમ પડે, તેથી secant modulus 1 % નહીં 100 % strain પર આપાય.")},
         {"name": tr("Strain energy at break", "તૂટતી વખતની strain energy"),
          "f": "W = 0.5 sigma eps   (area under the curve)",
          "terms": tr("22 MPa at 550 % gives about 60 MJ per m3, which is why a rubber bumper "
                      "absorbs a blow that would dent steel.",
                      "550 % પર 22 MPa એટલે લગભગ 60 MJ પ્રતિ m3, તેથી rubber bumper એવો ધક્કો શોષે જે "
                      "સ્ટીલને ખાડો પાડે.")},
     ]},
    {"title": tr("Thermal stress in a ceramic", "Ceramic માં thermal stress"),
     "items": [
         {"name": tr("Constrained thermal stress", "રોકાયેલા ભાગમાં thermal stress"),
          "f": "sigma = E alpha dT",
          "terms": tr("A part that cannot expand develops this stress; alumina at 200 K gives "
                      "480 MPa against a 300 MPa strength.",
                      "જે ભાગ ફેલાઈ શકે નહીં તેમાં આ stress બને; 200 K પર alumina 300 MPa તાકાત સામે "
                      "480 MPa આપે.")},
         {"name": tr("Thermal shock parameter", "Thermal shock ઝીલવાનો આંકડો R"),
          "f": "R = sigma_f (1 - nu)/(E alpha)",
          "terms": tr("The temperature step a brittle material survives: 97 K for alumina, 2300 K "
                      "for fused silica, which is why silica crucibles can be quenched.",
                      "ભંગુર સામગ્રી જે તાપમાનનો ફટકો ઝીલે: alumina માટે 97 K, fused silica માટે 2300 K, "
                      "તેથી silica crucible ઠારી શકાય.")},
         {"name": tr("Griffith strength", "Griffith તાકાત"),
          "f": "sigma_f = sqrt(2 E gamma/(pi a))",
          "terms": tr("Strength falls as the square root of the flaw size: 50 um gives 276 MPa and "
                      "200 um gives 138 MPa in the same alumina.",
                      "તિરાડના માપના વર્ગમૂળ પ્રમાણે તાકાત ઘટે: એ જ alumina માં 50 um એટલે 276 MPa અને "
                      "200 um એટલે 138 MPa.")},
     ]},
    {"title": tr("Heat through a refractory wall", "Refractory દીવાલમાંથી ઉષ્મા"),
     "items": [
         {"name": tr("Heat flux through layers", "સ્તરોમાંથી heat flux"),
          "f": "q = dT/(L1/k1 + L2/k2 + ...)",
          "terms": tr("Steady one-dimensional flow: 1200 C to 50 C across 0.230 m of firebrick and "
                      "0.115 m of insulation is 968 W per m2.",
                      "સ્થિર એક-દિશા પ્રવાહ: 0.230 m firebrick અને 0.115 m insulation પાર 1200 C થી 50 C "
                      "એટલે 968 W પ્રતિ m2.")},
         {"name": tr("Thermal resistance", "Thermal resistance"),
          "f": "R = L/k",
          "terms": tr("Adds in series like an electrical resistance: 0.230 and 0.958 m2 K/W here.",
                      "Electrical resistance ની જેમ series માં જોડાય: અહીં 0.230 અને 0.958 m2 K/W.")},
         {"name": tr("Temperature at any depth", "કોઈ પણ ઊંડાણે તાપમાન"),
          "f": "T(x) = T_hot - q x/k",
          "terms": tr("Gives the interface temperature: 1200 - 968 x 0.230 = 977 C.",
                      "Interface નું તાપમાન આપે: 1200 - 968 x 0.230 = 977 C.")},
     ]},
    {"title": tr("Electrical and thermal insulation", "વીજ અને ઉષ્મા અવાહકતા"),
     "items": [
         {"name": tr("Dielectric strength", "Dielectric strength"),
          "f": "E_b = V_break/d",
          "terms": tr("Breakdown voltage per millimetre: air 3, porcelain 15, PTFE 24 kV/mm.",
                      "પ્રતિ મિલીમીટર breakdown વોલ્ટેજ: હવા 3, porcelain 15, PTFE 24 kV/mm.")},
         {"name": tr("Thickness of an insulator", "Insulator ની જાડાઈ"),
          "f": "t = V x SF/E_b",
          "terms": tr("11 kV with a factor of 3 in porcelain: 33/15 = 2.2 mm, so 3 mm is specified.",
                      "Porcelain માં factor 3 સાથે 11 kV: 33/15 = 2.2 mm, તેથી 3 mm લખાય.")},
         {"name": tr("Heat through an insulator", "Insulator માંથી ઉષ્મા"),
          "f": "q = k A dT/L",
          "terms": tr("50 mm of glass wool at 0.040 W/m K over 10 K loses 8 W per m2.",
                      "0.040 W/m K નું 50 mm glass wool 10 K પર 8 W પ્રતિ m2 ગુમાવે.")},
     ]},
    {"title": tr("Abrasive wheel and adhesive joint", "Abrasive wheel અને adhesive જોડાણ"),
     "items": [
         {"name": tr("Wheel peripheral speed", "Wheel ની પરિઘ ઝડપ"),
          "f": "v = pi D N/60",
          "terms": tr("250 mm at 2000 rpm is 26 m/s; a vitrified wheel is rated 35 m/s.",
                      "250 mm પર 2000 rpm એટલે 26 m/s; vitrified wheel 35 m/s સુધી રેટેડ છે.")},
         {"name": tr("Lap shear stress", "Lap shear stress"),
          "f": "tau = P/A",
          "terms": tr("5 kN over 25 x 40 mm is 5 MPa, against 20 MPa for epoxy.",
                      "25 x 40 mm પર 5 kN એટલે 5 MPa, epoxy ના 20 MPa સામે.")},
         {"name": tr("Factor of safety of a joint", "જોડાણનું factor of safety"),
          "f": "SF = tau_allowable/tau_working",
          "terms": tr("20/5 = 4 here; a design that asks for 3 carries 6.67 kN instead of 5 kN.",
                      "અહીં 20/5 = 4; 3 માંગતું design 5 kN ને બદલે 6.67 kN ઉપાડે.")},
     ]},
]

VIVA = [
    {"title": tr("Non-metallic materials", "અધાતુ સામગ્રી (non-metallic)"),
     "items": [
         {"q": tr("What is a non-metallic material?", "Non-metallic material એટલે શું?"),
          "a": tr("Any engineering material with no free electron sea. The syllabus groups it into "
                  "polymers, ceramics, composites and natural materials, and the bond - not the "
                  "strength - is what separates them.",
                  "Free electrons નો સમુદ્ર ન હોય તેવી કોઈ પણ ઇજનેરી સામગ્રી. Syllabus તેને polymers, "
                  "ceramics, composites અને natural materials માં વહેંચે છે, અને તાકાત નહીં, bond તેમને "
                  "જુદા પાડે છે.")},
         {"q": tr("Why does a machine need a non-metal at all?", "મશીનને non-metal ની જરૂર કેમ પડે?"),
          "a": tr("For weight, insulation, quiet running and corrosion resistance: a guard, a tank "
                  "liner, a cable insulator, a rubber mount and a cork gasket are all jobs a metal "
                  "does badly or expensively.",
                  "વજન, insulation, શાંત ચાલ અને કાટ સામે ટકવા માટે: guard, ટાંકીનું lining, cable "
                  "insulator, rubber mount અને cork gasket - આ બધું metal મોંઘું કે ખરાબ કરે.")},
         {"q": tr("What is a composite, and why is it used?", "Composite એટલે શું, અને કેમ વપરાય?"),
          "a": tr("A stiff fibre inside a tough matrix - glass or carbon in epoxy, silicon carbide in "
                  "aluminium. The fibre carries the load and the matrix spreads it, so the stiffness "
                  "per kilogram is three to four times that of steel.",
                  "લચીલા matrix માં કઠણ fibre - epoxy માં glass કે carbon, aluminium માં silicon carbide. "
                  "Fibre લોડ ઉપાડે અને matrix ફેલાવે, તેથી કિલો દીઠ કઠણાઈ સ્ટીલ કરતાં ત્રણ-ચાર ગણી.")},
     ]},
    {"title": tr("Rubber", "Rubber"),
     "items": [
         {"q": tr("What is vulcanisation and what does it change?", "Vulcanisation એટલે શું અને શું બદલે?"),
          "a": tr("Heating rubber with 1 - 3 % sulphur so that sulphur bridges form between chains. "
                  "The strength rises from 2 to 22 MPa and the strain of 550 % becomes recoverable - "
                  "the gum becomes an elastic solid.",
                  "1 - 3 % sulphur સાથે rubber ગરમ કરવું જેથી chains વચ્ચે sulphur પુલ બને. તાકાત 2 થી 22 MPa "
                  "થાય અને 550 % strain પાછું આવે - gum લચીલો ઘન બને.")},
         {"q": tr("Why is carbon black added to a rubber compound?",
                  "Rubber compound માં carbon black કેમ ઉમેરાય?"),
          "a": tr("It bonds to the chains, carries part of the load and blunts a running crack. 50 phr "
                  "of black takes the tensile strength from 2 to 22 MPa and the 100 % modulus from "
                  "1.6 to 4.5 MPa.",
                  "તે chains સાથે જોડાય, લોડનો ભાગ ઉપાડે અને દોડતી તિરાડ અટકાવે. 50 phr black tensile "
                  "strength 2 થી 22 MPa અને 100 % modulus 1.6 થી 4.5 MPa કરે.")},
         {"q": tr("Why is nitrile rubber used for an oil seal and not natural rubber?",
                  "તેલના seal માટે natural rubber નહીં, nitrile કેમ?"),
          "a": tr("Because swell is a property of the rubber-fluid pair: natural rubber takes up 50 % "
                  "in mineral oil and nitrile only about 5 %. A swollen seal loses its grip in the "
                  "groove and leaks.",
                  "કારણ કે ફૂલવું એ rubber અને પ્રવાહીની જોડીનું ગુણધર્મ છે: natural rubber ખનીજ તેલમાં "
                  "50 % લે, nitrile ફક્ત 5 %. ફૂલેલો seal groove માં પકડ ગુમાવે અને ચૂ થાય.")},
     ]},
    {"title": tr("Ceramics and refractories", "Ceramics અને refractories"),
     "items": [
         {"q": tr("Why is a ceramic hard and brittle at the same time?",
                  "Ceramic સખત અને ભંગુર એક સાથે કેમ?"),
          "a": tr("Because a dislocation cannot move through a rigid ionic lattice - it would bring "
                  "like charges together - so the material cannot yield, and the only way to relieve "
                  "stress is a crack. Hardness and brittleness are the same fact.",
                  "કારણ કે કઠણ ionic lattice માં dislocation ખસી શકે નહીં - સરખા charge પાસે આવે - તેથી "
                  "સામગ્રી yield થઈ શકે નહીં, અને stress ઓછો કરવાનો એક જ રસ્તો તિરાડ છે. સખતાઈ અને ભંગુરતા "
                  "એક જ હકીકત છે.")},
         {"q": tr("What separates a traditional ceramic from an advanced one?",
                  "Traditional અને advanced ceramic માં શું ફરક?"),
          "a": tr("Purity, porosity and price: a traditional body is fired with 5 - 15 % open pores and "
                  "costs a few rupees a kilogram; an advanced body is sintered below 1 % porosity for "
                  "one property and costs a hundred times more.",
                  "શુદ્ધતા, porosity અને ભાવ: traditional body 5 - 15 % ખુલ્લા છિદ્ર સાથે પાકે અને કિલો "
                  "થોડા રૂપિયા; advanced body એક ગુણધર્મ માટે 1 % થી ઓછા porosity સુધી sinter થાય અને સો ગણું "
                  "મોંઘું પડે.")},
         {"q": tr("What is an acidic and a basic refractory, and why match the slag?",
                  "Acidic અને basic refractory એટલે શું, અને slag કેમ મેળવવો?"),
          "a": tr("Silica is acidic and magnesia or dolomite is basic; a basic slag dissolves an acid "
                  "brick. Chromite and graphite are neutral and survive either slag, which is why they "
                  "are used where the charge changes.",
                  "Silica acidic છે અને magnesia કે dolomite basic; basic slag acidic ઈંટને ઓગાળે. Chromite "
                  "અને graphite neutral છે અને બંને slag ઝીલે, તેથી જ્યાં charge બદલાય ત્યાં વપરાય.")},
     ]},
    {"title": tr("Insulators, abrasives and adhesives", "Insulators, abrasives અને adhesives"),
     "items": [
         {"q": tr("How do you decide the thickness of an insulator?",
                  "Insulator ની જાડાઈ કેમ નક્કી કરો?"),
          "a": tr("Divide the withstand voltage by the dielectric strength: t = V x SF/E_b. For 11 kV "
                  "and a factor of 3 in porcelain, 33/15 gives 2.2 mm, so 3 mm is drawn. The surface "
                  "leakage path is checked separately.",
                  "Withstand વોલ્ટેજને dielectric strength થી ભાગો: t = V x SF/E_b. Porcelain માં 11 kV અને "
                  "factor 3 માટે 33/15 એટલે 2.2 mm, તેથી 3 mm લખાય. સપાટીનો leakage પથ અલગ ચકાસાય.")},
         {"q": tr("What is self-sharpening of a grinding wheel?",
                  "Grinding wheel નું self-sharpening એટલે શું?"),
          "a": tr("As the grain dulls, the cutting force on it rises until the bond breaks and the worn "
                  "grain falls out, leaving a fresh edge. The bond is therefore chosen for the work: "
                  "hard bond on soft material, soft bond on hard material.",
                  "Grain થૂંસાતાં તેના પરનું કાપવાનું બળ વધે, bond તૂટે અને ઘસાયેલો grain નીકળી જાય, નવી "
                  "ધાર મળે. તેથી bond કામ પ્રમાણે પસંદ થાય: નરમ સામગ્રી પર સખત bond, સખત પર નરમ.")},
         {"q": tr("Why is a lap joint stronger than a butt joint?",
                  "Lap joint butt joint કરતાં મજબૂત કેમ?"),
          "a": tr("Because the load is carried in shear over the overlap area instead of in peel at an "
                  "edge. A butt joint on a 20 MPa epoxy carries less than a lap joint on a 6 MPa PVA, "
                  "so the geometry matters more than the glue.",
                  "કારણ કે લોડ ધાર પર peel માં નહીં, overlap area પર shear માં ઉપડે. 20 MPa epoxy નું butt "
                  "joint 6 MPa PVA ના lap joint કરતાં ઓછું ઉપાડે, તેથી ગુંદર કરતાં ભૂમિતિ વધુ મહત્વની.")},
     ]},
]

_PRACTICE = [
    ("An alumina spacer that cannot expand",
     "ફેલાઈ ન શકતું alumina spacer",
     "An alumina spacer of E 300 GPa and alpha 8.0e-6 per K is clamped between steel flanges so that "
     "it cannot expand. Find the stress in the spacer at a temperature rise of 200 K and of 100 K, "
     "compare with its 300 MPa flexural strength, and state two ways to make the joint safe.",
     "E 300 GPa અને alpha 8.0e-6 પ્રતિ K નું alumina spacer steel flange વચ્ચે એવી રીતે clamp થયું છે કે "
     "ફેલાઈ શકે નહીં. 200 K અને 100 K તાપમાન વધારા પર spacer માં stress શોધો, તેની 300 MPa flexural "
     "strength સાથે સરખાવો, અને જોડાણ સલામત કરવાની બે રીતો કહો.",
     [h4("Step 1 - the constrained stress", "પગલું 1 - રોકાયેલો stress"),
      math("sigma = E alpha dT = 300e9 x 8.0e-6 x dT = 2.4e6 x dT  Pa",
           "dT = 200 K:  sigma = 2.4e6 x 200 = 480 MPa",
           "dT = 100 K:  sigma = 2.4e6 x 100 = 240 MPa"),
      h4("Step 2 - compare with the strength", "પગલું 2 - તાકાત સાથે સરખામણી"),
      math("flexural strength 300 MPa",
           "480/300 = 1.60  ->  the spacer is 60 % over its strength and cracks",
           "240/300 = 0.80  ->  factor of safety 1.25, thin but safe"),
      eq("480 MPa at 200 K is a cracked spacer;  240 MPa at 100 K is a marginal one"),
      h4("Step 3 - two ways to make the joint safe", "પગલું 3 - જોડાણ સલામત કરવાની બે રીતો"),
      math("1. leave a clearance of alpha L dT, or put a compliant gasket in the joint",
           "2. use fused silica instead: 72e9 x 0.55e-6 x 200 = 7.9 MPa"),
      p("A fully constrained ceramic is the worst case in the whole of Unit 4: the metal frame has a "
        "higher expansion coefficient and a much higher strength, so it wins the argument and the "
        "ceramic breaks. Either let the ceramic move, or soften the load path with a gasket, or choose "
        "a ceramic with a lower expansion coefficient - fused silica at 0.55e-6 develops only 7.9 MPa "
        "where alumina develops 480 MPa.",
        "આખા Unit 4 માં fully constrained ceramic સૌથી ખરાબ કિસ્સો છે: metal frame નું expansion coefficient "
        "વધારે અને તાકાત ઘણી વધારે હોય, તેથી તે જીતે અને ceramic તૂટે. Ceramic ને ખસવા દો, અથવા gasket થી "
        "લોડનો રસ્તો નરમ કરો, અથવા ઓછા expansion વાળું ceramic પસંદ કરો - fused silica 0.55e-6 પર ફક્ત "
        "7.9 MPa બનાવે જ્યાં alumina 480 MPa બનાવે."),
      check("Units: E in Pa and alpha in per K give a stress in Pa, so 2.4e6 x 200 = 480e6 Pa = 480 MPa. "
            "Check the sign too: on cooling the stress reverses, and a ceramic is just as weak in "
            "tension then.",
            "એકમ: Pa માં E અને પ્રતિ K માં alpha એટલે Pa માં stress, તેથી 2.4e6 x 200 = 480e6 Pa = 480 MPa. "
            "ચિહ્ન પણ ચકાસો: ઠંડા પડતાં stress ઊલટો થાય, અને ceramic ત્યારે પણ તેટલું જ નબળું છે.")],
     7),

    ("Thermal shock: alumina against glass",
     "Thermal shock: alumina સામે glass",
     "Compare the thermal shock resistance of alumina (300 MPa, nu 0.22, E 300 GPa, alpha 8.0e-6), "
     "soda-lime glass (50 MPa, nu 0.22, E 70 GPa, alpha 9.0e-6) and fused silica (110 MPa, nu 0.17, "
     "E 72 GPa, alpha 0.55e-6). Say which one can be quenched in water and why.",
     "Alumina (300 MPa, nu 0.22, E 300 GPa, alpha 8.0e-6), soda-lime glass (50 MPa, nu 0.22, E 70 GPa, "
     "alpha 9.0e-6) અને fused silica (110 MPa, nu 0.17, E 72 GPa, alpha 0.55e-6) ની thermal shock "
     "resistance સરખાવો. કોને પાણીમાં ઠારી શકાય અને કેમ તે કહો.",
     [h4("Step 1 - the parameter R", "પગલું 1 - parameter R"),
      math("R = sigma_f (1 - nu)/(E alpha),  the temperature step the part survives",
           "alumina:     300e6 x 0.78/(300e9 x 8.0e-6) = 234e6/2.4e6   =  97 K",
           "soda glass:   50e6 x 0.78/(70e9 x 9.0e-6)  = 39e6/0.63e6  =  62 K",
           "fused silica: 110e6 x 0.83/(72e9 x 0.55e-6) = 91.3e6/39.6e3 = 2305 K"),
      h4("Step 2 - what the numbers mean", "પગલું 2 - આંકડાનો અર્થ"),
      math("a hot alumina part dropped in water sees about 200 K, so it cracks",
           "a glass part cracks at 62 K, so it cracks in warm water",
           "silica at 2305 K survives any quench a workshop can give it"),
      eq("alumina 97 K,  soda-lime glass 62 K,  fused silica 2305 K"),
      p("Fused silica is 24 times tougher against a quench than alumina, and it gets there not by being "
        "strong but by having almost no expansion: alpha 0.55e-6 against 8.0e-6 cancels the strength "
        "difference completely. That is why a laboratory crucible is silica and not alumina, and why a "
        "glass-ceramic cooktop can take a hot pan while ordinary window glass cannot.",
        "Fused silica quench સામે alumina કરતાં 24 ગણું ટકાઉ છે, અને એ તાકાત થી નહીં પણ લગભગ શૂન્ય "
        "expansion થી મળે: 0.55e-6 સામે 8.0e-6 તાકાતનો ફરક પૂરો કરી નાખે. તેથી lab ની crucible silica ની "
        "હોય, alumina ની નહીં, અને glass-ceramic cooktop ગરમ તવો ઝીલે જ્યારે સામાન્ય window glass નહીં."),
      check("R has the unit of temperature - if your answer comes out in MPa or in kelvin per metre, the "
            "bracket was assembled wrongly.",
            "R નું એકમ તાપમાન છે - જવાબ MPa કે kelvin પ્રતિ મીટરમાં આવે તો કૌંસ ખોટો ગોઠવાયો છે.")],
     6),

    ("A furnace wall, and what the insulation saves",
     "ભઠ્ઠીની દીવાલ, અને insulation શું બચાવે",
     "A furnace wall is 230 mm of firebrick (k 1.0 W/m K) on the hot side and 115 mm of insulating "
     "brick (k 0.12 W/m K) outside it. The hot face is at 1200 C and the cold face at 50 C. Find the "
     "heat loss per m2, the interface temperature, and the money saved per m2 in a month if the "
     "furnace runs continuously at Rs 8 per kWh.",
     "ભઠ્ઠીની દીવાલ ગરમ બાજુ 230 mm firebrick (k 1.0 W/m K) અને બહાર 115 mm insulating brick (k 0.12 "
     "W/m K) ની છે. ગરમ સપાટી 1200 C અને ઠંડી સપાટી 50 C છે. પ્રતિ m2 ઉષ્માનો વ્યય, interface નું તાપમાન, "
     "અને ભઠ્ઠી સતત ચાલે તો Rs 8 પ્રતિ kWh પર એક મહિનામાં પ્રતિ m2 કેટલા રૂપિયા બચે તે શોધો.",
     [h4("Step 1 - the two resistances", "પગલું 1 - બે resistance"),
      math("R1 = 0.230/1.00 = 0.230 m2 K/W      R2 = 0.115/0.12 = 0.958 m2 K/W",
           "sum = 1.188 m2 K/W"),
      h4("Step 2 - the heat flux and the interface", "પગલું 2 - heat flux અને interface"),
      math("q = (1200 - 50)/1.188 = 968 W per m2",
           "T(interface) = 1200 - 968 x 0.230 = 1200 - 223 = 977 C",
           "check from the cold side: 50 + 968 x 0.958 = 977 C"),
      h4("Step 3 - what the insulation saves", "પગલું 3 - insulation શું બચાવે"),
      math("bare firebrick: q = 1150/0.230 = 5000 W per m2",
           "saving = 5000 - 968 = 4032 W per m2 = 4.03 kW per m2",
           "one month = 720 h: 4.03 x 720 = 2903 kWh;  at Rs 8 = Rs 23,224 per m2"),
      eq("968 W per m2,  977 C at the joint,  Rs 23,224 per m2 per month saved"),
      p("The insulation is 115 mm thick against 230 mm of firebrick, and it takes 81 % of the "
        "temperature drop. That is the point of a two-layer wall: the cheap dense brick is there to "
        "resist the slag and the abrasion, and the thin, more expensive insulating layer is there to "
        "do the saving.",
        "Insulation 230 mm firebrick સામે 115 mm જ જાડું છે, અને તાપમાનનો 81 % ઘટાડો લે છે. બે સ્તરની "
        "દીવાલનો આ જ મુદ્દો છે: સસ્તી ગાઢ ઈંટ slag અને ઘસારો ઝીલવા, અને પાતળું મોંઘું અવાહક સ્તર બચત કરવા."),
      check("The flux must be the same through both layers - if your two interface temperatures differ, "
            "one of the resistances is wrong.",
            "બંને સ્તરમાંથી flux એક જ આવવો જોઈએ - બંને બાજુનું interface તાપમાન જુદું આવે તો એક resistance ખોટો છે.")],
     7),

    ("Porosity and absorption of a firebrick",
     "Firebrick નું porosity અને absorption",
     "A firebrick sample of bulk volume 120 cm3 weighs 320 g dry and 345 g after soaking in water. "
     "Find its bulk density, its water absorption, its apparent porosity and its true density, and say "
     "what that porosity does to the brick.",
     "120 cm3 bulk volume નો firebrick નમૂનો સૂકો 320 g અને પાણીમાં પલાળ્યા પછી 345 g છે. તેની bulk "
     "density, water absorption, apparent porosity અને true density શોધો, અને એ porosity ઈંટ સાથે શું "
     "કરે તે કહો.",
     [h4("Step 1 - the water that went in", "પગલું 1 - અંદર ગયેલું પાણી"),
      math("water absorbed = 345 - 320 = 25 g,  so 25 cm3 of open pore"),
      h4("Step 2 - the four numbers", "પગલું 2 - ચાર આંકડા"),
      math("bulk density   = 320/120 = 2.67 g/cm3",
           "water absorption = 25/320 x 100 = 7.8 %",
           "apparent porosity = 25/120 x 100 = 20.8 %",
           "true density    = 320/(120 - 25) = 3.37 g/cm3"),
      eq("2.67 g/cm3 bulk,  20.8 % open pore,  7.8 % absorption,  3.37 g/cm3 true"),
      p("One brick in five is empty space. That is why a firebrick insulates so well - the pores hold "
        "still air at 0.026 W/m K - and it is also why its cold crushing strength is 20 to 60 MPa "
        "against 3000 MPa for a dense alumina. Porosity buys insulation and pays for it in strength "
        "and in slag penetration, because the same open pores that let water in let slag in as well.",
        "ઈંટનો પાંચમો ભાગ ખાલી જગ્યા છે. તેથી જ firebrick એટલી સારી રીતે અવાહક છે - છિદ્રોમાં સ્થિર હવા "
        "0.026 W/m K પર રહે - અને તેથી જ તેની cold crushing strength 20 થી 60 MPa છે જ્યારે ગાઢ alumina ની "
        "3000 MPa. Porosity insulation ખરીદે અને તેની કિંમત તાકાત તથી slag ઘૂસવામાં ચૂકવે, કારણ કે જે "
        "છિદ્રોમાં પાણી ગયું તેમાં slag પણ જાય."),
      check("The two porosity routes must agree: 1 - 2.67/3.37 = 20.8 %, the same as 25/120.",
            "Porosity ના બંને રસ્તા મળવા જોઈએ: 1 - 2.67/3.37 = 20.8 %, જે 25/120 જ છે.")],
     6),

    ("An adhesive lap joint, and its factor of safety",
     "Adhesive lap joint, અને તેનું factor of safety",
     "A bracket is glued to a plate with an epoxy whose lap shear strength is 20 MPa. The overlap is "
     "25 mm wide and 40 mm long and the working load is 5 kN. Find the shear stress in the joint, its "
     "factor of safety, and the greatest load it may carry at a required factor of safety of 3.",
     "Bracket એક plate પર 20 MPa lap shear strength વાળા epoxy થી ગુંદાય છે. Overlap 25 mm પહોળું અને "
     "40 mm લાંબું છે અને કામનો લોડ 5 kN છે. જોડાણમાં shear stress, તેનું factor of safety, અને 3 નું "
     "factor of safety જોઈએ તો વધુમાં વધુ કેટલો લોડ ઉપાડી શકે તે શોધો.",
     [h4("Step 1 - the shear stress", "પગલું 1 - shear stress"),
      math("A = 25 x 40 = 1000 mm2      tau = P/A = 5000/1000 = 5.0 MPa"),
      h4("Step 2 - the factor of safety", "પગલું 2 - factor of safety"),
      math("SF = 20/5.0 = 4.0"),
      h4("Step 3 - the load allowed at SF 3", "પગલું 3 - SF 3 પર માન્ય લોડ"),
      math("tau_allow = 20/3 = 6.67 MPa",
           "P_max = 6.67 x 1000 = 6667 N = 6.67 kN"),
      eq("5.0 MPa working,  factor of safety 4.0,  6.67 kN at a factor of 3"),
      p("The joint is comfortable in shear, and that is the only reason it works. The same bracket in "
        "peel would carry a small fraction of 20 kN, because peel loads one adhesive line at a time "
        "instead of the whole area. A designer who wants the strength of the glue has to give it area "
        "in shear and keep the prying load out.",
        "જોડાણ shear માં આરામદાયક છે, અને એ જ એક કારણે ચાલે છે. એ જ bracket peel માં 20 kN નો થોડો ભાગ જ "
        "ઉપાડે, કારણ કે peel આખા area ને બદલે એક વખતે એક adhesive લાઇન પર લોડ નાખે. ગુંદરની તાકાત "
        "જોઈએ તો designer એ shear માં area આપવો પડે અને ઉચકવાનો લોડ દૂર રાખવો પડે."),
      check("Bond line thickness is not in this sum, but it decides the answer in practice: 0.1 - 0.2 mm "
            "is right, and a thick brittle line cracks before the sum says it should.",
            "Bond line ની જાડાઈ આ ગણતરીમાં નથી, પણ વ્યવહારમાં જવાબ એ જ નક્કી કરે: 0.1 - 0.2 mm સાચું છે, "
            "અને જાડી ભંગુર લાઇન ગણતરી કહે તે પહેલાં તૂટે.")],
     6),

    ("How thick must the insulator be",
     "Insulator કેટલું જાડું જોઈએ",
     "A bakelite support of dielectric strength 18 kV/mm is used on an 11 kV busbar. For a 3 mm sheet, "
     "find the breakdown voltage and the factor of safety at 11 kV; then find the least thickness that "
     "gives a factor of safety of 3, and say why the surface path is checked separately.",
     "18 kV/mm dielectric strength વાળું bakelite support 11 kV busbar પર વપરાય છે. 3 mm sheet માટે "
     "breakdown વોલ્ટેજ અને 11 kV પર factor of safety શોધો; પછી factor of safety 3 આપતી ઓછામાં ઓછી જાડાઈ "
     "શોધો, અને સપાટીનો રસ્તો અલગ કેમ ચકાસાય તે કહો.",
     [h4("Step 1 - the breakdown of the sheet", "પગલું 1 - sheet નું breakdown"),
      math("V_break = E_b x d = 18 x 3 = 54 kV"),
      h4("Step 2 - the factor of safety on 11 kV", "પગલું 2 - 11 kV પર factor of safety"),
      math("SF = 54/11 = 4.9"),
      h4("Step 3 - the thickness for a factor of 3", "પગલું 3 - factor 3 માટે જાડાઈ"),
      math("required withstand = 3 x 11 = 33 kV",
           "t = V/E_b = 33/18 = 1.83 mm,  so 2 mm is specified and 3 mm is comfortable"),
      eq("54 kV breakdown,  factor 4.9 at 11 kV,  1.83 mm needed for a factor of 3"),
      p("Thickness stops a puncture and nothing else. The flashover travels over the surface, so it is "
        "stopped by distance - the creepage length - and a wet or dusty surface has a far lower "
        "flashover voltage than a clean one. That is why a 3 mm sheet of bakelite on a 11 kV busbar is "
        "wrapped in a long ribbed porcelain or epoxy shed rather than left bare.",
        "જાડાઈ ફક્ત puncture રોકે. Flashover સપાટી પર થી પસાર થાય, તેથી તે અંતર - creepage લંબાઈ - થી "
        "રોકાય, અને ભીની કે ધૂળવાળી સપાટીનું flashover વોલ્ટેજ સાફ કરતાં ઘણું નીચું હોય. તેથી 11 kV busbar "
        "પરનું 3 mm bakelite નગ્ન નહીં, લાંબી ribbed porcelain કે epoxy છત્રીમાં લપેટાય."),
      check("Keep kV and mm together: 18 kV/mm times 3 mm is 54 kV, and never multiply by a factor of "
            "safety twice - once in the thickness and once in the load.",
            "kV અને mm સાથે રાખો: 18 kV/mm ગુણ્યા 3 mm એટલે 54 kV, અને factor of safety બે વાર ન લગાવો - "
            "એક વાર જાડાઈમાં અને ફરી લોડમાં નહીં.")],
     6),
]

PRACTICE = [(tr(h_en, h_gu), tr(q_en, q_gu), body(*parts_), m)
            for (h_en, h_gu, q_en, q_gu, parts_, m) in _PRACTICE]

EXAM = [{"q": q, "marks": m} for _, q, _, m in PRACTICE]
PRACTICE_ANSWERS = [a for _, _, a, _ in PRACTICE]

SOURCES = [
    ("GTU DI01000181 Engineering Materials Science syllabus (uploaded PDF, w.e.f. 2024-25)",
     "https://syllabus.gtu.ac.in/"),
    ("O. P. Khanna - Material Science and Metallurgy, Dhanpat Rai (ceramics, refractories, "
     "insulators, abrasives)", "https://www.dhanpatrai.com/"),
    ("V. Raghavan - Materials Science and Engineering, Prentice Hall India (ceramics, composites, "
     "failure of brittle materials)", "https://www.pearson.com/"),
    ("Substech open materials science reference - non-metallic materials, refractories, ceramics",
     "https://www.substech.com/dokuwiki/doku.php?id=classification_of_materials"),
    ("MatWeb material property data - polymer, ceramic and elastomer property tables",
     "https://www.matweb.com/"),
    ("BIS - IS 4854 rubber compounding and IS 1528 refractory test methods",
     "https://www.bis.gov.in/"),
]
