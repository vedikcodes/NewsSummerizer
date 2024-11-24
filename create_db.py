import sqlite3

# Connect to the database (it will create 'articles.db' if it doesn't exist)
conn = sqlite3.connect('articles.db')
cursor = conn.cursor()

# Create the 'articles' table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS articles (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        author TEXT,
        publication TEXT,
        summary TEXT,
        sentiment TEXT,
        url TEXT
    );
''')

# Commit changes and close the connection
conn.commit()
conn.close()

print("Database and table created successfully.")
