import 'dart:async';
import 'dart:convert';

import 'package:flutter/services.dart' show rootBundle;
import 'package:http/http.dart' as http;

import 'cache.dart';

/// Where the notes live online (GitHub Pages of the public "diplomaone-content" repo).
/// New / updated notes appear in the app automatically – no app update needed.
const kContentBase = 'https://sunilpa4.github.io/diplomaone-content/data';

abstract class ContentSource {
  Future<Map<String, dynamic>> catalog();
  Future<Map<String, dynamic>> subject(String code);
  Future<Map<String, dynamic>> unit(String code, int no);
}

/// Online source with an on-device cache and a bundled fallback:
///   catalog  : network (fresh) → last cached copy → copy bundled in the app
///   files    : cached copy with the same version hash → network → any cached copy → bundled
class OnlineSource implements ContentSource {
  OnlineSource({this.base = kContentBase});
  final String base;
  Map<String, dynamic> _files = {}; // path -> version hash (from catalog)

  Future<String?> _get(String url, {Duration timeout = const Duration(seconds: 10)}) async {
    try {
      final r = await http.get(Uri.parse(url)).timeout(timeout);
      if (r.statusCode == 200) return utf8.decode(r.bodyBytes);
    } catch (_) {/* offline / timeout */}
    return null;
  }

  Future<String?> _asset(String path) async {
    try {
      return await rootBundle.loadString('assets/content/$path');
    } catch (_) {
      return null;
    }
  }

  @override
  Future<Map<String, dynamic>> catalog() async {
    // minute-based query defeats stale CDN copies but still allows short caching
    final stamp = DateTime.now().millisecondsSinceEpoch ~/ 60000;
    var text = await _get('$base/catalog.json?t=$stamp', timeout: const Duration(seconds: 7));
    if (text != null) {
      await cacheWrite('catalog.json', text);
    } else {
      text = await cacheRead('catalog.json') ?? await _asset('catalog.json');
    }
    if (text == null) throw Exception('catalog unavailable');
    final c = jsonDecode(text) as Map<String, dynamic>;
    _files = (c['files'] as Map?)?.cast<String, dynamic>() ?? {};
    return c;
  }

  Future<Map<String, dynamic>> _file(String path) async {
    final hash = _files[path] as String?;
    final key = path.replaceAll('/', '__');
    if (hash != null) {
      final cached = await cacheRead('$key.$hash');
      if (cached != null) return jsonDecode(cached) as Map<String, dynamic>;
    }
    final net = await _get('$base/$path${hash != null ? '?h=$hash' : ''}');
    if (net != null) {
      await cacheWrite('$key.${hash ?? 'latest'}', net);
      await cacheWrite('$key.last', net);
      return jsonDecode(net) as Map<String, dynamic>;
    }
    final any = await cacheRead('$key.last') ?? await _asset(path);
    if (any == null) throw Exception('$path unavailable offline');
    return jsonDecode(any) as Map<String, dynamic>;
  }

  @override
  Future<Map<String, dynamic>> subject(String code) => _file('subjects/$code.json');
  @override
  Future<Map<String, dynamic>> unit(String code, int no) => _file('units/${code}_u$no.json');
}

/// Cached access used by all screens.
class Repo {
  Repo(this.source);
  final ContentSource source;

  Map<String, dynamic>? _catalog;
  Future<Map<String, dynamic>>? _catalogLoading;
  final _subjects = <String, Map<String, dynamic>>{};
  final _units = <String, Map<String, dynamic>>{};

  Future<Map<String, dynamic>> catalog() async {
    if (_catalog != null) return _catalog!;
    _catalogLoading ??= source.catalog();
    try {
      return _catalog = await _catalogLoading!;
    } catch (e) {
      _catalogLoading = null; // allow retry
      rethrow;
    }
  }

  Future<Map<String, dynamic>> subject(String code) async {
    await catalog();
    return _subjects[code] ??= await source.subject(code);
  }

  Future<Map<String, dynamic>> unit(String code, int no) async {
    await catalog();
    return _units['${code}_$no'] ??= await source.unit(code, no);
  }

  // ---- helpers over the catalog ----
  List<Map<String, dynamic>> branches() =>
      ((_catalog?['branches'] as List?) ?? []).cast<Map<String, dynamic>>();

  Map<String, dynamic>? subjectMeta(String code) =>
      (_catalog?['subjects'] as Map?)?[code] as Map<String, dynamic>?;

  List<Map<String, dynamic>> subjectsOf(Map<String, dynamic> branch, int sem) {
    final codes = ((branch['semesters'] as Map)['$sem'] as List?) ?? [];
    return codes.map((c) => subjectMeta(c as String)).whereType<Map<String, dynamic>>().toList();
  }

  int readyCount(Map<String, dynamic> branch, [int? sem]) {
    final sems = sem == null ? [1, 2, 3, 4, 5, 6] : [sem];
    var n = 0;
    for (final s in sems) {
      n += subjectsOf(branch, s).where((m) => m['status'] == 'available').length;
    }
    return n;
  }

  /// Branch + semester in which a subject appears first (for search results).
  (Map<String, dynamic>, int)? whereIs(String code) {
    for (final b in branches()) {
      for (var s = 1; s <= 6; s++) {
        if ((((b['semesters'] as Map)['$s'] as List?) ?? []).contains(code)) return (b, s);
      }
    }
    return null;
  }

  List<Map<String, dynamic>> allSubjects() =>
      ((_catalog?['subjects'] as Map?)?.values ?? []).cast<Map<String, dynamic>>().toList();
}

final repo = Repo(OnlineSource());
