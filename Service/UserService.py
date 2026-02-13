import uuid

from starlette import status
from starlette.exceptions import HTTPException

from Db.fernet_encrypt import encrypt_text, decrypt_text
from Db.firebase import db_api_users, ref
from Models.Adm import CreateUserResponse
from Models.User import User

ROLES = ["ADM", "USER"]

def add_user(client_id: str, roles: str, user: User):
    if "ADM" not in user.roles:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuário sem permissão para criar usuários")

    roles = roles.upper().replace(' ', '')
    roles_split = roles.split(',')

    for role in roles_split:
        if role not in ROLES:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Role '{}' não é válida".format(role)
            )

    user_exist = ref.child('api-users').child(client_id).get()

    if user_exist is not None:
        print('Usuário não criado, ClienteID já utilizado')
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="client_id já cadastrado"
        )
    else:
        user_client_scret = str(uuid.uuid4())
        client_secret_to_database = encrypt_text(user_client_scret)
        db_api_users.child(client_id).set({
            'client_secret': client_secret_to_database,
            'roles': roles_split
        })
        return CreateUserResponse(client_id=client_id, client_secret=user_client_scret, roles=roles)

def get_user_client_id(cliente_id: str):
    user_exist = db_api_users.child(cliente_id).get()

    if user_exist is not None:
        return user_exist

    else:
        raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Usuário não encontrado"
            )

def get_all_user():
    user_list = ref.child('api-users').get()
    for user in user_list:
        user_list[user]['client_secret'] = decrypt_text(user_list[user]['client_secret'])

    return user_list
