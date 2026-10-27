"""Tree helper for DS Unit 4: BST insert/delete/search, traversals, general->binary conversion, SVG drawing.
All diagrams / numericals of unit 4 are produced from this one verified logic."""
from flowchart_lib import text, line, arr, P, INK

BLUE, GREEN, ORANGE, RED = "#1565C0", "#2E7D32", "#E07B00", "#C62828"
NFILL, HIFILL = "#F1E8FC", "#FFF3B0"


class BN:                      # binary node
    def __init__(s, v, l=None, r=None):
        s.v, s.l, s.r = v, l, r


class GN:                      # general-tree node
    def __init__(s, v, *ch):
        s.v, s.ch = v, list(ch)


# ---------------- BST ----------------
def bst_insert(root, v):
    if root is None:
        return BN(v)
    if v < root.v:
        root.l = bst_insert(root.l, v)
    elif v > root.v:
        root.r = bst_insert(root.r, v)
    return root


def bst_build(vals):
    root = None
    for v in vals:
        root = bst_insert(root, v)
    return root


def bst_search_path(root, v):
    path = []
    while root:
        path.append(root.v)
        if v == root.v:
            return path, True
        root = root.l if v < root.v else root.r
    return path, False


def bst_delete(root, v):
    """standard: leaf -> remove; one child -> replace by child; two children -> inorder successor."""
    if root is None:
        return None
    if v < root.v:
        root.l = bst_delete(root.l, v)
    elif v > root.v:
        root.r = bst_delete(root.r, v)
    else:
        if root.l is None:
            return root.r
        if root.r is None:
            return root.l
        s = root.r
        while s.l:
            s = s.l
        root.v = s.v
        root.r = bst_delete(root.r, s.v)
    return root


def clone(t):
    return None if t is None else BN(t.v, clone(t.l), clone(t.r))


def inorder(t):
    return inorder(t.l) + [t.v] + inorder(t.r) if t else []


def preorder(t):
    return [t.v] + preorder(t.l) + preorder(t.r) if t else []


def postorder(t):
    return postorder(t.l) + postorder(t.r) + [t.v] if t else []


def height(t):          # height counted in edges; empty = -1, single node = 0
    return -1 if t is None else 1 + max(height(t.l), height(t.r))


def count(t):
    return 0 if t is None else 1 + count(t.l) + count(t.r)


def leaves(t):
    if t is None:
        return []
    if not t.l and not t.r:
        return [t.v]
    return leaves(t.l) + leaves(t.r)


# ---------------- general tree -> binary (left child, right sibling) ----------------
def gen_to_bin(g):
    if g is None:
        return None
    b = BN(g.v)
    kids = [gen_to_bin(c) for c in g.ch]
    for i in range(len(kids) - 1):
        kids[i].r = kids[i + 1]
    b.l = kids[0] if kids else None
    return b


def g_preorder(g):
    return [g.v] + sum((g_preorder(c) for c in g.ch), [])


def g_postorder(g):
    return sum((g_postorder(c) for c in g.ch), []) + [g.v]


# ---------------- layout + drawing ----------------
def pos_binary(t, x0, w, y0, lh):
    order, depth = [], {}

    def walk(n, d):
        if n:
            walk(n.l, d + 1); order.append(n); depth[id(n)] = d; walk(n.r, d + 1)
    walk(t, 0)
    k = len(order)
    return {id(n): (x0 + (i + 0.5) * w / k, y0 + depth[id(n)] * lh) for i, n in enumerate(order)}


def pos_general(g, x0, w, y0, lh):
    leaves_ = []

    def lv(n):
        if not n.ch:
            leaves_.append(n)
        for c in n.ch:
            lv(c)
    lv(g)
    slot = w / len(leaves_)
    pos = {}

    def place(n, d):
        if not n.ch:
            i = leaves_.index(n)
            x = x0 + (i + 0.5) * slot
        else:
            xs = [place(c, d + 1) for c in n.ch]
            x = (xs[0] + xs[-1]) / 2
        pos[id(n)] = (x, y0 + d * lh)
        return x
    place(g, 0)
    return pos


def _circle(x, y, v, r, fill, stroke, size):
    return (f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="1.5"/>'
            + text(x, y, str(v), size, weight="bold"))


