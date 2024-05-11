from sql_connect import connect_db, Error

from book import Book
from user import User
from author import Author
from menu import Menu





# MAIN CODE ------------------------------------
# Base book dictionary setup
Book.add_book("To Kill a Mockingbird", "Harper Lee", "9780061120084", "Classic", "1960-07-11")
Book.add_book("1984", "George Orwell", "9780451524935", "Science Fiction", "1949-06-08")
Book.add_book("The Catcher in the Rye", "J.D. Salinger", "9780316769488", "Coming-of-Age", "1951-07-16")
Book.add_book("Pride and Prejudice", "Jane Austen", "9780141439518", "Romance", "1813-01-28")
Book.add_book("Harry Potter and the Sorcerer's Stone", "J.K. Rowling", "9780590353427", "Fantasy", "1997-06-26")

# Base author dictionary setup
Author.add_author("Harper Lee", "Nelle Harper Lee was an American novelist whose 1960 novel To Kill a Mockingbird won the 1961 Pulitzer Prize and became a classic of modern American literature. She assisted her close friend Truman Capote in his research for the book In Cold Blood. Her second and final novel, Go Set a Watchman, was an earlier draft of Mockingbird that was published in July 2015 as a sequel.")

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