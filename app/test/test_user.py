# app/test/test_user.py
from . import *
class TestUser:

    def test_user(self, flask_client):
        res = flask_client.get('/')
        resp = json.loads(res.get_data())
        assert res.status_code == 200
        assert resp == 'hello_world'

    def test_post_user(selfk, flask_client):
        url = '/user'
        res = flask_client.post(url)
        assert res.status_code == 200