import 'package:flutter/material.dart';

import '../ads/ad_banner.dart';
import '../data/repository.dart';
import '../l10n.dart';
import '../state.dart';
import '../theme.dart';
import '../widgets/code_block.dart';
import '../widgets/common.dart';
import '../widgets/diagram.dart';
import '../widgets/html_body.dart';

/// Unit page: purple bar with tabs (Notes / Programs / Diagrams / ...), lavender section
/// headers, white tap-to-open cards – the design from the reference screenshot.
class UnitScreen extends StatelessWidget {
  const UnitScreen({super.key, required this.code, required this.unit});
  final String code;
  final int unit;

  Future<(Map<String, dynamic>, Map<String, dynamic>)> _load() async {
    final s = await repo.subject(code);
    final u = await repo.unit(code, unit);
    app.addRecent(RecentUnit(code, unit, Map<String, dynamic>.from(u['title'] as Map),
        Map<String, dynamic>.from(s['name'] as Map)));
    return (s, u);
  }

  @override
  Widget build(BuildContext context) {
    return Loader<(Map<String, dynamic>, Map<String, dynamic>)>(
      load: _load,
      builder: (context, d) => ListenableBuilder(
        listenable: app,
        builder: (context, _) => _UnitView(subject: d.$1, unit: d.$2),
      ),
    );
  }
}

class _UnitView extends StatelessWidget {
  const _UnitView({required this.subject, required this.unit});
  final Map<String, dynamic> subject, unit;

  @override
  Widget build(BuildContext context) {
    final ctx = UnitCtx(subject, unit);
    final tabs = ctx.tabs();
    return DefaultTabController(
      length: tabs.length,
      child: Scaffold(
        appBar: AppBar(
          titleSpacing: 0,
          title: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
            Text('${L('unit')} ${unit['unit']}: ${tr(unit['title'])}',
                maxLines: 1, overflow: TextOverflow.ellipsis, style: const TextStyle(fontSize: 17.5)),
            Text('${tr(subject['name'])} · ${subject['code']}',
                maxLines: 1,
                overflow: TextOverflow.ellipsis,
                style: const TextStyle(fontSize: 12.5, fontWeight: FontWeight.w500, color: Color(0xE6FFFFFF))),
          ]),
          actions: const [LangButton()],
          bottom: TabBar(
            isScrollable: true,
            tabs: [for (final t in tabs) Tab(text: L(t))],
          ),
        ),
        bottomNavigationBar: const AdBanner(),
        body: TabBarView(children: [for (final t in tabs) _TabList(key: PageStorageKey(t), ctx: ctx, tab: t)]),
      ),
    );
  }
}

/// Helpers over one unit's data.
class UnitCtx {
  UnitCtx(this.subject, this.unit);
  final Map<String, dynamic> subject, unit;

  String? get codeLang => subject['code_lang'] as String?;
  bool get isPy => codeLang == 'python';
  List<Map<String, dynamic>> list(String k) => ((unit[k] as List?) ?? []).cast<Map<String, dynamic>>();
  Map<String, dynamic> get svgs => (unit['svgs'] as Map?)?.cast<String, dynamic>() ?? {};

  static const knownTabs = {
    'notes', 'programs', 'diagrams', 'flowcharts', 'algorithms', 'syntax', 'equations', 'numericals', 'viva', 'exam'
  };

  List<String> tabs() {
    // A unit may list its own tabs (newer content); unknown names are skipped so old apps stay safe.
    final custom = (unit['tabs'] as List?)?.cast<String>().where(knownTabs.contains).toList();
    if (custom != null && custom.isNotEmpty) return custom;
    if (unit['programs'] != null) {
      return ['notes', 'programs', isPy ? 'diagrams' : 'flowcharts', 'syntax', 'viva', 'exam'];
    }
    if (unit['numericals'] != null) return ['notes', 'diagrams', 'equations', 'numericals', 'viva', 'exam'];
    return ['notes', 'diagrams', 'equations', 'viva', 'exam'];
  }

  String diagramTitle(String id) =>
      tr(list('diagrams').firstWhere((d) => d['id'] == id, orElse: () => {'title': id})['title']);

  Widget diagram(String id, {bool caption = true}) {
    final svg = svgs[id] as String?;
    if (svg == null) return const SizedBox.shrink();
    return DiagramInline(svg: svg, title: diagramTitle(id), caption: caption);
  }

