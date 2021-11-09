import hashlib

from ORM.usuario import User
from ORM.ENV import *

class ConUser():
    @classmethod
    def validate(cls, name, email, password):
        if len(name) > 50 or len(name) < 2:
            return 101
        elif len(email) > 100:
            return 102
        elif len(password) < 6 or len(password) > 20:
            return 103
        else:
            return 0
    @classmethod
    def exists(cls, email):
        if len(ConUser.search(email=email)) == 0:
            return 0
        else:
            return 104
    @classmethod
    def search(cls, **kargs):
        session = connection()
        users = session.query(User).all()
        for key, value in kargs.items():
            if key == 'id':
                users = list(filter(lambda user: user.id == value, users))
            if key == 'nome':
                users = list(filter(lambda user: user.name == value, users))
            if key == 'email':
                users = list(filter(lambda user: user.email == value, users))
        return users

    @classmethod
    def add(cls, nome: str, email: str, senha: str):
        session = connection()
        test = ConUser.validate(nome, email, senha)
        if test != 0:
            return test
        test = ConUser.exists(email)
        if test != 0:
            return test
        senha = hashlib.sha256(senha.encode()).hexdigest()
        user = User(name=nome, email=email, password=senha)
        session.add(user)
        session.commit()
        session.rollback()
        return 0
