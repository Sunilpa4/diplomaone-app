"""Digital Electronics Fundamentals (DI03000011) - Unit 5 extras: numericals (simulated and checked), equations, viva, exam."""
from content_DI03000011_u1_extras import N, E, V, X
from content_DI03000011_u3_common import solve
from de_gates import bh as B
import de_seq as S
from diagrams_DI03000011_u5 import D_IN

QB = B("!Q")
QNB = B("!(Qn)")
STATE_EN = {"hold": "No change", "set": "Set", "reset": "Reset", "toggle": "Toggle", "invalid": "Invalid"}
STATE_GU = {"hold": "ફેરફાર નહીં", "set": "Set", "reset": "Reset", "toggle": "Toggle", "invalid": "Invalid"}


def tbl(head, rows_):
    h = "<table><tr>" + "".join(f"<th>{x}</th>" for x in head) + "</tr>"
    for r in rows_:
        h += "<tr>" + "".join(f"<td>{v}</td>" for v in r) + "</tr>"
    return h + "</table>"


def kind_of(q, nq):
    if nq is None:
        return "invalid"
    return "hold" if q == nq else ("set" if nq == 1 else "reset")


# ---------------------------------------------------------------- n1: NOR latch sequence
SEQ1 = [(1, 0), (0, 0), (0, 1), (0, 0), (1, 0), (0, 0)]
q, r1 = 0, []
for i, (s, r) in enumerate(SEQ1):
    res = S.nor_latch(s, r, q)
    nq = res[0]
    k = kind_of(q, nq)
    r1.append((i + 1, s, r, q, nq, k))
    q = nq
assert [x[4] for x in r1] == [1, 1, 0, 0, 1, 1]
_t1e = tbl(["Step", "S", "R", "Q before", "Q after", "Action"], [(a, b, c, d, f"<b>{e}</b>", STATE_EN[k]) for a, b, c, d, e, k in r1])
_t1g = tbl(["Step", "S", "R", "પહેલાં Q", "પછી Q", "Action"], [(a, b, c, d, f"<b>{e}</b>", STATE_GU[k]) for a, b, c, d, e, k in r1])
A1E = f"<p>Use the NOR latch table: S = 1 sets, R = 1 resets, S = R = 0 holds. Initially Q = 0.</p>{_t1e}<p>Output sequence of Q: <b>{', '.join(str(x[4]) for x in r1)}</b>.</p>"
A1G = f"<p>NOR latch table વાપરો: S = 1 set કરે, R = 1 reset કરે, S = R = 0 hold કરે. શરૂઆતમાં Q = 0.</p>{_t1g}<p>Q નો output ક્રમ: <b>{', '.join(str(x[4]) for x in r1)}</b>.</p>"

# ---------------------------------------------------------------- n2: NAND latch sequence
SEQ2 = [(0, 1), (1, 1), (1, 0), (1, 1), (0, 0)]
q, r2 = 0, []
for i, (sb, rb) in enumerate(SEQ2):
    res = S.nand_latch(sb, rb, q)
    if res == (1, 1):
        r2.append((i + 1, sb, rb, q, f"1 (Q = {QB} = 1)", "invalid"))
        continue
    nq = res[0]
    r2.append((i + 1, sb, rb, q, nq, kind_of(q, nq)))
    q = nq
assert [x[5] for x in r2] == ["set", "hold", "reset", "hold", "invalid"]
_h2 = ["Step", B("!S"), B("!R"), "Q before", "Q after", "Action"]
_t2e = tbl(_h2, [(a, b, c, d, f"<b>{e}</b>", STATE_EN[k]) for a, b, c, d, e, k in r2])
_t2g = tbl(["Step", B("!S"), B("!R"), "પહેલાં Q", "પછી Q", "Action"], [(a, b, c, d, f"<b>{e}</b>", STATE_GU[k]) for a, b, c, d, e, k in r2])
A2E = (f"<p>Inputs are active LOW: {B('!S')} = 0 sets, {B('!R')} = 0 resets, both 1 hold, both 0 invalid. Initially Q = 0.</p>{_t2e}"
       "<p>Step 5 is the forbidden input: both outputs become 1, and the state after the inputs return to 1 cannot be predicted.</p>")
