n = input('Digite algo:')
print(f'{n} pode ser alfanumérico? {n.isalnum()}')
print(f'{n} pode ser alfabético? {n.isalpha()}')
print(f'{n} pode ser ASCII? {n.isascii()}')
print(f'{n} pode ser descimal? {n.isdecimal()}')
print(f'{n} contém apenas numeros? {n.isdigit()} ')
print(f'{n} pode ser uma variavel? {n.isidentifier()}')
print(f'{n} contém apenas mínuscula? {n.islower()}')
print(f'{n} é numérico? {n.isnumeric()}')
print(f'{n} é imprimivel ou está vazio? {n.isprintable()}')
print(f'{n} é espaço? {n.isspace()}')
print(f'{n} apenas o primeiro caracter é maiúscula? {n.istitle()}')
print(f'{n} contém apenas maiúsculas? {n.isupper()}')
print(f'Estes são todos os tipos primitivos que {n} pode assumir!')