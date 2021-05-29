from unittest import mock
import unittest
import tempfile

from elpais_reader import export


class TestRequest(unittest.TestCase):
    @mock.patch("elpais_reader.export.filepath")
    def test_export_html(self, mock_filepath):
        with tempfile.TemporaryDirectory() as tmpdirname:
            html = "Hello world!"
            filepath = f"{tmpdirname}/test.html"
            mock_filepath.return_value = filepath
            export.export_html(html)
            with open(filepath) as f:
                f.seek(0)
                self.assertEqual(html, f.read())
