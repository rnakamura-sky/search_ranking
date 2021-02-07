DROP TABLE IF EXISTS keyword;
DROP TABLE IF EXISTS statistics;

CREATE TABLE IF NOT EXISTS keyword(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    text STRING,
    del INTEGER DEFAULT 0 NOT NULL
);

CREATE TABLE IF NOT EXISTS statistics(
    date DATE,
    key_id INTEGER NOT NULL,
    rank INTEGER,
    page INTEGER,
    rank_in_page INTEGER,
    FOREIGN KEY (key_id) REFERENCES keyword (id)
);
