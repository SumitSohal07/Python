#Name:Sumit Sohal, StudentId: C0902846
# Program: Add, search, borrow and return books in a library (LMS).

import os

# Menu-function
def Menu():
    print("Library Management System")
    print("1. Display All Books")
    print("2. Add book")
    print("3. Borrow book")
    print("4. Search book")
    print("5. Return book")
    print("6. Exit")
    return input("Please enter your choice: ")

#Function to insert book
def Add(library):
    bookname = input("Enter Book Name: ")
    bookauthor = input("Enter Book Author: ")
    bookid = generate_bookid(library)
    availability = AVAILABLE
    library.append({'bookid': bookid,'bookname': bookname,'bookauthor': bookauthor,'availability': availability})
    save_library(library, filename)
    print(f"Book {bookid} added to the library successfully.")
def generate_bookid(library):
    if not library:
        return 1
    else:
        return int(max(book['bookid'] for book in library)) + 1

# This function saves library data to the file
def save_library(library, filename):
    with open(filename, 'w') as file:
        for book in library:
            file.write(f"{book['bookid']},{book['bookname']},{book['bookauthor']},{book['availability']}\n")

#This function loads library data from the file
def load_library(filename):
    library = []
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            for line in file:
                bookid, bookname, bookauthor, availability = line.strip().split(',')
                library.append({'bookid': bookid, 'bookname': bookname, 'bookauthor': bookauthor, 'availability': availability})
    return library


#This function searches the book
def Search(library):
    bookname = input("Enter the name of the book to search: ")
    found_book = [book for book in library if book['bookname'] == bookname]

    if found_book:
        print("\nBook Found:")
        for book in found_book:
            print(
                f"Book ID: {book['bookid']},Book Name: {book['bookname']}, Author: {book['bookauthor']}, Availability: {book['availability']}")
    else:
        print("\nBook not found.")

#This function is to borrow book
def Borrow(library):
    bookname = input("Enter the name of the book to borrow: ")
    for book in library:
        if book['bookname'] == bookname and book['availability'] == AVAILABLE:
            book['availability'] = BORROWED
            save_library(library,filename)
            print(f"\nYou have succesfully borrowed '{bookname}' from the library.\n")
            return
    print("Book already borrowed/can't find.")

#This function is to return book to the library
def Return(library):
    bookname = input("Enter the name of the book to return: ")
    for book in library:
        if book['bookname'] == bookname and book['availability'] == BORROWED:
            book['availability'] = AVAILABLE
            save_library(library, filename)
            print(f"You have returned '{bookname}' to the library.")
            return
    print("Book not found or not borrowed.")


#This function is to display all the books in the library
def Display(library):
    if not library:
        print("\nEmpty Library.\n")
    else:
        print("\n------------------ Books list ------------------\n")
        for book in library:
            print(f"BookId: {book['bookid']},BookName: {book['bookname']}, Author: {book['bookauthor']}, Availability: {book['availability']}\n")

filename = "library_db.txt"
AVAILABLE = 'yes'
BORROWED = 'no'

def main():
    library = load_library("library_db.txt")
    while True:
        choice = Menu()
        if choice == '1':
            Display(library)
        elif choice == '2':
            Add(library)
        elif choice == '3':
            Borrow(library)
        elif choice == '4':
            Search(library)
        elif choice == '5':
            Return(library)
        elif choice == '6': break
        else: print("\nPlease enter correct input.\n")

main()