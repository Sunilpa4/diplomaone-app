"""Digital Electronics Fundamentals (DI03000011) - Unit 1 notes, part A: 1.1 Digital systems, 1.2 Number systems."""


def T(h_en, h_gu, b_en, b_gu, diagram=None, examples=None, key=False):
    d = {"h": {"en": h_en, "gu": h_gu}, "body": {"en": b_en, "gu": b_gu}}
    if diagram:
        d["diagram"] = diagram
    if examples:
        d["examples"] = examples
    if key:
        d["key"] = True
    return d


def count_table():
    rows = ""
    for i in range(16):
        rows += f"<tr><td>{i}</td><td>{i:04b}</td><td>{i:o}</td><td>{i:X}</td></tr>"
    head = lambda a, b, c, d: f"<tr><th>{a}</th><th>{b}</th><th>{c}</th><th>{d}</th></tr>"
    return ("<table>" + head("Decimal", "Binary", "Octal", "Hex") + rows + "</table>",
            "<table>" + head("Decimal", "Binary", "Octal", "Hex") + rows + "</table>")


CT_EN, CT_GU = count_table()

SEC_1_1 = {
    "title": {"en": "1.1 Introduction to Digital Systems", "gu": "1.1 Digital Systems નો પરિચય"},
    "items": [
        T("1.1.1 Analog and Digital Signals", "1.1.1 Analog અને Digital Signals",
          """<p>A <b>signal</b> is a physical quantity (usually voltage) that carries information. Signals are of two types:</p>
<h4>Analog signal</h4>
<p>An <b>analog signal</b> is a <b>continuous</b> signal. It can have <b>any (infinite) value</b> within a range, and it changes smoothly with time.</p>
<p><i>Examples:</i> output of a microphone, temperature, sound, a sine wave from a signal generator, a needle-type (analog) meter.</p>
<h4>Digital signal</h4>
<p>A <b>digital signal</b> is a <b>discrete</b> signal. It has only <b>two levels</b>: HIGH (logic <b>1</b>, e.g. +5 V) and LOW (logic <b>0</b>, e.g. 0 V). It changes in steps, not smoothly.</p>
<p><i>Examples:</i> data inside a computer, output of a digital clock, signals on a USB cable.</p>
<h4>Comparison</h4>
<table><tr><th>Point</th><th>Analog</th><th>Digital</th></tr>
<tr><td>Nature</td><td>Continuous</td><td>Discrete (0 and 1)</td></tr>
<tr><td>Values</td><td>Infinite</td><td>Only two</td></tr>
<tr><td>Effect of noise</td><td>High</td><td>Low</td></tr>
<tr><td>Accuracy</td><td>Lower</td><td>High</td></tr>
<tr><td>Storage</td><td>Difficult</td><td>Easy (memory)</td></tr>
<tr><td>Circuit</td><td>Amplifier, filter</td><td>Logic gates, flip-flops</td></tr>
<tr><td>Example</td><td>Analog watch, thermometer</td><td>Digital watch, computer</td></tr></table>""",
          """<p><b>Signal</b> એ એવી physical quantity (સામાન્ય રીતે voltage) છે જે માહિતી લઈ જાય છે. Signals બે પ્રકારના હોય છે:</p>
<h4>Analog signal</h4>
<p><b>Analog signal</b> એ <b>સતત (continuous)</b> signal છે. તે range ની અંદર <b>કોઈ પણ (અનંત) કિંમત</b> લઈ શકે છે અને સમય સાથે ધીમે ધીમે (smoothly) બદલાય છે.</p>
<p><i>ઉદાહરણ:</i> microphone નું output, તાપમાન, અવાજ, signal generator માંથી મળતી sine wave, સોયવાળું (analog) meter.</p>
<h4>Digital signal</h4>
<p><b>Digital signal</b> એ <b>discrete (અલગ-અલગ)</b> signal છે. તેમાં માત્ર <b>બે levels</b> હોય છે: HIGH (logic <b>1</b>, દા.ત. +5 V) અને LOW (logic <b>0</b>, દા.ત. 0 V). તે smoothly નહીં પણ steps માં બદલાય છે.</p>
<p><i>ઉદાહરણ:</i> computer ની અંદરનો data, digital clock નું output, USB cable પરના signals.</p>
<h4>સરખામણી</h4>
<table><tr><th>મુદ્દો</th><th>Analog</th><th>Digital</th></tr>
<tr><td>પ્રકૃતિ</td><td>Continuous</td><td>Discrete (0 અને 1)</td></tr>
<tr><td>કિંમતો</td><td>અનંત</td><td>માત્ર બે</td></tr>
<tr><td>Noise ની અસર</td><td>વધુ</td><td>ઓછી</td></tr>
<tr><td>ચોકસાઈ</td><td>ઓછી</td><td>વધુ</td></tr>
<tr><td>Storage</td><td>અઘરું</td><td>સરળ (memory)</td></tr>
<tr><td>Circuit</td><td>Amplifier, filter</td><td>Logic gates, flip-flops</td></tr>
<tr><td>ઉદાહરણ</td><td>Analog ઘડિયાળ, thermometer</td><td>Digital ઘડિયાળ, computer</td></tr></table>""",
          diagram="de1_analog_digital", key=True),

        T("1.1.2 Digital System and its Applications", "1.1.2 Digital System અને તેના ઉપયોગો",
          """<p>A <b>digital system</b> is a combination of electronic circuits that <b>accepts, processes, stores and outputs information in binary form</b> (0 and 1).</p>
<h4>Parts of a digital system</h4>
<ol>
<li><b>Input unit:</b> gives data to the system, e.g. keyboard, switches, sensors. An analog input is first converted to digital by an <b>ADC</b> (Analog-to-Digital Converter).</li>
<li><b>Processing unit:</b> performs logical and arithmetic operations using <b>logic gates, flip-flops, counters, registers, processor and memory</b>.</li>
<li><b>Output unit:</b> gives the result, e.g. display, LEDs, printer. A <b>DAC</b> (Digital-to-Analog Converter) is used when an analog output (such as sound) is needed.</li>
</ol>
<h4>Applications</h4>
<ul>
<li>Computers, laptops, servers and calculators</li>
<li>Mobile phones, digital cameras, smart TVs</li>
<li>Digital watches, digital multimeters, weighing machines</li>
<li>ATMs, traffic-light controllers, washing machines (microcontrollers)</li>
<li>Digital communication: internet, satellite, digital TV, Wi-Fi</li>
</ul>""",
          """<p><b>Digital system</b> એ electronic circuits નું એવું જૂથ છે જે માહિતીને <b>binary સ્વરૂપમાં (0 અને 1) લે છે, process કરે છે, store કરે છે અને output આપે છે</b>.</p>
<h4>Digital system ના ભાગો</h4>
<ol>
<li><b>Input unit:</b> system ને data આપે છે, દા.ત. keyboard, switches, sensors. Analog input ને પહેલાં <b>ADC</b> (Analog-to-Digital Converter) દ્વારા digital માં ફેરવવામાં આવે છે.</li>
<li><b>Processing unit:</b> <b>logic gates, flip-flops, counters, registers, processor અને memory</b> ની મદદથી logical અને arithmetic operations કરે છે.</li>
<li><b>Output unit:</b> પરિણામ આપે છે, દા.ત. display, LEDs, printer. Analog output (જેમ કે અવાજ) જોઈએ ત્યારે <b>DAC</b> (Digital-to-Analog Converter) વપરાય છે.</li>
</ol>
<h4>ઉપયોગો (Applications)</h4>
<ul>
<li>Computers, laptops, servers અને calculators</li>
<li>Mobile phones, digital cameras, smart TVs</li>
<li>Digital ઘડિયાળ, digital multimeter, વજન કાંટા</li>
<li>ATM, traffic-light controller, washing machine (microcontrollers)</li>
<li>Digital communication: internet, satellite, digital TV, Wi-Fi</li>
</ul>""",
          diagram="de1_digital_system"),

        T("1.1.3 Advantages and Disadvantages of Digital Systems", "1.1.3 Digital Systems ના ફાયદા અને ગેરફાયદા",
          """<h4>Advantages</h4>
<ol>
<li><b>Less affected by noise:</b> only two levels have to be recognised, so small noise does not change the data.</li>
<li><b>High accuracy and precision:</b> accuracy can be increased simply by using more bits.</li>
<li><b>Easy storage:</b> data can be stored for a long time in memory (RAM, ROM, flash, hard disk).</li>
<li><b>Programmable:</b> the operation can be changed by changing the program (software), without changing hardware.</li>
<li><b>Easy design:</b> only switching circuits (ON/OFF) are needed; exact voltage values are not important.</li>
<li><b>Integration:</b> millions of gates can be put on one IC chip, so systems are small, cheap and reliable.</li>
<li><b>Error detection and correction</b> is possible using codes (parity, Hamming code).</li>
</ol>
<h4>Disadvantages</h4>
<ol>
<li>The real world is <b>analog</b>; so ADC and DAC are needed, which increases cost and delay.</li>
<li>Converting analog to digital causes <b>quantisation error</b> (some information is lost).</li>
<li>Digital circuits use more power at high speed, and need more bandwidth for transmission.</li>
</ol>""",
          """<h4>ફાયદા (Advantages)</h4>
<ol>
<li><b>Noise ની ઓછી અસર:</b> માત્ર બે levels ઓળખવાના હોય છે, તેથી નાનો noise data બદલી શકતો નથી.</li>
<li><b>વધુ ચોકસાઈ (accuracy):</b> વધુ bits વાપરીને સહેલાઈથી ચોકસાઈ વધારી શકાય છે.</li>
<li><b>સરળ storage:</b> data ને memory (RAM, ROM, flash, hard disk) માં લાંબા સમય સુધી store કરી શકાય છે.</li>
<li><b>Programmable:</b> hardware બદલ્યા વગર માત્ર program (software) બદલીને કાર્ય બદલી શકાય છે.</li>
<li><b>સરળ design:</b> માત્ર switching circuits (ON/OFF) જોઈએ; ચોક્કસ voltage કિંમત મહત્વની નથી.</li>
<li><b>Integration:</b> એક IC chip પર લાખો gates મૂકી શકાય છે, તેથી systems નાના, સસ્તા અને વિશ્વસનીય બને છે.</li>
<li>Codes (parity, Hamming code) વડે <b>error detection અને correction</b> શક્ય છે.</li>
</ol>
<h4>ગેરફાયદા (Disadvantages)</h4>
<ol>
<li>વાસ્તવિક દુનિયા <b>analog</b> છે; તેથી ADC અને DAC જોઈએ, જેનાથી cost અને delay વધે છે.</li>
<li>Analog ને digital માં ફેરવતાં <b>quantisation error</b> આવે છે (થોડી માહિતી ગુમાય છે).</li>
<li>વધુ speed પર digital circuits વધુ power વાપરે છે અને transmission માટે વધુ bandwidth જોઈએ છે.</li>
</ol>""",
          key=True),

        T("1.1.4 Bit, Nibble, Byte and Word", "1.1.4 Bit, Nibble, Byte અને Word",
          """<ul>
<li><b>Bit</b> (<b>Bi</b>nary digi<b>t</b>): a single 0 or 1. It is the smallest unit of information.</li>
<li><b>Nibble:</b> a group of <b>4 bits</b>, e.g. 1011. One hexadecimal digit = one nibble.</li>
<li><b>Byte:</b> a group of <b>8 bits</b>, e.g. 1011 0110. One character (ASCII) is stored in one byte.</li>
<li><b>Word:</b> the number of bits a processor handles at one time, e.g. 16, 32 or 64 bits.</li>
</ul>
<p><b>MSB</b> (Most Significant Bit) is the left-most bit with the highest weight; <b>LSB</b> (Least Significant Bit) is the right-most bit with the lowest weight.</p>
<p>With <b>n bits</b>, 2<sup>n</sup> different combinations are possible (0 to 2<sup>n</sup> − 1). For example, 4 bits give 16 combinations (0 to 15) and 8 bits give 256 (0 to 255).</p>
<p><i>Memory units:</i> 1 KB = 1024 bytes, 1 MB = 1024 KB, 1 GB = 1024 MB, 1 TB = 1024 GB.</p>""",
          """<ul>
<li><b>Bit</b> (<b>Bi</b>nary digi<b>t</b>): એક 0 અથવા 1. તે માહિતીનો સૌથી નાનો એકમ છે.</li>
<li><b>Nibble:</b> <b>4 bits</b> નું જૂથ, દા.ત. 1011. એક hexadecimal digit = એક nibble.</li>
<li><b>Byte:</b> <b>8 bits</b> નું જૂથ, દા.ત. 1011 0110. એક character (ASCII) એક byte માં store થાય છે.</li>
<li><b>Word:</b> processor એક સાથે જેટલા bits પર કામ કરે તે, દા.ત. 16, 32 અથવા 64 bits.</li>
</ul>
<p><b>MSB</b> (Most Significant Bit) એ સૌથી ડાબી બાજુનો અને સૌથી વધુ weight વાળો bit છે; <b>LSB</b> (Least Significant Bit) એ સૌથી જમણી બાજુનો અને સૌથી ઓછા weight વાળો bit છે.</p>
<p><b>n bits</b> વડે 2<sup>n</sup> જુદા જુદા combinations શક્ય છે (0 થી 2<sup>n</sup> − 1). દા.ત. 4 bits થી 16 combinations (0 થી 15) અને 8 bits થી 256 (0 થી 255) મળે.</p>
<p><i>Memory units:</i> 1 KB = 1024 bytes, 1 MB = 1024 KB, 1 GB = 1024 MB, 1 TB = 1024 GB.</p>"""),
    ],
}

