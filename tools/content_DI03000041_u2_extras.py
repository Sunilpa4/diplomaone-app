"""Fundamentals of Operating System (DI03000041) - Unit 2 extras: numericals (all simulated by os_sched.py), equations, viva, exam."""
from content_DI03000011_u1_extras import N, E, V, X
import os_sched as S

NAMES4 = ["P0", "P1", "P2", "P3"]
PA = S.P(NAMES4, [0, 1, 2, 3], [5, 3, 8, 6])            # Practical 2(a)
PB = S.P(NAMES4, [3, 0, 4, 5], [5, 4, 2, 4])            # Practical 2(b)
PRI = S.P(["P1", "P2", "P3", "P4", "P5"], [0] * 5, [10, 1, 2, 1, 5], [3, 1, 4, 5, 2])
PRI2 = S.P(["P1", "P2", "P3", "P4", "P5"], [0, 1, 2, 3, 4], [4, 3, 2, 5, 1], [3, 1, 4, 2, 1])
CONV = S.P(["P1", "P2", "P3"], [0, 0, 0], [24, 3, 3])
SR = S.P(["P1", "P2", "P3", "P4"], [0, 1, 2, 3], [8, 4, 9, 5])

RULE = {
    "fcfs": ("<p><b>Rule:</b> the CPU is given to processes in the order of their <b>arrival</b>; a running process is never pre-empted.</p>",
             "<p><b>નિયમ:</b> CPU processes ને તેમના <b>arrival</b> ના ક્રમમાં મળે છે; ચાલતી process ને ક્યારેય pre-empt કરાતી નથી.</p>"),
    "sjf": ("<p><b>Rule:</b> whenever the CPU becomes free, choose the <b>arrived</b> process with the <b>smallest burst time</b> (tie → FCFS). Non-preemptive: it runs to completion.</p>",
            "<p><b>નિયમ:</b> CPU મુક્ત થાય ત્યારે આવી ગયેલી processes માંથી <b>સૌથી નાના burst time</b> વાળી પસંદ કરો (સરખા હોય તો FCFS). Non-preemptive: તે પૂરી થાય ત્યાં સુધી ચાલે.</p>"),
    "srtf": ("<p><b>Rule (SRTF = preemptive SJF):</b> at every arrival, the process with the <b>shortest remaining time</b> gets the CPU; the running process can be pre-empted.</p>",
             "<p><b>નિયમ (SRTF = preemptive SJF):</b> દરેક arrival વખતે <b>સૌથી ઓછો remaining time</b> વાળી process ને CPU મળે; ચાલતી process pre-empt થઈ શકે.</p>"),
    "rr": ("<p><b>Rule:</b> each process runs for at most one <b>time quantum</b>, then goes to the tail of the ready queue. Convention used: a process arriving at the same moment a quantum expires enters the queue <b>before</b> the pre-empted process.</p>",
           "<p><b>નિયમ:</b> દરેક process વધુમાં વધુ એક <b>time quantum</b> ચાલે, પછી ready queue ના છેડે જાય. અહીં વપરાયેલી પ્રથા: quantum પૂરો થાય તે જ ક્ષણે આવતી process, pre-empt થયેલી process <b>પહેલાં</b> queue માં જાય.</p>"),
    "pri": ("<p><b>Rule:</b> when the CPU is free, choose the arrived process with the <b>highest priority</b> (smallest number; tie → FCFS). Non-preemptive.</p>",
            "<p><b>નિયમ:</b> CPU મુક્ત થાય ત્યારે આવી ગયેલી processes માંથી <b>સૌથી ઊંચી priority</b> (સૌથી નાની સંખ્યા; સરખી હોય તો FCFS) વાળી પસંદ કરો. Non-preemptive.</p>"),
}


def rr_trace_html(procs, q, gu=False):
    t = []
    S.rr(procs, q, t)
    hd = ["સમય", "ચાલે", "બાકી", "પછી ready queue"] if gu else ["Time", "Runs", "Remaining", "Ready queue after"]
    h = "<table><tr>" + "".join(f"<th>{x}</th>" for x in hd) + "</tr>"
    for a, b, n, rem, Q in t:
        h += f"<tr><td>{a}–{b}</td><td>{n}</td><td>{rem}</td><td>{', '.join(Q) or '—'}</td></tr>"
    return h + "</table>"


def sched(id_, procs, alg, q_en, q_gu, extra_en="", extra_gu="", quantum=None, pr=False):
    f = {"fcfs": S.fcfs, "sjf": S.sjf, "srtf": S.srtf, "pri": S.priority}.get(alg)
    segs, res = (S.rr(procs, quantum) if alg == "rr" else f(procs))
    r_en, r_gu = RULE[alg]
    tr_en = tr_gu = ""
    if alg == "rr":
        tr_en = f"<p><b>Ready-queue trace (q = {quantum}):</b></p>" + rr_trace_html(procs, quantum)
        tr_gu = f"<p><b>Ready-queue trace (q = {quantum}):</b></p>" + rr_trace_html(procs, quantum, True)
    giv = "<p><b>Given:</b></p>" + S.input_table(procs, pr)
    giv_gu = "<p><b>આપેલ:</b></p>" + S.input_table(procs, pr)
    en, gu = S.solve_html(procs, segs, res, extra_en, extra_gu, pr)
    return N(id_, q_en, q_gu, giv + r_en + tr_en + en, giv_gu + r_gu + tr_gu + gu), segs, res


