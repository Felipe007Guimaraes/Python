def pagar(valor):
    pagamento = input('Digite a forma de pagamento: Dinheiro ou Cartão\n').upper()
    if pagamento == 'DINHEIRO':
        desconto = 0
        return desconto
    elif pagamento == 'CARTÃO':
        desconto = valor * 0.05
        desconto = valor - desconto
        return desconto
tipo = input('Tipos de carnes:\n(Filé duplo)   (Alcatra)  (Picanha)\nInforme o tipo de carne a ser comprada:\n ').upper()
quantidade = float(input('Quantos quilos precisa?\n'))
if tipo == 'FILÉ DUPLO' and quantidade <= 5:
    valor = 4.90
elif tipo == 'FILÉ DUPLO' and quantidade > 5:
    valor = 5.80
elif tipo == 'ALCATRA' and quantidade <= 5:
    tipo = 'ALCATRA---'
    valor = 5.90
elif tipo == 'ALCATRA' and quantidade > 5:
    tipo = 'ALCATRA---'
    valor = 6.90
elif tipo == 'PICANHA' and quantidade <= 5:
    tipo = 'PICANHA---'
    valor = 6.90 
elif tipo == 'PICANHA' and quantidade > 5:
    tipo = 'PICANHA---'
    valor = 7.80
else:
    print('Entrada Inválida!')


valor *= quantidade
descontos = pagar(valor)
print(' _________________________________________________')
print('|------------------CUPOM FISCAL-------------------')
print(f'|Produto: {tipo}({quantidade})Kg----------------------')
print(f'|Valor : {valor:.2f}-----------Total de descontos:R${valor-descontos:.2f}')
print(f'|---------------------------------SUBTOTAL R${descontos:.2f}')
print(f'|_________________________________________________')


