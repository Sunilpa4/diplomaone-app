import 'package:flutter/material.dart';

import '../ads/ad_banner.dart';
import '../data/repository.dart';
import '../l10n.dart';
import '../state.dart';
import '../theme.dart';
import '../widgets/common.dart';
import 'subject_screen.dart';

void _soon(BuildContext context) => ScaffoldMessenger.of(context)
  ..hideCurrentSnackBar()
  ..showSnackBar(SnackBar(content: Text(L('soon_msg'))));

/// Opens a subject if it is ready, otherwise shows "coming soon".
void openSubject(BuildContext context, Map<String, dynamic> meta) {
  if (meta['status'] != 'available') return _soon(context);
  Navigator.push(context, MaterialPageRoute(builder: (_) => SubjectScreen(code: meta['code'] as String)));
}

// ======================================================================= Branches
class BranchesScreen extends StatefulWidget {
  const BranchesScreen({super.key});
  @override
  State<BranchesScreen> createState() => _BranchesScreenState();
}

class _BranchesScreenState extends State<BranchesScreen> {
  String _q = '';

  @override
  Widget build(BuildContext context) {
    return ListenableBuilder(
      listenable: app,
      builder: (context, _) {
        final list = repo.branches().where((b) {
          if (_q.isEmpty) return true;
          final s = '${tr(b['name'], 'en')} ${tr(b['name'], 'gu')} ${b['code']}'.toLowerCase();
          return s.contains(_q.toLowerCase());
        }).toList();
        return Scaffold(
          appBar: AppBar(title: Text(L('all_branches')), actions: const [LangButton()]),
          bottomNavigationBar: const AdBanner(),
          body: ListView(
            padding: const EdgeInsets.fromLTRB(12, 12, 12, 20),
            children: [
              TextField(
                onChanged: (v) => setState(() => _q = v),
                decoration: InputDecoration(
                  hintText: L('search'),
                  prefixIcon: const Icon(Icons.search_rounded),
                  filled: true,
                  fillColor: Colors.white,
                  isDense: true,
                  border: OutlineInputBorder(borderRadius: BorderRadius.circular(28), borderSide: BorderSide.none),
                ),
              ),
              const SizedBox(height: 12),
              for (final b in list) BranchTile(branch: b, wide: true),
            ],
          ),
        );
      },
    );
  }
}

class BranchTile extends StatelessWidget {
  const BranchTile({super.key, required this.branch, this.wide = false});
  final Map<String, dynamic> branch;
  final bool wide;

  @override
  Widget build(BuildContext context) {
    final col = C.hex(branch['color'] as String);
    final ready = repo.readyCount(branch);
    final open = () => Navigator.push(context, MaterialPageRoute(builder: (_) => SemestersScreen(branch: branch)));
    final icon = Container(
      width: wide ? 48 : 42,
      height: wide ? 48 : 42,
      decoration: BoxDecoration(color: col.withValues(alpha: 0.12), borderRadius: BorderRadius.circular(14)),
      child: Icon(branchIcon(branch['icon'] as String?), color: col, size: wide ? 26 : 23),
    );
    final status = ready > 0
        ? Pill('$ready ${L('subjects_ready')}', bg: const Color(0xFFE6F4EA), fg: C.green)
        : Pill(L('coming_soon'), bg: const Color(0xFFF0EDF3), fg: C.muted);
    return Card(
      elevation: 0,
      color: Colors.white,
      margin: EdgeInsets.only(bottom: wide ? 10 : 0),
      shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(14)),
      clipBehavior: Clip.antiAlias,
      child: InkWell(
        onTap: open,
        child: Padding(
          padding: EdgeInsets.all(wide ? 14 : 12),
          child: wide
              ? Row(children: [
                  icon,
                  const SizedBox(width: 14),
                  Expanded(
                    child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
                      Text(tr(branch['name']),
                          style: const TextStyle(fontSize: 15.5, fontWeight: FontWeight.w700, color: C.ink)),
                      const SizedBox(height: 5),
                      Row(children: [
                        Text('Code ${branch['code']}', style: const TextStyle(fontSize: 12.5, color: C.muted)),
                        const SizedBox(width: 8),
                        status,
                      ]),
                    ]),
                  ),
                  const Icon(Icons.chevron_right_rounded, color: C.muted),
                ])
              : Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
                  icon,
                  const Spacer(),
                  Text(tr(branch['name']),
                      maxLines: 2,
                      overflow: TextOverflow.ellipsis,
                      style: const TextStyle(fontSize: 13.5, fontWeight: FontWeight.w700, color: C.ink, height: 1.25)),
                  const SizedBox(height: 3),
                  Text(ready > 0 ? '$ready ${L('subjects_ready')}' : L('coming_soon'),
                      style: TextStyle(fontSize: 11.5, color: ready > 0 ? C.green : C.muted, fontWeight: FontWeight.w600)),
                ]),
        ),
      ),
    );
  }
}

