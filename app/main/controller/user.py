#app/main/controlelr/user.py
from . import *
@userApi.route('/')
@userApi.doc(
        responses={
            201: 'Success',
            400: 'Missing parameter',
            403: 'Insufficient permissions',
            500: 'Internal failure',
        },
    )
class UserAPI(Resource):
    
    # @userApi.doc(params={'id': 'An ID'})
    @userApi.marshal_list_with(dto_user, envelope='data')
    def get(self):
        """ summary : Get the user data from DB"""
        return get_all_user()

    @userApi.param('test', 'Some description')
    def post(self):
        """ summary : register User data from client """
        return 'POST'