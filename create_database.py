import sqlite3

# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect('db.db')
cursor = conn.cursor()

# Create the 'continents' table
cursor.execute('''
CREATE TABLE IF NOT EXISTS continents (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
)
''')

# Create the 'countries' table
cursor.execute('''
CREATE TABLE IF NOT EXISTS countries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    continent_id INTEGER,
    name TEXT NOT NULL,
    strength INTEGER NOT NULL,
    FOREIGN KEY (continent_id) REFERENCES continents (id)
)
''')

# Create the 'teams' table
cursor.execute('''
CREATE TABLE IF NOT EXISTS teams (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    country_id INTEGER,
    strength INTEGER NOT NULL,
    money INTEGER NOT NULL,
    FOREIGN KEY (country_id) REFERENCES countries (id)
)
''')

# Commit the changes and close the connection
conn.commit()
conn.close()