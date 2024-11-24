from flask import Flask, render_template, request
from newspaper import Article
from textblob import TextBlob
import sqlite3
import os

app = Flask(__name__, static_url_path='/static')

# Database setup
def init_db():
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

# Home Route to Summarize Articles
@app.route('/', methods=['GET', 'POST'])
def index():
    title = None
    author = None
    publication = None
    summary = None
    sentiment = None

    if request.method == 'POST':
        url = request.form.get('url')
        article = Article(url)
        article.download()
        article.parse()
        article.nlp()

        # Perform sentiment analysis
        analysis = TextBlob(article.text)

        # Get article details
        title = article.title
        author = ', '.join(article.authors)
        publication = article.publish_date if article.publish_date else "Unknown"
        summary = article.summary
        sentiment = f'Polarity: {analysis.polarity}, Sentiment: {"positive" if analysis.polarity > 0 else "negative" if analysis.polarity < 0 else "neutral"}'

        # Save article in database
        conn = sqlite3.connect('articles.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO articles (title, author, publication, summary, sentiment)
            VALUES (?, ?, ?, ?, ?)
        ''', (title, author, publication, summary, sentiment))
        conn.commit()
        conn.close()

    return render_template('index.html', title=title, author=author, publication=publication, summary=summary, sentiment=sentiment)

# History Route to View Summarized Articles
@app.route('/history')
def history():
    conn = sqlite3.connect('articles.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM articles')
    rows = cursor.fetchall()
    conn.close()

    return render_template('history.html', rows=rows)

if __name__ == '__main__':
    init_db()  # Initialize the database
    # Use the PORT from environment variable for Render deployment
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)























# from flask import Flask, render_template, request
# from newspaper import Article
# from textblob import TextBlob
# import sqlite3

# app = Flask(__name__, static_url_path='/static')

# # Database setup
# def init_db():
#     conn = sqlite3.connect('articles.db')
#     cursor = conn.cursor()
#     cursor.execute('''
#         CREATE TABLE IF NOT EXISTS articles (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             title TEXT,
#             author TEXT,
#             publication TEXT,
#             summary TEXT,
#             sentiment TEXT
#         )
#     ''')
#     conn.commit()
#     conn.close()

# # Home Route to Summarize Articles
# @app.route('/', methods=['GET', 'POST'])
# def index():
#     title = None
#     author = None
#     publication = None
#     summary = None
#     sentiment = None

#     if request.method == 'POST':
#         url = request.form.get('url')
#         article = Article(url)
#         article.download()
#         article.parse()
#         article.nlp()

#         # Perform sentiment analysis
#         analysis = TextBlob(article.text)

#         # Get article details
#         title = article.title
#         author = ', '.join(article.authors)
#         publication = article.publish_date if article.publish_date else "Unknown"
#         summary = article.summary
#         sentiment = f'Polarity: {analysis.polarity}, Sentiment: {"positive" if analysis.polarity > 0 else "negative" if analysis.polarity < 0 else "neutral"}'

#         # Save article in database
#         conn = sqlite3.connect('articles.db')
#         cursor = conn.cursor()
#         cursor.execute('''
#             INSERT INTO articles (title, author, publication, summary, sentiment)
#             VALUES (?, ?, ?, ?, ?)
#         ''', (title, author, publication, summary, sentiment))
#         conn.commit()
#         conn.close()

#     return render_template('index.html', title=title, author=author, publication=publication, summary=summary, sentiment=sentiment)

# # History Route to View Summarized Articles
# @app.route('/history')
# def history():
#     conn = sqlite3.connect('articles.db')
#     cursor = conn.cursor()
#     cursor.execute('SELECT * FROM articles')
#     rows = cursor.fetchall()
#     conn.close()

#     return render_template('history.html', rows=rows)

# if __name__ == '__main__':
#     init_db()  # Initialize the database
#     app.run(debug=True)


















# import sqlite3
# from flask import Flask, render_template, request
# from newspaper import Article
# from textblob import TextBlob

# app = Flask(__name__, static_url_path='/static')

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     title = None
#     author = None
#     publication = None
#     summary = None
#     sentiment = None

#     if request.method == 'POST':
#         url = request.form.get('url')
#         article = Article(url)
#         article.download()
#         article.parse()
#         article.nlp()

#         # Perform sentiment analysis
#         analysis = TextBlob(article.text)

#         # Get article details
#         title = article.title
#         author = ', '.join(article.authors)
#         publication = article.publish_date if article.publish_date else "Unknown"
#         summary = article.summary
#         sentiment = f'Polarity: {analysis.polarity}, Sentiment: {"positive" if analysis.polarity > 0 else "negative" if analysis.polarity < 0 else "neutral"}'

#         # Insert the article into the database
#         conn = sqlite3.connect('articles.db')
#         cursor = conn.cursor()
#         cursor.execute('''
#             INSERT INTO articles (title, author, publication, summary, sentiment, url)
#             VALUES (?, ?, ?, ?, ?, ?)
#         ''', (title, author, publication, summary, sentiment, url))
#         conn.commit()
#         conn.close()

#     return render_template('index.html', title=title, author=author, publication=publication, summary=summary, sentiment=sentiment)


# @app.route('/history')
# def history():
#     # Connect to the database and fetch articles
#     conn = sqlite3.connect('articles.db')
#     cursor = conn.cursor()
#     cursor.execute('SELECT * FROM articles ORDER BY id DESC;')  # Fetch articles in descending order by ID
#     rows = cursor.fetchall()
#     conn.close()

#     return render_template('history.html', articles=rows)


# if __name__ == '__main__':
#     app.run(debug=True)





# from flask import Flask, render_template, request, redirect
# from newspaper import Article
# from textblob import TextBlob
# import sqlite3
# import os

# app = Flask(__name__, static_url_path='/static')

# # Database file
# DATABASE = 'articles.db'

# # Function to connect to the database
# def get_db_connection():
#     conn = sqlite3.connect(DATABASE)
#     conn.row_factory = sqlite3.Row
#     return conn

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     title = None
#     author = None
#     publication = None
#     summary = None
#     sentiment = None

#     if request.method == 'POST':
#         url = request.form.get('url')
#         try:
#             # Article extraction
#             article = Article(url)
#             article.download()
#             article.parse()
#             article.nlp()

#             # Sentiment analysis
#             analysis = TextBlob(article.text)
#             sentiment = f'Polarity: {analysis.polarity}, Sentiment: {"positive" if analysis.polarity > 0 else "negative" if analysis.polarity < 0 else "neutral"}'

#             # Get article details
#             title = article.title or "No title available"
#             author = ', '.join(article.authors) or "Unknown author"
#             publication = article.publish_date if article.publish_date else "Unknown"
#             summary = article.summary or "No summary available"

#             # Save to database
#             conn = get_db_connection()
#             conn.execute(
#                 'INSERT INTO articles (title, author, publication, summary, sentiment, url) VALUES (?, ?, ?, ?, ?, ?)',
#                 (title, author, publication, summary, sentiment, url)
#             )
#             conn.commit()
#             conn.close()

#         except Exception as e:
#             return render_template('index.html', error=f"Error summarizing article: {str(e)}")

#     return render_template('index.html', title=title, author=author, publication=publication, summary=summary, sentiment=sentiment)

# @app.route('/history')
# def history():
#     conn = get_db_connection()
#     articles = conn.execute('SELECT * FROM articles ORDER BY id DESC').fetchall()
#     conn.close()
#     return render_template('history.html', articles=articles)

# if __name__ == '__main__':
#     if not os.path.exists(DATABASE):
#         print(f"Database not found! Run 'setup_db.py' to initialize.")
#     app.run(debug=True)
