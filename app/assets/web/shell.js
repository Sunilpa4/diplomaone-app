/* DiplomaOne live preview helper (injected first in <head>).
   1. Images that cannot load (e.g. img/campus.jpg) are replaced by a labelled placeholder.
   2. alert() is shown as an in-page box (Android WebView does not show alerts). */
(function () {
  var COLS = ['#7B2CD9', '#1565C0', '#2E7D32', '#E07B00', '#C62828', '#00796B', '#6D4C41', '#AD1457'];
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return {'&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;'}[c]; }); }
  function ph(img) {
    var src = img.getAttribute('src') || 'image';
    var name = src.split('/').pop().split('?')[0] || 'image';
    var w = parseInt(img.getAttribute('width'), 10) || 600;
    var h = parseInt(img.getAttribute('height'), 10) || Math.round(w * 2 / 3);
    var n = 0;
    for (var i = 0; i < name.length; i++) n = (n * 31 + name.charCodeAt(i)) % 9973;
    var c = COLS[n % COLS.length];
    var label = (img.getAttribute('alt') || name.replace(/\.[a-z0-9]+$/i, '').replace(/[-_]/g, ' '));
    var fs = Math.max(14, Math.round(Math.min(w, h) / 9));
    var svg = '<svg xmlns="http://www.w3.org/2000/svg" width="' + w + '" height="' + h + '" viewBox="0 0 ' + w + ' ' + h + '">' +
      '<defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="' + c + '"/>' +
      '<stop offset="1" stop-color="' + c + '" stop-opacity="0.55"/></linearGradient></defs>' +
      '<rect width="100%" height="100%" fill="url(#g)"/>' +
      '<circle cx="' + (w * 0.78) + '" cy="' + (h * 0.3) + '" r="' + (Math.min(w, h) * 0.12) + '" fill="#fff" fill-opacity="0.35"/>' +
      '<path d="M0 ' + h + ' L' + (w * 0.35) + ' ' + (h * 0.45) + ' L' + (w * 0.6) + ' ' + (h * 0.75) + ' L' + (w * 0.75) + ' ' + (h * 0.6) + ' L' + w + ' ' + h + ' Z" fill="#fff" fill-opacity="0.25"/>' +
      '<text x="50%" y="50%" fill="#fff" font-family="sans-serif" font-weight="bold" font-size="' + fs + '" text-anchor="middle" dominant-baseline="middle">' + esc(label) + '</text></svg>';
    return 'data:image/svg+xml;charset=utf-8,' + encodeURIComponent(svg);
  }
  document.addEventListener('error', function (e) {
    var t = e.target;
    if (t && t.tagName === 'IMG' && !t.getAttribute('data-ph')) {
      t.setAttribute('data-ph', '1');
      t.src = ph(t);
    }
  }, true);
  window.alert = function (msg) {
    var box = document.createElement('div');
    box.setAttribute('style', 'position:fixed;inset:0;background:rgba(0,0,0,.45);display:flex;align-items:center;justify-content:center;z-index:99999;font-family:sans-serif');
    box.innerHTML = '<div style="background:#fff;border-radius:10px;padding:18px 20px;min-width:240px;max-width:85%;box-shadow:0 6px 24px rgba(0,0,0,.3)">' +
      '<div style="font-size:13px;color:#666;margin-bottom:6px">Alert</div><div style="font-size:16px;white-space:pre-wrap">' + esc(msg) + '</div>' +
      '<div style="text-align:right;margin-top:14px"><button style="background:#7B2CD9;color:#fff;border:0;border-radius:6px;padding:6px 18px;font-size:14px">OK</button></div></div>';
    box.querySelector('button').onclick = function () { box.remove(); };
    (document.body || document.documentElement).appendChild(box);
  };
})();
