"""DI03000021 Unit 2 - solved C programs (stack, expressions, recursion, queue, circular queue). gcc-verified."""
from c_content import PE

PROGRAMS = [
    PE("ds2p1", "Stack using an array: PUSH, POP, PEEK, DISPLAY [Practical 2]", r'''
#include <stdio.h>
#define MAX 5

int stack[MAX], top = -1;

void push(int x)
{
    if (top == MAX - 1) {
        printf("Stack Overflow\n");
        return;
    }
    stack[++top] = x;
    printf("%d pushed\n", x);
}

int pop(void)
{
    if (top == -1) {
        printf("Stack Underflow\n");
        return -1;
    }
    return stack[top--];
}

void peek(void)
{
    if (top == -1)
        printf("Stack is empty\n");
    else
        printf("Top = %d\n", stack[top]);
}

void display(void)
{
    int i;
    if (top == -1) {
        printf("Stack is empty\n");
        return;
    }
    printf("Stack (top to bottom): ");
    for (i = top; i >= 0; i--)
        printf("%d ", stack[i]);
    printf("\n");
}

int main(void)
{
    int ch, x;
    do {
        printf("1.Push 2.Pop 3.Peek");
        printf(" 4.Show 5.Exit: ");
        scanf("%d", &ch);
        switch (ch) {
        case 1:
            printf("Value: ");
            scanf("%d", &x);
            push(x);
            break;
        case 2:
            x = pop();
            if (x != -1)
                printf("Popped %d\n", x);
            break;
        case 3: peek(); break;
        case 4: display(); break;
        }
    } while (ch != 5);
    return 0;
}
''', ["1", "10", "1", "20", "1", "30", "4", "2", "3", "4", "5"],
       r"""<ul><li><code>top</code> holds the index of the top element. <b>−1</b> means the stack is empty.</li>
<li><b>PUSH:</b> first check for overflow (<code>top == MAX − 1</code>), then <code>stack[++top] = x</code> (increment first, then store).</li>
<li><b>POP:</b> first check for underflow (<code>top == −1</code>), then <code>return stack[top--]</code> (read first, then decrement).</li>
<li><b>PEEK</b> only reads the top element without removing it.</li>
<li>Display runs from <code>top</code> down to 0, so the last pushed value (30) appears first: <b>LIFO</b>.</li>
<li>Every operation is <b>O(1)</b>, except display, which is O(n).</li></ul>"""),

    PE("ds2p2", "Stack overflow and underflow", r'''
#include <stdio.h>
#define MAX 3

int s[MAX], top = -1;

int push(int x)
{
    if (top == MAX - 1)
        return 0;             // overflow
    s[++top] = x;
    return 1;
}

int pop(int *x)
{
    if (top == -1)
        return 0;             // underflow
    *x = s[top--];
    return 1;
}

int main(void)
{
    int i, v;
    for (i = 1; i <= 4; i++) {
        if (push(i * 10))
            printf("push %d top=%d\n",
                   i * 10, top);
        else
            printf("push %d OVERFLOW\n",
                   i * 10);
    }
    for (i = 1; i <= 4; i++) {
        if (pop(&v))
            printf("pop  %d top=%d\n",
                   v, top);
        else
            printf("pop     UNDERFLOW\n");
    }
    return 0;
}
''', (),
       r"""<ul><li>The stack holds only <b>MAX = 3</b> elements, so the 4th push fails: <b>overflow</b>.</li>
<li>After three pops the stack is empty, so the 4th pop fails: <b>underflow</b>.</li>
<li>The functions return 1 (success) or 0 (failure) instead of printing. This lets the caller decide what to do, which is better design.</li>
<li><code>pop(&amp;v)</code> returns the popped value through a pointer, so a value like −1 can still be stored in the stack.</li></ul>"""),

    PE("ds2p3", "Reverse a string using a stack", r'''
#include <stdio.h>
#include <string.h>

char st[50];
int top = -1;

void push(char c) { st[++top] = c; }
char pop(void)    { return st[top--]; }

int main(void)
{
    char s[50];
    int i, n;

    printf("Enter a word: ");
    scanf("%49s", s);
    n = strlen(s);

    for (i = 0; i < n; i++)
        push(s[i]);           // push all
    for (i = 0; i < n; i++)
        s[i] = pop();         // pop all

    printf("Reversed: %s\n", s);
    return 0;
}
''', ["DIPLOMA"],
       r"""<ul><li>All characters are pushed: D, I, P, L, O, M, A (A is on top).</li>
<li>Popping returns them in the <b>opposite order</b>: A, M, O, L, P, I, D. This is the LIFO property.</li>
<li>Reversing is one of the simplest applications of a stack. The same idea is used for undo operations and the browser back button.</li></ul>"""),

    PE("ds2p4", "Check balanced parentheses ( ) [ ] { }", r'''
#include <stdio.h>

char st[50];
int top = -1;

int match(char open, char close)
{
    return (open == '(' && close == ')') ||
           (open == '[' && close == ']') ||
           (open == '{' && close == '}');
}

int balanced(char *e)
{
    int i;
    top = -1;
    for (i = 0; e[i] != '\0'; i++) {
        char c = e[i];
        if (c=='('||c=='['||c=='{')
            st[++top] = c;        // push
        else if (c==')'||c==']'||c=='}') {
            if (top == -1)
                return 0;
            if (!match(st[top--], c))
                return 0;
        }
    }
    return top == -1;                 // empty?
}

int main(void)
{
    char *t[] = {"{a+[b*(c-d)]}",
                 "(a+b]*c",
                 "((a+b)*c",
                 "[(x)]{y}"};
    int i;
    for (i = 0; i < 4; i++)
        printf("%-15s %s\n", t[i],
               balanced(t[i]) ? "Balanced"
                              : "Not OK");
    return 0;
}
''', (),
       r"""<ul><li>Every <b>opening</b> bracket is pushed.</li>
<li>For every <b>closing</b> bracket the top is popped. It must be the matching opening bracket, otherwise the expression is not balanced (<code>(a+b]</code>).</li>
<li>At the end the stack must be <b>empty</b>. In <code>((a+b)*c</code> one '(' is left over, so it is not balanced ("Not OK").</li>
<li>Compilers use this check to report "missing bracket" errors.</li></ul>"""),

    PE("ds2p5", "Convert infix expression to postfix", r'''
#include <stdio.h>
#include <ctype.h>

char st[50];
int top = -1;

int prec(char c)
{
    if (c == '^') return 3;
    if (c=='*'||c=='/'||c=='%') return 2;
    if (c=='+'||c=='-') return 1;
    return 0;                   // '('
}

int main(void)
{
    char in[50], out[50], c;
    int i, k = 0;

    printf("Infix: ");
    scanf("%49s", in);
    for (i = 0; (c = in[i]) != '\0'; i++) {
        if (isalnum((unsigned char)c))
            out[k++] = c;             // operand
        else if (c == '(')
            st[++top] = c;
        else if (c == ')') {
            while (st[top] != '(')
                out[k++] = st[top--];
            top--;                    // drop '('
        } else {                      // operator
            while (top != -1 &&
                (prec(st[top]) > prec(c) ||
                 (prec(st[top]) == prec(c)
                  && c != '^')))
                out[k++] = st[top--];
            st[++top] = c;
        }
    }
    while (top != -1)
        out[k++] = st[top--];
    out[k] = '\0';
    printf("Postfix: %s\n", out);
    return 0;
}
''', ["A+(B*C-(D/E^F)*G)*H"],
       r"""<ul><li><b>Operand</b> (letter or digit): goes straight to the output.</li>
<li><b>(</b>: always pushed. <b>)</b>: pop to the output until '(' is found; the '(' is discarded.</li>
<li><b>Operator</b>: pop operators of <b>higher</b> precedence (or <b>equal</b> precedence, for left-associative operators) to the output, then push the new operator. <code>^</code> is right-associative, so an equal <code>^</code> is not popped.</li>
<li>At the end, all remaining operators are popped.</li>
<li><code>prec('(')</code> returns 0, so '(' is never popped by an operator.</li>
<li>The full step table for this expression is in the Numericals tab.</li></ul>"""),

    PE("ds2p6", "Evaluate a postfix expression", r'''
#include <stdio.h>
#include <ctype.h>

int st[50], top = -1;

int main(void)
{
    char e[50], c;
    int i, a, b, r;

    printf("Postfix (single digits): ");
    scanf("%49s", e);
    for (i = 0; (c = e[i]) != '\0'; i++) {
        if (isdigit((unsigned char)c))
            st[++top] = c - '0';      // push
        else {
            b = st[top--];       // 2nd
            a = st[top--];       // 1st
            switch (c) {
            case '+': r = a + b; break;
            case '-': r = a - b; break;
            case '*': r = a * b; break;
            case '/': r = a / b; break;
            default:  r = 0;
            }
            printf("%d %c %d = %d\n",
                   a, c, b, r);
            st[++top] = r;
        }
    }
    printf("Result = %d\n", st[top]);
    return 0;
}
''', ["53+82-*"],
       r"""<ul><li>Scan from <b>left to right</b>. A digit is pushed (<code>c − '0'</code> converts the character '5' to the number 5).</li>
<li>For an operator, pop <b>two</b> values. The first popped is the <b>second</b> operand (b), the next is the first operand (a). This order matters for − and /.</li>
<li>The result <code>a op b</code> is pushed back.</li>
<li>When the expression ends, the only value left on the stack is the answer: (5 + 3) × (8 − 2) = <b>48</b>.</li>
<li>No precedence rules and no brackets are needed. This is why compilers convert infix to postfix.</li></ul>"""),

    PE("ds2p7", "Factorial using recursion (with trace) [Practical 3]", r'''
#include <stdio.h>

long fact(int n)
{
    long r;
    printf("call fact(%d)\n", n);
    if (n <= 1)
        r = 1;                // base case
    else
        r = n * fact(n - 1);  // recursive
    printf("fact(%d) returns %ld\n", n, r);
    return r;
}

int main(void)
{
    int n;
    printf("Enter n: ");
    scanf("%d", &n);
    printf("%d! = %ld\n", n, fact(n));
    return 0;
}
''', ["4"],
       r"""<ul><li><b>Base case:</b> fact(1) = 1 stops the recursion. Without it the function would call itself forever (stack overflow).</li>
<li><b>Recursive case:</b> fact(n) = n × fact(n − 1). Each call works on a smaller problem.</li>
<li>The trace shows the <b>winding</b> phase (calls 4 → 3 → 2 → 1, each pushed on the system stack) and the <b>unwinding</b> phase (returns 1 → 2 → 6 → 24, each popped).</li>
<li>Time O(n); space O(n) for n stack frames.</li></ul>"""),

    PE("ds2p8", "GCD using recursion (Euclid's method)", r'''
#include <stdio.h>

int gcd(int a, int b)
{
    printf("gcd(%d, %d)\n", a, b);
    if (b == 0)
        return a;             // base case
    return gcd(b, a % b);
}

int main(void)
{
    int a, b, g;
    printf("Enter two numbers: ");
    scanf("%d %d", &a, &b);
    g = gcd(a, b);
    printf("GCD = %d\n", g);
    printf("LCM = %d\n", a / g * b);
    return 0;
}
''', ["48 18"],
       r"""<ul><li>Euclid's rule: <b>gcd(a, b) = gcd(b, a % b)</b>, and <b>gcd(a, 0) = a</b> (base case).</li>
<li>48 % 18 = 12 → gcd(18, 12); 18 % 12 = 6 → gcd(12, 6); 12 % 6 = 0 → gcd(6, 0) = <b>6</b>.</li>
<li>The LCM follows from a × b = GCD × LCM. Writing <code>a / g * b</code> (dividing first) avoids overflow.</li>
<li>Very fast: about O(log(min(a, b))) calls.</li></ul>"""),

    PE("ds2p9", "Fibonacci series using recursion (with call count)", r'''
#include <stdio.h>

int calls = 0;

int fib(int n)
{
    calls++;
    if (n == 0) return 0;     // base cases
    if (n == 1) return 1;
    return fib(n - 1) + fib(n - 2);
}

int main(void)
{
    int n, i;
    printf("How many terms? ");
    scanf("%d", &n);
    printf("Series: ");
    for (i = 0; i < n; i++)
        printf("%d ", fib(i));
    printf("\n");

    calls = 0;
    printf("fib(10) = %d", fib(10));
    printf(" using %d calls\n", calls);
    return 0;
}
''', ["10"],
       r"""<ul><li>Two base cases: fib(0) = 0 and fib(1) = 1. Every other term is the sum of the previous two.</li>
<li>Each call makes <b>two</b> more calls, so the same values are computed again and again (see the recursion tree diagram).</li>
<li>The counter shows that fib(10) needs <b>177 calls</b>. The number of calls grows roughly like 2ⁿ, so the time complexity is <b>O(2ⁿ)</b>.</li>
<li>A simple loop computes the same series in O(n). Recursion is elegant, but not always efficient.</li></ul>"""),

    PE("ds2p10", "Queue using an array: INSERT, DELETE, DISPLAY [Practical 4]", r'''
#include <stdio.h>
#define MAX 5

int q[MAX], front = -1, rear = -1;

void insert(int x)
{
    if (rear == MAX - 1) {
        printf("Queue Overflow\n");
        return;
    }
    if (front == -1)
        front = 0;            // first item
    q[++rear] = x;
    printf("%d inserted\n", x);
}

void delete(void)
{
    if (front == -1 || front > rear) {
        printf("Queue Underflow\n");
        return;
    }
    printf("%d deleted\n", q[front++]);
}

void display(void)
{
    int i;
    if (front == -1 || front > rear) {
        printf("Queue is empty\n");
        return;
    }
    printf("Queue: ");
    for (i = front; i <= rear; i++)
        printf("%d ", q[i]);
    printf(" (F=%d R=%d)\n", front, rear);
}

int main(void)
{
    int ch, x;
    do {
        printf("1.Insert 2.Delete 3.Show");
        printf(" 4.Exit: ");
        scanf("%d", &ch);
        switch (ch) {
        case 1:
            printf("Value: ");
            scanf("%d", &x);
            insert(x);
            break;
        case 2: delete(); break;
        case 3: display(); break;
        }
    } while (ch != 4);
    return 0;
}
''', ["1", "10", "1", "20", "1", "30", "3", "2", "3", "4"],
       r"""<ul><li>Two indexes: <code>front</code> (where deletion happens) and <code>rear</code> (where insertion happens). Both start at −1.</li>
<li><b>Insert:</b> check overflow (<code>rear == MAX − 1</code>); on the very first insert set <code>front = 0</code>; then <code>q[++rear] = x</code>.</li>
<li><b>Delete:</b> check underflow (<code>front == −1</code> or <code>front &gt; rear</code>); then take <code>q[front++]</code>.</li>
<li>10 was inserted first and is deleted first: <b>FIFO</b>.</li>
<li>Insert and delete are both <b>O(1)</b>.</li></ul>"""),

    PE("ds2p11", "Limitation of a simple queue (wasted space)", r'''
#include <stdio.h>
#define MAX 5

int q[MAX], front = 0, rear = -1;

int main(void)
{
    int i, n;
    for (i = 1; i <= 5; i++)
        q[++rear] = i * 10;           // fill
    printf("Inserted 5, rear=%d\n", rear);

    for (i = 0; i < 3; i++)
        printf("Deleted %d\n", q[front++]);
    n = rear - front + 1;
    printf("front=%d rear=%d\n",
           front, rear);
    printf("Items = %d, free = %d\n",
           n, MAX - n);

    if (rear == MAX - 1)
        printf("Insert 60: Queue Full!\n");
    return 0;
}
''', (),
       r"""<ul><li>After 5 inserts and 3 deletes, only <b>2</b> items are in the queue and <b>3</b> places are free.</li>
<li>Yet a new insert is refused, because the test <code>rear == MAX − 1</code> is true. In a simple queue, <code>rear</code> can only move forward.</li>
<li>The free places at the front can never be used again, so memory is wasted.</li>
<li>The <b>circular queue</b> (next program) solves this by wrapping <code>rear</code> back to index 0.</li></ul>"""),

    PE("ds2p12", "Circular queue using an array", r'''
#include <stdio.h>
#define MAX 4

int q[MAX], front = -1, rear = -1;

void insert(int x)
{
    if ((rear + 1) % MAX == front) {
        printf("Insert %d: Full\n", x);
        return;
    }
    if (front == -1)
        front = 0;
    rear = (rear + 1) % MAX;          // wrap
    q[rear] = x;
    printf("Insert %d at [%d]\n", x, rear);
}

void delete(void)
{
    if (front == -1) {
        printf("Queue Empty\n");
        return;
    }
    printf("Delete %d from [%d]\n",
           q[front], front);
    if (front == rear)
        front = rear = -1;            // now empty
    else
        front = (front + 1) % MAX;
}

void display(void)
{
    int i = front;
    if (front == -1) {
        printf("Queue Empty\n");
        return;
    }
    printf("Queue: ");
    while (1) {
        printf("%d ", q[i]);
        if (i == rear)
            break;
        i = (i + 1) % MAX;
    }
    printf("(F=%d R=%d)\n", front, rear);
}

int main(void)
{
    insert(10); insert(20);
    insert(30); insert(40);
    insert(50);                       // full
    delete(); delete();
    insert(50); insert(60);           // wrap
    display();
    return 0;
}
''', (),
       r"""<ul><li>The modulus operator makes the indexes go round: with MAX = 4, after index 3 the next index is (3 + 1) % 4 = <b>0</b>.</li>
<li><b>Full</b> when <code>(rear + 1) % MAX == front</code>. <b>Empty</b> when <code>front == −1</code>.</li>
<li>After deleting 10 and 20, the new items 50 and 60 go into indexes <b>0 and 1</b>, the places freed at the front. No space is wasted.</li>
<li>When the last item is deleted (<code>front == rear</code>), both indexes are reset to −1.</li>
<li>Display walks from front to rear, wrapping round with % MAX.</li></ul>"""),

    PE("ds2p13", "Decimal to binary using a stack", r'''
#include <stdio.h>

int st[32], top = -1;

int main(void)
{
    int n, m;
    printf("Enter a decimal number: ");
    scanf("%d", &n);
    m = n;
    if (m == 0)
        st[++top] = 0;
    while (m > 0) {
        st[++top] = m % 2;            // remainder
        m = m / 2;
    }
    printf("Binary of %d = ", n);
    while (top != -1)
        printf("%d", st[top--]);      // reverse
    printf("\n");
    return 0;
}
''', ["45"],
       r"""<ul><li>Repeated division by 2 gives the binary digits in <b>reverse order</b> (least significant bit first): 45 → 1, 0, 1, 1, 0, 1.</li>
<li>Pushing the remainders and then popping them prints the digits in the correct order: <b>101101</b>.</li>
<li>This is another "reversing" application of the stack.</li></ul>"""),

    PE("ds2p14", "Queue of persons: add, serve and search [Project idea]", r'''
#include <stdio.h>
#include <string.h>
#define MAX 5

char q[MAX][20];
int front = 0, rear = -1;

void add(char *name)
{
    if (rear == MAX - 1) {
        printf("Line is full\n");
        return;
    }
    strcpy(q[++rear], name);
    printf("%s joined the line\n", name);
}

void serve(void)
{
    if (front > rear) {
        printf("No one in line\n");
        return;
    }
    printf("Serving %s\n", q[front++]);
}

void search(char *name)
{
    int i;
    for (i = front; i <= rear; i++)
        if (strcmp(q[i], name) == 0) {
            printf("%s is at place %d\n",
                   name, i - front + 1);
            return;
        }
    printf("%s is not in line\n", name);
}

int main(void)
{
    add("Ravi"); add("Meena"); add("Amit");
    search("Amit");
    serve();
    search("Amit");
    search("Ravi");
    return 0;
}
''', (),
       r"""<ul><li>The queue stores <b>names</b>: a 2-D char array in which each row is one string.</li>
<li>People are served in the order they joined (FIFO), like a ticket window.</li>
<li>The search reports the place in the line as <code>i − front + 1</code>. After Ravi is served, Amit moves from place 3 to place 2.</li>
<li>Ravi is no longer found once he has been served (deleted from the front).</li></ul>"""),
]
