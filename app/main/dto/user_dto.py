# app/main/dto/user_dto.py
from flask_restplus import Namespace, fields

class UserDto:
    api = Namespace('UserDTO', description = 'User Data Object')
    user = api.model('user', {
        'email' : fields.String(required=True, description = 'Email'),
        'name':fields.String(required=True, description='name'),
        'hobby':fields.String(required=True, description='hobby')
    })