"""Sequential-circuit helpers for Digital Electronics (DI03000011) Unit 5:
gate-level latch simulation, flip-flop next-state functions, timing waveforms, FF symbols and cross-coupled latch drawing."""
from flowchart_lib import text, line, P, INK
from de_gates import gate, wire, dot, lab, bexpr, GS, WIRE, HI

nand = lambda *a: 1 - int(all(a))
nor = lambda *a: 1 - int(any(a))

# ------------------------------------------------------------------ next-state (characteristic) functions; None = invalid
NEXT = {
    "SR": lambda s, r, q: None if (s and r) else (1 if s else (0 if r else q)),
    "JK": lambda j, k, q: (j & (1 - q)) | ((1 - k) & q),
    "D": lambda d, q: d,
    "T": lambda t, q: t ^ q,
}


def settle(f, a, b, q, qb, steps=8):
    """iterate a cross-coupled pair: Q = f(a, Qb), Qb = f(Q, b). Returns (Q, Qb) or None if it does not settle."""
    for _ in range(steps):
        nq, nqb = f(a, qb), f(q, b)
        if (nq, nqb) == (q, qb):
            return q, qb
        q, qb = nq, nqb
    return None


def nor_latch(s, r, q):
    """NOR latch: top gate inputs (R, Qb) -> Q, bottom gate (Q, S) -> Qb"""
    return settle(nor, r, s, q, 1 - q)


def nand_latch(sb, rb, q):
    """NAND latch with active-low inputs: top gate (Sb, Qb) -> Q, bottom gate (Q, Rb) -> Qb"""
    return settle(nand, sb, rb, q, 1 - q)


def clocked_sr(s, r, clk, q):
    """clocked SR flip-flop made of 4 NAND gates (level sensitive while CLK = 1)"""
    return nand_latch(nand(s, clk), nand(r, clk), q)


def clocked_d(d, clk, q):
    return clocked_sr(d, 1 - d, clk, q)


# self-checks of the gate-level models against the characteristic functions
for q in (0, 1):
    for s in (0, 1):
        for r in (0, 1):
            exp = NEXT["SR"](s, r, q)
            got = nor_latch(s, r, q)
            if exp is None:
                assert got == (0, 0)
            else:
                assert got == (exp, 1 - exp)
            g2 = clocked_sr(s, r, 1, q)
            assert (g2 == (1, 1)) if exp is None else g2 == (exp, 1 - exp)
            assert clocked_sr(s, r, 0, q) == (q, 1 - q)
    for d in (0, 1):
        assert clocked_d(d, 1, q) == (d, 1 - d) and clocked_d(d, 0, q) == (q, 1 - q)


def char_rows(kind):
    """characteristic table rows (inputs..., Qn, Qn+1) with 'X' for invalid"""
    out = []
    if kind in ("SR", "JK"):
        for a in (0, 1):
            for b in (0, 1):
                for q in (0, 1):
                    v = NEXT[kind](a, b, q)
                    out.append((a, b, q, "X" if v is None else v))
    else:
        for a in (0, 1):
            for q in (0, 1):
                out.append((a, q, NEXT[kind](a, q)))
    return out


def run(kind, inputs, q0=0):
    """apply inputs at successive clock edges -> list of (inputs, Qn, Qn+1)"""
    q, res = q0, []
    for inp in inputs:
        inp = inp if isinstance(inp, tuple) else (inp,)
        nq = NEXT[kind](*inp, q)
        res.append((inp, q, nq))
        q = nq if nq is not None else q
    return res


# ------------------------------------------------------------------ timing waveforms
def wave_path(x0, y, vals, step, h=18, color=INK, w=1.8):
    """digital waveform; vals = levels per step (0/1); y = baseline of 0 level"""
    d, prev = "", None
    for i, v in enumerate(vals):
        yy = y - h * v
        x = x0 + i * step
        if prev is None:
            d += f"M{x:.1f} {yy:.1f}"
        elif v != prev:
            d += f" L{x:.1f} {y - h * prev:.1f} L{x:.1f} {yy:.1f}"
        prev = v
    d += f" L{x0 + len(vals) * step:.1f} {y - h * prev:.1f}"
    return line(d, color, w)


