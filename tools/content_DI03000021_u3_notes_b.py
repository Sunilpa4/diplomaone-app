"""DI03000021 Unit 3 notes part B: 3.3 basic operations on singly linked list."""
from c_content import make_TE

SN = {
    "alg_trav": r'''
Algorithm TRAVERSE(START)
Step 1: Set PTR = START
Step 2: Repeat Steps 3 and 4
        while PTR != NULL
Step 3:   Process INFO(PTR)
Step 4:   Set PTR = LINK(PTR)
Step 5: Exit
''',
    "alg_insbeg": r'''
Algorithm INSBEG(START, ITEM)
Step 1: [Create a new node]
        NEW = getnode()
        If NEW = NULL then
            Write "Overflow" and Exit
Step 2: Set INFO(NEW) = ITEM
Step 3: Set LINK(NEW) = START
Step 4: Set START = NEW
Step 5: Exit
''',
    "c_insbeg": r'''
void ins_beg(int x)
{
    struct node *nw = getnode(x);
    nw->next = start;
    start = nw;
}
''',
    "alg_insend": r'''
Algorithm INSEND(START, ITEM)
Step 1: NEW = getnode()
        If NEW = NULL then
            Write "Overflow" and Exit
Step 2: Set INFO(NEW) = ITEM
        Set LINK(NEW) = NULL
Step 3: If START = NULL then
            Set START = NEW and Exit
Step 4: Set PTR = START
Step 5: Repeat while LINK(PTR) != NULL
            Set PTR = LINK(PTR)
Step 6: Set LINK(PTR) = NEW
Step 7: Exit
''',
    "c_insend": r'''
void ins_end(int x)
{
    struct node *nw = getnode(x), *p;
    if (start == NULL) {
        start = nw;
        return;
    }
    p = start;
    while (p->next != NULL)
        p = p->next;
    p->next = nw;
}
''',
    "alg_insafter": r'''
Algorithm INSAFTER(START, KEY, ITEM)
Step 1: Set PTR = START
Step 2: Repeat while PTR != NULL and
        INFO(PTR) != KEY
            Set PTR = LINK(PTR)
Step 3: If PTR = NULL then
            Write "Key not found" and Exit
Step 4: NEW = getnode()
        Set INFO(NEW) = ITEM
Step 5: Set LINK(NEW) = LINK(PTR)
Step 6: Set LINK(PTR) = NEW
Step 7: Exit
''',
    "alg_insbefore": r'''
Algorithm INSBEFORE(START, KEY, ITEM)
Step 1: Set PTR = START, PREV = NULL
Step 2: Repeat while PTR != NULL and
        INFO(PTR) != KEY
            Set PREV = PTR
            Set PTR = LINK(PTR)
Step 3: If PTR = NULL then
            Write "Key not found" and Exit
Step 4: NEW = getnode()
        Set INFO(NEW) = ITEM
        Set LINK(NEW) = PTR
Step 5: If PREV = NULL then
            Set START = NEW
        Else
            Set LINK(PREV) = NEW
Step 6: Exit
''',
    "alg_insord": r'''
Algorithm INSORD(START, ITEM)
Step 1: NEW = getnode()
        Set INFO(NEW) = ITEM
Step 2: If START = NULL or
        ITEM < INFO(START) then
            Set LINK(NEW) = START
            Set START = NEW and Exit
Step 3: Set PTR = START
Step 4: Repeat while LINK(PTR) != NULL
        and INFO(LINK(PTR)) < ITEM
            Set PTR = LINK(PTR)
Step 5: Set LINK(NEW) = LINK(PTR)
Step 6: Set LINK(PTR) = NEW
Step 7: Exit
''',
    "alg_delfirst": r'''
Algorithm DELFIRST(START)
Step 1: If START = NULL then
            Write "Underflow" and Exit
Step 2: Set PTR = START
Step 3: Set START = LINK(START)
Step 4: Free(PTR)
Step 5: Exit
''',
    "alg_dellast": r'''
Algorithm DELLAST(START)
Step 1: If START = NULL then
            Write "Underflow" and Exit
Step 2: If LINK(START) = NULL then
            Free(START), Set START = NULL
            and Exit
Step 3: Set PREV = START
        Set PTR = LINK(START)
Step 4: Repeat while LINK(PTR) != NULL
            Set PREV = PTR
            Set PTR = LINK(PTR)
Step 5: Set LINK(PREV) = NULL
Step 6: Free(PTR)
Step 7: Exit
''',
    "alg_search": r'''
Algorithm SEARCH(START, ITEM)
Step 1: Set PTR = START, POS = 1
Step 2: Repeat while PTR != NULL
          If INFO(PTR) = ITEM then
              Write "Found at", POS
              and Exit
          Set PTR = LINK(PTR)
          Set POS = POS + 1
Step 3: Write "Not found"
Step 4: Exit
''',
    "alg_count": r'''
Algorithm COUNT(START)
Step 1: Set COUNT = 0, PTR = START
Step 2: Repeat while PTR != NULL
          Set COUNT = COUNT + 1
          Set PTR = LINK(PTR)
Step 3: Return COUNT
''',
}
T0 = make_TE(SN)