A2G = (f"<p>Inputs active LOW છે: {B('!S')} = 0 set કરે, {B('!R')} = 0 reset કરે, બંને 1 hold, બંને 0 invalid. શરૂઆતમાં Q = 0.</p>{_t2g}"
       "<p>Step 5 forbidden input છે: બંને outputs 1 થાય છે, અને inputs પાછા 1 થયા પછીની state નક્કી કરી શકાતી નથી.</p>")

# ---------------------------------------------------------------- n3: clocked SR sequence (gate-level)
SEQ3 = [(1, 1, 0), (0, 0, 1), (1, 0, 0), (1, 0, 1), (0, 1, 0), (1, 1, 0)]
q, r3 = 0, []
for i, (clk, s, r) in enumerate(SEQ3):
    nq = S.clocked_sr(s, r, clk, q)[0]
    k = kind_of(q, nq)
    note_en = STATE_EN[k] + (" (CLK = 0)" if clk == 0 else "")
    note_gu = STATE_GU[k] + (" (CLK = 0)" if clk == 0 else "")
    r3.append((i + 1, clk, s, r, q, nq, note_en, note_gu))
    q = nq
assert [x[5] for x in r3] == [1, 1, 1, 0, 0, 1]
_t3e = tbl(["Step", "CLK", "S", "R", "Q<sub>n</sub>", "Q<sub>n+1</sub>", "Action"], [(a, b, c, d, e, f"<b>{f}</b>", g) for a, b, c, d, e, f, g, _ in r3])
_t3g = tbl(["Step", "CLK", "S", "R", "Q<sub>n</sub>", "Q<sub>n+1</sub>", "Action"], [(a, b, c, d, e, f"<b>{f}</b>", h) for a, b, c, d, e, f, _, h in r3])
A3E = f"<p>When CLK = 0 the flip-flop ignores S and R. When CLK = 1 it follows the SR table. Initially Q = 0.</p>{_t3e}<p>Note step 2 and step 5: the inputs ask for reset / set, but CLK = 0, so Q does not change.</p>"
A3G = f"<p>CLK = 0 હોય ત્યારે flip-flop S અને R ને અવગણે છે. CLK = 1 હોય ત્યારે SR table મુજબ ચાલે છે. શરૂઆતમાં Q = 0.</p>{_t3g}<p>Step 2 અને step 5 જુઓ: inputs reset / set માગે છે, પણ CLK = 0 હોવાથી Q બદલાતો નથી.</p>"

# ---------------------------------------------------------------- n4, n5, n9: characteristic equations by K-map
def char_kmap(kind, names, extra_en="", extra_gu=""):
    rows_ = S.char_rows(kind)
    n = len(names)
    ones = [i for i, r in enumerate(rows_) if r[-1] == 1]
    dc = [i for i, r in enumerate(rows_) if r[-1] == "X"]
    en, gu, g, ans = solve(n, ones, dc, names=names, out="Q+")
    head = list(names[:-1]) + ["Q<sub>n</sub>", "Q<sub>n+1</sub>"]
    ct = tbl(head, [(*r[:-1], f"<b>{r[-1]}</b>") for r in rows_])
    pre_en = f"<p><b>Characteristic table</b> (Q = Q<sub>n</sub>, Q+ = Q<sub>n+1</sub>):</p>{ct}"
    pre_gu = f"<p><b>Characteristic table</b> (Q = Q<sub>n</sub>, Q+ = Q<sub>n+1</sub>):</p>{ct}"
    return pre_en + en + extra_en, pre_gu + gu + extra_gu, ans


