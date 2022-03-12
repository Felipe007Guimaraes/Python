"""
Dados cinco inteiros positivos, encontre os valores mínimo e máximo que podem ser calculados somando exatamente quatro dos cinco inteiros. Em seguida, imprima os respectivos valores mínimo e máximo como uma única linha de dois inteiros longos separados por espaço.

Imprimir

Imprima dois inteiros separados por espaço em uma linha: a soma mínima e a soma máxima dedoelementos.

Formato de entrada

Uma única linha de cinco inteiros separados por espaço.

Formato de saída

Imprima dois inteiros longos separados por espaços denotando os respectivos valores mínimo e máximo que podem ser calculados somando exatamente quatro dos cinco inteiros. (A saída pode ser maior que um inteiro de 32 bits.)

"""

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    maior_menor = []
    for i in arr:
        maior_menor.append(sum(arr)-i)
    print(f'{max(maior_menor, key=int)} {min(maior_menor, key=int)}')

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
 