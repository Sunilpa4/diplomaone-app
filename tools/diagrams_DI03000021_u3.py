"""DI03000021 Data Structures - Unit 3 diagrams: pointer, structure, DMA, linked list types and SLL operations."""
import os
from flowchart_lib import *
from diagrams_DI03000021_u1 import (box, cells, CELL, BLUE, BLUEF, GREEN, GREENF, ORANGE, ORANGEF, RED, REDF,
                                    YEL, YELS, TEAL, TEALF)

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "content", "computer", "sem3", "DI03000021", "diagrams")

NW, PW, NH = 36, 22, 28          # data width, pointer width, node height
NODE = NW + PW


def node(x, y, val, fill="#F1E8FC", stroke=P, null=False, addr=None):
    b = box(x, y, NW, NH, fill, stroke, 0, 1.4) + box(x + NW, y, PW, NH, "#fff", stroke, 0, 1.4)
    b += text(x + NW / 2, y + NH / 2, str(val), 11.5, mono=True, weight="bold")
    if null:
        b += line(f"M{x + NW + 3} {y + NH - 3} L{x + NODE - 3} {y + 3}", RED, 1.4)
    else:
        b += f'<circle cx="{x + NW + PW / 2}" cy="{y + NH / 2}" r="2.6" fill="{INK}"/>'
    if addr:
        b += text(x + NODE / 2, y + NH + 11, addr, 8.6, mono=True, color="#888")
    return b


def link(x1, x2, y, color=INK):
    """arrow from pointer field of node at x1 to node starting at x2"""
    return arr([(x1 + NW + PW / 2, y + NH / 2), (x2 - 1, y + NH / 2)], color)


def slist(x, y, vals, gap=22, fills=None, start="START", null=True, addrs=None):
    b = ""
    xs = [x + i * (NODE + gap) for i in range(len(vals))]
    for i, v in enumerate(vals):
        f = (fills or {}).get(i, "#F1E8FC")
        b += node(xs[i], y, v, f, null=(null and i == len(vals) - 1), addr=addrs[i] if addrs else None)
        if i:
            b += link(xs[i - 1], xs[i], y)
    if start:
        b += text(xs[0] + NW / 2, y - 26, start, 9.6, weight="bold", color=BLUE, mono=True)
        b += arr([(xs[0] + NW / 2, y - 20), (xs[0] + NW / 2, y - 1)], BLUE)
    if null and vals:
        b += text(xs[-1] + NODE / 2, y + NH + (22 if addrs else 11), "NULL", 8.6, mono=True, color=RED)
    return b, xs


def note(x, y, w, lines, fill=BLUEF, stroke=BLUE, size=9.8, lh=15):
    b = box(x, y, w, 10 + lh * len(lines), fill, stroke, 7, 1.1)
    for i, s in enumerate(lines):
        if isinstance(s, tuple):
            s, c = s
        else:
            c = INK
        s = s.replace(" ", "\u00a0")
        b += text(x + 8, y + 15 + i * lh, s, size, anchor="start", mono=True, color=c)
    return b


# ------------------------------------------------------------------ 1. pointer
def pointer():
    b = title("Pointer: a Variable that Stores an Address")
    b += note(20, 34, 320, ["int x = 10;", "int *p;      /* pointer to int */", "p = &x;      /* p gets address of x */"], "#FCFAFF", "#D9C8F0")
    # x box
    b += box(40, 128, 86, 40, GREENF, GREEN, 6) + text(83, 148, "10", 14, mono=True, weight="bold")
    b += text(83, 120, "x", 12, weight="bold", color=GREEN) + text(83, 182, "address 1000", 9, mono=True, color="#888")
    b += box(226, 128, 86, 40, BLUEF, BLUE, 6) + text(269, 148, "1000", 14, mono=True, weight="bold")
    b += text(269, 120, "p", 12, weight="bold", color=BLUE) + text(269, 182, "address 2000", 9, mono=True, color="#888")
    b += arr([(224, 148), (128, 148)], RED) + text(176, 140, "points to", 9.4, color=RED)
    rows = [("&x", "1000", "address of x"), ("p", "1000", "value of p"), ("*p", "10", "value at address in p"),
            ("&p", "2000", "address of p")]
    for i, (e, v, d) in enumerate(rows):
        y = 210 + i * 19
        b += text(40, y, e, 11, anchor="start", mono=True, weight="bold", color=P)
        b += text(92, y, "= " + v, 11, anchor="start", mono=True)
        b += text(168, y, d, 9.6, anchor="start", color="#555")
    b += text(180, 296, "& = address-of operator,  * = value-at (indirection)", 9.6, color="#444")
    return svg(360, 308, b)


