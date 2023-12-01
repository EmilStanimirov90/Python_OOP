from typing import List, Optional


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

        self.page = 0

    def turn_page(self, page):
        self.page = page


class Library:
    def __init__(self):
        self.book_collection: List[Book] = []

    def add_book(self, book: Book):
        self.book_collection.append(book)

    def find_book(self, title: str) -> Optional[Book]:
        try:
            book = [b for b in self.book_collection if b.title == title][0]
            return book
        except IndexError:
            return None


book = Book("Tittle1", "test")
book2 = Book("Tittle2", "test2")
library = Library()
print(library.book_collection)
library.add_book(book)
print(library.book_collection)
print(library.find_book("asd"))
print(library.find_book("Tittle1"))
