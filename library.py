#Name Sumit Sohal
#Student Id C0902846

# Here we are defining a book class 
class Book:
    def __init__(self,title,author,isbn,available=True):
        self.title=title
        self.author=author
        self.isbn=isbn
        self.available=available

    def checkout(self):
        if self.available:
            self.available=False
            print(f'the book{self.title} has been checked out')
        else:
            print(f'the book{self.title} is not available...')

    def return_book(self):
        if not self.available:
            self.available=True
            print(f'Book returned{self.title} and author{self.author}')
        else:
            print("the book is already in the library")

    def __str__(self):

        return f"the book that is present is title: {self.title} and the authors is: {self.author}"

# Here we are defining a FictionBook class 
class FictionBook:
    def __init__(self, title, author, isbn,genre, available=True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available
        self.genre = genre

    def checkout(self):
        if self.available:
            self.available = False
            print(f'the book{self.title} has been checked out')
        else:
            print(f'the book{self.title} is not available...')

    def return_book(self):
        if not self.available:
            self.available = True
            print(f'Book returned{self.title} and author{self.author}')
        else:
            print("the book is already in the library")

    def __str__(self):

        return f"the book that is present is title: {self.title} and the authors is: {self.author} and genre{self.genre}"

# Here we are defining a NonFictionBook class
class NonFictionBook:
    def __init__(self, title, author, isbn,field,available=True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available
        self.field=  field

    def checkout(self):
        if self.available:
            self.available = False
            print(f'the book{self.title} has been checked out')
        else:
            print(f'the book{self.title} is not available...')

    def return_book(self):
        if not self.available:
            self.available = True
            print(f'Book returned{self.title} and author{self.author}')
        else:
            print("the book is already in the library")

    def __str__(self):

        return f"the book that is present is title: {self.title} and the authors is: {self.author} and field{self.field}"

# Here we are defining a library
class Library:
    def __init__(self):
        self.book_catalog = []
        self.fiction_catalog = []
        self.nonfiction_catalog = []

    def add_book(self, book, book_type):
        if book_type == "FictionBook":
            self.fiction_catalog.append(book)
        elif book_type == "NonFictionBook":
            self.nonfiction_catalog.append(book)
        else:
            self.book_catalog.append(book)

    def list_books(self):
        print("All Books in Library:")
        print("----- Fiction Books -----")
        for fiction_book in self.fiction_catalog:
            print(fiction_book)
        print("----- Non-Fiction Books -----")
        for non_fiction_book in self.nonfiction_catalog:
            print(non_fiction_book)
        print("----- Regular Books -----")
        for regular_book in self.book_catalog:
            print(regular_book)

    def checkout_book(self, title, book_type):
        catalog = self.get_catalog_by_type(book_type)
        if catalog:
            for book in catalog:
                if book.title == title and book.available:
                    book.checkout()
                    print(f"Book '{title}' checked out successfully.")
                    return
            print(f"Book '{title}' not found or is not available for checkout.")
        else:
            print(f"Invalid book type: {book_type}")

    def return_book(self, title, book_type):
        catalog = self.get_catalog_by_type(book_type)
        if catalog:
            for book in catalog:
                if book.title == title and not book.available:
                    book.return_book()
                    print(f"Book '{title}' returned successfully.")
                    return
            print(f"Book '{title}' not found or is already available.")
        else:
            print(f"Invalid book type: {book_type}")

    def get_catalog_by_type(self, book_type):
        if book_type == "Book":
            return self.book_catalog
        elif book_type == "FictionBook":
            return self.fiction_catalog
        elif book_type == "NonFictionBook":
            return self.nonfiction_catalog
        else:
            return None

library = Library()

# Creating instances of books
book1 = Book("The Catcher in the Rye", "J.D. Salinger", "978-0-316-76948-0")
book2 = FictionBook("To Kill a Mockingbird", "Harper Lee", "978-0-06-112008-4", "Classic")
book3 = NonFictionBook("Sapiens: A Brief History of Humankind", "Yuval Noah Harari", "978-0-06-2316097", "Anthropology")


# Adding books to the library
library.add_book(book1, "Book")
library.add_book(book2, "Fiction")
library.add_book(book3, "NonFiction")

# Listing all books in the library
library.list_books()
