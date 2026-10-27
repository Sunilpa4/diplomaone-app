"""Fundamentals of Operating System (DI03000041) - Unit 3 extras: numericals (simulated by os_mem.py), equations, viva, exam."""
from content_DI03000011_u1_extras import N, E, V, X
import os_mem as M

JOBS, PARTS = [20, 200, 500, 50, 150], [50, 300, 75, 700, 100]
MNAME = {"first": ("First fit", "First fit"), "best": ("Best fit", "Best fit"), "worst": ("Worst fit", "Worst fit")}
MRULE = {"first": ("Allocate the <b>first</b> partition (from the beginning) that is big enough.", "પૂરતું મોટું હોય તેવું <b>પહેલું</b> partition (શરૂઆતથી) ફાળવો."),
         "best": ("Allocate the <b>smallest</b> partition that is big enough.", "પૂરતું મોટું હોય તેવું <b>સૌથી નાનું</b> partition ફાળવો."),
         "worst": ("Allocate the <b>largest</b> available partition.", "ઉપલબ્ધ <b>સૌથી મોટું</b> partition ફાળવો.")}


def tbl(head, rows_):
    h = "<table><tr>" + "".join(f"<th>{x}</th>" for x in head) + "</tr>"
    for r in rows_:
        h += "<tr>" + "".join(f"<td>{v}</td>" for v in r) + "</tr>"
    return h + "</table>"


def fixed_answer(m, gu=False):
    res = M.fit_fixed(JOBS, PARTS, m)
    rows_, waste, wait = [], 0, []
    for j, i in res:
        if i is None:
            rows_.append((f"J{j + 1}", JOBS[j], "રાહ જુએ (કોઈ partition નહીં)" if gu else "waits (no partition)", "–"))
            wait.append(f"J{j + 1}")
        else:
            rows_.append((f"J{j + 1}", JOBS[j], f"{PARTS[i]} KB (#{i + 1})", f"{PARTS[i]} − {JOBS[j]} = {PARTS[i] - JOBS[j]}"))
            waste += PARTS[i] - JOBS[j]
    used = {i for _, i in res if i is not None}
    free = [f"{PARTS[i]} KB" for i in range(len(PARTS)) if i not in used]
    head = ["Job", "Size (KB)", "Partition", "Internal frag. (KB)"]
    if gu:
        return (f"<p><b>નિયમ:</b> {MRULE[m][1]} દરેક partition માં એક જ job (fixed partitions).</p>" + tbl(head, rows_)
                + f"<p><b>કુલ internal fragmentation = {waste} KB</b></p><p>મુક્ત રહેલા partitions: {', '.join(free) or 'કોઈ નહીં'}. રાહ જોતા jobs: <b>{', '.join(wait) or 'કોઈ નહીં'}</b>.</p>"), waste, wait
    return (f"<p><b>Rule:</b> {MRULE[m][0]} One job per partition (fixed partitions).</p>" + tbl(head, rows_)
            + f"<p><b>Total internal fragmentation = {waste} KB</b></p><p>Partitions left free: {', '.join(free) or 'none'}. Jobs that must wait: <b>{', '.join(wait) or 'none'}</b>.</p>"), waste, wait


def dyn_table(jobs, holes, m, gu=False, names=None):
    res, final = M.fit_dynamic(jobs, holes, m)
    names = names or [f"J{j + 1}" for j in range(len(jobs))]
    rows_ = []
    for j, i, before, after in res:
        if i is None:
            rows_.append((names[j], jobs[j], "રાહ જુએ" if gu else "waits", "–"))
        else:
            rows_.append((names[j], jobs[j], f"hole #{i + 1} ({before} KB)", f"{before} − {jobs[j]} = {after}"))
    head = ["Job", "Size", "Hole used", "Hole left (KB)"]
    return tbl(head, rows_), res, final


