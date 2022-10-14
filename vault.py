import sqlite3
def init_database ():
    with sqlite3.connect("password_vault.db") as db:
        cursor = db.cursor()
    cursor.execute("""
            CREATE TABLE IF NT EXIST master(
            id INTEGER PRIMARY KEY,
            password TEXT NOT NULL);
            """)

    cursor.execute("""
            CREATE TABLE IF NT EXIST vault(
            id INTEGER PRIMARY KEY,
            platform    TEXT NOT NULL,
            userid  TEXT NOT NULL,
            password TEXT NOT NULL);
            """)
    
    return db