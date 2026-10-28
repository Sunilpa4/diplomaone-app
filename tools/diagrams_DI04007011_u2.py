"""DI04007011 Web Development - Unit 2 diagrams: functions, arrays and strings."""
import os
from flowchart_lib import *
from diagrams_DI03000021_u1 import box, BLUE, BLUEF, GREEN, GREENF, ORANGE, ORANGEF, RED, REDF, YEL, TEAL, TEALF
from diagrams_DI03000011_u1 import note
from diagrams_DI03000031_u1 import lines, rarrow, grid, PF, GREY
from diagrams_DI03000061_u1 import code, OUT


def anatomy():
    b = title("Anatomy of a PHP Function")
    src = ["function fare($km, $rate = 1.2) {",
           "    $total = 250 + $km * $rate;",
           "    return $total;",
           "}",
           "",
           "echo fare(265);   // 318 + 250 = 568"]
    b += code(24, 64, src, size=8.2, lh=15)
    marks = [("name + params (in)", 64, GREEN),
             ("default if skipped", 79, ORANGE),
             ("return: value back", 94, BLUE),
             ("call: name(args)", 154, P)]
    for lbl, ly, c in marks:
        b += rarrow(196, 236, ly - 3, color=c)
        b += text(238, ly, lbl, 7.8, anchor="start", weight="bold", color=c)
    b += note(12, 178, 336, ["params = inputs at the doorway; return =",
                             "exactly one value back; the body never",
                             "echoes - it COMPUTES. Name rule: letter or",
                             "underscore first, no $ on the name."], size=9.0)
    return svg(360, 246, b)


def value_ref():
    b = title("By Value vs By Reference")
    b += box(12, 46, 158, 128, BLUEF, BLUE, 8, 1.2)
    b += text(91, 64, "BY VALUE (copy)", 8.6, weight="bold", color=BLUE)
    b += code(24, 82, ["function add($n) {",
                       "    $n += 10;",
                       "}",
                       "$x = 5;",
                       "add($x);",
                       "// $x still 5"], size=7.6, lh=13)
    b += box(192, 46, 158, 128, ORANGEF, ORANGE, 8, 1.2)
    b += text(271, 64, "BY REFERENCE (&)", 8.6, weight="bold", color=ORANGE)
    b += code(204, 82, ["function add(&$n) {",
                        "    $n += 10;",
                        "}",
                        "$x = 5;",
                        "add($x);",
                        "// $x is 15 !"], size=7.6, lh=13)
    b += note(12, 188, 336, ["Default: PHP photocopies the argument -",
                             "the original survives the call. With & the",
                             "function borrows the ORIGINAL box itself:",
                             "swap($a,$b) style updates need it."], size=9.2)
    return svg(360, 250, b)


def scope():
    b = title("Variable Scope: Rooms of the Script")
    b += box(16, 48, 150, 120, GREENF, GREEN, 8, 1.2)
    b += text(91, 66, "INSIDE function", 8.6, weight="bold", color=GREEN)
    b += code(28, 84, ["function bill() {",
                       "  $tip = 5;   // local",
                       "  // $total ? no",
                       "  global $total;",
                       "  $total += $tip;",
                       "}"], size=7.6, lh=13)
    b += box(194, 48, 150, 120, BLUEF, BLUE, 8, 1.2)
    b += text(269, 66, "OUTSIDE (global)", 8.6, weight="bold", color=BLUE)
    b += code(206, 84, ["$total = 100;",
                        "bill();",
                        "echo $total;",
                        "// 105 - changed!",
                        "// $tip ? gone"], size=7.6, lh=13)
    b += rarrow(166, 194, 128, color=GREY)
    b += text(180, 116, "global", 7.8, color=GREY, weight="bold")
    b += note(12, 182, 336, ["Local vars are born and die with the call.",
                             "global $x; (or $GLOBALS['x']) opens the",
                             "window. static $c remembers values",
                             "between calls of the same function."], size=9.0)
    return svg(360, 246, b)


def array_types():
    b = title("Three Flavours of PHP Arrays")
    b += box(12, 46, 108, 120, GREENF, GREEN, 7, 1.2)
    b += text(66, 62, "INDEXED", 8.6, weight="bold", color=GREEN)
    b += code(22, 78, ['$c = ["Surat",',
                       '        "Bharuch"];',
                       "// keys are",
                       "// 0, 1 auto",
                       "echo $c[0];"], size=7.4, lh=12)
    b += box(126, 46, 108, 120, BLUEF, BLUE, 7, 1.2)
    b += text(180, 62, "ASSOCIATIVE", 8.2, weight="bold", color=BLUE)
    b += code(136, 78, ['$f = ["SRT"=>250,',
                        '      "BRC"=>120];',
                        "// named keys",
                        "echo $f['SRT'];"], size=7.4, lh=12)
    b += box(240, 46, 108, 120, ORANGEF, ORANGE, 7, 1.2)
    b += text(294, 62, "MULTI-DIM", 8.6, weight="bold", color=ORANGE)
    b += code(250, 78, ['$bus = [',
                        '  ["id"=>7,',
                        '   "seats"=>40],',
                        ' ];',
                        'echo $bus[0]',
                        '     ["seats"];'], size=7.4, lh=12)
    b += note(12, 180, 336, ["One array type, three habits: numeric",
                             "positions, named keys, or arrays-in-arrays.",
                             "count($a) measures any of them."], size=9.2)
    return svg(360, 240, b)


