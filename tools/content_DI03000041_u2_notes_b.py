"""Fundamentals of Operating System (DI03000041) - Unit 2 notes part B: 2.3 Schedulers, queues, context switch;
2.4 Process synchronization; 2.5 Deadlock."""
import html
from content_DI03000011_u1_notes_a import T
from content_DI03000041_u1_notes import tbl


def code(s):
    s = s.strip("\n")
    assert all(len(l) <= 43 for l in s.split("\n")), s
    return '<pre class="c">' + html.escape(s, quote=False) + "</pre>"


PETERSON = code("""
do {
    flag[i] = true;
    turn = j;
    while (flag[j] && turn == j)
        ;   /* busy wait */

    /* critical section */

    flag[i] = false;

    /* remainder section */
} while (true);
""")
SEMA = code("""
wait(S) {          /* P operation */
    while (S <= 0)
        ;          /* busy wait */
    S--;
}
signal(S) {        /* V operation */
    S++;
}

/* use: mutex = 1 */
wait(mutex);
    /* critical section */
signal(mutex);
""")

SCH_EN = tbl(["Point", "Long-term", "Short-term", "Medium-term"], [
    ("Also called", "Job scheduler", "CPU scheduler", "Swapper"),
    ("Selects from → to", "Job pool (disk) → ready queue", "Ready queue → CPU", "Memory ↔ disk (swap out / in)"),
    ("Speed / frequency", "Slowest; runs rarely (minutes)", "Fastest; runs very often (ms)", "In between"),
    ("Degree of multiprogramming", "Controls it", "Little control", "Reduces it"),
    ("Present in time-sharing OS?", "Minimal or absent", "Yes", "Yes"),
    ("Main aim", "Good mix of I/O-bound and CPU-bound jobs", "Choose next process to run", "Free memory; improve the process mix")])
SCH_GU = tbl(["મુદ્દો", "Long-term", "Short-term", "Medium-term"], [
    ("બીજું નામ", "Job scheduler", "CPU scheduler", "Swapper"),
    ("ક્યાંથી → ક્યાં", "Job pool (disk) → ready queue", "Ready queue → CPU", "Memory ↔ disk (swap out / in)"),
    ("ઝડપ / આવર્તન", "સૌથી ધીમો; ક્યારેક ચાલે (minutes)", "સૌથી ઝડપી; વારંવાર ચાલે (ms)", "વચ્ચે"),
    ("Degree of multiprogramming", "Control કરે", "ઓછું control", "ઘટાડે"),
    ("Time-sharing OS માં?", "ઓછો કે નહીં", "હા", "હા"),
    ("મુખ્ય હેતુ", "I/O-bound અને CPU-bound jobs નું સારું મિશ્રણ", "આગળ ચલાવવાની process પસંદ કરવી", "Memory મુક્ત કરવી; process mix સુધારવું")])

PREV_EN = tbl(["Condition", "How to prevent it", "Drawback"], [
    ("Mutual exclusion", "Make resources sharable (e.g. read-only files, spooling for printer)", "Not possible for printers, tapes etc."),
    ("Hold and wait", "Request all resources before starting, or request only when holding none", "Low resource use; starvation"),
    ("No preemption", "If a request cannot be granted, release (pre-empt) all held resources", "Only for resources whose state can be saved (CPU, memory)"),
    ("Circular wait", "Number all resource types; request them only in increasing order", "Ordering is inconvenient for programmers")])
PREV_GU = tbl(["શરત", "કેવી રીતે અટકાવવી", "ખામી"], [
    ("Mutual exclusion", "Resources ને sharable બનાવો (દા.ત. read-only files, printer માટે spooling)", "Printers, tapes વગેરે માટે શક્ય નથી"),
    ("Hold and wait", "શરૂઆત પહેલાં બધા resources માંગો, અથવા કંઈ ન પકડ્યું હોય ત્યારે જ માંગો", "Resources નો ઓછો ઉપયોગ; starvation"),
    ("No preemption", "Request મંજૂર ન થાય તો પકડેલા બધા resources છોડી દો (pre-empt)", "માત્ર જેમની state save થઈ શકે તેવા resources (CPU, memory)"),
    ("Circular wait", "બધા resource types ને નંબર આપો; માત્ર વધતા ક્રમમાં માંગો", "Programmers માટે ક્રમ અગવડભર્યો")])