# ------------------------------------------------------------------ 2. structure + pointer to structure
def structure():
    b = title("Structure and Structure Pointer")
    b += note(12, 32, 160, ["struct student {", "  int roll;", "  char name[10];", "  float marks;", "};",
                            "struct student s;", "struct student *ptr;", "ptr = &s;"], "#FCFAFF", "#D9C8F0", 9.4, 14)
    # memory layout of s
    x, y = 196, 40
    b += text(268, y - 4, "variable s in memory", 9.6, weight="bold", color=P)
    parts = [("roll", "4 bytes", 34, GREENF, GREEN), ("name", "10 bytes", 56, BLUEF, BLUE), ("marks", "4 bytes", 34, ORANGEF, ORANGE)]
    yy = y + 4
    for n, sz, h, f, c in parts:
        b += box(x, yy, 80, h, f, c, 0, 1.3) + text(x + 40, yy + h / 2, n, 10.5, mono=True, weight="bold")
        b += text(x + 86, yy + h / 2, sz, 8.8, anchor="start", color="#666")
        yy += h
    b += text(240, yy + 14, "size ≥ 18 bytes (padding)", 8.8, color="#888")
    b += box(12, 172, 336, 92, "#fff", "#D9C8F0", 8, 1)
    b += text(180, 188, "Accessing members", 10.4, weight="bold", color=P)
    rows = [("s.roll", "dot operator: with a structure variable"), ("ptr->roll", "arrow operator: with a pointer"),
            ("(*ptr).roll", "same as ptr->roll")]
    for i, (e, d) in enumerate(rows):
        b += text(22, 208 + i * 19, e, 11, anchor="start", mono=True, weight="bold", color=BLUE)
        b += text(122, 208 + i * 19, d, 9.4, anchor="start", color="#444")
    b += text(180, 284, "A linked-list node is a self-referential structure", 9.8, color="#444")
    return svg(360, 296, b)


# ------------------------------------------------------------------ 3. DMA
def dma():
    b = title("Dynamic Memory Allocation (stdlib.h)")
    fns = [("malloc(size)", "one block, garbage values", GREEN), ("calloc(n, size)", "n blocks, all set to 0", BLUE),
           ("realloc(ptr, size)", "resize an old block", ORANGE), ("free(ptr)", "release the memory", RED)]
    for i, (f, d, c) in enumerate(fns):
        y = 34 + i * 34
        b += box(12, y, 336, 28, "#fff", c, 6, 1.3)
        b += text(22, y + 14, f, 11, anchor="start", mono=True, weight="bold", color=c)
        b += text(176, y + 14, d, 9.8, anchor="start", color="#333")
    b += note(12, 176, 336, ["int *a;", "a = (int *) malloc(5 * sizeof(int));", "if (a == NULL)  /* no memory */",
                             "...", "free(a);"], "#FCFAFF", "#D9C8F0", 9.6, 14)
    # heap picture
    b += text(60, 274, "stack", 9.6, weight="bold", color=P) + box(32, 282, 56, 24, BLUEF, BLUE, 0) + text(60, 294, "a", 11, mono=True, weight="bold")
    b += arr([(90, 294), (148, 294)], RED)
    b += text(240, 274, "heap: 5 ints (20 bytes)", 9.6, weight="bold", color=P)
    b += cells(150, 282, ["", "", "", "", ""], 36, 24)
    b += text(180, 326, "Memory is taken at run time, as much as needed", 9.6, color="#444")
    return svg(360, 338, b)


