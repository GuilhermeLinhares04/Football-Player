import sqlite3

# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect('db.db')
cursor = conn.cursor()

# Delete countries table
cursor.execute('''
DROP TABLE countries
''')

# Commit the changes and close the connection
conn.commit()
conn.close()