def timing(x0, y0, rows_, step, h=18, gap=34, edges=None, name_w=34):
    """rows_: [(name, vals, color)]. edges: step indexes to mark with dashed lines."""
    b = ""
    n = max(len(v) for _, v, _ in rows_)
    yb = y0 + len(rows_) * gap
    if edges:
        for e in edges:
            x = x0 + e * step
            b += line(f"M{x:.1f} {y0 - h - 6} L{x:.1f} {yb - gap + 6}", "#B39DDB", 1, "3 3")
    for k, (nm, vals, col) in enumerate(rows_):
        y = y0 + k * gap
        if "!" in nm:
            b += bexpr(x0 - 8, y - 5, nm, 10.5, anchor="end")
        else:
            b += lab(x0 - 8, y - 5, nm, "end", 10.5)
        b += line(f"M{x0} {y + 0.5} L{x0 + n * step} {y + 0.5}", "#EEE", 1)
        b += wave_path(x0, y, vals, step, h, col)
    return b, yb


def clock(n_cycles, low_first=True):
    out = []
    for _ in range(n_cycles):
        out += [0, 1] if low_first else [1, 0]
    return out


def rising(clk):
    return [i for i in range(1, len(clk)) if clk[i - 1] == 0 and clk[i] == 1]


def sample(kind, clk, inputs, q0=0):
    """edge-triggered (rising) simulation. inputs: list of per-step input tuples. Returns Q per step."""
    q, out = q0, []
    edges = set(rising(clk))
    for i in range(len(clk)):
        if i in edges:
            inp = inputs[i] if isinstance(inputs[i], tuple) else (inputs[i],)
            nq = NEXT[kind](*inp, q)
            q = q if nq is None else nq
        out.append(q)
    return out


# ------------------------------------------------------------------ flip-flop symbol
def ff_symbol(x, y, w, h, ins, title="", edge="pos", lead=22, size=11, clk_index=None, fill="#F1E8FC", ext=True):
    """FF symbol: ins = list of input names (one may be 'CLK'); outputs Q and !Q"""
    b = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="5" fill="{fill}" stroke="{P}" stroke-width="1.8"/>'
    if title:
        b += text(x + w / 2, y + h / 2 + 4, title, 10, weight="bold", color=GS)
    pts = {}
    for i, nm in enumerate(ins):
        yy = y + h * (i + 1) / (len(ins) + 1)
        if nm == "CLK":
            b += f'<path d="M{x} {yy - 6} L{x + 9} {yy} L{x} {yy + 6}" fill="none" stroke="{P}" stroke-width="1.5"/>'
            if edge == "neg":
                b += f'<circle cx="{x - 4.5}" cy="{yy}" r="4" fill="#fff" stroke="{P}" stroke-width="1.5"/>'
                b += wire([(x - lead, yy), (x - 9, yy)])
            else:
                b += wire([(x - lead, yy), (x, yy)])
            b += lab(x - lead - 4, yy + 4, "CLK", "end", size - 1) if ext else lab(x - lead + 2, yy - 5, "CLK", "start", size - 2)
        else:
            b += wire([(x - lead, yy), (x, yy)]) + text(x + 9, yy + 4, nm, size - 1, weight="bold", color=GS)
            if ext:
                b += lab(x - lead - 4, yy + 4, nm, "end", size)
        pts[nm] = (x - lead, yy)
    for i, nm in enumerate(["Q", "!Q"]):
        yy = y + h * (i + 1) / 3
        b += wire([(x + w, yy), (x + w + lead, yy)])
        b += bexpr(x + w - 9, yy + 4, nm, size - 1, anchor="end", color=GS) + bexpr(x + w + lead + 4, yy + 4, nm, size, anchor="start")
        pts[nm] = (x + w + lead, yy)
    return b, pts


