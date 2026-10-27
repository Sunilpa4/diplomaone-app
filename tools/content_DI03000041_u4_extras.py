"""Fundamentals of Operating System (DI03000041) - Unit 4 extras: numericals (disk scheduling simulated by os_disk.py),
equations, viva, exam."""
from content_DI03000011_u1_extras import N, E, V, X
import os_disk as D


def tbl(head, rows_):
    h = "<table><tr>" + "".join(f"<th>{x}</th>" for x in head) + "</tr>"
    for r in rows_:
        h += "<tr>" + "".join(f"<td>{v}</td>" for v in r) + "</tr>"
    return h + "</table>"


def move_table(path, gu=False, jump_at=None):
    rows_ = []
    for i, (a, b, d) in enumerate(D.moves(path)):
        note = ""
        if jump_at is not None and i == jump_at:
            note = " (return jump)" if not gu else " (પાછો jump)"
        rows_.append((i + 1, f"{a} → {b}{note}", d))
    rows_.append(("", "<b>Total</b>" if not gu else "<b>કુલ</b>", f"<b>{sum(d for *_, d in D.moves(path))}</b>"))
    return tbl(["Step", "Head move", "Tracks"] if not gu else ["પગલું", "Head move", "Tracks"], rows_)


QP5 = ("Disk with 200 tracks (0–199); queue 75, 90, 40, 135, 50, 170, 65, 10; head at 46.",
       "200 tracks (0–199) વાળી disk; queue 75, 90, 40, 135, 50, 170, 65, 10; head 46 પર.")
QS = ("Disk with 200 cylinders (0–199); queue 98, 183, 37, 122, 14, 124, 65, 67; head at 53.",
      "200 cylinders (0–199) વાળી disk; queue 98, 183, 37, 122, 14, 124, 65, 67; head 53 પર.")


def order(p):
    return " → ".join(map(str, p))


# ---- os4n1 SCAN left (Practical 5)
p1, t1 = D.scan(D.P5_Q, D.P5_H, "left")
assert t1 == 216
n1 = N("os4n1", "(Practical 5) " + QP5[0] + " The head moves towards the left (0). Find the total head movement using SCAN.",
       "(Practical 5) " + QP5[1] + " Head ડાબી બાજુ (0 તરફ) જાય છે. SCAN વડે કુલ head movement શોધો.",
       f"""<p><b>SCAN (elevator):</b> the head moves left, serving all requests on the way, goes to the <b>end of the disk (track 0)</b>, then reverses and serves the remaining requests while moving right.</p>
<p>Requests left of 46 (descending): 40, 10. Then track 0. Requests right of 46 (ascending): 50, 65, 75, 90, 135, 170.</p>
<p><b>Order:</b> {order(p1)}</p>{move_table(p1)}
<p>Short method: (46 − 0) + (170 − 0) = 46 + 170 = <b>{t1} tracks</b>.</p>""",
       f"""<p><b>SCAN (elevator):</b> head ડાબી બાજુ જતાં રસ્તામાંની બધી requests સંતોષે, <b>disk ના છેડા (track 0)</b> સુધી જાય, પછી દિશા બદલી જમણી બાજુ જતાં બાકીની requests સંતોષે.</p>
<p>46 ની ડાબી બાજુની requests (ઊતરતા ક્રમે): 40, 10. પછી track 0. 46 ની જમણી બાજુની requests (ચડતા ક્રમે): 50, 65, 75, 90, 135, 170.</p>
<p><b>ક્રમ:</b> {order(p1)}</p>{move_table(p1, True)}
<p>ટૂંકી રીત: (46 − 0) + (170 − 0) = 46 + 170 = <b>{t1} tracks</b>.</p>""")

