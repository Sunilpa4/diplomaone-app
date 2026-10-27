"""DI01000131 Computer Programming Fundamentals - Unit 5 diagrams (strings, command line, files)."""
import os
from flowchart_lib import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "content", "computer", "sem1", "DI01000131", "diagrams")
CELL = "#F5EEFD"; HL = "#FFF1C2"; HL_S = "#C99A00"; OK = "#E3F5E6"; OK_S = "#2E7D32"; BLUE = "#1565C0"; RED = "#C62828"
NUL_F = "#FDECEC"; GREYF = "#F0F0F0"


def cell(x, y, w, h, label="", fill=CELL, stroke=P, size=12, weight="bold", mono=True, color=INK):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}" stroke="{stroke}" stroke-width="1.4"/>'
            + (text(x + w / 2, y + h / 2, label, size, color=color, weight=weight, mono=mono) if label != "" else ""))


def chars(x, y, s, w=30, h=28, size=12, total=None, fills=None):
    """Draw a string as char boxes, adding \\0 and greyed unused cells up to total."""
    out = ""
    items = list(s) + ["\\0"]
    total = total or len(items)
    for i in range(total):
        if i < len(items):
            c = items[i]
            f, st, col = (NUL_F, RED, RED) if c == "\\0" else ((fills or {}).get(i, (CELL, P))[0], (fills or {}).get(i, (CELL, P))[1], INK)
            out += cell(x + i * w, y, w, h, c, f, st, size if c != "\\0" else size - 1.5, color=col)
        else:
            out += cell(x + i * w, y, w, h, "", GREYF, "#BBB")
    return out


# ------------------------------------------------------------------ 1. string in memory
def string_memory():
    b = title("String: Character Array Ending with '\\0'")
    b += text(180, 42, 'char s[10] = "GTU";', 11.5, color=P, mono=True, weight="bold")
    b += chars(30, 56, "GTU", 30, 32, 13, total=10)
    for i in range(10):
        b += text(45 + i * 30, 102, str(i), 10, mono=True, color="#666")
    b += text(30, 120, "s[0]", 10, anchor="start", mono=True, color="#444") + text(120, 120, "null character", 10, anchor="start", color=RED, weight="bold")
    b += text(240, 120, "unused", 10, anchor="start", color="#888")
    b += text(105, 146, 'strlen(s) = 3', 11, mono=True, color=INK, weight="bold") + text(255, 146, 'sizeof(s) = 10', 11, mono=True, color=INK, weight="bold")
    b += text(180, 164, "Array size must be at least length + 1 (for '\\0').", 10.5, color="#444")
    b += line("M20 180 H340", "#E0D3F2", 1)
    b += text(95, 200, "'A'  character constant", 10.5, mono=True, weight="bold", color=BLUE)
    b += cell(80, 210, 30, 30, "A", "#E3F0FC", BLUE, 13)
    b += text(95, 256, "1 byte", 10.5, color="#444")
    b += text(265, 200, '"A"  string constant', 10.5, mono=True, weight="bold", color=OK_S)
    b += chars(235, 210, "A", 30, 30, 13)
    b += text(265, 256, "2 bytes (A + \\0)", 10.5, color="#444")
    return svg(360, 270, b)


# ------------------------------------------------------------------ 2. reading methods
def read_methods():
    b = title("Reading a String: Different Methods")
    b += text(180, 42, "User types:  Ravi Patel ⏎", 11.5, color=P, mono=True, weight="bold")
    rows = [('scanf("%s", s);', "Ravi", "stops at first space", INK),
            ('scanf("%[^\\n]", s);', "Ravi Patel", "reads till newline", INK),
            ('gets(s);', "Ravi Patel", "unsafe – removed in C11", RED),
            ('fgets(s, 20, stdin);', "Ravi Patel\\n", "safe; keeps the newline", OK_S)]
    y = 62
    for code, res, note, col in rows:
        b += f'<rect x="10" y="{y}" width="340" height="46" rx="6" fill="#FAF7FE" stroke="#E0D3F2"/>'
        b += text(18, y + 17, code, 10.5, anchor="start", mono=True, weight="bold", color=col if col != INK else P)
        b += text(18, y + 35, note, 10, anchor="start", color=col if col != INK else "#555")
        b += rbox(272, y + 23, 140, 26, '"' + res + '"', OK if col == OK_S else ("#FDECEC" if col == RED else CELL),
                  OK_S if col == OK_S else (RED if col == RED else P), 11, "bold", mono=True)
        y += 54
    b += text(180, y + 8, "Use fgets() for safe input of a full line.", 10.5, color="#333", weight="bold")
    return svg(360, y + 22, b)


