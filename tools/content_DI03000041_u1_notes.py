"""Fundamentals of Operating System (DI03000041) - Unit 1 notes part A: 1.1 Introduction, goals, services; 1.2 Types of OS."""
from content_DI03000011_u1_notes_a import T


def tbl(head, rows_):
    h = "<table><tr>" + "".join(f"<th>{x}</th>" for x in head) + "</tr>"
    for r in rows_:
        h += "<tr>" + "".join(f"<td>{v}</td>" for v in r) + "</tr>"
    return h + "</table>"


TYPES_EN = tbl(["Type", "Main idea", "Main goal", "Example"], [
    ("Multiprogramming", "Many jobs in memory; CPU switches when a job waits for I/O", "Maximum CPU utilisation", "IBM OS/360"),
    ("Time sharing", "CPU time divided into small slices among users", "Minimum response time", "Unix, Multics"),
    ("Real time", "Result must come within a fixed deadline", "Meet deadlines", "VxWorks, QNX"),
    ("Multithreading", "One process has many threads running together", "Responsiveness, parallelism", "Windows, Linux"),
    ("Distributed", "Many networked computers look like one system", "Resource sharing, reliability", "Amoeba, LOCUS"),
    ("Embedded", "Built into a device for a dedicated job", "Small size, low power", "FreeRTOS, Embedded Linux")])
TYPES_GU = tbl(["પ્રકાર", "મુખ્ય વિચાર", "મુખ્ય ધ્યેય", "ઉદાહરણ"], [
    ("Multiprogramming", "Memory માં ઘણા jobs; job I/O ની રાહ જુએ ત્યારે CPU બીજા job પર જાય", "મહત્તમ CPU utilisation", "IBM OS/360"),
    ("Time sharing", "CPU time ના નાના ભાગ users વચ્ચે વહેંચાય", "ઓછામાં ઓછો response time", "Unix, Multics"),
    ("Real time", "પરિણામ નક્કી deadline માં મળવું જોઈએ", "Deadlines પૂરી કરવી", "VxWorks, QNX"),
    ("Multithreading", "એક process માં ઘણા threads સાથે ચાલે", "Responsiveness, parallelism", "Windows, Linux"),
    ("Distributed", "Network થી જોડાયેલા ઘણા computers એક system જેવા દેખાય", "Resource sharing, reliability", "Amoeba, LOCUS"),
    ("Embedded", "ચોક્કસ કામ માટે device માં જ બનાવેલી", "નાનું કદ, ઓછો power", "FreeRTOS, Embedded Linux")])

MP_TS_EN = tbl(["Point", "Multiprogramming", "Time sharing"], [
    ("Aim", "Maximise CPU use", "Minimise response time"),
    ("CPU switch when", "Running job waits for I/O", "Time slice (quantum) ends, or I/O"),
    ("User interaction", "Little or none (batch jobs)", "Interactive; many users at terminals"),
    ("Extra need", "Job scheduling, memory management", "CPU scheduling, fast context switch, protection"),
    ("Example", "IBM OS/360", "Unix, Linux")])
MP_TS_GU = tbl(["મુદ્દો", "Multiprogramming", "Time sharing"], [
    ("હેતુ", "CPU નો મહત્તમ ઉપયોગ", "Response time ઓછો કરવો"),
    ("CPU ક્યારે બદલાય", "ચાલતો job I/O ની રાહ જુએ ત્યારે", "Time slice (quantum) પૂરો થાય, અથવા I/O"),
    ("User interaction", "ઓછું કે નહીં (batch jobs)", "Interactive; terminals પર ઘણા users"),
    ("વધારાની જરૂર", "Job scheduling, memory management", "CPU scheduling, ઝડપી context switch, protection"),
    ("ઉદાહરણ", "IBM OS/360", "Unix, Linux")])

HS_EN = tbl(["Point", "Hard real-time", "Soft real-time"], [
    ("Deadline", "Must always be met", "Small misses are allowed"),
    ("Missed deadline", "System failure, may be dangerous", "Only quality / performance drops"),
    ("Use of disk, virtual memory", "Avoided (unpredictable delay)", "Can be used"),
    ("Examples", "Airbag, pacemaker, ABS, missile control", "Video streaming, online games, VoIP")])
HS_GU = tbl(["મુદ્દો", "Hard real-time", "Soft real-time"], [
    ("Deadline", "હંમેશા પૂરી થવી જ જોઈએ", "નાની ચૂક ચાલે"),
    ("Deadline ચૂકે તો", "System failure, જોખમી બની શકે", "માત્ર quality / performance ઘટે"),
    ("Disk, virtual memory નો ઉપયોગ", "ટાળવામાં આવે (અનિશ્ચિત delay)", "વાપરી શકાય"),
    ("ઉદાહરણ", "Airbag, pacemaker, ABS, missile control", "Video streaming, online games, VoIP")])