# ---- os4n2 C-SCAN left (Practical 5)
p2, t2, t2b = D.cscan(D.P5_Q, D.P5_H, "left")
assert (t2, t2b) == (394, 195)
n2 = N("os4n2", "(Practical 5) " + QP5[0] + " The head moves towards the left (0). Find the total head movement using C-SCAN.",
       "(Practical 5) " + QP5[1] + " Head ડાબી બાજુ (0 તરફ) જાય છે. C-SCAN વડે કુલ head movement શોધો.",
       f"""<p><b>C-SCAN (circular SCAN):</b> the head serves requests in <b>one direction only</b> (here, left). On reaching track 0 it <b>jumps to the other end (199)</b> without serving anything, and continues moving left.</p>
<p>Left of 46: 40, 10 → 0. Jump 0 → 199. Then (moving left from 199): 170, 135, 90, 75, 65, 50.</p>
<p><b>Order:</b> {order(p2)}</p>{move_table(p2, jump_at=3)}
<p>(46 − 0) + (199 − 0) + (199 − 50) = 46 + 199 + 149 = <b>{t2} tracks</b>.</p>
<p><b>Note:</b> some books do not count the return jump: 46 + 149 = <b>{t2b} tracks</b>. In the exam, state which convention you use.</p>""",
       f"""<p><b>C-SCAN (circular SCAN):</b> head requests ને <b>માત્ર એક જ દિશામાં</b> (અહીં ડાબી) સંતોષે. Track 0 પર પહોંચીને તે કંઈ પણ સંતોષ્યા વગર <b>બીજા છેડે (199) jump</b> કરે, અને ડાબી બાજુ આગળ વધે.</p>
<p>46 ની ડાબી: 40, 10 → 0. Jump 0 → 199. પછી (199 થી ડાબી બાજુ): 170, 135, 90, 75, 65, 50.</p>
<p><b>ક્રમ:</b> {order(p2)}</p>{move_table(p2, True, jump_at=3)}
<p>(46 − 0) + (199 − 0) + (199 − 50) = 46 + 199 + 149 = <b>{t2} tracks</b>.</p>
<p><b>નોંધ:</b> કેટલાંક પુસ્તકો return jump ગણતા નથી: 46 + 149 = <b>{t2b} tracks</b>. Exam માં કઈ પદ્ધતિ વાપરી તે લખો.</p>""")

# ---- os4n3 SCAN right
p3, t3 = D.scan(D.P5_Q, D.P5_H, "right")
assert t3 == 342
n3 = N("os4n3", QP5[0] + " If the head moves towards the right (199), find the total head movement using SCAN.",
       QP5[1] + " Head જમણી બાજુ (199 તરફ) જાય તો SCAN વડે કુલ head movement શોધો.",
       f"""<p>Moving right: 50, 65, 75, 90, 135, 170 → end 199; reverse: 40, 10.</p>
<p><b>Order:</b> {order(p3)}</p>{move_table(p3)}
<p>(199 − 46) + (199 − 10) = 153 + 189 = <b>{t3} tracks</b>.</p>""",
       f"""<p>જમણી બાજુ: 50, 65, 75, 90, 135, 170 → છેડો 199; દિશા બદલી: 40, 10.</p>
<p><b>ક્રમ:</b> {order(p3)}</p>{move_table(p3, True)}
<p>(199 − 46) + (199 − 10) = 153 + 189 = <b>{t3} tracks</b>.</p>""")

# ---- os4n4 C-SCAN right
p4, t4, t4b = D.cscan(D.P5_Q, D.P5_H, "right")
assert (t4, t4b) == (392, 193)
n4 = N("os4n4", QP5[0] + " If the head moves towards the right (199), find the total head movement using C-SCAN.",
       QP5[1] + " Head જમણી બાજુ (199 તરફ) જાય તો C-SCAN વડે કુલ head movement શોધો.",
       f"""<p>Moving right: 50, 65, 75, 90, 135, 170 → 199; jump 199 → 0; continue right: 10, 40.</p>
<p><b>Order:</b> {order(p4)}</p>{move_table(p4, jump_at=7)}
<p>(199 − 46) + (199 − 0) + (40 − 0) = 153 + 199 + 40 = <b>{t4} tracks</b> (without the return jump: <b>{t4b}</b>).</p>""",
       f"""<p>જમણી બાજુ: 50, 65, 75, 90, 135, 170 → 199; jump 199 → 0; જમણી બાજુ આગળ: 10, 40.</p>
<p><b>ક્રમ:</b> {order(p4)}</p>{move_table(p4, True, jump_at=7)}
<p>(199 − 46) + (199 − 0) + (40 − 0) = 153 + 199 + 40 = <b>{t4} tracks</b> (return jump વગર: <b>{t4b}</b>).</p>""")

# ---- os4n5 FCFS comparison
p5, t5 = D.fcfs(D.P5_Q, D.P5_H)
assert t5 == 554
n5 = N("os4n5", QP5[0] + " Find the total head movement using FCFS and compare it with SCAN and C-SCAN.",
       QP5[1] + " FCFS વડે કુલ head movement શોધો અને SCAN તથા C-SCAN સાથે સરખાવો.",
       f"""<p><b>FCFS:</b> requests are served in the order they arrive.</p>
<p><b>Order:</b> {order(p5)}</p>{move_table(p5)}
{tbl(["Algorithm (head 46, left)", "Total head movement"], [("FCFS", t5), ("SCAN", t1), ("C-SCAN", f"{t2} (or {t2b} without jump)")])}
<p>SCAN gives the least movement here; FCFS is the worst because the head swings back and forth (e.g. 40 → 135 → 50 → 170).</p>""",
       f"""<p><b>FCFS:</b> requests આવે તે ક્રમમાં સંતોષાય.</p>
<p><b>ક્રમ:</b> {order(p5)}</p>{move_table(p5, True)}
{tbl(["Algorithm (head 46, ડાબી)", "કુલ head movement"], [("FCFS", t5), ("SCAN", t1), ("C-SCAN", f"{t2} (jump વગર {t2b})")])}
<p>અહીં SCAN સૌથી ઓછું movement આપે છે; FCFS સૌથી ખરાબ છે કારણ કે head આગળ-પાછળ ઝૂલે છે (દા.ત. 40 → 135 → 50 → 170).</p>""")

