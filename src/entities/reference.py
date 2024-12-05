class Reference:
    def __init__(self):

        self.title = ""
        self.authors = ""
        self.year = ""
        self.publisher = ""
        self.editors = ""
        self.journal = ""
        self.booktitle = ""
        self.page = ""
        self.volume = ""
        self.number = ""
        self.month = ""
        self.howpublished = ""
        self.note = ""
        self.reference_type = ""
        self.reference_key = ""
        self.keywords = ""

    def handle_empty_value(self, value):

        if value is None:
            return ""

        return value
