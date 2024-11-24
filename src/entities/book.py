from .reference import Reference

class Book(Reference):
    def __init__(self, title, author, year, publisher, editor, reference_key, keywords):
        super().__init__(title, author, year, reference_key, keywords)
        self.publisher = publisher
        self.editor = editor

    def __str__(self):
        pass
