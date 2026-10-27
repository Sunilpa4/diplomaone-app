"""Fundamentals of Operating System (DI03000041) - Unit 4 notes part B: 4.3 Disk space allocation methods;
4.4 Secondary storage structure and disk scheduling (SCAN, C-SCAN)."""
from content_DI03000011_u1_notes_a import T
from content_DI03000041_u1_notes import tbl

ALLOC_EN = tbl(["Point", "Contiguous", "Linked", "Indexed"], [
    ("Directory stores", "Start, length", "First (and last) block", "Index block address"),
    ("Sequential access", "Fast", "Fast", "Fast"),
    ("Direct access", "Yes (start + i)", "No (follow pointers)", "Yes (via index block)"),
    ("External fragmentation", "Yes", "No", "No"),
    ("File growth", "Difficult", "Easy", "Easy (until index full)"),
    ("Space overhead", "None", "Pointer in every block", "Index block per file"),
    ("Reliability", "Good", "Poor (broken pointer)", "Good (index block is critical)"),
    ("Example", "CD-ROM, IBM VM/CMS", "FAT (MS-DOS)", "UNIX inode, NTFS")])
ALLOC_GU = tbl(["મુદ્દો", "Contiguous", "Linked", "Indexed"], [
    ("Directory રાખે", "Start, length", "પહેલો (અને છેલ્લો) block", "Index block address"),
    ("Sequential access", "ઝડપી", "ઝડપી", "ઝડપી"),
    ("Direct access", "હા (start + i)", "ના (pointers અનુસરવા)", "હા (index block વડે)"),
    ("External fragmentation", "હા", "ના", "ના"),
    ("File growth", "મુશ્કેલ", "સરળ", "સરળ (index ભરાય ત્યાં સુધી)"),
    ("Space overhead", "નહીં", "દરેક block માં pointer", "File દીઠ index block"),
    ("Reliability", "સારી", "નબળી (તૂટેલો pointer)", "સારી (index block મહત્વનો)"),
    ("ઉદાહરણ", "CD-ROM, IBM VM/CMS", "FAT (MS-DOS)", "UNIX inode, NTFS")])

SC_EN = tbl(["Point", "SCAN", "C-SCAN"], [
    ("Direction of service", "Both directions", "One direction only"),
    ("At the disk end", "Reverses and serves on the way back", "Jumps to the other end without serving"),
    ("Waiting time", "Less uniform (middle tracks favoured)", "More uniform"),
    ("Head movement", "Usually less", "More (return jump)"),
    ("Practical 5 (head 46, left)", "216", "394 (195 without jump)"),
    ("Variant", "LOOK (196)", "C-LOOK (316)")])
SC_GU = tbl(["મુદ્દો", "SCAN", "C-SCAN"], [
    ("Service ની દિશા", "બંને દિશાઓ", "માત્ર એક દિશા"),
    ("Disk ના છેડે", "દિશા બદલી પાછા વળતાં service", "Service વગર બીજા છેડે jump"),
    ("Waiting time", "ઓછો એકસરખો (વચ્ચેના tracks ને ફાયદો)", "વધુ એકસરખો"),
    ("Head movement", "સામાન્ય રીતે ઓછું", "વધુ (return jump)"),
    ("Practical 5 (head 46, ડાબી)", "216", "394 (jump વગર 195)"),
    ("પ્રકાર", "LOOK (196)", "C-LOOK (316)")])

