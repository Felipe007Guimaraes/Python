macakg = float(input('Insira a quantidade a ser adquirida de maçãs: '))
valor1 = 1.80

morangokg = float(input('Insira a quantidade a ser adquirida de morangos: '))
valor2 = 2.50

if macakg > 5:
    valor1 = 1.50

elif morangokg > 5:
    valor2 = 2.20

valor_macas = macakg * valor1
valor_morangos= morangokg * valor2
kg = macakg + morangokg
valor_total = valor_morangos + valor_macas

if kg > 8 or valor_total> 25:
    desconto = valor_total*0.10
    valor_total -= desconto
    print(f'O valor a ser pago pela compra será de R$ {valor_total:.2f}')
else:
    print(f'O valor a ser pago pela compra será de R$ {valor_total:.2f}')
