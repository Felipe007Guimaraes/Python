comeco = input('Informe um número que corresponda ao começo do intervalo:\n')
try:
    comeco.isdigit()
except:
    ValueError('Valor inválido!')
fim = input('Informe um número que corresponda ao fim do intervalo:\n')
try:
    fim.isdigit()
except:
    ValueError('Valor inválido!')

lista = []
for i in range(int(comeco), int(fim)+1):
    lista.append(i)
print(lista)
