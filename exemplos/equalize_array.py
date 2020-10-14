#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the equalizeArray function below.
def equalizeArray(arr):
    # analizar o array para encontrar itens repetidos
    # dos itens repetidos ver quais tem maior ocorrencia
    # escolhido o item de maior ocorrencia fazer a contagem necessaria para remover os demais 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

