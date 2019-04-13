#app/main/controlelr/user.py
from . import *

@user_blue.route('/')
def test_user():
    return 'hello_world', 200