def _edge(x1, y1, x2, y2, r, color, w=1.5, arrow=False):
    import math
    d = math.hypot(x2 - x1, y2 - y1) or 1
    ux, uy = (x2 - x1) / d, (y2 - y1) / d
    a, b = (x1 + ux * r, y1 + uy * r), (x2 - ux * r, y2 - uy * r)
    if arrow:
        return arr([a, b], color)
    return line(f"M{a[0]:.1f} {a[1]:.1f} L{b[0]:.1f} {b[1]:.1f}", color, w)


def draw_binary(t, x0, w, y0, lh=44, r=13, hi=None, hi_fill=HIFILL, edge_hi=None, size=11, lr_labels=False, stroke=P):
    hi, edge_hi = set(hi or []), set(edge_hi or [])
    pos = pos_binary(t, x0, w, y0, lh)
    s = ""

    def walk(n):
        nonlocal s
        if not n:
            return
        x, y = pos[id(n)]
        for c, side in ((n.l, "L"), (n.r, "R")):
            if c:
                cx, cy = pos[id(c)]
                hot = (n.v, c.v) in edge_hi
                s += _edge(x, y, cx, cy, r, RED if hot else "#777", 2.2 if hot else 1.5)
                if lr_labels:
                    s += text((x + cx) / 2 + (-7 if side == "L" else 7), (y + cy) / 2 - 4, side, 8.6, color=ORANGE, weight="bold")
            walk(c)
    walk(t)

    def nodes(n):
        nonlocal s
        if n:
            x, y = pos[id(n)]
            s += _circle(x, y, n.v, r, hi_fill if n.v in hi else NFILL, stroke, size)
            nodes(n.l); nodes(n.r)
    nodes(t)
    return s, pos


def draw_general(g, x0, w, y0, lh=44, r=13, hi=None, hi_fill=HIFILL, size=11, fills=None):
    hi = set(hi or [])
    fills = fills or {}
    pos = pos_general(g, x0, w, y0, lh)
    s = ""

    def edges(n):
        nonlocal s
        x, y = pos[id(n)]
        for c in n.ch:
            cx, cy = pos[id(c)]
            s += _edge(x, y, cx, cy, r, "#777")
            edges(c)

    def nodes(n):
        nonlocal s
        x, y = pos[id(n)]
        s += _circle(x, y, n.v, r, fills.get(n.v, hi_fill if n.v in hi else NFILL), P, size)
        for c in n.ch:
            nodes(c)
    edges(g); nodes(g)
    return s, pos


def draw_graph(vs, es, directed=False, weights=None, r=13, hi_edges=None, hi_nodes=None, size=11):
    """vs: {name: (x, y)}, es: [(a, b)]"""
    hi_edges, hi_nodes = set(hi_edges or []), set(hi_nodes or [])
    weights = weights or {}
    s = ""
    for a, b in es:
        (x1, y1), (x2, y2) = vs[a], vs[b]
        hot = (a, b) in hi_edges or (b, a) in hi_edges
        s += _edge(x1, y1, x2, y2, r + (1 if directed else 0), RED if hot else "#666", 2.2 if hot else 1.5, arrow=directed)
        if (a, b) in weights:
            mx, my = (x1 + x2) / 2, (y1 + y2) / 2
            s += f'<rect x="{mx - 9:.1f}" y="{my - 8:.1f}" width="18" height="15" rx="3" fill="#fff"/>'
            s += text(mx, my, str(weights[(a, b)]), 9.6, color=BLUE, weight="bold")
    for v, (x, y) in vs.items():
        s += _circle(x, y, v, r, HIFILL if v in hi_nodes else NFILL, P, size)
    return s


if __name__ == "__main__":
    t = bst_build([45, 25, 65, 15, 35, 55, 75, 30])
    print("in", inorder(t)); print("pre", preorder(t)); print("post", postorder(t))
    print("h", height(t), "n", count(t), "leaves", leaves(t))
    print("search 30", bst_search_path(t, 30), "search 60", bst_search_path(t, 60))
    t2 = bst_delete(clone(t), 25); print("del 25 in", inorder(t2), "pre", preorder(t2))
    g = GN("A", GN("B", GN("E"), GN("F")), GN("C"), GN("D", GN("G"), GN("H")))
    b = gen_to_bin(g); print("gen pre", g_preorder(g), "bin pre", preorder(b), "bin in", inorder(b))
