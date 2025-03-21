import sqlite3

def init_db():
    conn = sqlite3.connect("security.db")
    cursor = conn.cursor()
    
    # Création des tables
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT,
                        role TEXT,
                        encoding BLOB)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS access_logs (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT,
                        status TEXT,
                        timestamp TEXT)''')

    conn.commit()
    conn.close()

def get_connection():
    return sqlite3.connect("security.db")

# Initialiser la base au lancement
init_db()
