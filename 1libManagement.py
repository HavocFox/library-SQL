from sql_connect import connect_db, Error

from book import Book
from user import User
from author import Author
from menu import Menu
from datetime import date




# MAIN CODE ------------------------------------

print("\nConnecting to database...")
conn = connect_db()
if conn is not None:
            try:
                cursor = conn.cursor()
                print("MySQL Database connection successful!")
                print("-------------------------------------------\n")

            except Error as e:
                print(f"Error: {e}")

print("Welcome to the Library Management System!")
while True:
    tempuser = input("Please log in. Enter your username: ")        # This is so we don't start with no users in the database. We always need one to track.
    if ' ' in tempuser:
        print("Invalid username. Please enter a username without spaces.")
    else:
        tempid = input("Enter your library ID: ")                   # Enter as a string since we don't need to use it as an integer ever.
        if tempid.isdigit():                                        # We can still check if it's digits.
            User.add_user(tempuser, tempid)
            User.current_user = tempuser                            # Set tracked user to the one that just logged in.
            print(f"\nWelcome, {User.current_user}.\n")
            Menu.main_menu()
            break
        else:
            print("Invalid ID. Please enter a valid ID.")
    print(f"\nWelcome, {User.current_user}.\n")                     # Welcome the user that just logged in
    Menu.main_menu()                                                # Now we call the menus to display. From here we don't use this .py anymore
    break




# SQL Library has been attached for a base library of books and authors.
