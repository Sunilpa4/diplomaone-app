"""Render LaTeX stored in data-tex into real math markup, offline.

The app stores every displayed equation twice: readable Unicode inside the
<div class="math"> and the exact LaTeX source in data-tex. That Unicode was
linear ("a/b", "x^2"), which is not how maths is written on a board.

This module converts the LaTeX into stacked HTML:

        P                 b
    T = ─ ,       x = ─────
       P_fp           2a

so a fraction is a numerator, a rule and a denominator, and a symbol is the
symbol (α, ρ, μ, η) rather than its name.

Supported: fractions \\frac and \\dfrac (nested), sub/superscripts, \\sqrt,
\\int/\\oint with limits, \\sum, \\lim, \\ln/\\log/\\exp/\\sin, Greek, relations,
binary operators, \\left \ight, \\text, \\mathrm, \\quad spacing, accents.
Anything not understood is passed through as text rather than dropped.

Used by tools/subject_page.py and tools/preview_builder.py. Pure Python.
"""
import re

GREEK = {
    "alpha": "α", "beta": "β", "gamma": "γ", "delta": "δ", "epsilon": "ε",
    "varepsilon": "ε", "zeta": "ζ", "eta": "η", "theta": "θ", "vartheta": "ϑ",
    "iota": "ι", "kappa": "κ", "lambda": "λ", "mu": "μ", "nu": "ν", "xi": "ξ",
    "pi": "π", "rho": "ρ", "sigma": "σ", "tau": "τ", "upsilon": "υ", "phi": "φ",
    "varphi": "φ", "chi": "χ", "psi": "ψ", "omega": "ω",
    "Gamma": "Γ", "Delta": "Δ", "Theta": "Θ", "Lambda": "Λ", "Xi": "Ξ",
    "Pi": "Π", "Sigma": "Σ", "Phi": "Φ", "Psi": "Ψ", "Omega": "Ω",
}
SYMBOLS = {
    "propto": "∝", "approx": "≈", "neq": "≠", "ne": "≠", "leq": "≤", "le": "≤",
    "geq": "≥", "ge": "≥", "times": "×", "cdot": "·", "pm": "±", "mp": "∓",
    "infty": "∞", "partial": "∂", "nabla": "∇", "to": "→", "rightarrow": "→",
    "leftarrow": "←", "Rightarrow": "⇒", "Leftarrow": "⇐", "leftrightarrow": "↔",
    "Leftrightarrow": "⇔", "iff": "⇔", "equiv": "≡", "sim": "∼", "simeq": "≃",
    "cong": "≅", "ll": "≪", "gg": "≫", "degree": "°", "circ": "°",
    "sum": "∑", "prod": "∏", "int": "∫", "oint": "∮", "angle": "∠",
    "perp": "⊥", "parallel": "∥", "therefore": "∴", "because": "∵",
    "cup": "∪", "cap": "∩", "subset": "⊂", "in": "∈", "notin": "∉",
    "forall": "∀", "exists": "∃", "emptyset": "∅", "prime": "′",
}
FUNCS = {"ln", "log", "exp", "sin", "cos", "tan", "cot", "sec", "csc",
         "lim", "max", "min", "arcsin", "arccos", "arctan", "sinh", "cosh", "tanh"}
SPACES = {"quad": "  ", "qquad": "    ", ",": " ", ";": " ", ":": " ",
          "!": "", " ": " ", "enspace": " ", "thinspace": " "}
ACCENTS = {"bar": "\u0304", "overline": "\u0305", "hat": "\u0302",
           "dot": "\u0307", "vec": "\u20d7", "tilde": "\u0303"}