# ---- os4n6 classic SCAN toward 0
p6, t6 = D.scan(D.SIL_Q, D.SIL_H, "left")
assert t6 == 236
n6 = N("os4n6", QS[0] + " The head is moving towards 0. Find the total head movement using SCAN.",
       QS[1] + " Head 0 તરફ જાય છે. SCAN વડે કુલ head movement શોધો.",
       f"""<p><b>Order:</b> {order(p6)}</p>{move_table(p6)}
<p>(53 − 0) + (183 − 0) = 53 + 183 = <b>{t6} cylinders</b>. (FCFS for the same queue = 640.)</p>""",
       f"""<p><b>ક્રમ:</b> {order(p6)}</p>{move_table(p6, True)}
<p>(53 − 0) + (183 − 0) = 53 + 183 = <b>{t6} cylinders</b>. (આ જ queue માટે FCFS = 640.)</p>""")

# ---- os4n7 classic C-SCAN toward 199
p7, t7, t7b = D.cscan(D.SIL_Q, D.SIL_H, "right")
assert (t7, t7b) == (382, 183)
n7 = N("os4n7", QS[0] + " The head is moving towards 199. Find the total head movement using C-SCAN.",
       QS[1] + " Head 199 તરફ જાય છે. C-SCAN વડે કુલ head movement શોધો.",
       f"""<p><b>Order:</b> {order(p7)}</p>{move_table(p7, jump_at=6)}
<p>(199 − 53) + (199 − 0) + (37 − 0) = 146 + 199 + 37 = <b>{t7} cylinders</b> (without the return jump: <b>{t7b}</b>).</p>""",
       f"""<p><b>ક્રમ:</b> {order(p7)}</p>{move_table(p7, True, jump_at=6)}
<p>(199 − 53) + (199 − 0) + (37 − 0) = 146 + 199 + 37 = <b>{t7} cylinders</b> (return jump વગર: <b>{t7b}</b>).</p>""")

# ---- os4n8 LOOK and C-LOOK
p8a, t8a = D.look(D.P5_Q, D.P5_H, "left")
p8b, t8b = D.clook(D.P5_Q, D.P5_H, "left")
assert (t8a, t8b) == (196, 316)
n8 = N("os4n8", QP5[0] + " Head moving left. Find the total head movement using LOOK and C-LOOK (variants of SCAN and C-SCAN).",
       QP5[1] + " Head ડાબી બાજુ. LOOK અને C-LOOK (SCAN અને C-SCAN ના પ્રકારો) વડે કુલ head movement શોધો.",
       f"""<p><b>LOOK / C-LOOK</b> work like SCAN / C-SCAN, but the head goes only as far as the <b>last request</b> in each direction, not to the end of the disk.</p>
<p><b>LOOK order:</b> {order(p8a)} → (46 − 10) + (170 − 10) = 36 + 160 = <b>{t8a}</b></p>
<p><b>C-LOOK order:</b> {order(p8b)} → (46 − 10) + (170 − 10) + (170 − 50) = 36 + 160 + 120 = <b>{t8b}</b></p>
<p>LOOK saves the 2 × 10 = 20 tracks that SCAN wastes going from 10 to 0 and back.</p>""",
       f"""<p><b>LOOK / C-LOOK</b> SCAN / C-SCAN જેવા જ છે, પણ head disk ના છેડા સુધી નહીં, દરેક દિશામાં માત્ર <b>છેલ્લી request</b> સુધી જ જાય છે.</p>
<p><b>LOOK ક્રમ:</b> {order(p8a)} → (46 − 10) + (170 − 10) = 36 + 160 = <b>{t8a}</b></p>
<p><b>C-LOOK ક્રમ:</b> {order(p8b)} → (46 − 10) + (170 − 10) + (170 − 50) = 36 + 160 + 120 = <b>{t8b}</b></p>
<p>SCAN 10 થી 0 અને પાછા જવામાં 2 × 10 = 20 tracks વેડફે છે, જે LOOK બચાવે છે.</p>""")

