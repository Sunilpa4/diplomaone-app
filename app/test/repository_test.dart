import 'dart:convert';

import 'package:diploma_one/data/repository.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:http/http.dart' as http;

void main() {
  const code = 'TEST';
  const path = 'units/TEST_u1.json';
  final oldUnit = jsonEncode({'subject': code, 'unit': 1, 'title': {'en': 'Old'}});
  final newUnit = jsonEncode({'subject': code, 'unit': 1, 'title': {'en': 'New'}});
  String catalog(String hash) => jsonEncode({
        'branches': [],
        'subjects': {},
        'files': {path: hash},
      });

  test('invalid catalog and unit responses keep valid cached fallbacks', () async {
    final cache = <String, String>{
      'catalog.json': catalog('v2'),
      'units__TEST_u1.json.v2': '{broken',
      'units__TEST_u1.json.last': oldUnit,
    };
    final source = OnlineSource(
      base: 'https://example.test',
      get: (_) async => http.Response('not json', 200),
      readCache: (key) async => cache[key],
      writeCache: (key, value) async { cache[key] = value; },
      loadAsset: (_) async => null,
    );

    await source.catalog();
    expect((await source.unit(code, 1))['title']['en'], 'Old');
    expect(cache['catalog.json'], catalog('v2'));
    expect(cache['units__TEST_u1.json.last'], oldUnit);
    expect(cache['units__TEST_u1.json.v2'], '{broken');
  });

  test('invalid caches fall through to assets', () async {
    final source = OnlineSource(
      base: 'https://example.test',
      get: (_) async => http.Response('', 503),
      readCache: (_) async => '[]',
      writeCache: (_, __) async {},
      loadAsset: (key) async => key == 'catalog.json' ? catalog('v1') : oldUnit,
    );
    await source.catalog();
    expect((await source.unit(code, 1))['title']['en'], 'Old');
  });

  test('refresh and reopening a unit recover after going back online', () async {
    var online = false;
    final cache = <String, String>{
      'catalog.json': catalog('v1'),
      'units__TEST_u1.json.last': oldUnit,
    };
    final source = OnlineSource(
      base: 'https://example.test',
      get: (uri) async {
        if (!online) return http.Response('', 503);
        return http.Response(uri.path.endsWith('catalog.json') ? catalog('v2') : newUnit, 200);
      },
      readCache: (key) async => cache[key],
      writeCache: (key, value) async { cache[key] = value; },
      loadAsset: (_) async => null,
    );
    final repo = Repo(source);
    expect((await repo.unit(code, 1))['title']['en'], 'Old');
    online = true;
    await repo.refresh();
    expect((await repo.unit(code, 1))['title']['en'], 'New');
    expect(cache['units__TEST_u1.json.v2'], newUnit);
  });

  test('failed refresh retains the current catalog and can be retried', () async {
    final source = _CatalogSource();
    final repo = Repo(source);
    await repo.catalog();
    source.fail = true;
    await expectLater(repo.refresh(), throwsException);
    expect(repo.branches(), hasLength(1));
    source.fail = false;
    source.version = 2;
    await repo.refresh();
    expect(repo.branches().first['version'], 2);
  });
}

class _CatalogSource implements ContentSource {
  bool fail = false;
  int version = 1;

  @override
  Future<Map<String, dynamic>> catalog() async {
    if (fail) throw Exception('offline');
    return {'branches': [{'version': version}], 'subjects': <String, dynamic>{}};
  }

  @override
  Future<Map<String, dynamic>> subject(String code) => throw UnimplementedError();

  @override
  Future<Map<String, dynamic>> unit(String code, int no) => throw UnimplementedError();
}
