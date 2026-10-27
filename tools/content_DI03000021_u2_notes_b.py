"""DI03000021 Unit 2 notes part B: 2.4 queue, 2.5 circular queue and applications."""
from c_content import make_TE

SN = {
    "alg_qins": r'''
Algorithm QINSERT(Q, FRONT, REAR, MAX, ITEM)
Step 1: [Check overflow]
        If REAR = MAX - 1 then
            Write "Queue Overflow" and Exit
Step 2: If FRONT = -1 then
            Set FRONT = 0
Step 3: Set REAR = REAR + 1
Step 4: Set Q[REAR] = ITEM
Step 5: Exit
''',
    "alg_qdel": r'''
Algorithm QDELETE(Q, FRONT, REAR)
Step 1: [Check underflow]
        If FRONT = -1 or FRONT > REAR then
            Write "Queue Underflow" and Exit
Step 2: Set ITEM = Q[FRONT]
Step 3: Set FRONT = FRONT + 1
Step 4: Return ITEM
''',
    "alg_cqins": r'''
Algorithm CQINSERT(Q, FRONT, REAR, MAX, ITEM)
Step 1: [Check overflow]
        If (REAR + 1) mod MAX = FRONT then
            Write "Queue Full" and Exit
Step 2: If FRONT = -1 then
            Set FRONT = 0
Step 3: Set REAR = (REAR + 1) mod MAX
Step 4: Set Q[REAR] = ITEM
Step 5: Exit
''',
    "alg_cqdel": r'''
Algorithm CQDELETE(Q, FRONT, REAR, MAX)
Step 1: [Check underflow]
        If FRONT = -1 then
            Write "Queue Empty" and Exit
Step 2: Set ITEM = Q[FRONT]
Step 3: If FRONT = REAR then
            Set FRONT = REAR = -1
        Else
            Set FRONT = (FRONT + 1) mod MAX
Step 4: Return ITEM
''',
}
T0 = make_TE(SN)


def T(h, b, examples=None, **kw):
    d = T0(h, b, **kw)
    if examples:
        d["examples"] = examples
    return d


SEC_2_4 = {
    "title": {"en": "2.4 Queue"},
    "items": [
        T("2.4.1 Introduction to Queue",
          r"""<p>A <b>queue</b> is a <b>linear data structure</b> in which insertion is done at one end, called the <b>REAR</b>, and deletion is done at the other end, called the <b>FRONT</b>.</p>
<p>The element inserted <b>first</b> is removed <b>first</b>, so a queue follows the <b>FIFO (First In, First Out)</b> principle.</p>
<h4>Real-life examples</h4>
<ul><li>People standing in a line at a ticket counter or ATM.</li>
<li>Vehicles at a toll plaza.</li>
<li>Print jobs waiting for a printer.</li></ul>
<h4>Terms</h4>
<ul><li><b>FRONT:</b> index of the first element (the next to be deleted).</li>
<li><b>REAR:</b> index of the last element (where the next insert goes).</li>
<li><b>Enqueue / Insert:</b> adding an element at the rear.</li>
<li><b>Dequeue / Delete:</b> removing an element from the front.</li>
<li><b>Overflow:</b> inserting into a full queue (REAR = MAX − 1).</li>
<li><b>Underflow:</b> deleting from an empty queue (FRONT = −1 or FRONT &gt; REAR).</li></ul>
<h4>Stack vs queue</h4>
<table>
<tr><th>Stack</th><th>Queue</th></tr>
<tr><td>LIFO</td><td>FIFO</td></tr>
<tr><td>Insert and delete at one end (TOP)</td><td>Insert at REAR, delete at FRONT</td></tr>
<tr><td>One pointer: TOP</td><td>Two pointers: FRONT and REAR</td></tr>
<tr><td>Operations: PUSH, POP</td><td>Operations: INSERT (enqueue), DELETE (dequeue)</td></tr>
<tr><td>Empty: TOP = −1</td><td>Empty: FRONT = −1</td></tr>
<tr><td>Pile of plates</td><td>Line at a ticket counter</td></tr>
<tr><td>Recursion, expression evaluation</td><td>CPU scheduling, printer spooling</td></tr>
</table>""",
          diagram="ds2_queue_array", key=True),

        T("2.4.2 Array Representation of Queue: Insert and Delete",
          r"""<p>A queue is represented with an array <code>Q[MAX]</code> and two integer variables <code>FRONT</code> and <code>REAR</code>. Initially <b>FRONT = REAR = −1</b>.</p>
<h4>Insert algorithm</h4>
@@alg_qins@@
<h4>Delete algorithm</h4>
@@alg_qdel@@
<ul><li>On the first insertion, FRONT is set to 0.</li>
<li>Insert moves only <b>REAR</b> forward; delete moves only <b>FRONT</b> forward.</li>
<li>Number of elements in the queue = REAR − FRONT + 1.</li>
<li>Both operations take <b>O(1)</b> time.</li></ul>""",
          programs=["ds2p10"], examples=["ds2n11"], key=True),

        T("2.4.3 Limitation of a Simple Queue",
          r"""<p>In a simple (linear) queue, <b>REAR and FRONT only move forward</b>. When REAR reaches MAX − 1, the queue reports <b>"full"</b>, even if elements have been deleted from the front and those places are now free.</p>
<p><b>Example</b> (MAX = 5): insert 10, 20, 30, 40, 50 → REAR = 4. Delete three times → FRONT = 3. Only 2 elements remain, but inserting 60 gives "Queue Overflow", because REAR = MAX − 1.</p>
<ul><li>The free locations at the beginning of the array <b>cannot be reused</b>, so memory is wasted.</li>
<li>One fix is to shift all elements to the front after every deletion, but that costs O(n) time.</li>
<li>The better solution is the <b>circular queue</b>, in which REAR wraps round to index 0.</li></ul>""",
          diagram="ds2_queue_limit", programs=["ds2p11"], key=True),
    ],
}