A4E, A4G, ans4 = char_kmap("SR", "SRQ", "<p>So <b>Q<sub>n+1</sub> = S + " + B("!R") + "Q<sub>n</sub></b>, with the condition SR = 0 (S = R = 1 is used only as a don't-care).</p>",
                           "<p>તેથી <b>Q<sub>n+1</sub> = S + " + B("!R") + "Q<sub>n</sub></b>, શરત SR = 0 (S = R = 1 માત્ર don't-care તરીકે).</p>")
assert set(ans4.split(" + ")) == {"S", "!RQ"}
A5E, A5G, ans5 = char_kmap("JK", "JKQ", f"<p>So <b>Q<sub>n+1</sub> = J{QNB} + {B('!K')}Q<sub>n</sub></b>.</p>", f"<p>તેથી <b>Q<sub>n+1</sub> = J{QNB} + {B('!K')}Q<sub>n</sub></b>.</p>")
assert set(ans5.split(" + ")) == {"J!Q", "!KQ"}
_A9E, _A9G, ans9 = char_kmap("T", "TQ", f"<p>T{QNB} + {B('!T')}Q<sub>n</sub> = <b>T ⊕ Q<sub>n</sub></b>.</p>", f"<p>T{QNB} + {B('!T')}Q<sub>n</sub> = <b>T ⊕ Q<sub>n</sub></b>.</p>")
assert set(ans9.split(" + ")) == {"T!Q", "!TQ"}


# ---------------------------------------------------------------- n6, n7, n8: clocked sequences
def seq_table(kind, inputs, names, q0=0):
    out = S.run(kind, inputs, q0)
    rows_e, rows_g = [], []
    for i, (inp, q, nq) in enumerate(out):
        if kind in ("JK", "T") and nq != q and (kind == "T" or inp == (1, 1)):
            k = "toggle"
        else:
            k = kind_of(q, nq)
        rows_e.append((i + 1, *inp, q, f"<b>{nq}</b>", STATE_EN[k]))
        rows_g.append((i + 1, *inp, q, f"<b>{nq}</b>", STATE_GU[k]))
    head = ["Clock edge", *names, "Q<sub>n</sub>", "Q<sub>n+1</sub>", "Action"]
    return tbl(head, rows_e), tbl(head, rows_g), [x[2] for x in out]


SEQ6 = [(0, 0), (1, 0), (1, 1), (1, 1), (0, 1), (1, 1)]
_t6e, _t6g, q6 = seq_table("JK", SEQ6, ["J", "K"])
assert q6 == [0, 1, 0, 1, 0, 1]
A6E = f"<p>Use the JK table at each clock edge; J = K = 1 toggles. Initially Q = 0.</p>{_t6e}<p>Q after each edge: <b>{', '.join(map(str, q6))}</b>.</p>"
A6G = f"<p>દરેક clock edge વખતે JK table વાપરો; J = K = 1 toggle કરે. શરૂઆતમાં Q = 0.</p>{_t6g}<p>દરેક edge પછી Q: <b>{', '.join(map(str, q6))}</b>.</p>"

SEQ7 = [1, 0, 0, 1, 1, 0]
_t7e, _t7g, q7 = seq_table("D", SEQ7, ["D"])
assert q7 == SEQ7
A7E = f"<p>For a D flip-flop Q<sub>n+1</sub> = D at each edge. Initially Q = 0.</p>{_t7e}<p>Q simply copies D at each clock edge: <b>{', '.join(map(str, q7))}</b>.</p>"
A7G = f"<p>D flip-flop માટે દરેક edge વખતે Q<sub>n+1</sub> = D. શરૂઆતમાં Q = 0.</p>{_t7g}<p>Q દરેક clock edge વખતે D ની નકલ કરે છે: <b>{', '.join(map(str, q7))}</b>.</p>"

