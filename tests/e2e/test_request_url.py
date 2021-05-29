import unittest

from elpais_reader import request_url


class TestRequest(unittest.TestCase):
    def setUp(self):
        self.requester = request_url.UrlRequester()

    def test_get_url_as_str(self):
        url = "https://duckduckgo.com/"
        result = self.requester.get_url_html_as_str(url)
        self.assertTrue(len(result) > 1000)
