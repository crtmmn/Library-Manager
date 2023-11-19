import json
import os
from book import Book

class Library:
    def __init__(self, filename):
        self.filename = filename + ".json"
        self.users_list = []
        self.load()
    def load(self):
        try:
            with open(self.filename, 'r') as file:
                self.database = json.load(file)
        except (FileNotFoundError):
            self.database = []
            with open(self.filename, "w") as file:
                json.dump(self.database, file)
            file.close()
            return "File doesn't exists"
        except (json.JSONDecodeError):
            self.database = []
            return "File is empty"
        file.close()
        return self.database

    def save(self):
        with open(self.filename, "w") as file:
            json.dump(self.database, file, indent=4)
    
    def add_book(self, newBook):
        book_dict = Book.to_dict(newBook)
        for element in self.database:
            if(element.get("ISBN") == book_dict.get("ISBN")):
                element["num_copies"] += 1
                self.save()
                return "Copy was added"
        else:
            self.database.append(book_dict)
            self.save()
            return "Book was added"
    
    def lend_book(self, user, book):
        book_dict = Book.to_dict(book)
        for element in self.database:
            if(element.get("ISBN") == book_dict.get("ISBN")):
                if(element.get("num_copies") > 0):
                    element["num_copies"] -= 1
                    self.save()
                    user_info = {
                        "user_name": user,
                        "book_ISBN": element.get("ISBN")
                    }
                    self.users_list.append(user_info)
                    return "Book was lended"
                elif(element.get("num_copies") <= 0):
                    return "Book with this ISBN isn't available"
        else:
            return "Book with this ISBN doesn't exist"
            
    def return_book(self, user, book):
        book_dict = Book.to_dict(book)
        for element in self.users_list:
            if(element.get("user_name") == user and element.get("book_ISBN") == book_dict.get("ISBN")):
                self.add_book(book)
                self.users_list.remove(element)
                return "Book was returned"
        else:
            return "User with this name doesn't have that book to return"