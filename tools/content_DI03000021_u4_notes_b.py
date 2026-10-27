"""DI03000021 Unit 4 notes part B: 4.3 binary search tree; 4.4 graph."""
from c_content import make_TE

SN = {
    "alg_bins": r'''
Algorithm BSTINSERT(ROOT, ITEM)
Step 1: [Create node]
        NEW = getnode()
        INFO(NEW) = ITEM
        LEFT(NEW) = RIGHT(NEW) = NULL
Step 2: If ROOT = NULL then
          Set ROOT = NEW and Exit
Step 3: Set PTR = ROOT
Step 4: Repeat
          If ITEM < INFO(PTR) then
            If LEFT(PTR) = NULL then
              LEFT(PTR) = NEW, Exit
            Else PTR = LEFT(PTR)
          Else If ITEM > INFO(PTR) then
            If RIGHT(PTR) = NULL then
              RIGHT(PTR) = NEW, Exit
            Else PTR = RIGHT(PTR)
          Else
            Write "Duplicate", Exit
''',
    "c_bins": r'''
struct tnode *insert(struct tnode *t,
                     int x)
{
    if (t == NULL) {
        t = malloc(sizeof(struct tnode));
        t->data = x;
        t->left = t->right = NULL;
    } else if (x < t->data)
        t->left = insert(t->left, x);
    else if (x > t->data)
        t->right = insert(t->right, x);
    return t;
}
''',
    "alg_bsearch": r'''
Algorithm BSTSEARCH(ROOT, ITEM)
Step 1: Set PTR = ROOT
Step 2: Repeat while PTR != NULL
          If ITEM = INFO(PTR) then
            Write "Found" and Exit
          Else If ITEM < INFO(PTR) then
            Set PTR = LEFT(PTR)
          Else
            Set PTR = RIGHT(PTR)
Step 3: Write "Not found"
Step 4: Exit
''',
    "alg_bdel": r'''
Algorithm BSTDELETE(ROOT, ITEM)
Step 1: Search ITEM; let PTR be the
        node and PAR its parent.
        If not found: Write "Not
        found" and Exit
Step 2: [Case 1: leaf]
        If PTR has no child then
          set PAR's link to NULL
Step 3: [Case 2: one child]
        If PTR has one child then
          set PAR's link to that child
Step 4: [Case 3: two children]
        Find SUC = inorder successor
        (leftmost node of RIGHT(PTR))
        INFO(PTR) = INFO(SUC)
        Delete SUC (case 1 or 2)
Step 5: Free the removed node, Exit
''',
}
T0 = make_TE(SN)


def T(h, b, examples=None, **kw):
    d = T0(h, b, **kw)
    if examples:
        d["examples"] = examples
    return d


