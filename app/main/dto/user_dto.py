# app/main/dto/user_dto.py
from flask_restplus import Namespace, fields

class UserRegisterDto:
    api = Namespace('user_register', description = 'User Register Data Object')
    model = api.model('user_register',{
        'user_id':fields.String(required=True, description = 'User id - recommend email'),
        'user_pw':fields.String(required=True, description = 'User password'),
        'user_pw_':fields.String(required=True, description = 'User password two'),
        'user_hobby':fields.String(required=True, description='User Hobby info')
    })

class UserDto:
    api = Namespace('UserDTO', description = 'User Data Object')
    user = api.model('user', {
        'email' : fields.String(required=True, description = 'Email'),
        'name':fields.String(required=True, description='name'),
        'hobby':fields.String(required=True, description='hobby')
    })