# ------------------------------------------------------------------ cross-coupled latch
def cross_latch(kind, x, y1, gap=72, top_in=None, bot_in=None, out_len=40, labels=("Q", "!Q"), n_ext=1):
    """two gates (NOR or NAND) at y1 and y1+gap with cross-coupled feedback.
    top gate: inputs [external..., feedback from bottom output]; bottom gate: [feedback from top output, external...].
    Returns (svg, info) where info has 'top_ins', 'bot_ins' (external input points) and output ends."""
    y2 = y1 + gap
    n = n_ext + 1
    g1, (o1x, o1y), i1 = gate(kind, x, y1, n=n)
    g2, (o2x, o2y), i2 = gate(kind, x, y2, n=n)
    b = g1 + g2
    fa = y1 + gap * 0.40
    fb = y1 + gap * 0.60
    # top output -> bottom gate first input
    b += dot(o1x + 12, o1y) + wire([(o1x + 12, o1y), (o1x + 12, fa), (x - 10, fa), (x - 10, i2[0][1]), i2[0]])
    # bottom output -> top gate last input
    b += dot(o2x + 20, o2y) + wire([(o2x + 20, o2y), (o2x + 20, fb), (x - 20, fb), (x - 20, i1[-1][1]), i1[-1]])
    b += wire([(o1x, o1y), (o1x + out_len, o1y)]) + wire([(o2x, o2y), (o2x + out_len, o2y)])
    b += bexpr(o1x + out_len + 4, o1y + 4, labels[0], 11, anchor="start") + bexpr(o2x + out_len + 4, o2y + 4, labels[1], 11, anchor="start")
    return b, {"top_ins": i1[:-1], "bot_ins": i2[1:], "q": (o1x + out_len, o1y), "qb": (o2x + out_len, o2y), "x_out": o1x}


# ------------------------------------------------------------------ table with per-column widths, overline cells and a text 'State' column
def ftable(x, y, head, rows_, cws, rh=19, out_cols=1, state=True, size=10.5):
    from flowchart_lib import P as PP
    b = ""
    nc = len(head)
    xs = [x + sum(cws[:i]) for i in range(nc)]
    out_idx = set(range(nc - out_cols - (1 if state else 0), nc - (1 if state else 0)))
    for i, h in enumerate(head):
        fill = HI if i in out_idx else ("#5E35B1" if state and i == nc - 1 else PP)
        b += f'<rect x="{xs[i]}" y="{y}" width="{cws[i]}" height="{rh}" fill="{fill}" stroke="{PP}" stroke-width="1"/>'
        b += _cell(xs[i] + cws[i] / 2, y + rh / 2, h, size, "#fff", True)
    for r, row in enumerate(rows_):
        yy = y + (r + 1) * rh
        for i, v in enumerate(row):
            is_state = state and i == nc - 1
            fill = ("#E3F5E6" if i in out_idx else ("#fff" if is_state else ("#FAF6FF" if r % 2 else "#fff")))
            b += f'<rect x="{xs[i]}" y="{yy}" width="{cws[i]}" height="{rh}" fill="{fill}" stroke="#C9B3EC" stroke-width="1"/>'
            b += _cell(xs[i] + cws[i] / 2, yy + rh / 2, str(v), size - (1 if is_state else 0), INK, i in out_idx, mono=not is_state)
    return b, y + (len(rows_) + 1) * rh


def _cell(cx, cy, s, size, color, bold, mono=True):
    if "!" in s:
        return bexpr(cx, cy + size * 0.36, s, size, color=color, weight="bold" if bold else "normal")
    return text(cx, cy, s, size, color=color, weight="bold" if bold else "normal", mono=mono)
