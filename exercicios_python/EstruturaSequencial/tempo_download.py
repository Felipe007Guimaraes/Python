mb = float(input('Informe o tamanho e MB do arquivo: '))
mbps = float(input('Informe agora a velocidade do link em mbps: '))
tempo = mb/mbps
print(f'O tempo do download será de {tempo} segundos!')