"""Computer Networks (DI03000051) - Unit 3 extras: transmission numericals (computed), equations, viva, exam questions."""
import math
from content_DI03000011_u1_extras import N, E, V, X

C = 3e8
SUP = str.maketrans("0123456789-", "⁰¹²³⁴⁵⁶⁷⁸⁹⁻")


def sci(x):
    e = math.floor(math.log10(x)); m = x / 10 ** e
    return (f"{m:g} × " if m != 1 else "") + "10" + str(e).translate(SUP)


# n1: GEO satellite delay
H_GEO = 35786  # km
t_up = H_GEO * 1000 / C
t_one = 2 * t_up
n1 = N("cn3n1", f"A geostationary satellite is at a height of {H_GEO:,} km. Find the propagation delay (a) from earth station to satellite, (b) from one earth station to another through the satellite, and (c) for a reply to come back (round trip). Take c = 3 × 10⁸ m/s and assume the stations are directly below the satellite.",
       f"Geostationary satellite {H_GEO:,} km ઊંચાઈએ છે. Propagation delay શોધો (a) earth station થી satellite, (b) satellite મારફતે એક earth station થી બીજા સુધી, અને (c) જવાબ પાછો આવવા માટે (round trip). c = 3 × 10⁸ m/s લો અને stations satellite ની બરાબર નીચે છે તેમ માનો.",
       f"<p>Delay = distance / speed</p><p>(a) Uplink: {H_GEO * 1000:,} m / 3 × 10⁸ = <b>{t_up:.4f} s ≈ {t_up * 1000:.0f} ms</b></p>"
       f"<p>(b) Up + down = 2 × {t_up:.4f} = <b>{t_one:.4f} s ≈ {t_one * 1000:.0f} ms</b></p>"
       f"<p>(c) Round trip (question + reply) = 2 × {t_one:.4f} = <b>{2 * t_one:.3f} s</b>, about half a second, which is why satellite phone calls have a noticeable pause.</p>",
       f"<p>Delay = અંતર / ઝડપ</p><p>(a) Uplink: {H_GEO * 1000:,} m / 3 × 10⁸ = <b>{t_up:.4f} s ≈ {t_up * 1000:.0f} ms</b></p>"
       f"<p>(b) Up + down = 2 × {t_up:.4f} = <b>{t_one:.4f} s ≈ {t_one * 1000:.0f} ms</b></p>"
       f"<p>(c) Round trip (પ્રશ્ન + જવાબ) = 2 × {t_one:.4f} = <b>{2 * t_one:.3f} s</b>, લગભગ અડધી second, તેથી satellite phone calls માં સ્પષ્ટ વિરામ આવે છે.</p>")

# n2: microwave LOS
h1 = h2 = 100
d2 = 4.12 * (math.sqrt(h1) + math.sqrt(h2))
L2 = 400
hops = math.ceil(L2 / d2)
n2 = N("cn3n2", f"Two microwave antennas are mounted on towers of height {h1} m each. Find the maximum line-of-sight distance between them using d = 4.12 (√h1 + √h2) km. How many hops (tower-to-tower links) are needed for a {L2} km link?",
       f"બે microwave antennas દરેક {h1} m ઊંચા towers પર લગાવેલા છે. d = 4.12 (√h1 + √h2) km વાપરી તેમની વચ્ચે મહત્તમ line-of-sight અંતર શોધો. {L2} km ની link માટે કેટલા hops (tower-to-tower links) જોઈએ?",
       f"<p>d = 4.12 (√{h1} + √{h2}) = 4.12 ({math.sqrt(h1):g} + {math.sqrt(h2):g}) = <b>{d2:.1f} km</b></p>"
       f"<p>Hops = {L2} / {d2:.1f} = {L2 / d2:.2f} → round up = <b>{hops} hops</b> ({hops - 1} intermediate repeater towers)</p>"
       f"<p>Doubling the tower height does not double the distance, because d depends on √h.</p>",
       f"<p>d = 4.12 (√{h1} + √{h2}) = 4.12 ({math.sqrt(h1):g} + {math.sqrt(h2):g}) = <b>{d2:.1f} km</b></p>"
       f"<p>Hops = {L2} / {d2:.1f} = {L2 / d2:.2f} → ઉપર round = <b>{hops} hops</b> ({hops - 1} વચ્ચેના repeater towers)</p>"
       f"<p>Tower ની ઊંચાઈ બમણી કરવાથી અંતર બમણું થતું નથી, કારણ કે d √h પર આધારિત છે.</p>")

