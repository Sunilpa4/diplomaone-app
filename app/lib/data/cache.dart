// Device cache for downloaded notes: files on Android, memory-only on web
// (on web the browser's HTTP cache does the job).
export 'cache_web.dart' if (dart.library.io) 'cache_io.dart';
