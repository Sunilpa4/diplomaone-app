"""Fundamentals of Operating System (DI03000041) - Unit 4 notes part A: 4.1 File system; 4.2 Directory system."""
from content_DI03000011_u1_notes_a import T
from content_DI03000041_u1_notes import tbl

TYPES_EN = tbl(["File type", "Usual extensions", "Function"], [
    ("Executable", "exe, com, bin, none (Linux)", "Ready-to-run machine-language program"),
    ("Object", "obj, o", "Compiled machine code, not linked"),
    ("Source code", "c, cpp, java, py, asm", "Source code in various languages"),
    ("Batch / script", "bat, sh", "Commands to the command interpreter"),
    ("Text", "txt, doc, docx", "Textual data, documents"),
    ("Word processor", "docx, odt, rtf", "Various word-processor formats"),
    ("Library", "lib, a, so, dll", "Libraries of routines for programmers"),
    ("Print or view", "pdf, jpg, png, ps", "Files for printing or viewing"),
    ("Archive", "zip, tar, rar", "Related files grouped (often compressed)"),
    ("Multimedia", "mp3, mp4, avi", "Audio / video information")])
TYPES_GU = tbl(["File type", "સામાન્ય extensions", "કાર્ય"], [
    ("Executable", "exe, com, bin, none (Linux)", "ચલાવવા તૈયાર machine-language program"),
    ("Object", "obj, o", "Compile થયેલો machine code, link નથી થયો"),
    ("Source code", "c, cpp, java, py, asm", "જુદી જુદી ભાષાઓમાં source code"),
    ("Batch / script", "bat, sh", "Command interpreter માટે commands"),
    ("Text", "txt, doc, docx", "Text data, documents"),
    ("Word processor", "docx, odt, rtf", "જુદા જુદા word-processor formats"),
    ("Library", "lib, a, so, dll", "Programmers માટે routines ની libraries"),
    ("Print or view", "pdf, jpg, png, ps", "Print કે જોવા માટેની files"),
    ("Archive", "zip, tar, rar", "સંબંધિત files નો સમૂહ (ઘણી વાર compressed)"),
    ("Multimedia", "mp3, mp4, avi", "Audio / video માહિતી")])

DIR_EN = tbl(["Structure", "Sharing", "Grouping", "Name conflicts", "Main problem"], [
    ("Single-level", "–", "No", "Yes", "Unique names for all users"),
    ("Two-level", "No", "Per user only", "No (per user)", "No sharing, no subdirectories"),
    ("Tree", "No", "Yes", "No", "Cannot share files"),
    ("Acyclic graph", "Yes", "Yes", "No", "Aliasing, dangling links"),
    ("General graph", "Yes", "Yes", "No", "Cycles; needs garbage collection")])
DIR_GU = tbl(["Structure", "Sharing", "Grouping", "Name conflicts", "મુખ્ય સમસ્યા"], [
    ("Single-level", "–", "ના", "હા", "બધા users માટે unique names"),
    ("Two-level", "ના", "માત્ર user મુજબ", "ના (user મુજબ)", "Sharing નહીં, subdirectories નહીં"),
    ("Tree", "ના", "હા", "ના", "Files share ન થઈ શકે"),
    ("Acyclic graph", "હા", "હા", "ના", "Aliasing, dangling links"),
    ("General graph", "હા", "હા", "ના", "Cycles; garbage collection જોઈએ")])

