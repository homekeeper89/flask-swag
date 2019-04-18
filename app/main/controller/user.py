#app/main/controlelr/user.py
from . import *

@user_api_md.route('/')
class UserAPI(Resource):
    def get(self):
        return 'GET'
        
    def post(self):
        return 'POST'