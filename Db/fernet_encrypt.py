from cryptography.fernet import Fernet

from Config.env_config import fernet_key

key = fernet_key.encode()

f = Fernet(key)


def encrypt_text(text: str):
    text_encoded = text.encode()
    encrypted_text_encoded = f.encrypt(text_encoded)
    encrypted_text = encrypted_text_encoded.decode()

    return encrypted_text

def decrypt_text(encrypted_text: str):
    encrypted_text_encoded = encrypted_text.encode()
    text_encoded = f.decrypt(encrypted_text_encoded)
    text = text_encoded.decode()

    return text