def avg2(res):
    return S.fmt(S.avg(res, "tat")), S.fmt(S.avg(res, "wt"))


QA = ("Arrival times 0, 1, 2, 3 and burst times 5, 3, 8, 6 for P0, P1, P2, P3", "P0, P1, P2, P3 માટે arrival time 0, 1, 2, 3 અને burst time 5, 3, 8, 6")
QB = ("Arrival times 3, 0, 4, 5 and burst times 5, 4, 2, 4 for P0, P1, P2, P3", "P0, P1, P2, P3 માટે arrival time 3, 0, 4, 5 અને burst time 5, 4, 2, 4")
ASK = (" Draw the Gantt chart and find the average turnaround time and average waiting time.", " Gantt chart દોરો અને સરેરાશ turnaround time અને સરેરાશ waiting time શોધો.")

n1, s1, r1 = sched("os2n1", PA, "fcfs", "(Practical 2a) FCFS: " + QA[0] + "." + ASK[0], "(Practical 2a) FCFS: " + QA[1] + "." + ASK[1],
                   "<p>P0 arrives first (0) and runs 0–5; then P1, P2 and P3 in order of arrival.</p>", "<p>P0 પહેલી (0) આવે અને 0–5 ચાલે; પછી arrival ક્રમમાં P1, P2 અને P3.</p>")
n2, s2, r2 = sched("os2n2", PA, "sjf", "(Practical 2a) SJF (non-preemptive): " + QA[0] + "." + ASK[0], "(Practical 2a) SJF (non-preemptive): " + QA[1] + "." + ASK[1],
                   "<p>At 0 only P0 is present → P0 runs 0–5. At 5, P1 (3), P2 (8), P3 (6) are waiting → shortest P1 (5–8), then P3 (8–14), then P2 (14–22).</p>",
                   "<p>0 પર માત્ર P0 હાજર → P0 0–5 ચાલે. 5 પર P1 (3), P2 (8), P3 (6) રાહ જુએ છે → સૌથી નાનો P1 (5–8), પછી P3 (8–14), પછી P2 (14–22).</p>")
n3, s3, r3 = sched("os2n3", PA, "rr", "(Practical 2a) Round Robin with time quantum 2: " + QA[0] + "." + ASK[0],
                   "(Practical 2a) Time quantum 2 સાથે Round Robin: " + QA[1] + "." + ASK[1], quantum=2)
n4, s4, r4 = sched("os2n4", PB, "fcfs", "(Practical 2b) FCFS: " + QB[0] + "." + ASK[0], "(Practical 2b) FCFS: " + QB[1] + "." + ASK[1],
                   "<p>Order of arrival: P1 (0), P0 (3), P2 (4), P3 (5).</p>", "<p>Arrival નો ક્રમ: P1 (0), P0 (3), P2 (4), P3 (5).</p>")
n5, s5, r5 = sched("os2n5", PB, "sjf", "(Practical 2b) SJF (non-preemptive): " + QB[0] + "." + ASK[0], "(Practical 2b) SJF (non-preemptive): " + QB[1] + "." + ASK[1],
                   "<p>Only P1 is present at 0 → runs 0–4. At 4: P0 (5), P2 (2) → P2 (4–6). At 6: P0 (5), P3 (4) → P3 (6–10), then P0 (10–15).</p>",
                   "<p>0 પર માત્ર P1 → 0–4 ચાલે. 4 પર: P0 (5), P2 (2) → P2 (4–6). 6 પર: P0 (5), P3 (4) → P3 (6–10), પછી P0 (10–15).</p>")
n6, s6, r6 = sched("os2n6", PB, "rr", "(Practical 2b) Round Robin with time quantum 2: " + QB[0] + "." + ASK[0],
                   "(Practical 2b) Time quantum 2 સાથે Round Robin: " + QB[1] + "." + ASK[1],
                   "<p>P1 is alone from 0 to 4, so it gets two quanta one after another.</p>", "<p>0 થી 4 સુધી P1 એકલી છે, તેથી તેને સળંગ બે quantum મળે છે.</p>", quantum=2)
n7, s7, r7 = sched("os2n7", PRI, "pri", "Using non-preemptive priority scheduling, find the average waiting time and turnaround time. All processes arrive at time 0. Burst times: P1 = 10, P2 = 1, P3 = 2, P4 = 1, P5 = 5; priorities 3, 1, 4, 5, 2 (smaller number = higher priority).",
                   "Non-preemptive priority scheduling વાપરી સરેરાશ waiting time અને turnaround time શોધો. બધી processes 0 પર આવે છે. Burst time: P1 = 10, P2 = 1, P3 = 2, P4 = 1, P5 = 5; priorities 3, 1, 4, 5, 2 (નાની સંખ્યા = ઊંચી priority).",
                   "<p>All arrive together, so order by priority: P2 (1), P5 (2), P1 (3), P3 (4), P4 (5).</p>", "<p>બધી સાથે આવે છે, તેથી priority ક્રમ: P2 (1), P5 (2), P1 (3), P3 (4), P4 (5).</p>", pr=True)
