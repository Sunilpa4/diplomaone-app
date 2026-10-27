"""DI03000021 Data Structures - Unit 4 diagrams: tree terms, binary trees, conversion, traversal, BST, graphs."""
import os
from flowchart_lib import *
from diagrams_DI03000021_u1 import box, BLUE, BLUEF, GREEN, GREENF, ORANGE, ORANGEF, RED, REDF, YEL
from ds_tree import (BN, GN, bst_build, bst_delete, clone, bst_search_path, gen_to_bin, draw_binary, draw_general,
                     draw_graph, inorder, preorder, postorder, pos_general)

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "content", "computer", "sem3", "DI03000021", "diagrams")

TERMS_TREE = GN("A", GN("B", GN("E"), GN("F", GN("J"))), GN("C"), GN("D", GN("G"), GN("H"), GN("I")))
GEN_TREE = GN("A", GN("B", GN("E"), GN("F")), GN("C"), GN("D", GN("G"), GN("H")))
TRAV_TREE = BN("A", BN("B", BN("D"), BN("E", BN("G"))), BN("C", None, BN("F")))
BST_VALS = [45, 25, 65, 15, 35, 55, 75, 30]


def note(x, y, w, lines, fill=BLUEF, stroke=BLUE, size=9.6, lh=15, mono=False):
    b = box(x, y, w, 10 + lh * len(lines), fill, stroke, 7, 1.1)
    for i, s in enumerate(lines):
        c = INK
        if isinstance(s, tuple):
            s, c = s
        b += text(x + 8, y + 15 + i * lh, s.replace(" ", "\u00a0") if mono else s, size, anchor="start", mono=mono, color=c)
    return b


# ------------------------------------------------------------------ 1. tree terms
def terms():
    b = title("Tree: Basic Terminology")
    leaves = {"E", "J", "C", "G", "H", "I"}
    fills = {v: GREENF for v in leaves}
    fills["A"] = ORANGEF
    pos = pos_general(TERMS_TREE, 70, 280, 50, 46)
    # subtree of D (dashed box) drawn first
    b += f'<rect x="230" y="78" width="126" height="94" rx="10" fill="none" stroke="{BLUE}" stroke-width="1.2" stroke-dasharray="4 3"/>'
    s, _ = draw_general(TERMS_TREE, 70, 280, 50, 46, fills=fills)
    b += s
    for i in range(4):
        b += text(14, 50 + i * 46, f"Level {i}", 9.4, anchor="start", color="#666", weight="bold")
    b += text(293, 184, "subtree of D", 9, color=BLUE, weight="bold")
    b += text(pos[id(TERMS_TREE)][0] + 40, 46, "root", 9.6, color=ORANGE, weight="bold")
    b += box(12, 244, 336, 106, "#FCFAFF", "#D9C8F0", 8, 1)
    rows = [("Root: A", "Parent of E, F: B"), ("Leaf: E J C G H I", "Siblings: G, H, I"), ("Degree(A) = 3", "Degree(D) = 3"),
            ("Degree of tree = 3", "Height = 3 (levels 0-3)"), ("Path A-B-F-J", "Depth(J) = 3")]
    for i, (l, r) in enumerate(rows):
        b += text(22, 262 + i * 18, l, 10, anchor="start")
        b += text(186, 262 + i * 18, r, 10, anchor="start")
    return svg(360, 362, b)


# ------------------------------------------------------------------ 2. forest
def forest():
    b = title("Forest")
    whole = GN("R", GN("B", GN("E"), GN("F")), GN("C", GN("G")), GN("D", GN("H"), GN("I")))
    s, pos = draw_general(whole, 60, 240, 52, 42, fills={"R": REDF})
    b += s + text(212, 50, "delete root R", 9.6, color=RED, weight="bold", anchor="start")
    b += arr([(180, 160), (180, 182)], RED)
    x0 = 20
    for t, w in ((GN("B", GN("E"), GN("F")), 120), (GN("C", GN("G")), 80), (GN("D", GN("H"), GN("I")), 120)):
        s, _ = draw_general(t, x0, w, 204, 42)
        b += s
        x0 += w + 10
    b += text(180, 272, "Forest = a set of disjoint trees (here 3 trees)", 10, color="#444")
    b += text(180, 288, "Removing the root of a tree gives a forest", 10, color="#444")
    return svg(360, 300, b)