# ---- os4n9 disk capacity
cap = 8 * 1024 * 64 * 512
assert cap == 256 * 1024 * 1024
n9 = N("os4n9", "A disk has 8 surfaces, 1024 tracks per surface, 64 sectors per track and 512 bytes per sector. Find the disk capacity and the number of cylinders.",
       "Disk માં 8 surfaces, દરેક surface પર 1024 tracks, દરેક track માં 64 sectors અને દરેક sector માં 512 bytes છે. Disk capacity અને cylinders ની સંખ્યા શોધો.",
       f"""<p><b>Capacity</b> = surfaces × tracks/surface × sectors/track × bytes/sector</p>
<p>= 8 × 1024 × 64 × 512 = {cap:,} bytes = 2<sup>28</sup> bytes = <b>256 MB</b>.</p>
<p><b>Cylinders</b> = tracks per surface = <b>1024</b> (a cylinder is the same track on all 8 surfaces).</p>
<p>Capacity of one cylinder = 8 × 64 × 512 = 262,144 bytes = <b>256 KB</b>.</p>""",
       f"""<p><b>Capacity</b> = surfaces × tracks/surface × sectors/track × bytes/sector</p>
<p>= 8 × 1024 × 64 × 512 = {cap:,} bytes = 2<sup>28</sup> bytes = <b>256 MB</b>.</p>
<p><b>Cylinders</b> = surface દીઠ tracks = <b>1024</b> (cylinder એટલે બધી 8 surfaces પરનો એક જ track).</p>
<p>એક cylinder ની capacity = 8 × 64 × 512 = 262,144 bytes = <b>256 KB</b>.</p>""")

# ---- os4n10 access time
rot = 60000 / 7200
lat, tr = rot / 2, rot / 64
acc = 5 + lat + tr
assert abs(acc - 9.297) < 0.01
n10 = N("os4n10", "A disk rotates at 7200 rpm, has an average seek time of 5 ms and 64 sectors per track. Find the average time to read one sector.",
        "Disk 7200 rpm પર ફરે છે, average seek time 5 ms છે અને દરેક track માં 64 sectors છે. એક sector વાંચવાનો સરેરાશ સમય શોધો.",
        f"""<p>Time for one rotation = 60 / 7200 s = {rot:.2f} ms.</p>
<p><b>Average rotational latency</b> = half a rotation = {rot:.2f} / 2 = {lat:.2f} ms.</p>
<p><b>Transfer time</b> for one sector = rotation time / sectors per track = {rot:.2f} / 64 = {tr:.2f} ms.</p>
<p><b>Access time</b> = seek + latency + transfer = 5 + {lat:.2f} + {tr:.2f} = <b>{acc:.2f} ms</b>.</p>
<p>Seek time dominates; that is why disk-scheduling algorithms try to reduce head movement.</p>""",
        f"""<p>એક rotation નો સમય = 60 / 7200 s = {rot:.2f} ms.</p>
<p><b>Average rotational latency</b> = અડધું rotation = {rot:.2f} / 2 = {lat:.2f} ms.</p>
<p>એક sector નો <b>transfer time</b> = rotation time / track દીઠ sectors = {rot:.2f} / 64 = {tr:.2f} ms.</p>
<p><b>Access time</b> = seek + latency + transfer = 5 + {lat:.2f} + {tr:.2f} = <b>{acc:.2f} ms</b>.</p>
<p>Seek time સૌથી મોટો છે; તેથી disk-scheduling algorithms head movement ઘટાડવાનો પ્રયત્ન કરે છે.</p>""")

# ---- os4n11 paths
PATHS = [("notes.txt", "/home/ravi/os/notes.txt", "os/notes.txt"), ("prog.c", "/home/ravi/c/prog.c", "c/prog.c"),
         ("a.c", "/home/priya/a.c", "../priya/a.c"), ("passwd", "/etc/passwd", "../../etc/passwd")]