def foreach_map():
    b = title("foreach: Streaming an Array")
    b += box(20, 54, 130, 96, GREENF, GREEN, 7, 1.2)
    b += text(85, 70, "$fare map", 8.4, weight="bold", color=GREEN)
    b += code(32, 86, ['"SRT" => 250',
                       '"BRC" => 120',
                       '"AMD" => 160'], size=7.8, lh=14)
    b += box(196, 54, 144, 96, BLUEF, BLUE, 7, 1.2)
    b += text(268, 70, "each lap gives", 8.4, weight="bold", color=BLUE)
    b += code(206, 86, ["foreach ($fare as",
                        "     $city => $amt) {",
                        "  echo \"$city: $amt\";",
                        "}"], size=7.8, lh=14)
    b += rarrow(150, 196, 102)
    b += text(173, 96, "as", 8.0, color=GREY)
    b += box(20, 162, 320, 40, PF, P, 7, 1.2)
    b += text(180, 178, "output: SRT: 250 / BRC: 120 / AMD: 160", 8.2, weight="bold", color=P)
    b += text(180, 193, "key AND value per lap - no counter needed", 7.8)
    b += note(12, 214, 336, ["foreach ($a as $v)         values only",
                             "foreach ($a as $k => $v)  keys too.",
                             "The array pointer crew (current, next,",
                             "end...) is the manual gearbox."], size=8.8)
    return svg(360, 296, b)


def array_funcs():
    b = title("Array Function Toolbox")
    b += grid(12, 44, [108, 106, 122], [
        ["task", "function", "returns"],
        ["how many", "count($a)", "int size"],
        ["is inside", "in_array(5, $a)", "bool"],
        ["sort by val", "sort / rsort", "rekeys! lost keys"],
        ["sort keep keys", "asort / ksort / arsort", "assoc-safe"],
        ["glue arrays", "array_merge", "one big array"],
        ["flip order", "array_reverse", "reversed copy"],
        ["stack ops", "array_push / array_pop", "end add/remove"],
        ["pointer walk", "current next prev end", "element at pointer"],
        ["string bridge", "implode / explode", "join or split"],
        ["arrays ->", "vars list($a,$b)=", "unpack slots"],
    ], rh=19, size=7.4)
    b += note(12, 268, 336, ["sort() RENUMBERS keys (0..n) - on assoc",
                             "arrays use asort/ksort instead."], size=9.2)
    return svg(360, 322, b)


def quotes():
    b = title("Four Ways to Write a String")
    labels = [("SINGLE QUOTES", "'Fare: $fare'", "literal - no expansion", GREENF, GREEN),
              ("DOUBLE QUOTES", '"Fare: $fare"', "variables expand in place", BLUEF, BLUE),
              ("HEREDOC  <<<EOT", "multi-line, expands vars", "echo <<<EOT ... EOT;", TEALF, TEAL),
              ("NOWDOC <<<'EOT'", "multi-line, stays literal", "raw HTML / SQL blocks", ORANGEF, ORANGE)]
    for i, (h, s, sub, f, st) in enumerate(labels):
        x = 12 + (i % 2) * 174
        y = 46 + (i // 2) * 64
        b += box(x, y, 162, 54, f, st, 8, 1.2)
        b += text(x + 81, y + 16, h, 8.4, weight="bold", color=st)
        b += text(x + 81, y + 31, s, 8.0, mono=True, color=GREY)
        b += text(x + 81, y + 45, sub, 7.8)
    b += note(12, 182, 336, ["heredoc = double quotes without quotes;",
                             "nowdoc = single quotes without quotes.",
                             "Escaping: \\n newline, \\$ literal dollar,",
                             "htmlspecialchars() before echoing"],
                             size=9.0)
    return svg(360, 250, b)


def string_funcs():
    b = title("String Function Toolbox")
    b += grid(12, 44, [96, 118, 122], [
        ["task", "function", "result"],
        ["length", "strlen(\"Surat\")", "5"],
        ["change case", "strtolower / strtoupper", "SURAT / surat"],
        ["trim edges", "trim ltrim rtrim", "spaces gone"],
        ["cut a piece", "substr(\"Surat\",0,3)", "\"Sur\""],
        ["find position", "strpos(\"abc\",\"b\")", "1 (0-based)"],
        ["case-insens find", "stristr($h, $needle)", "rest of string"],
        ["replace", "str_replace(\"a\",\"o\",\"cat\")", "\"cot\""],
        ["compare", "strcmp / strcasecmp", "-1 0 or 1"],
        ["reverse", "strrev(\"madam\")", "\"madam\""],
        ["char<->code", "chr(65) / ord(\"A\")", "\"A\" / 65"],
    ], rh=19, size=7.4)
    b += note(12, 268, 336, ["strpos returns false when NOT found -",
                             "test with === false, never == (position",
                             "0 is falsy and would fool you)."], size=9.2)
    return svg(360, 322, b)


ALL = {"wd2_anatomy": anatomy, "wd2_value_ref": value_ref, "wd2_scope": scope,
       "wd2_array_types": array_types, "wd2_foreach_map": foreach_map, "wd2_array_funcs": array_funcs,
       "wd2_quotes": quotes, "wd2_string_funcs": string_funcs}

if __name__ == "__main__":
    import subject_DI04007011 as S
    for k, fn in ALL.items():
        with open(os.path.join(S.DIAG_DIR, k + ".svg"), "w", encoding="utf-8") as f:
            f.write(fn())
    print("written", len(ALL))
