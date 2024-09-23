import sqlite3

# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect('db.db')
cursor = conn.cursor()

# # Add countries
# cursor.execute('''
# INSERT INTO countries (continent_id, name, strength) VALUES
# (1, 'Germany', 84),
# (1, 'France', 92),
# (1, 'Spain', 92),
# (2, 'Brazil', 88),
# (2, 'Argentina', 94)
# ''')

cursor.execute('''
INSERT INTO teams (name, country_id, strength, money) VALUES
('Bayern Munich', 1, 90, 100000000),
('Borussia Dortmund', 1, 85, 50000000),
('Paris Saint-Germain', 2, 92, 100000005),
('Monaco', 2, 85, 50000000),
('Real Madrid', 3, 94, 200000000),
('Barcelona', 3, 92, 150000000),
('Flamengo', 4, 85, 50000000),
('Santos', 4, 80, 30000000),
('Boca Juniors', 5, 88, 80000000),
('River Plate', 5, 85, 50000000)
''')

# Commit the changes and close the connection
conn.commit()
conn.close()