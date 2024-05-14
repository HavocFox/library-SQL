from sql_connect import connect_db, Error
from datetime import date

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
                    conn.commit()                                    # fully commits the changes
                    print(f"Book added successfully!")

            except Error as e:
                print(f"Error: {e}")

            finally:
                cursor.close() # Don't forget to close!
                conn.close()


    # Borrow a book ------------------------------------------------------
    def borrow_book():
        print("Which book would you like to borrow? ")
        book_title = input("Please enter its title: ")  # We're storing books by title, so look for that.

        conn = connect_db()
        if conn is not None:
            try:
                cursor = conn.cursor()

                # Check if the book exists and is available
                query = "SELECT * FROM Books WHERE title = %s AND availability = 1"
                cursor.execute(query, (book_title,))
                existing_book = cursor.fetchone()
                cursor.fetchall()

                if existing_book:
                    name1 = User.current_user
                    # Update the availability of the book
                    book_id = existing_book[0]
                    query = "UPDATE Books SET availability = 0 WHERE id = %s"
                    cursor.execute(query, (book_id,))
                    conn.commit()

                    # Add to the user's borrowed books
                    query = f"INSERT INTO {name1}_BorrowedBooks (book_title) VALUES (%s)"
                    cursor.execute(query, (book_title,))
                    conn.commit()

                    print(f"{book_title} has been borrowed.\n")  # Let the user know what they did.
                else:
                    print("No book with that title exists or your book has already been borrowed.\n")

            except Error as e:
                print(f"Error: {e}")

            finally:
                cursor.close() # Don't forget to close!
                conn.close()

        else:
            print("Failed to connect to the database.")




    # Return a book ------------------------------------------------------
    def return_book():
        print("Which book would you like to return? ")
        book_title = input("Please enter its title: ")  # We're storing books by title, so look for that.

        conn = connect_db()
        if conn is not None:
            try:
                cursor = conn.cursor()
                name1 = User.current_user

                # Check if the book exists and is NOT available
                query = "SELECT * FROM Books WHERE title = %s AND availability = 0"
                cursor.execute(query, (book_title,))
                existing_book = cursor.fetchone()
                cursor.fetchall()

                if existing_book:
                    # Update the availability of the book
                    book_id = existing_book[0]
                    query = "UPDATE Books SET availability = 1 WHERE id = %s"
                    cursor.execute(query, (book_id,))
                    conn.commit()

                    # Remove the book from the user's borrowed books
                    delete_query = f"DELETE FROM {name1}_BorrowedBooks WHERE book_title = %s"
                    cursor.execute(delete_query, (book_title,))
                    conn.commit()

                    print(f"{book_title} has been returned.\n")  # Let the user know what they did.
                else:
                    print("No book with that title exists or your book has already been returned.\n")

            except Error as e:
                print(f"Error: {e}")

            finally:
                cursor.close() # Don't forget to close!
                conn.close()

        else:
            print("Failed to connect to the database.")

    # Search for a book ------------------------------------------------------
    def search_book():
        book_title = input("Please enter the title of the book you'd like to search for: ")  # We're storing books by title, so look for that.

        conn = connect_db()
        if conn is not None:
            try:
                cursor = conn.cursor()

                # Check if the book exists and is NOT available
                query = "SELECT * FROM Books WHERE title = %s"
                cursor.execute(query, (book_title,))
                existing_book = cursor.fetchone()
                cursor.fetchall()

                if existing_book:
                    print("Book found!")
                    book_id = existing_book[0]
                    print(f"Book ID: {book_id}")

                else:
                    print("No book with that title exists.")
                
            except Error as e:
                print(f"Error: {e}")

            finally:
                cursor.close() # Don't forget to close!
                conn.close()
                                
        else:
                print("There aren't any books in the library.\n")

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
                if cursor.fetchall():
                    for row in cursor.fetchall():
                        print(row)
                else:
                    print("No books found.")

            except Error as e:
                print(f"Error: {e}")

            finally:
                cursor.close() # Don't forget to close!
                conn.close()
                                
        else:
                print("There aren't any books in the library.\n")

from user import User       # Import User for tracking their books while we're borrowing and such.