print('Investigação')
print('Responda com "S" para sim e "N" para não')
sim = 0
nao = 0
primeira = input('Telefonou para a vítima? S ou N\n').upper()
if primeira == 'S':
    sim +=1
elif primeira == 'N':
    nao +=1
segunda = input('Esteve no local do crime? S ou N\n').upper()
if primeira == 'S':
    sim +=1
elif primeira == 'N':
    nao +=1
terceira = input('Mora perto da vítima? S ou N\n').upper()
if primeira == 'S':
    sim +=1
elif primeira == 'N':
    nao +=1
quarta = input('Devia para a vítima? S ou N\n').upper()
if primeira == 'S':
    sim +=1
elif primeira == 'N':
    nao +=1
quinta = input('Já trabalhou com a vítima? S ou N\n').upper()
if sim == 1 or sim == 0:
    print('Liberado(a)')
elif sim == 2:
    print('Suspeita!')
elif sim == 3 or sim == 4:
    print('Cúmplice!')
elif sim == 5:
    print('Assassino(a)')




