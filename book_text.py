def get_books_text(path):
    with open(path, encoding="utf-8") as f:
        return f.read()