"""Computer Networks (DI03000051) - Unit 3 notes part B: 3.2 Unguided media."""
from content_DI03000011_u1_notes_a import T
from content_DI03000041_u1_notes import tbl
from content_DI03000051_u1_notes_b import adv

PROP_EN = tbl(["Method", "Frequency", "How it travels", "Examples"], [
    ("Ground", "Below 2 MHz", "Low-frequency waves hug the earth's surface; distance depends on power", "AM radio, navigation, submarine communication"),
    ("Sky", "2-30 MHz", "Waves go up and are reflected back by the ionosphere; very long distance with low power", "Short-wave radio, amateur (ham) radio, international broadcast"),
    ("Line-of-sight", "Above 30 MHz", "Straight line from antenna to antenna; antennas must face each other, be tall or close", "FM, TV, microwave links, mobile, satellite")])
PROP_GU = tbl(["પદ્ધતિ", "Frequency", "કેવી રીતે જાય", "ઉદાહરણો"], [
    ("Ground", "2 MHz થી ઓછી", "ઓછી frequency ના તરંગો પૃથ્વીની સપાટીને અનુસરે; અંતર power પર આધારિત", "AM radio, navigation, submarine communication"),
    ("Sky", "2-30 MHz", "તરંગો ઉપર જઈ ionosphere થી પાછા પરાવર્તિત થાય; ઓછા power સાથે ખૂબ લાંબું અંતર", "Short-wave radio, amateur (ham) radio, international broadcast"),
    ("Line-of-sight", "30 MHz થી વધુ", "Antenna થી antenna સીધી રેખામાં; antennas સામસામે, ઊંચા કે નજીક હોવા જોઈએ", "FM, TV, microwave links, mobile, satellite")])

BANDS_EN = tbl(["Band", "Range", "Propagation", "Application"], [
    ("VLF / LF", "3-300 kHz", "Ground", "Navigation, AM long-wave"), ("MF", "300 kHz-3 MHz", "Sky", "AM radio"),
    ("HF", "3-30 MHz", "Sky", "Short-wave, ham radio, aircraft"), ("VHF", "30-300 MHz", "Sky / line-of-sight", "FM radio, VHF TV"),
    ("UHF", "300 MHz-3 GHz", "Line-of-sight", "UHF TV, mobile phones, Wi-Fi 2.4 GHz"), ("SHF", "3-30 GHz", "Line-of-sight", "Satellite, terrestrial microwave, Wi-Fi 5 GHz"),
    ("EHF", "30-300 GHz", "Line-of-sight", "Radar, 5G mmWave, satellite")])
BANDS_GU = tbl(["Band", "Range", "Propagation", "ઉપયોગ"], [
    ("VLF / LF", "3-300 kHz", "Ground", "Navigation, AM long-wave"), ("MF", "300 kHz-3 MHz", "Sky", "AM radio"),
    ("HF", "3-30 MHz", "Sky", "Short-wave, ham radio, aircraft"), ("VHF", "30-300 MHz", "Sky / line-of-sight", "FM radio, VHF TV"),
    ("UHF", "300 MHz-3 GHz", "Line-of-sight", "UHF TV, mobile phones, Wi-Fi 2.4 GHz"), ("SHF", "3-30 GHz", "Line-of-sight", "Satellite, terrestrial microwave, Wi-Fi 5 GHz"),
    ("EHF", "30-300 GHz", "Line-of-sight", "Radar, 5G mmWave, satellite")])

UCMP_EN = tbl(["Point", "Radio", "Microwave", "Infrared"], [
    ("Frequency", "3 kHz-1 GHz", "1-300 GHz", "300 GHz-400 THz"), ("Direction", "Omnidirectional", "Unidirectional", "Line of sight, short"),
    ("Walls", "Penetrates", "Blocked (high GHz)", "Cannot pass"), ("Distance", "Long", "~50 km per hop", "A few metres"),
    ("Antenna", "Simple (omni)", "Dish / horn", "LED + photodiode"), ("Example", "FM, AM, Wi-Fi", "Towers, satellite", "TV remote")])
