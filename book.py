from sql_connect import connect_db, Error

class Book:
    all_books = {}
    def __init__(self, title, author, isbn, genre, pubdate):        # Private attribute definition
        self.__title = title
        self.__author = author
        self.__isbn = isbn
        self.__genre = genre
        self.__pubdate = pubdate
        self.__avail = True

    # Getter methods for private attributes
    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_isbn(self):
        return self.__isbn

    def get_genre(self):
        return self.__genre

    def get_pubdate(self):
        return self.__pubdate

    def is_available(self):
        return self.__avail

    # Setter method for availability
    def set_availability(self, status):
        self.__avail = status


   # Add a book (Based on input from Operations) ------------------------
    @classmethod

    # Remember to:  Check dupes
    def add_book(self, title1, author1, isbn1, genre1, pubdate1):
        conn = connect_db()
        if conn is not None:
            try:
                cursor = conn.cursor()

                # Check if the book already exists
                query = "SELECT * FROM Books WHERE title = %s AND author = %s"
                cursor.execute(query, (title1, author1))
                existing_book = cursor.fetchone()

                if existing_book:
                    print("A book with the same title and author already exists.")
                else:
                    # Insert the new book
                    new_book = (title1, author1, isbn1, genre1, pubdate1)
                    insert_query = "INSERT INTO Books (title, author, isbn, genre, publication_date) VALUES (%s, %s, %s, %s, %s)"
                    cursor.execute(insert_query, new_book)
                    conn.commit()                       # fully commits the changes
                    print(f"Book added successfully!")

            except Error as e:
                print(f"Error: {e}")


    # Borrow a book ------------------------------------------------------
    def borrow_book():
        print("Which book would you like to borrow? ")
        book_title = input("Please enter its title: ")  # We're storing books by title, so look for that.

        if book_title in Book.all_books:                # Is it actually in the library?
            book = Book.all_books[book_title]
            if book.is_available():
                book.set_availability(False)                                         # Mark the book as borrowed if it is.
                User.all_users[User.current_user].get_borrowed_books().append(book_title)     # Append the title of the book to the list of borrowed books PER specific user.
                print(f"{book_title} has been borrowed.\n")                          # Let the user know what they did.
            else:
                print(f"{book_title} has already been borrowed.\n")                  # Is the book already unavailable?
        else:
            print(f"'{book_title}' is not in the library.\n")                        # We don't even have that book.

    # Return a book ------------------------------------------------------
    def return_book():
        print("Which book would you like to return? ")
        book_title = input("Please enter its title: ")  # We're storing books by title, so look for that.

        if book_title in Book.all_books:                # Is it actually in the library?
            book = Book.all_books[book_title]
            if not book.is_available():
                if book_title in User.all_users[User.current_user].get_borrowed_books():                # Did the current user actually borrow this book? Can't return what you don't have.
                    book.set_availability(True)                                                         # Mark the book as returned.
                    User.all_users[User.current_user].get_borrowed_books().remove(book_title)           # Remove the book object from the list of borrowed books PER user.
                    print(f"{book_title} has been returned.\n")                                         # Let the user know what they did.
                else:
                    print("Another user borrowed this book. To return it, please switch to that user. ")
            else:
                print(f"{book_title} has already been returned.\n")                  # Is the book already available?
        else:
            print(f"'{book_title}' is not in the library.\n")                        # We don't even have that book.

    # Search for a book ------------------------------------------------------
    def search_book():
        book_title = input("Please enter the title of the book you'd like to search for: ")  # We're storing books by title, so look for that.

        if Book.all_books:
            if book_title in Book.all_books:
                book = Book.all_books[book_title]                                            # We're making it easier to get individual pieces if we have each grabbed per iteration through the loop.
                print(f"Title: {book.get_title()}, Author: {book.get_author()}, ISBN: {book.get_isbn()}, Genre: {book.get_genre()}, Publication Date: {book.get_pubdate()}, Is it available? {book.is_available()}\n")
            else:
                print(f"'{book_title}' is not in the library.\n")                            # We don't even have that book.
        else:
            print("There aren't any books in the library.\n")                                # This shouldn't happen, but...

    # Search for a book ------------------------------------------------------
    def display_book():
        print("\nDisplaying all books: ")

        conn = connect_db()
        if conn is not None:
            try:
                cursor = conn.cursor()

                # Check if the book already exists
                query = "SELECT * from Books"
                cursor.execute(query)
                for row in cursor.fetchall():
                    print(row)

                
            except Error as e:
                print(f"Error: {e}")
        else:
                print("There aren't any books in the library.\n")

from user import User       # Import User for tracking their books while we're borrowing and such.