n8, s8, r8 = sched("os2n8", PRI2, "pri", "Non-preemptive priority scheduling with arrival times: P1 (AT 0, BT 4, priority 3), P2 (1, 3, 1), P3 (2, 2, 4), P4 (3, 5, 2), P5 (4, 1, 1). Smaller number = higher priority. Draw the Gantt chart and find average TAT and WT.",
                   "Arrival time સાથે non-preemptive priority scheduling: P1 (AT 0, BT 4, priority 3), P2 (1, 3, 1), P3 (2, 2, 4), P4 (3, 5, 2), P5 (4, 1, 1). નાની સંખ્યા = ઊંચી priority. Gantt chart દોરો અને સરેરાશ TAT અને WT શોધો.",
                   "<p>P1 is alone at 0 and runs 0–4 (no pre-emption). At 4 all others have arrived: P2 and P5 both have priority 1 → tie broken by arrival, so P2 (4–7), then P5 (7–8), P4 (8–13), P3 (13–15).</p>",
                   "<p>0 પર P1 એકલી છે અને 0–4 ચાલે (pre-emption નહીં). 4 પર બાકીની બધી આવી ગઈ: P2 અને P5 બંનેની priority 1 → arrival થી tie તોડો, તેથી P2 (4–7), પછી P5 (7–8), P4 (8–13), P3 (13–15).</p>", pr=True)

# n9: convoy effect, two orders
_c1s, _c1r = S.fcfs(CONV)
CONV2 = S.P(["P2", "P3", "P1"], [0, 0, 0], [3, 3, 24])
_c2s, _c2r = S.fcfs(CONV2)
assert S.avg(_c1r, "wt") == 17 and S.avg(_c2r, "wt") == 3
n9 = N("os2n9", "Processes P1, P2, P3 with burst times 24, 3, 3 ms arrive at time 0. Find the average waiting time under FCFS if they arrive in the order (i) P1, P2, P3 (ii) P2, P3, P1. What does this show?",
       "Burst time 24, 3, 3 ms વાળી processes P1, P2, P3 સમય 0 પર આવે છે. FCFS માં સરેરાશ waiting time શોધો જો ક્રમ (i) P1, P2, P3 (ii) P2, P3, P1 હોય. આ શું દર્શાવે છે?",
       f"<p><b>(i) Order P1, P2, P3</b></p>{S.gantt_html(_c1s)}<p>WT: P1 = 0, P2 = 24, P3 = 27 → average = (0 + 24 + 27)/3 = <b>17 ms</b></p>"
       f"<p><b>(ii) Order P2, P3, P1</b></p>{S.gantt_html(_c2s)}<p>WT: P2 = 0, P3 = 3, P1 = 6 → average = (0 + 3 + 6)/3 = <b>3 ms</b></p>"
       "<p><b>Conclusion:</b> FCFS waiting time depends heavily on the order. Short processes stuck behind one long process wait a lot: this is the <b>convoy effect</b>.</p>",
       f"<p><b>(i) ક્રમ P1, P2, P3</b></p>{S.gantt_html(_c1s)}<p>WT: P1 = 0, P2 = 24, P3 = 27 → સરેરાશ = (0 + 24 + 27)/3 = <b>17 ms</b></p>"
       f"<p><b>(ii) ક્રમ P2, P3, P1</b></p>{S.gantt_html(_c2s)}<p>WT: P2 = 0, P3 = 3, P1 = 6 → સરેરાશ = (0 + 3 + 6)/3 = <b>3 ms</b></p>"
       "<p><b>નિષ્કર્ષ:</b> FCFS નો waiting time ક્રમ પર ખૂબ આધાર રાખે છે. એક લાંબી process પાછળ ફસાયેલી નાની processes ઘણી રાહ જુએ છે: આને <b>convoy effect</b> કહે છે.</p>")

n10, s10, r10 = sched("os2n10", SR, "srtf", "Using preemptive SJF (SRTF), find the average waiting time: P1 (AT 0, BT 8), P2 (1, 4), P3 (2, 9), P4 (3, 5).",
                      "Preemptive SJF (SRTF) વાપરી સરેરાશ waiting time શોધો: P1 (AT 0, BT 8), P2 (1, 4), P3 (2, 9), P4 (3, 5).",
                      "<p>At 1, P2 (4) is shorter than P1's remaining 7 → P1 is pre-empted. P2 finishes at 5; then P4 (5) runs 5–10, P1 (7 left) 10–17, P3 17–26.</p>",
                      "<p>1 પર P2 (4) એ P1 ના બાકી 7 કરતાં નાનો → P1 pre-empt થાય. P2 5 પર પૂરી; પછી P4 (5) 5–10, P1 (7 બાકી) 10–17, P3 17–26.</p>")
assert S.avg(r10, "wt") == S.Fraction(13, 2)

