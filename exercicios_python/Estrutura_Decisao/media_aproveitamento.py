nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))
nota3 = float(input('Informe a terceira nota: '))
nota4 = float(input('Informe a quarta nota: '))
media = (nota1 + nota2 + nota3 + nota4)/4
if media < 4 and media > 0:
    aproveitamento = 'E'
elif media >=4 and media < 6:
    aproveitamento = 'D'
elif media >=6 and media < 7.5:
    aproveitamento = 'C'
elif media >=7.5 and media < 9:
    aproveitamento = 'B'
elif media >=9 and media < 10:
    aproveitamento = 'A'
else:
    print('Entrada Inválida!')
if aproveitamento == 'A' or aproveitamento == 'B' or aproveitamento == 'C':
    print('Aprovado!')
elif aproveitamento == 'D' or aproveitamento == 'E':
    print('Reprovado!')
print(f'Sua média: {media}')
print(f'Média de aproveitamento: {aproveitamento}')
print('Conceito:')
print('Entre 9.0 e 10.0\nA')
print('Entre 7.5 e 9.0\nB')
print('Entre 6.0 e 7.5\nC')
print('Entre 4.0 e 6.0\nD')
print('Entre zero e 4.0\nE')