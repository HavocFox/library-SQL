from sql_connect import connect_db, Error

from book import Book
from user import User
from author import Author
from menu import Menu
from datetime import date




# MAIN CODE ------------------------------------

# Base author dictionary setup
Author.add_author("Harper Lee", "Nelle Harper Lee was an American novelist whose 1960 novel To Kill a Mockingbird won the 1961 Pulitzer Prize and became a classic of modern American literature. She assisted her close friend Truman Capote in his research for the book In Cold Blood. Her second and final novel, Go Set a Watchman, was an earlier draft of Mockingbird that was published in July 2015 as a sequel.")

print("\nConnecting to database...")
conn = connect_db()
if conn is not None:
            try:
                cursor = conn.cursor()
                print("MySQL Database connection successful!")
                print("-------------------------------------------\n")

            except Error as e:
                print(f"Error: {e}")

print("Welcome to the Library Management System! ")
tempuser = input("Please log in. Enter your username: ")        # This is so we don't start with no users in the database. We always need one to track.
while True:
    tempid = input("Enter your library ID: ")                   # Enter as a string since we don't need to use it as an integer ever.
    if tempid.isdigit():                                        # We can still check if it's digits.
        User.add_user(tempuser, tempid)
        User.current_user = tempuser                            # Set tracked user to the one that just logged in.
        break
    else:
       print("Invalid ID. Please enter a valid ID.")

print(f"\nWelcome, {User.current_user}.\n")                     # Welcome the user that just logged in
Menu.main_menu()                                                # Now we call the menus to display. From here we don't use this .py anymore

# THINGS TO REMEMBER (delete when submitting)
    # Add some default books
    # Add some default authors

    # Am I able to submit the SQL library I made or do I need to create tables within the program?
    # Checking for duplicate entries
    # Checking for correctly formatted entries
    # Fix the weird datetime thing
    # How do we get all the garbage entries out of the table?
    # Should we still track the current user's books? CAN we? Might need to create a table per user.