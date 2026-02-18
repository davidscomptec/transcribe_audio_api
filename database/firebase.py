import firebase_admin
from firebase_admin import credentials, db

from config.env import credenciais_firebase as credenciais, url_firebase as url, users_child_api

cred = credentials.Certificate(credenciais)
firebase_admin.initialize_app(cred, {
    'databaseURL': url
})

# 3. Referência ao banco de dados
ref = db.reference('/')

db_api_users = ref.child(users_child_api)

