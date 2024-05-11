from sql_connect import connect_db, Error
import re
# Only using RegEx here.
# This module is used for operations that take input or are more complicated to run inside the respective classes.

class Operations:
# BOOK OPERATIONS ----------------------------------------------
    # Add a book:
    def add_book():
        title = input("Please enter the book's title. ")
        author = input("Please enter the book's author. ")
        while True:
                isbn = input("Please enter the book's ISBN. ")                                   # We don't need to manipulate the ISBN, so we can let it be a string.
                if len(isbn) not in (10, 13) or not isbn.isdigit():                              # ISBNs seem to usually be 10 or 13 digits in length and are digits.
                    print("Please enter a valid ISBN.")
                else:
                    break

        genre = input("Please enter the book's genre. ")
        while True:
                pubdate = input("Please enter the book's publication date (YYYY-MM-DD). ")
                if not re.match(r"\d{4}-\d{2}-\d{2}$", pubdate):                                # Let's make sure the publication date is actually something that makes sense.
                    print("Please enter a valid date in the format YYYY-MM-DD.")
                else:
                     break

        print("Adding book... \n")
        Book.add_book(title, author, isbn, genre, pubdate)                                      # Call book.py's Add function with the data we just got.

    # Borrow a book: > Refer to book.py.
    # Return a book: > Refer to book.py.
    # Search for a book: > Refer to book.py.
    # Display books: > Refer to book.py.

    #--------------------------------------------------------------
    # USER OPERATIONS ----------------------------------------------
    # Add a user:
    def add_user():
        name = input("Please enter the user's name. ")
        while True:
            userid = input("Please enter the user's library ID. ")                    # I don't know what this library's IDs are usually like, so we're just restricting them to being digits without length rules.
            if userid.isdigit():
                 break
            else:
                 print("Please enter a valid ID. ")

        print("Adding user... \n")
        User.add_user(name, userid)                                                   # Call user.py's Add function with the data we just got.

    # Refer to user.py for display users and display current user details.

    #--------------------------------------------------------------
    # AUTHOR OPERATIONS ----------------------------------------------
    # Add an author:
    def add_author():
        name = input("Please enter the author's name. ")
        authorbio = input("Please enter the author's biography. ")


        print("Adding author... \n")
        Author.add_author(name, authorbio)                                            # Call author.py's Add function with the data we just got.

    # Refer to author.py for display authors and display author details.


# Import other classes so we can use their Add functions. Menu is here just in case we need to add something referring to it later.
from menu import Menu
from book import Book
from author import Author
from user import User