SEC_4_1 = {
    "title": {"en": "4.1 File System", "gu": "4.1 File System"},
    "items": [
        T("4.1.1 File Concept and File Attributes", "4.1.1 File Concept અને File Attributes",
          """<p>A <b>file</b> is a named collection of related information that is recorded on secondary storage (disk, SSD, pen drive). From the user's point of view, a file is the smallest unit of logical storage: data cannot be written to secondary storage unless it is inside a file. The <b>file system</b> is the part of the OS that manages files: naming, storing, accessing, protecting and organising them in directories.</p>
<h4>File attributes</h4>
<p>Besides its data, every file has information about itself called <b>attributes</b> (metadata). They are kept in the directory entry or in a file control block (inode in UNIX).</p>
<ul>
<li><b>Name:</b> the symbolic, human-readable name (e.g. <code>report.txt</code>).</li>
<li><b>Identifier:</b> a unique number (tag) by which the file system identifies the file (e.g. inode number).</li>
<li><b>Type:</b> needed by systems that support different file types (text, executable…).</li>
<li><b>Location:</b> pointer to the device and the position of the file on it.</li>
<li><b>Size:</b> current size in bytes / blocks, and possibly the maximum allowed size.</li>
<li><b>Protection:</b> access-control information: who can read, write, execute.</li>
<li><b>Time, date and user identification:</b> creation, last modification and last access; useful for protection, security and usage monitoring.</li>
</ul>
<p>In Linux, <code>ls -l</code> shows many of these attributes (permissions, owner, size, date, name) and <code>stat file</code> shows all of them.</p>""",
          """<p><b>File</b> એ secondary storage (disk, SSD, pen drive) પર સંગ્રહિત સંબંધિત માહિતીનો નામવાળો સમૂહ છે. User ના દૃષ્ટિકોણથી file એ logical storage નો સૌથી નાનો એકમ છે: data file ની અંદર ન હોય તો secondary storage પર લખી શકાતો નથી. <b>File system</b> એ OS નો ભાગ છે જે files નું સંચાલન કરે છે: naming, storing, accessing, protecting અને directories માં ગોઠવણી.</p>
<h4>File attributes</h4>
<p>Data ઉપરાંત દરેક file પાસે પોતાના વિશેની માહિતી હોય છે જેને <b>attributes</b> (metadata) કહે છે. તે directory entry અથવા file control block (UNIX માં inode) માં રખાય છે.</p>
<ul>
<li><b>Name:</b> symbolic, માણસ વાંચી શકે તેવું નામ (દા.ત. <code>report.txt</code>).</li>
<li><b>Identifier:</b> unique number (tag) જેનાથી file system file ને ઓળખે (દા.ત. inode number).</li>
<li><b>Type:</b> જુદા જુદા file types (text, executable…) support કરતી systems માટે જરૂરી.</li>
<li><b>Location:</b> device અને તેના પર file ના સ્થાનનો pointer.</li>
<li><b>Size:</b> bytes / blocks માં હાલનું કદ, અને કદાચ મહત્તમ મંજૂર કદ.</li>
<li><b>Protection:</b> access-control માહિતી: કોણ read, write, execute કરી શકે.</li>
<li><b>Time, date અને user identification:</b> creation, છેલ્લો ફેરફાર અને છેલ્લો access; protection, security અને usage monitoring માટે ઉપયોગી.</li>
</ul>
<p>Linux માં <code>ls -l</code> આમાંના ઘણા attributes (permissions, owner, size, date, name) બતાવે છે અને <code>stat file</code> બધા બતાવે છે.</p>"""),
        T("4.1.2 File Operations", "4.1.2 File Operations",
          """<p>A file is an <b>abstract data type</b>; the OS provides system calls to perform operations on it.</p>
<ol>
<li><b>Create:</b> find space in the file system and make a new entry in the directory.</li>
<li><b>Open:</b> search the directory, check permissions, and copy the file's information into the <b>open-file table</b>; returns a file handle / descriptor used by later operations.</li>
<li><b>Write:</b> a system call with the file name and data; the OS keeps a <b>write pointer</b> to the location of the next write.</li>
<li><b>Read:</b> a system call with the file name and memory buffer; the OS uses a <b>read pointer</b> (current-file-position pointer).</li>
<li><b>Reposition (seek):</b> change the current-file-position pointer to a given value; no actual I/O.</li>
<li><b>Delete:</b> search the directory, release all file space and erase the directory entry.</li>
<li><b>Truncate:</b> erase the contents but keep the attributes; the file length becomes zero.</li>
<li><b>Close:</b> remove the entry from the open-file table and free resources.</li>
</ol>
<p>Other operations (append, rename, copy) can be built from these basic ones.</p>
<h4>Open-file table information</h4>
<ul><li><b>File pointer</b> (current position), per process.</li><li><b>File-open count</b>: number of processes that have the file open; the entry is removed when it becomes 0.</li><li><b>Disk location</b> of the file and <b>access rights</b> (mode).</li></ul>
<h4>Access methods</h4>
<ul><li><b>Sequential access:</b> records processed in order, one after another (editors, compilers).</li><li><b>Direct (random) access:</b> fixed-length records read in any order by block number (databases).</li></ul>""",
          """<p>File એ <b>abstract data type</b> છે; OS તેના પર operations કરવા system calls આપે છે.</p>
<ol>
<li><b>Create:</b> file system માં જગ્યા શોધી directory માં નવી entry બનાવવી.</li>
<li><b>Open:</b> directory શોધી, permissions તપાસી, file ની માહિતી <b>open-file table</b> માં copy કરવી; પછીના operations માટે file handle / descriptor પાછું આપે.</li>
<li><b>Write:</b> file name અને data સાથે system call; OS આગળના write ના સ્થાન માટે <b>write pointer</b> રાખે.</li>
<li><b>Read:</b> file name અને memory buffer સાથે system call; OS <b>read pointer</b> (current-file-position pointer) વાપરે.</li>
<li><b>Reposition (seek):</b> current-file-position pointer ને આપેલી કિંમતે બદલવો; ખરેખર I/O થતો નથી.</li>
<li><b>Delete:</b> directory શોધી, file ની બધી જગ્યા મુક્ત કરી directory entry ભૂંસવી.</li>
<li><b>Truncate:</b> contents ભૂંસી નાખવા પણ attributes રાખવા; file length શૂન્ય થાય.</li>
<li><b>Close:</b> open-file table માંથી entry દૂર કરી resources મુક્ત કરવા.</li>
</ol>
<p>બીજા operations (append, rename, copy) આ મૂળભૂત operations પરથી બનાવી શકાય.</p>
<h4>Open-file table માહિતી</h4>
<ul><li><b>File pointer</b> (હાલનું સ્થાન), process મુજબ.</li><li><b>File-open count</b>: file open રાખેલી processes ની સંખ્યા; 0 થાય ત્યારે entry દૂર થાય.</li><li>File નું <b>disk location</b> અને <b>access rights</b> (mode).</li></ul>
<h4>Access methods</h4>
<ul><li><b>Sequential access:</b> records ક્રમમાં, એક પછી એક process થાય (editors, compilers).</li><li><b>Direct (random) access:</b> fixed-length records block number વડે ગમે તે ક્રમમાં વંચાય (databases).</li></ul>"""),
        T("4.1.3 File Types", "4.1.3 File Types",
          """<p>The OS must know the <b>type</b> of a file to operate on it sensibly (e.g. not try to print a binary object file). A common technique is to include the type as part of the name: <b>name.extension</b>, e.g. <code>resume.docx</code>, <code>server.c</code>, <code>ReaderThread.class</code>.</p>
<ul>
<li><b>Windows / MS-DOS:</b> the extension decides the type; only .exe, .com and .bat files can be executed.</li>
<li><b>UNIX / Linux:</b> extensions are only hints (conventions); executables are recognised by permission bits and a <b>magic number</b> at the start of the file.</li>
<li><b>macOS:</b> each file also stores the creator program as an attribute.</li>
</ul>
<h4>Common file types</h4>
""" + TYPES_EN + """
<h4>File types in UNIX (first character of ls -l)</h4>
<ul><li><code>-</code> regular file, <code>d</code> directory, <code>l</code> symbolic link, <code>c</code> character device, <code>b</code> block device, <code>p</code> named pipe, <code>s</code> socket.</li></ul>""",
          """<p>File પર યોગ્ય રીતે કામ કરવા OS ને તેનો <b>type</b> ખબર હોવો જોઈએ (દા.ત. binary object file ને print કરવાનો પ્રયત્ન ન કરે). સામાન્ય રીત એ છે કે type ને નામના ભાગ તરીકે રાખવો: <b>name.extension</b>, દા.ત. <code>resume.docx</code>, <code>server.c</code>, <code>ReaderThread.class</code>.</p>
<ul>
<li><b>Windows / MS-DOS:</b> extension type નક્કી કરે; માત્ર .exe, .com અને .bat files ચલાવી શકાય.</li>
<li><b>UNIX / Linux:</b> extensions માત્ર સૂચન (conventions) છે; executables permission bits અને file ની શરૂઆતના <b>magic number</b> થી ઓળખાય.</li>
<li><b>macOS:</b> દરેક file creator program ને પણ attribute તરીકે રાખે છે.</li>
</ul>
<h4>સામાન્ય file types</h4>
""" + TYPES_GU + """
<h4>UNIX માં file types (ls -l નો પહેલો અક્ષર)</h4>
<ul><li><code>-</code> regular file, <code>d</code> directory, <code>l</code> symbolic link, <code>c</code> character device, <code>b</code> block device, <code>p</code> named pipe, <code>s</code> socket.</li></ul>"""),
        T("4.1.4 File Paths: Absolute and Relative", "4.1.4 File Paths: Absolute અને Relative",
          """<p>In a hierarchical (tree) file system, a file is identified by its <b>path name</b>: the list of directories from a starting point to the file, separated by <code>/</code> (UNIX) or <code>\\</code> (Windows).</p>
<h4>Absolute path</h4>
<ul>
<li>Begins at the <b>root</b> directory and follows the path down to the file.</li>
<li>Always starts with <code>/</code> in UNIX (or a drive letter like <code>C:\\</code> in Windows).</li>
<li>Same meaning from any current directory. Example: <code>/home/ravi/os/notes.txt</code>.</li>
</ul>
<h4>Relative path</h4>
<ul>
<li>Begins at the <b>current (working) directory</b> of the process.</li>
<li>Does not start with <code>/</code>. Special names: <code>.</code> = current directory, <code>..</code> = parent directory, <code>~</code> = home directory.</li>
<li>Shorter, but its meaning depends on the current directory. Example (cwd = /home/ravi): <code>os/notes.txt</code>, <code>../priya/a.c</code>.</li>
</ul>
<p>Commands: <code>pwd</code> prints the current directory; <code>cd path</code> changes it.</p>""",
          """<p>Hierarchical (tree) file system માં file તેના <b>path name</b> થી ઓળખાય છે: શરૂઆતના બિંદુથી file સુધીની directories ની યાદી, <code>/</code> (UNIX) અથવા <code>\\</code> (Windows) થી અલગ કરેલી.</p>
<h4>Absolute path</h4>
<ul>
<li><b>Root</b> directory થી શરૂ થઈ file સુધીનો રસ્તો અનુસરે.</li>
<li>UNIX માં હંમેશા <code>/</code> થી શરૂ થાય (અથવા Windows માં <code>C:\\</code> જેવા drive letter થી).</li>
<li>કોઈ પણ current directory થી સરખો અર્થ. ઉદાહરણ: <code>/home/ravi/os/notes.txt</code>.</li>
</ul>
<h4>Relative path</h4>
<ul>
<li>Process ની <b>current (working) directory</b> થી શરૂ થાય.</li>
<li><code>/</code> થી શરૂ ન થાય. ખાસ નામો: <code>.</code> = current directory, <code>..</code> = parent directory, <code>~</code> = home directory.</li>
<li>ટૂંકો, પણ અર્થ current directory પર આધાર રાખે. ઉદાહરણ (cwd = /home/ravi): <code>os/notes.txt</code>, <code>../priya/a.c</code>.</li>
</ul>
<p>Commands: <code>pwd</code> current directory બતાવે; <code>cd path</code> તેને બદલે.</p>""",
          diagram="os4_paths", examples=["os4n11"]),
        T("4.1.5 File Security and Protection Mechanism", "4.1.5 File Security અને Protection Mechanism",
          """<p><b>Protection</b> controls <b>who</b> may access a file and <b>how</b>; <b>security</b> also defends the system against outside attacks. Files need protection from improper access (privacy) and from physical damage (reliability: backups, RAID).</p>
<h4>Types of access controlled</h4>
<ul><li>Read, write, execute, append, delete, list (attributes).</li></ul>
<h4>1. Access-control list (ACL)</h4>
<p>Each file has a list of user names and the types of access allowed to each user. When a user requests access, the OS checks the list. Very flexible, but the list can be long and must be maintained.</p>
<h4>2. Owner–group–others (UNIX permissions)</h4>
<p>To shorten ACLs, users are classified into three classes for each file:</p>
<ul>
<li><b>Owner (u):</b> the user who created the file.</li>
<li><b>Group (g):</b> a set of users who share the file and need similar access.</li>
<li><b>Others / universe (o):</b> all other users.</li>
</ul>
<p>Each class has three bits <b>r w x</b> (read = 4, write = 2, execute = 1). Example: <code>-rwxr-xr--</code> = 754: owner all rights, group read + execute, others read only. Changed by <code>chmod</code> (mode), <code>chown</code> (owner) and <code>chgrp</code> (group).</p>
<h4>3. Passwords</h4>
<p>A password is associated with each file; access is given only if the correct password is supplied. Drawbacks: many passwords to remember, and one password gives all-or-nothing access.</p>
<h4>Other security measures</h4>
<ul><li>User authentication (login), encryption of files, backups, antivirus, and audit logs.</li></ul>""",
          """<p><b>Protection</b> નક્કી કરે છે કે file ને <b>કોણ</b> અને <b>કેવી રીતે</b> access કરી શકે; <b>security</b> system ને બહારના હુમલાઓથી પણ બચાવે છે. Files ને ખોટા access (privacy) અને physical નુકસાન (reliability: backups, RAID) થી રક્ષણ જોઈએ.</p>
<h4>નિયંત્રિત access ના પ્રકારો</h4>
<ul><li>Read, write, execute, append, delete, list (attributes).</li></ul>
<h4>1. Access-control list (ACL)</h4>
<p>દરેક file પાસે user names અને દરેક user ને મંજૂર access ના પ્રકારોની યાદી હોય. User access માંગે ત્યારે OS યાદી તપાસે. ખૂબ લવચીક, પણ યાદી લાંબી થાય અને જાળવવી પડે.</p>
<h4>2. Owner–group–others (UNIX permissions)</h4>
<p>ACL ટૂંકું કરવા દરેક file માટે users ને ત્રણ વર્ગમાં વહેંચાય:</p>
<ul>
<li><b>Owner (u):</b> file બનાવનાર user.</li>
<li><b>Group (g):</b> file share કરતા અને સરખો access જોઈતા users નો સમૂહ.</li>
<li><b>Others / universe (o):</b> બાકીના બધા users.</li>
</ul>
<p>દરેક વર્ગ પાસે ત્રણ bits <b>r w x</b> (read = 4, write = 2, execute = 1). ઉદાહરણ: <code>-rwxr-xr--</code> = 754: owner ને બધા અધિકાર, group ને read + execute, others ને માત્ર read. <code>chmod</code> (mode), <code>chown</code> (owner) અને <code>chgrp</code> (group) વડે બદલાય.</p>
<h4>3. Passwords</h4>
<p>દરેક file સાથે password જોડાય; સાચો password આપે તો જ access મળે. ગેરફાયદા: ઘણા passwords યાદ રાખવા પડે, અને એક password all-or-nothing access આપે.</p>
<h4>બીજા security ઉપાયો</h4>
<ul><li>User authentication (login), files નું encryption, backups, antivirus અને audit logs.</li></ul>""",
          diagram="os4_perm", examples=["os4n12"]),
    ]}

