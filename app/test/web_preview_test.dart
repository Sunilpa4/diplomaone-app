import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:diploma_one/widgets/code_block.dart';
import 'package:diploma_one/widgets/web_preview.dart';

void main() {
  const a = {
    'bootstrap.min.css': '/*BS-CSS*/',
    'bootstrap.bundle.min.js': '/*BS-JS*/',
    'jquery.min.js': '/*JQ*/',
    'bootstrap-icons.min.css': '/*ICONS*/',
    'shell.js': '/*SHELL*/',
  };
  const page = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">
  <script src="https://code.jquery.com/jquery-3.7.1.min.js"></script>
</head>
<body>
  <h1 class="text-center">Hi</h1>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>''';

  test('CDN tags are replaced by bundled files', () {
    final h = buildPreviewHtml(page, a);
    for (final k in ['/*BS-CSS*/', '/*BS-JS*/', '/*JQ*/', '/*ICONS*/', '/*SHELL*/']) {
      expect(h.contains(k), isTrue, reason: k);
    }
    expect(h.contains('cdn.jsdelivr'), isFalse);
    expect(h.contains('code.jquery.com'), isFalse);
    expect(h.indexOf('/*SHELL*/') < h.indexOf('/*BS-CSS*/'), isTrue);
    expect(buildPreviewHtml(page, a, desktop: true).contains('width=1100'), isTrue);
  });

  test('HTML highlighting keeps the text unchanged', () {
    final spans = highlight(page, 'html');
    expect(spans.map((s) => s.toPlainText()).join(), page);
    expect(spans.length > 20, isTrue);
  });

  testWidgets('Run button renders', (t) async {
    await t.pumpWidget(const MaterialApp(home: Scaffold(body: RunButton(code: page, title: 'x'))));
    expect(find.byType(FilledButton), findsOneWidget);
  });
}