Q3 = ("Jobs J1 = 20 KB, J2 = 200 KB, J3 = 500 KB, J4 = 50 KB, J5 = 150 KB arrive in this order. Memory partitions are 50, 300, 75, 700 and 100 KB.",
      "Jobs J1 = 20 KB, J2 = 200 KB, J3 = 500 KB, J4 = 50 KB, J5 = 150 KB આ ક્રમમાં આવે છે. Memory partitions 50, 300, 75, 700 અને 100 KB છે.")
nums, FIX = [], {}
for k, m in enumerate(["first", "best", "worst"]):
    en, w, wait = fixed_answer(m)
    gu, _, _ = fixed_answer(m, True)
    FIX[m] = (w, wait)
    nums.append(N(f"os3n{k + 1}", f"(Practical 3) {MNAME[m][0]}: {Q3[0]} Allocate the jobs using {MNAME[m][0].lower()} (fixed partitions) and find the internal fragmentation.",
                  f"(Practical 3) {MNAME[m][1]}: {Q3[1]} {MNAME[m][1]} (fixed partitions) વડે jobs ફાળવો અને internal fragmentation શોધો.", en, gu))
assert FIX["first"] == (355, ["J5"]) and FIX["best"] == (355, ["J5"]) and FIX["worst"] == (830, ["J3", "J5"])

# n4: Practical 3 with dynamic partitions (holes)
_d = {m: dyn_table(JOBS, PARTS, m) for m in ("first", "best", "worst")}
_dg = {m: dyn_table(JOBS, PARTS, m, True) for m in ("first", "best", "worst")}
assert [x[1] for x in _d["first"][1]] == [0, 1, 3, 1, 3] and [x[1] for x in _d["worst"][1]] == [3, 3, None, 3, 3]
n4 = N("os3n4", "(Practical 3, variable partitions) Treat the partitions 50, 300, 75, 700, 100 KB as free holes: a job uses part of a hole and the rest remains free. Allocate J1 = 20, J2 = 200, J3 = 500, J4 = 50, J5 = 150 KB using first, best and worst fit.",
       "(Practical 3, variable partitions) Partitions 50, 300, 75, 700, 100 KB ને free holes ગણો: job hole નો ભાગ વાપરે અને બાકીનો મુક્ત રહે. J1 = 20, J2 = 200, J3 = 500, J4 = 50, J5 = 150 KB ને first, best અને worst fit વડે ફાળવો.",
       "".join(f"<p><b>{MNAME[m][0]}</b></p>{_d[m][0]}<p>Free holes at the end: {', '.join(map(str, _d[m][2]))} KB</p>" for m in _d)
       + "<p><b>Result:</b> first and best fit place all five jobs; worst fit fills the 700 KB hole first, so J3 (500 KB) cannot be placed and must wait.</p>",
       "".join(f"<p><b>{MNAME[m][1]}</b></p>{_dg[m][0]}<p>અંતે free holes: {', '.join(map(str, _dg[m][2]))} KB</p>" for m in _dg)
       + "<p><b>પરિણામ:</b> first અને best fit પાંચેય jobs મૂકે છે; worst fit પહેલાં 700 KB hole ભરે છે, તેથી J3 (500 KB) મૂકી શકાતો નથી અને રાહ જુએ છે.</p>")

