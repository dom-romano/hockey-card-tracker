import sqlite3

def create_database():
    conn = sqlite3.connect('data\\value_history.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS card (
            card_id INTEGER PRIMARY KEY AUTOINCREMENT,
            year TEXT,
            set_name TEXT,
            card_name TEXT,
            parallel TEXT DEFAULT 'Base',
            insert_set TEXT,
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