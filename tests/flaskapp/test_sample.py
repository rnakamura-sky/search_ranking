from flaskapp import create_app

def test_ok_sample():
    assert 1 == 1

def test_flask_sample():
    app = create_app()
    app.config['TESTING'] = True
    client = app.test_client()
    result = client.get('/')
    assert b'Hello, World' == result.data