n11, s11, r11 = sched("os2n11", CONV, "rr", "Round Robin with quantum 4 ms: P1, P2, P3 with burst times 24, 3, 3 ms, all arriving at 0. Find average waiting time and compare it with FCFS.",
                      "Quantum 4 ms સાથે Round Robin: burst time 24, 3, 3 ms વાળી P1, P2, P3, બધી 0 પર આવે. સરેરાશ waiting time શોધો અને FCFS સાથે સરખાવો.",
                      "<p>P2 and P3 finish within their first quantum; P1 then runs alone in quanta of 4 till 30.</p>",
                      "<p>P2 અને P3 પહેલા quantum માં જ પૂરી થાય; પછી P1 એકલી 4 ના quanta માં 30 સુધી ચાલે.</p>", quantum=4)
assert S.fmt(S.avg(r11, "wt")) == "5.67"
n11["a"]["en"] += "<p>FCFS (order P1, P2, P3) gave average WT = 17 ms; RR gives 5.67 ms because the short jobs need not wait behind P1.</p>"
n11["a"]["gu"] += "<p>FCFS (ક્રમ P1, P2, P3) માં સરેરાશ WT = 17 ms હતો; RR માં 5.67 ms, કારણ કે નાના jobs ને P1 પાછળ રાહ જોવી પડતી નથી.</p>"

# ---------------------------------------------------------------- Banker's algorithm
ALLOC = [[0, 1, 0], [2, 0, 0], [3, 0, 2], [2, 1, 1], [0, 0, 2]]
MAXM = [[7, 5, 3], [3, 2, 2], [9, 0, 2], [2, 2, 2], [4, 3, 3]]
AVAIL = [3, 3, 2]
need, seq, ok, steps = S.bankers(ALLOC, MAXM, AVAIL)
assert ok and seq == ["P1", "P3", "P4", "P0", "P2"]


def mat_table(rows_, gu=False):
    h = "<table><tr><th>Process</th><th>Allocation<br>A B C</th><th>Max<br>A B C</th><th>Need = Max − Alloc<br>A B C</th></tr>"
    for i, (a, m, n) in enumerate(rows_):
        h += f"<tr><td>P{i}</td><td>{' '.join(map(str, a))}</td><td>{' '.join(map(str, m))}</td><td>{' '.join(map(str, n))}</td></tr>"
    return h + "</table>"


def steps_table(st, gu=False, req="Need"):
    hd = ["Step", "Process", f"{req} ≤ Work?", "Work = Work + Alloc"]
    if gu:
        hd = ["પગલું", "Process", f"{req} ≤ Work?", "Work = Work + Alloc"]
    h = "<table><tr>" + "".join(f"<th>{x}</th>" for x in hd) + "</tr>"
    for i, (p_, nd, old, new) in enumerate(st):
        h += f"<tr><td>{i + 1}</td><td>{p_}</td><td>{S.vec(nd)} ≤ {S.vec(old)} ✓</td><td>{S.vec(new)}</td></tr>"
    return h + "</table>"


_mt = mat_table(list(zip(ALLOC, MAXM, need)))
n12 = N("os2n12", "Banker's algorithm: 5 processes P0–P4 and 3 resource types A (10 instances), B (5), C (7). Allocation: P0 (0 1 0), P1 (2 0 0), P2 (3 0 2), P3 (2 1 1), P4 (0 0 2). Max: P0 (7 5 3), P1 (3 2 2), P2 (9 0 2), P3 (2 2 2), P4 (4 3 3). Available = (3 3 2). Find the Need matrix and check whether the system is in a safe state.",
        "Banker's algorithm: 5 processes P0–P4 અને 3 resource types A (10 instances), B (5), C (7). Allocation: P0 (0 1 0), P1 (2 0 0), P2 (3 0 2), P3 (2 1 1), P4 (0 0 2). Max: P0 (7 5 3), P1 (3 2 2), P2 (9 0 2), P3 (2 2 2), P4 (4 3 3). Available = (3 3 2). Need matrix શોધો અને system safe state માં છે કે નહીં તે તપાસો.",
        f"<p><b>Step 1: Need = Max − Allocation</b></p>{_mt}"
        "<p><b>Step 2: Safety algorithm.</b> Work = Available = (3, 3, 2). Repeatedly find a process with Need ≤ Work; let it finish and release its allocation.</p>"
        f"{steps_table(steps)}<p>(P0 was checked first but Need (7, 4, 3) &gt; Work (3, 3, 2), so it had to wait.)</p>"
        f"<p>All processes can finish → the system is in a <b>SAFE state</b>.<br><b>Safe sequence: &lt;{', '.join(seq)}&gt;</b></p>"
        "<p>Check: final Work = (10, 5, 7) = total instances ✓</p>",
        f"<p><b>પગલું 1: Need = Max − Allocation</b></p>{_mt}"
        "<p><b>પગલું 2: Safety algorithm.</b> Work = Available = (3, 3, 2). વારંવાર Need ≤ Work હોય તેવી process શોધો; તેને પૂરી થવા દો અને તેનું allocation મુક્ત કરો.</p>"
        f"{steps_table(steps, True)}<p>(P0 પહેલાં તપાસી પણ Need (7, 4, 3) &gt; Work (3, 3, 2), તેથી તેણે રાહ જોવી પડી.)</p>"
        f"<p>બધી processes પૂરી થઈ શકે → system <b>SAFE state</b> માં છે.<br><b>Safe sequence: &lt;{', '.join(seq)}&gt;</b></p>"
        "<p>ચકાસણી: અંતિમ Work = (10, 5, 7) = કુલ instances ✓</p>")
