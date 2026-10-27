final _mem = <String, String>{};

Future<String?> cacheRead(String key) async => _mem[key];
Future<void> cacheWrite(String key, String value) async => _mem[key] = value;
