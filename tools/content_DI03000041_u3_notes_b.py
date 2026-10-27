"""Fundamentals of Operating System (DI03000041) - Unit 3 notes part B: 3.3 Paging and segmentation;
3.4 Page replacement (demand paging, FIFO, LRU)."""
from content_DI03000011_u1_notes_a import T
from content_DI03000041_u1_notes import tbl

PS_EN = tbl(["Point", "Paging", "Segmentation"], [
    ("Division", "Fixed-size pages (by hardware)", "Variable-size segments (logical units)"),
    ("Done by", "OS / hardware; invisible to the programmer", "Compiler / programmer view"),
    ("Address", "(page number p, offset d)", "(segment number s, offset d)"),
    ("Table", "Page table: frame number", "Segment table: base + limit"),
    ("Fragmentation", "Internal (last page)", "External"),
    ("User view", "Not supported", "Supports the user's view (main, stack, data…)"),
    ("Sharing / protection", "Harder (page may mix code and data)", "Easy, per segment"),
    ("Size check", "Not needed (d always fits)", "d &lt; limit checked, else trap")])
PS_GU = tbl(["મુદ્દો", "Paging", "Segmentation"], [
    ("વિભાજન", "Fixed-size pages (hardware વડે)", "Variable-size segments (logical units)"),
    ("કોણ કરે", "OS / hardware; programmer ને દેખાતું નથી", "Compiler / programmer નો view"),
    ("Address", "(page number p, offset d)", "(segment number s, offset d)"),
    ("Table", "Page table: frame number", "Segment table: base + limit"),
    ("Fragmentation", "Internal (છેલ્લું page)", "External"),
    ("User view", "Support નથી", "User ના view ને support (main, stack, data…)"),
    ("Sharing / protection", "અઘરું (page માં code અને data ભળી શકે)", "સરળ, દરેક segment મુજબ"),
    ("Size check", "જરૂર નથી (d હંમેશા સમાય)", "d &lt; limit તપાસાય, નહીં તો trap")])

FL_EN = tbl(["Point", "FIFO", "LRU", "Optimal (OPT)"], [
    ("Victim page", "Oldest loaded page", "Page not used for the longest past time", "Page not used for the longest future time"),
    ("Needs", "Queue of load order", "Time of last use (counter / stack)", "Future reference string"),
    ("Implementation", "Simplest", "Harder; needs hardware help", "Not possible (only for comparison)"),
    ("Belady's anomaly", "Yes, can occur", "No (stack algorithm)", "No"),
    ("Faults (classic string, 3 frames)", "15", "12", "9")])
FL_GU = tbl(["મુદ્દો", "FIFO", "LRU", "Optimal (OPT)"], [
    ("Victim page", "સૌથી જૂનું load થયેલું page", "ભૂતકાળમાં સૌથી લાંબા સમયથી ન વપરાયેલું page", "ભવિષ્યમાં સૌથી લાંબા સમય સુધી ન વપરાનાર page"),
    ("જરૂર", "Load ક્રમની queue", "છેલ્લા ઉપયોગનો સમય (counter / stack)", "ભવિષ્યની reference string"),
    ("અમલ", "સૌથી સરળ", "અઘરો; hardware મદદ જોઈએ", "શક્ય નથી (માત્ર સરખામણી માટે)"),
    ("Belady's anomaly", "હા, થઈ શકે", "ના (stack algorithm)", "ના"),
    ("Faults (classic string, 3 frames)", "15", "12", "9")])

