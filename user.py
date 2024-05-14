from sql_connect import connect_db, Error

class User:
    all_users = {}                                  # Class level storing of all users ever
    current_user = "default"                        # Tracking the current user so we can hold their own specific books
    first_user = True                               # Making sure add_user works based on the first login prompt when booting
    def __init__(self, name, library_id):           # Private attributes
        self.__name = name
        self.__library_id = library_id
        self.__borrowed_books = []


    # Add a user (Based on input from Operations) ------------------------
    @classmethod
    def add_user(self, name1, userid1):
        conn = connect_db()
        if conn is not None:
            try:
                cursor = conn.cursor()

            # Check if the user already exists
                query = "SELECT * FROM Users WHERE name = %s AND libid = %s"
                cursor.execute(query, (name1, userid1))
                existing_user = cursor.fetchone()
                cursor.fetchall()

            # Is this NOT the first logged in user, and we already have the entered user?
                if existing_user and not User.first_user:       # Checking if this is not the first logged in user
                    user_switch = input("This user already exists. Would you like to switch to this user? Y or N. ").upper()

                    if user_switch == 'Y':
                        print(f"User switched to {name1}.\n")
                        User.current_user = name1               # Update current user
                        return

                else:
                # Insert the new user
                    query = "INSERT INTO Users (name, libid) VALUES (%s, %s)"
                    cursor.execute(query, (name1, userid1))
                    conn.commit()                               # fully commit the changes
                    if User.first_user == False:
                        print(f"User added successfully!")      # Flavor. Keep it out if it's the first time since a diff. message goes with that.
                    else:
                        pass

                # Create a table for borrowed books for the new user if it doesn't exist
                    name1_formatted = name1.replace(" ", "_").lower()       # SQL can't make tables with spaces or capital letters. So we format to make sure it's an accepted name.
                    query = f"CREATE TABLE IF NOT EXISTS {name1_formatted}_BorrowedBooks (id INT AUTO_INCREMENT PRIMARY KEY, book_title VARCHAR(255) NOT NULL)"     # we FURTHER format it to be lowercase.
                    cursor.execute(query)
                    conn.commit()

                # Now that you added it, would you like to use it?
                    if not User.first_user:
                        user_switch = input("Would you like to switch to this user? Y or N. ").upper()

                        if user_switch == 'Y':
                            print(f"User switched to {name1}.\n")
                            User.current_user = name1  # Update current user
                            return
                    else:
                        User.current_user = name1
                        print("Introductory user added successfully.")
                        User.first_user = False
                        return                         # This is our first time logging in.

            except Error as e:
                print(f"Error: {e}")

            finally:
                cursor.close()                         # Don't forget to close!
                conn.close()


    # Display user details --------------------------------------------------
    def user_details():
        print("\nViewing details of current user: ")

        conn = connect_db()
        if conn is not None:
            try:
                cursor = conn.cursor()
                nameget = User.current_user

                # Find the user that matches you to show the details.
                query = "SELECT * FROM Users WHERE name = %s"
                cursor.execute(query, (User.current_user,))
                existing_user = cursor.fetchone()
                cursor.fetchall()

                if existing_user:
                    print(f"\nUser Details:\nName: {existing_user[1]}\nLibrary ID: {existing_user[2]}")

                    # Retrieve borrowed books for the current user
                    query = f"SELECT * FROM {User.current_user}_BorrowedBooks"
                    cursor.execute(query)
                    borrowed_books = cursor.fetchall()
                    if borrowed_books:
                        print("Borrowed books:")
                        for book_row in borrowed_books:
                            print(f"{book_row[1]}\n")
                    else:
                        print("No borrowed books.")

                else:
                    print("Something went wrong, but did not trigger an exception. Try checking your semantics.")
                
            except Error as e:
                print(f"Error: {e}")

            finally:
                cursor.close() # Don't forget to close!
                conn.close()
                                
        else:
                print("Failed to connect.\n")

    # Search for a book ------------------------------------------------------
    def display_users():
        print("\nDisplaying all users:")
    
        conn = connect_db()
        if conn is not None:
            try:
                cursor = conn.cursor()

                query = "SELECT * FROM Users"
                cursor.execute(query)
                for user_row in cursor.fetchall():
                    user_name = user_row[1]          # Assuming name is in the second column
                    user_id = user_row[2]
                    print(f"\nUser Details:\nName:{user_name}\nLibrary ID: {user_id}")
                
                    # Retrieve borrowed books for the current user
                    query = f"SELECT * FROM {user_name}_BorrowedBooks"
                    cursor.execute(query)
                    borrowed_books = cursor.fetchall()

                    if borrowed_books:
                        print("Borrowed books:")
                        for book_row in borrowed_books:
                            print(f"{book_row[1]}\n")
                    else:
                        print("No borrowed books.")

            except Error as e:
                print(f"Error: {e}")

            finally:
                cursor.close()                        # Don't forget to close!
                conn.close()

        else:
            print("Failed to connect to the database.")


