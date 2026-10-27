"""Computer Networks (DI03000051) - Unit 3 notes part A: 3.1 Guided media.
Part B (3.2 unguided media) and part C (3.3 network devices) are in content_DI03000051_u3_notes_b / _c."""
from content_DI03000011_u1_notes_a import T
from content_DI03000041_u1_notes import tbl
from content_DI03000051_u1_notes_b import adv

CAT_EN = tbl(["Category", "Max data rate", "Use"], [
    ("Cat 3", "10 Mbps", "Telephone, old 10BaseT LAN"), ("Cat 5", "100 Mbps", "Fast Ethernet"),
    ("Cat 5e", "1 Gbps", "Gigabit Ethernet (most common)"), ("Cat 6", "1-10 Gbps (10 G up to 55 m)", "Gigabit / 10G LAN"),
    ("Cat 6a", "10 Gbps (100 m)", "Data centres"), ("Cat 7 / 8", "10-40 Gbps", "Shielded, data centres")])
CAT_GU = tbl(["Category", "મહત્તમ data rate", "ઉપયોગ"], [
    ("Cat 3", "10 Mbps", "Telephone, જૂનું 10BaseT LAN"), ("Cat 5", "100 Mbps", "Fast Ethernet"),
    ("Cat 5e", "1 Gbps", "Gigabit Ethernet (સૌથી સામાન્ય)"), ("Cat 6", "1-10 Gbps (10 G 55 m સુધી)", "Gigabit / 10G LAN"),
    ("Cat 6a", "10 Gbps (100 m)", "Data centres"), ("Cat 7 / 8", "10-40 Gbps", "Shielded, data centres")])

UTPSTP_EN = tbl(["UTP", "STP"], [
    ("Unshielded Twisted Pair", "Shielded Twisted Pair"), ("No metal shield", "Metal foil / braided shield around pairs"),
    ("Cheaper, lighter, flexible, easy to install", "Costly, heavier, bulky, harder to install"),
    ("More affected by noise and crosstalk", "Better protection from EMI and crosstalk"),
    ("Used in LANs, telephone lines", "Used in noisy industrial areas, data centres"), ("Connector RJ-45 / RJ-11", "Shielded RJ-45; shield must be grounded")])
UTPSTP_GU = tbl(["UTP", "STP"], [
    ("Unshielded Twisted Pair", "Shielded Twisted Pair"), ("Metal shield નથી", "Pairs ફરતે metal foil / braided shield"),
    ("સસ્તું, હલકું, flexible, install કરવું સહેલું", "ખર્ચાળ, ભારે, જાડું, install કરવું મુશ્કેલ"),
    ("Noise અને crosstalk ની વધુ અસર", "EMI અને crosstalk થી વધુ રક્ષણ"),
    ("LANs, telephone lines માં વપરાય", "Noisy industrial વિસ્તારો, data centres માં વપરાય"), ("Connector RJ-45 / RJ-11", "Shielded RJ-45; shield ground કરવું જરૂરી")])

PINS_EN = tbl(["Pin", "T568A", "T568B"], [
    ("1", "White-green", "White-orange"), ("2", "Green", "Orange"), ("3", "White-orange", "White-green"), ("4", "Blue", "Blue"),
    ("5", "White-blue", "White-blue"), ("6", "Orange", "Green"), ("7", "White-brown", "White-brown"), ("8", "Brown", "Brown")])
PINS_GU = tbl(["Pin", "T568A", "T568B"], [
    ("1", "White-green", "White-orange"), ("2", "Green", "Orange"), ("3", "White-orange", "White-green"), ("4", "Blue", "Blue"),
    ("5", "White-blue", "White-blue"), ("6", "Orange", "Green"), ("7", "White-brown", "White-brown"), ("8", "Brown", "Brown")])

