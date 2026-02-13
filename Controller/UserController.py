from fastapi import APIRouter, Depends

from Db.fernet_encrypt import decrypt_text
from Service.TokenService import auth_login, is_adm
from Service.UserService import get_user_client_id, get_all_user, add_user
from Models.Adm import CreateUserRequest, CreateUserResponse

user = APIRouter(tags=["Usuários"], prefix="/user")

@user.post("/create", response_model=CreateUserResponse)
def create_user(request: CreateUserRequest, auth_user = Depends(auth_login)):
    if is_adm(auth_user):
        new_user = add_user(request.client_id, request.roles, auth_user)
        return new_user

    return None

@user.get("/get/{client_id}")
def get_user_by_client_id(client_id: str, auth_user = Depends(auth_login)):
    if is_adm(auth_user):
        user_found = get_user_client_id(client_id)
        user_found['client_secret'] = decrypt_text(user_found['client_secret'])
        return user_found
    return None


@user.get("/get")
def get_all_users(auth_user = Depends(auth_login)):
    if is_adm(auth_user):
        user_list = get_all_user()
        return user_list

    return None