n11 = N("os4n11", "Directory tree: / contains bin (ls), home and etc (passwd); home contains ravi and priya (a.c); ravi contains os (notes.txt) and c (prog.c). The current directory is /home/ravi. Write the absolute and relative paths of notes.txt, prog.c, a.c and passwd.",
        "Directory tree: / માં bin (ls), home અને etc (passwd); home માં ravi અને priya (a.c); ravi માં os (notes.txt) અને c (prog.c). Current directory /home/ravi છે. notes.txt, prog.c, a.c અને passwd ના absolute અને relative paths લખો.",
        """<p><b>Absolute path</b> starts from the root (/). <b>Relative path</b> starts from the current directory; <code>..</code> means the parent directory and <code>.</code> means the current directory.</p>"""
        + tbl(["File", "Absolute path", "Relative path (cwd = /home/ravi)"], PATHS)
        + "<p>For passwd: go up twice (ravi → home → /), then down into etc.</p>",
        """<p><b>Absolute path</b> root (/) થી શરૂ થાય. <b>Relative path</b> current directory થી શરૂ થાય; <code>..</code> એટલે parent directory અને <code>.</code> એટલે current directory.</p>"""
        + tbl(["File", "Absolute path", "Relative path (cwd = /home/ravi)"], PATHS)
        + "<p>passwd માટે: બે વાર ઉપર જાઓ (ravi → home → /), પછી etc માં નીચે.</p>")

# ---- os4n12 permissions
def octal(s):
    return "".join(str(sum(v for ch, v in zip(s[i:i + 3], (4, 2, 1)) if ch != "-")) for i in (0, 3, 6))


def sym(o):
    return "".join("".join(c if int(d) & v else "-" for c, v in zip("rwx", (4, 2, 1))) for d in o)


assert octal("rwxr-xr--") == "754" and octal("rw-r--r--") == "644" and sym("750") == "rwxr-x---" and sym("600") == "rw-------"
PR = [("rwxr-xr--", "754"), ("rw-r--r--", "644"), (sym("750"), "750"), (sym("600"), "600")]
n12 = N("os4n12", "Convert the Unix permissions: (a) rwxr-xr-- and (b) rw-r--r-- to octal; (c) 750 and (d) 600 to symbolic form. Write the chmod command for (a).",
        "Unix permissions ફેરવો: (a) rwxr-xr-- અને (b) rw-r--r-- ને octal માં; (c) 750 અને (d) 600 ને symbolic સ્વરૂપમાં. (a) માટે chmod command લખો.",
        """<p>Each group of three (owner, group, others): r = 4, w = 2, x = 1; add the values.</p>"""
        + tbl(["Symbolic", "Octal", "Owner / Group / Others"], [(a, b, " / ".join(a[i:i + 3] + f" = {b[i // 3]}" for i in (0, 3, 6))) for a, b in PR])
        + "<p>(a) <code>chmod 754 file</code> (or <code>chmod u=rwx,g=rx,o=r file</code>). 600 is typical for private files: only the owner can read and write.</p>",
        """<p>ત્રણના દરેક group (owner, group, others) માં: r = 4, w = 2, x = 1; કિંમતો ઉમેરો.</p>"""
        + tbl(["Symbolic", "Octal", "Owner / Group / Others"], [(a, b, " / ".join(a[i:i + 3] + f" = {b[i // 3]}" for i in (0, 3, 6))) for a, b in PR])
        + "<p>(a) <code>chmod 754 file</code> (અથવા <code>chmod u=rwx,g=rx,o=r file</code>). 600 private files માટે સામાન્ય છે: માત્ર owner વાંચી અને લખી શકે.</p>")

# ---- os4n13 locating a logical block
n13 = N("os4n13", "File tr uses contiguous allocation (start 14, length 3). File jeep uses linked allocation 9 → 16 → 1 → 10 → 25 and, in another case, indexed allocation with index block 19. Find the physical block of logical block 2 of tr and logical block 3 of jeep, and the number of disk reads needed in each case.",
        "File tr contiguous allocation (start 14, length 3) વાપરે છે. File jeep linked allocation 9 → 16 → 1 → 10 → 25 અને બીજા કિસ્સામાં index block 19 સાથે indexed allocation વાપરે છે. tr નો logical block 2 અને jeep નો logical block 3 કયા physical block માં છે, અને દરેક કિસ્સામાં કેટલા disk reads જોઈએ તે શોધો.",
        tbl(["Method", "Calculation", "Physical block", "Disk reads"], [
            ("Contiguous (tr)", "start + i = 14 + 2", "<b>16</b>", "1 (direct)"),
            ("Linked (jeep)", "follow 9 → 16 → 1 → 10", "<b>10</b>", "4 (blocks 0–3 in turn)"),
            ("Indexed (jeep)", "read index block 19, entry 3", "<b>10</b>", "2 (index + data)")])
        + "<p>Contiguous and indexed allow <b>direct access</b>; linked allocation needs sequential traversal. If the index block is already in memory, indexed needs only 1 read.</p>",
        tbl(["પદ્ધતિ", "ગણતરી", "Physical block", "Disk reads"], [
            ("Contiguous (tr)", "start + i = 14 + 2", "<b>16</b>", "1 (direct)"),
            ("Linked (jeep)", "9 → 16 → 1 → 10 અનુસરો", "<b>10</b>", "4 (blocks 0–3 વારાફરતી)"),
            ("Indexed (jeep)", "index block 19 વાંચો, entry 3", "<b>10</b>", "2 (index + data)")])
        + "<p>Contiguous અને indexed <b>direct access</b> આપે છે; linked allocation માં ક્રમશઃ traversal કરવું પડે. Index block પહેલેથી memory માં હોય તો indexed માં માત્ર 1 read જોઈએ.</p>")

