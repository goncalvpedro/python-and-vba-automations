import sqlite3

connection = sqlite3.connect('qrcode-readings.db')

print(connection.total_changes)