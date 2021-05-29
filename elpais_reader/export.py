import pathlib
import logging


class HtmlExporter:
    def __init__(self):
        self._logger = logging.getLogger(__name__)

    def export_html(self, html: str) -> None:
        self._logger.debug(f"Init: {self.filepath}")
        with open(self.filepath, "w") as f:
            f.write(html)

    @property
    def filepath(self) -> str:
        module_path = pathlib.Path(__file__).parent.absolute()
        result = module_path.joinpath("index.html")
        return str(result)
