import 'package:flutter/material.dart';

import '../l10n.dart';
import '../state.dart';
import '../theme.dart';

/// Lavender section strip with optional ⋮ menu (Expand all / Collapse all) – as in the screenshot.
class SectionHeader extends StatelessWidget {
  const SectionHeader(this.title, {super.key, this.onExpand, this.onCollapse});
  final String title;
  final VoidCallback? onExpand, onCollapse;

  @override
  Widget build(BuildContext context) {
    return Container(
      color: C.lav,
      margin: const EdgeInsets.only(bottom: 8),
      padding: EdgeInsets.fromLTRB(18, onExpand == null ? 14 : 4, 4, onExpand == null ? 14 : 4),
      child: Row(children: [
        Expanded(
            child: Text(title,
                style: const TextStyle(fontSize: 17, fontWeight: FontWeight.w800, color: C.ink))),
        if (onExpand != null)
          PopupMenuButton<int>(
            icon: const Icon(Icons.more_vert, color: Color(0xFF222222)),
            onSelected: (v) => v == 1 ? onExpand!() : onCollapse!(),
            itemBuilder: (_) => [
              PopupMenuItem(value: 1, child: Text(L('expand'))),
              PopupMenuItem(value: 2, child: Text(L('collapse'))),
            ],
          ),
      ]),
    );
  }
}

/// White rounded card: purple numbered title + chevron; tap reveals the answer.
/// The body is built only when open (keeps long units fast).
class ExpandCard extends StatelessWidget {
  const ExpandCard({
    super.key,
    required this.open,
    required this.onTap,
    required this.title,
    required this.body,
    this.number,
    this.heading = false,
    this.keyPoints = false,
    this.trailing,
    this.bodyPadding,
  });
  final bool open, heading, keyPoints;
  final VoidCallback? onTap;
  final Widget title;
  final WidgetBuilder? body;
  final String? number;
  final Widget? trailing;
  final EdgeInsets? bodyPadding;

  @override
  Widget build(BuildContext context) {
    final color = keyPoints ? const Color(0xFF1B5E20) : C.p;
    return Container(
      margin: const EdgeInsets.fromLTRB(0, 0, 0, 8),
      decoration: BoxDecoration(
        color: Colors.white,
        borderRadius: BorderRadius.circular(6),
        border: keyPoints ? const Border(left: BorderSide(color: C.green, width: 4)) : null,
        boxShadow: const [BoxShadow(color: Color(0x243C146E), blurRadius: 3, offset: Offset(0, 1))],
      ),
      child: Column(crossAxisAlignment: CrossAxisAlignment.stretch, children: [
        InkWell(
          onTap: onTap,
          child: Padding(
            padding: const EdgeInsets.fromLTRB(18, 15, 12, 15),
            child: Row(crossAxisAlignment: CrossAxisAlignment.start, children: [
              if (number != null)
                SizedBox(
                    width: 30,
                    child: Text(number!,
                        style: TextStyle(color: color, fontSize: 16.5, height: 1.45,
                            fontWeight: heading ? FontWeight.w700 : FontWeight.w500))),
              Expanded(
                child: DefaultTextStyle.merge(
                  style: TextStyle(color: color, fontSize: 16.5, height: 1.45,
                      fontWeight: heading ? FontWeight.w700 : FontWeight.w500),
                  child: title,
                ),
              ),
              if (trailing != null) trailing!,
              if (body != null)
                AnimatedRotation(
                  turns: open ? 0.5 : 0,
                  duration: const Duration(milliseconds: 200),
                  child: Icon(Icons.keyboard_arrow_down_rounded, color: color, size: 28),
                ),
            ]),
          ),
        ),
        if (body != null)
          AnimatedSize(
            duration: const Duration(milliseconds: 180),
            alignment: Alignment.topCenter,
            child: open
                ? Padding(
                    padding: bodyPadding ?? EdgeInsets.fromLTRB(number != null ? 48 : 18, 0, 16, 16),
                    child: body!(context))
                : const SizedBox(width: double.infinity),
          ),
      ]),
    );
  }
}

/// EN / ગુ toggle button for app bars.
class LangButton extends StatelessWidget {
  const LangButton({super.key, this.light = true});
  final bool light;
  @override
  Widget build(BuildContext context) {
    return ListenableBuilder(
      listenable: app,
      builder: (_, __) => Padding(
        padding: const EdgeInsets.only(right: 8),
        child: Material(
          color: light ? const Color(0x2EFFFFFF) : C.lav,
          shape: const StadiumBorder(),
          child: InkWell(
            customBorder: const StadiumBorder(),
            onTap: app.toggleLang,
            child: Padding(
              padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 6),
              child: Row(mainAxisSize: MainAxisSize.min, children: [
                Icon(Icons.translate_rounded, size: 16, color: light ? Colors.white : C.p),
                const SizedBox(width: 5),
                Text(app.lang == 'en' ? 'ગુ' : 'EN',
                    style: TextStyle(
                        fontWeight: FontWeight.w800, fontSize: 14, color: light ? Colors.white : C.p)),
              ]),
            ),
          ),
        ),
      ),
    );
  }
}

