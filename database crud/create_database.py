import sqlite3

# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect('../db.db')
cursor = conn.cursor()

# Add facilities column to the teams table
cursor.execute('''
ALTER TABLE teams ADD COLUMN facilities INTEGER
''')


# Commit the changes and close the connection
conn.commit()
conn.close()