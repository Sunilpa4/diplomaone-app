import tempfile
import json
import unittest
import base64
from hashlib import sha256
from pathlib import Path
# Historical byte-preservation/replacement tests exercise OFFLINE staging.
# Separate public-publisher tests below assert that paid bytes never publish.
from publish_solved_papers import prepare, stage_reviewed_files as publish, publish as publish_public


def solution():
    return '<main>' + ''.join('<section>' + ''.join('<details><summary><span class="en">Question</span><span class="gu">પ્રશ્ન</span></summary></details>' for _ in range(28 if i == 0 else 0)) + '</section>' for i in range(5)) + '</main>'


class PublisherTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        root = Path(self.temp.name)
        self.src, self.site = root / 'src', root / 'site'
        self.src.mkdir(); self.site.mkdir()
        folder = self.src / '4351902'; folder.mkdir()
        (folder / 'summer-2026.html').write_text(solution(), encoding='utf-8')
        (folder / 'summer-2026.pdf').write_bytes(b'%PDF-1.4\n%%EOF\n')

    def tearDown(self):
        self.temp.cleanup()

    def test_public_publisher_never_copies_paid_answers_pdfs_or_images(self):
        image, _ = self.add_image()
        changed = publish_public(self.src, self.site)
        self.assertEqual([p.name for p in changed], ['summer-2026.json'])
        metadata = json.loads(changed[0].read_text())
        self.assertEqual(metadata, {'version': 1, 'private': True, 'id': '4351902--summer-2026'})
        self.assertEqual(list((self.site / 'papers' / '4351902').iterdir()), changed)
        self.assertFalse((self.site / 'papers' / image.relative_to(self.src)).exists())
        self.assertEqual(publish_public(self.src, self.site), [])

    def test_public_publisher_preserves_existing_paid_copies_for_explicit_private_migration(self):
        target = self.site / 'papers' / '4351902' / 'summer-2026.html'
        target.parent.mkdir(parents=True)
        target.write_bytes((self.src / '4351902' / 'summer-2026.html').read_bytes())
        before = target.read_bytes()
        publish_public(self.src, self.site)
        self.assertEqual(target.read_bytes(), before, 'Do not delete before verified private backup/import')
        self.assertFalse(target.with_suffix('.pdf').exists(), 'No new paid PDF is published')

    def test_public_publisher_keeps_common_papers_free(self):
        folder = self.src / '4351902'
        folder.rename(self.src / 'DI01000021')
        self.assertEqual(len(publish_public(self.src, self.site)), 2)
        self.assertTrue((self.site / 'papers' / 'DI01000021' / 'summer-2026.html').exists())
        self.assertTrue((self.site / 'papers' / 'DI01000021' / 'summer-2026.pdf').exists())
        self.assertEqual(len(publish_public(self.src, self.site)), 0)

    def test_public_metadata_conflict_or_symlink_aborts_before_writes(self):
        target = self.site / 'papers' / '4351902' / 'summer-2026.json'
        target.parent.mkdir(parents=True)
        target.write_text('{"private": false}')
        with self.assertRaisesRegex(ValueError, 'Unreviewed'):
            publish_public(self.src, self.site)
        self.assertEqual(target.read_text(), '{"private": false}')
        target.unlink()
        target.symlink_to(self.src / '4351902' / 'summer-2026.html')
        with self.assertRaisesRegex(ValueError, 'Unsafe'):
            publish_public(self.src, self.site)

    def test_additive_and_idempotent(self):
        other = self.site / 'papers' / 'DI03000141' / 'old.html'
        other.parent.mkdir(parents=True); other.write_text('preserve')
        self.assertEqual(len(publish(self.src, self.site)), 2)
        self.assertEqual(len(publish(self.src, self.site)), 0)
        self.assertEqual(other.read_text(), 'preserve')

    def test_conflicts_abort_before_any_write(self):
        target = self.site / 'papers' / '4351902' / 'summer-2026.pdf'
        target.parent.mkdir(parents=True); target.write_bytes(b'existing')
        with self.assertRaisesRegex(ValueError, 'refusing to overwrite'):
            publish(self.src, self.site)
        self.assertEqual(target.read_bytes(), b'existing')
        self.assertFalse((target.parent / 'summer-2026.html').exists())

    def test_malformed_and_missing_files_rejected(self):
        (self.src / '4351902' / 'summer-2026.pdf').unlink()
        with self.assertRaisesRegex(ValueError, 'matching original PDF'):
            prepare(self.src, self.site)
        (self.src / '4351902' / 'summer-2026.pdf').write_bytes(b'not a pdf')
        with self.assertRaisesRegex(ValueError, 'Invalid PDF'):
            prepare(self.src, self.site)

    def test_explicit_english_only_and_partial_translations(self):
        path = self.src / '4351902' / 'summer-2026.html'
        body = ''.join('<section>' + ''.join('<details><summary>Question</summary><div>Answer</div></details>' for _ in range(28 if i == 0 else 0)) + '</section>' for i in range(5))
        english = '<html lang="en"><head><meta name="paper-language" content="en-only"></head><main>' + body + '</main></html>'
        path.write_text(english, encoding='utf-8')
        self.assertEqual(len(prepare(self.src, self.site)), 2)
        for invalid in (english.replace('en-only', 'en'), english.replace('lang="en"', 'lang="gu"'), english.replace('<details>', '<details class="en">', 1), english.replace('<details>', '<details class="gu">', 1), english.replace('<details>', '<div>', 1)):
            path.write_text(invalid, encoding='utf-8')
            with self.assertRaisesRegex(ValueError, 'Incomplete'):
                prepare(self.src, self.site)

    def test_explicit_missing_original_manifest(self):
        pdf = self.src / '4351902' / 'summer-2026.pdf'
        pdf.unlink()
        manifest = Path(self.temp.name) / 'missing.json'
        manifest.write_text(json.dumps(['4351902/summer-2026']))
        self.assertEqual(len(prepare(self.src, self.site, manifest)), 1)
        with self.assertRaisesRegex(ValueError, 'matching original PDF'):
            prepare(self.src, self.site)
        for entries in ([], ['4351902/winter-2025'], ['../summer-2026'], ['4351902/summer-2026']*2):
            manifest.write_text(json.dumps(entries))
            with self.assertRaises(ValueError):
                prepare(self.src, self.site, manifest)
        manifest.write_text(json.dumps(['4351902/summer-2026']))
        pdf.write_bytes(b'%PDF-1.4\n%%EOF\n')
        with self.assertRaisesRegex(ValueError, 'matching original PDF'):
            prepare(self.src, self.site, manifest)  # stale exceptions are forbidden

    def test_pdf_only_pairs_and_existing_html_guard(self):
        folder = self.src / '4351902'
        (folder / 'summer-2026.html').unlink()
        solution_pdf = folder / 'summer-2026.solution.pdf'
        solution_pdf.write_bytes(b'%PDF-1.4\nsolution\n%%EOF\n')
        self.assertEqual(len(prepare(self.src, self.site)), 2)
        solution_pdf.write_bytes((folder / 'summer-2026.pdf').read_bytes())
        with self.assertRaisesRegex(ValueError, 'different PDFs'):
            prepare(self.src, self.site)
        solution_pdf.write_bytes(b'%PDF-1.4\nsolution\n%%EOF\n')
        (folder / 'summer-2026.pdf').unlink()
        with self.assertRaisesRegex(ValueError, 'matching original'):
            prepare(self.src, self.site)
        (folder / 'summer-2026.pdf').write_bytes(b'%PDF-1.4\n%%EOF\n')
        published = self.site / 'papers' / '4351902' / 'summer-2026.html'
        published.parent.mkdir(parents=True)
        published.write_text('previous solution')
        with self.assertRaisesRegex(ValueError, 'Existing HTML'):
            prepare(self.src, self.site)

    def test_destination_symlinks_rejected(self):
        (self.site / 'papers').symlink_to(self.src, target_is_directory=True)
        with self.assertRaisesRegex(ValueError, 'Unsafe target'):
            publish(self.src, self.site)

    def add_image(self):
        image = self.src / '4351902' / 'summer-2026.assets' / '0001.png'
        image.parent.mkdir(exist_ok=True)
        image.write_bytes(base64.b64decode('iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/x8AAwMCAO+a7ioAAAAASUVORK5CYII='))
        html = self.src / '4351902' / 'summer-2026.html'
        html.write_text(solution().replace('</summary>', '</summary><img src="summer-2026.assets/0001.png">', 1))
        return image, html

    def test_scoped_images_are_published_and_idempotent(self):
        image, _ = self.add_image()
        self.assertEqual(len(publish(self.src, self.site)), 3)
        self.assertEqual(len(publish(self.src, self.site)), 0)
        self.assertEqual((self.site / 'papers' / image.relative_to(self.src)).read_bytes(), image.read_bytes())
        image.write_bytes(image.read_bytes() + b'changed')
        with self.assertRaises(ValueError):
            prepare(self.src, self.site)

    def test_missing_or_orphan_images_abort_before_writes(self):
        image, html = self.add_image()
        data = image.read_bytes()
        image.unlink()
        with self.assertRaisesRegex(ValueError, 'Missing or unreferenced'):
            publish(self.src, self.site)
        self.assertFalse((self.site / 'papers').exists())
        image.write_bytes(data)
        html.write_text(solution())
        with self.assertRaisesRegex(ValueError, 'Missing or unreferenced'):
            publish(self.src, self.site)
        self.assertFalse((self.site / 'papers').exists())

    def test_unscoped_references_and_non_image_assets_rejected(self):
        image, html = self.add_image()
        good = html.read_text()
        for bad in ('../0001.png', 'winter-2025.assets/0001.png', '/summer-2026.assets/0001.png',
                    'https://example.com/0001.png', 'summer-2026.assets/../0001.png',
                    'summer-2026.assets/0001.svg', 'summer-2026.assets/0001.png?x=1',
                    'summer-2026.assets/%30%30%30%31.png', 'summer-2026.assets\\\\0001.png'):
            html.write_text(good.replace('summer-2026.assets/0001.png', bad))
            with self.subTest(reference=bad), self.assertRaisesRegex(ValueError, 'Unscoped'):
                prepare(self.src, self.site)
        html.write_text(good)
        image.write_bytes(b'<svg onload="alert(1)"></svg>')
        with self.assertRaisesRegex(ValueError, 'Invalid paper image'):
            prepare(self.src, self.site)

    def test_asset_and_ancestor_symlinks_are_rejected(self):
        image, _ = self.add_image()
        target = self.site / 'papers' / '4351902'
        target.mkdir(parents=True)
        (target / 'summer-2026.assets').symlink_to(image.parent, target_is_directory=True)
        with self.assertRaisesRegex(ValueError, 'Unsafe target'):
            publish(self.src, self.site)
        (target / 'summer-2026.assets').unlink()
        (target / 'summer-2026.assets').write_text('not a directory')
        with self.assertRaisesRegex(ValueError, 'Unsafe target'):
            publish(self.src, self.site)
        (target / 'summer-2026.assets').unlink()
        data = image.read_bytes()
        image.unlink()
        original = Path(self.temp.name) / 'source.png'; original.write_bytes(data)
        image.symlink_to(original)
        with self.assertRaisesRegex(ValueError, 'Symlinks'):
            publish(self.src, self.site)

    def test_explicit_38_item_common_paper_and_each_language(self):
        folder = self.src / '4351902'
        folder.rename(self.src / 'DI01000021')
        html = self.src / 'DI01000021' / 'summer-2026.html'
        content = '<html lang="en"><meta name="paper-layout" content="source-pdf-cards-v1"><meta name="paper-question-count" content="38"><meta name="paper-language" content="en-only"><main>'
        content += ''.join('<section>' + ''.join('<details><summary>Question</summary><div class="answer">Worked answer</div></details>' for _ in range(38 if i == 0 else 0)) + '</section>' for i in range(5)) + '</main></html>'
        html.write_text(content)
        self.assertEqual(len(prepare(self.src, self.site)), 2)
        for bad in (content.replace('content="38"', 'content="28"'),
                    content.replace('source-pdf-cards-v1', 'unknown'),
                    content.replace('<div class="answer">', '<div>', 1),
                    content.replace('</main>', '<script>bad()</script></main>'),
                    content.replace('<details>', '<details onclick="bad()">', 1)):
            html.write_text(bad)
            with self.assertRaises(ValueError):
                prepare(self.src, self.site)

    def test_new_html_replaces_pdf_presentation_without_modifying_pdfs(self):
        target = self.site / 'papers' / '4351902'; target.mkdir(parents=True)
        pdf = self.src / '4351902' / 'summer-2026.pdf'
        (target / pdf.name).write_bytes(pdf.read_bytes())
        solved = b'%PDF-1.4\nsource solution\n%%EOF\n'
        (self.src / '4351902' / 'summer-2026.solution.pdf').write_bytes(solved)
        (target / 'summer-2026.solution.pdf').write_bytes(solved)
        added = publish(self.src, self.site)
        self.assertEqual([p.name for p in added], ['summer-2026.html'])
        self.assertEqual((target / pdf.name).read_bytes(), pdf.read_bytes())
        self.assertEqual((target / 'summer-2026.solution.pdf').read_bytes(), solved)

    def replacement_review(self, old=b'previous reviewed HTML'):
        rel = '4351902/summer-2026.html'
        record = {'path': rel, 'old_sha256': sha256(old).hexdigest(),
                  'new_sha256': sha256((self.src / rel).read_bytes()).hexdigest(),
                  'reason': 'Owner requested the newly supplied answers for this same exam.',
                  'source_drive_id': 'reviewed-source-id'}
        manifest = Path(self.temp.name) / 'replacements.json'
        manifest.write_text(json.dumps([record]))
        return manifest, record

    def test_reviewed_html_replacement_is_explicit_pinned_and_idempotent(self):
        manifest, record = self.replacement_review()
        target = self.site / 'papers' / record['path']; target.parent.mkdir(parents=True)
        target.write_bytes(b'previous reviewed HTML')
        with self.assertRaisesRegex(ValueError, 'refusing to overwrite'):
            publish(self.src, self.site)
        self.assertFalse(target.with_suffix('.pdf').exists())
        self.assertEqual(len(publish(self.src, self.site, replacements=manifest)), 2)
        self.assertEqual(target.read_bytes(), (self.src / record['path']).read_bytes())
        self.assertEqual(len(publish(self.src, self.site, replacements=manifest)), 0)

    def test_replacement_rejects_changed_old_or_incoming_bytes_before_writes(self):
        manifest, record = self.replacement_review()
        target = self.site / 'papers' / record['path']; target.parent.mkdir(parents=True)
        target.write_bytes(b'another revision not reviewed')
        with self.assertRaisesRegex(ValueError, 'refusing to overwrite'):
            publish(self.src, self.site, replacements=manifest)
        self.assertFalse(target.with_suffix('.pdf').exists())
        target.write_bytes(b'previous reviewed HTML')
        source = self.src / record['path']; source.write_bytes(source.read_bytes() + b'changed')
        with self.assertRaisesRegex(ValueError, 'Incoming reader differs'):
            publish(self.src, self.site, replacements=manifest)
        self.assertEqual(target.read_bytes(), b'previous reviewed HTML')
        self.assertFalse(target.with_suffix('.pdf').exists())

    def test_only_exact_reviewed_html_paths_and_complete_metadata_allowed(self):
        manifest, record = self.replacement_review()
        bad_records = [dict(record, path=name) for name in (
            '../4351902/summer-2026.html', '/4351902/summer-2026.html',
            '4351902/../summer-2026.html', '4351902/summer-2026.pdf',
            '4351902/summer-2026.assets/0001.png', '4351902/Question_Paper.html')]
        bad_records += [dict(record, old_sha256='not a hash'), dict(record, new_sha256=record['old_sha256']),
                        dict(record, reason=''), dict(record, source_drive_id=''),
                        {k:v for k,v in record.items() if k != 'old_sha256'}]
        for bad in bad_records:
            manifest.write_text(json.dumps([bad]))
            with self.subTest(record=bad), self.assertRaises(ValueError):
                publish(self.src, self.site, replacements=manifest)
            self.assertFalse((self.site / 'papers').exists())
        manifest.write_text(json.dumps([record, record]))
        with self.assertRaisesRegex(ValueError, 'Duplicate'):
            publish(self.src, self.site, replacements=manifest)

    def test_replacement_manifest_cannot_authorize_other_overwrites(self):
        manifest, record = self.replacement_review()
        target = self.site / 'papers' / record['path']; target.parent.mkdir(parents=True)
        target.write_bytes(b'previous reviewed HTML')
        pdf = target.with_suffix('.pdf'); pdf.write_bytes(b'preserve existing original PDF')
        with self.assertRaisesRegex(ValueError, 'refusing to overwrite'):
            publish(self.src, self.site, replacements=manifest)
        self.assertEqual(target.read_bytes(), b'previous reviewed HTML')
        self.assertEqual(pdf.read_bytes(), b'preserve existing original PDF')

    def test_replacement_manifest_stale_paths_and_symlinks_rejected(self):
        manifest, record = self.replacement_review()
        manifest.write_text(json.dumps([dict(record, path='4351902/winter-2025.html')]))
        with self.assertRaisesRegex(ValueError, 'absent staged'):
            publish(self.src, self.site, replacements=manifest)
        self.assertFalse((self.site / 'papers').exists())
        link = Path(self.temp.name) / 'link.json'; link.symlink_to(manifest)
        with self.assertRaisesRegex(ValueError, 'regular file'):
            publish(self.src, self.site, replacements=link)


if __name__ == '__main__':
    unittest.main()
