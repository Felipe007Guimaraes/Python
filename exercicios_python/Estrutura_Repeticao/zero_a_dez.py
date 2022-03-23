nota = float(input('Informe uma nota entre 0 e 10:\n'))
while nota > 10 or nota < 0:
    print('Informe um valor válido')
    nota = float(input('Informe uma nota entre 0 e 10:\n'))
print(nota)