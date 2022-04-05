'''Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento 
de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.1%. Faça um programa
 que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a 
 população do país B, mantidas as taxas de crescimento.'''
print('Iniciando')
a = 80000
taxaA = 80000 * 0.03
b = 200000
taxaB = 200000 * 0.011
anos = 0
while a < b:
    a += taxaA
    b += taxaB
    anos += 1
    print(a, b, anos)
    if a == b or a > b:
        break
print(anos)
