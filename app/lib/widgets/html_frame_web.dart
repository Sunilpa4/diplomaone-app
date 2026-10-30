import 'dart:js_interop';
import 'dart:js_interop_unsafe';

import 'package:flutter/widgets.dart';

const bool isWebFrame = true;

class HtmlFrame extends StatelessWidget {
  const HtmlFrame({super.key, required this.html});
  final String html;

  @override
  Widget build(BuildContext context) => HtmlElementView.fromTagName(
        key: ValueKey(html.hashCode),
        tagName: 'iframe',
        onElementCreated: (Object e) {
          // ignore: invalid_runtime_check_with_js_interop_types
          final f = e as JSObject;
          final st = f.getProperty<JSObject>('style'.toJS);
          st.setProperty('border'.toJS, 'none'.toJS);
          st.setProperty('width'.toJS, '100%'.toJS);
          st.setProperty('height'.toJS, '100%'.toJS);
          st.setProperty('background'.toJS, 'white'.toJS);
          // Keep lesson scripts in an opaque origin, away from the app's storage.
          f.callMethod('setAttribute'.toJS, 'sandbox'.toJS, 'allow-scripts allow-forms'.toJS);
          f.setProperty('srcdoc'.toJS, html.toJS);
        },
      );
}