# n5: textbook example
SJ, SH = [212, 417, 112, 426], [100, 500, 200, 300, 600]
SN = ["P1", "P2", "P3", "P4"]
_s = {m: dyn_table(SJ, SH, m, names=SN) for m in ("first", "best", "worst")}
_sg = {m: dyn_table(SJ, SH, m, True, SN) for m in ("first", "best", "worst")}
assert [x[1] for x in _s["best"][1]] == [3, 1, 2, 4] and _s["first"][1][3][1] is None and _s["worst"][1][3][1] is None
n5 = N("os3n5", "Given memory holes of 100, 500, 200, 300 and 600 KB (in order), how would first fit, best fit and worst fit place processes of 212, 417, 112 and 426 KB (in order)? Which algorithm uses memory most efficiently?",
       "Memory holes 100, 500, 200, 300 અને 600 KB (ક્રમમાં) હોય, તો first fit, best fit અને worst fit 212, 417, 112 અને 426 KB (ક્રમમાં) ની processes કેવી રીતે મૂકશે? કયો algorithm memory નો સૌથી કાર્યક્ષમ ઉપયોગ કરે છે?",
       "".join(f"<p><b>{MNAME[m][0]}</b></p>{_s[m][0]}" for m in _s) + "<p><b>Best fit</b> is the most efficient here: it is the only one that places all four processes (426 KB must wait in first and worst fit).</p>",
       "".join(f"<p><b>{MNAME[m][1]}</b></p>{_sg[m][0]}" for m in _sg) + "<p>અહીં <b>best fit</b> સૌથી કાર્યક્ષમ છે: તે એકમાત્ર ચારેય processes મૂકે છે (first અને worst fit માં 426 KB એ રાહ જોવી પડે).</p>")

# ---------------------------------------------------------------- paging
PT6 = [5, 2, 7, 9]
r6 = [M.page_translate(la, 1024, PT6) for la in (2500, 1200)]
assert r6[0] == (2, 452, 7, 7620) and r6[1] == (1, 176, 2, 2224)
n6 = N("os3n6", "A system uses paging with page size 1 KB (1024 bytes). The page table of a process is: page 0 → frame 5, page 1 → frame 2, page 2 → frame 7, page 3 → frame 9. Find the physical addresses for logical addresses (i) 2500 (ii) 1200 (iii) 5000.",
       "System page size 1 KB (1024 bytes) સાથે paging વાપરે છે. Process નું page table: page 0 → frame 5, page 1 → frame 2, page 2 → frame 7, page 3 → frame 9. Logical addresses (i) 2500 (ii) 1200 (iii) 5000 માટે physical addresses શોધો.",
       "<p>p = LA ÷ 1024 (integer part), d = LA mod 1024, PA = f × 1024 + d</p>"
       "<p><b>(i)</b> 2500 ÷ 1024 → p = 2, d = 2500 − 2048 = 452; f = 7 → PA = 7 × 1024 + 452 = 7168 + 452 = <b>7620</b></p>"
       "<p><b>(ii)</b> 1200 ÷ 1024 → p = 1, d = 176; f = 2 → PA = 2 × 1024 + 176 = <b>2224</b></p>"
       "<p><b>(iii)</b> 5000 ÷ 1024 → p = 4, d = 904. The process has only pages 0–3, so page 4 is <b>invalid → trap (addressing error)</b>.</p>",
       "<p>p = LA ÷ 1024 (પૂર્ણાંક ભાગ), d = LA mod 1024, PA = f × 1024 + d</p>"
       "<p><b>(i)</b> 2500 ÷ 1024 → p = 2, d = 2500 − 2048 = 452; f = 7 → PA = 7 × 1024 + 452 = 7168 + 452 = <b>7620</b></p>"
       "<p><b>(ii)</b> 1200 ÷ 1024 → p = 1, d = 176; f = 2 → PA = 2 × 1024 + 176 = <b>2224</b></p>"
       "<p><b>(iii)</b> 5000 ÷ 1024 → p = 4, d = 904. Process પાસે માત્ર pages 0–3 છે, તેથી page 4 <b>invalid → trap (addressing error)</b>.</p>")

PT7 = [5, 6, 1, 2]
r7 = [(la,) + M.page_translate(la, 4, PT7) for la in (0, 3, 4, 13)]
assert [x[4] for x in r7] == [20, 23, 24, 9]
_t7 = tbl(["Logical address", "p = LA ÷ 4", "d = LA mod 4", "f", "PA = f × 4 + d"], [(la, p, d, f, f"{f} × 4 + {d} = {pa}") for la, p, d, f, pa in r7])
n7 = N("os3n7", "Page size = 4 bytes, physical memory = 32 bytes (8 frames). Page table: 0 → 5, 1 → 6, 2 → 1, 3 → 2. Find the physical address of logical addresses 0, 3, 4 and 13.",
       "Page size = 4 bytes, physical memory = 32 bytes (8 frames). Page table: 0 → 5, 1 → 6, 2 → 1, 3 → 2. Logical addresses 0, 3, 4 અને 13 ના physical address શોધો.",
       _t7 + "<p>E.g. logical address 13 is in page 3 at offset 1; page 3 is in frame 2, so PA = 2 × 4 + 1 = <b>9</b>.</p>",
       _t7 + "<p>દા.ત. logical address 13 page 3 માં offset 1 પર છે; page 3 frame 2 માં છે, તેથી PA = 2 × 4 + 1 = <b>9</b>.</p>")