FMODE_EN = tbl(["Point", "Single mode", "Multimode"], [
    ("Core diameter", "8-10 µm (very thin)", "50 or 62.5 µm"), ("Light source", "Laser", "LED / laser"),
    ("Paths of light", "One", "Many (step / graded index)"), ("Distance", "Up to 40-100 km", "Up to about 2 km"),
    ("Bandwidth", "Very high", "Lower (modal dispersion)"), ("Cost", "Cable cheaper, equipment costly", "Equipment cheaper"),
    ("Use", "Telecom, Internet backbone, MAN / WAN", "LAN, campus, data centre")])
FMODE_GU = tbl(["મુદ્દો", "Single mode", "Multimode"], [
    ("Core diameter", "8-10 µm (ખૂબ પાતળો)", "50 અથવા 62.5 µm"), ("Light source", "Laser", "LED / laser"),
    ("પ્રકાશના માર્ગો", "એક", "ઘણા (step / graded index)"), ("અંતર", "40-100 km સુધી", "લગભગ 2 km સુધી"),
    ("Bandwidth", "ખૂબ વધુ", "ઓછી (modal dispersion)"), ("ખર્ચ", "Cable સસ્તો, equipment મોંઘું", "Equipment સસ્તું"),
    ("ઉપયોગ", "Telecom, Internet backbone, MAN / WAN", "LAN, campus, data centre")])

GCMP_EN = tbl(["Point", "Twisted pair", "Coaxial", "Fiber optic"], [
    ("Signal", "Electrical", "Electrical", "Light"), ("Bandwidth", "Low-medium", "Medium-high", "Very high"),
    ("Distance without repeater", "100 m", "185-500 m", "2-100 km"), ("Noise immunity", "Low (UTP)", "Good", "Complete (no EMI)"),
    ("Cost", "Lowest", "Medium", "Highest"), ("Installation", "Easiest", "Moderate", "Difficult, skilled"),
    ("Security", "Easy to tap", "Moderate", "Very hard to tap"), ("Connector", "RJ-45, RJ-11", "BNC, F-type", "SC, ST, LC")])
GCMP_GU = tbl(["મુદ્દો", "Twisted pair", "Coaxial", "Fiber optic"], [
    ("Signal", "Electrical", "Electrical", "પ્રકાશ"), ("Bandwidth", "ઓછી-મધ્યમ", "મધ્યમ-વધુ", "ખૂબ વધુ"),
    ("Repeater વગર અંતર", "100 m", "185-500 m", "2-100 km"), ("Noise સામે રક્ષણ", "ઓછું (UTP)", "સારું", "સંપૂર્ણ (EMI નહીં)"),
    ("ખર્ચ", "સૌથી ઓછો", "મધ્યમ", "સૌથી વધુ"), ("Installation", "સૌથી સહેલું", "મધ્યમ", "મુશ્કેલ, કુશળ"),
    ("Security", "Tap કરવું સહેલું", "મધ્યમ", "Tap કરવું ખૂબ મુશ્કેલ"), ("Connector", "RJ-45, RJ-11", "BNC, F-type", "SC, ST, LC")])

TP_AD = adv(["Cheapest and most widely available medium.", "Light, thin and flexible; easy to install and terminate.",
             "Supports high data rates (1-10 Gbps) over short distances.", "Twisting reduces noise and crosstalk."],
            ["Short distance: about 100 m per segment, then a repeater / switch is needed.", "Susceptible to EMI and noise (UTP); attenuation is high.",
             "Lower bandwidth than coaxial and fiber.", "Easy to tap, so less secure."],
            ["સૌથી સસ્તું અને વ્યાપક રીતે ઉપલબ્ધ medium.", "હલકું, પાતળું અને flexible; install અને terminate કરવું સહેલું.",
             "ટૂંકા અંતર માટે વધુ data rates (1-10 Gbps) support કરે.", "Twisting noise અને crosstalk ઘટાડે."],
            ["ટૂંકું અંતર: segment દીઠ લગભગ 100 m, પછી repeater / switch જોઈએ.", "EMI અને noise ની અસર (UTP); attenuation વધુ.",
             "Coaxial અને fiber કરતાં ઓછી bandwidth.", "Tap કરવું સહેલું, તેથી ઓછું secure."])
