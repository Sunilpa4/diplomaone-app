"""Shared K-map solution writer for DE Unit 3 (EN + GU). Everything is computed by de_kmap and checked."""
import de_kmap as K
import de_gates as G

B = G.bh
VN = "ABCD"


def why(c, n, pos=False, names=VN):
    """explain which variables stay constant in a group"""
    en, gu = [], []
    for i in range(n):
        v = names[i]
        if c[i] == "-":
            en.append(f"{v} changes → eliminated")
            gu.append(f"{v} બદલાય છે → દૂર")
        else:
            lit = (("!" + v) if c[i] == "1" else v) if pos else (v if c[i] == "1" else "!" + v)
            en.append(f"{v} stays {c[i]} → {B(lit)}")
            gu.append(f"{v} = {c[i]} સ્થિર → {B(lit)}")
    return "; ".join(en), "; ".join(gu)


def solve(n, ones, dc=(), pos=False, names=VN, out="Y"):
    """returns (en_html, gu_html, cubes, answer_str)"""
    ones, dc = sorted(ones), sorted(dc)
    target = [m for m in range(2 ** n) if m not in ones and m not in dc] if pos else ones
    g = K.minimise(n, target, dc)
    K.check(n, target, dc, g)
    alts = K.all_minimal(n, target, dc)
    ans = K.pos_str(g, names) if pos else K.sop_str(g, names)
    fx = out + " = Σm(" + ", ".join(map(str, ones)) + ")" + (" + d(" + ", ".join(map(str, dc)) + ")" if dc else "")
    mp = K.html_map(n, ones, dc, names)
    rows_en = rows_gu = ""
    for i, c in enumerate(g):
        sz_en, sz_gu = K.size_name(c)
        cells = ", ".join(f"m{m}" for m in K.cube_mins(c))
        term = K.cube_sum(c, names) if pos else K.cube_term(c, names)
        we, wg = why(c, n, pos, names)
        rows_en += f"<tr><td>{i + 1}. {sz_en}</td><td>{cells}</td><td>{we}</td><td><b>{B(term)}</b></td></tr>"
        rows_gu += f"<tr><td>{i + 1}. {sz_gu}</td><td>{cells}</td><td>{wg}</td><td><b>{B(term)}</b></td></tr>"
    what_en = "0s (for POS)" if pos else "1s"
    what_gu = "0s (POS માટે)" if pos else "1s"
    en = (f"<p>{fx}</p><p><b>Step 1:</b> Plot the map ({2 ** n} cells; 1 for minterms" + (", X for don't-cares" if dc else "") + "):</p>" + mp
          + f"<p><b>Step 2:</b> Group the {what_en} (largest groups first" + (", using X only where it helps" if dc else "") + "):</p>"
          + "<table><tr><th>Group</th><th>Cells</th><th>Reason</th><th>Term</th></tr>" + rows_en + "</table>"
          + f"<p><b>Step 3:</b> {'AND' if pos else 'OR'} the terms:</p><p><b>{out} = {B(ans)}</b></p>")
    gu = (f"<p>{fx}</p><p><b>Step 1:</b> Map દોરો ({2 ** n} cells; minterms માટે 1" + (", don't-cares માટે X" if dc else "") + "):</p>" + mp
          + f"<p><b>Step 2:</b> {what_gu} ના groups બનાવો (પહેલાં મોટા groups" + (", X નો ઉપયોગ જ્યાં ફાયદો હોય ત્યાં જ" if dc else "") + "):</p>"
          + "<table><tr><th>Group</th><th>Cells</th><th>કારણ</th><th>Term</th></tr>" + rows_gu + "</table>"
          + f"<p><b>Step 3:</b> Terms નો {'AND' if pos else 'OR'} કરો:</p><p><b>{out} = {B(ans)}</b></p>")
    if len(alts) > 1:
        other = [s for s in alts if sorted(s) != sorted(g)]
        o = " or ".join(B(K.pos_str(s, names) if pos else K.sop_str(s, names)) for s in other)
        o_gu = " અથવા ".join(B(K.pos_str(s, names) if pos else K.sop_str(s, names)) for s in other)
        en += f"<p><i>Note: this map has more than one minimal answer. {out} = {o} is equally correct (same number of terms and literals).</i></p>"
        gu += f"<p><i>નોંધ: આ map ના એકથી વધુ minimal જવાબ છે. {out} = {o_gu} પણ એટલો જ સાચો છે (સરખા terms અને literals).</i></p>"
    return en, gu, g, ans
