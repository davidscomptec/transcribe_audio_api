import firebase_admin
from firebase_admin import credentials, db

from Config.env_config import credenciais_firebase as credenciais, url_firebase as url

cred = credentials.Certificate(credenciais)
firebase_admin.initialize_app(cred, {
    'databaseURL': url
})

# 3. Referência ao banco de dados
ref = db.reference('/')

db_api_users = ref.child('api-users')

