import math 
area = float(input('Informe quantos Metros quadrados serão pintados: '))
cobertura = area/6
quantidade_latas = cobertura/18
quantidade_galoes = cobertura/3.6
print(f'Serão necessárias {cobertura:.2f} litros de tinta para pintar {area} metros!')
print(f'Comprando apenas latas serão necessários {math.ceil(quantidade_latas)} galões!')
print(f'Comprando apenas galões serão necessários {math.ceil(quantidade_galoes)} galões!')
