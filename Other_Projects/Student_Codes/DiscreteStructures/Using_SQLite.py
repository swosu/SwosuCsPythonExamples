import sqlite3

# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect('example.db')

# Create a cursor object
cursor = conn.cursor()

# Create a table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    password TEXT NOT NULL
)
''')

# Insert data into the table
users = [
    ('Alice', 'password123'),
    ('Bob', 'securepass'),
    ('Charlie', 'mypassword'),
    ('David', 'passw0rd'),
    ('Eve', '12345')
]

cursor.executemany('''
INSERT INTO users (name, password) VALUES (?, ?)
''', users)

# Commit the changes
conn.commit()

# Query data from the table
cursor.execute('SELECT * FROM users')
rows = cursor.fetchall()

# Print the results
for row in rows:
    print(row)

# Close the connection
conn.close()