SEQ8 = [1, 1, 0, 1, 0, 1]
_t8e, _t8g, q8 = seq_table("T", SEQ8, ["T"])
assert q8 == [1, 0, 0, 1, 1, 0]
A8E = f"<p>T = 1 toggles Q, T = 0 holds it. Initially Q = 0.</p>{_t8e}<p>Q after each edge: <b>{', '.join(map(str, q8))}</b>.</p>"
A8G = f"<p>T = 1 Q ને toggle કરે, T = 0 hold કરે. શરૂઆતમાં Q = 0.</p>{_t8g}<p>દરેક edge પછી Q: <b>{', '.join(map(str, q8))}</b>.</p>"

# ---------------------------------------------------------------- n9: T frequency division + equation
F = 8
_div = [(f"FF{i + 1}", f"{F / 2 ** (i + 1):g} kHz") for i in range(3)]
assert _div[-1][1] == "1 kHz"
A9E = (f"<p><b>(a)</b> With T = 1, Q toggles at every clock edge, so one Q cycle takes two clock cycles: f<sub>Q</sub> = {F} / 2 = <b>4 kHz</b>.</p>"
       f"<p><b>(b)</b> Three T flip-flops in cascade (each Q drives the next clock):</p>" + tbl(["Stage", "Output frequency"], _div)
       + f"<p>f = {F} kHz / 2<sup>3</sup> = <b>1 kHz</b>.</p><p><b>(c)</b> Characteristic equation by K-map:</p>" + _A9E)
A9G = (f"<p><b>(a)</b> T = 1 હોય ત્યારે Q દરેક clock edge વખતે toggle થાય, તેથી Q ની એક cycle બે clock cycles લે: f<sub>Q</sub> = {F} / 2 = <b>4 kHz</b>.</p>"
       f"<p><b>(b)</b> Cascade માં ત્રણ T flip-flops (દરેક Q પછીના FF ને clock આપે):</p>" + tbl(["Stage", "Output frequency"], _div)
       + f"<p>f = {F} kHz / 2<sup>3</sup> = <b>1 kHz</b>.</p><p><b>(c)</b> K-map વડે characteristic equation:</p>" + _A9G)

# ---------------------------------------------------------------- n10: D timing diagram
clk = [v for v in S.clock(6) for _ in (0, 1)]
ed = S.rising(clk)
q10 = S.sample("D", clk, D_IN)
samples = [D_IN[e] for e in ed]
assert [q10[e] for e in ed] == samples
_t10 = tbl(["Rising edge", "1", "2", "3", "4", "5", "6"], [["D at edge", *samples], ["Q after edge", *[f"<b>{v}</b>" for v in samples]]])
A10E = (f"<p>Mark each rising edge of the clock (dashed lines in the diagram) and read D at that instant; Q takes that value and holds it until the next rising edge.</p>{_t10}"
        "<p>Changes in D between edges (e.g. the short changes just after an edge) do not affect Q.</p>")
A10G = (f"<p>Clock ની દરેક rising edge દર્શાવો (diagram માં dashed lines) અને તે ક્ષણે D વાંચો; Q તે કિંમત લે છે અને પછીની rising edge સુધી જાળવી રાખે છે.</p>{_t10}"
        "<p>Edges વચ્ચે D માં થતા ફેરફારો (દા.ત. edge પછી તરત થતા નાના ફેરફારો) Q ને અસર કરતા નથી.</p>")

# ---------------------------------------------------------------- n11: JK -> D and JK -> T
r11 = []
for d in (0, 1):
    for q in (0, 1):
        j, k = d, 1 - d
        nq = S.NEXT["JK"](j, k, q)
        assert nq == d
        r11.append((d, q, j, k, f"<b>{nq}</b>"))
r11t = []
for t in (0, 1):
    for q in (0, 1):
        nq = S.NEXT["JK"](t, t, q)
        assert nq == t ^ q
        r11t.append((t, q, t, t, f"<b>{nq}</b>"))
