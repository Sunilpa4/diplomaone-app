"""Digital Electronics Fundamentals (DI03000011) - Unit 5 notes: 5.1 Sequential circuits, 5.2 Flip-flops."""
from content_DI03000011_u1_notes_a import T
from de_gates import tt_html, bh as B
from diagrams_DI03000011_u5 import NOR_ROWS, NAND_ROWS

QB = B("!Q")
QNB = B("!(Qn)")


def st_table(head, rows_):
    h = "<table><tr>" + "".join(f"<th>{x}</th>" for x in head) + "</tr>"
    for r in rows_:
        h += "<tr>" + "".join(f"<td>{v}</td>" for v in r) + "</tr>"
    return h + "</table>"


TT_NOR = st_table(["S", "R", "Q", "State"], [(a, b, q.replace("*", " (Q = " + QB + " = 0)") if "*" in q else q, s) for a, b, q, s in NOR_ROWS])
TT_NAND = st_table([B("!S"), B("!R"), "Q", "State"], [(a, b, q.replace("*", " (Q = " + QB + " = 1)") if "*" in q else q, s) for a, b, q, s in NAND_ROWS])
TT_SR = st_table(["CLK", "S", "R", "Q<sub>n+1</sub>", "State"], [("0", "X", "X", "Q<sub>n</sub>", "No change"), ("1", "0", "0", "Q<sub>n</sub>", "No change"),
                                                                 ("1", "0", "1", "0", "Reset"), ("1", "1", "0", "1", "Set"), ("1", "1", "1", "?", "Invalid (not allowed)")])
TT_JK = st_table(["CLK", "J", "K", "Q<sub>n+1</sub>", "State"], [("0", "X", "X", "Q<sub>n</sub>", "No change"), ("↑", "0", "0", "Q<sub>n</sub>", "No change"),
                                                                 ("↑", "0", "1", "0", "Reset"), ("↑", "1", "0", "1", "Set"), ("↑", "1", "1", QNB, "Toggle")])
TT_D = st_table(["CLK", "D", "Q<sub>n+1</sub>", "State"], [("0", "X", "Q<sub>n</sub>", "No change"), ("↑", "0", "0", "Reset"), ("↑", "1", "1", "Set")])
TT_T = st_table(["CLK", "T", "Q<sub>n+1</sub>", "State"], [("0", "X", "Q<sub>n</sub>", "No change"), ("↑", "0", "Q<sub>n</sub>", "No change"), ("↑", "1", QNB, "Toggle")])

GU_STATE = {"No change": "No change (ફેરફાર નહીં)", "Reset": "Reset", "Set": "Set", "Invalid": "Invalid (અમાન્ય)", "Toggle": "Toggle (ઉલટાય)",
            "Invalid (not allowed)": "Invalid (મંજૂર નથી)"}


def gu_tbl(h):
    for k, v in sorted(GU_STATE.items(), key=lambda kv: -len(kv[0])):
        h = h.replace(f"<td>{k}</td>", f"<td>{v}</td>")
    return h


