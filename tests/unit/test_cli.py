import unittest

from elpais_reader import cli


class TestCli(unittest.TestCase):
    def setUp(self):
        self.cli = cli.Cli()

    def test_is_valid_url_for_valid_url(self):
        url = "https://duckduckgo.com"
        self.assertTrue(self.cli._is_valid_url(url))

    def test_is_valid_url_for_invalid_urls(self):
        for url in [
            "2",
            "http://test",
            "test.com",
        ]:
            self.assertFalse(self.cli._is_valid_url(url))
