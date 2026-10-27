"""Digital Electronics Fundamentals (DI03000011) - Unit 4 notes, part B: 4.3 Data transmission circuits."""
from content_DI03000011_u1_notes_a import T
from de_gates import tt_html, bh as B
from diagrams_DI03000011_u4 import ENC_ROWS

TT_ENC = tt_html(["D3", "D2", "D1", "D0", "Y1", "Y0"], ENC_ROWS, 2)
TT_DEC = tt_html(["A", "B", "Y0", "Y1", "Y2", "Y3"], [(a, b, *[int(2 * a + b == k) for k in range(4)]) for a in (0, 1) for b in (0, 1)], 4)
TT_MUX = tt_html(["S1", "S0", "Y"], [(0, 0, "I0"), (0, 1, "I1"), (1, 0, "I2"), (1, 1, "I3")], 1)
TT_DMX = tt_html(["S1", "S0", "Y0", "Y1", "Y2", "Y3"], [(s1, s0, *["D" if 2 * s1 + s0 == k else 0 for k in range(4)]) for s1 in (0, 1) for s0 in (0, 1)], 4)
S1, S0 = B("!(S1)"), B("!(S0)")
YMUX = f"Y = {S1}{S0}I0 + {S1}S0I1 + S1{S0}I2 + S1S0I3"