assert steps[-1][3] == [10, 5, 7]

# n13: resource request by P1 (1 0 2)
REQ = [1, 0, 2]
A2 = [r[:] for r in ALLOC]; A2[1] = [A2[1][j] + REQ[j] for j in range(3)]
AV2 = [AVAIL[j] - REQ[j] for j in range(3)]
need2, seq2, ok2, steps2 = S.bankers(A2, MAXM, AV2)
assert ok2 and AV2 == [2, 3, 0] and seq2 == ["P1", "P3", "P4", "P0", "P2"]
n13 = N("os2n13", "In the system of the previous question, P1 requests (1, 0, 2). Can the request be granted immediately? Use the resource-request algorithm.",
        "આગળના પ્રશ્નની system માં P1 (1, 0, 2) માંગે છે. શું request તરત મંજૂર થઈ શકે? Resource-request algorithm વાપરો.",
        "<p><b>Step 1:</b> Request (1, 0, 2) ≤ Need<sub>P1</sub> (1, 2, 2) ✓ (P1 does not exceed its maximum claim).</p>"
        "<p><b>Step 2:</b> Request (1, 0, 2) ≤ Available (3, 3, 2) ✓ (resources are free).</p>"
        "<p><b>Step 3: Pretend to allocate:</b> Available = (3, 3, 2) − (1, 0, 2) = <b>(2, 3, 0)</b>; Allocation<sub>P1</sub> = (3, 0, 2); Need<sub>P1</sub> = (0, 2, 0).</p>"
        f"<p><b>Step 4: Safety check</b> with Work = (2, 3, 0):</p>{steps_table(steps2)}"
        f"<p>A safe sequence &lt;{', '.join(seq2)}&gt; exists, so the new state is safe → <b>the request is granted immediately</b>.</p>",
        "<p><b>પગલું 1:</b> Request (1, 0, 2) ≤ Need<sub>P1</sub> (1, 2, 2) ✓ (P1 તેના maximum claim થી વધુ માંગતી નથી).</p>"
        "<p><b>પગલું 2:</b> Request (1, 0, 2) ≤ Available (3, 3, 2) ✓ (resources મુક્ત છે).</p>"
        "<p><b>પગલું 3: Allocate કર્યું હોય તેમ માનો:</b> Available = (3, 3, 2) − (1, 0, 2) = <b>(2, 3, 0)</b>; Allocation<sub>P1</sub> = (3, 0, 2); Need<sub>P1</sub> = (0, 2, 0).</p>"
        f"<p><b>પગલું 4: Safety check</b>, Work = (2, 3, 0):</p>{steps_table(steps2, True)}"
        f"<p>Safe sequence &lt;{', '.join(seq2)}&gt; મળે છે, તેથી નવી state safe છે → <b>request તરત મંજૂર થાય છે</b>.</p>")

# n14: deadlock detection
DA = [[0, 1, 0], [2, 0, 0], [3, 0, 3], [2, 1, 1], [0, 0, 2]]
DR1 = [[0, 0, 0], [2, 0, 2], [0, 0, 0], [1, 0, 0], [0, 0, 2]]
DR2 = [[0, 0, 0], [2, 0, 2], [0, 0, 1], [1, 0, 0], [0, 0, 2]]
dseq1, dl1, dst1 = S.detect(DA, DR1, [0, 0, 0])
dseq2, dl2, dst2 = S.detect(DA, DR2, [0, 0, 0])
assert dl1 == [] and dl2 == ["P1", "P2", "P3", "P4"] and dseq2 == ["P0"]


def det_table(gu=False):
    h = "<table><tr><th>Process</th><th>Allocation<br>A B C</th><th>Request<br>A B C</th></tr>"
    for i in range(5):
        h += f"<tr><td>P{i}</td><td>{' '.join(map(str, DA[i]))}</td><td>{' '.join(map(str, DR1[i]))}</td></tr>"
    return h + "</table>"


