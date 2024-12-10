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

    def format_fields_with_multiple_values(self):

        separator = ";"

        self.authors = self.authors.replace(separator, " and ")
        self.editors = self.editors.replace(separator, " and ")
        self.keywords = self.keywords.replace(separator, ", ")

    def add_values_from_dictionary(self, items):
        for key, value in items:
            setattr(self, key, value)

    def add_values_from_database(self, data):
        self.title = data.title
        self.authors = data.authors
        self.year = data.year
        self.publisher = data.publisher
        self.editors = data.editors
        self.journal = data.journal
        self.booktitle = data.booktitle
        self.page = data.page
        self.volume = data.volume
        self.number = data.number
        self.month = data.month
        self.howpublished = data.howpublished
        self.note = data.note
        self.reference_type = data.reference_type
        self.reference_key = data.reference_key
        self.keywords = data.keywords

    def set_reference_key(self, key):
        self.reference_key = key

    def create_readable_string(self):
        ref_data = {'title': self.title,
                    'author': self.authors,
                    'year': self.year,
                    'publisher': self.publisher,
                    'editor': self.editors,
                    'booktitle': self.booktitle,
                    'journal': self.journal,
                    'volume': self.volume,
                    'page': self.page,
                    'number': self.number,
                    'month': self.month,
                    'howpublished': self.howpublished,
                    'note': self.note,
                    }
        string = ""
        for value in ref_data.values():
            if value and string == "":
                string += value
            elif value:
                string += f", {value}"
        return string
