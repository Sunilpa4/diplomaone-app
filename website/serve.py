"""Local website preview using the same generated data as the app.

Run `python3 tools/export_app_content.py`, then `python3 website/serve.py`.
"""
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import os
import urllib.parse

ROOT = Path(__file__).resolve().parent.parent
DATA = Path(os.environ.get('DATA_DIR', ROOT / 'build' / 'data')).resolve()


class Handler(SimpleHTTPRequestHandler):
    def translate_path(self, path):
        parsed = urllib.parse.urlsplit(path).path
        if parsed == '/data' or parsed.startswith('/data/'):
            rel = parsed.removeprefix('/data').lstrip('/')
            base = DATA
            target = (base / urllib.parse.unquote(rel)).resolve()
            return str(target if target.is_relative_to(base) else base / '__not_found__')
        return super().translate_path(path)

    def end_headers(self):
        self.send_header('Cache-Control', 'no-store')
        super().end_headers()


if __name__ == '__main__':
    os.chdir(ROOT / 'website')
    port = int(os.environ.get('PORT', '8000'))
    print(f'DiplomaOne website: http://0.0.0.0:{port}', flush=True)
    ThreadingHTTPServer(('0.0.0.0', port), partial(Handler, directory=str(ROOT / 'website'))).serve_forever()
