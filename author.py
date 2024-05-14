from sql_connect import connect_db, Error

class Author:
    all_authors = {}                            # Class-level dictionary of every author added.
    def __init__(self, name, biography):        # Private attributes
        self.__name = name
        self.__biography = biography


    # Add an author (Based on input from Operations) ------------------------
    @classmethod
    def add_author(self, name1, bio1):

        conn = connect_db()
        if conn is not None:
            try:
                cursor = conn.cursor()

                # Check if the author already exists
                query = "SELECT * FROM Authors WHERE name = %s AND bio = %s"
                cursor.execute(query, (name1, bio1))
                existing_auth = cursor.fetchone()

                if existing_auth:
                    print("This author is already present in the database.")
                else:
                    # Insert the new author
                    new_auth = (name1, bio1)
                    insert_query = "INSERT INTO Authors (name, bio) VALUES (%s, %s)"
                    cursor.execute(insert_query, new_auth)
                    conn.commit()                                    # fully commits the changes
                    print(f"Author added successfully!")

            except Error as e:
                print(f"Error: {e}")

            finally:
                cursor.close() # Don't forget to close!
                conn.close()

    # Display author details ------------------------------------------------------
    def auth_details():
        auth_choice = input("What author do you want to view the details of? ")     # Using name as key.
        conn = connect_db()
        if conn is not None:
            try:
                cursor = conn.cursor()

                # Check if the author exists
                query = "SELECT * FROM Authors WHERE name = %s"
                cursor.execute(query, (auth_choice,))
                existing_auth = cursor.fetchone()
                cursor.fetchall()


                if existing_auth:
                    print("Author found!")
                    auth_id = existing_auth
                    print(f"Author Details: \nName: {auth_id[1]} \nBiography: {auth_id[2]} \n")

                else:
                    print("That author could not be found.")
                
            except Error as e:
                print(f"Error: {e}")

            finally:
                cursor.close() # Don't forget to close!
                conn.close()
                                
        else:
                print("There aren't any authors in the database.\n")


    # Display all authors ------------------------------------------------------
    def display_authors():
        print("\nDisplaying all authors:\n")

        conn = connect_db()
        if conn is not None:
            try:
                cursor = conn.cursor()

                # Select all authors to display
                query = "SELECT * from Authors"
                cursor.execute(query)
                authors = cursor.fetchall()
                if authors:
                    for row in authors:
                        print(f"Author Details: \nName: {row[1]} \nBiography: {row[2]} \n")
                else:
                    print("No authors could be found.")

            except Error as e:
                print(f"Error: {e}")

            finally:
                cursor.close() # Don't forget to close!
                conn.close()
                                
        else:
                print("There aren't any authors in the database.\n")