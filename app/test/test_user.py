# app/test/test_user.py
class TestUser:

    def test_user(self, flask_client):
        res = flask_client.get('/')
        assert res.status_code == 200