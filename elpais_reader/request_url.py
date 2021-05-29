import logging
import urllib.request


class UrlRequester:
    def __init__(self):
        self._logger = logging.getLogger(__name__)

    def get_url_html_as_str(self, url: str) -> str:
        self._logger.debug(f"Init: {url}")
        with urllib.request.urlopen(url) as f:
            return f.read().decode("utf-8")