# ------------------------------------------------------------------ 3. binary tree types
def binary_types():
    b = title("Binary Tree, Strict and Complete")
    trees = [("Binary tree", BN(1, BN(2, None, BN(4)), BN(3, BN(5), None)), "0, 1 or 2 children"),
             ("Strict binary", BN(1, BN(2), BN(3, BN(4), BN(5))), "0 or 2 children"),
             ("Complete binary", BN(1, BN(2, BN(4), BN(5)), BN(3, BN(6), None)), "last level filled left")]
    for k, (name, t, d) in enumerate(trees):
        x = 4 + k * 118
        b += box(x, 32, 114, 176, "#FCFAFF", "#D9C8F0", 8, 1)
        b += text(x + 57, 48, name, 10, weight="bold", color=P)
        s, _ = draw_binary(t, x + 4, 106, 72, 42, 10, size=9.4)
        b += s
        b += text(x + 57, 196, d, 8.8, color="#444")
    b += note(12, 218, 336, ["Binary tree: each node has at most 2 children", "(left child and right child).",
                             "Strict: every non-leaf node has exactly 2 children.", "Complete: all levels full except possibly",
                             "the last, which is filled from the left."], size=9.6)
    return svg(360, 310, b)


# ------------------------------------------------------------------ 4. linked representation
def node_repr():
    b = title("Binary Tree: Linked Representation")
    b += note(12, 32, 180, ["struct tnode {", "  struct tnode *left;", "  int data;", "  struct tnode *right;", "};"],
              "#FCFAFF", "#D9C8F0", 9.4, 14, mono=True)
    b += box(214, 50, 24, 28, "#fff", P, 0, 1.4) + box(238, 50, 36, 28, "#F1E8FC", P, 0, 1.4) + box(274, 50, 24, 28, "#fff", P, 0, 1.4)
    b += text(256, 64, "data", 10, mono=True, weight="bold") + text(226, 90, "left", 8.8, color="#666") + text(286, 90, "right", 8.8, color="#666")

    def tn(x, y, v, lnull=True, rnull=True):
        s = box(x, y, 20, 26, "#fff", P, 0, 1.3) + box(x + 20, y, 30, 26, "#F1E8FC", P, 0, 1.3) + box(x + 50, y, 20, 26, "#fff", P, 0, 1.3)
        s += text(x + 35, y + 13, str(v), 11, mono=True, weight="bold")
        if lnull:
            s += line(f"M{x + 3} {y + 23} L{x + 17} {y + 3}", RED, 1.2)
        if rnull:
            s += line(f"M{x + 53} {y + 23} L{x + 67} {y + 3}", RED, 1.2)
        return s
    b += text(180, 132, "root", 9.4, color=BLUE, weight="bold") + arr([(180, 138), (180, 149)], BLUE)
    b += tn(145, 150, 10, False, False)
    b += tn(40, 214, 20, True, False) + tn(250, 214, 30)
    b += tn(130, 276, 40)
    b += arr([(155, 168), (75, 213)], INK) + arr([(205, 168), (285, 213)], INK) + arr([(100, 232), (164, 275)], INK)
    b += text(180, 322, "Leaf nodes have left = right = NULL", 9.6, color="#444")
    return svg(360, 334, b)


# ------------------------------------------------------------------ 5. general -> binary
def gen2bin():
    b = title("General Tree to Binary Tree")
    b += text(14, 40, "General tree", 10.4, anchor="start", weight="bold", color=P)
    s, _ = draw_general(GEN_TREE, 60, 260, 58, 40, 12, size=10)
    b += s
    b += arr([(180, 150), (180, 168)], RED)
    b += text(14, 178, "Binary tree", 10.4, anchor="start", weight="bold", color=P)
    s, _ = draw_binary(gen_to_bin(GEN_TREE), 60, 280, 186, 30, 11, size=10, lr_labels=True)
    b += s
    b += note(12, 356, 336, ["Rule: Left child, Right sibling", "1. leftmost child  →  LEFT child", "2. next sibling  →  RIGHT child",
                             "3. remove other parent-child links"], size=9.6)
    return svg(360, 430, b)


