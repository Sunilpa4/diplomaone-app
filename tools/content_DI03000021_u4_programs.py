"""DI03000021 Unit 4 - solved C programs (binary tree, traversal, BST, general->binary, graph). gcc-verified."""
from c_content import PE

PROGRAMS = [
    PE("ds4p1", "Create a binary tree (linked) and find nodes, leaves, height", r'''
#include <stdio.h>
#include <stdlib.h>

struct tnode {
    struct tnode *left;
    char data;
    struct tnode *right;
};

struct tnode *nn(char x)
{
    struct tnode *t;
    t = malloc(sizeof(struct tnode));
    t->data = x;
    t->left = t->right = NULL;
    return t;
}

int nodes(struct tnode *t)
{
    if (t == NULL) return 0;
    return 1 + nodes(t->left)
             + nodes(t->right);
}

int leaves(struct tnode *t)
{
    if (t == NULL) return 0;
    if (!t->left && !t->right) return 1;
    return leaves(t->left)
         + leaves(t->right);
}

int height(struct tnode *t)  /* edges */
{
    int l, r;
    if (t == NULL) return -1;
    l = height(t->left);
    r = height(t->right);
    return 1 + (l > r ? l : r);
}

int main(void)
{
    struct tnode *root = nn('A');
    root->left = nn('B');
    root->right = nn('C');
    root->left->left = nn('D');
    root->left->right = nn('E');
    root->left->right->left = nn('G');
    root->right->right = nn('F');

    printf("Nodes  = %d\n", nodes(root));
    printf("Leaves = %d\n", leaves(root));
    printf("Height = %d\n", height(root));
    return 0;
}
''', (),
       r"""<ul><li>Each tree node has a <b>left</b> pointer, <b>data</b> and a <b>right</b> pointer (linked representation).</li>
<li>The tree built is the one in the traversal diagram: A(B(D, E(G)), C(–, F)).</li>
<li>All three functions are <b>recursive</b>: the answer for a tree = the answer for its left subtree + right subtree (+ the node itself).</li>
<li>Leaves are D, G and F. Height = 3 edges (A → B → E → G).</li></ul>"""),

    PE("ds4p2", "Inorder, preorder and postorder traversal (recursive)", r'''
#include <stdio.h>
#include <stdlib.h>

struct tnode {
    struct tnode *left;
    char data;
    struct tnode *right;
};

struct tnode *nn(char x, struct tnode *l,
                 struct tnode *r)
{
    struct tnode *t;
    t = malloc(sizeof(struct tnode));
    t->data = x;
    t->left = l;
    t->right = r;
    return t;
}

void inorder(struct tnode *t)
{
    if (t != NULL) {
        inorder(t->left);
        printf("%c ", t->data);
        inorder(t->right);
    }
}

void preorder(struct tnode *t)
{
    if (t != NULL) {
        printf("%c ", t->data);
        preorder(t->left);
        preorder(t->right);
    }
}

void postorder(struct tnode *t)
{
    if (t != NULL) {
        postorder(t->left);
        postorder(t->right);
        printf("%c ", t->data);
    }
}

int main(void)
{
    struct tnode *root;
    root = nn('A',
              nn('B', nn('D', NULL, NULL),
                 nn('E',
                    nn('G', NULL, NULL),
                    NULL)),
              nn('C', NULL,
                 nn('F', NULL, NULL)));

    printf("Inorder  : ");
    inorder(root);
    printf("\nPreorder : ");
    preorder(root);
    printf("\nPostorder: ");
    postorder(root);
    printf("\n");
    return 0;
}
''', (),
       r"""<ul><li><b>Inorder (L N R):</b> left subtree, node, right subtree.</li>
<li><b>Preorder (N L R):</b> node first; the root is always the <b>first</b> value.</li>
<li><b>Postorder (L R N):</b> node last; the root is always the <b>last</b> value.</li>
<li>The three functions differ only in <b>where the printf is placed</b>. The recursion stops at NULL.</li></ul>"""),

    PE("ds4p3", "Construct a Binary Search Tree and display it [Practical 10]", r'''
#include <stdio.h>
#include <stdlib.h>

struct tnode {
    struct tnode *left;
    int data;
    struct tnode *right;
};

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
    else
        printf("%d is duplicate\n", x);
    return t;
}

void inorder(struct tnode *t)
{
    if (t) {
        inorder(t->left);
        printf("%d ", t->data);
        inorder(t->right);
    }
}

void preorder(struct tnode *t)
{
    if (t) {
        printf("%d ", t->data);
        preorder(t->left);
        preorder(t->right);
    }
}

int main(void)
{
    struct tnode *root = NULL;
    int n, i, x;

    scanf("%d", &n);
    for (i = 0; i < n; i++) {
        scanf("%d", &x);
        root = insert(root, x);
    }
    printf("Inorder : ");
    inorder(root);
    printf("\nPreorder: ");
    preorder(root);
    printf("\n");
    return 0;
}
''', ("9", "45 25 65 15 35 55 75 30 35"),
       r"""<ul><li><b>BST rule:</b> smaller values go to the <b>left</b> subtree and larger values to the <b>right</b>.</li>
<li><code>insert()</code> is recursive: it moves left or right until it finds a NULL place and creates the new node there.</li>
<li>Duplicates are not inserted (the second 35 is rejected).</li>
<li>The <b>inorder</b> traversal of a BST always gives the values in <b>ascending order</b>.</li></ul>"""),

    PE("ds4p4", "Search a value in a BST (shows the path)", r'''
#include <stdio.h>
#include <stdlib.h>

struct tnode {
    struct tnode *left;
    int data;
    struct tnode *right;
};

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

void search(struct tnode *t, int x)
{
    int c = 0;
    printf("Search %d: ", x);
    while (t != NULL) {
        c++;
        printf("%d ", t->data);
        if (x == t->data) {
            printf("FOUND, %d steps\n", c);
            return;
        }
        t = (x < t->data) ? t->left
                          : t->right;
    }
    printf("NOT FOUND, %d steps\n", c);
}

int main(void)
{
    int a[8] = {45, 25, 65, 15,
                35, 55, 75, 30};
    struct tnode *root = NULL;
    int i;
    for (i = 0; i < 8; i++)
        root = insert(root, a[i]);
    search(root, 30);
    search(root, 75);
    search(root, 60);
    return 0;
}
''', (),
       r"""<ul><li>At each node: if x is equal → found; if smaller → go left; if larger → go right.</li>
<li>Only <b>one path</b> from the root is checked, so a search takes O(h) comparisons (h = height), not O(n).</li>
<li>60 is not found: 60 &gt; 45 → right, 60 &lt; 65 → left, 60 &gt; 55 → right is NULL.</li></ul>"""),

    PE("ds4p5", "Delete a node from a BST (all three cases)", r'''
#include <stdio.h>
#include <stdlib.h>

struct tnode {
    struct tnode *left;
    int data;
    struct tnode *right;
};

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

struct tnode *del(struct tnode *t, int x)
{
    struct tnode *tmp;
    if (t == NULL) {
        printf("%d not found\n", x);
        return NULL;
    }
    if (x < t->data)
        t->left = del(t->left, x);
    else if (x > t->data)
        t->right = del(t->right, x);
    else if (t->left && t->right) {
        tmp = t->right;      /* 2 children */
        while (tmp->left)
            tmp = tmp->left;  /* successor */
        t->data = tmp->data;
        t->right = del(t->right,
                       tmp->data);
    } else {                 /* 0 or 1 child */
        tmp = t;
        t = t->left ? t->left : t->right;
        free(tmp);
    }
    return t;
}

void inorder(struct tnode *t)
{
    if (t) {
        inorder(t->left);
        printf("%d ", t->data);
        inorder(t->right);
    }
}

void preorder(struct tnode *t)
{
    if (t) {
        printf("%d ", t->data);
        preorder(t->left);
        preorder(t->right);
    }
}

void show(struct tnode *t)
{
    printf("  pre: "); preorder(t);
    printf("| in: "); inorder(t);
    printf("\n");
}

int main(void)
{
    int a[8] = {45, 25, 65, 15,
                35, 55, 75, 30};
    struct tnode *root = NULL;
    int i;
    for (i = 0; i < 8; i++)
        root = insert(root, a[i]);
    show(root);
    printf("delete 15 (leaf)\n");
    root = del(root, 15); show(root);
    printf("delete 35 (one child)\n");
    root = del(root, 35); show(root);
    printf("delete 45 (two children)\n");
    root = del(root, 45); show(root);
    root = del(root, 99);
    return 0;
}
''', (),
       r"""<ul><li><b>Case 1, leaf:</b> the node is simply removed (its parent's pointer becomes NULL).</li>
<li><b>Case 2, one child:</b> the child takes the place of the deleted node (35 is replaced by 30).</li>
<li><b>Case 3, two children:</b> copy the <b>inorder successor</b> (the smallest value in the right subtree) into the node, then delete the successor. Deleting the root 45 makes 55 the new root.</li>
<li>Inorder is still sorted after every deletion, which proves the BST property is kept. The preorder shows the new shape.</li></ul>"""),

    PE("ds4p6", "Find the minimum and maximum in a BST", r'''
#include <stdio.h>
#include <stdlib.h>

struct tnode {
    struct tnode *left;
    int data;
    struct tnode *right;
};

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

int findmin(struct tnode *t)
{
    while (t->left != NULL)
        t = t->left;
    return t->data;
}

int findmax(struct tnode *t)
{
    while (t->right != NULL)
        t = t->right;
    return t->data;
}

int main(void)
{
    int a[7] = {50, 30, 70, 20,
                40, 60, 80};
    struct tnode *root = NULL;
    int i;
    for (i = 0; i < 7; i++)
        root = insert(root, a[i]);
    printf("Min = %d\n", findmin(root));
    printf("Max = %d\n", findmax(root));
    return 0;
}
''', (),
       r"""<ul><li>The <b>smallest</b> value is the <b>leftmost</b> node: keep going left until left is NULL.</li>
<li>The <b>largest</b> value is the <b>rightmost</b> node.</li>
<li>No comparisons with data are needed; the BST shape itself gives the answer in O(h).</li></ul>"""),

    PE("ds4p7", "BST statistics: count, leaves, internal nodes, height", r'''
#include <stdio.h>
#include <stdlib.h>

struct tnode {
    struct tnode *left;
    int data;
    struct tnode *right;
};

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

int count(struct tnode *t)
{
    return t ? 1 + count(t->left)
               + count(t->right) : 0;
}

int leaves(struct tnode *t)
{
    if (!t) return 0;
    if (!t->left && !t->right) return 1;
    return leaves(t->left)
         + leaves(t->right);
}

int height(struct tnode *t)
{
    int l, r;
    if (!t) return -1;
    l = height(t->left);
    r = height(t->right);
    return 1 + (l > r ? l : r);
}

int main(void)
{
    int a[8] = {45, 25, 65, 15,
                35, 55, 75, 30};
    struct tnode *root = NULL;
    int i, n, lf;
    for (i = 0; i < 8; i++)
        root = insert(root, a[i]);
    n = count(root);
    lf = leaves(root);
    printf("Total nodes = %d\n", n);
    printf("Leaf nodes  = %d\n", lf);
    printf("Internal    = %d\n", n - lf);
    printf("Height      = %d\n",
           height(root));
    return 0;
}
''', (),
       r"""<ul><li>Leaves are 15, 30, 55 and 75. Internal (non-leaf) nodes = total − leaves = 4.</li>
<li>Height is counted in <b>edges</b> on the longest path from the root: 45 → 25 → 35 → 30 = 3. (Some books count levels and say 4; write which one you use.)</li></ul>"""),

    PE("ds4p8", "BST menu: insert, search, delete, traversals", r'''
#include <stdio.h>
#include <stdlib.h>

struct tnode {
    struct tnode *left;
    int data;
    struct tnode *right;
};

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

int search(struct tnode *t, int x)
{
    while (t && t->data != x)
        t = x < t->data ? t->left
                        : t->right;
    return t != NULL;
}

struct tnode *del(struct tnode *t, int x)
{
    struct tnode *s;
    if (!t) return NULL;
    if (x < t->data)
        t->left = del(t->left, x);
    else if (x > t->data)
        t->right = del(t->right, x);
    else if (t->left && t->right) {
        for (s = t->right; s->left; )
            s = s->left;
        t->data = s->data;
        t->right = del(t->right, s->data);
    } else {
        s = t;
        t = t->left ? t->left : t->right;
        free(s);
    }
    return t;
}

void in(struct tnode *t)
{
    if (t) {
        in(t->left);
        printf("%d ", t->data);
        in(t->right);
    }
}

void pre(struct tnode *t)
{
    if (t) {
        printf("%d ", t->data);
        pre(t->left);
        pre(t->right);
    }
}

void post(struct tnode *t)
{
    if (t) {
        post(t->left);
        post(t->right);
        printf("%d ", t->data);
    }
}

int main(void)
{
    struct tnode *root = NULL;
    int ch, x;
    do {
        puts("1.Insert 2.Search 3.Delete");
        puts("4.Traverse 0.Exit");
        scanf("%d", &ch);
        switch (ch) {
        case 1: scanf("%d", &x);
                root = insert(root, x);
                break;
        case 2: scanf("%d", &x);
                if (search(root, x))
                    puts("Found");
                else
                    puts("Not found");
                break;
        case 3: scanf("%d", &x);
                root = del(root, x); break;
        case 4: printf("In: ");
                in(root);
                printf("\nPre: ");
                pre(root);
                printf("\nPost: ");
                post(root);
                printf("\n");
                break;
        }
    } while (ch != 0);
    return 0;
}
''', ("1 50", "1 30", "1 70", "1 20", "1 40", "4", "2 40", "3 30", "4", "2 30", "0"),
       r"""<ul><li>A complete menu-driven BST program for the practical.</li>
<li>Sample run: insert 50, 30, 70, 20, 40 → traverse; search 40 → Found; delete 30 (two children, successor 40 replaces it) → traverse again; search 30 → Not found.</li>
<li>After deleting 30, the preorder changes from 50 30 20 40 70 to 50 40 20 70.</li></ul>"""),

    PE("ds4p9", "General tree to binary tree (left child, right sibling)", r'''
#include <stdio.h>
#include <stdlib.h>

/* binary form: left = first child,
   right = next sibling              */
struct gnode {
    char data;
    struct gnode *child;
    struct gnode *sib;
};

struct gnode *nn(char x)
{
    struct gnode *t;
    t = malloc(sizeof(struct gnode));
    t->data = x;
    t->child = t->sib = NULL;
    return t;
}

void add(struct gnode *p, struct gnode *c)
{
    struct gnode *t = p->child;
    if (t == NULL) {
        p->child = c;
        return;
    }
    while (t->sib) t = t->sib;
    t->sib = c;        /* new right sibling */
}

void show(struct gnode *t)
{
    if (t == NULL) return;
    printf("%c: left=%c right=%c\n",
           t->data,
           t->child ? t->child->data : '-',
           t->sib ? t->sib->data : '-');
    show(t->child);
    show(t->sib);
}

int main(void)
{
    struct gnode *A = nn('A');
    struct gnode *B = nn('B');
    struct gnode *D = nn('D');
    add(A, B); add(A, nn('C')); add(A, D);
    add(B, nn('E')); add(B, nn('F'));
    add(D, nn('G')); add(D, nn('H'));
    show(A);
    return 0;
}
''', (),
       r"""<ul><li>A general tree node can have any number of children, but every node has only <b>one first child</b> and <b>one next sibling</b>.</li>
<li>Storing <b>first child → left</b> and <b>next sibling → right</b> turns any general tree into a binary tree.</li>
<li>The output lists each node's left and right in the converted tree (same as the diagram): A's left is B; B's right is C; C's right is D; D's left is G, and so on.</li></ul>"""),

    PE("ds4p10", "Undirected graph: adjacency matrix and degree", r'''
#include <stdio.h>

int main(void)
{
    int adj[10][10] = {{0}};
    int n, e, i, j, u, v, deg;

    scanf("%d %d", &n, &e);
    for (i = 0; i < e; i++) {
        scanf("%d %d", &u, &v);
        adj[u][v] = adj[v][u] = 1;
    }
    printf("Adjacency matrix:\n   ");
    for (j = 0; j < n; j++)
        printf("%c ", 'A' + j);
    printf("\n");
    for (i = 0; i < n; i++) {
        printf("%c: ", 'A' + i);
        for (j = 0; j < n; j++)
            printf("%d ", adj[i][j]);
        printf("\n");
    }
    for (i = 0; i < n; i++) {
        deg = 0;
        for (j = 0; j < n; j++)
            deg += adj[i][j];
        printf("Degree(%c) = %d\n",
               'A' + i, deg);
    }
    return 0;
}
''', ("5 7", "0 1", "1 2", "0 3", "1 3", "1 4", "2 4", "3 4"),
       r"""<ul><li>The graph is the one in the "Graph: Basic Terms" diagram: vertices A to E (0 to 4) and 7 edges.</li>
<li>In the <b>adjacency matrix</b>, <code>adj[i][j] = 1</code> if there is an edge between i and j. For an undirected graph it is <b>symmetric</b>.</li>
<li><b>Degree</b> of a vertex = number of edges touching it = sum of its row. The sum of all degrees = 2 × edges = 14.</li></ul>"""),

    PE("ds4p11", "Directed graph: in-degree and out-degree", r'''
#include <stdio.h>

int main(void)
{
    int adj[10][10] = {{0}};
    int n = 4, i, j, in, out;
    int e[5][2] = {{0, 1}, {1, 2}, {2, 0},
                   {2, 3}, {3, 1}};

    for (i = 0; i < 5; i++)
        adj[e[i][0]][e[i][1]] = 1;

    printf("Vertex  In  Out\n");
    for (i = 0; i < n; i++) {
        in = out = 0;
        for (j = 0; j < n; j++) {
            out += adj[i][j];   /* row */
            in += adj[j][i];  /* column */
        }
        printf("  %c     %d   %d\n",
               'A' + i, in, out);
    }
    return 0;
}
''', (),
       r"""<ul><li>Edges: A→B, B→C, C→A, C→D, D→B. For a directed graph the matrix is <b>not symmetric</b>.</li>
<li><b>Out-degree</b> = edges leaving a vertex = sum of its <b>row</b>.</li>
<li><b>In-degree</b> = edges entering a vertex = sum of its <b>column</b>.</li>
<li>Total in-degree = total out-degree = number of edges (5).</li></ul>"""),

    PE("ds4p12", "Weighted graph: cost matrix and total weight", r'''
#include <stdio.h>

int main(void)
{
    int w[10][10] = {{0}};
    int n = 4, i, j, total = 0;
    int e[5][3] = {{0, 1, 4}, {0, 2, 2},
                   {1, 2, 7}, {1, 3, 5},
                   {2, 3, 3}};

    for (i = 0; i < 5; i++) {
        w[e[i][0]][e[i][1]] = e[i][2];
        w[e[i][1]][e[i][0]] = e[i][2];
    }
    printf("Cost matrix (0 = no edge):\n");
    for (i = 0; i < n; i++) {
        for (j = 0; j < n; j++)
            printf("%3d", w[i][j]);
        printf("\n");
    }
    printf("Edges:\n");
    for (i = 0; i < n; i++)
        for (j = i + 1; j < n; j++)
            if (w[i][j]) {
                printf("%c-%c = %d\n",
                       'A' + i, 'A' + j,
                       w[i][j]);
                total += w[i][j];
            }
    printf("Total weight = %d\n", total);
    return 0;
}
''', (),
       r"""<ul><li>In a <b>weighted graph</b> every edge has a value (cost, distance, time).</li>
<li>The matrix stores the <b>weight</b> instead of 1. Here 0 means no edge.</li>
<li>For an undirected graph each edge is printed once by scanning only the upper triangle (<code>j &gt; i</code>).</li></ul>"""),

    PE("ds4p13", "Check whether a graph is connected and complete", r'''
#include <stdio.h>

int adj[10][10], seen[10], n;

void visit(int v)          /* DFS */
{
    int j;
    seen[v] = 1;
    for (j = 0; j < n; j++)
        if (adj[v][j] && !seen[j])
            visit(j);
}

void check(int e, int ed[][2])
{
    int i, c = 1;
    for (i = 0; i < 100; i++)
        adj[i / 10][i % 10] = 0;
    for (i = 0; i < 10; i++)
        seen[i] = 0;
    for (i = 0; i < e; i++)
        adj[ed[i][0]][ed[i][1]] =
        adj[ed[i][1]][ed[i][0]] = 1;
    visit(0);
    for (i = 0; i < n; i++)
        if (!seen[i]) c = 0;
    printf("n=%d e=%d: ", n, e);
    printf(c ? "connected, "
             : "disconnected, ");
    if (e == n * (n - 1) / 2)
        printf("complete\n");
    else
        printf("not complete\n");
}

int main(void)
{
    int g1[3][2] = {{0, 1}, {0, 2},
                    {2, 3}};
    int g2[2][2] = {{0, 1}, {2, 3}};
    int g3[6][2] = {{0, 1}, {0, 2},
                    {0, 3}, {1, 2},
                    {1, 3}, {2, 3}};
    n = 4;
    check(3, g1);
    check(2, g2);
    check(6, g3);
    return 0;
}
''', (),
       r"""<ul><li>The three graphs are the Connected, Disconnected and Complete (K4) panels of the "Types of Graph" diagram.</li>
<li><b>Connected:</b> starting from vertex A, a depth-first visit reaches every vertex.</li>
<li><b>Complete:</b> every pair of vertices is joined, so the edges = n(n − 1)/2 = 6 for n = 4.</li></ul>"""),

    PE("ds4p14", "Graph using adjacency list (linked lists)", r'''
#include <stdio.h>
#include <stdlib.h>

struct enode {
    int v;
    struct enode *next;
};
struct enode *head[5];

void add(int u, int v)
{
    struct enode *t;
    t = malloc(sizeof(struct enode));
    t->v = v;
    t->next = head[u];  /* at start */
    head[u] = t;
}

int main(void)
{
    int e[7][2] = {{0, 1}, {1, 2}, {0, 3},
                   {1, 3}, {1, 4}, {2, 4},
                   {3, 4}};
    int i;
    struct enode *p;

    for (i = 0; i < 7; i++) {
        add(e[i][0], e[i][1]);
        add(e[i][1], e[i][0]);
    }
    for (i = 0; i < 5; i++) {
        printf("%c:", 'A' + i);
        for (p = head[i]; p; p = p->next)
            printf(" -> %c", 'A' + p->v);
        printf("\n");
    }
    return 0;
}
''', (),
       r"""<ul><li>Each vertex has a <b>linked list</b> of its adjacent vertices (an application of Unit 3).</li>
<li>New neighbours are inserted at the <b>beginning</b> of the list (O(1)), so they appear in reverse order of input.</li>
<li>An adjacency list uses memory only for the existing edges, so it is better than a matrix for <b>sparse</b> graphs.</li></ul>"""),
]