_t11a = tbl(["D", "Q<sub>n</sub>", "J = D", "K = " + B("!D"), "Q<sub>n+1</sub>"], r11)
_t11b = tbl(["T", "Q<sub>n</sub>", "J = T", "K = T", "Q<sub>n+1</sub>"], r11t)
A11E = (f"<p><b>JK to D:</b> connect J = D and K = {B('!D')} (one NOT gate).</p>{_t11a}<p>Q<sub>n+1</sub> = D in every row ✔</p>"
        f"<p><b>JK to T:</b> connect J and K together to T.</p>{_t11b}<p>Q<sub>n+1</sub> = T ⊕ Q<sub>n</sub> in every row ✔</p>")
A11G = (f"<p><b>JK થી D:</b> J = D અને K = {B('!D')} જોડો (એક NOT gate).</p>{_t11a}<p>દરેક row માં Q<sub>n+1</sub> = D ✔</p>"
        f"<p><b>JK થી T:</b> J અને K ને સાથે T સાથે જોડો.</p>{_t11b}<p>દરેક row માં Q<sub>n+1</sub> = T ⊕ Q<sub>n</sub> ✔</p>")

# ---------------------------------------------------------------- n12: number of flip-flops
import math
_r12 = [("Store one byte (8 bits)", "8 bits", 8), ("Number of states with 4 FFs", "2<sup>4</sup>", 16), ("Count 0 to 9 (10 states)", "2<sup>n</sup> ≥ 10", math.ceil(math.log2(10))),
        ("Count 100 states", "2<sup>n</sup> ≥ 100", math.ceil(math.log2(100)))]
assert [x[2] for x in _r12] == [8, 16, 4, 7]
A12E = ("<p>One flip-flop stores 1 bit; n flip-flops have 2<sup>n</sup> states. To get N states choose the smallest n with 2<sup>n</sup> ≥ N.</p>"
        + tbl(["Requirement", "Rule", "Answer"], [(a, b, f"<b>{c}</b>") for a, b, c in _r12])
        + "<p>So: (a) 8 FFs, (b) 16 states, (c) 4 FFs (2<sup>3</sup> = 8 is too few), (d) 7 FFs (2<sup>7</sup> = 128 ≥ 100).</p>")
A12G = ("<p>એક flip-flop 1 bit store કરે; n flip-flops ની 2<sup>n</sup> states હોય. N states માટે 2<sup>n</sup> ≥ N થાય તેવો સૌથી નાનો n લો.</p>"
        + tbl(["જરૂરિયાત", "નિયમ", "જવાબ"], [(a, b, f"<b>{c}</b>") for a, b, c in _r12])
        + "<p>તેથી: (a) 8 FFs, (b) 16 states, (c) 4 FFs (2<sup>3</sup> = 8 ઓછા પડે), (d) 7 FFs (2<sup>7</sup> = 128 ≥ 100).</p>")

