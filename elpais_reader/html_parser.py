from bs4 import BeautifulSoup


# TODO
class HtmlParser:
    def get_body(self, filepath: str):
        breakpoint()
        with open(filepath) as f:

            html_doc = f.read()

        soup = BeautifulSoup(html_doc, "html.parser")
        print(soup)
