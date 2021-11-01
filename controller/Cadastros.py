from ORM.usuario import User
from ORM.ENV import *

class ConUser():
    @classmethod
    def validate(cls, nome, email, senha):
        if len(nome) > 50 or len(nome) < 2:
            return 101
        elif len(email) < 10 or len(email) > 100:
            return 102
        elif len(senha) < 6 or senha > 20:
            return 103
        else:
            return 0
    @classmethod
    def exists(cls, email):
        session = connection()
        if len(session.query(User).filter_by(email=email)) == 0:
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
        if ConUser.validate(nome, email, senha) == 0 and ConUser.exists(email) == 0:
            user = User(name=nome,
                        email=email,
                        password=senha)
            session = connection()
            session.add(user)
            session.rollback()
            session.commit()
        else:
            print('Não foi possivel cadastrar!')
    @classmethod
    def editPass(cls, id, nome, senhaAtual, senhaNova):
        session = connection()
        user = session.query(User).filter(User.id == id)
        if len(user) != 0 and user.name == nome and user.password == senhaAtual:
            user[0].senha = senhaNova
            session.commit()
            return 0
        else:
            return 301



        