class _P:
    """A tiny recursive-descent reader over the LaTeX source."""

    def __init__(self, s):
        self.s = s
        self.i = 0

    def eof(self):
        return self.i >= len(self.s)

    def peek(self):
        return self.s[self.i] if self.i < len(self.s) else ""

    def take(self):
        c = self.s[self.i]
        self.i += 1
        return c

    def skip_ws(self):
        while self.i < len(self.s) and self.s[self.i] in " \t\n":
            self.i += 1

    # ---------------------------------------------------------------- atoms
    def group(self):
        """Read one argument: {...} group, \\command, or a single character."""
        self.skip_ws()
        if self.eof():
            return ""
        if self.peek() == "{":
            self.take()
            inner = self.seq(stop="}")
            if not self.eof() and self.peek() == "}":
                self.take()
            return inner
        if self.peek() == "\\":
            return self.command()
        return self.char()

    def raw_group(self):
        """Read a {..} group as raw text (for \\text and \\mathrm)."""
        self.skip_ws()
        if self.peek() == "{":
            self.take()
            depth, out = 1, []
            while not self.eof():
                c = self.take()
                if c == "{":
                    depth += 1
                elif c == "}":
                    depth -= 1
                    if depth == 0:
                        break
                out.append(c)
            return "".join(out)
        return self.group()

    def char(self):
        c = self.take()
        if c == "-":
            return "−"
        if c == "*":
            return "·"
        if c == "~":
            return "\u00a0"
        if c == "'":
            return "′"
        return c

    def command(self):
        self.take()  # backslash
        if self.eof():
            return ""
        if not self.peek().isalpha():
            name = self.take()
            return SPACES.get(name, name)
        name = ""
        while not self.eof() and self.peek().isalpha():
            name += self.take()

        if name == "frac" or name == "dfrac" or name == "tfrac":
            num = self.group()
            den = self.group()
            cls = "frac" if name != "dfrac" else "frac dfrac"
            return (f'<span class="{cls}"><span class="num">{num}</span>'
                    f'<span class="den">{den}</span></span>')
        if name == "sqrt":
            idx = ""
            self.skip_ws()
            if self.peek() == "[":
                self.take()
                idx = self.seq(stop="]")
                if self.peek() == "]":
                    self.take()
            body = self.group()
            root = "" if not idx else f'<span class="root">{idx}</span>'
            return f'<span class="sqrt">{root}<span class="radical">√</span><span class="radicand">{body}</span></span>'
        if name in ("text", "textrm", "mathrm", "operatorname", "mbox"):
            return f'<span class="txt">{self.raw_group()}</span>'
        if name == "mathit":
            return f'<span class="it">{self.group()}</span>'
        if name == "mathbf":
            return f'<span class="bf">{self.group()}</span>'
        if name == "left" or name == "right":
            return ""
        if name in ("big", "Big", "bigg", "Bigg"):
            return ""
        if name in GREEK:
            return f'<span class="grk">{GREEK[name]}</span>'
        if name in FUNCS:
            lim = ""
            if name in ("lim", "max", "min"):
                # optional limit directly after
                save = self.i
                self.skip_ws()
                if self.peek() == "_":
                    self.take()
                    sub = self.group()
                    lim = f'<span class="limsub">{sub}</span>'
                else:
                    self.i = save
            return f'<span class="fn">{name}</span>{lim}'
        if name in SPACES:
            return SPACES[name]
        if name in ACCENTS:
            body = self.group()
            return f'{body}<span class="accent">{ACCENTS[name]}</span>'
        if name in SYMBOLS:
            return f'<span class="op">{SYMBOLS[name]}</span>'
        if name == "\\":
            return "<br>"
        # unknown command: keep the name so nothing silently disappears
        return f'<span class="unk">\\{name}</span>'

    # ---------------------------------------------------------------- runs
    def script(self, base):
        """Attach ^ and _ runs to a base atom."""
        sub = sup = ""
        for _ in range(2):
            self.skip_ws()
            if self.peek() == "^":
                self.take()
                sup = self.group()
            elif self.peek() == "_":
                self.take()
                sub = self.group()
            else:
                break
        if not sub and not sup:
            return base
        out = f'<span class="scr"><span class="base">{base}</span>'
        if sup:
            out += f'<span class="sup">{sup}</span>'
        if sub:
            out += f'<span class="sub">{sub}</span>'
        return out + "</span>"


    def seq(self, stop=""):
        parts = []
        while not self.eof():
            c = self.peek()
            if stop and c == stop:
                break
            if c == "}":
                break
            if c == "{":
                parts.append(self.script(self.group()))
                continue
            if c == "\\":
                parts.append(self.script(self.command()))
                continue
            if c == "^" or c == "_":
                # script on the preceding atom
                prev = parts.pop() if parts else ""
                parts.append(self.script(prev) if prev else self.script(""))
                continue
            if c == "&":
                self.take()
                parts.append(" ")
                continue
            parts.append(self.script(self.char()))
        return "".join(parts)


