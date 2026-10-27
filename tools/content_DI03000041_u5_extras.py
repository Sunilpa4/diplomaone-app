"""Fundamentals of Operating System (DI03000041) - Unit 5 extras: syntax quick reference, viva, exam questions."""
from content_DI03000011_u1_extras import V, X


def S(name_en, name_gu, f, terms_en, terms_gu):
    f = f.strip("\n")
    for ln in f.splitlines():
        assert len(ln) <= 43, ln
    return {"name": {"en": name_en, "gu": name_gu}, "f": f, "terms": {"en": terms_en, "gu": terms_gu}}


def G(en, gu, items):
    return {"title": {"en": en, "gu": gu}, "items": items}


SYNTAX = [
    G("Directory Commands", "Directory Commands", [
        S("pwd – print working directory", "pwd – current directory બતાવો", "pwd", "Shows the absolute path of the current directory, e.g. /home/student.", "Current directory નો absolute path બતાવે, દા.ત. /home/student."),
        S("cd – change directory", "cd – directory બદલો", "cd dir     cd ..     cd /\ncd ~      cd -      cd", "<code>..</code> parent, <code>~</code> or plain <code>cd</code> home, <code>-</code> previous directory.", "<code>..</code> parent, <code>~</code> અથવા માત્ર <code>cd</code> home, <code>-</code> પાછલી directory."),
        S("mkdir – make directory", "mkdir – directory બનાવો", "mkdir dir1 dir2\nmkdir -p a/b/c", "<code>-p</code> creates parent directories as needed (no error if they exist).", "<code>-p</code> જરૂર મુજબ parent directories બનાવે (હોય તો error નહીં)."),
        S("rmdir – remove empty directory", "rmdir – ખાલી directory દૂર કરો", "rmdir dir\nrmdir -p a/b/c", "Works only on <b>empty</b> directories; use <code>rm -r</code> for non-empty ones.", "માત્ર <b>ખાલી</b> directories પર કામ કરે; ખાલી ન હોય તો <code>rm -r</code> વાપરો."),
        S("ls – list directory contents", "ls – directory contents ની યાદી", "ls [-l -a -R -t -r -i -h] [path]", "<code>-l</code> long, <code>-a</code> all incl. hidden, <code>-R</code> recursive, <code>-t</code> by time, <code>-r</code> reverse, <code>-i</code> inode, <code>-h</code> human sizes.", "<code>-l</code> long, <code>-a</code> hidden સહિત બધું, <code>-R</code> recursive, <code>-t</code> time મુજબ, <code>-r</code> reverse, <code>-i</code> inode, <code>-h</code> human sizes."),
    ]),
    G("File Commands", "File Commands", [
        S("cat – display / create / join files", "cat – files બતાવો / બનાવો / જોડો", "cat file\ncat > newfile    (Ctrl+D ends)\ncat f1 f2 > f3\ncat f1 >> f2\ncat -n file", "<code>&gt;</code> creates/overwrites, <code>&gt;&gt;</code> appends, <code>-n</code> numbers lines.", "<code>&gt;</code> બનાવે/overwrite કરે, <code>&gt;&gt;</code> append કરે, <code>-n</code> lines ને નંબર આપે."),
        S("cp – copy", "cp – copy", "cp src dest\ncp f1 f2 dir/\ncp -r dir1 dir2\ncp -i src dest", "<code>-r</code> recursive (directories), <code>-i</code> ask before overwrite, <code>-v</code> verbose.", "<code>-r</code> recursive (directories), <code>-i</code> overwrite પહેલાં પૂછે, <code>-v</code> verbose."),
        S("rm – remove files", "rm – files દૂર કરો", "rm file\nrm -i file\nrm -r dir\nrm -f file", "<code>-r</code> directory and its contents, <code>-i</code> confirm, <code>-f</code> force. Deleted files cannot be recovered.", "<code>-r</code> directory અને તેની સામગ્રી, <code>-i</code> ખાતરી, <code>-f</code> force. Delete થયેલી files પાછી મળતી નથી."),
        S("mv – move / rename", "mv – move / rename", "mv old new\nmv file dir/\nmv -i src dest", "Renames if the destination is a new name in the same directory; moves if it is a directory.", "Destination એ જ directory માં નવું નામ હોય તો rename; directory હોય તો move."),
    ]),
    G("Text Processing Commands", "Text Processing Commands", [
        S("wc – word count", "wc – word count", "wc file\nwc -l file   wc -w   wc -c", "Prints lines, words and bytes (characters). <code>-l</code> lines, <code>-w</code> words, <code>-c</code> bytes.", "Lines, words અને bytes (characters) છાપે. <code>-l</code> lines, <code>-w</code> words, <code>-c</code> bytes."),
        S("split – split a file", "split – file ને ભાગમાં વહેંચો", "split -l 4 file part_\nsplit -b 1k file part_", "Creates part_aa, part_ab, … Default: 1000 lines per piece. <code>-b</code> by size.", "part_aa, part_ab, … બનાવે. Default: ભાગ દીઠ 1000 lines. <code>-b</code> size મુજબ."),
        S("head – first lines", "head – શરૂઆતની lines", "head file\nhead -n 5 file   (or head -5)", "Default first 10 lines.", "Default પહેલી 10 lines."),
        S("tail – last lines", "tail – છેલ્લી lines", "tail file\ntail -n 3 file\ntail -n +5 file\ntail -f log.txt", "Default last 10 lines; <code>+5</code> from line 5; <code>-f</code> follow a growing file.", "Default છેલ્લી 10 lines; <code>+5</code> line 5 થી; <code>-f</code> વધતી file ને follow કરે."),
        S("grep – search a pattern", "grep – pattern શોધો", "grep pattern file\ngrep -i -v -c -n -l pat files\ngrep '^A' file   grep 'x$' file", "<code>-i</code> ignore case, <code>-v</code> non-matching lines, <code>-c</code> count, <code>-n</code> line numbers, <code>-l</code> file names. <code>^</code> start, <code>$</code> end of line.", "<code>-i</code> case અવગણો, <code>-v</code> મેળ ન ખાતી lines, <code>-c</code> count, <code>-n</code> line numbers, <code>-l</code> file names. <code>^</code> શરૂઆત, <code>$</code> line નો અંત."),
        S("sort – sort lines", "sort – lines ને sort કરો", "sort file\nsort -r -n -u file\nsort -k3 -n file\nsort file -o out", "<code>-r</code> reverse, <code>-n</code> numeric, <code>-u</code> unique, <code>-k</code> by field, <code>-t</code> field separator, <code>-o</code> output file.", "<code>-r</code> reverse, <code>-n</code> numeric, <code>-u</code> unique, <code>-k</code> field મુજબ, <code>-t</code> field separator, <code>-o</code> output file."),
    ]),
    G("Comparison Commands", "Comparison Commands", [
        S("cmp – compare byte by byte", "cmp – byte દર byte સરખામણી", "cmp file1 file2\ncmp -l file1 file2", "Reports the first differing byte and line; no output if identical (exit status 0).", "પહેલો જુદો byte અને line જણાવે; સરખી હોય તો output નહીં (exit status 0)."),
        S("comm – common lines (sorted files)", "comm – common lines (sorted files)", "comm f1 f2\ncomm -12 f1 f2", "Three columns: only in f1, only in f2, in both. <code>-1 -2 -3</code> hide a column.", "ત્રણ columns: માત્ર f1 માં, માત્ર f2 માં, બંનેમાં. <code>-1 -2 -3</code> column છુપાવે."),
        S("diff – differences", "diff – તફાવતો", "diff f1 f2\ndiff -i -w f1 f2", "Shows changes to make f1 same as f2: <code>a</code> add, <code>c</code> change, <code>d</code> delete; <code>&lt;</code> f1 lines, <code>&gt;</code> f2 lines.", "f1 ને f2 જેવી બનાવવા ફેરફારો બતાવે: <code>a</code> add, <code>c</code> change, <code>d</code> delete; <code>&lt;</code> f1 ની lines, <code>&gt;</code> f2 ની lines."),
    ]),
    G("Editors and gcc", "Editors અને gcc", [
        S("vi / vim – open a file", "vi / vim – file ખોલો", "vi file      vim file\nvi +10 file", "Opens in command mode; <code>+10</code> starts at line 10.", "Command mode માં ખૂલે; <code>+10</code> line 10 થી શરૂ."),
        S("vi – insert and save", "vi – insert અને save", "i a o I A O   insert\nEsc           command mode\n:w  :q  :wq  :q!  ZZ", "<code>i</code> before cursor, <code>a</code> after, <code>o</code> new line below; <code>:q!</code> quit without saving.", "<code>i</code> cursor પહેલાં, <code>a</code> પછી, <code>o</code> નીચે નવી line; <code>:q!</code> save કર્યા વગર quit."),
        S("vi – edit commands", "vi – edit commands", "x  dd  3dd  yy  p  u  .\n/word  n   :%s/old/new/g\nh j k l  gg  G  :set nu", "x delete char, dd delete line, yy copy, p paste, u undo, / search, :%s replace all, :set nu line numbers.", "x અક્ષર delete, dd line delete, yy copy, p paste, u undo, / search, :%s બધે replace, :set nu line numbers."),
        S("gedit – GUI editor", "gedit – GUI editor", "gedit file &", "Graphical text editor of GNOME; <code>&amp;</code> runs it in the background.", "GNOME નો graphical text editor; <code>&amp;</code> તેને background માં ચલાવે."),
        S("gcc – compile C", "gcc – C compile કરો", "gcc prog.c          (a.out)\ngcc prog.c -o prog\n./prog\ngcc -Wall prog.c -lm", "<code>-o</code> output name, <code>-Wall</code> all warnings, <code>-lm</code> link math library, <code>-c</code> object only.", "<code>-o</code> output નામ, <code>-Wall</code> બધી warnings, <code>-lm</code> math library link, <code>-c</code> માત્ર object."),
    ]),
    G("Shell Script Constructs", "Shell Script Constructs", [
        S("Run a script", "Script ચલાવો", "bash file.sh   sh file.sh\nchmod +x file.sh; ./file.sh", "First line <code>#!/bin/bash</code> (shebang) selects the interpreter.", "પહેલી line <code>#!/bin/bash</code> (shebang) interpreter પસંદ કરે."),
        S("Variables, echo, read", "Variables, echo, read", "name=Ravi      (no spaces)\necho \"Hi $name\"\nread a b\nx=$(command)   x=`command`", "No spaces around <code>=</code>. Double quotes expand variables, single quotes do not.", "<code>=</code> ની આસપાસ spaces નહીં. Double quotes variables expand કરે, single quotes નહીં."),
        S("Command-line arguments", "Command-line arguments", "$0 $1 … $9 ${10}\n$#  $@  $*  $?  $$", "$0 script name, $# count, $@ all args, $? exit status of last command, $$ PID.", "$0 script નામ, $# સંખ્યા, $@ બધા args, $? છેલ્લા command નો exit status, $$ PID."),
        S("Arithmetic", "Arithmetic", "expr $a + $b   expr $a \\* $b\n$((a + b))   let c=a*b", "Operators + - * / % (and ** in $(( ))). expr needs spaces and \\*.", "Operators + - * / % (અને $(( )) માં **). expr ને spaces અને \\* જોઈએ."),
        S("Relational (numbers)", "Relational (numbers)", "-eq -ne -gt -ge -lt -le\n[ $a -gt $b ]", "Equal, not equal, greater, greater-or-equal, less, less-or-equal.", "Equal, not equal, greater, greater-or-equal, less, less-or-equal."),
        S("Logical and string tests", "Logical અને string tests", "[ c1 -a c2 ]  [ c1 -o c2 ]  [ ! c ]\n[ c1 ] && [ c2 ]   [ c1 ] || [ c2 ]\n[ \"$s\" = \"x\" ]  != -z -n", "-a AND, -o OR, ! NOT; = equal, != not equal, -z empty, -n not empty.", "-a AND, -o OR, ! NOT; = equal, != not equal, -z empty, -n not empty."),
        S("test – file tests", "test – file tests", "test -f file   [ -f file ]\n-e -f -d -r -w -x -s", "exists, regular file, directory, readable, writable, executable, size &gt; 0. Spaces inside [ ] are required.", "exists, regular file, directory, readable, writable, executable, size &gt; 0. [ ] ની અંદર spaces જરૂરી."),
        S("if / if-else / if-elif", "if / if-else / if-elif", "if [ cond ]\nthen\n  cmds\nelif [ cond2 ]\nthen\n  cmds\nelse\n  cmds\nfi", "<code>elif</code> and <code>else</code> are optional; ends with <code>fi</code>.", "<code>elif</code> અને <code>else</code> વૈકલ્પિક; <code>fi</code> થી પૂરું."),
        S("case", "case", "case $var in\n  pat1) cmds ;;\n  a|b)  cmds ;;\n  *)    cmds ;;\nesac", "Each block ends with <code>;;</code>; <code>*)</code> default; ends with <code>esac</code>.", "દરેક block <code>;;</code> થી પૂરો; <code>*)</code> default; <code>esac</code> થી પૂરું."),
        S("while loop", "while loop", "while [ cond ]\ndo\n  cmds\ndone", "Repeats while the condition is true. <code>until</code> repeats while it is false.", "શરત સાચી હોય ત્યાં સુધી ફરે. <code>until</code> ખોટી હોય ત્યાં સુધી ફરે."),
        S("for loop", "for loop", "for i in 1 2 3\ndo\n  cmds\ndone\nfor ((i=1; i<=5; i++))", "List may be words, {1..10}, $(seq 1 10), *.c or \"$@\". break / continue control the loop.", "યાદી શબ્દો, {1..10}, $(seq 1 10), *.c કે \"$@\" હોઈ શકે. break / continue loop ને નિયંત્રિત કરે."),
    ]),
]