// ======================================================================= Semesters
class SemestersScreen extends StatelessWidget {
  const SemestersScreen({super.key, required this.branch});
  final Map<String, dynamic> branch;

  @override
  Widget build(BuildContext context) {
    final col = C.hex(branch['color'] as String);
    return ListenableBuilder(
      listenable: app,
      builder: (context, _) => Scaffold(
        appBar: AppBar(title: Text(tr(branch['name'])), actions: const [LangButton()]),
        bottomNavigationBar: const AdBanner(),
        body: ListView(padding: const EdgeInsets.all(12), children: [
          Container(
            padding: const EdgeInsets.all(16),
            decoration: BoxDecoration(gradient: C.heroGradient, borderRadius: BorderRadius.circular(16)),
            child: Row(children: [
              Container(
                width: 54,
                height: 54,
                decoration: BoxDecoration(color: Colors.white, borderRadius: BorderRadius.circular(16)),
                child: Icon(branchIcon(branch['icon'] as String?), color: col, size: 30),
              ),
              const SizedBox(width: 14),
              Expanded(
                child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
                  Text(tr(branch['name']),
                      style: const TextStyle(color: Colors.white, fontSize: 17, fontWeight: FontWeight.w800)),
                  const SizedBox(height: 4),
                  Text('GTU Diploma · Code ${branch['code']} · Syllabus ${AppInfo.syllabus}',
                      style: const TextStyle(color: Color(0xE6FFFFFF), fontSize: 12.5)),
                ]),
              ),
            ]),
          ),
          const SizedBox(height: 14),
          Padding(
            padding: const EdgeInsets.only(left: 4, bottom: 8),
            child: Text(L('semesters'), style: const TextStyle(fontSize: 17, fontWeight: FontWeight.w800)),
          ),
          GridView.count(
            crossAxisCount: 2,
            shrinkWrap: true,
            physics: const NeverScrollableScrollPhysics(),
            mainAxisSpacing: 10,
            crossAxisSpacing: 10,
            childAspectRatio: 1.35,
            children: [for (var s = 1; s <= 6; s++) _semTile(context, s)],
          ),
        ]),
      ),
    );
  }

  Widget _semTile(BuildContext context, int s) {
    final subs = repo.subjectsOf(branch, s);
    final ready = repo.readyCount(branch, s);
    final has = subs.isNotEmpty;
    return Material(
      color: Colors.white,
      borderRadius: BorderRadius.circular(16),
      clipBehavior: Clip.antiAlias,
      child: InkWell(
        onTap: () => has
            ? Navigator.push(context, MaterialPageRoute(builder: (_) => SubjectsScreen(branch: branch, sem: s)))
            : _soon(context),
        child: Padding(
          padding: const EdgeInsets.all(14),
          child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
            Row(children: [
              Container(
                width: 40,
                height: 40,
                alignment: Alignment.center,
                decoration: BoxDecoration(
                    color: has ? C.p : const Color(0xFFE9E3F0), borderRadius: BorderRadius.circular(12)),
                child: Text('$s',
                    style: TextStyle(
                        color: has ? Colors.white : C.muted, fontSize: 20, fontWeight: FontWeight.w800)),
              ),
              const Spacer(),
              if (ready > 0) const Icon(Icons.check_circle_rounded, color: C.green, size: 20),
            ]),
            const Spacer(),
            Text('${L('semester')} $s', style: const TextStyle(fontSize: 15.5, fontWeight: FontWeight.w800)),
            const SizedBox(height: 2),
            Text(
              has ? '${subs.length} ${L('subjects')} · $ready ${L('ready')}' : L('coming_soon'),
              style: TextStyle(fontSize: 12, color: ready > 0 ? C.green : C.muted, fontWeight: FontWeight.w600),
            ),
          ]),
        ),
      ),
    );
  }
}

// ======================================================================= Subjects
class SubjectsScreen extends StatelessWidget {
  const SubjectsScreen({super.key, required this.branch, required this.sem});
  final Map<String, dynamic> branch;
  final int sem;

