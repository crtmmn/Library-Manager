class Book:
    def __init__(self, title, author, ISBN, num_copies):
        self.ISBN = ISBN
        self.title = title
        self.author = author
        self.num_copies = num_copies
    def to_dict(newBook):
        newBook_dict = {
            "title": newBook.title,
            "author": newBook.author,
            "ISBN": newBook.ISBN,
            "num_copies": newBook.num_copies
        }
        return newBook_dict