SEC_2_3 = {
    "title": {"en": "2.3 Overview of Schedulers", "gu": "2.3 Schedulers નો પરિચય"},
    "items": [
        T("2.3.1 Types of Schedulers", "2.3.1 Schedulers ના પ્રકારો",
          """<p>A <b>scheduler</b> is the part of the OS that selects processes from a queue for the next step. A process migrates among various queues during its life; three schedulers handle this.</p>
<h4>1. Long-term scheduler (job scheduler)</h4>
<ul>
<li>Selects processes from the <b>job pool</b> (programs waiting on disk) and loads them into memory, i.e. into the <b>ready queue</b> (new → ready).</li>
<li>Controls the <b>degree of multiprogramming</b> (number of processes in memory).</li>
<li>Runs less frequently (minutes); can take more time to decide.</li>
<li>Should select a good <b>mix of I/O-bound processes</b> (spend more time in I/O) and <b>CPU-bound processes</b> (spend more time computing), so that both the CPU and devices stay busy.</li>
<li>Time-sharing systems (Unix, Windows) have almost no long-term scheduler; every new process is put in memory.</li>
</ul>
<h4>2. Short-term scheduler (CPU scheduler)</h4>
<ul>
<li>Selects one process from the <b>ready queue</b> and allocates the <b>CPU</b> to it (ready → running), with the help of the dispatcher.</li>
<li>Runs very frequently (at least once every 100 ms), so it must be very <b>fast</b>.</li>
<li>Uses algorithms such as FCFS, SJF, RR and priority.</li>
</ul>
<h4>3. Medium-term scheduler (swapper)</h4>
<ul>
<li>Removes (<b>swaps out</b>) a partially executed process from memory to disk, and later brings it back (<b>swaps in</b>) to continue from where it stopped.</li>
<li>Used when memory is over-committed, or to improve the mix of processes.</li>
<li><b>Reduces</b> the degree of multiprogramming; part of time-sharing systems.</li>
</ul>""",
          """<p><b>Scheduler</b> એ OS નો ભાગ છે જે આગળના પગલા માટે queue માંથી processes પસંદ કરે છે. Process તેના જીવન દરમિયાન જુદી જુદી queues વચ્ચે ફરે છે; ત્રણ schedulers આ સંભાળે છે.</p>
<h4>1. Long-term scheduler (job scheduler)</h4>
<ul>
<li><b>Job pool</b> (disk પર રાહ જોતા programs) માંથી processes પસંદ કરી memory માં, એટલે કે <b>ready queue</b> માં load કરે (new → ready).</li>
<li><b>Degree of multiprogramming</b> (memory માં processes ની સંખ્યા) ને control કરે.</li>
<li>ઓછી વાર ચાલે (minutes); નિર્ણય માટે વધુ સમય લઈ શકે.</li>
<li><b>I/O-bound processes</b> (I/O માં વધુ સમય) અને <b>CPU-bound processes</b> (ગણતરીમાં વધુ સમય) નું સારું <b>મિશ્રણ</b> પસંદ કરવું જોઈએ, જેથી CPU અને devices બંને વ્યસ્ત રહે.</li>
<li>Time-sharing systems (Unix, Windows) માં long-term scheduler લગભગ નથી; દરેક નવી process memory માં મુકાય છે.</li>
</ul>
<h4>2. Short-term scheduler (CPU scheduler)</h4>
<ul>
<li><b>Ready queue</b> માંથી એક process પસંદ કરી dispatcher ની મદદથી તેને <b>CPU</b> આપે (ready → running).</li>
<li>ખૂબ વારંવાર ચાલે (ઓછામાં ઓછું દર 100 ms એ એક વાર), તેથી ખૂબ <b>ઝડપી</b> હોવો જોઈએ.</li>
<li>FCFS, SJF, RR અને priority જેવા algorithms વાપરે.</li>
</ul>
<h4>3. Medium-term scheduler (swapper)</h4>
<ul>
<li>અંશતઃ ચાલેલી process ને memory માંથી disk પર કાઢે (<b>swap out</b>), અને પછી જ્યાં અટકી હતી ત્યાંથી આગળ ચલાવવા પાછી લાવે (<b>swap in</b>).</li>
<li>Memory ઓછી પડે ત્યારે, અથવા processes નું મિશ્રણ સુધારવા વપરાય.</li>
<li>Degree of multiprogramming <b>ઘટાડે</b>; time-sharing systems નો ભાગ.</li>
</ul>""",
          diagram="os2_schedulers"),
        T("2.3.2 Comparison of Schedulers", "2.3.2 Schedulers ની સરખામણી",
          "<p>A favourite 3/4-mark question:</p>" + SCH_EN,
          "<p>ઘણો પૂછાતો 3/4 ગુણનો પ્રશ્ન:</p>" + SCH_GU),
        T("2.3.3 Scheduling Queues", "2.3.3 Scheduling Queues",
          """<p>The OS keeps processes in different <b>queues</b> (linked lists of PCBs) according to their state:</p>
<ul>
<li><b>Job queue:</b> all processes in the system.</li>
<li><b>Ready queue:</b> processes in main memory that are ready and waiting to execute. Its header points to the first and last PCB.</li>
<li><b>Device (I/O) queues:</b> processes waiting for a particular I/O device; each device has its own queue.</li>
</ul>
<h4>Queueing diagram</h4>
<p>A new process is first put in the ready queue. It waits there until it is selected (dispatched) for execution. While it is running, one of these events may occur:</p>
<ol>
<li>It issues an <b>I/O request</b> and is placed in an I/O queue.</li>
<li>Its <b>time slice expires</b> and it is put back in the ready queue.</li>
<li>It <b>creates a child process</b> (fork) and waits for the child to finish.</li>
<li>It <b>waits for an interrupt</b> and is removed from the CPU until the interrupt occurs.</li>
</ol>
<p>In each case the process eventually returns to the ready queue. It continues this cycle until it terminates; then it is removed from all queues and its PCB and resources are released.</p>
<p>In the diagram, rectangles are queues, the circle is the resource that serves the queue (CPU), and arrows show the flow of processes.</p>""",
          """<p>OS processes ને તેમની state પ્રમાણે જુદી જુદી <b>queues</b> (PCBs ની linked lists) માં રાખે છે:</p>
<ul>
<li><b>Job queue:</b> system ની બધી processes.</li>
<li><b>Ready queue:</b> main memory માં રહેલી, ready અને ચાલવાની રાહ જોતી processes. તેનું header પહેલા અને છેલ્લા PCB તરફ point કરે.</li>
<li><b>Device (I/O) queues:</b> કોઈ ચોક્કસ I/O device ની રાહ જોતી processes; દરેક device ની પોતાની queue.</li>
</ul>
<h4>Queueing diagram</h4>
<p>નવી process પહેલા ready queue માં મુકાય છે. Execution માટે પસંદ (dispatch) થાય ત્યાં સુધી ત્યાં રાહ જુએ છે. ચાલતી વખતે આમાંથી એક event થઈ શકે:</p>
<ol>
<li>તે <b>I/O request</b> આપે અને I/O queue માં મુકાય.</li>
<li>તેનો <b>time slice પૂરો થાય</b> અને ફરી ready queue માં મુકાય.</li>
<li>તે <b>child process બનાવે</b> (fork) અને child પૂરી થાય તેની રાહ જુએ.</li>
<li>તે <b>interrupt ની રાહ જુએ</b> અને interrupt થાય ત્યાં સુધી CPU પરથી દૂર થાય.</li>
</ol>
<p>દરેક કિસ્સામાં process અંતે ready queue માં પાછી આવે છે. Terminate થાય ત્યાં સુધી આ ચક્ર ચાલે; પછી તેને બધી queues માંથી દૂર કરાય અને તેનું PCB તથા resources મુક્ત થાય.</p>
<p>આકૃતિમાં લંબચોરસ queues છે, વર્તુળ queue ને સેવા આપતો resource (CPU) છે, અને તીર processes નો પ્રવાહ દર્શાવે છે.</p>""",
          diagram="os2_queues"),
        T("2.3.4 Context Switch", "2.3.4 Context Switch",
          """<p>The <b>context</b> of a process is its current state, stored in its PCB: CPU register values, program counter, process state and memory-management information.</p>
<p>A <b>context switch</b> is the task of switching the CPU from one process to another: the kernel <b>saves the context of the old process</b> in its PCB and <b>loads the saved context of the new process</b> scheduled to run.</p>
<h4>When does it occur?</h4>
<ul><li>Interrupt (e.g. timer interrupt when the time quantum ends).</li><li>System call / I/O request by the running process.</li><li>A higher-priority process becomes ready (pre-emption).</li></ul>
<h4>Steps</h4>
<ol>
<li>P0 is running; an interrupt or system call occurs.</li>
<li>The OS saves the state of P0 into PCB0.</li>
<li>The scheduler selects P1; the OS reloads the state of P1 from PCB1.</li>
<li>P1 runs while P0 stays idle (ready or waiting).</li>
<li>Later, on another interrupt, the state of P1 is saved into PCB1 and P0 is reloaded from PCB0.</li>
</ol>
<p><b>Context-switch time is pure overhead</b>: the system does no useful work while switching. It typically takes a few microseconds and depends on memory speed, the number of registers and hardware support (some CPUs have multiple register sets). Too many context switches (e.g. a very small RR quantum) reduce performance.</p>""",
          """<p>Process નો <b>context</b> એટલે તેની હાલની state, જે તેના PCB માં store હોય છે: CPU register values, program counter, process state અને memory-management information.</p>
<p><b>Context switch</b> એટલે CPU ને એક process થી બીજી process પર switch કરવાનું કામ: kernel <b>જૂની process નો context</b> તેના PCB માં save કરે છે અને ચલાવવા માટે schedule થયેલી <b>નવી process નો saved context load</b> કરે છે.</p>
<h4>ક્યારે થાય?</h4>
<ul><li>Interrupt (દા.ત. time quantum પૂરો થાય ત્યારે timer interrupt).</li><li>ચાલતી process નો system call / I/O request.</li><li>ઊંચી priority વાળી process ready થાય (pre-emption).</li></ul>
<h4>પગલાં</h4>
<ol>
<li>P0 ચાલે છે; interrupt કે system call થાય.</li>
<li>OS P0 ની state PCB0 માં save કરે.</li>
<li>Scheduler P1 પસંદ કરે; OS PCB1 માંથી P1 ની state reload કરે.</li>
<li>P1 ચાલે અને P0 idle (ready કે waiting) રહે.</li>
<li>પછી બીજા interrupt પર P1 ની state PCB1 માં save થાય અને P0 PCB0 માંથી reload થાય.</li>
</ol>
<p><b>Context-switch time સંપૂર્ણ overhead છે</b>: switching વખતે system કોઈ ઉપયોગી કામ કરતી નથી. તે સામાન્ય રીતે થોડા microseconds લે છે અને memory ની ઝડપ, registers ની સંખ્યા અને hardware support (કેટલાક CPUs માં ઘણા register sets) પર આધાર રાખે છે. વધુ પડતા context switches (દા.ત. ખૂબ નાનો RR quantum) performance ઘટાડે છે.</p>""",
          diagram="os2_context"),
    ]}

