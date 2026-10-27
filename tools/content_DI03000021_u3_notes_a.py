"""DI03000021 Unit 3 notes part A: 3.1 pointer, structure, DMA; 3.2 linked list representation, types, applications."""
from c_content import make_TE

SN = {
    "c_ptr": r'''
int x = 10;
int *p;          /* declaration */
p = &x;          /* initialisation */
printf("%d", *p);   /* prints 10 */
int *q = NULL;   /* NULL pointer */
int **pp = &p;   /* pointer to pointer */
''',
    "c_struct": r'''
struct student {
    int roll;
    char name[20];
    float marks;
};
struct student s1 = {1, "Ravi", 78.5};
struct student s[60];  /* array */
s1.marks = 80;         /* dot operator */
''',
    "c_sptr": r'''
struct student *ptr;
ptr = &s1;
ptr->roll = 5;       /* arrow operator */
(*ptr).roll = 5;     /* same meaning */
''',
    "c_self": r'''
struct node {
    int data;
    struct node *next;  /* same type */
};
''',
    "c_dma": r'''
ptr = (type *) malloc(byte_size);
ptr = (type *) calloc(n, elem_size);
ptr = (type *) realloc(ptr, new_size);
free(ptr);
''',
    "c_dma_ex": r'''
int *a = (int *) malloc(5 * sizeof(int));
if (a == NULL)
    printf("Out of memory");
...
free(a);
a = NULL;   /* avoid dangling pointer */
''',
    "c_getnode": r'''
struct node *getnode(int x)
{
    struct node *nw;
    nw = (struct node *)
         malloc(sizeof(struct node));
    nw->data = x;
    nw->next = NULL;
    return nw;
}
''',
    "c_types": r'''
/* singly / circular */
struct node {
    int data;
    struct node *next;
};
/* doubly */
struct dnode {
    struct dnode *prev;
    int data;
    struct dnode *next;
};
''',
}
T0 = make_TE(SN)


def T(h, b, examples=None, **kw):
    d = T0(h, b, **kw)
    if examples:
        d["examples"] = examples
    return d