UCMP_GU = tbl(["મુદ્દો", "Radio", "Microwave", "Infrared"], [
    ("Frequency", "3 kHz-1 GHz", "1-300 GHz", "300 GHz-400 THz"), ("દિશા", "Omnidirectional", "Unidirectional", "Line of sight, ટૂંકું"),
    ("દીવાલો", "પસાર થાય", "અટકે (વધુ GHz)", "પસાર ન થાય"), ("અંતર", "લાંબું", "Hop દીઠ ~50 km", "થોડા metres"),
    ("Antenna", "સરળ (omni)", "Dish / horn", "LED + photodiode"), ("ઉદાહરણ", "FM, AM, Wi-Fi", "Towers, satellite", "TV remote")])

ORBIT_EN = tbl(["Orbit", "Height", "Satellites needed", "Example"], [
    ("GEO (geostationary)", "35,786 km", "3 cover the earth", "DTH TV, VSAT, weather (INSAT, GSAT)"),
    ("MEO (medium earth)", "5,000-15,000 km", "24-30", "GPS, NavIC navigation"),
    ("LEO (low earth)", "500-2,000 km", "Hundreds / thousands", "Starlink, OneWeb Internet, Iridium phones")])
ORBIT_GU = tbl(["Orbit", "ઊંચાઈ", "જરૂરી satellites", "ઉદાહરણ"], [
    ("GEO (geostationary)", "35,786 km", "3 પૃથ્વીને આવરે", "DTH TV, VSAT, weather (INSAT, GSAT)"),
    ("MEO (medium earth)", "5,000-15,000 km", "24-30", "GPS, NavIC navigation"),
    ("LEO (low earth)", "500-2,000 km", "સેંકડો / હજારો", "Starlink, OneWeb Internet, Iridium phones")])

RADIO_AD = adv(["Omnidirectional: no need to align antennas; good for broadcasting.", "Penetrates walls; works indoors.", "Travels long distances; mobility for users."],
               ["Low bandwidth compared to microwave.", "Interference: all users of the same frequency interfere; needs government licence.", "Less secure: anyone in range can receive the signal."],
               ["Omnidirectional: antennas ગોઠવવાની જરૂર નહીં; broadcasting માટે સારું.", "દીવાલોમાંથી પસાર થાય; indoor કામ કરે.", "લાંબું અંતર કાપે; users માટે mobility."],
               ["Microwave ની સરખામણીમાં ઓછી bandwidth.", "Interference: સરખી frequency ના બધા users દખલ કરે; સરકારી licence જોઈએ.", "ઓછું secure: range માં કોઈ પણ signal મેળવી શકે."])
MW_AD = adv(["High bandwidth and data rate.", "No cables or right-of-way needed; cheaper than laying cable over long distances.", "Easy to install towers; quick setup over rivers, hills."],
            ["Line of sight required: towers must be tall and aligned; repeaters every ~50 km.", "Affected by rain, fog and storms (attenuation at high frequency).", "Cannot pass through walls or buildings; licence needed."],
            ["વધુ bandwidth અને data rate.", "Cables કે right-of-way ની જરૂર નહીં; લાંબા અંતરે cable નાખવા કરતાં સસ્તું.", "Towers install કરવા સહેલા; નદી, ટેકરીઓ પર ઝડપી setup."],
            ["Line of sight જરૂરી: towers ઊંચા અને ગોઠવાયેલા; દર ~50 km એ repeaters.", "વરસાદ, ધુમ્મસ અને તોફાનની અસર (વધુ frequency પર attenuation).", "દીવાલો કે buildings માંથી પસાર ન થાય; licence જોઈએ."])
IR_AD = adv(["Cannot pass walls, so no interference between rooms and better security.", "No licence needed; cheap LEDs and sensors.", "Low power; simple devices."],
            ["Very short range (a few metres) and line of sight needed.", "Cannot be used outdoors in sunlight (sun's infrared interferes).", "Low data rate; obstacles block the signal."],
            ["દીવાલોમાંથી પસાર ન થાય, તેથી રૂમો વચ્ચે interference નહીં અને વધુ security.", "Licence ની જરૂર નહીં; સસ્તા LEDs અને sensors.", "ઓછો power; સરળ devices."],
            ["ખૂબ ટૂંકી range (થોડા metres) અને line of sight જરૂરી.", "સૂર્યપ્રકાશમાં બહાર ન વાપરી શકાય (સૂર્યનો infrared દખલ કરે).", "ઓછો data rate; અવરોધો signal અટકાવે."])