n14 = N("os2n14", "Deadlock detection: 5 processes, resources A (7), B (2), C (6). Available = (0, 0, 0). Allocation and current Request are given in the table. (i) Is the system deadlocked? (ii) What happens if P2 makes one more request for C?",
        "Deadlock detection: 5 processes, resources A (7), B (2), C (6). Available = (0, 0, 0). Allocation અને હાલની Request table માં આપેલી છે. (i) System deadlock માં છે? (ii) P2 C નું એક વધુ instance માંગે તો શું થાય?",
        f"{det_table()}<p><b>(i)</b> Work = (0, 0, 0). Find a process whose Request ≤ Work, let it finish and add its allocation to Work:</p>{steps_table(dst1, req='Request')}"
        f"<p>All processes finish (sequence &lt;{', '.join(dseq1)}&gt;) → <b>no deadlock</b>.</p>"
        f"<p><b>(ii)</b> Request<sub>P2</sub> becomes (0, 0, 1). Only P0 can finish (Work becomes (0, 1, 0)). Now no other request ≤ (0, 1, 0).</p>"
        f"<p>→ <b>Deadlock</b> exists; deadlocked processes: <b>{', '.join(dl2)}</b>.</p>",
        f"{det_table()}<p><b>(i)</b> Work = (0, 0, 0). Request ≤ Work હોય તેવી process શોધો, તેને પૂરી થવા દો અને તેનું allocation Work માં ઉમેરો:</p>{steps_table(dst1, True, 'Request')}"
        f"<p>બધી processes પૂરી થાય છે (ક્રમ &lt;{', '.join(dseq1)}&gt;) → <b>deadlock નથી</b>.</p>"
        f"<p><b>(ii)</b> Request<sub>P2</sub> = (0, 0, 1) બને. માત્ર P0 પૂરી થઈ શકે (Work = (0, 1, 0)). હવે બીજી કોઈ request ≤ (0, 1, 0) નથી.</p>"
        f"<p>→ <b>Deadlock</b> છે; deadlocked processes: <b>{', '.join(dl2)}</b>.</p>")

NUMERICALS = [n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11, n12, n13, n14]
RESULTS = {"a_fcfs": avg2(r1), "a_sjf": avg2(r2), "a_rr": avg2(r3), "b_fcfs": avg2(r4), "b_sjf": avg2(r5), "b_rr": avg2(r6)}
assert RESULTS["a_fcfs"] == ("11.25", "5.75") and RESULTS["a_sjf"] == ("10.75", "5.25") and RESULTS["a_rr"] == ("15.25", "9.75")
assert RESULTS["b_fcfs"] == ("6.75", "3") and RESULTS["b_sjf"] == ("5.75", "2") and RESULTS["b_rr"] == ("7.25", "3.5")
assert avg2(r7) == ("12", "8.2") and avg2(r8) == ("7.4", "4.4")

EQUATIONS = [
    {"title": {"en": "CPU Scheduling Formulas", "gu": "CPU Scheduling સૂત્રો"}, "items": [
        E("Turnaround time", "Turnaround time", "TAT = CT − AT", "CT = completion time, AT = arrival time", "CT = completion time, AT = arrival time"),
        E("Waiting time", "Waiting time", "WT = TAT − BT", "BT = burst (execution) time", "BT = burst (execution) time"),
        E("Response time", "Response time", "RT = (time of first CPU allocation) − AT", "Equal to WT for non-preemptive algorithms", "Non-preemptive algorithms માં WT જેટલો"),
        E("Average TAT / WT", "સરેરાશ TAT / WT", "Avg = (sum of values of all processes) / n", "n = number of processes", "n = processes ની સંખ્યા"),
        E("Throughput", "Throughput", "Throughput = n / total time", "Processes completed per unit time", "એકમ સમયમાં પૂરી થતી processes"),
        E("CPU utilisation", "CPU utilisation", "CPU utilisation = (CPU busy time / total time) × 100%", "Idle time lowers utilisation", "Idle time utilisation ઘટાડે"),
    ]},
    {"title": {"en": "Banker's Algorithm", "gu": "Banker's Algorithm"}, "items": [
        E("Need matrix", "Need matrix", "Need[i][j] = Max[i][j] − Allocation[i][j]", "Remaining resources process i may still request", "Process i હજી માંગી શકે તેટલા બાકી resources"),
        E("Total instances", "કુલ instances", "Total = Available + Σ Allocation", "Used to find Available if total is given", "Total આપ્યું હોય તો Available શોધવા"),
        E("Safety step", "Safety step", "If Need<sub>i</sub> ≤ Work: Work = Work + Allocation<sub>i</sub>", "Start with Work = Available", "Work = Available થી શરૂ કરો"),
        E("Request check", "Request check", "Request<sub>i</sub> ≤ Need<sub>i</sub> and Request<sub>i</sub> ≤ Available", "Then pretend to allocate and run the safety check", "પછી allocate કર્યું માની safety check ચલાવો"),
    ]},
]