SEC_2_4 = {
    "title": {"en": "2.4 Process Synchronization", "gu": "2.4 Process Synchronization"},
    "items": [
        T("2.4.1 Race Condition", "2.4.1 Race Condition",
          """<p><b>Cooperating processes</b> share data (shared memory, files). When several processes <b>access and modify the same shared data concurrently</b>, and the <b>final result depends on the order</b> in which their instructions execute, the situation is called a <b>race condition</b>.</p>
<h4>Example</h4>
<p>A shared variable <code>counter = 5</code>. Process P1 (producer) executes <code>counter++</code> and P2 (consumer) executes <code>counter--</code>. In machine language each statement is three instructions:</p>
<ul>
<li><code>counter++</code>: reg1 = counter; reg1 = reg1 + 1; counter = reg1</li>
<li><code>counter--</code>: reg2 = counter; reg2 = reg2 − 1; counter = reg2</li>
</ul>
<p>If these instructions interleave as shown in the diagram, the final value is 4 (or 6 with another order), but the correct value is <b>5</b>. The error happens because both processes manipulate <code>counter</code> at the same time.</p>
<p><b>Solution:</b> ensure that only <b>one process at a time</b> can manipulate the shared variable: this needs <b>process synchronization</b> (critical-section solutions, locks, semaphores).</p>""",
          """<p><b>Cooperating processes</b> data વહેંચે છે (shared memory, files). જ્યારે ઘણી processes <b>એક જ shared data ને એક સાથે access અને modify કરે</b>, અને <b>અંતિમ પરિણામ તેમના instructions ના execution ક્રમ પર આધાર રાખે</b>, ત્યારે તે પરિસ્થિતિને <b>race condition</b> કહે છે.</p>
<h4>ઉદાહરણ</h4>
<p>Shared variable <code>counter = 5</code>. Process P1 (producer) <code>counter++</code> ચલાવે છે અને P2 (consumer) <code>counter--</code>. Machine language માં દરેક statement ત્રણ instructions છે:</p>
<ul>
<li><code>counter++</code>: reg1 = counter; reg1 = reg1 + 1; counter = reg1</li>
<li><code>counter--</code>: reg2 = counter; reg2 = reg2 − 1; counter = reg2</li>
</ul>
<p>આ instructions આકૃતિ પ્રમાણે ભળી જાય તો અંતિમ કિંમત 4 (અથવા બીજા ક્રમમાં 6) આવે, પણ સાચી કિંમત <b>5</b> છે. ભૂલ એટલે થાય છે કે બંને processes એક જ સમયે <code>counter</code> બદલે છે.</p>
<p><b>ઉકેલ:</b> એક સમયે <b>માત્ર એક process</b> shared variable બદલી શકે તેની ખાતરી કરવી: તેના માટે <b>process synchronization</b> (critical-section solutions, locks, semaphores) જોઈએ.</p>""",
          diagram="os2_race"),
        T("2.4.2 Critical Section", "2.4.2 Critical Section",
          """<p>A <b>critical section (CS)</b> is the segment of code in which a process accesses <b>shared resources</b> (common variables, tables, files). The <b>critical-section problem</b> is to design a protocol so that <b>no two processes execute in their critical sections at the same time</b>.</p>
<h4>Structure of a process</h4>
<ul>
<li><b>Entry section:</b> code that requests permission to enter the CS.</li>
<li><b>Critical section:</b> code that accesses shared data.</li>
<li><b>Exit section:</b> code that announces leaving the CS.</li>
<li><b>Remainder section:</b> the rest of the code.</li>
</ul>
<h4>Requirements of a solution</h4>
<ol>
<li><b>Mutual exclusion:</b> if a process is executing in its CS, no other process can execute in its CS.</li>
<li><b>Progress:</b> if no process is in the CS and some processes want to enter, only those not in their remainder sections take part in deciding who enters next, and this decision cannot be postponed forever.</li>
<li><b>Bounded waiting:</b> there is a limit on the number of times other processes may enter their CS after a process has requested entry and before that request is granted (no starvation).</li>
</ol>
<p>Also: no assumption may be made about the speed or number of CPUs.</p>""",
          """<p><b>Critical section (CS)</b> એ code નો એવો ભાગ છે જેમાં process <b>shared resources</b> (સામાન્ય variables, tables, files) access કરે છે. <b>Critical-section problem</b> એટલે એવો protocol બનાવવો કે <b>કોઈ બે processes એક સાથે તેમના critical sections માં ન ચાલે</b>.</p>
<h4>Process નું structure</h4>
<ul>
<li><b>Entry section:</b> CS માં પ્રવેશની પરવાનગી માંગતો code.</li>
<li><b>Critical section:</b> shared data access કરતો code.</li>
<li><b>Exit section:</b> CS છોડ્યાની જાહેરાત કરતો code.</li>
<li><b>Remainder section:</b> બાકીનો code.</li>
</ul>
<h4>Solution ની જરૂરિયાતો</h4>
<ol>
<li><b>Mutual exclusion:</b> કોઈ process તેના CS માં ચાલતી હોય તો બીજી કોઈ process તેના CS માં ચાલી ન શકે.</li>
<li><b>Progress:</b> કોઈ process CS માં ન હોય અને કેટલીક પ્રવેશવા માંગતી હોય, તો remainder section માં ન હોય તેવી processes જ આગળ કોણ પ્રવેશે તે નક્કી કરે, અને આ નિર્ણય અનિશ્ચિત સમય સુધી ટાળી ન શકાય.</li>
<li><b>Bounded waiting:</b> process એ પ્રવેશ માંગ્યા પછી અને મંજૂરી મળે તે પહેલાં બીજી processes કેટલી વાર તેમના CS માં પ્રવેશી શકે તેની મર્યાદા હોય (starvation નહીં).</li>
</ol>
<p>વળી: CPUs ની ઝડપ કે સંખ્યા વિશે કોઈ ધારણા ન કરી શકાય.</p>""",
          diagram="os2_cs"),
        T("2.4.3 Mutual Exclusion", "2.4.3 Mutual Exclusion",
          """<p><b>Mutual exclusion</b> means that if one process is using a shared resource (variable, file, printer) inside its critical section, all other processes are <b>excluded</b> from doing the same thing at that time. It is the first and most important requirement for avoiding race conditions.</p>
<h4>Methods for achieving mutual exclusion</h4>
<ol>
<li><b>Disabling interrupts:</b> a process disables interrupts on entering its CS, so no context switch can happen. Simple, but unsafe to give users this power and does not work on multiprocessors.</li>
<li><b>Lock variable:</b> a shared variable lock = 0 (free) / 1 (busy). A process waits while lock is 1, then sets it to 1. It fails because two processes may read 0 at the same time.</li>
<li><b>Strict alternation:</b> a variable <code>turn</code> decides whose turn it is. It gives mutual exclusion but violates progress.</li>
<li><b>Peterson's solution</b> (two processes): uses <code>flag[2]</code> (who wants to enter) and <code>turn</code> (whose turn). It satisfies all three requirements.</li>
<li><b>Hardware instructions:</b> atomic <b>TSL</b> (test-and-set lock) or <b>swap</b> instructions.</li>
<li><b>Semaphores</b> (Dijkstra): an integer variable S accessed only through the atomic operations <b>wait(S)</b> (P) and <b>signal(S)</b> (V). A <b>binary semaphore</b> (0/1) is a <b>mutex lock</b>; a <b>counting semaphore</b> controls a resource with many instances.</li>
</ol>
<h4>Peterson's solution (process i; the other is j)</h4>
""" + PETERSON + """
<h4>Semaphore operations</h4>
""" + SEMA + """
<p><b>Busy waiting</b> (spinning in a loop) wastes CPU time; practical semaphores block the waiting process in a queue and wake it up on signal().</p>""",
          """<p><b>Mutual exclusion</b> એટલે કે જો એક process તેના critical section માં shared resource (variable, file, printer) વાપરતી હોય, તો બીજી બધી processes ને તે સમયે તે જ કામ કરતા <b>અટકાવવામાં</b> આવે. Race conditions ટાળવાની તે પહેલી અને સૌથી મહત્ત્વની જરૂરિયાત છે.</p>
<h4>Mutual exclusion મેળવવાની પદ્ધતિઓ</h4>
<ol>
<li><b>Interrupts બંધ કરવા:</b> process CS માં પ્રવેશે ત્યારે interrupts બંધ કરે, તેથી context switch ન થઈ શકે. સરળ, પણ users ને આ સત્તા આપવી જોખમી અને multiprocessors પર કામ ન કરે.</li>
<li><b>Lock variable:</b> shared variable lock = 0 (મુક્ત) / 1 (વ્યસ્ત). Process lock 1 હોય ત્યાં સુધી રાહ જુએ, પછી તેને 1 કરે. નિષ્ફળ જાય છે કારણ કે બે processes એક સાથે 0 વાંચી શકે.</li>
<li><b>Strict alternation:</b> variable <code>turn</code> નક્કી કરે કે કોનો વારો છે. Mutual exclusion આપે પણ progress નો ભંગ કરે.</li>
<li><b>Peterson's solution</b> (બે processes): <code>flag[2]</code> (કોણ પ્રવેશવા માંગે છે) અને <code>turn</code> (કોનો વારો) વાપરે. ત્રણેય જરૂરિયાતો સંતોષે.</li>
<li><b>Hardware instructions:</b> atomic <b>TSL</b> (test-and-set lock) અથવા <b>swap</b> instructions.</li>
<li><b>Semaphores</b> (Dijkstra): integer variable S જે માત્ર atomic operations <b>wait(S)</b> (P) અને <b>signal(S)</b> (V) વડે access થાય. <b>Binary semaphore</b> (0/1) એ <b>mutex lock</b> છે; <b>counting semaphore</b> ઘણા instances વાળા resource ને control કરે.</li>
</ol>
<h4>Peterson's solution (process i; બીજી j)</h4>
""" + PETERSON + """
<h4>Semaphore operations</h4>
""" + SEMA + """
<p><b>Busy waiting</b> (loop માં ફરતા રહેવું) CPU time વેડફે છે; વ્યવહારુ semaphores રાહ જોતી process ને queue માં block કરે અને signal() પર જગાડે છે.</p>""",
          diagram="os2_mutex"),
    ]}

