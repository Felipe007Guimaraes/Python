primeiro = float(input("Informe um número: "))
segundo = float(input('Informe um segundo número: '))
terceiro = float(input('Informe um terceiro número: '))
if primeiro <= segundo and primeiro <= terceiro and segundo <= terceiro:
    print(f'O maior é o {terceiro} e o menor é o {primeiro}') 
elif primeiro <= segundo and primeiro <= terceiro and segundo >= terceiro:
    print(f'O maior é o {segundo} e o menor é o {primeiro}') 
elif segundo <= terceiro and segundo <= primeiro and primeiro <= terceiro:
    print(f'O maior é o {terceiro} e o menor é o {segundo}')
elif segundo <= terceiro and segundo <= primeiro and primeiro >= terceiro:
    print(f'O maior é o {primeiro} e o menor é o {segundo}')
elif terceiro <= primeiro and terceiro <= segundo and primeiro <= segundo:
    print(f'O maior é o {segundo} e o menor é o {terceiro}')
elif terceiro <= primeiro and terceiro <= segundo and primeiro >= segundo:
    print(print(f'O maior é o {primeiro} e o menor é o {terceiro}'))