# n3: wavelength
cases = [("Wi-Fi", 2.4e9), ("FM radio", 100e6), ("Satellite Ku band", 12e9)]
rows = "".join(f"<li>{nm}: λ = 3 × 10⁸ / {sci(f)} = <b>{C / f:.4g} m</b>" + (f" = {C / f * 100:.3g} cm" if C / f < 1 else "") + "</li>" for nm, f in cases)
rows_gu = rows
n3 = N("cn3n3", "Find the wavelength of (a) Wi-Fi at 2.4 GHz, (b) FM radio at 100 MHz, (c) a satellite Ku band signal at 12 GHz. Take c = 3 × 10⁸ m/s.",
       "તરંગલંબાઈ શોધો (a) 2.4 GHz પર Wi-Fi, (b) 100 MHz પર FM radio, (c) 12 GHz પર satellite Ku band signal. c = 3 × 10⁸ m/s લો.",
       f"<p>λ = c / f</p><ul>{rows}</ul><p>Higher frequency → shorter wavelength → smaller antenna (antenna size is a fraction of λ).</p>",
       f"<p>λ = c / f</p><ul>{rows_gu}</ul><p>વધુ frequency → ટૂંકી wavelength → નાનું antenna (antenna size λ નો અમુક ભાગ હોય).</p>")

# n4: fiber critical angle and NA
n_1, n_2 = 1.48, 1.46
thc = math.degrees(math.asin(n_2 / n_1))
NA = math.sqrt(n_1 ** 2 - n_2 ** 2)
acc = math.degrees(math.asin(NA))
n4 = N("cn3n4", f"An optical fiber has core refractive index n1 = {n_1} and cladding refractive index n2 = {n_2}. Find (a) the critical angle, (b) the numerical aperture and (c) the acceptance angle.",
       f"Optical fiber ના core નો refractive index n1 = {n_1} અને cladding નો n2 = {n_2} છે. શોધો (a) critical angle, (b) numerical aperture અને (c) acceptance angle.",
       f"<p>(a) sin θc = n2 / n1 = {n_2} / {n_1} = {n_2 / n_1:.4f} → θc = <b>{thc:.2f}°</b></p>"
       f"<p>(b) NA = √(n1² − n2²) = √({n_1 ** 2:.4f} − {n_2 ** 2:.4f}) = √{n_1 ** 2 - n_2 ** 2:.4f} = <b>{NA:.4f}</b></p>"
       f"<p>(c) Acceptance angle θa = sin⁻¹(NA) = <b>{acc:.2f}°</b></p>"
       f"<p>Light hitting the core-cladding boundary at more than {thc:.2f}° (from the normal) is totally internally reflected.</p>",
       f"<p>(a) sin θc = n2 / n1 = {n_2} / {n_1} = {n_2 / n_1:.4f} → θc = <b>{thc:.2f}°</b></p>"
       f"<p>(b) NA = √(n1² − n2²) = √({n_1 ** 2:.4f} − {n_2 ** 2:.4f}) = √{n_1 ** 2 - n_2 ** 2:.4f} = <b>{NA:.4f}</b></p>"
       f"<p>(c) Acceptance angle θa = sin⁻¹(NA) = <b>{acc:.2f}°</b></p>"
       f"<p>Core-cladding સીમા પર {thc:.2f}° (normal થી) થી વધુ ખૂણે પડતો પ્રકાશ total internal reflection પામે.</p>")