VIVA = [
    {"title": {"en": "Process and Threads", "gu": "Process અને Threads"}, "items": [
        V("What is a process?", "Process શું છે?", "A program in execution; an active entity with a PC, registers, stack, data and heap.", "Execution માં રહેલો program; PC, registers, stack, data અને heap વાળી active entity."),
        V("Difference between program and process?", "Program અને process વચ્ચે તફાવત?", "A program is passive (file on disk); a process is active (program loaded and running).", "Program passive છે (disk પરની file); process active છે (load થઈને ચાલતો program)."),
        V("Name the five process states.", "Process ની પાંચ states જણાવો.", "New, Ready, Running, Waiting (blocked) and Terminated.", "New, Ready, Running, Waiting (blocked) અને Terminated."),
        V("What is a PCB?", "PCB શું છે?", "Process Control Block: a data structure that stores all information about a process (PID, state, PC, registers, etc.).", "Process Control Block: process ની બધી માહિતી (PID, state, PC, registers વગેરે) સંગ્રહતું data structure."),
        V("Why is a thread called a light-weight process?", "Thread ને light-weight process કેમ કહે છે?", "It shares code, data and files with other threads, so creating and switching it is cheap.", "તે code, data અને files બીજા threads સાથે વહેંચે છે, તેથી તેને બનાવવું અને switch કરવું સસ્તું છે."),
    ]},
    {"title": {"en": "CPU Scheduling", "gu": "CPU Scheduling"}, "items": [
        V("List the CPU scheduling criteria.", "CPU scheduling criteria જણાવો.", "CPU utilisation, throughput, turnaround time, waiting time and response time.", "CPU utilisation, throughput, turnaround time, waiting time અને response time."),
        V("Preemptive vs non-preemptive scheduling?", "Preemptive vs non-preemptive scheduling?", "Preemptive: the CPU can be taken away from a running process; non-preemptive: the process keeps the CPU until it finishes or blocks.", "Preemptive: ચાલતી process પાસેથી CPU લઈ શકાય; non-preemptive: process પૂરી થાય કે block થાય ત્યાં સુધી CPU રાખે."),
        V("What is the convoy effect?", "Convoy effect શું છે?", "In FCFS, short processes wait behind one long process, increasing average waiting time.", "FCFS માં નાની processes એક લાંબી process પાછળ રાહ જુએ, જેથી સરેરાશ waiting time વધે."),
        V("Which algorithm gives the minimum average waiting time?", "કયો algorithm ઓછામાં ઓછો સરેરાશ waiting time આપે?", "SJF (it is optimal), but the burst time must be known in advance.", "SJF (તે optimal છે), પણ burst time અગાઉથી જાણવો પડે."),
        V("What happens if the RR time quantum is very large or very small?", "RR નો time quantum ખૂબ મોટો કે ખૂબ નાનો હોય તો શું થાય?", "Very large → RR becomes FCFS; very small → too many context switches (overhead).", "ખૂબ મોટો → RR એ FCFS બને; ખૂબ નાનો → ઘણા context switches (overhead)."),
        V("What is starvation and how is it solved?", "Starvation શું છે અને તે કેવી રીતે ઉકેલાય?", "A low-priority process waits indefinitely; solved by aging (gradually raising its priority).", "Low-priority process અનિશ્ચિત સમય રાહ જુએ; aging (ધીમે ધીમે priority વધારવી) થી ઉકેલાય."),
    ]},
    {"title": {"en": "Schedulers and Context Switch", "gu": "Schedulers અને Context Switch"}, "items": [
        V("Which scheduler controls the degree of multiprogramming?", "Degree of multiprogramming ને કયો scheduler control કરે છે?", "The long-term (job) scheduler.", "Long-term (job) scheduler."),
        V("Which scheduler runs most frequently?", "કયો scheduler સૌથી વધુ વાર ચાલે છે?", "The short-term (CPU) scheduler, every few milliseconds.", "Short-term (CPU) scheduler, દર થોડી milliseconds એ."),
        V("What does the medium-term scheduler do?", "Medium-term scheduler શું કરે છે?", "It swaps processes out of memory to disk and later swaps them back in.", "તે processes ને memory માંથી disk પર swap out કરે અને પછી પાછી swap in કરે."),
        V("What is a context switch?", "Context switch શું છે?", "Saving the state of the current process in its PCB and loading the saved state of the next process.", "હાલની process ની state તેના PCB માં save કરી બીજી process ની saved state load કરવી."),
        V("What is a dispatcher?", "Dispatcher શું છે?", "The module that gives control of the CPU to the process chosen by the short-term scheduler.", "Short-term scheduler એ પસંદ કરેલી process ને CPU નું control આપતું module."),
    ]},
    {"title": {"en": "Process Synchronization", "gu": "Process Synchronization"}, "items": [
        V("What is a race condition?", "Race condition શું છે?", "When the result of shared-data access depends on the order of execution of processes.", "જ્યારે shared data ના access નું પરિણામ processes ના execution ક્રમ પર આધાર રાખે."),
        V("What is a critical section?", "Critical section શું છે?", "The part of code in which a process accesses shared data.", "Code નો તે ભાગ જેમાં process shared data access કરે છે."),
        V("State the three requirements of a critical-section solution.", "Critical-section solution ની ત્રણ જરૂરિયાતો જણાવો.", "Mutual exclusion, progress and bounded waiting.", "Mutual exclusion, progress અને bounded waiting."),
        V("What is a semaphore?", "Semaphore શું છે?", "An integer variable accessed only by the atomic operations wait() (P) and signal() (V).", "માત્ર atomic operations wait() (P) અને signal() (V) વડે access થતો integer variable."),
    ]},
    {"title": {"en": "Deadlock", "gu": "Deadlock"}, "items": [
        V("Define deadlock.", "Deadlock ની વ્યાખ્યા આપો.", "A set of processes each waiting for a resource held by another process of the set, so none can proceed.", "Processes નો સમૂહ જેમાં દરેક સમૂહની બીજી process પાસેના resource ની રાહ જુએ, તેથી કોઈ આગળ વધી શકે નહીં."),
        V("State the four necessary conditions for deadlock.", "Deadlock માટેની ચાર જરૂરી શરતો જણાવો.", "Mutual exclusion, hold and wait, no preemption and circular wait.", "Mutual exclusion, hold and wait, no preemption અને circular wait."),
        V("What is the ostrich algorithm?", "Ostrich algorithm શું છે?", "Ignoring the deadlock problem, assuming it is rare (used by Windows and Linux).", "Deadlock ને દુર્લભ માની તેની અવગણના કરવી (Windows અને Linux વાપરે છે)."),
        V("Does a cycle in a RAG always mean deadlock?", "RAG માં cycle હંમેશા deadlock દર્શાવે?", "Only if each resource has a single instance; with multiple instances, deadlock is possible but not certain.", "માત્ર દરેક resource નું એક instance હોય તો; ઘણા instances હોય તો deadlock શક્ય છે પણ નિશ્ચિત નહીં."),
        V("Which algorithm is used for deadlock avoidance?", "Deadlock avoidance માટે કયો algorithm વપરાય?", "Banker's algorithm (Dijkstra), which keeps the system in a safe state.", "Banker's algorithm (Dijkstra), જે system ને safe state માં રાખે."),
        V("What is a safe state?", "Safe state શું છે?", "A state in which there is at least one sequence in which all processes can finish.", "એવી state જેમાં ઓછામાં ઓછો એક ક્રમ હોય જેમાં બધી processes પૂરી થઈ શકે."),
    ]},
]

