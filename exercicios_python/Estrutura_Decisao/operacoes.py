numero = float(input('Insira um valor: '))
print('Qual a operação que deseja realizar\nA-Par ou Impar\nB-Positivo ou Negativo\nC-Inteiro ou Decimal')
opcoes = input()
opcoes = opcoes.upper()
if opcoes == 'A':
    if numero%2==0:
        print('É par')
    else:
        print('É impar')
elif opcoes == 'B':
    if numero>0:
        print('É positivo!')
    elif numero == 0:
        print('0 é neutro')
    else:
        print('É negativo')
elif opcoes == 'C':
    if numero//1 == numero:
        print('Número inteiro')
    else:
        print('Número decimal')
else:
    print('Opção inválida!')