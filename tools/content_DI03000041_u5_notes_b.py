"""Fundamentals of Operating System (DI03000041) - Unit 5 notes part B: 5.3 Editors vi, vim, gedit and gcc;
5.4 Basic shell scripts (arguments, operators, test, if, case, while, for)."""
import html
from content_DI03000011_u1_notes_a import T
from content_DI03000041_u1_notes import tbl
import os_u5_demos as D


def TP(*a, programs=None, **k):
    t = T(*a, **k)
    if programs:
        t["programs"] = programs
    return t


def code(s):
    s = s.strip("\n")
    for ln in s.splitlines():
        assert len(ln) <= 43, ln
    return '<pre class="c">' + html.escape(s) + "</pre>"


VI_EN = tbl(["Task", "Command (in command mode)"], [
    ("Insert", "i (before cursor), a (after), o (new line below), I, A, O"),
    ("Move", "h j k l (left, down, up, right), w / b word, 0 / $ line start / end, gg / G first / last line, :n go to line n"),
    ("Delete", "x character, dw word, dd line, 3dd three lines, D to end of line"),
    ("Copy / paste", "yy copy line, 3yy three lines, p paste below, P above"),
    ("Undo / redo", "u undo, Ctrl+R redo, . repeat last change"),
    ("Search / replace", "/word forward, ?word backward, n next, :%s/old/new/g replace all"),
    ("Save / quit", ":w save, :w name save as, :q quit, :wq or ZZ save and quit, :q! quit without saving"),
    ("Settings", ":set nu line numbers, :set nonu, :syntax on (vim)")])
VI_GU = tbl(["કાર્ય", "Command (command mode માં)"], [
    ("Insert", "i (cursor પહેલાં), a (પછી), o (નીચે નવી line), I, A, O"),
    ("Move", "h j k l (ડાબે, નીચે, ઉપર, જમણે), w / b શબ્દ, 0 / $ line ની શરૂઆત / અંત, gg / G પહેલી / છેલ્લી line, :n line n પર"),
    ("Delete", "x અક્ષર, dw શબ્દ, dd line, 3dd ત્રણ lines, D line ના અંત સુધી"),
    ("Copy / paste", "yy line copy, 3yy ત્રણ lines, p નીચે paste, P ઉપર"),
    ("Undo / redo", "u undo, Ctrl+R redo, . છેલ્લો ફેરફાર ફરી"),
    ("Search / replace", "/word આગળ, ?word પાછળ, n આગળનું, :%s/old/new/g બધે replace"),
    ("Save / quit", ":w save, :w name save as, :q quit, :wq અથવા ZZ save અને quit, :q! save વગર quit"),
    ("Settings", ":set nu line numbers, :set nonu, :syntax on (vim)")])

ARITH_EN = tbl(["Operator", "Meaning", "expr form", "$(( )) form"], [
    ("+", "Addition", "expr $a + $b", "$((a + b))"), ("-", "Subtraction", "expr $a - $b", "$((a - b))"),
    ("*", "Multiplication", "expr $a \\* $b", "$((a * b))"), ("/", "Integer division", "expr $a / $b", "$((a / b))"),
    ("%", "Remainder (modulus)", "expr $a % $b", "$((a % b))"), ("=", "Assignment", "a=10 (no spaces)", "let a=b+1")])
ARITH_GU = tbl(["Operator", "અર્થ", "expr સ્વરૂપ", "$(( )) સ્વરૂપ"], [
    ("+", "સરવાળો", "expr $a + $b", "$((a + b))"), ("-", "બાદબાકી", "expr $a - $b", "$((a - b))"),
    ("*", "ગુણાકાર", "expr $a \\* $b", "$((a * b))"), ("/", "Integer ભાગાકાર", "expr $a / $b", "$((a / b))"),
    ("%", "શેષ (modulus)", "expr $a % $b", "$((a % b))"), ("=", "Assignment", "a=10 (spaces નહીં)", "let a=b+1")])
REL_EN = tbl(["Operator", "Meaning", "Example (a=10, b=20)"], [
    ("-eq", "equal to", "[ $a -eq $b ] → false"), ("-ne", "not equal to", "[ $a -ne $b ] → true"),
    ("-gt", "greater than", "[ $a -gt $b ] → false"), ("-ge", "greater than or equal", "[ $a -ge 10 ] → true"),
    ("-lt", "less than", "[ $a -lt $b ] → true"), ("-le", "less than or equal", "[ $b -le 15 ] → false")])
REL_GU = tbl(["Operator", "અર્થ", "ઉદાહરણ (a=10, b=20)"], [
    ("-eq", "બરાબર", "[ $a -eq $b ] → false"), ("-ne", "બરાબર નથી", "[ $a -ne $b ] → true"),
    ("-gt", "થી મોટું", "[ $a -gt $b ] → false"), ("-ge", "થી મોટું કે બરાબર", "[ $a -ge 10 ] → true"),
    ("-lt", "થી નાનું", "[ $a -lt $b ] → true"), ("-le", "થી નાનું કે બરાબર", "[ $b -le 15 ] → false")])
