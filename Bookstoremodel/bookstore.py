class Book:
    def __init__(self, title, author, price):
        """
        #Constructor for the Book class.

        :param title: A string representing the title of the book.
        :param author: A string representing the author of the book.
        :param price: A float representing the price of the book.
        """
        self.title = title
        self.author = author
        self.price = price

    def display_book_details(self):
        """
        Method to display the details of the book.
        """
        print(f"Book Details:\nTitle: {self.title}\nAuthor: {self.author}\nPrice: ${self.price:.2f}")

# Example usage:

# Creating OBJECTS/ instance of the Book class
my_book = Book("1984", "George Orwell", 15.99)

# Displaying the details of the book
my_book.display_book_details()