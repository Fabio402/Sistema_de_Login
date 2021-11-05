from controller.Cadastros import *
from controller.Senhas import *
from ORM.usuario import *
class Login():
    @classmethod
    def check(cls, email, password):
        if ConUser.exists(email) == 104:
            pessoas = ConUser.search(email=email)
            if len(pessoas) == 1:
                pessoa = pessoas[0]
                key = pessoa.nome+pessoa.email
                if ConCrypt.decode(pessoa.password, key) == password:
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
            if ConCrypt.encode(senha) == pessoa.password:
                session = connection()
                user = session.query(User).filter(User.id == pessoa.id).all()
                key = pessoa.nome+pessoa.email
                user[0].senha = ConCrypt.encode(novaSenha, key)
                session.commit()
                return 0
            else:
                return 302
        except:
            return 301

