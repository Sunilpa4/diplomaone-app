import 'package:flutter/material.dart';

import '../ads/ad_banner.dart';
import '../data/repository.dart';
import '../l10n.dart';
import '../state.dart';
import '../theme.dart';
import '../widgets/common.dart';
import 'unit_screen.dart';

class SubjectScreen extends StatelessWidget {
  const SubjectScreen({super.key, required this.code});
  final String code;

  @override
  Widget build(BuildContext context) {
    final meta = repo.subjectMeta(code);
    return ListenableBuilder(
      listenable: app,
      builder: (context, _) => Scaffold(
        appBar: AppBar(
          title: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
            Text(tr(meta?['name']), maxLines: 1, overflow: TextOverflow.ellipsis),
            Text(code, style: const TextStyle(fontSize: 12.5, fontWeight: FontWeight.w500, color: Color(0xE6FFFFFF))),
          ]),
          actions: const [LangButton()],
        ),
        bottomNavigationBar: const AdBanner(),
        body: Loader<Map<String, dynamic>>(
          load: () => repo.subject(code),
          builder: (context, s) => _body(context, s, meta),
        ),
      ),
    );
  }

  Widget _body(BuildContext context, Map<String, dynamic> s, Map<String, dynamic>? meta) {
    final units = (s['units'] as List).cast<Map<String, dynamic>>();
    final avail = ((s['available_units'] as List?) ?? []).cast<int>();
    final ex = (s['exam'] as Map?)?.cast<String, dynamic>() ?? {};
    return ListView(children: [
      Container(
        margin: const EdgeInsets.all(12),
        padding: const EdgeInsets.all(16),
        decoration: BoxDecoration(gradient: C.heroGradient, borderRadius: BorderRadius.circular(16)),
        child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
          Text(tr(s['name']), style: const TextStyle(color: Colors.white, fontSize: 18, fontWeight: FontWeight.w800)),
          const SizedBox(height: 4),
          Text(
            '${s['code']}${meta?['alt_code'] != null ? '  ·  ${L('also_code')}: ${meta!['alt_code']}' : ''}',
            style: const TextStyle(color: Color(0xE6FFFFFF), fontSize: 12.5),
          ),
          const SizedBox(height: 12),
          Wrap(spacing: 8, runSpacing: 8, children: [
            _chip('${ex['credits'] ?? meta?['credits'] ?? '-'} ${L('credits')}'),
            _chip('${units.length} ${L('units')}'),
            if (meta?['type'] != null) _chip(L('type_${meta!['type']}')),
            _chip('Syllabus ${s['syllabus_year'] ?? AppInfo.syllabus}'),
          ]),
          if (ex.isNotEmpty) ...[
            const SizedBox(height: 14),
            Text(L('exam_scheme'),
                style: const TextStyle(color: Colors.white, fontWeight: FontWeight.w800, fontSize: 13.5)),
            const SizedBox(height: 6),
            Container(
              padding: const EdgeInsets.symmetric(vertical: 8, horizontal: 6),
              decoration: BoxDecoration(color: const Color(0x26FFFFFF), borderRadius: BorderRadius.circular(10)),
              child: Row(children: [
                _ex('${L('theory')} ESE', ex['theory_ese']),
                _ex('${L('theory')} PA', ex['theory_pa']),
                _ex('${L('practical')} PA', ex['practical_pa']),
                _ex('${L('practical')} ESE', ex['practical_ese']),
                _ex(L('total'), ex['total'], bold: true),
              ]),
            ),
          ],
        ]),
      ),
      SectionHeader(L('units')),
      Padding(
        padding: const EdgeInsets.symmetric(horizontal: 10),
        child: Column(children: [
          for (final u in units) _unitCard(context, s, u, avail.contains(u['no'])),
        ]),
      ),
      const SizedBox(height: 8),
      SectionHeader(L('paper_solutions')),
      Padding(
        padding: const EdgeInsets.symmetric(horizontal: 10),
        child: Container(
          padding: const EdgeInsets.all(16),
          decoration: BoxDecoration(color: Colors.white, borderRadius: BorderRadius.circular(12)),
          child: Row(children: [
            const Icon(Icons.assignment_rounded, color: C.muted),
            const SizedBox(width: 12),
            Expanded(child: Text(L('paper_soon'), style: const TextStyle(color: C.muted))),
            Pill(L('coming_soon'), bg: const Color(0xFFF0EDF3), fg: C.muted),
          ]),
        ),
      ),
      const SizedBox(height: 20),
    ]);
  }

  Widget _chip(String t) => Container(
        padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 4),
        decoration: BoxDecoration(color: const Color(0x2EFFFFFF), borderRadius: BorderRadius.circular(12)),
        child: Text(t, style: const TextStyle(color: Colors.white, fontSize: 12, fontWeight: FontWeight.w700)),
      );

  Widget _ex(String label, dynamic v, {bool bold = false}) => Expanded(
        child: Column(children: [
          Text('${v ?? 0}',
              style: TextStyle(color: Colors.white, fontSize: bold ? 17 : 15.5, fontWeight: FontWeight.w800)),
          const SizedBox(height: 2),
          Text(label,
              textAlign: TextAlign.center,
              style: const TextStyle(color: Color(0xDDFFFFFF), fontSize: 10, height: 1.2)),
        ]),
      );

  Widget _unitCard(BuildContext context, Map<String, dynamic> s, Map<String, dynamic> u, bool ready) {
    final no = u['no'] as int;
    return Container(
      margin: const EdgeInsets.only(bottom: 8),
      child: Material(
        color: Colors.white,
        borderRadius: BorderRadius.circular(10),
        clipBehavior: Clip.antiAlias,
        child: InkWell(
          onTap: ready
              ? () => Navigator.push(context, MaterialPageRoute(builder: (_) => UnitScreen(code: code, unit: no)))
              : () => ScaffoldMessenger.of(context).showSnackBar(SnackBar(content: Text(L('soon_msg')))),
          child: Padding(
            padding: const EdgeInsets.fromLTRB(14, 14, 8, 14),
            child: Row(children: [
              Container(
                width: 42,
                height: 42,
                alignment: Alignment.center,
                decoration: BoxDecoration(
                    color: ready ? C.p : const Color(0xFFE9E3F0), borderRadius: BorderRadius.circular(21)),
                child: Text('$no',
                    style: TextStyle(color: ready ? Colors.white : C.muted, fontSize: 18, fontWeight: FontWeight.w800)),
              ),
              const SizedBox(width: 12),
              Expanded(
                child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
                  Text(tr(u['title']),
                      style: const TextStyle(color: C.p, fontSize: 15.5, fontWeight: FontWeight.w700, height: 1.3)),
                  const SizedBox(height: 4),
                  Text('${L('unit')} $no · ${u['weightage']}% ${L('weightage')} · ${u['hours']} ${L('hours')}',
                      style: const TextStyle(fontSize: 12.5, color: C.muted)),
                ]),
              ),
              Icon(Icons.chevron_right_rounded, color: ready ? C.p : C.muted),
            ]),
          ),
        ),
      ),
    );
  }
}
