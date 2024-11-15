from reference import Reference

class Book(Reference):
    def __init__(self, title, author, year, publisher, editor):
        super().__init__(title, author, year)
        self.publisher = publisher
        self.editor = editor

    def __str__(self):
        pass
