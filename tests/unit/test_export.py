import pathlib
import unittest

from elpais_reader import export


class TestHtmlParser(unittest.TestCase):
    def setUp(self):
        self.exporter = export.HtmlExporter()

    def test_filepath_default(self):
        self.assertTrue(self.exporter.filepath.endswith("index.html"))
        working_directory = str(pathlib.Path().absolute())
        self.assertTrue(self.exporter.filepath.startswith(working_directory))