# ---- os4n14 indexed file size
ptrs = 1024 // 4
assert ptrs == 256 and ptrs * ptrs * 1024 == 64 * 1024 * 1024
n14 = N("os4n14", "Block size is 1 KB and a disk-block pointer is 4 bytes. Find the maximum file size with (a) one index block and (b) a two-level index. Also find the pointer overhead in linked allocation.",
        "Block size 1 KB છે અને disk-block pointer 4 bytes છે. (a) એક index block અને (b) two-level index સાથે મહત્તમ file size શોધો. Linked allocation માં pointer overhead પણ શોધો.",
        f"""<p>Pointers per index block = 1024 / 4 = <b>{ptrs}</b>.</p>
<p>(a) One index block: {ptrs} data blocks × 1 KB = <b>256 KB</b>.</p>
<p>(b) Two-level index: {ptrs} × {ptrs} = 65,536 data blocks × 1 KB = <b>64 MB</b>.</p>
<p>Linked allocation: each 1 KB block stores a 4-byte next pointer → data per block = 1020 bytes; overhead = 4 / 1024 ≈ <b>0.39%</b>.</p>""",
        f"""<p>Index block દીઠ pointers = 1024 / 4 = <b>{ptrs}</b>.</p>
<p>(a) એક index block: {ptrs} data blocks × 1 KB = <b>256 KB</b>.</p>
<p>(b) Two-level index: {ptrs} × {ptrs} = 65,536 data blocks × 1 KB = <b>64 MB</b>.</p>
<p>Linked allocation: દરેક 1 KB block માં 4-byte next pointer → block દીઠ data = 1020 bytes; overhead = 4 / 1024 ≈ <b>0.39%</b>.</p>""")

NUMERICALS = [n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11, n12, n13, n14]

EQUATIONS = [
    {"title": {"en": "Disk Performance", "gu": "Disk Performance"}, "items": [
        E("Disk access time", "Disk access time", "Access time = seek time + rotational latency + transfer time", "Seek = move head to the track; latency = wait for the sector", "Seek = head ને track પર લઈ જવો; latency = sector ની રાહ"),
        E("Average rotational latency", "Average rotational latency", "Latency = ½ × (60 / rpm) s", "e.g. 7200 rpm → 4.17 ms", "દા.ત. 7200 rpm → 4.17 ms"),
        E("Transfer time (one sector)", "Transfer time (એક sector)", "Transfer = rotation time / sectors per track", "Or bytes ÷ transfer rate", "અથવા bytes ÷ transfer rate"),
        E("Disk capacity", "Disk capacity", "Capacity = surfaces × tracks × sectors × bytes per sector", "Cylinders = tracks per surface", "Cylinders = surface દીઠ tracks"),
    ]},
    {"title": {"en": "Disk Scheduling", "gu": "Disk Scheduling"}, "items": [
        E("Total head movement", "કુલ head movement", "Total = Σ |next track − current track|", "Sum over every move of the head", "Head ની દરેક move નો સરવાળો"),
        E("SCAN (moving to 0)", "SCAN (0 તરફ)", "Total = (head − 0) + (largest request − 0)", "When requests exist on both sides", "બંને બાજુ requests હોય ત્યારે"),
        E("C-SCAN (moving to 0)", "C-SCAN (0 તરફ)", "Total = head + (N − 1) + (N − 1 − smallest request right of head)", "N = number of tracks; drop (N − 1) if the jump is not counted", "N = tracks ની સંખ્યા; jump ન ગણો તો (N − 1) કાઢો"),
    ]},
    {"title": {"en": "Files and Allocation", "gu": "Files અને Allocation"}, "items": [
        E("Octal permission", "Octal permission", "digit = 4·r + 2·w + 1·x (for owner, group, others)", "rwxr-xr-- = 754", "rwxr-xr-- = 754"),
        E("Contiguous: physical block", "Contiguous: physical block", "block = start + logical block number", "Direct access in one read", "એક read માં direct access"),
        E("Pointers per index block", "Index block દીઠ pointers", "P = block size / pointer size", "Max file (1 index block) = P × block size", "મહત્તમ file (1 index block) = P × block size"),
    ]},
]

