import math


def equacao(a, b, c):
    delta = b**2 -4*a*c
    if delta < 0:
        return print('Equação não possui raizes reais!')
    x1 = ((-b)+ math.sqrt(delta))/2*a
    x2 = ((-b)- math.sqrt(delta))/2*a
    print(f'Delta vale', delta)
    return print(f'x1 vale {x1}\nx2 vale {x2}')


def verificacao(delta):
    if delta == 0:
        return print(f'Equação possui apenas uma raiz real!') 


a = int(input('Informe o valor de A: '))
if a == 0:
    print('Esta equação não é do 2° Grau!')
    
else:
    b = int(input('Informe o valor de B: '))
    c = int(input('Informe o valor de C: '))
    delta = b**2 -4*a*c


    verificacao(delta)
    equacao(a, b, c)