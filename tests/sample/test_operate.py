import datetime
import sample.operate
from sample.model import Keyword, Statistics


def test_simple():
    result = 1
    expected = 1

    assert result == expected

def test_get_keyword_list(db):
    keywords = sample.operate.get_keyword_list()
    assert len(keywords) == 0

def test_regist_key(db):
    keyword = Keyword()
    keyword.text = 'TEST'
    keyword = sample.operate.regist_key(keyword)

    conn = sample.operate.get_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM keyword;')
    rows = cursor.fetchall()
    results = []
    for row in rows:
        results.append(dict(row))
    conn.close()
    assert len(results) == 1

    result_row = results[0]
    assert result_row['id'] == keyword.id
    assert result_row['text'] == keyword.text
    assert result_row['del'] == keyword.delete

def test_regist_statistics(db):
    keyword = Keyword()
    keyword.text = 'TEST'

    keyword = sample.operate.regist_key(keyword)

    statistics = Statistics(keyword)

    today = datetime.date.today()
    statistics.date = today
    statistics.rank = 1
    statistics.page = 1
    statistics.page_in_rank = 1

    result = sample.operate.regist_statistics(statistics)
    assert result == statistics

    conn = sample.operate.get_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM statistics;')
    rows = cursor.fetchall()
    results = []
    for row in rows:
        results.append(dict(row))
    conn.close()

    assert len(results) == 1
    result_row = results[0]
    assert result_row['date'] == statistics.date
    assert result_row['key_id'] == statistics.keyword.id
    assert result_row['rank'] == statistics.rank
    assert result_row['rank'] == statistics.page
    assert result_row['rank_in_page'] == statistics.rank_in_page


