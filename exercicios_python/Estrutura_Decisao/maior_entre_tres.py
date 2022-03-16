primeiro = float(input('Insira um número: '))
segundo = float(input('Insira um segundo número: '))
terceiro = float(input('Insira um terceiro número: '))
if primeiro > segundo and primeiro > terceiro:
    print(f'O maior é {primeiro}!')
elif segundo > primeiro and segundo > terceiro:
    print(f'O maior é {segundo}!')
else:
    print('O maior é o terceiro!')
