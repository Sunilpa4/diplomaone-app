"""Fundamentals of Operating System (DI03000041) - Unit 5 shell programs (run for real by sh_runner.py).
Practicals 9-12 plus scripts for operators, test, if, case, while and for."""
from sh_runner import run_script

MAXW = 43


def P(id_, title_en, title_gu, code, expl_en, expl_gu, inputs=(), args=(), files=None, name="script.sh", runs=None):
    code = code.strip("\n") + "\n"
    for ln in code.splitlines():
        assert len(ln) <= MAXW, f"{id_}: line too long ({len(ln)}): {ln}"
    outs = []
    for r in (runs or [dict(inputs=inputs, args=args)]):
        o, _ = run_script(code, r.get("inputs", ()), r.get("args", ()), files, name)
        outs.append(o)
    out = "\n\n".join(outs)
    assert "command not found" not in out and "syntax error" not in out, (id_, out)
    return {"id": id_, "title": {"en": title_en, "gu": title_gu}, "code": {"en": code.rstrip("\n"), "gu": code.rstrip("\n")},
            "out": out, "expl": {"en": expl_en, "gu": expl_gu}}


PROGRAMS = [
    P("os5p1", "Practical 9: Print Hello using a command-line argument", "Practical 9: Command-line argument વડે Hello છાપો", r'''
#!/bin/bash
# Practical 9: read a name from the
# command line and print Hello
if [ $# -eq 0 ]
then
  echo "Usage: bash hello.sh <name>"
  exit 1
fi
echo "Hello"
echo "Hello, $1! Welcome to Linux."
echo "Script name : $0"
echo "No. of args : $#"
''', "<p><code>$1</code> is the first command-line argument, <code>$#</code> the number of arguments and <code>$0</code> the script name. If no name is given, a usage message is printed and the script exits with status 1.</p>",
      "<p><code>$1</code> પહેલો command-line argument, <code>$#</code> arguments ની સંખ્યા અને <code>$0</code> script નું નામ છે. નામ ન આપ્યું હોય તો usage message છાપી script status 1 સાથે exit થાય છે.</p>",
      name="hello.sh", runs=[dict(args=("Ravi",)), dict(args=())]),

    P("os5p2", "Print Hello using read (keyboard input)", "read (keyboard input) વડે Hello છાપો", r'''
#!/bin/bash
echo -n "Enter your name: "
read name
echo "Hello, $name"
''', "<p><code>read name</code> waits for the user to type a line and stores it in the variable <code>name</code>. <code>echo -n</code> prints the prompt without a newline. A variable is used with <code>$</code>: <code>$name</code>.</p>",
      "<p><code>read name</code> user એક line type કરે તેની રાહ જુએ છે અને તેને variable <code>name</code> માં રાખે છે. <code>echo -n</code> newline વગર prompt છાપે છે. Variable ને <code>$</code> સાથે વાપરાય: <code>$name</code>.</p>",
      inputs=("Priya",)),

    P("os5p3", "Practical 10: Display a file and append it to another file", "Practical 10: File બતાવો અને બીજી file માં append કરો", r'''
#!/bin/bash
echo -n "Enter first file name: "
read f1
echo -n "Enter second file name: "
read f2
if [ ! -f "$f1" ]
then
  echo "$f1 does not exist"
  exit 1
fi
echo "--- Contents of $f1 ---"
cat "$f1"
cat "$f1" >> "$f2"
echo "--- $f2 after appending ---"
cat "$f2"
''', "<p><code>[ ! -f \"$f1\" ]</code> checks that the first file exists. <code>cat f1</code> displays it, and <code>cat f1 &gt;&gt; f2</code> <b>appends</b> it to the end of f2 (<code>&gt;</code> would overwrite f2).</p>",
      "<p><code>[ ! -f \"$f1\" ]</code> પહેલી file છે કે નહીં તે તપાસે છે. <code>cat f1</code> તેને બતાવે છે, અને <code>cat f1 &gt;&gt; f2</code> તેને f2 ના અંતે <b>append</b> કરે છે (<code>&gt;</code> f2 ને overwrite કરે).</p>",
      inputs=("a.txt", "b.txt"), files={"a.txt": "Operating System\nUnit 5: Linux\n", "b.txt": "GTU Diploma\n"}),

    P("os5p4", "Practical 11: Convert a lower-case string to upper case", "Practical 11: Lower-case string ને upper case માં ફેરવો", r'''
#!/bin/bash
echo -n "Enter a string in lower case: "
read str
up=$(echo "$str" | tr 'a-z' 'A-Z')
echo "Upper case : $up"
# bash 4+ shortcut
echo "Using \${str^^}: ${str^^}"
''', "<p><code>tr 'a-z' 'A-Z'</code> translates every lower-case letter to upper case. The output of the pipe is stored using <b>command substitution</b> <code>$( … )</code>. In bash 4+, <code>${str^^}</code> also converts to upper case (<code>${str,,}</code> to lower).</p>",
      "<p><code>tr 'a-z' 'A-Z'</code> દરેક lower-case અક્ષરને upper case માં ફેરવે છે. Pipe નું output <b>command substitution</b> <code>$( … )</code> વડે રખાય છે. bash 4+ માં <code>${str^^}</code> પણ upper case માં ફેરવે છે (<code>${str,,}</code> lower માં).</p>",
      inputs=("hello gtu students",)),

    P("os5p5", "Practical 12: Add two numbers", "Practical 12: બે સંખ્યાઓનો સરવાળો", r'''
#!/bin/bash
echo -n "Enter first number: "
read a
echo -n "Enter second number: "
read b
sum=`expr $a + $b`
echo "Sum using expr : $sum"
echo "Sum using \$(( )): $((a + b))"
''', "<p>Shell variables are strings, so arithmetic needs <code>expr</code> (spaces around <code>+</code> are required) or the arithmetic expansion <code>$(( ))</code>. Back-quotes <code>`…`</code> are the old form of command substitution.</p>",
      "<p>Shell variables strings છે, તેથી arithmetic માટે <code>expr</code> (<code>+</code> ની આસપાસ spaces જરૂરી) અથવા arithmetic expansion <code>$(( ))</code> જોઈએ. Back-quotes <code>`…`</code> command substitution નું જૂનું સ્વરૂપ છે.</p>",
      inputs=("25", "17")),

    P("os5p6", "Add two numbers given as command-line arguments", "Command-line arguments તરીકે આપેલી બે સંખ્યાઓનો સરવાળો", r'''
#!/bin/bash
if [ $# -ne 2 ]
then
  echo "Usage: bash add.sh num1 num2"
  exit 1
fi
echo "$1 + $2 = $(($1 + $2))"
''', "<p><code>[ $# -ne 2 ]</code> checks that exactly two arguments are given. <code>$1</code> and <code>$2</code> are the positional parameters.</p>",
      "<p><code>[ $# -ne 2 ]</code> બરાબર બે arguments આપ્યા છે કે નહીં તે તપાસે છે. <code>$1</code> અને <code>$2</code> positional parameters છે.</p>",
      name="add.sh", runs=[dict(args=("40", "60")), dict(args=("5",))]),

    P("os5p7", "Arithmetic operators", "Arithmetic operators", r'''
#!/bin/bash
a=17
b=5
echo "a + b = `expr $a + $b`"
echo "a - b = `expr $a - $b`"
echo "a * b = `expr $a \* $b`"
echo "a / b = `expr $a / $b`"
echo "a % b = `expr $a % $b`"
echo "a ** 2 = $((a ** 2))"
let c=a+b
echo "let c=a+b -> $c"
''', "<p>With <code>expr</code>, <code>*</code> must be escaped as <code>\\*</code> (otherwise the shell expands it to file names). Division is integer division: 17 / 5 = 3, remainder 2. <code>let</code> and <code>$(( ))</code> do not need spaces or escapes.</p>",
      "<p><code>expr</code> સાથે <code>*</code> ને <code>\\*</code> તરીકે escape કરવો પડે (નહીં તો shell તેને file names માં ફેરવે). Division integer division છે: 17 / 5 = 3, શેષ 2. <code>let</code> અને <code>$(( ))</code> ને spaces કે escapes ની જરૂર નથી.</p>"),

    P("os5p8", "Relational and logical operators (marks in range)", "Relational અને logical operators (marks range માં)", r'''
#!/bin/bash
echo -n "Enter marks (0-100): "
read m
if [ $m -ge 0 -a $m -le 100 ]
then
  echo "Valid marks"
else
  echo "Invalid marks"
fi
if [ $m -ge 35 ] && [ $m -le 100 ]
then
  echo "Result: PASS"
elif [ $m -ge 0 -a $m -lt 35 ]
then
  echo "Result: FAIL"
fi
''', "<p>Relational operators for numbers: <code>-eq -ne -gt -ge -lt -le</code>. Logical operators inside <code>[ ]</code>: <code>-a</code> (AND), <code>-o</code> (OR), <code>!</code> (NOT); between commands: <code>&amp;&amp;</code> and <code>||</code>.</p>",
      "<p>સંખ્યાઓ માટે relational operators: <code>-eq -ne -gt -ge -lt -le</code>. <code>[ ]</code> ની અંદર logical operators: <code>-a</code> (AND), <code>-o</code> (OR), <code>!</code> (NOT); commands વચ્ચે: <code>&amp;&amp;</code> અને <code>||</code>.</p>",
      runs=[dict(inputs=("72",)), dict(inputs=("20",)), dict(inputs=("150",))]),

    P("os5p9", "Even or odd (if-else)", "Even કે odd (if-else)", r'''
#!/bin/bash
echo -n "Enter a number: "
read n
if [ `expr $n % 2` -eq 0 ]
then
  echo "$n is even"
else
  echo "$n is odd"
fi
''', "<p>The remainder <code>n % 2</code> is 0 for even numbers. Note the required spaces inside <code>[ … ]</code> and the closing <code>fi</code>.</p>",
      "<p>Even સંખ્યા માટે શેષ <code>n % 2</code> 0 હોય છે. <code>[ … ]</code> ની અંદર જરૂરી spaces અને અંતે <code>fi</code> નોંધો.</p>",
      runs=[dict(inputs=("14",)), dict(inputs=("7",))]),

    P("os5p10", "Largest of three numbers (if-elif-else)", "ત્રણ સંખ્યાઓમાં સૌથી મોટી (if-elif-else)", r'''
#!/bin/bash
echo -n "Enter three numbers: "
read a b c
if [ $a -ge $b -a $a -ge $c ]
then
  echo "Largest = $a"
elif [ $b -ge $c ]
then
  echo "Largest = $b"
else
  echo "Largest = $c"
fi
''', "<p><code>read a b c</code> splits one input line into three variables. The <code>if … elif … else … fi</code> ladder tests the conditions one after another.</p>",
      "<p><code>read a b c</code> એક input line ને ત્રણ variables માં વહેંચે છે. <code>if … elif … else … fi</code> ladder conditions એક પછી એક તપાસે છે.</p>",
      inputs=("45 82 19",)),

    P("os5p11", "File test operators using test", "test વડે file test operators", r'''
#!/bin/bash
for f in notes.txt os missing.txt
do
  if test -f $f
  then
    echo "$f : regular file"
  elif test -d $f
  then
    echo "$f : directory"
  else
    echo "$f : does not exist"
  fi
done
f=notes.txt
[ -r $f ] && echo "$f is readable"
[ -s $f ] && echo "$f is not empty"
''', "<p><code>test expr</code> and <code>[ expr ]</code> are the same. File tests: <code>-e</code> exists, <code>-f</code> regular file, <code>-d</code> directory, <code>-r -w -x</code> permissions, <code>-s</code> size &gt; 0.</p>",
      "<p><code>test expr</code> અને <code>[ expr ]</code> સરખા છે. File tests: <code>-e</code> exists, <code>-f</code> regular file, <code>-d</code> directory, <code>-r -w -x</code> permissions, <code>-s</code> size &gt; 0.</p>",
      files={"notes.txt": "Linux notes\n", "os/readme": "x\n"}),

    P("os5p12", "String comparison and length", "String comparison અને length", r'''
#!/bin/bash
echo -n "Enter password: "
read p
if [ -z "$p" ]
then
  echo "Empty password"
elif [ "$p" = "gtu123" ]
then
  echo "Login successful"
else
  echo "Wrong password"
fi
echo "Length of input = ${#p}"
''', "<p>String tests: <code>=</code> equal, <code>!=</code> not equal, <code>-z</code> empty, <code>-n</code> not empty. Always quote string variables (<code>\"$p\"</code>) so an empty value does not cause an error. <code>${#p}</code> gives the length.</p>",
      "<p>String tests: <code>=</code> equal, <code>!=</code> not equal, <code>-z</code> empty, <code>-n</code> not empty. String variables ને હંમેશા quote કરો (<code>\"$p\"</code>) જેથી ખાલી કિંમતથી error ન આવે. <code>${#p}</code> length આપે છે.</p>",
      runs=[dict(inputs=("gtu123",)), dict(inputs=("abc",))]),

    P("os5p13", "Menu-driven calculator (case)", "Menu-driven calculator (case)", r'''
#!/bin/bash
echo -n "Enter two numbers: "
read a b
echo "1.Add 2.Subtract 3.Multiply 4.Divide"
echo -n "Enter choice: "
read ch
case $ch in
  1) echo "Sum = $((a + b))" ;;
  2) echo "Difference = $((a - b))" ;;
  3) echo "Product = $((a * b))" ;;
  4) if [ $b -eq 0 ]; then
       echo "Cannot divide by zero"
     else
       echo "Quotient = $((a / b))"
     fi ;;
  *) echo "Invalid choice" ;;
esac
''', "<p><code>case</code> compares <code>$ch</code> with each pattern; the matching block runs until <code>;;</code>. <code>*)</code> is the default case. The statement ends with <code>esac</code>.</p>",
      "<p><code>case</code> <code>$ch</code> ને દરેક pattern સાથે સરખાવે છે; મેળ ખાતો block <code>;;</code> સુધી ચાલે છે. <code>*)</code> default case છે. Statement <code>esac</code> થી પૂરું થાય છે.</p>",
      runs=[dict(inputs=("20 4", "3")), dict(inputs=("20 0", "4"))]),

    P("os5p14", "Vowel or consonant (case with patterns)", "Vowel કે consonant (patterns સાથે case)", r'''
#!/bin/bash
echo -n "Enter a character: "
read c
case $c in
  [aeiouAEIOU]) echo "$c is a vowel" ;;
  [a-zA-Z]) echo "$c is a consonant" ;;
  [0-9]) echo "$c is a digit" ;;
  *) echo "$c is a special symbol" ;;
esac
''', "<p>case patterns can use wildcards: <code>[aeiou]</code> any one of the listed characters, <code>[a-z]</code> a range, <code>*</code> anything, and <code>|</code> for alternatives (<code>yes|y)</code>).</p>",
      "<p>case patterns માં wildcards વાપરી શકાય: <code>[aeiou]</code> યાદીમાંનો કોઈ એક અક્ષર, <code>[a-z]</code> range, <code>*</code> કંઈ પણ, અને વિકલ્પો માટે <code>|</code> (<code>yes|y)</code>).</p>",
      runs=[dict(inputs=("e",)), dict(inputs=("k",)), dict(inputs=("7",))]),

    P("os5p15", "Factorial of a number (while loop)", "સંખ્યાનો factorial (while loop)", r'''
#!/bin/bash
echo -n "Enter a number: "
read n
fact=1
i=1
while [ $i -le $n ]
do
  fact=`expr $fact \* $i`
  i=`expr $i + 1`
done
echo "Factorial of $n = $fact"
''', "<p>The <code>while</code> loop repeats the body between <code>do</code> and <code>done</code> as long as the condition is true. Here i goes from 1 to n and fact = 1 × 2 × … × n.</p>",
      "<p><code>while</code> loop શરત સાચી રહે ત્યાં સુધી <code>do</code> અને <code>done</code> વચ્ચેનો ભાગ ફરી ફરી ચલાવે છે. અહીં i 1 થી n સુધી જાય છે અને fact = 1 × 2 × … × n.</p>",
      inputs=("6",)),

    P("os5p16", "Sum of digits and reverse of a number (while)", "સંખ્યાના અંકોનો સરવાળો અને reverse (while)", r'''
#!/bin/bash
echo -n "Enter a number: "
read n
num=$n
sum=0
rev=0
while [ $n -gt 0 ]
do
  d=$((n % 10))
  sum=$((sum + d))
  rev=$((rev * 10 + d))
  n=$((n / 10))
done
echo "Sum of digits of $num = $sum"
echo "Reverse of $num = $rev"
''', "<p><code>n % 10</code> gives the last digit and <code>n / 10</code> removes it. The loop runs once per digit.</p>",
      "<p><code>n % 10</code> છેલ્લો અંક આપે છે અને <code>n / 10</code> તેને દૂર કરે છે. Loop દરેક અંક માટે એક વાર ચાલે છે.</p>",
      inputs=("4825",)),

    P("os5p17", "Multiplication table (for loop)", "ઘડિયો (for loop)", r'''
#!/bin/bash
echo -n "Enter a number: "
read n
for i in 1 2 3 4 5 6 7 8 9 10
do
  echo "$n x $i = $((n * i))"
done
''', "<p>The <code>for</code> loop takes each word of the list in turn into <code>i</code>. The list can also be <code>$(seq 1 10)</code>, <code>{1..10}</code>, file names (<code>*.c</code>) or <code>\"$@\"</code>.</p>",
      "<p><code>for</code> loop યાદીનો દરેક શબ્દ વારાફરતી <code>i</code> માં લે છે. યાદી <code>$(seq 1 10)</code>, <code>{1..10}</code>, file names (<code>*.c</code>) અથવા <code>\"$@\"</code> પણ હોઈ શકે.</p>",
      inputs=("7",)),

    P("os5p18", "Sum of all command-line arguments (for with $@)", "બધા command-line arguments નો સરવાળો ($@ સાથે for)", r'''
#!/bin/bash
sum=0
for x in "$@"
do
  sum=$((sum + x))
done
echo "Arguments : $@"
echo "Count     : $#"
echo "Sum       : $sum"
''', "<p><code>\"$@\"</code> expands to all arguments as separate words, so the loop visits each one. <code>$#</code> is their count.</p>",
      "<p><code>\"$@\"</code> બધા arguments ને અલગ શબ્દો તરીકે આપે છે, તેથી loop દરેકની મુલાકાત લે છે. <code>$#</code> તેમની સંખ્યા છે.</p>",
      name="sum.sh", args=("10", "20", "30", "40")),
]

if __name__ == "__main__":
    for p in PROGRAMS:
        print("=" * 10, p["id"], p["title"]["en"])
        print(p["out"])