def T(h, b, examples=None, **kw):
    d = T0(h, b, **kw)
    if examples:
        d["examples"] = examples
    return d


SEC_3_3 = {
    "title": {"en": "3.3 Basic Operations on Singly Linked List"},
    "items": [
        T("3.3.1 Operations and Notation; Traversal",
          r"""<p>The basic operations on a singly linked list are:</p>
<ul><li><b>Traversal:</b> visiting every node once.</li>
<li><b>Insertion:</b> at the beginning, at the end, after or before a given node, in a sorted list.</li>
<li><b>Deletion:</b> of the first node, the last node (or a given node).</li>
<li><b>Searching</b> a node and <b>counting</b> the nodes.</li></ul>
<h4>Notation used in the algorithms</h4>
<table>
<tr><th>Algorithm</th><th>C code</th><th>Meaning</th></tr>
<tr><td>INFO(PTR)</td><td><code>ptr-&gt;data</code></td><td>data of node PTR</td></tr>
<tr><td>LINK(PTR)</td><td><code>ptr-&gt;next</code></td><td>address of the next node</td></tr>
<tr><td>getnode()</td><td><code>malloc(…)</code></td><td>create a new node</td></tr>
<tr><td>Free(PTR)</td><td><code>free(ptr)</code></td><td>release the node</td></tr>
</table>
<h4>Traversal algorithm</h4>
@@alg_trav@@
<p>A temporary pointer PTR is used so that START is not lost. Traversal takes <b>O(n)</b> time.</p>""",
          programs=["ds3p7"]),

        T("3.3.2 Insertion of a Node at the Beginning",
          r"""<p>The new node becomes the first node, and START points to it.</p>
@@alg_insbeg@@
<h4>C function</h4>
@@c_insbeg@@
<ul><li><b>Order is important:</b> first link the new node to the old first node (<code>nw-&gt;next = start</code>), and only then move START. If START is moved first, the rest of the list is lost.</li>
<li>The algorithm also works for an empty list: the new node's next becomes NULL.</li>
<li>Time complexity: <b>O(1)</b>, because no traversal is needed.</li></ul>""",
          diagram="ds3_insert_begin", programs=["ds3p8"], key=True),

        T("3.3.3 Insertion of a Node at the End",
          r"""<p>The new node is attached after the current last node, and its link is NULL.</p>
@@alg_insend@@
<h4>C function</h4>
@@c_insend@@
<ul><li>The last node is the one whose LINK is NULL. The loop condition is <code>p-&gt;next != NULL</code>, not <code>p != NULL</code>, so that p stops <b>on</b> the last node.</li>
<li>If the list is empty, the new node becomes START.</li>
<li>Time complexity: <b>O(n)</b> because of the traversal. Keeping an extra LAST pointer makes it O(1).</li></ul>""",
          diagram="ds3_insert_end", programs=["ds3p8"], key=True),

        T("3.3.4 Insertion of a Node After / Before a Given Node",
          r"""<h4>(a) Insert after a given node (KEY)</h4>
<p>Search for the node containing KEY, then place the new node between it and its next node.</p>
@@alg_insafter@@
<p><b>Important:</b> Step 5 must be done before Step 6. If <code>LINK(PTR) = NEW</code> is done first, the address of the rest of the list is lost.</p>
<h4>(b) Insert before a given node (KEY)</h4>
<p>In a singly linked list we cannot move backwards, so a second pointer <b>PREV</b> follows one node behind PTR.</p>
@@alg_insbefore@@
<ul><li>If KEY is in the first node, PREV stays NULL and the new node becomes the new START (same as insert at beginning).</li>
<li>Both operations take <b>O(n)</b> time in the worst case (searching for KEY).</li></ul>""",
          diagram="ds3_insert_after", programs=["ds3p9"], examples=["ds3n9"], key=True),

        T("3.3.5 Insertion of a Node in a Sorted Linked List",
          r"""<p>In a sorted (ascending) list, the new node must be inserted at its correct position so that the list <b>stays sorted</b>.</p>
@@alg_insord@@
<h4>Working</h4>
<ul><li><b>Case 1:</b> the list is empty or ITEM is smaller than the first node → insert at the beginning.</li>
<li><b>Case 2:</b> otherwise, move PTR while the <b>next</b> node's data is smaller than ITEM. PTR stops at the node after which ITEM must go (this also covers insertion at the end).</li>
<li>Example: inserting 25 into 10 → 20 → 30 → 40: PTR stops at 20 (because 30 &gt; 25), so the list becomes 10 → 20 → 25 → 30 → 40.</li>
<li>Inserting every element this way builds a sorted list (the idea of insertion sort).</li></ul>""",
          diagram="ds3_insert_sorted", programs=["ds3p10"], examples=["ds3n6"], key=True),

        T("3.3.6 Deleting the First and the Last Node",
          r"""<h4>(a) Delete the first node</h4>
@@alg_delfirst@@
<ul><li>Save START in PTR, move START to the second node, then free the old first node. <b>O(1)</b>.</li>
<li>Deleting from an empty list is <b>underflow</b>.</li></ul>
<h4>(b) Delete the last node</h4>
@@alg_dellast@@
<ul><li>Two pointers are needed: PTR reaches the last node and PREV the second-last. PREV becomes the new last node (its link is set to NULL).</li>
<li>Special case: if the list has only one node, START becomes NULL.</li>
<li>Time complexity: <b>O(n)</b>.</li>
<li>Always <code>free()</code> the deleted node; otherwise memory leaks.</li></ul>""",
          diagram="ds3_delete", programs=["ds3p11"], key=True),

        T("3.3.7 Searching a Node and Counting the Nodes",
          r"""<h4>(a) Searching</h4>
<p>Starting from START, each node's data is compared with ITEM until it is found or NULL is reached (<b>linear search</b>).</p>
@@alg_search@@
<ul><li>Best case O(1) (first node); worst case <b>O(n)</b> (last node or not present).</li>
<li>Binary search is not practical because there is no direct access to the middle node.</li></ul>
<h4>(b) Counting the nodes</h4>
@@alg_count@@
<ul><li>Every node visited adds 1 to COUNT. An empty list gives 0.</li>
<li>Time complexity: <b>O(n)</b>.</li></ul>""",
          diagram="ds3_traverse", programs=["ds3p12"], examples=["ds3n8"], key=True),

        T("3.3.8 Summary: Complete Program and Time Complexity",
          r"""<p>The practical combines all operations in one menu-driven program (see the program below).</p>
<table>
<tr><th>Operation</th><th>Time</th><th>Pointer changes</th></tr>
<tr><td>Insert at beginning</td><td>O(1)</td><td>new→next = start; start = new</td></tr>
<tr><td>Insert at end</td><td>O(n)</td><td>last→next = new</td></tr>
<tr><td>Insert after node</td><td>O(n)</td><td>new→next = p→next; p→next = new</td></tr>
<tr><td>Insert in sorted list</td><td>O(n)</td><td>find position, then insert after</td></tr>
<tr><td>Delete first</td><td>O(1)</td><td>start = start→next</td></tr>
<tr><td>Delete last</td><td>O(n)</td><td>prev→next = NULL</td></tr>
<tr><td>Search / Count</td><td>O(n)</td><td>none (traversal only)</td></tr>
</table>
<h4>Common mistakes</h4>
<ul><li>Losing the list by moving START without saving it.</li>
<li>Not checking for an empty list (START = NULL) before deleting.</li>
<li>Not handling the one-node list when deleting the last node.</li>
<li>Forgetting to set the new last node's next to NULL.</li>
<li>Not freeing the deleted node.</li></ul>""",
          programs=["ds3p13"], examples=["ds3n5"]),
    ],
}

NOTES_B = [SEC_3_3]