# ------------------------------------------------------------------ 4. node + list representation
def representation():
    b = title("Linked List Representation")
    b += node(40, 46, "data") 
    b += text(40 + NW / 2, 88, "info", 9.4, color="#666") + text(40 + NW + PW / 2, 88, "next", 9.4, color="#666")
    b += text(40 + NODE / 2, 38, "one NODE", 9.6, weight="bold", color=P)
    b += note(140, 32, 208, ["struct node {", "  int data;", "  struct node *next;", "};"], "#FCFAFF", "#D9C8F0", 9.6, 14)
    lst, xs = slist(14, 140, [10, 20, 30, 40], 24, addrs=["@500", "@820", "@300", "@760"])
    b += lst
    b += box(12, 206, 336, 76, BLUEF, BLUE, 8, 1.1)
    for i, s in enumerate(["START holds the address of the first node", "each next field holds the address of",
                           "the following node; last node: next = NULL", "nodes need NOT be in continuous memory"]):
        b += text(22, 222 + i * 16, s, 9.8, anchor="start")
    return svg(360, 294, b)


# ------------------------------------------------------------------ 5. types
def types():
    b = title("Types of Linked List")
    b += text(14, 40, "1. Singly linked list", 10.6, anchor="start", weight="bold", color=P)
    s, _ = slist(60, 52, ["A", "B", "C"], 30, start=None)
    b += text(30, 66, "START", 8.6, color=BLUE, mono=True, weight="bold") + arr([(30, 74), (30, 80), (58, 66)], BLUE) if False else ""
    b += text(30, 66, "START", 8.6, color=BLUE, mono=True, weight="bold") + arr([(46, 70), (59, 70)], BLUE)
    b += s
    # circular
    b += text(14, 118, "2. Circular linked list", 10.6, anchor="start", weight="bold", color=P)
    c, xs = slist(60, 130, ["A", "B", "C"], 30, start=None, null=False)
    b += c + text(30, 144, "START", 8.6, color=BLUE, mono=True, weight="bold") + arr([(46, 148), (59, 148)], BLUE)
    px = xs[-1] + NW + PW / 2
    b += arr([(px, 144), (px + 24, 144), (px + 24, 172), (xs[0] + NW / 2, 172), (xs[0] + NW / 2, 159)], GREEN)
    b += text((xs[0] + px) / 2 + 12, 184, "last node points back to first", 9, color=GREEN)
    # doubly
    b += text(14, 212, "3. Doubly linked list", 10.6, anchor="start", weight="bold", color=P)
    W3, G3 = 70, 30
    for i, v in enumerate(["A", "B", "C"]):
        x = 60 + i * (W3 + G3)
        b += box(x, 224, 18, NH, "#fff", P, 0, 1.4) + box(x + 18, 224, 34, NH, "#F1E8FC", P, 0, 1.4) + box(x + 52, 224, 18, NH, "#fff", P, 0, 1.4)
        b += text(x + 35, 238, v, 11.5, mono=True, weight="bold")
        if i == 0:
            b += line(f"M{x + 3} {224 + NH - 3} L{x + 15} {227}", RED, 1.3)
        if i == 2:
            b += line(f"M{x + 55} {224 + NH - 3} L{x + 67} {227}", RED, 1.3)
        if i:
            px = x - G3
            b += arr([(px - 9, 232), (x - 1, 232)], INK)
            b += arr([(x + 9, 246), (px + 1, 246)], ORANGE)
    b += text(30, 238, "START", 8.6, color=BLUE, mono=True, weight="bold") + arr([(46, 242), (59, 242)], BLUE)
    b += text(180, 272, "prev | data | next : move both directions", 9.4, color="#444", mono=True)
    return svg(360, 284, b)


# ------------------------------------------------------------------ 6. insert at beginning
def insert_begin():
    b = title("Insert a Node at the Beginning")
    b += text(14, 42, "Before", 10.4, anchor="start", weight="bold", color="#555")
    s, xs = slist(100, 64, [20, 30, 40], 22)
    b += s
    b += text(346, 126, "After inserting 10", 10.4, anchor="end", weight="bold", color=GREEN)
    s, xs = slist(20, 158, [10, 20, 30, 40], 22, fills={0: GREENF}, start="START")
    b += s + text(20 + NODE / 2, 202, "new", 9.4, color=GREEN, weight="bold")
    b += note(12, 222, 336, ["new = malloc(sizeof(struct node));", "new->data = 10;",
                             ("new->next = START;  /* step 1 */", BLUE), ("START = new;       /* step 2 */", BLUE)], "#FCFAFF", "#D9C8F0", 9.8, 15)
    b += text(180, 306, "Order matters: link first, then move START.  O(1)", 9.4, color="#444")
    return svg(360, 318, b)


