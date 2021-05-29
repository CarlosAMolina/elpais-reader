import unittest

from elpais_reader.request_url import get_url_html_as_str


class TestRequest(unittest.TestCase):
    def test_get_url_as_str(self):
        url = "https://duckduckgo.com/"
        result = get_url_html_as_str(url)
        self.assertTrue(len(result) > 1000)
