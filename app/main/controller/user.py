#app/main/controlelr/user.py
from . import *

@user_reg_api.route('/')
class UserModel(Resource):
    @user_reg_api.expect(user_dto_register)
    def post(self):
        obj = user_reg_api.payload
        set_user(obj)
        return 'success', 201

    @user_reg_api.marshal_list_with(user_dto_register, code=203,envelope='userObj')
    def get(self):
        obj = get_all_user()
        return obj

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

