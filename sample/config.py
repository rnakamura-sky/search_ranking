class AppConfig:
    def __init__(self, mode='production'):
        self.mode = mode
        self.db_name = 'scraping.db'

app_config = AppConfig()
