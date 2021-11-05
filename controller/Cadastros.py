from ORM.usuario import User
from ORM.ENV import *
from controller.Senhas import *

class ConUser():
    @classmethod
    def validate(cls, nome, email, senha):
        if len(nome) > 50 or len(nome) < 2:
            return 101
        elif len(email) > 100:
            return 102
        elif len(senha) < 6 or len(senha) > 20:
            return 103
        else:
            return 0
    @classmethod
    def exists(cls, email):
        aux = ConUser.search(email=email)
        user = User(aux.id, aux.email, aux.name, aux.password)
        if len(user) == 0:
            return 0
        else:
            return 104
    @classmethod
    def search(cls, **kargs):
        session = connection()
        users = session.query(User)
        for key, value in kargs.items():
            if key == 'id':
                users.filter(User.id == value)
            if key == 'nome':
                users = users.filter(User.name == value)
            if key == 'email':
                users = users.filter(User.email == value)
        return users
    @classmethod
    def add(cls, nome, email, senha):
        print('função')
        if ConUser.validate(nome, email, senha) == 0:
            print('if')
            if ConUser.exists(email) == 0:
                print('to no if')
                key = nome+email
                senha = ConCrypt.encode(senha, key)
                print('hash feita')
                user = User(nome, email, senha)
                print('usuario')
                session = connection()
                print('Conectado')
                session.add(user)
                print('add')
                session.rollback()
                session.commit()
                print('Commit')
                return 0
        else:
            return 105