EXAM_QS = [
    X("Define process. Differentiate between process and program.", "Process ની વ્યાખ્યા આપો. Process અને program વચ્ચે તફાવત આપો.", 3),
    X("Differentiate between process and thread.", "Process અને thread વચ્ચે તફાવત આપો.", 3),
    X("Draw and explain the process state diagram.", "Process state diagram દોરો અને સમજાવો.", 4),
    X("What is a PCB? Explain its fields with a diagram.", "PCB શું છે? તેના fields આકૃતિ સાથે સમજાવો.", 4),
    X("Explain CPU scheduling criteria.", "CPU scheduling criteria સમજાવો.", 3),
    X("Differentiate between preemptive and non-preemptive scheduling.", "Preemptive અને non-preemptive scheduling વચ્ચે તફાવત આપો.", 3),
    X("Explain FCFS and SJF scheduling with an example. Give their advantages and disadvantages.", "FCFS અને SJF scheduling ઉદાહરણ સાથે સમજાવો. તેમના ફાયદા અને ગેરફાયદા આપો.", 7),
    X("Explain Round Robin scheduling with an example.", "Round Robin scheduling ઉદાહરણ સાથે સમજાવો.", 4),
    X("Solve FCFS, SJF and Round Robin (quantum 2) for P0–P3 with arrival times 0, 1, 2, 3 and burst times 5, 3, 8, 6. Find average TAT and WT.", "Arrival time 0, 1, 2, 3 અને burst time 5, 3, 8, 6 વાળી P0–P3 માટે FCFS, SJF અને Round Robin (quantum 2) ઉકેલો. સરેરાશ TAT અને WT શોધો.", 7),
    X("Explain non-preemptive priority scheduling. What is starvation?", "Non-preemptive priority scheduling સમજાવો. Starvation શું છે?", 4),
    X("Explain long-term, short-term and medium-term schedulers with a diagram.", "Long-term, short-term અને medium-term schedulers આકૃતિ સાથે સમજાવો.", 7),
    X("What is a context switch? Explain with a diagram.", "Context switch શું છે? આકૃતિ સાથે સમજાવો.", 3),
    X("Explain scheduling queues with a queueing diagram.", "Queueing diagram સાથે scheduling queues સમજાવો.", 4),
    X("Define race condition, critical section and mutual exclusion.", "Race condition, critical section અને mutual exclusion ની વ્યાખ્યા આપો.", 3),
    X("Explain the critical-section problem and the requirements of its solution.", "Critical-section problem અને તેના solution ની જરૂરિયાતો સમજાવો.", 4),
    X("What is deadlock? Explain the necessary conditions for deadlock.", "Deadlock શું છે? Deadlock માટેની જરૂરી શરતો સમજાવો.", 4),
    X("Explain the resource allocation graph with examples.", "Resource allocation graph ઉદાહરણ સાથે સમજાવો.", 4),
    X("Explain deadlock prevention methods.", "Deadlock prevention ની પદ્ધતિઓ સમજાવો.", 4),
    X("Explain the methods of dealing with deadlock: ignorance, detection and recovery, avoidance, prevention.", "Deadlock સંભાળવાની પદ્ધતિઓ સમજાવો: ignorance, detection and recovery, avoidance, prevention.", 7),
    X("Explain Banker's algorithm with an example.", "Banker's algorithm ઉદાહરણ સાથે સમજાવો.", 7),
]
