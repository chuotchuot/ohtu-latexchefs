class Reference:
    def __init__(
            self, title, reference_type, reference_key,
            year=None, authors=None, publisher=None, editor=None,
            journal=None, booktitle=None, page=None, volume=None,
            number=None, month=None, howpublished=None, note=None,
            keywords=None
        ):

        self.title = title
        self.author = self.handle_empty_value(authors)
        self.year = self.handle_empty_value(year)
        self.publisher = self.handle_empty_value(publisher)
        self.editor = self.handle_empty_value(editor)
        self.journal = self.handle_empty_value(journal)
        self.booktitle = self.handle_empty_value(booktitle)
        self.page = self.handle_empty_value(page)
        self.volume = self.handle_empty_value(volume)
        self.number = self.handle_empty_value(number)
        self.month = self.handle_empty_value(month)
        self.howpublished = self.handle_empty_value(howpublished)
        self.note = self.handle_empty_value(note)
        self.reference_type = reference_type
        self.reference_key = reference_key
        self.keywords = self.handle_empty_value(keywords)

    def handle_empty_value(self, value):

        if value is None:
            return ""

        return value
