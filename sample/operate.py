import datetime
import sqlite3

from .model import Keyword, Statistics
from .config import app_config

def convert_date(date_str):
    d = datetime.datetime.strptime(date_str.decode('utf-8'), '%Y-%m-%d')
    return datetime.date(d.year, d.month, d.day)

sqlite3.register_adapter(datetime.date, str)
sqlite3.register_converter('DATE', convert_date)

def get_db():
    conn = sqlite3.connect(app_config.db_name, detect_types=sqlite3.PARSE_DECLTYPES)
    conn.row_factory = sqlite3.Row
    return conn

def regist_key(keyword: Keyword):
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute(
        'INSERT INTO keyword(text, del) VALUES (?, ?);',
        (keyword.text, keyword.delete)
    )

    key_id = cursor.lastrowid
    keyword.id = key_id

    conn.commit()
    conn.close()

    return keyword

def get_keyword_list():
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute(
        'SELECT * FROM keyword;'
    )

    rows = cursor.fetchall()

    results_dict = []
    for row in rows:
        results_dict.append(dict(row))
    conn.close()


    results = []
    for r in results_dict:
        k = Keyword()
        k.id = r['id']
        k.text = r['text']
        k.delet = r['del']
        results.append(k)
    
    return results


def regist_statistics(stat):
    key_id = stat.keyword.id

    conn = get_db()
    cursor = conn.cursor()

    cursor.execute(
        'INSERT INTO statistics VALUES(?, ?, ?, ?, ?);',
        (stat.date, key_id, stat.rank, stat.page, stat.rank_in_page)
    )
    conn.commit()
    conn.close()
    return stat