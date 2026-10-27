"""Fundamentals of Operating System (DI03000041) - Unit 5 notes part A: 5.1 Linux introduction and architecture;
5.2 Shell and commands (real terminal output from os_u5_demos)."""
from content_DI03000011_u1_notes_a import T
from content_DI03000041_u1_notes import tbl
import os_u5_demos as D


def TP(*a, programs=None, **k):
    t = T(*a, **k)
    if programs:
        t["programs"] = programs
    return t


UW_EN = tbl(["Point", "Unix", "Linux"], [
    ("Origin", "AT&amp;T Bell Labs, 1969 (Ken Thompson, Dennis Ritchie)", "Linus Torvalds, 1991"),
    ("Licence", "Mostly proprietary (AIX, HP-UX, Solaris, macOS)", "Free and open source (GPL)"),
    ("Hardware", "Specific vendor hardware", "Runs on almost all hardware"),
    ("Examples", "AIX, HP-UX, Solaris, BSD", "Ubuntu, Fedora, Debian, Mint"),
    ("Cost", "Usually paid", "Mostly free")])
UW_GU = tbl(["મુદ્દો", "Unix", "Linux"], [
    ("ઉદ્ભવ", "AT&amp;T Bell Labs, 1969 (Ken Thompson, Dennis Ritchie)", "Linus Torvalds, 1991"),
    ("Licence", "મોટે ભાગે proprietary (AIX, HP-UX, Solaris, macOS)", "Free અને open source (GPL)"),
    ("Hardware", "ચોક્કસ vendor નું hardware", "લગભગ બધા hardware પર ચાલે"),
    ("ઉદાહરણો", "AIX, HP-UX, Solaris, BSD", "Ubuntu, Fedora, Debian, Mint"),
    ("કિંમત", "સામાન્ય રીતે paid", "મોટે ભાગે free")])

SHELLS_EN = tbl(["Shell", "Program", "Notes"], [
    ("Bourne shell", "sh", "Original Unix shell (Stephen Bourne); prompt $"),
    ("Bourne Again shell", "bash", "Default on most Linux systems; history, completion"),
    ("C shell", "csh / tcsh", "C-like syntax; prompt %"),
    ("Korn shell", "ksh", "Combines sh and csh features"),
    ("Z shell", "zsh", "Default on macOS; powerful completion")])
SHELLS_GU = tbl(["Shell", "Program", "નોંધ"], [
    ("Bourne shell", "sh", "મૂળ Unix shell (Stephen Bourne); prompt $"),
    ("Bourne Again shell", "bash", "મોટા ભાગની Linux systems માં default; history, completion"),
    ("C shell", "csh / tcsh", "C જેવી syntax; prompt %"),
    ("Korn shell", "ksh", "sh અને csh ના features ભેગા"),
    ("Z shell", "zsh", "macOS માં default; શક્તિશાળી completion")])

