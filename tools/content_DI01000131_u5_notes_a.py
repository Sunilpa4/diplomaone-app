"""DI01000131 Unit 5 notes part A: 5.1 Character arrays and strings (incl. command line arguments)."""
from c_content import make_TE

SN = {
    "decl_syn": r'''
char string_name[size];
''',
    "decl_ex": r'''
char name[20];      /* up to 19 chars + '\0' */
char city[30];
char line[81];      /* one 80-column line */
''',
    "init_forms": r'''
char s1[10] = "GTU";             /* rest filled with '\0' */
char s2[]   = "GTU";             /* size 4 decided by compiler */
char s3[4]  = {'G','T','U','\0'};
char s4[]   = {'G','T','U','\0'};
char s5[3]  = "GTU";             /* no room for '\0' – avoid */
''',
    "init_error": r'''
char s[10];
s = "GTU";                       /* ERROR: array cannot be assigned */
strcpy(s, "GTU");                /* correct way */
''',
    "read_scanf": r'''
char name[20];
scanf("%s", name);               /* no & : name is an address */
scanf("%19s", name);             /* width limit: safer */
''',
    "read_scanset": r'''
scanf("%[^\n]", line);           /* read till newline */
scanf("%[a-z]", word);           /* only lowercase letters */
''',
    "read_getchar": r'''
char line[81], ch;
int i = 0;
while ((ch = getchar()) != '\n' && i < 80)
    line[i++] = ch;
line[i] = '\0';                  /* must terminate */
''',
    "read_fgets": r'''
fgets(line, sizeof(line), stdin);
line[strcspn(line, "\n")] = '\0';  /* remove '\n' */
''',
    "write_printf": r'''
char s[] = "Diploma";
printf("%s\n", s);       /* Diploma      */
printf("%10s|\n", s);    /*    Diploma|  */
printf("%-10s|\n", s);   /* Diploma   |  */
printf("%.3s\n", s);     /* Dip          */
printf("%10.3s|\n", s);  /*        Dip|  */
''',
    "write_puts": r'''
puts(s);                 /* prints s + newline */
for (i = 0; s[i] != '\0'; i++)
    putchar(s[i]);       /* char by char */
''',
    "char_arith": r'''
char ch = 'A';
printf("%d", ch);        /* 65 : ASCII value */
ch = ch + 1;             /* 'B' */
ch = 'a' - 32;           /* 'A' : lower -> upper */
int d = '7' - '0';       /* 7   : digit char -> number */
if (ch >= 'A' && ch <= 'Z')
    printf("Uppercase");
''',
    "atoi_ex": r'''
#include <stdlib.h>
int  n = atoi("125");    /* 125   */
float f = atof("3.14");  /* 3.14  */
long l = atol("70000");  /* 70000 */
''',
    "func_ex": r'''
char a[30] = "Good", b[] = "Day";
strlen(a);               /* 4               */
strcpy(a, "Hi");         /* a = "Hi"        */
strcat(a, b);            /* a = "HiDay"     */
strcmp("abc", "abd");    /* negative        */
strncpy(a, "Hello", 3);  /* first 3 chars   */
strncat(a, "World", 2);  /* append 2 chars  */
strchr("hello", 'l');    /* -> "llo"        */
strstr("diploma", "lom");/* -> "loma"       */
''',
    "cmp_use": r'''
if (strcmp(s1, s2) == 0)
    printf("Equal");
else if (strcmp(s1, s2) < 0)
    printf("s1 comes first");
else
    printf("s2 comes first");
''',
    "cmp_wrong": r'''
if (s1 == s2)            /* WRONG: compares addresses */
''',
    "tbl_decl": r'''
char name[4][8] = {"Amit", "Riya", "Om", "Kavya"};
printf("%s", name[1]);     /* Riya */
printf("%c", name[1][0]);  /* R    */
''',
    "tbl_read": r'''
for (i = 0; i < n; i++)
    scanf("%19s", name[i]);
for (i = 0; i < n; i++)
    printf("%s\n", name[i]);
''',
    "tbl_ptr": r'''
char *day[] = {"Mon", "Tue", "Wed"};  /* ragged */
''',
    "cmd_syn": r'''
int main(int argc, char *argv[])
{
    ...
}
''',
    "cmd_ex": r'''
/* run as: ./marks Ravi 25 Surat */
argc    = 4
argv[0] = "./marks"
argv[1] = "Ravi"
argv[2] = "25"     /* a string! */
argv[3] = "Surat"
argv[4] = NULL
''',
}
T = make_TE(SN)