LOG_EN = tbl(["Operator", "Meaning", "Example"], [
    ("-a", "AND (inside [ ])", "[ $a -gt 0 -a $a -lt 100 ]"), ("-o", "OR (inside [ ])", "[ $x -eq 1 -o $x -eq 2 ]"),
    ("!", "NOT", "[ ! -f file ]"), ("&amp;&amp;", "AND between commands", "[ $a -gt 0 ] &amp;&amp; [ $a -lt 100 ]"),
    ("||", "OR between commands", "[ -f f ] || echo \"missing\"")])
LOG_GU = tbl(["Operator", "અર્થ", "ઉદાહરણ"], [
    ("-a", "AND ([ ] ની અંદર)", "[ $a -gt 0 -a $a -lt 100 ]"), ("-o", "OR ([ ] ની અંદર)", "[ $x -eq 1 -o $x -eq 2 ]"),
    ("!", "NOT", "[ ! -f file ]"), ("&amp;&amp;", "Commands વચ્ચે AND", "[ $a -gt 0 ] &amp;&amp; [ $a -lt 100 ]"),
    ("||", "Commands વચ્ચે OR", "[ -f f ] || echo \"missing\"")])
TEST_EN = tbl(["Type", "Test", "True if"], [
    ("String", "s1 = s2  /  s1 != s2", "strings are equal / not equal"), ("String", "-z s  /  -n s", "string is empty / not empty"),
    ("File", "-e f", "file exists"), ("File", "-f f  /  -d f", "regular file / directory"),
    ("File", "-r f  -w f  -x f", "readable / writable / executable"), ("File", "-s f", "file exists and size &gt; 0"),
    ("Number", "-eq -ne -gt -ge -lt -le", "numeric comparison (see relational operators)")])
TEST_GU = tbl(["પ્રકાર", "Test", "ક્યારે true"], [
    ("String", "s1 = s2  /  s1 != s2", "strings સરખી / જુદી"), ("String", "-z s  /  -n s", "string ખાલી / ખાલી નથી"),
    ("File", "-e f", "file છે"), ("File", "-f f  /  -d f", "regular file / directory"),
    ("File", "-r f  -w f  -x f", "readable / writable / executable"), ("File", "-s f", "file છે અને size &gt; 0"),
    ("Number", "-eq -ne -gt -ge -lt -le", "numeric સરખામણી (relational operators જુઓ)")])
ARGS_EN = tbl(["Variable", "Meaning"], [
    ("$0", "Name of the script"), ("$1 … $9, ${10}", "First to ninth (tenth…) argument"), ("$#", "Number of arguments"),
    ("$@", "All arguments as separate words (\"$@\")"), ("$*", "All arguments as a single string (\"$*\")"),
    ("$?", "Exit status of the last command (0 = success)"), ("$$", "Process ID (PID) of the current shell")])
ARGS_GU = tbl(["Variable", "અર્થ"], [
    ("$0", "Script નું નામ"), ("$1 … $9, ${10}", "પહેલાથી નવમો (દસમો…) argument"), ("$#", "Arguments ની સંખ્યા"),
    ("$@", "બધા arguments અલગ શબ્દો તરીકે (\"$@\")"), ("$*", "બધા arguments એક string તરીકે (\"$*\")"),
    ("$?", "છેલ્લા command નો exit status (0 = success)"), ("$$", "હાલના shell નો Process ID (PID)")])

IF_CODE = code('''
# simple if
if [ $n -gt 0 ]
then
  echo "Positive"
fi

# if-else
if [ $n -gt 0 ]; then
  echo "Positive"
else
  echo "Not positive"
fi

# if-elif-else ladder
if [ $n -gt 0 ]; then
  echo "Positive"
elif [ $n -lt 0 ]; then
  echo "Negative"
else
  echo "Zero"
fi
''')
CASE_CODE = code('''
case $var in
  pattern1) commands ;;
  pattern2|pattern3) commands ;;
  *) default commands ;;
esac
''')
WHILE_CODE = code('''
i=1
while [ $i -le 5 ]
do
  echo $i
  i=`expr $i + 1`
done

# until: repeats while condition is FALSE
until [ $i -gt 5 ]; do ...; done
''')
FOR_CODE = code('''
for name in list
do
  commands
done

for i in 1 2 3 4 5     # list of words
for i in {1..10}       # range
for f in *.txt         # file names
for x in "$@"          # all arguments
for (( i=1; i<=5; i++ ))   # C-style
''')
FIRST_CODE = code('''
#!/bin/bash
# my first shell script
echo "Today is a good day"
echo -n "Enter your name: "
read name
echo "Hello, $name"
''')