VIVA = [
    {"title": {"en": "Files", "gu": "Files"}, "items": [
        V("What is a file?", "File શું છે?", "A named collection of related information stored on secondary storage; the smallest unit of logical storage for the user.", "Secondary storage પર સંગ્રહિત સંબંધિત માહિતીનો નામવાળો સમૂહ; user માટે logical storage નો સૌથી નાનો એકમ."),
        V("Name any four file attributes.", "કોઈ પણ ચાર file attributes જણાવો.", "Name, type, location, size, protection, time/date and user identification.", "Name, type, location, size, protection, time/date અને user identification."),
        V("List the basic file operations.", "મૂળભૂત file operations જણાવો.", "Create, write, read, reposition (seek), delete, truncate; also open and close.", "Create, write, read, reposition (seek), delete, truncate; ઉપરાંત open અને close."),
        V("Difference between absolute and relative path?", "Absolute અને relative path વચ્ચે તફાવત?", "An absolute path starts from the root (/home/ravi/a.c); a relative path starts from the current directory (a.c).", "Absolute path root થી શરૂ થાય (/home/ravi/a.c); relative path current directory થી શરૂ થાય (a.c)."),
        V("What does chmod 644 mean?", "chmod 644 નો અર્થ શું?", "Owner read + write (6), group read (4), others read (4): rw-r--r--.", "Owner read + write (6), group read (4), others read (4): rw-r--r--."),
        V("What is an access-control list (ACL)?", "Access-control list (ACL) શું છે?", "A list attached to a file giving the user names and the access types allowed for each.", "File સાથે જોડાયેલી યાદી જે દરેક user નું નામ અને તેને મંજૂર access types આપે."),
    ]},
    {"title": {"en": "Directories", "gu": "Directories"}, "items": [
        V("What is a directory?", "Directory શું છે?", "A symbol table that maps file names to their directory entries (location and attributes).", "File names ને તેમની directory entries (location અને attributes) સાથે map કરતી symbol table."),
        V("Main problem of a single-level directory?", "Single-level directory ની મુખ્ય સમસ્યા?", "All files are in one directory, so names must be unique and files cannot be grouped.", "બધી files એક directory માં હોવાથી names unique જોઈએ અને files group ન થઈ શકે."),
        V("What are MFD and UFD?", "MFD અને UFD શું છે?", "In a two-level directory, the master file directory has one entry per user pointing to that user's user file directory.", "Two-level directory માં master file directory માં દરેક user ની એક entry હોય જે તે user ની user file directory તરફ point કરે."),
        V("What advantage does an acyclic-graph directory add?", "Acyclic-graph directory કયો ફાયદો ઉમેરે?", "Sharing: a file or subdirectory can appear in more than one directory (links), without cycles.", "Sharing: file કે subdirectory એક કરતાં વધુ directories માં (links વડે) દેખાઈ શકે, cycles વગર."),
        V("Why are cycles a problem in a general graph directory?", "General graph directory માં cycles શા માટે સમસ્યા છે?", "Searches can loop forever and deleted files may never reach a reference count of zero; garbage collection is needed.", "Search હંમેશ માટે loop માં ફસાઈ શકે અને deleted files નો reference count ક્યારેય શૂન્ય ન થાય; garbage collection જોઈએ."),
    ]},
    {"title": {"en": "Allocation Methods", "gu": "Allocation Methods"}, "items": [
        V("What is contiguous allocation?", "Contiguous allocation શું છે?", "Each file occupies a set of consecutive blocks; the directory stores start and length.", "દરેક file સળંગ blocks રોકે છે; directory start અને length રાખે છે."),
        V("Main drawback of contiguous allocation?", "Contiguous allocation નો મુખ્ય ગેરફાયદો?", "External fragmentation and difficulty in growing a file.", "External fragmentation અને file વધારવામાં મુશ્કેલી."),
        V("How does linked allocation work?", "Linked allocation કેવી રીતે કામ કરે?", "Each block holds a pointer to the next block; the directory stores the first and last block.", "દરેક block આગળના block નો pointer રાખે છે; directory પહેલો અને છેલ્લો block રાખે છે."),
        V("What is FAT?", "FAT શું છે?", "File Allocation Table: a variation of linked allocation where all next pointers are kept in a table at the start of the disk (MS-DOS, USB drives).", "File Allocation Table: linked allocation નો પ્રકાર જેમાં બધા next pointers disk ની શરૂઆતમાં એક table માં રાખાય (MS-DOS, USB drives)."),
        V("What is an index block?", "Index block શું છે?", "In indexed allocation, a block that holds the addresses of all the data blocks of a file; entry i points to block i.", "Indexed allocation માં file ના બધા data blocks ના addresses રાખતો block; entry i block i તરફ point કરે."),
    ]},
    {"title": {"en": "Disk Structure and Scheduling", "gu": "Disk Structure અને Scheduling"}, "items": [
        V("Define track, sector and cylinder.", "Track, sector અને cylinder ની વ્યાખ્યા આપો.", "Track: a circle on a platter surface; sector: a fixed-size part of a track; cylinder: the set of tracks at one arm position on all surfaces.", "Track: platter surface પરનું વર્તુળ; sector: track નો fixed-size ભાગ; cylinder: એક arm position પર બધી surfaces ના tracks નો સમૂહ."),
        V("What is seek time?", "Seek time શું છે?", "The time for the disk arm to move the head to the required cylinder.", "Disk arm ને head જરૂરી cylinder પર લઈ જવામાં લાગતો સમય."),
        V("What is rotational latency?", "Rotational latency શું છે?", "The time waiting for the required sector to rotate under the head.", "જરૂરી sector head ની નીચે ફરીને આવે ત્યાં સુધીની રાહનો સમય."),
        V("Why is SCAN called the elevator algorithm?", "SCAN ને elevator algorithm શા માટે કહે છે?", "Like a lift, the head moves in one direction serving requests to the end, then reverses.", "Lift ની જેમ head એક દિશામાં છેડા સુધી requests સંતોષતો જાય, પછી દિશા બદલે."),
        V("How is C-SCAN different from SCAN?", "C-SCAN, SCAN થી કેવી રીતે જુદું?", "C-SCAN serves requests in one direction only; at the end it jumps back to the other end without serving, giving more uniform waiting time.", "C-SCAN requests માત્ર એક દિશામાં સંતોષે; છેડે પહોંચી સંતોષ્યા વગર બીજા છેડે jump કરે, તેથી waiting time વધુ એકસરખો રહે."),
        V("What is the difference between SCAN and LOOK?", "SCAN અને LOOK વચ્ચે તફાવત?", "SCAN goes to the end of the disk; LOOK reverses at the last request in that direction.", "SCAN disk ના છેડા સુધી જાય; LOOK તે દિશાની છેલ્લી request પર દિશા બદલે."),
    ]},
]