SEC_5_1 = {
    "title": {"en": "5.1 Linux Introduction and Architecture", "gu": "5.1 Linux પરિચય અને Architecture"},
    "items": [
        T("5.1.1 Introduction to Unix and Linux", "5.1.1 Unix અને Linux નો પરિચય",
          """<p><b>Unix</b> is a multi-user, multitasking operating system developed in 1969 at AT&amp;T Bell Labs by Ken Thompson and Dennis Ritchie. It was rewritten in the C language in 1973, which made it portable to many machines.</p>
<p><b>Linux</b> is a free and open-source, Unix-like operating system. Its <b>kernel</b> was created in 1991 by <b>Linus Torvalds</b>, a student in Finland. The Linux kernel combined with GNU tools (bash, gcc, coreutils) forms a complete OS, often called <b>GNU/Linux</b>. A <b>distribution (distro)</b> packages the kernel, tools, desktop and installer: Ubuntu, Fedora, Debian, Linux Mint, Red Hat, Kali.</p>
<h4>Features of Linux</h4>
<ul>
<li><b>Free and open source:</b> source code is available under the GPL; anyone can study, modify and distribute it.</li>
<li><b>Multi-user:</b> many users can use the system at the same time, each with their own account.</li>
<li><b>Multitasking:</b> many programs run concurrently.</li>
<li><b>Portable:</b> runs on PCs, servers, phones (Android), routers and supercomputers.</li>
<li><b>Security:</b> user accounts, file permissions (rwx), root/superuser separation.</li>
<li><b>Hierarchical file system:</b> everything starts from the root <code>/</code>; devices are also files.</li>
<li><b>Shell and utilities:</b> powerful command line with hundreds of small commands that can be combined using pipes.</li>
<li><b>Networking</b> support built in; stable and reliable; little need for antivirus.</li>
</ul>
<h4>Unix vs Linux</h4>
""" + UW_EN,
          """<p><b>Unix</b> એ multi-user, multitasking operating system છે જે 1969 માં AT&amp;T Bell Labs માં Ken Thompson અને Dennis Ritchie એ વિકસાવી હતી. 1973 માં તેને C language માં ફરી લખાઈ, જેથી તે ઘણા machines પર portable બની.</p>
<p><b>Linux</b> એ free અને open-source, Unix જેવી operating system છે. તેનું <b>kernel</b> 1991 માં Finland ના વિદ્યાર્થી <b>Linus Torvalds</b> એ બનાવ્યું. Linux kernel GNU tools (bash, gcc, coreutils) સાથે મળી સંપૂર્ણ OS બનાવે છે, જેને ઘણી વાર <b>GNU/Linux</b> કહે છે. <b>Distribution (distro)</b> kernel, tools, desktop અને installer ને પૅક કરે છે: Ubuntu, Fedora, Debian, Linux Mint, Red Hat, Kali.</p>
<h4>Linux ના features</h4>
<ul>
<li><b>Free અને open source:</b> source code GPL હેઠળ ઉપલબ્ધ; કોઈ પણ તેનો અભ્યાસ, ફેરફાર અને વિતરણ કરી શકે.</li>
<li><b>Multi-user:</b> ઘણા users એક સાથે system વાપરી શકે, દરેક પોતાના account સાથે.</li>
<li><b>Multitasking:</b> ઘણા programs એક સાથે ચાલે.</li>
<li><b>Portable:</b> PCs, servers, phones (Android), routers અને supercomputers પર ચાલે.</li>
<li><b>Security:</b> user accounts, file permissions (rwx), root/superuser અલગ.</li>
<li><b>Hierarchical file system:</b> બધું root <code>/</code> થી શરૂ; devices પણ files છે.</li>
<li><b>Shell અને utilities:</b> સેંકડો નાના commands સાથેની શક્તિશાળી command line, જે pipes વડે જોડી શકાય.</li>
<li><b>Networking</b> support built-in; સ્થિર અને વિશ્વસનીય; antivirus ની ભાગ્યે જ જરૂર.</li>
</ul>
<h4>Unix vs Linux</h4>
""" + UW_GU),
        T("5.1.2 Basic Architecture of Unix / Linux", "5.1.2 Unix / Linux નું Basic Architecture",
          """<p>The Unix/Linux system is organised in <b>layers</b> around the hardware. Each layer uses the services of the layer inside it.</p>
<h4>1. Hardware</h4>
<p>The innermost layer: CPU, memory, disks, terminals and other devices.</p>
<h4>2. Kernel</h4>
<p>The <b>heart of the OS</b>; it is loaded into memory at boot and runs in kernel (privileged) mode. It interacts directly with the hardware and provides services to programs through <b>system calls</b> (fork, exec, open, read, write).</p>
<ul><li>Process management (creation, scheduling, termination, IPC)</li><li>Memory management (allocation, paging, swapping)</li><li>File management (file system, permissions)</li><li>Device management (device drivers, I/O)</li><li>Networking and security</li></ul>
<h4>3. Shell</h4>
<p>The <b>command interpreter</b> and the interface between the user and the kernel. It reads commands typed by the user, interprets them and asks the kernel to execute the programs. It also provides a programming language (shell scripts).</p>
<h4>4. Utilities and application programs</h4>
<p>Commands and programs used by users: <code>ls, cp, grep, sort, vi, gcc</code>, editors, compilers, browsers, databases.</p>
<h4>5. Users</h4>
<p>Users interact with the system through the shell or a graphical desktop.</p>""",
          """<p>Unix/Linux system hardware ની આસપાસ <b>layers</b> માં ગોઠવાયેલી છે. દરેક layer પોતાની અંદરની layer ની સેવાઓ વાપરે છે.</p>
<h4>1. Hardware</h4>
<p>સૌથી અંદરની layer: CPU, memory, disks, terminals અને બીજા devices.</p>
<h4>2. Kernel</h4>
<p><b>OS નું હૃદય</b>; boot વખતે memory માં load થાય અને kernel (privileged) mode માં ચાલે. તે hardware સાથે સીધું કામ કરે છે અને <b>system calls</b> (fork, exec, open, read, write) દ્વારા programs ને સેવાઓ આપે છે.</p>
<ul><li>Process management (creation, scheduling, termination, IPC)</li><li>Memory management (allocation, paging, swapping)</li><li>File management (file system, permissions)</li><li>Device management (device drivers, I/O)</li><li>Networking અને security</li></ul>
<h4>3. Shell</h4>
<p><b>Command interpreter</b> અને user તથા kernel વચ્ચેનું interface. તે user એ type કરેલા commands વાંચે, તેનું અર્થઘટન કરે અને kernel ને programs ચલાવવા કહે. તે programming language (shell scripts) પણ આપે છે.</p>
<h4>4. Utilities અને application programs</h4>
<p>Users દ્વારા વપરાતા commands અને programs: <code>ls, cp, grep, sort, vi, gcc</code>, editors, compilers, browsers, databases.</p>
<h4>5. Users</h4>
<p>Users shell કે graphical desktop દ્વારા system સાથે કામ કરે છે.</p>""",
          diagram="os5_arch"),
        T("5.1.3 Linux System Structure and Programming Basics", "5.1.3 Linux System Structure અને Programming Basics",
          """<h4>Linux system structure (user space and kernel space)</h4>
<ul>
<li><b>User space:</b> applications, shell and system utilities, and <b>system libraries</b> (glibc) that wrap system calls into functions such as <code>printf()</code>, <code>fopen()</code>.</li>
<li><b>System call interface:</b> the only entry from user space into the kernel.</li>
<li><b>Kernel space:</b> the Linux kernel is <b>monolithic</b> but supports <b>loadable kernel modules</b> (drivers can be added at run time).</li>
</ul>
<h4>Programming basics</h4>
<p>Programming on Unix/Linux is based on a few simple ideas:</p>
<ul>
<li><b>Everything is a file:</b> ordinary files, directories, devices (<code>/dev/sda</code>, <code>/dev/tty</code>) and even processes (<code>/proc</code>) are accessed like files.</li>
<li><b>Small tools, combined:</b> each command does one job well; commands are joined with <b>pipes</b> (<code>|</code>) and <b>redirection</b> (<code>&gt;</code>, <code>&lt;</code>).</li>
<li><b>Text streams:</b> every program has three standard files: <b>stdin</b> (0, keyboard), <b>stdout</b> (1, screen) and <b>stderr</b> (2, screen).</li>
<li><b>Processes:</b> a new process is created with <code>fork()</code> and a new program is loaded with <code>exec()</code>; each process has a PID (<code>ps</code>, <code>kill</code>).</li>
<li><b>Users and permissions:</b> every file has an owner, a group and rwx permissions; <b>root</b> is the superuser.</li>
<li><b>Programming tools:</b> shell scripts (bash), editors (vi, vim, gedit, nano), the C compiler <b>gcc</b>, <code>make</code>, debugger <code>gdb</code>; also Python, Java and more.</li>
</ul>
<h4>Logging in</h4>
<p>The user logs in with a user name and password; the shell then shows a <b>prompt</b> such as <code>student@pc:~$</code> (<code>#</code> for root). Commands are typed after the prompt and executed when Enter is pressed. <code>exit</code> or Ctrl+D logs out.</p>""",
          """<h4>Linux system structure (user space અને kernel space)</h4>
<ul>
<li><b>User space:</b> applications, shell અને system utilities, અને <b>system libraries</b> (glibc) જે system calls ને <code>printf()</code>, <code>fopen()</code> જેવા functions માં લપેટે છે.</li>
<li><b>System call interface:</b> user space માંથી kernel માં જવાનો એકમાત્ર રસ્તો.</li>
<li><b>Kernel space:</b> Linux kernel <b>monolithic</b> છે પણ <b>loadable kernel modules</b> ને support કરે છે (drivers run time પર ઉમેરી શકાય).</li>
</ul>
<h4>Programming basics</h4>
<p>Unix/Linux પર programming થોડા સરળ વિચારો પર આધારિત છે:</p>
<ul>
<li><b>બધું જ file છે:</b> સામાન્ય files, directories, devices (<code>/dev/sda</code>, <code>/dev/tty</code>) અને processes (<code>/proc</code>) પણ files ની જેમ access થાય છે.</li>
<li><b>નાના tools, જોડીને:</b> દરેક command એક કામ સારી રીતે કરે છે; commands <b>pipes</b> (<code>|</code>) અને <b>redirection</b> (<code>&gt;</code>, <code>&lt;</code>) વડે જોડાય છે.</li>
<li><b>Text streams:</b> દરેક program પાસે ત્રણ standard files હોય: <b>stdin</b> (0, keyboard), <b>stdout</b> (1, screen) અને <b>stderr</b> (2, screen).</li>
<li><b>Processes:</b> નવી process <code>fork()</code> થી બને અને નવો program <code>exec()</code> થી load થાય; દરેક process ને PID હોય (<code>ps</code>, <code>kill</code>).</li>
<li><b>Users અને permissions:</b> દરેક file ને owner, group અને rwx permissions હોય; <b>root</b> superuser છે.</li>
<li><b>Programming tools:</b> shell scripts (bash), editors (vi, vim, gedit, nano), C compiler <b>gcc</b>, <code>make</code>, debugger <code>gdb</code>; ઉપરાંત Python, Java વગેરે.</li>
</ul>
<h4>Login</h4>
<p>User user name અને password થી login કરે; પછી shell <code>student@pc:~$</code> જેવો <b>prompt</b> બતાવે (root માટે <code>#</code>). Commands prompt પછી type કરાય અને Enter દબાવતાં ચાલે. <code>exit</code> અથવા Ctrl+D logout કરે.</p>""",
          diagram="os5_kernel"),
        T("5.1.4 Linux Directory Hierarchy", "5.1.4 Linux Directory Hierarchy",
          """<p>All files in Linux are arranged in a <b>single inverted tree</b> that starts at the <b>root directory /</b>. There are no drive letters as in Windows; other disks and pen drives are <b>mounted</b> on a directory of this tree (e.g. <code>/media/usb</code>). The layout follows the <b>Filesystem Hierarchy Standard (FHS)</b>.</p>
""" + tbl(["Directory", "Contents"], [("/", "Root of the whole file system"), ("/bin, /sbin", "Essential user and system commands (ls, cp, mount)"), ("/boot", "Kernel image and boot loader (GRUB) files"), ("/dev", "Device files: /dev/sda (disk), /dev/tty (terminal), /dev/null"), ("/etc", "System configuration files: passwd, group, hosts, fstab"), ("/home", "Home directories of users (/home/student)"), ("/lib", "Shared libraries and kernel modules"), ("/root", "Home directory of the superuser root"), ("/tmp", "Temporary files, cleared at reboot"), ("/usr", "User programs and data: /usr/bin, /usr/lib, /usr/share"), ("/var", "Variable data: logs (/var/log), mail, spool"), ("/mnt, /media", "Mount points for other file systems, pen drives"), ("/proc", "Virtual files with process and kernel information")]) + """
<p>Each user has a <b>home directory</b> (<code>/home/student</code>, written as <code>~</code>) where the shell starts after login; users can create files only there (and in <code>/tmp</code>). Path names can be absolute (<code>/etc/passwd</code>) or relative (<code>../notes.txt</code>).</p>""",
          """<p>Linux માં બધી files <b>root directory /</b> થી શરૂ થતા <b>એક જ ઊંધા tree</b> માં ગોઠવાયેલી છે. Windows જેવા drive letters નથી; બીજી disks અને pen drives આ tree ની કોઈ directory પર <b>mount</b> થાય છે (દા.ત. <code>/media/usb</code>). ગોઠવણી <b>Filesystem Hierarchy Standard (FHS)</b> મુજબ છે.</p>
""" + tbl(["Directory", "સામગ્રી"], [("/", "આખી file system નું root"), ("/bin, /sbin", "જરૂરી user અને system commands (ls, cp, mount)"), ("/boot", "Kernel image અને boot loader (GRUB) files"), ("/dev", "Device files: /dev/sda (disk), /dev/tty (terminal), /dev/null"), ("/etc", "System configuration files: passwd, group, hosts, fstab"), ("/home", "Users ની home directories (/home/student)"), ("/lib", "Shared libraries અને kernel modules"), ("/root", "Superuser root ની home directory"), ("/tmp", "કામચલાઉ files, reboot પર સાફ"), ("/usr", "User programs અને data: /usr/bin, /usr/lib, /usr/share"), ("/var", "બદલાતો data: logs (/var/log), mail, spool"), ("/mnt, /media", "બીજી file systems, pen drives ના mount points"), ("/proc", "Process અને kernel માહિતી ધરાવતી virtual files")]) + """
<p>દરેક user પાસે <b>home directory</b> (<code>/home/student</code>, <code>~</code> તરીકે લખાય) હોય છે જ્યાં login પછી shell શરૂ થાય; users માત્ર ત્યાં (અને <code>/tmp</code> માં) files બનાવી શકે. Path names absolute (<code>/etc/passwd</code>) કે relative (<code>../notes.txt</code>) હોઈ શકે.</p>""",
          diagram="os5_fs_tree"),
    ]}

