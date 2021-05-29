import pathlib
import unittest

from elpais_reader import export


class TestHtmlParser(unittest.TestCase):
    def test_filepath_default(self):
        self.assertTrue(export.filepath().endswith("index.html"))
        working_directory = str(pathlib.Path().absolute())
        self.assertTrue(export.filepath().startswith(working_directory))