SEC_4_3 = {
    "title": {"en": "4.3 Disk Space Allocation Methods", "gu": "4.3 Disk Space Allocation Methods"},
    "items": [
        T("4.3.1 Contiguous Allocation", "4.3.1 Contiguous Allocation",
          """<p>Allocation methods decide <b>how disk blocks are allocated to files</b> so that disk space is used effectively and files can be accessed quickly. The three main methods are contiguous, linked and indexed.</p>
<p>In <b>contiguous allocation</b>, each file occupies a set of <b>consecutive blocks</b> on the disk. If a file is n blocks long and starts at block b, it occupies blocks b, b + 1, …, b + n − 1. The directory entry stores the <b>starting block</b> and the <b>length</b>.</p>
<p>Example: file <code>tr</code> starts at 14 with length 3 → blocks 14, 15, 16; file <code>mail</code> starts at 19 with length 6 → blocks 19 to 24.</p>
<h4>Advantages</h4>
<ul>
<li><b>Sequential and direct access</b> are both easy and fast: logical block i is at physical block b + i.</li>
<li>Minimum head movement (blocks are adjacent), so very good performance.</li>
<li>Simple: only start and length are stored.</li>
</ul>
<h4>Disadvantages</h4>
<ul>
<li><b>External fragmentation:</b> free space is broken into small holes (same as dynamic memory partitions); first fit / best fit are used, and <b>compaction</b> (defragmentation) may be needed.</li>
<li>The <b>file size must be known</b> when it is created; a file is <b>hard to grow</b> if the next blocks are used (it may need to be copied to a bigger hole).</li>
<li>Over-estimating size causes internal waste.</li>
</ul>
<p>A modified scheme allocates an <b>extent</b> (another contiguous chunk) when the file grows.</p>""",
          """<p>Allocation methods નક્કી કરે છે કે <b>files ને disk blocks કેવી રીતે ફાળવવા</b>, જેથી disk space નો અસરકારક ઉપયોગ થાય અને files ઝડપથી access થાય. ત્રણ મુખ્ય પદ્ધતિઓ છે contiguous, linked અને indexed.</p>
<p><b>Contiguous allocation</b> માં દરેક file disk પર <b>સળંગ blocks</b> નો સમૂહ રોકે છે. File n blocks લાંબી હોય અને block b થી શરૂ થાય તો તે blocks b, b + 1, …, b + n − 1 રોકે. Directory entry <b>starting block</b> અને <b>length</b> રાખે છે.</p>
<p>ઉદાહરણ: file <code>tr</code> 14 થી શરૂ, length 3 → blocks 14, 15, 16; file <code>mail</code> 19 થી શરૂ, length 6 → blocks 19 થી 24.</p>
<h4>ફાયદા</h4>
<ul>
<li><b>Sequential અને direct access</b> બંને સરળ અને ઝડપી: logical block i physical block b + i પર છે.</li>
<li>ઓછામાં ઓછું head movement (blocks બાજુ બાજુમાં), તેથી ખૂબ સારું performance.</li>
<li>સરળ: માત્ર start અને length રખાય.</li>
</ul>
<h4>ગેરફાયદા</h4>
<ul>
<li><b>External fragmentation:</b> free space નાના holes માં તૂટી જાય (dynamic memory partitions જેવું); first fit / best fit વપરાય, અને <b>compaction</b> (defragmentation) ની જરૂર પડી શકે.</li>
<li>File બનાવતી વખતે <b>file size ખબર હોવી જોઈએ</b>; આગળના blocks વપરાયેલા હોય તો file <b>વધારવી મુશ્કેલ</b> (મોટા hole માં copy કરવી પડે).</li>
<li>કદ વધુ ધારવાથી અંદરનો બગાડ થાય.</li>
</ul>
<p>સુધારેલી પદ્ધતિમાં file વધે ત્યારે <b>extent</b> (બીજો સળંગ ટુકડો) ફાળવાય છે.</p>""",
          diagram="os4_contig"),
        T("4.3.2 Linked Allocation", "4.3.2 Linked Allocation",
          """<p>In <b>linked allocation</b>, each file is a <b>linked list of disk blocks</b>; the blocks may be <b>scattered anywhere</b> on the disk. The directory contains pointers to the <b>first and last blocks</b> of the file. Each block contains a <b>pointer to the next block</b> (the last block has −1 / null).</p>
<p>Example: file <code>jeep</code> starts at block 9 → 16 → 1 → 10 → 25 (end). If a block is 512 bytes and a pointer is 4 bytes, the user sees 508 data bytes per block.</p>
<h4>Working</h4>
<ul><li><b>Create:</b> new directory entry with first-block pointer = null, size 0.</li><li><b>Write:</b> take a free block from the free-space list, write data, and link it to the end of the file.</li><li><b>Read:</b> follow the pointers block by block.</li></ul>
<h4>Advantages</h4>
<ul><li><b>No external fragmentation</b>: any free block can be used.</li><li>File size need not be declared; a file can <b>grow easily</b>.</li><li>No compaction needed.</li></ul>
<h4>Disadvantages</h4>
<ul>
<li>Efficient only for <b>sequential access</b>; finding block i needs i disk reads (no direct access).</li>
<li><b>Space for pointers</b> in every block (solution: allocate <b>clusters</b> of blocks).</li>
<li><b>Reliability:</b> if a pointer is lost or damaged, the rest of the file is lost.</li>
</ul>
<h4>File Allocation Table (FAT)</h4>
<p>An important variation used by MS-DOS and USB drives: a table at the beginning of the volume has one entry per disk block; the entry contains the number of the <b>next block</b> of the file. The directory entry holds the first block number. Since the FAT can be cached in memory, random access becomes faster.</p>""",
          """<p><b>Linked allocation</b> માં દરેક file <b>disk blocks નું linked list</b> છે; blocks disk પર <b>ગમે ત્યાં વેરવિખેર</b> હોઈ શકે. Directory માં file ના <b>પહેલા અને છેલ્લા blocks</b> ના pointers હોય. દરેક block માં <b>આગળના block નો pointer</b> હોય (છેલ્લા block માં −1 / null).</p>
<p>ઉદાહરણ: file <code>jeep</code> block 9 થી શરૂ → 16 → 1 → 10 → 25 (અંત). Block 512 bytes અને pointer 4 bytes હોય તો user ને block દીઠ 508 data bytes દેખાય.</p>
<h4>કાર્યપદ્ધતિ</h4>
<ul><li><b>Create:</b> first-block pointer = null, size 0 સાથે નવી directory entry.</li><li><b>Write:</b> free-space list માંથી free block લઈ, data લખી, file ના અંતે link કરવો.</li><li><b>Read:</b> pointers ને block દર block અનુસરવા.</li></ul>
<h4>ફાયદા</h4>
<ul><li><b>External fragmentation નહીં</b>: કોઈ પણ free block વાપરી શકાય.</li><li>File size જાહેર કરવી ન પડે; file <b>સરળતાથી વધી</b> શકે.</li><li>Compaction ની જરૂર નહીં.</li></ul>
<h4>ગેરફાયદા</h4>
<ul>
<li>માત્ર <b>sequential access</b> માટે કાર્યક્ષમ; block i શોધવા i disk reads જોઈએ (direct access નહીં).</li>
<li>દરેક block માં <b>pointers માટે જગ્યા</b> (ઉકેલ: blocks ના <b>clusters</b> ફાળવવા).</li>
<li><b>Reliability:</b> pointer ખોવાય કે બગડે તો file નો બાકીનો ભાગ ખોવાય.</li>
</ul>
<h4>File Allocation Table (FAT)</h4>
<p>MS-DOS અને USB drives માં વપરાતો મહત્વનો પ્રકાર: volume ની શરૂઆતમાં table હોય જેમાં દરેક disk block ની એક entry હોય; entry માં file ના <b>આગળના block</b> નો નંબર હોય. Directory entry પહેલો block number રાખે. FAT memory માં cache કરી શકાય, તેથી random access ઝડપી બને.</p>""",
          diagram="os4_linked"),
        T("4.3.3 Indexed Allocation", "4.3.3 Indexed Allocation",
          """<p>Linked allocation solves external fragmentation but cannot support direct access, because the pointers are scattered with the blocks. <b>Indexed allocation</b> brings all the pointers together into one location: the <b>index block</b>.</p>
<h4>Working</h4>
<ul>
<li>Each file has its own <b>index block</b>, an array of disk-block addresses.</li>
<li>The i<sup>th</sup> entry of the index block points to the i<sup>th</sup> block of the file.</li>
<li>The directory contains the address of the index block.</li>
<li>To read block i, read the index block, take entry i, and read that block.</li>
<li>When the file is created, all entries are −1 (null); when block i is first written, a free block is taken and its address put in entry i.</li>
</ul>
<p>Example: file <code>jeep</code> has index block 19 containing 9, 16, 1, 10, 25, −1, −1, −1.</p>
<h4>Advantages</h4>
<ul><li><b>Direct access</b> without external fragmentation.</li><li>Any free block can be used; files grow easily.</li></ul>
<h4>Disadvantages</h4>
<ul><li><b>Wasted space</b>: a whole index block is needed even for a 1–2 block file (pointer overhead greater than linked).</li><li>Index block size limits the file size; an extra read for the index block (unless cached).</li></ul>
<h4>Schemes for large files</h4>
<ul>
<li><b>Linked scheme:</b> index blocks are linked together; the last entry points to the next index block.</li>
<li><b>Multilevel index:</b> a first-level index block points to second-level index blocks, which point to data blocks (1 KB blocks, 4-byte pointers → 256 × 256 blocks = 64 MB).</li>
<li><b>Combined scheme (UNIX inode):</b> 12 direct pointers plus single, double and triple indirect pointers.</li>
</ul>""",
          """<p>Linked allocation external fragmentation ઉકેલે છે પણ direct access support કરી શકતું નથી, કારણ કે pointers blocks સાથે વેરવિખેર છે. <b>Indexed allocation</b> બધા pointers ને એક જગ્યાએ ભેગા કરે છે: <b>index block</b>.</p>
<h4>કાર્યપદ્ધતિ</h4>
<ul>
<li>દરેક file પાસે પોતાનો <b>index block</b> હોય, જે disk-block addresses નો array છે.</li>
<li>Index block ની i<sup>મી</sup> entry file ના i<sup>મા</sup> block તરફ point કરે.</li>
<li>Directory માં index block નું address હોય.</li>
<li>Block i વાંચવા index block વાંચો, entry i લો, અને તે block વાંચો.</li>
<li>File બને ત્યારે બધી entries −1 (null) હોય; block i પહેલી વાર લખાય ત્યારે free block લઈ તેનું address entry i માં મુકાય.</li>
</ul>
<p>ઉદાહરણ: file <code>jeep</code> નો index block 19 છે જેમાં 9, 16, 1, 10, 25, −1, −1, −1 છે.</p>
<h4>ફાયદા</h4>
<ul><li>External fragmentation વગર <b>direct access</b>.</li><li>કોઈ પણ free block વાપરી શકાય; files સરળતાથી વધે.</li></ul>
<h4>ગેરફાયદા</h4>
<ul><li><b>જગ્યાનો બગાડ</b>: 1–2 block ની file માટે પણ આખો index block જોઈએ (pointer overhead linked કરતાં વધુ).</li><li>Index block નું કદ file size મર્યાદિત કરે; index block માટે વધારાનો read (cache ન હોય તો).</li></ul>
<h4>મોટી files માટેની પદ્ધતિઓ</h4>
<ul>
<li><b>Linked scheme:</b> index blocks એકબીજા સાથે link થાય; છેલ્લી entry આગળના index block તરફ point કરે.</li>
<li><b>Multilevel index:</b> first-level index block second-level index blocks તરફ point કરે, જે data blocks તરફ point કરે (1 KB blocks, 4-byte pointers → 256 × 256 blocks = 64 MB).</li>
<li><b>Combined scheme (UNIX inode):</b> 12 direct pointers ઉપરાંત single, double અને triple indirect pointers.</li>
</ul>""",
          diagram="os4_indexed", examples=["os4n13", "os4n14"]),
        T("4.3.4 Comparison of Allocation Methods", "4.3.4 Allocation Methods ની સરખામણી",
          """<p>The choice depends on how files are accessed: contiguous is best for small or read-only files with direct access, linked for sequential files that grow, and indexed for large files needing direct access.</p>
""" + ALLOC_EN + """
<p>Many systems combine methods: contiguous for small files and indexed for large ones.</p>""",
          """<p>પસંદગી files કેવી રીતે access થાય છે તેના પર આધાર રાખે: direct access વાળી નાની કે read-only files માટે contiguous, વધતી sequential files માટે linked, અને direct access જોઈતી મોટી files માટે indexed શ્રેષ્ઠ છે.</p>
""" + ALLOC_GU + """
<p>ઘણી systems પદ્ધતિઓ ભેગી કરે છે: નાની files માટે contiguous અને મોટી files માટે indexed.</p>"""),
    ]}

