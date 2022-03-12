print('Informe a nota dos quatro bimestres do aluno para a média:')
primeiro_bi = float(input(f'Informe a nota do primeiro bimestre: '))
segundo_bi = float(input(f'Informe a nota do segundo bimestre: '))
terceiro_bi = float(input(f'Informe a nota do terceiro bimestre: '))
quarto_bi = float(input(f'Informe a nota do quarto bimestre: '))
media = (primeiro_bi + segundo_bi + terceiro_bi + quarto_bi)/4
print(f'A média do aluno é {media:.1f}')