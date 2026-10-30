import 'package:diploma_one/widgets/common.dart';
import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';

void main() {
  testWidgets('standalone loader offers retry and a way back on failure', (tester) async {
    var attempts = 0;
    await tester.pumpWidget(MaterialApp(home: Builder(builder: (context) => Scaffold(
      body: TextButton(
        onPressed: () => Navigator.push(context, MaterialPageRoute(builder: (_) => Loader<String>(
          standalone: true,
          load: () async {
            attempts++;
            if (attempts == 1) throw Exception('offline');
            return 'loaded';
          },
          builder: (_, value) => Scaffold(body: Text(value)),
        ))),
        child: const Text('open'),
      ),
    ))));
    await tester.tap(find.text('open'));
    await tester.pumpAndSettle();
    expect(find.text('Could not load content. Please try again.'), findsOneWidget);
    expect(find.byTooltip('Back'), findsOneWidget);
    await tester.tap(find.text('Retry'));
    await tester.pumpAndSettle();
    expect(find.text('loaded'), findsOneWidget);
  });
}
