class User:
    def __init__(self, client_id, client_secret, roles):
        self.client_id = client_id
        self.client_secret = client_secret
        self.roles = roles or []