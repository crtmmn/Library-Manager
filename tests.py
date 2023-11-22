import unittest
from unittest.mock import patch, mock_open
from unittest import mock, TestCase
import os
import sys
from book import Book
from library import Library, NotificationSystem


class TestAddNewBook(unittest.TestCase):
    def test_add_new_book(self):
        add_book = Library("books").add_book(Book("Bastion", "Stephen King", 789, 8))
        self.assertEqual(add_book, "Book was added")
        
        
    def mocked_return_add_book(*args, **kwargs):
        return "Book was added"
    
    @mock.patch("library.Library.add_book", new=mocked_return_add_book)
    def test_add_new_book_mocked(self):
        add_book = Library("books").add_book(Book("Bastion", "Stephen King", 2137, 8))
        self.assertEqual(add_book, "Book was added")
        
class TestAddCopy(unittest.TestCase):
    def test_add_copy(self):
        add_book = Library("books").add_book(Book("Slepnac od swiatel", "Jakub Zulczyk", 2137, 8))
        self.assertEqual(add_book, "Copy was added")
        
    
    def mocked_return_add_copy(*args, **kwargs):
        return "Copy was added"
    
    
    @mock.patch("library.Library.add_book", new=mocked_return_add_copy)
    def test_add_new_book_mocked(self):
        add_book = Library("books").add_book(Book("Slepnac od swiatel", "Jakub Zulczyk", 1, 8))
        self.assertEqual(add_book, "Copy was added")
    
        
class TestLendBook(unittest.TestCase):
    def test_lend_book(self):
        lend_book = Library("books").lend_book("Anrzej", Book("Kordian", "Juliusz Slowacki", 543, 12))
        self.assertEqual(lend_book, "Book was lended")
        
    def mocked_return_lend_book(*args, **kwargs):
        return "Book was lended"
    
    def mocked_send_notification(*args, **kwargs):
        return "Notification that book was lended"
    
    @mock.patch("library.NotificationSystem.send_notification", new=mocked_send_notification)
    @mock.patch("library.Library.lend_book", new=mocked_return_lend_book)
    def test_lend_book_mocked(self):
        lend_book = Library("books").lend_book("Anrzej", Book("Kordian", "Juliusz Slowacki", 753, 12))
        notification = NotificationSystem.send_notification(self, "Anrzej", "notification")
        self.assertEqual(lend_book, "Book was lended")
        self.assertEqual(notification, "Notification that book was lended")

class TestLendNotAvailableBook(unittest.TestCase):
    def test_lend_not_available_book(self):
        lend_book = Library("books").lend_book("Anrzej", Book("Dziady", "Adam Mickiewicz", 987, 12))
        self.assertEqual(lend_book, "Book with this ISBN isn't available")
        
        
    def mocked_return_lend_not_available_book(*args, **kwargs):
        return "Book with this ISBN isn't available"
    
    @mock.patch("library.Library.lend_book", new=mocked_return_lend_not_available_book)
    def test_lend_not_available_mocked(self):
        lend_book = Library("books").lend_book("Anrzej", Book("Psy", "Waldemar Morawiec", 2137, 12))
        self.assertEqual(lend_book, "Book with this ISBN isn't available")
    
class TestLendNotExistBook(unittest.TestCase):
    def test_lend_not_exist_book(self):
        lend_book = Library("books").lend_book("Anrzej", Book("Psy", "Waldemar Morawiec", 997, 12))
        self.assertEqual(lend_book, "Book with this ISBN doesn't exist")
        
    def mocked_return_lend_not_exist_book(*args, **kwargs):
        return "Book with this ISBN doesn't exist"
    
    @mock.patch("library.Library.lend_book", new=mocked_return_lend_not_exist_book)
    def test_lend_not_exist_book_mocked(self):
        lend_book = Library("books").lend_book("Anrzej", Book("Psy", "Waldemar Morawiec", 123, 12))
        self.assertEqual(lend_book, "Book with this ISBN doesn't exist")
        
class TestReturnBook(unittest.TestCase):
    def test_return_book(self):
        L = Library("books")
        L.lend_book("Anrzejek", Book("Psy", "Waldemar Morawiec", 123, 12))
        return_book = L.return_book("Anrzejek", Book("Psy", "Waldemar Morawiec", 123, 12))
        self.assertEqual(return_book, "Book was returned")
        
    def mocked_return_test_return_book(*args, **kwargs):
        return "Book was returned"
    
    def mocked_send_notification(*args, **kwargs):
        return "Notification that book was returned"
    
    @mock.patch("library.NotificationSystem.send_notification", new=mocked_send_notification)
    @mock.patch("library.Library.return_book", new=mocked_return_test_return_book)
    def test_return_book_mocked(self):
        return_book = Library("books").return_book("Anrzej", Book("Psy", "Waldemar Morawiec", 997, 12))
        notification = NotificationSystem.send_notification(self, "Anrzej", "notification")
        self.assertEqual(return_book, "Book was returned")
        self.assertEqual(notification, "Notification that book was returned")
        
class TestReturnBookNotLended(unittest.TestCase):
    def test_return_book_not_lended(self):
        L = Library("books")
        return_book = L.return_book("Anrzejek", Book("Psy", "Waldemar Morawiec", 123, 12))
        self.assertEqual(return_book, "User with this name doesn't have that book to return")

    def mocked_return_test_return_book_not_lended(*args, **kwargs):
        return "User with this name doesn't have that book to return"
    
    @mock.patch("library.Library.return_book", new=mocked_return_test_return_book_not_lended)
    def test_return_book_not_lended_mocked(self):
        L = Library("books")
        return_book = L.return_book("Anrzejek", Book("Psy", "Waldemar Morawiec", 123, 12))
        self.assertEqual(return_book, "User with this name doesn't have that book to return")
        
        
        
        
if __name__ == '__main__':
    unittest.main()
