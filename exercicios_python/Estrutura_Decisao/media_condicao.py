nota1 = float(input('Insira a primeira nota: '))
nota2 = float(input('Insira a segunda nota: '))
nota3 = float(input('Insira a terceira nota: '))
nota4 = float(input('Insira a quarta nota: '))
media = (nota1 + nota2+ nota3 + nota4)/4
if media == 10:
    print('Aprovado com Distinção!')
elif media >=7:
    print('Aprovado!')
else:
    print('Reprovado.')