# app/main/dto/user_dto.py
from flask_restplus import Namespace, fields

class UserDto:
    api = Namespace('testuser_dto', description = 'User for Test, Swagger')
    user = api.model('user', {
        'email' : fields.String(required=True, description = 'User Email'),
        'name':fields.String(required=True, description='user name')
    })