"""Fundamentals of Operating System (DI03000041) - Unit 2 notes part A: 2.1 Concepts of process; 2.2 Process scheduling."""
from content_DI03000011_u1_notes_a import T
from content_DI03000041_u1_notes import tbl
from content_DI03000041_u2_extras import RESULTS

PT_EN = tbl(["Point", "Process", "Thread"], [
    ("Meaning", "Program in execution", "Smallest unit of execution inside a process"),
    ("Weight", "Heavy-weight", "Light-weight"),
    ("Memory", "Own separate address space", "Shares code, data, files of its process"),
    ("Creation / switching", "Slow, costly", "Fast, cheap"),
    ("Communication", "Needs IPC (OS help)", "Directly through shared memory"),
    ("Failure", "One process crash does not affect others", "One thread crash can stop the whole process"),
    ("Example", "Two different programs: Word and Chrome", "Typing and spell-check threads in Word")])
PT_GU = tbl(["મુદ્દો", "Process", "Thread"], [
    ("અર્થ", "Execution માં રહેલો program", "Process ની અંદર execution નો સૌથી નાનો એકમ"),
    ("વજન", "Heavy-weight", "Light-weight"),
    ("Memory", "પોતાની અલગ address space", "Process ના code, data, files વહેંચે"),
    ("બનાવવું / switching", "ધીમું, મોંઘું", "ઝડપી, સસ્તું"),
    ("Communication", "IPC (OS ની મદદ) જોઈએ", "Shared memory દ્વારા સીધું"),
    ("Failure", "એક process crash બીજાને અસર ન કરે", "એક thread crash આખી process અટકાવી શકે"),
    ("ઉદાહરણ", "બે અલગ programs: Word અને Chrome", "Word માં typing અને spell-check threads")])

PNP_EN = tbl(["Point", "Preemptive", "Non-preemptive"], [
    ("CPU taken away?", "Yes, on interrupt / higher priority / time-out", "No, process keeps CPU till it ends or blocks"),
    ("Response time", "Good", "Poor for short jobs"),
    ("Overhead", "More context switches", "Less"),
    ("Starvation", "Possible", "Possible (long job blocks others)"),
    ("Examples", "RR, SRTF, preemptive priority", "FCFS, SJF, non-preemptive priority")])
PNP_GU = tbl(["મુદ્દો", "Preemptive", "Non-preemptive"], [
    ("CPU લઈ લેવાય?", "હા, interrupt / ઊંચી priority / time-out પર", "ના, process પૂરી કે block થાય ત્યાં સુધી CPU રાખે"),
    ("Response time", "સારો", "નાના jobs માટે ખરાબ"),
    ("Overhead", "વધુ context switches", "ઓછો"),
    ("Starvation", "શક્ય", "શક્ય (લાંબો job બીજાને રોકે)"),
    ("ઉદાહરણ", "RR, SRTF, preemptive priority", "FCFS, SJF, non-preemptive priority")])

A, B = RESULTS, RESULTS
CMP_EN = tbl(["Algorithm", "Type", "Selection", "Advantage", "Disadvantage"], [
    ("FCFS", "Non-preemptive", "Earliest arrival", "Simple, fair order", "Convoy effect, high WT"),
    ("SJF", "Non-preemptive (SRTF = preemptive)", "Smallest burst", "Minimum average WT (optimal)", "Burst must be known; starvation"),
    ("Round Robin", "Preemptive", "Turn by turn, quantum q", "Good response, no starvation", "Context-switch overhead; depends on q"),
    ("Priority", "Non-preemptive (or preemptive)", "Highest priority", "Important jobs first", "Starvation (solved by aging)")])
CMP_GU = tbl(["Algorithm", "પ્રકાર", "પસંદગી", "ફાયદો", "ગેરફાયદો"], [
    ("FCFS", "Non-preemptive", "સૌથી પહેલું arrival", "સરળ, ન્યાયી ક્રમ", "Convoy effect, વધુ WT"),
    ("SJF", "Non-preemptive (SRTF = preemptive)", "સૌથી નાનો burst", "ઓછામાં ઓછો સરેરાશ WT (optimal)", "Burst જાણવો પડે; starvation"),
    ("Round Robin", "Preemptive", "વારાફરતી, quantum q", "સારો response, starvation નહીં", "Context-switch overhead; q પર આધાર"),
    ("Priority", "Non-preemptive (અથવા preemptive)", "સૌથી ઊંચી priority", "મહત્ત્વના jobs પહેલા", "Starvation (aging થી ઉકેલ)")])