SEC_4_4 = {
    "title": {"en": "4.4 Secondary Storage Structure", "gu": "4.4 Secondary Storage Structure"},
    "items": [
        T("4.4.1 Physical Structure of Disk", "4.4.1 Disk નું Physical Structure",
          """<p>Magnetic disks (hard disk drives, HDD) provide the bulk of secondary storage in computers.</p>
<h4>Parts of a disk</h4>
<ul>
<li><b>Platters:</b> flat circular plates coated with magnetic material on both surfaces; information is recorded magnetically.</li>
<li><b>Spindle:</b> all platters are fixed on it; a motor rotates it at 5400, 7200, 10000 or 15000 rpm.</li>
<li><b>Read-write heads:</b> one per surface, flying just above the surface.</li>
<li><b>Disk arm (arm assembly):</b> moves all heads together across the surfaces.</li>
<li><b>Track:</b> a circular path on a platter surface (thousands per surface).</li>
<li><b>Sector:</b> a track is divided into sectors, the smallest unit of transfer (512 bytes or 4 KB).</li>
<li><b>Cylinder:</b> the set of tracks at one arm position, i.e. the same track on all surfaces.</li>
</ul>
<p>The disk address is mapped as a one-dimensional array of <b>logical blocks</b>: sector 0 is the first sector of the first track on the outermost cylinder, continuing through that track, then the other tracks of the cylinder, then inward cylinders.</p>
<h4>Disk access time</h4>
<ul>
<li><b>Seek time:</b> time for the arm to move the heads to the desired cylinder (largest part).</li>
<li><b>Rotational latency:</b> time for the desired sector to rotate under the head (average = half a rotation).</li>
<li><b>Transfer time:</b> time to actually transfer the data.</li>
</ul>
<p><b>Access time = seek time + rotational latency + transfer time.</b> <b>Disk bandwidth</b> = total bytes transferred ÷ total time from the first request to the end of the last transfer.</p>
<p>A <b>head crash</b> (head touching the surface) damages the disk permanently. SSDs (flash) have no moving parts, so they have no seek time or latency.</p>""",
          """<p>Magnetic disks (hard disk drives, HDD) computers માં secondary storage નો મોટો ભાગ પૂરો પાડે છે.</p>
<h4>Disk ના ભાગો</h4>
<ul>
<li><b>Platters:</b> બંને surfaces પર magnetic material ના પડવાળી સપાટ ગોળ plates; માહિતી magnetically નોંધાય.</li>
<li><b>Spindle:</b> બધી platters તેના પર લગાવેલી; motor તેને 5400, 7200, 10000 કે 15000 rpm પર ફેરવે.</li>
<li><b>Read-write heads:</b> દરેક surface માટે એક, surface ની બરાબર ઉપર ઊડતું.</li>
<li><b>Disk arm (arm assembly):</b> બધા heads ને સાથે surfaces પર ખસેડે.</li>
<li><b>Track:</b> platter surface પરનો ગોળ માર્ગ (surface દીઠ હજારો).</li>
<li><b>Sector:</b> track ને sectors માં વહેંચાય, transfer નો સૌથી નાનો એકમ (512 bytes કે 4 KB).</li>
<li><b>Cylinder:</b> એક arm position પરના tracks નો સમૂહ, એટલે કે બધી surfaces પરનો એક જ track.</li>
</ul>
<p>Disk address ને <b>logical blocks</b> ના એક-પરિમાણી array તરીકે map કરાય છે: sector 0 એ સૌથી બહારના cylinder ના પહેલા track નો પહેલો sector છે, પછી તે track, પછી cylinder ના બીજા tracks, પછી અંદરના cylinders.</p>
<h4>Disk access time</h4>
<ul>
<li><b>Seek time:</b> arm ને heads જરૂરી cylinder પર લઈ જવામાં લાગતો સમય (સૌથી મોટો ભાગ).</li>
<li><b>Rotational latency:</b> જરૂરી sector head ની નીચે ફરીને આવે તેનો સમય (સરેરાશ = અડધું rotation).</li>
<li><b>Transfer time:</b> ખરેખર data transfer કરવાનો સમય.</li>
</ul>
<p><b>Access time = seek time + rotational latency + transfer time.</b> <b>Disk bandwidth</b> = transfer થયેલા કુલ bytes ÷ પહેલી request થી છેલ્લા transfer ના અંત સુધીનો કુલ સમય.</p>
<p><b>Head crash</b> (head surface ને અડે) disk ને કાયમી નુકસાન કરે. SSDs (flash) માં ફરતા ભાગો નથી, તેથી seek time કે latency નથી.</p>""",
          diagram="os4_disk", examples=["os4n9", "os4n10"]),
        T("4.4.2 Disk Scheduling", "4.4.2 Disk Scheduling",
          """<p>In a multiprogramming system, many processes generate disk I/O requests; they wait in the <b>disk queue</b>. <b>Disk scheduling</b> decides the order in which pending requests are served, with the aims of:</p>
<ul><li><b>Minimising seek time</b> (total head movement), since seek time is the dominant cost.</li><li><b>Maximising disk bandwidth</b> and throughput.</li><li>Giving fair, bounded waiting time to every request (no starvation).</li></ul>
<p>Each request specifies: input or output, disk address (cylinder/track), memory address and number of sectors. The performance of an algorithm is measured by the <b>total head movement</b> (number of tracks or cylinders crossed) for a given queue and initial head position.</p>
<h4>FCFS (baseline)</h4>
<p>First-Come First-Served serves requests in arrival order. It is fair but not efficient: the head swings widely. For Practical 5 (head 46), FCFS needs 554 tracks, while SCAN needs only 216.</p>
<h4>Algorithms</h4>
<ul><li><b>FCFS</b>, <b>SSTF</b> (shortest seek time first; may starve far requests), <b>SCAN</b>, <b>C-SCAN</b>, <b>LOOK</b>, <b>C-LOOK</b>. The syllabus focuses on <b>SCAN</b> and <b>C-SCAN</b>.</li></ul>
<h4>Steps to solve a disk-scheduling numerical</h4>
<ol><li>Write the queue in sorted order and mark the head position.</li><li>Decide the service order according to the algorithm and direction.</li><li>Add the absolute difference of every move: Σ |next − current|.</li><li>Draw the head-movement chart (tracks on the x-axis, time downwards).</li></ol>""",
          """<p>Multiprogramming system માં ઘણી processes disk I/O requests બનાવે છે; તે <b>disk queue</b> માં રાહ જુએ છે. <b>Disk scheduling</b> બાકી requests કયા ક્રમમાં સંતોષવી તે નક્કી કરે છે, આ હેતુઓ સાથે:</p>
<ul><li><b>Seek time ઓછો કરવો</b> (કુલ head movement), કારણ કે seek time સૌથી મોટો ખર્ચ છે.</li><li><b>Disk bandwidth</b> અને throughput વધારવા.</li><li>દરેક request ને ન્યાયી, મર્યાદિત waiting time આપવો (starvation નહીં).</li></ul>
<p>દરેક request જણાવે: input કે output, disk address (cylinder/track), memory address અને sectors ની સંખ્યા. Algorithm નું performance આપેલી queue અને શરૂઆતના head position માટે <b>કુલ head movement</b> (પાર કરેલા tracks કે cylinders ની સંખ્યા) થી મપાય છે.</p>
<h4>FCFS (આધાર)</h4>
<p>First-Come First-Served requests આવે તે ક્રમમાં સંતોષે. તે ન્યાયી છે પણ કાર્યક્ષમ નથી: head ખૂબ ઝૂલે છે. Practical 5 (head 46) માટે FCFS ને 554 tracks જોઈએ, જ્યારે SCAN ને માત્ર 216.</p>
<h4>Algorithms</h4>
<ul><li><b>FCFS</b>, <b>SSTF</b> (shortest seek time first; દૂરની requests starve થઈ શકે), <b>SCAN</b>, <b>C-SCAN</b>, <b>LOOK</b>, <b>C-LOOK</b>. Syllabus <b>SCAN</b> અને <b>C-SCAN</b> પર ભાર મૂકે છે.</li></ul>
<h4>Disk-scheduling numerical ઉકેલવાના પગલાં</h4>
<ol><li>Queue ને sorted ક્રમમાં લખો અને head position દર્શાવો.</li><li>Algorithm અને દિશા મુજબ service ક્રમ નક્કી કરો.</li><li>દરેક move નો absolute તફાવત ઉમેરો: Σ |next − current|.</li><li>Head-movement chart દોરો (x-axis પર tracks, સમય નીચે તરફ).</li></ol>""",
          examples=["os4n5"]),
        T("4.4.3 SCAN Disk Scheduling", "4.4.3 SCAN Disk Scheduling",
          """<p>In <b>SCAN</b>, the disk arm starts at one end of the disk and moves towards the other end, <b>serving requests as it reaches each track</b>. At the <b>end of the disk</b>, the direction of head movement is <b>reversed</b> and servicing continues. The head continuously scans back and forth across the disk. It is also called the <b>elevator algorithm</b>, because it behaves like a lift that serves all floors going up, then all floors going down.</p>
<h4>Algorithm</h4>
<ol>
<li>Note the head position and the direction of movement.</li>
<li>Serve all requests in the current direction in order of position.</li>
<li>Continue to the last track (0 or N − 1) even if no request is there.</li>
<li>Reverse the direction and serve the remaining requests.</li>
</ol>
<h4>Practical 5</h4>
<p>Tracks 0–199; queue 75, 90, 40, 135, 50, 170, 65, 10; head 46 moving left.</p>
<p>Order: 46 → 40 → 10 → 0 → 50 → 65 → 75 → 90 → 135 → 170.</p>
<p>Total = (46 − 0) + (170 − 0) = 46 + 170 = <b>216 tracks</b>.</p>
<h4>Advantages</h4>
<ul><li>Much less head movement than FCFS; high throughput.</li><li>No starvation: every request is served within two sweeps; low variance compared with SSTF.</li></ul>
<h4>Disadvantages</h4>
<ul><li>Goes to the end of the disk even if there are no requests there (wasted movement; LOOK fixes this).</li><li>Waiting time is not uniform: requests just behind the head wait for almost two sweeps, while middle tracks are visited more often.</li></ul>""",
          """<p><b>SCAN</b> માં disk arm disk ના એક છેડેથી શરૂ થઈ બીજા છેડા તરફ જાય છે, અને <b>દરેક track પર પહોંચતાં ત્યાંની requests સંતોષે</b> છે. <b>Disk ના છેડે</b> head movement ની દિશા <b>બદલાય</b> છે અને service ચાલુ રહે છે. Head સતત disk પર આગળ-પાછળ scan કરે છે. તેને <b>elevator algorithm</b> પણ કહે છે, કારણ કે તે lift જેવું વર્તે છે જે ઉપર જતાં બધા માળ અને પછી નીચે જતાં બધા માળ સંતોષે.</p>
<h4>Algorithm</h4>
<ol>
<li>Head position અને movement ની દિશા નોંધો.</li>
<li>હાલની દિશામાંની બધી requests સ્થાનના ક્રમમાં સંતોષો.</li>
<li>ત્યાં request ન હોય તો પણ છેલ્લા track (0 કે N − 1) સુધી જાઓ.</li>
<li>દિશા બદલી બાકીની requests સંતોષો.</li>
</ol>
<h4>Practical 5</h4>
<p>Tracks 0–199; queue 75, 90, 40, 135, 50, 170, 65, 10; head 46 ડાબી બાજુ.</p>
<p>ક્રમ: 46 → 40 → 10 → 0 → 50 → 65 → 75 → 90 → 135 → 170.</p>
<p>કુલ = (46 − 0) + (170 − 0) = 46 + 170 = <b>216 tracks</b>.</p>
<h4>ફાયદા</h4>
<ul><li>FCFS કરતાં ઘણું ઓછું head movement; ઊંચો throughput.</li><li>Starvation નહીં: દરેક request બે sweeps માં સંતોષાય; SSTF ની સરખામણીમાં ઓછો variance.</li></ul>
<h4>ગેરફાયદા</h4>
<ul><li>ત્યાં requests ન હોય તો પણ disk ના છેડા સુધી જાય (વેડફાતું movement; LOOK આ સુધારે).</li><li>Waiting time એકસરખો નથી: head ની બરાબર પાછળની requests લગભગ બે sweeps રાહ જુએ, જ્યારે વચ્ચેના tracks વધુ વાર મુલાકાત પામે.</li></ul>""",
          diagram="os4_scan", examples=["os4n1", "os4n3", "os4n6"]),
        T("4.4.4 C-SCAN Disk Scheduling", "4.4.4 C-SCAN Disk Scheduling",
          """<p><b>C-SCAN (Circular SCAN)</b> is a variant of SCAN designed to give a <b>more uniform waiting time</b>. Like SCAN, it moves the head from one end of the disk to the other, serving requests on the way. However, when the head reaches the end, it <b>immediately returns to the beginning of the disk without serving any requests</b> on the return trip. The cylinders are treated as a <b>circular list</b> that wraps around from the last cylinder to the first.</p>
<h4>Algorithm</h4>
<ol>
<li>Serve all requests in the chosen direction up to the end of the disk.</li>
<li>Jump to the other end (return seek, no service).</li>
<li>Continue in the <b>same direction</b> and serve the remaining requests.</li>
</ol>
<h4>Practical 5</h4>
<p>Head 46 moving left: 46 → 40 → 10 → 0, jump 0 → 199, then 170 → 135 → 90 → 75 → 65 → 50.</p>
<p>Total = (46 − 0) + (199 − 0) + (199 − 50) = 46 + 199 + 149 = <b>394 tracks</b>.</p>
<p>If the return jump is not counted (some textbooks): 46 + 149 = <b>195 tracks</b>. Always state your convention in the exam.</p>
<h4>Advantages</h4>
<ul><li><b>Uniform waiting time</b>: every track is visited once per cycle in the same direction; better than SCAN for heavy loads.</li><li>No starvation.</li></ul>
<h4>Disadvantages</h4>
<ul><li>More total head movement than SCAN because of the return seek.</li><li>Goes to the disk ends even without requests (C-LOOK fixes this).</li></ul>""",
          """<p><b>C-SCAN (Circular SCAN)</b> એ <b>વધુ એકસરખો waiting time</b> આપવા માટે બનાવાયેલો SCAN નો પ્રકાર છે. SCAN ની જેમ તે head ને disk ના એક છેડેથી બીજા છેડે ખસેડી રસ્તામાંની requests સંતોષે છે. પણ head છેડે પહોંચે ત્યારે તે પાછા ફરતાં <b>કોઈ request સંતોષ્યા વગર તરત disk ની શરૂઆતમાં પાછો જાય</b> છે. Cylinders ને <b>circular list</b> ગણાય છે જે છેલ્લા cylinder થી પહેલા સુધી વીંટળાય છે.</p>
<h4>Algorithm</h4>
<ol>
<li>પસંદ કરેલી દિશામાં disk ના છેડા સુધીની બધી requests સંતોષો.</li>
<li>બીજા છેડે jump કરો (return seek, service નહીં).</li>
<li><b>એ જ દિશામાં</b> આગળ વધી બાકીની requests સંતોષો.</li>
</ol>
<h4>Practical 5</h4>
<p>Head 46 ડાબી બાજુ: 46 → 40 → 10 → 0, jump 0 → 199, પછી 170 → 135 → 90 → 75 → 65 → 50.</p>
<p>કુલ = (46 − 0) + (199 − 0) + (199 − 50) = 46 + 199 + 149 = <b>394 tracks</b>.</p>
<p>Return jump ન ગણીએ તો (કેટલાંક પુસ્તકો): 46 + 149 = <b>195 tracks</b>. Exam માં હંમેશા તમારી પદ્ધતિ લખો.</p>
<h4>ફાયદા</h4>
<ul><li><b>એકસરખો waiting time</b>: દરેક track ની દરેક cycle માં એક જ દિશામાં એક વાર મુલાકાત; ભારે load માટે SCAN કરતાં સારું.</li><li>Starvation નહીં.</li></ul>
<h4>ગેરફાયદા</h4>
<ul><li>Return seek ને કારણે SCAN કરતાં વધુ કુલ head movement.</li><li>Requests વગર પણ disk ના છેડા સુધી જાય (C-LOOK આ સુધારે).</li></ul>""",
          diagram="os4_cscan", examples=["os4n2", "os4n4", "os4n7"]),
        T("4.4.5 SCAN vs C-SCAN (and LOOK, C-LOOK)", "4.4.5 SCAN vs C-SCAN (અને LOOK, C-LOOK)",
          """<p>Both are sweep algorithms that avoid starvation; the difference is what happens at the end of the disk.</p>
""" + SC_EN + """
<h4>LOOK and C-LOOK</h4>
<p>In practice, the arm goes only as far as the <b>final request</b> in each direction, then reverses (LOOK) or jumps to the first request at the other side (C-LOOK), without going all the way to the disk end. This saves unnecessary movement: for Practical 5, LOOK = 196 vs SCAN = 216.</p>
<h4>Choosing an algorithm</h4>
<ul><li>SCAN and C-SCAN perform better for systems that place a <b>heavy load</b> on the disk.</li><li>SSTF or LOOK is a reasonable default for light loads.</li><li>File-allocation method affects requests: contiguous files generate requests close together.</li></ul>""",
          """<p>બંને sweep algorithms છે જે starvation ટાળે છે; તફાવત disk ના છેડે શું થાય છે તેમાં છે.</p>
""" + SC_GU + """
<h4>LOOK અને C-LOOK</h4>
<p>વ્યવહારમાં arm દરેક દિશામાં માત્ર <b>છેલ્લી request</b> સુધી જાય, પછી દિશા બદલે (LOOK) અથવા બીજી બાજુની પહેલી request પર jump કરે (C-LOOK), disk ના છેડા સુધી ગયા વગર. આ બિનજરૂરી movement બચાવે છે: Practical 5 માટે LOOK = 196 vs SCAN = 216.</p>
<h4>Algorithm ની પસંદગી</h4>
<ul><li>Disk પર <b>ભારે load</b> હોય તેવી systems માં SCAN અને C-SCAN સારું કામ આપે.</li><li>હળવા load માટે SSTF કે LOOK યોગ્ય default છે.</li><li>File-allocation method requests પર અસર કરે: contiguous files નજીક નજીકની requests બનાવે.</li></ul>""",
          examples=["os4n8"]),
    ]}
