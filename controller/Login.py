from controller.Cadastros import *
from ORM.usuario import *
class Login():
    @classmethod
    def check(cls, email, password):
        if ConUser.exists(email) == 104:
            pessoas = ConUser.search(email=email)
            if len(pessoas) == 1:
                pessoa = pessoas[0]
                if hashlib.sha256(password.encode()).hexdigest() == pessoa.password:
                    return pessoa
                else:
                    return 202
            else:
                return 203
        else:
            return 201
    @classmethod
    def alter(cls, pessoa: User,senha, novaSenha):
        try:
            if hashlib.sha256(senha.encode()).hexdigest() == pessoa.password:
                session = connection()
                user = session.query(User).filter(User.id == pessoa.id).all()
                user[0].password = hashlib.sha256(novaSenha.encode()).hexdigest()

                session.commit()
                return 0
            else:
                return 302
        except:
            return 301