RES_TBL = tbl(["Practical", "FCFS (TAT / WT)", "SJF (TAT / WT)", "RR q=2 (TAT / WT)"], [
    ("2(a)", " / ".join(A["a_fcfs"]), " / ".join(A["a_sjf"]), " / ".join(A["a_rr"])),
    ("2(b)", " / ".join(B["b_fcfs"]), " / ".join(B["b_sjf"]), " / ".join(B["b_rr"]))])

SEC_2_1 = {
    "title": {"en": "2.1 Concepts of Process", "gu": "2.1 Process ના Concepts"},
    "items": [
        T("2.1.1 Process: Overview", "2.1.1 Process: પરિચય",
          """<p>A <b>process</b> is a <b>program in execution</b>. A program is a <b>passive</b> entity (an executable file stored on disk); it becomes a process, an <b>active</b> entity, when it is loaded into memory and starts running. One program can create several processes (e.g. opening two windows of the same browser).</p>
<h4>A process in memory has</h4>
<ul>
<li><b>Text section:</b> the program code.</li>
<li><b>Data section:</b> global and static variables.</li>
<li><b>Heap:</b> memory allocated dynamically at run time (malloc / new).</li>
<li><b>Stack:</b> temporary data such as function parameters, return addresses and local variables.</li>
<li>Plus the current activity: the <b>program counter</b> (PC) and the contents of CPU <b>registers</b>.</li>
</ul>
<p>The stack grows downwards and the heap grows upwards into the free space between them.</p>
<h4>Program vs process</h4>
<ul>
<li>Program: passive, stored on disk, exists until deleted, needs no resources.</li>
<li>Process: active, in main memory, exists only while running, needs CPU, memory, files and I/O.</li>
</ul>
<p><b>Operations on processes:</b> creation (e.g. <code>fork()</code> in Unix creates a child process), scheduling, blocking, waking up and termination (<code>exit()</code>).</p>""",
          """<p><b>Process</b> એટલે <b>execution માં રહેલો program</b>. Program <b>passive</b> entity છે (disk પર store થયેલી executable file); તે memory માં load થઈ ચાલવા લાગે ત્યારે process એટલે કે <b>active</b> entity બને છે. એક program ઘણી processes બનાવી શકે (દા.ત. એક જ browser ની બે windows ખોલવી).</p>
<h4>Memory માં process પાસે હોય છે</h4>
<ul>
<li><b>Text section:</b> program code.</li>
<li><b>Data section:</b> global અને static variables.</li>
<li><b>Heap:</b> run time પર dynamically ફાળવાતી memory (malloc / new).</li>
<li><b>Stack:</b> function parameters, return addresses અને local variables જેવો કામચલાઉ data.</li>
<li>સાથે હાલની પ્રવૃત્તિ: <b>program counter</b> (PC) અને CPU <b>registers</b> ની કિંમતો.</li>
</ul>
<p>Stack નીચે તરફ અને heap ઉપર તરફ, તેમની વચ્ચેની free space માં વધે છે.</p>
<h4>Program vs process</h4>
<ul>
<li>Program: passive, disk પર store, delete ન થાય ત્યાં સુધી રહે, resources ની જરૂર નહીં.</li>
<li>Process: active, main memory માં, ચાલે ત્યાં સુધી જ રહે, CPU, memory, files અને I/O જોઈએ.</li>
</ul>
<p><b>Processes પરના operations:</b> creation (દા.ત. Unix માં <code>fork()</code> child process બનાવે), scheduling, blocking, wake up અને termination (<code>exit()</code>).</p>""",
          diagram="os2_memory"),
        T("2.1.2 Threads and Process vs Thread", "2.1.2 Threads અને Process vs Thread",
          """<p>A <b>thread</b> is a basic unit of CPU utilisation inside a process. It has its own <b>thread ID, program counter, register set and stack</b>, and shares the <b>code section, data section and OS resources</b> (open files, signals) with the other threads of the same process. A traditional process has a single thread; modern processes have many.</p>
<p><b>Example:</b> in a browser, one thread shows the page, another downloads images, another plays a video.</p>
<p><b>Benefits:</b> responsiveness, resource sharing, economy (cheaper than processes) and scalability on multi-core CPUs.</p>
<p><b>Types:</b> user-level threads (managed by a library, fast, kernel unaware) and kernel-level threads (managed by the OS).</p>
<h4>Process vs thread</h4>
""" + PT_EN,
          """<p><b>Thread</b> એ process ની અંદર CPU utilisation નો મૂળભૂત એકમ છે. તેને પોતાના <b>thread ID, program counter, register set અને stack</b> હોય છે, અને તે એ જ process ના બીજા threads સાથે <b>code section, data section અને OS resources</b> (open files, signals) વહેંચે છે. પરંપરાગત process માં એક thread હોય; આધુનિક processes માં ઘણા.</p>
<p><b>ઉદાહરણ:</b> browser માં એક thread page બતાવે, બીજો images download કરે, ત્રીજો video ચલાવે.</p>
<p><b>ફાયદા:</b> responsiveness, resource sharing, economy (processes કરતાં સસ્તા) અને multi-core CPUs પર scalability.</p>
<p><b>પ્રકારો:</b> user-level threads (library વડે સંચાલિત, ઝડપી, kernel અજાણ) અને kernel-level threads (OS વડે સંચાલિત).</p>
<h4>Process vs thread</h4>
""" + PT_GU),
        T("2.1.3 Process Life Cycle / Process States", "2.1.3 Process Life Cycle / Process States",
          """<p>As a process executes, it changes its <b>state</b>. The state is the current activity of the process. Only <b>one process can be running</b> on one CPU at a time; many may be ready or waiting.</p>
<h4>Five states</h4>
<ol>
<li><b>New:</b> the process is being created (PCB is built, memory allocated).</li>
<li><b>Ready:</b> loaded in memory and waiting to be assigned the CPU.</li>
<li><b>Running:</b> its instructions are being executed by the CPU.</li>
<li><b>Waiting (Blocked):</b> waiting for some event, e.g. I/O completion or a signal.</li>
<li><b>Terminated (Exit):</b> finished execution; its resources are released.</li>
</ol>
<h4>State transitions</h4>
<ul>
<li><b>New → Ready (admitted):</b> the long-term scheduler admits the process.</li>
<li><b>Ready → Running (scheduler dispatch):</b> the short-term scheduler selects it.</li>
<li><b>Running → Ready (interrupt):</b> time quantum over or a higher-priority process arrives (pre-emption).</li>
<li><b>Running → Waiting (I/O or event wait):</b> the process requests I/O or waits for an event.</li>
<li><b>Waiting → Ready (I/O or event completion):</b> the event occurs; the process again waits for the CPU (it never goes directly to running).</li>
<li><b>Running → Terminated (exit):</b> the process finishes or is killed.</li>
</ul>
<p>Some systems add <b>suspended ready</b> and <b>suspended blocked</b> states for processes swapped out to disk (7-state model).</p>""",
          """<p>Process ચાલે તેમ તેની <b>state</b> બદલાય છે. State એ process ની હાલની પ્રવૃત્તિ છે. એક CPU પર એક સમયે <b>માત્ર એક process running</b> હોઈ શકે; ઘણી ready કે waiting હોઈ શકે.</p>
<h4>પાંચ states</h4>
<ol>
<li><b>New:</b> process બની રહી છે (PCB બને, memory ફાળવાય).</li>
<li><b>Ready:</b> memory માં load થઈ છે અને CPU મળવાની રાહ જુએ છે.</li>
<li><b>Running:</b> CPU તેના instructions ચલાવે છે.</li>
<li><b>Waiting (Blocked):</b> કોઈ event ની રાહ જુએ છે, દા.ત. I/O completion કે signal.</li>
<li><b>Terminated (Exit):</b> execution પૂરું; તેના resources મુક્ત થાય.</li>
</ol>
<h4>State transitions</h4>
<ul>
<li><b>New → Ready (admitted):</b> long-term scheduler process ને પ્રવેશ આપે.</li>
<li><b>Ready → Running (scheduler dispatch):</b> short-term scheduler તેને પસંદ કરે.</li>
<li><b>Running → Ready (interrupt):</b> time quantum પૂરો થાય કે ઊંચી priority વાળી process આવે (pre-emption).</li>
<li><b>Running → Waiting (I/O or event wait):</b> process I/O માંગે કે event ની રાહ જુએ.</li>
<li><b>Waiting → Ready (I/O or event completion):</b> event થાય; process ફરી CPU ની રાહ જુએ (સીધી running માં ક્યારેય ન જાય).</li>
<li><b>Running → Terminated (exit):</b> process પૂરી થાય કે kill થાય.</li>
</ul>
<p>કેટલીક systems disk પર swap out થયેલી processes માટે <b>suspended ready</b> અને <b>suspended blocked</b> states ઉમેરે છે (7-state model).</p>""",
          diagram="os2_states"),
        T("2.1.4 Process Control Block (PCB)", "2.1.4 Process Control Block (PCB)",
          """<p>Each process is represented in the OS by a <b>Process Control Block (PCB)</b>, also called a <b>task control block</b>. It is a data structure in the kernel that stores all the information needed to manage the process. The PCB is created when the process is created and deleted when it terminates.</p>
<h4>Fields of a PCB</h4>
<ol>
<li><b>Pointer:</b> links the PCB into a scheduling queue (ready queue, device queue).</li>
<li><b>Process state:</b> new, ready, running, waiting or terminated.</li>
<li><b>Process ID (PID):</b> unique identification number (also parent PID).</li>
<li><b>Program counter:</b> address of the next instruction to execute.</li>
<li><b>CPU registers:</b> accumulator, index registers, stack pointer, general-purpose registers; saved on an interrupt so that the process can continue correctly later.</li>
<li><b>CPU-scheduling information:</b> priority, pointers to scheduling queues, other scheduling parameters.</li>
<li><b>Memory-management information:</b> base and limit registers, page tables or segment tables.</li>
<li><b>Accounting information:</b> CPU time used, real time used, time limits, job number.</li>
<li><b>I/O status information:</b> list of I/O devices allocated, list of open files.</li>
</ol>
<p><b>Role in context switch:</b> when the CPU switches from one process to another, the state of the old process is saved in its PCB and the state of the new process is loaded from its PCB.</p>""",
          """<p>OS માં દરેક process ને <b>Process Control Block (PCB)</b> વડે દર્શાવાય છે, જેને <b>task control block</b> પણ કહે છે. તે kernel માં રહેલું data structure છે જે process ના સંચાલન માટે જરૂરી બધી માહિતી રાખે છે. Process બને ત્યારે PCB બને અને process પૂરી થાય ત્યારે delete થાય.</p>
<h4>PCB ના fields</h4>
<ol>
<li><b>Pointer:</b> PCB ને scheduling queue (ready queue, device queue) માં જોડે છે.</li>
<li><b>Process state:</b> new, ready, running, waiting અથવા terminated.</li>
<li><b>Process ID (PID):</b> અનન્ય ઓળખ નંબર (parent PID પણ).</li>
<li><b>Program counter:</b> ચલાવવાના આગળના instruction નું address.</li>
<li><b>CPU registers:</b> accumulator, index registers, stack pointer, general-purpose registers; interrupt વખતે save થાય જેથી process પછી બરાબર આગળ ચાલી શકે.</li>
<li><b>CPU-scheduling information:</b> priority, scheduling queues ના pointers, બીજા scheduling parameters.</li>
<li><b>Memory-management information:</b> base અને limit registers, page tables અથવા segment tables.</li>
<li><b>Accounting information:</b> વપરાયેલો CPU time, real time, time limits, job number.</li>
<li><b>I/O status information:</b> ફાળવેલા I/O devices ની યાદી, open files ની યાદી.</li>
</ol>
<p><b>Context switch માં ભૂમિકા:</b> CPU એક process થી બીજી પર જાય ત્યારે જૂની process ની state તેના PCB માં save થાય અને નવી process ની state તેના PCB માંથી load થાય.</p>""",
          diagram="os2_pcb"),
    ]}

