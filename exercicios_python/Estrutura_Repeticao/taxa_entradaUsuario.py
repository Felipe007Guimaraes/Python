print('Iniciando')
a = int(input('Informe a quantidade de habitantes da população A:'))
taxaA = 80000 * 0.03
print('Taxa de crescimento da população A = 3%')
b = int(input('Informe a quantidade de hábitantes da população B:'))
taxaB = 200000 * 0.011
while a > b:
    print('A população A deve começar com menos habitantes que a população B')
    a = int(input('Informe a quantidade de habitantes da população A:'))
    taxaA = 80000 * 0.03
    print('Taxa de crescimento da população A = 3%')
    b = int(input('Informe a quantidade de hábitantes da população B:'))
taxaB = 200000 * 0.011

print('Taxa de crescimento da população A = 1,1%')
anos = 0
while a < b:
    a += taxaA
    b += taxaB
    anos += 1
    if a == b or a > b:
        break
print(f'A populção A irá ultrpassar a populção B em {anos} anos!')