SEC_1_1 = {
    "title": {"en": "1.1 Introduction: Goals and Services of OS", "gu": "1.1 પરિચય: OS ના Goals અને Services"},
    "items": [
        T("1.1.1 What is an Operating System?", "1.1.1 Operating System શું છે?",
          """<p>An <b>Operating System (OS)</b> is a <b>system software</b> that acts as an <b>interface between the user and the computer hardware</b>. It manages all hardware and software resources and provides an environment in which users can run programs <b>conveniently</b> and <b>efficiently</b>.</p>
<p>The OS is the first program loaded into memory when the computer starts (<b>booting</b>), and it keeps running until the computer is shut down. The part of the OS that is always in memory is called the <b>kernel</b>.</p>
<h4>Components of a computer system</h4>
<ol>
<li><b>Hardware:</b> CPU, memory, disk and I/O devices: the basic computing resources.</li>
<li><b>Operating system:</b> controls the hardware and coordinates its use among the various programs and users.</li>
<li><b>Application programs:</b> word processors, compilers, web browsers, games: they use the resources to solve users' problems.</li>
<li><b>Users:</b> people, machines or other computers.</li>
</ol>
<h4>Two views of an OS</h4>
<ul>
<li><b>User view:</b> the OS is a program that makes the computer <b>easy to use</b> (good interface, ease of use).</li>
<li><b>System view:</b> the OS is a <b>resource allocator</b> (decides who gets the CPU, memory, files and devices, and for how long) and a <b>control program</b> (controls the running of user programs and prevents errors and misuse).</li>
</ul>
<p><b>Examples:</b> Microsoft Windows, Linux (Ubuntu, Fedora), macOS, Unix, Android, iOS.</p>""",
          """<p><b>Operating System (OS)</b> એક <b>system software</b> છે જે <b>user અને computer hardware વચ્ચે interface</b> તરીકે કામ કરે છે. તે બધા hardware અને software resources નું management કરે છે અને એવું વાતાવરણ આપે છે જેમાં users programs ને <b>સરળતાથી</b> અને <b>કાર્યક્ષમ રીતે</b> ચલાવી શકે.</p>
<p>Computer શરૂ થાય ત્યારે (<b>booting</b>) memory માં load થતો પહેલો program OS છે, અને computer બંધ થાય ત્યાં સુધી તે ચાલતો રહે છે. OS નો જે ભાગ હંમેશા memory માં રહે છે તેને <b>kernel</b> કહે છે.</p>
<h4>Computer system ના ઘટકો</h4>
<ol>
<li><b>Hardware:</b> CPU, memory, disk અને I/O devices: મૂળભૂત computing resources.</li>
<li><b>Operating system:</b> hardware ને control કરે છે અને જુદા જુદા programs અને users વચ્ચે તેના ઉપયોગનું સંકલન કરે છે.</li>
<li><b>Application programs:</b> word processors, compilers, web browsers, games: users ની સમસ્યાઓ ઉકેલવા resources વાપરે છે.</li>
<li><b>Users:</b> લોકો, machines અથવા બીજા computers.</li>
</ol>
<h4>OS ના બે દૃષ્ટિકોણ</h4>
<ul>
<li><b>User view:</b> OS એ computer ને <b>વાપરવામાં સરળ</b> બનાવતો program છે (સારો interface, ease of use).</li>
<li><b>System view:</b> OS એ <b>resource allocator</b> છે (CPU, memory, files અને devices કોને અને કેટલા સમય માટે મળે તે નક્કી કરે) અને <b>control program</b> છે (user programs ના execution ને control કરે અને errors તથા દુરુપયોગ અટકાવે).</li>
</ul>
<p><b>ઉદાહરણ:</b> Microsoft Windows, Linux (Ubuntu, Fedora), macOS, Unix, Android, iOS.</p>""",
          diagram="os1_role"),
        T("1.1.2 Fundamental Goals and Functions of OS", "1.1.2 OS ના મૂળભૂત Goals અને Functions",
          """<h4>Fundamental goals</h4>
<ol>
<li><b>Convenience:</b> make the computer easy to use; hide hardware details behind a simple interface.</li>
<li><b>Efficiency:</b> use the CPU, memory and devices in the best possible way (high throughput, little idle time).</li>
<li><b>Ability to evolve:</b> allow new hardware, new services and bug fixes to be added without disturbing existing work.</li>
</ol>
<p>Other goals: <b>reliability</b> (work correctly without crashing), <b>security and protection</b> of data, and <b>fairness</b> among users.</p>
<h4>Functions of an OS</h4>
<ol>
<li><b>Process management:</b> creating and deleting processes, scheduling them on the CPU, suspending/resuming, process synchronisation and communication, deadlock handling.</li>
<li><b>Memory management:</b> keeping track of which part of memory is used and by whom, allocating and freeing memory, deciding which process to load (virtual memory).</li>
<li><b>File management:</b> creating, deleting, reading and writing files and directories; mapping files to disk; backup.</li>
<li><b>Device (I/O) management:</b> controlling devices through <b>device drivers</b>, buffering, caching and spooling.</li>
<li><b>Secondary storage management:</b> free-space management, storage allocation and <b>disk scheduling</b>.</li>
<li><b>Security and protection:</b> user login and passwords, access rights to files and memory, protection from viruses.</li>
<li><b>Networking / communication:</b> data exchange among computers over a network.</li>
<li><b>User interface:</b> command line (CLI), graphical (GUI) or touch interface.</li>
<li><b>Error detection and accounting:</b> detect hardware/software errors and keep records of resource use.</li>
</ol>""",
          """<h4>મૂળભૂત goals</h4>
<ol>
<li><b>Convenience (સુવિધા):</b> computer ને વાપરવામાં સરળ બનાવવું; hardware ની વિગતો સરળ interface પાછળ છુપાવવી.</li>
<li><b>Efficiency (કાર્યક્ષમતા):</b> CPU, memory અને devices નો શ્રેષ્ઠ ઉપયોગ કરવો (વધુ throughput, ઓછો idle time).</li>
<li><b>Ability to evolve (વિકાસ ક્ષમતા):</b> ચાલુ કામને ખલેલ વગર નવા hardware, નવી services અને bug fixes ઉમેરી શકાય.</li>
</ol>
<p>બીજા goals: <b>reliability</b> (crash વગર સાચું કામ), data ની <b>security અને protection</b>, અને users વચ્ચે <b>fairness</b>.</p>
<h4>OS ના functions</h4>
<ol>
<li><b>Process management:</b> processes બનાવવી અને delete કરવી, CPU પર schedule કરવી, suspend/resume, process synchronisation અને communication, deadlock handling.</li>
<li><b>Memory management:</b> memory નો કયો ભાગ કોણ વાપરે છે તેનો હિસાબ રાખવો, memory આપવી અને મુક્ત કરવી, કયો process load કરવો તે નક્કી કરવું (virtual memory).</li>
<li><b>File management:</b> files અને directories બનાવવી, delete કરવી, read અને write કરવી; files ને disk સાથે map કરવી; backup.</li>
<li><b>Device (I/O) management:</b> <b>device drivers</b> દ્વારા devices નું control, buffering, caching અને spooling.</li>
<li><b>Secondary storage management:</b> free-space management, storage allocation અને <b>disk scheduling</b>.</li>
<li><b>Security અને protection:</b> user login અને passwords, files અને memory ના access rights, viruses થી રક્ષણ.</li>
<li><b>Networking / communication:</b> network પર computers વચ્ચે data ની આપ-લે.</li>
<li><b>User interface:</b> command line (CLI), graphical (GUI) અથવા touch interface.</li>
<li><b>Error detection અને accounting:</b> hardware/software errors શોધવી અને resource ઉપયોગનો record રાખવો.</li>
</ol>""",
          diagram="os1_functions"),
        T("1.1.3 Operating System Services", "1.1.3 Operating System Services",
          """<p>An OS provides an environment for running programs. It offers certain <b>services</b> to programs and users. Programs request these services through <b>system calls</b> (e.g. <code>fork()</code>, <code>open()</code>, <code>read()</code>, <code>write()</code>), which form the interface between a running program and the OS.</p>
<h4>(A) Services that help the user</h4>
<ol>
<li><b>User interface:</b> CLI (commands typed in a shell), GUI (windows, icons, mouse) or touch screen.</li>
<li><b>Program execution:</b> load a program into memory, run it, and end it normally or abnormally (with an error).</li>
<li><b>I/O operations:</b> a running program may need a file or device; users cannot control devices directly, so the OS does the I/O.</li>
<li><b>File-system manipulation:</b> create, delete, read, write, search and list files and directories; manage permissions.</li>
<li><b>Communication:</b> processes exchange data on the same computer or over a network, using <b>shared memory</b> or <b>message passing</b>.</li>
<li><b>Error detection:</b> detect and handle errors in CPU, memory, I/O devices (e.g. printer out of paper) and user programs (e.g. divide by zero).</li>
</ol>
<h4>(B) Services for efficient operation of the system</h4>
<ol>
<li><b>Resource allocation:</b> when many users or jobs run together, the OS allocates CPU cycles, memory, files and devices to each of them.</li>
<li><b>Accounting:</b> keeps track of which user uses how much and what kind of resources (for billing or usage statistics).</li>
<li><b>Protection and security:</b> <b>protection</b> controls the access of processes to resources; <b>security</b> defends the system from outsiders using passwords/authentication.</li>
</ol>""",
          """<p>OS programs ચલાવવા માટે વાતાવરણ આપે છે. તે programs અને users ને કેટલીક <b>services</b> આપે છે. Programs આ services <b>system calls</b> (દા.ત. <code>fork()</code>, <code>open()</code>, <code>read()</code>, <code>write()</code>) દ્વારા માંગે છે, જે ચાલતા program અને OS વચ્ચેનો interface છે.</p>
<h4>(A) User ને મદદ કરતી services</h4>
<ol>
<li><b>User interface:</b> CLI (shell માં commands type કરવા), GUI (windows, icons, mouse) અથવા touch screen.</li>
<li><b>Program execution:</b> program ને memory માં load કરવો, ચલાવવો, અને સામાન્ય રીતે અથવા અસામાન્ય રીતે (error સાથે) પૂરો કરવો.</li>
<li><b>I/O operations:</b> ચાલતા program ને file કે device જોઈએ; users devices ને સીધા control કરી શકતા નથી, તેથી OS I/O કરે છે.</li>
<li><b>File-system manipulation:</b> files અને directories બનાવવી, delete, read, write, search અને list કરવી; permissions સંભાળવી.</li>
<li><b>Communication:</b> processes એક જ computer પર કે network પર <b>shared memory</b> અથવા <b>message passing</b> વડે data ની આપ-લે કરે.</li>
<li><b>Error detection:</b> CPU, memory, I/O devices (દા.ત. printer માં કાગળ ખતમ) અને user programs (દા.ત. શૂન્ય વડે ભાગાકાર) ની errors શોધી સંભાળવી.</li>
</ol>
<h4>(B) System ના કાર્યક્ષમ સંચાલન માટેની services</h4>
<ol>
<li><b>Resource allocation:</b> ઘણા users કે jobs સાથે ચાલે ત્યારે OS દરેકને CPU cycles, memory, files અને devices ફાળવે છે.</li>
<li><b>Accounting:</b> કયો user કેટલા અને કેવા resources વાપરે છે તેનો હિસાબ રાખે (billing અથવા usage statistics માટે).</li>
<li><b>Protection અને security:</b> <b>protection</b> processes ના resources પરના access ને control કરે છે; <b>security</b> passwords/authentication વડે બહારના લોકોથી system નું રક્ષણ કરે છે.</li>
</ol>""",
          diagram="os1_services"),
    ]}

