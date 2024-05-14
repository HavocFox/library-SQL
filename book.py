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

   # Add a book (Based on input from Operations) ------------------------
    @classmethod

    def add_book(self, title1, author1, isbn1, genre1, pubdate1, retdate1):
        conn = connect_db()
        if conn is not None:
            try:
                cursor = conn.cursor()

                # Check if the book already exists
                query = "SELECT * FROM Books WHERE title = %s"          # Select all books that match the input title
                cursor.execute(query, (title1,))
                existing_book = cursor.fetchone()
                retdate1 = date.today().strftime('%Y-%m-%d')

                if existing_book:                                                       # Did we grab anything?
                    print("A book with the same title and author already exists.")
                else:
                    # Insert the new book
                    new_book = (title1, author1, isbn1, genre1, pubdate1, retdate1)               # If we didn't grab anything, add the new one.
                    insert_query = "INSERT INTO Books (title, author, isbn, genre, publication_date, returndate) VALUES (%s, %s, %s, %s, %s, %s)"
                    cursor.execute(insert_query, new_book)
                    conn.commit()                                                       # fully commits the changes
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
                cursor.close()                                   # Don't forget to close!
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


                if existing_book:                               # Does the book exist in the first place?
                    query = f"SELECT * FROM {name1}_BorrowedBooks WHERE book_title = %s"
                    cursor.execute(query, (book_title,))
                    user_has_book = cursor.fetchone()
                    cursor.fetchall()
 
                    if user_has_book:                           # Do you HAVE the book you are trying to return?

                        # Update the availability of the book
                        book_id = existing_book[0]
                        query = "UPDATE Books SET availability = 1 WHERE id = %s"
                        cursor.execute(query, (book_id,))
                        conn.commit()
                        # Update return date
                        retdate1 = date.today().strftime('%Y-%m-%d')
                        query = "UPDATE Books SET returndate = %s WHERE id = %s"
                        cursor.execute(query, (retdate1, book_id))

                        conn.commit()

                        # Remove the book from the user's borrowed books
                        delete_query = f"DELETE FROM {name1}_BorrowedBooks WHERE book_title = %s"
                        cursor.execute(delete_query, (book_title,))
                        conn.commit()

                        print(f"{book_title} has been returned.\n")  # Let the user know what they did.

                    else:
                        print("Another user borrowed this book. Please log into that user to return it.")
                        
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
                query = "SELECT * FROM Books WHERE title = %s"      # Grab everything from books that matches the search
                cursor.execute(query, (book_title,))
                existing_book = cursor.fetchone()
                cursor.fetchall()

                if existing_book:                                   # did our grab pick anything up? If so, go forward.
                    print("Book found!")
                    book_id = existing_book           
                    print(f"Book Details:\n----- \nName: {book_id[1]} \nAuthor: {book_id[2]}\nISBN: {book_id[3]}\nGenre: {book_id[4]}\nPublication Date (YYYY-MM-DD): {book_id[5]}\nLast Return Date (YYYY-MM-DD): {book_id[7]}")
                    if book_id[6] == 0:
                        print("Available?: No")
                    else:
                        print("Available?: Yes")

                else:
                    print("No book with that title exists.")
                
            except Error as e:
                print(f"Error: {e}")

            finally:
                cursor.close()                                      # Don't forget to close!
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

                # Select everything from Books to display but do check if anything is IN Books.
                query = "SELECT * from Books"       
                cursor.execute(query)
                allbooks = cursor.fetchall()
                if allbooks:
                    for row in allbooks:
                        print(f"\nBook Details:\n----- \nName: {row[1]} \nAuthor: {row[2]}\nISBN: {row[3]}\nGenre: {row[4]}\nPublication Date (YYYY-MM-DD): {row[5]}\nLast Return Date (YYYY-MM-DD): {row[7]}")
                        if row[6] == 0:
                            print("Available?: No")
                        else:
                            print("Available?: Yes")
                else:
                    print("No books found.")

            except Error as e:
                print(f"Error: {e}")

            finally:
                cursor.close()          # Don't forget to close!
                conn.close()
                                
        else:
                print("There aren't any books in the library.\n")

from user import User       # Import User for tracking their books while we're borrowing and such.