  @override
  Widget build(BuildContext context) {
    return ListenableBuilder(
      listenable: app,
      builder: (context, _) {
        final subs = repo.subjectsOf(branch, sem);
        subs.sort((a, b) => (a['status'] == 'available' ? 0 : 1).compareTo(b['status'] == 'available' ? 0 : 1));
        return Scaffold(
          appBar: AppBar(
            title: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
              Text('${L('semester')} $sem'),
              Text(tr(branch['name']),
                  style: const TextStyle(fontSize: 12.5, fontWeight: FontWeight.w500, color: Color(0xE6FFFFFF))),
            ]),
            actions: const [LangButton()],
          ),
          bottomNavigationBar: const AdBanner(),
          body: ListView(children: [
            SectionHeader('${L('subjects_t')} (${subs.length})'),
            Padding(
              padding: const EdgeInsets.symmetric(horizontal: 10),
              child: Column(children: [for (final m in subs) SubjectCard(meta: m)]),
            ),
            const SizedBox(height: 16),
          ]),
        );
      },
    );
  }
}

class SubjectCard extends StatelessWidget {
  const SubjectCard({super.key, required this.meta, this.subtitle});
  final Map<String, dynamic> meta;
  final String? subtitle;

  @override
  Widget build(BuildContext context) {
    final ready = meta['status'] == 'available';
    return Container(
      margin: const EdgeInsets.only(bottom: 10),
      child: Material(
        color: Colors.white,
        borderRadius: BorderRadius.circular(12),
        clipBehavior: Clip.antiAlias,
        child: InkWell(
          onTap: () => openSubject(context, meta),
          child: Padding(
            padding: const EdgeInsets.all(14),
            child: Row(crossAxisAlignment: CrossAxisAlignment.start, children: [
              Container(
                width: 44,
                height: 44,
                decoration: BoxDecoration(
                    color: ready ? C.lav : const Color(0xFFF0EDF3), borderRadius: BorderRadius.circular(12)),
                child: Icon(subjectTypeIcon(meta['type'] as String?), color: ready ? C.p : C.muted),
              ),
              const SizedBox(width: 12),
              Expanded(
                child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
                  Text(tr(meta['name']),
                      style: TextStyle(
                          fontSize: 15.5, fontWeight: FontWeight.w700, color: ready ? C.ink : const Color(0xFF6B6375))),
                  const SizedBox(height: 4),
                  Text(subtitle ?? '${meta['code']} · ${meta['category']}',
                      style: const TextStyle(fontSize: 12.5, color: C.muted)),
                  const SizedBox(height: 8),
                  Wrap(spacing: 6, runSpacing: 6, children: [
                    ready
                        ? Pill('${L('ready')} · ${meta['units']} ${L('units')}',
                            bg: const Color(0xFFE6F4EA), fg: C.green, icon: Icons.check_rounded)
                        : Pill(L('coming_soon'), bg: const Color(0xFFF0EDF3), fg: C.muted, icon: Icons.schedule_rounded),
                    Pill('${meta['credits']} ${L('credits')}'),
                    Pill(L('type_${meta['type']}')),
                  ]),
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

// ======================================================================= Search
class SearchScreen extends StatefulWidget {
  const SearchScreen({super.key});
  @override
  State<SearchScreen> createState() => _SearchScreenState();
}

class _SearchScreenState extends State<SearchScreen> {
  String _q = '';

  @override
  Widget build(BuildContext context) {
    final q = _q.trim().toLowerCase();
    final res = repo.allSubjects().where((m) {
      if (q.isEmpty) return m['status'] == 'available';
      final s = '${tr(m['name'], 'en')} ${tr(m['name'], 'gu')} ${m['code']} ${m['alt_code']}'.toLowerCase();
      return s.contains(q);
    }).toList()
      ..sort((a, b) => (a['status'] == 'available' ? 0 : 1).compareTo(b['status'] == 'available' ? 0 : 1));
    return Scaffold(
      appBar: AppBar(
        titleSpacing: 0,
        title: TextField(
          autofocus: true,
          onChanged: (v) => setState(() => _q = v),
          style: const TextStyle(color: Colors.white, fontSize: 16.5),
          cursorColor: Colors.white,
          decoration: InputDecoration(
            hintText: L('search'),
            hintStyle: const TextStyle(color: Color(0xBBFFFFFF)),
            border: InputBorder.none,
          ),
        ),
      ),
      body: res.isEmpty
          ? Center(child: Text(L('no_results'), style: const TextStyle(color: C.muted)))
          : ListView(padding: const EdgeInsets.all(10), children: [
              for (final m in res)
                SubjectCard(meta: m, subtitle: () {
                  final w = repo.whereIs(m['code'] as String);
                  final where = w == null ? '' : ' · ${L('sem')} ${w.$2} · ${tr(w.$1['name'])}';
                  return '${m['code']}$where';
                }()),
            ]),
    );
  }
}
