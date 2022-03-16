primeiro = float(input("Informe um número: "))
segundo = float(input('Informe um segundo número: '))
terceiro = float(input('Informe um terceiro número: '))
if primeiro <= segundo and primeiro <= terceiro and segundo <= terceiro:
    print(primeiro, segundo, terceiro) 
elif primeiro <= segundo and primeiro <= terceiro and segundo >= terceiro:
    print(primeiro, terceiro, segundo) 
elif segundo <= terceiro and segundo <= primeiro and primeiro <= terceiro:
    print(segundo, primeiro, terceiro)
elif segundo <= terceiro and segundo <= primeiro and primeiro >= terceiro:
    print(segundo, terceiro, primeiro)
elif terceiro <= primeiro and terceiro <= segundo and primeiro <= segundo:
    print(terceiro, primeiro, segundo)
elif terceiro <= primeiro and terceiro <= segundo and primeiro >= segundo:
    print(terceiro, segundo, primeiro)