SEC_3_1 = {
    "title": {"en": "3.1 Pointer, Structure and Dynamic Memory Allocation"},
    "items": [
        T("3.1.1 Pointer",
          r"""<p>A <b>pointer</b> is a variable that stores the <b>memory address</b> of another variable.</p>
<h4>Declaration and use</h4>
@@c_ptr@@
<h4>Pointer operators</h4>
<ul><li><b>&amp; (address-of):</b> gives the address of a variable. <code>&amp;x</code> is the address of x.</li>
<li><b>* (indirection / value-at):</b> gives the value stored at the address held by the pointer. <code>*p</code> is the value of x.</li></ul>
<h4>Important points</h4>
<ul><li><b>NULL pointer:</b> a pointer that points to nothing (<code>p = NULL</code>). The last node of a linked list has <code>next = NULL</code>.</li>
<li><b>Pointer arithmetic:</b> <code>p + 1</code> moves by <code>sizeof(data type)</code> bytes. For an int pointer at address 1000, <code>p + 1</code> is 1004 (4-byte int).</li>
<li><b>Pointer and array:</b> the array name is the address of its first element, so <code>a[i]</code> = <code>*(a + i)</code>.</li>
<li><b>Pointer to pointer:</b> <code>int **pp = &amp;p;</code> stores the address of another pointer; <code>**pp</code> is the value of x.</li>
<li><b>Size</b> of every pointer is the same (4 bytes on 32-bit and 8 bytes on 64-bit systems), whatever type it points to.</li></ul>
<h4>Uses / advantages of pointers</h4>
<ul><li>Dynamic memory allocation (malloc, calloc).</li>
<li>Building dynamic data structures: <b>linked list, tree, graph</b>.</li>
<li>Call by reference: a function can change the caller's variables (swap).</li>
<li>Efficient handling of arrays and strings; returning more than one value.</li></ul>""",
          diagram="ds3_pointer", programs=["ds3p1", "ds3p2"], examples=["ds3n1", "ds3n2"], key=True),

        T("3.1.2 Structure",
          r"""<p>A <b>structure</b> is a <b>user-defined data type</b> that groups related data items of <b>different data types</b> under one name. Each item is called a <b>member</b> (field).</p>
<h4>Syntax and example</h4>
@@c_struct@@
<ul><li>The keyword <code>struct</code> defines the structure; the definition itself takes no memory.</li>
<li>Memory is allocated when a variable is declared (<code>s1</code>). Its size is at least the sum of the member sizes (the compiler may add padding).</li>
<li>Members are accessed using the <b>dot (.) operator</b>: <code>s1.roll</code>.</li>
<li>An <b>array of structures</b> stores many records, e.g. 60 students.</li></ul>
<h4>Array vs structure</h4>
<table>
<tr><th>Array</th><th>Structure</th></tr>
<tr><td>Collection of elements of the <b>same</b> type</td><td>Collection of members of <b>different</b> types</td></tr>
<tr><td>Elements accessed by index <code>a[i]</code></td><td>Members accessed by name <code>s.roll</code></td></tr>
<tr><td>Built-in (derived) type</td><td>User-defined type (keyword struct)</td></tr>
<tr><td>e.g. marks of 60 students</td><td>e.g. one student's roll, name and marks</td></tr>
</table>""",
          diagram="ds3_structure", programs=["ds3p3"], examples=["ds3n3"], key=True),

        T("3.1.3 Structure using Pointer",
          r"""<p>A pointer can store the address of a structure variable. Such a pointer is called a <b>structure pointer</b>.</p>
@@c_sptr@@
<ul><li>Members are accessed through a pointer with the <b>arrow operator (-&gt;)</b>.</li>
<li><code>ptr-&gt;roll</code> is the same as <code>(*ptr).roll</code>. The brackets are needed because <b>.</b> has higher precedence than <b>*</b>.</li>
<li>Passing a structure pointer to a function is faster than passing the whole structure (no copy is made).</li>
<li>Incrementing the pointer (<code>ptr++</code>) moves to the next structure in an array.</li></ul>
<h4>Self-referential structure</h4>
<p>A structure that contains a <b>pointer to a structure of the same type</b> is called a self-referential structure. It is the <b>building block of a linked list</b> (and of trees).</p>
@@c_self@@""",
          programs=["ds3p4"], key=True),

        T("3.1.4 Dynamic Memory Allocation (DMA)",
          r"""<p><b>Dynamic memory allocation</b> means allocating memory <b>at run time</b> (during program execution) from the <b>heap</b>, as much as is actually needed. The functions are declared in <code>&lt;stdlib.h&gt;</code>.</p>
<h4>Static vs dynamic allocation</h4>
<table>
<tr><th>Static allocation</th><th>Dynamic allocation</th></tr>
<tr><td>Memory allocated at <b>compile time</b></td><td>Memory allocated at <b>run time</b></td></tr>
<tr><td>Size is fixed and cannot change</td><td>Size can grow or shrink (realloc)</td></tr>
<tr><td>Memory may be wasted or be insufficient</td><td>No wastage: allocate as needed</td></tr>
<tr><td>Uses stack memory</td><td>Uses heap memory</td></tr>
<tr><td>Freed automatically</td><td>Must be freed with <code>free()</code></td></tr>
<tr><td>e.g. <code>int a[100];</code></td><td>e.g. <code>malloc(n * sizeof(int))</code></td></tr>
</table>
<h4>DMA functions</h4>
@@c_dma@@
<ol><li><b>malloc()</b> (memory allocation): allocates <b>one block</b> of the given size in bytes. The memory contains <b>garbage values</b>. It returns a <code>void *</code> pointer, or NULL if memory is not available.</li>
<li><b>calloc()</b> (contiguous allocation): allocates <b>n blocks</b> of the given size and initialises all bytes to <b>zero</b>.</li>
<li><b>realloc()</b> (re-allocation): changes the size of previously allocated memory and keeps the old data.</li>
<li><b>free()</b>: releases dynamically allocated memory back to the heap.</li></ol>
@@c_dma_ex@@
<h4>malloc vs calloc</h4>
<table>
<tr><th>malloc()</th><th>calloc()</th></tr>
<tr><td>One argument: total bytes</td><td>Two arguments: number of blocks and size of each</td></tr>
<tr><td>Memory has garbage values</td><td>Memory is set to 0</td></tr>
<tr><td>Slightly faster</td><td>Slightly slower (initialisation)</td></tr>
</table>
<ul><li><b>Memory leak:</b> allocated memory that is never freed.</li>
<li><b>Dangling pointer:</b> a pointer that still holds the address of freed memory. Set it to NULL after <code>free()</code>.</li></ul>""",
          diagram="ds3_dma", programs=["ds3p5", "ds3p6"], examples=["ds3n4"], key=True),
    ],
}