  Map<String, dynamic>? program(String id) => list('programs').where((p) => p['id'] == id).firstOrNull;
  Map<String, dynamic>? numerical(String id) => list('numericals').where((p) => p['id'] == id).firstOrNull;

  Widget label(String k) => Padding(
        padding: const EdgeInsets.only(top: 8, bottom: 4),
        child: Text(L(k).toUpperCase(),
            style: const TextStyle(fontSize: 12, fontWeight: FontWeight.w800, color: C.pd, letterSpacing: 0.4)),
      );

  /// Code + Output (+ plot) + Explanation.
  Widget programBody(Map<String, dynamic> p) => Column(crossAxisAlignment: CrossAxisAlignment.stretch, children: [
        label('code'),
        CodeBlock(tr(p['code']), lang: codeLang),
        label('output'),
        CodeBlock(p['out'] as String? ?? '', output: true),
        if (p['plot'] != null) ...[label('plot'), diagram(p['plot'] as String, caption: false)],
        if (p['expl'] != null && tr(p['expl']).isNotEmpty) ...[
          label('expl'),
          HtmlBody(tr(p['expl']), codeLang: codeLang),
        ],
      ]);

  Widget programBox(String id) {
    final p = program(id);
    if (p == null) return const SizedBox.shrink();
    return _box(const Color(0xFF2E8B7A), const Color(0xFFF2FBF8), const Color(0xFF1F6E60),
        '${L('prog')}: ${tr(p['title'])}', programBody(p));
  }

  Widget exampleBox(String id) {
    final n = numerical(id);
    if (n == null) return const SizedBox.shrink();
    return _box(const Color(0xFFC9A227), const Color(0xFFFFFBEF), C.gold, L('ex'),
        Column(crossAxisAlignment: CrossAxisAlignment.stretch, children: [
          HtmlBody('<b>${tr(n['q'])}</b>'),
          const SizedBox(height: 6),
          HtmlBody(tr(n['a'])),
        ]));
  }

  Widget _box(Color border, Color bg, Color fg, String title, Widget child) => Container(
        margin: const EdgeInsets.only(top: 12, bottom: 10),
        padding: const EdgeInsets.all(12),
        decoration: BoxDecoration(
          color: bg,
          borderRadius: BorderRadius.circular(10),
          border: Border.all(color: border, width: 1.5),
        ),
        child: Column(crossAxisAlignment: CrossAxisAlignment.stretch, children: [
          Text(title, style: TextStyle(fontWeight: FontWeight.w800, color: fg, fontSize: 13.5)),
          const SizedBox(height: 6),
          child,
        ]),
      );
}

/// One row in a tab list: a section header, a card, or any widget.
class _Row {
  _Row.header(this.title, [this.groupKeys]) : key = null, builder = null, widget = null;
  _Row.card(this.key, this.builder) : title = null, groupKeys = null, widget = null;
  _Row.widget(this.widget) : title = null, groupKeys = null, key = null, builder = null;
  final String? title, key;
  final List<String>? groupKeys;
  final Widget Function(bool open, VoidCallback toggle)? builder;
  final Widget? widget;
}

class _TabList extends StatefulWidget {
  const _TabList({super.key, required this.ctx, required this.tab});
  final UnitCtx ctx;
  final String tab;
  @override
  State<_TabList> createState() => _TabListState();
}

class _TabListState extends State<_TabList> with AutomaticKeepAliveClientMixin {
  final Set<String> _open = {};
  @override
  bool get wantKeepAlive => true;

  @override
  void initState() {
    super.initState();
    if (widget.tab == 'notes') _open.add('n0_0'); // first topic open, like the preview
  }

  void _toggle(String k) => setState(() => _open.contains(k) ? _open.remove(k) : _open.add(k));

  @override
  Widget build(BuildContext context) {
    super.build(context);
    final rows = _rows();
    return ListView.builder(
      padding: const EdgeInsets.only(bottom: 24),
      itemCount: rows.length,
      itemBuilder: (context, i) {
        final r = rows[i];
        if (r.widget != null) return r.widget!;
        if (r.title != null) {
          final keys = r.groupKeys;
          return SectionHeader(r.title!,
              onExpand: keys == null ? null : () => setState(() => _open.addAll(keys)),
              onCollapse: keys == null ? null : () => setState(() => _open.removeAll(keys)));
        }
        return Padding(
          padding: const EdgeInsets.symmetric(horizontal: 10),
          child: r.builder!(_open.contains(r.key), () => _toggle(r.key!)),
        );
      },
    );
  }

