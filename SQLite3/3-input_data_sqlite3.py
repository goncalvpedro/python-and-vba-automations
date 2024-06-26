import sqlite3

connection = sqlite3.connect('qrcode-readings.db')

cursor = connection.cursor()

cursor.execute('''
    INSERT INTO qrcodes 
               ''')