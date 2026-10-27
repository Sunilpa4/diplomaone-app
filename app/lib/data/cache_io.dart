import 'dart:io';

import 'package:path_provider/path_provider.dart';

Directory? _dir;

Future<Directory> _root() async {
  if (_dir != null) return _dir!;
  final base = await getApplicationSupportDirectory();
  _dir = Directory('${base.path}/content_cache');
  if (!await _dir!.exists()) await _dir!.create(recursive: true);
  return _dir!;
}

String _safe(String key) => key.replaceAll(RegExp(r'[^A-Za-z0-9_.-]'), '_');

Future<String?> cacheRead(String key) async {
  try {
    final f = File('${(await _root()).path}/${_safe(key)}');
    return await f.exists() ? await f.readAsString() : null;
  } catch (_) {
    return null;
  }
}

Future<void> cacheWrite(String key, String value) async {
  try {
    final f = File('${(await _root()).path}/${_safe(key)}');
    await f.writeAsString(value, flush: true);
  } catch (_) {/* storage full / unavailable: ignore */}
}