SEC_5_2 = {
    "title": {"en": "5.2 Shell and Commands", "gu": "5.2 Shell અને Commands"},
    "items": [
        T("5.2.1 Introduction to Shell and Commands", "5.2.1 Shell અને Commands નો પરિચય",
          """<p>The <b>shell</b> is a program that provides the <b>command-line interface</b> to Linux. It is both a <b>command interpreter</b> (runs commands typed by the user) and a <b>programming language</b> (shell scripts with variables, conditions and loops).</p>
<h4>Types of shells</h4>
""" + SHELLS_EN + """
<p><code>echo $SHELL</code> shows the current shell; <code>cat /etc/shells</code> lists the available shells.</p>
<h4>How the shell executes a command</h4>
<ol><li>Displays the prompt and reads the command line.</li><li>Parses it into command, options and arguments; expands wildcards (<code>*</code>, <code>?</code>, <code>[ ]</code>), variables (<code>$x</code>) and command substitution.</li><li>Finds the command: a <b>built-in</b> (cd, echo, pwd) or an external program searched in the directories of <code>$PATH</code>.</li><li>Creates a child process (<code>fork</code>), runs the program in it (<code>exec</code>) and <b>waits</b>; then shows the prompt again.</li></ol>
<h4>Command format</h4>
<p><code>command [options] [arguments]</code> e.g. <code>ls -l /home</code>. Options usually start with <code>-</code> and can be combined (<code>ls -la</code>). Commands are case-sensitive. Help: <code>man ls</code>, <code>ls --help</code>.</p>
<h4>Redirection, pipes and wildcards</h4>
<ul><li><code>&gt;</code> output to a file (overwrite), <code>&gt;&gt;</code> append, <code>&lt;</code> input from a file, <code>2&gt;</code> errors to a file.</li><li><code>|</code> pipe: output of one command becomes input of the next.</li><li><code>*</code> any characters, <code>?</code> one character, <code>[abc]</code> one of the listed characters.</li><li>Quotes: <code>"…"</code> expands variables, <code>'…'</code> does not.</li></ul>
<h4>Example (real output)</h4>
""" + D.pre(D.SHELL),
          """<p><b>Shell</b> એ program છે જે Linux નું <b>command-line interface</b> આપે છે. તે <b>command interpreter</b> (user એ type કરેલા commands ચલાવે) અને <b>programming language</b> (variables, conditions અને loops સાથેના shell scripts) બંને છે.</p>
<h4>Shells ના પ્રકારો</h4>
""" + SHELLS_GU + """
<p><code>echo $SHELL</code> હાલનો shell બતાવે; <code>cat /etc/shells</code> ઉપલબ્ધ shells ની યાદી આપે.</p>
<h4>Shell command કેવી રીતે ચલાવે છે</h4>
<ol><li>Prompt બતાવી command line વાંચે.</li><li>તેને command, options અને arguments માં વહેંચે; wildcards (<code>*</code>, <code>?</code>, <code>[ ]</code>), variables (<code>$x</code>) અને command substitution expand કરે.</li><li>Command શોધે: <b>built-in</b> (cd, echo, pwd) અથવા <code>$PATH</code> ની directories માં શોધાતો external program.</li><li>Child process બનાવે (<code>fork</code>), તેમાં program ચલાવે (<code>exec</code>) અને <b>રાહ જુએ</b>; પછી ફરી prompt બતાવે.</li></ol>
<h4>Command format</h4>
<p><code>command [options] [arguments]</code> દા.ત. <code>ls -l /home</code>. Options સામાન્ય રીતે <code>-</code> થી શરૂ થાય અને ભેગા કરી શકાય (<code>ls -la</code>). Commands case-sensitive છે. મદદ: <code>man ls</code>, <code>ls --help</code>.</p>
<h4>Redirection, pipes અને wildcards</h4>
<ul><li><code>&gt;</code> output file માં (overwrite), <code>&gt;&gt;</code> append, <code>&lt;</code> file માંથી input, <code>2&gt;</code> errors file માં.</li><li><code>|</code> pipe: એક command નું output આગળના command નું input બને.</li><li><code>*</code> કોઈ પણ અક્ષરો, <code>?</code> એક અક્ષર, <code>[abc]</code> યાદીમાંનો એક અક્ષર.</li><li>Quotes: <code>"…"</code> variables expand કરે, <code>'…'</code> નહીં.</li></ul>
<h4>ઉદાહરણ (ખરું output)</h4>
""" + D.pre(D.SHELL),
          diagram="os5_shell"),
        T("5.2.2 Directory Commands: pwd, cd, mkdir, rmdir, ls", "5.2.2 Directory Commands: pwd, cd, mkdir, rmdir, ls",
          """<h4>pwd (print working directory)</h4>
<p>Displays the absolute path of the current directory. Syntax: <code>pwd</code></p>
<h4>cd (change directory)</h4>
<p>Changes the current directory. <code>cd dir</code>, <code>cd ..</code> (parent), <code>cd /</code> (root), <code>cd</code> or <code>cd ~</code> (home), <code>cd -</code> (previous directory). Both absolute and relative paths can be used.</p>
<h4>mkdir (make directory)</h4>
<p>Creates one or more directories: <code>mkdir os</code>, <code>mkdir d1 d2</code>. Option <code>-p</code> creates the whole path including missing parents: <code>mkdir -p sem3/os/unit5</code>.</p>
<h4>rmdir (remove directory)</h4>
<p>Removes <b>empty</b> directories only: <code>rmdir os</code>. A non-empty directory gives an error; use <code>rm -r</code> to delete it with its contents.</p>
<h4>ls (list)</h4>
<p>Lists the files and directories. Common options:</p>
<ul><li><code>-l</code> long listing (permissions, links, owner, group, size, date, name)</li><li><code>-a</code> all files including hidden ones (names starting with <code>.</code>)</li><li><code>-R</code> recursive (subdirectories too), <code>-t</code> sort by time, <code>-r</code> reverse, <code>-i</code> inode number, <code>-h</code> human-readable sizes, <code>-d</code> directory itself</li></ul>
<h4>Example (real output)</h4>
""" + D.pre(D.DIRS),
          """<h4>pwd (print working directory)</h4>
<p>Current directory નો absolute path બતાવે છે. Syntax: <code>pwd</code></p>
<h4>cd (change directory)</h4>
<p>Current directory બદલે છે. <code>cd dir</code>, <code>cd ..</code> (parent), <code>cd /</code> (root), <code>cd</code> અથવા <code>cd ~</code> (home), <code>cd -</code> (પાછલી directory). Absolute અને relative બંને paths વાપરી શકાય.</p>
<h4>mkdir (make directory)</h4>
<p>એક કે વધુ directories બનાવે: <code>mkdir os</code>, <code>mkdir d1 d2</code>. Option <code>-p</code> ખૂટતા parents સહિત આખો path બનાવે: <code>mkdir -p sem3/os/unit5</code>.</p>
<h4>rmdir (remove directory)</h4>
<p>માત્ર <b>ખાલી</b> directories દૂર કરે: <code>rmdir os</code>. ખાલી ન હોય તો error આવે; તેને સામગ્રી સહિત delete કરવા <code>rm -r</code> વાપરો.</p>
<h4>ls (list)</h4>
<p>Files અને directories ની યાદી આપે. સામાન્ય options:</p>
<ul><li><code>-l</code> long listing (permissions, links, owner, group, size, date, name)</li><li><code>-a</code> hidden (<code>.</code> થી શરૂ થતી) સહિત બધી files</li><li><code>-R</code> recursive (subdirectories પણ), <code>-t</code> time મુજબ, <code>-r</code> reverse, <code>-i</code> inode number, <code>-h</code> human-readable sizes, <code>-d</code> directory પોતે</li></ul>
<h4>ઉદાહરણ (ખરું output)</h4>
""" + D.pre(D.DIRS),
          diagram="os5_ls_l"),
        T("5.2.3 File Commands: cat, cp, rm, mv", "5.2.3 File Commands: cat, cp, rm, mv",
          """<h4>cat (concatenate)</h4>
<ul><li><code>cat file</code> displays a file; <code>cat f1 f2</code> displays several files one after another.</li><li><code>cat &gt; file</code> creates a file from keyboard input (end with <b>Ctrl+D</b>); <code>cat &gt;&gt; file</code> appends.</li><li><code>cat f1 f2 &gt; f3</code> joins files into f3; <code>-n</code> numbers the lines.</li></ul>
<h4>cp (copy)</h4>
<ul><li><code>cp src dest</code> copies a file; <code>cp f1 f2 dir/</code> copies files into a directory.</li><li><code>-r</code> copies directories recursively, <code>-i</code> asks before overwriting, <code>-p</code> preserves time and permissions.</li></ul>
<h4>rm (remove)</h4>
<ul><li><code>rm file</code> deletes files permanently (no recycle bin).</li><li><code>-i</code> asks for confirmation, <code>-r</code> deletes a directory and everything in it, <code>-f</code> forces without asking. <code>rm -rf</code> must be used very carefully.</li></ul>
<h4>mv (move / rename)</h4>
<ul><li><code>mv old new</code> renames a file or directory.</li><li><code>mv file dir/</code> moves it into another directory (the inode is unchanged, so moving within the same file system is instant).</li><li><code>-i</code> asks before overwriting.</li></ul>
<h4>Example (real output)</h4>
""" + D.pre(D.FILES),
          """<h4>cat (concatenate)</h4>
<ul><li><code>cat file</code> file બતાવે; <code>cat f1 f2</code> ઘણી files એક પછી એક બતાવે.</li><li><code>cat &gt; file</code> keyboard input થી file બનાવે (<b>Ctrl+D</b> થી પૂરું); <code>cat &gt;&gt; file</code> append કરે.</li><li><code>cat f1 f2 &gt; f3</code> files ને f3 માં જોડે; <code>-n</code> lines ને નંબર આપે.</li></ul>
<h4>cp (copy)</h4>
<ul><li><code>cp src dest</code> file copy કરે; <code>cp f1 f2 dir/</code> files ને directory માં copy કરે.</li><li><code>-r</code> directories ને recursively copy કરે, <code>-i</code> overwrite પહેલાં પૂછે, <code>-p</code> time અને permissions જાળવે.</li></ul>
<h4>rm (remove)</h4>
<ul><li><code>rm file</code> files ને કાયમ માટે delete કરે (recycle bin નથી).</li><li><code>-i</code> ખાતરી માંગે, <code>-r</code> directory અને તેમાંનું બધું delete કરે, <code>-f</code> પૂછ્યા વગર force કરે. <code>rm -rf</code> ખૂબ સાવધાનીથી વાપરવું.</li></ul>
<h4>mv (move / rename)</h4>
<ul><li><code>mv old new</code> file કે directory નું નામ બદલે.</li><li><code>mv file dir/</code> તેને બીજી directory માં ખસેડે (inode બદલાતો નથી, તેથી એ જ file system માં move તરત થાય).</li><li><code>-i</code> overwrite પહેલાં પૂછે.</li></ul>
<h4>ઉદાહરણ (ખરું output)</h4>
""" + D.pre(D.FILES)),
        T("5.2.4 wc, split, head and tail", "5.2.4 wc, split, head અને tail",
          """<h4>wc (word count)</h4>
<p>Counts <b>lines, words and characters (bytes)</b> of a file. Output order: lines, words, bytes, file name. Options: <code>-l</code> lines only, <code>-w</code> words, <code>-c</code> bytes, <code>-m</code> characters. With a pipe: <code>ls | wc -l</code> counts files.</p>
<h4>split</h4>
<p>Splits a large file into smaller pieces named <code>xaa, xab, …</code> (or with a given prefix). Default: 1000 lines per piece. <code>-l n</code> n lines per piece, <code>-b size</code> by bytes (<code>1k</code>, <code>1m</code>). The pieces can be joined back with <code>cat part_* &gt; file</code>.</p>
<h4>head</h4>
<p>Displays the <b>first</b> lines of a file (default 10). <code>head -n 3 file</code> or <code>head -3 file</code>; <code>-c</code> for bytes.</p>
<h4>tail</h4>
<p>Displays the <b>last</b> lines of a file (default 10). <code>tail -n 2 file</code>; <code>tail -n +5 file</code> from line 5 to the end; <code>tail -f log</code> keeps showing new lines as the file grows (used for log files).</p>
<p>Combined: <code>head -7 file | tail -3</code> shows lines 5 to 7.</p>
<h4>Example (real output)</h4>
""" + D.pre(D.WC),
          """<h4>wc (word count)</h4>
<p>File ની <b>lines, words અને characters (bytes)</b> ગણે છે. Output ક્રમ: lines, words, bytes, file name. Options: <code>-l</code> માત્ર lines, <code>-w</code> words, <code>-c</code> bytes, <code>-m</code> characters. Pipe સાથે: <code>ls | wc -l</code> files ગણે.</p>
<h4>split</h4>
<p>મોટી file ને <code>xaa, xab, …</code> (અથવા આપેલા prefix) નામના નાના ભાગોમાં વહેંચે. Default: ભાગ દીઠ 1000 lines. <code>-l n</code> ભાગ દીઠ n lines, <code>-b size</code> bytes મુજબ (<code>1k</code>, <code>1m</code>). ભાગો <code>cat part_* &gt; file</code> થી ફરી જોડી શકાય.</p>
<h4>head</h4>
<p>File ની <b>શરૂઆતની</b> lines બતાવે (default 10). <code>head -n 3 file</code> અથવા <code>head -3 file</code>; bytes માટે <code>-c</code>.</p>
<h4>tail</h4>
<p>File ની <b>છેલ્લી</b> lines બતાવે (default 10). <code>tail -n 2 file</code>; <code>tail -n +5 file</code> line 5 થી અંત સુધી; <code>tail -f log</code> file વધે તેમ નવી lines બતાવતું રહે (log files માટે).</p>
<p>ભેગા: <code>head -7 file | tail -3</code> lines 5 થી 7 બતાવે.</p>
<h4>ઉદાહરણ (ખરું output)</h4>
""" + D.pre(D.WC)),
        T("5.2.5 Comparing Files: cmp, comm, diff", "5.2.5 Files ની સરખામણી: cmp, comm, diff",
          """<h4>cmp (compare)</h4>
<p>Compares two files <b>byte by byte</b> and reports the <b>first</b> difference (byte number and line number). If the files are identical it prints nothing and returns exit status 0. Works for binary files too. <code>-l</code> lists all differing bytes.</p>
<h4>comm (common)</h4>
<p>Compares two <b>sorted</b> files line by line and prints three columns:</p>
<ol><li>lines only in file 1,</li><li>lines only in file 2 (one tab),</li><li>lines common to both (two tabs).</li></ol>
<p><code>-1</code>, <code>-2</code>, <code>-3</code> suppress the corresponding column; <code>comm -12 f1 f2</code> shows only common lines.</p>
<h4>diff (difference)</h4>
<p>Shows <b>all</b> line differences and tells what changes are needed to make file 1 identical to file 2. Codes: <code>a</code> add, <code>c</code> change, <code>d</code> delete; lines from file 1 are marked <code>&lt;</code> and lines from file 2 <code>&gt;</code>. Example: <code>3c3</code> means line 3 of f1 must be changed to line 3 of f2. Options: <code>-i</code> ignore case, <code>-w</code> ignore white space, <code>-u</code> unified format.</p>
<h4>Example (real output)</h4>
""" + D.pre(D.CMP),
          """<h4>cmp (compare)</h4>
<p>બે files ને <b>byte દર byte</b> સરખાવે અને <b>પહેલો</b> તફાવત (byte number અને line number) જણાવે. Files સરખી હોય તો કંઈ છાપતું નથી અને exit status 0 આપે. Binary files માટે પણ કામ કરે. <code>-l</code> બધા જુદા bytes ની યાદી આપે.</p>
<h4>comm (common)</h4>
<p>બે <b>sorted</b> files ને line દર line સરખાવે અને ત્રણ columns છાપે:</p>
<ol><li>માત્ર file 1 માંની lines,</li><li>માત્ર file 2 માંની lines (એક tab),</li><li>બંનેમાં સામાન્ય lines (બે tabs).</li></ol>
<p><code>-1</code>, <code>-2</code>, <code>-3</code> અનુરૂપ column છુપાવે; <code>comm -12 f1 f2</code> માત્ર સામાન્ય lines બતાવે.</p>
<h4>diff (difference)</h4>
<p><b>બધા</b> line તફાવતો બતાવે અને file 1 ને file 2 જેવી બનાવવા કયા ફેરફારો જોઈએ તે કહે. Codes: <code>a</code> add, <code>c</code> change, <code>d</code> delete; file 1 ની lines <code>&lt;</code> અને file 2 ની lines <code>&gt;</code> થી દર્શાવાય. ઉદાહરણ: <code>3c3</code> એટલે f1 ની line 3 ને f2 ની line 3 માં બદલવી. Options: <code>-i</code> case અવગણો, <code>-w</code> white space અવગણો, <code>-u</code> unified format.</p>
<h4>ઉદાહરણ (ખરું output)</h4>
""" + D.pre(D.CMP)),
        T("5.2.6 Searching and Sorting: grep, sort", "5.2.6 Searching અને Sorting: grep, sort",
          """<h4>grep (Global Regular Expression Print)</h4>
<p>Searches files for lines that <b>match a pattern</b> and prints them. Syntax: <code>grep [options] pattern [files]</code></p>
<ul>
<li><code>-i</code> ignore case, <code>-v</code> print lines that do <b>not</b> match, <code>-c</code> count matching lines, <code>-n</code> show line numbers, <code>-l</code> list only file names, <code>-w</code> whole word, <code>-e</code> several patterns.</li>
<li>Regular expressions: <code>^</code> start of line, <code>$</code> end of line, <code>.</code> any character, <code>*</code> zero or more, <code>[abc]</code> one of. Example: <code>grep '^A' file</code> lines starting with A.</li>
</ul>
<h4>sort</h4>
<p>Sorts the lines of a file (default: alphabetical, ascending) and prints them; the file itself is not changed unless <code>-o</code> is used.</p>
<ul>
<li><code>-r</code> reverse, <code>-n</code> numeric, <code>-u</code> remove duplicates, <code>-f</code> ignore case.</li>
<li><code>-k n</code> sort by field n, <code>-t ':'</code> field separator (e.g. <code>sort -t: -k3 -n /etc/passwd</code>).</li>
<li><code>-o file</code> write the result to a file.</li>
</ul>
<h4>Example (real output)</h4>
<p>File <code>students.txt</code> has 10 lines of the form <i>name branch marks</i>.</p>
""" + D.pre(D.GREP) + D.pre(D.SORT),
          """<h4>grep (Global Regular Expression Print)</h4>
<p>Files માં <b>pattern સાથે મેળ ખાતી</b> lines શોધી છાપે છે. Syntax: <code>grep [options] pattern [files]</code></p>
<ul>
<li><code>-i</code> case અવગણો, <code>-v</code> મેળ <b>ન</b> ખાતી lines, <code>-c</code> મેળ ખાતી lines ગણો, <code>-n</code> line numbers બતાવો, <code>-l</code> માત્ર file names, <code>-w</code> આખો શબ્દ, <code>-e</code> ઘણા patterns.</li>
<li>Regular expressions: <code>^</code> line ની શરૂઆત, <code>$</code> line નો અંત, <code>.</code> કોઈ પણ અક્ષર, <code>*</code> શૂન્ય કે વધુ, <code>[abc]</code> તેમાંનો એક. ઉદાહરણ: <code>grep '^A' file</code> A થી શરૂ થતી lines.</li>
</ul>
<h4>sort</h4>
<p>File ની lines sort કરી છાપે (default: alphabetical, ચડતો ક્રમ); <code>-o</code> ન વાપરો ત્યાં સુધી file પોતે બદલાતી નથી.</p>
<ul>
<li><code>-r</code> reverse, <code>-n</code> numeric, <code>-u</code> duplicates દૂર, <code>-f</code> case અવગણો.</li>
<li><code>-k n</code> field n મુજબ sort, <code>-t ':'</code> field separator (દા.ત. <code>sort -t: -k3 -n /etc/passwd</code>).</li>
<li><code>-o file</code> પરિણામ file માં લખો.</li>
</ul>
<h4>ઉદાહરણ (ખરું output)</h4>
<p>File <code>students.txt</code> માં <i>name branch marks</i> સ્વરૂપની 10 lines છે.</p>
""" + D.pre(D.GREP) + D.pre(D.SORT)),
    ]}

from content_DI03000041_u5_notes_b import SEC_5_3, SEC_5_4  # noqa: E402

NOTES = [SEC_5_1, SEC_5_2, SEC_5_3, SEC_5_4]