/// Material icon for a branch icon key (from catalog.json).
IconData branchIcon(String? k) => switch (k) {
      'computer' => Icons.computer_rounded,
      'lan' => Icons.lan_rounded,
      'terminal' => Icons.terminal_rounded,
      'wifi' => Icons.wifi_rounded,
      'settings' => Icons.settings_rounded,
      'apartment' => Icons.apartment_rounded,
      'bolt' => Icons.bolt_rounded,
      'antenna' => Icons.settings_input_antenna_rounded,
      'car' => Icons.directions_car_rounded,
      'science' => Icons.science_rounded,
      'flight' => Icons.flight_rounded,
      'heart' => Icons.monitor_heart_rounded,
      'eco' => Icons.eco_rounded,
      'speed' => Icons.speed_rounded,
      'boat' => Icons.directions_boat_rounded,
      'robot' => Icons.smart_toy_rounded,
      'hardware' => Icons.hardware_rounded,
      'landscape' => Icons.landscape_rounded,
      'category' => Icons.category_rounded,
      'power' => Icons.electrical_services_rounded,
      'textile' => Icons.checkroom_rounded,
      'factory' => Icons.factory_rounded,
      'print' => Icons.print_rounded,
      'bus' => Icons.directions_bus_rounded,
      'fire' => Icons.local_fire_department_rounded,
      _ => Icons.school_rounded,
    };

IconData subjectTypeIcon(String? t) => switch (t) {
      'programming' => Icons.code_rounded,
      'practical' => Icons.handyman_rounded,
      _ => Icons.menu_book_rounded,
    };

class Pill extends StatelessWidget {
  const Pill(this.text, {super.key, this.bg = C.lav, this.fg = C.pd, this.icon});
  final String text;
  final Color bg, fg;
  final IconData? icon;
  @override
  Widget build(BuildContext context) => Container(
        padding: const EdgeInsets.symmetric(horizontal: 9, vertical: 3),
        decoration: BoxDecoration(color: bg, borderRadius: BorderRadius.circular(12)),
        child: Row(mainAxisSize: MainAxisSize.min, children: [
          if (icon != null) ...[Icon(icon, size: 13, color: fg), const SizedBox(width: 4)],
          Text(text, style: TextStyle(fontSize: 12, fontWeight: FontWeight.w800, color: fg)),
        ]),
      );
}

/// Loads a future and shows a spinner / error with retry.
class Loader<T> extends StatefulWidget {
  const Loader({super.key, required this.load, required this.builder});
  final Future<T> Function() load;
  final Widget Function(BuildContext, T) builder;
  @override
  State<Loader<T>> createState() => _LoaderState<T>();
}

class _LoaderState<T> extends State<Loader<T>> {
  late Future<T> _f = widget.load();
  @override
  Widget build(BuildContext context) => FutureBuilder<T>(
        future: _f,
        builder: (context, s) {
          if (s.hasError) {
            return Center(
              child: Padding(
                padding: const EdgeInsets.all(24),
                child: Column(mainAxisSize: MainAxisSize.min, children: [
                  const Icon(Icons.cloud_off_rounded, size: 48, color: C.muted),
                  const SizedBox(height: 10),
                  Text(L('load_error'), textAlign: TextAlign.center),
                  const SizedBox(height: 10),
                  FilledButton(onPressed: () => setState(() => _f = widget.load()), child: Text(L('retry'))),
                ]),
              ),
            );
          }
          if (!s.hasData) return const Center(child: CircularProgressIndicator());
          return widget.builder(context, s.data as T);
        },
      );
}


/// DiplomaOne logo: white rounded tile with a purple "D" and gold "1".
class BrandMark extends StatelessWidget {
  const BrandMark({super.key, this.size = 42});
  final double size;
  @override
  Widget build(BuildContext context) => Container(
        width: size,
        height: size,
        alignment: Alignment.center,
        decoration: BoxDecoration(
          color: Colors.white,
          borderRadius: BorderRadius.circular(size * 0.3),
          boxShadow: const [BoxShadow(color: Color(0x33000000), blurRadius: 6, offset: Offset(0, 2))],
        ),
        child: Text.rich(TextSpan(children: [
          TextSpan(text: 'D', style: TextStyle(color: C.p, fontSize: size * 0.55, fontWeight: FontWeight.w900, height: 1)),
          TextSpan(text: '1', style: TextStyle(color: const Color(0xFFF2A900), fontSize: size * 0.42, fontWeight: FontWeight.w900, height: 1)),
        ])),
      );
}

/// "Diploma" + gold "One".
class BrandName extends StatelessWidget {
  const BrandName({super.key, this.fontSize = 22});
  final double fontSize;
  @override
  Widget build(BuildContext context) => Text.rich(TextSpan(children: [
        TextSpan(text: 'Diploma', style: TextStyle(color: Colors.white, fontSize: fontSize, fontWeight: FontWeight.w800)),
        TextSpan(text: 'One', style: TextStyle(color: const Color(0xFFFFD54F), fontSize: fontSize, fontWeight: FontWeight.w900)),
      ]));
}