SEC_4_2 = {
    "title": {"en": "4.2 Directory System", "gu": "4.2 Directory System"},
    "items": [
        T("4.2.1 Directory and Directory Operations", "4.2.1 Directory અને Directory Operations",
          """<p>A <b>directory</b> is a special file (symbol table) that translates <b>file names into directory entries</b>: name, location, size, type and other attributes. A disk can be divided into <b>partitions (volumes)</b>, and each volume has a device directory.</p>
<h4>Operations on a directory</h4>
<ul>
<li><b>Search</b> for a file (by name or pattern).</li>
<li><b>Create</b> a file (add an entry) and <b>delete</b> a file (remove an entry).</li>
<li><b>List</b> a directory (names and attributes).</li>
<li><b>Rename</b> a file (may change its position in the directory).</li>
<li><b>Traverse</b> the file system (visit every directory and file, e.g. for backup).</li>
</ul>
<h4>Goals of directory organisation</h4>
<ul><li><b>Efficiency:</b> locate a file quickly.</li><li><b>Naming:</b> convenient for users; two users may use the same name; one file may have several names.</li><li><b>Grouping:</b> logical grouping of files by properties (all Java programs, all games).</li></ul>
<p>The common logical structures are single-level, two-level, tree, acyclic graph and general graph.</p>""",
          """<p><b>Directory</b> એ ખાસ file (symbol table) છે જે <b>file names ને directory entries માં</b> ફેરવે છે: name, location, size, type અને બીજા attributes. Disk ને <b>partitions (volumes)</b> માં વહેંચી શકાય, અને દરેક volume પાસે device directory હોય.</p>
<h4>Directory પરના operations</h4>
<ul>
<li>File <b>search</b> કરવી (નામ કે pattern વડે).</li>
<li>File <b>create</b> કરવી (entry ઉમેરવી) અને <b>delete</b> કરવી (entry દૂર કરવી).</li>
<li>Directory <b>list</b> કરવી (names અને attributes).</li>
<li>File <b>rename</b> કરવી (directory માં તેનું સ્થાન બદલાઈ શકે).</li>
<li>File system <b>traverse</b> કરવી (દરેક directory અને file ની મુલાકાત, દા.ત. backup માટે).</li>
</ul>
<h4>Directory ગોઠવણીના ધ્યેય</h4>
<ul><li><b>Efficiency:</b> file ઝડપથી શોધવી.</li><li><b>Naming:</b> users માટે અનુકૂળ; બે users એક જ નામ વાપરી શકે; એક file ના ઘણા નામ હોઈ શકે.</li><li><b>Grouping:</b> ગુણધર્મ મુજબ files નું logical grouping (બધા Java programs, બધી games).</li></ul>
<p>સામાન્ય logical structures: single-level, two-level, tree, acyclic graph અને general graph.</p>"""),
        T("4.2.2 Single-Level Directory", "4.2.2 Single-Level Directory",
          """<p>The simplest structure: <b>all files are contained in the same directory</b>, for all users.</p>
<h4>Advantages</h4>
<ul><li>Simple to understand and implement.</li><li>Searching, creating and deleting are easy when there are few files.</li></ul>
<h4>Disadvantages</h4>
<ul>
<li><b>Naming problem:</b> all files must have <b>unique names</b>; two users cannot both call a file <code>test</code>.</li>
<li><b>Grouping problem:</b> no way to group related files; with many files (hundreds of users) it becomes hard to remember names.</li>
<li>Searching becomes slow as the number of files grows.</li>
</ul>
<p>Used in early, single-user systems (e.g. CP/M).</p>""",
          """<p>સૌથી સરળ structure: બધા users માટે <b>બધી files એક જ directory માં</b> હોય.</p>
<h4>ફાયદા</h4>
<ul><li>સમજવા અને અમલ કરવા સરળ.</li><li>Files ઓછી હોય ત્યારે search, create અને delete સરળ.</li></ul>
<h4>ગેરફાયદા</h4>
<ul>
<li><b>Naming problem:</b> બધી files ના <b>unique names</b> હોવા જોઈએ; બે users બંને file ને <code>test</code> નામ ન આપી શકે.</li>
<li><b>Grouping problem:</b> સંબંધિત files group કરવાનો કોઈ રસ્તો નહીં; ઘણી files (સેંકડો users) હોય ત્યારે નામ યાદ રાખવા મુશ્કેલ.</li>
<li>Files વધે તેમ search ધીમી થાય.</li>
</ul>
<p>શરૂઆતની single-user systems (દા.ત. CP/M) માં વપરાતી.</p>""",
          diagram="os4_single"),
        T("4.2.3 Two-Level Directory", "4.2.3 Two-Level Directory",
          """<p>Each user has a separate <b>user file directory (UFD)</b> listing only that user's files. The system has a <b>master file directory (MFD)</b>, indexed by user name or account number, whose entries point to the UFDs.</p>
<h4>Working</h4>
<ul>
<li>When a user logs in, the MFD is searched to find the user's UFD.</li>
<li>File references (create, delete, search) are searched only in that user's UFD.</li>
<li>A file is named by a <b>path name</b>: user name + file name, e.g. <code>/user1/a</code>.</li>
<li>System files (compilers, libraries) are kept in a special user directory that is searched when a file is not found in the user's UFD (<b>search path</b>).</li>
</ul>
<h4>Advantages</h4>
<ul><li>Different users can have files with the <b>same name</b>.</li><li>Efficient searching (only one UFD); isolation between users.</li></ul>
<h4>Disadvantages</h4>
<ul><li>Users are isolated: <b>no sharing</b> or cooperation is easy.</li><li>No grouping within a user's files (no subdirectories).</li></ul>""",
          """<p>દરેક user પાસે અલગ <b>user file directory (UFD)</b> હોય જેમાં માત્ર તે user ની files હોય. System પાસે <b>master file directory (MFD)</b> હોય, જે user name કે account number થી indexed હોય અને તેની entries UFDs તરફ point કરે.</p>
<h4>કાર્યપદ્ધતિ</h4>
<ul>
<li>User login કરે ત્યારે તેની UFD શોધવા MFD search થાય.</li>
<li>File references (create, delete, search) માત્ર તે user ની UFD માં શોધાય.</li>
<li>File ને <b>path name</b> થી ઓળખાય: user name + file name, દા.ત. <code>/user1/a</code>.</li>
<li>System files (compilers, libraries) ખાસ user directory માં રખાય, જે user ની UFD માં file ન મળે ત્યારે શોધાય (<b>search path</b>).</li>
</ul>
<h4>ફાયદા</h4>
<ul><li>જુદા users ની files નું <b>સરખું નામ</b> હોઈ શકે.</li><li>કાર્યક્ષમ search (માત્ર એક UFD); users વચ્ચે isolation.</li></ul>
<h4>ગેરફાયદા</h4>
<ul><li>Users અલગ પડી જાય: <b>sharing</b> કે સહકાર સરળ નથી.</li><li>User ની files માં grouping નહીં (subdirectories નહીં).</li></ul>""",
          diagram="os4_two"),
        T("4.2.4 Tree-Structured Directory", "4.2.4 Tree-Structured Directory",
          """<p>The natural generalisation of the two-level directory is a <b>tree of arbitrary height</b>. The tree has a <b>root directory</b>, and every file has a unique path name. A directory contains files and/or <b>subdirectories</b>. This is the structure used by most systems (UNIX, Windows).</p>
<h4>Features</h4>
<ul>
<li>Each directory entry has a bit telling whether it is a file (0) or a subdirectory (1).</li>
<li>Each process has a <b>current directory</b>; files are searched there unless a path is given.</li>
<li><b>Absolute</b> and <b>relative</b> path names are supported.</li>
<li>Users can create and delete their own subdirectories (<code>mkdir</code>, <code>rmdir</code>). Deleting a non-empty directory either is refused or deletes everything under it (<code>rm -r</code>).</li>
</ul>
<h4>Advantages</h4>
<ul><li>Very general and scalable; efficient searching.</li><li>Logical <b>grouping</b> of files into subdirectories; same name allowed in different directories.</li></ul>
<h4>Disadvantages</h4>
<ul><li><b>No sharing</b>: a file or directory has exactly one parent, so it cannot belong to two directories.</li><li>Long path names may be needed to reach deep files.</li></ul>""",
          """<p>Two-level directory નું સ્વાભાવિક વિસ્તરણ એ <b>કોઈ પણ ઊંચાઈનું tree</b> છે. Tree પાસે <b>root directory</b> હોય, અને દરેક file નું unique path name હોય. Directory માં files અને/અથવા <b>subdirectories</b> હોય. મોટા ભાગની systems (UNIX, Windows) આ structure વાપરે છે.</p>
<h4>લક્ષણો</h4>
<ul>
<li>દરેક directory entry માં bit હોય જે કહે કે તે file (0) છે કે subdirectory (1).</li>
<li>દરેક process પાસે <b>current directory</b> હોય; path ન આપ્યો હોય તો files ત્યાં શોધાય.</li>
<li><b>Absolute</b> અને <b>relative</b> path names support થાય.</li>
<li>Users પોતાની subdirectories બનાવી અને delete કરી શકે (<code>mkdir</code>, <code>rmdir</code>). ખાલી ન હોય તેવી directory delete કરવાનો ઇનકાર થાય અથવા તેની નીચેનું બધું delete થાય (<code>rm -r</code>).</li>
</ul>
<h4>ફાયદા</h4>
<ul><li>ખૂબ સામાન્ય અને scalable; કાર્યક્ષમ search.</li><li>Files નું subdirectories માં logical <b>grouping</b>; જુદી directories માં સરખું નામ મંજૂર.</li></ul>
<h4>ગેરફાયદા</h4>
<ul><li><b>Sharing નહીં</b>: file કે directory ને બરાબર એક parent હોય, તેથી તે બે directories માં ન હોઈ શકે.</li><li>ઊંડી files સુધી પહોંચવા લાંબા path names જોઈએ.</li></ul>""",
          diagram="os4_tree"),
        T("4.2.5 Acyclic-Graph Directory", "4.2.5 Acyclic-Graph Directory",
          """<p>An <b>acyclic graph</b> (a graph with no cycles) allows directories to <b>share subdirectories and files</b>. The same file or subdirectory may appear in two different directories. It is a natural generalisation of the tree, useful when two programmers work on a joint project.</p>
<h4>Implementation of sharing</h4>
<ul>
<li><b>Links:</b> a new directory entry that is a pointer to another file or subdirectory.<ul><li><b>Symbolic (soft) link:</b> contains the path name of the real file (<code>ln -s</code>).</li><li><b>Hard link:</b> another directory entry pointing to the same file (same inode) (<code>ln</code>).</li></ul></li>
<li><b>Duplicate entries:</b> copy all information about the file into both directories (problem: keeping copies consistent).</li>
</ul>
<h4>Advantages</h4>
<ul><li>Sharing of files and directories; a change made by one user is seen by others immediately.</li></ul>
<h4>Problems</h4>
<ul>
<li><b>Aliasing:</b> a file may have several absolute path names; traversals (backup, search) may visit it twice.</li>
<li><b>Deletion:</b> if the file is deleted, other links become <b>dangling pointers</b>. Solutions: delete the symbolic links too (or leave them invalid), or keep a <b>reference count</b> and delete the file only when the count becomes 0 (hard links in UNIX).</li>
<li>Must ensure no cycles are created when adding links.</li>
</ul>""",
          """<p><b>Acyclic graph</b> (cycles વગરનો graph) directories ને <b>subdirectories અને files share</b> કરવા દે છે. એક જ file કે subdirectory બે જુદી directories માં દેખાઈ શકે. તે tree નું સ્વાભાવિક વિસ્તરણ છે, જે બે programmers સંયુક્ત project પર કામ કરે ત્યારે ઉપયોગી છે.</p>
<h4>Sharing નો અમલ</h4>
<ul>
<li><b>Links:</b> નવી directory entry જે બીજી file કે subdirectory તરફનો pointer છે.<ul><li><b>Symbolic (soft) link:</b> ખરી file નું path name રાખે (<code>ln -s</code>).</li><li><b>Hard link:</b> એ જ file (એ જ inode) તરફ point કરતી બીજી directory entry (<code>ln</code>).</li></ul></li>
<li><b>Duplicate entries:</b> file વિશેની બધી માહિતી બંને directories માં copy કરવી (સમસ્યા: નકલો consistent રાખવી).</li>
</ul>
<h4>ફાયદા</h4>
<ul><li>Files અને directories નું sharing; એક user એ કરેલો ફેરફાર બીજાને તરત દેખાય.</li></ul>
<h4>સમસ્યાઓ</h4>
<ul>
<li><b>Aliasing:</b> file ના ઘણા absolute path names હોઈ શકે; traversals (backup, search) તેની બે વાર મુલાકાત લઈ શકે.</li>
<li><b>Deletion:</b> file delete થાય તો બીજી links <b>dangling pointers</b> બને. ઉકેલ: symbolic links પણ delete કરો (અથવા invalid રહેવા દો), અથવા <b>reference count</b> રાખો અને count 0 થાય ત્યારે જ file delete કરો (UNIX માં hard links).</li>
<li>Links ઉમેરતી વખતે cycle ન બને તેની ખાતરી કરવી પડે.</li>
</ul>""",
          diagram="os4_acyclic"),
        T("4.2.6 General Graph Directory", "4.2.6 General Graph Directory",
          """<p>If links are allowed to point to <b>any directory</b>, including an ancestor, the structure becomes a <b>general graph</b> that may contain <b>cycles</b>.</p>
<h4>Problems caused by cycles</h4>
<ul>
<li><b>Infinite loops:</b> a search or traversal algorithm may go round the cycle forever; it may also search the same part many times (poor performance).</li>
<li><b>Deletion:</b> because of self-references, the reference count of a directory may never become 0 even when it is no longer reachable, so its space is never freed.</li>
</ul>
<h4>Solutions</h4>
<ul>
<li><b>Garbage collection:</b> traverse the whole file system and mark everything reachable; then free everything not marked (very time-consuming on disk).</li>
<li><b>Bypass links during traversal</b>, or limit the number of directories visited in a search.</li>
<li><b>Cycle detection:</b> check every new link for a cycle (expensive); or allow links only to <b>files</b>, not directories (UNIX hard links to directories are not allowed), which keeps the graph acyclic.</li>
</ul>
<h4>Comparison of directory structures</h4>
""" + DIR_EN,
          """<p>Links ને <b>કોઈ પણ directory</b> તરફ, ancestor સહિત, point કરવા દઈએ તો structure <b>general graph</b> બને છે જેમાં <b>cycles</b> હોઈ શકે.</p>
<h4>Cycles થી થતી સમસ્યાઓ</h4>
<ul>
<li><b>Infinite loops:</b> search કે traversal algorithm cycle માં હંમેશ માટે ફરતો રહે; એક જ ભાગ ઘણી વાર શોધે (ખરાબ performance).</li>
<li><b>Deletion:</b> self-references ને કારણે directory reachable ન હોય તો પણ તેનો reference count ક્યારેય 0 ન થાય, તેથી તેની જગ્યા ક્યારેય મુક્ત ન થાય.</li>
</ul>
<h4>ઉકેલો</h4>
<ul>
<li><b>Garbage collection:</b> આખી file system traverse કરી reachable બધું mark કરો; પછી mark ન થયેલું બધું મુક્ત કરો (disk પર ખૂબ સમય લે).</li>
<li>Traversal દરમિયાન <b>links ને bypass</b> કરો, અથવા search માં મુલાકાત લેવાતી directories ની સંખ્યા મર્યાદિત કરો.</li>
<li><b>Cycle detection:</b> દરેક નવી link માટે cycle તપાસો (મોંઘું); અથવા links માત્ર <b>files</b> તરફ જ મંજૂર કરો, directories તરફ નહીં (UNIX માં directories ની hard links મંજૂર નથી), જેથી graph acyclic રહે.</li>
</ul>
<h4>Directory structures ની સરખામણી</h4>
""" + DIR_GU,
          diagram="os4_general"),
    ]}

from content_DI03000041_u4_notes_b import SEC_4_3, SEC_4_4  # noqa: E402

NOTES = [SEC_4_1, SEC_4_2, SEC_4_3, SEC_4_4]
