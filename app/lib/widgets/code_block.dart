import 'package:flutter/material.dart';
import 'package:flutter/services.dart';

import '../l10n.dart';
import '../theme.dart';

const _kw = Color(0xFFC792EA), _ty = Color(0xFF82AAFF), _st = Color(0xFFC3E88D), _cm = Color(0xFF8E9AAF);
const _pp = Color(0xFFF78C6C), _nu = Color(0xFFF9C46B), _fn = Color(0xFFFFCB6B);

final _cKw = 'auto break case const continue default do else enum extern for goto if register return signed sizeof static struct switch typedef union unsigned volatile while'.split(' ').toSet();
final _cTy = 'int char float double void long short FILE size_t'.split(' ').toSet();
final _pKw = 'False None True and as assert async await break class continue def del elif else except finally for from global if import in is lambda nonlocal not or pass raise return try while with yield'.split(' ').toSet();
final _pTy = 'int float str bool list tuple set dict complex frozenset bytes bytearray range object'.split(' ').toSet();

final _cRe = RegExp(
    r'''(//[^\n]*|/\*[\s\S]*?\*/)|("(?:\\.|[^"\\\n])*"|'(?:\\.|[^'\\\n])*')|(^[ \t]*#[^\n]*)|([A-Za-z_]\w*)(?=\s*\()|([A-Za-z_]\w*)|(\b\d+(?:\.\d+)?[fFlLuU]*\b)''',
    multiLine: true);
final _pyRe = RegExp(
    r'''(#[^\n]*)|((?:\b[rRbBfFuU]{1,2})?(?:'{3}[\s\S]*?'{3}|"{3}[\s\S]*?"{3}|'(?:\\.|[^'\\\n])*'|"(?:\\.|[^"\\\n])*"))|(^>>>|^\.\.\.(?= ))|([A-Za-z_]\w*)(?=\s*\()|([A-Za-z_]\w*)|(\b(?:0[xXoObB][0-9a-fA-F_]+|\d[\d_]*(?:\.\d+)?(?:[eE][-+]?\d+)?j?)\b)''',
    multiLine: true);

/// Syntax highlighting for C and Python (same colours as the HTML preview).
List<TextSpan> highlight(String src, String? lang) {
  if (lang != 'c' && lang != 'python') return [TextSpan(text: src)];
  final py = lang == 'python';
  final re = py ? _pyRe : _cRe;
  final kw = py ? _pKw : _cKw, ty = py ? _pTy : _cTy;
  final out = <TextSpan>[];
  var last = 0;
  for (final m in re.allMatches(src)) {
    if (m.start > last) out.add(TextSpan(text: src.substring(last, m.start)));
    last = m.end;
    final w = m.group(0)!;
    Color? c;
    var bold = false, italic = false;
    if (m.group(1) != null) {
      c = _cm;
      italic = true;
    } else if (m.group(2) != null) {
      c = _st;
    } else if (m.group(3) != null) {
      c = _pp;
    } else if (m.group(4) != null) {
      final id = m.group(4)!;
      if (kw.contains(id)) {
        c = _kw;
        bold = true;
      } else {
        c = ty.contains(id) ? _ty : _fn;
      }
    } else if (m.group(5) != null) {
      final id = m.group(5)!;
      if (kw.contains(id)) {
        c = _kw;
        bold = true;
      } else if (ty.contains(id)) {
        c = _ty;
      }
    } else {
      c = _nu;
    }
    out.add(TextSpan(
        text: w,
        style: TextStyle(
            color: c,
            fontWeight: bold ? FontWeight.w700 : null,
            fontStyle: italic ? FontStyle.italic : null)));
  }
  if (last < src.length) out.add(TextSpan(text: src.substring(last)));
  return out;
}

/// Dark code box with horizontal scroll and a copy button.
class CodeBlock extends StatelessWidget {
  const CodeBlock(this.code, {super.key, this.lang, this.output = false, this.compact = false, this.copy = true});
  final String code;
  final String? lang;
  final bool output, compact, copy;

  @override
  Widget build(BuildContext context) {
    final fs = compact ? 12.0 : 12.5;
    final text = Text.rich(
      TextSpan(
          children: output ? [TextSpan(text: code)] : highlight(code, lang),
          style: TextStyle(
              fontFamily: kMono, fontSize: fs, height: 1.5, color: output ? C.outInk : C.codeInk)),
      softWrap: false,
    );
    return Container(
      width: double.infinity,
      margin: EdgeInsets.only(bottom: compact ? 0 : 10, top: compact ? 6 : 0),
      decoration: BoxDecoration(color: output ? C.outBg : C.codeBg, borderRadius: BorderRadius.circular(8)),
      child: Stack(children: [
        SingleChildScrollView(
          scrollDirection: Axis.horizontal,
          padding: EdgeInsets.fromLTRB(11, compact ? 8 : 10, (copy && !output && !compact) ? 40 : 11, compact ? 8 : 10),
          child: text,
        ),
        if (copy && !output && !compact)
          Positioned(
            right: 2,
            top: 2,
            child: IconButton(
              tooltip: 'Copy',
              visualDensity: VisualDensity.compact,
              icon: const Icon(Icons.copy_rounded, size: 17, color: Color(0x99FFFFFF)),
              onPressed: () {
                Clipboard.setData(ClipboardData(text: code));
                ScaffoldMessenger.of(context)
                  ..hideCurrentSnackBar()
                  ..showSnackBar(SnackBar(content: Text(L('copied')), duration: const Duration(seconds: 1)));
              },
            ),
          ),
      ]),
    );
  }
}