SEC_2_2 = {
    "title": {"en": "2.2 Process Scheduling", "gu": "2.2 Process Scheduling"},
    "items": [
        T("2.2.1 CPU Scheduling: Basic Concepts", "2.2.1 CPU Scheduling: મૂળભૂત Concepts",
          """<p><b>CPU scheduling</b> is the method of selecting a process from the <b>ready queue</b> and allocating the CPU to it. It is the basis of multiprogramming: by switching the CPU among processes, the OS keeps the CPU busy.</p>
<ul>
<li><b>CPU–I/O burst cycle:</b> a process alternates between <b>CPU bursts</b> (computing) and <b>I/O bursts</b> (waiting for I/O). The <b>burst time (BT)</b> is the CPU time a process needs.</li>
<li><b>CPU scheduler (short-term scheduler):</b> selects the next process from the ready queue.</li>
<li><b>Dispatcher:</b> gives control of the CPU to the selected process: switches context, switches to user mode and jumps to the proper location. The time it takes is the <b>dispatch latency</b>.</li>
</ul>
<h4>When does scheduling happen?</h4>
<ol>
<li>A process switches from running to waiting (I/O request).</li>
<li>A process switches from running to ready (interrupt / time-out).</li>
<li>A process switches from waiting to ready (I/O completion).</li>
<li>A process terminates.</li>
</ol>
<p>If scheduling happens only in cases 1 and 4, it is <b>non-preemptive</b>; otherwise it is <b>preemptive</b>.</p>
<h4>Preemptive vs non-preemptive scheduling</h4>
""" + PNP_EN,
          """<p><b>CPU scheduling</b> એટલે <b>ready queue</b> માંથી process પસંદ કરી તેને CPU આપવાની પદ્ધતિ. તે multiprogramming નો આધાર છે: processes વચ્ચે CPU switch કરી OS CPU ને વ્યસ્ત રાખે છે.</p>
<ul>
<li><b>CPU–I/O burst cycle:</b> process <b>CPU bursts</b> (ગણતરી) અને <b>I/O bursts</b> (I/O ની રાહ) વચ્ચે ફરતી રહે છે. <b>Burst time (BT)</b> એ process ને જોઈતો CPU time છે.</li>
<li><b>CPU scheduler (short-term scheduler):</b> ready queue માંથી આગળની process પસંદ કરે.</li>
<li><b>Dispatcher:</b> પસંદ કરેલી process ને CPU નું control આપે: context switch કરે, user mode માં જાય અને યોગ્ય સ્થાને jump કરે. તેમાં લાગતો સમય <b>dispatch latency</b> છે.</li>
</ul>
<h4>Scheduling ક્યારે થાય?</h4>
<ol>
<li>Process running માંથી waiting માં જાય (I/O request).</li>
<li>Process running માંથી ready માં જાય (interrupt / time-out).</li>
<li>Process waiting માંથી ready માં જાય (I/O completion).</li>
<li>Process terminate થાય.</li>
</ol>
<p>Scheduling માત્ર 1 અને 4 માં થાય તો તે <b>non-preemptive</b>; નહીં તો <b>preemptive</b>.</p>
<h4>Preemptive vs non-preemptive scheduling</h4>
""" + PNP_GU),
        T("2.2.2 Scheduling Criteria", "2.2.2 Scheduling Criteria",
          """<p>Scheduling algorithms are compared using the following <b>criteria</b>:</p>
<ol>
<li><b>CPU utilisation:</b> keep the CPU as busy as possible (40% light load to 90% heavy load). <i>Maximise.</i></li>
<li><b>Throughput:</b> number of processes completed per unit time. <i>Maximise.</i></li>
<li><b>Turnaround time (TAT):</b> total time from submission (arrival) to completion: TAT = CT − AT. It includes waiting in the ready queue, executing and doing I/O. <i>Minimise.</i></li>
<li><b>Waiting time (WT):</b> total time a process spends waiting in the ready queue: WT = TAT − BT. The scheduling algorithm directly affects only this. <i>Minimise.</i></li>
<li><b>Response time (RT):</b> time from arrival until the process gets the CPU for the first time (first response). Important for interactive systems. <i>Minimise.</i></li>
</ol>
<p>Other goals: <b>fairness</b> (every process gets a fair share, no starvation) and <b>predictability</b>.</p>
<h4>Terms used in numericals</h4>
<ul>
<li><b>AT (arrival time):</b> time when the process enters the ready queue.</li>
<li><b>BT (burst time):</b> CPU time required.</li>
<li><b>CT (completion time):</b> time when the process finishes.</li>
<li><b>Gantt chart:</b> a bar chart showing which process runs in which time interval.</li>
</ul>""",
          """<p>Scheduling algorithms ની સરખામણી નીચેના <b>criteria</b> થી થાય છે:</p>
<ol>
<li><b>CPU utilisation:</b> CPU ને શક્ય તેટલું વ્યસ્ત રાખવું (ઓછા load માં 40% થી ભારે load માં 90%). <i>વધારવું.</i></li>
<li><b>Throughput:</b> એકમ સમયમાં પૂરી થતી processes ની સંખ્યા. <i>વધારવું.</i></li>
<li><b>Turnaround time (TAT):</b> submission (arrival) થી completion સુધીનો કુલ સમય: TAT = CT − AT. તેમાં ready queue માં રાહ, execution અને I/O સમાવિષ્ટ છે. <i>ઘટાડવું.</i></li>
<li><b>Waiting time (WT):</b> process એ ready queue માં રાહ જોવામાં ગાળેલો કુલ સમય: WT = TAT − BT. Scheduling algorithm સીધી રીતે માત્ર આને અસર કરે છે. <i>ઘટાડવું.</i></li>
<li><b>Response time (RT):</b> arrival થી process ને પહેલી વાર CPU મળે ત્યાં સુધીનો સમય (પહેલો response). Interactive systems માટે મહત્ત્વનો. <i>ઘટાડવું.</i></li>
</ol>
<p>બીજા ધ્યેય: <b>fairness</b> (દરેક process ને યોગ્ય ભાગ, starvation નહીં) અને <b>predictability</b>.</p>
<h4>Numericals માં વપરાતા શબ્દો</h4>
<ul>
<li><b>AT (arrival time):</b> process ready queue માં આવે તે સમય.</li>
<li><b>BT (burst time):</b> જરૂરી CPU time.</li>
<li><b>CT (completion time):</b> process પૂરી થાય તે સમય.</li>
<li><b>Gantt chart:</b> કયા સમય ગાળામાં કઈ process ચાલે છે તે દર્શાવતો bar chart.</li>
</ul>""",
          diagram="os2_times"),
        T("2.2.3 First Come First Serve (FCFS)", "2.2.3 First Come First Serve (FCFS)",
          """<p><b>FCFS</b> is the simplest scheduling algorithm. The process that <b>requests the CPU first gets it first</b>. It is implemented with a <b>FIFO queue</b>: a new process's PCB is linked at the tail of the ready queue, and the CPU is given to the process at the head.</p>
<p>FCFS is <b>non-preemptive</b>: once a process gets the CPU, it keeps it until it terminates or requests I/O.</p>
<h4>Steps to solve</h4>
<ol>
<li>Sort the processes by arrival time.</li>
<li>Run each process completely, one after another (if the CPU is free and no process has arrived, the CPU stays idle).</li>
<li>Draw the Gantt chart; find CT, then TAT = CT − AT and WT = TAT − BT.</li>
</ol>
<h4>Advantages</h4>
<ul><li>Simple to understand and implement.</li><li>Fair in the order of arrival; no starvation.</li></ul>
<h4>Disadvantages</h4>
<ul><li>Average waiting time is often long.</li><li><b>Convoy effect:</b> short processes wait behind one long process, so CPU and I/O devices are poorly used.</li><li>Not suitable for time-sharing systems.</li></ul>""",
          """<p><b>FCFS</b> સૌથી સરળ scheduling algorithm છે. <b>જે process પહેલા CPU માંગે તેને પહેલા મળે</b>. તે <b>FIFO queue</b> થી અમલ થાય છે: નવી process નું PCB ready queue ના છેડે જોડાય, અને CPU queue ની શરૂઆતની process ને મળે.</p>
<p>FCFS <b>non-preemptive</b> છે: process ને CPU મળે પછી તે પૂરી થાય કે I/O માંગે ત્યાં સુધી રાખે છે.</p>
<h4>ઉકેલવાના પગલાં</h4>
<ol>
<li>Processes ને arrival time પ્રમાણે ગોઠવો.</li>
<li>દરેક process ને એક પછી એક સંપૂર્ણ ચલાવો (CPU મુક્ત હોય અને કોઈ process ન આવી હોય તો CPU idle રહે).</li>
<li>Gantt chart દોરો; CT શોધો, પછી TAT = CT − AT અને WT = TAT − BT.</li>
</ol>
<h4>ફાયદા</h4>
<ul><li>સમજવા અને અમલ કરવા સરળ.</li><li>Arrival ના ક્રમમાં ન્યાયી; starvation નહીં.</li></ul>
<h4>ગેરફાયદા</h4>
<ul><li>સરેરાશ waiting time ઘણી વાર લાંબો.</li><li><b>Convoy effect:</b> નાની processes એક લાંબી process પાછળ રાહ જુએ, તેથી CPU અને I/O devices નો ખરાબ ઉપયોગ.</li><li>Time-sharing systems માટે યોગ્ય નથી.</li></ul>""",
          diagram="os2_fcfs", examples=["os2n1", "os2n4", "os2n9"]),
        T("2.2.4 Shortest Job First (SJF)", "2.2.4 Shortest Job First (SJF)",
          """<p>In <b>SJF</b>, when the CPU is free it is given to the waiting process with the <b>smallest next CPU burst</b>. If two processes have the same burst, FCFS breaks the tie.</p>
<h4>Two versions</h4>
<ul>
<li><b>Non-preemptive SJF:</b> once a process starts, it runs to completion even if a shorter process arrives.</li>
<li><b>Preemptive SJF = Shortest Remaining Time First (SRTF):</b> if a newly arrived process has a burst shorter than the <b>remaining</b> time of the running process, the running process is pre-empted.</li>
</ul>
<h4>Steps to solve (non-preemptive)</h4>
<ol>
<li>At time t, look at all processes that have <b>arrived</b> (AT ≤ t) and are not finished.</li>
<li>Pick the one with the smallest BT; run it completely; set t = its CT.</li>
<li>Repeat. If none has arrived, the CPU is idle until the next arrival.</li>
</ol>
<h4>Advantages</h4>
<ul><li>Gives the <b>minimum average waiting time</b> for a given set of processes (provably optimal).</li><li>High throughput.</li></ul>
<h4>Disadvantages</h4>
<ul><li>The length of the next CPU burst cannot be known exactly; it must be estimated (e.g. exponential average of previous bursts).</li><li><b>Starvation</b> of long processes if short ones keep arriving.</li></ul>""",
          """<p><b>SJF</b> માં CPU મુક્ત થાય ત્યારે તે <b>સૌથી નાના next CPU burst</b> વાળી રાહ જોતી process ને મળે છે. બે processes નો burst સરખો હોય તો FCFS થી નક્કી થાય.</p>
<h4>બે પ્રકાર</h4>
<ul>
<li><b>Non-preemptive SJF:</b> process શરૂ થયા પછી નાની process આવે તો પણ પૂરી થાય ત્યાં સુધી ચાલે.</li>
<li><b>Preemptive SJF = Shortest Remaining Time First (SRTF):</b> નવી આવેલી process નો burst ચાલતી process ના <b>બાકી</b> સમય કરતાં નાનો હોય તો ચાલતી process pre-empt થાય.</li>
</ul>
<h4>ઉકેલવાના પગલાં (non-preemptive)</h4>
<ol>
<li>સમય t પર, <b>આવી ગયેલી</b> (AT ≤ t) અને પૂરી ન થયેલી બધી processes જુઓ.</li>
<li>સૌથી નાના BT વાળી પસંદ કરો; સંપૂર્ણ ચલાવો; t = તેનો CT.</li>
<li>પુનરાવર્તન કરો. કોઈ ન આવી હોય તો આગળના arrival સુધી CPU idle.</li>
</ol>
<h4>ફાયદા</h4>
<ul><li>આપેલી processes માટે <b>ઓછામાં ઓછો સરેરાશ waiting time</b> આપે (optimal સાબિત).</li><li>વધુ throughput.</li></ul>
<h4>ગેરફાયદા</h4>
<ul><li>આગળના CPU burst ની લંબાઈ ચોક્કસ જાણી શકાતી નથી; અંદાજ કાઢવો પડે (દા.ત. પાછલા bursts નો exponential average).</li><li>નાની processes આવતી રહે તો લાંબી processes ની <b>starvation</b>.</li></ul>""",
          diagram="os2_sjf", examples=["os2n2", "os2n5", "os2n10"]),
        T("2.2.5 Round Robin (RR)", "2.2.5 Round Robin (RR)",
          """<p><b>Round Robin</b> is designed for <b>time-sharing</b> systems. It is like FCFS, but with <b>pre-emption</b>. A small unit of time, the <b>time quantum (time slice) q</b>, usually 10–100 ms, is defined. The ready queue is a <b>circular FIFO queue</b>.</p>
<h4>Working</h4>
<ol>
<li>The scheduler picks the first process from the ready queue and sets a timer for one quantum.</li>
<li>If the process's remaining burst ≤ q, it finishes and releases the CPU voluntarily.</li>
<li>Otherwise the timer interrupts after q; the process is pre-empted (context switch) and put at the <b>tail</b> of the ready queue.</li>
<li>The next process in the queue gets the CPU, and so on.</li>
</ol>
<p>With n processes and quantum q, no process waits more than (n − 1) × q time units for its next turn.</p>
<h4>Choice of time quantum</h4>
<ul>
<li><b>Very large q</b> → RR behaves like FCFS.</li>
<li><b>Very small q</b> → too many context switches; most CPU time is wasted in switching.</li>
<li>Rule of thumb: about 80% of CPU bursts should be shorter than q.</li>
</ul>
<h4>Advantages</h4>
<ul><li>Fair; every process gets the CPU regularly; <b>no starvation</b>.</li><li>Good response time for interactive users.</li></ul>
<h4>Disadvantages</h4>
<ul><li>Context-switch overhead; average waiting time is often high.</li><li>Performance depends heavily on q.</li></ul>""",
          """<p><b>Round Robin</b> <b>time-sharing</b> systems માટે બનાવાયો છે. તે FCFS જેવો છે, પણ <b>pre-emption</b> સાથે. સમયનો નાનો એકમ, <b>time quantum (time slice) q</b>, સામાન્ય રીતે 10–100 ms, નક્કી થાય છે. Ready queue એક <b>circular FIFO queue</b> છે.</p>
<h4>કાર્યપદ્ધતિ</h4>
<ol>
<li>Scheduler ready queue માંથી પહેલી process પસંદ કરે અને એક quantum નો timer મૂકે.</li>
<li>Process નો બાકી burst ≤ q હોય તો તે પૂરી થઈ જાતે CPU છોડે.</li>
<li>નહીં તો q પછી timer interrupt આપે; process pre-empt થાય (context switch) અને ready queue ના <b>છેડે</b> મુકાય.</li>
<li>Queue ની આગળની process ને CPU મળે, વગેરે.</li>
</ol>
<p>n processes અને quantum q હોય તો કોઈ process તેના આગળના વારા માટે (n − 1) × q થી વધુ રાહ જોતી નથી.</p>
<h4>Time quantum ની પસંદગી</h4>
<ul>
<li><b>ખૂબ મોટો q</b> → RR એ FCFS જેવો બને.</li>
<li><b>ખૂબ નાનો q</b> → ઘણા context switches; મોટા ભાગનો CPU time switching માં વેડફાય.</li>
<li>સામાન્ય નિયમ: આશરે 80% CPU bursts q કરતાં નાના હોવા જોઈએ.</li>
</ul>
<h4>ફાયદા</h4>
<ul><li>ન્યાયી; દરેક process ને નિયમિત CPU મળે; <b>starvation નહીં</b>.</li><li>Interactive users માટે સારો response time.</li></ul>
<h4>ગેરફાયદા</h4>
<ul><li>Context-switch overhead; સરેરાશ waiting time ઘણી વાર વધુ.</li><li>Performance q પર ખૂબ આધાર રાખે.</li></ul>""",
          diagram="os2_rr", examples=["os2n3", "os2n6", "os2n11"]),
        T("2.2.6 Non-Preemptive Priority Scheduling", "2.2.6 Non-Preemptive Priority Scheduling",
          """<p>In <b>priority scheduling</b>, a <b>priority number</b> is associated with each process, and the CPU is given to the process with the <b>highest priority</b>. In this syllabus (and most books), a <b>smaller number means higher priority</b> (0 or 1 = highest). Equal priorities are scheduled in FCFS order.</p>
<p>In the <b>non-preemptive</b> version, if a higher-priority process arrives while another is running, it is simply placed at the head of the ready queue; the running process is <b>not</b> interrupted. (In the preemptive version, the running process would be pre-empted.)</p>
<p>Priorities can be <b>internal</b> (memory needs, time limits, number of open files) or <b>external</b> (importance of the user, payment, department).</p>
<p>SJF is a special case of priority scheduling where priority = predicted burst time.</p>
<h4>Problem: starvation (indefinite blocking)</h4>
<p>A low-priority process may wait forever if higher-priority processes keep arriving.</p>
<p><b>Solution: aging</b>: gradually increase the priority of processes that wait for a long time (e.g. raise priority by 1 every 15 minutes), so that eventually they get the CPU.</p>
<h4>Advantages / disadvantages</h4>
<ul><li><b>+</b> Important (system or real-time) processes run first.</li><li><b>−</b> Starvation; choosing priorities is difficult.</li></ul>""",
          """<p><b>Priority scheduling</b> માં દરેક process સાથે <b>priority number</b> જોડાય છે, અને CPU <b>સૌથી ઊંચી priority</b> વાળી process ને મળે છે. આ syllabus (અને મોટા ભાગના પુસ્તકો) માં <b>નાની સંખ્યા એટલે ઊંચી priority</b> (0 કે 1 = સૌથી ઊંચી). સરખી priorities FCFS ક્રમે schedule થાય.</p>
<p><b>Non-preemptive</b> version માં, બીજી process ચાલતી હોય ત્યારે ઊંચી priority વાળી process આવે તો તે માત્ર ready queue ની શરૂઆતમાં મુકાય; ચાલતી process ને <b>અટકાવાતી નથી</b>. (Preemptive version માં ચાલતી process pre-empt થાય.)</p>
<p>Priorities <b>internal</b> (memory જરૂરિયાત, time limits, open files ની સંખ્યા) અથવા <b>external</b> (user નું મહત્ત્વ, ચુકવણી, department) હોઈ શકે.</p>
<p>SJF એ priority scheduling નો ખાસ કિસ્સો છે જ્યાં priority = અંદાજિત burst time.</p>
<h4>સમસ્યા: starvation (indefinite blocking)</h4>
<p>ઊંચી priority વાળી processes આવતી રહે તો low-priority process કાયમ રાહ જોઈ શકે.</p>
<p><b>ઉકેલ: aging</b>: લાંબો સમય રાહ જોતી processes ની priority ધીમે ધીમે વધારવી (દા.ત. દર 15 મિનિટે priority 1 વધારવી), જેથી અંતે તેમને CPU મળે.</p>
<h4>ફાયદા / ગેરફાયદા</h4>
<ul><li><b>+</b> મહત્ત્વની (system કે real-time) processes પહેલા ચાલે.</li><li><b>−</b> Starvation; priorities નક્કી કરવી મુશ્કેલ.</li></ul>""",
          diagram="os2_priority", examples=["os2n7", "os2n8"]),
        T("2.2.7 Comparison of Scheduling Algorithms", "2.2.7 Scheduling Algorithms ની સરખામણી",
          CMP_EN + "<h4>Results of Practical 2 (average TAT / WT)</h4>" + RES_TBL
          + "<p>SJF gives the lowest averages; RR has the highest averages but the best response time.</p>",
          CMP_GU + "<h4>Practical 2 ના પરિણામ (સરેરાશ TAT / WT)</h4>" + RES_TBL
          + "<p>SJF સૌથી ઓછી સરેરાશ આપે છે; RR ની સરેરાશ સૌથી વધુ છે પણ response time સૌથી સારો છે.</p>"),
    ]}

from content_DI03000041_u2_notes_b import SEC_2_3, SEC_2_4, SEC_2_5  # noqa: E402

NOTES = [SEC_2_1, SEC_2_2, SEC_2_3, SEC_2_4, SEC_2_5]