SEC_5_1 = {
    "title": {"en": "5.1 Basic Sequential Circuits", "gu": "5.1 Basic Sequential Circuits"},
    "items": [
        T("5.1.1 Introduction to Sequential Circuits", "5.1.1 Sequential Circuits નો પરિચય",
          """<p>A <b>sequential circuit</b> is a logic circuit whose output depends on the <b>present inputs</b> and also on the <b>past state</b> (previous outputs). It therefore needs <b>memory</b>.</p>
<p>It consists of a <b>combinational circuit</b> plus <b>memory elements</b> (flip-flops) connected in a <b>feedback</b> path:</p>
<ul>
<li>The combinational circuit uses the external inputs and the <b>present state</b> (from memory) to produce the outputs and the <b>next state</b>.</li>
<li>The memory elements store the state; usually they change only at the <b>clock</b> signal.</li>
</ul>
<p>The sequence of states, not only the present input, decides the output. Example: a counter gives 0, 1, 2, 3… for the same clock input.</p>
<h4>Types</h4>
<ul>
<li><b>Synchronous sequential circuits:</b> all memory elements change state together, controlled by a common clock (e.g. synchronous counter).</li>
<li><b>Asynchronous sequential circuits:</b> outputs change whenever inputs change; there is no common clock (e.g. ripple counter, basic latch).</li>
</ul>
<p><b>Examples:</b> flip-flops, registers, counters, RAM, the control unit of a CPU.</p>""",
          """<p><b>Sequential circuit</b> એવો logic circuit છે જેનો output <b>હાલના inputs</b> પર અને સાથે <b>અગાઉની state</b> (પહેલાંના outputs) પર પણ આધાર રાખે છે. તેથી તેમાં <b>memory</b> જરૂરી છે.</p>
<p>તે <b>combinational circuit</b> અને <b>feedback</b> path માં જોડાયેલા <b>memory elements</b> (flip-flops) થી બને છે:</p>
<ul>
<li>Combinational circuit બહારના inputs અને <b>present state</b> (memory માંથી) વાપરી outputs અને <b>next state</b> બનાવે છે.</li>
<li>Memory elements state ને store કરે છે; સામાન્ય રીતે તેઓ માત્ર <b>clock</b> signal વખતે બદલાય છે.</li>
</ul>
<p>માત્ર હાલનો input નહીં, પણ states નો ક્રમ output નક્કી કરે છે. ઉદાહરણ: counter એક જ clock input માટે 0, 1, 2, 3… આપે છે.</p>
<h4>પ્રકારો</h4>
<ul>
<li><b>Synchronous sequential circuits:</b> બધા memory elements common clock ના નિયંત્રણમાં એકસાથે state બદલે છે (દા.ત. synchronous counter).</li>
<li><b>Asynchronous sequential circuits:</b> inputs બદલાય ત્યારે outputs બદલાય; common clock નથી (દા.ત. ripple counter, basic latch).</li>
</ul>
<p><b>ઉદાહરણો:</b> flip-flops, registers, counters, RAM, CPU નું control unit.</p>""",
          diagram="de5_seq", key=True),

        T("5.1.2 Clock Signal and Triggering", "5.1.2 Clock Signal અને Triggering",
          """<p>A <b>clock</b> is a periodic square-wave signal that controls <b>when</b> a synchronous sequential circuit changes state.</p>
<ul>
<li><b>Period (T):</b> time of one cycle; <b>frequency</b> f = 1/T (e.g. T = 1 ms → f = 1 kHz).</li>
<li><b>Positive (rising) edge:</b> the change from 0 to 1.</li>
<li><b>Negative (falling) edge:</b> the change from 1 to 0.</li>
</ul>
<h4>Triggering</h4>
<p>Making a flip-flop respond to its inputs is called <b>triggering</b>:</p>
<ul>
<li><b>Level triggering:</b> the circuit responds during the whole time the clock is HIGH (positive level) or LOW (negative level). Latches are level triggered.</li>
<li><b>Edge triggering:</b> the circuit responds only at the instant of a clock edge: <b>positive-edge</b> (0 → 1) or <b>negative-edge</b> (1 → 0) triggered. Most flip-flops are edge triggered, so the output changes only once per clock cycle.</li>
</ul>""",
          """<p><b>Clock</b> એક periodic square-wave signal છે જે synchronous sequential circuit <b>ક્યારે</b> state બદલે તે નક્કી કરે છે.</p>
<ul>
<li><b>Period (T):</b> એક cycle નો સમય; <b>frequency</b> f = 1/T (દા.ત. T = 1 ms → f = 1 kHz).</li>
<li><b>Positive (rising) edge:</b> 0 થી 1 તરફનો ફેરફાર.</li>
<li><b>Negative (falling) edge:</b> 1 થી 0 તરફનો ફેરફાર.</li>
</ul>
<h4>Triggering</h4>
<p>Flip-flop ને તેના inputs પ્રત્યે પ્રતિભાવ આપતો કરવો તેને <b>triggering</b> કહે છે:</p>
<ul>
<li><b>Level triggering:</b> clock HIGH (positive level) કે LOW (negative level) હોય તે આખા સમય દરમિયાન circuit પ્રતિભાવ આપે. Latches level triggered હોય છે.</li>
<li><b>Edge triggering:</b> circuit માત્ર clock edge ની ક્ષણે પ્રતિભાવ આપે: <b>positive-edge</b> (0 → 1) અથવા <b>negative-edge</b> (1 → 0) triggered. મોટા ભાગના flip-flops edge triggered હોય છે, તેથી output દરેક clock cycle માં એક જ વાર બદલાય છે.</li>
</ul>""",
          diagram="de5_clock"),

        T("5.1.3 Difference between Combinational and Sequential Circuits", "5.1.3 Combinational અને Sequential Circuits વચ્ચે તફાવત",
          """<table><tr><th>No.</th><th>Combinational circuit</th><th>Sequential circuit</th></tr>
<tr><td>1</td><td>Output depends only on present inputs.</td><td>Output depends on present inputs and past state.</td></tr>
<tr><td>2</td><td>No memory element.</td><td>Has memory elements (flip-flops).</td></tr>
<tr><td>3</td><td>No feedback path.</td><td>Feedback from output (state) to input.</td></tr>
<tr><td>4</td><td>No clock needed.</td><td>Clock is usually needed (synchronous).</td></tr>
<tr><td>5</td><td>Faster and easier to design.</td><td>Slower and more complex to design.</td></tr>
<tr><td>6</td><td>Described by a truth table.</td><td>Described by a state table / characteristic table and timing diagram.</td></tr>
<tr><td>7</td><td>Building blocks: logic gates.</td><td>Building blocks: flip-flops + gates.</td></tr>
<tr><td>8</td><td>Examples: adder, subtractor, MUX, decoder.</td><td>Examples: flip-flop, register, counter, RAM.</td></tr></table>""",
          """<table><tr><th>ક્રમ</th><th>Combinational circuit</th><th>Sequential circuit</th></tr>
<tr><td>1</td><td>Output માત્ર હાલના inputs પર આધાર રાખે.</td><td>Output હાલના inputs અને અગાઉની state પર આધાર રાખે.</td></tr>
<tr><td>2</td><td>Memory element નથી.</td><td>Memory elements (flip-flops) હોય છે.</td></tr>
<tr><td>3</td><td>Feedback path નથી.</td><td>Output (state) થી input તરફ feedback.</td></tr>
<tr><td>4</td><td>Clock ની જરૂર નથી.</td><td>સામાન્ય રીતે clock જોઈએ (synchronous).</td></tr>
<tr><td>5</td><td>ઝડપી અને design કરવામાં સરળ.</td><td>ધીમો અને design કરવામાં જટિલ.</td></tr>
<tr><td>6</td><td>Truth table વડે વર્ણન.</td><td>State table / characteristic table અને timing diagram વડે વર્ણન.</td></tr>
<tr><td>7</td><td>Building blocks: logic gates.</td><td>Building blocks: flip-flops + gates.</td></tr>
<tr><td>8</td><td>ઉદાહરણો: adder, subtractor, MUX, decoder.</td><td>ઉદાહરણો: flip-flop, register, counter, RAM.</td></tr></table>""",
          diagram="de5_compare", key=True),
    ],
}

