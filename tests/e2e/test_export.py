from unittest import mock
import unittest
import tempfile

from elpais_reader import export


class TestExport(unittest.TestCase):
    def setUp(self):
        self.exporter = export.HtmlExporter()

    @mock.patch(
        "elpais_reader.export.HtmlExporter.filepath",
        new_callable=mock.PropertyMock,
    )
    def test_export_html(self, mock_filepath):
        with tempfile.TemporaryDirectory() as tmpdirname:
            html = "Hello world!"
            filepath = f"{tmpdirname}/test.html"
            mock_filepath.return_value = filepath
            self.exporter.export_html(html)
            with open(filepath) as f:
                f.seek(0)
                self.assertEqual(html, f.read())
