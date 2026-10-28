import 'package:flutter/material.dart';
import 'package:flutter/services.dart';

import '../l10n.dart';
import '../theme.dart';
import 'html_frame.dart';

/// Live preview for HTML / Bootstrap / jQuery programs.
/// CDN <link>/<script> tags are replaced by copies bundled in assets/web, so pages work offline.
class WebAssets {
  static Future<Map<String, String>>? _f;

  static Future<Map<String, String>> load() => _f ??= () async {
        const names = ['bootstrap.min.css', 'bootstrap.bundle.min.js', 'jquery.min.js', 'bootstrap-icons.min.css', 'shell.js'];
        final m = <String, String>{};
        for (final n in names) {
          m[n] = await rootBundle.loadString('assets/web/$n');
        }
        return m;
      }();
}

final _reLinkIcons = RegExp(r'''<link\b[^>]*href\s*=\s*["'][^"']*bootstrap-icons[^"']*\.css[^"']*["'][^>]*>''', caseSensitive: false);
final _reLinkBs = RegExp(r'''<link\b[^>]*href\s*=\s*["'][^"']*/bootstrap(?:\.min)?\.css[^"']*["'][^>]*>''', caseSensitive: false);
final _reScriptBs = RegExp(r'''<script\b[^>]*src\s*=\s*["'][^"']*/bootstrap(?:\.bundle)?(?:\.min)?\.js[^"']*["'][^>]*>\s*</script>''', caseSensitive: false);
final _reScriptJq = RegExp(r'''<script\b[^>]*src\s*=\s*["'][^"']*/jquery[^"'/]*\.js[^"']*["'][^>]*>\s*</script>''', caseSensitive: false);
final _reHead = RegExp(r'<head\b[^>]*>', caseSensitive: false);
final _reViewport = RegExp(r'width\s*=\s*device-width', caseSensitive: false);

/// Builds the self-contained page that is shown in the preview.
String buildPreviewHtml(String code, Map<String, String> a, {bool desktop = false}) {
  var h = code;
  h = h.replaceAllMapped(_reLinkIcons, (_) => '<style>${a['bootstrap-icons.min.css']}</style>');
  h = h.replaceAllMapped(_reLinkBs, (_) => '<style>${a['bootstrap.min.css']}</style>');
  h = h.replaceAllMapped(_reScriptJq, (_) => '<script>${a['jquery.min.js']}</script>');
  h = h.replaceAllMapped(_reScriptBs, (_) => '<script>${a['bootstrap.bundle.min.js']}</script>');
  if (desktop) h = h.replaceFirst(_reViewport, 'width=1100');
  final shell = '<script>${a['shell.js']}</script>';
  final m = _reHead.firstMatch(h);
  h = m != null ? h.replaceRange(m.end, m.end, shell) : shell + h;
  return h;
}

/// "Run" button shown under the code of a web program.
class RunButton extends StatelessWidget {
  const RunButton({super.key, required this.code, required this.title});
  final String code, title;

  @override
  Widget build(BuildContext context) => Padding(
        padding: const EdgeInsets.only(bottom: 10),
        child: Align(
          alignment: Alignment.centerLeft,
          child: FilledButton.icon(
            style: FilledButton.styleFrom(backgroundColor: C.green, visualDensity: VisualDensity.compact),
            icon: const Icon(Icons.play_arrow_rounded, size: 20),
            label: Text(L('run'), style: const TextStyle(fontWeight: FontWeight.w700)),
            onPressed: () => Navigator.push(
                context, MaterialPageRoute(builder: (_) => PreviewScreen(code: code, title: title))),
          ),
        ),
      );
}

class PreviewScreen extends StatefulWidget {
  const PreviewScreen({super.key, required this.code, required this.title});
  final String code, title;

  @override
  State<PreviewScreen> createState() => _PreviewScreenState();
}

class _PreviewScreenState extends State<PreviewScreen> {
  bool desktop = false;
  int run = 0;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.white,
      appBar: AppBar(
        backgroundColor: C.p,
        foregroundColor: Colors.white,
        titleSpacing: 0,
        title: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
          Text(L('preview'), style: const TextStyle(fontSize: 16, fontWeight: FontWeight.w800)),
          Text(widget.title,
              maxLines: 1, overflow: TextOverflow.ellipsis, style: const TextStyle(fontSize: 12, color: Color(0xE6FFFFFF))),
        ]),
        actions: [
          IconButton(
            tooltip: desktop ? L('phone_view') : L('desktop_view'),
            icon: Icon(desktop ? Icons.smartphone_rounded : Icons.desktop_windows_rounded),
            onPressed: () => setState(() => desktop = !desktop),
          ),
          IconButton(
            tooltip: L('rerun'),
            icon: const Icon(Icons.refresh_rounded),
            onPressed: () => setState(() => run++),
          ),
        ],
      ),
      body: FutureBuilder<Map<String, String>>(
        future: WebAssets.load(),
        builder: (context, snap) {
          if (!snap.hasData) return const Center(child: CircularProgressIndicator());
          final html = buildPreviewHtml(widget.code, snap.data!, desktop: desktop && !isWebFrame);
          return Column(children: [
            Container(
              width: double.infinity,
              color: C.lav,
              padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 5),
              child: Text(desktop ? L('desktop_note') : L('phone_note'),
                  style: const TextStyle(fontSize: 12, color: C.pd, fontWeight: FontWeight.w600)),
            ),
            Expanded(
              child: LayoutBuilder(builder: (context, box) {
                // On the web the frame width itself simulates the device; on Android the viewport does.
                final w = !isWebFrame ? box.maxWidth : (desktop ? box.maxWidth : (box.maxWidth < 420 ? box.maxWidth : 400.0));
                return Container(
                  color: isWebFrame && !desktop ? const Color(0xFFEDE7F6) : Colors.white,
                  alignment: Alignment.topCenter,
                  child: SizedBox(
                    width: w,
                    height: box.maxHeight,
                    child: HtmlFrame(key: ValueKey('$run-$desktop'), html: html),
                  ),
                );
              }),
            ),
          ]);
        },
      ),
    );
  }
}