SEC_1_2 = {
    "title": {"en": "1.2 Number Systems", "gu": "1.2 Number Systems"},
    "items": [
        T("1.2.1 Number System, Base and Positional Weight", "1.2.1 Number System, Base અને Positional Weight",
          """<p>A <b>number system</b> is a method of representing numbers using a set of symbols (digits).</p>
<ul>
<li><b>Base or radix (r):</b> the number of different digits used in the system. Digits go from 0 to (r − 1).</li>
<li><b>Positional (weighted) system:</b> the value of a digit depends on its <b>position</b>. Each position has a <b>weight</b> = r<sup>position</sup>.</li>
</ul>
<p>For a number with integer digits d<sub>n−1</sub> … d<sub>1</sub> d<sub>0</sub> and fraction digits d<sub>−1</sub> d<sub>−2</sub> …:</p>
<p style="text-align:center"><b>Value = d<sub>n−1</sub>×r<sup>n−1</sup> + … + d<sub>1</sub>×r<sup>1</sup> + d<sub>0</sub>×r<sup>0</sup> + d<sub>−1</sub>×r<sup>−1</sup> + d<sub>−2</sub>×r<sup>−2</sup> + …</b></p>
<p>Positions to the left of the point are 0, 1, 2 …; positions to the right are −1, −2, −3 …</p>
<p>The base is written as a subscript to avoid confusion: (101)<sub>2</sub>, (101)<sub>8</sub>, (101)<sub>10</sub> and (101)<sub>16</sub> are four different values (5, 65, 101 and 257).</p>
<h4>Four number systems used in digital electronics</h4>
<table><tr><th>System</th><th>Base</th><th>Digits</th></tr>
<tr><td>Binary</td><td>2</td><td>0, 1</td></tr>
<tr><td>Octal</td><td>8</td><td>0 to 7</td></tr>
<tr><td>Decimal</td><td>10</td><td>0 to 9</td></tr>
<tr><td>Hexadecimal</td><td>16</td><td>0 to 9, A to F</td></tr></table>""",
          """<p><b>Number system</b> એ symbols (digits) ના સમૂહ વડે સંખ્યાઓ દર્શાવવાની પદ્ધતિ છે.</p>
<ul>
<li><b>Base અથવા radix (r):</b> system માં વપરાતા જુદા જુદા digits ની સંખ્યા. Digits 0 થી (r − 1) સુધી હોય છે.</li>
<li><b>Positional (weighted) system:</b> digit ની કિંમત તેના <b>સ્થાન (position)</b> પર આધાર રાખે છે. દરેક position નું <b>weight</b> = r<sup>position</sup>.</li>
</ul>
<p>Integer digits d<sub>n−1</sub> … d<sub>1</sub> d<sub>0</sub> અને fraction digits d<sub>−1</sub> d<sub>−2</sub> … વાળી સંખ્યા માટે:</p>
<p style="text-align:center"><b>કિંમત = d<sub>n−1</sub>×r<sup>n−1</sup> + … + d<sub>1</sub>×r<sup>1</sup> + d<sub>0</sub>×r<sup>0</sup> + d<sub>−1</sub>×r<sup>−1</sup> + d<sub>−2</sub>×r<sup>−2</sup> + …</b></p>
<p>Point ની ડાબી બાજુના positions 0, 1, 2 … અને જમણી બાજુના positions −1, −2, −3 … છે.</p>
<p>ગૂંચવણ ટાળવા base ને subscript માં લખાય છે: (101)<sub>2</sub>, (101)<sub>8</sub>, (101)<sub>10</sub> અને (101)<sub>16</sub> ચાર અલગ કિંમતો છે (5, 65, 101 અને 257).</p>
<h4>Digital electronics માં વપરાતી ચાર number systems</h4>
<table><tr><th>System</th><th>Base</th><th>Digits</th></tr>
<tr><td>Binary</td><td>2</td><td>0, 1</td></tr>
<tr><td>Octal</td><td>8</td><td>0 થી 7</td></tr>
<tr><td>Decimal</td><td>10</td><td>0 થી 9</td></tr>
<tr><td>Hexadecimal</td><td>16</td><td>0 થી 9, A થી F</td></tr></table>""",
          diagram="de1_number_systems", key=True),

        T("1.2.2 Decimal Number System", "1.2.2 Decimal Number System",
          """<p>The <b>decimal</b> system has base <b>10</b> and uses ten digits <b>0, 1, 2, … 9</b>. It is the system we use in daily life.</p>
<p>Weights of positions: … 10<sup>3</sup>=1000, 10<sup>2</sup>=100, 10<sup>1</sup>=10, 10<sup>0</sup>=1 . 10<sup>−1</sup>=0.1, 10<sup>−2</sup>=0.01 …</p>
<p><b>Example:</b> (526.34)<sub>10</sub> = 5×10<sup>2</sup> + 2×10<sup>1</sup> + 6×10<sup>0</sup> + 3×10<sup>−1</sup> + 4×10<sup>−2</sup> = 500 + 20 + 6 + 0.3 + 0.04</p>
<p>Digital circuits cannot easily work with ten voltage levels, so the decimal system is <b>not used directly inside</b> digital systems. Decimal numbers are converted to binary (or coded in BCD).</p>""",
          """<p><b>Decimal</b> system નો base <b>10</b> છે અને તેમાં દસ digits <b>0, 1, 2, … 9</b> વપરાય છે. આ system આપણે રોજિંદા જીવનમાં વાપરીએ છીએ.</p>
<p>Positions ના weights: … 10<sup>3</sup>=1000, 10<sup>2</sup>=100, 10<sup>1</sup>=10, 10<sup>0</sup>=1 . 10<sup>−1</sup>=0.1, 10<sup>−2</sup>=0.01 …</p>
<p><b>ઉદાહરણ:</b> (526.34)<sub>10</sub> = 5×10<sup>2</sup> + 2×10<sup>1</sup> + 6×10<sup>0</sup> + 3×10<sup>−1</sup> + 4×10<sup>−2</sup> = 500 + 20 + 6 + 0.3 + 0.04</p>
<p>Digital circuits માટે દસ voltage levels સાથે કામ કરવું અઘરું છે, તેથી decimal system digital systems ની <b>અંદર સીધી વપરાતી નથી</b>. Decimal સંખ્યાઓને binary માં ફેરવાય છે (અથવા BCD માં code કરાય છે).</p>"""),

        T("1.2.3 Binary Number System", "1.2.3 Binary Number System",
          """<p>The <b>binary</b> system has base <b>2</b> and uses only two digits, <b>0 and 1</b>. Each binary digit is called a <b>bit</b>.</p>
<p>Weights of positions: … 2<sup>4</sup>=16, 2<sup>3</sup>=8, 2<sup>2</sup>=4, 2<sup>1</sup>=2, 2<sup>0</sup>=1 . 2<sup>−1</sup>=0.5, 2<sup>−2</sup>=0.25, 2<sup>−3</sup>=0.125 …</p>
<p><b>Example:</b> (1101.101)<sub>2</sub> = 8 + 4 + 0 + 1 + 0.5 + 0 + 0.125 = <b>(13.625)<sub>10</sub></b></p>
<h4>Why binary is used in digital systems</h4>
<ul>
<li>Electronic devices have two natural states: switch ON/OFF, transistor saturation/cut-off, LED ON/OFF, high/low voltage.</li>
<li>Circuits for two states are <b>simple, cheap and reliable</b>, and less affected by noise.</li>
<li>Binary arithmetic and logic (Boolean algebra) are very simple.</li>
</ul>
<p><b>Disadvantage:</b> binary numbers are long (e.g. 255 = 11111111), so they are hard for humans to read. Octal and hexadecimal are used as short forms.</p>""",
          """<p><b>Binary</b> system નો base <b>2</b> છે અને તેમાં માત્ર બે digits <b>0 અને 1</b> વપરાય છે. દરેક binary digit ને <b>bit</b> કહે છે.</p>
<p>Positions ના weights: … 2<sup>4</sup>=16, 2<sup>3</sup>=8, 2<sup>2</sup>=4, 2<sup>1</sup>=2, 2<sup>0</sup>=1 . 2<sup>−1</sup>=0.5, 2<sup>−2</sup>=0.25, 2<sup>−3</sup>=0.125 …</p>
<p><b>ઉદાહરણ:</b> (1101.101)<sub>2</sub> = 8 + 4 + 0 + 1 + 0.5 + 0 + 0.125 = <b>(13.625)<sub>10</sub></b></p>
<h4>Digital systems માં binary કેમ વપરાય છે</h4>
<ul>
<li>Electronic devices ની બે કુદરતી અવસ્થાઓ હોય છે: switch ON/OFF, transistor saturation/cut-off, LED ON/OFF, high/low voltage.</li>
<li>બે અવસ્થા માટેના circuits <b>સરળ, સસ્તા અને વિશ્વસનીય</b> હોય છે અને noise ની અસર ઓછી થાય છે.</li>
<li>Binary arithmetic અને logic (Boolean algebra) ખૂબ સરળ છે.</li>
</ul>
<p><b>ગેરફાયદો:</b> binary સંખ્યાઓ લાંબી હોય છે (દા.ત. 255 = 11111111), તેથી માણસ માટે વાંચવી અઘરી છે. ટૂંકા સ્વરૂપ તરીકે octal અને hexadecimal વપરાય છે.</p>""",
          diagram="de1_positional", key=True),

        T("1.2.4 Octal and Hexadecimal Number Systems", "1.2.4 Octal અને Hexadecimal Number Systems",
          """<h4>Octal number system</h4>
<p>Base <b>8</b>, digits <b>0 to 7</b>. Weights: 8<sup>0</sup>=1, 8<sup>1</sup>=8, 8<sup>2</sup>=64, 8<sup>3</sup>=512 …</p>
<p>Since 8 = 2<sup>3</sup>, <b>one octal digit = 3 bits</b>. Digits 8 and 9 do not exist in octal.</p>
<h4>Hexadecimal number system</h4>
<p>Base <b>16</b>, sixteen digits <b>0–9 and A–F</b>, where A=10, B=11, C=12, D=13, E=14, F=15. Weights: 16<sup>0</sup>=1, 16<sup>1</sup>=16, 16<sup>2</sup>=256, 16<sup>3</sup>=4096 …</p>
<p>Since 16 = 2<sup>4</sup>, <b>one hex digit = 4 bits (one nibble)</b>; one byte = two hex digits (e.g. 1011 0110 = B6).</p>
<h4>Uses</h4>
<ul>
<li>Short and readable form of long binary numbers.</li>
<li>Hex is used for <b>memory addresses</b>, machine code, colour codes in HTML (#7B2CD9), MAC addresses.</li>
<li>Octal is used for file permissions in Linux (chmod 755) and in older computers.</li>
</ul>
<h4>Counting table (0 to 15) – learn this</h4>""" + CT_EN,
          """<h4>Octal number system</h4>
<p>Base <b>8</b>, digits <b>0 થી 7</b>. Weights: 8<sup>0</sup>=1, 8<sup>1</sup>=8, 8<sup>2</sup>=64, 8<sup>3</sup>=512 …</p>
<p>8 = 2<sup>3</sup> હોવાથી <b>એક octal digit = 3 bits</b>. Octal માં 8 અને 9 digits હોતા નથી.</p>
<h4>Hexadecimal number system</h4>
<p>Base <b>16</b>, સોળ digits <b>0–9 અને A–F</b>, જ્યાં A=10, B=11, C=12, D=13, E=14, F=15. Weights: 16<sup>0</sup>=1, 16<sup>1</sup>=16, 16<sup>2</sup>=256, 16<sup>3</sup>=4096 …</p>
<p>16 = 2<sup>4</sup> હોવાથી <b>એક hex digit = 4 bits (એક nibble)</b>; એક byte = બે hex digits (દા.ત. 1011 0110 = B6).</p>
<h4>ઉપયોગો</h4>
<ul>
<li>લાંબી binary સંખ્યાઓનું ટૂંકું અને વાંચી શકાય તેવું સ્વરૂપ.</li>
<li>Hex નો ઉપયોગ <b>memory addresses</b>, machine code, HTML ના colour codes (#7B2CD9), MAC addresses માં થાય છે.</li>
<li>Octal નો ઉપયોગ Linux ની file permissions (chmod 755) અને જૂના computers માં થાય છે.</li>
</ul>
<h4>ગણતરી કોષ્ટક (0 થી 15) – યાદ રાખો</h4>""" + CT_GU),
    ],
}

NOTES_A = [SEC_1_1, SEC_1_2]