CO_AD = adv(["Higher bandwidth and longer distance than twisted pair.", "Better shielding: less affected by noise and interference.",
             "Durable; supports many TV channels (broadband).", "Cheaper than fiber."],
            ["Thicker, heavier and less flexible than twisted pair; harder to install.", "A fault in a bus-type coaxial cable can bring down the whole network.",
             "Costlier than twisted pair; replaced by UTP and fiber in LANs."],
            ["Twisted pair કરતાં વધુ bandwidth અને લાંબું અંતર.", "સારું shielding: noise અને interference ની ઓછી અસર.",
             "ટકાઉ; ઘણી TV channels (broadband) support કરે.", "Fiber કરતાં સસ્તું."],
            ["Twisted pair કરતાં જાડું, ભારે અને ઓછું flexible; install કરવું મુશ્કેલ.", "Bus-type coaxial cable માં fault આખું network બંધ કરી શકે.",
             "Twisted pair કરતાં મોંઘું; LANs માં UTP અને fiber એ સ્થાન લીધું."])
FO_AD = adv(["Very high bandwidth (Tbps possible) and data rate.", "Very low attenuation: long distance (up to 100 km) without repeaters.",
             "Immune to electromagnetic interference and lightning; no crosstalk.", "Very secure: difficult to tap without detection.",
             "Thin and light; glass does not corrode."],
            ["Expensive cable, connectors and equipment (lasers, optical transceivers).", "Installation and splicing need skill and special tools.",
             "Fragile: glass breaks if bent too sharply.", "Light travels in one direction: two fibers are needed for two-way communication."],
            ["ખૂબ વધુ bandwidth (Tbps શક્ય) અને data rate.", "ખૂબ ઓછું attenuation: repeaters વગર લાંબું અંતર (100 km સુધી).",
             "Electromagnetic interference અને વીજળીથી મુક્ત; crosstalk નહીં.", "ખૂબ secure: પકડાયા વગર tap કરવું મુશ્કેલ.",
             "પાતળું અને હલકું; glass કાટ લાગતો નથી."],
            ["મોંઘા cable, connectors અને equipment (lasers, optical transceivers).", "Installation અને splicing માટે કુશળતા અને ખાસ સાધનો જોઈએ.",
             "નાજુક: વધુ વાળવાથી glass તૂટે.", "પ્રકાશ એક દિશામાં જાય: two-way communication માટે બે fibers જોઈએ."])

