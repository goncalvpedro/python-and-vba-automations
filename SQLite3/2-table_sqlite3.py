import sqlite3

# Connecting to the database file. If the file does not exist, it will be created.
connection = sqlite3.connect('qrcode-readings.db')


# Creating a cursor object, which allows us to execute SQL queries
cursor = connection.cursor()

# Creating a table
cursor.execute('''
    CREATE TABLE qrcodes(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               code_sequence TEXT NOT NULL,
               pn_client TEXT NOT NULL,
               client TEXT NOT NULL,
               marker TEXT NOT NULL,
               intraday_seq TEXT NOT NULL,
               date TEXT NOT NULL

    );
''')

print('Table created successfully.')
connection.close()