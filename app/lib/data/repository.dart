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
  OnlineSource({
    this.base = kContentBase,
    Future<http.Response> Function(Uri)? get,
    Future<String?> Function(String)? readCache,
    Future<void> Function(String, String)? writeCache,
    Future<String?> Function(String)? loadAsset,
  })  : _request = get ?? http.get,
        _readCache = readCache ?? cacheRead,
        _writeCache = writeCache ?? cacheWrite,
        _loadAsset = loadAsset;

  final String base;
  final Future<http.Response> Function(Uri) _request;
  final Future<String?> Function(String) _readCache;
  final Future<void> Function(String, String) _writeCache;
  final Future<String?> Function(String)? _loadAsset;
  Map<String, dynamic> _files = {}; // path -> version hash (from catalog)

  Future<String?> _get(String url, {Duration timeout = const Duration(seconds: 10)}) async {
    try {
      final r = await _request(Uri.parse(url)).timeout(timeout);
      if (r.statusCode == 200) return utf8.decode(r.bodyBytes);
    } catch (_) {/* offline / timeout */}
    return null;
  }

  Future<String?> _asset(String path) async {
    try {
      final loader = _loadAsset;
      if (loader != null) return await loader(path);
      return await rootBundle.loadString('assets/content/$path');
    } catch (_) {
      return null;
    }
  }

  Map<String, dynamic>? _decode(String? text, bool Function(Map<String, dynamic>) valid) {
    if (text == null) return null;
    try {
      final data = jsonDecode(text);
      if (data is Map<String, dynamic> && valid(data)) return data;
    } catch (_) {/* invalid data: try another source */}
    return null;
  }

  bool _validCatalog(Map<String, dynamic> c) =>
      c['branches'] is List && c['subjects'] is Map && (c['files'] == null || c['files'] is Map);

  @override
  Future<Map<String, dynamic>> catalog() async {
    // minute-based query defeats stale CDN copies but still allows short caching
    final stamp = DateTime.now().millisecondsSinceEpoch ~/ 60000;
    final text = await _get('$base/catalog.json?t=$stamp', timeout: const Duration(seconds: 7));
    var c = _decode(text, _validCatalog);
    if (c != null) {
      await _writeCache('catalog.json', text!);
    } else {
      c = _decode(await _readCache('catalog.json'), _validCatalog) ??
          _decode(await _asset('catalog.json'), _validCatalog);
    }
    if (c == null) throw Exception('catalog unavailable');
    _files = (c['files'] as Map?)?.cast<String, dynamic>() ?? {};
    return c;
  }

  Future<Map<String, dynamic>> _file(String path, bool Function(Map<String, dynamic>) valid) async {
    final hash = _files[path] is String ? _files[path] as String : null;
    final key = path.replaceAll('/', '__');
    if (hash != null) {
      final cached = _decode(await _readCache('$key.$hash'), valid);
      if (cached != null) return cached;
    }
    final net = await _get('$base/$path${hash != null ? '?h=$hash' : ''}');
    final downloaded = _decode(net, valid);
    if (downloaded != null) {
      final text = net!;
      await _writeCache('$key.${hash ?? 'latest'}', text);
      await _writeCache('$key.last', text);
      return downloaded;
    }
    final fallback = _decode(await _readCache('$key.last'), valid) ??
        _decode(await _asset(path), valid);
    if (fallback == null) throw Exception('$path unavailable offline');
    return fallback;
  }

  @override
  Future<Map<String, dynamic>> subject(String code) => _file(
      'subjects/$code.json', (s) => s['code'] == code && s['name'] is Map && s['units'] is List);
  @override
  Future<Map<String, dynamic>> unit(String code, int no) => _file(
      'units/${code}_u$no.json', (u) => u['subject'] == code && u['unit'] == no && u['title'] is Map);
}

/// Cached access used by all screens.
class Repo {
  Repo(this.source);
  final ContentSource source;

  Map<String, dynamic>? _catalog;
  Future<Map<String, dynamic>>? _catalogLoading;

  Future<Map<String, dynamic>> catalog() async {
    if (_catalog != null) return _catalog!;
    return refresh();
  }

  /// Fetch the catalog again; on failure the previous in-memory copy is retained.
  Future<Map<String, dynamic>> refresh() async {
    final loading = _catalogLoading ??= source.catalog();
    try {
      return _catalog = await loading;
    } finally {
      if (identical(_catalogLoading, loading)) _catalogLoading = null;
    }
  }

  Future<Map<String, dynamic>> subject(String code) async {
    await catalog();
    return source.subject(code);
  }

  Future<Map<String, dynamic>> unit(String code, int no) async {
    await catalog();
    return source.unit(code, no);
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
