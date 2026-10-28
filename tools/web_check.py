"""Render every program of a RWPD unit at phone and desktop width; report JS errors; save screenshots.
  python3 tools/web_check.py 1 [ids...]   -> /home/user/chk/<id>_390.png, _1100.png"""
import importlib, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from web_runner import shots

u = sys.argv[1]
want = set(sys.argv[2:])
mod = importlib.import_module(f"content_DI03000061_u{u}_programs")
os.makedirs("/home/user/chk", exist_ok=True)
bad = 0
for p in mod.PROGRAMS:
    if want and p["id"] not in want:
        continue
    r = shots(p["code"]["en"], f"/home/user/chk/{p['id']}", actions=p.get("_actions"))
    errs = [e for e in r["errors"] if "favicon" not in e and "Failed to load resource" not in e]
    bad += bool(errs)
    print(p["id"], "h:", r["height"], "ERR" if errs else "ok", errs[:3])
print("programs with errors:", bad)
