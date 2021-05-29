import pathlib


def export_html(html: str) -> None:
    with open(filepath(), "w") as f:
        f.write(html)


def filepath() -> str:
    module_path = pathlib.Path(__file__).parent.absolute()
    return f"{module_path}/index.html"