VIVA = [
    G("Linux Basics", "Linux Basics", [
        V("What is Linux?", "Linux શું છે?", "A free, open-source, Unix-like operating system kernel created by Linus Torvalds in 1991; with GNU tools it forms a complete OS.", "1991 માં Linus Torvalds એ બનાવેલું free, open-source, Unix-like operating system kernel; GNU tools સાથે સંપૂર્ણ OS બને છે."),
        V("Name some Linux distributions.", "કેટલાંક Linux distributions જણાવો.", "Ubuntu, Fedora, Debian, Linux Mint, Red Hat Enterprise Linux, Kali, Arch.", "Ubuntu, Fedora, Debian, Linux Mint, Red Hat Enterprise Linux, Kali, Arch."),
        V("What is the kernel?", "Kernel શું છે?", "The core of the OS that manages processes, memory, files and devices and talks directly to the hardware.", "OS નો મુખ્ય ભાગ જે processes, memory, files અને devices નું સંચાલન કરે છે અને hardware સાથે સીધો વાત કરે છે."),
        V("What is a shell?", "Shell શું છે?", "A command interpreter that reads user commands and asks the kernel to execute them (sh, bash, csh, ksh).", "Command interpreter જે user ના commands વાંચે છે અને kernel ને તેમને ચલાવવા કહે છે (sh, bash, csh, ksh)."),
        V("What is the root directory?", "Root directory શું છે?", "The top of the Linux file hierarchy, written as /. (root is also the name of the superuser.)", "Linux file hierarchy નું ટોચનું સ્થાન, / તરીકે લખાય. (root superuser નું નામ પણ છે.)"),
        V("What is a hidden file?", "Hidden file શું છે?", "A file whose name starts with a dot (e.g. .profile); shown only by ls -a.", "જેનું નામ dot થી શરૂ થાય તેવી file (દા.ત. .profile); માત્ર ls -a થી દેખાય."),
    ]),
    G("Commands", "Commands", [
        V("Difference between rmdir and rm -r?", "rmdir અને rm -r વચ્ચે તફાવત?", "rmdir removes only an empty directory; rm -r removes a directory with all its contents.", "rmdir માત્ર ખાલી directory દૂર કરે; rm -r directory ને તેની બધી સામગ્રી સાથે દૂર કરે."),
        V("Difference between > and >>?", "> અને >> વચ્ચે તફાવત?", "> redirects output to a file, overwriting it; >> appends to the end of the file.", "> output ને file માં redirect કરી overwrite કરે; >> file ના અંતે append કરે."),
        V("What is a pipe?", "Pipe શું છે?", "The | symbol sends the output of one command as input to the next, e.g. ls | wc -l.", "| ચિહ્ન એક command નું output આગળના command ને input તરીકે મોકલે, દા.ત. ls | wc -l."),
        V("Difference between cmp and diff?", "cmp અને diff વચ્ચે તફાવત?", "cmp reports the first differing byte; diff lists all line differences and how to change one file into the other.", "cmp પહેલો જુદો byte જણાવે; diff બધા line તફાવતો અને એક file ને બીજી જેવી કેવી રીતે બનાવવી તે બતાવે."),
        V("What does comm need and show?", "comm ને શું જોઈએ અને શું બતાવે?", "Two sorted files; it shows lines only in file 1, only in file 2, and common to both in three columns.", "બે sorted files; તે ત્રણ columns માં માત્ર file 1 માં, માત્ર file 2 માં અને બંનેમાં સામાન્ય lines બતાવે."),
        V("What does grep stand for?", "grep નું પૂરું નામ?", "Global Regular Expression Print: it prints lines that match a pattern.", "Global Regular Expression Print: pattern સાથે મેળ ખાતી lines છાપે."),
        V("How do you sort numerically in reverse?", "Numeric reverse sort કેવી રીતે કરશો?", "sort -nr file (use -k to choose a field).", "sort -nr file (field પસંદ કરવા -k વાપરો)."),
    ]),
    G("Editors and gcc", "Editors અને gcc", [
        V("What are the modes of vi?", "vi ના modes કયા છે?", "Command mode (default), insert mode (i, a, o) and last-line/ex mode (:).", "Command mode (default), insert mode (i, a, o) અને last-line/ex mode (:)."),
        V("How do you save and quit vi?", "vi માં save અને quit કેવી રીતે?", ":wq or ZZ; :q! quits without saving.", ":wq અથવા ZZ; :q! save કર્યા વગર quit કરે."),
        V("Difference between vi and vim?", "vi અને vim વચ્ચે તફાવત?", "vim (vi improved) adds syntax highlighting, multi-level undo, split windows and plugins.", "vim (vi improved) syntax highlighting, multi-level undo, split windows અને plugins ઉમેરે છે."),
        V("What is the default output file of gcc?", "gcc ની default output file કઈ?", "a.out; use -o name to choose another name.", "a.out; બીજું નામ આપવા -o name વાપરો."),
    ]),
    G("Shell Scripts", "Shell Scripts", [
        V("What is a shell script?", "Shell script શું છે?", "A text file containing a sequence of shell commands with variables, conditions and loops, executed by the shell.", "Variables, conditions અને loops સાથેના shell commands નો ક્રમ ધરાવતી text file, જે shell ચલાવે છે."),
        V("What is the shebang line?", "Shebang line શું છે?", "The first line #!/bin/bash, telling the system which interpreter runs the script.", "પહેલી line #!/bin/bash, જે system ને કહે કે કયો interpreter script ચલાવશે."),
        V("What are $#, $@ and $?", "$#, $@ અને $? શું છે?", "$# number of arguments, $@ all arguments, $? exit status of the last command (0 = success).", "$# arguments ની સંખ્યા, $@ બધા arguments, $? છેલ્લા command નો exit status (0 = success)."),
        V("Why is * escaped in expr?", "expr માં * ને escape શા માટે કરાય?", "Otherwise the shell expands * to the list of file names before expr sees it.", "નહીં તો expr સુધી પહોંચે તે પહેલાં shell * ને file names ની યાદીમાં ફેરવી દે."),
        V("What is the test command?", "test command શું છે?", "It evaluates an expression (numeric, string or file test) and returns exit status 0 for true; [ ] is its short form.", "તે expression (numeric, string કે file test) મૂલવે છે અને સાચું હોય તો exit status 0 આપે; [ ] તેનું ટૂંકું સ્વરૂપ છે."),
        V("How do you end if, case, while and for?", "if, case, while અને for કેવી રીતે પૂરા કરશો?", "if … fi, case … esac, while … do … done, for … do … done.", "if … fi, case … esac, while … do … done, for … do … done."),
    ]),
]

