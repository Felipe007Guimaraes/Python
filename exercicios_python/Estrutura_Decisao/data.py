data = input('Informe uma data no formato dd/mm/aaaa\nInforme apenas números: ')
dia = int(data[0:2])
mes = int(data[2:4])
ano = int(data[4:8])
if ((len(data) ==8)  and (dia <= 31) and (mes<=12)and not(data[2:4] == '02' and dia>28)):
    print(f'Data informada: {data[0:2]}/{data[2:4]}/{data[4:8]}')

elif (ano % 4 == 0) and (ano % 100 != 0) or (ano % 400 == 0) and (data[2:4] == '02' and dia>=29):
    print(f'O ano é bissexto portanto fevereiro tem 29 dias!\ndata informada: {data[0:2]}/{data[2:4]}/{data[4:8]}')

else:
    print('Formato Inválido!')
    