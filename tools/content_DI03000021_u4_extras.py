"""DI03000021 Unit 4 extras: algorithms, numericals (all computed with ds_tree), viva, exam."""
from c_content import SXE, VE, XE, G
from content_DI03000021_u4_notes_a import SN as SNA
from content_DI03000021_u4_notes_b import SN as SNB
from ds_expr import table
from ds_tree import (BN, bst_build, bst_insert, bst_delete, bst_search_path, clone, gen_to_bin, g_preorder,
                     inorder, preorder, postorder, height, count, leaves)
from diagrams_DI03000021_u4 import TERMS_TREE, GEN_TREE, TRAV_TREE

SNX = {**SNA, **SNB}


def A(name, key, terms=""):
    return SXE(name, SNX[key].strip("\n"), terms)


def N(id_, q, a):
    return {"id": id_, "q": {"en": q}, "a": {"en": a}}


def J(lst):
    return " ".join(map(str, lst))


ALGORITHMS = [
    G("Traversal", [
        A("Inorder (L N R)", "alg_in", "BST inorder = ascending order."),
        A("Preorder (N L R)", "alg_pre", "Root comes first."),
        A("Postorder (L R N)", "alg_post", "Root comes last."),
        A("General to binary tree", "alg_g2b", "Left child, right sibling."),
    ]),
    G("Binary Search Tree", [
        A("BST insert", "alg_bins", "New node is always a leaf. O(h)."),
        A("BST search", "alg_bsearch", "O(h): O(log n) balanced, O(n) skewed."),
        A("BST delete", "alg_bdel", "Successor = leftmost node of right subtree."),
    ]),
    G("Formulas", [
        SXE("Binary tree", "Max nodes at level l  = 2^l\nMax nodes, height h  = 2^(h+1) - 1\nMin height, n nodes  = floor(log2 n)\nLeaves = (nodes with 2 children) + 1", ""),
        SXE("Graph", "Sum of degrees = 2 x edges\nComplete graph K_n: n(n-1)/2 edges\nComplete digraph: n(n-1) edges\nTree with n nodes: n - 1 edges", ""),
    ]),
]


# ---------- helpers ----------
def node_table(t):
    rows = []

    def walk(n):
        if n:
            rows.append((n.v, n.l.v if n.l else "-", n.r.v if n.r else "-"))
            walk(n.l); walk(n.r)
    walk(t)
    return table(["Node", "Left child", "Right child"], rows)


def insert_paths(vals):
    root, rows = None, []
    for v in vals:
        if root is None:
            rows.append((v, "root")); root = BN(v); continue
        p, steps = root, []
        while True:
            if v < p.v:
                steps.append(f"{v}&lt;{p.v} L")
                if p.l is None:
                    p.l = BN(v); break
                p = p.l
            else:
                steps.append(f"{v}&gt;{p.v} R")
                if p.r is None:
                    p.r = BN(v); break
                p = p.r
        rows.append((v, ", ".join(steps)))
    return root, table(["Insert", "Path (L = left, R = right)"], rows)


def bracket(t, kind):
    """show traversal subtree-wise: inorder of A(B..)(C..) = (in B) A (in C)"""
    def f(n):
        if n is None:
            return ""
        if not n.l and not n.r:
            return str(n.v)
        L, R = f(n.l), f(n.r)
        L = f"({L})" if L and (n.l.l or n.l.r) else L
        R = f"({R})" if R and (n.r.l or n.r.r) else R
        parts = {"in": [L, str(n.v), R], "pre": [str(n.v), L, R], "post": [L, R, str(n.v)]}[kind]
        return " ".join(x for x in parts if x)
    return f(t)


def build_from(inord, preord, rows, depth=0):
    if not inord:
        return None
    r = preord[0]
    i = inord.index(r)
    rows.append((r, J(inord[:i]) or "-", J(inord[i + 1:]) or "-"))
    t = BN(r)
    t.l = build_from(inord[:i], preord[1:1 + i], rows, depth + 1)
    t.r = build_from(inord[i + 1:], preord[1 + i:], rows, depth + 1)
    return t


def same(a, b):
    if a is None or b is None:
        return a is b
    return a.v == b.v and same(a.l, b.l) and same(a.r, b.r)


# n1: terms table
def g_rows(g, parent="-", lvl=0, out=None):
    out = out if out is not None else []

    def h(n):
        return 0 if not n.ch else 1 + max(h(c) for c in n.ch)
    out.append((g.v, parent, ", ".join(c.v for c in g.ch) or "-", len(g.ch), lvl, h(g), "leaf" if not g.ch else "internal"))
    for c in g.ch:
        g_rows(c, g.v, lvl + 1, out)
    return out


