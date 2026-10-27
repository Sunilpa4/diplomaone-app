"""DI03000021 Unit 4 notes part A: 4.1 tree concepts, binary trees, conversion; 4.2 traversal."""
from c_content import make_TE
from ds_tree import inorder, preorder, postorder
from diagrams_DI03000021_u4 import TRAV_TREE

SN = {
    "c_tnode": r'''
struct tnode {
    struct tnode *left;
    int data;
    struct tnode *right;
};
''',
    "alg_in": r'''
Algorithm INORDER(T)
Step 1: If T != NULL then
          INORDER(LEFT(T))
          Visit INFO(T)
          INORDER(RIGHT(T))
Step 2: Exit
''',
    "alg_pre": r'''
Algorithm PREORDER(T)
Step 1: If T != NULL then
          Visit INFO(T)
          PREORDER(LEFT(T))
          PREORDER(RIGHT(T))
Step 2: Exit
''',
    "alg_post": r'''
Algorithm POSTORDER(T)
Step 1: If T != NULL then
          POSTORDER(LEFT(T))
          POSTORDER(RIGHT(T))
          Visit INFO(T)
Step 2: Exit
''',
    "alg_g2b": r'''
Conversion: General -> Binary
Step 1: Keep the root as it is.
Step 2: For every node, its leftmost
        (first) child becomes its
        LEFT child.
Step 3: Its next sibling (immediate
        right brother) becomes its
        RIGHT child.
Step 4: Delete all other links from
        parent to children.
''',
}
T0 = make_TE(SN)


def T(h, b, examples=None, **kw):
    d = T0(h, b, **kw)
    if examples:
        d["examples"] = examples
    return d


IN, PRE, POST = (" ".join(f(TRAV_TREE)) for f in (inorder, preorder, postorder))

