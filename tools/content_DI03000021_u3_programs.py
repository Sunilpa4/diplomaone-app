"""DI03000021 Unit 3 - solved C programs (pointer, structure, DMA, linked lists). gcc-verified."""
from c_content import PE

PROGRAMS = [
    PE("ds3p1", "Pointer basics: &, * and swapping using pointers", r'''
#include <stdio.h>

void swap(int *a, int *b)
{
    int t = *a;
    *a = *b;
    *b = t;
}

int main(void)
{
    int x = 10, y = 20;
    int *p = &x;

    printf("x = %d, *p = %d\n", x, *p);
    *p = 50;              /* changes x */
    printf("after *p = 50, x = %d\n", x);
    printf("p == &x ? %s\n",
           p == &x ? "yes" : "no");

    swap(&x, &y);
    printf("after swap: x = %d, y = %d\n",
           x, y);
    return 0;
}
''', (),
       r"""<ul><li><code>p = &amp;x</code> stores the <b>address</b> of x in p; <code>*p</code> gives the <b>value at</b> that address.</li>
<li>Writing <code>*p = 50</code> changes x itself, because p points to x.</li>
<li><code>swap()</code> receives addresses (<b>call by reference</b>), so it can change the caller's variables.</li></ul>"""),

    PE("ds3p2", "Pointer arithmetic: traverse an array with a pointer", r'''
#include <stdio.h>

int main(void)
{
    int a[5] = {12, 7, 25, 3, 18};
    int *p = a;     /* same as &a[0] */
    int i, sum = 0, max = *p;

    for (i = 0; i < 5; i++) {
        printf("*(p+%d) = %d\n", i,
               *(p + i));
        sum += *(p + i);
        if (*(p + i) > max)
            max = *(p + i);
    }
    printf("Sum = %d, Max = %d\n",
           sum, max);
    printf("p+1 moves %d bytes\n",
           (int)sizeof(*p));
    return 0;
}
''', (),
       r"""<ul><li>The array name <code>a</code> is the address of the first element, so <code>p = a</code>.</li>
<li><code>*(p + i)</code> is the same as <code>a[i]</code>. Adding 1 to an int pointer moves it by <code>sizeof(int)</code> bytes (4), not by 1 byte.</li></ul>"""),

    PE("ds3p3", "Structure: read and display student records", r'''
#include <stdio.h>

struct student {
    int roll;
    char name[20];
    float marks;
};

int main(void)
{
    struct student s[3];
    int i;

    for (i = 0; i < 3; i++)
        scanf("%d %19s %f", &s[i].roll,
              s[i].name, &s[i].marks);

    printf("Roll  Name      Marks\n");
    for (i = 0; i < 3; i++)
        printf("%-5d %-9s %.1f\n",
               s[i].roll, s[i].name,
               s[i].marks);
    return 0;
}
''', ("1 Ravi 78.5", "2 Meena 91", "3 Amit 66.5"),
       r"""<ul><li>A <b>structure</b> groups related data of different types (int, char array, float) under one name.</li>
<li>An array of structures <code>s[3]</code> stores three complete records.</li>
<li>Members are accessed with the <b>dot operator</b>: <code>s[i].roll</code>.</li></ul>"""),

    PE("ds3p4", "Structure using pointer: find the topper with -> [Practical 5]", r'''
#include <stdio.h>

struct student {
    int roll;
    char name[20];
    float marks;
};

void show(struct student *p)
{
    printf("%d %s %.1f\n", p->roll,
           p->name, p->marks);
}

int main(void)
{
    struct student s[4] = {
        {1, "Ravi", 78.5},
        {2, "Meena", 91},
        {3, "Amit", 66},
        {4, "Neha", 88}
    };
    struct student *ptr, *top = s;

    for (ptr = s; ptr < s + 4; ptr++) {
        show(ptr);
        if (ptr->marks > top->marks)
            top = ptr;
    }
    printf("Topper: %s (%.1f)\n",
           top->name, top->marks);
    return 0;
}
''', (),
       r"""<ul><li><code>ptr</code> is a <b>pointer to a structure</b>; members are reached with the <b>arrow operator</b> <code>ptr-&gt;marks</code>, which is the same as <code>(*ptr).marks</code>.</li>
<li><code>ptr++</code> moves to the next record (by <code>sizeof(struct student)</code> bytes).</li>
<li>Passing a pointer to <code>show()</code> avoids copying the whole structure.</li></ul>"""),

    PE("ds3p5", "Dynamic memory: malloc for n numbers, then free", r'''
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int n, i, sum = 0;
    int *a;

    printf("How many numbers? ");
    scanf("%d", &n);
    a = (int *) malloc(n * sizeof(int));
    if (a == NULL) {
        printf("Memory not available\n");
        return 1;
    }
    for (i = 0; i < n; i++) {
        scanf("%d", &a[i]);
        sum += a[i];
    }
    printf("Sum = %d, Average = %.2f\n",
           sum, (float)sum / n);
    free(a);
    return 0;
}
''', ("5", "10 20 30 40 55"),
       r"""<ul><li>The size <b>n</b> is known only at run time, so memory is taken from the <b>heap</b> with <code>malloc()</code>.</li>
<li><code>malloc</code> returns <code>void *</code> (cast to <code>int *</code>) or <b>NULL</b> if memory is not available, so always check it.</li>
<li><code>free(a)</code> returns the memory. Forgetting it causes a <b>memory leak</b>.</li></ul>"""),

    PE("ds3p6", "calloc and realloc: grow an array at run time", r'''
#include <stdio.h>
#include <stdlib.h>

void show(int *a, int n)
{
    int i;
    for (i = 0; i < n; i++)
        printf("%d ", a[i]);
    printf("\n");
}

int main(void)
{
    int i, *a, *t;

    a = (int *) calloc(3, sizeof(int));
    if (a == NULL) return 1;
    printf("after calloc : ");
    show(a, 3);              /* all 0 */

    for (i = 0; i < 3; i++)
        a[i] = (i + 1) * 10;
    t = realloc(a, 5 * sizeof(int));
    if (t == NULL) { free(a); return 1; }
    a = t;
    a[3] = 40;
    a[4] = 50;
    printf("after realloc: ");
    show(a, 5);
    free(a);
    return 0;
}
''', (),
       r"""<ul><li><code>calloc(3, sizeof(int))</code> allocates 3 blocks and sets them all to <b>0</b> (malloc leaves garbage).</li>
<li><code>realloc</code> resizes the block to 5 ints and <b>keeps the old values</b> 10, 20, 30.</li>
<li>The result is stored in a temporary pointer <code>t</code> first, so the old block is not lost if realloc fails.</li></ul>"""),

    PE("ds3p7", "Create a singly linked list of n nodes and display it", r'''
#include <stdio.h>
#include <stdlib.h>

struct node {
    int data;
    struct node *next;
};

int main(void)
{
    struct node *start = NULL;
    struct node *last = NULL;
    struct node *nw, *ptr;
    int n, i, x;

    scanf("%d", &n);
    for (i = 0; i < n; i++) {
        scanf("%d", &x);
        nw = malloc(sizeof(struct node));
        nw->data = x;
        nw->next = NULL;
        if (start == NULL)
            start = nw;
        else
            last->next = nw;
        last = nw;
    }
    printf("List: ");
    for (ptr = start; ptr != NULL;
         ptr = ptr->next)
        printf("%d -> ", ptr->data);
    printf("NULL\n");
    return 0;
}
''', ("4", "10 20 30 40"),
       r"""<ul><li>Each node is a <b>self-referential structure</b>: data plus a pointer to the next node.</li>
<li>Every node is created with <code>malloc</code>. The first node becomes <code>start</code>; later nodes are joined with <code>last-&gt;next = nw</code>.</li>
<li>Keeping a <code>last</code> pointer makes each append O(1). Display walks from start until <b>NULL</b>.</li></ul>"""),

    PE("ds3p8", "Insert a node at the beginning and at the end", r'''
#include <stdio.h>
#include <stdlib.h>

struct node {
    int data;
    struct node *next;
};
struct node *start = NULL;

struct node *getnode(int x)
{
    struct node *nw;
    nw = malloc(sizeof(struct node));
    nw->data = x;
    nw->next = NULL;
    return nw;
}

void ins_beg(int x)
{
    struct node *nw = getnode(x);
    nw->next = start;
    start = nw;
}

void ins_end(int x)
{
    struct node *nw = getnode(x), *p;
    if (start == NULL) {
        start = nw;
        return;
    }
    for (p = start; p->next != NULL;
         p = p->next)
        ;
    p->next = nw;
}

void display(void)
{
    struct node *p;
    for (p = start; p != NULL; p = p->next)
        printf("%d -> ", p->data);
    printf("NULL\n");
}

int main(void)
{
    ins_end(20); ins_end(30);
    display();
    ins_beg(10);
    display();
    ins_end(40);
    display();
    return 0;
}
''', (),
       r"""<ul><li><b>Beginning:</b> <code>nw-&gt;next = start; start = nw;</code>. No traversal, so O(1). The order matters: link first, then move start.</li>
<li><b>End:</b> walk to the last node (the one whose next is NULL), then <code>p-&gt;next = nw</code>. This is O(n).</li>
<li>The empty-list case (<code>start == NULL</code>) must be handled separately.</li></ul>"""),

    PE("ds3p9", "Insert a node after / before a given node", r'''
#include <stdio.h>
#include <stdlib.h>

struct node {
    int data;
    struct node *next;
};
struct node *start = NULL;

struct node *getnode(int x)
{
    struct node *nw;
    nw = malloc(sizeof(struct node));
    nw->data = x;
    nw->next = NULL;
    return nw;
}

void ins_after(int key, int x)
{
    struct node *p = start, *nw;
    while (p != NULL && p->data != key)
        p = p->next;
    if (p == NULL) {
        printf("%d not found\n", key);
        return;
    }
    nw = getnode(x);
    nw->next = p->next;
    p->next = nw;
}

void ins_before(int key, int x)
{
    struct node *p = start, *prev = NULL;
    struct node *nw;
    while (p != NULL && p->data != key) {
        prev = p;
        p = p->next;
    }
    if (p == NULL) {
        printf("%d not found\n", key);
        return;
    }
    nw = getnode(x);
    nw->next = p;
    if (prev == NULL)
        start = nw;        /* before 1st */
    else
        prev->next = nw;
}

void display(void)
{
    struct node *p;
    for (p = start; p != NULL; p = p->next)
        printf("%d -> ", p->data);
    printf("NULL\n");
}

int main(void)
{
    start = getnode(10);
    start->next = getnode(30);
    display();
    ins_after(10, 20);
    display();
    ins_before(10, 5);
    ins_before(30, 25);
    display();
    ins_after(99, 1);
    return 0;
}
''', (),
       r"""<ul><li><b>After key:</b> find the key node p, then <code>nw-&gt;next = p-&gt;next; p-&gt;next = nw;</code>.</li>
<li><b>Before key:</b> a second pointer <code>prev</code> trails one node behind p, because a singly list cannot move backwards. The new node goes between prev and p.</li>
<li>If the key is the first node (prev is NULL), the new node becomes the new <code>start</code>.</li></ul>"""),

    PE("ds3p10", "Insert into a sorted linked list (builds an ordered list)", r'''
#include <stdio.h>
#include <stdlib.h>

struct node {
    int data;
    struct node *next;
};
struct node *start = NULL;

void ins_sorted(int x)
{
    struct node *nw, *p;
    nw = malloc(sizeof(struct node));
    nw->data = x;
    if (start == NULL || x < start->data) {
        nw->next = start;
        start = nw;
        return;
    }
    p = start;
    while (p->next != NULL &&
           p->next->data < x)
        p = p->next;
    nw->next = p->next;
    p->next = nw;
}

void display(void)
{
    struct node *p;
    for (p = start; p != NULL; p = p->next)
        printf("%d ", p->data);
    printf("\n");
}

int main(void)
{
    int a[6] = {30, 10, 50, 20, 5, 40};
    int i;
    for (i = 0; i < 6; i++) {
        ins_sorted(a[i]);
        printf("insert %2d: ", a[i]);
        display();
    }
    return 0;
}
''', (),
       r"""<ul><li>The list always stays in <b>ascending order</b>, whatever the input order.</li>
<li>If x is smaller than the first node (or the list is empty), it goes at the beginning.</li>
<li>Otherwise p stops at the last node whose <b>next</b> is not smaller than x, and the new node is inserted after p.</li>
<li>The output shows the list after every insertion: 5 goes at the front, 50 at the end, 20 in the middle.</li></ul>"""),

    PE("ds3p11", "Delete the first node and the last node", r'''
#include <stdio.h>
#include <stdlib.h>

struct node {
    int data;
    struct node *next;
};
struct node *start = NULL;

void push_front(int x)
{
    struct node *nw;
    nw = malloc(sizeof(struct node));
    nw->data = x;
    nw->next = start;
    start = nw;
}

void del_first(void)
{
    struct node *p = start;
    if (p == NULL) {
        printf("List empty\n");
        return;
    }
    start = start->next;
    printf("deleted %d\n", p->data);
    free(p);
}

void del_last(void)
{
    struct node *p = start, *prev = NULL;
    if (p == NULL) {
        printf("List empty\n");
        return;
    }
    while (p->next != NULL) {
        prev = p;
        p = p->next;
    }
    if (prev == NULL)
        start = NULL;      /* only node */
    else
        prev->next = NULL;
    printf("deleted %d\n", p->data);
    free(p);
}

void display(void)
{
    struct node *p;
    for (p = start; p != NULL; p = p->next)
        printf("%d ", p->data);
    printf("\n");
}

int main(void)
{
    int i;
    for (i = 4; i >= 1; i--)
        push_front(i * 10);
    display();
    del_first();  display();
    del_last();   display();
    del_last(); del_last(); del_last();
    return 0;
}
''', (),
       r"""<ul><li><b>Delete first:</b> save start in p, move <code>start = start-&gt;next</code>, then <code>free(p)</code>. O(1).</li>
<li><b>Delete last:</b> walk with p and prev until p is the last node, set <code>prev-&gt;next = NULL</code>, then free p. O(n).</li>
<li>Special cases: an empty list (underflow message) and a single node (start becomes NULL). The last call shows "List empty".</li></ul>"""),

    PE("ds3p12", "Search a node and count the nodes", r'''
#include <stdio.h>
#include <stdlib.h>

struct node {
    int data;
    struct node *next;
};
struct node *start = NULL;

void append(int x)
{
    struct node *nw, *p;
    nw = malloc(sizeof(struct node));
    nw->data = x;
    nw->next = NULL;
    if (start == NULL) {
        start = nw;
        return;
    }
    for (p = start; p->next; p = p->next)
        ;
    p->next = nw;
}

int count(void)
{
    int c = 0;
    struct node *p;
    for (p = start; p != NULL; p = p->next)
        c++;
    return c;
}

int search(int x)
{
    int pos = 1;
    struct node *p;
    for (p = start; p; p = p->next) {
        if (p->data == x)
            return pos;
        pos++;
    }
    return -1;
}

int main(void)
{
    int a[5] = {15, 42, 8, 23, 4}, i, k;
    for (i = 0; i < 5; i++)
        append(a[i]);
    printf("Total nodes = %d\n", count());
    k = search(23);
    printf("23 found at position %d\n", k);
    k = search(99);
    if (k == -1)
        printf("99 not found\n");
    return 0;
}
''', (),
       r"""<ul><li>Both operations <b>traverse</b> the list from start to NULL.</li>
<li><b>count()</b> adds 1 for every node visited.</li>
<li><b>search()</b> compares each node's data with x and returns its <b>position</b> (1-based), or −1 if it reaches NULL.</li>
<li>A linked list has no index, so only <b>linear search</b> is possible (O(n)); binary search is not practical.</li></ul>"""),

    PE("ds3p13", "Singly linked list menu: insert, delete, search, count [Practicals 6-9]", r'''
#include <stdio.h>
#include <stdlib.h>

struct node {
    int data;
    struct node *next;
};
struct node *start = NULL;

void ins_beg(int x)
{
    struct node *nw;
    nw = malloc(sizeof(struct node));
    nw->data = x;
    nw->next = start;
    start = nw;
}

void ins_end(int x)
{
    struct node *nw, *p;
    nw = malloc(sizeof(struct node));
    nw->data = x;
    nw->next = NULL;
    if (start == NULL) {
        start = nw;
        return;
    }
    for (p = start; p->next; p = p->next)
        ;
    p->next = nw;
}

void del_beg(void)
{
    struct node *p = start;
    if (p == NULL) {
        printf("Empty\n");
        return;
    }
    start = p->next;
    printf("Deleted %d\n", p->data);
    free(p);
}

void del_end(void)
{
    struct node *p = start, *q = NULL;
    if (p == NULL) {
        printf("Empty\n");
        return;
    }
    while (p->next) { q = p; p = p->next; }
    if (q) q->next = NULL;
    else start = NULL;
    printf("Deleted %d\n", p->data);
    free(p);
}

void display(void)
{
    struct node *p;
    int c = 0;
    for (p = start; p; p = p->next, c++)
        printf("%d ", p->data);
    printf("(count = %d)\n", c);
}

int search(int x)
{
    struct node *p;
    int pos = 1;
    for (p = start; p; p = p->next, pos++)
        if (p->data == x) return pos;
    return -1;
}

void menu(void)
{
    puts("1.AddBeg 2.AddEnd 3.DelBeg");
    puts("4.DelEnd 5.Find 6.Show 0.Exit");
}

int main(void)
{
    int ch, x;
    do {
        menu();
        scanf("%d", &ch);
        switch (ch) {
        case 1: scanf("%d", &x);
                ins_beg(x); break;
        case 2: scanf("%d", &x);
                ins_end(x); break;
        case 3: del_beg(); break;
        case 4: del_end(); break;
        case 5: scanf("%d", &x);
                printf("Position: %d\n",
                       search(x));
                break;
        case 6: display(); break;
        }
    } while (ch != 0);
    return 0;
}
''', ("2 20", "2 30", "1 10", "6", "5 30", "3", "4", "6", "0"),
       r"""<ul><li>The complete practical program: a menu-driven singly linked list.</li>
<li>Sample run: insert 20 and 30 at the end, 10 at the beginning → list 10 20 30; search 30 → position 3; delete first (10) and last (30) → only 20 remains.</li>
<li><code>display()</code> also counts the nodes while printing them.</li>
<li>Each delete function handles the <b>empty</b> list; del_end also handles the <b>single node</b> case.</li></ul>"""),

    PE("ds3p14", "Circular linked list: create and display", r'''
#include <stdio.h>
#include <stdlib.h>

struct node {
    int data;
    struct node *next;
};

int main(void)
{
    struct node *start = NULL;
    struct node *last = NULL;
    struct node *nw, *p;
    int i, c = 0;

    for (i = 1; i <= 4; i++) {
        nw = malloc(sizeof(struct node));
        nw->data = i * 10;
        if (start == NULL)
            start = nw;
        else
            last->next = nw;
        last = nw;
        last->next = start;  /* circle */
    }
    p = start;
    do {
        printf("%d -> ", p->data);
        p = p->next;
        c++;
    } while (p != start);
    printf("(back to %d)\n", p->data);
    printf("nodes = %d\n", c);
    printf("last->next->data = %d\n",
           last->next->data);
    return 0;
}
''', (),
       r"""<ul><li>In a <b>circular</b> list the last node's next points back to the <b>first</b> node; no node contains NULL.</li>
<li>The traversal uses <code>do … while (p != start)</code>: it stops when it comes round to start again. A <code>p != NULL</code> loop would never end.</li>
<li><code>last-&gt;next-&gt;data</code> is 10, which proves the circle is closed.</li></ul>"""),

    PE("ds3p15", "Doubly linked list: display forward and backward", r'''
#include <stdio.h>
#include <stdlib.h>

struct dnode {
    struct dnode *prev;
    int data;
    struct dnode *next;
};

int main(void)
{
    struct dnode *start = NULL;
    struct dnode *last = NULL;
    struct dnode *nw, *p;
    int i;

    for (i = 1; i <= 4; i++) {
        nw = malloc(sizeof(struct dnode));
        nw->data = i * 10;
        nw->next = NULL;
        nw->prev = last;
        if (start == NULL)
            start = nw;
        else
            last->next = nw;
        last = nw;
    }
    printf("Forward : ");
    for (p = start; p; p = p->next)
        printf("%d ", p->data);
    printf("\nBackward: ");
    for (p = last; p; p = p->prev)
        printf("%d ", p->data);
    printf("\n");
    return 0;
}
''', (),
       r"""<ul><li>Each node of a <b>doubly</b> linked list has two pointers: <code>prev</code> and <code>next</code>.</li>
<li>A new node's prev points to the old last node, and the old last node's next points to the new node.</li>
<li>So the list can be traversed in <b>both directions</b>: forward from start using next, backward from last using prev. The extra pointer costs more memory per node.</li></ul>"""),
]