_seq = lambda xs: ", ".join("(" + ", ".join(map(str, x)) + ")" for x in xs)
NUMERICALS = [
    N("de5n1", f"A NOR SR latch starts with Q = 0. Find Q for the input sequence (S, R) = {_seq(SEQ1)}.",
      f"NOR SR latch Q = 0 થી શરૂ થાય છે. Input ક્રમ (S, R) = {_seq(SEQ1)} માટે Q શોધો.", A1E, A1G),
    N("de5n2", f"A NAND SR latch starts with Q = 0. Find Q for ({B('!S')}, {B('!R')}) = {_seq(SEQ2)}.",
      f"NAND SR latch Q = 0 થી શરૂ થાય છે. ({B('!S')}, {B('!R')}) = {_seq(SEQ2)} માટે Q શોધો.", A2E, A2G),
    N("de5n3", f"A clocked SR flip-flop starts with Q = 0. Find Q for (CLK, S, R) = {_seq(SEQ3)}.",
      f"Clocked SR flip-flop Q = 0 થી શરૂ થાય છે. (CLK, S, R) = {_seq(SEQ3)} માટે Q શોધો.", A3E, A3G),
    N("de5n4", "Derive the characteristic equation of the SR flip-flop using a K-map.", "K-map વડે SR flip-flop નું characteristic equation મેળવો.", A4E, A4G),
    N("de5n5", "Derive the characteristic equation of the JK flip-flop using a K-map.", "K-map વડે JK flip-flop નું characteristic equation મેળવો.", A5E, A5G),
    N("de5n6", f"A JK flip-flop starts with Q = 0. Find Q after each clock edge for (J, K) = {_seq(SEQ6)}.",
      f"JK flip-flop Q = 0 થી શરૂ થાય છે. (J, K) = {_seq(SEQ6)} માટે દરેક clock edge પછી Q શોધો.", A6E, A6G),
    N("de5n7", f"A D flip-flop starts with Q = 0. Find Q after each clock edge for D = {', '.join(map(str, SEQ7))}.",
      f"D flip-flop Q = 0 થી શરૂ થાય છે. D = {', '.join(map(str, SEQ7))} માટે દરેક clock edge પછી Q શોધો.", A7E, A7G),
    N("de5n8", f"A T flip-flop starts with Q = 0. Find Q after each clock edge for T = {', '.join(map(str, SEQ8))}.",
      f"T flip-flop Q = 0 થી શરૂ થાય છે. T = {', '.join(map(str, SEQ8))} માટે દરેક clock edge પછી Q શોધો.", A8E, A8G),
    N("de5n9", f"(a) A {F} kHz clock is applied to a T flip-flop with T = 1. Find the output frequency. (b) Find it for three such flip-flops in cascade. (c) Derive Qn+1 of the T flip-flop.",
      f"(a) T = 1 વાળા T flip-flop ને {F} kHz clock અપાય છે. Output frequency શોધો. (b) આવા ત્રણ flip-flops cascade માં હોય તો શોધો. (c) T flip-flop નું Qn+1 મેળવો.", A9E, A9G),
    N("de5n10", "For the D flip-flop timing diagram (topic 5.2.8), find Q after each rising edge.",
      "D flip-flop ના timing diagram (topic 5.2.8) માટે દરેક rising edge પછી Q શોધો.", A10E, A10G),
    N("de5n11", "Convert a JK flip-flop into (a) a D flip-flop and (b) a T flip-flop. Verify with tables.",
      "JK flip-flop ને (a) D flip-flop અને (b) T flip-flop માં ફેરવો. Tables વડે ચકાસો.", A11E, A11G),
    N("de5n12", "How many flip-flops are needed to (a) store one byte, (c) count 0 to 9, (d) count 100 states? (b) How many states do 4 flip-flops have?",
      "(a) એક byte store કરવા, (c) 0 થી 9 ગણવા, (d) 100 states ગણવા કેટલા flip-flops જોઈએ? (b) 4 flip-flops ની કેટલી states હોય?", A12E, A12G),
]

EQUATIONS = [
    {"title": {"en": "Characteristic Equations", "gu": "Characteristic Equations"}, "items": [
        E("SR flip-flop", "SR flip-flop", "Q<sub>n+1</sub> = S + " + B("!R") + "Q<sub>n</sub>", "Condition SR = 0", "શરત SR = 0"),
        E("JK flip-flop", "JK flip-flop", f"Q<sub>n+1</sub> = J{QNB} + {B('!K')}Q<sub>n</sub>", "J = K = 1 toggles", "J = K = 1 toggle"),
        E("D flip-flop", "D flip-flop", "Q<sub>n+1</sub> = D", "Output follows D at the clock edge", "Clock edge વખતે output D ને અનુસરે"),
        E("T flip-flop", "T flip-flop", "Q<sub>n+1</sub> = T ⊕ Q<sub>n</sub>", "T = 1 toggles", "T = 1 toggle"),
    ]},
    {"title": {"en": "Conversions and Counting", "gu": "Conversions અને ગણતરી"}, "items": [
        E("SR / JK to D", "SR / JK થી D", "S = J = D, &nbsp; R = K = " + B("!D"), "", ""),
        E("JK to T", "JK થી T", "J = K = T", "", ""),
        E("Clock frequency", "Clock frequency", "f = 1 / T", "T = clock period", "T = clock period"),
        E("Toggle frequency division", "Toggle frequency division", "f<sub>out</sub> = f<sub>CLK</sub> / 2<sup>n</sup>", "n = toggling FFs in cascade", "n = cascade માં toggling FFs"),
        E("Number of states", "States ની સંખ્યા", "States = 2<sup>n</sup>", "n = number of flip-flops", "n = flip-flops ની સંખ્યા"),
    ]},
]

