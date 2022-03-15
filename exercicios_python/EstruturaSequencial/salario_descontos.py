valor = float(input('Informe quanto recebe por hora: '))
tempo = float(input('Informe quantas horas trabalhou no mês: '))
salario = valor*tempo
imposto = salario*0.11
inss = salario*0.08
sindicato = salario*0.05
print('+       Salário         :')
print('R$                       ')
print(f'IR      (11%)   : R${imposto:.2f}')
print(f'INSS     (8%)   : R${inss:.2f}')
print(f'Sindicato(5%)   : R${sindicato:.2f}')
print('R$                       ')
print('+    Salário liquido    :')
print(f'R$:       {salario-(imposto+inss+sindicato):.2f}')