  // ------------------------------------------------------------------ rows per tab
  List<_Row> _rows() {
    final c = widget.ctx;
    switch (widget.tab) {
      case 'notes':
        return _notes(c);
      case 'programs':
        final ps = c.list('programs');
        final keys = [for (var i = 0; i < ps.length; i++) 'p$i'];
        return [
          _Row.header(L('programs'), keys),
          for (var i = 0; i < ps.length; i++)
            _Row.card(keys[i], (o, t) => ExpandCard(
                  open: o,
                  onTap: t,
                  heading: true,
                  number: '${i + 1}.',
                  title: Text(tr(ps[i]['title'])),
                  bodyPadding: const EdgeInsets.fromLTRB(14, 0, 14, 16),
                  body: (_) => c.programBody(ps[i]),
                )),
        ];
      case 'diagrams':
      case 'flowcharts':
        final ds = c.list('diagrams');
        return [
          _Row.header(L(widget.tab)),
          for (var i = 0; i < ds.length; i++) _Row.widget(_diagramCard(c, i, ds[i])),
        ];
      case 'equations':
        return _grouped(c, 'equations', 'e', (e, i, o, t) => ExpandCard(
              open: o,
              onTap: t,
              number: '${i + 1}.',
              title: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
                Text(tr(e['name'])),
                const SizedBox(height: 6),
                Container(
                  padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 8),
                  decoration: BoxDecoration(color: const Color(0xFFF5EEFD), borderRadius: BorderRadius.circular(6)),
                  child: HtmlBody('<b>${tr(e['f'])}</b>', fontSize: 17),
                ),
              ]),
              body: tr(e['terms']).isEmpty ? null : (_) => HtmlBody(tr(e['terms'])),
            ));
      case 'numericals':
        final ns = c.list('numericals');
        final keys = [for (var i = 0; i < ns.length; i++) 'num$i'];
        return [
          _Row.header(L('numericals'), keys),
          for (var i = 0; i < ns.length; i++)
            _Row.card(keys[i], (o, t) => ExpandCard(
                  open: o,
                  onTap: t,
                  number: '${i + 1}.',
                  title: HtmlBody(tr(ns[i]['q']), fontSize: 16.5),
                  body: (_) => HtmlBody(tr(ns[i]['a'])),
                )),
        ];
      case 'syntax':
      case 'algorithms':
        return _grouped(c, widget.tab, widget.tab == 'syntax' ? 's' : 'a', (e, i, o, t) => ExpandCard(
              open: o,
              onTap: tr(e['terms']).isEmpty ? null : t,
              number: '${i + 1}.',
              title: Column(crossAxisAlignment: CrossAxisAlignment.stretch, children: [
                Text(tr(e['name'])),
                CodeBlock(tr(e['f']), lang: c.codeLang, compact: true),
              ]),
              body: tr(e['terms']).isEmpty ? null : (_) => HtmlBody(tr(e['terms']), codeLang: c.codeLang),
            ));
      case 'viva':
        return _grouped(c, 'viva', 'v', (e, i, o, t) => ExpandCard(
              open: o,
              onTap: t,
              number: '${i + 1}.',
              title: Text(tr(e['q'])),
              body: (_) => HtmlBody(tr(e['a']), codeLang: c.codeLang),
            ));
      case 'exam':
        final xs = c.list('exam_questions');
        return [
          _Row.header(L('examhead')),
          for (var i = 0; i < xs.length; i++)
            _Row.card('x$i', (o, t) => ExpandCard(
                  open: false,
                  onTap: null,
                  number: '${i + 1}.',
                  title: Text(tr(xs[i]['q'])),
                  body: null,
                  trailing: Padding(
                    padding: const EdgeInsets.only(left: 8, top: 2),
                    child: Pill('${xs[i]['marks']} ${L('marks')}', bg: C.goldBg, fg: C.gold),
                  ),
                )),
        ];
    }
    return [];
  }

  List<_Row> _notes(UnitCtx c) {
    final u = c.unit;
    final introKey = c.unit['intro'] is String
        ? c.unit['intro'] as String
        : (c.unit['programs'] != null ? (c.isPy ? 'intro_py' : 'intro_c') : 'intro_d');
    final rows = <_Row>[
      _Row.widget(Container(
        margin: const EdgeInsets.fromLTRB(10, 12, 10, 12),
        padding: const EdgeInsets.all(16),
        decoration: BoxDecoration(gradient: C.heroGradient, borderRadius: BorderRadius.circular(14)),
        child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
          Text(tr(u['title']), style: const TextStyle(color: Colors.white, fontSize: 16.5, fontWeight: FontWeight.w800)),
          const SizedBox(height: 4),
          Text('${L('unit')} ${u['unit']} · ${u['weightage']}% ${L('weightage')} · ${u['hours']} ${L('hours')}',
              style: const TextStyle(color: Color(0xE6FFFFFF), fontSize: 13)),
          const SizedBox(height: 4),
          Text(L(introKey), style: const TextStyle(color: Color(0xE6FFFFFF), fontSize: 13)),
        ]),
      )),
    ];
    final secs = c.list('notes');
    for (var si = 0; si < secs.length; si++) {
      final items = ((secs[si]['items'] as List?) ?? []).cast<Map<String, dynamic>>();
      final keys = [for (var i = 0; i < items.length; i++) 'n${si}_$i'];
      rows.add(_Row.header(tr(secs[si]['title']), keys));
      for (var i = 0; i < items.length; i++) {
        final it = items[i];
        if (it['h'] != null) {
          rows.add(_Row.card(keys[i], (o, t) => ExpandCard(
                open: o,
                onTap: t,
                heading: true,
                title: Text(tr(it['h'])),
                bodyPadding: const EdgeInsets.fromLTRB(18, 0, 16, 16),
                body: (_) => Column(crossAxisAlignment: CrossAxisAlignment.stretch, children: [
                  HtmlBody(tr(it['body']), codeLang: c.codeLang),
                  if (it['diagram'] != null) c.diagram(it['diagram'] as String),
                  for (final ex in ((it['examples'] as List?) ?? [])) c.exampleBox(ex as String),
                  for (final p in ((it['programs'] as List?) ?? [])) c.programBox(p as String),
                ]),
              )));
        } else {
          rows.add(_Row.card(keys[i], (o, t) => ExpandCard(
                open: o,
                onTap: t,
                number: '${i + 1}.',
                title: Text(tr(it['q'])),
                body: (_) => Column(crossAxisAlignment: CrossAxisAlignment.stretch, children: [
                  HtmlBody(tr(it['a']), codeLang: c.codeLang),
                  if (it['diagram'] != null) c.diagram(it['diagram'] as String),
                ]),
              )));
        }
      }
    }
    return rows;
  }

  List<_Row> _grouped(UnitCtx c, String field, String prefix,
      Widget Function(Map<String, dynamic> e, int i, bool open, VoidCallback toggle) card) {
    final rows = <_Row>[];
    final groups = c.list(field);
    for (var g = 0; g < groups.length; g++) {
      final items = ((groups[g]['items'] as List?) ?? []).cast<Map<String, dynamic>>();
      final keys = [for (var i = 0; i < items.length; i++) '$prefix${g}_$i'];
      rows.add(_Row.header(tr(groups[g]['title']), keys));
      for (var i = 0; i < items.length; i++) {
        rows.add(_Row.card(keys[i], (o, t) => card(items[i], i, o, t)));
      }
    }
    return rows;
  }

  Widget _diagramCard(UnitCtx c, int i, Map<String, dynamic> d) {
    final svg = c.svgs[d['id']] as String?;
    if (svg == null) return const SizedBox.shrink();
    final title = tr(d['title']);
    return Container(
      margin: const EdgeInsets.fromLTRB(10, 4, 10, 8),
      decoration: BoxDecoration(
        color: Colors.white,
        borderRadius: BorderRadius.circular(10),
        boxShadow: const [BoxShadow(color: Color(0x243C146E), blurRadius: 3, offset: Offset(0, 1))],
      ),
      clipBehavior: Clip.antiAlias,
      child: InkWell(
        onTap: () => openDiagram(context, svg, title),
        child: Column(crossAxisAlignment: CrossAxisAlignment.stretch, children: [
          Padding(
            padding: const EdgeInsets.fromLTRB(14, 12, 14, 10),
            child: Text('${i + 1}. $title',
                style: const TextStyle(color: C.p, fontWeight: FontWeight.w700, fontSize: 15.5)),
          ),
          const Divider(height: 1, color: Color(0xFFF0E8F9)),
          DiagramPicture(svg: svg),
        ]),
      ),
    );
  }
}