SEC_2_5 = {
    "title": {"en": "2.5 Circular Queue and Applications of Queue"},
    "items": [
        T("2.5.1 Concept of Circular Queue",
          r"""<p>A <b>circular queue</b> is a queue in which the <b>last position is connected back to the first</b>, forming a circle. After the last index (MAX − 1), the next index is 0. It is also called a <b>ring buffer</b>.</p>
<p>The wrap-around is done with the <b>modulus</b> operator:</p>
<p style="text-align:center"><b>REAR = (REAR + 1) % MAX</b> &nbsp;&nbsp; <b>FRONT = (FRONT + 1) % MAX</b></p>
<h4>Conditions</h4>
<ul><li><b>Empty:</b> FRONT = −1</li>
<li><b>Full:</b> (REAR + 1) % MAX = FRONT</li>
<li><b>Only one element:</b> FRONT = REAR</li></ul>
<h4>Insert algorithm</h4>
@@alg_cqins@@
<h4>Delete algorithm</h4>
@@alg_cqdel@@
<p>When the only remaining element is deleted (FRONT = REAR), both are reset to −1 so that the queue becomes empty.</p>""",
          diagram="ds2_circular", programs=["ds2p12"], examples=["ds2n12"], key=True),

        T("2.5.2 Difference between Simple Queue and Circular Queue",
          r"""<table>
<tr><th>Simple (linear) queue</th><th>Circular queue</th></tr>
<tr><td>Elements arranged in a straight line</td><td>Last position connected back to the first (circle)</td></tr>
<tr><td>REAR = REAR + 1</td><td>REAR = (REAR + 1) % MAX</td></tr>
<tr><td>Full when REAR = MAX − 1</td><td>Full when (REAR + 1) % MAX = FRONT</td></tr>
<tr><td>Space freed by deletion cannot be reused</td><td>Freed space is reused</td></tr>
<tr><td>Memory wastage</td><td>Efficient use of memory</td></tr>
<tr><td>Simple to implement</td><td>Slightly more complex (modulus)</td></tr>
<tr><td>May show "full" when it is not</td><td>Shows "full" only when all places are used</td></tr>
<tr><td>Example: simple waiting line</td><td>Example: CPU round-robin scheduling, traffic lights, keyboard buffer</td></tr>
</table>""",
          key=True),

        T("2.5.3 Applications of Queue",
          r"""<ol><li><b>CPU scheduling:</b> processes waiting for the CPU are kept in a ready queue (FCFS, round robin).</li>
<li><b>Printer spooling:</b> print jobs are printed in the order they were sent.</li>
<li><b>Keyboard buffer:</b> key presses are stored and processed in order.</li>
<li><b>Disk and I/O scheduling:</b> requests for a device wait in a queue.</li>
<li><b>Call centre systems:</b> calls are answered in the order they arrive.</li>
<li><b>Data transfer between processes</b> (pipes, buffers in networking, routers).</li>
<li><b>Breadth-first search (BFS)</b> of a graph and level-order traversal of a tree.</li>
<li><b>Simulation</b> of real lines: bank counters, ticket windows, traffic signals.</li></ol>
<h4>Types of queue (for reference)</h4>
<ul><li><b>Simple queue</b>, <b>circular queue</b> (this unit).</li>
<li><b>Priority queue:</b> elements are served by priority, not by arrival.</li>
<li><b>Double-ended queue (deque):</b> insertion and deletion at both ends.</li></ul>""",
          programs=["ds2p14"]),
    ],
}

NOTES_B = [SEC_2_4, SEC_2_5]