n8 = N("os3n8", "A logical address space has 8 pages of 1024 words each, mapped onto a physical memory of 32 frames. How many bits are there in (i) the logical address (ii) the physical address?",
       "Logical address space માં 1024 words ના 8 pages છે, જે 32 frames ની physical memory પર map થાય છે. (i) logical address (ii) physical address માં કેટલા bits છે?",
       "<p>Offset: page size 1024 = 2<sup>10</sup> → <b>10 bits</b> for d.</p><p><b>(i)</b> 8 pages = 2<sup>3</sup> → 3 bits for p. Logical address = 3 + 10 = <b>13 bits</b> (8 × 1024 = 8192 = 2<sup>13</sup>).</p>"
       "<p><b>(ii)</b> 32 frames = 2<sup>5</sup> → 5 bits for f. Physical address = 5 + 10 = <b>15 bits</b> (32 × 1024 = 32768 = 2<sup>15</sup>).</p>",
       "<p>Offset: page size 1024 = 2<sup>10</sup> → d માટે <b>10 bits</b>.</p><p><b>(i)</b> 8 pages = 2<sup>3</sup> → p માટે 3 bits. Logical address = 3 + 10 = <b>13 bits</b> (8 × 1024 = 8192 = 2<sup>13</sup>).</p>"
       "<p><b>(ii)</b> 32 frames = 2<sup>5</sup> → f માટે 5 bits. Physical address = 5 + 10 = <b>15 bits</b> (32 × 1024 = 32768 = 2<sup>15</sup>).</p>")

# ---------------------------------------------------------------- segmentation
SEG = [(219, 600), (2300, 14), (90, 100), (1327, 580), (1952, 96)]
QS = [(0, 430), (1, 10), (2, 500), (3, 400), (4, 112)]
r9 = [M.seg_translate(s, d, SEG) for s, d in QS]
assert r9 == [649, 2310, None, 1727, None]
_st = tbl(["Segment", "Base", "Length (limit)"], [(i, b, l) for i, (b, l) in enumerate(SEG)])
_r9 = tbl(["(s, d)", "d &lt; limit?", "Physical address"], [(f"({s}, {d})", f"{d} &lt; {SEG[s][1]} ✓" if r is not None else f"{d} ≥ {SEG[s][1]} ✗",
                                                           f"{SEG[s][0]} + {d} = <b>{r}</b>" if r is not None else "<b>trap</b> (illegal)") for (s, d), r in zip(QS, r9)])
_r9g = _r9.replace("(illegal)", "(અમાન્ય)")
n9 = N("os3n9", "Consider the segment table: segment 0 (base 219, length 600), 1 (2300, 14), 2 (90, 100), 3 (1327, 580), 4 (1952, 96). What are the physical addresses for the logical addresses (0, 430), (1, 10), (2, 500), (3, 400) and (4, 112)?",
       "Segment table: segment 0 (base 219, length 600), 1 (2300, 14), 2 (90, 100), 3 (1327, 580), 4 (1952, 96). Logical addresses (0, 430), (1, 10), (2, 500), (3, 400) અને (4, 112) ના physical addresses શું છે?",
       _st + "<p>Rule: if d &lt; limit, PA = base + d; otherwise trap to the OS.</p>" + _r9,
       _st + "<p>નિયમ: d &lt; limit હોય તો PA = base + d; નહીં તો OS ને trap.</p>" + _r9g)

