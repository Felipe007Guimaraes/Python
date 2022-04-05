nome = input('Informe um nome com mais de 3 caracteres:\n')
while len(nome) <= 3:
    print('Nome precisa ser maior!')
    nome = input('Informe um nome com mais de 3 caracteres:\n')
idade = int(input('Informe a idade\ndeve ser maior que 0 e menor que 150\n'))
while (idade < 0 ) or (idade > 150):
    print('Idade inválida!')
    idade = int(input('Informe a idade\ndeve ser maior que 0 e menor que 150\n'))
salario = float(input('Informe agora o salario\nLembrando que deve ser maior que 0.\n'))
while salario < 0:
    print('Salário inválido!')
    salario = float(input('Informe agora o salario\nLembrando que deve ser maior que 0.\n'))
sexo = input('Informe o sexo:\nF para feminino e M para masculino').upper()
while (sexo != 'F') or (sexo != 'M'):
    if sexo == 'F':
        sexo = 'Feminino'
        break
    elif sexo == 'M':
        sexo = 'Masculino'
        break
    print('Sexo Inválido!')
    sexo = input('Informe o sexo:\nF para feminino e M para masculino').upper()

estado_Civil = input('Informe o estado civíl agora:\nS- Solteiro(a)\nC- Casado(a)\nV- Viúvo(a)\nD- Divorciado(a)').upper()
while estado_Civil != 'S' or estado_Civil != 'C' or estado_Civil != 'V' or estado_Civil != 'D':
    if estado_Civil == 'S':
        estado_Civil = 'Solteiro'
        break
    elif estado_Civil == 'C':
        estado_Civil = 'Casado'
        break
    elif estado_Civil == 'V':
        estado_Civil = 'Viúvo'
        break
    elif estado_Civil == 'D':
        estado_Civil = 'Divorciado'
        break
    print('Estado civil inválido!')
    estado_Civil = input('Informe o estado civíl agora:\nS- Solteiro(a)\nC- Casado(a)\nV- Viúvo(a)\nD- Divorciado(a)\n').upper()

print(f'Nome: {nome}\nIdade: {idade}\nSalário: {salario:.2f}\nSexo: {sexo}\nEstado civil: {estado_Civil}')
