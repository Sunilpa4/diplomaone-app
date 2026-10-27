"""DI01000131 Unit 3 notes part B: 3.2 Pointers (English only)."""
from c_content import make_TE

SN = {
    "intro": r'''
int x = 25;       /* x: value 25, stored at (say) 1000 */
int *p = &x;      /* p: value 1000 = address of x     */
''',
    "addr": r'''
int x = 25;
printf("%d\n", x);          /* 25 */
printf("%p\n", (void *) &x); /* address */
scanf("%d", &x);    /* & passes the address */
''',
    "addr_bad": r'''
&125          /* error: constant has no address  */
&(a + b)      /* error: expression has no address */
int arr[5];
&arr          /* allowed, but arr alone is already an address */
''',
    "deref": r'''
int x = 25, y;
int *p = &x;
y = *p;       /* y = 25   (read through pointer)  */
*p = 40;      /* x = 40   (write through pointer) */
''',
    "decl": r'''
data_type *pointer_name;
''',
    "decl_ex": r'''
int   *ip;        /* pointer to int   */
float *fp;        /* pointer to float */
char  *cp;        /* pointer to char  */
int   *a, *b;     /* two pointers */
int   *c, d;      /* c is pointer, d is int! */
''',
    "init": r'''
int x = 10;
int *p;
p = &x;           /* initialization by assignment */

int y = 20;
int *q = &y;      /* declaration + initialization */

int *r = NULL;    /* points nowhere (safe) */
int *s = q;       /* copy of another pointer */
''',
    "init_bad": r'''
float f = 2.5;
int *p = &f;      /* wrong: type mismatch */
int *q = 1000;    /* wrong: integer is not an address */
int *w;
*w = 5;           /* wrong: wild pointer, garbage address */
''',
    "ptr_ptr": r'''
int x = 25;
int *p = &x;
int **q = &p;     /* pointer to pointer */
printf("%d", **q);  /* 25 */
''',
    "arith": r'''
int a[5] = {10, 20, 30, 40, 50};
int *p = a;       /* p = &a[0] */
p++;              /* now p = &a[1]  (address + 4) */
printf("%d", *p);       /* 20 */
printf("%d", *(p + 2)); /* 40 */
''',
    "void_ex": r'''
void *vp;
int n = 5;
vp = &n;
printf("%d", *(int *) vp);   /* cast before * */
''',
    "null_ex": r'''
#include <stdio.h>     /* NULL is defined here */
int *p = NULL;
if (p != NULL)
    printf("%d", *p);  /* safe */
''',
}
T = make_TE(SN)

