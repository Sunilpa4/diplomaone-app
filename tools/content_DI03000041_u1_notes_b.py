"""Fundamentals of Operating System (DI03000041) - Unit 1 notes part B: 1.3 Structure of OS; 1.4 Case study: Linux, Windows, macOS."""
from content_DI03000011_u1_notes_a import T


def tbl(head, rows_):
    h = "<table><tr>" + "".join(f"<th>{x}</th>" for x in head) + "</tr>"
    for r in rows_:
        h += "<tr>" + "".join(f"<td>{v}</td>" for v in r) + "</tr>"
    return h + "</table>"


STR_EN = tbl(["Point", "Monolithic", "Layered", "Microkernel"], [
    ("Kernel size", "Very large", "Large, split into layers", "Very small"),
    ("Services run in", "Kernel space", "Kernel, layer by layer", "User space (servers)"),
    ("Communication", "Direct function calls", "Calls to the lower layer", "Message passing (IPC)"),
    ("Speed", "Fastest", "Slower (many layers)", "Slower (many messages)"),
    ("Reliability", "Low: one bug can crash all", "Medium", "High: a server crash does not crash the kernel"),
    ("Extending / debugging", "Difficult", "Easy, one layer at a time", "Easy: add a new server"),
    ("Examples", "MS-DOS, Unix, Linux", "THE OS, Multics", "QNX, MINIX 3, L4, Mach")])
STR_GU = tbl(["મુદ્દો", "Monolithic", "Layered", "Microkernel"], [
    ("Kernel નું કદ", "ખૂબ મોટું", "મોટું, layers માં વહેંચેલું", "ખૂબ નાનું"),
    ("Services ક્યાં ચાલે", "Kernel space", "Kernel, layer પ્રમાણે", "User space (servers)"),
    ("Communication", "સીધા function calls", "નીચેના layer ને calls", "Message passing (IPC)"),
    ("ઝડપ", "સૌથી ઝડપી", "ધીમું (ઘણા layers)", "ધીમું (ઘણા messages)"),
    ("Reliability", "ઓછી: એક bug બધું crash કરે", "મધ્યમ", "વધુ: server crash થી kernel crash ન થાય"),
    ("Extend / debug કરવું", "મુશ્કેલ", "સરળ, એક સમયે એક layer", "સરળ: નવો server ઉમેરો"),
    ("ઉદાહરણ", "MS-DOS, Unix, Linux", "THE OS, Multics", "QNX, MINIX 3, L4, Mach")])

