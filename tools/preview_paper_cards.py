#!/usr/bin/env python3
"""Local review site for staged papers; never modifies production JS or data.

Run `python3 tools/preview_paper_cards.py` and open port 4173. Exported notes and
screenshots stay under ignored build/. The production app's two trusted paper
URLs are changed in memory to same-origin local staging paths for this preview.
"""
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import unquote, urlsplit
import argparse
import json
import subprocess
import sys

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / 'build/card-preview/data'
PAPERS = ROOT / 'papers-upload/papers'


class Preview(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT / 'website'), **kwargs)

    def do_GET(self):
        path = unquote(urlsplit(self.path).path)
        if path == '/app.js':
            body = (ROOT / 'website/app.js').read_text().replace(
                "const paperBase = 'https://sunilpa4.github.io/diplomaone-content/papers';",
                "const paperBase = '/papers';").replace(
                "const paperTreeUrl = 'https://api.github.com/repos/Sunilpa4/diplomaone-content/git/trees/main?recursive=1';",
                "const paperTreeUrl = '/paper-tree.json';").encode()
            return self.respond(body, 'text/javascript; charset=utf-8')
        if path == '/paper-tree.json':
            tree = {'truncated': False, 'tree': [
                {'path': 'papers/' + p.relative_to(PAPERS).as_posix(), 'type': 'blob', 'mode': '100644'}
                for p in sorted(PAPERS.rglob('*')) if p.is_file()]}
            return self.respond(json.dumps(tree).encode(), 'application/json')
        if path.startswith('/papers/'):
            return self.local(PAPERS, path[len('/papers/'):])
        if path.startswith('/data/'):
            return self.local(DATA, path[len('/data/'):])
        return super().do_GET()

    def local(self, base, rel):
        target = (base / rel).resolve()
        if not target.is_relative_to(base) or not target.is_file():
            return self.send_error(404)
        return self.respond(target.read_bytes(), self.guess_type(str(target)))

    def respond(self, body, mime):
        self.send_response(200)
        self.send_header('Content-Type', mime)
        self.send_header('Content-Length', str(len(body)))
        self.send_header('Cache-Control', 'no-store')
        self.end_headers()
        self.wfile.write(body)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--port', type=int, default=4173)
    args = parser.parse_args()
    if not (DATA / 'catalog.json').is_file():
        subprocess.run([sys.executable, str(ROOT / 'tools/export_app_content.py'), '--out', str(DATA)], check=True)
    print(f'Staged question-card preview on port {args.port}; not a production deployment.', flush=True)
    ThreadingHTTPServer(('0.0.0.0', args.port), Preview).serve_forever()
