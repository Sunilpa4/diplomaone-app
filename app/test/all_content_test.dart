import 'dart:convert';
import 'dart:io';

import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:diploma_one/screens/unit_screen.dart';
import 'package:diploma_one/widgets/code_block.dart';
import 'package:diploma_one/widgets/diagram.dart';
import 'package:diploma_one/widgets/html_body.dart';

String en(dynamic o) => o is Map ? (o['en'] ?? '') as String : (o ?? '').toString();

void main() {
  final files = Directory('../build/data/units').listSync().whereType<File>().toList()
    ..sort((a, b) => a.path.compareTo(b.path));
  for (final f in files) {
    testWidgets(f.uri.pathSegments.last, (t) async {
      t.view.physicalSize = const Size(412, 880);
      t.view.devicePixelRatio = 1;
      final u = jsonDecode(f.readAsStringSync()) as Map<String, dynamic>;
      final code = u['subject'] as String;
      final s = jsonDecode(File('../build/data/subjects/$code.json').readAsStringSync()) as Map<String, dynamic>;
      final c = UnitCtx(s, u);
      final parts = <String, Widget>{};
      for (final sec in c.list('notes')) {
        for (final it in (sec['items'] as List)) {
          parts['note ${en(it['h'] ?? it['q'])}'] = Column(crossAxisAlignment: CrossAxisAlignment.stretch, children: [
            HtmlBody(en(it['body'] ?? it['a']), codeLang: c.codeLang),
            if (it['diagram'] != null) c.diagram(it['diagram']),
            for (final e in (it['examples'] as List? ?? [])) c.exampleBox(e),
            for (final p in (it['programs'] as List? ?? [])) c.programBox(p),
          ]);
        }
      }
      for (final p in c.list('programs')) { parts['prog ${p['id']}'] = c.programBody(p); }
      for (final n in c.list('numericals')) { parts['num ${n['id']}'] = Column(children: [HtmlBody(en(n['q'])), HtmlBody(en(n['a']))]); }
      for (final g in [...c.list('equations'), ...c.list('syntax'), ...c.list('algorithms'), ...c.list('viva')]) {
        for (final e in (g['items'] as List)) {
          parts['item ${en(e['name'] ?? e['q'])}'] = Column(children: [
            if (e['f'] != null) (c.unit['syntax'] != null || c.unit['algorithms'] != null ? CodeBlock(e['f'], lang: c.codeLang, compact: true) : HtmlBody('<b>${e['f']}</b>')),
            HtmlBody(en(e['terms'] ?? e['a']), codeLang: c.codeLang),
          ]);
        }
      }
      for (final d in c.list('diagrams')) { parts['dg ${d['id']}'] = DiagramPicture(svg: c.svgs[d['id']]); }
      for (final tab in c.tabs()) {
        expect(UnitCtx.knownTabs.contains(tab), true, reason: 'unknown tab $tab');
      }
      var bad = 0;
      for (final e in parts.entries) {
        await t.pumpWidget(MaterialApp(home: Scaffold(body: ListView(children: [e.value]))));
        await t.pump(const Duration(milliseconds: 300));
        final ex = t.takeException();
        if (ex != null) {
          bad++;
          // ignore: avoid_print
          print('  BAD ${e.key}: ${ex.toString().split('\n').first}');
        }
      }
      // ignore: avoid_print
      print('${f.uri.pathSegments.last}: ${parts.length} parts, $bad bad');
      expect(bad, 0, reason: 'some content parts failed to render');
    });
  }
}
