import 'package:flutter/material.dart';

import 'ads/ad_banner.dart';
import 'screens/home_screen.dart';
import 'state.dart';
import 'theme.dart';

Future<void> main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await app.load();
  initAds(); // AdMob on Android; no-op on web
  runApp(const DiplomaApp());
}

class DiplomaApp extends StatelessWidget {
  const DiplomaApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: AppInfo.name,
      debugShowCheckedModeBanner: false,
      theme: buildTheme(),
      // On wide screens (web on desktop) keep a phone-like column in the centre.
      builder: (context, child) => ColoredBox(
        color: const Color(0xFFD8CCE8),
        child: Center(
          child: ConstrainedBox(
            constraints: const BoxConstraints(maxWidth: 560),
            child: ClipRect(child: child),
          ),
        ),
      ),
      home: const HomeScreen(),
    );
  }
}