SEC_5_3 = {
    "title": {"en": "5.3 Editing Files: vi, vim, gedit and gcc", "gu": "5.3 Files Editing: vi, vim, gedit અને gcc"},
    "items": [
        T("5.3.1 vi and vim Editors", "5.3.1 vi અને vim Editors",
          """<p><b>vi</b> (visual editor) is the standard screen-oriented text editor available on every Unix/Linux system; it works in a terminal without a mouse. <b>vim</b> (vi improved) is an enhanced version with syntax highlighting, multi-level undo, split windows, tabs and plugins. On most Linux systems the <code>vi</code> command actually starts vim.</p>
<p>Start: <code>vi notes.txt</code> or <code>vim notes.txt</code> (creates the file if it does not exist).</p>
<h4>Modes of vi</h4>
<ol>
<li><b>Command mode (normal mode):</b> the default mode when vi starts. Keys act as commands: move the cursor, delete, copy, paste, undo.</li>
<li><b>Insert mode:</b> entered by <code>i, a, o, I, A, O</code>; whatever you type is inserted into the file. Press <b>Esc</b> to return to command mode.</li>
<li><b>Last-line (ex / command-line) mode:</b> entered by typing <code>:</code> in command mode; the cursor moves to the bottom line for commands like save, quit, search-replace and settings. Enter executes the command.</li>
</ol>
<h4>Important vi commands</h4>
""" + VI_EN + """
<p><b>Typical session:</b> <code>vi hello.sh</code> → press <code>i</code> → type the script → <b>Esc</b> → <code>:wq</code> → Enter.</p>""",
          """<p><b>vi</b> (visual editor) એ દરેક Unix/Linux system પર ઉપલબ્ધ standard screen-oriented text editor છે; તે mouse વગર terminal માં કામ કરે છે. <b>vim</b> (vi improved) syntax highlighting, multi-level undo, split windows, tabs અને plugins વાળું સુધારેલું version છે. મોટા ભાગની Linux systems માં <code>vi</code> command ખરેખર vim શરૂ કરે છે.</p>
<p>શરૂ કરવા: <code>vi notes.txt</code> અથવા <code>vim notes.txt</code> (file ન હોય તો બનાવે).</p>
<h4>vi ના modes</h4>
<ol>
<li><b>Command mode (normal mode):</b> vi શરૂ થાય ત્યારનો default mode. Keys commands તરીકે કામ કરે: cursor ખસેડવો, delete, copy, paste, undo.</li>
<li><b>Insert mode:</b> <code>i, a, o, I, A, O</code> થી પ્રવેશ; જે type કરો તે file માં ઉમેરાય. Command mode માં પાછા જવા <b>Esc</b> દબાવો.</li>
<li><b>Last-line (ex / command-line) mode:</b> command mode માં <code>:</code> type કરવાથી પ્રવેશ; save, quit, search-replace અને settings જેવા commands માટે cursor નીચેની line પર જાય. Enter command ચલાવે.</li>
</ol>
<h4>vi ના મહત્વના commands</h4>
""" + VI_GU + """
<p><b>સામાન્ય session:</b> <code>vi hello.sh</code> → <code>i</code> દબાવો → script type કરો → <b>Esc</b> → <code>:wq</code> → Enter.</p>""",
          diagram="os5_vi_modes"),
        T("5.3.2 gedit Editor", "5.3.2 gedit Editor",
          """<p><b>gedit</b> is the default <b>graphical (GUI) text editor</b> of the GNOME desktop (Ubuntu, Fedora). It is easy to use, like Notepad on Windows, with menus and mouse support.</p>
<ul>
<li>Start: <code>gedit file.txt &amp;</code> from the terminal (<code>&amp;</code> runs it in the background so the terminal remains free), or from the applications menu.</li>
<li>Features: syntax highlighting for C, Python, shell, HTML; line numbers; multiple tabs; search and replace (Ctrl+H); spell check; undo/redo; plugins.</li>
<li>Shortcuts: Ctrl+N new, Ctrl+O open, Ctrl+S save, Ctrl+Shift+S save as, Ctrl+F find, Ctrl+Q quit.</li>
</ul>
<h4>vi vs gedit</h4>
<ul><li>vi works in any terminal (also over SSH, without a GUI); gedit needs a graphical desktop.</li><li>vi is mode-based and keyboard-driven; gedit is modeless and mouse-friendly, easier for beginners.</li><li>Other editors: <b>nano</b> (simple terminal editor), emacs, VS Code.</li></ul>""",
          """<p><b>gedit</b> એ GNOME desktop (Ubuntu, Fedora) નો default <b>graphical (GUI) text editor</b> છે. તે Windows ના Notepad જેવો, menus અને mouse support સાથે, વાપરવામાં સરળ છે.</p>
<ul>
<li>શરૂ કરવા: terminal માંથી <code>gedit file.txt &amp;</code> (<code>&amp;</code> તેને background માં ચલાવે જેથી terminal મુક્ત રહે), અથવા applications menu માંથી.</li>
<li>Features: C, Python, shell, HTML માટે syntax highlighting; line numbers; ઘણી tabs; search અને replace (Ctrl+H); spell check; undo/redo; plugins.</li>
<li>Shortcuts: Ctrl+N new, Ctrl+O open, Ctrl+S save, Ctrl+Shift+S save as, Ctrl+F find, Ctrl+Q quit.</li>
</ul>
<h4>vi vs gedit</h4>
<ul><li>vi કોઈ પણ terminal માં (SSH પર, GUI વગર પણ) કામ કરે; gedit ને graphical desktop જોઈએ.</li><li>vi mode-based અને keyboard-driven છે; gedit modeless અને mouse-friendly છે, શરૂઆત કરનારા માટે સરળ.</li><li>બીજા editors: <b>nano</b> (સરળ terminal editor), emacs, VS Code.</li></ul>"""),
        T("5.3.3 Compiling C Programs with gcc", "5.3.3 gcc વડે C Programs Compile કરવા",
          """<p><b>gcc</b> (GNU Compiler Collection) is the standard compiler for C (and C++) on Linux. A C program is written with an editor (vi / gedit), compiled with gcc and run from the shell.</p>
<h4>Steps</h4>
<ol><li>Write the program: <code>vi hello.c</code> (or <code>gedit hello.c</code>).</li><li>Compile: <code>gcc hello.c</code> creates the executable <code>a.out</code>; <code>gcc hello.c -o hello</code> names it <code>hello</code>.</li><li>Run: <code>./a.out</code> or <code>./hello</code> (<code>./</code> because the current directory is not in PATH).</li><li>If there are errors, gcc shows the file name, line number and message; edit and compile again.</li></ol>
<h4>Stages of compilation</h4>
<ul><li><b>Preprocessing</b> (<code>gcc -E</code>): handles <code>#include</code> and <code>#define</code> → .i</li><li><b>Compilation</b> (<code>gcc -S</code>): C to assembly → .s</li><li><b>Assembly</b> (<code>gcc -c</code>): assembly to object code → .o</li><li><b>Linking</b>: joins object files and libraries (printf from libc) → executable</li></ul>
<h4>Useful options</h4>
<p><code>-o name</code> output file, <code>-Wall</code> show all warnings, <code>-g</code> debugging information (for gdb), <code>-lm</code> link the math library (for <code>sqrt</code>, <code>pow</code>), <code>-c</code> compile only.</p>
<h4>Example (real output)</h4>
""" + D.pre(D.GCC),
          """<p><b>gcc</b> (GNU Compiler Collection) એ Linux પર C (અને C++) માટેનો standard compiler છે. C program editor (vi / gedit) થી લખાય, gcc થી compile થાય અને shell માંથી ચલાવાય.</p>
<h4>પગલાં</h4>
<ol><li>Program લખો: <code>vi hello.c</code> (અથવા <code>gedit hello.c</code>).</li><li>Compile: <code>gcc hello.c</code> executable <code>a.out</code> બનાવે; <code>gcc hello.c -o hello</code> તેને <code>hello</code> નામ આપે.</li><li>ચલાવો: <code>./a.out</code> અથવા <code>./hello</code> (<code>./</code> કારણ કે current directory PATH માં નથી).</li><li>Errors હોય તો gcc file name, line number અને message બતાવે; સુધારી ફરી compile કરો.</li></ol>
<h4>Compilation ના તબક્કા</h4>
<ul><li><b>Preprocessing</b> (<code>gcc -E</code>): <code>#include</code> અને <code>#define</code> સંભાળે → .i</li><li><b>Compilation</b> (<code>gcc -S</code>): C થી assembly → .s</li><li><b>Assembly</b> (<code>gcc -c</code>): assembly થી object code → .o</li><li><b>Linking</b>: object files અને libraries (libc નું printf) જોડે → executable</li></ul>
<h4>ઉપયોગી options</h4>
<p><code>-o name</code> output file, <code>-Wall</code> બધી warnings, <code>-g</code> debugging માહિતી (gdb માટે), <code>-lm</code> math library link (<code>sqrt</code>, <code>pow</code> માટે), <code>-c</code> માત્ર compile.</p>
<h4>ઉદાહરણ (ખરું output)</h4>
""" + D.pre(D.GCC),
          diagram="os5_gcc"),
    ]}

