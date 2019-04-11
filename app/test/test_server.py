# test/test_server.py
from .conftest import  *

class TestServer:

    def test_run_server(self):
        app = create_app('dev')
        app_context = app.app_context()
        app_context.push()
        assert app_context is not None
    
    def test_server_dev(self):
        app = create_app('dev')
        assert app.config['DB']['addr'] == 'dev_host'
    
    def test_server_test(self):
        app = create_app('test')
        assert app.config['DB']['addr'] == 'test_host'
    