VIVA = [
    {"title": {"en": "Sequential Circuits", "gu": "Sequential Circuits"}, "items": [
        V("What is a sequential circuit?", "Sequential circuit શું છે?", "A circuit whose output depends on present inputs and the past state; it has memory.", "જેનો output હાલના inputs અને અગાઉની state પર આધાર રાખે તેવો circuit; તેમાં memory હોય છે."),
        V("Give one main difference between combinational and sequential circuits.", "Combinational અને sequential circuits વચ્ચે એક મુખ્ય તફાવત આપો.", "Sequential circuits have memory and feedback; combinational circuits do not.", "Sequential circuits માં memory અને feedback હોય છે; combinational માં નહીં."),
        V("What is a clock?", "Clock શું છે?", "A periodic square wave that controls when a synchronous circuit changes state.", "Synchronous circuit ક્યારે state બદલે તે નક્કી કરતો periodic square wave."),
        V("What is edge triggering?", "Edge triggering શું છે?", "Responding only at the rising or falling edge of the clock.", "Clock ની rising કે falling edge વખતે જ પ્રતિભાવ આપવો."),
        V("Differentiate synchronous and asynchronous circuits.", "Synchronous અને asynchronous circuits નો તફાવત આપો.", "Synchronous: all FFs share a common clock; asynchronous: no common clock.", "Synchronous: બધા FFs નો common clock; asynchronous: common clock નથી."),
    ]},
    {"title": {"en": "Flip-Flops", "gu": "Flip-Flops"}, "items": [
        V("What is a flip-flop?", "Flip-flop શું છે?", "A bistable 1-bit memory element with outputs Q and Q̄.", "Q અને Q̄ outputs ધરાવતો bistable 1-bit memory element."),
        V("Difference between a latch and a flip-flop?", "Latch અને flip-flop વચ્ચે તફાવત?", "A latch is level triggered (or unclocked); a flip-flop is edge triggered.", "Latch level triggered (અથવા clock વગરનો) છે; flip-flop edge triggered છે."),
        V("What is the invalid state of an SR flip-flop?", "SR flip-flop ની invalid state કઈ છે?", "S = R = 1 (both outputs become equal).", "S = R = 1 (બંને outputs સરખા થઈ જાય)."),
        V("How does a JK flip-flop remove the invalid state?", "JK flip-flop invalid state કેવી રીતે દૂર કરે?", "By feeding Q and Q̄ back to the input gates; J = K = 1 then toggles.", "Q અને Q̄ ને input gates માં feedback આપીને; ત્યારે J = K = 1 toggle કરે."),
        V("What is the race-around condition?", "Race-around condition શું છે?", "Repeated toggling of a JK FF when J = K = 1 and the clock pulse is longer than the propagation delay.", "J = K = 1 અને clock pulse propagation delay કરતાં લાંબો હોય ત્યારે JK FF નું વારંવાર toggle થવું."),
        V("How is race-around avoided?", "Race-around કેવી રીતે ટાળાય?", "Edge triggering or a master–slave JK flip-flop.", "Edge triggering અથવા master–slave JK flip-flop."),
        V("Why is the D flip-flop called a delay flip-flop?", "D flip-flop ને delay flip-flop કેમ કહે છે?", "The input appears at the output after one clock period.", "Input એક clock period પછી output પર દેખાય છે."),
        V("How is a D flip-flop made from an SR flip-flop?", "SR flip-flop માંથી D flip-flop કેવી રીતે બને?", "S = D and R = D̄ using a NOT gate.", "NOT gate વડે S = D અને R = D̄."),
        V("How is a T flip-flop made from a JK flip-flop?", "JK flip-flop માંથી T flip-flop કેવી રીતે બને?", "By connecting J and K together (J = K = T).", "J અને K ને સાથે જોડીને (J = K = T)."),
        V("What does a T flip-flop do when T = 1?", "T = 1 હોય ત્યારે T flip-flop શું કરે?", "Toggles at every clock edge; divides frequency by 2.", "દરેક clock edge વખતે toggle થાય; frequency ને 2 વડે ભાગે."),
        V("Which flip-flop is called universal?", "કયો flip-flop universal કહેવાય?", "The JK flip-flop.", "JK flip-flop."),
        V("Write the characteristic equation of a JK flip-flop.", "JK flip-flop નું characteristic equation લખો.", "Qn+1 = JQ̄n + K̄Qn.", "Qn+1 = JQ̄n + K̄Qn."),
        V("What do Preset and Clear inputs do?", "Preset અને Clear inputs શું કરે?", "Force Q = 1 or Q = 0 immediately, independent of the clock.", "Clock થી સ્વતંત્ર રીતે તરત જ Q = 1 કે Q = 0 કરે."),
        V("Give two applications of flip-flops.", "Flip-flops ના બે ઉપયોગ આપો.", "Registers and counters (also memory, frequency division).", "Registers અને counters (memory, frequency division પણ)."),
        V("Name an IC containing D flip-flops.", "D flip-flops ધરાવતો IC જણાવો.", "7474 (dual positive-edge D flip-flop).", "7474 (dual positive-edge D flip-flop)."),
    ]},
]