SEC_1_3 = {
    "title": {"en": "1.3 Structure of Operating System", "gu": "1.3 Operating System નું Structure"},
    "items": [
        T("1.3.0 Introduction: Kernel, User Mode and Kernel Mode", "1.3.0 પરિચય: Kernel, User Mode અને Kernel Mode",
          """<p>The <b>structure</b> of an OS means how its parts (process manager, memory manager, file system, drivers) are organised and connected. A large OS must be divided into small parts so that it is easy to build, test and change.</p>
<ul>
<li><b>Kernel:</b> the core part of the OS that is always in memory and has full control of the hardware.</li>
<li><b>Kernel mode (supervisor mode):</b> code can execute every instruction, including privileged ones, and access all memory. The kernel runs here.</li>
<li><b>User mode:</b> restricted mode for application programs. To get an OS service, a program makes a <b>system call</b>, which switches the CPU from user mode to kernel mode (mode bit: 0 = kernel, 1 = user).</li>
</ul>
<p>The syllabus covers three structures: <b>layered</b>, <b>monolithic</b> and <b>microkernel</b>. They differ in how much code runs in kernel mode.</p>""",
          """<p>OS નું <b>structure</b> એટલે તેના ભાગો (process manager, memory manager, file system, drivers) કઈ રીતે ગોઠવાયેલા અને જોડાયેલા છે. મોટી OS ને નાના ભાગોમાં વહેંચવી પડે જેથી તેને બનાવવી, test કરવી અને બદલવી સરળ બને.</p>
<ul>
<li><b>Kernel:</b> OS નો મુખ્ય ભાગ જે હંમેશા memory માં રહે છે અને hardware પર સંપૂર્ણ control ધરાવે છે.</li>
<li><b>Kernel mode (supervisor mode):</b> code privileged સહિત દરેક instruction ચલાવી શકે અને આખી memory access કરી શકે. Kernel અહીં ચાલે છે.</li>
<li><b>User mode:</b> application programs માટેનો મર્યાદિત mode. OS service મેળવવા program <b>system call</b> કરે છે, જે CPU ને user mode માંથી kernel mode માં લઈ જાય છે (mode bit: 0 = kernel, 1 = user).</li>
</ul>
<p>Syllabus માં ત્રણ structures છે: <b>layered</b>, <b>monolithic</b> અને <b>microkernel</b>. Kernel mode માં કેટલો code ચાલે છે તેમાં તેઓ જુદા પડે છે.</p>"""),
        T("1.3.1 Layered Structure", "1.3.1 Layered Structure",
          """<p>In the <b>layered approach</b>, the OS is divided into a number of <b>layers (levels)</b>, each built on top of the lower one. The bottom layer (<b>layer 0</b>) is the <b>hardware</b> and the highest layer (<b>layer N</b>) is the <b>user interface</b>.</p>
<p><b>Rule:</b> each layer uses <b>only the functions and services of the layer just below it</b>, and provides services to the layer above it. A layer does not need to know how the lower layer works; it only needs to know <b>what</b> it does (data hiding).</p>
<h4>Example: THE operating system (Dijkstra, 1968)</h4>
<ul>
<li>Layer 5: user programs</li>
<li>Layer 4: buffering for I/O devices</li>
<li>Layer 3: operator–console (process) communication</li>
<li>Layer 2: memory management</li>
<li>Layer 1: CPU scheduling</li>
<li>Layer 0: hardware</li>
</ul>
<h4>Advantages</h4>
<ul>
<li><b>Simple to build and debug:</b> layer 1 is tested first using only hardware; when it works, layer 2 is tested, and so on. An error found in a layer must be in that layer.</li>
<li><b>Modularity and data hiding:</b> a layer can be changed without affecting the others if its interface stays the same.</li>
</ul>
<h4>Disadvantages</h4>
<ul>
<li><b>Hard to define the layers:</b> each layer may use only lower layers, so careful planning is needed (e.g. the disk driver must be below memory management, which uses it for swapping).</li>
<li><b>Less efficient:</b> a request passes through many layers, and each adds overhead.</li>
</ul>""",
          """<p><b>Layered approach</b> માં OS ને ઘણા <b>layers (levels)</b> માં વહેંચવામાં આવે છે, દરેક નીચેના layer ઉપર બનેલો. સૌથી નીચેનો layer (<b>layer 0</b>) <b>hardware</b> છે અને સૌથી ઉપરનો (<b>layer N</b>) <b>user interface</b> છે.</p>
<p><b>નિયમ:</b> દરેક layer <b>માત્ર તેની તરત નીચેના layer ના functions અને services</b> વાપરે છે, અને ઉપરના layer ને services આપે છે. નીચેનો layer <b>કેવી રીતે</b> કામ કરે છે તે જાણવાની જરૂર નથી; તે <b>શું</b> કરે છે એટલું જ જાણવું પડે (data hiding).</p>
<h4>ઉદાહરણ: THE operating system (Dijkstra, 1968)</h4>
<ul>
<li>Layer 5: user programs</li>
<li>Layer 4: I/O devices માટે buffering</li>
<li>Layer 3: operator–console (process) communication</li>
<li>Layer 2: memory management</li>
<li>Layer 1: CPU scheduling</li>
<li>Layer 0: hardware</li>
</ul>
<h4>ફાયદા</h4>
<ul>
<li><b>બનાવવું અને debug કરવું સરળ:</b> પહેલાં માત્ર hardware વાપરી layer 1 test થાય; તે બરાબર ચાલે પછી layer 2, વગેરે. કોઈ layer માં મળેલી error તે જ layer માં હોય.</li>
<li><b>Modularity અને data hiding:</b> interface સરખો રહે તો એક layer ને બીજાને અસર વગર બદલી શકાય.</li>
</ul>
<h4>ગેરફાયદા</h4>
<ul>
<li><b>Layers નક્કી કરવા મુશ્કેલ:</b> દરેક layer માત્ર નીચેના layers વાપરી શકે, તેથી કાળજીપૂર્વક આયોજન જોઈએ (દા.ત. disk driver memory management ની નીચે હોવો જોઈએ, કારણ કે swapping માટે તે તેને વાપરે છે).</li>
<li><b>ઓછી કાર્યક્ષમ:</b> request ઘણા layers માંથી પસાર થાય, અને દરેક overhead ઉમેરે.</li>
</ul>""",
          diagram="os1_layered"),
        T("1.3.2 Monolithic Structure", "1.3.2 Monolithic Structure",
          """<p>In a <b>monolithic kernel</b>, the <b>entire OS runs as one large program in kernel mode</b>. Process management, memory management, file system, device drivers, networking and IPC are all inside a single kernel and share one address space. Any function can directly call any other function.</p>
<p>User programs request services through the <b>system call interface</b>; the kernel then does the whole job itself.</p>
<p><b>Simple monolithic</b> (no clear structure, e.g. <b>MS-DOS</b>): application programs could even access the hardware directly, so one faulty program could crash the whole system.</p>
<p><b>Modular monolithic</b> (e.g. <b>Linux</b>): the kernel is still one large program, but parts such as device drivers can be added or removed at run time as <b>loadable kernel modules</b>.</p>
<h4>Advantages</h4>
<ul>
<li><b>High performance:</b> services communicate through fast, direct function calls; there is very little overhead.</li>
<li>Simple design for small systems.</li>
</ul>
<h4>Disadvantages</h4>
<ul>
<li><b>Low reliability:</b> a bug in any part (e.g. a driver) can crash the entire system.</li>
<li><b>Difficult to maintain, extend and debug</b> because the code is large and closely connected.</li>
<li>Adding a new feature often means recompiling the whole kernel (unless modules are used).</li>
</ul>
<p><b>Examples:</b> MS-DOS, traditional Unix, Linux, FreeBSD.</p>""",
          """<p><b>Monolithic kernel</b> માં <b>આખી OS kernel mode માં એક મોટા program તરીકે ચાલે છે</b>. Process management, memory management, file system, device drivers, networking અને IPC બધું એક જ kernel માં હોય છે અને એક જ address space વહેંચે છે. કોઈ પણ function બીજા કોઈ પણ function ને સીધું call કરી શકે.</p>
<p>User programs <b>system call interface</b> દ્વારા services માંગે છે; પછી kernel પોતે આખું કામ કરે છે.</p>
<p><b>Simple monolithic</b> (સ્પષ્ટ structure નહીં, દા.ત. <b>MS-DOS</b>): application programs hardware ને સીધું પણ access કરી શકતા, તેથી એક ખરાબ program આખી system crash કરી શકતો.</p>
<p><b>Modular monolithic</b> (દા.ત. <b>Linux</b>): kernel હજી એક મોટો program છે, પણ device drivers જેવા ભાગો run time પર <b>loadable kernel modules</b> તરીકે ઉમેરી કે કાઢી શકાય.</p>
<h4>ફાયદા</h4>
<ul>
<li><b>ઊંચું performance:</b> services ઝડપી, સીધા function calls થી communicate કરે; overhead ખૂબ ઓછો.</li>
<li>નાની systems માટે સરળ design.</li>
</ul>
<h4>ગેરફાયદા</h4>
<ul>
<li><b>ઓછી reliability:</b> કોઈ પણ ભાગ (દા.ત. driver) નો bug આખી system crash કરી શકે.</li>
<li>Code મોટો અને નજીકથી જોડાયેલો હોવાથી <b>maintain, extend અને debug કરવું મુશ્કેલ</b>.</li>
<li>નવું feature ઉમેરવા ઘણી વાર આખું kernel ફરી compile કરવું પડે (modules ન હોય તો).</li>
</ul>
<p><b>ઉદાહરણ:</b> MS-DOS, પરંપરાગત Unix, Linux, FreeBSD.</p>""",
          diagram="os1_monolithic"),
        T("1.3.3 Microkernel Structure", "1.3.3 Microkernel Structure",
          """<p>In the <b>microkernel approach</b>, all non-essential parts are <b>removed from the kernel</b> and run as ordinary programs in <b>user mode</b>, called <b>servers</b>. The kernel becomes very small (a <b>microkernel</b>).</p>
<p>The microkernel keeps only the minimum functions:</p>
<ul>
<li><b>Inter-process communication (IPC)</b>, i.e. message passing</li>
<li>Basic <b>CPU scheduling</b> and process/thread management</li>
<li>Basic <b>memory management</b></li>
</ul>
<p>File system, device drivers, networking etc. run as <b>user-level servers</b>. When an application wants to read a file, it sends a <b>message</b> to the file server <b>through the microkernel</b>; the file server does the work and replies with a message.</p>
<h4>Advantages</h4>
<ul>
<li><b>Reliability and security:</b> if a server (e.g. a driver) fails, only that server is restarted; the kernel keeps running.</li>
<li><b>Easy to extend:</b> new services are added as user-mode servers without changing the kernel.</li>
<li><b>Portability:</b> the small kernel is easy to move to new hardware.</li>
</ul>
<h4>Disadvantages</h4>
<ul>
<li><b>Lower performance:</b> many messages and user–kernel mode switches add overhead.</li>
</ul>
<p><b>Examples:</b> QNX (used in cars), MINIX 3, L4, Mach. <b>Hybrid kernels</b> mix both ideas: macOS (XNU = Mach + BSD) and Windows NT.</p>""",
          """<p><b>Microkernel approach</b> માં બધા બિન-જરૂરી ભાગો <b>kernel માંથી કાઢી</b> નાખી <b>user mode</b> માં સામાન્ય programs તરીકે ચલાવાય છે, જેને <b>servers</b> કહે છે. Kernel ખૂબ નાનું બને છે (<b>microkernel</b>).</p>
<p>Microkernel માત્ર ઓછામાં ઓછા functions રાખે છે:</p>
<ul>
<li><b>Inter-process communication (IPC)</b>, એટલે કે message passing</li>
<li>મૂળભૂત <b>CPU scheduling</b> અને process/thread management</li>
<li>મૂળભૂત <b>memory management</b></li>
</ul>
<p>File system, device drivers, networking વગેરે <b>user-level servers</b> તરીકે ચાલે છે. Application ને file વાંચવી હોય ત્યારે તે <b>microkernel દ્વારા</b> file server ને <b>message</b> મોકલે છે; file server કામ કરી message વડે જવાબ આપે છે.</p>
<h4>ફાયદા</h4>
<ul>
<li><b>Reliability અને security:</b> કોઈ server (દા.ત. driver) fail થાય તો માત્ર તે server restart થાય; kernel ચાલુ રહે.</li>
<li><b>Extend કરવું સરળ:</b> kernel બદલ્યા વગર નવી services user-mode servers તરીકે ઉમેરાય.</li>
<li><b>Portability:</b> નાનું kernel નવા hardware પર સરળતાથી લઈ જવાય.</li>
</ul>
<h4>ગેરફાયદા</h4>
<ul>
<li><b>ઓછું performance:</b> ઘણા messages અને user–kernel mode switches overhead ઉમેરે.</li>
</ul>
<p><b>ઉદાહરણ:</b> QNX (cars માં વપરાય), MINIX 3, L4, Mach. <b>Hybrid kernels</b> બંને વિચાર ભેગા કરે: macOS (XNU = Mach + BSD) અને Windows NT.</p>""",
          diagram="os1_microkernel"),
        T("1.3.4 Comparison: Monolithic vs Layered vs Microkernel", "1.3.4 સરખામણી: Monolithic vs Layered vs Microkernel",
          """<p>The comparison is often asked as a 4-mark question (monolithic vs microkernel).</p>
""" + STR_EN,
          """<p>આ સરખામણી ઘણી વાર 4 ગુણના પ્રશ્ન તરીકે પૂછાય છે (monolithic vs microkernel).</p>
""" + STR_GU),
    ]}

