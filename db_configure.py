# Case this file is executed, it will create the database and its tables. 
# It will create a file named tasks.db in the same directory as this file.
import sqlite3

# Connect to the database (or create if it doesn't exist)
conn = sqlite3.connect('tasks.db')
cursor = conn.cursor()

# Create tasks table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT NOT NULL,
        name TEXT NOT NULL,
        type TEXT NOT NULL,
        duration INTEGER NOT NULL
    )
''')

# Create types table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS types (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    )
''')

# Create users table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
    )
''')

# Include some default types
cursor.execute("INSERT INTO types (name) VALUES ('Work')")
cursor.execute("INSERT INTO types (name) VALUES ('Study')")
cursor.execute("INSERT INTO types (name) VALUES ('Exercise')")
cursor.execute("INSERT INTO types (name) VALUES ('4Fun')")

# Commit the changes and close the connection
conn.commit()
conn.close()