# ------------------------------------------------------------------ 6. traversal
def traversal():
    b = title("Tree Traversal")
    s, _ = draw_binary(TRAV_TREE, 40, 280, 52, 44, 13)
    b += s
    rows = [("Inorder", "L  N  R", inorder(TRAV_TREE), GREEN), ("Preorder", "N  L  R", preorder(TRAV_TREE), BLUE),
            ("Postorder", "L  R  N", postorder(TRAV_TREE), ORANGE)]
    b += box(12, 206, 336, 94, "#FCFAFF", "#D9C8F0", 8, 1)
    for i, (n, r, o, c) in enumerate(rows):
        y = 228 + i * 26
        b += text(22, y, n, 10.6, anchor="start", weight="bold", color=c)
        b += text(104, y, r, 9.6, anchor="start", mono=True, color="#666")
        b += text(166, y, " ".join(o), 11, anchor="start", mono=True, weight="bold")
    b += text(180, 318, "N = visit node, L = left subtree, R = right subtree", 9.4, color="#444")
    return svg(360, 330, b)


# ------------------------------------------------------------------ 7. BST build
def bst_build_d():
    b = title("Binary Search Tree (BST)")
    b += text(180, 40, "Insert: " + " ".join(map(str, BST_VALS)), 10.6, mono=True, weight="bold", color=BLUE)
    t = bst_build(BST_VALS)
    s, _ = draw_binary(t, 30, 300, 70, 46, 14, hi=[30], edge_hi=[(45, 25), (25, 35), (35, 30)])
    b += s
    b += note(12, 224, 336, ["Left subtree < node < right subtree", ("Insert 30: 30<45 left, 30>25 right,", RED),
                             ("30<35 left  →  new leaf", RED), "Inorder gives sorted order:", "15 25 30 35 45 55 65 75"], size=9.8)
    return svg(360, 314, b)


# ------------------------------------------------------------------ 8. BST search
def bst_search_d():
    b = title("Searching in a BST")
    t = bst_build(BST_VALS)
    p, _ = bst_search_path(t, 30)
    edges = list(zip(p, p[1:]))
    s, _ = draw_binary(t, 30, 300, 52, 46, 14, hi=p, edge_hi=edges)
    b += s
    p2, _ = bst_search_path(t, 60)
    b += note(12, 206, 336, [("Search 30: 45 → 25 → 35 → 30  FOUND", GREEN), "  (4 comparisons)",
                             (f"Search 60: {' → '.join(map(str, p2))} → NULL", RED), "  NOT FOUND (60 > 55, right is NULL)",
                             "Each step goes left or right: O(h)"], size=9.8)
    return svg(360, 296, b)


# ------------------------------------------------------------------ 9. BST delete
def bst_delete_d():
    b = title("Deleting a Node from a BST")
    base = bst_build(BST_VALS)
    cases = [("Case 1: leaf (delete 15)", 15, "just remove it"), ("Case 2: one child (delete 35)", 35, "child 30 takes its place"),
             ("Case 3: two children (delete 25)", 25, "replace by inorder successor 30")]
    y = 34
    for name, v, how in cases:
        b += text(14, y + 10, name, 10, anchor="start", weight="bold", color=RED)
        b += text(346, y + 10, how, 8.8, anchor="end", color="#555")
        s, _ = draw_binary(base, 8, 156, y + 32, 24, 9, hi=[v], hi_fill=REDF, size=8.4)
        b += s
        b += arr([(168, y + 66), (190, y + 66)], RED)
        after = bst_delete(clone(base), v)
        s, _ = draw_binary(after, 196, 156, y + 32, 24, 9, hi=[30] if v in (35, 25) else [], hi_fill=GREENF, size=8.4)
        b += s
        y += 122
    return svg(360, 404, b)


