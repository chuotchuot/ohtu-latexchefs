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

    def add_values_from_doi(self, data):
        self.reference_type = "article"
        self.title = data.get("title")
        self.authors = data.get("author")
        self.year = data.get("year")
        self.journal = data.get("journal")
        self.volume = data.get("volume")
        self.number = data.get("number")
        self.page = data.get("page")
        self.month = data.get("month")
        self.note = data.get("note")

    def set_reference_key(self, key):
        self.reference_key = key
