import 'package:flutter/material.dart';
import 'package:webview_flutter/webview_flutter.dart';

const bool isWebFrame = false;

class HtmlFrame extends StatefulWidget {
  const HtmlFrame({super.key, required this.html});
  final String html;

  @override
  State<HtmlFrame> createState() => _HtmlFrameState();
}

class _HtmlFrameState extends State<HtmlFrame> {
  late final WebViewController _c = WebViewController()
    ..setJavaScriptMode(JavaScriptMode.unrestricted)
    ..setBackgroundColor(Colors.white)
    ..loadHtmlString(widget.html);

  @override
  void didUpdateWidget(HtmlFrame old) {
    super.didUpdateWidget(old);
    if (old.html != widget.html) _c.loadHtmlString(widget.html);
  }

  @override
  Widget build(BuildContext context) => WebViewWidget(controller: _c);
}
