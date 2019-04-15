#app/main/controlelr/user.py
from . import *


class UserAPI(MethodView):

    def post(self):
        return jsonify('post'), 200