SEC_3_2 = {
    "title": {"en": "3.2 Pointers"},
    "items": [
        T("3.2.1 Introduction to Pointers",
          r"""<p>Computer memory is a sequence of storage cells (bytes), and each byte has a unique number called its <b>address</b>. When a variable is declared, the compiler reserves memory for it at some address.</p>
<p><b>Definition:</b> A <b>pointer</b> is a <b>variable that stores the memory address</b> of another variable.</p>
@@intro@@
<p>Since p contains the address of x, we say "<b>p points to x</b>" (see diagram). A pointer variable has its own address too (here 2000).</p>
<h4>Why pointers? (Applications)</h4>
<ul><li>Access and change variables indirectly (e.g. swap via functions – call by reference).</li>
<li>Return more than one value from a function.</li>
<li>Efficient handling of arrays and strings.</li>
<li>Dynamic memory allocation (malloc, calloc).</li>
<li>Building data structures: linked lists, trees, stacks.</li>
<li>File handling (FILE pointers, Unit 5).</li></ul>""",
          diagram="c3_pointer"),

        T("3.2.2 Characteristics of Pointers",
          r"""<ul>
<li>A pointer stores an <b>address</b>, not an ordinary value.</li>
<li>Every pointer has a <b>type</b>: an <code>int *</code> points to an int, a <code>float *</code> to a float. The type tells the compiler how many bytes to read at that address.</li>
<li>The <b>size of a pointer</b> is the same for all types on a given system (4 bytes on 32-bit, 8 bytes on 64-bit), because it stores only an address.</li>
<li><b>&amp;</b> gives the address of a variable; <b>*</b> gives the value at an address.</li>
<li>A pointer must be <b>initialized</b> before use; otherwise it is a <b>wild pointer</b> with a garbage address.</li>
<li><b>Pointer arithmetic</b> is allowed: <code>p + 1</code> moves to the next element (address + sizeof(type)).</li>
<li>The <b>array name</b> is a constant pointer to the first element.</li>
<li>A pointer can point to another pointer (<b>pointer to pointer</b>, <code>int **q</code>).</li>
<li>Special types: <b>void pointer</b> (generic) and <b>NULL pointer</b> (points nowhere).</li>
</ul>
<h4>Advantages and disadvantages</h4>
<table><tr><th>Advantages</th><th>Disadvantages</th></tr>
<tr><td>Faster, efficient array/string handling</td><td>Uninitialized pointers cause crashes</td></tr>
<tr><td>Call by reference; return many values</td><td>Hard to understand and debug</td></tr>
<tr><td>Dynamic memory allocation</td><td>Memory leaks if memory is not freed</td></tr>
<tr><td>Data structures (lists, trees)</td><td>Can corrupt other data by wrong addresses</td></tr></table>"""),

        T("3.2.3 Address of Operator (&) and Indirection Operator (*)",
          r"""<h4>1. Address of operator ( &amp; )</h4>
<p>The unary operator <b>&amp;</b> returns the <b>memory address</b> of its operand. It is read as "<b>address of</b>". <code>%p</code> is used to print an address.</p>
@@addr@@
<p>&amp; can be used only with variables and array elements, not with constants or expressions:</p>
@@addr_bad@@
<h4>2. Indirection operator ( * )</h4>
<p>The unary operator <b>*</b>, applied to a pointer, gives the <b>value stored at the address</b> the pointer holds. It is read as "<b>value at address</b>" and is also called the <b>dereference</b> operator.</p>
@@deref@@
<h4>Relation between &amp; and *</h4>
<table><tr><th>Expression</th><th>Value (x = 25 at 1000, p = &amp;x at 2000)</th></tr>
<tr><td><code>x</code></td><td>25</td></tr><tr><td><code>&amp;x</code></td><td>1000</td></tr>
<tr><td><code>p</code></td><td>1000</td></tr><tr><td><code>*p</code></td><td>25</td></tr>
<tr><td><code>&amp;p</code></td><td>2000</td></tr><tr><td><code>*&amp;x</code></td><td>25 (* and &amp; cancel)</td></tr></table>
<p><b>Note:</b> the * in a declaration (<code>int *p;</code>) only says that p is a pointer; the * in an expression (<code>*p</code>) means "value at".</p>""",
          programs=["c3p12"]),

        T("3.2.4 Declaration and Initialization of Pointers",
          r"""<h4>Declaration</h4>
<p><b>Syntax:</b></p>
@@decl@@
<ul><li><b>*</b> tells the compiler that the variable is a pointer.</li>
<li><b>data_type</b> is the type of the variable the pointer will point to.</li></ul>
@@decl_ex@@
<h4>Initialization</h4>
<p>Assigning the address of a variable to a pointer is called <b>pointer initialization</b>. The variable must be declared before its address is taken.</p>
@@init@@
<h4>Rules / common errors</h4>
@@init_bad@@
<ul><li>The data type of the pointer and the variable must match.</li>
<li>Never use <code>*p</code> before p holds a valid address.</li>
<li>If no address is available yet, initialize with <code>NULL</code>.</li></ul>
<h4>Pointer to pointer</h4>
<p>A pointer that stores the address of another pointer is declared with two stars (see diagram):</p>
@@ptr_ptr@@""",
          diagram="c3_ptr_ptr", programs=["c3p13"]),

        T("3.2.5 Pointer Arithmetic and Arrays",
          r"""<p>The name of an array is the <b>address of its first element</b>: <code>a == &amp;a[0]</code>. So a pointer can be set to an array and moved through it.</p>
@@arith@@
<h4>Allowed pointer operations</h4>
<ul><li><code>p + n</code>, <code>p - n</code>, <code>p++</code>, <code>p--</code>: move n <b>elements</b> forward/back. The address changes by <code>n × sizeof(type)</code>.</li>
<li><code>p2 - p1</code>: number of elements between two pointers into the same array.</li>
<li>Comparison <code>p1 &lt; p2</code>, <code>p == NULL</code>.</li></ul>
<h4>Not allowed</h4>
<p>Adding two pointers (<code>p1 + p2</code>), multiplying or dividing pointers, adding a float to a pointer.</p>
<h4>Equivalent notations (see diagram)</h4>
<p style="text-align:center"><code>a[i]  ≡  *(a + i)  ≡  *(p + i)  ≡  p[i]</code>  and  <code>&amp;a[i]  ≡  a + i</code></p>""",
          diagram="c3_ptr_array", programs=["c3p14"]),

        T("3.2.6 Types of Pointers: void Pointer",
          r"""<p>A <b>void pointer</b> is a <b>generic pointer</b> declared with type <code>void</code>. It can hold the address of a variable of <b>any data type</b>.</p>
<p><b>Syntax:</b> <code>void *pointer_name;</code></p>
@@void_ex@@
<h4>Features</h4>
<ul><li>One void pointer can point to int, float, char, … at different times.</li>
<li>It <b>cannot be dereferenced directly</b>; it must first be type-cast to the proper pointer type: <code>*(float *) vp</code>.</li>
<li>Pointer arithmetic is not allowed on void pointers (the size of the data is unknown).</li>
<li>Used in generic functions: <code>malloc()</code> and <code>calloc()</code> return <code>void *</code>; <code>memcpy()</code> and <code>qsort()</code> take void pointers.</li></ul>""",
          diagram="c3_void_null", programs=["c3p15"]),

        T("3.2.7 Types of Pointers: NULL Pointer",
          r"""<p>A <b>NULL pointer</b> is a pointer that <b>does not point to any valid memory location</b>. It is created by assigning the constant <code>NULL</code> (defined in <code>&lt;stdio.h&gt;</code>, <code>&lt;stdlib.h&gt;</code>, value 0).</p>
<p><b>Syntax:</b> <code>data_type *pointer_name = NULL;</code></p>
@@null_ex@@
<h4>Uses</h4>
<ul><li>To initialize a pointer when no address is available yet (avoids wild pointers).</li>
<li>To check whether a pointer is valid before dereferencing it.</li>
<li>Functions return NULL to signal failure: <code>malloc()</code> when memory is not available, <code>fopen()</code> when a file cannot be opened (Unit 5).</li>
<li>To mark the end of linked lists.</li></ul>
<p>Dereferencing a NULL pointer gives a run-time error (segmentation fault).</p>
<h4>Comparison of special pointers</h4>
<table><tr><th>Pointer</th><th>Meaning</th><th>Safe to use *?</th></tr>
<tr><td><b>void pointer</b></td><td>Generic pointer to any type</td><td>Only after casting</td></tr>
<tr><td><b>NULL pointer</b></td><td>Points to nothing (value 0)</td><td>No – check first</td></tr>
<tr><td><b>Wild pointer</b></td><td>Uninitialized, garbage address</td><td>No – always initialize</td></tr>
<tr><td><b>Dangling pointer</b></td><td>Points to memory that was freed or no longer exists</td><td>No – set to NULL after free</td></tr></table>
<p><b>void pointer vs NULL pointer:</b> void is a <i>type</i> of pointer (generic), whereas NULL is a <i>value</i> of a pointer (no address). A void pointer can also be NULL.</p>""",
          programs=["c3p16"]),

        T("Key Points – 3.2",
          r"""<ul>
<li>Pointer = variable that stores the <b>address</b> of another variable: <code>int *p = &amp;x;</code></li>
<li><b>&amp;</b> address-of operator; <b>*</b> indirection (value-at) operator; <code>*&amp;x == x</code>.</li>
<li>Declare: <code>type *name;</code> – the pointer type must match the variable type.</li>
<li>Pointer size is the same for all types (8 bytes on 64-bit). Print addresses with <code>%p</code>.</li>
<li><code>p + 1</code> moves by sizeof(type); <code>a[i] ≡ *(a + i)</code>.</li>
<li><b>void pointer</b>: generic, cast before * (<code>*(int *)vp</code>).</li>
<li><b>NULL pointer</b>: points nowhere; check <code>if (p != NULL)</code> before use.</li>
<li>Wild pointer = uninitialized; dangling pointer = points to freed memory.</li>
</ul>""", key=True),
    ],
}

NOTES_B = [SEC_3_2]
