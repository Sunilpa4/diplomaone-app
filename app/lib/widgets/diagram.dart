import 'package:flutter/material.dart';
import 'package:flutter_svg/flutter_svg.dart';

import '../l10n.dart';
import '../theme.dart';


final _vb = RegExp(r'viewBox="\s*[-\d.]+[\s,]+[-\d.]+[\s,]+([\d.]+)[\s,]+([\d.]+)');
final _wh = RegExp(r'<svg[^>]*?\swidth="([\d.]+)[a-z]*"[^>]*?\sheight="([\d.]+)');
final _aspects = <int, double>{};

/// width / height of an SVG from its viewBox (fallback: width/height attributes).
double svgAspect(String svg) => _aspects.putIfAbsent(svg.hashCode, () {
      final m = _vb.firstMatch(svg) ?? _wh.firstMatch(svg);
      if (m == null) return 1.4;
      final w = double.tryParse(m.group(1)!) ?? 0, h = double.tryParse(m.group(2)!) ?? 0;
      return (w > 0 && h > 0) ? w / h : 1.4;
    });

/// SVG that takes the full width and the correct height (safe inside scroll views).
Widget svgBox(String svg) => AspectRatio(
      aspectRatio: svgAspect(svg),
      child: SvgPicture.string(svg, fit: BoxFit.contain),
    );

/// Inline diagram with caption; tap opens the zoom viewer.
class DiagramInline extends StatelessWidget {
  const DiagramInline({super.key, required this.svg, required this.title, this.caption = true});
  final String svg;
  final String title;
  final bool caption;

  @override
  Widget build(BuildContext context) {
    return Column(crossAxisAlignment: CrossAxisAlignment.stretch, children: [
      GestureDetector(
        onTap: () => openDiagram(context, svg, title),
        child: Container(
          margin: const EdgeInsets.only(top: 6, bottom: 4),
          decoration: BoxDecoration(
              color: Colors.white,
              border: Border.all(color: C.line),
              borderRadius: BorderRadius.circular(10)),
          clipBehavior: Clip.antiAlias,
          child: svgBox(svg),
        ),
      ),
      if (caption)
        Padding(
          padding: const EdgeInsets.only(bottom: 10),
          child: Text('📐 $title · ${L('tapzoom')}',
              textAlign: TextAlign.center, style: const TextStyle(fontSize: 12, color: C.muted)),
        ),
    ]);
  }
}

void openDiagram(BuildContext context, String svg, String title) {
  Navigator.of(context).push(PageRouteBuilder(
    opaque: false,
    barrierColor: const Color(0xEB140A23),
    pageBuilder: (_, __, ___) => DiagramViewer(svg: svg, title: title),
    transitionsBuilder: (_, a, __, child) => FadeTransition(opacity: a, child: child),
  ));
}

/// Full-screen pinch/zoom viewer.
class DiagramViewer extends StatefulWidget {
  const DiagramViewer({super.key, required this.svg, required this.title});
  final String svg, title;
  @override
  State<DiagramViewer> createState() => _DiagramViewerState();
}

class _DiagramViewerState extends State<DiagramViewer> {
  final _tc = TransformationController();
  double _z = 1;

  void _zoom(double z) {
    setState(() => _z = z.clamp(1.0, 5.0));
    _tc.value = Matrix4.identity()..scaleByDouble(_z, _z, 1, 1);
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.transparent,
      body: SafeArea(
        child: Column(children: [
          Padding(
            padding: const EdgeInsets.fromLTRB(16, 8, 8, 8),
            child: Row(children: [
              Expanded(
                  child: Text(widget.title,
                      style: const TextStyle(color: Colors.white, fontWeight: FontWeight.w700, fontSize: 16))),
              IconButton(
                  onPressed: () => Navigator.pop(context),
                  icon: const Icon(Icons.close_rounded, color: Colors.white)),
            ]),
          ),
          Expanded(
            child: InteractiveViewer(
              transformationController: _tc,
              minScale: 1,
              maxScale: 5,
              onInteractionEnd: (_) => setState(() => _z = _tc.value.getMaxScaleOnAxis()),
              child: Center(
                child: Container(
                  margin: const EdgeInsets.all(10),
                  decoration: BoxDecoration(color: Colors.white, borderRadius: BorderRadius.circular(8)),
                  clipBehavior: Clip.antiAlias,
                  child: svgBox(widget.svg),
                ),
              ),
            ),
          ),
          Padding(
            padding: const EdgeInsets.all(12),
            child: Row(mainAxisAlignment: MainAxisAlignment.center, children: [
              _zb('−', () => _zoom(_z - 0.5)),
              const SizedBox(width: 14),
              _zb('${(_z * 100).round()}%', () => _zoom(1)),
              const SizedBox(width: 14),
              _zb('+', () => _zoom(_z + 0.5)),
            ]),
          ),
        ]),
      ),
    );
  }

  Widget _zb(String t, VoidCallback f) => Material(
        color: Colors.white,
        shape: const StadiumBorder(),
        child: InkWell(
          customBorder: const StadiumBorder(),
          onTap: f,
          child: Padding(
            padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 8),
            child: Text(t, style: const TextStyle(fontSize: 18, fontWeight: FontWeight.w800, color: C.p)),
          ),
        ),
      );
}

/// Bare full-width SVG (used inside diagram cards).
class DiagramPicture extends StatelessWidget {
  const DiagramPicture({super.key, required this.svg});
  final String svg;
  @override
  Widget build(BuildContext context) => svgBox(svg);
}
