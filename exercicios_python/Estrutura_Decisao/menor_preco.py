preco1 = float(input('Informe o primeiro preço para comparação:'))
preco2 = float(input('Informe outro preço: '))
print(f'Produto 1 = {preco1:.2f} \n Produto 2 = {preco2:.2f}')
if preco1 < preco2:
    print('Compre o primeiro produto, pois está com menor valor!')
else:
    print('Compre o segundo produto, pois está com menor valor!')