# ---------------------------------------------------------------- page replacement
REFS = [1, 2, 3, 4, 5, 1, 3, 1, 6, 3, 2, 3]
CLS = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1]
BEL = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]
RULE = {"fifo": ("<p><b>FIFO:</b> on a fault with all frames full, replace the page that was <b>loaded earliest</b>.</p>",
                 "<p><b>FIFO:</b> fault વખતે બધી frames ભરેલી હોય તો <b>સૌથી પહેલું load</b> થયેલું page બદલો.</p>"),
        "lru": ("<p><b>LRU:</b> on a fault with all frames full, replace the page that has <b>not been used for the longest time</b> (look backwards).</p>",
                "<p><b>LRU:</b> fault વખતે બધી frames ભરેલી હોય તો <b>સૌથી લાંબા સમયથી ન વપરાયેલું</b> page બદલો (પાછળ જુઓ).</p>")}


def pr_num(id_, refs, nf, algo, q_en, q_gu, extra_en="", extra_gu=""):
    st, f = M.replace(refs, nf, algo)
    n = len(refs)
    tail_en = f"<p><b>Page faults = {f}</b>, hits = {n - f}. Fault rate = {f}/{n} = {f / n * 100:.2f}%, hit ratio = {n - f}/{n} = {(n - f) / n * 100:.2f}%.</p>"
    tail_gu = f"<p><b>Page faults = {f}</b>, hits = {n - f}. Fault rate = {f}/{n} = {f / n * 100:.2f}%, hit ratio = {n - f}/{n} = {(n - f) / n * 100:.2f}%.</p>"
    return N(id_, q_en, q_gu, RULE[algo][0] + M.replace_html(st, nf) + "<p>F = fault (bold = page just loaded), H = hit.</p>" + tail_en + extra_en,
             RULE[algo][1] + M.replace_html(st, nf, True) + "<p>F = fault (bold = હમણાં load થયેલું page), H = hit.</p>" + tail_gu + extra_gu), f


QP = ("Reference string 1, 2, 3, 4, 5, 1, 3, 1, 6, 3, 2, 3 with 4 frames (initially empty).", "Reference string 1, 2, 3, 4, 5, 1, 3, 1, 6, 3, 2, 3, 4 frames (શરૂઆતમાં ખાલી).")
n10, f10 = pr_num("os3n10", REFS, 4, "fifo", "(Practical 4) Find the number of page faults using FIFO. " + QP[0], "(Practical 4) FIFO વડે page faults શોધો. " + QP[1])
n11, f11 = pr_num("os3n11", REFS, 4, "lru", "(Practical 4) Find the number of page faults using LRU. " + QP[0], "(Practical 4) LRU વડે page faults શોધો. " + QP[1],
                  "<p>Compared with FIFO (9 faults), LRU gives 8 faults: at reference 6 LRU removes page 4 (unused longest) and keeps page 3, which is needed next.</p>",
                  "<p>FIFO (9 faults) ની સરખામણીએ LRU 8 faults આપે છે: reference 6 પર LRU page 4 (સૌથી લાંબા સમયથી ન વપરાયેલું) કાઢે છે અને page 3 રાખે છે, જે તરત જરૂરી છે.</p>")
assert (f10, f11) == (9, 8)
QC = ("Reference string 7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1 with 3 frames.", "Reference string 7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1, 3 frames.")
n12, f12 = pr_num("os3n12", CLS, 3, "fifo", "Find the page faults using FIFO. " + QC[0], "FIFO વડે page faults શોધો. " + QC[1])
n13, f13 = pr_num("os3n13", CLS, 3, "lru", "Find the page faults using LRU. " + QC[0], "LRU વડે page faults શોધો. " + QC[1],
                  "<p>FIFO gives 15 faults for the same string, so LRU (12) performs better. (The optimal algorithm would give 9.)</p>",
                  "<p>આ જ string માટે FIFO 15 faults આપે છે, તેથી LRU (12) વધુ સારું છે. (Optimal algorithm 9 આપે.)</p>")
