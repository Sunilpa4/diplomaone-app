import 'package:flutter/material.dart';

import '../ads/ad_banner.dart';
import '../data/repository.dart';
import '../l10n.dart';
import '../state.dart';
import '../theme.dart';
import '../widgets/common.dart';
import 'browse.dart';
import 'unit_screen.dart';

class HomeScreen extends StatefulWidget {
  const HomeScreen({super.key});

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  bool _refreshing = false;

  Future<void> _refresh() async {
    if (_refreshing) return;
    setState(() => _refreshing = true);
    try {
      await repo.refresh();
    } catch (_) {
      if (mounted) ScaffoldMessenger.of(context).showSnackBar(SnackBar(content: Text(L('load_error'))));
    } finally {
      if (mounted) setState(() => _refreshing = false);
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      bottomNavigationBar: const AdBanner(),
      body: Loader<Map<String, dynamic>>(
        load: repo.catalog,
        builder: (context, _) => ListenableBuilder(listenable: app, builder: (context, _) => _body(context)),
      ),
    );
  }

  Widget _body(BuildContext context) {
    final branches = repo.branches();
    final ready = repo.allSubjects().where((m) => m['status'] == 'available').toList();
    return RefreshIndicator(
      onRefresh: _refresh,
      child: CustomScrollView(
        physics: const AlwaysScrollableScrollPhysics(),
        slivers: [
          SliverToBoxAdapter(child: _hero(context, branches.length, ready.length)),
          if (app.recent.isNotEmpty) ...[
            _title(L('continue')),
            SliverToBoxAdapter(
              child: SizedBox(
                height: 112,
                child: ListView.separated(
                  scrollDirection: Axis.horizontal,
                  padding: const EdgeInsets.symmetric(horizontal: 14),
                  itemCount: app.recent.length,
                  separatorBuilder: (_, __) => const SizedBox(width: 10),
                  itemBuilder: (context, i) => _recentCard(context, app.recent[i]),
                ),
              ),
            ),
          ],
          _title(L('choose_branch'),
              action: TextButton(
                onPressed: () => Navigator.push(context, MaterialPageRoute(builder: (_) => const BranchesScreen())),
                child: Text('${L('view_all')} (${branches.length}) →',
                    style: const TextStyle(fontWeight: FontWeight.w800)),
              )),
          SliverPadding(
            padding: const EdgeInsets.symmetric(horizontal: 14),
            sliver: SliverGrid.count(
              crossAxisCount: 2,
              mainAxisSpacing: 10,
              crossAxisSpacing: 10,
              childAspectRatio: 1.45,
              children: [for (final b in branches.take(6)) BranchTile(branch: b)],
            ),
          ),
          SliverToBoxAdapter(
            child: Padding(
              padding: const EdgeInsets.fromLTRB(14, 10, 14, 0),
              child: OutlinedButton.icon(
                style: OutlinedButton.styleFrom(
                    foregroundColor: C.p,
                    side: const BorderSide(color: C.p, width: 1.4),
                    padding: const EdgeInsets.symmetric(vertical: 12),
                    shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12))),
                onPressed: () => Navigator.push(context, MaterialPageRoute(builder: (_) => const BranchesScreen())),
                icon: const Icon(Icons.grid_view_rounded),
                label: Text(L('all_branches'), style: const TextStyle(fontWeight: FontWeight.w800)),
              ),
            ),
          ),
          _title(L('ready_to_study')),
          SliverPadding(
            padding: const EdgeInsets.symmetric(horizontal: 14),
            sliver: SliverList.list(children: [
              for (final m in ready)
                SubjectCard(
                  meta: m,
                  subtitle: () {
                    final w = repo.whereIs(m['code'] as String);
                    return w == null ? m['code'] as String : '${m['code']} · ${L('sem')} ${w.$2} · ${tr(w.$1['name'])}';
                  }(),
                ),
            ]),
          ),
          SliverToBoxAdapter(
            child: Padding(
              padding: const EdgeInsets.fromLTRB(16, 6, 16, 24),
              child: Text('${L('syllabus_note')} ${AppInfo.syllabus}',
                  textAlign: TextAlign.center, style: const TextStyle(fontSize: 12, color: C.muted)),
            ),
          ),
        ],
      ),
    );
  }
  Widget _title(String t, {Widget? action}) => SliverToBoxAdapter(
        child: Padding(
          padding: EdgeInsets.fromLTRB(16, 20, 8, action == null ? 10 : 2),
          child: Row(children: [
            Expanded(child: Text(t, style: const TextStyle(fontSize: 18, fontWeight: FontWeight.w800, color: C.ink))),
            if (action != null) action,
          ]),
        ),
      );

  Widget _hero(BuildContext context, int nBranches, int nReady) {
    final top = MediaQuery.of(context).padding.top;
    return Container(
      padding: EdgeInsets.fromLTRB(18, top + 14, 18, 20),
      decoration: const BoxDecoration(
        gradient: C.heroGradient,
        borderRadius: BorderRadius.vertical(bottom: Radius.circular(28)),
      ),
      child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
        Row(children: [
          const BrandMark(size: 42),
          const SizedBox(width: 12),
          const Expanded(child: BrandName(fontSize: 23)),
          IconButton(
            tooltip: L('refresh_content'),
            onPressed: _refreshing ? null : _refresh,
            icon: const Icon(Icons.refresh, color: Colors.white),
          ),
          const LangButton(),
        ]),
        const SizedBox(height: 10),
        Text(L('tagline'), style: const TextStyle(color: Color(0xE6FFFFFF), fontSize: 13.5)),
        const SizedBox(height: 16),
        Material(
          color: Colors.white,
          borderRadius: BorderRadius.circular(28),
          child: InkWell(
            borderRadius: BorderRadius.circular(28),
            onTap: () => Navigator.push(context, MaterialPageRoute(builder: (_) => const SearchScreen())),
            child: Padding(
              padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 13),
              child: Row(children: [
                const Icon(Icons.search_rounded, color: C.muted),
                const SizedBox(width: 10),
                Expanded(child: Text(L('search'), style: const TextStyle(color: C.muted, fontSize: 15))),
              ]),
            ),
          ),
        ),
        const SizedBox(height: 16),
        Row(children: [
          _stat('$nBranches', L('branches'), Icons.account_tree_rounded),
          const SizedBox(width: 8),
          _stat('6', L('semesters'), Icons.calendar_month_rounded),
          const SizedBox(width: 8),
          _stat('$nReady', L('ready_subjects'), Icons.menu_book_rounded),
        ]),
      ]),
    );
  }

  Widget _stat(String n, String label, IconData ic) => Expanded(
        child: Container(
          padding: const EdgeInsets.symmetric(vertical: 10, horizontal: 10),
          decoration: BoxDecoration(color: const Color(0x2EFFFFFF), borderRadius: BorderRadius.circular(14)),
          child: Row(children: [
            Icon(ic, color: Colors.white, size: 20),
            const SizedBox(width: 8),
            Expanded(
              child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
                Text(n, style: const TextStyle(color: Colors.white, fontSize: 17, fontWeight: FontWeight.w800)),
                Text(label,
                    maxLines: 1,
                    overflow: TextOverflow.ellipsis,
                    style: const TextStyle(color: Color(0xE6FFFFFF), fontSize: 11)),
              ]),
            ),
          ]),
        ),
      );

  Widget _recentCard(BuildContext context, RecentUnit r) => SizedBox(
        width: 240,
        child: Material(
          color: Colors.white,
          borderRadius: BorderRadius.circular(14),
          clipBehavior: Clip.antiAlias,
          child: InkWell(
            onTap: () => Navigator.push(
              context, MaterialPageRoute(builder: (_) => UnitScreen(code: r.code, unit: r.unit))),
            child: Padding(
              padding: const EdgeInsets.all(12),
              child: Row(children: [
                Container(
                  width: 6,
                  decoration: BoxDecoration(color: C.p, borderRadius: BorderRadius.circular(3)),
                ),
                const SizedBox(width: 10),
                Expanded(
                  child: Column(crossAxisAlignment: CrossAxisAlignment.start, mainAxisAlignment: MainAxisAlignment.center, children: [
                    Text('${L('unit')} ${r.unit}',
                        style: const TextStyle(color: C.p, fontWeight: FontWeight.w800, fontSize: 12.5)),
                    const SizedBox(height: 3),
                    Text(tr(r.unitTitle),
                        maxLines: 2,
                        overflow: TextOverflow.ellipsis,
                        style: const TextStyle(fontWeight: FontWeight.w700, fontSize: 14, height: 1.25)),
                    const SizedBox(height: 3),
                    Text(tr(r.subjectName),
                        maxLines: 1, overflow: TextOverflow.ellipsis, style: const TextStyle(fontSize: 11.5, color: C.muted)),
                  ]),
                ),
                const Icon(Icons.play_circle_fill_rounded, color: C.p, size: 30),
              ]),
            ),
          ),
        ),
      );
}
