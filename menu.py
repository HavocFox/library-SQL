from sql_connect import connect_db, Error

class Menu:

    # Display book menu and enable choices based on numeric selection.
    @staticmethod     # During debugging and minor AI error checking - this came up - kept it, but debating whether to remain using it in the future. Will we learn this?
    def book_menu():
        print("\n----------------------------------------------------------")
        while True:
            print("\nBook Operations:")
            print("     1. Add a new book\n     2. Borrow a book\n     3. Return a book\n     4. Search for a book\n     5. Display all books\n     6. Back to main menu")
            try:
                bookchoice = int(input("Please enter a numeric selection. "))       # Try to catch weird entries. We DO need to have ints here.
            except ValueError:
                print("Please enter a valid numeric selection.\n")
            else:                                                                   # Call the function within the appropriate class if choice is valid.
                if bookchoice == 1:
                    print("\nYou have chosen to add a book.")
                    Operations.add_book()
                if bookchoice == 2:
                    print("\nYou have chosen to borrow a book.")
                    Book.borrow_book()
                if bookchoice == 3:
                    print("\nYou have chosen to return a book.")
                    Book.return_book()
                if bookchoice == 4:
                    print("\nYou have chosen to search for a book.")
                    Book.search_book()
                if bookchoice == 5:
                    print("\nYou have chosen to display all books.")
                    Book.display_book()
                if bookchoice == 6:
                    return True         # Return to main menu
                if bookchoice < 1 or bookchoice > 6:
                    print("Please enter a valid numeric selection.\n")

    # Display user menu and enable choices based on numeric selection.
    def user_menu():
        print("\n----------------------------------------------------------")

        while True:
            print("\nUser Operations:")
            print("     1. Add a new user\n     2. View user details\n     3. Display all users\n     4. Back to main menu")
            try:
                userchoice = int(input("Please enter a numeric selection. "))       # Try to catch weird entries. We DO need to have ints here.
            except ValueError:
                print("Please enter a valid numeric selection.\n")
            else:                                                                   # Call the function within the appropriate class if choice is valid.
                if userchoice == 1:
                    print("\nYou have chosen to add a user. ")
                    Operations.add_user()
                if userchoice == 2:
                    print("\nYou have chosen to view the current user's details. ")
                    User.user_details()
                if userchoice == 3:
                    print("\nYou have chosen to display all users. ")
                    User.display_users()
                if userchoice == 4:
                    return True         # Return to main menu
                if userchoice < 1 or userchoice > 4:
                    print("Please enter a valid numeric selection.\n")

    # Display author menu and enable choices based on numeric selection.
    def author_menu():
        print("\n----------------------------------------------------------")

        while True:
            print("\nAuthor Operations:")
            print("     1. Add a new author\n     2. View author details\n     3. Display all authors\n     4. Back to main menu")
            try:
                authchoice = int(input("Please enter a numeric selection. "))       # Try to catch weird entries. We DO need to have ints here.
            except ValueError:
                print("Please enter a valid numeric selection.\n")
            else:                                                                   # Call the function within the appropriate class if choice is valid.
                 if authchoice == 1:
                    print("\nYou have chosen to add an author. ")
                    Operations.add_author()
                 if authchoice == 2:
                    print("\nYou have chosen to view an author's details. ")
                    Author.auth_details()
                 if authchoice == 3:
                    print("\nYou have chosen to display all authors. ")
                    Author.display_authors()
                 if authchoice == 4:
                    return True         # Return to main menu
                 if authchoice < 1 or authchoice > 4:
                    print("Please enter a valid numeric selection.\n")


    # Display main menu. Calls on intro but we can return to it.
    def main_menu():
        while True:
            print("\nMain Menu: \n     1. Book Operations\n     2. User Operations\n     3. Author Operations\n     4. Quit")
            try:
                mainchoice = int(input("Please enter a numeric selection. "))       # Try to catch weird entries. We DO need to have ints here.
            except ValueError:
                print("That is not a valid numeric selection.\n")
            else:                                                                   # Call the correct menu to display if choice is valid.
                if mainchoice == 1:
                    Menu.book_menu()
                if mainchoice == 2:
                    Menu.user_menu()
                if mainchoice == 3:
                    Menu.author_menu()
                if mainchoice == 4:
                    conn = connect_db()
                    cursor = conn.cursor()
                    if conn and conn.is_connected():
                        cursor.close()
                        conn.close()                                                # ALWAYS MAKE SURE YOU CLOSE YOUR CONNECTION WHEN DONE
                        print("MySQL Connection Closed")
                        break                                                       # Maybe closing it here was redundant, but better safe than sorry?
                if mainchoice < 1 or mainchoice > 4:
                    print("Please enter a valid numeric selection.\n")

from operations import Operations       # We only need Operations here because here is where we transition to getting user input for adding entries to our classes.
from book import Book
from user import User
from author import Author
from menu import Menu