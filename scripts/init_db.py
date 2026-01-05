import sqlite3
from dotenv import load_dotenv
import os

load_dotenv()

def create_database():
    conn = sqlite3.connect(os.getenv("DATABASE_PATH"))
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cards (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            card_id TEXT UNIQUE,
            card_number TEXT,
            year TEXT,
            brand TEXT,
            set_name TEXT,
            card_name TEXT,
            team TEXT,
            parallel_insert TEXT DEFAULT 'Base',
            quantity INTEGER DEFAULT 1,
            is_graded BOOLEAN,
            grader TEXT,
            grade REAL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS transaction_history (
            trans_id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            card_id INTEGER,
            value REAL,
            FOREIGN KEY (card_id) REFERENCES card(card_id)
        )
    ''')

    conn.commit()
    conn.close()
    print("'value_history.db' created successfully with Card and Transaction tables.")

if __name__ == "__main__":
    create_database()