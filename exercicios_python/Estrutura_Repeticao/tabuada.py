tabuada = input('Informe a tabuada a ser exibida:\n')
try:
    tabuada.isdigit()
except:
    ValueError('Valor inválido!')
for i in range(1, 10+1):
    print(f'{tabuada} X {i} = {int(tabuada)*int(i)}')