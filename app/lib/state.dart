import 'dart:convert';

import 'package:flutter/foundation.dart';
import 'package:shared_preferences/shared_preferences.dart';

/// A recently opened unit (for "Continue reading").
class RecentUnit {
  final String code;
  final int unit;
  final Map<String, dynamic> unitTitle;
  final Map<String, dynamic> subjectName;
  RecentUnit(this.code, this.unit, this.unitTitle, this.subjectName);

  Map<String, dynamic> toJson() => {'code': code, 'unit': unit, 'ut': unitTitle, 'sn': subjectName};
  static RecentUnit fromJson(Map<String, dynamic> j) => RecentUnit(
      j['code'] as String, j['unit'] as int,
      Map<String, dynamic>.from(j['ut'] as Map), Map<String, dynamic>.from(j['sn'] as Map));
}

/// Global app state: UI language + recently opened units. Saved on the device.
class AppState extends ChangeNotifier {
  String lang = 'en';
  List<RecentUnit> recent = [];
  SharedPreferences? _p;

  Future<void> load() async {
    try {
      _p = await SharedPreferences.getInstance();
      lang = _p!.getString('lang') ?? 'en';
      final r = _p!.getString('recent');
      if (r != null) {
        recent = (jsonDecode(r) as List).map((e) => RecentUnit.fromJson(Map<String, dynamic>.from(e))).toList();
      }
    } catch (_) {/* first run / storage unavailable */}
  }

  void toggleLang() {
    lang = lang == 'en' ? 'gu' : 'en';
    _p?.setString('lang', lang);
    notifyListeners();
  }

  void addRecent(RecentUnit u) {
    recent.removeWhere((e) => e.code == u.code && e.unit == u.unit);
    recent.insert(0, u);
    if (recent.length > 6) recent = recent.sublist(0, 6);
    _p?.setString('recent', jsonEncode(recent.map((e) => e.toJson()).toList()));
    notifyListeners();
  }
}

final app = AppState();