SEC_4_3 = {
    "title": {"en": "4.3 Binary Search Tree (BST)"},
    "items": [
        T("4.3.1 Binary Search Tree: Definition and Construction",
          r"""<p>A <b>binary search tree</b> is a binary tree in which, for <b>every node</b>:</p>
<ul><li>all values in its <b>left subtree</b> are <b>less than</b> the node's value,</li>
<li>all values in its <b>right subtree</b> are <b>greater than</b> the node's value, and</li>
<li>the left and right subtrees are also binary search trees.</li></ul>
<p>Duplicate values are normally not allowed.</p>
<h4>Construction</h4>
<p>Insert the values one by one. The first value becomes the root. For each next value, start at the root and move <b>left if smaller</b>, <b>right if larger</b>, until an empty (NULL) place is found; the new node is placed there as a leaf.</p>
<p><b>Example:</b> insert 45, 25, 65, 15, 35, 55, 75, 30.</p>
<ul><li>45 is the root. 25 &lt; 45 → left. 65 &gt; 45 → right.</li>
<li>15 → left of 25. 35 → right of 25. 55 → left of 65. 75 → right of 65.</li>
<li>30: 30 &lt; 45 left, 30 &gt; 25 right, 30 &lt; 35 left → left child of 35.</li>
<li>Inorder: 15 25 30 35 45 55 65 75 (sorted).</li></ul>
<h4>Advantages</h4>
<ul><li>Searching, insertion and deletion take <b>O(h)</b> time: O(log n) for a balanced tree.</li>
<li>Inorder traversal gives sorted data.</li>
<li>Disadvantage: if the data is inserted in sorted order, the BST becomes <b>skewed</b> (like a linked list) and operations become O(n).</li></ul>""",
          diagram="ds4_bst_build", programs=["ds4p3"], examples=["ds4n5", "ds4n6"], key=True),

        T("4.3.2 Insertion of a Node in a BST",
          r"""@@alg_bins@@
<h4>Recursive C function</h4>
@@c_bins@@
<ul><li>A new node is always inserted as a <b>leaf</b>.</li>
<li>The path followed is the same path a search for that value would follow.</li>
<li>Time: O(h).</li></ul>""",
          programs=["ds4p3"], key=True),

        T("4.3.3 Searching a Node in a BST",
          r"""<p>Compare the item with the root. If equal, the search is successful. If smaller, search only the <b>left</b> subtree; if larger, search only the <b>right</b> subtree. Half of the remaining tree is skipped at each step (like binary search).</p>
@@alg_bsearch@@
<ul><li>Example: search 30 → 45, 25, 35, 30: found in 4 comparisons.</li>
<li>Search 60 → 45, 65, 55, then the right of 55 is NULL: not found.</li>
<li>The <b>minimum</b> value is the leftmost node and the <b>maximum</b> is the rightmost node.</li>
<li>Time: best O(1), average O(log n), worst O(n) (skewed tree).</li></ul>""",
          diagram="ds4_bst_search", programs=["ds4p4", "ds4p6"], key=True),

        T("4.3.4 Deletion of a Node from a BST",
          r"""<p>After deletion the tree must still be a BST. There are <b>three cases</b>:</p>
<h4>Case 1: the node is a leaf</h4>
<p>Simply remove it: the parent's link becomes NULL. Example: delete 15.</p>
<h4>Case 2: the node has one child</h4>
<p>Connect the parent directly to the node's only child, then remove the node. Example: delete 35 (child 30) → 30 takes the place of 35.</p>
<h4>Case 3: the node has two children</h4>
<p>Replace the node's value with its <b>inorder successor</b> (the smallest value in its right subtree: go right once, then left as far as possible), and then delete the successor (which is case 1 or 2). Example: delete 25 → successor 30 replaces 25.</p>
<p>(The <b>inorder predecessor</b>, the largest value in the left subtree, can be used instead.)</p>
@@alg_bdel@@""",
          diagram="ds4_bst_delete", programs=["ds4p5"], examples=["ds4n7"], key=True),

        T("4.3.5 Complete BST Program and Applications of Trees",
          r"""<p>The menu-driven program below combines insert, search, delete and the three traversals.</p>
<h4>Applications of trees</h4>
<ul><li><b>BST:</b> fast searching, sorting (inorder) and dictionaries.</li>
<li>File systems and folder hierarchy (general tree).</li>
<li><b>Expression trees</b> in compilers (infix, prefix, postfix).</li>
<li>Database indexing (B-trees), heaps for priority queues.</li>
<li>Decision trees, game trees, organisation charts.</li>
<li>Huffman coding trees for data compression.</li></ul>""",
          programs=["ds4p8", "ds4p7"]),
    ],
}

