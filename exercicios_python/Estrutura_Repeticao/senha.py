user = input('Insira um nome de usuário\n')
senha = input('Insira uma senha:\n')
while senha == user:
    print('Erro\nSenha deve ser diferente de usuário')
    user = input('Insira um nome de usuário\n')
    senha = input('Insira uma senha:\n')
print(f'Bem vindo, {user}')