SEC_5_2 = {
    "title": {"en": "5.2 Flip-Flops", "gu": "5.2 Flip-Flops"},
    "items": [
        T("5.2.1 Introduction to Flip-Flops; SR Latch using NOR Gates", "5.2.1 Flip-Flops નો પરિચય; NOR Gates વડે SR Latch",
          f"""<p>A <b>flip-flop (FF)</b> is a <b>1-bit memory element</b>: a bistable circuit with two stable states, 1 (set) and 0 (reset). It stays in a state until an input changes it. It has two complementary outputs, <b>Q</b> and <b>{QB}</b>.</p>
<p><b>Types:</b> SR, JK, D and T flip-flops. A <b>latch</b> is the basic unclocked (or level-triggered) form; a <b>flip-flop</b> usually means a clocked, edge-triggered device.</p>
<h4>SR latch using NOR gates</h4>
<p>Two NOR gates are <b>cross-coupled</b>: the output of each gate is fed back to an input of the other. Inputs: S (set) and R (reset).</p>{TT_NOR}
<ul><li>S = 0, R = 0: outputs stay as they were (<b>memory / hold</b>).</li>
<li>S = 0, R = 1: Q = 0 (<b>reset</b>).</li>
<li>S = 1, R = 0: Q = 1 (<b>set</b>).</li>
<li>S = 1, R = 1: Q = {QB} = 0, which breaks the rule that the outputs are complements. When both inputs return to 0 the final state is unpredictable, so this is the <b>invalid (forbidden)</b> condition.</li></ul>""",
          f"""<p><b>Flip-flop (FF)</b> એક <b>1-bit memory element</b> છે: બે stable states, 1 (set) અને 0 (reset), ધરાવતો bistable circuit. Input તેને બદલે નહીં ત્યાં સુધી તે એક state માં રહે છે. તેને બે complementary outputs, <b>Q</b> અને <b>{QB}</b>, હોય છે.</p>
<p><b>પ્રકારો:</b> SR, JK, D અને T flip-flops. <b>Latch</b> મૂળભૂત clock વગરનું (અથવા level-triggered) સ્વરૂપ છે; <b>flip-flop</b> સામાન્ય રીતે clocked, edge-triggered device ને કહે છે.</p>
<h4>NOR gates વડે SR latch</h4>
<p>બે NOR gates <b>cross-coupled</b> હોય છે: દરેક gate નો output બીજા gate ના input માં feedback તરીકે જાય છે. Inputs: S (set) અને R (reset).</p>{gu_tbl(TT_NOR)}
<ul><li>S = 0, R = 0: outputs પહેલાં જેવા જ રહે (<b>memory / hold</b>).</li>
<li>S = 0, R = 1: Q = 0 (<b>reset</b>).</li>
<li>S = 1, R = 0: Q = 1 (<b>set</b>).</li>
<li>S = 1, R = 1: Q = {QB} = 0, જે outputs complement હોવાનો નિયમ તોડે છે. બંને inputs પાછા 0 થાય ત્યારે અંતિમ state અનિશ્ચિત હોય છે, તેથી આ <b>invalid (forbidden)</b> condition છે.</li></ul>""",
          diagram="de5_latch", examples=["de5n1"], key=True),

        T("5.2.2 SR Latch using NAND Gates", "5.2.2 NAND Gates વડે SR Latch",
          f"""<p>An SR latch can also be made with two cross-coupled <b>NAND</b> gates. Its inputs are <b>active LOW</b>, so they are written {B('!S')} and {B('!R')}: a 0 on an input performs the action.</p>{TT_NAND}
<ul><li>{B('!S')} = 1, {B('!R')} = 1: hold (no change).</li>
<li>{B('!S')} = 1, {B('!R')} = 0: reset, Q = 0.</li>
<li>{B('!S')} = 0, {B('!R')} = 1: set, Q = 1.</li>
<li>{B('!S')} = {B('!R')} = 0: Q = {QB} = 1: invalid.</li></ul>
<p>Compared with the NOR latch, the table is the same but with inverted inputs. Adding NOT gates (or NAND gates with a clock) at the inputs gives an active-HIGH SR latch / flip-flop.</p>""",
          f"""<p>SR latch બે cross-coupled <b>NAND</b> gates વડે પણ બને છે. તેના inputs <b>active LOW</b> છે, તેથી તેમને {B('!S')} અને {B('!R')} લખાય છે: input પર 0 આપવાથી action થાય છે.</p>{gu_tbl(TT_NAND)}
<ul><li>{B('!S')} = 1, {B('!R')} = 1: hold (ફેરફાર નહીં).</li>
<li>{B('!S')} = 1, {B('!R')} = 0: reset, Q = 0.</li>
<li>{B('!S')} = 0, {B('!R')} = 1: set, Q = 1.</li>
<li>{B('!S')} = {B('!R')} = 0: Q = {QB} = 1: invalid.</li></ul>
<p>NOR latch ની સરખામણીમાં table સરખું છે પણ inputs ઊલટા છે. Inputs પર NOT gates (અથવા clock સાથે NAND gates) ઉમેરવાથી active-HIGH SR latch / flip-flop બને છે.</p>""",
          diagram="de5_sr_nand", examples=["de5n2"]),

        T("5.2.3 SR Flip-Flop (Clocked SR)", "5.2.3 SR Flip-Flop (Clocked SR)",
          f"""<p>A <b>clocked SR flip-flop</b> is a NAND latch with two extra NAND gates (steering gates) at the input, controlled by the <b>clock (CLK)</b>.</p>
<ul><li><b>CLK = 0:</b> both steering gates give 1, so the latch holds its state whatever S and R are.</li>
<li><b>CLK = 1:</b> the steering gates pass {B('!S')} and {B('!R')} to the latch, so it works as an active-HIGH SR latch.</li></ul>
<h4>Truth table</h4>{TT_SR}
<h4>Characteristic equation</h4>
<p><b>Q<sub>n+1</sub> = S + {B('!R')}Q<sub>n</sub></b> &nbsp; with the condition SR = 0 (derived by K-map in the solved example).</p>
<p><b>Drawback:</b> S = R = 1 is not allowed (invalid state). The JK flip-flop removes this problem.</p>""",
          f"""<p><b>Clocked SR flip-flop</b> એ NAND latch છે જેના input પર <b>clock (CLK)</b> વડે નિયંત્રિત બે વધારાના NAND gates (steering gates) હોય છે.</p>
<ul><li><b>CLK = 0:</b> બંને steering gates 1 આપે, તેથી S અને R ગમે તે હોય latch તેની state જાળવી રાખે.</li>
<li><b>CLK = 1:</b> steering gates {B('!S')} અને {B('!R')} latch ને આપે, તેથી તે active-HIGH SR latch તરીકે કામ કરે.</li></ul>
<h4>Truth table</h4>{gu_tbl(TT_SR)}
<h4>Characteristic equation</h4>
<p><b>Q<sub>n+1</sub> = S + {B('!R')}Q<sub>n</sub></b> &nbsp; શરત SR = 0 સાથે (solved example માં K-map વડે મેળવેલ).</p>
<p><b>ખામી:</b> S = R = 1 મંજૂર નથી (invalid state). JK flip-flop આ સમસ્યા દૂર કરે છે.</p>""",
          diagram="de5_sr", examples=["de5n3", "de5n4"], key=True),

        T("5.2.4 JK Flip-Flop", "5.2.4 JK Flip-Flop",
          f"""<p>The <b>JK flip-flop</b> is a modified SR flip-flop in which the invalid state is removed. The outputs are fed back: <b>{QB}</b> goes to the J steering gate and <b>Q</b> goes to the K steering gate. J acts like S (set) and K like R (reset).</p>
<h4>Truth table</h4>{TT_JK}
<ul><li>J = K = 0: no change.</li><li>J = 0, K = 1: reset (Q = 0).</li><li>J = 1, K = 0: set (Q = 1).</li>
<li>J = K = 1: the output <b>toggles</b> (changes to its complement). Because of the feedback, only one steering gate is enabled at a time, so the invalid state cannot occur.</li></ul>
<h4>Characteristic equation</h4>
<p><b>Q<sub>n+1</sub> = J{B('!(Qn)')} + {B('!K')}Q<sub>n</sub></b></p>
<h4>Race-around condition</h4>
<p>In a level-triggered JK flip-flop with J = K = 1, the output toggles; if the clock stays HIGH longer than the propagation delay, the new output is fed back and the output toggles again and again. This uncertain oscillation is the <b>race-around condition</b>.</p>
<p><b>Remedies:</b> keep the clock pulse width less than the propagation delay, use <b>edge triggering</b>, or use a <b>master–slave JK flip-flop</b> (two latches: the master responds when CLK = 1 and the slave copies it when CLK = 0, so the output changes only once per clock).</p>""",
          f"""<p><b>JK flip-flop</b> એ modified SR flip-flop છે જેમાં invalid state દૂર કરેલી છે. Outputs ને feedback અપાય છે: <b>{QB}</b> J steering gate માં અને <b>Q</b> K steering gate માં જાય છે. J એ S (set) જેવું અને K એ R (reset) જેવું કામ કરે છે.</p>
<h4>Truth table</h4>{gu_tbl(TT_JK)}
<ul><li>J = K = 0: ફેરફાર નહીં.</li><li>J = 0, K = 1: reset (Q = 0).</li><li>J = 1, K = 0: set (Q = 1).</li>
<li>J = K = 1: output <b>toggle</b> થાય (તેના complement માં બદલાય). Feedback ના કારણે એક સમયે એક જ steering gate enable થાય છે, તેથી invalid state આવી શકતી નથી.</li></ul>
<h4>Characteristic equation</h4>
<p><b>Q<sub>n+1</sub> = J{B('!(Qn)')} + {B('!K')}Q<sub>n</sub></b></p>
<h4>Race-around condition</h4>
<p>J = K = 1 વાળા level-triggered JK flip-flop માં output toggle થાય છે; જો clock propagation delay કરતાં વધુ સમય HIGH રહે, તો નવો output feedback થઈ output વારંવાર toggle થાય છે. આ અનિશ્ચિત oscillation ને <b>race-around condition</b> કહે છે.</p>
<p><b>ઉપાયો:</b> clock pulse width propagation delay કરતાં ઓછી રાખવી, <b>edge triggering</b> વાપરવું, અથવા <b>master–slave JK flip-flop</b> વાપરવો (બે latches: CLK = 1 હોય ત્યારે master પ્રતિભાવ આપે અને CLK = 0 હોય ત્યારે slave તેની નકલ કરે, તેથી output દરેક clock માં એક જ વાર બદલાય).</p>""",
          diagram="de5_jk", examples=["de5n5", "de5n6"], key=True),

        T("5.2.5 D Flip-Flop", "5.2.5 D Flip-Flop",
          f"""<p>The <b>D (Data / Delay) flip-flop</b> has a single data input D. It is made from an SR flip-flop by connecting <b>S = D</b> and <b>R = {B('!D')}</b> through a NOT gate. So S and R are always complements and the invalid state S = R = 1 can never occur.</p>
<h4>Truth table</h4>{TT_D}
<h4>Characteristic equation</h4>
<p><b>Q<sub>n+1</sub> = D</b></p>
<p>At each clock edge the output simply takes the value of D and holds it until the next edge. The data appears at the output one clock period later, hence the name <b>delay</b> flip-flop.</p>
<p><b>Applications:</b> storing data bits, <b>registers</b> (shift registers, buffer registers), delay elements, synchronising inputs. ICs: 7474 (dual positive-edge D FF), 74175.</p>""",
          f"""<p><b>D (Data / Delay) flip-flop</b> માં એક જ data input D હોય છે. તે SR flip-flop માં NOT gate વડે <b>S = D</b> અને <b>R = {B('!D')}</b> જોડીને બને છે. તેથી S અને R હંમેશા complement હોય છે અને invalid state S = R = 1 ક્યારેય આવતી નથી.</p>
<h4>Truth table</h4>{gu_tbl(TT_D)}
<h4>Characteristic equation</h4>
<p><b>Q<sub>n+1</sub> = D</b></p>
<p>દરેક clock edge વખતે output માત્ર D ની કિંમત લે છે અને પછીની edge સુધી તેને જાળવી રાખે છે. Data output પર એક clock period પછી દેખાય છે, તેથી તેને <b>delay</b> flip-flop કહે છે.</p>
<p><b>ઉપયોગો:</b> data bits store કરવા, <b>registers</b> (shift registers, buffer registers), delay elements, inputs synchronise કરવા. ICs: 7474 (dual positive-edge D FF), 74175.</p>""",
          diagram="de5_d", examples=["de5n7"], key=True),

        T("5.2.6 T (Toggle) Flip-Flop", "5.2.6 T (Toggle) Flip-Flop",
          f"""<p>The <b>T (Toggle) flip-flop</b> has a single input T. It is obtained from a JK flip-flop by connecting <b>J = K = T</b>.</p>
<h4>Truth table</h4>{TT_T}
<ul><li>T = 0: no change (J = K = 0).</li><li>T = 1: the output toggles at every clock edge (J = K = 1).</li></ul>
<h4>Characteristic equation</h4>
<p><b>Q<sub>n+1</sub> = T{B('!(Qn)')} + {B('!T')}Q<sub>n</sub> = T ⊕ Q<sub>n</sub></b></p>
<h4>Frequency division</h4>
<p>With T = 1 the output changes once per clock cycle, so Q completes one cycle every two clock cycles: <b>f<sub>Q</sub> = f<sub>CLK</sub> / 2</b>. Cascading n T flip-flops divides the frequency by 2<sup>n</sup>.</p>
<p><b>Applications:</b> counters (ripple / binary counters), frequency dividers.</p>""",
          f"""<p><b>T (Toggle) flip-flop</b> માં એક જ input T હોય છે. તે JK flip-flop માં <b>J = K = T</b> જોડીને મળે છે.</p>
<h4>Truth table</h4>{gu_tbl(TT_T)}
<ul><li>T = 0: ફેરફાર નહીં (J = K = 0).</li><li>T = 1: દરેક clock edge વખતે output toggle થાય (J = K = 1).</li></ul>
<h4>Characteristic equation</h4>
<p><b>Q<sub>n+1</sub> = T{B('!(Qn)')} + {B('!T')}Q<sub>n</sub> = T ⊕ Q<sub>n</sub></b></p>
<h4>Frequency division</h4>
<p>T = 1 હોય ત્યારે output દરેક clock cycle માં એક વાર બદલાય છે, તેથી Q દર બે clock cycles માં એક cycle પૂરી કરે છે: <b>f<sub>Q</sub> = f<sub>CLK</sub> / 2</b>. n T flip-flops cascade કરવાથી frequency 2<sup>n</sup> વડે ભાગાય છે.</p>
<p><b>ઉપયોગો:</b> counters (ripple / binary counters), frequency dividers.</p>""",
          diagram="de5_t", examples=["de5n8", "de5n9"], key=True),

        T("5.2.7 Flip-Flop Symbols and Edge Triggering", "5.2.7 Flip-Flop Symbols અને Edge Triggering",
          f"""<p>In a flip-flop symbol the inputs are on the left and the outputs Q and {QB} on the right.</p>
<ul>
<li>A small <b>triangle (&gt;)</b> at the clock input means <b>edge triggered</b>.</li>
<li>Triangle only: <b>positive-edge</b> triggered (acts at 0 → 1).</li>
<li>Bubble + triangle: <b>negative-edge</b> triggered (acts at 1 → 0).</li>
<li>No triangle: <b>level triggered</b> (latch); a bubble means active-LOW level.</li>
</ul>
<p>Practical flip-flop ICs also have asynchronous <b>Preset (PR)</b> and <b>Clear (CLR)</b> inputs that set Q = 1 or Q = 0 immediately, independent of the clock. They are used to give the flip-flop a known starting state.</p>""",
          f"""<p>Flip-flop symbol માં inputs ડાબી બાજુ અને outputs Q અને {QB} જમણી બાજુ હોય છે.</p>
<ul>
<li>Clock input પર નાનો <b>triangle (&gt;)</b> એટલે <b>edge triggered</b>.</li>
<li>માત્ર triangle: <b>positive-edge</b> triggered (0 → 1 વખતે કામ કરે).</li>
<li>Bubble + triangle: <b>negative-edge</b> triggered (1 → 0 વખતે કામ કરે).</li>
<li>Triangle નહીં: <b>level triggered</b> (latch); bubble એટલે active-LOW level.</li>
</ul>
<p>વ્યવહારુ flip-flop ICs માં asynchronous <b>Preset (PR)</b> અને <b>Clear (CLR)</b> inputs પણ હોય છે, જે clock થી સ્વતંત્ર રીતે તરત જ Q = 1 કે Q = 0 કરે છે. તેનો ઉપયોગ flip-flop ને જાણીતી શરૂઆતની state આપવા થાય છે.</p>""",
          diagram="de5_symbols"),

        T("5.2.8 Timing Diagram of a Flip-Flop", "5.2.8 Flip-Flop નો Timing Diagram",
          """<p>A <b>timing diagram</b> shows the clock, the inputs and the output of a flip-flop against time. It is drawn as follows:</p>
<ol>
<li>Draw the clock waveform and mark each <b>active edge</b> (rising edge for a positive-edge FF) with a dashed line.</li>
<li>Draw the input waveform(s).</li>
<li>At each active edge, read the inputs and find Q<sub>n+1</sub> from the truth table (for D: Q = D; for T: toggle if T = 1; for JK: use the JK table).</li>
<li>Keep Q constant between edges.</li>
</ol>
<p>For a D flip-flop, changes in D between edges have <b>no effect</b>; only the value at the edge matters. The input must be stable for a short <b>set-up time</b> before the edge and a <b>hold time</b> after it.</p>""",
          """<p><b>Timing diagram</b> flip-flop ના clock, inputs અને output ને સમય સામે દર્શાવે છે. તે નીચે મુજબ દોરાય છે:</p>
<ol>
<li>Clock waveform દોરો અને દરેક <b>active edge</b> (positive-edge FF માટે rising edge) ને dashed line વડે દર્શાવો.</li>
<li>Input waveform(s) દોરો.</li>
<li>દરેક active edge વખતે inputs વાંચી truth table પરથી Q<sub>n+1</sub> શોધો (D માટે: Q = D; T માટે: T = 1 હોય તો toggle; JK માટે: JK table વાપરો).</li>
<li>બે edges વચ્ચે Q અચળ રાખો.</li>
</ol>
<p>D flip-flop માટે edges વચ્ચે D માં થતા ફેરફારોની <b>કોઈ અસર નથી</b>; માત્ર edge વખતની કિંમત મહત્વની છે. Input edge પહેલાં થોડા <b>set-up time</b> અને edge પછી <b>hold time</b> સુધી stable હોવો જોઈએ.</p>""",
          diagram="de5_timing", examples=["de5n10"]),

        T("5.2.9 Comparison, Characteristic Equations and Conversions", "5.2.9 સરખામણી, Characteristic Equations અને Conversions",
          f"""<table><tr><th>FF</th><th>Inputs</th><th>Characteristic equation</th><th>Special feature</th></tr>
<tr><td>SR</td><td>S, R</td><td>Q<sub>n+1</sub> = S + {B('!R')}Q<sub>n</sub> (SR = 0)</td><td>S = R = 1 invalid</td></tr>
<tr><td>JK</td><td>J, K</td><td>Q<sub>n+1</sub> = J{QNB} + {B('!K')}Q<sub>n</sub></td><td>J = K = 1 toggles; no invalid state</td></tr>
<tr><td>D</td><td>D</td><td>Q<sub>n+1</sub> = D</td><td>Output follows input; data storage</td></tr>
<tr><td>T</td><td>T</td><td>Q<sub>n+1</sub> = T ⊕ Q<sub>n</sub></td><td>T = 1 toggles; counters</td></tr></table>
<h4>Conversions</h4>
<ul>
<li><b>SR to D:</b> S = D, R = {B('!D')}.</li>
<li><b>JK to D:</b> J = D, K = {B('!D')}.</li>
<li><b>JK to T:</b> J = K = T.</li>
<li><b>JK to SR:</b> J = S, K = R (with S = R = 1 not used).</li>
</ul>
<p>Because SR, D and T can all be made from it, the <b>JK flip-flop is called the universal flip-flop</b>.</p>""",
          f"""<table><tr><th>FF</th><th>Inputs</th><th>Characteristic equation</th><th>વિશેષતા</th></tr>
<tr><td>SR</td><td>S, R</td><td>Q<sub>n+1</sub> = S + {B('!R')}Q<sub>n</sub> (SR = 0)</td><td>S = R = 1 invalid</td></tr>
<tr><td>JK</td><td>J, K</td><td>Q<sub>n+1</sub> = J{QNB} + {B('!K')}Q<sub>n</sub></td><td>J = K = 1 toggle; invalid state નથી</td></tr>
<tr><td>D</td><td>D</td><td>Q<sub>n+1</sub> = D</td><td>Output input ને અનુસરે; data storage</td></tr>
<tr><td>T</td><td>T</td><td>Q<sub>n+1</sub> = T ⊕ Q<sub>n</sub></td><td>T = 1 toggle; counters</td></tr></table>
<h4>Conversions</h4>
<ul>
<li><b>SR થી D:</b> S = D, R = {B('!D')}.</li>
<li><b>JK થી D:</b> J = D, K = {B('!D')}.</li>
<li><b>JK થી T:</b> J = K = T.</li>
<li><b>JK થી SR:</b> J = S, K = R (S = R = 1 વાપરવું નહીં).</li>
</ul>
<p>SR, D અને T બધા તેમાંથી બની શકે છે, તેથી <b>JK flip-flop ને universal flip-flop</b> કહે છે.</p>""",
          diagram="de5_convert", examples=["de5n11"], key=True),

        T("5.2.10 Applications of Flip-Flops", "5.2.10 Flip-Flops ના ઉપયોગો",
          """<ul>
<li><b>Memory:</b> one flip-flop stores one bit; n flip-flops store an n-bit word (static RAM cells, CPU registers).</li>
<li><b>Registers:</b> groups of D flip-flops to hold or shift data (buffer, shift registers, serial ↔ parallel conversion).</li>
<li><b>Counters:</b> T or JK flip-flops count clock pulses (ripple and synchronous counters, digital clocks).</li>
<li><b>Frequency division:</b> each toggling flip-flop divides the frequency by 2.</li>
<li><b>Switch debouncing:</b> an SR latch removes contact bounce of mechanical switches.</li>
<li><b>Data synchronisation</b> and <b>event detection</b> (storing that an event happened).</li>
</ul>
<p>n flip-flops have <b>2<sup>n</sup> possible states</b>, e.g. 4 flip-flops → 16 states (a mod-16 counter).</p>""",
          """<ul>
<li><b>Memory:</b> એક flip-flop એક bit store કરે; n flip-flops n-bit word store કરે (static RAM cells, CPU registers).</li>
<li><b>Registers:</b> data રાખવા કે shift કરવા D flip-flops ના સમૂહ (buffer, shift registers, serial ↔ parallel conversion).</li>
<li><b>Counters:</b> T અથવા JK flip-flops clock pulses ગણે (ripple અને synchronous counters, digital clocks).</li>
<li><b>Frequency division:</b> દરેક toggling flip-flop frequency ને 2 વડે ભાગે.</li>
<li><b>Switch debouncing:</b> SR latch mechanical switches નો contact bounce દૂર કરે.</li>
<li><b>Data synchronisation</b> અને <b>event detection</b> (કોઈ ઘટના બની તે store કરવું).</li>
</ul>
<p>n flip-flops ની <b>2<sup>n</sup> શક્ય states</b> હોય છે, દા.ત. 4 flip-flops → 16 states (mod-16 counter).</p>""",
          examples=["de5n12"]),
    ],
}

NOTES = [SEC_5_1, SEC_5_2]