SAT_AD = adv(["Covers a very large area (one GEO satellite covers about one-third of the earth).", "Reaches remote, hilly areas, ships and aircraft where cables are not possible.", "Broadcast: one signal to millions of receivers (DTH TV); cost does not depend on distance."],
             ["Very high launch and maintenance cost.", "Long propagation delay (about 0.24 s one way for GEO) is noticeable in voice calls.", "Affected by heavy rain; limited lifetime (10-15 years); security issues as anyone can receive."],
             ["ખૂબ મોટો વિસ્તાર આવરે (એક GEO satellite પૃથ્વીનો લગભગ ત્રીજો ભાગ આવરે).", "જ્યાં cables શક્ય નથી તેવા દૂરના, પહાડી વિસ્તારો, જહાજો અને વિમાનો સુધી પહોંચે.", "Broadcast: એક signal લાખો receivers ને (DTH TV); ખર્ચ અંતર પર આધારિત નથી."],
             ["ખૂબ વધુ launch અને maintenance ખર્ચ.", "લાંબો propagation delay (GEO માટે એક તરફ લગભગ 0.24 s) voice calls માં જણાય.", "ભારે વરસાદની અસર; મર્યાદિત આયુષ્ય (10-15 વર્ષ); કોઈ પણ મેળવી શકે તેથી security સમસ્યા."])