SEC_1_2 = {
    "title": {"en": "1.2 Types of Operating System", "gu": "1.2 Operating System ના પ્રકારો"},
    "items": [
        T("1.2.1 Multiprogramming Operating System", "1.2.1 Multiprogramming Operating System",
          """<p>In early <b>batch systems</b>, only one job was in memory. When that job waited for I/O (which is very slow compared to the CPU), the CPU stayed <b>idle</b>.</p>
<p>A <b>multiprogramming OS</b> keeps <b>several jobs in main memory at the same time</b>. The OS picks one job and runs it. When this job has to wait for an I/O operation, the OS <b>switches the CPU to another job</b>. When that job waits, the CPU switches again, and so on. As long as at least one job is ready, the CPU is never idle.</p>
<p><b>Real-life example:</b> a lawyer works on one case; while waiting for a court date, he works on another case instead of sitting idle.</p>
<h4>Requirements</h4>
<ul>
<li><b>Job scheduling:</b> choose which jobs from disk are brought into memory.</li>
<li><b>Memory management:</b> many jobs must share memory.</li>
<li><b>CPU scheduling:</b> choose which ready job runs next.</li>
<li><b>Protection:</b> one job must not disturb another.</li>
</ul>
<h4>Advantages</h4>
<ul><li>High <b>CPU utilisation</b> and throughput.</li><li>Less idle time of CPU and devices.</li></ul>
<h4>Disadvantages</h4>
<ul><li>No direct user interaction with a running job.</li><li>Complex scheduling and memory management; a long job may make others wait.</li></ul>
<p><b>Degree of multiprogramming</b> = number of processes in memory at a time.</p>""",
          """<p>શરૂઆતની <b>batch systems</b> માં memory માં માત્ર એક job રહેતો. તે job I/O ની રાહ જુએ (જે CPU ની સરખામણીએ ઘણું ધીમું છે) ત્યારે CPU <b>idle</b> રહેતું.</p>
<p><b>Multiprogramming OS</b> એક જ સમયે <b>main memory માં ઘણા jobs</b> રાખે છે. OS એક job પસંદ કરી તેને ચલાવે છે. આ job ને I/O operation ની રાહ જોવી પડે ત્યારે OS <b>CPU ને બીજા job પર switch કરે છે</b>. તે job રાહ જુએ ત્યારે ફરી switch થાય, વગેરે. ઓછામાં ઓછો એક job ready હોય ત્યાં સુધી CPU ક્યારેય idle રહેતું નથી.</p>
<p><b>રોજિંદું ઉદાહરણ:</b> વકીલ એક case પર કામ કરે છે; court ની તારીખની રાહ જોતી વખતે બેસી રહેવાને બદલે બીજા case પર કામ કરે છે.</p>
<h4>જરૂરિયાતો</h4>
<ul>
<li><b>Job scheduling:</b> disk પરથી કયા jobs memory માં લાવવા તે પસંદ કરવું.</li>
<li><b>Memory management:</b> ઘણા jobs એ memory વહેંચવી પડે.</li>
<li><b>CPU scheduling:</b> કયો ready job આગળ ચાલશે તે પસંદ કરવું.</li>
<li><b>Protection:</b> એક job બીજાને ખલેલ ન પહોંચાડે.</li>
</ul>
<h4>ફાયદા</h4>
<ul><li>વધુ <b>CPU utilisation</b> અને throughput.</li><li>CPU અને devices નો idle time ઓછો.</li></ul>
<h4>ગેરફાયદા</h4>
<ul><li>ચાલતા job સાથે user નું સીધું interaction નહીં.</li><li>જટિલ scheduling અને memory management; લાંબો job બીજાને રાહ જોવડાવી શકે.</li></ul>
<p><b>Degree of multiprogramming</b> = એક સમયે memory માં રહેલી processes ની સંખ્યા.</p>""",
          diagram="os1_multiprog"),
        T("1.2.2 Time-Sharing (Multitasking) Operating System", "1.2.2 Time-Sharing (Multitasking) Operating System",
          """<p>A <b>time-sharing OS</b> is a logical extension of multiprogramming. The <b>CPU time is divided into small slices</b> called the <b>time quantum</b> (typically 10–100 ms). The CPU executes each user's program for one quantum and then switches to the next one in turn.</p>
<p>The switching is so fast that <b>each user feels that he has the whole computer</b>, although many users share it through their terminals. It is also called <b>multitasking</b> (one user running many programs together, e.g. music player + browser + editor).</p>
<h4>Features</h4>
<ul>
<li><b>Interactive:</b> the user gives commands and gets the response immediately.</li>
<li>Uses <b>CPU scheduling</b> (e.g. Round Robin) and fast <b>context switching</b>.</li>
<li>Needs <b>memory management</b>, <b>virtual memory</b>, file system and <b>protection</b>.</li>
</ul>
<h4>Advantages</h4>
<ul><li>Quick <b>response time</b>; many users share costly hardware.</li><li>Reduces CPU idle time; avoids duplication of software.</li></ul>
<h4>Disadvantages</h4>
<ul><li>Problems of reliability, security and data integrity.</li><li>Overhead of frequent context switches; data communication problems.</li></ul>
<p><b>Examples:</b> Unix, Linux, Multics, Windows (desktop multitasking).</p>
<h4>Multiprogramming vs Time sharing</h4>
""" + MP_TS_EN,
          """<p><b>Time-sharing OS</b> એ multiprogramming નું તાર્કિક વિસ્તરણ છે. <b>CPU time ને નાના ભાગો</b> માં વહેંચવામાં આવે છે જેને <b>time quantum</b> (સામાન્ય રીતે 10–100 ms) કહે છે. CPU દરેક user ના program ને એક quantum સુધી ચલાવે છે અને પછી વારાફરતી બીજા પર જાય છે.</p>
<p>Switching એટલું ઝડપી છે કે ઘણા users terminals દ્વારા computer વહેંચતા હોવા છતાં <b>દરેક user ને લાગે છે કે આખું computer તેનું જ છે</b>. તેને <b>multitasking</b> પણ કહે છે (એક user ઘણા programs સાથે ચલાવે, દા.ત. music player + browser + editor).</p>
<h4>લક્ષણો</h4>
<ul>
<li><b>Interactive:</b> user commands આપે અને તરત response મળે.</li>
<li><b>CPU scheduling</b> (દા.ત. Round Robin) અને ઝડપી <b>context switching</b> વાપરે.</li>
<li><b>Memory management</b>, <b>virtual memory</b>, file system અને <b>protection</b> જરૂરી.</li>
</ul>
<h4>ફાયદા</h4>
<ul><li>ઝડપી <b>response time</b>; ઘણા users મોંઘું hardware વહેંચે.</li><li>CPU idle time ઘટે; software નું duplication ટળે.</li></ul>
<h4>ગેરફાયદા</h4>
<ul><li>Reliability, security અને data integrity ની સમસ્યા.</li><li>વારંવાર context switch નો overhead; data communication ની સમસ્યા.</li></ul>
<p><b>ઉદાહરણ:</b> Unix, Linux, Multics, Windows (desktop multitasking).</p>
<h4>Multiprogramming vs Time sharing</h4>
""" + MP_TS_GU,
          diagram="os1_timeshare"),
        T("1.2.3 Real-Time Operating System (RTOS)", "1.2.3 Real-Time Operating System (RTOS)",
          """<p>A <b>real-time OS</b> is used when the <b>result must be produced within a fixed time limit (deadline)</b>. A correct result that comes late is treated as a wrong result. The time from an event (input) to the system's response is called the <b>response time</b>; in an RTOS it must be small and <b>predictable</b>.</p>
<p>RTOS is used in systems that control machines or processes, using <b>sensors</b> to read data and <b>actuators</b> to act on it.</p>
<h4>Types</h4>
<ol>
<li><b>Hard real-time system:</b> the deadline must <b>always</b> be met. Missing it causes failure, which may be dangerous. Data is kept in fast memory/ROM; virtual memory and long disk delays are avoided. Examples: airbag system, heart pacemaker, anti-lock brakes (ABS), missile and flight control, industrial robots.</li>
<li><b>Soft real-time system:</b> a critical task gets <b>priority</b> over other tasks, but an occasional missed deadline is acceptable; only quality drops. Examples: video/audio streaming, online games, VoIP calls, virtual reality.</li>
</ol>
<h4>Features</h4>
<ul><li>Fast, predictable response; priority-based <b>pre-emptive scheduling</b>.</li><li>High reliability; small size; little user interface.</li></ul>
<p><b>Examples of RTOS:</b> VxWorks, QNX, FreeRTOS, RTLinux, Windows CE.</p>
<h4>Hard vs Soft real-time</h4>
""" + HS_EN,
          """<p><b>Real-time OS</b> ત્યારે વપરાય છે જ્યારે <b>પરિણામ નક્કી સમય મર્યાદા (deadline) માં મળવું જ જોઈએ</b>. મોડું આવેલું સાચું પરિણામ પણ ખોટું ગણાય છે. Event (input) થી system ના response સુધીના સમયને <b>response time</b> કહે છે; RTOS માં તે નાનો અને <b>predictable</b> હોવો જોઈએ.</p>
<p>RTOS machines કે processes ને control કરતી systems માં વપરાય છે, જ્યાં data વાંચવા <b>sensors</b> અને કામ કરવા <b>actuators</b> હોય છે.</p>
<h4>પ્રકારો</h4>
<ol>
<li><b>Hard real-time system:</b> deadline <b>હંમેશા</b> પૂરી થવી જ જોઈએ. ચૂકે તો failure થાય, જે જોખમી બની શકે. Data ઝડપી memory/ROM માં રખાય; virtual memory અને disk ના લાંબા delay ટાળવામાં આવે. ઉદાહરણ: airbag system, heart pacemaker, anti-lock brakes (ABS), missile અને flight control, industrial robots.</li>
<li><b>Soft real-time system:</b> critical task ને બીજા tasks કરતાં <b>priority</b> મળે, પણ ક્યારેક deadline ચૂકાય તો ચાલે; માત્ર quality ઘટે. ઉદાહરણ: video/audio streaming, online games, VoIP calls, virtual reality.</li>
</ol>
<h4>લક્ષણો</h4>
<ul><li>ઝડપી, predictable response; priority આધારિત <b>pre-emptive scheduling</b>.</li><li>ઊંચી reliability; નાનું કદ; ઓછો user interface.</li></ul>
<p><b>RTOS ના ઉદાહરણ:</b> VxWorks, QNX, FreeRTOS, RTLinux, Windows CE.</p>
<h4>Hard vs Soft real-time</h4>
""" + HS_GU,
          diagram="os1_realtime"),
        T("1.2.4 Multithreading Operating System", "1.2.4 Multithreading Operating System",
          """<p>A <b>thread</b> is the smallest unit of CPU execution, also called a <b>light-weight process</b>. Each thread has its own <b>thread ID, program counter, registers and stack</b>, but all threads of a process <b>share the code, data and open files</b> of that process.</p>
<p>A <b>multithreading OS</b> allows <b>one process to have many threads</b> that run concurrently (on one CPU by switching, or truly in parallel on a multi-core CPU).</p>
<p><b>Examples:</b> a web browser loads images in one thread while you scroll in another; a word processor checks spelling, saves automatically and accepts typing at the same time; a web server serves each client in a separate thread.</p>
<h4>Benefits</h4>
<ol>
<li><b>Responsiveness:</b> the program keeps responding even if one part is busy.</li>
<li><b>Resource sharing:</b> threads share memory and files without extra effort.</li>
<li><b>Economy:</b> creating and switching threads is cheaper than processes.</li>
<li><b>Scalability:</b> threads can run in parallel on multi-core processors.</li>
</ol>
<h4>Types of threads</h4>
<ul>
<li><b>User-level threads:</b> managed by a thread library in user space; fast, but the kernel does not know them.</li>
<li><b>Kernel-level threads:</b> managed directly by the OS kernel; slower to create, but the kernel can schedule them on different CPUs.</li>
</ul>
<p>Multithreading models: <b>many-to-one</b>, <b>one-to-one</b> and <b>many-to-many</b> (user threads to kernel threads). Windows, Linux, macOS and Solaris support multithreading.</p>""",
          """<p><b>Thread</b> એ CPU execution નો સૌથી નાનો એકમ છે, જેને <b>light-weight process</b> પણ કહે છે. દરેક thread ને પોતાના <b>thread ID, program counter, registers અને stack</b> હોય છે, પણ process ના બધા threads તે process ના <b>code, data અને open files વહેંચે છે</b>.</p>
<p><b>Multithreading OS</b> <b>એક process માં ઘણા threads</b> ને સાથે ચલાવવા દે છે (એક CPU પર switching વડે, અથવા multi-core CPU પર ખરેખર parallel).</p>
<p><b>ઉદાહરણ:</b> web browser એક thread માં images load કરે અને બીજા thread માં તમે scroll કરો; word processor એક સાથે spelling તપાસે, આપોઆપ save કરે અને typing સ્વીકારે; web server દરેક client ને અલગ thread માં સેવા આપે.</p>
<h4>ફાયદા</h4>
<ol>
<li><b>Responsiveness:</b> એક ભાગ વ્યસ્ત હોય તો પણ program response આપતો રહે.</li>
<li><b>Resource sharing:</b> threads વધારાના પ્રયત્ન વગર memory અને files વહેંચે.</li>
<li><b>Economy:</b> threads બનાવવા અને switch કરવા processes કરતાં સસ્તું.</li>
<li><b>Scalability:</b> multi-core processors પર threads parallel ચાલી શકે.</li>
</ol>
<h4>Threads ના પ્રકાર</h4>
<ul>
<li><b>User-level threads:</b> user space માં thread library વડે સંચાલિત; ઝડપી, પણ kernel તેમને જાણતું નથી.</li>
<li><b>Kernel-level threads:</b> OS kernel સીધું સંચાલન કરે; બનાવવામાં ધીમા, પણ kernel તેમને જુદા CPUs પર schedule કરી શકે.</li>
</ul>
<p>Multithreading models: <b>many-to-one</b>, <b>one-to-one</b> અને <b>many-to-many</b> (user threads થી kernel threads). Windows, Linux, macOS અને Solaris multithreading support કરે છે.</p>""",
          diagram="os1_multithread"),
        T("1.2.5 Distributed Operating System", "1.2.5 Distributed Operating System",
          """<p>A <b>distributed OS</b> manages a group of <b>independent computers (sites/nodes)</b> connected by a <b>communication network</b> and makes them appear to the user as a <b>single computer</b>. Each node has its own CPU, memory and disk (<b>loosely coupled</b> system); nodes communicate by passing messages over the network (LAN/WAN).</p>
<p>The user does not need to know on which machine a program runs or where a file is stored (<b>transparency</b>).</p>
<h4>Advantages</h4>
<ol>
<li><b>Resource sharing:</b> a user at one site can use files, printers and data of another site.</li>
<li><b>Computation speed-up:</b> a job is divided into parts that run on different sites at the same time (<b>load sharing</b>).</li>
<li><b>Reliability:</b> if one site fails, the remaining sites continue to work.</li>
<li><b>Communication:</b> users at different sites exchange information (e-mail, file transfer).</li>
<li><b>Scalability:</b> new computers can be added easily.</li>
</ol>
<h4>Disadvantages</h4>
<ul><li>Complex software; network failure can stop communication.</li><li>Security problems because data travels over the network; costly set-up.</li></ul>
<p><b>Examples:</b> Amoeba, LOCUS, Mach; modern cloud and cluster systems (Google, Hadoop clusters) use the same ideas.</p>
<p><b>Note:</b> a <b>network OS</b> (e.g. Windows Server) lets users access remote machines knowingly; a <b>distributed OS</b> hides the network completely.</p>""",
          """<p><b>Distributed OS</b> <b>communication network</b> થી જોડાયેલા <b>સ્વતંત્ર computers (sites/nodes)</b> ના જૂથનું સંચાલન કરે છે અને user ને તે <b>એક જ computer</b> જેવા દેખાડે છે. દરેક node ને પોતાનું CPU, memory અને disk હોય છે (<b>loosely coupled</b> system); nodes network (LAN/WAN) પર messages મોકલી communicate કરે છે.</p>
<p>Program કયા machine પર ચાલે છે કે file ક્યાં store છે તે user ને જાણવાની જરૂર નથી (<b>transparency</b>).</p>
<h4>ફાયદા</h4>
<ol>
<li><b>Resource sharing:</b> એક site નો user બીજી site ની files, printers અને data વાપરી શકે.</li>
<li><b>Computation speed-up:</b> job ને ભાગોમાં વહેંચી જુદી sites પર એક સાથે ચલાવાય (<b>load sharing</b>).</li>
<li><b>Reliability:</b> એક site fail થાય તો બાકીની sites કામ ચાલુ રાખે.</li>
<li><b>Communication:</b> જુદી sites ના users માહિતીની આપ-લે કરે (e-mail, file transfer).</li>
<li><b>Scalability:</b> નવા computers સરળતાથી ઉમેરી શકાય.</li>
</ol>
<h4>ગેરફાયદા</h4>
<ul><li>જટિલ software; network failure communication અટકાવી શકે.</li><li>Data network પર જાય તેથી security ની સમસ્યા; set-up મોંઘું.</li></ul>
<p><b>ઉદાહરણ:</b> Amoeba, LOCUS, Mach; આધુનિક cloud અને cluster systems (Google, Hadoop clusters) આ જ વિચાર વાપરે છે.</p>
<p><b>નોંધ:</b> <b>network OS</b> (દા.ત. Windows Server) માં users જાણીને remote machines વાપરે છે; <b>distributed OS</b> network ને સંપૂર્ણ છુપાવે છે.</p>""",
          diagram="os1_distributed"),
        T("1.2.6 Embedded Operating System", "1.2.6 Embedded Operating System",
          """<p>An <b>embedded OS</b> is a small OS designed to run inside an <b>embedded system</b>: a computer built into a device to perform a <b>specific, dedicated task</b>. The user usually does not even see it as a computer.</p>
<p>It runs on a <b>microcontroller</b> or small processor, is stored in <b>ROM / flash memory</b>, takes input from <b>sensors or buttons</b>, and controls <b>motors, displays or other outputs</b>.</p>
<h4>Features</h4>
<ul>
<li>Designed for <b>one dedicated job</b>; limited or no user interface.</li>
<li><b>Small size</b>, needs little memory; <b>low power</b> (battery devices).</li>
<li><b>Fast and reliable</b>; often <b>real-time</b>.</li>
<li>Low cost; usually cannot be changed by the user.</li>
</ul>
<h4>Examples of devices</h4>
<p>Washing machine, microwave oven, digital camera, smart TV, set-top box, ATM, car engine control unit, traffic lights, smartwatch, printers and routers, IoT devices.</p>
<p><b>Embedded OS examples:</b> FreeRTOS, Embedded Linux, VxWorks, Zephyr, Windows IoT, Android Things.</p>
<h4>Advantages / disadvantages</h4>
<ul><li><b>+</b> Fast, small, cheap, reliable, low power.</li><li><b>−</b> Limited resources; hard to upgrade; one-purpose only.</li></ul>""",
          """<p><b>Embedded OS</b> એક નાની OS છે જે <b>embedded system</b> ની અંદર ચાલવા માટે બનાવાય છે: <b>ચોક્કસ, નિર્ધારિત કામ</b> કરવા device માં જ બનાવેલું computer. User ઘણી વાર તેને computer તરીકે જોતો પણ નથી.</p>
<p>તે <b>microcontroller</b> કે નાના processor પર ચાલે, <b>ROM / flash memory</b> માં store હોય, <b>sensors અથવા buttons</b> પાસેથી input લે, અને <b>motors, displays અથવા બીજા outputs</b> ને control કરે.</p>
<h4>લક્ષણો</h4>
<ul>
<li><b>એક નિર્ધારિત કામ</b> માટે બનેલી; મર્યાદિત કે કોઈ user interface નહીં.</li>
<li><b>નાનું કદ</b>, ઓછી memory જોઈએ; <b>ઓછો power</b> (battery devices).</li>
<li><b>ઝડપી અને reliable</b>; ઘણી વાર <b>real-time</b>.</li>
<li>ઓછી કિંમત; સામાન્ય રીતે user બદલી શકતો નથી.</li>
</ul>
<h4>Devices ના ઉદાહરણ</h4>
<p>Washing machine, microwave oven, digital camera, smart TV, set-top box, ATM, car engine control unit, traffic lights, smartwatch, printers અને routers, IoT devices.</p>
<p><b>Embedded OS ના ઉદાહરણ:</b> FreeRTOS, Embedded Linux, VxWorks, Zephyr, Windows IoT, Android Things.</p>
<h4>ફાયદા / ગેરફાયદા</h4>
<ul><li><b>+</b> ઝડપી, નાની, સસ્તી, reliable, ઓછો power.</li><li><b>−</b> મર્યાદિત resources; upgrade મુશ્કેલ; માત્ર એક હેતુ.</li></ul>""",
          diagram="os1_embedded"),
        T("1.2.7 Comparison of Types of OS", "1.2.7 OS ના પ્રકારોની સરખામણી",
          """<p>The table below summarises the six types of OS in the syllabus. A modern OS such as Linux or Windows combines several of them: it is multiprogrammed, time-shared and multithreaded, and supports networking.</p>
""" + TYPES_EN,
          """<p>નીચેનું table syllabus ના છ પ્રકારની OS નો સાર આપે છે. Linux કે Windows જેવી આધુનિક OS તેમાંના ઘણાને જોડે છે: તે multiprogrammed, time-shared અને multithreaded છે, અને networking support કરે છે.</p>
""" + TYPES_GU),
    ]}

from content_DI03000041_u1_notes_b import SEC_1_3, SEC_1_4  # noqa: E402

NOTES = [SEC_1_1, SEC_1_2, SEC_1_3, SEC_1_4]
