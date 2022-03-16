vogais = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U',]
letra = input('Informe a letra a ser conferida: ')
if letra in vogais:
    print('É vogal!')
else:
    print('É consoante!')