SEC_3_2 = {
    "title": {"en": "3.2 Unguided Media", "gu": "3.2 Unguided Media"},
    "items": [
        T("3.2.1 Unguided Media and Propagation Methods", "3.2.1 Unguided Media અને Propagation Methods",
          """<p><b>Unguided media</b> (wireless communication) transport electromagnetic waves without using a physical conductor. Signals are broadcast through free space and are available to anyone who has a device capable of receiving them. An <b>antenna</b> converts electrical signals to electromagnetic waves at the sender and back at the receiver.</p>
<p>Unguided signals can travel from the source to the destination in three ways:</p>
<ol>
<li><b>Ground propagation:</b> radio waves travel through the lowest part of the atmosphere, <b>hugging the earth</b>. These low-frequency signals emanate in all directions from the antenna and follow the curvature of the planet. Distance depends on the amount of power: more power, greater distance.</li>
<li><b>Sky propagation:</b> higher-frequency radio waves radiate upward into the <b>ionosphere</b> (the layer of the atmosphere where particles exist as ions), where they are <b>reflected back to earth</b>. This allows greater distances with lower output power.</li>
<li><b>Line-of-sight propagation:</b> very high-frequency signals are transmitted in <b>straight lines</b> directly from antenna to antenna. Antennas must be directional, facing each other, and either tall enough or close enough together not to be affected by the curvature of the earth.</li>
</ol>
""" + PROP_EN,
          """<p><b>Unguided media</b> (wireless communication) physical conductor વાપર્યા વગર electromagnetic waves લઈ જાય છે. Signals મુક્ત અવકાશમાં broadcast થાય અને તે મેળવી શકે તેવું device ધરાવતા કોઈ પણને ઉપલબ્ધ હોય છે. <b>Antenna</b> sender પર electrical signals ને electromagnetic waves માં અને receiver પર પાછા ફેરવે છે.</p>
<p>Unguided signals source થી destination સુધી ત્રણ રીતે જઈ શકે:</p>
<ol>
<li><b>Ground propagation:</b> radio waves વાતાવરણના સૌથી નીચેના ભાગમાં <b>પૃથ્વીને વળગીને</b> જાય છે. આ ઓછી frequency ના signals antenna થી બધી દિશામાં ફેલાય અને પૃથ્વીના વળાંકને અનુસરે. અંતર power પર આધારિત: વધુ power, વધુ અંતર.</li>
<li><b>Sky propagation:</b> વધુ frequency ના radio waves ઉપર <b>ionosphere</b> (વાતાવરણનું સ્તર જ્યાં કણો ions તરીકે હોય) માં જાય, જ્યાં તે <b>પૃથ્વી પર પાછા પરાવર્તિત</b> થાય. તેથી ઓછા output power સાથે વધુ અંતર મળે.</li>
<li><b>Line-of-sight propagation:</b> ખૂબ વધુ frequency ના signals antenna થી antenna સુધી <b>સીધી રેખામાં</b> મોકલાય. Antennas directional, સામસામે, અને પૃથ્વીના વળાંકની અસર ન થાય તેટલા ઊંચા કે નજીક હોવા જોઈએ.</li>
</ol>
""" + PROP_GU,
          diagram="cn3_prop"),
        T("3.2.2 Electromagnetic Spectrum", "3.2.2 Electromagnetic Spectrum",
          """<p>The <b>electromagnetic spectrum</b> is the complete range of electromagnetic waves arranged by frequency (or wavelength): radio waves, microwaves, infrared, visible light, ultraviolet, X-rays and gamma rays. Frequency and wavelength are related by <b>λ = c / f</b>, where c = 3 × 10⁸ m/s.</p>
<p>The part from <b>3 kHz to 900 THz</b> is used for wireless communication. It is divided into <b>bands</b>, regulated by authorities (ITU internationally, DoT / TRAI in India); most bands need a licence, while the <b>ISM bands</b> (2.4 GHz, 5 GHz) are free for Wi-Fi, Bluetooth and microwave ovens.</p>
""" + BANDS_EN + """
<p>Higher frequency means higher bandwidth (more data) but shorter range, more line-of-sight dependence and more attenuation by rain and walls. Ultraviolet, X-rays and gamma rays are not used for communication because they are harmful and difficult to generate and modulate.</p>""",
          """<p><b>Electromagnetic spectrum</b> એ frequency (કે wavelength) પ્રમાણે ગોઠવેલા electromagnetic waves ની સંપૂર્ણ range છે: radio waves, microwaves, infrared, visible light, ultraviolet, X-rays અને gamma rays. Frequency અને wavelength <b>λ = c / f</b> થી સંબંધિત છે, જ્યાં c = 3 × 10⁸ m/s.</p>
<p><b>3 kHz થી 900 THz</b> સુધીનો ભાગ wireless communication માટે વપરાય છે. તે <b>bands</b> માં વહેંચાયેલો છે, જે સત્તાવાળાઓ (આંતરરાષ્ટ્રીય ITU, ભારતમાં DoT / TRAI) નિયંત્રિત કરે; મોટા ભાગના bands ને licence જોઈએ, જ્યારે <b>ISM bands</b> (2.4 GHz, 5 GHz) Wi-Fi, Bluetooth અને microwave ovens માટે મફત છે.</p>
""" + BANDS_GU + """
<p>વધુ frequency એટલે વધુ bandwidth (વધુ data) પણ ઓછી range, line-of-sight પર વધુ આધાર અને વરસાદ અને દીવાલોથી વધુ attenuation. Ultraviolet, X-rays અને gamma rays હાનિકારક અને બનાવવા તથા modulate કરવા મુશ્કેલ હોવાથી communication માટે વપરાતા નથી.</p>""",
          diagram="cn3_spectrum", examples=["cn3n3"]),
        T("3.2.3 Radio Transmission", "3.2.3 Radio Transmission",
          """<p><b>Radio waves</b> are electromagnetic waves in the range <b>3 kHz to 1 GHz</b>. They are mostly <b>omnidirectional</b>: an antenna transmits in all directions, so the sending and receiving antennas do not have to be aligned. Radio waves, especially low and medium frequencies, can travel long distances (sky propagation) and <b>penetrate walls</b>.</p>
<ul><li><b>Antennas:</b> omnidirectional (simple wire / rod antennas).</li><li><b>Problem:</b> waves sent by one antenna can be received by any antenna, so signals using the same frequency interfere; the spectrum must be licensed.</li></ul>
<h4>Applications</h4>
<p>Multicasting / broadcasting where there is one sender and many receivers: <b>AM and FM radio</b>, television, cordless phones, paging, walkie-talkies, maritime radio. Wi-Fi and Bluetooth (2.4 GHz) also use radio waves.</p>
""" + RADIO_AD[0],
          """<p><b>Radio waves</b> એ <b>3 kHz થી 1 GHz</b> ની range ના electromagnetic waves છે. તે મોટે ભાગે <b>omnidirectional</b> છે: antenna બધી દિશામાં મોકલે, તેથી sending અને receiving antennas ગોઠવવાની જરૂર નથી. Radio waves, ખાસ કરીને ઓછી અને મધ્યમ frequency, લાંબું અંતર (sky propagation) કાપી શકે અને <b>દીવાલોમાંથી પસાર</b> થઈ શકે.</p>
<ul><li><b>Antennas:</b> omnidirectional (સરળ wire / rod antennas).</li><li><b>સમસ્યા:</b> એક antenna એ મોકલેલા તરંગો કોઈ પણ antenna મેળવી શકે, તેથી સરખી frequency વાપરતા signals દખલ કરે; spectrum licensed હોવું જોઈએ.</li></ul>
<h4>ઉપયોગો</h4>
<p>એક sender અને ઘણા receivers હોય ત્યાં multicasting / broadcasting: <b>AM અને FM radio</b>, television, cordless phones, paging, walkie-talkies, maritime radio. Wi-Fi અને Bluetooth (2.4 GHz) પણ radio waves વાપરે.</p>
""" + RADIO_AD[1]),
        T("3.2.4 Microwave Transmission", "3.2.4 Microwave Transmission",
          """<p><b>Microwaves</b> are electromagnetic waves with frequencies between <b>1 and 300 GHz</b>. They are <b>unidirectional</b>: the sending and receiving antennas must be <b>aligned (line of sight)</b>. Microwaves at very high frequencies cannot penetrate walls.</p>
<h4>Terrestrial microwave</h4>
<p>Uses <b>parabolic dish antennas</b> (or horn antennas) mounted on tall towers. Because of the earth's curvature, towers are placed about <b>40-50 km apart</b> with <b>repeaters</b> that receive, amplify and retransmit the signal. Higher towers give a longer distance: d ≈ 4.12 (√h1 + √h2) km, with antenna heights h in metres.</p>
<h4>Applications</h4>
<p>Unicast (one-to-one) communication: <b>mobile phone networks</b> (backhaul links between towers), long-distance telephone, TV studio-to-transmitter links, wireless LANs and point-to-point links between buildings, <b>satellite</b> communication, radar.</p>
""" + MW_AD[0],
          """<p><b>Microwaves</b> એ <b>1 થી 300 GHz</b> frequency વાળા electromagnetic waves છે. તે <b>unidirectional</b> છે: sending અને receiving antennas <b>ગોઠવાયેલા (line of sight)</b> હોવા જોઈએ. ખૂબ વધુ frequency ના microwaves દીવાલોમાંથી પસાર ન થઈ શકે.</p>
<h4>Terrestrial microwave</h4>
<p>ઊંચા towers પર લગાવેલા <b>parabolic dish antennas</b> (કે horn antennas) વાપરે. પૃથ્વીના વળાંકને કારણે towers લગભગ <b>40-50 km ના અંતરે</b> મુકાય, signal મેળવી, amplify કરી ફરી મોકલતા <b>repeaters</b> સાથે. વધુ ઊંચા towers વધુ અંતર આપે: d ≈ 4.12 (√h1 + √h2) km, antenna ની ઊંચાઈ h metres માં.</p>
<h4>ઉપયોગો</h4>
<p>Unicast (એક-થી-એક) communication: <b>mobile phone networks</b> (towers વચ્ચે backhaul links), લાંબા અંતરના telephone, TV studio-to-transmitter links, wireless LANs અને buildings વચ્ચે point-to-point links, <b>satellite</b> communication, radar.</p>
""" + MW_AD[1],
          diagram="cn3_microwave", examples=["cn3n2"]),
        T("3.2.5 Infrared Transmission", "3.2.5 Infrared Transmission",
          """<p><b>Infrared waves</b> have frequencies from <b>300 GHz to 400 THz</b> (wavelengths from 1 mm to 770 nm). They are used for <b>short-range</b> communication in a closed area using <b>line-of-sight</b> propagation. An infrared <b>LED</b> sends the signal and a <b>photodiode</b> receives it.</p>
<ul><li>Infrared waves <b>cannot penetrate walls</b>; this prevents interference between one system and another (a remote in one room does not affect a TV in the next room).</li><li>They cannot be used outside a building because the sun's rays contain infrared waves that interfere.</li><li>The <b>IrDA</b> (Infrared Data Association) standard defines data rates of 115 kbps to 4 Mbps.</li></ul>
<h4>Applications</h4>
<p>TV / AC <b>remote controls</b>, wireless keyboards and mice (older), IrDA data transfer between laptops / phones, infrared sensors, night-vision cameras, short-range indoor communication.</p>
""" + IR_AD[0] + """
<h4>Comparison of unguided media</h4>
""" + UCMP_EN,
          """<p><b>Infrared waves</b> ની frequency <b>300 GHz થી 400 THz</b> (wavelength 1 mm થી 770 nm) છે. તે <b>line-of-sight</b> propagation વાપરીને બંધ વિસ્તારમાં <b>ટૂંકા અંતરના</b> communication માટે વપરાય છે. Infrared <b>LED</b> signal મોકલે અને <b>photodiode</b> તે મેળવે.</p>
<ul><li>Infrared waves <b>દીવાલોમાંથી પસાર થઈ શકતા નથી</b>; તે એક system અને બીજી વચ્ચે interference અટકાવે (એક રૂમનું remote બાજુના રૂમના TV ને અસર ન કરે).</li><li>Building ની બહાર વાપરી શકાતા નથી કારણ કે સૂર્યના કિરણોમાં infrared waves હોય છે જે દખલ કરે.</li><li><b>IrDA</b> (Infrared Data Association) standard 115 kbps થી 4 Mbps ના data rates નક્કી કરે.</li></ul>
<h4>ઉપયોગો</h4>
<p>TV / AC <b>remote controls</b>, wireless keyboards અને mice (જૂના), laptops / phones વચ્ચે IrDA data transfer, infrared sensors, night-vision cameras, ટૂંકા અંતરનું indoor communication.</p>
""" + IR_AD[1] + """
<h4>Unguided media ની સરખામણી</h4>
""" + UCMP_GU),
        T("3.2.6 Satellite Transmission", "3.2.6 Satellite Transmission",
          """<p>A <b>communication satellite</b> is a microwave relay station placed in space. An earth station sends a signal to the satellite on the <b>uplink</b> frequency; the satellite's <b>transponder</b> receives it, amplifies it, changes the frequency, and broadcasts it back on the <b>downlink</b> frequency to earth stations over a large area (the <b>footprint</b>). Different up / down frequencies prevent interference (e.g. C band: 6 GHz up / 4 GHz down; Ku band: 14 / 12 GHz).</p>
<p>It works like line-of-sight microwave with a very tall "tower", overcoming the earth's curvature.</p>
<h4>Types of orbit</h4>
""" + ORBIT_EN + """
<p>A <b>geostationary</b> satellite revolves at the same speed as the earth's rotation (24 hours), so it appears fixed in the sky and ground antennas do not need to track it. Three GEO satellites 120° apart can cover the whole earth except the poles.</p>
<h4>Applications</h4>
<p>DTH television (Tata Play, DD Free Dish), VSAT networks for banks and ATMs, GPS / NavIC navigation, weather forecasting, Internet in remote areas (Starlink), ship and aircraft communication, disaster management.</p>
""" + SAT_AD[0],
          """<p><b>Communication satellite</b> એ અવકાશમાં મુકાયેલું microwave relay station છે. Earth station satellite ને <b>uplink</b> frequency પર signal મોકલે; satellite નું <b>transponder</b> તે મેળવી, amplify કરી, frequency બદલી, મોટા વિસ્તાર (<b>footprint</b>) ના earth stations ને <b>downlink</b> frequency પર પાછું broadcast કરે. જુદી up / down frequencies interference અટકાવે (દા.ત. C band: 6 GHz up / 4 GHz down; Ku band: 14 / 12 GHz).</p>
<p>તે ખૂબ ઊંચા "tower" વાળા line-of-sight microwave જેવું કામ કરે, પૃથ્વીના વળાંકની મર્યાદા દૂર કરે.</p>
<h4>Orbit ના પ્રકારો</h4>
""" + ORBIT_GU + """
<p><b>Geostationary</b> satellite પૃથ્વીના પરિભ્રમણ જેટલી જ ઝડપે (24 કલાક) ફરે, તેથી આકાશમાં સ્થિર દેખાય અને જમીન પરના antennas ને તેનો પીછો કરવો પડતો નથી. 120° ના અંતરે ત્રણ GEO satellites ધ્રુવો સિવાય આખી પૃથ્વી આવરી શકે.</p>
<h4>ઉપયોગો</h4>
<p>DTH television (Tata Play, DD Free Dish), banks અને ATMs માટે VSAT networks, GPS / NavIC navigation, હવામાન આગાહી, દૂરના વિસ્તારોમાં Internet (Starlink), જહાજ અને વિમાન communication, આપત્તિ વ્યવસ્થાપન.</p>
""" + SAT_AD[1],
          diagram="cn3_satellite", examples=["cn3n1"]),
    ]}
