#app/main/controlelr/user.py
from . import *

@user_api_md.route('/')
class UserAPI(Resource):
    def get(self):
        return jsonify('get'), 200
        
    def post(self):
        return jsonify('post'), 200