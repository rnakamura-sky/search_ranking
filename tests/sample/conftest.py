import pytest
from sample.config import app_config
import sample.app_init

@pytest.fixture()
def db(tmpdir):
    p = tmpdir.join('test.db')
    db_path = str(p)
    app_config.db_name = db_path
    sample.app_init.db_init()

    