SEC_3_1 = {
    "title": {"en": "3.1 Guided Media", "gu": "3.1 Guided Media"},
    "items": [
        T("3.1.1 Transmission Media and Classification", "3.1.1 Transmission Media અને વર્ગીકરણ",
          """<p>A <b>transmission medium</b> is the <b>physical path</b> between the sender and the receiver through which signals travel. It is located below the physical layer and is controlled by it (sometimes called layer 0).</p>
<h4>Classification</h4>
<ul>
<li><b>Guided (wired / bounded) media:</b> provide a conduit from one device to another; the signal is directed and contained by the physical limits of the medium. Examples: <b>twisted pair cable</b>, <b>coaxial cable</b> (both carry electric current, copper) and <b>fiber optic cable</b> (carries light).</li>
<li><b>Unguided (wireless / unbounded) media:</b> transport electromagnetic waves <b>without a physical conductor</b>; signals are broadcast through free space (air, vacuum, water). Examples: <b>radio waves, microwaves, infrared</b>; satellite communication uses microwaves.</li>
</ul>
<h4>Factors for selecting a medium</h4>
<p>Bandwidth / data rate required, distance (attenuation), cost, ease of installation, noise immunity, security, and the environment (indoor / outdoor).</p>
<p><b>Transmission impairments:</b> <b>attenuation</b> (loss of signal strength with distance), <b>distortion</b> (change of signal shape) and <b>noise</b> (unwanted signals: thermal, crosstalk, EMI).</p>""",
          """<p><b>Transmission medium</b> એ sender અને receiver વચ્ચેનો <b>physical માર્ગ</b> છે જેમાંથી signals પસાર થાય છે. તે physical layer ની નીચે આવેલું છે અને તેના દ્વારા નિયંત્રિત થાય છે (ક્યારેક layer 0 કહેવાય).</p>
<h4>વર્ગીકરણ</h4>
<ul>
<li><b>Guided (wired / bounded) media:</b> એક device થી બીજા device સુધી માર્ગ આપે; signal medium ની physical મર્યાદામાં દિશાબદ્ધ અને સમાયેલો રહે. ઉદાહરણો: <b>twisted pair cable</b>, <b>coaxial cable</b> (બંને electric current વહન કરે, copper) અને <b>fiber optic cable</b> (પ્રકાશ વહન કરે).</li>
<li><b>Unguided (wireless / unbounded) media:</b> <b>physical conductor વગર</b> electromagnetic waves લઈ જાય; signals મુક્ત અવકાશ (હવા, vacuum, પાણી) માં broadcast થાય. ઉદાહરણો: <b>radio waves, microwaves, infrared</b>; satellite communication microwaves વાપરે.</li>
</ul>
<h4>Medium પસંદ કરવાનાં પરિબળો</h4>
<p>જરૂરી bandwidth / data rate, અંતર (attenuation), ખર્ચ, installation ની સરળતા, noise immunity, security, અને વાતાવરણ (indoor / outdoor).</p>
<p><b>Transmission impairments:</b> <b>attenuation</b> (અંતર સાથે signal ની તાકાત ઘટવી), <b>distortion</b> (signal નો આકાર બદલાવો) અને <b>noise</b> (અનિચ્છનીય signals: thermal, crosstalk, EMI).</p>""",
          diagram="cn3_class"),
        T("3.1.2 Twisted Pair Cable: UTP and STP", "3.1.2 Twisted Pair Cable: UTP અને STP",
          """<p>A twisted pair consists of <b>two insulated copper conductors twisted together</b>. One wire carries the signal and the other is the ground reference. <b>Twisting</b> makes both wires equally affected by external noise, so the receiver (which uses the difference) cancels the noise; it also reduces <b>crosstalk</b> between pairs. A LAN cable has <b>4 pairs (8 wires)</b> with colour codes orange, green, blue and brown.</p>
<h4>Types</h4>
<ul><li><b>UTP (Unshielded Twisted Pair):</b> no metal shield; most common LAN cable.</li><li><b>STP (Shielded Twisted Pair):</b> each pair and/or the whole cable is covered with metal foil or braided mesh, which reduces electromagnetic interference (EMI) and crosstalk.</li></ul>
""" + UTPSTP_EN + """
<h4>Categories (EIA/TIA)</h4>
""" + CAT_EN + """
<h4>Connectors</h4>
<p><b>RJ-45</b> (8 pins, LAN cables), <b>RJ-11</b> (4/6 pins, telephone).</p>
<h4>Applications</h4>
<p>Ethernet LANs (10BaseT, 100BaseTX, 1000BaseT), telephone lines, DSL broadband, CCTV (with baluns).</p>
""" + TP_AD[0],
          """<p>Twisted pair માં <b>એકબીજા સાથે વળેલા બે insulated copper conductors</b> હોય છે. એક wire signal લઈ જાય અને બીજો ground reference છે. <b>Twisting</b> થી બંને wires પર બહારના noise ની સરખી અસર થાય, તેથી receiver (જે તફાવત વાપરે છે) noise રદ કરે; તે pairs વચ્ચેનું <b>crosstalk</b> પણ ઘટાડે. LAN cable માં orange, green, blue અને brown colour codes સાથે <b>4 pairs (8 wires)</b> હોય છે.</p>
<h4>પ્રકારો</h4>
<ul><li><b>UTP (Unshielded Twisted Pair):</b> metal shield નથી; સૌથી સામાન્ય LAN cable.</li><li><b>STP (Shielded Twisted Pair):</b> દરેક pair અને/અથવા આખો cable metal foil કે braided mesh થી ઢંકાયેલો, જે electromagnetic interference (EMI) અને crosstalk ઘટાડે.</li></ul>
""" + UTPSTP_GU + """
<h4>Categories (EIA/TIA)</h4>
""" + CAT_GU + """
<h4>Connectors</h4>
<p><b>RJ-45</b> (8 pins, LAN cables), <b>RJ-11</b> (4/6 pins, telephone).</p>
<h4>ઉપયોગો</h4>
<p>Ethernet LANs (10BaseT, 100BaseTX, 1000BaseT), telephone lines, DSL broadband, CCTV (baluns સાથે).</p>
""" + TP_AD[1],
          diagram="cn3_tp"),
        T("3.1.3 Straight and Cross UTP Cable (Practical 3)", "3.1.3 Straight અને Cross UTP Cable (Practical 3)",
          """<p>UTP cables are terminated with <b>RJ-45</b> connectors according to the EIA/TIA <b>T568A</b> or <b>T568B</b> colour standards. Hold the connector with the clip facing down and the pins towards you: pin 1 is on the left.</p>
""" + PINS_EN + """
<h4>Types of cable</h4>
<ul>
<li><b>Straight-through cable:</b> the <b>same standard at both ends</b> (B-B or A-A). Pin 1 connects to pin 1, and so on. Used to connect <b>different devices</b>: PC to switch / hub, switch to router.</li>
<li><b>Crossover cable:</b> <b>T568A at one end and T568B at the other</b>. Pins 1-3 and 2-6 are swapped so that the transmit pair of one device reaches the receive pair of the other. Used to connect <b>similar devices</b>: PC to PC, switch to switch, router to router (modern ports with <b>Auto-MDIX</b> work with either cable).</li>
<li><b>Rollover (console) cable:</b> pin order fully reversed (1-8, 2-7 …); connects a PC to the console port of a router / switch.</li>
</ul>
<h4>Procedure</h4>
<ol><li>Tools: Cat5e / Cat6 cable, RJ-45 connectors, <b>crimping tool</b>, wire stripper, <b>LAN cable tester</b>.</li><li>Strip about 2-3 cm of the outer jacket without cutting the wires.</li><li>Untwist the pairs and arrange the 8 wires in the T568B (or T568A) order; straighten and cut them evenly to about 1.5 cm.</li><li>Insert the wires fully into the RJ-45 connector (clip down) so that every wire touches the end; the jacket should go inside the connector.</li><li>Crimp firmly with the crimping tool.</li><li>Repeat at the other end: same standard for straight, the other standard for cross.</li><li>Test with the LAN tester: for straight, LEDs 1-8 light in the same order on both units; for cross, 1→3, 2→6, 3→1, 6→2.</li></ol>""",
          """<p>UTP cables EIA/TIA <b>T568A</b> કે <b>T568B</b> colour standards મુજબ <b>RJ-45</b> connectors વડે terminate થાય છે. Connector ને clip નીચે અને pins તમારી તરફ રાખી પકડો: pin 1 ડાબી બાજુ છે.</p>
""" + PINS_GU + """
<h4>Cable ના પ્રકારો</h4>
<ul>
<li><b>Straight-through cable:</b> <b>બંને છેડે સરખું standard</b> (B-B અથવા A-A). Pin 1 pin 1 સાથે, વગેરે. <b>જુદા devices</b> જોડવા વપરાય: PC થી switch / hub, switch થી router.</li>
<li><b>Crossover cable:</b> <b>એક છેડે T568A અને બીજા છેડે T568B</b>. Pins 1-3 અને 2-6 અદલાબદલી થાય જેથી એક device ની transmit pair બીજાની receive pair સુધી પહોંચે. <b>સરખા devices</b> જોડવા વપરાય: PC થી PC, switch થી switch, router થી router (<b>Auto-MDIX</b> વાળા આધુનિક ports કોઈ પણ cable સાથે કામ કરે).</li>
<li><b>Rollover (console) cable:</b> pin ક્રમ સંપૂર્ણ ઊલટો (1-8, 2-7 …); PC ને router / switch ના console port સાથે જોડે.</li>
</ul>
<h4>પદ્ધતિ</h4>
<ol><li>સાધનો: Cat5e / Cat6 cable, RJ-45 connectors, <b>crimping tool</b>, wire stripper, <b>LAN cable tester</b>.</li><li>Wires કાપ્યા વગર બહારનું jacket લગભગ 2-3 cm છોલો.</li><li>Pairs ખોલી 8 wires ને T568B (કે T568A) ક્રમમાં ગોઠવો; સીધા કરી લગભગ 1.5 cm સરખા કાપો.</li><li>Wires ને RJ-45 connector (clip નીચે) માં પૂરા દાખલ કરો જેથી દરેક wire છેડાને અડે; jacket connector ની અંદર જવું જોઈએ.</li><li>Crimping tool થી મજબૂત crimp કરો.</li><li>બીજા છેડે પુનરાવર્તન કરો: straight માટે સરખું standard, cross માટે બીજું standard.</li><li>LAN tester થી test કરો: straight માટે બંને units પર LEDs 1-8 સરખા ક્રમમાં ઝબકે; cross માટે 1→3, 2→6, 3→1, 6→2.</li></ol>""",
          diagram="cn3_rj45"),
        T("3.1.4 Coaxial Cable", "3.1.4 Coaxial Cable",
          """<p>Coaxial cable (coax) carries signals of higher frequency than twisted pair. It has a <b>central copper conductor</b> enclosed in an <b>insulating sheath (dielectric)</b>, which is encased in an <b>outer conductor of metal foil / braid</b> (acting as a shield and as the second conductor), all covered by a <b>protective plastic jacket</b>. Both conductors share the same axis, hence "co-axial".</p>
<h4>Standards (Radio Government ratings)</h4>
<ul><li><b>RG-59</b> (75 Ω): cable TV, CCTV.</li><li><b>RG-58</b> (50 Ω): thin Ethernet (10Base2, 185 m).</li><li><b>RG-11</b> (50 Ω): thick Ethernet (10Base5, 500 m).</li><li>RG-6: satellite / cable TV and broadband.</li></ul>
<h4>Connectors</h4>
<ul><li><b>BNC connector</b> (Bayonet Neill-Concelman): connects the end of the cable to a device (TV, NIC).</li><li><b>BNC T-connector:</b> used in Ethernet bus networks to branch out to a computer.</li><li><b>BNC terminator:</b> at the ends of the bus to prevent signal reflection.</li><li><b>F-type connector:</b> cable TV and set-top boxes.</li></ul>
<h4>Applications</h4>
<p>Cable TV distribution, CCTV cameras, old Ethernet LANs (bus topology), long-distance telephone trunks, cable broadband Internet (DOCSIS), connecting antennas to radios.</p>
""" + CO_AD[0],
          """<p>Coaxial cable (coax) twisted pair કરતાં વધુ frequency ના signals વહન કરે છે. તેમાં <b>વચ્ચે copper conductor</b> હોય છે જે <b>insulating sheath (dielectric)</b> થી ઢંકાયેલો હોય, તે <b>metal foil / braid ના બહારના conductor</b> (shield અને બીજા conductor તરીકે કામ કરે) માં બંધ હોય, અને બધું <b>રક્ષણાત્મક plastic jacket</b> થી ઢંકાયેલું હોય. બંને conductors ની ધરી (axis) એક જ છે, તેથી "co-axial".</p>
<h4>Standards (Radio Government ratings)</h4>
<ul><li><b>RG-59</b> (75 Ω): cable TV, CCTV.</li><li><b>RG-58</b> (50 Ω): thin Ethernet (10Base2, 185 m).</li><li><b>RG-11</b> (50 Ω): thick Ethernet (10Base5, 500 m).</li><li>RG-6: satellite / cable TV અને broadband.</li></ul>
<h4>Connectors</h4>
<ul><li><b>BNC connector</b> (Bayonet Neill-Concelman): cable ના છેડાને device (TV, NIC) સાથે જોડે.</li><li><b>BNC T-connector:</b> Ethernet bus networks માં computer સુધી શાખા કાઢવા.</li><li><b>BNC terminator:</b> signal reflection અટકાવવા bus ના છેડે.</li><li><b>F-type connector:</b> cable TV અને set-top boxes.</li></ul>
<h4>ઉપયોગો</h4>
<p>Cable TV distribution, CCTV cameras, જૂના Ethernet LANs (bus topology), લાંબા અંતરની telephone trunks, cable broadband Internet (DOCSIS), antennas ને radios સાથે જોડવા.</p>
""" + CO_AD[1],
          diagram="cn3_coax"),
        T("3.1.5 Fiber Optic Cable", "3.1.5 Fiber Optic Cable",
          """<p>A fiber optic cable is made of <b>glass or plastic</b> and transmits signals in the form of <b>light</b>. It consists of a <b>core</b> (thin glass with higher refractive index n1), surrounded by <b>cladding</b> (glass with lower refractive index n2), a <b>buffer coating</b> (plastic, protects from moisture) and an outer <b>jacket</b> (with strength members such as Kevlar).</p>
<h4>Principle: total internal reflection</h4>
<p>When light travels from a denser medium (core) to a less dense medium (cladding) and the angle of incidence is <b>greater than the critical angle</b>, the light is reflected completely back into the core. So light travels along the fiber by repeated reflection, even around gentle bends. Critical angle: sin θc = n2 / n1. A <b>LED or laser</b> converts electrical signals to light at the sender; a <b>photodiode</b> converts light back at the receiver.</p>
<h4>Propagation modes</h4>
<ul>
<li><b>Multimode step-index:</b> core density is uniform and changes abruptly at the cladding; many beams take different paths, so pulses spread (modal dispersion). Short distances.</li>
<li><b>Multimode graded-index:</b> refractive index is highest at the centre and decreases gradually towards the edge; beams curve, reducing distortion.</li>
<li><b>Single mode:</b> very thin core (8-10 µm) and a laser source; light travels almost straight in one path; least distortion, highest bandwidth and longest distance.</li>
</ul>
""" + FMODE_EN + """
<h4>Connectors</h4>
<p><b>SC</b> (subscriber channel, push-pull), <b>ST</b> (straight tip, bayonet), <b>LC</b> (small form factor), <b>MT-RJ</b> (duplex, same size as RJ-45).</p>
<h4>Applications</h4>
<p>Internet backbone and undersea cables, FTTH broadband (JioFiber, Airtel Xstream), LAN backbones between buildings, cable TV trunks, medical endoscopy, military networks.</p>
""" + FO_AD[0],
          """<p>Fiber optic cable <b>glass કે plastic</b> નો બનેલો છે અને signals ને <b>પ્રકાશ</b> સ્વરૂપે મોકલે છે. તેમાં <b>core</b> (વધુ refractive index n1 વાળો પાતળો glass), તેની ફરતે <b>cladding</b> (ઓછા refractive index n2 વાળો glass), <b>buffer coating</b> (plastic, ભેજથી રક્ષણ) અને બહાર <b>jacket</b> (Kevlar જેવા strength members સાથે) હોય છે.</p>
<h4>સિદ્ધાંત: total internal reflection</h4>
<p>પ્રકાશ ઘટ્ટ માધ્યમ (core) થી ઓછા ઘટ્ટ માધ્યમ (cladding) માં જાય અને આપાત કોણ <b>critical angle કરતાં મોટો</b> હોય ત્યારે પ્રકાશ સંપૂર્ણ રીતે core માં પાછો પરાવર્તિત થાય. તેથી પ્રકાશ વારંવાર પરાવર્તન દ્વારા fiber માં આગળ જાય, હળવા વળાંકોમાં પણ. Critical angle: sin θc = n2 / n1. Sender પર <b>LED કે laser</b> electrical signals ને પ્રકાશમાં ફેરવે; receiver પર <b>photodiode</b> પ્રકાશને પાછો ફેરવે.</p>
<h4>Propagation modes</h4>
<ul>
<li><b>Multimode step-index:</b> core ની ઘનતા એકસરખી અને cladding પાસે અચાનક બદલાય; ઘણાં કિરણો જુદા માર્ગ લે, તેથી pulses ફેલાય (modal dispersion). ટૂંકાં અંતર.</li>
<li><b>Multimode graded-index:</b> refractive index કેન્દ્રમાં સૌથી વધુ અને ધાર તરફ ધીમે ધીમે ઘટે; કિરણો વળે, distortion ઘટે.</li>
<li><b>Single mode:</b> ખૂબ પાતળો core (8-10 µm) અને laser source; પ્રકાશ લગભગ સીધો એક માર્ગે જાય; સૌથી ઓછું distortion, સૌથી વધુ bandwidth અને સૌથી લાંબું અંતર.</li>
</ul>
""" + FMODE_GU + """
<h4>Connectors</h4>
<p><b>SC</b> (subscriber channel, push-pull), <b>ST</b> (straight tip, bayonet), <b>LC</b> (small form factor), <b>MT-RJ</b> (duplex, RJ-45 જેટલું).</p>
<h4>ઉપયોગો</h4>
<p>Internet backbone અને દરિયાઈ cables, FTTH broadband (JioFiber, Airtel Xstream), buildings વચ્ચે LAN backbones, cable TV trunks, medical endoscopy, military networks.</p>
""" + FO_AD[1],
          diagram="cn3_fiber", examples=["cn3n4"]),
        T("3.1.6 Fiber Modes and Comparison of Guided Media", "3.1.6 Fiber Modes અને Guided Media ની સરખામણી",
          """<p>The three guided media differ in signal type, bandwidth, distance and cost. Fiber is used where very high speed or long distance is needed; twisted pair is used for the last connection to computers; coaxial is now mostly used for cable TV.</p>
""" + GCMP_EN + """
<p><b>Propagation speed</b> in copper and fiber is about 2 × 10⁸ m/s (two-thirds of the speed of light), so a signal needs about 5 µs per km.</p>""",
          """<p>ત્રણ guided media signal ના પ્રકાર, bandwidth, અંતર અને ખર્ચમાં જુદા પડે છે. ખૂબ વધુ speed કે લાંબું અંતર જોઈએ ત્યાં fiber; computers સુધીના છેલ્લા જોડાણ માટે twisted pair; coaxial હવે મોટે ભાગે cable TV માટે વપરાય છે.</p>
""" + GCMP_GU + """
<p>Copper અને fiber માં <b>propagation speed</b> લગભગ 2 × 10⁸ m/s (પ્રકાશની ઝડપનો બે-તૃતીયાંશ) છે, તેથી signal ને km દીઠ લગભગ 5 µs લાગે.</p>""",
          diagram="cn3_fiber_modes", examples=["cn3n5"]),
    ]}

from content_DI03000051_u3_notes_b import SEC_3_2  # noqa: E402
from content_DI03000051_u3_notes_c import SEC_3_3  # noqa: E402

NOTES = [SEC_3_1, SEC_3_2, SEC_3_3]