# ------------------------------------------------------------------ 7. insert at end
def insert_end():
    b = title("Insert a Node at the End")
    s, xs = slist(14, 66, [10, 20, 30, 40], 24, fills={3: GREENF}, null=True)
    b += s
    # old null crossed out note
    b += text(xs[3] + NODE / 2, 50, "new", 9.4, color=GREEN, weight="bold")
    b += text(xs[2] + NODE / 2, 50, "ptr (last)", 9, color=ORANGE, weight="bold")
    b += arr([(xs[2] + NODE / 2 + 22, 44), (xs[2] + NODE / 2 + 22, 52), (xs[2] + NW + PW / 2, 62)], ORANGE) if False else ""
    b += note(12, 126, 336, ["new->data = 40;  new->next = NULL;", "if (START == NULL)  START = new;", "else {",
                             "  ptr = START;", ("  while (ptr->next != NULL)", BLUE), ("      ptr = ptr->next;", BLUE),
                             ("  ptr->next = new;", RED), "}"], "#FCFAFF", "#D9C8F0", 9.8, 15)
    b += text(180, 268, "Traverse to the last node first: O(n)", 9.6, color="#444")
    return svg(360, 280, b)


# ------------------------------------------------------------------ 8. insert after / before
def insert_after():
    b = title("Insert After / Before a Given Node")
    b += text(346, 42, "Insert 25 after node 20", 10.4, anchor="end", weight="bold", color=P)
    s, xs = slist(14, 74, [10, 20, 30, 40], 24)
    b += s
    # new node below between 20 and 30
    nx, ny = xs[1] + 40, 124
    b += node(nx, ny, 25, GREENF)
    b += text(nx - 14, ny + NH / 2, "new", 9, anchor="end", color=GREEN, weight="bold")
    b += text(xs[1] + NODE / 2, 66, "ptr", 9, color=ORANGE, weight="bold") if False else ""
    b += arr([(xs[1] + NW + PW / 2, 88 + 2), (xs[1] + NW + PW / 2, 108), (nx + 10, 108), (nx + 10, ny - 1)], RED)
    b += arr([(nx + NW + PW / 2, ny + NH / 2), (xs[2] + NODE / 2 + 10, ny + NH / 2), (xs[2] + NODE / 2 + 10, 74 + NH + 1)], GREEN)
    b += line(f"M{xs[1] + NODE + 6} 80 L{xs[2] - 6} 96", RED, 1.6)
    b += note(12, 168, 336, [("new->next = ptr->next;  /* 1 */", GREEN), ("ptr->next = new;        /* 2 */", RED)],
              "#FCFAFF", "#D9C8F0", 9.8, 15)
    b += note(12, 218, 336, ["Insert BEFORE node X:", "keep two pointers prev and ptr;", "move till ptr->data == X,",
                             "then insert new after prev", "(if X is the first node: insert at beginning)"], BLUEF, BLUE, 9.6, 15)
    return svg(360, 312, b)


# ------------------------------------------------------------------ 9. sorted insert
def insert_sorted():
    b = title("Insert into a Sorted Linked List")
    b += text(346, 42, "Insert 25 into ascending list", 10.4, anchor="end", weight="bold", color=P)
    s, xs = slist(14, 70, [10, 20, 30, 40], 24, fills={1: ORANGEF})
    b += s + text(xs[1] + NODE / 2, 112, "stop here", 9, color=ORANGE, weight="bold")
    b += text(xs[1] + NODE / 2, 124, "next 30 > 25", 8.6, color=ORANGE, mono=True)
    s, xs2 = slist(14, 176, [10, 20, 25, 30, 40], 10, fills={2: GREENF}, start="START")
    b += s
    b += note(12, 224, 336, ["if (START==NULL || x < START->data)", "    insert at beginning;", "else {",
                             "  ptr = START;", ("  while (ptr->next != NULL &&", BLUE), ("         ptr->next->data < x)", BLUE),
                             "      ptr = ptr->next;", "  insert new after ptr;  }"], "#FCFAFF", "#D9C8F0", 9.4, 14)
    return svg(360, 352, b)