SEC_3_3 = {
    "title": {"en": "3.3 Non-contiguous Allocation: Paging and Segmentation", "gu": "3.3 Non-contiguous Allocation: Paging અને Segmentation"},
    "items": [
        T("3.3.1 Paging", "3.3.1 Paging",
          """<p><b>Paging</b> is a memory-management scheme that allows the physical address space of a process to be <b>non-contiguous</b>. It completely avoids external fragmentation and the need for compaction.</p>
<h4>Basic method</h4>
<ul>
<li><b>Physical memory</b> is divided into fixed-size blocks called <b>frames</b>.</li>
<li><b>Logical memory</b> (the process) is divided into blocks of the same size called <b>pages</b>.</li>
<li>Page size = frame size, a power of 2 (typically 4 KB; range 512 bytes to 1 GB).</li>
<li>To run a process of n pages, the OS finds n free frames (anywhere) and loads the pages into them.</li>
<li>A <b>page table</b> (one per process) stores, for every page, the frame in which it is loaded.</li>
<li>The OS keeps a <b>frame table</b> showing which frames are free or allocated.</li>
</ul>
<p>Example: a process of 4 pages (0–3) may be loaded as page 0 → frame 1, page 1 → frame 4, page 2 → frame 3, page 3 → frame 7. The pages are scattered, but the program sees one contiguous logical space.</p>
<h4>Advantages</h4>
<ul><li>No external fragmentation; any free frame can be used.</li><li>Easy allocation (just a list of free frames); no compaction.</li><li>Supports sharing of common code (reentrant code) and virtual memory.</li></ul>
<h4>Disadvantages</h4>
<ul><li><b>Internal fragmentation</b> in the last page (on average half a page per process).</li><li>Page table needs memory and each access needs an extra memory reference (solved with a <b>TLB</b>).</li></ul>""",
          """<p><b>Paging</b> એ memory-management પદ્ધતિ છે જે process ની physical address space ને <b>non-contiguous</b> (છૂટી છૂટી) રહેવા દે છે. તે external fragmentation અને compaction ની જરૂરિયાત સંપૂર્ણ ટાળે છે.</p>
<h4>મૂળ પદ્ધતિ</h4>
<ul>
<li><b>Physical memory</b> ને fixed-size blocks માં વહેંચાય છે જેને <b>frames</b> કહે છે.</li>
<li><b>Logical memory</b> (process) ને સરખા કદના blocks માં વહેંચાય છે જેને <b>pages</b> કહે છે.</li>
<li>Page size = frame size, 2 ની ઘાત (સામાન્ય રીતે 4 KB; range 512 bytes થી 1 GB).</li>
<li>n pages ની process ચલાવવા OS n free frames (ગમે ત્યાં) શોધી pages તેમાં load કરે.</li>
<li><b>Page table</b> (દરેક process માટે એક) દરેક page કઈ frame માં load છે તે રાખે છે.</li>
<li>OS <b>frame table</b> રાખે છે જે બતાવે કે કઈ frames free કે allocated છે.</li>
</ul>
<p>ઉદાહરણ: 4 pages (0–3) ની process આ રીતે load થઈ શકે: page 0 → frame 1, page 1 → frame 4, page 2 → frame 3, page 3 → frame 7. Pages વેરવિખેર છે, પણ program ને એક સળંગ logical space દેખાય છે.</p>
<h4>ફાયદા</h4>
<ul><li>External fragmentation નહીં; કોઈ પણ free frame વાપરી શકાય.</li><li>સરળ allocation (માત્ર free frames ની યાદી); compaction નહીં.</li><li>Common code (reentrant code) નું sharing અને virtual memory ને support.</li></ul>
<h4>ગેરફાયદા</h4>
<ul><li>છેલ્લા page માં <b>internal fragmentation</b> (સરેરાશ process દીઠ અડધું page).</li><li>Page table ને memory જોઈએ અને દરેક access માં એક વધારાનો memory reference (<b>TLB</b> વડે ઉકેલ).</li></ul>""",
          diagram="os3_paging"),
        T("3.3.2 Address Translation in Paging", "3.3.2 Paging માં Address Translation",
          """<p>Every logical address generated by the CPU is divided into two parts:</p>
<ul>
<li><b>Page number (p):</b> used as an index into the page table.</li>
<li><b>Page offset (d):</b> position of the byte within the page.</li>
</ul>
<p>If the logical address space is 2<sup>m</sup> and page size is 2<sup>n</sup>, the high-order <b>m − n bits</b> give p and the low-order <b>n bits</b> give d.</p>
<h4>Steps (paging hardware)</h4>
<ol>
<li>CPU generates logical address (p, d).</li>
<li>p = LA div page size, d = LA mod page size.</li>
<li>Page table[p] gives frame number <b>f</b>.</li>
<li>Physical address = <b>f × page size + d</b> (i.e. f replaces p; d is copied unchanged).</li>
</ol>
<h4>Worked example</h4>
<p>Page size = 1 KB (1024 bytes), page table: page 0 → 5, 1 → 6, 2 → 1, 3 → 2. Logical address 2500:</p>
<ul><li>p = 2500 div 1024 = 2, d = 2500 mod 1024 = 452.</li><li>f = page table[2] = 1.</li><li>PA = 1 × 1024 + 452 = <b>1476</b>.</li></ul>
<h4>Translation look-aside buffer (TLB)</h4>
<p>Keeping the page table in memory needs two memory accesses per reference. A <b>TLB</b> is a small, fast associative cache of recent (page, frame) pairs. On a <b>TLB hit</b> the frame is found immediately; on a <b>TLB miss</b> the page table in memory is used and the pair is added to the TLB.</p>
<p><b>Effective access time (EAT)</b> = h × (TLB time + memory time) + (1 − h) × (TLB time + 2 × memory time), where h is the hit ratio.</p>
<p><b>Protection:</b> each page-table entry has a <b>valid–invalid bit</b> and read/write bits; access to an invalid page causes a trap.</p>""",
          """<p>CPU એ બનાવેલું દરેક logical address બે ભાગમાં વહેંચાય છે:</p>
<ul>
<li><b>Page number (p):</b> page table માં index તરીકે વપરાય.</li>
<li><b>Page offset (d):</b> page ની અંદર byte નું સ્થાન.</li>
</ul>
<p>Logical address space 2<sup>m</sup> અને page size 2<sup>n</sup> હોય તો ઊંચા <b>m − n bits</b> p આપે અને નીચા <b>n bits</b> d આપે.</p>
<h4>પગલાં (paging hardware)</h4>
<ol>
<li>CPU logical address (p, d) બનાવે.</li>
<li>p = LA div page size, d = LA mod page size.</li>
<li>Page table[p] frame number <b>f</b> આપે.</li>
<li>Physical address = <b>f × page size + d</b> (એટલે કે p ની જગ્યાએ f આવે; d એમનો એમ copy થાય).</li>
</ol>
<h4>ઉકેલેલું ઉદાહરણ</h4>
<p>Page size = 1 KB (1024 bytes), page table: page 0 → 5, 1 → 6, 2 → 1, 3 → 2. Logical address 2500:</p>
<ul><li>p = 2500 div 1024 = 2, d = 2500 mod 1024 = 452.</li><li>f = page table[2] = 1.</li><li>PA = 1 × 1024 + 452 = <b>1476</b>.</li></ul>
<h4>Translation look-aside buffer (TLB)</h4>
<p>Page table memory માં રાખવાથી દરેક reference માટે બે memory accesses જોઈએ. <b>TLB</b> એ તાજેતરના (page, frame) જોડીઓનો નાનો, ઝડપી associative cache છે. <b>TLB hit</b> પર frame તરત મળે; <b>TLB miss</b> પર memory માંની page table વપરાય અને જોડી TLB માં ઉમેરાય.</p>
<p><b>Effective access time (EAT)</b> = h × (TLB time + memory time) + (1 − h) × (TLB time + 2 × memory time), જ્યાં h hit ratio છે.</p>
<p><b>Protection:</b> દરેક page-table entry માં <b>valid–invalid bit</b> અને read/write bits હોય; invalid page ના access પર trap થાય.</p>""",
          diagram="os3_paging_hw", examples=["os3n6", "os3n7", "os3n8"]),
        T("3.3.3 Segmentation", "3.3.3 Segmentation",
          """<p><b>Segmentation</b> is a memory-management scheme that supports the <b>programmer's (user's) view of memory</b>. A program is seen as a collection of logical units of <b>different sizes</b>, called <b>segments</b>: main program, functions, stack, symbol table, global data, arrays, etc.</p>
<h4>Basic method</h4>
<ul>
<li>Each segment has a <b>name (number)</b> and a <b>length</b>.</li>
<li>A logical address is a pair <b>&lt;segment number s, offset d&gt;</b>.</li>
<li>The compiler creates the segments automatically (e.g. code, global variables, heap, stack, C library).</li>
<li>Each segment is loaded into a contiguous area of memory, but different segments can be anywhere (non-contiguous).</li>
<li>A <b>segment table</b> stores for each segment:<ul><li><b>Base:</b> starting physical address of the segment.</li><li><b>Limit:</b> length of the segment.</li></ul></li>
</ul>
<h4>Advantages</h4>
<ul><li>Matches the user's view; segments can grow (e.g. stack).</li><li>Easy <b>protection</b> (code segment read-only) and <b>sharing</b> (a shared library segment).</li><li>No internal fragmentation.</li></ul>
<h4>Disadvantages</h4>
<ul><li><b>External fragmentation</b>, because segments are of variable size (needs best/first fit, compaction).</li><li>Large segments may be hard to place. Solution: <b>segmentation with paging</b> (used by Intel x86).</li></ul>""",
          """<p><b>Segmentation</b> એ memory-management પદ્ધતિ છે જે <b>programmer (user) ના memory view</b> ને support કરે છે. Program ને <b>જુદા જુદા કદના</b> logical units નો સમૂહ ગણાય છે જેને <b>segments</b> કહે છે: main program, functions, stack, symbol table, global data, arrays વગેરે.</p>
<h4>મૂળ પદ્ધતિ</h4>
<ul>
<li>દરેક segment ને <b>નામ (number)</b> અને <b>length</b> હોય.</li>
<li>Logical address એક જોડી છે <b>&lt;segment number s, offset d&gt;</b>.</li>
<li>Compiler segments આપમેળે બનાવે (દા.ત. code, global variables, heap, stack, C library).</li>
<li>દરેક segment memory ના એક સળંગ વિસ્તારમાં load થાય, પણ જુદા segments ગમે ત્યાં હોઈ શકે (non-contiguous).</li>
<li><b>Segment table</b> દરેક segment માટે રાખે:<ul><li><b>Base:</b> segment નું શરૂઆતનું physical address.</li><li><b>Limit:</b> segment ની length.</li></ul></li>
</ul>
<h4>ફાયદા</h4>
<ul><li>User ના view સાથે મેળ; segments વધી શકે (દા.ત. stack).</li><li>સરળ <b>protection</b> (code segment read-only) અને <b>sharing</b> (shared library segment).</li><li>Internal fragmentation નહીં.</li></ul>
<h4>ગેરફાયદા</h4>
<ul><li>Segments variable size ના હોવાથી <b>external fragmentation</b> (best/first fit, compaction જોઈએ).</li><li>મોટા segments મૂકવા મુશ્કેલ. ઉકેલ: <b>segmentation with paging</b> (Intel x86 માં વપરાય).</li></ul>""",
          diagram="os3_segment"),
        T("3.3.4 Address Translation in Segmentation", "3.3.4 Segmentation માં Address Translation",
          """<p>The <b>segmentation hardware</b> maps the two-dimensional logical address (s, d) to a one-dimensional physical address using the segment table.</p>
<h4>Steps</h4>
<ol>
<li>CPU generates logical address <b>(s, d)</b>.</li>
<li>Segment number s is used as an index into the segment table to get <b>base</b> and <b>limit</b>.</li>
<li>Check: <b>d &lt; limit?</b><ul><li>No → <b>trap</b> to OS (addressing error: offset beyond end of segment).</li><li>Yes → <b>physical address = base + d</b>.</li></ul></li>
</ol>
<p>Two registers help: <b>STBR</b> (segment-table base register) points to the segment table in memory, and <b>STLR</b> (segment-table length register) gives the number of segments; s must be &lt; STLR.</p>
<h4>Worked example</h4>
<p>Segment table: segment 2 → base 4300, limit 400; segment 3 → base 3200, limit 1100.</p>
<ul>
<li>(2, 53): 53 &lt; 400 ✓ → PA = 4300 + 53 = <b>4353</b>.</li>
<li>(3, 852): 852 &lt; 1100 ✓ → PA = 3200 + 852 = <b>4052</b>.</li>
<li>(2, 500): 500 ≥ 400 ✗ → <b>trap</b> (illegal address).</li>
</ul>
<p>Each segment-table entry can also hold protection bits (read / write / execute) and a valid bit.</p>""",
          """<p><b>Segmentation hardware</b> segment table વડે બે-પરિમાણી logical address (s, d) ને એક-પરિમાણી physical address માં map કરે છે.</p>
<h4>પગલાં</h4>
<ol>
<li>CPU logical address <b>(s, d)</b> બનાવે.</li>
<li>Segment number s ને segment table માં index તરીકે વાપરી <b>base</b> અને <b>limit</b> મેળવાય.</li>
<li>તપાસ: <b>d &lt; limit?</b><ul><li>ના → OS ને <b>trap</b> (addressing error: offset segment ના અંત પછી).</li><li>હા → <b>physical address = base + d</b>.</li></ul></li>
</ol>
<p>બે registers મદદ કરે: <b>STBR</b> (segment-table base register) memory માંની segment table તરફ point કરે, અને <b>STLR</b> (segment-table length register) segments ની સંખ્યા આપે; s &lt; STLR હોવું જોઈએ.</p>
<h4>ઉકેલેલું ઉદાહરણ</h4>
<p>Segment table: segment 2 → base 4300, limit 400; segment 3 → base 3200, limit 1100.</p>
<ul>
<li>(2, 53): 53 &lt; 400 ✓ → PA = 4300 + 53 = <b>4353</b>.</li>
<li>(3, 852): 852 &lt; 1100 ✓ → PA = 3200 + 852 = <b>4052</b>.</li>
<li>(2, 500): 500 ≥ 400 ✗ → <b>trap</b> (illegal address).</li>
</ul>
<p>દરેક segment-table entry માં protection bits (read / write / execute) અને valid bit પણ રાખી શકાય.</p>""",
          diagram="os3_seg_hw", examples=["os3n9"]),
        T("3.3.5 Paging vs Segmentation", "3.3.5 Paging vs Segmentation",
          """<p>Both are <b>non-contiguous</b> allocation methods, but they divide memory differently: paging uses fixed-size physical blocks, segmentation uses variable-size logical blocks.</p>
""" + PS_EN + """
<p><b>Segmentation with paging:</b> each segment is itself divided into pages, combining the user view of segmentation with the no-external-fragmentation benefit of paging (e.g. Intel IA-32).</p>""",
          """<p>બંને <b>non-contiguous</b> allocation પદ્ધતિઓ છે, પણ memory ને જુદી રીતે વહેંચે છે: paging fixed-size physical blocks વાપરે, segmentation variable-size logical blocks વાપરે.</p>
""" + PS_GU + """
<p><b>Segmentation with paging:</b> દરેક segment ને pages માં વહેંચાય, જેથી segmentation નો user view અને paging નો no-external-fragmentation લાભ બંને મળે (દા.ત. Intel IA-32).</p>"""),
    ]}