SEC_2_5 = {
    "title": {"en": "2.5 Deadlock", "gu": "2.5 Deadlock"},
    "items": [
        T("2.5.1 Definition of Deadlock", "2.5.1 Deadlock ની વ્યાખ્યા",
          """<p>A process uses a resource in the sequence: <b>request → use → release</b>. Resources can be physical (printer, scanner, memory, CPU) or logical (files, semaphores).</p>
<p><b>Deadlock:</b> a set of processes is in a deadlock state when <b>every process in the set is waiting for an event (release of a resource) that can be caused only by another process in the set</b>. Since all of them are waiting, none of them ever runs, releases its resources or is woken up: they wait forever.</p>
<h4>Example</h4>
<p>P1 holds the printer (R1) and requests the scanner (R2); P2 holds the scanner (R2) and requests the printer (R1). Neither can continue.</p>
<p><b>Real-life example:</b> four cars at a four-way crossing, each waiting for the car on its right to move; or two cars from opposite sides on a one-lane bridge.</p>
<p><b>Deadlock vs starvation:</b> in deadlock, processes wait forever for each other (circular); in starvation, a process waits indefinitely because others keep getting the resource, but the system keeps running.</p>""",
          """<p>Process resource ને આ ક્રમમાં વાપરે છે: <b>request → use → release</b>. Resources physical (printer, scanner, memory, CPU) અથવા logical (files, semaphores) હોઈ શકે.</p>
<p><b>Deadlock:</b> processes નો સમૂહ deadlock state માં હોય છે જ્યારે <b>સમૂહની દરેક process એવી event (resource ના release) ની રાહ જુએ છે જે માત્ર સમૂહની બીજી process જ કરી શકે</b>. બધી રાહ જોતી હોવાથી કોઈ ક્યારેય ચાલતી નથી, resources છોડતી નથી કે જાગતી નથી: તેઓ કાયમ રાહ જુએ છે.</p>
<h4>ઉદાહરણ</h4>
<p>P1 પાસે printer (R1) છે અને તે scanner (R2) માંગે છે; P2 પાસે scanner (R2) છે અને તે printer (R1) માંગે છે. બંનેમાંથી કોઈ આગળ ન વધી શકે.</p>
<p><b>રોજિંદું ઉદાહરણ:</b> ચાર રસ્તા પર ચાર cars, દરેક તેની જમણી બાજુની car ખસે તેની રાહ જુએ; અથવા એક-lane bridge પર સામસામેથી આવતી બે cars.</p>
<p><b>Deadlock vs starvation:</b> deadlock માં processes એકબીજાની કાયમ રાહ જુએ (circular); starvation માં બીજાને resource મળતો રહેતો હોવાથી process અનિશ્ચિત રાહ જુએ, પણ system ચાલતી રહે.</p>""",
          diagram="os2_deadlock"),
        T("2.5.2 Necessary Conditions for Deadlock", "2.5.2 Deadlock માટેની જરૂરી શરતો",
          """<p>A deadlock can arise only if <b>all four</b> of the following conditions hold <b>at the same time</b> (Coffman conditions):</p>
<ol>
<li><b>Mutual exclusion:</b> at least one resource must be held in a non-sharable mode: only one process can use it at a time (e.g. a printer).</li>
<li><b>Hold and wait:</b> a process is holding at least one resource and waiting to get additional resources held by other processes.</li>
<li><b>No preemption:</b> a resource cannot be taken away forcibly; it is released only voluntarily by the process holding it, after finishing its task.</li>
<li><b>Circular wait:</b> a set {P0, P1, …, Pn} of waiting processes exists such that P0 waits for a resource held by P1, P1 waits for P2, …, and Pn waits for P0.</li>
</ol>
<p>If any <b>one</b> of these conditions is prevented, deadlock cannot occur. This idea is the basis of <b>deadlock prevention</b>.</p>""",
          """<p>Deadlock ત્યારે જ થઈ શકે જ્યારે નીચેની <b>ચારેય</b> શરતો <b>એક સાથે</b> સાચી હોય (Coffman conditions):</p>
<ol>
<li><b>Mutual exclusion:</b> ઓછામાં ઓછો એક resource non-sharable mode માં હોવો જોઈએ: એક સમયે માત્ર એક process તેને વાપરી શકે (દા.ત. printer).</li>
<li><b>Hold and wait:</b> process ઓછામાં ઓછો એક resource પકડી રાખે છે અને બીજી processes પાસેના વધારાના resources મેળવવા રાહ જુએ છે.</li>
<li><b>No preemption:</b> resource બળજબરીથી લઈ શકાતો નથી; તેને પકડનાર process કામ પૂરું કર્યા પછી જાતે જ છોડે.</li>
<li><b>Circular wait:</b> રાહ જોતી processes નો સમૂહ {P0, P1, …, Pn} એવો હોય કે P0 એ P1 પાસેના resource ની રાહ જુએ, P1 એ P2 ની, …, અને Pn એ P0 ની.</li>
</ol>
<p>આમાંથી કોઈ <b>એક</b> શરત અટકાવી દેવાય તો deadlock થઈ શકે નહીં. આ વિચાર <b>deadlock prevention</b> નો આધાર છે.</p>"""),
        T("2.5.3 Resource Allocation Graph (RAG)", "2.5.3 Resource Allocation Graph (RAG)",
          """<p>Deadlocks can be described precisely by a directed graph called the <b>resource allocation graph</b>. It has a set of vertices V and edges E.</p>
<h4>Vertices</h4>
<ul>
<li><b>Process nodes</b> P = {P1, P2, …}: drawn as <b>circles</b>.</li>
<li><b>Resource nodes</b> R = {R1, R2, …}: drawn as <b>rectangles</b>; each <b>dot</b> inside is one instance of the resource.</li>
</ul>
<h4>Edges</h4>
<ul>
<li><b>Request edge</b> Pi → Rj: process Pi has requested an instance of Rj and is waiting.</li>
<li><b>Assignment edge</b> Rj → Pi: an instance of Rj has been allocated to Pi (drawn from a dot).</li>
</ul>
<p>When a request is granted, the request edge is changed into an assignment edge; when the process releases the resource, the edge is deleted.</p>
<h4>Detecting deadlock from a RAG</h4>
<ol>
<li>If the graph has <b>no cycle</b> → <b>no deadlock</b>.</li>
<li>If there is a cycle and <b>each resource has only one instance</b> → <b>deadlock</b> (cycle is necessary and sufficient).</li>
<li>If there is a cycle and resources have <b>several instances</b> → deadlock <b>may or may not</b> exist (cycle is necessary but not sufficient). In figure (b), P4 can finish and release R2, so P3 gets it and the cycle breaks.</li>
</ol>""",
          """<p>Deadlocks ને <b>resource allocation graph</b> નામના directed graph વડે ચોક્કસ રીતે દર્શાવી શકાય. તેમાં vertices V અને edges E હોય છે.</p>
<h4>Vertices</h4>
<ul>
<li><b>Process nodes</b> P = {P1, P2, …}: <b>વર્તુળ</b> તરીકે દોરાય.</li>
<li><b>Resource nodes</b> R = {R1, R2, …}: <b>લંબચોરસ</b> તરીકે; અંદરનું દરેક <b>ટપકું</b> resource નું એક instance છે.</li>
</ul>
<h4>Edges</h4>
<ul>
<li><b>Request edge</b> Pi → Rj: process Pi એ Rj નું instance માંગ્યું છે અને રાહ જુએ છે.</li>
<li><b>Assignment edge</b> Rj → Pi: Rj નું એક instance Pi ને ફાળવાયું છે (ટપકામાંથી દોરાય).</li>
</ul>
<p>Request મંજૂર થાય ત્યારે request edge assignment edge માં બદલાય; process resource છોડે ત્યારે edge દૂર થાય.</p>
<h4>RAG પરથી deadlock શોધવું</h4>
<ol>
<li>Graph માં <b>cycle નથી</b> → <b>deadlock નથી</b>.</li>
<li>Cycle છે અને <b>દરેક resource નું માત્ર એક instance</b> છે → <b>deadlock</b> (cycle જરૂરી અને પૂરતી).</li>
<li>Cycle છે અને resources ના <b>ઘણા instances</b> છે → deadlock <b>હોઈ શકે કે ન પણ હોય</b> (cycle જરૂરી પણ પૂરતી નહીં). આકૃતિ (b) માં P4 પૂરી થઈ R2 છોડી શકે, તેથી P3 ને તે મળે અને cycle તૂટે.</li>
</ol>""",
          diagram="os2_rag"),
        T("2.5.4 Dealing with Deadlock; Ignorance of Deadlock", "2.5.4 Deadlock સંભાળવું; Deadlock ની અવગણના",
          """<p>There are four ways of dealing with deadlock:</p>
<ol>
<li><b>Ignore the problem</b> (ostrich algorithm): pretend deadlocks never occur.</li>
<li><b>Detection and recovery:</b> let deadlocks occur, detect them, and take action to recover.</li>
<li><b>Dynamic avoidance:</b> carefully allocate resources so that the system never enters an unsafe state (Banker's algorithm).</li>
<li><b>Prevention:</b> structurally make one of the four necessary conditions impossible.</li>
</ol>
<h4>Ignorance of deadlock (ostrich algorithm)</h4>
<p>Like an ostrich that "sticks its head in the sand", the OS simply <b>ignores</b> the problem. This is used when:</p>
<ul>
<li>deadlocks occur very rarely (e.g. once in years), and</li>
<li>the cost of prevention, avoidance or detection (performance loss, restrictions) is higher than the cost of an occasional deadlock.</li>
</ul>
<p>If a deadlock does happen, the user or administrator <b>restarts</b> the stuck program or the system. <b>Most general-purpose OSs, including Unix, Linux and Windows, use this approach</b>, leaving it to application developers to write deadlock-free programs.</p>
<p>Disadvantage: when a deadlock happens, work may be lost and the system's performance degrades until a manual restart.</p>""",
          """<p>Deadlock સંભાળવાની ચાર રીતો છે:</p>
<ol>
<li><b>સમસ્યાની અવગણના</b> (ostrich algorithm): deadlocks થતા જ નથી એમ માનવું.</li>
<li><b>Detection and recovery:</b> deadlocks થવા દેવા, તેમને શોધવા, અને recover થવા પગલાં લેવા.</li>
<li><b>Dynamic avoidance:</b> resources એવી કાળજીથી ફાળવવા કે system ક્યારેય unsafe state માં ન જાય (Banker's algorithm).</li>
<li><b>Prevention:</b> ચાર જરૂરી શરતોમાંથી એકને structurally અશક્ય બનાવવી.</li>
</ol>
<h4>Deadlock ની અવગણના (ostrich algorithm)</h4>
<p>"રેતીમાં માથું છુપાવતા" શાહમૃગની જેમ OS સમસ્યાની <b>અવગણના</b> કરે છે. આ ત્યારે વપરાય જ્યારે:</p>
<ul>
<li>deadlocks ખૂબ ભાગ્યે જ થાય (દા.ત. વર્ષોમાં એક વાર), અને</li>
<li>prevention, avoidance કે detection નો ખર્ચ (performance ઘટાડો, પ્રતિબંધો) ક્યારેક થતા deadlock ના ખર્ચ કરતાં વધુ હોય.</li>
</ul>
<p>Deadlock થાય તો user કે administrator અટકેલા program કે system ને <b>restart</b> કરે. <b>Unix, Linux અને Windows સહિત મોટા ભાગની general-purpose OS આ રીત વાપરે છે</b>, અને deadlock-free programs લખવાનું application developers પર છોડે છે.</p>
<p>ગેરફાયદો: deadlock થાય ત્યારે કામ ગુમાવાઈ શકે અને manual restart સુધી system નું performance ઘટે.</p>"""),
        T("2.5.5 Deadlock Prevention", "2.5.5 Deadlock Prevention",
          """<p><b>Deadlock prevention</b> ensures that <b>at least one of the four necessary conditions can never hold</b>. It restricts how processes can request resources.</p>
""" + PREV_EN + """
<h4>Circular-wait example</h4>
<p>Give numbers: tape drive = 1, disk drive = 5, printer = 12. A process holding the disk drive (5) may request the printer (12) but not the tape drive (1). Because every process requests resources in increasing order, a cycle can never form.</p>
<p><b>Disadvantages of prevention:</b> low device utilisation and reduced system throughput.</p>""",
          """<p><b>Deadlock prevention</b> એ ખાતરી કરે છે કે <b>ચાર જરૂરી શરતોમાંથી ઓછામાં ઓછી એક ક્યારેય સાચી ન બને</b>. તે processes resources કેવી રીતે માંગી શકે તેના પર પ્રતિબંધ મૂકે છે.</p>
""" + PREV_GU + """
<h4>Circular-wait ઉદાહરણ</h4>
<p>નંબર આપો: tape drive = 1, disk drive = 5, printer = 12. Disk drive (5) પકડતી process printer (12) માંગી શકે પણ tape drive (1) નહીં. દરેક process વધતા ક્રમમાં resources માંગે છે, તેથી cycle ક્યારેય બની શકતી નથી.</p>
<p><b>Prevention ના ગેરફાયદા:</b> devices નો ઓછો ઉપયોગ અને system throughput ઘટે.</p>"""),
        T("2.5.6 Deadlock Avoidance: Safe State and Banker's Algorithm", "2.5.6 Deadlock Avoidance: Safe State અને Banker's Algorithm",
          """<p><b>Dynamic avoidance</b> requires each process to declare in advance the <b>maximum number</b> of resources of each type it may need. Before granting a request, the OS checks whether the resulting state is <b>safe</b>; if not, the process must wait even if the resources are free.</p>
<h4>Safe state</h4>
<p>A state is <b>safe</b> if there exists a <b>safe sequence</b> &lt;P1, P2, …, Pn&gt; in which each process can get its remaining needs from the currently available resources plus the resources held by all earlier processes, and then finish. A safe state has no deadlock. An <b>unsafe</b> state <b>may</b> lead to deadlock; avoidance never enters it.</p>
<h4>Banker's algorithm (Dijkstra)</h4>
<p>Named because a bank never lends money in such a way that it cannot satisfy all its customers. Data structures for n processes and m resource types:</p>
<ul>
<li><b>Available[m]:</b> free instances of each resource.</li>
<li><b>Max[n][m]:</b> maximum demand of each process.</li>
<li><b>Allocation[n][m]:</b> instances currently allocated.</li>
<li><b>Need[n][m] = Max − Allocation:</b> remaining need.</li>
</ul>
<h4>Safety algorithm</h4>
<ol>
<li>Work = Available; Finish[i] = false for all i.</li>
<li>Find i with Finish[i] = false and Need<sub>i</sub> ≤ Work. If none, go to step 4.</li>
<li>Work = Work + Allocation<sub>i</sub>; Finish[i] = true; go to step 2.</li>
<li>If Finish[i] is true for all i, the state is safe.</li>
</ol>
<h4>Resource-request algorithm</h4>
<ol>
<li>If Request<sub>i</sub> &gt; Need<sub>i</sub> → error (exceeds maximum claim).</li>
<li>If Request<sub>i</sub> &gt; Available → Pi must wait.</li>
<li>Pretend to allocate: Available −= Request; Allocation<sub>i</sub> += Request; Need<sub>i</sub> −= Request. Run the safety algorithm: safe → grant; unsafe → restore the old state and Pi waits.</li>
</ol>
<p><b>Limitations:</b> maximum needs must be known in advance; the number of processes and resources must be fixed; processes may wait even when resources are free.</p>""",
          """<p><b>Dynamic avoidance</b> માં દરેક process એ અગાઉથી દરેક પ્રકારના resource ની <b>મહત્તમ સંખ્યા</b> જાહેર કરવી પડે. Request મંજૂર કરતા પહેલાં OS તપાસે છે કે પરિણામી state <b>safe</b> છે કે નહીં; ન હોય તો resources મુક્ત હોય તો પણ process એ રાહ જોવી પડે.</p>
<h4>Safe state</h4>
<p>State <b>safe</b> છે જો એવો <b>safe sequence</b> &lt;P1, P2, …, Pn&gt; હોય જેમાં દરેક process હાલના available resources અને અગાઉની બધી processes ના resources વડે તેની બાકીની જરૂરિયાત મેળવી પૂરી થઈ શકે. Safe state માં deadlock નથી. <b>Unsafe</b> state deadlock તરફ લઈ જઈ <b>શકે</b>; avoidance તેમાં ક્યારેય જતું નથી.</p>
<h4>Banker's algorithm (Dijkstra)</h4>
<p>નામ એટલે કે bank ક્યારેય એવી રીતે પૈસા ઉછીના નથી આપતી કે તે બધા ગ્રાહકોને સંતોષી ન શકે. n processes અને m resource types માટે data structures:</p>
<ul>
<li><b>Available[m]:</b> દરેક resource ના મુક્ત instances.</li>
<li><b>Max[n][m]:</b> દરેક process ની મહત્તમ માંગ.</li>
<li><b>Allocation[n][m]:</b> હાલ ફાળવેલા instances.</li>
<li><b>Need[n][m] = Max − Allocation:</b> બાકી જરૂરિયાત.</li>
</ul>
<h4>Safety algorithm</h4>
<ol>
<li>Work = Available; બધા i માટે Finish[i] = false.</li>
<li>Finish[i] = false અને Need<sub>i</sub> ≤ Work હોય તેવો i શોધો. ન મળે તો પગલું 4.</li>
<li>Work = Work + Allocation<sub>i</sub>; Finish[i] = true; પગલું 2 પર જાઓ.</li>
<li>બધા i માટે Finish[i] true હોય તો state safe છે.</li>
</ol>
<h4>Resource-request algorithm</h4>
<ol>
<li>Request<sub>i</sub> &gt; Need<sub>i</sub> હોય → error (maximum claim થી વધુ).</li>
<li>Request<sub>i</sub> &gt; Available હોય → Pi એ રાહ જોવી પડે.</li>
<li>Allocate કર્યું હોય તેમ માનો: Available −= Request; Allocation<sub>i</sub> += Request; Need<sub>i</sub> −= Request. Safety algorithm ચલાવો: safe → મંજૂર; unsafe → જૂની state પાછી લાવો અને Pi રાહ જુએ.</li>
</ol>
<p><b>મર્યાદાઓ:</b> મહત્તમ જરૂરિયાત અગાઉથી જાણવી પડે; processes અને resources ની સંખ્યા નિશ્ચિત હોવી જોઈએ; resources મુક્ત હોય તો પણ processes ને રાહ જોવી પડી શકે.</p>""",
          diagram="os2_safe", examples=["os2n12", "os2n13"]),
        T("2.5.7 Deadlock Detection and Recovery", "2.5.7 Deadlock Detection and Recovery",
          """<p>Here the system <b>allows deadlocks to occur</b>, periodically runs a <b>detection algorithm</b>, and then <b>recovers</b>.</p>
<h4>Detection</h4>
<ul>
<li><b>Single instance of each resource:</b> build a <b>wait-for graph</b> from the RAG by removing resource nodes and joining the edges: Pi → Pj means Pi waits for a resource held by Pj. A <b>cycle</b> in the wait-for graph means deadlock.</li>
<li><b>Several instances:</b> use a Banker-like algorithm with Available, Allocation and <b>Request</b> matrices. Work = Available; a process whose Request ≤ Work is assumed to finish and release its allocation. Processes that can never finish are <b>deadlocked</b>.</li>
<li><b>When to run it?</b> On every request that cannot be granted (costly), at fixed intervals (e.g. once per hour), or when CPU utilisation drops below e.g. 40%.</li>
</ul>
<h4>Recovery</h4>
<ol>
<li><b>Process termination:</b>
<ul><li>abort <b>all</b> deadlocked processes (sure but costly: all partial work is lost), or</li>
<li>abort <b>one process at a time</b> until the cycle disappears (choose the victim by priority, time used, resources held, etc.).</li></ul></li>
<li><b>Resource preemption:</b> take resources away from some processes and give them to others:
<ul><li><b>Selecting a victim:</b> minimum cost.</li><li><b>Rollback:</b> return the victim to a safe earlier state (checkpoint) and restart it from there.</li><li><b>Starvation:</b> make sure the same process is not always the victim (include the number of rollbacks in the cost).</li></ul></li>
</ol>""",
          """<p>અહીં system <b>deadlocks થવા દે છે</b>, સમયાંતરે <b>detection algorithm</b> ચલાવે છે, અને પછી <b>recover</b> થાય છે.</p>
<h4>Detection</h4>
<ul>
<li><b>દરેક resource નું એક instance:</b> RAG માંથી resource nodes દૂર કરી edges જોડી <b>wait-for graph</b> બનાવો: Pi → Pj એટલે Pi એ Pj પાસેના resource ની રાહ જુએ છે. Wait-for graph માં <b>cycle</b> એટલે deadlock.</li>
<li><b>ઘણા instances:</b> Available, Allocation અને <b>Request</b> matrices સાથે Banker જેવો algorithm વાપરો. Work = Available; Request ≤ Work હોય તેવી process પૂરી થઈ તેનું allocation છોડે એમ માનો. ક્યારેય પૂરી ન થઈ શકે તેવી processes <b>deadlocked</b> છે.</li>
<li><b>ક્યારે ચલાવવો?</b> મંજૂર ન થઈ શકે તેવી દરેક request પર (મોંઘું), નિયમિત અંતરે (દા.ત. કલાકમાં એક વાર), અથવા CPU utilisation દા.ત. 40% થી નીચે જાય ત્યારે.</li>
</ul>
<h4>Recovery</h4>
<ol>
<li><b>Process termination:</b>
<ul><li><b>બધી</b> deadlocked processes abort કરવી (ચોક્કસ પણ મોંઘું: બધું અધૂરું કામ ગુમાવાય), અથવા</li>
<li>cycle દૂર થાય ત્યાં સુધી <b>એક સમયે એક process</b> abort કરવી (priority, વપરાયેલો સમય, પકડેલા resources વગેરે પરથી victim પસંદ કરો).</li></ul></li>
<li><b>Resource preemption:</b> કેટલીક processes પાસેથી resources લઈ બીજાને આપવા:
<ul><li><b>Victim પસંદગી:</b> ઓછામાં ઓછો ખર્ચ.</li><li><b>Rollback:</b> victim ને અગાઉની safe state (checkpoint) પર પાછી લાવી ત્યાંથી restart કરવી.</li><li><b>Starvation:</b> એ જ process હંમેશા victim ન બને તેની કાળજી (ખર્ચમાં rollbacks ની સંખ્યા ગણો).</li></ul></li>
</ol>""",
          diagram="os2_waitfor", examples=["os2n14"]),
    ]}
