# app/service/user_service.py
USER_DATA_OBJ = []

def get_all_user():
    global USER_DATA_OBJ
    return USER_DATA_OBJ

def set_user(user_dto):
    global USER_DATA_OBJ
    USER_DATA_OBJ.append(user_dto)