EXAM_QS = [
    X("Define sequential circuit. Draw its block diagram.", "Sequential circuit ની વ્યાખ્યા આપો. તેનો block diagram દોરો.", 3),
    X("Differentiate between combinational and sequential circuits.", "Combinational અને sequential circuits વચ્ચે તફાવત આપો.", 4),
    X("What is a flip-flop? List its types.", "Flip-flop શું છે? તેના પ્રકારો જણાવો.", 3),
    X("Explain the SR latch using NOR gates with truth table.", "Truth table સાથે NOR gates વડે SR latch સમજાવો.", 4),
    X("Explain the clocked SR flip-flop with logic diagram and truth table.", "Logic diagram અને truth table સાથે clocked SR flip-flop સમજાવો.", 4),
    X("Explain the JK flip-flop with logic diagram and truth table.", "Logic diagram અને truth table સાથે JK flip-flop સમજાવો.", 7),
    X("What is the race-around condition? How is it eliminated?", "Race-around condition શું છે? તેને કેવી રીતે દૂર કરાય?", 3),
    X("Explain the D flip-flop with diagram and truth table.", "Diagram અને truth table સાથે D flip-flop સમજાવો.", 4),
    X("Explain the T flip-flop with diagram and truth table.", "Diagram અને truth table સાથે T flip-flop સમજાવો.", 4),
    X("Compare SR, JK, D and T flip-flops.", "SR, JK, D અને T flip-flops ની સરખામણી કરો.", 4),
    X("Explain level triggering and edge triggering.", "Level triggering અને edge triggering સમજાવો.", 3),
    X("Convert a JK flip-flop into D and T flip-flops.", "JK flip-flop ને D અને T flip-flops માં ફેરવો.", 4),
    X("Draw the timing diagram of a positive-edge triggered D flip-flop.", "Positive-edge triggered D flip-flop નો timing diagram દોરો.", 3),
    X("Give applications of flip-flops.", "Flip-flops ના ઉપયોગો આપો.", 3),
]
