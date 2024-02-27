
import sqlite3

# Function to connect to the SQLite database
def connect_to_database():
    connection = sqlite3.connect("contact_book.db")
    cursor = connection.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS contacts
                      (ID INTEGER PRIMARY KEY AUTOINCREMENT,
                       Name TEXT,
                       CellNumber TEXT,
                       Email TEXT)''')
    return connection, cursor

# Function to insert data into the contacts table
def insert_data(connection, cursor, name, cell_number, email):
    cursor.execute("INSERT INTO contacts (Name, CellNumber, Email) VALUES (?, ?, ?)", (name, cell_number, email))
    connection.commit()

# Function to fetch and display all data from the contacts table
def display_all_data(cursor):
    cursor.execute("SELECT * FROM contacts")
    data = cursor.fetchall()
    for row in data:
        print("ID:", row[0])
        print("Name:", row[1])
        print("Cell Number:", row[2])
        print("Email:", row[3])
        print("")

# Connect to the database
connection, cursor = connect_to_database()

# Insert 5 rows of data
insert_data(connection, cursor, "FLick", "1234567890", "Flick@example.com")
insert_data(connection, cursor, "Lia", "9876543210", "Lia@example.com")
insert_data(connection, cursor, "Divya", "5551234567", "divya@example.com")
insert_data(connection, cursor, "Manasa", "9998887777", "manasa@example.com")
insert_data(connection, cursor, "Gayathri", "4445556666", "gayathri@example.com")

# Display all data
print("All Contacts:")
display_all_data(cursor)

# Close the database connection
connection.close()