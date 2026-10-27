import 'package:flutter/material.dart';

import 'ad_config.dart';

Future<void> initAds() async {}

class AdBanner extends StatelessWidget {
  const AdBanner({super.key});
  @override
  Widget build(BuildContext context) {
    if (!AdConfig.showWebPlaceholder) return const SizedBox.shrink();
    return Container(
      height: 52,
      decoration: const BoxDecoration(
          color: Colors.white, border: Border(top: BorderSide(color: Color(0xFFE3D8F0)))),
      alignment: Alignment.center,
      child: Row(mainAxisSize: MainAxisSize.min, children: [
        Container(
          padding: const EdgeInsets.symmetric(horizontal: 5, vertical: 1),
          decoration: BoxDecoration(color: const Color(0xFFF2C94C), borderRadius: BorderRadius.circular(3)),
          child: const Text('AD', style: TextStyle(fontSize: 10.5, fontWeight: FontWeight.w800, color: Color(0xFF5B4300))),
        ),
        const SizedBox(width: 8),
        const Text('AdMob banner space', style: TextStyle(fontSize: 12.5, color: Color(0xFF8B8199))),
      ]),
    );
  }
}
