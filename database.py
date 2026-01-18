import sqlite3

def init_db():
    conn = sqlite3.connect("employees.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            department TEXT NOT NULL,
            salary REAL NOT NULL,
            status TEXT DEFAULT 'ACTIVE'
        )
    ''')
    conn.commit()
    conn.close()

def query_db(query, params=(), fetchone=False, fetchall=False):
    
    with sqlite3.connect("employees.db") as conn:
        cursor = conn.cursor()
        cursor.execute(query, params)
        conn.commit()
        if fetchone: return cursor.fetchone()
        if fetchall: return cursor.fetchall()