assert (f12, f13) == (15, 12) and M.replace(CLS, 3, "opt")[1] == 9

_b3, fb3 = M.replace(BEL, 3, "fifo")
_b4, fb4 = M.replace(BEL, 4, "fifo")
assert (fb3, fb4) == (9, 10)
n14 = N("os3n14", "Show Belady's anomaly using FIFO for the reference string 1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5 with 3 frames and with 4 frames.",
        "Reference string 1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5 માટે 3 frames અને 4 frames સાથે FIFO વડે Belady's anomaly બતાવો.",
        f"<p><b>3 frames:</b></p>{M.replace_html(_b3, 3)}<p>Page faults = <b>{fb3}</b></p><p><b>4 frames:</b></p>{M.replace_html(_b4, 4)}<p>Page faults = <b>{fb4}</b></p>"
        "<p>With <b>more frames, FIFO gives more faults</b> (10 &gt; 9). This unexpected result is <b>Belady's anomaly</b>. LRU and optimal never suffer from it (they are stack algorithms).</p>",
        f"<p><b>3 frames:</b></p>{M.replace_html(_b3, 3, True)}<p>Page faults = <b>{fb3}</b></p><p><b>4 frames:</b></p>{M.replace_html(_b4, 4, True)}<p>Page faults = <b>{fb4}</b></p>"
        "<p><b>વધુ frames હોવા છતાં FIFO વધુ faults આપે છે</b> (10 &gt; 9). આ અણધાર્યા પરિણામને <b>Belady's anomaly</b> કહે છે. LRU અને optimal માં તે ક્યારેય થતું નથી (તેઓ stack algorithms છે).</p>")

NUMERICALS = nums + [n4, n5, n6, n7, n8, n9, n10, n11, n12, n13, n14]

EQUATIONS = [
    {"title": {"en": "Address Binding and Protection", "gu": "Address Binding અને Protection"}, "items": [
        E("Physical address (relocation)", "Physical address (relocation)", "PA = relocation (base) register + LA", "LA = logical address generated by the CPU", "LA = CPU એ બનાવેલું logical address"),
        E("Protection check", "Protection check", "LA &lt; limit register, else trap", "Limit = size of the process's address range", "Limit = process ની address range નું કદ"),
        E("Internal fragmentation", "Internal fragmentation", "Waste = partition size − process size", "Summed over all allocated partitions", "બધા ફાળવેલા partitions નો સરવાળો"),
    ]},
    {"title": {"en": "Paging", "gu": "Paging"}, "items": [
        E("Page number", "Page number", "p = LA div page size", "Integer part of LA ÷ page size", "LA ÷ page size નો પૂર્ણાંક ભાગ"),
        E("Offset", "Offset", "d = LA mod page size", "Position inside the page", "Page ની અંદર સ્થાન"),
        E("Physical address", "Physical address", "PA = f × page size + d", "f = page_table[p]", "f = page_table[p]"),
        E("Address bits", "Address bits", "LA bits = log<sub>2</sub>(pages) + log<sub>2</sub>(page size)", "PA bits = log<sub>2</sub>(frames) + log<sub>2</sub>(page size)", "PA bits = log<sub>2</sub>(frames) + log<sub>2</sub>(page size)"),
    ]},
    {"title": {"en": "Segmentation and Page Replacement", "gu": "Segmentation અને Page Replacement"}, "items": [
        E("Segment address", "Segment address", "PA = base[s] + d   (if d &lt; limit[s])", "Otherwise trap: addressing error", "નહીં તો trap: addressing error"),
        E("Page fault rate", "Page fault rate", "Fault rate = page faults / references", "× 100 for percentage", "ટકા માટે × 100"),
        E("Hit ratio", "Hit ratio", "Hit ratio = (references − faults) / references", "Hit ratio + fault rate = 1", "Hit ratio + fault rate = 1"),
    ]},
]

