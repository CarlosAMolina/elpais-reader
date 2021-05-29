import unittest
import tempfile

from elpais_reader.export import export_html


class TestRequest(unittest.TestCase):
    def test_export_html(self):
        with tempfile.TemporaryDirectory() as tmpdirname:
            html = "Hello world!"
            filepath = f"{tmpdirname}/test.html"
            export_html(html, filepath)
            with open(filepath) as f:
                f.seek(0)
                self.assertEqual(html, f.read())