# ------------------------------------------------------------------ 3. string functions
def str_funcs():
    b = title("Important String Functions <string.h>")
    cards = [("strlen(s)", 'strlen("Hello")', "→ 5", "length, without '\\0'"),
             ("strcpy(d, s)", 'strcpy(d, "Hi")', '→ d = "Hi"', "copies s into d"),
             ("strcat(s1, s2)", 's1="GTU ", s2="C"', '→ s1 = "GTU C"', "joins s2 at end of s1"),
             ("strcmp(s1, s2)", 'strcmp("abc","abd")', "→ negative", "0 if equal, <0, >0"),
             ("strchr(s, ch)", "strchr(\"hello\",'l')", '→ "llo"', "first occurrence of ch"),
             ("strstr(s1, s2)", 'strstr("diploma","lom")', '→ "loma"', "first occurrence of s2")]
    for i, (fn, ex, res, note) in enumerate(cards):
        x = 10 + (i % 2) * 175; y = 34 + (i // 2) * 82
        b += f'<rect x="{x}" y="{y}" width="165" height="74" rx="8" fill="#FAF7FE" stroke="#C9B3EC" stroke-width="1.2"/>'
        b += f'<rect x="{x}" y="{y}" width="165" height="22" rx="8" fill="{P}"/><rect x="{x}" y="{y + 12}" width="165" height="10" fill="{P}"/>'
        b += text(x + 82, y + 11, fn, 11, mono=True, weight="bold", color="#fff")
        b += text(x + 82, y + 35, ex, 9.5, mono=True, color=INK)
        b += text(x + 82, y + 50, res, 10.5, mono=True, weight="bold", color=OK_S)
        b += text(x + 82, y + 65, note, 9.5, color="#555")
    return svg(360, 34 + 3 * 82 + 6, b)


# ------------------------------------------------------------------ 4. strcmp working
def strcmp_diag():
    b = title("How strcmp() Compares Two Strings")
    b += text(180, 42, 'strcmp("Apple", "Apply")', 11.5, color=P, mono=True, weight="bold")
    s1, s2 = "Apple", "Apply"
    x0, w = 80, 40
    b += text(70, 74, "s1", 11, anchor="end", mono=True, weight="bold") + text(70, 142, "s2", 11, anchor="end", mono=True, weight="bold")
    for i in range(5):
        same = s1[i] == s2[i]
        f, st = (OK, OK_S) if same else (HL, HL_S)
        b += cell(x0 + i * w, 60, w, 28, s1[i], f, st, 13) + cell(x0 + i * w, 128, w, 28, s2[i], f, st, 13)
        b += text(x0 + i * w + w / 2, 100, str(ord(s1[i])), 9.5, mono=True, color="#555")
        b += text(x0 + i * w + w / 2, 115, "=" if same else "≠", 12, weight="bold", color=OK_S if same else RED)
        b += text(x0 + i * w + w / 2, 168, str(ord(s2[i])), 9.5, mono=True, color="#555")
    b += text(180, 196, "Characters are compared one by one (ASCII values)", 10.5, color="#444")
    b += text(180, 212, "until they differ or '\\0' is reached.", 10.5, color="#444")
    b += text(180, 236, "'e' (101) − 'y' (121) = −20  →  result < 0", 11, mono=True, weight="bold", color="#8D6E00")
    b += text(180, 254, '"Apple" comes before "Apply"', 10.5, color="#333")
    rows = [("0", "s1 and s2 are equal"), ("< 0", "s1 comes before s2"), ("> 0", "s1 comes after s2")]
    y = 272
    b += f'<rect x="60" y="{y}" width="240" height="22" fill="{P}"/>'
    b += text(110, y + 11, "Return value", 10.5, color="#fff", weight="bold") + text(230, y + 11, "Meaning", 10.5, color="#fff", weight="bold")
    for i, (v, m) in enumerate(rows):
        yy = y + 22 + i * 22
        if i % 2:
            b += f'<rect x="60" y="{yy}" width="240" height="22" fill="#FAF7FE"/>'
        b += text(110, yy + 11, v, 11, mono=True, weight="bold") + text(230, yy + 11, m, 10.5, color="#333")
    return svg(360, y + 22 + 66 + 12, b)


# ------------------------------------------------------------------ 5. array of strings
def str_array():
    b = title("Array of Strings (2-D Character Array)")
    b += text(180, 42, 'char name[4][8] = {"Amit", "Riya", "Om", "Kavya"};', 9.5, color=P, mono=True, weight="bold")
    names = ["Amit", "Riya", "Om", "Kavya"]
    x0, w, h = 96, 30, 26
    for c in range(8):
        b += text(x0 + c * w + w / 2, 66, str(c), 10, mono=True, color="#666")
    for r, n in enumerate(names):
        y = 74 + r * 32
        b += text(x0 - 8, y + h / 2, f"name[{r}]", 10.5, anchor="end", mono=True, weight="bold", color=BLUE)
        b += chars(x0, y, n, w, h, 12, total=8)
    y = 74 + 4 * 32 + 10
    pts = ["Each row stores one string (max 7 chars + '\\0').", "name[i] is the address of row i → use with %s:",
           'printf("%s", name[1]);   →  Riya', "Rows: number of strings; columns: max length + 1."]
    for i, s in enumerate(pts):
        b += text(20, y + 14 + i * 18, s, 10.5 if i != 2 else 10.5, anchor="start", mono=(i == 2), color="#333" if i != 2 else "#8D6E00",
                  weight="bold" if i == 2 else "normal")
    return svg(360, y + 14 + 4 * 18, b)


# ------------------------------------------------------------------ 6. command line arguments
def cmdline():
    b = title("Command Line Arguments")
    b += f'<rect x="20" y="32" width="320" height="26" rx="5" fill="#1E1530"/>'
    b += text(30, 45, "$ ./marks Ravi 25 Surat", 11.5, anchor="start", mono=True, color="#B9F6CA", weight="bold")
    b += text(180, 76, "int main(int argc, char *argv[])", 11, mono=True, color=P, weight="bold")
    b += text(40, 104, "argc", 11, anchor="start", mono=True, weight="bold") + cell(80, 90, 40, 28, "4", HL, HL_S, 13)
    b += text(130, 104, "(number of arguments incl. program name)", 9.5, anchor="start", color="#555")
    strs = ["./marks", "Ravi", "25", "Surat"]
    y0 = 136
    for i in range(5):
        y = y0 + i * 34
        b += text(70, y + 14, f"argv[{i}]", 10.5, anchor="end", mono=True, weight="bold", color=BLUE)
        if i < 4:
            b += cell(78, y, 40, 28, "", "#E3F0FC", BLUE)
            b += f'<circle cx="98" cy="{y + 14}" r="3" fill="{BLUE}"/>'
            b += arr([(98, y + 14), (146, y + 14)], BLUE)
            b += chars(150, y, strs[i], 24, 28, 11)
        else:
            b += cell(78, y, 40, 28, "NULL", NUL_F, RED, 9)
    y = y0 + 5 * 34 + 6
    b += text(180, y + 4, "argv[ ] is an array of strings (char pointers).", 10.5, color="#333")
    b += text(180, y + 21, 'Numbers arrive as strings: age = atoi(argv[2]);', 10.5, color="#8D6E00", mono=False, weight="bold")
    return svg(360, y + 34, b)


# ------------------------------------------------------------------ 7. file I/O concept
def file_io():
    b = title("File Input / Output in C")
    b += rbox(62, 92, 96, 56, "Program\n(RAM)", "#E3F0FC", BLUE, 11.5, "bold")
    b += rbox(180, 92, 80, 56, "Buffer", HL, HL_S, 11.5, "bold")
    b += f'<path d="M262 66 h72 v52 h-72 z" fill="{OK}" stroke="{OK_S}" stroke-width="1.6"/>'
    b += f'<ellipse cx="298" cy="66" rx="36" ry="8" fill="{OK}" stroke="{OK_S}" stroke-width="1.6"/>'
    b += f'<path d="M262 118 a36 8 0 0 0 72 0" fill="{OK}" stroke="{OK_S}" stroke-width="1.6"/>'
    b += text(298, 92, "File on", 11, weight="bold", color="#1B5E20") + text(298, 106, "disk", 11, weight="bold", color="#1B5E20")
    b += arr([(110, 80), (140, 80)], RED) + arr([(220, 80), (260, 80)], RED)
    b += arr([(260, 104), (220, 104)], OK_S) + arr([(140, 104), (110, 104)], OK_S)
    b += text(180, 142, "write: fputc  fputs  fprintf", 10.5, mono=True, color=RED, weight="bold")
    b += text(180, 160, "read : fgetc  fgets  fscanf", 10.5, mono=True, color=OK_S, weight="bold")
    b += text(180, 186, "Steps of file handling", 11.5, weight="bold", color=P)
    steps = [("1", "FILE *fp;", "declare"), ("2", "fopen()", "open"), ("3", "read / write", "process"), ("4", "fclose(fp)", "close")]
    for i, (n, c, d) in enumerate(steps):
        x = 48 + i * 88
        b += rbox(x, 216, 76, 34, c, CELL, P, 9.5, "bold", mono=True)
        b += text(x, 244, d, 10, color="#555")
        if i < 3:
            b += arr([(x + 38, 216), (x + 50, 216)])
    b += text(180, 270, "Data in a file is permanent (stays after the program ends).", 10.5, color="#444")
    return svg(360, 284, b)


# ------------------------------------------------------------------ 8. file modes
def file_modes():
    b = title("File Opening Modes (Text Files)")
    b += text(180, 40, 'fp = fopen("data.txt", "mode");', 11, color=P, mono=True, weight="bold")
    cols = [(10, 40, "Mode"), (50, 92, "Purpose"), (142, 104, "File exists"), (246, 104, "File not found")]
    rows = [("r", "read", "open, read from start", "returns NULL"),
            ("w", "write", "contents erased", "new file created"),
            ("a", "append", "write at the end", "new file created"),
            ("r+", "read + write", "open from start", "returns NULL"),
            ("w+", "write + read", "contents erased", "new file created"),
            ("a+", "read + append", "read; write at end", "new file created")]
    y = 54
    b += f'<rect x="10" y="{y}" width="340" height="24" fill="{P}"/>'
    for x, w, h in cols:
        b += text(x + w / 2, y + 12, h, 10.5, color="#fff", weight="bold")
    for i, r in enumerate(rows):
        yy = y + 24 + i * 30
        if i % 2:
            b += f'<rect x="10" y="{yy}" width="340" height="30" fill="#FAF7FE"/>'
        for j, ((x, w, _), v) in enumerate(zip(cols, r)):
            col = INK
            if j == 3 and "NULL" in v:
                col = RED
            if j == 2 and "erased" in v:
                col = "#8D6E00"
            b += text(x + w / 2, yy + 15, v, 11.5 if j == 0 else 10, mono=(j == 0), weight="bold" if j == 0 else "normal", color=col)
    yy = y + 24 + 6 * 30
    b += line(f"M10 {yy} H350", "#E0D3F2", 1)
    b += text(180, yy + 20, 'Always check: if (fp == NULL) → file not opened', 10.5, color="#333", weight="bold")
    return svg(360, yy + 34, b)


# ------------------------------------------------------------------ 9. file functions
def file_funcs():
    b = title("File I/O Functions <stdio.h>")
    y = 34
    cols = [(10, 96, "Type"), (106, 122, "Read"), (228, 122, "Write")]
    rows = [("Character", "fgetc(fp)\ngetc(fp)", "fputc(ch, fp)\nputc(ch, fp)"),
            ("String", "fgets(s, n, fp)", "fputs(s, fp)"),
            ("Formatted", "fscanf(fp, ...)", "fprintf(fp, ...)"),
            ("Open / Close", "fopen(name, mode)", "fclose(fp)"),
            ("End of file", "EOF, feof(fp)", "—")]
    b += f'<rect x="10" y="{y}" width="340" height="24" fill="{P}"/>'
    for x, w, h in cols:
        b += text(x + w / 2, y + 12, h, 10.5, color="#fff", weight="bold")
    yy = y + 24
    for i, (t, r, w_) in enumerate(rows):
        h = 40 if "\n" in r else 30
        if i % 2:
            b += f'<rect x="10" y="{yy}" width="340" height="{h}" fill="#FAF7FE"/>'
        b += text(58, yy + h / 2, t, 10.5, weight="bold", color="#333")
        b += text(167, yy + h / 2, r, 10, mono=True, color=OK_S, weight="bold")
        b += text(289, yy + h / 2, w_, 10, mono=True, color=RED, weight="bold")
        yy += h
    b += line(f"M10 {yy} H350", "#E0D3F2", 1)
    b += text(180, yy + 20, "Same as getchar/putchar, gets/puts, scanf/printf", 10.5, color="#444")
    b += text(180, yy + 36, "but with a FILE pointer.", 10.5, color="#444")
    return svg(360, yy + 50, b)


# ------------------------------------------------------------------ 10. flowchart: copy file
def fc_copy():
    b = title("Flowchart: Copy One File to Another")
    x = 150
    b += terminal(x, 44, "Start")
    b += down(x, 60, 76) + process(x, 96, "open source (r)\nopen target (w)", 170, 40)
    b += down(x, 116, 132) + decision(x, 160, "fs == NULL ?", 130, 56, mono=True)
    b += arr([(215, 160), (300, 160), (300, 186)], label="True", lpos=(258, 151))
    b += io(300, 203, "Print error", 96, 34)
    b += line("M300 220 V470") + arrowhead(194, 470, 180, 7, INK) + line("M300 470 H196")
    b += arr([(x, 188), (x, 208)], label="False", lpos=(x + 24, 198))
    b += process(x, 225, "ch = fgetc(fs)", 150, 34, mono=True)
    b += down(x, 242, 259) + decision(x, 288, "ch != EOF ?", 130, 58, mono=True)
    b += arr([(x, 317), (x, 337)], label="True", lpos=(x + 22, 327))
    b += process(x, 354, "fputc(ch, ft)", 150, 34, mono=True)
    b += arr([(x, 371), (x, 384), (36, 384), (36, 200), (x - 4, 200)])
    b += text(26, 300, "Loop", 10.5, color=GREY, weight="bold").replace("<text ", '<text transform="rotate(-90 26 300)" ')
    b += arr([(215, 288), (245, 288), (245, 398), (x, 398), (x, 404)], label="False", lpos=(232, 279))
    b += process(x, 421, "fclose(fs); fclose(ft);", 186, 34, mono=True)
    b += down(x, 438, 454) + terminal(x, 470, "Stop", 90)
    return svg(360, 496, b)


DIAGRAMS = {
    "c5_string_memory": string_memory, "c5_read_methods": read_methods, "c5_str_funcs": str_funcs,
    "c5_strcmp": strcmp_diag, "c5_str_array": str_array, "c5_cmdline": cmdline, "c5_file_io": file_io,
    "c5_file_modes": file_modes, "c5_file_funcs": file_funcs, "c5_fc_copy": fc_copy,
}

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for k, f in DIAGRAMS.items():
        with open(os.path.join(OUT, k + ".svg"), "w", encoding="utf-8") as fh:
            fh.write(f())
    print("written", len(DIAGRAMS))
