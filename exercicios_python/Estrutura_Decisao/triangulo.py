primeiro_lado = float(input('Informe o primeiro lado: '))
segundo_lado = float(input('Informe o segundo lado: '))
terceiro_lado = float(input('Informe o terceiro lado: '))
def tipo_triangulo(primeiro_lado, segundo_lado, terceiro_lado):
    if (primeiro_lado == segundo_lado) and (primeiro_lado == terceiro_lado) and (segundo_lado == terceiro_lado):
        return print('Triângulo Equilátero')
    if (primeiro_lado == segundo_lado) or (primeiro_lado == terceiro_lado) or (segundo_lado == terceiro_lado):
        return print('Triângulo Isósceles')
    if (primeiro_lado != segundo_lado) and (primeiro_lado != terceiro_lado) and (segundo_lado != terceiro_lado):
        return print('Triângulo Escaleno')


if (primeiro_lado + segundo_lado) > terceiro_lado:
    tipo_triangulo(primeiro_lado, segundo_lado, terceiro_lado)


elif (primeiro_lado + terceiro_lado) > segundo_lado:
    tipo_triangulo(primeiro_lado, segundo_lado, terceiro_lado)


elif (terceiro_lado + segundo_lado) > primeiro_lado:
    tipo_triangulo(primeiro_lado, segundo_lado, terceiro_lado)

else:
    print('Não é um triângulo!')