# n5: propagation and transmission time
v5, L5 = 2e8, 1000
tp = L5 / v5
size, rate = 1500 * 8, 100e6
tt = size / rate
n5 = N("cn3n5", f"A 1,500-byte frame is sent on a {L5 / 1000:g} km cable with propagation speed 2 × 10⁸ m/s at 100 Mbps. Find the propagation delay, the transmission time and the total time for the last bit to arrive.",
       f"1,500-byte frame {L5 / 1000:g} km cable પર 2 × 10⁸ m/s propagation speed સાથે 100 Mbps એ મોકલાય છે. Propagation delay, transmission time અને છેલ્લો bit પહોંચવાનો કુલ સમય શોધો.",
       f"<p>Propagation delay = distance / speed = {L5} / 2 × 10⁸ = <b>{tp * 1e6:g} µs</b></p>"
       f"<p>Transmission time = frame size / bandwidth = {size:,} bits / 10⁸ = <b>{tt * 1e6:g} µs</b></p>"
       f"<p>Total = {tt * 1e6:g} + {tp * 1e6:g} = <b>{(tt + tp) * 1e6:g} µs</b></p>",
       f"<p>Propagation delay = અંતર / ઝડપ = {L5} / 2 × 10⁸ = <b>{tp * 1e6:g} µs</b></p>"
       f"<p>Transmission time = frame size / bandwidth = {size:,} bits / 10⁸ = <b>{tt * 1e6:g} µs</b></p>"
       f"<p>કુલ = {tt * 1e6:g} + {tp * 1e6:g} = <b>{(tt + tp) * 1e6:g} µs</b></p>")

NUMERICALS = [n1, n2, n3, n4, n5]

EQUATIONS = [
    {"title": {"en": "Waves and delay", "gu": "Waves અને delay"}, "items": [
        E("Wavelength", "Wavelength", "λ = c / f", "c = 3 × 10⁸ m/s in free space; f in Hz", "Free space માં c = 3 × 10⁸ m/s; f Hz માં"),
        E("Propagation delay", "Propagation delay", "Tp = distance / propagation speed", "≈ 2 × 10⁸ m/s in copper and fiber (5 µs per km)", "Copper અને fiber માં ≈ 2 × 10⁸ m/s (km દીઠ 5 µs)"),
        E("Transmission time", "Transmission time", "Tt = message size (bits) / bandwidth (bps)", "Total latency = Tt + Tp + queuing + processing", "કુલ latency = Tt + Tp + queuing + processing"),
        E("GEO satellite delay", "GEO satellite delay", "Tp = 2 × 35,786 km / c ≈ 0.24 s", "Earth to satellite to earth, one way", "Earth થી satellite થી earth, એક તરફ"),
    ]},
    {"title": {"en": "Microwave and fiber", "gu": "Microwave અને fiber"}, "items": [
        E("Line-of-sight distance", "Line-of-sight અંતર", "d = 4.12 (√h1 + √h2) km", "h1, h2 = antenna heights in metres", "h1, h2 = antenna ની ઊંચાઈ metres માં"),
        E("Critical angle", "Critical angle", "sin θc = n2 / n1", "n1 = core, n2 = cladding; n1 > n2", "n1 = core, n2 = cladding; n1 > n2"),
        E("Numerical aperture", "Numerical aperture", "NA = √(n1² − n2²) = sin θa", "θa = acceptance angle", "θa = acceptance angle"),
    ]},
]

