from sql_connect import connect_db, Error

class Author:
    all_authors = {}                            # Class-level dictionary of every author added.
    def __init__(self, name, biography):        # Private attributes
        self.__name = name
        self.__biography = biography

    # Getter methods for private attributes
    def get_name(self):
        return self.__name

    def get_biography(self):
        return self.__biography

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
                    # Insert the new book
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
                    print("Book found!")
                    auth_id = existing_auth[0]
                    print(f"Author Details: {auth_id}")

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
        print("\nDisplaying all authors: ")

        conn = connect_db()
        if conn is not None:
            try:
                cursor = conn.cursor()

                query = "SELECT * from Authors"
                cursor.execute(query)
                if cursor.fetchall():
                    for row in cursor.fetchall():
                        print(row)
                else:
                    print("No authors could be found.")

            except Error as e:
                print(f"Error: {e}")

            finally:
                cursor.close() # Don't forget to close!
                conn.close()
                                
        else:
                print("There aren't any authors in the database.\n")