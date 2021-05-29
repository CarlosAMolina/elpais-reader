import browser
import export
import cli
import request_url
from log import logger


def main() -> None:
    url = cli.Cli().get_url()
    html = request_url.UrlRequester().get_url_html_as_str(url)
    export.HtmlExporter().export_html(html)
    browser.Browser().open_html()


if __name__ == "__main__":
    logger.configure()
    main()
