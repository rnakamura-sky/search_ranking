import sample.config

def test_config():
    conf = sample.config.app_config
    assert conf.mode == 'production'
    assert conf.db_name == 'scraping.db'