SEC_3_2 = {
    "title": {"en": "3.2 Linked List"},
    "items": [
        T("3.2.1 Linked List Representation",
          r"""<p>A <b>linked list</b> is a <b>linear</b> collection of data elements called <b>nodes</b>, in which the linear order is given by <b>pointers</b>. Each node points to the next node.</p>
<h4>Node</h4>
<p>Each node has two parts:</p>
<ul><li><b>INFO (data) field:</b> stores the actual data.</li>
<li><b>LINK (next) field:</b> stores the address of the next node.</li></ul>
@@c_self@@
<h4>Representation</h4>
<ul><li>A pointer variable <b>START</b> (or HEAD) holds the address of the <b>first node</b>.</li>
<li>The LINK field of the <b>last node</b> contains <b>NULL</b>, which marks the end of the list.</li>
<li>If <code>START = NULL</code>, the list is <b>empty</b>.</li>
<li>Nodes are created with <b>malloc()</b> and need <b>not</b> be stored in continuous memory locations.</li></ul>
<h4>Creating a node</h4>
@@c_getnode@@
<h4>Advantages</h4>
<ul><li><b>Dynamic size:</b> grows and shrinks at run time; no memory wastage.</li>
<li><b>Easy insertion and deletion:</b> only links change; no shifting of elements.</li>
<li>Used to implement stacks, queues, trees and graphs.</li></ul>
<h4>Disadvantages</h4>
<ul><li><b>Extra memory</b> is needed for the pointer in every node.</li>
<li><b>No random access:</b> to reach the n-th node all previous nodes must be visited (O(n)); binary search is not practical.</li>
<li>Reverse traversal is not possible in a singly linked list.</li></ul>""",
          diagram="ds3_representation", programs=["ds3p7"], examples=["ds3n7"], key=True),

        T("3.2.2 Array vs Linked List",
          r"""<table>
<tr><th>Array</th><th>Linked list</th></tr>
<tr><td>Fixed size, decided at compile time</td><td>Dynamic size, grows and shrinks at run time</td></tr>
<tr><td>Elements stored in <b>continuous</b> memory</td><td>Nodes can be <b>anywhere</b> in memory</td></tr>
<tr><td><b>Random access</b> by index: O(1)</td><td><b>Sequential access</b> only: O(n)</td></tr>
<tr><td>Insertion and deletion need shifting: O(n)</td><td>Insertion and deletion change only links</td></tr>
<tr><td>No extra memory for links</td><td>Extra memory for a pointer in each node</td></tr>
<tr><td>Memory may be wasted (unused size)</td><td>Memory is used as needed</td></tr>
<tr><td>Binary search possible (sorted)</td><td>Only linear search</td></tr>
<tr><td>Static memory allocation</td><td>Dynamic memory allocation</td></tr>
</table>""",
          key=True),

        T("3.2.3 Types of Linked List",
          r"""<h4>1. Singly linked list</h4>
<ul><li>Each node has <b>data</b> and <b>one pointer</b> (next) to the next node.</li>
<li>The last node's next is NULL.</li>
<li>Traversal is possible in the <b>forward direction only</b>.</li></ul>
<h4>2. Circular linked list</h4>
<ul><li>A singly linked list in which the <b>last node points back to the first node</b> instead of NULL.</li>
<li>No node contains NULL. Any node can be the starting point, and the list can be traversed again and again.</li>
<li>Traversal stops when the pointer comes back to START (<code>do … while (p != start)</code>).</li>
<li>Used in round-robin CPU scheduling and multiplayer turn-taking games.</li></ul>
<h4>3. Doubly linked list</h4>
<ul><li>Each node has <b>three</b> parts: <b>prev</b> (address of the previous node), <b>data</b> and <b>next</b> (address of the next node).</li>
<li>The first node's prev and the last node's next are NULL.</li>
<li>Traversal is possible in <b>both directions</b>; deleting a given node is easier.</li>
<li>Needs more memory (two pointers per node).</li>
<li>Used in browser back/forward navigation and in undo/redo.</li></ul>
@@c_types@@
<p>A <b>circular doubly linked list</b> combines both: the last node's next points to the first node, and the first node's prev points to the last node.</p>
<h4>Comparison</h4>
<table>
<tr><th>Point</th><th>Singly</th><th>Circular</th><th>Doubly</th></tr>
<tr><td>Pointers per node</td><td>1</td><td>1</td><td>2</td></tr>
<tr><td>Last node's next</td><td>NULL</td><td>first node</td><td>NULL</td></tr>
<tr><td>Traversal</td><td>forward</td><td>forward, circular</td><td>forward and backward</td></tr>
<tr><td>Memory</td><td>less</td><td>less</td><td>more</td></tr>
</table>""",
          diagram="ds3_types", programs=["ds3p14", "ds3p15"], key=True),

        T("3.2.4 Applications of Linked List",
          r"""<ol><li><b>Implementation of stack and queue</b> without a size limit (dynamic stack and queue).</li>
<li><b>Polynomial representation and arithmetic:</b> each node stores a coefficient and an exponent, e.g. 5x³ + 4x² + 2 → (5,3) → (4,2) → (2,0).</li>
<li><b>Dynamic memory management:</b> the operating system keeps lists of free memory blocks.</li>
<li><b>Representation of trees and graphs</b> (adjacency list).</li>
<li><b>Sparse matrix</b> representation: only non-zero elements are stored.</li>
<li><b>Undo/redo</b> in editors and <b>back/forward</b> in browsers (doubly linked list).</li>
<li><b>Music playlist and image viewer:</b> next and previous item; a circular list repeats the playlist.</li>
<li><b>Round-robin scheduling</b> in an operating system (circular linked list).</li>
<li>Large-number arithmetic: each node stores some digits of a very long number.</li></ol>"""),
    ],
}

NOTES_A = [SEC_3_1, SEC_3_2]