SEC_4_1 = {
    "title": {"en": "4.1 Tree: Fundamental Concepts"},
    "items": [
        T("4.1.1 Introduction to Tree; General Tree",
          r"""<p>A <b>tree</b> is a <b>non-linear</b> data structure that stores data in a <b>hierarchical</b> (parent–child) form.</p>
<p><b>Definition:</b> a tree is a finite set of one or more nodes such that:</p>
<ol><li>there is one specially designated node called the <b>root</b>, and</li>
<li>the remaining nodes are divided into n ≥ 0 disjoint sets T1, T2, …, Tn, each of which is itself a tree, called a <b>subtree</b> of the root.</li></ol>
<p>This definition is <b>recursive</b>: a tree is made of smaller trees.</p>
<h4>General tree</h4>
<p>A <b>general tree</b> is a tree in which a node can have <b>any number of children</b> (0, 1, 2, 3, …). Example: the folder structure of a computer, an organisation chart, a family tree.</p>
<h4>Properties</h4>
<ul><li>There is exactly <b>one path</b> between the root and any node.</li>
<li>A tree with n nodes has exactly <b>n − 1 edges</b>.</li>
<li>A tree has no cycle.</li></ul>
<h4>Linear vs non-linear</h4>
<p>In arrays, stacks, queues and linked lists, each element has one next element (linear). In a tree, one node can have <b>many</b> next nodes (children), so it is non-linear.</p>""",
          diagram="ds4_terms", key=True),

        T("4.1.2 Tree Terminology",
          r"""<p>The examples refer to the tree in the "Tree: Basic Terminology" diagram: A has children B, C, D; B has E, F; F has J; D has G, H, I.</p>
<table>
<tr><th>Term</th><th>Meaning</th><th>Example</th></tr>
<tr><td><b>Node</b></td><td>an element of the tree holding data</td><td>A, B, …, J (10 nodes)</td></tr>
<tr><td><b>Root node</b></td><td>the topmost node; it has no parent</td><td>A</td></tr>
<tr><td><b>Edge</b></td><td>the link between a parent and a child</td><td>A–B (9 edges)</td></tr>
<tr><td><b>Parent node</b></td><td>a node that has a child (immediate predecessor)</td><td>B is the parent of E and F</td></tr>
<tr><td><b>Child node</b></td><td>an immediate successor of a node</td><td>E and F are children of B</td></tr>
<tr><td><b>Sibling</b></td><td>nodes with the same parent</td><td>G, H, I; also B, C, D</td></tr>
<tr><td><b>Leaf node</b> (terminal)</td><td>a node with no child (degree 0)</td><td>E, J, C, G, H, I</td></tr>
<tr><td><b>Internal node</b></td><td>a node with at least one child</td><td>A, B, F, D</td></tr>
<tr><td><b>Degree of a node</b></td><td>number of children (subtrees) of the node</td><td>deg(A) = 3, deg(F) = 1, deg(E) = 0</td></tr>
<tr><td><b>Degree of a tree</b></td><td>maximum degree of any node</td><td>3</td></tr>
<tr><td><b>In-degree</b></td><td>number of edges coming <b>into</b> a node</td><td>root: 0; every other node: 1</td></tr>
<tr><td><b>Out-degree</b></td><td>number of edges going <b>out</b> of a node (= number of children)</td><td>out(D) = 3</td></tr>
<tr><td><b>Subtree</b></td><td>a node together with all its descendants</td><td>D, G, H, I</td></tr>
<tr><td><b>Level</b></td><td>root is at level 0; a child is one level below its parent</td><td>level(J) = 3</td></tr>
<tr><td><b>Path</b></td><td>sequence of nodes connected by edges</td><td>A → B → F → J (length 3)</td></tr>
<tr><td><b>Depth of a node</b></td><td>length of the path from the root to the node</td><td>depth(F) = 2</td></tr>
<tr><td><b>Height of a node</b></td><td>length of the longest path from the node down to a leaf</td><td>height(B) = 2</td></tr>
<tr><td><b>Height of a tree</b></td><td>height of the root = maximum level</td><td>3</td></tr>
<tr><td><b>Ancestor / Descendant</b></td><td>nodes on the path above / below a node</td><td>ancestors of J: F, B, A</td></tr>
</table>
<p><b>Note:</b> some books start levels at 1 and count height in levels (then the height here is 4). In the exam, state the convention you use.</p>""",
          examples=["ds4n1"], key=True),

        T("4.1.3 Forest",
          r"""<p>A <b>forest</b> is a set of <b>n ≥ 0 disjoint trees</b>.</p>
<ul><li>If the <b>root</b> of a tree is deleted, its subtrees form a forest.</li>
<li>Conversely, if a new node is added as the parent of the roots of all trees in a forest, we get a single tree.</li>
<li>Example: deleting root R from a tree whose children are B, C, D gives a forest of 3 trees rooted at B, C and D.</li>
<li>A forest can also be converted into one binary tree: convert each tree into a binary tree, then join the roots as right siblings.</li></ul>""",
          diagram="ds4_forest"),

        T("4.1.4 Binary Tree, Strict Binary Tree and Complete Binary Tree",
          r"""<h4>Binary tree</h4>
<p>A <b>binary tree</b> is a tree in which every node has <b>at most two children</b>, called the <b>left child</b> and the <b>right child</b>. (A binary tree may also be empty.) The order matters: a node with only a left child is different from a node with only a right child.</p>
<h4>Strict binary tree</h4>
<p>A binary tree in which every non-leaf node has <b>exactly two children</b> (each node has 0 or 2 children). A strict binary tree with n leaves always has <b>2n − 1</b> nodes.</p>
<h4>Complete binary tree</h4>
<p>A binary tree in which <b>all levels are completely filled except possibly the last level</b>, and the nodes of the last level are placed <b>as far left as possible</b>. Complete binary trees are used for heaps and can be stored easily in an array.</p>
<p>(A <b>full / perfect</b> binary tree has all levels completely filled: 2<sup>h+1</sup> − 1 nodes.)</p>
<h4>Properties of a binary tree</h4>
<ul><li>Maximum number of nodes at level l = <b>2<sup>l</sup></b> (root at level 0).</li>
<li>Maximum number of nodes in a binary tree of height h = <b>2<sup>h+1</sup> − 1</b>.</li>
<li>Minimum height of a binary tree with n nodes = <b>⌊log<sub>2</sub> n⌋</b>.</li>
<li>Number of leaves = number of nodes with two children + 1.</li></ul>""",
          diagram="ds4_binary_types", examples=["ds4n12"], key=True),

        T("4.1.5 Representation of a Binary Tree",
          r"""<h4>Linked representation</h4>
<p>Each node of a binary tree is a structure with three fields: a pointer to the <b>left</b> child, the <b>data</b>, and a pointer to the <b>right</b> child.</p>
@@c_tnode@@
<ul><li>A pointer <b>root</b> holds the address of the root node; <code>root = NULL</code> means the tree is empty.</li>
<li>A missing child is shown by a NULL pointer; leaf nodes have both pointers NULL.</li>
<li>Nodes are created dynamically with malloc, so the tree can grow as needed.</li></ul>
<h4>Array (sequential) representation</h4>
<ul><li>The root is stored at index 0. For a node at index i, the <b>left child</b> is at <b>2i + 1</b> and the <b>right child</b> at <b>2i + 2</b>; the parent is at ⌊(i − 1)/2⌋.</li>
<li>It suits complete binary trees; for other trees many array places stay empty (memory waste).</li></ul>""",
          diagram="ds4_node_repr", programs=["ds4p1"]),

        T("4.1.6 Conversion of a General Tree to a Binary Tree",
          r"""<p>A general tree can have any number of children, which is hard to store. It is converted to a binary tree using the <b>left child – right sibling</b> method.</p>
@@alg_g2b@@
<h4>Example</h4>
<p>General tree: A has children B, C, D; B has E, F; D has G, H.</p>
<ul><li>A: left = B (first child), right = none (the root has no sibling).</li>
<li>B: left = E, right = C. C: right = D.</li>
<li>E: right = F. D: left = G. G: right = H.</li></ul>
<p>In the binary tree, a <b>left</b> link means "first child" and a <b>right</b> link means "next sibling". The <b>preorder</b> of the binary tree is the same as the preorder of the general tree (A B E F C D G H). The root of the converted tree never has a right child.</p>""",
          diagram="ds4_gen2bin", programs=["ds4p9"], examples=["ds4n2"], key=True),
    ],
}

