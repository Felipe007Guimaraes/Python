numero = int(input('Insira um número menor que 1000: '))
if numero >= 1000:
    print('Inválido, número maior ou igual a 1000!')
elif numero < 0:
    print('Insira um número positivo!')
elif numero < 10:
    numero = str(numero)
    print(f'Centenas: 0\nDezenas:  0\nUnidades: {numero[0]}')
elif numero < 100:
    numero = str(numero)
    print(f'Centenas: 0\nDezenas:  {numero[0]}\nUnidades: {numero[1]}')
else:
    numero = str(numero)
    print(f'Centenas: {numero[0]}\nDezenas:  {numero[1]}\nUnidades: {numero[2]}')
