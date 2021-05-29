import urllib.request


def get_url_html_as_str(url: str) -> str:
    with urllib.request.urlopen(url) as f:
        return f.read().decode("utf-8")