# ------------------------------------------------------------------ 10. delete first / last
def delete():
    b = title("Delete the First and the Last Node")
    b += text(346, 42, "Delete first", 10.4, anchor="end", weight="bold", color=RED)
    s, xs = slist(40, 72, [10, 20, 30, 40], 22, fills={0: REDF}, start=None)
    b += s
    b += text(xs[0] + NW / 2, 120, "freed", 9, color=RED, weight="bold")
    b += text(xs[1] + NW / 2, 46, "START", 9.4, color=BLUE, weight="bold", mono=True) + arr([(xs[1] + NW / 2, 52), (xs[1] + NW / 2, 71)], BLUE)
    b += note(12, 130, 336, ["ptr = START;", ("START = START->next;", BLUE), "free(ptr);"], "#FCFAFF", "#D9C8F0", 9.6, 14)
    b += text(346, 202, "Delete last", 10.4, anchor="end", weight="bold", color=RED)
    s, xs = slist(40, 230, [10, 20, 30, 40], 22, fills={3: REDF}, null=True)
    b += s
    b += line(f"M{xs[2] + NODE + 4} 238 L{xs[3] - 4} 250", RED, 1.6)
    b += line(f"M{xs[2] + NW + 3} {230 + NH - 3} L{xs[2] + NODE - 3} 233", RED, 1.4)
    b += text(xs[2] + NODE / 2, 272, "prev: next=NULL", 8.6, color=ORANGE, weight="bold")
    b += note(12, 284, 336, ["prev = NULL; ptr = START;", "while (ptr->next != NULL)", "  { prev = ptr; ptr = ptr->next; }",
                             ("prev->next = NULL;  free(ptr);", BLUE), "(only one node: START = NULL)"], "#FCFAFF", "#D9C8F0", 9.6, 14)
    return svg(360, 368, b)


# ------------------------------------------------------------------ 11. search + count (traversal)
def traverse():
    b = title("Traversal: Search and Count")
    s, xs = slist(14, 66, [10, 20, 30, 40], 24, fills={2: YEL})
    b += s
    for i, x in enumerate(xs[:3]):
        b += text(x + NW / 2, 120, f"ptr{'→' if i < 2 else ''}", 9, color=ORANGE, weight="bold")
    b += text(xs[2] + NW / 2, 134, "found 30", 9, color=GREEN, weight="bold")
    b += text(xs[2] + NW / 2, 146, "position 3", 8.6, color=GREEN, mono=True)
    b += note(12, 160, 164, ["/* search x */", "ptr = START; pos = 1;", "while (ptr != NULL) {", " if (ptr->data == x)",
                             "   return pos;", " ptr = ptr->next;", " pos++;", "}", "return -1;"], "#FCFAFF", "#D9C8F0", 8.8, 13)
    b += note(184, 160, 164, ["/* count nodes */", "ptr = START;", "count = 0;", "while (ptr != NULL) {", "  count++;",
                              "  ptr = ptr->next;", "}", "/* count = 4 */"], GREENF, GREEN, 8.8, 13)
    b += text(180, 298, "Linear search only: no index, O(n)", 9.6, color="#444")
    return svg(360, 310, b)


DIAGRAMS = {"ds3_pointer": pointer, "ds3_structure": structure, "ds3_dma": dma, "ds3_representation": representation,
            "ds3_types": types, "ds3_insert_begin": insert_begin, "ds3_insert_end": insert_end,
            "ds3_insert_after": insert_after, "ds3_insert_sorted": insert_sorted, "ds3_delete": delete, "ds3_traverse": traverse}

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for k, f in DIAGRAMS.items():
        with open(os.path.join(OUT, k + ".svg"), "w", encoding="utf-8") as fh:
            fh.write(f())
    print("written", len(DIAGRAMS))
