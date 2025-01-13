class Document:
    def __init__(self, title, author, genre, publication_date, doc_type, total_copies):
        self.title = title
        self.author = author
        self.genre = genre
        self.publication_date = publication_date
        self.type = doc_type
        self.total_copies = total_copies
        self.available_copies = total_copies
        self.availability = True