R1 = g_rows(TERMS_TREE)
assert len(R1) == 10 and max(r[4] for r in R1) == 3

# n2
B2 = gen_to_bin(GEN_TREE)
assert preorder(B2) == g_preorder(GEN_TREE)

# n4: expression tree (A+B)*(C-D/E)
EXP = BN("*", BN("+", BN("A"), BN("B")), BN("-", BN("C"), BN("/", BN("D"), BN("E"))))
assert J(postorder(EXP)) == "A B + C D E / - *"

# n5
V5 = [50, 30, 70, 20, 40, 60, 80, 35, 65]
T5, P5 = insert_paths(V5)
assert inorder(T5) == sorted(V5)

# n6 months
MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
T6 = bst_build(MONTHS)

# n7 delete sequence on T5
def del_rows():
    t, rows = clone(T5), []
    for v in (20, 30, 50):
        p = t
        while p.v != v:
            p = p.l if v < p.v else p.r
        k = (p.l is not None) + (p.r is not None)
        case = {0: "Case 1: leaf", 1: "Case 2: one child", 2: "Case 3: two children"}[k]
        how = "removed"
        if k == 1:
            how = f"replaced by child {(p.l or p.r).v}"
        if k == 2:
            s = p.r
            while s.l:
                s = s.l
            how = f"replaced by inorder successor {s.v}"
        t = bst_delete(t, v)
        rows.append((v, case, how, J(preorder(t)), J(inorder(t))))
    return t, table(["Delete", "Case", "Action", "Preorder after", "Inorder after"], rows)


T7, D7 = del_rows()

# n8
R8 = []
T8 = build_from(inorder(TRAV_TREE), preorder(TRAV_TREE), R8)
assert same(T8, TRAV_TREE)

# n9 graph degrees
ES = [("A", "B"), ("B", "C"), ("A", "D"), ("B", "D"), ("B", "E"), ("C", "E"), ("D", "E")]
DEG = {v: sum(v in e for e in ES) for v in "ABCDE"}
assert sum(DEG.values()) == 2 * len(ES)

# n10 digraph
DE = [("A", "B"), ("B", "C"), ("C", "A"), ("C", "D"), ("D", "B")]
IO = [(v, sum(b == v for a, b in DE), sum(a == v for a, b in DE)) for v in "ABCD"]

