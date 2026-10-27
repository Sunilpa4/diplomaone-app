import 'package:flutter/material.dart';
import 'package:flutter_widget_from_html_core/flutter_widget_from_html_core.dart';

import '../theme.dart';
import 'code_block.dart';

/// Renders the HTML used in notes/answers (p, b, ul/ol, h4, table, sub/sup, code, pre).
class HtmlBody extends StatelessWidget {
  const HtmlBody(this.html, {super.key, this.codeLang, this.fontSize = 15});
  final String html;
  final String? codeLang;
  final double fontSize;

  @override
  Widget build(BuildContext context) {
    return HtmlWidget(
      html,
      textStyle: TextStyle(fontSize: fontSize, height: 1.6, color: const Color(0xFF222222)),
      customStylesBuilder: _styles,
      customWidgetBuilder: (e) {
        if (e.localName == 'pre') {
          return CodeBlock(e.text.replaceAll(RegExp(r'\n$'), ''), lang: codeLang);
        }
        if (e.localName == 'table') {
          final firstRow = e.querySelector('tr');
          final cols = firstRow == null ? 0 : firstRow.children.length;
          return _Table(e.outerHtml, cols: cols, codeLang: codeLang, fontSize: fontSize);
        }
        return null;
      },
    );
  }

  static Map<String, String>? _styles(dynamic e) {
    switch (e.localName) {
      case 'h4':
        return {'color': '#6420B8', 'font-size': '1.0em', 'margin': '12px 0 6px 0', 'font-weight': '700'};
      case 'p':
        return {'margin': '0 0 10px 0'};
      case 'ul':
      case 'ol':
        return {'margin': '0 0 10px 0', 'padding-left': '22px'};
      case 'li':
        return {'margin-bottom': '4px'};
      case 'b':
      case 'strong':
        return {'color': '#111111'};
      case 'code':
        return {
          'background-color': '#F1E9FB',
          'color': '#5B1BB0',
          'font-family': kMono,
          'font-size': '0.88em',
        };
      case 'th':
        return {
          'background-color': '#7B2CD9',
          'color': '#FFFFFF',
          'padding': '7px 8px',
          'font-weight': '700',
          'text-align': 'left',
          'vertical-align': 'top',
        };
      case 'td':
        return {'padding': '7px 8px', 'border-bottom': '1px solid #EADFF6', 'vertical-align': 'top'};
      case 'table':
        return {'border-collapse': 'collapse', 'font-size': '0.88em', 'margin': '0 0 10px 0'};
    }
    return null;
  }
}

/// Tables: narrow ones fill the width; wide ones (4+ columns) scroll sideways.
class _Table extends StatelessWidget {
  const _Table(this.html, {required this.cols, this.codeLang, required this.fontSize});
  final String html;
  final int cols;
  final String? codeLang;
  final double fontSize;

  @override
  Widget build(BuildContext context) {
    final inner = HtmlWidget(
      html,
      textStyle: TextStyle(fontSize: fontSize, height: 1.4, color: const Color(0xFF222222)),
      customStylesBuilder: HtmlBody._styles,
    );
    return Padding(
      padding: const EdgeInsets.only(bottom: 10),
      child: LayoutBuilder(builder: (context, c) {
        final want = cols * 118.0;
        final box = ClipRRect(borderRadius: BorderRadius.circular(6), child: inner);
        if (cols < 4 || want <= c.maxWidth) return box;
        return SingleChildScrollView(
          scrollDirection: Axis.horizontal,
          child: SizedBox(width: want, child: box),
        );
      }),
    );
  }
}
