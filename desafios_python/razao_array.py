"""
Dada uma matriz de inteiros, calcule as razões de seus elementos que são positivos , negativos e zero . Imprima o valor decimal de cada fração em uma nova linha comcasas após a vírgula.

Nota: Este desafio apresenta problemas de precisão. Os casos de teste são dimensionados para seis casas decimais, embora respostas com erro absoluto de atésão aceitáveis.

Exemplo

tem elementos, dois positivos, dois negativos e um zero. Suas proporções são,e. Os resultados são impressos como:

0.400000
0.400000
0.200000
Descrição da função

Complete a função plusMinus no editor abaixo.

plusMinus tem os seguintes parâmetros:

int arr[n] : uma matriz de inteiros
Imprimir
Imprime as proporções de valores positivos, negativos e zero na matriz. Cada valor deve ser impresso em uma linha separada comdígitos após o decimal. A função não deve retornar um valor.

Formato de entrada

A primeira linha contém um número inteiro,, o tamanho da matriz.
A segunda linha contém inteiros separados por espaço que descrevem.

Restrições



Formato de saída

Imprima o seguintelinhas, cada uma paradecimais:

proporção de valores positivos
proporção de valores negativos
proporção de zeros
Entrada de amostra

STDIN           Function
-----           --------
6               arr[] size n = 6
-4 3 -9 0 4 1   arr = [-4, 3, -9, 0, 4, 1]
Saída de Amostra

0.500000
0.333333
0.166667
Explicação

temnúmeros positivos,números negativos ezero na matriz.
"""

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    positivo = 0
    negativo = 0
    zero = 0
    for i in arr:
        if i > 0:
            positivo +=1
        if i < 0:
            negativo +=1
        if i ==0:
            zero +=1
    print(f'{positivo/n:.6f}')
    print(f'{negativo/n:.6f}')
    print(f'{zero/n:.6f}')

    # Write your code here

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