SEC_5_4 = {
    "title": {"en": "5.4 Basic Shell Scripts", "gu": "5.4 Basic Shell Scripts"},
    "items": [
        TP("5.4.1 Shell Script Basics: Variables, echo, read", "5.4.1 Shell Script Basics: Variables, echo, read",
           """<p>A <b>shell script</b> is a text file containing a sequence of shell commands, along with variables, conditions and loops. It is used to automate repetitive tasks (backups, installations, reports).</p>
<h4>Writing and running a script</h4>
<ol><li>Create the file: <code>vi first.sh</code></li><li>First line <code>#!/bin/bash</code> (the <b>shebang</b>) tells which interpreter runs it; <code>#</code> starts a comment.</li><li>Run with <code>bash first.sh</code> or <code>sh first.sh</code>; or give execute permission <code>chmod +x first.sh</code> and run <code>./first.sh</code>.</li></ol>
""" + FIRST_CODE + """
<h4>Variables</h4>
<ul>
<li><b>User-defined:</b> <code>name=Ravi</code>, <code>n=10</code> (no spaces around <code>=</code>; no data types, all values are strings). Use with <code>$</code>: <code>echo $name</code> or <code>${name}</code>.</li>
<li><b>System (environment) variables:</b> <code>$HOME</code>, <code>$PATH</code>, <code>$USER</code>, <code>$SHELL</code>, <code>$PWD</code>.</li>
<li><code>readonly x</code> makes a constant; <code>unset x</code> removes a variable.</li>
</ul>
<h4>echo and read</h4>
<ul><li><code>echo "text $var"</code> prints; <code>-n</code> no newline; <code>-e</code> enables <code>\\n</code>, <code>\\t</code>.</li><li><code>read var</code> reads a line from the keyboard; <code>read a b c</code> reads several words; <code>read -p "Prompt: " x</code> shows a prompt.</li></ul>
<h4>Quotes and command substitution</h4>
<ul><li><code>"…"</code> double quotes: variables are expanded. <code>'…'</code> single quotes: everything literal. <code>\\</code> escapes one character.</li><li><code>today=$(date)</code> or <code>`date`</code> stores the output of a command.</li></ul>""",
           """<p><b>Shell script</b> એ variables, conditions અને loops સાથેના shell commands નો ક્રમ ધરાવતી text file છે. તેનો ઉપયોગ પુનરાવર્તિત કાર્યો (backups, installations, reports) automate કરવા થાય છે.</p>
<h4>Script લખવી અને ચલાવવી</h4>
<ol><li>File બનાવો: <code>vi first.sh</code></li><li>પહેલી line <code>#!/bin/bash</code> (<b>shebang</b>) કહે કે કયો interpreter ચલાવશે; <code>#</code> comment શરૂ કરે.</li><li><code>bash first.sh</code> અથવા <code>sh first.sh</code> થી ચલાવો; અથવા execute permission આપો <code>chmod +x first.sh</code> અને <code>./first.sh</code> ચલાવો.</li></ol>
""" + FIRST_CODE + """
<h4>Variables</h4>
<ul>
<li><b>User-defined:</b> <code>name=Ravi</code>, <code>n=10</code> (<code>=</code> ની આસપાસ spaces નહીં; data types નથી, બધી કિંમતો strings છે). <code>$</code> સાથે વાપરો: <code>echo $name</code> અથવા <code>${name}</code>.</li>
<li><b>System (environment) variables:</b> <code>$HOME</code>, <code>$PATH</code>, <code>$USER</code>, <code>$SHELL</code>, <code>$PWD</code>.</li>
<li><code>readonly x</code> constant બનાવે; <code>unset x</code> variable દૂર કરે.</li>
</ul>
<h4>echo અને read</h4>
<ul><li><code>echo "text $var"</code> છાપે; <code>-n</code> newline નહીં; <code>-e</code> <code>\\n</code>, <code>\\t</code> ચાલુ કરે.</li><li><code>read var</code> keyboard માંથી line વાંચે; <code>read a b c</code> ઘણા શબ્દો વાંચે; <code>read -p "Prompt: " x</code> prompt બતાવે.</li></ul>
<h4>Quotes અને command substitution</h4>
<ul><li><code>"…"</code> double quotes: variables expand થાય. <code>'…'</code> single quotes: બધું શાબ્દિક. <code>\\</code> એક અક્ષરને escape કરે.</li><li><code>today=$(date)</code> અથવા <code>`date`</code> command નું output રાખે.</li></ul>""",
           programs=["os5p2", "os5p4"]),
        TP("5.4.2 Reading Command-Line Arguments", "5.4.2 Command-Line Arguments વાંચવા",
           """<p>Values can be passed to a script on the command line after its name: <code>bash add.sh 40 60</code>. Inside the script they are available as <b>positional parameters</b>.</p>
""" + ARGS_EN + """
<h4>Points to remember</h4>
<ul>
<li>Always check <code>$#</code> and print a usage message if the arguments are missing.</li>
<li><code>shift</code> shifts the arguments left: <code>$2</code> becomes <code>$1</code>, and <code>$#</code> decreases by 1 (useful in loops).</li>
<li><code>set a b c</code> sets the positional parameters inside a script.</li>
<li><code>exit 0</code> ends the script successfully; a non-zero value indicates an error (seen by the caller in <code>$?</code>).</li>
</ul>""",
           """<p>Script ના નામ પછી command line પર કિંમતો આપી શકાય: <code>bash add.sh 40 60</code>. Script ની અંદર તે <b>positional parameters</b> તરીકે મળે છે.</p>
""" + ARGS_GU + """
<h4>યાદ રાખવાના મુદ્દા</h4>
<ul>
<li>હંમેશા <code>$#</code> તપાસો અને arguments ખૂટતા હોય તો usage message છાપો.</li>
<li><code>shift</code> arguments ને ડાબે ખસેડે: <code>$2</code> એ <code>$1</code> બને, અને <code>$#</code> 1 ઘટે (loops માં ઉપયોગી).</li>
<li><code>set a b c</code> script ની અંદર positional parameters set કરે.</li>
<li><code>exit 0</code> script ને સફળતાપૂર્વક પૂરી કરે; non-zero કિંમત error દર્શાવે (caller ને <code>$?</code> માં દેખાય).</li>
</ul>""",
           programs=["os5p1", "os5p6", "os5p18"]),
        TP("5.4.3 Arithmetic, Relational and Logical Operators", "5.4.3 Arithmetic, Relational અને Logical Operators",
           """<p>Shell variables hold strings, so arithmetic must be done with <code>expr</code>, <code>$(( ))</code> or <code>let</code>. Only <b>integer</b> arithmetic is supported (use <code>bc</code> for decimals: <code>echo "5/2" | bc -l</code>).</p>
<h4>Arithmetic operators</h4>
""" + ARITH_EN + """
<p>With <code>expr</code>, spaces around operators are required and <code>*</code> must be escaped (<code>\\*</code>).</p>
<h4>Relational operators (for numbers)</h4>
""" + REL_EN + """
<p>Inside <code>(( ))</code> the C-style operators <code>== != &gt; &gt;= &lt; &lt;=</code> can be used: <code>if (( a &gt; b ))</code>.</p>
<h4>Logical operators</h4>
""" + LOG_EN,
           """<p>Shell variables strings રાખે છે, તેથી arithmetic <code>expr</code>, <code>$(( ))</code> કે <code>let</code> થી કરવું પડે. માત્ર <b>integer</b> arithmetic support છે (decimals માટે <code>bc</code>: <code>echo "5/2" | bc -l</code>).</p>
<h4>Arithmetic operators</h4>
""" + ARITH_GU + """
<p><code>expr</code> સાથે operators ની આસપાસ spaces જરૂરી અને <code>*</code> ને escape (<code>\\*</code>) કરવો પડે.</p>
<h4>Relational operators (સંખ્યાઓ માટે)</h4>
""" + REL_GU + """
<p><code>(( ))</code> ની અંદર C-style operators <code>== != &gt; &gt;= &lt; &lt;=</code> વાપરી શકાય: <code>if (( a &gt; b ))</code>.</p>
<h4>Logical operators</h4>
""" + LOG_GU,
           programs=["os5p5", "os5p7", "os5p8"]),
        TP("5.4.4 Evaluating Expressions with the test Command", "5.4.4 test Command વડે Expressions મૂલવવા",
           """<p>The <b>test</b> command evaluates a condition and returns an <b>exit status</b>: <b>0 (true)</b> if the condition holds and <b>1 (false)</b> otherwise. It prints nothing; it is used with <code>if</code>, <code>while</code>, <code>&amp;&amp;</code> and <code>||</code>.</p>
<p>Two equivalent forms: <code>test $a -gt $b</code> and <code>[ $a -gt $b ]</code>. In the bracket form, <b>spaces after <code>[</code> and before <code>]</code> are compulsory</b>. bash also has <code>[[ … ]]</code>, which allows <code>&amp;&amp;</code>, <code>||</code> and pattern matching inside.</p>
<h4>Types of tests</h4>
""" + TEST_EN + """
<h4>Examples</h4>
<ul>
<li><code>test -f notes.txt &amp;&amp; echo "exists"</code></li>
<li><code>[ "$ans" = "yes" ]</code> (quote variables so an empty value does not cause an error)</li>
<li><code>[ -d backup ] || mkdir backup</code></li>
<li><code>test 5 -eq 5; echo $?</code> prints 0 (true).</li>
</ul>""",
           """<p><b>test</b> command શરત મૂલવે છે અને <b>exit status</b> આપે છે: શરત સાચી હોય તો <b>0 (true)</b> અને નહીં તો <b>1 (false)</b>. તે કંઈ છાપતું નથી; તે <code>if</code>, <code>while</code>, <code>&amp;&amp;</code> અને <code>||</code> સાથે વપરાય છે.</p>
<p>બે સરખા સ્વરૂપ: <code>test $a -gt $b</code> અને <code>[ $a -gt $b ]</code>. Bracket સ્વરૂપમાં <b><code>[</code> પછી અને <code>]</code> પહેલાં spaces ફરજિયાત</b> છે. bash માં <code>[[ … ]]</code> પણ છે, જે અંદર <code>&amp;&amp;</code>, <code>||</code> અને pattern matching મંજૂર કરે છે.</p>
<h4>Tests ના પ્રકારો</h4>
""" + TEST_GU + """
<h4>ઉદાહરણો</h4>
<ul>
<li><code>test -f notes.txt &amp;&amp; echo "exists"</code></li>
<li><code>[ "$ans" = "yes" ]</code> (variables ને quote કરો જેથી ખાલી કિંમતથી error ન આવે)</li>
<li><code>[ -d backup ] || mkdir backup</code></li>
<li><code>test 5 -eq 5; echo $?</code> 0 (true) છાપે.</li>
</ul>""",
           programs=["os5p11", "os5p12"]),
        TP("5.4.5 Branching: if, if...else, if...elif", "5.4.5 Branching: if, if...else, if...elif",
           """<p>The <b>if</b> statement executes commands depending on the exit status of a condition (usually a <code>test</code>). If the status is 0 (true), the <code>then</code> part runs.</p>
<h4>Forms</h4>
<ul><li><b>Simple if:</b> run commands only when the condition is true.</li><li><b>if-else:</b> choose between two blocks.</li><li><b>if-elif-else (ladder):</b> test several conditions in turn; the first true block runs.</li><li><b>Nested if:</b> an if inside another if.</li></ul>
""" + IF_CODE + """
<h4>Rules</h4>
<ul><li><code>then</code> must be on a new line or after <code>;</code>.</li><li>Every <code>if</code> ends with <code>fi</code> (if written backwards).</li><li>Spaces inside <code>[ ]</code> are required: <code>[ $a -gt $b ]</code>, not <code>[$a -gt $b]</code>.</li></ul>""",
           """<p><b>if</b> statement શરત (સામાન્ય રીતે <code>test</code>) ના exit status મુજબ commands ચલાવે છે. Status 0 (true) હોય તો <code>then</code> ભાગ ચાલે.</p>
<h4>સ્વરૂપો</h4>
<ul><li><b>Simple if:</b> શરત સાચી હોય ત્યારે જ commands ચલાવો.</li><li><b>if-else:</b> બે blocks માંથી એક પસંદ કરો.</li><li><b>if-elif-else (ladder):</b> ઘણી શરતો વારાફરતી તપાસો; પહેલો સાચો block ચાલે.</li><li><b>Nested if:</b> એક if ની અંદર બીજું if.</li></ul>
""" + IF_CODE + """
<h4>નિયમો</h4>
<ul><li><code>then</code> નવી line પર કે <code>;</code> પછી હોવું જોઈએ.</li><li>દરેક <code>if</code> <code>fi</code> (if ઊંધું) થી પૂરું થાય.</li><li><code>[ ]</code> ની અંદર spaces જરૂરી: <code>[ $a -gt $b ]</code>, <code>[$a -gt $b]</code> નહીં.</li></ul>""",
           diagram="os5_if", programs=["os5p9", "os5p10", "os5p3"]),
        TP("5.4.6 Branching: case Statement", "5.4.6 Branching: case Statement",
           """<p>The <b>case</b> statement is a multi-way branch, a cleaner alternative to a long if-elif ladder when one value is compared with many patterns (menus, choices).</p>
""" + CASE_CODE + """
<h4>Working</h4>
<ul>
<li>The value of <code>$var</code> is compared with each pattern from top to bottom.</li>
<li>The commands of the <b>first matching</b> pattern run up to <code>;;</code>, then control goes to <code>esac</code>.</li>
<li><code>*)</code> matches anything and acts as the <b>default</b>; it is written last.</li>
<li>Patterns may use wildcards: <code>[aeiou]</code>, <code>[0-9]</code>, <code>[a-z]*</code>, and <code>|</code> for alternatives (<code>y|Y|yes)</code>).</li>
<li>The statement ends with <code>esac</code> (case written backwards).</li>
</ul>""",
           """<p><b>case</b> statement multi-way branch છે; એક કિંમતને ઘણા patterns સાથે સરખાવવાની હોય (menus, choices) ત્યારે લાંબા if-elif ladder નો સ્વચ્છ વિકલ્પ છે.</p>
""" + CASE_CODE + """
<h4>કાર્યપદ્ધતિ</h4>
<ul>
<li><code>$var</code> ની કિંમત ઉપરથી નીચે દરેક pattern સાથે સરખાવાય.</li>
<li><b>પહેલા મેળ ખાતા</b> pattern ના commands <code>;;</code> સુધી ચાલે, પછી control <code>esac</code> પર જાય.</li>
<li><code>*)</code> કંઈ પણ સાથે મેળ ખાય અને <b>default</b> તરીકે કામ કરે; તે છેલ્લે લખાય.</li>
<li>Patterns માં wildcards વાપરી શકાય: <code>[aeiou]</code>, <code>[0-9]</code>, <code>[a-z]*</code>, અને વિકલ્પો માટે <code>|</code> (<code>y|Y|yes)</code>).</li>
<li>Statement <code>esac</code> (case ઊંધું) થી પૂરું થાય.</li>
</ul>""",
           diagram="os5_case", programs=["os5p13", "os5p14"]),
        TP("5.4.7 Looping: while Loop", "5.4.7 Looping: while Loop",
           """<p>A <b>loop</b> repeats a set of commands. The <b>while</b> loop repeats the body <b>as long as the condition is true</b> (exit status 0). It is used when the number of repetitions is not known in advance.</p>
""" + WHILE_CODE + """
<h4>Working</h4>
<ol><li>Initialise the loop variable (<code>i=1</code>).</li><li>Test the condition; if false, jump after <code>done</code>.</li><li>Execute the body between <code>do</code> and <code>done</code>.</li><li><b>Update</b> the variable (otherwise the loop never ends), then go back to step 2.</li></ol>
<h4>Loop control</h4>
<ul><li><code>break</code> exits the loop immediately; <code>continue</code> skips to the next iteration.</li><li><code>while true</code> or <code>while :</code> creates an infinite loop (stop with <code>break</code> or Ctrl+C).</li><li><code>while read line; do … done &lt; file</code> reads a file line by line.</li></ul>""",
           """<p><b>Loop</b> commands ના સમૂહને ફરી ફરી ચલાવે છે. <b>while</b> loop <b>શરત સાચી રહે ત્યાં સુધી</b> (exit status 0) body ફરી ચલાવે છે. પુનરાવર્તનોની સંખ્યા અગાઉથી ખબર ન હોય ત્યારે વપરાય.</p>
""" + WHILE_CODE + """
<h4>કાર્યપદ્ધતિ</h4>
<ol><li>Loop variable initialise કરો (<code>i=1</code>).</li><li>શરત તપાસો; ખોટી હોય તો <code>done</code> પછી જાઓ.</li><li><code>do</code> અને <code>done</code> વચ્ચેની body ચલાવો.</li><li>Variable <b>update</b> કરો (નહીં તો loop ક્યારેય પૂરો ન થાય), પછી step 2 પર પાછા.</li></ol>
<h4>Loop control</h4>
<ul><li><code>break</code> loop માંથી તરત બહાર નીકળે; <code>continue</code> આગળના iteration પર જાય.</li><li><code>while true</code> અથવા <code>while :</code> infinite loop બનાવે (<code>break</code> કે Ctrl+C થી બંધ).</li><li><code>while read line; do … done &lt; file</code> file ને line દર line વાંચે.</li></ul>""",
           diagram="os5_while", programs=["os5p15", "os5p16"]),
        TP("5.4.8 Looping: for Loop", "5.4.8 Looping: for Loop",
           """<p>The <b>for</b> loop executes the body <b>once for each item in a list</b>; the loop variable takes the items one by one. It is used when the items (or the count) are known.</p>
""" + FOR_CODE + """
<h4>Working</h4>
<ol><li>The first item of the list is assigned to the variable.</li><li>The body between <code>do</code> and <code>done</code> runs.</li><li>The next item is assigned and the body runs again, until the list is finished.</li></ol>
<h4>while vs for</h4>
<ul><li><b>while</b>: condition-controlled; the variable must be updated by the programmer.</li><li><b>for</b>: list-controlled; the shell assigns each item automatically.</li><li>Both support <code>break</code> and <code>continue</code> and end with <code>done</code>.</li></ul>""",
           """<p><b>for</b> loop <b>યાદીની દરેક item માટે એક વાર</b> body ચલાવે છે; loop variable items ને એક પછી એક લે છે. Items (કે સંખ્યા) ખબર હોય ત્યારે વપરાય.</p>
""" + FOR_CODE + """
<h4>કાર્યપદ્ધતિ</h4>
<ol><li>યાદીની પહેલી item variable ને અપાય.</li><li><code>do</code> અને <code>done</code> વચ્ચેની body ચાલે.</li><li>આગળની item અપાય અને body ફરી ચાલે, યાદી પૂરી થાય ત્યાં સુધી.</li></ol>
<h4>while vs for</h4>
<ul><li><b>while</b>: condition-controlled; variable programmer એ update કરવો પડે.</li><li><b>for</b>: list-controlled; shell દરેક item આપમેળે આપે.</li><li>બંને <code>break</code> અને <code>continue</code> support કરે અને <code>done</code> થી પૂરા થાય.</li></ul>""",
           diagram="os5_for", programs=["os5p17"]),
    ]}
