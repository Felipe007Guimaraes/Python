salario = float(input('Informe o salário antes do reajuste: '))
print(f'Salário sem ajuste: {salario}')
if salario < 280:
    aumento = salario*0.20
    salario += aumento
    print(f'Aumento de 20%\nValor do aumento: {aumento:.2f}\nSalário atual: R${salario:.2f} ')
elif salario >= 280 and salario < 700:
    aumento = salario*0.15
    salario += aumento
    print(f'Aumento de 15%\nValor do aumento: {aumento:.2f}\nSalário atual: R${salario:.2f} ')
elif salario >= 700 and salario < 1500:
    aumento = salario*0.10
    salario += aumento
    print(f'Aumento de 10%\nValor do aumento: {aumento:.2f}\nSalário atual: R${salario:.2f} ') 
elif salario > 1500:
    aumento = salario*0.05
    salario += aumento
    print(f'Aumento de 5%\nValor do aumento: {aumento:.2f}\nSalário atual: R${salario:.2f} ')
    