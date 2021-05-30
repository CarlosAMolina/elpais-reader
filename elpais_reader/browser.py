import logging
import webbrowser

from . import export


class Browser:
    def __init__(self):
        self._logger = logging.getLogger(__name__)

    def open_html(self) -> None:
        self._logger.debug(f"Init: {self._url}")
        webbrowser.open_new_tab(self._url)

    @property
    def _url(self) -> str:
        return f"file:///{export.HtmlExporter().filepath}"
