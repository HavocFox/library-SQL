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

        if name1 in self.all_users:
            user_switch = input("This user already exists. Would you like to switch to this user? Y or N. ").upper()    # We already have this user, so are you trying to log into it?
            if user_switch == 'Y':                                                                                      # Basically a roundabout way of preventing duplicates.
                print(f"User switched to {name1}.\n")
                User.current_user = name1                    # Let user's class-level tracking update to reflect the switch.
                return
        new_user = User(name = name1, library_id = userid1)  # Create a new Book object
        self.all_users[name1] = new_user                     # Add the book to the dictionary with title as key

        print("User added successfully!\n")
        if User.first_user == True:                          # Checking if this is the first logged in User - AKA, don't ask to switch if there's no one to switch to
            User.first_user = False                          # Now we can switch if this is called again
            return
        else:
            switchchoice = input("Would you like to switch to this user? Y or N. ").upper()         # Basically "Now that we added this user, wanna use it?"
            if switchchoice == 'Y':
                print(f"User switched to {name1}.\n")
                User.current_user = name1                                                           # Let user's class-level tracking update to reflect the switch.

                return
            else:
                return                                       # You don't have to switch, though.

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