SEC_4_2 = {
    "title": {"en": "4.2 Tree Traversal"},
    "items": [
        T("4.2.1 Inorder, Preorder and Postorder Traversal",
          rf"""<p><b>Traversal</b> means visiting every node of a tree <b>exactly once</b> in a fixed order. A binary tree has three standard (depth-first) traversals, named by <b>when the root (N) is visited</b>.</p>
<h4>1. Inorder (Left – Node – Right)</h4>
@@alg_in@@
<h4>2. Preorder (Node – Left – Right)</h4>
@@alg_pre@@
<h4>3. Postorder (Left – Right – Node)</h4>
@@alg_post@@
<h4>Example (tree in the diagram)</h4>
<table>
<tr><th>Traversal</th><th>Order</th><th>Result</th></tr>
<tr><td>Inorder</td><td>L N R</td><td><b>{IN}</b></td></tr>
<tr><td>Preorder</td><td>N L R</td><td><b>{PRE}</b></td></tr>
<tr><td>Postorder</td><td>L R N</td><td><b>{POST}</b></td></tr>
</table>
<h4>Points to remember</h4>
<ul><li>In <b>preorder</b> the root is <b>first</b>; in <b>postorder</b> the root is <b>last</b>.</li>
<li>The <b>inorder</b> traversal of a BST gives the data in <b>ascending order</b>.</li>
<li>For an expression tree, inorder gives the infix, preorder the prefix and postorder the postfix expression.</li>
<li>Each traversal takes <b>O(n)</b> time. Recursion uses the system stack.</li></ul>
<h4>Easy trick</h4>
<p>Go round the tree anticlockwise starting from the left of the root. Write a node when you pass its <b>left</b> side (preorder), its <b>bottom</b> (inorder) or its <b>right</b> side (postorder).</p>""",
          diagram="ds4_traversal", programs=["ds4p2"], examples=["ds4n3", "ds4n4"], key=True),

        T("4.2.2 Constructing a Binary Tree from Traversals",
          r"""<p>A unique binary tree can be built from <b>inorder + preorder</b> or from <b>inorder + postorder</b>. (Preorder + postorder alone is not enough.)</p>
<h4>Method (inorder + preorder)</h4>
<ol><li>The <b>first</b> value of the preorder is the <b>root</b>.</li>
<li>Find the root in the inorder: values on its <b>left</b> form the left subtree; values on its <b>right</b> form the right subtree.</li>
<li>Repeat for each subtree with the next values of the preorder.</li></ol>
<p>With <b>postorder</b>, the <b>last</b> value is the root, and the subtrees are built right first, then left.</p>""",
          examples=["ds4n8"]),
    ],
}

NOTES_A = [SEC_4_1, SEC_4_2]
