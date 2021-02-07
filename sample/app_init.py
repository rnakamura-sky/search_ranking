import sqlite3
import datetime
from sample.config import app_config
import sample.operate as operate



def db_init():
    conn = operate.get_db()
    cursor = conn.cursor()

    cursor.execute(
        'CREATE TABLE IF NOT EXISTS keyword('
        'id INTEGER PRIMARY KEY AUTOINCREMENT,'
        'text STRING,'
        'del INTEGER DEFAULT 0'
        ');'
    )

    cursor.execute(
        'CREATE TABLE IF NOT EXISTS statistics('
        'date DATE,'
        'key_id INTEGER,'
        'rank INTEGER,'
        'page INTEGER,'
        'rank_in_page INTEGER'
        ')'
    )

    conn.close()

def create_test_data(dbname):
    conn = sqlite3.connect(dbname)
    cursor = conn.cursor()

    cursor.execute(
        'INSERT INTO keyword VALUES (?, ?, ?);',
        (1, 'TEST', '0')
    )
    key_id = cursor.lastrowid
    cursor.execute(
        'INSERT INTO statistics VALUES (?, ?, ?, ?, ?);',
        (datetime.datetime.now().date(), key_id, 1, 1, 1)
    )

    conn.commit()
    conn.close()



if __name__ == '__main__':
    db_init()
    # create_test_data(DB_NAME)