SEC_1_4 = {
    "title": {"en": "1.4 Case Study: Linux, Windows and macOS", "gu": "1.4 Case Study: Linux, Windows અને macOS"},
    "items": [
        T("1.4.1 Linux Operating System", "1.4.1 Linux Operating System",
          """<p><b>Linux</b> is a <b>free and open-source, Unix-like</b> operating system. Its kernel was first written by <b>Linus Torvalds</b> (a Finnish student) in <b>1991</b>, and it is now developed by thousands of programmers worldwide under the <b>GNU GPL</b> licence. A complete Linux system = Linux kernel + GNU tools + other software, packaged as a <b>distribution (distro)</b>.</p>
<h4>Structure (layers)</h4>
<ol>
<li><b>Hardware:</b> CPU, memory, disk, devices.</li>
<li><b>Kernel:</b> the core: process scheduling, memory management, file system, device drivers, networking. It is <b>monolithic but modular</b> (loadable kernel modules).</li>
<li><b>Shell:</b> command interpreter between the user and the kernel (bash, zsh).</li>
<li><b>Applications and utilities:</b> commands (ls, cp, grep), compilers (gcc), editors, browsers, desktop (GNOME, KDE).</li>
</ol>
<h4>Features</h4>
<ul>
<li><b>Open source and free;</b> anyone can study and modify the code.</li>
<li><b>Multi-user and multitasking.</b></li>
<li><b>Portable:</b> runs on PCs, servers, phones (Android uses the Linux kernel), embedded devices and all of the world's top supercomputers.</li>
<li><b>Secure:</b> file permissions (read/write/execute), user accounts, root/superuser.</li>
<li><b>Hierarchical file system</b> starting from root <code>/</code>; file systems ext4, Btrfs, XFS.</li>
<li>Powerful <b>shell</b> and scripting; GUI desktops are also available.</li>
</ul>
<p><b>Popular distributions:</b> Ubuntu, Fedora, Debian, Linux Mint, Red Hat Enterprise Linux (RHEL), Kali Linux.</p>
<p><b>Uses:</b> web servers, cloud, Android phones, routers, smart TVs, programming and education.</p>""",
          """<p><b>Linux</b> એક <b>free અને open-source, Unix-જેવી</b> operating system છે. તેનું kernel સૌપ્રથમ <b>Linus Torvalds</b> (Finland ના વિદ્યાર્થી) એ <b>1991</b> માં લખ્યું હતું, અને હવે વિશ્વના હજારો programmers <b>GNU GPL</b> licence હેઠળ તેને વિકસાવે છે. સંપૂર્ણ Linux system = Linux kernel + GNU tools + બીજું software, જે <b>distribution (distro)</b> તરીકે મળે છે.</p>
<h4>Structure (layers)</h4>
<ol>
<li><b>Hardware:</b> CPU, memory, disk, devices.</li>
<li><b>Kernel:</b> મુખ્ય ભાગ: process scheduling, memory management, file system, device drivers, networking. તે <b>monolithic પણ modular</b> છે (loadable kernel modules).</li>
<li><b>Shell:</b> user અને kernel વચ્ચેનો command interpreter (bash, zsh).</li>
<li><b>Applications અને utilities:</b> commands (ls, cp, grep), compilers (gcc), editors, browsers, desktop (GNOME, KDE).</li>
</ol>
<h4>લક્ષણો</h4>
<ul>
<li><b>Open source અને free;</b> કોઈ પણ code નો અભ્યાસ કરી બદલી શકે.</li>
<li><b>Multi-user અને multitasking.</b></li>
<li><b>Portable:</b> PCs, servers, phones (Android Linux kernel વાપરે છે), embedded devices અને વિશ્વના બધા top supercomputers પર ચાલે.</li>
<li><b>Secure:</b> file permissions (read/write/execute), user accounts, root/superuser.</li>
<li>Root <code>/</code> થી શરૂ થતી <b>hierarchical file system</b>; file systems ext4, Btrfs, XFS.</li>
<li>શક્તિશાળી <b>shell</b> અને scripting; GUI desktops પણ ઉપલબ્ધ.</li>
</ul>
<p><b>લોકપ્રિય distributions:</b> Ubuntu, Fedora, Debian, Linux Mint, Red Hat Enterprise Linux (RHEL), Kali Linux.</p>
<p><b>ઉપયોગ:</b> web servers, cloud, Android phones, routers, smart TVs, programming અને શિક્ષણ.</p>""",
          diagram="os1_linux"),
        T("1.4.2 Microsoft Windows (Latest: Windows 11)", "1.4.2 Microsoft Windows (નવીનતમ: Windows 11)",
          """<p><b>Microsoft Windows</b> is the most widely used desktop OS, developed by <b>Microsoft</b>. It is a <b>closed-source, commercial (paid)</b> OS with a graphical user interface. The first version, Windows 1.0, came in 1985. Since <b>Windows NT</b> (1993), all versions use the <b>NT kernel</b>, a <b>hybrid kernel</b> (microkernel ideas, but most services run in kernel mode for speed).</p>
<p><b>Latest version:</b> <b>Windows 11</b> (first released October 2021). It gets one feature update every year; the latest is <b>version 26H2</b> (September 2026). Support for Windows 10 ended in October 2025.</p>
<h4>Structure (simplified)</h4>
<ul>
<li><b>User mode:</b> applications, environment subsystems (Win32 API), system services.</li>
<li><b>Kernel mode:</b> Executive (I/O manager, memory manager, process manager, security monitor), kernel, device drivers and the <b>HAL</b> (Hardware Abstraction Layer, which hides hardware differences).</li>
</ul>
<h4>Features of Windows 11</h4>
<ul>
<li>Modern GUI: centred <b>Start menu and taskbar</b>, snap layouts, virtual desktops, widgets.</li>
<li><b>Security:</b> needs <b>TPM 2.0</b> and Secure Boot; Windows Hello (face/fingerprint login), Microsoft Defender, BitLocker.</li>
<li><b>AI features:</b> Copilot assistant and AI actions in File Explorer.</li>
<li>File system <b>NTFS</b>; command line through <b>PowerShell</b> and Command Prompt; <b>WSL</b> to run Linux inside Windows.</li>
<li>Runs on x86-64 and ARM PCs; huge support for software, games and hardware drivers.</li>
</ul>
<h4>Limitations</h4>
<ul><li>Paid licence; closed source.</li><li>Higher hardware requirements; the most targeted OS for malware.</li></ul>""",
          """<p><b>Microsoft Windows</b> સૌથી વધુ વપરાતી desktop OS છે, જે <b>Microsoft</b> એ વિકસાવી છે. તે graphical user interface વાળી <b>closed-source, commercial (paid)</b> OS છે. પહેલું version Windows 1.0 1985 માં આવ્યું. <b>Windows NT</b> (1993) થી બધા versions <b>NT kernel</b> વાપરે છે, જે <b>hybrid kernel</b> છે (microkernel ના વિચારો, પણ ઝડપ માટે મોટા ભાગની services kernel mode માં ચાલે).</p>
<p><b>નવીનતમ version:</b> <b>Windows 11</b> (પહેલી વાર October 2021 માં). દર વર્ષે એક feature update મળે છે; નવીનતમ <b>version 26H2</b> (September 2026) છે. Windows 10 નો support October 2025 માં પૂરો થયો.</p>
<h4>Structure (સરળ)</h4>
<ul>
<li><b>User mode:</b> applications, environment subsystems (Win32 API), system services.</li>
<li><b>Kernel mode:</b> Executive (I/O manager, memory manager, process manager, security monitor), kernel, device drivers અને <b>HAL</b> (Hardware Abstraction Layer, જે hardware ના તફાવતો છુપાવે છે).</li>
</ul>
<h4>Windows 11 ના લક્ષણો</h4>
<ul>
<li>આધુનિક GUI: વચ્ચે <b>Start menu અને taskbar</b>, snap layouts, virtual desktops, widgets.</li>
<li><b>Security:</b> <b>TPM 2.0</b> અને Secure Boot જરૂરી; Windows Hello (face/fingerprint login), Microsoft Defender, BitLocker.</li>
<li><b>AI features:</b> Copilot assistant અને File Explorer માં AI actions.</li>
<li>File system <b>NTFS</b>; <b>PowerShell</b> અને Command Prompt દ્વારા command line; Windows ની અંદર Linux ચલાવવા <b>WSL</b>.</li>
<li>x86-64 અને ARM PCs પર ચાલે; software, games અને hardware drivers નો વિશાળ support.</li>
</ul>
<h4>મર્યાદાઓ</h4>
<ul><li>Paid licence; closed source.</li><li>વધુ hardware જરૂરિયાત; malware નું સૌથી વધુ નિશાન બનતી OS.</li></ul>"""),
        T("1.4.3 Apple macOS", "1.4.3 Apple macOS",
          """<p><b>macOS</b> (earlier Mac OS X / OS X) is the operating system of Apple's <b>Mac</b> computers (MacBook, iMac, Mac mini). It is a <b>Unix-based</b> OS, officially certified as UNIX, and it is <b>free with every Mac</b> but runs only on Apple hardware.</p>
<p><b>Latest version:</b> <b>macOS 27 "Golden Gate"</b> (September 2026). It runs only on Macs with <b>Apple silicon</b> (M-series chips); support for Intel Macs has ended. The previous version, macOS 26 Tahoe, introduced the "Liquid Glass" design.</p>
<h4>Structure</h4>
<ul>
<li><b>Darwin:</b> the open-source Unix core of macOS.</li>
<li><b>XNU kernel</b> ("X is Not Unix"): a <b>hybrid kernel</b> = <b>Mach microkernel</b> (IPC, scheduling, memory) + <b>BSD</b> layer (file system, networking, POSIX API, permissions) + I/O Kit for drivers.</li>
<li>Above it: frameworks (Cocoa), the <b>Aqua</b> GUI and applications.</li>
</ul>
<h4>Features</h4>
<ul>
<li>Clean, consistent GUI: Dock, Finder, Spotlight search, Mission Control.</li>
<li><b>Apple Intelligence</b> and Siri AI features; close integration with iPhone/iPad (Handoff, AirDrop, Continuity).</li>
<li><b>Security:</b> Gatekeeper (only trusted apps), System Integrity Protection (SIP), FileVault encryption, sandboxed apps.</li>
<li>File system <b>APFS</b> (Apple File System); Terminal with <b>zsh</b> shell; Unix commands work.</li>
<li>Very stable and power-efficient because Apple makes both the hardware and the software.</li>
</ul>
<h4>Limitations</h4>
<ul><li>Runs only on costly Apple hardware.</li><li>Fewer games; less customisation; mostly closed source.</li></ul>""",
          """<p><b>macOS</b> (પહેલાં Mac OS X / OS X) Apple ના <b>Mac</b> computers (MacBook, iMac, Mac mini) ની operating system છે. તે <b>Unix-આધારિત</b> OS છે, સત્તાવાર રીતે UNIX તરીકે certified, અને <b>દરેક Mac સાથે free</b> મળે છે પણ માત્ર Apple hardware પર ચાલે છે.</p>
<p><b>નવીનતમ version:</b> <b>macOS 27 "Golden Gate"</b> (September 2026). તે માત્ર <b>Apple silicon</b> (M-series chips) વાળા Macs પર ચાલે છે; Intel Macs નો support પૂરો થયો છે. પાછલા version macOS 26 Tahoe એ "Liquid Glass" design રજૂ કરી હતી.</p>
<h4>Structure</h4>
<ul>
<li><b>Darwin:</b> macOS નો open-source Unix core.</li>
<li><b>XNU kernel</b> ("X is Not Unix"): <b>hybrid kernel</b> = <b>Mach microkernel</b> (IPC, scheduling, memory) + <b>BSD</b> layer (file system, networking, POSIX API, permissions) + drivers માટે I/O Kit.</li>
<li>તેની ઉપર: frameworks (Cocoa), <b>Aqua</b> GUI અને applications.</li>
</ul>
<h4>લક્ષણો</h4>
<ul>
<li>સ્વચ્છ, એકસરખો GUI: Dock, Finder, Spotlight search, Mission Control.</li>
<li><b>Apple Intelligence</b> અને Siri AI features; iPhone/iPad સાથે નજીકનું integration (Handoff, AirDrop, Continuity).</li>
<li><b>Security:</b> Gatekeeper (માત્ર વિશ્વસનીય apps), System Integrity Protection (SIP), FileVault encryption, sandboxed apps.</li>
<li>File system <b>APFS</b> (Apple File System); <b>zsh</b> shell સાથે Terminal; Unix commands ચાલે.</li>
<li>Apple hardware અને software બંને બનાવે છે તેથી ખૂબ stable અને power-efficient.</li>
</ul>
<h4>મર્યાદાઓ</h4>
<ul><li>માત્ર મોંઘા Apple hardware પર ચાલે.</li><li>ઓછી games; ઓછું customisation; મોટા ભાગે closed source.</li></ul>"""),
        T("1.4.4 Comparison: Linux vs Windows vs macOS", "1.4.4 સરખામણી: Linux vs Windows vs macOS",
          """<p>This comparison is the subject of <b>Practical 1</b> (case study of Linux, latest Windows and macOS). The chart gives the main points.</p>
<h4>Which to choose?</h4>
<ul>
<li><b>Linux:</b> servers, programming, networking, students who want a free and customisable system.</li>
<li><b>Windows:</b> general office and home use, gaming, widest software support.</li>
<li><b>macOS:</b> graphics, video editing, app development for Apple devices, users of iPhone/iPad.</li>
</ul>
<p><b>Common points:</b> all three are multi-user, multitasking, multithreaded and support networking, GUI, virtual memory and multi-core CPUs.</p>""",
          """<p>આ સરખામણી <b>Practical 1</b> (Linux, નવીનતમ Windows અને macOS નો case study) નો વિષય છે. Chart મુખ્ય મુદ્દા આપે છે.</p>
<h4>કઈ પસંદ કરવી?</h4>
<ul>
<li><b>Linux:</b> servers, programming, networking, free અને customisable system ઇચ્છતા વિદ્યાર્થીઓ.</li>
<li><b>Windows:</b> સામાન્ય office અને ઘરનો ઉપયોગ, gaming, સૌથી વધુ software support.</li>
<li><b>macOS:</b> graphics, video editing, Apple devices માટે app development, iPhone/iPad ના users.</li>
</ul>
<p><b>સામાન્ય મુદ્દા:</b> ત્રણેય multi-user, multitasking, multithreaded છે અને networking, GUI, virtual memory અને multi-core CPUs support કરે છે.</p>""",
          diagram="os1_case"),
    ]}