SEC_3_4 = {
    "title": {"en": "3.4 Page Replacement", "gu": "3.4 Page Replacement"},
    "items": [
        T("3.4.1 Virtual Memory, Demand Paging and Page Fault", "3.4.1 Virtual Memory, Demand Paging અને Page Fault",
          """<p><b>Virtual memory</b> is a technique that allows a process to execute even if it is <b>not completely in main memory</b>. Programs can be larger than physical memory, more programs run at once, and less I/O is needed to load programs.</p>
<h4>Demand paging</h4>
<p>In <b>demand paging</b>, a page is loaded into memory <b>only when it is needed</b> (on demand), not in advance. A <b>lazy swapper (pager)</b> never brings a page into memory unless it will be used. The <b>valid–invalid bit</b> in the page table tells whether the page is in memory (v) or not (i).</p>
<h4>Page fault</h4>
<p>A <b>page fault</b> occurs when a process accesses a page that is <b>not in main memory</b> (invalid bit). Steps to handle it:</p>
<ol>
<li>The process references a page; the page-table entry is invalid → <b>trap</b> to the OS.</li>
<li>The OS checks: if the reference is illegal, terminate the process; if legal but not in memory, page it in.</li>
<li>Find a <b>free frame</b> (if none, use a <b>page-replacement algorithm</b> to choose a victim).</li>
<li>Schedule a disk operation to read the page from the <b>backing store</b> into the frame.</li>
<li>Update the page table (frame number, valid bit = v).</li>
<li><b>Restart the instruction</b> that caused the fault.</li>
</ol>
<h4>Page replacement</h4>
<p>When no frame is free, the OS selects a <b>victim page</b>, writes it to disk if it was modified (<b>dirty / modify bit</b>), and loads the new page in its place. A good algorithm gives the <b>lowest page-fault rate</b>. Algorithms are evaluated on a <b>reference string</b> (sequence of page numbers) with a given number of frames.</p>
<p><b>Thrashing:</b> if a process does not have enough frames, it page-faults continuously and spends more time paging than executing.</p>""",
          """<p><b>Virtual memory</b> એવી પદ્ધતિ છે જે process <b>સંપૂર્ણ main memory માં ન હોય</b> તો પણ તેને ચલાવવા દે છે. Programs physical memory કરતાં મોટા હોઈ શકે, એક સાથે વધુ programs ચાલે, અને programs load કરવા ઓછો I/O જોઈએ.</p>
<h4>Demand paging</h4>
<p><b>Demand paging</b> માં page અગાઉથી નહીં, પણ <b>જરૂર પડે ત્યારે જ</b> (on demand) memory માં load થાય છે. <b>Lazy swapper (pager)</b> જે page વપરાશે નહીં તેને ક્યારેય memory માં લાવતો નથી. Page table નો <b>valid–invalid bit</b> કહે છે કે page memory માં છે (v) કે નથી (i).</p>
<h4>Page fault</h4>
<p>Process <b>main memory માં ન હોય</b> (invalid bit) તેવું page access કરે ત્યારે <b>page fault</b> થાય. તેને handle કરવાના પગલાં:</p>
<ol>
<li>Process page નો reference કરે; page-table entry invalid → OS ને <b>trap</b>.</li>
<li>OS તપાસે: reference ગેરકાયદે હોય તો process terminate; કાયદેસર પણ memory માં ન હોય તો page in કરે.</li>
<li><b>Free frame</b> શોધે (ન હોય તો victim પસંદ કરવા <b>page-replacement algorithm</b> વાપરે).</li>
<li><b>Backing store</b> માંથી page ને frame માં વાંચવા disk operation schedule કરે.</li>
<li>Page table update કરે (frame number, valid bit = v).</li>
<li>Fault કરનાર <b>instruction ફરી શરૂ</b> કરે.</li>
</ol>
<h4>Page replacement</h4>
<p>કોઈ frame free ન હોય ત્યારે OS <b>victim page</b> પસંદ કરે, તે બદલાયું હોય (<b>dirty / modify bit</b>) તો disk પર લખે, અને તેની જગ્યાએ નવું page load કરે. સારો algorithm <b>ઓછામાં ઓછો page-fault rate</b> આપે. Algorithms ને આપેલી frames સાથે <b>reference string</b> (page numbers નો ક્રમ) પર મૂલવાય છે.</p>
<p><b>Thrashing:</b> process પાસે પૂરતી frames ન હોય તો તે સતત page fault કરે અને execution કરતાં paging માં વધુ સમય ગાળે.</p>""",
          diagram="os3_pagefault"),
        T("3.4.2 FIFO Page Replacement and Belady's Anomaly", "3.4.2 FIFO Page Replacement અને Belady's Anomaly",
          """<p><b>FIFO (First In First Out)</b> is the simplest page-replacement algorithm. When a page must be replaced, the <b>oldest page</b> (the one brought into memory first) is chosen as the victim.</p>
<h4>Working</h4>
<ul>
<li>The OS keeps a <b>FIFO queue</b> of all pages in memory.</li>
<li>A new page is inserted at the tail; the page at the <b>head</b> is replaced.</li>
<li>If the referenced page is already in memory → <b>hit</b> (queue does not change).</li>
</ul>
<h4>Example (Practical 4)</h4>
<p>Reference string 1, 2, 3, 4, 5, 1, 3, 1, 6, 3, 2, 3 with 4 frames → <b>9 page faults</b> using FIFO (see the solved numerical).</p>
<h4>Advantages</h4>
<ul><li>Easy to understand and implement; low overhead.</li></ul>
<h4>Disadvantages</h4>
<ul><li>Performance is not always good: the oldest page may be a heavily used page (e.g. a variable initialised early and used all the time).</li><li>Suffers from <b>Belady's anomaly</b>.</li></ul>
<h4>Belady's anomaly</h4>
<p>Normally, giving more frames should reduce page faults. <b>Belady's anomaly</b> is the unexpected situation in which the <b>page-fault rate increases when the number of frames increases</b>. It occurs with FIFO.</p>
<p>Example: reference string 1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5 → FIFO gives <b>9 faults with 3 frames</b> but <b>10 faults with 4 frames</b>.</p>
<p>LRU and Optimal are <b>stack algorithms</b> (the set of pages with n frames is always a subset of the set with n + 1 frames), so they never suffer from Belady's anomaly.</p>""",
          """<p><b>FIFO (First In First Out)</b> એ સૌથી સરળ page-replacement algorithm છે. Page બદલવું પડે ત્યારે <b>સૌથી જૂનું page</b> (memory માં પહેલું આવેલું) victim તરીકે પસંદ થાય છે.</p>
<h4>કાર્યપદ્ધતિ</h4>
<ul>
<li>OS memory માંના બધા pages ની <b>FIFO queue</b> રાખે છે.</li>
<li>નવું page tail પર ઉમેરાય; <b>head</b> પરનું page બદલાય.</li>
<li>Reference થયેલું page memory માં પહેલેથી હોય → <b>hit</b> (queue બદલાતી નથી).</li>
</ul>
<h4>ઉદાહરણ (Practical 4)</h4>
<p>Reference string 1, 2, 3, 4, 5, 1, 3, 1, 6, 3, 2, 3 અને 4 frames → FIFO વડે <b>9 page faults</b> (ઉકેલેલું numerical જુઓ).</p>
<h4>ફાયદા</h4>
<ul><li>સમજવા અને અમલ કરવા સરળ; overhead ઓછો.</li></ul>
<h4>ગેરફાયદા</h4>
<ul><li>Performance હંમેશા સારું નથી: સૌથી જૂનું page ખૂબ વપરાતું page હોઈ શકે (દા.ત. શરૂઆતમાં initialise થયેલો અને સતત વપરાતો variable).</li><li><b>Belady's anomaly</b> થાય છે.</li></ul>
<h4>Belady's anomaly</h4>
<p>સામાન્ય રીતે વધુ frames આપવાથી page faults ઘટવા જોઈએ. <b>Belady's anomaly</b> એ અણધારી સ્થિતિ છે જેમાં <b>frames ની સંખ્યા વધારતાં page-fault rate વધે</b>. તે FIFO માં થાય છે.</p>
<p>ઉદાહરણ: reference string 1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5 → FIFO <b>3 frames સાથે 9 faults</b> પણ <b>4 frames સાથે 10 faults</b> આપે.</p>
<p>LRU અને Optimal <b>stack algorithms</b> છે (n frames સાથેના pages નો set હંમેશા n + 1 frames સાથેના set નો subset હોય), તેથી તેમાં Belady's anomaly ક્યારેય થતી નથી.</p>""",
          diagram="os3_fifo", examples=["os3n10", "os3n12", "os3n14"]),
        T("3.4.3 LRU (Least Recently Used) Page Replacement", "3.4.3 LRU (Least Recently Used) Page Replacement",
          """<p><b>LRU</b> replaces the page that has <b>not been used for the longest period of time</b>. It uses the recent past as an approximation of the near future (principle of <b>locality</b>): a page not used for a long time is unlikely to be used soon.</p>
<h4>Working</h4>
<ul>
<li>Each page is associated with the time of its <b>last use</b>.</li>
<li>On a fault with no free frame, the page with the <b>oldest last-use time</b> is replaced.</li>
<li>On a hit, the page becomes the <b>most recently used</b> (its time is updated) – this is the key difference from FIFO.</li>
</ul>
<h4>Implementation</h4>
<ul>
<li><b>Counters:</b> a logical clock is copied into the page-table entry on every reference; replace the page with the smallest time value.</li>
<li><b>Stack:</b> keep a stack of page numbers; a referenced page is moved to the top; the LRU page is always at the bottom.</li>
<li>Both need hardware support; approximations such as the <b>reference bit</b> / <b>second-chance (clock)</b> algorithm are used in practice.</li>
</ul>
<h4>Example (Practical 4)</h4>
<p>Reference string 1, 2, 3, 4, 5, 1, 3, 1, 6, 3, 2, 3 with 4 frames → <b>8 page faults</b> using LRU (FIFO gave 9). For the classic string 7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1 with 3 frames: LRU = 12, FIFO = 15.</p>
<h4>Advantages / disadvantages</h4>
<ul><li><b>+</b> Good performance, close to optimal; no Belady's anomaly.</li><li><b>−</b> Costly to implement: needs a timestamp or stack update on every memory reference.</li></ul>
<h4>Optimal (OPT) – for comparison</h4>
<p>Replace the page that <b>will not be used for the longest time in the future</b>. It gives the lowest possible fault rate but needs future knowledge, so it is used only as a benchmark (classic string: 9 faults).</p>""",
          """<p><b>LRU</b> એવું page બદલે છે જે <b>સૌથી લાંબા સમયથી વપરાયું નથી</b>. તે નજીકના ભવિષ્યના અંદાજ તરીકે તાજેતરના ભૂતકાળનો ઉપયોગ કરે છે (<b>locality</b> નો સિદ્ધાંત): લાંબા સમયથી ન વપરાયેલું page જલ્દી વપરાય તેવી શક્યતા ઓછી છે.</p>
<h4>કાર્યપદ્ધતિ</h4>
<ul>
<li>દરેક page સાથે તેના <b>છેલ્લા ઉપયોગનો સમય</b> જોડાય.</li>
<li>Free frame વગર fault થાય ત્યારે <b>સૌથી જૂના last-use time</b> વાળું page બદલાય.</li>
<li>Hit પર page <b>most recently used</b> બને (તેનો time update થાય) – FIFO થી આ મુખ્ય તફાવત છે.</li>
</ul>
<h4>અમલ</h4>
<ul>
<li><b>Counters:</b> દરેક reference પર logical clock ને page-table entry માં copy કરાય; સૌથી નાની time value વાળું page બદલાય.</li>
<li><b>Stack:</b> page numbers નો stack રાખો; reference થયેલું page top પર ખસે; LRU page હંમેશા bottom પર.</li>
<li>બંનેને hardware support જોઈએ; વ્યવહારમાં <b>reference bit</b> / <b>second-chance (clock)</b> algorithm જેવા અંદાજો વપરાય.</li>
</ul>
<h4>ઉદાહરણ (Practical 4)</h4>
<p>Reference string 1, 2, 3, 4, 5, 1, 3, 1, 6, 3, 2, 3 અને 4 frames → LRU વડે <b>8 page faults</b> (FIFO એ 9 આપ્યા). Classic string 7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1 અને 3 frames માટે: LRU = 12, FIFO = 15.</p>
<h4>ફાયદા / ગેરફાયદા</h4>
<ul><li><b>+</b> સારું performance, optimal ની નજીક; Belady's anomaly નહીં.</li><li><b>−</b> અમલ મોંઘો: દરેક memory reference પર timestamp કે stack update જોઈએ.</li></ul>
<h4>Optimal (OPT) – સરખામણી માટે</h4>
<p>એવું page બદલો જે <b>ભવિષ્યમાં સૌથી લાંબા સમય સુધી વપરાશે નહીં</b>. તે શક્ય તેટલો ઓછો fault rate આપે પણ ભવિષ્યની જાણકારી જોઈએ, તેથી માત્ર benchmark તરીકે વપરાય (classic string: 9 faults).</p>""",
          diagram="os3_lru", examples=["os3n11", "os3n13"]),
        T("3.4.4 Comparison of FIFO, LRU and Optimal", "3.4.4 FIFO, LRU અને Optimal ની સરખામણી",
          """<p>The three algorithms differ only in how they choose the victim page when memory is full.</p>
""" + FL_EN + """
<h4>How to solve a page-replacement numerical (exam method)</h4>
<ol>
<li>Draw a table: one column per reference, one row per frame.</li>
<li>For each reference: if the page is in a frame → hit (write H or leave blank); otherwise → fault (F).</li>
<li>If a frame is free, load the page there; else choose the victim by the algorithm rule (FIFO: oldest loaded; LRU: least recently used; OPT: used farthest in future).</li>
<li>Count the faults. <b>Page-fault rate</b> = faults ÷ references; <b>hit ratio</b> = hits ÷ references.</li>
</ol>
<p>Practical 4 (12 references, 4 frames): FIFO 9 faults (75%), LRU 8 faults (66.7%), OPT 6 faults (50%).</p>""",
          """<p>ત્રણેય algorithms માત્ર memory ભરાઈ જાય ત્યારે victim page કેવી રીતે પસંદ કરે છે તેમાં જ જુદા પડે છે.</p>
""" + FL_GU + """
<h4>Page-replacement numerical કેવી રીતે ઉકેલવું (exam પદ્ધતિ)</h4>
<ol>
<li>Table દોરો: દરેક reference માટે એક column, દરેક frame માટે એક row.</li>
<li>દરેક reference માટે: page કોઈ frame માં હોય → hit (H લખો કે ખાલી છોડો); નહીં તો → fault (F).</li>
<li>Frame free હોય તો page ત્યાં load કરો; નહીં તો algorithm ના નિયમ મુજબ victim પસંદ કરો (FIFO: સૌથી જૂનું load; LRU: least recently used; OPT: ભવિષ્યમાં સૌથી દૂર વપરાનાર).</li>
<li>Faults ગણો. <b>Page-fault rate</b> = faults ÷ references; <b>hit ratio</b> = hits ÷ references.</li>
</ol>
<p>Practical 4 (12 references, 4 frames): FIFO 9 faults (75%), LRU 8 faults (66.7%), OPT 6 faults (50%).</p>"""),
    ]}
