from cryptography.fernet import Fernet
class ConCrypt:
    @classmethod
    def encode(cls, password, key):
        f = Fernet(key)
        token = f.encrypt(password)
        return token

    @classmethod
    def decode(cls, token, key):
        f = Fernet(key)
        password = f.decrypt(token)
        return password
