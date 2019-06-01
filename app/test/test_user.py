# app/test/test_user.py
from . import *
class TestUser:
    @pytest.mark.skip(reason='first test set')
    def test_user(self, flask_client):
        res = flask_client.get('/')
        resp = json.loads(res.get_data())
        assert res.status_code == 200
        assert resp == 'hello_world'
    @pytest.mark.skip(reason='first test set')
    def test_post_user(self, flask_client):
        url = '/user'
        res = flask_client.post(url)
        assert res.status_code == 200
    @pytest.mark.skip(reason='first test set')
    def test_get_user(self,flask_client):
        url = '/api/v1/user/'
        res = flask_client.get(url)
        assert res.status_code == 200

    def test_post_user(self, flask_client):
        url = '/api/v1/user/'
        res = flask_client.post(url)
        assert res.status_code == 200