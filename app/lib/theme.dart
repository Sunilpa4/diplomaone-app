import 'package:flutter/material.dart';

/// App name and colours in one place (easy to rebrand later).
class AppInfo {
  static const name = 'DiplomaOne';
  static const nameGu = 'DiplomaOne';
  static const syllabus = '2024-25';
}

class C {
  static const p = Color(0xFF7B2CD9); // app bar purple (from screenshot)
  static const pd = Color(0xFF6420B8);
  static const pdeep = Color(0xFF5B1BB0);
  static const lav = Color(0xFFEADDF7); // section header strip
  static const bg = Color(0xFFF3ECFA); // page background
  static const ink = Color(0xFF1D1B20);
  static const muted = Color(0xFF7A6F88);
  static const line = Color(0xFFEADFF6);
  static const codeBg = Color(0xFF1E1530);
  static const codeInk = Color(0xFFEDE7F6);
  static const outBg = Color(0xFF0E1B12);
  static const outInk = Color(0xFFB9F6CA);
  static const green = Color(0xFF2E7D32);
  static const gold = Color(0xFF9A5B00);
  static const goldBg = Color(0xFFFFF1D6);

  static const heroGradient = LinearGradient(
    colors: [Color(0xFF8E3BE8), Color(0xFF5B1BB0)],
    begin: Alignment.topLeft,
    end: Alignment.bottomRight,
  );

  static Color hex(String s) => Color(int.parse('FF${s.replaceFirst('#', '')}', radix: 16));
}

const kMono = 'DejaVu Sans Mono';

ThemeData buildTheme() {
  final base = ThemeData(
    useMaterial3: true,
    colorScheme: ColorScheme.fromSeed(seedColor: C.p, primary: C.p, surface: Colors.white),
    scaffoldBackgroundColor: C.bg,
  );
  return base.copyWith(
    appBarTheme: const AppBarTheme(
      backgroundColor: C.p,
      foregroundColor: Colors.white,
      elevation: 2,
      titleTextStyle: TextStyle(fontSize: 19, fontWeight: FontWeight.w700, color: Colors.white),
    ),
    tabBarTheme: const TabBarThemeData(
      labelColor: Colors.white,
      unselectedLabelColor: Color(0xDDFFFFFF),
      indicatorColor: Colors.white,
      indicatorSize: TabBarIndicatorSize.label,
      labelStyle: TextStyle(fontWeight: FontWeight.w800, fontSize: 15),
      unselectedLabelStyle: TextStyle(fontWeight: FontWeight.w600, fontSize: 15),
      dividerColor: Colors.transparent,
      tabAlignment: TabAlignment.start,
    ),
    snackBarTheme: const SnackBarThemeData(behavior: SnackBarBehavior.floating),
  );
}
