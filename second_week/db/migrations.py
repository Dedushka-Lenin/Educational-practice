import sqlite3


db_path = 'db/app.db'

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Comments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        message VARCHAR(255) NOT NULL,
        masterID INTEGER NOT NULL,
        requestID INTEGER NOT NULL
    );
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Requests (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        startDate DATE NOT NULL,
        climateTechType VARCHAR(255),
        climateTechModel VARCHAR(255),
        problemDescryption VARCHAR(255),
        requestStatus VARCHAR(255) NOT NULL,
        completionDate DATE,
        repairParts VARCHAR(255),
        masterID INTEGER NOT NULL,
        clientID INTEGER NOT NULL
    );
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fio VARCHAR(255),
        phone INTEGER NOT NULL,
        login VARCHAR(255),
        password VARCHAR(255),
        type VARCHAR(255)
    );
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS token (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        token VARCHAR(255) NOT NULL
    );
""")

conn.commit()
conn.close()