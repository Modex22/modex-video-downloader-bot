import sqlite3

DATABASE = "bot.db"


def connect():
    return sqlite3.connect(DATABASE)

def save_user(user):

    conn = connect()

    cursor = conn.cursor()

    cursor.execute("""
    INSERT OR IGNORE INTO users
    (
        telegram_id,
        username,
        first_name
    )

    VALUES (?, ?, ?)
    """,
    (
        user.id,
        user.username,
        user.first_name
    ))

    conn.commit()
    conn.close()

def save_download(user_id, platform, url):

    conn = connect()

    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO downloads
    (
        telegram_id,
        platform,
        url
    )

    VALUES (?, ?, ?)
    """,
    (
        user_id,
        platform,
        url
    ))

    conn.commit()
    conn.close()


def create_tables():
    conn = connect()

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        telegram_id INTEGER UNIQUE,

        username TEXT,

        first_name TEXT,

        joined_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS downloads (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        telegram_id INTEGER,

        platform TEXT,

        url TEXT,

        downloaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()