NUMERICALS = [
    N("ds4n1", "For the tree A(B(E, F(J)), C, D(G, H, I)) (the terminology diagram), find for every node: parent, children, degree, level, height and type. Also find the root, leaves, degree of the tree and height of the tree.",
      table(["Node", "Parent", "Children", "Degree", "Level", "Height", "Type"], R1)
      + "<p>Root = A. Leaves = E, J, C, G, H, I. Internal = A, B, F, D.<br>Degree of tree = 3. Height of tree = 3 (levels 0 to 3). Nodes = 10, edges = 9 (n − 1).</p>"),
    N("ds4n2", "Convert the general tree A(B(E, F), C, D(G, H)) into a binary tree.",
      "<p>Rule: first child → LEFT, next sibling → RIGHT.</p>" + node_table(B2)
      + f"<p>Check: preorder of the general tree = {J(g_preorder(GEN_TREE))} = preorder of the binary tree = {J(preorder(B2))}.</p>"),
    N("ds4n3", "Find the inorder, preorder and postorder traversal of the binary tree A(B(D, E(G, –)), C(–, F)).",
      table(["Traversal", "Subtree-wise", "Result"], [("Inorder (LNR)", bracket(TRAV_TREE, "in"), J(inorder(TRAV_TREE))),
                                                      ("Preorder (NLR)", bracket(TRAV_TREE, "pre"), J(preorder(TRAV_TREE))),
                                                      ("Postorder (LRN)", bracket(TRAV_TREE, "post"), J(postorder(TRAV_TREE)))])
      + "<p>Brackets show the subtrees: for inorder, write the whole left subtree, then the root, then the right subtree.</p>"),
    N("ds4n4", "Draw the expression tree for (A + B) * (C − D / E) and write its inorder, preorder and postorder.",
      "<p>The operator applied last (*) is the root. Its left subtree is A + B; its right subtree is C − D / E, whose root is − with right child D / E.</p>"
      + node_table(EXP)
      + table(["Traversal", "Result", "Gives"], [("Inorder", J(inorder(EXP)), "infix (without brackets)"),
                                                 ("Preorder", J(preorder(EXP)), "prefix"), ("Postorder", J(postorder(EXP)), "postfix")])),
    N("ds4n5", f"Construct a binary search tree by inserting {', '.join(map(str, V5))}. Write its traversals and height.",
      P5 + "<p><b>Resulting BST:</b></p>" + node_table(T5)
      + table(["Traversal", "Result"], [("Inorder", J(inorder(T5))), ("Preorder", J(preorder(T5))), ("Postorder", J(postorder(T5)))])
      + f"<p>Height = {height(T5)} (50 → 30 → 40 → 35). Leaves = {J(leaves(T5))}. Inorder is sorted, so the BST is correct.</p>"),
    N("ds4n6", "Construct a BST for the months: " + ", ".join(MONTHS) + " (alphabetical order).",
      "<p>Compare strings alphabetically (like strcmp): Apr &lt; Aug &lt; Dec &lt; Feb &lt; Jan &lt; Jul &lt; Jun &lt; Mar &lt; May &lt; Nov &lt; Oct &lt; Sep.</p>"
      + node_table(T6)
      + f"<p>Inorder: {J(inorder(T6))} (alphabetical).<br>Preorder: {J(preorder(T6))}.<br>Height = {height(T6)}, leaves = {J(leaves(T6))}.</p>"),
    N("ds4n7", "From the BST of the previous example (50, 30, 70, 20, 40, 60, 80, 35, 65), delete 20, then 30, then 50. Write the case and the traversals after each deletion.",
      D7 + "<p>When 50 is deleted, the successor 60 is copied into the root, and 60's right child 65 takes 60's old place.</p>"),
    N("ds4n8", f"Construct the binary tree whose inorder is {J(inorder(TRAV_TREE))} and preorder is {J(preorder(TRAV_TREE))}.",
      "<p>Take the next preorder value as the root; split the inorder around it.</p>"
      + table(["Root (from preorder)", "Left part (inorder)", "Right part (inorder)"], R8)
      + "<p><b>Tree:</b></p>" + node_table(T8) + f"<p>Check, postorder: {J(postorder(T8))}.</p>"),
    N("ds4n9", "For the undirected graph with edges (A,B), (B,C), (A,D), (B,D), (B,E), (C,E), (D,E), find the degree of each vertex and verify the handshake rule.",
      table(["Vertex", "Degree"], list(DEG.items()))
      + f"<p>Sum of degrees = {' + '.join(map(str, DEG.values()))} = {sum(DEG.values())} = 2 × {len(ES)} edges. ✓</p>"),
    N("ds4n10", "For the directed graph with edges A→B, B→C, C→A, C→D, D→B, find the in-degree and out-degree of each vertex.",
      table(["Vertex", "In-degree", "Out-degree"], IO)
      + f"<p>Total in-degree = total out-degree = {len(DE)} = number of edges.</p>"),
    N("ds4n11", "Find the number of edges in a complete undirected graph and in a complete directed graph with 4, 5, 6 and 10 vertices.",
      table(["n", "Undirected n(n−1)/2", "Directed n(n−1)"], [(n, n * (n - 1) // 2, n * (n - 1)) for n in (4, 5, 6, 10)])),
    N("ds4n12", "Find: (a) maximum nodes at level 3 of a binary tree, (b) maximum nodes in a binary tree of height 3 and of height 4, (c) minimum height of a binary tree with 20 nodes, (d) leaves of a strict binary tree with 15 nodes.",
      table(["Part", "Formula", "Answer"], [("(a)", "2^l = 2^3", 2 ** 3), ("(b) h = 3", "2^(h+1) − 1 = 2^4 − 1", 2 ** 4 - 1),
                                            ("(b) h = 4", "2^5 − 1", 2 ** 5 - 1), ("(c)", "⌊log2 20⌋", 4),
                                            ("(d)", "n = 2L − 1 → L = (15 + 1)/2", 8)])
      + "<p>(c) A tree of height 3 holds at most 15 nodes, so 20 nodes need height 4. (Root at level 0, height in edges.)</p>"),
]

VIVA = [
    G("Tree Terms", [
        VE("What is a tree?", "A non-linear hierarchical data structure of nodes with one root, in which every other node has exactly one parent."),
        VE("What is a root node?", "The topmost node of a tree; it has no parent."),
        VE("What is a leaf node?", "A node with no children (degree 0)."),
        VE("What are siblings?", "Nodes having the same parent."),
        VE("What is the degree of a node?", "The number of children (subtrees) of that node."),
        VE("What is the in-degree of the root?", "Zero; every other node in a tree has in-degree 1."),
        VE("Define height and depth.", "Depth of a node = length of the path from the root to it; height = length of the longest path from it down to a leaf."),
        VE("How many edges does a tree with n nodes have?", "n − 1."),
        VE("What is a forest?", "A set of disjoint trees; removing the root of a tree gives a forest."),
    ]),
    G("Binary Tree and Traversal", [
        VE("What is a binary tree?", "A tree in which every node has at most two children: left and right."),
        VE("What is a strict binary tree?", "A binary tree in which every node has 0 or 2 children."),
        VE("What is a complete binary tree?", "All levels are full except possibly the last, which is filled from the left."),
        VE("Maximum nodes in a binary tree of height h?", "2^(h+1) − 1."),
        VE("How is a general tree converted to a binary tree?", "First child becomes the left child and the next sibling becomes the right child."),
        VE("What is tree traversal?", "Visiting every node exactly once in a fixed order."),
        VE("Give the order of the three traversals.", "Inorder L N R, preorder N L R, postorder L R N."),
        VE("Which traversal gives the root first and which last?", "Preorder gives it first; postorder gives it last."),
        VE("Which traversals are needed to build a unique tree?", "Inorder with preorder, or inorder with postorder."),
    ]),
    G("BST", [
        VE("What is a BST?", "A binary tree where left subtree values are smaller and right subtree values are larger than the node, for every node."),
        VE("Which traversal of a BST gives sorted output?", "Inorder."),
        VE("Where is a new node inserted in a BST?", "Always as a leaf, at the NULL position reached by the search path."),
        VE("Where are the minimum and maximum in a BST?", "Minimum is the leftmost node; maximum is the rightmost node."),
        VE("What are the cases of BST deletion?", "Leaf node, node with one child, node with two children."),
        VE("What is the inorder successor?", "The smallest node in the right subtree: go right once, then left as far as possible."),
        VE("What is the time complexity of BST search?", "O(h): O(log n) when balanced, O(n) when skewed."),
    ]),
    G("Graph", [
        VE("What is a graph?", "A non-linear structure G = (V, E) of vertices and edges connecting them."),
        VE("Difference between directed and undirected graph?", "Directed edges have a direction (arrow); undirected edges work both ways."),
        VE("What is a path and a cycle?", "A path is a sequence of connected vertices; a cycle is a path that starts and ends at the same vertex."),
        VE("What is a complete graph?", "A graph in which every vertex is connected to every other vertex; it has n(n−1)/2 edges."),
        VE("What is a weighted graph?", "A graph in which each edge carries a value such as distance or cost."),
        VE("What is a connected graph?", "A graph in which there is a path between every pair of vertices."),
        VE("Name two ways to represent a graph.", "Adjacency matrix and adjacency list."),
        VE("Give one difference between tree and graph.", "A tree has a root and no cycles; a graph has no root and may have cycles."),
    ]),
]

EXAM_QS = [
    XE("Define the following terms: root, leaf, sibling, degree, level, depth, height.", 4),
    XE("Explain in-degree, out-degree, path and subtree with an example.", 3),
    XE("Define binary tree, strict binary tree and complete binary tree with diagrams.", 3),
    XE("What is a forest? Explain with an example.", 3),
    XE("Explain the conversion of a general tree into a binary tree with an example.", 4),
    XE("Explain inorder, preorder and postorder traversals with algorithms and an example.", 7),
    XE("Write the inorder, preorder and postorder traversals of a given binary tree.", 3),
    XE("Construct a binary tree from given inorder and preorder traversals.", 4),
    XE("What is a binary search tree? Construct a BST for 50, 30, 70, 20, 40, 60, 80, 35, 65.", 4),
    XE("Write an algorithm to insert a node in a binary search tree.", 4),
    XE("Write an algorithm to search a node in a binary search tree.", 3),
    XE("Explain the deletion of a node from a BST with all cases.", 7),
    XE("Write a C program to construct a BST and display its inorder traversal.", 7),
    XE("Define graph. Explain vertex, edge, path and cycle.", 3),
    XE("Explain types of graphs: directed, undirected, connected, complete and weighted.", 4),
    XE("Explain the adjacency matrix and adjacency list representation of a graph.", 4),
    XE("Differentiate tree and graph.", 3),
    XE("Give applications of trees and graphs.", 3),
]
