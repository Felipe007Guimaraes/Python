import math 
area = float(input('Informe quantos Metros quadrados serão pintados: '))
cobertura = area/6
quantidade = cobertura/18
print(f'Serão necessárias {cobertura:.2f} litros de tinta, {math.ceil(quantidade)} latas para pintar {area} metros!')