def latex_to_html(tex, mode="display"):
    """LaTeX -> HTML with stacked fractions and real symbols."""
    if not tex:
        return ""
    src = str(tex).strip()
    body = _P(src).seq()
    return f'<span class="mathx {"block" if mode == "display" else "inline"}">{body}</span>'


# --------------------------------------------------------------------- CSS
CSS = """
.mathx{font-family:"Cambria Math","STIX Two Math","Latin Modern Math",Georgia,"Times New Roman",serif;
  font-size:1.06em;line-height:1.1;color:#3d1a6b}
.mathx.block{display:block;text-align:center;padding:10px 6px;overflow-x:auto;overflow-y:hidden}
.mathx .frac{display:inline-flex;flex-direction:column;vertical-align:middle;
  text-align:center;margin:0 .18em;position:relative;top:-.06em}
.mathx .frac>.num{border-bottom:1.4px solid currentColor;padding:0 .22em .06em;display:block;line-height:1.15}
.mathx .frac>.den{padding:.06em .22em 0;display:block;line-height:1.15}
.mathx .dfrac>.num,.mathx .dfrac>.den{font-size:1em}
.mathx .scr{display:inline}
.mathx .scr>.base{display:inline}
.mathx .scr>.sup{font-size:.68em;line-height:0;vertical-align:.62em;padding-left:.04em}
.mathx .scr>.sub{font-size:.68em;line-height:0;vertical-align:-.28em;padding-left:.04em}
.mathx .sqrt{display:inline-flex;align-items:flex-start}
.mathx .sqrt>.radical{font-size:1.15em;line-height:.9}
.mathx .sqrt>.radicand{border-top:1.2px solid currentColor;padding:0 .12em;margin-top:.12em}
.mathx .sqrt>.root{font-size:.62em;margin-right:-.2em;position:relative;top:-.25em;left:.15em}
.mathx .grk{font-style:italic}
.mathx .fn{font-style:normal;padding-right:.12em}
.mathx .limsub{font-size:.72em;display:inline-block;vertical-align:-.35em}
.mathx .op{padding:0 .1em}
.mathx .txt{font-family:inherit;font-style:normal}
.mathx .it{font-style:italic}
.mathx .bf{font-weight:700}
.mathx .accent{display:inline-block;margin-left:-.35em;font-size:.9em}
.mathx .unk{color:#b03030}
.eqn{background:#f7f2fd;border-left:4px solid #7b2cd9;border-radius:8px;
  margin:10px 0 14px;padding:4px 14px 6px}
.eqn .mathx.block{padding:8px 4px}
@media print{.eqn{break-inside:avoid}}
"""


if __name__ == "__main__":  # quick visual check in the terminal
    import sys
    for t in sys.argv[1:] or [r"T=T_{fp}\,\frac{P}{P_{fp}}",
                              r"P_{abs}=P_{gauge}+P_{atm}",
                              r"A=\pi D^2/4",
                              r"W=nRT\ln\frac{V_2}{V_1}"]:
        print(f"{t}\n  -> {latex_to_html(t)[:220]}\n")
