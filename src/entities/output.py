from bibtexparser.bibdatabase import BibDatabase
import bibtexparser

class Output:
    def __init__(self, data):
        self.id = ""
        self.title = data.title
        self.author = data.authors
        self.year = data.year
        self.publisher = data.publisher
        self.editor = data.editors
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

    def set_id(self, id):
        self.id = id

    def create_readable_string(self):
        ref_data = [self.title,
                    self.author,
                    self.year,
                    self.publisher,
                    self.editor,
                    self.booktitle,
                    self.journal,
                    self.volume,
                    self.page,
                    self.number,
                    self.month,
                    self.howpublished,
                    self.note,
                    ]
        string = ""
        for value in ref_data:
            if value and string == "":
                string += value
            elif value:
                string += f", {value}"
        return {"id":self.id,"text":string}

    def create_bibtex_string(self):
        bibdb = BibDatabase()
        bibdb.entries = []
        bibdb.entries.append(self.create_bibtex_instance())
        string = bibtexparser.dumps(bibdb)
        return {"id":self.id,"text":string}

    def create_bibtex_instance(self):
        bibtex_dict = {
            "ENTRYTYPE" : str(self.reference_type),
            "ID"        : str(self.reference_key)
        }
        reference_attributes = ["title","author","year","publisher","editor",
                                "journal","booktitle","page","volume","number",
                                "month","howpublished","note","keywords"]
        for attribute in reference_attributes:
            if getattr(self, attribute):
                bibtex_dict[attribute] = str(getattr(self, attribute))

        bibtex_dict = self.bibtex_seperate_multiple(bibtex_dict)
        return bibtex_dict

    def bibtex_seperate_multiple(self, bibtex_dict):
        if "author" in bibtex_dict:
            bibtex_dict["author"] = bibtex_dict["author"].replace(" and "," and \n          ")
            #menee rikki jos authorina " and "
        if "keywords" in bibtex_dict:
            bibtex_dict["keywords"] = bibtex_dict["keywords"].replace(", ",",\n             " )
            #menee rikki jos keywordina ", "
            #vois muuttaa databasee ettei voi mennä rikki
        return bibtex_dict