SEC_4_4 = {
    "title": {"en": "4.4 Graph"},
    "items": [
        T("4.4.1 Graph: Fundamental Concepts",
          r"""<p>A <b>graph</b> G = (V, E) is a non-linear data structure that consists of a set of <b>vertices</b> V and a set of <b>edges</b> E, where each edge connects a pair of vertices.</p>
<table>
<tr><th>Term</th><th>Meaning</th></tr>
<tr><td><b>Vertex (node)</b></td><td>a point of the graph that stores data, e.g. A, B, C</td></tr>
<tr><td><b>Edge (arc)</b></td><td>a line joining two vertices, written (A, B)</td></tr>
<tr><td><b>Adjacent vertices</b></td><td>two vertices joined by an edge</td></tr>
<tr><td><b>Degree</b></td><td>number of edges connected to a vertex (undirected graph)</td></tr>
<tr><td><b>In-degree / Out-degree</b></td><td>number of edges coming into / going out of a vertex (directed graph)</td></tr>
<tr><td><b>Path</b></td><td>a sequence of vertices in which each consecutive pair is joined by an edge, e.g. A–B–E–C</td></tr>
<tr><td><b>Cycle</b></td><td>a path that starts and ends at the same vertex with no edge repeated, e.g. B–D–E–B</td></tr>
<tr><td><b>Isolated vertex</b></td><td>a vertex with degree 0</td></tr>
<tr><td><b>Self-loop</b></td><td>an edge from a vertex to itself</td></tr>
</table>
<p>In an undirected graph, the <b>sum of the degrees of all vertices = 2 × number of edges</b>.</p>""",
          diagram="ds4_graph_terms", programs=["ds4p10"], examples=["ds4n9"], key=True),

        T("4.4.2 Types of Graphs",
          r"""<ol><li><b>Undirected graph:</b> edges have no direction; (A, B) is the same as (B, A). Example: a road with two-way traffic.</li>
<li><b>Directed graph (digraph):</b> every edge has a direction, shown by an arrow; &lt;A, B&gt; goes from A to B only. Example: one-way roads, links between web pages.</li>
<li><b>Connected graph:</b> there is a path between <b>every pair</b> of vertices. If not, it is a <b>disconnected</b> graph.</li>
<li><b>Complete graph:</b> every vertex is joined to <b>every other</b> vertex. An undirected complete graph with n vertices has <b>n(n − 1)/2</b> edges (written K<sub>n</sub>). A complete digraph has n(n − 1) edges.</li>
<li><b>Weighted graph:</b> every edge has a value (weight) such as distance, cost or time. Example: a road map with distances.</li></ol>
<p>Other types: a <b>cyclic</b> graph contains a cycle; an <b>acyclic</b> graph does not. A tree is a connected acyclic graph.</p>""",
          diagram="ds4_graph_types", programs=["ds4p11", "ds4p12", "ds4p13"], examples=["ds4n10", "ds4n11"], key=True),

        T("4.4.3 Graph Representation; Tree vs Graph",
          r"""<h4>1. Adjacency matrix</h4>
<p>A 2-D array <code>adj[n][n]</code> where <code>adj[i][j] = 1</code> if there is an edge from i to j, else 0. For a weighted graph the weight is stored. It is symmetric for an undirected graph. Memory: O(n²).</p>
<h4>2. Adjacency list</h4>
<p>An array of linked lists: list i contains all vertices adjacent to vertex i. It uses memory only for existing edges, O(n + e), so it suits <b>sparse</b> graphs.</p>
<h4>Tree vs graph</h4>
<table>
<tr><th>Tree</th><th>Graph</th></tr>
<tr><td>Hierarchical structure</td><td>Network structure</td></tr>
<tr><td>Has one root node</td><td>No root node</td></tr>
<tr><td>No cycles</td><td>May contain cycles</td></tr>
<tr><td>n nodes → exactly n − 1 edges</td><td>Any number of edges</td></tr>
<tr><td>Exactly one path between two nodes</td><td>One or more paths</td></tr>
<tr><td>Traversal: inorder, preorder, postorder</td><td>Traversal: BFS, DFS</td></tr>
<tr><td>e.g. folder structure</td><td>e.g. road map, social network</td></tr>
</table>
<h4>Applications of graphs</h4>
<ul><li>Maps and GPS shortest routes, computer networks, social networks (friends), web page links, airline routes, project scheduling.</li></ul>""",
          programs=["ds4p14"]),
    ],
}

NOTES_B = [SEC_4_3, SEC_4_4]