# ------------------------------------------------------------------ 10. graph terms
def graph_terms():
    b = title("Graph: Basic Terms")
    vs = {"A": (50, 80), "B": (160, 60), "C": (270, 80), "D": (110, 180), "E": (230, 180)}
    es = [("A", "B"), ("B", "C"), ("A", "D"), ("B", "D"), ("B", "E"), ("C", "E"), ("D", "E")]
    b += draw_graph(vs, es, hi_edges=[("A", "B"), ("B", "E"), ("E", "C")], r=14)
    b += text(300, 60, "vertex", 9.4, color=P, weight="bold") + text(84, 140, "edge", 9.4, color="#666", weight="bold")
    b += note(12, 212, 336, ["G = (V, E)", "V = {A, B, C, D, E}  (5 vertices)", "E = 7 edges, e.g. (A,B), (B,D)",
                             ("Path A-B-E-C (red)", RED), "Cycle: B-D-E-B (starts and ends at B)", "Degree(B) = 4, Degree(A) = 2",
                             "Adjacent: A and B (joined by an edge)"], size=9.8)
    return svg(360, 330, b)


# ------------------------------------------------------------------ 11. graph types
def graph_types():
    b = title("Types of Graph")
    pan = [("Undirected", False, None, [("A", "B"), ("B", "C"), ("C", "A")]),
           ("Directed (digraph)", True, None, [("A", "B"), ("B", "C"), ("C", "A")]),
           ("Weighted", False, {("A", "B"): 4, ("B", "C"): 7, ("C", "A"): 2}, [("A", "B"), ("B", "C"), ("C", "A")])]
    for k, (name, d, w, es) in enumerate(pan):
        x = 4 + k * 118
        b += box(x, 30, 114, 132, "#FCFAFF", "#D9C8F0", 8, 1) + text(x + 57, 46, name, 9.8, weight="bold", color=P)
        vs = {"A": (x + 57, 68), "B": (x + 22, 136), "C": (x + 92, 136)}
        b += draw_graph(vs, es, directed=d, weights=w, r=12, size=10)
    # connected / disconnected / complete
    y = 172
    b += box(4, y, 114, 132, "#FCFAFF", "#D9C8F0", 8, 1) + text(61, y + 16, "Connected", 9.8, weight="bold", color=P)
    vs = {"A": (30, y + 46), "B": (92, y + 46), "C": (30, y + 106), "D": (92, y + 106)}
    b += draw_graph(vs, [("A", "B"), ("A", "C"), ("C", "D")], r=12, size=10)
    b += box(122, y, 114, 132, "#FCFAFF", "#D9C8F0", 8, 1) + text(179, y + 16, "Disconnected", 9.8, weight="bold", color=P)
    vs = {"A": (148, y + 46), "B": (210, y + 46), "C": (148, y + 106), "D": (210, y + 106)}
    b += draw_graph(vs, [("A", "B"), ("C", "D")], r=12, size=10)
    b += box(240, y, 116, 132, "#FCFAFF", "#D9C8F0", 8, 1) + text(298, y + 16, "Complete (K4)", 9.8, weight="bold", color=P)
    vs = {"A": (266, y + 46), "B": (330, y + 46), "C": (266, y + 106), "D": (330, y + 106)}
    b += draw_graph(vs, [("A", "B"), ("A", "C"), ("A", "D"), ("B", "C"), ("B", "D"), ("C", "D")], r=12, size=10)
    b += text(180, 322, "Complete graph with n vertices has n(n-1)/2 edges", 9.6, color="#444")
    return svg(360, 334, b)


DIAGRAMS = {"ds4_terms": terms, "ds4_forest": forest, "ds4_binary_types": binary_types, "ds4_node_repr": node_repr,
            "ds4_gen2bin": gen2bin, "ds4_traversal": traversal, "ds4_bst_build": bst_build_d, "ds4_bst_search": bst_search_d,
            "ds4_bst_delete": bst_delete_d, "ds4_graph_terms": graph_terms, "ds4_graph_types": graph_types}

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for k, f in DIAGRAMS.items():
        with open(os.path.join(OUT, k + ".svg"), "w", encoding="utf-8") as fh:
            fh.write(f())
    print("written", len(DIAGRAMS))
