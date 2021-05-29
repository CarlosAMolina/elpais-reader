import unittest

from elpais_reader.html_parser import HtmlParser


# TODO
class TestHtmlParser(unittest.TestCase):
    def _test_get_body(self):
        HtmlParser().get_body("tests/files/test.html")