VIVA = [
    {"title": {"en": "Guided media", "gu": "Guided media"}, "items": [
        V("What is transmission media?", "Transmission media એટલે શું?", "The physical path between sender and receiver through which signals travel; it is below the physical layer.", "Sender અને receiver વચ્ચેનો physical માર્ગ જેમાંથી signals જાય; તે physical layer ની નીચે છે."),
        V("Why are wires twisted in twisted pair cable?", "Twisted pair cable માં વાયર શા માટે વળેલા હોય?", "Twisting cancels electromagnetic interference and crosstalk because noise affects both wires equally.", "વળ આપવાથી electromagnetic interference અને crosstalk રદ થાય કારણ કે noise બંને વાયરને સરખી અસર કરે."),
        V("Difference between UTP and STP?", "UTP અને STP વચ્ચે તફાવત?", "STP has a metal foil / braid shield around the pairs for better noise protection; UTP has no shield and is cheaper.", "STP માં વધુ noise રક્ષણ માટે pairs ફરતે metal foil / braid shield હોય; UTP માં shield નથી અને સસ્તું છે."),
        V("Which connector is used with UTP for LAN?", "LAN માટે UTP સાથે કયું connector વપરાય?", "RJ-45 (8 pins). RJ-11 is used for telephone lines.", "RJ-45 (8 pins). Telephone lines માટે RJ-11 વપરાય."),
        V("When is a cross-over cable used?", "Cross-over cable ક્યારે વપરાય?", "To connect similar devices directly (PC to PC, switch to switch). One end T568A, other end T568B.", "સરખા devices સીધા જોડવા (PC થી PC, switch થી switch). એક છેડો T568A, બીજો T568B."),
        V("Name the layers of a coaxial cable.", "Coaxial cable ના સ્તરોના નામ આપો.", "Central copper conductor, insulator (dielectric), outer metallic braid shield, plastic jacket.", "મધ્ય copper conductor, insulator (dielectric), બાહ્ય metallic braid shield, plastic jacket."),
        V("On which principle does optical fiber work?", "Optical fiber કયા સિદ્ધાંત પર કામ કરે?", "Total internal reflection: the core has a higher refractive index than the cladding.", "Total internal reflection: core નો refractive index cladding કરતાં વધુ હોય."),
        V("Single-mode vs multimode fiber?", "Single-mode vs multimode fiber?", "Single-mode has a very thin core (8-10 µm), one path, laser source, long distance. Multimode has a thicker core, many paths, LED source, shorter distance.", "Single-mode માં ખૂબ પાતળું core (8-10 µm), એક path, laser source, લાંબું અંતર. Multimode માં જાડું core, ઘણા paths, LED source, ટૂંકું અંતર."),
    ]},
    {"title": {"en": "Unguided media", "gu": "Unguided media"}, "items": [
        V("What are the three propagation methods?", "ત્રણ propagation methods કઈ?", "Ground (below 2 MHz), sky (2-30 MHz, reflected by ionosphere) and line-of-sight (above 30 MHz).", "Ground (2 MHz થી ઓછી), sky (2-30 MHz, ionosphere થી પરાવર્તિત) અને line-of-sight (30 MHz થી વધુ)."),
        V("Why are radio waves used for broadcasting?", "Broadcasting માટે radio waves શા માટે વપરાય?", "They are omnidirectional and penetrate walls, so one antenna reaches many receivers.", "તે omnidirectional છે અને દીવાલોમાંથી પસાર થાય, તેથી એક antenna ઘણા receivers સુધી પહોંચે."),
        V("Why are microwave towers tall and placed about 50 km apart?", "Microwave towers ઊંચા અને લગભગ 50 km ના અંતરે શા માટે?", "Microwaves travel in line of sight; the earth's curvature blocks them, so tall towers and repeaters are needed.", "Microwaves line of sight માં જાય; પૃથ્વીનો વળાંક અટકાવે, તેથી ઊંચા towers અને repeaters જોઈએ."),
        V("Why does a TV remote not work from another room?", "TV remote બીજા રૂમમાંથી કેમ કામ ન કરે?", "It uses infrared, which cannot pass through walls and needs line of sight.", "તે infrared વાપરે, જે દીવાલોમાંથી પસાર ન થાય અને line of sight જોઈએ."),
        V("What is a geostationary satellite?", "Geostationary satellite એટલે શું?", "A satellite at 35,786 km above the equator that rotates with the earth (24 h), so it appears fixed.", "વિષુવવૃત્ત ઉપર 35,786 km એ પૃથ્વી સાથે (24 h) ફરતો satellite, તેથી સ્થિર દેખાય."),
        V("What are uplink and downlink?", "Uplink અને downlink એટલે શું?", "Uplink: earth station to satellite. Downlink: satellite to earth. They use different frequencies (e.g. 6 / 4 GHz).", "Uplink: earth station થી satellite. Downlink: satellite થી earth. જુદી frequencies વાપરે (દા.ત. 6 / 4 GHz)."),
        V("What is a transponder?", "Transponder એટલે શું?", "The satellite unit that receives the uplink signal, amplifies it, shifts the frequency and retransmits it.", "Satellite નું એકમ જે uplink signal મેળવે, amplify કરે, frequency બદલે અને ફરી મોકલે."),
    ]},
    {"title": {"en": "Network devices", "gu": "Network devices"}, "items": [
        V("Difference between a repeater and an amplifier?", "Repeater અને amplifier વચ્ચે તફાવત?", "An amplifier boosts the signal along with noise; a repeater regenerates the original clean bit pattern.", "Amplifier signal સાથે noise પણ વધારે; repeater મૂળ સ્વચ્છ bit pattern ફરી બનાવે."),
        V("Active hub vs passive hub?", "Active hub vs passive hub?", "An active hub regenerates signals and needs power (multiport repeater); a passive hub only connects wires.", "Active hub signals regenerate કરે અને power જોઈએ (multiport repeater); passive hub ફક્ત વાયર જોડે."),
        V("Why is a switch better than a hub?", "Switch hub કરતાં શા માટે સારું?", "A switch sends frames only to the destination port using the MAC table, giving separate collision domains, full duplex and better security.", "Switch MAC table વાપરી frames ફક્ત destination port પર મોકલે, જેથી અલગ collision domains, full duplex અને વધુ security મળે."),
        V("Which address does a bridge use?", "Bridge કયું address વાપરે?", "The MAC (physical) address, stored in its bridge table.", "MAC (physical) address, તેના bridge table માં સંગ્રહિત."),
        V("Which address does a router use?", "Router કયું address વાપરે?", "The destination IP (logical) address, with a routing table.", "Routing table સાથે destination IP (logical) address."),
        V("What is a gateway?", "Gateway એટલે શું?", "A protocol converter that connects networks using different protocols; it can work at all layers.", "જુદા protocols વાપરતા networks જોડતું protocol converter; બધા layers પર કામ કરી શકે."),
        V("What is an SSID?", "SSID એટલે શું?", "The Service Set Identifier: the Wi-Fi network name broadcast by an access point.", "Service Set Identifier: access point દ્વારા broadcast થતું Wi-Fi network નામ."),
        V("How long is a MAC address?", "MAC address કેટલું લાંબું હોય?", "48 bits, written as 12 hexadecimal digits, e.g. 00:1A:2B:3C:4D:5E.", "48 bits, 12 hexadecimal અંકોમાં લખાય, દા.ત. 00:1A:2B:3C:4D:5E."),
        V("What is the advantage of a layer 3 switch?", "Layer 3 switch નો ફાયદો શું?", "It routes between VLANs inside the switch at hardware speed, without a separate router.", "તે અલગ router વગર switch ની અંદર hardware speed પર VLANs વચ્ચે route કરે."),
    ]},
]

