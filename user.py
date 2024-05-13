from sql_connect import connect_db, Error

class User:
    all_users = {}                                  # Class level storing of all users ever
    current_user = "default"                        # Tracking the current user so we can hold their own specific books
    first_user = True                               # Making sure add_user works based on the first login prompt when booting
    def __init__(self, name, library_id):           # Private attributes
        self.__name = name
        self.__library_id = library_id
        self.__borrowed_books = []

    # Getter methods for private attributes
    def get_name(self):
        return self.__name

    def get_library_id(self):
        return self.__library_id

    def get_borrowed_books(self):
        return self.__borrowed_books

    # Add a user (Based on input from Operations) ------------------------
    @classmethod
    def add_user(self, name1, userid1):
        conn = connect_db()
        if conn is not None:
            try:
                cursor = conn.cursor()

                # Check if the user already exists
                query = "SELECT * FROM Users WHERE name = %s"
                cursor.execute(query, (name1, userid1))
                existing_user = cursor.fetchone()
                cursor.fetchall()                       # Prevent unread results

                # Is this NOT the first logged in user, and we already have the entered user?
                if existing_user and User.first_user == False:                          # Checking if this is the first logged in User - AKA, don't ask to switch if there's no one to switch to
                    user_switch = input("This user already exists. Would you like to switch to this user? Y or N. ").upper()

                if user_switch == 'Y':
                    print(f"User switched to {name1}.\n")
                    User.current_user = name1                                           # Let user's class-level tracking update to reflect the switch.
                    return

                else:
                    # Insert the new user
                    new_user = (name1, userid1)
                    query = "INSERT INTO Users (name, libid) VALUES (%s, %s)"
                    cursor.execute(query, new_user)
                    conn.commit()                                                                       # fully commits the changes
                    print(f"User added successfully!")
                    User.first_user = False

                    # Create a table for borrowed books for the new user if it doesn't exist
                    query = f"CREATE TABLE IF NOT EXISTS {name1}_BorrowedBooks (id INT AUTO_INCREMENT PRIMARY KEY, book_title VARCHAR(255) NOT NULL, borrow_date DATE NOT NULL)"
                    cursor.execute(query)
                    conn.commit()

                    # Now that you added it, would you like to use it?
                    user_switch = input("Would you like to switch to this user? Y or N. ").upper()

                    if user_switch == 'Y':                                                  # Basically a roundabout way of preventing duplicates.
                        print(f"User switched to {name1}.\n")
                        User.current_user = name1                                           # Let user's class-level tracking update to reflect the switch.
                        return
                    else:
                        return                                                              # It's not required.

            except Error as e:
                print(f"Error: {e}")

            finally:
                cursor.close() # Don't forget to close!
                conn.close()

    # Display user details --------------------------------------------------
    def user_details():
        print("Viewing details of current user:")
        if User.current_user in User.all_users:
            curuser = User.all_users[User.current_user]         # Pick up that one user so we can call getters on it.
            print(f"Name: {curuser.get_name()}, Library ID: {curuser.get_library_id()} \nBooks borrowed:")
            borrowed_books = curuser.get_borrowed_books()
            if borrowed_books:                                  # Do they have anything borrowed?
                for book in borrowed_books:
                    print(book)                                 # Just print its title.
            else:
                print("None borrowed\n")                        # Prevents weird blank output if they don't have anything.
        else:
            print("Current user does not exist.")               # this should not happen!


    # Search for a book ------------------------------------------------------
    def display_users():
        print("\nDisplaying all users:")
        if User.all_users:
            for name, user in User.all_users.items():
                print(f"Name: {user.get_name()}, Library ID: {user.get_library_id()}\nBooks borrowed:")
                borrowed_books = user.get_borrowed_books()
                if borrowed_books:                                # Do they have anything borrowed?
                    for book in borrowed_books:
                        print(book)                               # Just print its title.
                else:
                    print("None borrowed")                        # Prevents weird blank output if they don't have anything.
                print()                                           # Add an empty line between users for better readability
        else:
            print("There aren't any users.\n")                    # Realistically this would never trigger, though

