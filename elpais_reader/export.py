def export_html(html: str, filepath: str = "index.html"):
    with open(filepath, "w") as f:
        f.write(html)
