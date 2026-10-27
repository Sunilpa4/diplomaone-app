"""DI01000131 Unit 5 - solved C programs (strings, command line arguments, text files). English only; compiled & run with gcc."""
from c_content import PE


def CL(p, cmd):
    """Show the command line used to run a command-line-argument program."""
    import re
    prog = cmd.split()[0]
    p["out"] = "$ " + cmd + "\n" + re.sub(r"/tmp/\S+/p\b", prog, p["out"])
    return p


POEM = "Twinkle twinkle little star\nHow I wonder what you are\nUp above the world so high\nLike a diamond in the sky\n"
STORY = "I like tea in the morning.\nTea keeps me fresh.\nMy friend also likes tea.\n"

PROGRAMS = [
    PE("c5p1", "Declaring, initializing and printing strings", r'''
#include <stdio.h>
#include <string.h>

int main(void)
{
    char s1[10] = "GTU";                        // string literal
    char s2[]   = {'C', 'P', 'F', '\0'};        // char by char
    char s3[20] = "Diploma";
    int i;

    printf("s1 = %s\n", s1);
    printf("s2 = %s\n", s2);
    puts(s3);                                   // adds newline

    printf("Characters of s3: ");
    for (i = 0; s3[i] != '\0'; i++)             // loop till null
        printf("%c ", s3[i]);
    printf("\n");

    printf("strlen(s1) = %zu, sizeof(s1) = %zu\n", strlen(s1), sizeof(s1));
    printf("[%10s] [%-10s] [%.3s]\n", s3, s3, s3);
    return 0;
}
''', (),
       r"""<ul><li><code>"GTU"</code> automatically gets <code>'\0'</code> at the end. When initializing character by character, <code>'\0'</code> must be added by hand.</li>
<li><code>%s</code> prints characters until it reaches <code>'\0'</code>. <code>puts()</code> prints the string and a newline.</li>
<li>The loop <code>s3[i] != '\0'</code> is the standard way to process a string one character at a time.</li>
<li><code>strlen</code> gives the number of characters (3); <code>sizeof</code> gives the array size (10 bytes).</li>
<li><code>%10s</code> right-aligns in a width of 10, <code>%-10s</code> left-aligns, and <code>%.3s</code> prints only the first 3 characters.</li></ul>"""),

    PE("c5p2", "Reading strings: scanf %s, scanf %[^\\n] and fgets", r'''
#include <stdio.h>
#include <string.h>

int main(void)
{
    char first[20], city[30], addr[50];

    printf("Enter full name: ");
    scanf("%s", first);                     // stops at space
    printf("scanf %%s read      : %s\n", first);
    while (getchar() != '\n')               // discard rest of line
        ;

    printf("Enter city: ");
    scanf("%[^\n]", city);                  // reads till newline
    printf("scanf %%[^\\n] read  : %s\n", city);
    getchar();                              // remove the newline

    printf("Enter address: ");
    fgets(addr, sizeof(addr), stdin);       // safe, keeps '\n'
    addr[strcspn(addr, "\n")] = '\0';       // remove '\n'
    printf("fgets read         : %s\n", addr);
    return 0;
}
''', ["Ravi Patel", "Surat City", "12 Ring Road, Surat"],
       r"""<ul><li><code>scanf("%s", s)</code> reads only up to the first white space, so "Ravi Patel" gives only "Ravi". No <code>&amp;</code> is needed, because an array name is already an address.</li>
<li><code>scanf("%[^\n]", s)</code> (scanset) reads everything up to the newline, so spaces are included.</li>
<li><code>fgets(s, size, stdin)</code> reads a whole line <b>safely</b>: never more than size−1 characters. It keeps the <code>'\n'</code>, which is removed with <code>strcspn()</code>.</li>
<li><code>gets()</code> is not used because it does not check the size and was removed from C11.</li></ul>"""),

    PE("c5p3", "Count vowels, consonants, digits and spaces in a line", r'''
#include <stdio.h>
#include <ctype.h>

int main(void)
{
    char s[100];
    int i, v = 0, c = 0, d = 0, sp = 0;

    printf("Enter a line: ");
    fgets(s, sizeof(s), stdin);

    for (i = 0; s[i] != '\0'; i++)
    {
        char ch = tolower(s[i]);
        if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u')
            v++;
        else if (isalpha(ch))
            c++;
        else if (isdigit(ch))
            d++;
        else if (ch == ' ')
            sp++;
    }
    printf("Vowels = %d, Consonants = %d, Digits = %d, Spaces = %d\n", v, c, d, sp);
    return 0;
}
''', ["GTU Diploma Sem 1 exam in 2025"],
       r"""<p>Each character is checked using functions from <code>&lt;ctype.h&gt;</code>: <code>isalpha()</code> (letter), <code>isdigit()</code> (digit) and <code>tolower()</code> (convert to lowercase, so both 'A' and 'a' are counted). Other useful functions: <code>isupper()</code>, <code>islower()</code>, <code>isspace()</code>, <code>toupper()</code>.</p>"""),

    PE("c5p4", "String length with and without strlen()", r'''
#include <stdio.h>
#include <string.h>

int main(void)
{
    char s[50];
    int len = 0;

    printf("Enter a word: ");
    scanf("%49s", s);               // width limit avoids overflow

    while (s[len] != '\0')          // count until null character
        len++;

    printf("Length (loop)   = %d\n", len);
    printf("Length (strlen) = %zu\n", strlen(s));
    return 0;
}
''', ["Programming"],
       r"""<p>A string ends with <code>'\0'</code>, so its length is the number of characters before the null character. The loop counts them exactly as <code>strlen()</code> does. <code>%49s</code> limits input to 49 characters, leaving room for <code>'\0'</code> in the 50-byte array.</p>"""),

    PE("c5p5", "Demonstration of string-handling functions", r'''
#include <stdio.h>
#include <string.h>

int main(void)
{
    char a[40] = "Computer", b[20] = "Science", c[40];

    printf("strlen(a)       = %zu\n", strlen(a));

    strcpy(c, a);                       // c = "Computer"
    printf("strcpy(c, a)    : c = %s\n", c);

    strcat(c, " ");
    strcat(c, b);                       // join
    printf("strcat          : c = %s\n", c);

    printf("strcmp(a, b)    = %d\n", strcmp(a, b) < 0 ? -1 : 1);
    printf("strcmp(a, a)    = %d\n", strcmp(a, a));

    strncpy(c, a, 4);                   // copy first 4 chars
    c[4] = '\0';
    printf("strncpy(c, a, 4): c = %s\n", c);

    printf("strchr(a, 'p')  = %s\n", strchr(a, 'p'));
    printf("strstr(a, \"put\") = %s\n", strstr(a, "put"));
    return 0;
}
''', (),
       r"""<ul><li><code>strcpy(dest, src)</code> copies src into dest. <b>A string cannot be assigned with =</b> (<code>c = a;</code> is an error).</li>
<li><code>strcat(s1, s2)</code> appends s2 to s1. s1 must be large enough to hold both.</li>
<li><code>strcmp</code> returns 0 if the strings are equal; a negative value if s1 comes first in dictionary (ASCII) order; a positive value otherwise. The exact number depends on the compiler, so we only check the sign.</li>
<li><code>strncpy</code> copies at most n characters and may not add <code>'\0'</code>, so it is added by hand.</li>
<li><code>strchr</code> and <code>strstr</code> return a pointer to the first occurrence, which prints the rest of the string.</li></ul>"""),

    PE("c5p6", "Compare two strings (equal / alphabetical order)", r'''
#include <stdio.h>
#include <string.h>

int main(void)
{
    char s1[30], s2[30];
    int r;

    printf("Enter first string : ");
    scanf("%29s", s1);
    printf("Enter second string: ");
    scanf("%29s", s2);

    r = strcmp(s1, s2);
    if (r == 0)
        printf("Both strings are EQUAL\n");
    else if (r < 0)
        printf("\"%s\" comes before \"%s\"\n", s1, s2);
    else
        printf("\"%s\" comes after \"%s\"\n", s1, s2);
    return 0;
}
''', ["Apple", "Apply"],
       r"""<p><code>strcmp</code> compares character by character using ASCII values. The first difference is 'e' (101) and 'y' (121), so the result is negative and "Apple" comes first (see the diagram "How strcmp() Compares Two Strings"). Note that <code>s1 == s2</code> would compare <b>addresses</b>, not contents.</p>"""),

    PE("c5p7", "Reverse a string and check palindrome (without strrev)", r'''
#include <stdio.h>
#include <string.h>

int main(void)
{
    char s[50], r[50];
    int i, n;

    printf("Enter a string: ");
    scanf("%49s", s);

    n = strlen(s);
    for (i = 0; i < n; i++)
        r[i] = s[n - 1 - i];            // last char first
    r[n] = '\0';                        // terminate the copy

    printf("Reverse = %s\n", r);
    if (strcmp(s, r) == 0)
        printf("%s is a PALINDROME\n", s);
    else
        printf("%s is NOT a palindrome\n", s);
    return 0;
}
''', ["madam"],
       r"""<p>Characters are copied from the end of <code>s</code> to the start of <code>r</code>. After the loop, <code>r[n] = '\0'</code> must be added, otherwise r is not a valid string. A <b>palindrome</b> reads the same backwards (madam, level, racecar). <code>strrev()</code> exists only in Turbo C and is not part of standard C, so writing the logic yourself is preferred in exams.</p>"""),

    PE("c5p8", "User-defined versions of strcpy, strcat and strlen", r'''
#include <stdio.h>

int my_strlen(char s[]);
void my_strcpy(char d[], char s[]);
void my_strcat(char d[], char s[]);

int main(void)
{
    char a[40], b[] = "Engineering";

    my_strcpy(a, "Computer ");
    printf("After copy : %s\n", a);
    my_strcat(a, b);
    printf("After join : %s\n", a);
    printf("Length     : %d\n", my_strlen(a));
    return 0;
}

int my_strlen(char s[])
{
    int i = 0;
    while (s[i] != '\0')
        i++;
    return i;
}

void my_strcpy(char d[], char s[])
{
    int i = 0;
    while ((d[i] = s[i]) != '\0')       // copy including '\0'
        i++;
}

void my_strcat(char d[], char s[])
{
    int i = my_strlen(d), j = 0;        // start at end of d
    while (s[j] != '\0')
        d[i++] = s[j++];
    d[i] = '\0';
}
''', (),
       r"""<ul><li><b>Copy:</b> each character, including the final <code>'\0'</code>, is copied. The assignment inside the condition copies first, then tests.</li>
<li><b>Concatenate:</b> start writing at the position of <code>'\0'</code> in d (its length), copy s, then terminate.</li>
<li>Strings are passed to functions as character arrays, i.e. by address, so the changes to <code>d</code> are seen in main().</li></ul>"""),

    PE("c5p9", "Convert case and count words in a sentence", r'''
#include <stdio.h>
#include <ctype.h>

int main(void)
{
    char s[100];
    int i, words = 0, inword = 0;

    printf("Enter a sentence: ");
    fgets(s, sizeof(s), stdin);

    for (i = 0; s[i] != '\0'; i++)
    {
        if (isspace(s[i]))
            inword = 0;
        else if (!inword)               // start of a new word
        {
            inword = 1;
            words++;
        }
    }

    printf("Upper  : ");
    for (i = 0; s[i] != '\0'; i++) putchar(toupper(s[i]));
    printf("Lower  : ");
    for (i = 0; s[i] != '\0'; i++) putchar(tolower(s[i]));
    printf("Toggle : ");
    for (i = 0; s[i] != '\0'; i++)
        putchar(isupper(s[i]) ? tolower(s[i]) : toupper(s[i]));
    printf("Words  = %d\n", words);
    return 0;
}
''', ["Welcome To  GTU Diploma"],
       r"""<ul><li>Case conversion is done character by character with <code>toupper()</code> and <code>tolower()</code>. <code>strupr()</code>/<code>strlwr()</code> are Turbo C only.</li>
<li><b>Character arithmetic</b> gives the same result: <code>'a' - 32 = 'A'</code>, because lowercase letters are 32 more than uppercase in ASCII.</li>
<li>Word counting uses a flag <code>inword</code>: a word starts when a non-space character follows a space, so even double spaces are handled correctly.</li>
<li>The printed lines end with the newline that <code>fgets()</code> kept.</li></ul>"""),

    PE("c5p10", "Sort names in alphabetical order (array of strings)", r'''
#include <stdio.h>
#include <string.h>

int main(void)
{
    char name[10][20], temp[20];
    int n, i, j;

    printf("How many names? ");
    scanf("%d", &n);
    printf("Enter %d names:\n", n);
    for (i = 0; i < n; i++)
        scanf("%19s", name[i]);         // name[i] is a row (string)

    for (i = 0; i < n - 1; i++)         // bubble sort on strings
        for (j = 0; j < n - 1 - i; j++)
            if (strcmp(name[j], name[j + 1]) > 0)
            {
                strcpy(temp, name[j]);
                strcpy(name[j], name[j + 1]);
                strcpy(name[j + 1], temp);
            }

    printf("Sorted names:\n");
    for (i = 0; i < n; i++)
        printf("%d. %s\n", i + 1, name[i]);
    return 0;
}
''', ["5", "Riya", "Amit", "Kavya", "Om", "Dhruv"],
       r"""<ul><li><code>char name[10][20]</code> stores up to 10 names of up to 19 characters each; <code>name[i]</code> is the i-th string.</li>
<li>Strings are compared with <code>strcmp()</code> and swapped with <code>strcpy()</code> (not with = or &gt;).</li>
<li>The logic is the same bubble sort as for numbers in Unit 3.</li></ul>"""),

    CL(PE("c5p11", "Command line arguments: display argc and argv", r'''
#include <stdio.h>

int main(int argc, char *argv[])
{
    int i;

    printf("Number of arguments (argc) = %d\n", argc);
    for (i = 0; i < argc; i++)
        printf("argv[%d] = %s\n", i, argv[i]);
    return 0;
}
''', (), r"""<ul><li><b>Command line arguments</b> are values given after the program name when it is run from the command prompt.</li>
<li><code>argc</code> (argument count) = number of words including the program name, here 4.</li>
<li><code>argv</code> (argument vector) is an array of strings; <code>argv[0]</code> is the program name.</li>
<li>In Turbo C, run with <i>Run → Arguments</i>; in a terminal, type <code>./marks Ravi 25 Surat</code> (Linux) or <code>marks Ravi 25 Surat</code> (Windows).</li></ul>""",
        args=["Ravi", "25", "Surat"]), "./marks Ravi 25 Surat"),

    CL(PE("c5p12", "Sum of numbers passed as command line arguments", r'''
#include <stdio.h>
#include <stdlib.h>                     // atoi()

int main(int argc, char *argv[])
{
    int i, sum = 0;

    if (argc < 2)
    {
        printf("Usage: %s num1 num2 ...\n", argv[0]);
        return 1;
    }
    for (i = 1; i < argc; i++)          // skip argv[0]
        sum += atoi(argv[i]);           // string -> int

    printf("Sum of %d numbers = %d\n", argc - 1, sum);
    return 0;
}
''', (), r"""<p>All command line arguments arrive as <b>strings</b>, so "10" must be converted to the integer 10 with <code>atoi()</code> (or <code>atof()</code> for real numbers) from <code>&lt;stdlib.h&gt;</code>. The loop starts at 1 to skip the program name. If no numbers are given, a usage message is printed.</p>""",
        args=["10", "25", "40", "5"]), "./sum 10 25 40 5"),

    PE("c5p13", "Write to a text file and read it back (fputs, fprintf, fgets)", r'''
#include <stdio.h>

int main(void)
{
    FILE *fp;
    char line[100];

    fp = fopen("note.txt", "w");                // open for writing
    if (fp == NULL)
    {
        printf("Cannot create file\n");
        return 1;
    }
    printf("Enter a line: ");
    fgets(line, sizeof(line), stdin);
    fputs(line, fp);                            // write string
    fprintf(fp, "Written by C program, %d lines\n", 2);
    fclose(fp);                                 // save and close

    fp = fopen("note.txt", "r");                // open for reading
    if (fp == NULL)
    {
        printf("Cannot open file\n");
        return 1;
    }
    printf("--- Contents of note.txt ---\n");
    while (fgets(line, sizeof(line), fp) != NULL)
        printf("%s", line);
    fclose(fp);
    return 0;
}
''', ["C programming is fun"],
       r"""<ul><li><code>FILE *fp;</code> declares a <b>file pointer</b>. <code>fopen()</code> returns NULL if the file cannot be opened, so always check it.</li>
<li>Mode <code>"w"</code> creates the file, or erases it if it already exists. <code>fputs()</code> writes a string and <code>fprintf()</code> writes formatted text.</li>
<li><code>fclose()</code> writes any data left in the buffer to the disk and releases the file.</li>
<li>Mode <code>"r"</code> opens it for reading. <code>fgets()</code> returns NULL at end of file, which ends the loop.</li></ul>"""),

    PE("c5p14", "Count characters, words and lines in a file (fgetc)", r'''
#include <stdio.h>
#include <ctype.h>

int main(void)
{
    FILE *fp;
    int ch, chars = 0, words = 0, lines = 0, inword = 0;

    fp = fopen("poem.txt", "r");
    if (fp == NULL)
    {
        printf("File not found\n");
        return 1;
    }

    while ((ch = fgetc(fp)) != EOF)     // read till end of file
    {
        putchar(ch);                    // display the file
        chars++;
        if (ch == '\n')
            lines++;
        if (isspace(ch))
            inword = 0;
        else if (!inword)
        {
            inword = 1;
            words++;
        }
    }
    fclose(fp);

    printf("Characters = %d, Words = %d, Lines = %d\n", chars, words, lines);
    return 0;
}
''', (), r"""<ul><li><code>fgetc(fp)</code> reads one character from the file. At the end it returns <b>EOF</b> (End Of File, usually −1).</li>
<li><code>ch</code> is declared <b>int</b>, not char, so that EOF can be distinguished from a real character.</li>
<li>The file <code>poem.txt</code> had 4 lines of text. The character count includes the newline characters.</li></ul>""",
       files={"poem.txt": POEM}),

    CL(PE("c5p15", "Copy one file to another (file names from command line)", r'''
#include <stdio.h>

int main(int argc, char *argv[])
{
    FILE *fs, *ft;
    int ch;

    if (argc != 3)
    {
        printf("Usage: %s source target\n", argv[0]);
        return 1;
    }
    fs = fopen(argv[1], "r");
    if (fs == NULL)
    {
        printf("Cannot open %s\n", argv[1]);
        return 1;
    }
    ft = fopen(argv[2], "w");
    if (ft == NULL)
    {
        printf("Cannot create %s\n", argv[2]);
        fclose(fs);
        return 1;
    }

    while ((ch = fgetc(fs)) != EOF)     // copy char by char
        fputc(ch, ft);
    fclose(fs);
    fclose(ft);
    printf("%s copied to %s\n", argv[1], argv[2]);

    ft = fopen(argv[2], "r");           // show the copy
    printf("--- %s ---\n", argv[2]);
    while ((ch = fgetc(ft)) != EOF)
        putchar(ch);
    fclose(ft);
    return 0;
}
''', (), r"""<p>This combines <b>command line arguments</b> and <b>file handling</b> and follows the flowchart "Copy One File to Another". The source is opened in "r" mode and the target in "w" mode. Each character read with <code>fgetc()</code> is written with <code>fputc()</code> until EOF. Both files are closed, then the copy is opened again to show that it is identical.</p>""",
        args=["story.txt", "copy.txt"], files={"story.txt": STORY}), "./copy story.txt copy.txt"),

    PE("c5p16", "Student records with fprintf / fscanf and append mode", r'''
#include <stdio.h>

int main(void)
{
    FILE *fp;
    int n, i, roll, marks;
    char name[20];

    fp = fopen("students.txt", "w");
    if (fp == NULL) return 1;
    printf("How many students? ");
    scanf("%d", &n);
    for (i = 0; i < n; i++)
    {
        printf("Roll Name Marks: ");
        scanf("%d %19s %d", &roll, name, &marks);
        fprintf(fp, "%d %s %d\n", roll, name, marks);   // formatted write
    }
    fclose(fp);

    fp = fopen("students.txt", "a");                    // append mode
    fprintf(fp, "%d %s %d\n", 104, "Kavya", 91);
    fclose(fp);

    fp = fopen("students.txt", "r");
    printf("\n%-6s %-10s %s\n", "Roll", "Name", "Marks");
    while (fscanf(fp, "%d %19s %d", &roll, name, &marks) == 3)
        printf("%-6d %-10s %d\n", roll, name, marks);
    fclose(fp);
    return 0;
}
''', ["3", "101 Amit 78", "102 Riya 85", "103 Om 69"],
       r"""<ul><li><code>fprintf(fp, …)</code> works like printf but writes to the file. <code>fscanf(fp, …)</code> works like scanf but reads from the file.</li>
<li><code>fscanf()</code> returns the number of items read; the loop stops when it can no longer read 3 items (end of file).</li>
<li>Mode <code>"a"</code> (append) adds the new record at the <b>end</b> without erasing the existing data; mode "w" would have erased it.</li></ul>"""),

    PE("c5p17", "Find and replace a word in a file", r'''
#include <stdio.h>
#include <string.h>

void replace(char *line, char *find, char *rep, char *out);

int main(void)
{
    FILE *fin, *fout;
    char line[200], out[400], find[30], rep[30];
    int count = 0;

    printf("Word to find   : ");
    scanf("%29s", find);
    printf("Replace with   : ");
    scanf("%29s", rep);

    fin = fopen("story.txt", "r");
    fout = fopen("result.txt", "w");
    if (fin == NULL || fout == NULL)
    {
        printf("File error\n");
        return 1;
    }
    while (fgets(line, sizeof(line), fin) != NULL)
    {
        if (strstr(line, find) != NULL)
            count++;
        replace(line, find, rep, out);
        fputs(out, fout);
    }
    fclose(fin);
    fclose(fout);
    printf("Lines changed  : %d\n--- result.txt ---\n", count);

    fin = fopen("result.txt", "r");
    while (fgets(line, sizeof(line), fin) != NULL)
        printf("%s", line);
    fclose(fin);
    return 0;
}

void replace(char *line, char *find, char *rep, char *out)
{
    char *p = line, *q;
    int fl = strlen(find);

    out[0] = '\0';
    while ((q = strstr(p, find)) != NULL)   // next occurrence
    {
        strncat(out, p, q - p);             // text before word
        strcat(out, rep);                   // new word
        p = q + fl;                         // skip old word
    }
    strcat(out, p);                         // rest of line
}
''', ["tea", "coffee"],
       r"""<p>This is the GTU micro-project "find and replace in a file". Each line is read with <code>fgets()</code>. <code>strstr()</code> finds each occurrence of the word, and the new line is built in <code>out</code> using <code>strncat()</code> (the text before the word) and <code>strcat()</code> (the replacement). The result is written to a new file with <code>fputs()</code> and then displayed.</p>
<p><b>Note:</b> the search is case-sensitive, so "Tea" in line 2 is not changed. strstr() also matches inside longer words (e.g. "tea" inside "team"); a complete solution would also check word boundaries.</p>""",
       files={"story.txt": STORY}),
]

if __name__ == "__main__":
    for p in PROGRAMS:
        print("=" * 20, p["id"], p["title"]["en"]); print(p["out"])