VIVA = [
    {"title": {"en": "Addresses and Swapping", "gu": "Addresses અને Swapping"}, "items": [
        V("What is a logical address?", "Logical address શું છે?", "An address generated by the CPU; also called a virtual address.", "CPU એ બનાવેલું address; તેને virtual address પણ કહે છે."),
        V("What is a physical address?", "Physical address શું છે?", "The actual address of a location in main memory, seen by the memory unit.", "Main memory માં સ્થાનનું ખરું address, જે memory unit જુએ છે."),
        V("What is the MMU?", "MMU શું છે?", "Memory Management Unit: hardware that maps logical addresses to physical addresses at run time.", "Memory Management Unit: run time પર logical addresses ને physical addresses માં map કરતું hardware."),
        V("What is swapping?", "Swapping શું છે?", "Temporarily moving a process from memory to a backing store and bringing it back later.", "Process ને કામચલાઉ memory માંથી backing store પર ખસેડી પછી પાછી લાવવી."),
        V("What is roll out, roll in?", "Roll out, roll in શું છે?", "A swapping variant for priority scheduling: a low-priority process is swapped out for a high-priority one.", "Priority scheduling માટે swapping નો પ્રકાર: high-priority process માટે low-priority process swap out થાય."),
    ]},
    {"title": {"en": "Contiguous Allocation", "gu": "Contiguous Allocation"}, "items": [
        V("What is internal fragmentation?", "Internal fragmentation શું છે?", "Unused memory inside an allocated partition or page.", "ફાળવેલા partition કે page ની અંદરની ન વપરાયેલી memory."),
        V("What is external fragmentation?", "External fragmentation શું છે?", "Enough total free memory exists but it is split into non-contiguous holes.", "કુલ free memory પૂરતી હોય પણ non-contiguous holes માં વહેંચાયેલી હોય."),
        V("What is compaction?", "Compaction શું છે?", "Moving processes so that all free holes join into one large block.", "Processes ખસેડી બધા free holes ને એક મોટા block માં જોડવા."),
        V("Which fit leaves the largest leftover hole?", "કયો fit સૌથી મોટો બાકી hole છોડે છે?", "Worst fit, because it always uses the largest hole.", "Worst fit, કારણ કે તે હંમેશા સૌથી મોટો hole વાપરે છે."),
        V("Which registers are used for protection?", "Protection માટે કયા registers વપરાય?", "The relocation (base) register and the limit register.", "Relocation (base) register અને limit register."),
        V("What is MFT and MVT?", "MFT અને MVT શું છે?", "MFT: multiprogramming with a fixed number of tasks (fixed partitions); MVT: with a variable number of tasks (dynamic partitions).", "MFT: fixed partitions સાથે multiprogramming; MVT: dynamic (variable) partitions સાથે multiprogramming."),
    ]},
    {"title": {"en": "Paging and Segmentation", "gu": "Paging અને Segmentation"}, "items": [
        V("What are pages and frames?", "Pages અને frames શું છે?", "Fixed-size blocks of logical memory are pages; equal-size blocks of physical memory are frames.", "Logical memory ના fixed-size blocks pages છે; physical memory ના સમાન કદના blocks frames છે."),
        V("What does a page table contain?", "Page table માં શું હોય છે?", "The frame number for each page of the process (plus valid/invalid and protection bits).", "Process ના દરેક page નો frame number (સાથે valid/invalid અને protection bits)."),
        V("Does paging have external fragmentation?", "Paging માં external fragmentation હોય?", "No; it can have only internal fragmentation in the last page.", "ના; માત્ર છેલ્લા page માં internal fragmentation હોઈ શકે."),
        V("What is a segment?", "Segment શું છે?", "A logical unit of a program such as main, a function, the stack or an array, of variable size.", "Program નો logical unit જેમ કે main, function, stack કે array, જેનું કદ બદલાય."),
        V("What does a segment table entry contain?", "Segment table entry માં શું હોય?", "The base (starting physical address) and limit (length) of the segment.", "Segment નો base (શરૂઆતનું physical address) અને limit (લંબાઈ)."),
    ]},
    {"title": {"en": "Page Replacement", "gu": "Page Replacement"}, "items": [
        V("What is a page fault?", "Page fault શું છે?", "A trap that occurs when a process accesses a page that is not in main memory.", "Process main memory માં ન હોય તેવું page access કરે ત્યારે થતો trap."),
        V("What is demand paging?", "Demand paging શું છે?", "Loading a page into memory only when it is needed (on a page fault).", "Page ની જરૂર પડે ત્યારે જ (page fault પર) તેને memory માં load કરવું."),
        V("Which page does FIFO replace?", "FIFO કયું page બદલે છે?", "The page that has been in memory the longest (loaded first).", "Memory માં સૌથી લાંબા સમયથી રહેલું (પહેલું load થયેલું) page."),
        V("Which page does LRU replace?", "LRU કયું page બદલે છે?", "The page that has not been used for the longest period of time.", "સૌથી લાંબા સમયથી ન વપરાયેલું page."),
        V("What is Belady's anomaly?", "Belady's anomaly શું છે?", "With FIFO, increasing the number of frames can increase the number of page faults.", "FIFO માં frames ની સંખ્યા વધારવાથી page faults વધી શકે."),
        V("What is thrashing?", "Thrashing શું છે?", "A process spends more time paging (swapping pages in and out) than executing.", "Process execution કરતાં paging (pages અંદર-બહાર) માં વધુ સમય ગાળે."),
    ]},
]

