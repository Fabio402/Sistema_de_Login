from controller.Login import *
from controller.Cadastros import *
def login():
    email = input('E-mail: ').lower()
    senha = input('Senha: ')
    ans = Login.check(email, senha)
    if isinstance(ans, User):
        print(f'Olá {ans.name}, bem vindo!')
        while True:
            op = int(input('1- Alterar sua senha\n'
                       '0- Sair'))
            if op == 1:
                senha = input('Senha atual: ')
                novaSenha = input('Nova senha: ')
                novaSenha2 = input('Digite a nova senha mais uma vez: ')
                if novaSenha == novaSenha2:
                    ans = Login.alter(ans, senha, novaSenha)
                    if ans == 0:
                        print('Senha alterada')
                    else:
                        print(f'Erro {ans}')
            elif op == 0:
                break
            else:
                print('Opção invalida!')
    else:
        print(f'Erro {ans}')

def cadastrar():
    nome = input('Nome: ')
    email = input('E-mail: ').lower()
    senha = input('Senha: ')
    ans = ConUser.add(nome, email, senha)
    if ans == 0:
        print('Cadastro efetuado com sucesso')
    else:
        print(f'Erro {ans}')

def main():
    print('Bem vindo ao sistema de login!\n\n')
    while True:
        op =int(input('Menu:\n'
                      '1- Login\n'
                      '2- Cadastrar\n'
                      '0- Sair\n'))
        if op == 1:
            login()
        elif op == 2:
            cadastrar()
        elif op == 0:
            break
        else:
            print('Opção inválida!')
if __name__ == '__main__':
    main()