SEC_4_3 = {
    "title": {"en": "4.3 Data Transmission Circuits", "gu": "4.3 Data Transmission Circuits"},
    "items": [
        T("4.3.1 Encoder (4-to-2 Encoder)", "4.3.1 Encoder (4-to-2 Encoder)",
          f"""<p>An <b>encoder</b> is a combinational circuit that converts an active input signal into a <b>coded (binary) output</b>. It has <b>2<sup>n</sup> inputs</b> and <b>n outputs</b>; only <b>one input is active (1) at a time</b>, and the output is the binary code of that input.</p>
<h4>4-to-2 encoder</h4>
<p>Inputs: D0, D1, D2, D3 &nbsp; Outputs: Y1 (MSB), Y0 (LSB)</p>{TT_ENC}
<p>Y1 is 1 for D2 or D3; Y0 is 1 for D1 or D3:</p>
<p><b>Y1 = D2 + D3</b> &nbsp;&nbsp; <b>Y0 = D1 + D3</b></p>
<p><b>Logic diagram:</b> two 2-input OR gates. D0 is not connected (when only D0 is high, both outputs are 0).</p>
<h4>Limitations and priority encoder</h4>
<ul><li>If two inputs are high together (e.g. D1 and D2), the output is 11, which is wrong.</li>
<li>Output 00 is the same for "D0 active" and "no input active".</li>
<li>A <b>priority encoder</b> solves this: it gives the code of the highest-priority active input and has a valid output (V) signal.</li></ul>
<p><b>Applications:</b> keyboard encoding (decimal-to-BCD encoder IC 74147), interrupt requests.</p>""",
          f"""<p><b>Encoder</b> એવો combinational circuit છે જે active input signal ને <b>coded (binary) output</b> માં ફેરવે છે. તેમાં <b>2<sup>n</sup> inputs</b> અને <b>n outputs</b> હોય છે; <b>એક સમયે એક જ input active (1)</b> હોય છે અને output તે input નો binary code હોય છે.</p>
<h4>4-to-2 encoder</h4>
<p>Inputs: D0, D1, D2, D3 &nbsp; Outputs: Y1 (MSB), Y0 (LSB)</p>{TT_ENC}
<p>D2 કે D3 માટે Y1 = 1; D1 કે D3 માટે Y0 = 1:</p>
<p><b>Y1 = D2 + D3</b> &nbsp;&nbsp; <b>Y0 = D1 + D3</b></p>
<p><b>Logic diagram:</b> બે 2-input OR gates. D0 જોડાયેલ નથી (માત્ર D0 high હોય ત્યારે બંને outputs 0).</p>
<h4>મર્યાદાઓ અને priority encoder</h4>
<ul><li>બે inputs એકસાથે high હોય (દા.ત. D1 અને D2), તો output 11 આવે, જે ખોટો છે.</li>
<li>"D0 active" અને "કોઈ input active નથી" બંને માટે output 00 સરખો છે.</li>
<li><b>Priority encoder</b> આ ઉકેલે છે: તે સૌથી વધુ priority વાળા active input નો code આપે છે અને valid output (V) signal ધરાવે છે.</li></ul>
<p><b>ઉપયોગો:</b> keyboard encoding (decimal-to-BCD encoder IC 74147), interrupt requests.</p>""",
          diagram="de4_enc", examples=["de4n9"], key=True),

        T("4.3.2 Decoder (2-to-4 Decoder)", "4.3.2 Decoder (2-to-4 Decoder)",
          f"""<p>A <b>decoder</b> converts an <b>n-bit binary input</b> into <b>2<sup>n</sup> outputs</b>, of which <b>exactly one is active</b> for each input combination. It does the opposite of an encoder.</p>
<h4>2-to-4 decoder</h4>
<p>Inputs: A (MSB), B &nbsp; Outputs: Y0, Y1, Y2, Y3</p>{TT_DEC}
<p><b>Y0 = {B('!A!B')}</b>, &nbsp; <b>Y1 = {B('!AB')}</b>, &nbsp; <b>Y2 = {B('A!B')}</b>, &nbsp; <b>Y3 = AB</b></p>
<p>Each output is one <b>minterm</b> of the inputs, so a decoder is also called a <b>minterm generator</b>.</p>
<p><b>Logic diagram:</b> 2 NOT gates and 4 two-input AND gates.</p>
<p><b>Enable input (E):</b> practical decoders have an enable input; when E = 0 all outputs are 0, and when E = 1 the decoder works normally (every AND gate gets E as an extra input). IC 74139 is a dual 2-to-4 decoder; IC 74138 is a 3-to-8 decoder.</p>
<p><b>Applications:</b> memory address decoding, selecting I/O devices, BCD-to-7-segment display drivers, implementing Boolean functions (decoder + OR gate).</p>""",
          f"""<p><b>Decoder</b> <b>n-bit binary input</b> ને <b>2<sup>n</sup> outputs</b> માં ફેરવે છે, જેમાંથી દરેક input combination માટે <b>બરાબર એક output active</b> હોય છે. તે encoder થી ઊલટું કાર્ય કરે છે.</p>
<h4>2-to-4 decoder</h4>
<p>Inputs: A (MSB), B &nbsp; Outputs: Y0, Y1, Y2, Y3</p>{TT_DEC}
<p><b>Y0 = {B('!A!B')}</b>, &nbsp; <b>Y1 = {B('!AB')}</b>, &nbsp; <b>Y2 = {B('A!B')}</b>, &nbsp; <b>Y3 = AB</b></p>
<p>દરેક output inputs નો એક <b>minterm</b> છે, તેથી decoder ને <b>minterm generator</b> પણ કહે છે.</p>
<p><b>Logic diagram:</b> 2 NOT gates અને 4 two-input AND gates.</p>
<p><b>Enable input (E):</b> વ્યવહારુ decoders માં enable input હોય છે; E = 0 હોય ત્યારે બધા outputs 0, અને E = 1 હોય ત્યારે decoder સામાન્ય રીતે કામ કરે (દરેક AND gate ને E વધારાના input તરીકે મળે). IC 74139 dual 2-to-4 decoder છે; IC 74138 3-to-8 decoder છે.</p>
<p><b>ઉપયોગો:</b> memory address decoding, I/O devices ની પસંદગી, BCD-to-7-segment display drivers, Boolean functions બનાવવા (decoder + OR gate).</p>""",
          diagram="de4_dec", examples=["de4n10"], key=True),

        T("4.3.3 Multiplexer (4-to-1 MUX): Introduction and Block Diagram", "4.3.3 Multiplexer (4-to-1 MUX): પરિચય અને Block Diagram",
          f"""<p>A <b>multiplexer (MUX)</b> is a combinational circuit that <b>selects one of many input lines</b> and connects it to a <b>single output line</b>. The input to be selected is chosen by the <b>select lines</b>. It is also called a <b>data selector</b> ("many to one").</p>
<p>A MUX with <b>2<sup>n</sup> data inputs</b> needs <b>n select lines</b> and has <b>1 output</b>. It works like a rotary switch controlled electronically.</p>
<h4>4-to-1 MUX</h4>
<p>Data inputs: I0, I1, I2, I3 &nbsp; Select lines: S1, S0 &nbsp; Output: Y</p>
<h4>Function (truth) table</h4>{TT_MUX}
<p><b>Applications:</b> data routing and selection, parallel-to-serial conversion, time-division multiplexing in communication, implementing Boolean functions without K-map simplification. ICs: 74153 (dual 4:1), 74151 (8:1), 74150 (16:1).</p>""",
          f"""<p><b>Multiplexer (MUX)</b> એવો combinational circuit છે જે <b>ઘણી input lines માંથી એક પસંદ</b> કરીને તેને <b>એક જ output line</b> સાથે જોડે છે. કયો input પસંદ કરવો તે <b>select lines</b> નક્કી કરે છે. તેને <b>data selector</b> પણ કહે છે ("many to one").</p>
<p><b>2<sup>n</sup> data inputs</b> વાળા MUX માં <b>n select lines</b> અને <b>1 output</b> હોય છે. તે electronically control થતી rotary switch જેવું કામ કરે છે.</p>
<h4>4-to-1 MUX</h4>
<p>Data inputs: I0, I1, I2, I3 &nbsp; Select lines: S1, S0 &nbsp; Output: Y</p>
<h4>Function (truth) table</h4>{TT_MUX}
<p><b>ઉપયોગો:</b> data routing અને selection, parallel-to-serial conversion, communication માં time-division multiplexing, K-map simplification વગર Boolean functions બનાવવા. ICs: 74153 (dual 4:1), 74151 (8:1), 74150 (16:1).</p>""",
          diagram="de4_mux", examples=["de4n11"], key=True),

        T("4.3.4 4-to-1 Multiplexer: Logic Diagram", "4.3.4 4-to-1 Multiplexer: Logic Diagram",
          f"""<p>From the function table, I0 reaches the output when S1S0 = 00, I1 when 01, I2 when 10 and I3 when 11:</p>
<p style="text-align:center"><b>{YMUX}</b></p>
<h4>Logic diagram</h4>
<ul><li>2 NOT gates for {S1} and {S0}.</li>
<li>4 three-input AND gates; each gets one data input and one combination of select lines.</li>
<li>1 four-input OR gate combines the AND outputs.</li></ul>
<p>For any select combination, only one AND gate is enabled, so only its data input passes to Y.</p>
<h4>Implementing a function with a MUX</h4>
<p>A function of n variables can be implemented with a 2<sup>n</sup>-to-1 MUX: connect the variables to the select lines and apply 0 or 1 to each data input according to the truth table. With a 4-to-1 MUX, a 3-variable function is possible: two variables go to the select lines and each data input gets 0, 1, C or {B('!C')}.</p>""",
          f"""<p>Function table પરથી S1S0 = 00 હોય ત્યારે I0, 01 હોય ત્યારે I1, 10 હોય ત્યારે I2 અને 11 હોય ત્યારે I3 output માં જાય છે:</p>
<p style="text-align:center"><b>{YMUX}</b></p>
<h4>Logic diagram</h4>
<ul><li>{S1} અને {S0} માટે 2 NOT gates.</li>
<li>4 three-input AND gates; દરેકને એક data input અને select lines નું એક combination મળે.</li>
<li>1 four-input OR gate AND outputs ને જોડે.</li></ul>
<p>કોઈ પણ select combination માટે માત્ર એક AND gate enable થાય છે, તેથી માત્ર તેનો data input Y સુધી પહોંચે છે.</p>
<h4>MUX વડે function બનાવવું</h4>
<p>n variables નું function 2<sup>n</sup>-to-1 MUX વડે બનાવી શકાય: variables ને select lines સાથે જોડો અને truth table મુજબ દરેક data input પર 0 કે 1 આપો. 4-to-1 MUX વડે 3-variable function પણ શક્ય છે: બે variables select lines પર અને દરેક data input પર 0, 1, C અથવા {B('!C')}.</p>""",
          diagram="de4_mux_logic", examples=["de4n12", "de4n13"]),

        T("4.3.5 Demultiplexer (1-to-4 DEMUX): Introduction and Block Diagram", "4.3.5 Demultiplexer (1-to-4 DEMUX): પરિચય અને Block Diagram",
          f"""<p>A <b>demultiplexer (DEMUX)</b> takes <b>one input</b> and sends it to <b>one of many output lines</b>, chosen by the <b>select lines</b>. It does the reverse of a multiplexer and is also called a <b>data distributor</b> ("one to many").</p>
<p>A DEMUX with <b>1 input</b> and <b>2<sup>n</sup> outputs</b> needs <b>n select lines</b>.</p>
<h4>1-to-4 DEMUX</h4>
<p>Data input: D &nbsp; Select lines: S1, S0 &nbsp; Outputs: Y0, Y1, Y2, Y3</p>
<h4>Function (truth) table</h4>{TT_DMX}
<p>The selected output equals D; all other outputs are 0.</p>
<p><b>Applications:</b> serial-to-parallel conversion, distributing data to several devices, the receiving end of a multiplexed communication link, and as a decoder. ICs: 74139 (dual 1:4), 74138 (1:8), 74154 (1:16).</p>""",
          f"""<p><b>Demultiplexer (DEMUX)</b> <b>એક input</b> લઈને તેને <b>ઘણી output lines માંથી એક</b> પર મોકલે છે, જે <b>select lines</b> નક્કી કરે છે. તે multiplexer થી ઊલટું કાર્ય કરે છે અને તેને <b>data distributor</b> પણ કહે છે ("one to many").</p>
<p><b>1 input</b> અને <b>2<sup>n</sup> outputs</b> વાળા DEMUX માં <b>n select lines</b> હોય છે.</p>
<h4>1-to-4 DEMUX</h4>
<p>Data input: D &nbsp; Select lines: S1, S0 &nbsp; Outputs: Y0, Y1, Y2, Y3</p>
<h4>Function (truth) table</h4>{TT_DMX}
<p>પસંદ થયેલો output D બરાબર થાય; બાકીના બધા outputs 0.</p>
<p><b>ઉપયોગો:</b> serial-to-parallel conversion, ઘણા devices ને data વહેંચવો, multiplexed communication link નો receiving છેડો, અને decoder તરીકે. ICs: 74139 (dual 1:4), 74138 (1:8), 74154 (1:16).</p>""",
          diagram="de4_demux", examples=["de4n14"], key=True),

        T("4.3.6 1-to-4 Demultiplexer: Logic Diagram", "4.3.6 1-to-4 Demultiplexer: Logic Diagram",
          f"""<p>From the function table:</p>
<p><b>Y0 = D{S1}{S0}</b>, &nbsp; <b>Y1 = D{S1}S0</b>, &nbsp; <b>Y2 = DS1{S0}</b>, &nbsp; <b>Y3 = DS1S0</b></p>
<h4>Logic diagram</h4>
<ul><li>2 NOT gates for {S1} and {S0}.</li><li>4 three-input AND gates; D goes to all of them.</li><li>No OR gate is needed (4 separate outputs).</li></ul>
<h4>DEMUX as a decoder</h4>
<p>If D is kept at 1, the outputs become Y0 = {S1}{S0}, Y1 = {S1}S0, Y2 = S1{S0}, Y3 = S1S0, which are exactly the outputs of a 2-to-4 decoder. So a 1-to-4 DEMUX is a 2-to-4 decoder with an enable input (D = E). That is why the same IC (74139) is sold as a "decoder/demultiplexer".</p>""",
          f"""<p>Function table પરથી:</p>
<p><b>Y0 = D{S1}{S0}</b>, &nbsp; <b>Y1 = D{S1}S0</b>, &nbsp; <b>Y2 = DS1{S0}</b>, &nbsp; <b>Y3 = DS1S0</b></p>
<h4>Logic diagram</h4>
<ul><li>{S1} અને {S0} માટે 2 NOT gates.</li><li>4 three-input AND gates; D બધાને જાય છે.</li><li>OR gate ની જરૂર નથી (4 અલગ outputs).</li></ul>
<h4>DEMUX decoder તરીકે</h4>
<p>D ને 1 રાખવાથી outputs Y0 = {S1}{S0}, Y1 = {S1}S0, Y2 = S1{S0}, Y3 = S1S0 બને છે, જે 2-to-4 decoder ના outputs જ છે. તેથી 1-to-4 DEMUX એ enable input (D = E) વાળો 2-to-4 decoder છે. આ કારણથી એ જ IC (74139) "decoder/demultiplexer" તરીકે વેચાય છે.</p>""",
          diagram="de4_demux_logic"),

        T("4.3.7 Comparison of Data Transmission Circuits", "4.3.7 Data Transmission Circuits ની સરખામણી",
          """<table><tr><th>Point</th><th>Encoder</th><th>Decoder</th></tr>
<tr><td>Inputs → outputs</td><td>2ⁿ → n</td><td>n → 2ⁿ</td></tr>
<tr><td>Function</td><td>Active line → binary code</td><td>Binary code → one active line</td></tr>
<tr><td>Gates (4:2 / 2:4)</td><td>2 OR</td><td>2 NOT + 4 AND</td></tr>
<tr><td>Example IC</td><td>74147, 74148</td><td>74139, 74138</td></tr></table>
<table><tr><th>Point</th><th>Multiplexer</th><th>Demultiplexer</th></tr>
<tr><td>Inputs → outputs</td><td>2ⁿ → 1</td><td>1 → 2ⁿ</td></tr>
<tr><td>Select lines</td><td>n</td><td>n</td></tr>
<tr><td>Also called</td><td>Data selector</td><td>Data distributor</td></tr>
<tr><td>Gates (4:1 / 1:4)</td><td>2 NOT + 4 AND + 1 OR</td><td>2 NOT + 4 AND</td></tr>
<tr><td>Conversion</td><td>Parallel → serial</td><td>Serial → parallel</td></tr>
<tr><td>Example IC</td><td>74153, 74151</td><td>74139, 74138</td></tr></table>
<p><b>Number of select lines:</b> n = log<sub>2</sub>(number of data lines); 2:1 → 1, 4:1 → 2, 8:1 → 3, 16:1 → 4.</p>""",
          """<table><tr><th>મુદ્દો</th><th>Encoder</th><th>Decoder</th></tr>
<tr><td>Inputs → outputs</td><td>2ⁿ → n</td><td>n → 2ⁿ</td></tr>
<tr><td>કાર્ય</td><td>Active line → binary code</td><td>Binary code → એક active line</td></tr>
<tr><td>Gates (4:2 / 2:4)</td><td>2 OR</td><td>2 NOT + 4 AND</td></tr>
<tr><td>ઉદાહરણ IC</td><td>74147, 74148</td><td>74139, 74138</td></tr></table>
<table><tr><th>મુદ્દો</th><th>Multiplexer</th><th>Demultiplexer</th></tr>
<tr><td>Inputs → outputs</td><td>2ⁿ → 1</td><td>1 → 2ⁿ</td></tr>
<tr><td>Select lines</td><td>n</td><td>n</td></tr>
<tr><td>બીજું નામ</td><td>Data selector</td><td>Data distributor</td></tr>
<tr><td>Gates (4:1 / 1:4)</td><td>2 NOT + 4 AND + 1 OR</td><td>2 NOT + 4 AND</td></tr>
<tr><td>Conversion</td><td>Parallel → serial</td><td>Serial → parallel</td></tr>
<tr><td>ઉદાહરણ IC</td><td>74153, 74151</td><td>74139, 74138</td></tr></table>
<p><b>Select lines ની સંખ્યા:</b> n = log<sub>2</sub>(data lines ની સંખ્યા); 2:1 → 1, 4:1 → 2, 8:1 → 3, 16:1 → 4.</p>""",
          diagram="de4_compare", examples=["de4n15"]),
    ],
}

NOTES_B = [SEC_4_3]