EXAM_QS = [
    X("Differentiate between logical and physical address.", "Logical અને physical address વચ્ચે તફાવત આપો.", 3),
    X("Explain swapping with a diagram.", "Swapping આકૃતિ સાથે સમજાવો.", 3),
    X("Explain multiprogramming with fixed partitions and dynamic partitions.", "Fixed partitions અને dynamic partitions સાથે multiprogramming સમજાવો.", 4),
    X("Differentiate between internal and external fragmentation. What is compaction?", "Internal અને external fragmentation વચ્ચે તફાવત આપો. Compaction શું છે?", 4),
    X("Explain memory relocation and protection using base and limit registers.", "Base અને limit registers વડે memory relocation અને protection સમજાવો.", 4),
    X("Explain first fit, best fit and worst fit with an example.", "First fit, best fit અને worst fit ઉદાહરણ સાથે સમજાવો.", 4),
    X("Jobs 20, 200, 500, 50, 150 KB; partitions 50, 300, 75, 700, 100 KB. Apply first, best and worst fit.", "Jobs 20, 200, 500, 50, 150 KB; partitions 50, 300, 75, 700, 100 KB. First, best અને worst fit લાગુ કરો.", 7),
    X("Explain paging with a diagram.", "Paging આકૃતિ સાથે સમજાવો.", 4),
    X("Explain address translation in paging with the hardware diagram.", "Hardware diagram સાથે paging માં address translation સમજાવો.", 7),
    X("Explain segmentation and its address translation.", "Segmentation અને તેનું address translation સમજાવો.", 7),
    X("Differentiate between paging and segmentation.", "Paging અને segmentation વચ્ચે તફાવત આપો.", 4),
    X("What is a page fault? Explain the steps in handling a page fault.", "Page fault શું છે? Page fault સંભાળવાના પગલાં સમજાવો.", 4),
    X("Explain FIFO page replacement. What is Belady's anomaly?", "FIFO page replacement સમજાવો. Belady's anomaly શું છે?", 4),
    X("Find page faults using FIFO and LRU for 1, 2, 3, 4, 5, 1, 3, 1, 6, 3, 2, 3 with 4 frames.", "4 frames સાથે 1, 2, 3, 4, 5, 1, 3, 1, 6, 3, 2, 3 માટે FIFO અને LRU વડે page faults શોધો.", 7),
    X("Compare FIFO and LRU page replacement algorithms.", "FIFO અને LRU page replacement algorithms ની સરખામણી કરો.", 3),
]
