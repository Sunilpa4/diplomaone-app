"""DI01000131 Unit 5 notes part B: 5.2 File management in C (text mode)."""
from c_content import make_TE

SN = {
    "fp_decl": r'''
FILE *fp;                /* FILE is defined in stdio.h */
''',
    "fopen_syn": r'''
fp = fopen("filename", "mode");
''',
    "fopen_ex": r'''
FILE *fp;
fp = fopen("data.txt", "r");
if (fp == NULL)
{
    printf("Cannot open file\n");
    return 1;            /* or exit(1); */
}
''',
    "fclose_syn": r'''
fclose(fp);              /* returns 0 on success, EOF on error */
''',
    "fclose_ex": r'''
FILE *f1, *f2;
f1 = fopen("in.txt", "r");
f2 = fopen("out.txt", "w");
/* ... processing ... */
fclose(f1);
fclose(f2);
''',
    "fgetc_syn": r'''
int ch = fgetc(fp);      /* read one char; EOF at end */
fputc(ch, fp);           /* write one char */
''',
    "fgetc_ex": r'''
int ch;                  /* int, to hold EOF */
while ((ch = fgetc(fp)) != EOF)
    putchar(ch);         /* display whole file */
''',
    "fputc_ex": r'''
fp = fopen("a.txt", "w");
while ((ch = getchar()) != '\n')
    fputc(ch, fp);       /* keyboard -> file */
fclose(fp);
''',
    "fgets_syn": r'''
fgets(str, n, fp);       /* NULL at end of file */
fputs(str, fp);          /* returns EOF on error */
''',
    "fgets_ex": r'''
char line[100];
while (fgets(line, sizeof(line), fp) != NULL)
    printf("%s", line);  /* line by line */
''',
    "fputs_ex": r'''
fputs("GTU Diploma\n", fp);
fputs(name, fp);
''',
    "fprintf_syn": r'''
fprintf(fp, "control string", var1, var2, ...);
fscanf(fp, "control string", &var1, &var2, ...);
''',
    "fprintf_ex": r'''
fprintf(fp, "%d %s %.2f\n", roll, name, per);
''',
    "fscanf_ex": r'''
while (fscanf(fp, "%d %s %f", &roll, name, &per) == 3)
    printf("%d %s %.2f\n", roll, name, per);
''',
    "std_streams": r'''
fprintf(stdout, "Hello\n");   /* same as printf */
fprintf(stderr, "Error!\n");  /* error message  */
fscanf(stdin, "%d", &n);      /* same as scanf  */
''',
    "feof_ex": r'''
ch = fgetc(fp);
while (!feof(fp))        /* true after reading past end */
{
    putchar(ch);
    ch = fgetc(fp);
}
''',
    "err_ex": r'''
#include <stdlib.h>
fp = fopen(argv[1], "r");
if (fp == NULL)
{
    printf("Error: %s not found\n", argv[1]);
    exit(1);             /* end the program */
}
''',
    "steps": r'''
#include <stdio.h>
int main(void)
{
    FILE *fp;                         /* 1. declare */
    fp = fopen("demo.txt", "w");      /* 2. open    */
    if (fp == NULL) return 1;
    fprintf(fp, "Hello File\n");      /* 3. process */
    fclose(fp);                       /* 4. close   */
    return 0;
}
''',
}
T = make_TE(SN)