EXAM_QS = [
    X("Classify transmission media with a diagram.", "આકૃતિ સાથે transmission media નું વર્ગીકરણ કરો.", 3),
    X("Explain twisted pair cable. Differentiate UTP and STP.", "Twisted pair cable સમજાવો. UTP અને STP નો તફાવત આપો.", 4),
    X("Write the colour code for straight-through and cross-over cables. State where each is used.", "Straight-through અને cross-over cables નો colour code લખો. દરેક ક્યાં વપરાય તે જણાવો.", 4),
    X("Explain coaxial cable with its construction, advantages and applications.", "Coaxial cable ની રચના, ફાયદા અને ઉપયોગો સાથે સમજાવો.", 4),
    X("Explain fiber optic cable with a neat diagram. Explain its propagation modes.", "સ્વચ્છ આકૃતિ સાથે fiber optic cable સમજાવો. તેના propagation modes સમજાવો.", 7),
    X("Compare twisted pair, coaxial and fiber optic cable.", "Twisted pair, coaxial અને fiber optic cable ની સરખામણી કરો.", 4),
    X("Explain the propagation methods of unguided media.", "Unguided media ની propagation methods સમજાવો.", 3),
    X("Explain microwave transmission with its advantages and disadvantages.", "Microwave transmission તેના ફાયદા અને ગેરફાયદા સાથે સમજાવો.", 4),
    X("Write a short note on satellite communication.", "Satellite communication પર ટૂંકનોંધ લખો.", 4),
    X("Compare radio waves, microwaves and infrared.", "Radio waves, microwaves અને infrared ની સરખામણી કરો.", 3),
    X("Differentiate hub and switch.", "Hub અને switch નો તફાવત આપો.", 3),
    X("Explain repeater, bridge and router.", "Repeater, bridge અને router સમજાવો.", 7),
    X("What is a gateway? Differentiate router and gateway.", "Gateway એટલે શું? Router અને gateway નો તફાવત આપો.", 3),
    X("Differentiate layer 2 switch and layer 3 switch.", "Layer 2 switch અને layer 3 switch નો તફાવત આપો.", 4),
    X("Explain network devices with respect to OSI layers.", "OSI layers ના સંદર્ભમાં network devices સમજાવો.", 4),
    X("Explain NIC and wireless access point.", "NIC અને wireless access point સમજાવો.", 3),
]
