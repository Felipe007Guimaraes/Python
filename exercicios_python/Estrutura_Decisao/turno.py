turno = input('M- Matutino  /  V- Vespertino  /  N- Noturno\nInforme o turno em que estuda: ')
if turno == 'M' or turno == 'm':
    print('Bom dia!')
elif turno == 'V' or turno == 'v':
    print('Boa tarde!')
elif turno == 'N' or turno == 'n':
    print('Boa noite!')
else:
    print("Valor Inválido!")