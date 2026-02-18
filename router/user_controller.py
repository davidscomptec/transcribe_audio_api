from fastapi import APIRouter, Depends

from service.token_service import auth_login, is_adm
from service.user_service import get_user_client_id, get_all_user, add_user
from models.adm import CreateUserRequest, CreateUserResponse

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
        return user_found
    return None


@user.get("/get")
def get_all_users(auth_user = Depends(auth_login)):
    if is_adm(auth_user):
        user_list = get_all_user()
        return user_list

    return None