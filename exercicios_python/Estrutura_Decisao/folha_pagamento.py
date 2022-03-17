valor = float(input('Informe quanto recebe por hora: '))
tempo = float(input('Informe quantas horas trabalhou no mês: '))
salario = valor*tempo
inss = salario*0.10
sindicato = salario*0.03
fgts = salario*0.11
porcentagem = 0
print('+     Salário Bruto        :')
print(f'R$        {salario}             ')
print(f' FGTS     (11%)   : R${fgts:.2f}')
print(f'-INSS     (10%)   : R${inss:.2f}')
print(f'-Sindicato (3%)   : R${sindicato:.2f}')
if salario <= 900:
    imposto = 0
    porcentagem = 'Isento'
    print(f'IR        Isento ')
elif salario > 900 and salario <= 1500:
    imposto = salario*0.05
    porcentagem = '5%'
    print(f'-IR        ({porcentagem})   : R${imposto:.2f}')
else:
    imposto = salario*0.20
    porcentagem = '20%'
    print(f'-IR        ({porcentagem})   : R${imposto:.2f}')
descontos = imposto+inss+sindicato
print(f'- Total de descontos  {descontos}')
print('+     Salário liquido      :')
print(f'R$:       {salario-descontos:.2f}')