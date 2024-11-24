import sqlite3

def setup_db():
    conn = sqlite3.connect('articles.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS articles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            author TEXT,
            publication TEXT,
            summary TEXT,
            sentiment TEXT
        )
    ''')
    conn.commit()
    conn.close()

setup_db()























# import sqlite3

# DATABASE = 'articles.db'

# # Initialize database
# conn = sqlite3.connect(DATABASE)
# cursor = conn.cursor()

# # Create articles table
# cursor.execute('''
# CREATE TABLE IF NOT EXISTS articles (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     title TEXT,
#     author TEXT,
#     publication TEXT,
#     summary TEXT,
#     sentiment TEXT,
#     url TEXT
# )
# ''')

# conn.commit()
# conn.close()
# print("Database setup completed!")
