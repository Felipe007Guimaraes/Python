
combustivel = input('Insira A para álcool e G para gasolina: ').upper()

if combustivel == 'A':
    print(f'Promoção Álcool\nAté 20 litros 3% de desconto\nAcima de 20 litros 5% de desconto')

elif combustivel == 'G':
    print(f'Promoção Gasolina\nAté 20 litros 4% de desconto\nAcima de 20 litros 6% de desconto')
litros = float(input('Insira a quantidade a ser abastecida: '))

if litros <= 20 and combustivel == 'A':
    valor = litros*1.90
    desconto = valor * 0.03
    valor -= desconto
    print(f'Valor do litro R$ {litros*1.90:.2f}\nDesconto a ser aplicado: R$ {desconto}\nValor com desconto R$ {valor:.2f}')

elif litros > 20 and combustivel == 'A':
    valor = litros*1.90
    desconto = valor * 0.05
    valor -= desconto
    print(f'Valor do litro R$ {litros*1.90:.2f}\nDesconto a ser aplicado: R$ {desconto}\nValor com desconto R$ {valor:.2f}')

elif litros <= 20 and combustivel == 'G':
    valor = litros*2.50
    desconto = valor * 0.04
    valor -= desconto
    print(f'Valor do litro R$ {litros*2.50:.2f}\nDesconto a ser aplicado: R$ {desconto}\nValor com desconto R$ {valor:.2f}')
elif litros > 20 and combustivel == 'G':
    valor = litros*2.50
    desconto = valor * 0.06
    valor -= desconto
    print(f'Valor do litro R$ {litros*2.50:.2f}\nDesconto a ser aplicado: R$ {desconto}\nValor com desconto R$ {valor:.2f}')
else:
    print('Valor inválido!')

