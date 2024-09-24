import sqlite3

# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect('db.db')
cursor = conn.cursor()

# Delete teams with id bigger or equal to 11
cursor.execute('''
DELETE FROM teams WHERE id >= 11
''')

# Commit the changes and close the connection
conn.commit()
conn.close()