SEC_5_1 = {
    "title": {"en": "5.1 Character Arrays and Strings"},
    "items": [
        T("5.1.1 Introduction to Strings",
          r"""<p>A <b>string</b> is a sequence of characters treated as a single data item, e.g. "GTU", "Hello World". C has <b>no separate string data type</b>. A string is stored in a <b>character array</b> and always ends with the <b>null character</b> <code>'\0'</code> (ASCII value 0).</p>
<h4>Null character '\0'</h4>
<ul><li>It marks the <b>end of the string</b>. Functions like <code>printf("%s")</code>, <code>strlen()</code> and <code>strcpy()</code> stop when they reach it.</li>
<li>So a string of <i>n</i> characters needs an array of at least <b>n + 1</b> characters.</li>
<li>For <code>char s[10] = "GTU";</code>: <code>s[0]='G'</code>, <code>s[1]='T'</code>, <code>s[2]='U'</code>, <code>s[3]='\0'</code>; the remaining elements are unused (see diagram).</li></ul>
<h4>Character constant vs string constant</h4>
<table>
<tr><th>Character constant</th><th>String constant</th></tr>
<tr><td>Single quotes: <code>'A'</code></td><td>Double quotes: <code>"A"</code></td></tr>
<tr><td>One character</td><td>Zero or more characters + '\0'</td></tr>
<tr><td>Occupies 1 byte</td><td><code>"A"</code> occupies 2 bytes ('A' and '\0')</td></tr>
<tr><td>Has an integer (ASCII) value: 'A' = 65</td><td>Represents the address of its first character</td></tr>
</table>
<h4>Common operations on strings</h4>
<ul><li>Reading and writing strings</li>
<li>Combining strings (concatenation)</li>
<li>Copying one string to another</li>
<li>Comparing strings for equality or order</li>
<li>Finding the length, searching for a character or substring</li></ul>""",
          diagram="c5_string_memory"),

        T("5.1.2 Declaring and Initializing String Variables",
          r"""<h4>Declaration</h4>
@@decl_syn@@
<p>The <b>size</b> is the maximum number of characters <b>plus one</b> for <code>'\0'</code>.</p>
@@decl_ex@@
<h4>Initialization</h4>
<p>A character array can be initialized in two ways:</p>
<ol><li><b>With a string literal:</b> <code>char s[10] = "GTU";</code>. The compiler adds <code>'\0'</code> automatically.</li>
<li><b>Character by character:</b> <code>char s[] = {'G','T','U','\0'};</code>. Here <code>'\0'</code> must be written by hand.</li></ol>
@@init_forms@@
<ul><li>If the size is omitted, the compiler takes the size from the initializer ("GTU" → 4).</li>
<li>If the size is larger than needed, the remaining elements are filled with <code>'\0'</code>.</li>
<li>If the size is too small, there is no room for '\0'. The array is then not a proper string, and printing it may show garbage.</li></ul>
<h4>Assignment is not allowed</h4>
<p>An array name is a constant address, so a string cannot be assigned with <code>=</code> after declaration. Use <code>strcpy()</code> instead.</p>
@@init_error@@""",
          programs=["c5p1"]),

        T("5.1.3 Reading Strings from the Terminal",
          r"""<p>C offers several ways to read a string from the keyboard (see diagram):</p>
<h4>1. scanf() with %s</h4>
@@read_scanf@@
<ul><li>Reads characters until the first <b>white space</b> (space, tab, newline), so it reads only <b>one word</b>. For "Ravi Patel" it stores only "Ravi".</li>
<li>No <code>&amp;</code> is needed, because the array name is already the address.</li>
<li><code>'\0'</code> is added automatically. A width such as <code>%19s</code> prevents overflow.</li></ul>
<h4>2. scanf() with a scanset %[ ]</h4>
@@read_scanset@@
<p><code>%[^\n]</code> reads all characters <b>except</b> newline, so a full line with spaces is read.</p>
<h4>3. getchar() in a loop</h4>
@@read_getchar@@
<p>Reads one character at a time until Enter. The programmer must add <code>'\0'</code> at the end.</p>
<h4>4. gets() – unsafe</h4>
<p><code>gets(s)</code> reads a whole line, but it <b>does not check the array size</b>, so a long input can overwrite other memory (buffer overflow). It was <b>removed in C11</b> and should not be used.</p>
<h4>5. fgets() – recommended</h4>
@@read_fgets@@
<ul><li>Reads at most <code>size − 1</code> characters, so it is <b>safe</b>.</li>
<li>It keeps the <code>'\n'</code> in the string, so remove it if needed.</li></ul>
<table>
<tr><th>Method</th><th>Reads spaces?</th><th>Safe?</th><th>Keeps '\n'?</th></tr>
<tr><td>scanf("%s")</td><td>No</td><td>Only with width</td><td>No</td></tr>
<tr><td>scanf("%[^\n]")</td><td>Yes</td><td>Only with width</td><td>No</td></tr>
<tr><td>getchar() loop</td><td>Yes</td><td>Yes (if counted)</td><td>No</td></tr>
<tr><td>gets()</td><td>Yes</td><td><b>No</b></td><td>No</td></tr>
<tr><td>fgets()</td><td>Yes</td><td><b>Yes</b></td><td>Yes</td></tr>
</table>""",
          diagram="c5_read_methods", programs=["c5p2", "c5p4"]),

        T("5.1.4 Writing Strings to the Screen",
          r"""<h4>1. printf() with %s</h4>
<p>Prints characters until <code>'\0'</code>. A width and a precision can be given:</p>
@@write_printf@@
<ul><li><code>%ws</code>: right-justified in a field of w columns.</li>
<li><code>%-ws</code>: left-justified.</li>
<li><code>%.ns</code>: prints only the first n characters.</li></ul>
<h4>2. puts() and putchar()</h4>
@@write_puts@@
<ul><li><code>puts(s)</code> prints the string and <b>automatically adds a newline</b>.</li>
<li><code>putchar(ch)</code> prints one character; in a loop it can print a string character by character.</li></ul>""",
          programs=["c5p1"]),

        T("5.1.5 Arithmetic Operations on Characters",
          r"""<p>In C every character is stored as its <b>integer ASCII code</b>, so characters can be used in arithmetic and comparisons. Useful codes: 'A'–'Z' = 65–90, 'a'–'z' = 97–122, '0'–'9' = 48–57.</p>
@@char_arith@@
<ul><li><b>Case conversion:</b> lowercase = uppercase + 32, so <code>ch - 32</code> converts to uppercase and <code>ch + 32</code> to lowercase.</li>
<li><b>Digit to number:</b> <code>'7' - '0'</code> = 55 − 48 = 7.</li></ul>
<h4>Character functions &lt;ctype.h&gt;</h4>
<table>
<tr><th>Function</th><th>Returns true (non-zero) if ch is…</th></tr>
<tr><td>isalpha(ch)</td><td>a letter</td></tr>
<tr><td>isdigit(ch)</td><td>a digit 0–9</td></tr>
<tr><td>isalnum(ch)</td><td>a letter or digit</td></tr>
<tr><td>isupper(ch) / islower(ch)</td><td>uppercase / lowercase</td></tr>
<tr><td>isspace(ch)</td><td>space, tab or newline</td></tr>
<tr><td>ispunct(ch)</td><td>a punctuation mark</td></tr>
<tr><td>toupper(ch) / tolower(ch)</td><td>(converts the case)</td></tr>
</table>
<h4>String to number &lt;stdlib.h&gt;</h4>
@@atoi_ex@@
<p><code>atoi()</code> (ASCII to integer) is especially useful with command line arguments, which are always strings.</p>""",
          programs=["c5p3", "c5p9"]),

        T("5.1.6 String-handling Functions (string.h)",
          r"""<p>The C library provides ready-made functions for strings in <code>&lt;string.h&gt;</code> (see diagram).</p>
<table>
<tr><th>Function</th><th>Purpose</th><th>Example / result</th></tr>
<tr><td><b>strlen(s)</b></td><td>Number of characters (without '\0')</td><td>strlen("Hello") → 5</td></tr>
<tr><td><b>strcpy(d, s)</b></td><td>Copies s into d</td><td>d = "Hello"</td></tr>
<tr><td><b>strncpy(d, s, n)</b></td><td>Copies first n characters</td><td>may not add '\0'</td></tr>
<tr><td><b>strcat(s1, s2)</b></td><td>Appends s2 to the end of s1</td><td>"Good"+"Day" → "GoodDay"</td></tr>
<tr><td><b>strncat(s1, s2, n)</b></td><td>Appends first n characters of s2</td><td></td></tr>
<tr><td><b>strcmp(s1, s2)</b></td><td>Compares two strings</td><td>0 / &lt;0 / &gt;0</td></tr>
<tr><td><b>strncmp(s1, s2, n)</b></td><td>Compares first n characters</td><td></td></tr>
<tr><td><b>strchr(s, ch)</b></td><td>Pointer to first occurrence of ch</td><td>NULL if not found</td></tr>
<tr><td><b>strrchr(s, ch)</b></td><td>Pointer to last occurrence of ch</td><td></td></tr>
<tr><td><b>strstr(s1, s2)</b></td><td>Pointer to first occurrence of s2 in s1</td><td>NULL if not found</td></tr>
</table>
@@func_ex@@
<h4>Important points</h4>
<ul><li>The destination of <code>strcpy</code>/<code>strcat</code> must be <b>large enough</b>; C does not check it.</li>
<li><code>strrev()</code>, <code>strupr()</code>, <code>strlwr()</code> and <code>stricmp()</code> exist in Turbo C but are <b>not standard C</b>. In exams, write your own logic (programs c5p7 and c5p9).</li>
<li><code>strlen</code> returns a <code>size_t</code> value, printed with <code>%zu</code> (or cast to int and use <code>%d</code>).</li></ul>""",
          diagram="c5_str_funcs", programs=["c5p5", "c5p8"]),

        T("5.1.7 Comparison of Strings – strcmp()",
          r"""<p><code>strcmp(s1, s2)</code> compares two strings <b>character by character</b> using their ASCII values until the characters differ or <code>'\0'</code> is reached (see diagram).</p>
<table>
<tr><th>Return value</th><th>Meaning</th><th>Example</th></tr>
<tr><td>0</td><td>s1 and s2 are equal</td><td>strcmp("GTU", "GTU")</td></tr>
<tr><td>&lt; 0</td><td>s1 comes before s2 (dictionary order)</td><td>strcmp("Apple", "Apply")</td></tr>
<tr><td>&gt; 0</td><td>s1 comes after s2</td><td>strcmp("Cat", "Bat")</td></tr>
</table>
<p>For "Apple" and "Apply": the first four characters match; then 'e' (101) − 'y' (121) = −20, so the result is negative.</p>
@@cmp_use@@
<ul><li>The comparison is <b>case-sensitive</b>: 'Z' (90) &lt; 'a' (97), so "Zebra" comes before "apple".</li>
<li>Strings must <b>not</b> be compared with <code>==</code>, which compares the addresses of the arrays, not their contents:</li></ul>
@@cmp_wrong@@
<p>strcmp() is used for checking passwords, searching names and sorting strings alphabetically.</p>""",
          diagram="c5_strcmp", programs=["c5p6", "c5p7"]),

        T("5.1.8 Table of Strings (Array of Strings)",
          r"""<p>A list of strings, such as names of students or days, is stored in a <b>two-dimensional character array</b>. Each <b>row</b> holds one string (see diagram).</p>
<p><code>char name[rows][columns];</code>: rows = number of strings; columns = maximum length + 1.</p>
@@tbl_decl@@
<ul><li><code>name[i]</code> is the address of row i, i.e. the i-th string, used with <code>%s</code>, <code>scanf</code>, <code>strcpy</code>, etc.</li>
<li><code>name[i][j]</code> is the j-th character of the i-th string.</li>
<li>Each row has the same fixed size, so short strings waste some memory.</li></ul>
<h4>Reading and printing a list</h4>
@@tbl_read@@
<h4>Array of pointers (alternative)</h4>
@@tbl_ptr@@
<p>Each element points to a string literal of its own length, so memory is not wasted. These literals should not be modified.</p>
<p>A common use is sorting names alphabetically with <code>strcmp()</code> and <code>strcpy()</code> (program c5p10).</p>""",
          diagram="c5_str_array", programs=["c5p10"]),

        T("5.1.9 Command Line Arguments",
          r"""<p><b>Command line arguments</b> are values passed to a program <b>when it is run</b> from the command prompt, after the program name. They let the user give input (file names, numbers, options) without the program asking for it.</p>
<h4>Syntax</h4>
@@cmd_syn@@
<ul><li><b>argc</b> (argument count): an int holding the number of arguments, <b>including the program name</b>. It is always at least 1.</li>
<li><b>argv</b> (argument vector): an array of character pointers (strings). <code>argv[0]</code> is the program name, <code>argv[1]</code> the first argument, …, and <code>argv[argc]</code> is NULL.</li></ul>
<h4>Example</h4>
@@cmd_ex@@
<ul><li>Arguments are separated by spaces. An argument containing spaces is enclosed in quotes: <code>"Ravi Patel"</code>.</li>
<li>All arguments are <b>strings</b>. Numbers must be converted with <code>atoi()</code>/<code>atof()</code>.</li>
<li>Check <code>argc</code> before using <code>argv</code>. If the arguments are missing, print a usage message.</li>
<li>Running: Linux <code>./marks Ravi 25 Surat</code>; Windows <code>marks Ravi 25 Surat</code>; Turbo C <i>Run → Arguments</i>; Code::Blocks <i>Project → Set program's arguments</i>.</li></ul>
<h4>Uses</h4>
<ul><li>Passing file names to file-copy or file-display programs (like the DOS <code>copy a.txt b.txt</code> command)</li>
<li>Giving numbers or options to a program in scripts</li></ul>""",
          diagram="c5_cmdline", programs=["c5p11", "c5p12", "c5p15"]),

        T("Key Points – 5.1",
          r"""<ul>
<li>A string is a character array terminated by <b>'\0'</b>; size needed = length + 1.</li>
<li><code>'A'</code> is a char (1 byte); <code>"A"</code> is a string (2 bytes).</li>
<li>Strings cannot be assigned with = or compared with ==; use <b>strcpy()</b> and <b>strcmp()</b>.</li>
<li><code>scanf("%s")</code> reads one word; <code>%[^\n]</code> and <code>fgets()</code> read a whole line; <code>gets()</code> is unsafe (removed in C11).</li>
<li><code>printf("%10.3s")</code>: width 10, first 3 characters; <code>puts()</code> adds a newline.</li>
<li>Characters are integers (ASCII): 'a' − 32 = 'A', '7' − '0' = 7; use the &lt;ctype.h&gt; functions.</li>
<li>string.h: strlen, strcpy, strncpy, strcat, strncat, strcmp, strncmp, strchr, strstr.</li>
<li>strcmp returns 0 (equal), &lt;0 (first is smaller), &gt;0 (first is larger).</li>
<li>Table of strings = 2-D char array <code>char s[rows][len+1]</code>; <code>s[i]</code> is the i-th string.</li>
<li><code>main(int argc, char *argv[])</code>: argc counts the arguments including the program name; argv[0] = program name; convert with atoi().</li>
</ul>""", key=True),
    ],
}

NOTES_A = [SEC_5_1]
