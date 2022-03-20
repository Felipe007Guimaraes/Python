saque = int(input('Notas Disponiveis\n1, 5, 10, 50, 100\nValor mínimo para saque: 10\nValor máximo para saque: 600\nInsira o valor para saque: '))
if saque >600 or saque < 10:
    print('Insira um valor valido para saque!\nSaque máximo 600 \nSaque minimo 10')
notas100=0
notas50=0
notas10=0
notas5=0
notas1=0
if saque >=100:
    notas100=saque//100
    saque -=notas100*100
    print(f'{notas100} notas de 100')
if saque>=50:
    notas50 = saque//50
    saque -=notas50*50
    print(f'{notas50} notas de 50')
if saque >=10:
    notas10 = saque//10
    saque -= notas10*10
    print(f'{notas10} notas de 10')
if saque >=5:
    notas5=saque//5
    saque -=notas5*5
    print(f'{notas5} notas de 5')
if saque >=1:
    notas1=saque//1
    saque -=notas1*1
    print(f'{notas1} notas de 1')