EXAM_QS = [
    X("Explain the architecture of the Unix/Linux operating system.", "Unix/Linux operating system નું architecture સમજાવો.", 4),
    X("Explain the features of Linux.", "Linux ના features સમજાવો.", 3),
    X("Explain the Linux directory structure (file hierarchy).", "Linux directory structure (file hierarchy) સમજાવો.", 3),
    X("What is a shell? Explain types of shells and how a command is executed.", "Shell શું છે? Shells ના પ્રકારો અને command કેવી રીતે ચાલે છે તે સમજાવો.", 4),
    X("Explain pwd, cd, mkdir, rmdir and ls commands with examples.", "pwd, cd, mkdir, rmdir અને ls commands ઉદાહરણ સાથે સમજાવો.", 4),
    X("Explain cat, cp, rm and mv commands with options.", "cat, cp, rm અને mv commands options સાથે સમજાવો.", 4),
    X("Explain wc, split, head and tail commands.", "wc, split, head અને tail commands સમજાવો.", 4),
    X("Explain cmp, comm and diff commands with examples.", "cmp, comm અને diff commands ઉદાહરણ સાથે સમજાવો.", 4),
    X("Explain grep and sort commands with options.", "grep અને sort commands options સાથે સમજાવો.", 4),
    X("Explain the modes of the vi editor and its important commands.", "vi editor ના modes અને તેના મહત્વના commands સમજાવો.", 4),
    X("How is a C program compiled and executed in Linux using gcc?", "Linux માં gcc વડે C program કેવી રીતે compile અને execute થાય છે?", 3),
    X("Explain command-line arguments in shell scripts with an example.", "Shell scripts માં command-line arguments ઉદાહરણ સાથે સમજાવો.", 3),
    X("Explain arithmetic, relational and logical operators in shell script.", "Shell script માં arithmetic, relational અને logical operators સમજાવો.", 4),
    X("Explain the test command with numeric, string and file tests.", "Numeric, string અને file tests સાથે test command સમજાવો.", 4),
    X("Explain if, if-else and case statements with examples.", "if, if-else અને case statements ઉદાહરણ સાથે સમજાવો.", 7),
    X("Explain while and for loops with examples.", "while અને for loops ઉદાહરણ સાથે સમજાવો.", 4),
    X("Write a shell script to add two numbers.", "બે સંખ્યાઓ ઉમેરવા shell script લખો.", 3),
    X("Write a shell script to convert a lower-case string to upper case.", "Lower-case string ને upper case માં ફેરવવા shell script લખો.", 3),
    X("Write a shell script to display a file and append it to another file.", "File બતાવવા અને બીજી file માં append કરવા shell script લખો.", 4),
]