SEC_5_2 = {
    "title": {"en": "5.2 File Management in C (Text Files)"},
    "items": [
        T("5.2.1 Introduction to Files",
          r"""<p>A <b>file</b> is a named collection of related data stored <b>permanently</b> on a secondary storage device such as a hard disk or pen drive.</p>
<h4>Why files are needed</h4>
<ul><li>Variables and arrays are stored in RAM, so the data is <b>lost</b> when the program ends or the power goes off. Data in a file is <b>permanent</b>.</li>
<li>Large amounts of data can be stored and read again later, without typing them every time.</li>
<li>The output of one program can be used as the input of another.</li></ul>
<h4>Types of files</h4>
<table>
<tr><th>Text file</th><th>Binary file</th></tr>
<tr><td>Data stored as readable characters (ASCII)</td><td>Data stored in the same form as in memory (bytes)</td></tr>
<tr><td>Can be opened in Notepad</td><td>Not readable in a text editor</td></tr>
<tr><td>Lines end with a newline character</td><td>No line structure</td></tr>
<tr><td>e.g. .txt, .c, .csv</td><td>e.g. .exe, .jpg, .dat</td></tr>
<tr><td>Modes: "r", "w", "a"</td><td>Modes: "rb", "wb", "ab"</td></tr>
</table>
<p>The syllabus covers <b>text files</b> only.</p>
<h4>Basic file operations</h4>
<ol><li>Naming / creating a file</li><li>Opening a file</li><li>Reading data from a file</li><li>Writing data to a file</li><li>Closing a file</li></ol>
<h4>File pointer and buffer</h4>
<p>All file functions are declared in <code>&lt;stdio.h&gt;</code>. A file is accessed through a <b>file pointer</b>: a pointer to a structure of type <code>FILE</code>, which stores information about the file (name, current position, buffer, mode, etc.).</p>
@@fp_decl@@
<p>Data does not go directly between the program and the disk; it passes through a temporary memory area called the <b>buffer</b> (see diagram). The four steps of file handling are: declare → open → read/write → close.</p>
@@steps@@""",
          diagram="c5_file_io", programs=["c5p13"]),

        T("5.2.2 Opening a File – fopen() and File Modes",
          r"""<p><code>fopen()</code> opens a file in a given mode and returns a file pointer. If the file cannot be opened (file not found, no permission, disk full), it returns <b>NULL</b>.</p>
@@fopen_syn@@
<p>Both the file name and the mode are <b>strings</b> (double quotes). The file name may include a path, e.g. <code>"C:\\data\\marks.txt"</code>.</p>
<h4>File opening modes (text files)</h4>
<table>
<tr><th>Mode</th><th>Meaning</th><th>If file exists</th><th>If file does not exist</th></tr>
<tr><td><b>"r"</b></td><td>Read only</td><td>Opened; reading starts at the beginning</td><td>Returns NULL</td></tr>
<tr><td><b>"w"</b></td><td>Write only</td><td><b>Contents erased</b> (overwritten)</td><td>New file created</td></tr>
<tr><td><b>"a"</b></td><td>Append</td><td>Data added at the end</td><td>New file created</td></tr>
<tr><td><b>"r+"</b></td><td>Read and write</td><td>Opened from the beginning</td><td>Returns NULL</td></tr>
<tr><td><b>"w+"</b></td><td>Write and read</td><td>Contents erased</td><td>New file created</td></tr>
<tr><td><b>"a+"</b></td><td>Read and append</td><td>Read anywhere; write only at the end</td><td>New file created</td></tr>
</table>
<h4>Always check for NULL</h4>
@@fopen_ex@@
<p>Using a NULL file pointer in other file functions makes the program crash.</p>""",
          diagram="c5_file_modes", programs=["c5p13", "c5p16"]),

        T("5.2.3 Closing a File – fclose()",
          r"""<p>A file must be closed after its work is finished.</p>
@@fclose_syn@@
<h4>Why closing is necessary</h4>
<ul><li>It <b>flushes the buffer</b>: data still waiting in the buffer is written to the disk. Without fclose(), the last data may be lost.</li>
<li>It breaks the link between the file pointer and the file and releases the memory used.</li>
<li>Only a limited number of files can be open at the same time.</li>
<li>To change mode (e.g. after writing, to read the same file), close it and reopen it in the new mode.</li></ul>
@@fclose_ex@@
<p>All open files are closed automatically when the program ends normally, but it is good practice to close each file explicitly.</p>""",
          programs=["c5p13"]),

        T("5.2.4 Character I/O – fgetc() / fputc() and EOF",
          r"""@@fgetc_syn@@
<ul><li><code>fgetc(fp)</code> (also <code>getc(fp)</code>) reads the next character from the file and moves the position forward. At the end of the file it returns <b>EOF</b>.</li>
<li><code>fputc(ch, fp)</code> (also <code>putc(ch, fp)</code>) writes one character to the file.</li></ul>
<h4>EOF (End Of File)</h4>
<p><code>EOF</code> is a constant defined in stdio.h (usually <b>−1</b>), returned when there is no more data to read. The variable receiving fgetc() must be <b>int</b>, not char, so that EOF can be distinguished from a valid character.</p>
<h4>Reading a whole file</h4>
@@fgetc_ex@@
<h4>Writing from the keyboard to a file</h4>
@@fputc_ex@@
<h4>feof()</h4>
<p><code>feof(fp)</code> returns non-zero (true) once an attempt has been made to read <b>past</b> the end of the file:</p>
@@feof_ex@@
<p>Character I/O is used for copying files and counting characters, words and lines (see the flowchart "Copy One File to Another").</p>""",
          diagram="c5_fc_copy", programs=["c5p14", "c5p15"]),

        T("5.2.5 String I/O – fgets() / fputs()",
          r"""@@fgets_syn@@
<ul><li><code>fgets(str, n, fp)</code> reads a line from the file into str. It stops after a newline, after n−1 characters, or at the end of the file. The newline is kept and <code>'\0'</code> is added. It returns <b>NULL</b> at the end of the file.</li>
<li><code>fputs(str, fp)</code> writes the string to the file. Unlike <code>puts()</code>, it does <b>not</b> add a newline.</li></ul>
<h4>Reading a file line by line</h4>
@@fgets_ex@@
<h4>Writing strings</h4>
@@fputs_ex@@
<p>String I/O is convenient for processing text line by line, e.g. searching or replacing a word in a file (program c5p17).</p>""",
          programs=["c5p13", "c5p17"]),

        T("5.2.6 Formatted I/O – fprintf() / fscanf()",
          r"""<p>These work exactly like <code>printf()</code> and <code>scanf()</code>, but take a file pointer as the first argument. They are used to store and read <b>mixed data</b> (int, float, string) such as student or employee records.</p>
@@fprintf_syn@@
<h4>Writing a record</h4>
@@fprintf_ex@@
<h4>Reading records until the end of the file</h4>
@@fscanf_ex@@
<ul><li><code>fscanf()</code> returns the <b>number of items read</b>, or EOF at the end of the file, so the loop condition <code>== 3</code> stops correctly.</li>
<li>Like scanf("%s"), fscanf reads a string only up to white space.</li></ul>
<h4>Standard files</h4>
<p>C automatically opens three files: <b>stdin</b> (keyboard), <b>stdout</b> (screen) and <b>stderr</b> (screen, for errors). They can be used with file functions:</p>
@@std_streams@@""",
          programs=["c5p16"]),

        T("5.2.7 Summary of File Functions and Error Handling",
          r"""<table>
<tr><th>Function</th><th>Purpose</th><th>Returns at end / on error</th></tr>
<tr><td>fopen(name, mode)</td><td>Opens a file</td><td>NULL</td></tr>
<tr><td>fclose(fp)</td><td>Closes a file</td><td>EOF</td></tr>
<tr><td>fgetc(fp) / getc(fp)</td><td>Reads a character</td><td>EOF</td></tr>
<tr><td>fputc(ch, fp) / putc(ch, fp)</td><td>Writes a character</td><td>EOF</td></tr>
<tr><td>fgets(s, n, fp)</td><td>Reads a line</td><td>NULL</td></tr>
<tr><td>fputs(s, fp)</td><td>Writes a string</td><td>EOF</td></tr>
<tr><td>fscanf(fp, …)</td><td>Formatted read</td><td>EOF</td></tr>
<tr><td>fprintf(fp, …)</td><td>Formatted write</td><td>negative value</td></tr>
<tr><td>feof(fp)</td><td>Tests end of file</td><td>non-zero at end</td></tr>
</table>
<h4>Common file errors</h4>
<ul><li>Opening a file that does not exist in "r" mode</li>
<li>Using an invalid file name, or a directory without permission</li>
<li>Reading past the end of the file</li>
<li>Writing to a file opened in "r" mode, or reading one opened in "w" mode</li>
<li>Using a file pointer after fclose()</li></ul>
<h4>Error handling</h4>
@@err_ex@@
<p>Always check the return value of <code>fopen()</code>, and use the return values of the read functions (EOF/NULL) or <code>feof()</code> to stop reading.</p>""",
          diagram="c5_file_funcs"),

        T("Key Points – 5.2",
          r"""<ul>
<li>A file stores data <b>permanently</b> on disk; variables are lost when the program ends.</li>
<li>Text file = readable characters with lines; binary file = raw bytes (not in syllabus).</li>
<li>Steps: <code>FILE *fp;</code> → <code>fopen()</code> → read/write → <code>fclose()</code>.</li>
<li>fopen returns <b>NULL</b> on failure; always check it.</li>
<li>Modes: "r" (read, must exist), "w" (write, erases), "a" (append at end), "r+", "w+", "a+".</li>
<li>fclose flushes the buffer to the disk and frees the file.</li>
<li>Character I/O: fgetc/fputc; string I/O: fgets/fputs; formatted I/O: fscanf/fprintf.</li>
<li>EOF (usually −1) marks the end of the file; store fgetc() in an <b>int</b>.</li>
<li>fgets keeps the newline and returns NULL at end; fputs does not add a newline.</li>
<li>stdin, stdout and stderr are opened automatically.</li>
</ul>""", key=True),
    ],
}

NOTES_B = [SEC_5_2]
