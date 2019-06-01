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
        data =  {"user_id": "string",
                "user_pw": "string",
                "user_pw_": "string",
                "user_hobby": "string"}
        res = flask_client.post(url, data=json.dumps(data), headers = {'content-type':'application/json'})
        assert res.status_code == 201
    
    def test_get_user(self, flask_client):
        url = '/api/v1/user/'
        res = flask_client.get(url)
        assert res.status_code == 200
        print(res.get_data())