EXAM_QS = [
    X("Explain file attributes and file operations.", "File attributes અને file operations સમજાવો.", 4),
    X("Explain different file types with their extensions.", "જુદા જુદા file types તેમના extensions સાથે સમજાવો.", 3),
    X("Explain absolute and relative file paths with an example.", "Absolute અને relative file paths ઉદાહરણ સાથે સમજાવો.", 3),
    X("Explain file security and protection mechanisms.", "File security અને protection mechanisms સમજાવો.", 4),
    X("Explain single-level and two-level directory structures.", "Single-level અને two-level directory structures સમજાવો.", 4),
    X("Explain tree-structured directory with a diagram.", "Tree-structured directory આકૃતિ સાથે સમજાવો.", 4),
    X("Explain acyclic-graph and general graph directory structures.", "Acyclic-graph અને general graph directory structures સમજાવો.", 4),
    X("Explain contiguous, linked and indexed allocation methods.", "Contiguous, linked અને indexed allocation methods સમજાવો.", 7),
    X("Compare contiguous, linked and indexed allocation.", "Contiguous, linked અને indexed allocation ની સરખામણી કરો.", 3),
    X("Explain the physical structure of a disk.", "Disk નું physical structure સમજાવો.", 4),
    X("Define seek time, rotational latency and transfer time.", "Seek time, rotational latency અને transfer time ની વ્યાખ્યા આપો.", 3),
    X("Explain the SCAN disk scheduling algorithm with an example.", "SCAN disk scheduling algorithm ઉદાહરણ સાથે સમજાવો.", 4),
    X("Explain the C-SCAN disk scheduling algorithm with an example.", "C-SCAN disk scheduling algorithm ઉદાહરણ સાથે સમજાવો.", 4),
    X("Disk 0–199; queue 75, 90, 40, 135, 50, 170, 65, 10; head 46 moving left. Find total head movement using SCAN and C-SCAN.", "Disk 0–199; queue 75, 90, 40, 135, 50, 170, 65, 10; head 46 ડાબી બાજુ. SCAN અને C-SCAN વડે કુલ head movement શોધો.", 7),
    X("Differentiate between SCAN and C-SCAN.", "SCAN અને C-SCAN વચ્ચે તફાવત આપો.", 3),
]

assert len({n["id"] for n in NUMERICALS}) == 14
